# -*- coding: utf-8 -*-

import os

# pip install boto3 psutil requests
# based on https://gist.github.com/ipmb/c45d44589b37272de354820069de93fb#file-cloudwatch_sysstats-py
import boto3
import psutil
import requests

NAMESPACE = 'onPrem'
INSTANCE_NAME = 'blabla.bcosmin.net'
INSTANCE_TYPE = 'non-ec2'
os.environ.setdefault('AWS_DEFAULT_REGION', 'eu-central-1')


def extract_metric_tuple(metric, prefix, unit, dimensions=None):
    metrics = []
    for k, v in metric._asdict().items():
        name = ''.join([prefix, k.capitalize()])
        data = dict(name=name, value=v, dimensions=dimensions)
        if k == 'percent':
            data['unit'] = 'Percent'
        elif k.endswith('_time'):
            data['unit'] = 'Milliseconds'
        elif k.endswith('_sent') or k.endswith('_recv'):
            data['unit'] = 'Bytes'
        else:
            data['unit'] = unit
        metrics.append(data)
    return metrics


def collect_metrics():

    total_cpu = psutil.cpu_percent(interval=1)
    cpu_cores = psutil.cpu_count()
    if not hasattr(psutil, "sensors_temperatures"):
        print("platform not supported for temp sensors")
        cpu_temp = 0.0
    else:
        cpu_temp = psutil.sensors_temperatures(fahrenheit=False)["coretemp"][0][1]
    total_mem = float(psutil.virtual_memory().total)
    total_mem = float("{0:.2f}".format((total_mem/1024)/1024))
    used_mem = psutil.virtual_memory().percent
    free_mem = float(psutil.virtual_memory().available)
    free_mem = float("{0:.2f}".format((free_mem/1024)/1024))
    swap_total = float(psutil.swap_memory().total)
    swap_total = float("{0:.2f}".format((swap_total/1024)/1024))
    swap_free = float(psutil.swap_memory().free)
    swap_free = float("{0:.2f}".format((swap_free/1024)/1024))
    disk_total_root = float(psutil.disk_usage('/').total)
    disk_total_root = float("{0:.2f}".format((disk_total_root/1024)/1024))
    disk_usage_root = psutil.disk_usage('/').percent
    net_kbytes_recieved = float(psutil.net_io_counters().bytes_recv)
    net_kbytes_recieved = float("{0:.2f}".format(net_kbytes_recieved/1024))
    net_kbytes_sent = float(psutil.net_io_counters().bytes_sent)
    net_kbytes_sent = float("{0:.2f}".format(net_kbytes_sent/1024))

    metrics = [
        dict(name='Users', value=len(psutil.users()), unit='Count'),
        dict(name='Processes', value=len(psutil.pids()), unit='Count'),
        dict(name='CPULoad', value=total_cpu, unit='Percent'),
        dict(name='CPUCoresCount', value=cpu_cores, unit='Count'),
        dict(name='CPUTemp', value=cpu_temp, unit='Count'),
        dict(name='TotalMem', value=total_mem, unit='Megabytes'),
        dict(name='UsedMem', value=used_mem, unit='Percent'),
        dict(name='FreeMem', value=free_mem, unit='Megabytes'),
        dict(name='TotalSwap', value=swap_total, unit='Megabytes'),
        dict(name='FreeSwap', value=swap_free, unit='Megabytes'),
        dict(name='RootVolSize', value=disk_total_root, unit='Megabytes'),
        dict(name='RootVolUsage', value=disk_usage_root, unit='Percent'),
        dict(name='NetKBRecieved', value=net_kbytes_recieved, unit='Kilobytes'),
        dict(name='NetKBSent', value=net_kbytes_sent, unit='Kilobytes'),
    ]
    return metrics


def chunks(l, n):
    """Yield successive n-sized chunks from l."""
    for i in xrange(0, len(l), n):
        yield l[i:i + n]


def send_metrics(metrics):
    cloudwatch = boto3.client('cloudwatch')
    dimensions = [
        {'Name': 'InstanceId', 'Value': INSTANCE_NAME},
        {'Name': 'InstanceType', 'Value': INSTANCE_TYPE},
    ]
    metric_payload = []
    for metric in metrics:
        metric_data = {'MetricName': metric['name'],
                       'Value': metric['value'],
                       'Dimensions': list(dimensions),
                       'Unit': metric['unit']}
        if metric.get('dimensions'):
            for k, v in metric['dimensions'].items():
                metric_data['Dimensions'].append({'Name': k, 'Value': v})
        metric_payload.append(metric_data)

    # You may send not more, than 20 metrics at a time
    for batch in list(chunks(metric_payload, 20)):
        cloudwatch.put_metric_data(Namespace=NAMESPACE, MetricData=batch)


def main():
    metrics = collect_metrics()
    send_metrics(metrics)


if __name__ == '__main__':
    main()
