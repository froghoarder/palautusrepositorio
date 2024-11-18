*** Settings ***
Resource  resource.robot
Suite Setup     Open And Configure Browser
Suite Teardown  Close Browser
Test Setup      Reset Application Create User And Go To Register Page

*** Test Cases ***

Register With Valid Username And Password
    Set Username  ankka
    Set Password  ankka123
    Set Password Confirmation  ankka123
    Submit Credentials
    Registration Should Succeed

Register With Too Short Username And Valid Password
    Set Username  a
    Set Password  ankka123
    Set Password Confirmation  ankka123
    Submit Credentials
    Registration Should Fail With Message  Username is too short

Register With Valid Username And Too Short Password
    Set Username  ankka
    Set Password  ankka
    Set Password Confirmation  ankka
    Submit Credentials
    Registration Should Fail With Message  Password is too short


Register With Valid Username And Invalid Password
    Set Username  ankka
    Set Password  ankkaaaa
    Set Password Confirmation  ankkaaaa
    Submit Credentials
    Registration Should Fail With Message  Password cannot contain only letters

Register With Nonmatching Password And Password Confirmation
    Set Username  ankka
    Set Password  ankka123
    Set Password Confirmation  ankka456
    Submit Credentials
    Registration Should Fail With Message  Passwords do not match


Register With Username That Is Already In Use
    Set Username  kalle
    Set Password  kalle123
    Set Password Confirmation  kalle123
    Submit Credentials
    Registration Should Fail With Message  Username is already in use

*** Keywords ***
Registration Should Succeed
    Welcome Page Should Be Open

Registration Should Fail With Message
    [Arguments]  ${message}
    Register Page Should Be Open
    Page Should Contain  ${message}

Submit Credentials
    Click Button  Register

Set Username
    [Arguments]  ${username}
    Input Text  username  ${username}

Set Password
    [Arguments]  ${password}
    Input Password  password  ${password}

Set Password Confirmation
    [Arguments]  ${password_confirmation}
    Input Password  password_confirmation  ${password_confirmation}

*** Keywords ***
Reset Application Create User And Go To Register Page
    Reset Application
    Create User  kalle  kalle123
    Go To Register Page
