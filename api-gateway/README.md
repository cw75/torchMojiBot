# Setting up the API Gateway

1. Go to the API Gateway [console](https://console.aws.amazon.com/apigateway)---if you have existing APIs created, click `Create API`.
2. Click `Build` under REST API (non-private), select `New API`, enter a name, choose `Regional` as the Endpoint Type and click `Create API`.
3. From the `Actions` drop-down menu, click `Create Resource`, enter "events" as the resource name, and click `Create Resource`.
4. Click `/events` in the `Resources` directory, and from the `Actions` drop-down list, click `Create Method`.
5. Select `POST` from the drop-down list and check the box.
6. **Important**: check `Use Lambda Proxy integration`. This tells API Gateway to preserve each request's HTTP headers. The Lambda function needs the information in the header to perform Slack's authentication.
7. Choose `Lambda Function` as the integration type and specify the region and the name (e.g., "emojize") of your Lambda function.
8. Click `Save` and `OK`.
9. From the `Actions` drop-down menu, click `Deploy API`. Select `New Stage` and name the stage (e.g., "slack"). Then click `Deploy`.
10. Append `/events` to the `Invoke URL`. It should look something like https://unique-id.amazonaws.com/slack/events. Paste it to the Slackbot event subscription page.

You're almost there! The last step is to finish setting up the Slackbot by completing step 6 [here](https://github.com/cw75/torchMojiBot/tree/master/slack).
