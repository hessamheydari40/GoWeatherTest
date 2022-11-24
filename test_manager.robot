*** Settings ***
Documentation    Suite description
Library         customLibrary/everyThing.py


*** Test Cases ***
scrollScreenshotAndprecipitation
    [Tags]    DEBUG
    open app
    forecast tab Click
    scrooll
    screenshot
MostPuplarcityDegreeAssertion
    open app
    click main menu
    add city
    popular city
    ${degree}=   find degree is 50
    should be true  ${degree}
