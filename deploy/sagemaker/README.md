# Deploying the model on SageMaker

The first step is to build a docker image that runs a [Flask server](https://github.com/cw75/torchMojiBot/blob/master/sagemaker/emojibot-sagemaker.py) that responds to SageMaker's health check (ping) requests and serves prediction by running the torchMoji model.

Before building the image, you need two files for model initialization: `vocabulary.json` for sentence tokenization and `pytorch_model.bin` that stores pre-trained model weights.
`vocabulary.json` is already in `model/vocabulary.json`. To download `pytorch_model.bin`, simply run `python3 scripts/download_weights.py` (note that you need to install `wget` to execute the script). The weights will be downloaded to `model/pytorch_model.bin`.

Then, build a docker image and push it to AWS ECR:
1. Go to AWS [ECR console](https://console.aws.amazon.com/ecr) and create a new repository.
2. Click the repository name and click `View push commands` to see necessary steps for [authentication](https://docs.aws.amazon.com/AmazonECR/latest/userguide/Registries.html#registry_auth). You only need to perform step 1 in `View push commands`.
3. Return to this repo and run `docker build . -f emojibot-sagemaker.dockerfile -t <Your ECR URI>` to build the docker image.
4. Run `docker push <Your ECR URI>` to push the docker image to ECR.

Next, create a SageMaker model:
1. Click the `Models` tab on the [SageMaker console](https://console.aws.amazon.com/sagemaker/) and click `Create model`.
2. Create a name for the model and assign an [IAM role](https://console.aws.amazon.com/iam/home?ad=c&cp=bn&p=iam#/roles). If you don't have one, click `Create a new role` from the drop-down list and click `Create role`. This will create a role that has the `AmazonSageMakerFullAccess` IAM policy attached, which is sufficient for our purpose.
3. In container definition, choose `Provide model artifacts and inference image location` and paste the ECR URI into `Location of inference code image`.
4. Click `Create model`.

Then, create an endpoint configuration:
1. Click the `Endpoint configurations` tab and click `Create endpoint configuration`.
2. Create a name for the endpoint configuration.
3. Click `Add model` and select the model you just created.
4. Click `Create endpoint configuration`.

Finally, create a SageMaker endpoint:
1. Click the `Endpoints` tab and click `Create endpoint`.
2. Create a name for the endpoint.
3. Select `Use an existing endpoint configuration` and choose the endpoint configuration that you just created.
4. Click `Create endpoint`.

Now that you've deployed the model, the next step is to deploy the AWS Lambda function that performs request authentication and routes traffic between Slack and SageMaker. Proceed to [here](https://github.com/cw75/torchMojiBot/tree/master/lambda).
