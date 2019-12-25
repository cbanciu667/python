import boto3
 
s3 = boto3.resource('s3')
bucket = s3.Bucket('bcosmin-videos')
for object in bucket.objects.all():
    #folder, filename = object.key.split("/")
    #only look in backup01 folder
    #if folder == "filme":    
    object = s3.Object(object.bucket_name, object.key)
    #if it's in Glacier
    if object.storage_class == "GLACIER":
        #and not currently being restored:
        if object.restore is None:
            print("Requesting restore for --> "+object.key) 
            object.restore_object(RestoreRequest={'Days': 30}) 
        #list ones currently queued for restore
        elif 'ongoing-request="true"' in object.restore:
            print("Already in restore queue --> "+ object.key)
        #list ones already restored
        elif 'ongoing-request="false"' in object.restore:
            print("Already restored --> "+object.key)