# eks-cdk-spot
EKS built using CDK and leveraging Spot Workers for cost optimisation

## How to start
```
cdk bootstrap aws://$(aws sts get-caller-identity | jq -r .Account)/eu-west-1
# cd into non-empty directory
cdk init app --language python
```

### Useful commands
```
 * `cdk ls`          list all stacks in the app
 * `cdk synth`       emits the synthesized CloudFormation template
 * `cdk deploy`      deploy this stack to your default AWS account/region
 * `cdk diff`        compare deployed stack with current state
 * `cdk docs`        open CDK documentation
```

## Managing AWS Construct Library modules
```
python -m pip install aws-cdk.aws-s3 aws-cdk.aws-lambda
```

## Upgrading dependencies
```
pip install --upgrade -r requirements.txt
```

## Docs
[cdk cli docs](https://docs.aws.amazon.com/cdk/latest/guide/cli.html) or type `cdk docs` 

## Troubleshooting
If `cdk init app --language python` was unsuccesful because of venv try to install `sudo apt install python3-venv` and check instructions [here](eks/README.md) to follow setup again.

