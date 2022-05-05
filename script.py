import csv
import json
from datetime import date

today = date.today()
class Indicators(object):
    def __init__(self, indicatorName,indicatorDescription,indicatorReportName, indicatorReportValue):
        self.indicatorName = indicatorName
        self.indicatorDescription = indicatorDescription
        self.indicatorReportName = indicatorReportName
        self.indicatorReportValue = indicatorReportValue


with open ('Anonymized dataset - Connected People 3-2 - 2022-03-07 (1).csv', 'r') as f1:
    reader = csv.reader(f1)
    next(reader)
    numberOfPeopleWhoAnswerA3orA4 = 0
    totalNumberofPeople = 0
    for index, row in enumerate(reader):
        if(row[4] and row[5]):
            if(row[4] == 'A3' or row[4] == 'A4'):
                numberOfPeopleWhoAnswerA3orA4 +=1
            elif(row[5] == 'A3' or row[5] == 'A4'):
                numberOfPeopleWhoAnswerA3orA4 +=1
    totalNumberofPeople = index

with open ('Anonymized dataset - Connected People 3-2 - 2022-03-07 (1).csv', 'r') as f1:
    reader = csv.reader(f1)
    next(reader)
    numberOfPeopleWhoAnswerBoth = 0
    numberOfPeopleReportingIncrease = 0
    numberOfPeopleWhoAnswerA3orA4 = 0
    for index, row in enumerate(reader):
        if(row[4] and row[5]):
            numberOfPeopleWhoAnswerBoth+=1
            if(row[4] == 'A1'):
                if(row[5] == 'A2' or row[5] == 'A3' or row[5] == 'A4'):
                    numberOfPeopleReportingIncrease+=1
            if(row[4] == 'A2'):
                if(row[5] == 'A3' or row[5] == 'A4'):
                    numberOfPeopleReportingIncrease+=1
            if(row[4] == 'A3'):
                numberOfPeopleWhoAnswerA3orA4 +=1
                if(row[5] == 'A4'):
                    numberOfPeopleReportingIncrease+=1
            if(row[4] == 'A4'):
                numberOfPeopleWhoAnswerA3orA4 +=1

IndicatorOptions = [
    Indicators('Sense of Belonging - Longitudinal comparison',
    '% participants reporting an increased sense of belonging with the local community. Longitudinal comparison of pre- and post- rating for individual respondents.',
    '% participants reporting an increased sense of belonging with the local community',
    (numberOfPeopleReportingIncrease/numberOfPeopleWhoAnswerBoth)*100)
    , Indicators('Sense of Belonging - Cross-sectional comparison',
    '% participants reporting an increased sense of belonging with the local community. Cross-sectional comparison of groups before and after intervention.',
    '% participants reporting an increased sense of belonging with the local community',
    (numberOfPeopleReportingIncrease/numberOfPeopleWhoAnswerBoth)*100)]

for index, obj in enumerate(IndicatorOptions):        
    data = [
    {
        "@context": "http://ontology.eil.utoronto.ca/cids/contexts/CIDSOrganizationContext.json",
        "@type": "cids:Organization",
        "@id": "https://www.logicaloutcomes.net/",
        "hasID": {
            "@context": "http://ontology.eil.utoronto.ca/CIDS/contexts/OrganizationIDContext.json",
            "@type": "org:OrganizationID",
            "issuedBy": "http://https://www.canada.ca/en/revenue-agency.html",
            "identifier": "12345678"
        },
        "hasLegalName": "LogicalOutcomes Canada"
    },
    {
        "@context": "http://ontology.eil.utoronto.ca/cids/contexts/OutcomeContext.json",
        "@type": "cids:Outcome",
        "@id": "https://www.logicaloutcomes.net/outcome1",
        "hasName": "Sense of Belonging",
        "hasDescription": "Think back to when you first joined us. How would you describe your sense of belonging to your local community at that time? Would you say it was… ",
        "forDomain": "http://ontology.eil.utoronto.ca/CIDS/cids#sdg1",
        "dateCreated": str(today)
    },
    {
        "@context": "http://ontology.eil.utoronto.ca/cids/contexts/IndicatorContext.json",
        "@type": "cids:Indicator",
        "@id": "https://www.logicaloutcomes.net/indicator1",
        "hasName": obj.indicatorName,
        "hasDescription":obj.indicatorDescription,
        "hasOutcome": "https://www.logicaloutcomes.net/outcome1"
    },
    {
        "@context": "http://ontology.eil.utoronto.ca/cids/contexts/IndicatorReportContext.json",
        "@type": "cids:IndicatorReport",
        "@id": "https://www.logicaloutcomes.net/indicatorReport1",
        "hasName": obj.indicatorReportName,
        "hasTimeInterval": {
            "@context": "http://ontology.eil.utoronto.ca/CIDS/contexts/TimeContext.json",
            "@type": "time:DateTimeInterval",
            "hasBeginnning": {
                "@type": "time:DateTimeDescription",
                "year": "yyyy",
                "month": "mm",
                "day": "dd"
            },
            "hasEnd": {
                "@type": "time:DateTimeDescription",
                "year": "yyyy",
                "month": "mm",
                "day": "dd"
            }
        },
        "forOrganization": "https://www.logicaloutcomes.net/",
        "forIndicator": "https://www.logicaloutcomes.net/indicator1",
        "value": {
            "@context": "http://ontology.eil.utoronto.ca/CIDS/contexts/ISO21972Context.json",
            "@type": "i72:Measure",
            "numerical_value": obj.indicatorReportValue
        },
        "dateCreated": str(today)
    }
]
    with open('LO-Indicator-IndicatorReport'+ str(index)+ '.json', 'w') as f:
        json.dump(data,f,indent=4, allow_nan=False)
