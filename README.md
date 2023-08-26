</head>
<body>
  <div class="container">
    <h1>Steganography with AWS SaaS</h1>
    <p>This repository demonstrates the implementation of steganography for file encryption, coupled with secure storage on AWS Cloud as a SaaS solution.</p>
    <h2>Features</h2>
    <ul>
      <li>Advanced steganography techniques for concealed data encryption.</li>
      <li>Secure storage of encrypted files on AWS Cloud's SaaS platform.</li>
      <li>Enhanced privacy and accessibility for encrypted data.</li>
    </ul>
    <h2>Usage</h2>
    <p>To encrypt a file and store it on AWS SaaS:</p>
    <code>
      git clone https://github.com/Dharmarajrathod/stepnography-aws.git<br>
      cd your-repo<br>
      # Follow the instructions to encrypt and upload files.<br>
      <p># Dependencies

Before you begin playing with the source code you might need to install deps just as shown below;

`pip3 install -r requirement.txt`

# Setting up AWS S3

For setting up AWS S3 for uploading and featching files from the bucket you first need to setup your AWS account and create a bucket.
To do so, you can follow the following documentation of [AWS S3](https://docs.aws.amazon.com/AmazonS3/latest/userguide/creating-bucket.html).

You probably want to setup IAM users and give the access either though a bucket policy or on the user level. With bucket policies you can easily define what paths users are able to edit and access. When you create an IAM user you also have the option of creating one for Programmatic(CLI) access only which will give you a set of credentials for that user only. Just use aws configure and set the access and token key.

You also probably want to make sure you are using an IAM user yourself as it's generally recommended for security.

To do so, you can go here [AWS Access Key](https://console.aws.amazon.com/iam/home#/security_credentials$access_key) and under the Access keys (access key ID and secret access key) section click on 'Create New Access Key'. And don't forget to note down the AWS Secret Access Key because it is kinda one time thing and if you lose or forget your secret key, you cannot retrieve it. Instead, you have to create a new access key and make the old key inactive.

After noting down the credentials, open the windows cmd and type

`aws configure`

Enter the AWS Access Key ID and AWS Secret Access Key. Now you are good to go!

# Setting up Mailtrap account

The decryption phase of this process involves the use of your Mailtrap account.
You need to sign up for [Mailtrap account.](https://mailtrap.io) After signing up you just need to keep the Mailtrap username and Mailtrap password handy to use their API.

Now, naviagate to **Colossus/generate_config.py** and edit the required parameters. You can find the smtp login details [here,](https://mailtrap.io/inboxes) under the **SMPT settings** option. 
After editing, run this python script, it will generate a **configurations.ini** in the same directory which will be used to easily configure the software for you.

 `python generate_config.py`
 
# Running the App
In order to run the app on your device run this command,

`python main.py -h`

# Hybrid Cryptography

Hybrid encryption is a mode of encryption that merges two or more encryption systems. It incorporates a combination of asymmetric and symmetric encryption to benefit from the strengths of each form of encryption. These strengths are respectively defined as speed and security.

Hybrid encryption is considered a highly secure type of encryption as long as the public and private keys are fully secure.

A hybrid encryption scheme is one that blends the convenience of an asymmetric encryption scheme with the effectiveness of a symmetric encryption scheme.

Hybrid encryption is achieved through data transfer using unique session keys along with symmetrical encryption. Public key encryption is implemented for random symmetric key encryption. The recipient then uses the public key encryption method to decrypt the symmetric key. Once the symmetric key is recovered, it is then used to decrypt the message.

The combination of encryption methods has various advantages. One is that a connection channel is established between two users' sets of equipment. Users then have the ability to communicate through hybrid encryption. Asymmetric encryption can slow down the encryption process, but with the simultaneous use of symmetric encryption, both forms of encryption are enhanced. The result is the added security of the transmittal process along with overall improved system performance.


The idea of hybrid encryption is quite simple. Instead of using AES to encrypt the text, we use AES to encrypt the message. Then, they maintain the secrecy of the key, and we encrypt the key using RSA. The steps of hybrid encryption are:


    1. Generate a symmetric key. The symmetric key needs to be kept a secret.
    2. Encrypt the data using the secret symmetric key.
    3. The person to whom we wish to send a message will share her public key and keep the private key a secret.
    4. Encrypt the symmetric key using the public key of the receiver.
    5. Send the encrypted symmetric key to the receiver.
    6. Send the encrypted message text.
    7. The receiver decrypts the encrypted symmetric key using her private key and gets the symmetric key needed for decryption.
    8. The receiver uses the decrypted symmetric key to decrypt the message, getting the original message.


# Why to use Python for Cryptography?

Python makes implementing certain types of algorithms easy without being insanely slow, namely those that use a few simple operations on BigIntegers (RSA, DH, etc).
Symmetric algorithms such as AES or SHA256 implemented in Python will be slow.
For writing simple programs to cryptanalyze classic ciphers, Python is a pretty solid choice - normally they are weak enough to not require huge amounts of CPU time to crack.  Python has a relative small quantity of lines of code, which makes it less prone to issues, easier to debug, and more maintainable.
</p>
    </code>
    <h2>Contributing</h2>
    <p>Contributions are welcome! Fork the repo and create a pull request with your enhancements.</p>
    <h2>License</h2>
    <p>This project is licensed under the MIT License - see the <a href="LICENSE">LICENSE</a> file for details.</p>
  </div>
</body>
</html>
