# InstanceDetails
Lambda function that fetches details of instances per region.

# Table of contents

1. Purporse
2. Prerequisites
3. Getting started
4. Application strcuture
5. Logic



# Purporse
This application exposes a API to fetch details of instances per region through API gateway and lambda function

# Prerequisites

python
awscli
pytest


# Getting started
git clone https://gitlab.com/Nithwan/instancedetails.git
pip install -r requirements.txt  # To install project dependencies

# Application strcuture

|-- src
    |-- handler
|-- test
    |-- test.py
|-- requirement.txt

# Logic

1. User request reaches is Authenticated
2. Upon successful authentication, Each region is selected
3. In each region, Instances Ids are fetched if present.
4. As a reslut, Instance details from all the regoins is returned to the user.
