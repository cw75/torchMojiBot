# Authentication and message routing with AWS Lambda

This directory contains the code for the [AWS Lambda](https://aws.amazon.com/lambda/) function that:
1. Accepts and responds to the [URL verification](https://api.slack.com/events/url_verification) request from Slack.
2. Authenticates the Slack subscription message, extracts the text and sends it to the prediction service (SageMaker or Algorithmia).
3. Receives the prediction response (emoji) and uses the Slack web client to post the emoji reaction to Slack workspace.

The `package` folder contains all the Python dependencies required by `lambda_function.py`.

Before uploading to AWS Lambda, you need to replace the credential placeholders in `lambda_function.py` with yours.

Regardless of which platform you used to deploy the model, you need to provide your Slackbot user's OAuth access token and Slack app's signing secret (lines 12 and 14 of `sagemaker/lambda_function.py` or `algorithmia/lambda_function.py`). They can be found by clicking the Slack app name in your [app directory](https://api.slack.com/apps). The OAuth access token can be found under the `OAuth & Permissions` tab and the signing secret can be found under the `Basic Information` tab.

If you deployed the model on SageMaker, in `sagemaker/lambda_function.py`, replace the `EndpointName` on line 44 with your SageMaker endpoint name.

If you deployed the model on Algorithmia, in `algorithmia/lambda_function.py`, provide your Algorithmia API key on line 17 and path (in the form of `username/modelname/version`) to your deployed model on line 19.

Run `cd package && zip -r9 ${OLDPWD}/function.zip . && cd ${OLDPWD}`.

If you deployed the model on SageMaker, run `cd sagemaker && zip -g ${OLDPWD}/function.zip lambda_function.py && cd ${OLDPWD}`.

If you deployed the model on Algorithmia, run `cd algorithmia && zip -g ${OLDPWD}/function.zip lambda_function.py && cd ${OLDPWD}`.

For SageMaker deployment, before creating the Lambda function, you need to create an IAM policy that allows the function to invoke SageMaker endpoints.
1. Go to the IAM [policy](https://console.aws.amazon.com/iam/home?ad=c&cp=bn&p=iam#/policies) and click `Create policy`.
2. Open the `JSON` tab and paste the following:
```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "VisualEditor0",
            "Effect": "Allow",
            "Action": "sagemaker:InvokeEndpoint",
            "Resource": "*"
        }
    ]
}
```
3. Click `Review policy`, give it a name, and click `Create policy`.

Now you are ready to create and upload the Lambda function. On the AWS Lambda [console](https://console.aws.amazon.com/lambda/),
1. Click `Create function`.
2. Name the function (e.g., "emojize").
3. Select Python3.6 as Runtime.
4. Click `Choose or create an execution role` and select `Create a new role with basic Lambda permissions`.
5. Click `Create function`.

If you deployed the model on SageMaker, attach the IAM policy you just created to the execution role.
1. Go to the IAM [role](https://console.aws.amazon.com/iam/home?ad=c&cp=bn&p=iam#/roles) and search for the execution role.
2. Click `Attach policies` and search for the IAM policy.
3. Click `Attach policy`.

Finally, upload the zip file to AWS Lambda by running  
`aws lambda update-function-code --function-name emojize --zip-file fileb://function.zip`

Now that you've deployed the Lambda function, the next step is to set up the API gateway that routes traffic to the Lambda function and exposes a REST endpoint to Slack. Instruction [here](https://github.com/cw75/torchMojiBot/tree/master/api-gateway).
