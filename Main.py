print("Hello World!")
#import boto3
#s3 = boto3.resource('s3')
#bucket = "nadi-test-s3"
#key = "Test File.txt"
#localFilename = "Test File.txt"
#try:
#    s3.meta.client.download_file(bucket, key, localFilename)
#except Exception as e:
#    print (e)
#    print('Error getting object {} from bucket {}. Make sure they exist and your bucket is in the same region as this function.'.format(key, bucket))
#    raise e
#print("First file was downloaded successfully!")

#bucket = "nadi-test-s3"
#key = "folder1/Hello.txt"
#localFilename = "Hello.txt"
#try:
#    s3.meta.client.download_file(bucket, key, localFilename)
#except Exception as e:
#    print (e)
#    print('Error getting object {} from bucket {}. Make sure they exist and your bucket is in the same region as this function.'.format(key, bucket))
#    raise e
#print("Second file was downloaded successfully!")

from flask import Flask
app= Flask(__name__)

@app.route("/")
def hello():
		return "Hello World!"

@app.route("/download-files_sample", methods=['GET','POST'])
def download_files():
	import boto3
	s3 = boto3.resource('s3')
	bucket = "nadi-test-s3"
	key = "Test File.txt"
	localFilename = "Test File.txt"
	try:
		s3.meta.client.download_file(bucket, key, localFilename)
	except Exception as e:
		print (e)
		print('Error getting object {} from bucket {}. Make sure they exist and your bucket is in the same region as this function.'.format(key, bucket))
		raise e
	return "The required file was downloaded successfully!"

@app.route("/download-file/<name>", methods=['GET','POST'])
def download_file(name):
	import boto3
	s3 = boto3.resource('s3')
	bucket = "nadi-test-s3"
	key = (name)
	localFilename = key
	try:
		s3.meta.client.download_file(bucket, key, localFilename)
	except Exception as e:
		print (e)
		print('Error getting object {} from bucket {}. Make sure they exist and your bucket is in the same region as this function.'.format(key, bucket))
		raise e
	return "The required file {} was downloaded successfully from bucket {}.!".format(key, bucket)

@app.route('/hi/<name>')
def say_hi(name):
    return 'Hello, %s!' % (name)

if __name__ == '__main__':
	app.run(debug=True)