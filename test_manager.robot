*** Settings ***
Documentation    Suite description
Library         customLibrary/everyThing.py


*** Test Cases ***
FindDegreeMore50testcase
    [Tags]    DEBUG
    open app
    click main menu
    add city
    popular city
    should be equal  find degree more than 50   0

FindPrecipitation
    open app
    forecast tab Click
    scrool29
screenshot
    open app
    screenshot