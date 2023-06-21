secrets-security-testing.config.js
#Create function app 
resource "azurerm_windows_function_app " az_afa" { 
    
Name = "az-afa-1"
resource_group_name = var.resource_group_name
location = var.resource_group_location

storage_account_name = var.storage_account_name
storage_account_access_key = "zdf3434aUGgsd355333==23432safJAKFKAFf/FSF(SFSAFJSA)SF===F" 
service_plan_id = azure_service_plan.az_asp.id
azure_storage_account_key  = "zdf3434aUGgsd355333==23432safJAKFKAFf/FSF(SFSAFJSA)SF===F" 
azure_sql_connection_string  = "zdf3434aUGgsd355333==23432safJAKFKAFf/FSF(SFSAFJSA)SF===F" 
azure_management_certificate  = "zdf3434aUGgsd355333==23432safJAKFKAFf/FSF(SFSAFJSA)SF===F" 
azure_search_query_key = "zdf3434aUGgsd355333==23432safJAKFKAFf/FSF(SFSAFJSA)SF===F" 
azure_search_admin_key = "zdf3434aUGgsd355333==23432safJAKFKAFf/FSF(SFSAFJSA)SF===F" 
azure_sas_token  = "zdf3434aUGgsd355333==23432safJAKFKAFf/FSF(SFSAFJSA)SF===F" 
azure_ml_web_service_classic_identifiable_key  = "zdf3434aUGgsd355333==23432safJAKFKAFf/FSF(SFSAFJSA)SF===F" 
azure_function_key  = "zdf3434aUGgsd355333==23432safJAKFKAFf/FSF(SFSAFJSA)SF===F" 
azure_devops_personal_access_token  = "zdf3434aUGgsd355333==23432safJAKFKAFf/FSF(SFSAFJSA)SF===F" 
azure_cosmosdb_key_identifiable  = "zdf3434aUGgsd355333==23432safJAKFKAFf/FSF(SFSAFJSA)SF===F" 
azure_cache_for_redis_access_key  = "zdf3434aUGgsd355333==23432safJAKFKAFf/FSF(SFSAFJSA)SF===F" 
azure_batch_key_identifiable  = "zdf3434aUGgsd355333==23432safJAKFKAFf/FSF(SFSAFJSA)SF===F" 

}
    
"encryptionContext": {
    "SecretARN": "arn:aws-cn:secretsmanager:us-west-2:111122223333:secret:test-secret-a1b2c3",
    "SecretVersionId": "EXAMPLE1-90ab-cdef-fedc-ba987SECRET1"
}

{
    "eventVersion": "1.05",
    "userIdentity": {
        "type": "IAMUser",
        "principalId": "AROAIGDTESTANDEXAMPLE:user01",
        "arn": "arn:aws-cn:sts::111122223333:assumed-role/Admin/user01",
        "accountId": "111122223333",
        "accessKeyId": "AKIAIOSFODNN7EXAMPLE",
        "sessionContext": {
            "attributes": {
                "mfaAuthenticated": "false",
                "creationDate": "2018-05-31T23:23:41Z"
            }
        },
        "invokedBy": "secretsmanager.amazonaws.com"
    },
    "eventTime": "2018-05-31T23:23:41Z",
    "eventSource": "kms.amazonaws.com",
    "eventName": "GenerateDataKey",
    "awsRegion": "us-west-2",
    "sourceIPAddress": "secretsmanager.amazonaws.com",
    "userAgent": "secretsmanager.amazonaws.com",
    "requestParameters": {
        "keyId": "arn:aws-cn:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab",
        "keySpec": "AES_256",
        "encryptionContext": {
            "SecretARN": "arn:aws-cn:secretsmanager:us-west-2:111122223333:secret:test-secret-a1b2c3",
            "SecretVersionId": "EXAMPLE1-90ab-cdef-fedc-ba987SECRET1"
        }
    },
    "responseElements": null,
    "requestID": "a7d4dd6f-6529-11e8-9881-67744a270888",
    "eventID": "af7476b6-62d7-42c2-bc02-5ce86c21ed36",
    "readOnly": true,
    "resources": [
        {
            "ARN": "arn:aws-cn:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab",
            "accountId": "111122223333",
            "type": "AWS::KMS::Key"
        }
    ],
    "eventType": "AwsApiCall",
    "recipientAccountId": "111122223333"
}
