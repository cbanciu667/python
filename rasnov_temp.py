# -*- coding: utf-8 -*-

import os
import boto3
import psutil
import requests
from weather import Weather, Unit
# pip install boto3 psutil requests weather-api
# based on https://gist.github.com/ipmb/c45d44589b37272de354820069de93fb#file-cloudwatch_sysstats-py


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

    weather = Weather(unit=Unit.CELSIUS)
    lookup = weather.lookup_by_latlng(45.35,25.27)
    condition = lookup.condition

    metrics = [
        dict(name='RasnovTemp', value=float("{0:.2f}".format(float(condition.temp))), unit='Count'),
    ]
    return metrics


def chunks(l, n):
    """Yield successive n-sized chunks from l."""
    for i in xrange(0, len(l), n):
        yield l[i:i + n]


def send_metrics(metrics):
    cloudwatch = boto3.client('cloudwatch')
    dimensions = [
        {'Name': 'OutsideTemp', 'Value': 'Rasnov'},
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
        cloudwatch.put_metric_data(Namespace='RasnovTemp', MetricData=batch)


def main():
    metrics = collect_metrics()
    send_metrics(metrics)


if __name__ == '__main__':
    main()
