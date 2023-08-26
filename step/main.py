import getopt
import sys
import os
import boto3

import decrypt
import hybrid
import uploadS3


def main():
    ccproject4 = None
    object_name = None
    src = None
    file_type = None

    try:
        opts, args = getopt.getopt(sys.argv[1:], "b:o:i:t:h:")
    except getopt.GetoptError:
        print("Usage: python main.py -t upload -b <bucket_name> -o <object_name> -i <input_file>")
        print("Usage: python main.py -t download -b <bucket_name> -o <object_name> -i <output_file>")
        print("Usage: python main.py -t decrypt -i <input_file>")
        sys.exit(2)

    for opt, arg in opts:
        if opt == '-h':
            print("Usage: python main.py -t upload -b <bucket_name> -o <object_name> -i <input_file>")
            print("Usage: python main.py -t download -b <bucket_name> -o <object_name> -i <output_file>")
            print("Usage: python main.py -t decrypt -i <input_file>")
            sys.exit()
        elif opt == '-t':
            file_type = arg
        elif opt == '-b':
            ccproject4 = arg
        elif opt == '-o':
            object_name = arg
        elif opt == '-i':
            src = arg

    if file_type == "upload":
        hybrid.mainMenu()
        uploadS3.upload_file(src, ccproject4, object_name)
        print("Uploaded successfully!")
    elif file_type == "download":
        if not os.path.exists(os.path.dirname(src)):
            os.makedirs(os.path.dirname(src))
        s3 = boto3.client('s3')
        s3.download_file(ccproject4, object_name, src)
        print("Downloaded successfully!")
    elif file_type == "decrypt":
        decrypt.main(src)


if __name__ == '__main__':
    main()
    