# Test Report Markdown Export

This file is an export of the RDF test report made out of [EARL vocabulary](https://www.w3.org/TR/EARL10/)

This test is powered by Corese, check the [website](https://project.inria.fr/corese/) and the [repository](https://github.com/Wimmics/corese)

The original test report is available in turtle syntax [here](./query-test-manual-NicoRobertIn-2024-06-13T15-52-06.ttl).

# Test Context

Here is some context about under which context this test was made

|Assertor|[NicoRobertIn](https://github.com/NicoRobertIn)|
|----|-----|
|Title|NicoRobertIn&#32;using&#32;manual&#32;script|
|Description|Test&#32;triggered&#32;by&#32;[@NicoRobertIn](https://github.com/NicoRobertIn)&#32;by&#32;manual&#32;trigger|
|Script|[query test suite](https://github.com/Wimmics/olivaw/blob/main/olivaw/test/query/suite.py)
|Date|2024-06-13 15:51:57|

***


# Statistic summary

Here is a short overview for this test report

197 Outcomes

:boom:1 MajorFail, :exclamation:5 MinorFail, :warning:0 CannotTell, :grey_question:7 NotTested, :white_check_mark:184 Pass

<div  style="border-radius: 12px; height: 25px; overflow: hidden"><img src="../assets/red.png" width="1%" height="25px"/><img src="../assets/orange.png" width="2%" height="25px"/><img src="../assets/grey.png" width="0%" height="25px"/><img src="../assets/white.png" width="3%" height="25px"/><img src="../assets/green.png" width="94%" height="25px"/></div>

<br/>

The different status types are an extension of the [EARL](https://www.w3.org/TR/EARL10-Schema/) vocabulary where the nextended terms can be found in the [olivaw-earl dataset](https://github.com/Wimmics/olivaw/blob/main/olivaw/test/olivaw-earl.ttl), each outcome type means:
* :boom: MajorFail: This is an error that is critical and consider as blocking for production
* :exclamation: MinorFail: This is an error that should be fixed, but it is cannot be considered as critical error
* :warning: CannotTell: It is unclear if the subject passed or failed the test. This happens when an automated test requires human judgement to make a definite decision.
* :grey_question: NotTested:  The test has not been carried out. Here this is because a previous test that was mandatory to be passed did not end up as Pass.
* :white_check_mark: Pass: The subject passed the test.

***


# MajorFail Outcomes

[Jump to statistic summary](#statistic-summary)	|	Previous section	|	[Next section](#minorfail-outcomes)

Here is the chapter related to the MajorFail outcome

:boom:1 MajorFail outcomes

<details>
<summary>Fold/Unfold the 1 summary and details</summary>

## MajorFail Outcomes Summary

:boom:1 MajorFail outcomes

|*Jump*|*Number*|*Status*|*Subject*|*Criterion*|*Title*|*Link*|
|------|--------|--------|---------|-----------|-------|------|
|[Chapter top](#majorfail-outcomes)|<div id="summary-MajorFail-1">1/1</div>|:boom:MajorFail|`question-manufacturing-environments-discover-core-q6`|[syntax](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#syntax)|Test subject has syntax errors|[Jump](#majorfail-outcome-number-1)|

***

## MajorFail Outcomes Details

This subchapter gives more details to the :boom:MajorFail outcomes

### MajorFail Outcome number 1

[Jump to summary definition](#summary-MajorFail-1)	|	Previous MajorFail outcome	|	Next MajorFail outcome

:boom:MajorFail outcome
#### Subject detail
|Name|question-manufacturing-environments-discover-core-q6|
|----|----|
|Title|competency&#32;question&#32;domains/manufacturing-environments/discover-core/q6.rq&#32;from&#32;branch&#32;main|
|Composition|- [Competency question manufacturing-environments/discover-core/q6](https://github.com/HyperAgents/hmas/blob/main/domains/manufacturing-environments/discover-core/q6.rq.ttl)|

#### Criterion detail
|Identifier|[syntax](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#syntax)|
|----|----|
|Title|Syntax&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;check&#32;wether&#32;the&#32;test&#32;subject&#32;is&#32;syntaxically&#32;correct&#32;or&#32;not.|

#### Outcome Detail
|Jump|Type|:boom:MajorFail|
|----|----|----|
|[Section top](#majorfail-outcome-number-1)|Identifier|`syntax-error`|
|[Section top](#majorfail-outcome-number-1)|Title|Test&#32;subject&#32;has&#32;syntax&#32;errors|
|[Section top](#majorfail-outcome-number-1)|Description|Encountered&#32; &#34;&#60; &#34;&#32;at&#32;line&#32;1,&#32;column&#32;14.|
|[Section top](#majorfail-outcome-number-1)|Pointer|<pre lang="Turtle"><code>prefix&#32;hmas:&#32; &#60;https://purl.org/hmas/  &#10;prefix&#32;ex:&#32; &#60;http://example.org/>  &#10;ask&#32;{  &#10; &#32; &#32; &#32; &#32;bind&#32;(ex:productionCell1&#32;as&#32;?workspace1)  &#10; &#32; &#32; &#32; &#32;bind&#32;(ex:productionCell2&#32;as&#32;?workspace2)  &#10; &#32; &#32; &#32; &#32;ex:autonomousBob&#32;hmas:isContainedIn&#32;?workspace1,&#32;?workspace2&#32;.  &#10; &#32; &#32; &#32; &#32;?workspace1&#32;a&#32;hmas:Workspace&#32;.  &#10; &#32; &#32; &#32; &#32;?workspace2&#32;a&#32;hmas:Workspace&#32;.  &#10;}</code></pre>|

***

</details>

***


# MinorFail Outcomes

[Jump to statistic summary](#statistic-summary)	|	[Previous section](#majorfail-outcomes)	|	[Next section](#nottested-outcomes)

Here is the chapter related to the MinorFail outcome

:exclamation:5 MinorFail outcomes

<details>
<summary>Fold/Unfold the 5 summary and details</summary>

## MinorFail Outcomes Summary

:exclamation:5 MinorFail outcomes

|*Jump*|*Number*|*Status*|*Subject*|*Criterion*|*Title*|*Link*|
|------|--------|--------|---------|-----------|-------|------|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-1">1/5</div>|:exclamation:MinorFail|`question-manufacturing-environments-safety-rules-4`|[uri-validity](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#uri-validity)|Invalid URI|[Jump](#minorfail-outcome-number-1)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-2">2/5</div>|:exclamation:MinorFail|`question-manufacturing-environments-safety-rules-4`|[uri-validity](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#uri-validity)|Invalid URI|[Jump](#minorfail-outcome-number-2)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-3">3/5</div>|:exclamation:MinorFail|`question-manufacturing-environments-safety-rules-3`|[uri-validity](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#uri-validity)|Invalid URI|[Jump](#minorfail-outcome-number-3)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-4">4/5</div>|:exclamation:MinorFail|`question-manufacturing-environments-safety-rules-2`|[uri-validity](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#uri-validity)|Invalid URI|[Jump](#minorfail-outcome-number-4)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-5">5/5</div>|:exclamation:MinorFail|`question-manufacturing-environments-safety-rules-1`|[uri-validity](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#uri-validity)|Invalid URI|[Jump](#minorfail-outcome-number-5)|

***

## MinorFail Outcomes Details

This subchapter gives more details to the :exclamation:MinorFail outcomes

### MinorFail Outcome number 1

[Jump to summary definition](#summary-MinorFail-1)	|	Previous MinorFail outcome	|	[Next MinorFail outcome](#minorfail-outcome-number-2)

:exclamation:MinorFail outcome
#### Subject detail
|Name|question-manufacturing-environments-safety-rules-4|
|----|----|
|Title|competency&#32;question&#32;domains/manufacturing-environments/safety-rules/4.rq&#32;from&#32;branch&#32;main|
|Composition|- [Competency question manufacturing-environments/safety-rules/4](https://github.com/HyperAgents/hmas/blob/main/domains/manufacturing-environments/safety-rules/4.rq.ttl)|

#### Criterion detail
|Identifier|[uri-validity](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#uri-validity)|
|----|----|
|Title|URI&#32;validity&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;check&#32;if&#32;all&#32;the&#32;URIs&#32;of&#32;the&#32;resource&#32;are&#32;well-formed|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-1)|Identifier|`invalid-uri`|
|[Section top](#minorfail-outcome-number-1)|Title|Invalid&#32;URI|
|[Section top](#minorfail-outcome-number-1)|Description|Expected&#32;valid&#32;URIs&#32;in&#32;subject&#32;but&#32;got:&#32;#enforcesNorm|
|[Section top](#minorfail-outcome-number-1)|Pointer|<pre lang="Turtle"><code>PREFIX&#32;:&#32; &#60;#>  &#10;SELECT&#32;?norm  &#10;WHERE&#32;{  &#10; &#32;&#32;?organization&#32;:enforcesNorm&#32;?norm&#32;.  &#10; &#32;&#32;?norm&#32;:hasNormativeContext&#32;?context&#32;.  &#10; &#32;&#32;FILTER(?context&#32;=&#32;:myContext)  &#10;}</code></pre>|

***
### MinorFail Outcome number 2

[Jump to summary definition](#summary-MinorFail-2)	|	[Previous MinorFail outcome](#minorfail-outcome-number-1)	|	[Next MinorFail outcome](#minorfail-outcome-number-3)

:exclamation:MinorFail outcome
#### Subject detail
|Name|question-manufacturing-environments-safety-rules-4|
|----|----|
|Title|competency&#32;question&#32;domains/manufacturing-environments/safety-rules/4.rq&#32;from&#32;branch&#32;main|
|Composition|- [Competency question manufacturing-environments/safety-rules/4](https://github.com/HyperAgents/hmas/blob/main/domains/manufacturing-environments/safety-rules/4.rq.ttl)|

#### Criterion detail
|Identifier|[uri-validity](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#uri-validity)|
|----|----|
|Title|URI&#32;validity&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;check&#32;if&#32;all&#32;the&#32;URIs&#32;of&#32;the&#32;resource&#32;are&#32;well-formed|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-2)|Identifier|`invalid-uri`|
|[Section top](#minorfail-outcome-number-2)|Title|Invalid&#32;URI|
|[Section top](#minorfail-outcome-number-2)|Description|Expected&#32;valid&#32;URIs&#32;in&#32;subject&#32;but&#32;got:&#32;#hasNormativeContext|
|[Section top](#minorfail-outcome-number-2)|Pointer|<pre lang="Turtle"><code>PREFIX&#32;:&#32; &#60;#>  &#10;SELECT&#32;?norm  &#10;WHERE&#32;{  &#10; &#32;&#32;?organization&#32;:enforcesNorm&#32;?norm&#32;.  &#10; &#32;&#32;?norm&#32;:hasNormativeContext&#32;?context&#32;.  &#10; &#32;&#32;FILTER(?context&#32;=&#32;:myContext)  &#10;}</code></pre>|

***
### MinorFail Outcome number 3

[Jump to summary definition](#summary-MinorFail-3)	|	[Previous MinorFail outcome](#minorfail-outcome-number-2)	|	[Next MinorFail outcome](#minorfail-outcome-number-4)

:exclamation:MinorFail outcome
#### Subject detail
|Name|question-manufacturing-environments-safety-rules-3|
|----|----|
|Title|competency&#32;question&#32;domains/manufacturing-environments/safety-rules/3.rq&#32;from&#32;branch&#32;main|
|Composition|- [Competency question manufacturing-environments/safety-rules/3](https://github.com/HyperAgents/hmas/blob/main/domains/manufacturing-environments/safety-rules/3.rq.ttl)|

#### Criterion detail
|Identifier|[uri-validity](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#uri-validity)|
|----|----|
|Title|URI&#32;validity&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;check&#32;if&#32;all&#32;the&#32;URIs&#32;of&#32;the&#32;resource&#32;are&#32;well-formed|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-3)|Identifier|`invalid-uri`|
|[Section top](#minorfail-outcome-number-3)|Title|Invalid&#32;URI|
|[Section top](#minorfail-outcome-number-3)|Description|Expected&#32;valid&#32;URIs&#32;in&#32;subject&#32;but&#32;got:&#32;#hasRespectStatus|
|[Section top](#minorfail-outcome-number-3)|Pointer|<pre lang="Turtle"><code>PREFIX&#32;:&#32; &#60;#>  &#10;SELECT&#32;?norm  &#10;WHERE&#32;{  &#10; &#32;&#32;?norm&#32;:hasRespectStatus&#32;false&#32;.  &#10;}</code></pre>|

***
### MinorFail Outcome number 4

[Jump to summary definition](#summary-MinorFail-4)	|	[Previous MinorFail outcome](#minorfail-outcome-number-3)	|	[Next MinorFail outcome](#minorfail-outcome-number-5)

:exclamation:MinorFail outcome
#### Subject detail
|Name|question-manufacturing-environments-safety-rules-2|
|----|----|
|Title|competency&#32;question&#32;domains/manufacturing-environments/safety-rules/2.rq&#32;from&#32;branch&#32;main|
|Composition|- [Competency question manufacturing-environments/safety-rules/2](https://github.com/HyperAgents/hmas/blob/main/domains/manufacturing-environments/safety-rules/2.rq.ttl)|

#### Criterion detail
|Identifier|[uri-validity](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#uri-validity)|
|----|----|
|Title|URI&#32;validity&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;check&#32;if&#32;all&#32;the&#32;URIs&#32;of&#32;the&#32;resource&#32;are&#32;well-formed|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-4)|Identifier|`invalid-uri`|
|[Section top](#minorfail-outcome-number-4)|Title|Invalid&#32;URI|
|[Section top](#minorfail-outcome-number-4)|Description|Expected&#32;valid&#32;URIs&#32;in&#32;subject&#32;but&#32;got:&#32;#hasNormativeTarget|
|[Section top](#minorfail-outcome-number-4)|Pointer|<pre lang="Turtle"><code>PREFIX&#32;:&#32; &#60;#>  &#10;SELECT&#32;?agent  &#10;WHERE&#32;{  &#10; &#32;&#32;?norm&#32;:hasNormativeTarget&#32;?agent&#32;.  &#10;}</code></pre>|

***
### MinorFail Outcome number 5

[Jump to summary definition](#summary-MinorFail-5)	|	[Previous MinorFail outcome](#minorfail-outcome-number-4)	|	Next MinorFail outcome

:exclamation:MinorFail outcome
#### Subject detail
|Name|question-manufacturing-environments-safety-rules-1|
|----|----|
|Title|competency&#32;question&#32;domains/manufacturing-environments/safety-rules/1.rq&#32;from&#32;branch&#32;main|
|Composition|- [Competency question manufacturing-environments/safety-rules/1](https://github.com/HyperAgents/hmas/blob/main/domains/manufacturing-environments/safety-rules/1.rq.ttl)|

#### Criterion detail
|Identifier|[uri-validity](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#uri-validity)|
|----|----|
|Title|URI&#32;validity&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;check&#32;if&#32;all&#32;the&#32;URIs&#32;of&#32;the&#32;resource&#32;are&#32;well-formed|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-5)|Identifier|`invalid-uri`|
|[Section top](#minorfail-outcome-number-5)|Title|Invalid&#32;URI|
|[Section top](#minorfail-outcome-number-5)|Description|Expected&#32;valid&#32;URIs&#32;in&#32;subject&#32;but&#32;got:&#32;#RegulativeNorm|
|[Section top](#minorfail-outcome-number-5)|Pointer|<pre lang="Turtle"><code>PREFIX&#32;:&#32; &#60;#>  &#10;SELECT&#32;?norm  &#10;WHERE&#32;{  &#10; &#32;&#32;?norm&#32;rdf:type&#32;:RegulativeNorm&#32;.  &#10;}</code></pre>|

***

</details>

***


# NotTested Outcomes

[Jump to statistic summary](#statistic-summary)	|	[Previous section](#minorfail-outcomes)	|	[Next section](#pass-outcomes)

Here is the chapter related to the NotTested outcome

:grey_question:7 NotTested outcomes

<details>
<summary>Fold/Unfold the 7 summary and details</summary>

## NotTested Outcomes Summary

:grey_question:7 NotTested outcomes

|*Jump*|*Number*|*Status*|*Subject*|*Criterion*|*Title*|*Link*|
|------|--------|--------|---------|-----------|-------|------|
|[Chapter top](#nottested-outcomes)|<div id="summary-NotTested-1">1/7</div>|:grey_question:NotTested|`question-manufacturing-environments-safety-rules-4`|[namespace-validity](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#namespace-validity)|The test could not be run|[Jump](#nottested-outcome-number-1)|
|[Chapter top](#nottested-outcomes)|<div id="summary-NotTested-2">2/7</div>|:grey_question:NotTested|`question-manufacturing-environments-safety-rules-3`|[namespace-validity](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#namespace-validity)|The test could not be run|[Jump](#nottested-outcome-number-2)|
|[Chapter top](#nottested-outcomes)|<div id="summary-NotTested-3">3/7</div>|:grey_question:NotTested|`question-manufacturing-environments-safety-rules-2`|[namespace-validity](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#namespace-validity)|The test could not be run|[Jump](#nottested-outcome-number-3)|
|[Chapter top](#nottested-outcomes)|<div id="summary-NotTested-4">4/7</div>|:grey_question:NotTested|`question-manufacturing-environments-safety-rules-1`|[namespace-validity](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#namespace-validity)|The test could not be run|[Jump](#nottested-outcome-number-4)|
|[Chapter top](#nottested-outcomes)|<div id="summary-NotTested-5">5/7</div>|:grey_question:NotTested|`question-manufacturing-environments-discover-core-q6`|[namespace-validity](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#namespace-validity)|The test could not be run|[Jump](#nottested-outcome-number-5)|
|[Chapter top](#nottested-outcomes)|<div id="summary-NotTested-6">6/7</div>|:grey_question:NotTested|`question-manufacturing-environments-discover-core-q6`|[query-type](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#query-type)|The test could not be run|[Jump](#nottested-outcome-number-6)|
|[Chapter top](#nottested-outcomes)|<div id="summary-NotTested-7">7/7</div>|:grey_question:NotTested|`question-manufacturing-environments-discover-core-q6`|[uri-validity](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#uri-validity)|The test could not be run|[Jump](#nottested-outcome-number-7)|

***

## NotTested Outcomes Details

This subchapter gives more details to the :grey_question:NotTested outcomes

### NotTested Outcome number 1

[Jump to summary definition](#summary-NotTested-1)	|	Previous NotTested outcome	|	[Next NotTested outcome](#nottested-outcome-number-2)

:grey_question:NotTested outcome
#### Subject detail
|Name|question-manufacturing-environments-safety-rules-4|
|----|----|
|Title|competency&#32;question&#32;domains/manufacturing-environments/safety-rules/4.rq&#32;from&#32;branch&#32;main|
|Composition|- [Competency question manufacturing-environments/safety-rules/4](https://github.com/HyperAgents/hmas/blob/main/domains/manufacturing-environments/safety-rules/4.rq.ttl)|

#### Criterion detail
|Identifier|[namespace-validity](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#namespace-validity)|
|----|----|
|Title|Prefix&#32;validity&#32;test|
|Description|A&#32;test&#32;case&#32;checking&#32;if&#32;all&#32;the&#32;prefixes&#32;are&#32;not&#32;too&#32;close&#32;from&#32;the&#32;most&#32;used&#32;existing&#32;namespaces&#32;(according&#32;to&#32;prefix&#32;cc)&#32;or&#32;an&#32;ontology&#32;namespace|

#### Outcome Detail
|Jump|Type|:grey_question:NotTested|
|----|----|----|
|[Section top](#nottested-outcome-number-1)|Identifier|`namespace-typo`|
|[Section top](#nottested-outcome-number-1)|Title|The&#32;test&#32;could&#32;not&#32;be&#32;run|
|[Section top](#nottested-outcome-number-1)|Description|All&#32;the&#32;subject&#32;URIs&#32;should&#32;be&#32;well-formed|

***
### NotTested Outcome number 2

[Jump to summary definition](#summary-NotTested-2)	|	[Previous NotTested outcome](#nottested-outcome-number-1)	|	[Next NotTested outcome](#nottested-outcome-number-3)

:grey_question:NotTested outcome
#### Subject detail
|Name|question-manufacturing-environments-safety-rules-3|
|----|----|
|Title|competency&#32;question&#32;domains/manufacturing-environments/safety-rules/3.rq&#32;from&#32;branch&#32;main|
|Composition|- [Competency question manufacturing-environments/safety-rules/3](https://github.com/HyperAgents/hmas/blob/main/domains/manufacturing-environments/safety-rules/3.rq.ttl)|

#### Criterion detail
|Identifier|[namespace-validity](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#namespace-validity)|
|----|----|
|Title|Prefix&#32;validity&#32;test|
|Description|A&#32;test&#32;case&#32;checking&#32;if&#32;all&#32;the&#32;prefixes&#32;are&#32;not&#32;too&#32;close&#32;from&#32;the&#32;most&#32;used&#32;existing&#32;namespaces&#32;(according&#32;to&#32;prefix&#32;cc)&#32;or&#32;an&#32;ontology&#32;namespace|

#### Outcome Detail
|Jump|Type|:grey_question:NotTested|
|----|----|----|
|[Section top](#nottested-outcome-number-2)|Identifier|`namespace-typo`|
|[Section top](#nottested-outcome-number-2)|Title|The&#32;test&#32;could&#32;not&#32;be&#32;run|
|[Section top](#nottested-outcome-number-2)|Description|All&#32;the&#32;subject&#32;URIs&#32;should&#32;be&#32;well-formed|

***
### NotTested Outcome number 3

[Jump to summary definition](#summary-NotTested-3)	|	[Previous NotTested outcome](#nottested-outcome-number-2)	|	[Next NotTested outcome](#nottested-outcome-number-4)

:grey_question:NotTested outcome
#### Subject detail
|Name|question-manufacturing-environments-safety-rules-2|
|----|----|
|Title|competency&#32;question&#32;domains/manufacturing-environments/safety-rules/2.rq&#32;from&#32;branch&#32;main|
|Composition|- [Competency question manufacturing-environments/safety-rules/2](https://github.com/HyperAgents/hmas/blob/main/domains/manufacturing-environments/safety-rules/2.rq.ttl)|

#### Criterion detail
|Identifier|[namespace-validity](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#namespace-validity)|
|----|----|
|Title|Prefix&#32;validity&#32;test|
|Description|A&#32;test&#32;case&#32;checking&#32;if&#32;all&#32;the&#32;prefixes&#32;are&#32;not&#32;too&#32;close&#32;from&#32;the&#32;most&#32;used&#32;existing&#32;namespaces&#32;(according&#32;to&#32;prefix&#32;cc)&#32;or&#32;an&#32;ontology&#32;namespace|

#### Outcome Detail
|Jump|Type|:grey_question:NotTested|
|----|----|----|
|[Section top](#nottested-outcome-number-3)|Identifier|`namespace-typo`|
|[Section top](#nottested-outcome-number-3)|Title|The&#32;test&#32;could&#32;not&#32;be&#32;run|
|[Section top](#nottested-outcome-number-3)|Description|All&#32;the&#32;subject&#32;URIs&#32;should&#32;be&#32;well-formed|

***
### NotTested Outcome number 4

[Jump to summary definition](#summary-NotTested-4)	|	[Previous NotTested outcome](#nottested-outcome-number-3)	|	[Next NotTested outcome](#nottested-outcome-number-5)

:grey_question:NotTested outcome
#### Subject detail
|Name|question-manufacturing-environments-safety-rules-1|
|----|----|
|Title|competency&#32;question&#32;domains/manufacturing-environments/safety-rules/1.rq&#32;from&#32;branch&#32;main|
|Composition|- [Competency question manufacturing-environments/safety-rules/1](https://github.com/HyperAgents/hmas/blob/main/domains/manufacturing-environments/safety-rules/1.rq.ttl)|

#### Criterion detail
|Identifier|[namespace-validity](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#namespace-validity)|
|----|----|
|Title|Prefix&#32;validity&#32;test|
|Description|A&#32;test&#32;case&#32;checking&#32;if&#32;all&#32;the&#32;prefixes&#32;are&#32;not&#32;too&#32;close&#32;from&#32;the&#32;most&#32;used&#32;existing&#32;namespaces&#32;(according&#32;to&#32;prefix&#32;cc)&#32;or&#32;an&#32;ontology&#32;namespace|

#### Outcome Detail
|Jump|Type|:grey_question:NotTested|
|----|----|----|
|[Section top](#nottested-outcome-number-4)|Identifier|`namespace-typo`|
|[Section top](#nottested-outcome-number-4)|Title|The&#32;test&#32;could&#32;not&#32;be&#32;run|
|[Section top](#nottested-outcome-number-4)|Description|All&#32;the&#32;subject&#32;URIs&#32;should&#32;be&#32;well-formed|

***
### NotTested Outcome number 5

[Jump to summary definition](#summary-NotTested-5)	|	[Previous NotTested outcome](#nottested-outcome-number-4)	|	[Next NotTested outcome](#nottested-outcome-number-6)

:grey_question:NotTested outcome
#### Subject detail
|Name|question-manufacturing-environments-discover-core-q6|
|----|----|
|Title|competency&#32;question&#32;domains/manufacturing-environments/discover-core/q6.rq&#32;from&#32;branch&#32;main|
|Composition|- [Competency question manufacturing-environments/discover-core/q6](https://github.com/HyperAgents/hmas/blob/main/domains/manufacturing-environments/discover-core/q6.rq.ttl)|

#### Criterion detail
|Identifier|[namespace-validity](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#namespace-validity)|
|----|----|
|Title|Prefix&#32;validity&#32;test|
|Description|A&#32;test&#32;case&#32;checking&#32;if&#32;all&#32;the&#32;prefixes&#32;are&#32;not&#32;too&#32;close&#32;from&#32;the&#32;most&#32;used&#32;existing&#32;namespaces&#32;(according&#32;to&#32;prefix&#32;cc)&#32;or&#32;an&#32;ontology&#32;namespace|

#### Outcome Detail
|Jump|Type|:grey_question:NotTested|
|----|----|----|
|[Section top](#nottested-outcome-number-5)|Identifier|`namespace-typo`|
|[Section top](#nottested-outcome-number-5)|Title|The&#32;test&#32;could&#32;not&#32;be&#32;run|
|[Section top](#nottested-outcome-number-5)|Description|The&#32;subject&#32;must&#32;be&#32;syntaxically&#32;correct|

***
### NotTested Outcome number 6

[Jump to summary definition](#summary-NotTested-6)	|	[Previous NotTested outcome](#nottested-outcome-number-5)	|	[Next NotTested outcome](#nottested-outcome-number-7)

:grey_question:NotTested outcome
#### Subject detail
|Name|question-manufacturing-environments-discover-core-q6|
|----|----|
|Title|competency&#32;question&#32;domains/manufacturing-environments/discover-core/q6.rq&#32;from&#32;branch&#32;main|
|Composition|- [Competency question manufacturing-environments/discover-core/q6](https://github.com/HyperAgents/hmas/blob/main/domains/manufacturing-environments/discover-core/q6.rq.ttl)|

#### Criterion detail
|Identifier|[query-type](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#query-type)|
|----|----|
|Title|Query&#32;type&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;check&#32;if&#32;the&#32;query&#32;is&#32;indeed&#32;of&#32;type&#32;Select&#32;or&#32;Ask|

#### Outcome Detail
|Jump|Type|:grey_question:NotTested|
|----|----|----|
|[Section top](#nottested-outcome-number-6)|Identifier|`wrong-query-type`|
|[Section top](#nottested-outcome-number-6)|Title|The&#32;test&#32;could&#32;not&#32;be&#32;run|
|[Section top](#nottested-outcome-number-6)|Description|The&#32;query&#32;must&#32;be&#32;syntaxically&#32;correct|

***
### NotTested Outcome number 7

[Jump to summary definition](#summary-NotTested-7)	|	[Previous NotTested outcome](#nottested-outcome-number-6)	|	Next NotTested outcome

:grey_question:NotTested outcome
#### Subject detail
|Name|question-manufacturing-environments-discover-core-q6|
|----|----|
|Title|competency&#32;question&#32;domains/manufacturing-environments/discover-core/q6.rq&#32;from&#32;branch&#32;main|
|Composition|- [Competency question manufacturing-environments/discover-core/q6](https://github.com/HyperAgents/hmas/blob/main/domains/manufacturing-environments/discover-core/q6.rq.ttl)|

#### Criterion detail
|Identifier|[uri-validity](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#uri-validity)|
|----|----|
|Title|URI&#32;validity&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;check&#32;if&#32;all&#32;the&#32;URIs&#32;of&#32;the&#32;resource&#32;are&#32;well-formed|

#### Outcome Detail
|Jump|Type|:grey_question:NotTested|
|----|----|----|
|[Section top](#nottested-outcome-number-7)|Identifier|`invalid-uri`|
|[Section top](#nottested-outcome-number-7)|Title|The&#32;test&#32;could&#32;not&#32;be&#32;run|
|[Section top](#nottested-outcome-number-7)|Description|The&#32;subject&#32;must&#32;be&#32;syntaxically&#32;valid|

***

</details>

***


# Pass Outcomes

[Jump to statistic summary](#statistic-summary)	|	[Previous section](#nottested-outcomes)	|	Next section

Here is the chapter related to the Pass outcome

:white_check_mark:184 Pass outcomes

<details>
<summary>Fold/Unfold the 184 summary and details</summary>

## Pass Outcomes Summary

:white_check_mark:184 Pass outcomes

|*Jump*|*Number*|*Status*|*Subject*|*Criterion*|*Title*|*Link*|
|------|--------|--------|---------|-----------|-------|------|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-1">1/184</div>|:white_check_mark:Pass|`question-manufacturing-environments-safety-rules-4`|[query-type](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#query-type)|Accurate query type|[Jump](#pass-outcome-number-1)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-2">2/184</div>|:white_check_mark:Pass|`question-manufacturing-environments-safety-rules-4`|[syntax](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#syntax)|Correct syntax|[Jump](#pass-outcome-number-2)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-3">3/184</div>|:white_check_mark:Pass|`question-manufacturing-environments-safety-rules-3`|[query-type](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#query-type)|Accurate query type|[Jump](#pass-outcome-number-3)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-4">4/184</div>|:white_check_mark:Pass|`question-manufacturing-environments-safety-rules-3`|[syntax](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#syntax)|Correct syntax|[Jump](#pass-outcome-number-4)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-5">5/184</div>|:white_check_mark:Pass|`question-manufacturing-environments-safety-rules-2`|[query-type](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#query-type)|Accurate query type|[Jump](#pass-outcome-number-5)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-6">6/184</div>|:white_check_mark:Pass|`question-manufacturing-environments-safety-rules-2`|[syntax](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#syntax)|Correct syntax|[Jump](#pass-outcome-number-6)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-7">7/184</div>|:white_check_mark:Pass|`question-manufacturing-environments-safety-rules-1`|[query-type](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#query-type)|Accurate query type|[Jump](#pass-outcome-number-7)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-8">8/184</div>|:white_check_mark:Pass|`question-manufacturing-environments-safety-rules-1`|[syntax](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#syntax)|Correct syntax|[Jump](#pass-outcome-number-8)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-9">9/184</div>|:white_check_mark:Pass|`question-manufacturing-environments-discover-signifiers-q3`|[namespace-validity](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#namespace-validity)|No namespace typo|[Jump](#pass-outcome-number-9)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-10">10/184</div>|:white_check_mark:Pass|`question-manufacturing-environments-discover-signifiers-q3`|[query-type](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#query-type)|Accurate query type|[Jump](#pass-outcome-number-10)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-11">11/184</div>|:white_check_mark:Pass|`question-manufacturing-environments-discover-signifiers-q3`|[syntax](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#syntax)|Correct syntax|[Jump](#pass-outcome-number-11)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-12">12/184</div>|:white_check_mark:Pass|`question-manufacturing-environments-discover-signifiers-q3`|[uri-validity](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#uri-validity)|All subject URI valid|[Jump](#pass-outcome-number-12)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-13">13/184</div>|:white_check_mark:Pass|`question-manufacturing-environments-discover-signifiers-q2`|[namespace-validity](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#namespace-validity)|No namespace typo|[Jump](#pass-outcome-number-13)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-14">14/184</div>|:white_check_mark:Pass|`question-manufacturing-environments-discover-signifiers-q2`|[query-type](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#query-type)|Accurate query type|[Jump](#pass-outcome-number-14)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-15">15/184</div>|:white_check_mark:Pass|`question-manufacturing-environments-discover-signifiers-q2`|[syntax](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#syntax)|Correct syntax|[Jump](#pass-outcome-number-15)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-16">16/184</div>|:white_check_mark:Pass|`question-manufacturing-environments-discover-signifiers-q2`|[uri-validity](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#uri-validity)|All subject URI valid|[Jump](#pass-outcome-number-16)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-17">17/184</div>|:white_check_mark:Pass|`question-manufacturing-environments-discover-signifiers-q1`|[namespace-validity](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#namespace-validity)|No namespace typo|[Jump](#pass-outcome-number-17)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-18">18/184</div>|:white_check_mark:Pass|`question-manufacturing-environments-discover-signifiers-q1`|[query-type](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#query-type)|Accurate query type|[Jump](#pass-outcome-number-18)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-19">19/184</div>|:white_check_mark:Pass|`question-manufacturing-environments-discover-signifiers-q1`|[syntax](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#syntax)|Correct syntax|[Jump](#pass-outcome-number-19)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-20">20/184</div>|:white_check_mark:Pass|`question-manufacturing-environments-discover-signifiers-q1`|[uri-validity](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#uri-validity)|All subject URI valid|[Jump](#pass-outcome-number-20)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-21">21/184</div>|:white_check_mark:Pass|`question-manufacturing-environments-discover-platforms-q4`|[namespace-validity](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#namespace-validity)|No namespace typo|[Jump](#pass-outcome-number-21)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-22">22/184</div>|:white_check_mark:Pass|`question-manufacturing-environments-discover-platforms-q4`|[query-type](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#query-type)|Accurate query type|[Jump](#pass-outcome-number-22)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-23">23/184</div>|:white_check_mark:Pass|`question-manufacturing-environments-discover-platforms-q4`|[syntax](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#syntax)|Correct syntax|[Jump](#pass-outcome-number-23)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-24">24/184</div>|:white_check_mark:Pass|`question-manufacturing-environments-discover-platforms-q4`|[uri-validity](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#uri-validity)|All subject URI valid|[Jump](#pass-outcome-number-24)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-25">25/184</div>|:white_check_mark:Pass|`question-manufacturing-environments-discover-platforms-q3`|[namespace-validity](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#namespace-validity)|No namespace typo|[Jump](#pass-outcome-number-25)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-26">26/184</div>|:white_check_mark:Pass|`question-manufacturing-environments-discover-platforms-q3`|[query-type](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#query-type)|Accurate query type|[Jump](#pass-outcome-number-26)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-27">27/184</div>|:white_check_mark:Pass|`question-manufacturing-environments-discover-platforms-q3`|[syntax](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#syntax)|Correct syntax|[Jump](#pass-outcome-number-27)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-28">28/184</div>|:white_check_mark:Pass|`question-manufacturing-environments-discover-platforms-q3`|[uri-validity](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#uri-validity)|All subject URI valid|[Jump](#pass-outcome-number-28)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-29">29/184</div>|:white_check_mark:Pass|`question-manufacturing-environments-discover-platforms-q2`|[namespace-validity](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#namespace-validity)|No namespace typo|[Jump](#pass-outcome-number-29)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-30">30/184</div>|:white_check_mark:Pass|`question-manufacturing-environments-discover-platforms-q2`|[query-type](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#query-type)|Accurate query type|[Jump](#pass-outcome-number-30)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-31">31/184</div>|:white_check_mark:Pass|`question-manufacturing-environments-discover-platforms-q2`|[syntax](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#syntax)|Correct syntax|[Jump](#pass-outcome-number-31)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-32">32/184</div>|:white_check_mark:Pass|`question-manufacturing-environments-discover-platforms-q2`|[uri-validity](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#uri-validity)|All subject URI valid|[Jump](#pass-outcome-number-32)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-33">33/184</div>|:white_check_mark:Pass|`question-manufacturing-environments-discover-platforms-q1`|[namespace-validity](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#namespace-validity)|No namespace typo|[Jump](#pass-outcome-number-33)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-34">34/184</div>|:white_check_mark:Pass|`question-manufacturing-environments-discover-platforms-q1`|[query-type](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#query-type)|Accurate query type|[Jump](#pass-outcome-number-34)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-35">35/184</div>|:white_check_mark:Pass|`question-manufacturing-environments-discover-platforms-q1`|[syntax](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#syntax)|Correct syntax|[Jump](#pass-outcome-number-35)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-36">36/184</div>|:white_check_mark:Pass|`question-manufacturing-environments-discover-platforms-q1`|[uri-validity](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#uri-validity)|All subject URI valid|[Jump](#pass-outcome-number-36)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-37">37/184</div>|:white_check_mark:Pass|`question-manufacturing-environments-discover-organization-q3`|[namespace-validity](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#namespace-validity)|No namespace typo|[Jump](#pass-outcome-number-37)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-38">38/184</div>|:white_check_mark:Pass|`question-manufacturing-environments-discover-organization-q3`|[query-type](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#query-type)|Accurate query type|[Jump](#pass-outcome-number-38)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-39">39/184</div>|:white_check_mark:Pass|`question-manufacturing-environments-discover-organization-q3`|[syntax](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#syntax)|Correct syntax|[Jump](#pass-outcome-number-39)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-40">40/184</div>|:white_check_mark:Pass|`question-manufacturing-environments-discover-organization-q3`|[uri-validity](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#uri-validity)|All subject URI valid|[Jump](#pass-outcome-number-40)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-41">41/184</div>|:white_check_mark:Pass|`question-manufacturing-environments-discover-organization-q2`|[namespace-validity](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#namespace-validity)|No namespace typo|[Jump](#pass-outcome-number-41)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-42">42/184</div>|:white_check_mark:Pass|`question-manufacturing-environments-discover-organization-q2`|[query-type](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#query-type)|Accurate query type|[Jump](#pass-outcome-number-42)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-43">43/184</div>|:white_check_mark:Pass|`question-manufacturing-environments-discover-organization-q2`|[syntax](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#syntax)|Correct syntax|[Jump](#pass-outcome-number-43)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-44">44/184</div>|:white_check_mark:Pass|`question-manufacturing-environments-discover-organization-q2`|[uri-validity](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#uri-validity)|All subject URI valid|[Jump](#pass-outcome-number-44)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-45">45/184</div>|:white_check_mark:Pass|`question-manufacturing-environments-discover-organization-q1`|[namespace-validity](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#namespace-validity)|No namespace typo|[Jump](#pass-outcome-number-45)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-46">46/184</div>|:white_check_mark:Pass|`question-manufacturing-environments-discover-organization-q1`|[query-type](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#query-type)|Accurate query type|[Jump](#pass-outcome-number-46)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-47">47/184</div>|:white_check_mark:Pass|`question-manufacturing-environments-discover-organization-q1`|[syntax](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#syntax)|Correct syntax|[Jump](#pass-outcome-number-47)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-48">48/184</div>|:white_check_mark:Pass|`question-manufacturing-environments-discover-organization-q1`|[uri-validity](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#uri-validity)|All subject URI valid|[Jump](#pass-outcome-number-48)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-49">49/184</div>|:white_check_mark:Pass|`question-manufacturing-environments-discover-core-q7`|[namespace-validity](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#namespace-validity)|No namespace typo|[Jump](#pass-outcome-number-49)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-50">50/184</div>|:white_check_mark:Pass|`question-manufacturing-environments-discover-core-q7`|[query-type](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#query-type)|Accurate query type|[Jump](#pass-outcome-number-50)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-51">51/184</div>|:white_check_mark:Pass|`question-manufacturing-environments-discover-core-q7`|[syntax](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#syntax)|Correct syntax|[Jump](#pass-outcome-number-51)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-52">52/184</div>|:white_check_mark:Pass|`question-manufacturing-environments-discover-core-q7`|[uri-validity](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#uri-validity)|All subject URI valid|[Jump](#pass-outcome-number-52)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-53">53/184</div>|:white_check_mark:Pass|`question-manufacturing-environments-discover-core-q5`|[namespace-validity](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#namespace-validity)|No namespace typo|[Jump](#pass-outcome-number-53)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-54">54/184</div>|:white_check_mark:Pass|`question-manufacturing-environments-discover-core-q5`|[query-type](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#query-type)|Accurate query type|[Jump](#pass-outcome-number-54)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-55">55/184</div>|:white_check_mark:Pass|`question-manufacturing-environments-discover-core-q5`|[syntax](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#syntax)|Correct syntax|[Jump](#pass-outcome-number-55)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-56">56/184</div>|:white_check_mark:Pass|`question-manufacturing-environments-discover-core-q5`|[uri-validity](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#uri-validity)|All subject URI valid|[Jump](#pass-outcome-number-56)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-57">57/184</div>|:white_check_mark:Pass|`question-manufacturing-environments-discover-core-q4`|[namespace-validity](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#namespace-validity)|No namespace typo|[Jump](#pass-outcome-number-57)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-58">58/184</div>|:white_check_mark:Pass|`question-manufacturing-environments-discover-core-q4`|[query-type](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#query-type)|Accurate query type|[Jump](#pass-outcome-number-58)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-59">59/184</div>|:white_check_mark:Pass|`question-manufacturing-environments-discover-core-q4`|[syntax](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#syntax)|Correct syntax|[Jump](#pass-outcome-number-59)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-60">60/184</div>|:white_check_mark:Pass|`question-manufacturing-environments-discover-core-q4`|[uri-validity](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#uri-validity)|All subject URI valid|[Jump](#pass-outcome-number-60)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-61">61/184</div>|:white_check_mark:Pass|`question-manufacturing-environments-discover-core-q3`|[namespace-validity](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#namespace-validity)|No namespace typo|[Jump](#pass-outcome-number-61)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-62">62/184</div>|:white_check_mark:Pass|`question-manufacturing-environments-discover-core-q3`|[query-type](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#query-type)|Accurate query type|[Jump](#pass-outcome-number-62)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-63">63/184</div>|:white_check_mark:Pass|`question-manufacturing-environments-discover-core-q3`|[syntax](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#syntax)|Correct syntax|[Jump](#pass-outcome-number-63)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-64">64/184</div>|:white_check_mark:Pass|`question-manufacturing-environments-discover-core-q3`|[uri-validity](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#uri-validity)|All subject URI valid|[Jump](#pass-outcome-number-64)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-65">65/184</div>|:white_check_mark:Pass|`question-manufacturing-environments-discover-core-q2`|[namespace-validity](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#namespace-validity)|No namespace typo|[Jump](#pass-outcome-number-65)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-66">66/184</div>|:white_check_mark:Pass|`question-manufacturing-environments-discover-core-q2`|[query-type](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#query-type)|Accurate query type|[Jump](#pass-outcome-number-66)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-67">67/184</div>|:white_check_mark:Pass|`question-manufacturing-environments-discover-core-q2`|[syntax](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#syntax)|Correct syntax|[Jump](#pass-outcome-number-67)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-68">68/184</div>|:white_check_mark:Pass|`question-manufacturing-environments-discover-core-q2`|[uri-validity](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#uri-validity)|All subject URI valid|[Jump](#pass-outcome-number-68)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-69">69/184</div>|:white_check_mark:Pass|`question-manufacturing-environments-discover-core-q1`|[namespace-validity](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#namespace-validity)|No namespace typo|[Jump](#pass-outcome-number-69)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-70">70/184</div>|:white_check_mark:Pass|`question-manufacturing-environments-discover-core-q1`|[query-type](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#query-type)|Accurate query type|[Jump](#pass-outcome-number-70)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-71">71/184</div>|:white_check_mark:Pass|`question-manufacturing-environments-discover-core-q1`|[syntax](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#syntax)|Correct syntax|[Jump](#pass-outcome-number-71)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-72">72/184</div>|:white_check_mark:Pass|`question-manufacturing-environments-discover-core-q1`|[uri-validity](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#uri-validity)|All subject URI valid|[Jump](#pass-outcome-number-72)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-73">73/184</div>|:white_check_mark:Pass|`question-manufacturing-environments-discover-behavior-specifications-q5`|[namespace-validity](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#namespace-validity)|No namespace typo|[Jump](#pass-outcome-number-73)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-74">74/184</div>|:white_check_mark:Pass|`question-manufacturing-environments-discover-behavior-specifications-q5`|[query-type](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#query-type)|Accurate query type|[Jump](#pass-outcome-number-74)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-75">75/184</div>|:white_check_mark:Pass|`question-manufacturing-environments-discover-behavior-specifications-q5`|[syntax](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#syntax)|Correct syntax|[Jump](#pass-outcome-number-75)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-76">76/184</div>|:white_check_mark:Pass|`question-manufacturing-environments-discover-behavior-specifications-q5`|[uri-validity](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#uri-validity)|All subject URI valid|[Jump](#pass-outcome-number-76)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-77">77/184</div>|:white_check_mark:Pass|`question-manufacturing-environments-discover-behavior-specifications-q4`|[namespace-validity](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#namespace-validity)|No namespace typo|[Jump](#pass-outcome-number-77)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-78">78/184</div>|:white_check_mark:Pass|`question-manufacturing-environments-discover-behavior-specifications-q4`|[query-type](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#query-type)|Accurate query type|[Jump](#pass-outcome-number-78)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-79">79/184</div>|:white_check_mark:Pass|`question-manufacturing-environments-discover-behavior-specifications-q4`|[syntax](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#syntax)|Correct syntax|[Jump](#pass-outcome-number-79)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-80">80/184</div>|:white_check_mark:Pass|`question-manufacturing-environments-discover-behavior-specifications-q4`|[uri-validity](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#uri-validity)|All subject URI valid|[Jump](#pass-outcome-number-80)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-81">81/184</div>|:white_check_mark:Pass|`question-manufacturing-environments-discover-behavior-specifications-q3`|[namespace-validity](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#namespace-validity)|No namespace typo|[Jump](#pass-outcome-number-81)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-82">82/184</div>|:white_check_mark:Pass|`question-manufacturing-environments-discover-behavior-specifications-q3`|[query-type](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#query-type)|Accurate query type|[Jump](#pass-outcome-number-82)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-83">83/184</div>|:white_check_mark:Pass|`question-manufacturing-environments-discover-behavior-specifications-q3`|[syntax](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#syntax)|Correct syntax|[Jump](#pass-outcome-number-83)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-84">84/184</div>|:white_check_mark:Pass|`question-manufacturing-environments-discover-behavior-specifications-q3`|[uri-validity](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#uri-validity)|All subject URI valid|[Jump](#pass-outcome-number-84)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-85">85/184</div>|:white_check_mark:Pass|`question-manufacturing-environments-discover-behavior-specifications-q2`|[namespace-validity](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#namespace-validity)|No namespace typo|[Jump](#pass-outcome-number-85)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-86">86/184</div>|:white_check_mark:Pass|`question-manufacturing-environments-discover-behavior-specifications-q2`|[query-type](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#query-type)|Accurate query type|[Jump](#pass-outcome-number-86)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-87">87/184</div>|:white_check_mark:Pass|`question-manufacturing-environments-discover-behavior-specifications-q2`|[syntax](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#syntax)|Correct syntax|[Jump](#pass-outcome-number-87)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-88">88/184</div>|:white_check_mark:Pass|`question-manufacturing-environments-discover-behavior-specifications-q2`|[uri-validity](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#uri-validity)|All subject URI valid|[Jump](#pass-outcome-number-88)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-89">89/184</div>|:white_check_mark:Pass|`question-manufacturing-environments-discover-behavior-specifications-q1`|[namespace-validity](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#namespace-validity)|No namespace typo|[Jump](#pass-outcome-number-89)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-90">90/184</div>|:white_check_mark:Pass|`question-manufacturing-environments-discover-behavior-specifications-q1`|[query-type](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#query-type)|Accurate query type|[Jump](#pass-outcome-number-90)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-91">91/184</div>|:white_check_mark:Pass|`question-manufacturing-environments-discover-behavior-specifications-q1`|[syntax](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#syntax)|Correct syntax|[Jump](#pass-outcome-number-91)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-92">92/184</div>|:white_check_mark:Pass|`question-manufacturing-environments-discover-behavior-specifications-q1`|[uri-validity](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#uri-validity)|All subject URI valid|[Jump](#pass-outcome-number-92)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-93">93/184</div>|:white_check_mark:Pass|`question-logistics-structure-organization-q6`|[namespace-validity](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#namespace-validity)|No namespace typo|[Jump](#pass-outcome-number-93)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-94">94/184</div>|:white_check_mark:Pass|`question-logistics-structure-organization-q6`|[query-type](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#query-type)|Accurate query type|[Jump](#pass-outcome-number-94)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-95">95/184</div>|:white_check_mark:Pass|`question-logistics-structure-organization-q6`|[syntax](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#syntax)|Correct syntax|[Jump](#pass-outcome-number-95)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-96">96/184</div>|:white_check_mark:Pass|`question-logistics-structure-organization-q6`|[uri-validity](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#uri-validity)|All subject URI valid|[Jump](#pass-outcome-number-96)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-97">97/184</div>|:white_check_mark:Pass|`question-logistics-structure-organization-q5`|[namespace-validity](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#namespace-validity)|No namespace typo|[Jump](#pass-outcome-number-97)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-98">98/184</div>|:white_check_mark:Pass|`question-logistics-structure-organization-q5`|[query-type](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#query-type)|Accurate query type|[Jump](#pass-outcome-number-98)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-99">99/184</div>|:white_check_mark:Pass|`question-logistics-structure-organization-q5`|[syntax](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#syntax)|Correct syntax|[Jump](#pass-outcome-number-99)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-100">100/184</div>|:white_check_mark:Pass|`question-logistics-structure-organization-q5`|[uri-validity](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#uri-validity)|All subject URI valid|[Jump](#pass-outcome-number-100)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-101">101/184</div>|:white_check_mark:Pass|`question-logistics-structure-organization-q4`|[namespace-validity](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#namespace-validity)|No namespace typo|[Jump](#pass-outcome-number-101)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-102">102/184</div>|:white_check_mark:Pass|`question-logistics-structure-organization-q4`|[query-type](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#query-type)|Accurate query type|[Jump](#pass-outcome-number-102)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-103">103/184</div>|:white_check_mark:Pass|`question-logistics-structure-organization-q4`|[syntax](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#syntax)|Correct syntax|[Jump](#pass-outcome-number-103)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-104">104/184</div>|:white_check_mark:Pass|`question-logistics-structure-organization-q4`|[uri-validity](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#uri-validity)|All subject URI valid|[Jump](#pass-outcome-number-104)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-105">105/184</div>|:white_check_mark:Pass|`question-logistics-structure-organization-q3`|[namespace-validity](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#namespace-validity)|No namespace typo|[Jump](#pass-outcome-number-105)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-106">106/184</div>|:white_check_mark:Pass|`question-logistics-structure-organization-q3`|[query-type](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#query-type)|Accurate query type|[Jump](#pass-outcome-number-106)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-107">107/184</div>|:white_check_mark:Pass|`question-logistics-structure-organization-q3`|[syntax](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#syntax)|Correct syntax|[Jump](#pass-outcome-number-107)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-108">108/184</div>|:white_check_mark:Pass|`question-logistics-structure-organization-q3`|[uri-validity](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#uri-validity)|All subject URI valid|[Jump](#pass-outcome-number-108)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-109">109/184</div>|:white_check_mark:Pass|`question-logistics-structure-organization-q2`|[namespace-validity](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#namespace-validity)|No namespace typo|[Jump](#pass-outcome-number-109)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-110">110/184</div>|:white_check_mark:Pass|`question-logistics-structure-organization-q2`|[query-type](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#query-type)|Accurate query type|[Jump](#pass-outcome-number-110)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-111">111/184</div>|:white_check_mark:Pass|`question-logistics-structure-organization-q2`|[syntax](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#syntax)|Correct syntax|[Jump](#pass-outcome-number-111)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-112">112/184</div>|:white_check_mark:Pass|`question-logistics-structure-organization-q2`|[uri-validity](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#uri-validity)|All subject URI valid|[Jump](#pass-outcome-number-112)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-113">113/184</div>|:white_check_mark:Pass|`question-logistics-structure-organization-q1`|[namespace-validity](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#namespace-validity)|No namespace typo|[Jump](#pass-outcome-number-113)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-114">114/184</div>|:white_check_mark:Pass|`question-logistics-structure-organization-q1`|[query-type](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#query-type)|Accurate query type|[Jump](#pass-outcome-number-114)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-115">115/184</div>|:white_check_mark:Pass|`question-logistics-structure-organization-q1`|[syntax](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#syntax)|Correct syntax|[Jump](#pass-outcome-number-115)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-116">116/184</div>|:white_check_mark:Pass|`question-logistics-structure-organization-q1`|[uri-validity](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#uri-validity)|All subject URI valid|[Jump](#pass-outcome-number-116)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-117">117/184</div>|:white_check_mark:Pass|`question-logistics-create-organization-q9`|[namespace-validity](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#namespace-validity)|No namespace typo|[Jump](#pass-outcome-number-117)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-118">118/184</div>|:white_check_mark:Pass|`question-logistics-create-organization-q9`|[query-type](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#query-type)|Accurate query type|[Jump](#pass-outcome-number-118)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-119">119/184</div>|:white_check_mark:Pass|`question-logistics-create-organization-q9`|[syntax](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#syntax)|Correct syntax|[Jump](#pass-outcome-number-119)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-120">120/184</div>|:white_check_mark:Pass|`question-logistics-create-organization-q9`|[uri-validity](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#uri-validity)|All subject URI valid|[Jump](#pass-outcome-number-120)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-121">121/184</div>|:white_check_mark:Pass|`question-logistics-create-organization-q8`|[namespace-validity](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#namespace-validity)|No namespace typo|[Jump](#pass-outcome-number-121)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-122">122/184</div>|:white_check_mark:Pass|`question-logistics-create-organization-q8`|[query-type](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#query-type)|Accurate query type|[Jump](#pass-outcome-number-122)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-123">123/184</div>|:white_check_mark:Pass|`question-logistics-create-organization-q8`|[syntax](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#syntax)|Correct syntax|[Jump](#pass-outcome-number-123)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-124">124/184</div>|:white_check_mark:Pass|`question-logistics-create-organization-q8`|[uri-validity](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#uri-validity)|All subject URI valid|[Jump](#pass-outcome-number-124)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-125">125/184</div>|:white_check_mark:Pass|`question-logistics-create-organization-q7`|[namespace-validity](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#namespace-validity)|No namespace typo|[Jump](#pass-outcome-number-125)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-126">126/184</div>|:white_check_mark:Pass|`question-logistics-create-organization-q7`|[query-type](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#query-type)|Accurate query type|[Jump](#pass-outcome-number-126)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-127">127/184</div>|:white_check_mark:Pass|`question-logistics-create-organization-q7`|[syntax](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#syntax)|Correct syntax|[Jump](#pass-outcome-number-127)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-128">128/184</div>|:white_check_mark:Pass|`question-logistics-create-organization-q7`|[uri-validity](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#uri-validity)|All subject URI valid|[Jump](#pass-outcome-number-128)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-129">129/184</div>|:white_check_mark:Pass|`question-logistics-create-organization-q6`|[namespace-validity](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#namespace-validity)|No namespace typo|[Jump](#pass-outcome-number-129)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-130">130/184</div>|:white_check_mark:Pass|`question-logistics-create-organization-q6`|[query-type](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#query-type)|Accurate query type|[Jump](#pass-outcome-number-130)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-131">131/184</div>|:white_check_mark:Pass|`question-logistics-create-organization-q6`|[syntax](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#syntax)|Correct syntax|[Jump](#pass-outcome-number-131)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-132">132/184</div>|:white_check_mark:Pass|`question-logistics-create-organization-q6`|[uri-validity](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#uri-validity)|All subject URI valid|[Jump](#pass-outcome-number-132)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-133">133/184</div>|:white_check_mark:Pass|`question-logistics-create-organization-q5`|[namespace-validity](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#namespace-validity)|No namespace typo|[Jump](#pass-outcome-number-133)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-134">134/184</div>|:white_check_mark:Pass|`question-logistics-create-organization-q5`|[query-type](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#query-type)|Accurate query type|[Jump](#pass-outcome-number-134)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-135">135/184</div>|:white_check_mark:Pass|`question-logistics-create-organization-q5`|[syntax](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#syntax)|Correct syntax|[Jump](#pass-outcome-number-135)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-136">136/184</div>|:white_check_mark:Pass|`question-logistics-create-organization-q5`|[uri-validity](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#uri-validity)|All subject URI valid|[Jump](#pass-outcome-number-136)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-137">137/184</div>|:white_check_mark:Pass|`question-logistics-create-organization-q4`|[namespace-validity](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#namespace-validity)|No namespace typo|[Jump](#pass-outcome-number-137)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-138">138/184</div>|:white_check_mark:Pass|`question-logistics-create-organization-q4`|[query-type](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#query-type)|Accurate query type|[Jump](#pass-outcome-number-138)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-139">139/184</div>|:white_check_mark:Pass|`question-logistics-create-organization-q4`|[syntax](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#syntax)|Correct syntax|[Jump](#pass-outcome-number-139)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-140">140/184</div>|:white_check_mark:Pass|`question-logistics-create-organization-q4`|[uri-validity](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#uri-validity)|All subject URI valid|[Jump](#pass-outcome-number-140)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-141">141/184</div>|:white_check_mark:Pass|`question-logistics-create-organization-q3`|[namespace-validity](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#namespace-validity)|No namespace typo|[Jump](#pass-outcome-number-141)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-142">142/184</div>|:white_check_mark:Pass|`question-logistics-create-organization-q3`|[query-type](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#query-type)|Accurate query type|[Jump](#pass-outcome-number-142)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-143">143/184</div>|:white_check_mark:Pass|`question-logistics-create-organization-q3`|[syntax](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#syntax)|Correct syntax|[Jump](#pass-outcome-number-143)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-144">144/184</div>|:white_check_mark:Pass|`question-logistics-create-organization-q3`|[uri-validity](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#uri-validity)|All subject URI valid|[Jump](#pass-outcome-number-144)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-145">145/184</div>|:white_check_mark:Pass|`question-logistics-create-organization-q2`|[namespace-validity](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#namespace-validity)|No namespace typo|[Jump](#pass-outcome-number-145)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-146">146/184</div>|:white_check_mark:Pass|`question-logistics-create-organization-q2`|[query-type](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#query-type)|Accurate query type|[Jump](#pass-outcome-number-146)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-147">147/184</div>|:white_check_mark:Pass|`question-logistics-create-organization-q2`|[syntax](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#syntax)|Correct syntax|[Jump](#pass-outcome-number-147)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-148">148/184</div>|:white_check_mark:Pass|`question-logistics-create-organization-q2`|[uri-validity](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#uri-validity)|All subject URI valid|[Jump](#pass-outcome-number-148)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-149">149/184</div>|:white_check_mark:Pass|`question-logistics-create-organization-q1`|[namespace-validity](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#namespace-validity)|No namespace typo|[Jump](#pass-outcome-number-149)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-150">150/184</div>|:white_check_mark:Pass|`question-logistics-create-organization-q1`|[query-type](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#query-type)|Accurate query type|[Jump](#pass-outcome-number-150)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-151">151/184</div>|:white_check_mark:Pass|`question-logistics-create-organization-q1`|[syntax](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#syntax)|Correct syntax|[Jump](#pass-outcome-number-151)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-152">152/184</div>|:white_check_mark:Pass|`question-logistics-create-organization-q1`|[uri-validity](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#uri-validity)|All subject URI valid|[Jump](#pass-outcome-number-152)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-153">153/184</div>|:white_check_mark:Pass|`question-logistics-coordinate-activities-q3`|[namespace-validity](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#namespace-validity)|No namespace typo|[Jump](#pass-outcome-number-153)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-154">154/184</div>|:white_check_mark:Pass|`question-logistics-coordinate-activities-q3`|[query-type](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#query-type)|Accurate query type|[Jump](#pass-outcome-number-154)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-155">155/184</div>|:white_check_mark:Pass|`question-logistics-coordinate-activities-q3`|[syntax](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#syntax)|Correct syntax|[Jump](#pass-outcome-number-155)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-156">156/184</div>|:white_check_mark:Pass|`question-logistics-coordinate-activities-q3`|[uri-validity](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#uri-validity)|All subject URI valid|[Jump](#pass-outcome-number-156)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-157">157/184</div>|:white_check_mark:Pass|`question-logistics-coordinate-activities-q2`|[namespace-validity](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#namespace-validity)|No namespace typo|[Jump](#pass-outcome-number-157)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-158">158/184</div>|:white_check_mark:Pass|`question-logistics-coordinate-activities-q2`|[query-type](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#query-type)|Accurate query type|[Jump](#pass-outcome-number-158)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-159">159/184</div>|:white_check_mark:Pass|`question-logistics-coordinate-activities-q2`|[syntax](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#syntax)|Correct syntax|[Jump](#pass-outcome-number-159)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-160">160/184</div>|:white_check_mark:Pass|`question-logistics-coordinate-activities-q2`|[uri-validity](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#uri-validity)|All subject URI valid|[Jump](#pass-outcome-number-160)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-161">161/184</div>|:white_check_mark:Pass|`question-logistics-coordinate-activities-q1`|[namespace-validity](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#namespace-validity)|No namespace typo|[Jump](#pass-outcome-number-161)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-162">162/184</div>|:white_check_mark:Pass|`question-logistics-coordinate-activities-q1`|[query-type](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#query-type)|Accurate query type|[Jump](#pass-outcome-number-162)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-163">163/184</div>|:white_check_mark:Pass|`question-logistics-coordinate-activities-q1`|[syntax](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#syntax)|Correct syntax|[Jump](#pass-outcome-number-163)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-164">164/184</div>|:white_check_mark:Pass|`question-logistics-coordinate-activities-q1`|[uri-validity](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#uri-validity)|All subject URI valid|[Jump](#pass-outcome-number-164)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-165">165/184</div>|:white_check_mark:Pass|`question-logistics-configure-organization-q4`|[namespace-validity](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#namespace-validity)|No namespace typo|[Jump](#pass-outcome-number-165)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-166">166/184</div>|:white_check_mark:Pass|`question-logistics-configure-organization-q4`|[query-type](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#query-type)|Accurate query type|[Jump](#pass-outcome-number-166)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-167">167/184</div>|:white_check_mark:Pass|`question-logistics-configure-organization-q4`|[syntax](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#syntax)|Correct syntax|[Jump](#pass-outcome-number-167)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-168">168/184</div>|:white_check_mark:Pass|`question-logistics-configure-organization-q4`|[uri-validity](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#uri-validity)|All subject URI valid|[Jump](#pass-outcome-number-168)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-169">169/184</div>|:white_check_mark:Pass|`question-logistics-configure-organization-q3`|[namespace-validity](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#namespace-validity)|No namespace typo|[Jump](#pass-outcome-number-169)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-170">170/184</div>|:white_check_mark:Pass|`question-logistics-configure-organization-q3`|[query-type](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#query-type)|Accurate query type|[Jump](#pass-outcome-number-170)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-171">171/184</div>|:white_check_mark:Pass|`question-logistics-configure-organization-q3`|[syntax](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#syntax)|Correct syntax|[Jump](#pass-outcome-number-171)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-172">172/184</div>|:white_check_mark:Pass|`question-logistics-configure-organization-q3`|[uri-validity](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#uri-validity)|All subject URI valid|[Jump](#pass-outcome-number-172)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-173">173/184</div>|:white_check_mark:Pass|`question-logistics-configure-organization-q2`|[namespace-validity](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#namespace-validity)|No namespace typo|[Jump](#pass-outcome-number-173)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-174">174/184</div>|:white_check_mark:Pass|`question-logistics-configure-organization-q2`|[query-type](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#query-type)|Accurate query type|[Jump](#pass-outcome-number-174)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-175">175/184</div>|:white_check_mark:Pass|`question-logistics-configure-organization-q2`|[syntax](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#syntax)|Correct syntax|[Jump](#pass-outcome-number-175)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-176">176/184</div>|:white_check_mark:Pass|`question-logistics-configure-organization-q2`|[uri-validity](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#uri-validity)|All subject URI valid|[Jump](#pass-outcome-number-176)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-177">177/184</div>|:white_check_mark:Pass|`question-logistics-configure-organization-q1`|[namespace-validity](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#namespace-validity)|No namespace typo|[Jump](#pass-outcome-number-177)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-178">178/184</div>|:white_check_mark:Pass|`question-logistics-configure-organization-q1`|[query-type](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#query-type)|Accurate query type|[Jump](#pass-outcome-number-178)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-179">179/184</div>|:white_check_mark:Pass|`question-logistics-configure-organization-q1`|[syntax](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#syntax)|Correct syntax|[Jump](#pass-outcome-number-179)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-180">180/184</div>|:white_check_mark:Pass|`question-logistics-configure-organization-q1`|[uri-validity](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#uri-validity)|All subject URI valid|[Jump](#pass-outcome-number-180)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-181">181/184</div>|:white_check_mark:Pass|`question-domain-template-scenario-template-q1`|[namespace-validity](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#namespace-validity)|No namespace typo|[Jump](#pass-outcome-number-181)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-182">182/184</div>|:white_check_mark:Pass|`question-domain-template-scenario-template-q1`|[query-type](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#query-type)|Accurate query type|[Jump](#pass-outcome-number-182)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-183">183/184</div>|:white_check_mark:Pass|`question-domain-template-scenario-template-q1`|[syntax](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#syntax)|Correct syntax|[Jump](#pass-outcome-number-183)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-184">184/184</div>|:white_check_mark:Pass|`question-domain-template-scenario-template-q1`|[uri-validity](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#uri-validity)|All subject URI valid|[Jump](#pass-outcome-number-184)|

***

## Pass Outcomes Details

This subchapter gives more details to the :white_check_mark:Pass outcomes

### Pass Outcome number 1

[Jump to summary definition](#summary-Pass-1)	|	Previous Pass outcome	|	[Next Pass outcome](#pass-outcome-number-2)

:white_check_mark:Pass outcome
#### Subject detail
|Name|question-manufacturing-environments-safety-rules-4|
|----|----|
|Title|competency&#32;question&#32;domains/manufacturing-environments/safety-rules/4.rq&#32;from&#32;branch&#32;main|
|Composition|- [Competency question manufacturing-environments/safety-rules/4](https://github.com/HyperAgents/hmas/blob/main/domains/manufacturing-environments/safety-rules/4.rq.ttl)|

#### Criterion detail
|Identifier|[query-type](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#query-type)|
|----|----|
|Title|Query&#32;type&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;check&#32;if&#32;the&#32;query&#32;is&#32;indeed&#32;of&#32;type&#32;Select&#32;or&#32;Ask|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-1)|Identifier|`wrong-query-type`|
|[Section top](#pass-outcome-number-1)|Title|Accurate&#32;query&#32;type|
|[Section top](#pass-outcome-number-1)|Description|The&#32;query&#32;is&#32;of&#32;type&#32;Select&#32;or&#32;Ask|

***
### Pass Outcome number 2

[Jump to summary definition](#summary-Pass-2)	|	[Previous Pass outcome](#pass-outcome-number-1)	|	[Next Pass outcome](#pass-outcome-number-3)

:white_check_mark:Pass outcome
#### Subject detail
|Name|question-manufacturing-environments-safety-rules-4|
|----|----|
|Title|competency&#32;question&#32;domains/manufacturing-environments/safety-rules/4.rq&#32;from&#32;branch&#32;main|
|Composition|- [Competency question manufacturing-environments/safety-rules/4](https://github.com/HyperAgents/hmas/blob/main/domains/manufacturing-environments/safety-rules/4.rq.ttl)|

#### Criterion detail
|Identifier|[syntax](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#syntax)|
|----|----|
|Title|Syntax&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;check&#32;wether&#32;the&#32;test&#32;subject&#32;is&#32;syntaxically&#32;correct&#32;or&#32;not.|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-2)|Identifier|`syntax-error`|
|[Section top](#pass-outcome-number-2)|Title|Correct&#32;syntax|
|[Section top](#pass-outcome-number-2)|Description|Test&#32;subject&#32;has&#32;a&#32;correct&#32;syntax|

***
### Pass Outcome number 3

[Jump to summary definition](#summary-Pass-3)	|	[Previous Pass outcome](#pass-outcome-number-2)	|	[Next Pass outcome](#pass-outcome-number-4)

:white_check_mark:Pass outcome
#### Subject detail
|Name|question-manufacturing-environments-safety-rules-3|
|----|----|
|Title|competency&#32;question&#32;domains/manufacturing-environments/safety-rules/3.rq&#32;from&#32;branch&#32;main|
|Composition|- [Competency question manufacturing-environments/safety-rules/3](https://github.com/HyperAgents/hmas/blob/main/domains/manufacturing-environments/safety-rules/3.rq.ttl)|

#### Criterion detail
|Identifier|[query-type](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#query-type)|
|----|----|
|Title|Query&#32;type&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;check&#32;if&#32;the&#32;query&#32;is&#32;indeed&#32;of&#32;type&#32;Select&#32;or&#32;Ask|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-3)|Identifier|`wrong-query-type`|
|[Section top](#pass-outcome-number-3)|Title|Accurate&#32;query&#32;type|
|[Section top](#pass-outcome-number-3)|Description|The&#32;query&#32;is&#32;of&#32;type&#32;Select&#32;or&#32;Ask|

***
### Pass Outcome number 4

[Jump to summary definition](#summary-Pass-4)	|	[Previous Pass outcome](#pass-outcome-number-3)	|	[Next Pass outcome](#pass-outcome-number-5)

:white_check_mark:Pass outcome
#### Subject detail
|Name|question-manufacturing-environments-safety-rules-3|
|----|----|
|Title|competency&#32;question&#32;domains/manufacturing-environments/safety-rules/3.rq&#32;from&#32;branch&#32;main|
|Composition|- [Competency question manufacturing-environments/safety-rules/3](https://github.com/HyperAgents/hmas/blob/main/domains/manufacturing-environments/safety-rules/3.rq.ttl)|

#### Criterion detail
|Identifier|[syntax](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#syntax)|
|----|----|
|Title|Syntax&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;check&#32;wether&#32;the&#32;test&#32;subject&#32;is&#32;syntaxically&#32;correct&#32;or&#32;not.|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-4)|Identifier|`syntax-error`|
|[Section top](#pass-outcome-number-4)|Title|Correct&#32;syntax|
|[Section top](#pass-outcome-number-4)|Description|Test&#32;subject&#32;has&#32;a&#32;correct&#32;syntax|

***
### Pass Outcome number 5

[Jump to summary definition](#summary-Pass-5)	|	[Previous Pass outcome](#pass-outcome-number-4)	|	[Next Pass outcome](#pass-outcome-number-6)

:white_check_mark:Pass outcome
#### Subject detail
|Name|question-manufacturing-environments-safety-rules-2|
|----|----|
|Title|competency&#32;question&#32;domains/manufacturing-environments/safety-rules/2.rq&#32;from&#32;branch&#32;main|
|Composition|- [Competency question manufacturing-environments/safety-rules/2](https://github.com/HyperAgents/hmas/blob/main/domains/manufacturing-environments/safety-rules/2.rq.ttl)|

#### Criterion detail
|Identifier|[query-type](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#query-type)|
|----|----|
|Title|Query&#32;type&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;check&#32;if&#32;the&#32;query&#32;is&#32;indeed&#32;of&#32;type&#32;Select&#32;or&#32;Ask|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-5)|Identifier|`wrong-query-type`|
|[Section top](#pass-outcome-number-5)|Title|Accurate&#32;query&#32;type|
|[Section top](#pass-outcome-number-5)|Description|The&#32;query&#32;is&#32;of&#32;type&#32;Select&#32;or&#32;Ask|

***
### Pass Outcome number 6

[Jump to summary definition](#summary-Pass-6)	|	[Previous Pass outcome](#pass-outcome-number-5)	|	[Next Pass outcome](#pass-outcome-number-7)

:white_check_mark:Pass outcome
#### Subject detail
|Name|question-manufacturing-environments-safety-rules-2|
|----|----|
|Title|competency&#32;question&#32;domains/manufacturing-environments/safety-rules/2.rq&#32;from&#32;branch&#32;main|
|Composition|- [Competency question manufacturing-environments/safety-rules/2](https://github.com/HyperAgents/hmas/blob/main/domains/manufacturing-environments/safety-rules/2.rq.ttl)|

#### Criterion detail
|Identifier|[syntax](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#syntax)|
|----|----|
|Title|Syntax&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;check&#32;wether&#32;the&#32;test&#32;subject&#32;is&#32;syntaxically&#32;correct&#32;or&#32;not.|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-6)|Identifier|`syntax-error`|
|[Section top](#pass-outcome-number-6)|Title|Correct&#32;syntax|
|[Section top](#pass-outcome-number-6)|Description|Test&#32;subject&#32;has&#32;a&#32;correct&#32;syntax|

***
### Pass Outcome number 7

[Jump to summary definition](#summary-Pass-7)	|	[Previous Pass outcome](#pass-outcome-number-6)	|	[Next Pass outcome](#pass-outcome-number-8)

:white_check_mark:Pass outcome
#### Subject detail
|Name|question-manufacturing-environments-safety-rules-1|
|----|----|
|Title|competency&#32;question&#32;domains/manufacturing-environments/safety-rules/1.rq&#32;from&#32;branch&#32;main|
|Composition|- [Competency question manufacturing-environments/safety-rules/1](https://github.com/HyperAgents/hmas/blob/main/domains/manufacturing-environments/safety-rules/1.rq.ttl)|

#### Criterion detail
|Identifier|[query-type](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#query-type)|
|----|----|
|Title|Query&#32;type&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;check&#32;if&#32;the&#32;query&#32;is&#32;indeed&#32;of&#32;type&#32;Select&#32;or&#32;Ask|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-7)|Identifier|`wrong-query-type`|
|[Section top](#pass-outcome-number-7)|Title|Accurate&#32;query&#32;type|
|[Section top](#pass-outcome-number-7)|Description|The&#32;query&#32;is&#32;of&#32;type&#32;Select&#32;or&#32;Ask|

***
### Pass Outcome number 8

[Jump to summary definition](#summary-Pass-8)	|	[Previous Pass outcome](#pass-outcome-number-7)	|	[Next Pass outcome](#pass-outcome-number-9)

:white_check_mark:Pass outcome
#### Subject detail
|Name|question-manufacturing-environments-safety-rules-1|
|----|----|
|Title|competency&#32;question&#32;domains/manufacturing-environments/safety-rules/1.rq&#32;from&#32;branch&#32;main|
|Composition|- [Competency question manufacturing-environments/safety-rules/1](https://github.com/HyperAgents/hmas/blob/main/domains/manufacturing-environments/safety-rules/1.rq.ttl)|

#### Criterion detail
|Identifier|[syntax](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#syntax)|
|----|----|
|Title|Syntax&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;check&#32;wether&#32;the&#32;test&#32;subject&#32;is&#32;syntaxically&#32;correct&#32;or&#32;not.|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-8)|Identifier|`syntax-error`|
|[Section top](#pass-outcome-number-8)|Title|Correct&#32;syntax|
|[Section top](#pass-outcome-number-8)|Description|Test&#32;subject&#32;has&#32;a&#32;correct&#32;syntax|

***
### Pass Outcome number 9

[Jump to summary definition](#summary-Pass-9)	|	[Previous Pass outcome](#pass-outcome-number-8)	|	[Next Pass outcome](#pass-outcome-number-10)

:white_check_mark:Pass outcome
#### Subject detail
|Name|question-manufacturing-environments-discover-signifiers-q3|
|----|----|
|Title|competency&#32;question&#32;domains/manufacturing-environments/discover-signifiers/q3.rq&#32;from&#32;branch&#32;main|
|Composition|- [Competency question manufacturing-environments/discover-signifiers/q3](https://github.com/HyperAgents/hmas/blob/main/domains/manufacturing-environments/discover-signifiers/q3.rq.ttl)|

#### Criterion detail
|Identifier|[namespace-validity](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#namespace-validity)|
|----|----|
|Title|Prefix&#32;validity&#32;test|
|Description|A&#32;test&#32;case&#32;checking&#32;if&#32;all&#32;the&#32;prefixes&#32;are&#32;not&#32;too&#32;close&#32;from&#32;the&#32;most&#32;used&#32;existing&#32;namespaces&#32;(according&#32;to&#32;prefix&#32;cc)&#32;or&#32;an&#32;ontology&#32;namespace|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-9)|Identifier|`namespace-typo`|
|[Section top](#pass-outcome-number-9)|Title|No&#32;namespace&#32;typo|
|[Section top](#pass-outcome-number-9)|Description|It&#32;seems&#32;that&#32;none&#32;of&#32;the&#32;subject&#32;URIs&#32;have&#32;namespaces&#32;typos|

***
### Pass Outcome number 10

[Jump to summary definition](#summary-Pass-10)	|	[Previous Pass outcome](#pass-outcome-number-9)	|	[Next Pass outcome](#pass-outcome-number-11)

:white_check_mark:Pass outcome
#### Subject detail
|Name|question-manufacturing-environments-discover-signifiers-q3|
|----|----|
|Title|competency&#32;question&#32;domains/manufacturing-environments/discover-signifiers/q3.rq&#32;from&#32;branch&#32;main|
|Composition|- [Competency question manufacturing-environments/discover-signifiers/q3](https://github.com/HyperAgents/hmas/blob/main/domains/manufacturing-environments/discover-signifiers/q3.rq.ttl)|

#### Criterion detail
|Identifier|[query-type](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#query-type)|
|----|----|
|Title|Query&#32;type&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;check&#32;if&#32;the&#32;query&#32;is&#32;indeed&#32;of&#32;type&#32;Select&#32;or&#32;Ask|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-10)|Identifier|`wrong-query-type`|
|[Section top](#pass-outcome-number-10)|Title|Accurate&#32;query&#32;type|
|[Section top](#pass-outcome-number-10)|Description|The&#32;query&#32;is&#32;of&#32;type&#32;Select&#32;or&#32;Ask|

***
### Pass Outcome number 11

[Jump to summary definition](#summary-Pass-11)	|	[Previous Pass outcome](#pass-outcome-number-10)	|	[Next Pass outcome](#pass-outcome-number-12)

:white_check_mark:Pass outcome
#### Subject detail
|Name|question-manufacturing-environments-discover-signifiers-q3|
|----|----|
|Title|competency&#32;question&#32;domains/manufacturing-environments/discover-signifiers/q3.rq&#32;from&#32;branch&#32;main|
|Composition|- [Competency question manufacturing-environments/discover-signifiers/q3](https://github.com/HyperAgents/hmas/blob/main/domains/manufacturing-environments/discover-signifiers/q3.rq.ttl)|

#### Criterion detail
|Identifier|[syntax](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#syntax)|
|----|----|
|Title|Syntax&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;check&#32;wether&#32;the&#32;test&#32;subject&#32;is&#32;syntaxically&#32;correct&#32;or&#32;not.|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-11)|Identifier|`syntax-error`|
|[Section top](#pass-outcome-number-11)|Title|Correct&#32;syntax|
|[Section top](#pass-outcome-number-11)|Description|Test&#32;subject&#32;has&#32;a&#32;correct&#32;syntax|

***
### Pass Outcome number 12

[Jump to summary definition](#summary-Pass-12)	|	[Previous Pass outcome](#pass-outcome-number-11)	|	[Next Pass outcome](#pass-outcome-number-13)

:white_check_mark:Pass outcome
#### Subject detail
|Name|question-manufacturing-environments-discover-signifiers-q3|
|----|----|
|Title|competency&#32;question&#32;domains/manufacturing-environments/discover-signifiers/q3.rq&#32;from&#32;branch&#32;main|
|Composition|- [Competency question manufacturing-environments/discover-signifiers/q3](https://github.com/HyperAgents/hmas/blob/main/domains/manufacturing-environments/discover-signifiers/q3.rq.ttl)|

#### Criterion detail
|Identifier|[uri-validity](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#uri-validity)|
|----|----|
|Title|URI&#32;validity&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;check&#32;if&#32;all&#32;the&#32;URIs&#32;of&#32;the&#32;resource&#32;are&#32;well-formed|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-12)|Identifier|`invalid-uri`|
|[Section top](#pass-outcome-number-12)|Title|All&#32;subject&#32;URI&#32;valid|
|[Section top](#pass-outcome-number-12)|Description|All&#32;the&#32;URIs&#32;of&#32;the&#32;subject&#32;are&#32;valid|

***
### Pass Outcome number 13

[Jump to summary definition](#summary-Pass-13)	|	[Previous Pass outcome](#pass-outcome-number-12)	|	[Next Pass outcome](#pass-outcome-number-14)

:white_check_mark:Pass outcome
#### Subject detail
|Name|question-manufacturing-environments-discover-signifiers-q2|
|----|----|
|Title|competency&#32;question&#32;domains/manufacturing-environments/discover-signifiers/q2.rq&#32;from&#32;branch&#32;main|
|Composition|- [Competency question manufacturing-environments/discover-signifiers/q2](https://github.com/HyperAgents/hmas/blob/main/domains/manufacturing-environments/discover-signifiers/q2.rq.ttl)|

#### Criterion detail
|Identifier|[namespace-validity](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#namespace-validity)|
|----|----|
|Title|Prefix&#32;validity&#32;test|
|Description|A&#32;test&#32;case&#32;checking&#32;if&#32;all&#32;the&#32;prefixes&#32;are&#32;not&#32;too&#32;close&#32;from&#32;the&#32;most&#32;used&#32;existing&#32;namespaces&#32;(according&#32;to&#32;prefix&#32;cc)&#32;or&#32;an&#32;ontology&#32;namespace|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-13)|Identifier|`namespace-typo`|
|[Section top](#pass-outcome-number-13)|Title|No&#32;namespace&#32;typo|
|[Section top](#pass-outcome-number-13)|Description|It&#32;seems&#32;that&#32;none&#32;of&#32;the&#32;subject&#32;URIs&#32;have&#32;namespaces&#32;typos|

***
### Pass Outcome number 14

[Jump to summary definition](#summary-Pass-14)	|	[Previous Pass outcome](#pass-outcome-number-13)	|	[Next Pass outcome](#pass-outcome-number-15)

:white_check_mark:Pass outcome
#### Subject detail
|Name|question-manufacturing-environments-discover-signifiers-q2|
|----|----|
|Title|competency&#32;question&#32;domains/manufacturing-environments/discover-signifiers/q2.rq&#32;from&#32;branch&#32;main|
|Composition|- [Competency question manufacturing-environments/discover-signifiers/q2](https://github.com/HyperAgents/hmas/blob/main/domains/manufacturing-environments/discover-signifiers/q2.rq.ttl)|

#### Criterion detail
|Identifier|[query-type](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#query-type)|
|----|----|
|Title|Query&#32;type&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;check&#32;if&#32;the&#32;query&#32;is&#32;indeed&#32;of&#32;type&#32;Select&#32;or&#32;Ask|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-14)|Identifier|`wrong-query-type`|
|[Section top](#pass-outcome-number-14)|Title|Accurate&#32;query&#32;type|
|[Section top](#pass-outcome-number-14)|Description|The&#32;query&#32;is&#32;of&#32;type&#32;Select&#32;or&#32;Ask|

***
### Pass Outcome number 15

[Jump to summary definition](#summary-Pass-15)	|	[Previous Pass outcome](#pass-outcome-number-14)	|	[Next Pass outcome](#pass-outcome-number-16)

:white_check_mark:Pass outcome
#### Subject detail
|Name|question-manufacturing-environments-discover-signifiers-q2|
|----|----|
|Title|competency&#32;question&#32;domains/manufacturing-environments/discover-signifiers/q2.rq&#32;from&#32;branch&#32;main|
|Composition|- [Competency question manufacturing-environments/discover-signifiers/q2](https://github.com/HyperAgents/hmas/blob/main/domains/manufacturing-environments/discover-signifiers/q2.rq.ttl)|

#### Criterion detail
|Identifier|[syntax](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#syntax)|
|----|----|
|Title|Syntax&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;check&#32;wether&#32;the&#32;test&#32;subject&#32;is&#32;syntaxically&#32;correct&#32;or&#32;not.|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-15)|Identifier|`syntax-error`|
|[Section top](#pass-outcome-number-15)|Title|Correct&#32;syntax|
|[Section top](#pass-outcome-number-15)|Description|Test&#32;subject&#32;has&#32;a&#32;correct&#32;syntax|

***
### Pass Outcome number 16

[Jump to summary definition](#summary-Pass-16)	|	[Previous Pass outcome](#pass-outcome-number-15)	|	[Next Pass outcome](#pass-outcome-number-17)

:white_check_mark:Pass outcome
#### Subject detail
|Name|question-manufacturing-environments-discover-signifiers-q2|
|----|----|
|Title|competency&#32;question&#32;domains/manufacturing-environments/discover-signifiers/q2.rq&#32;from&#32;branch&#32;main|
|Composition|- [Competency question manufacturing-environments/discover-signifiers/q2](https://github.com/HyperAgents/hmas/blob/main/domains/manufacturing-environments/discover-signifiers/q2.rq.ttl)|

#### Criterion detail
|Identifier|[uri-validity](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#uri-validity)|
|----|----|
|Title|URI&#32;validity&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;check&#32;if&#32;all&#32;the&#32;URIs&#32;of&#32;the&#32;resource&#32;are&#32;well-formed|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-16)|Identifier|`invalid-uri`|
|[Section top](#pass-outcome-number-16)|Title|All&#32;subject&#32;URI&#32;valid|
|[Section top](#pass-outcome-number-16)|Description|All&#32;the&#32;URIs&#32;of&#32;the&#32;subject&#32;are&#32;valid|

***
### Pass Outcome number 17

[Jump to summary definition](#summary-Pass-17)	|	[Previous Pass outcome](#pass-outcome-number-16)	|	[Next Pass outcome](#pass-outcome-number-18)

:white_check_mark:Pass outcome
#### Subject detail
|Name|question-manufacturing-environments-discover-signifiers-q1|
|----|----|
|Title|competency&#32;question&#32;domains/manufacturing-environments/discover-signifiers/q1.rq&#32;from&#32;branch&#32;main|
|Composition|- [Competency question manufacturing-environments/discover-signifiers/q1](https://github.com/HyperAgents/hmas/blob/main/domains/manufacturing-environments/discover-signifiers/q1.rq.ttl)|

#### Criterion detail
|Identifier|[namespace-validity](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#namespace-validity)|
|----|----|
|Title|Prefix&#32;validity&#32;test|
|Description|A&#32;test&#32;case&#32;checking&#32;if&#32;all&#32;the&#32;prefixes&#32;are&#32;not&#32;too&#32;close&#32;from&#32;the&#32;most&#32;used&#32;existing&#32;namespaces&#32;(according&#32;to&#32;prefix&#32;cc)&#32;or&#32;an&#32;ontology&#32;namespace|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-17)|Identifier|`namespace-typo`|
|[Section top](#pass-outcome-number-17)|Title|No&#32;namespace&#32;typo|
|[Section top](#pass-outcome-number-17)|Description|It&#32;seems&#32;that&#32;none&#32;of&#32;the&#32;subject&#32;URIs&#32;have&#32;namespaces&#32;typos|

***
### Pass Outcome number 18

[Jump to summary definition](#summary-Pass-18)	|	[Previous Pass outcome](#pass-outcome-number-17)	|	[Next Pass outcome](#pass-outcome-number-19)

:white_check_mark:Pass outcome
#### Subject detail
|Name|question-manufacturing-environments-discover-signifiers-q1|
|----|----|
|Title|competency&#32;question&#32;domains/manufacturing-environments/discover-signifiers/q1.rq&#32;from&#32;branch&#32;main|
|Composition|- [Competency question manufacturing-environments/discover-signifiers/q1](https://github.com/HyperAgents/hmas/blob/main/domains/manufacturing-environments/discover-signifiers/q1.rq.ttl)|

#### Criterion detail
|Identifier|[query-type](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#query-type)|
|----|----|
|Title|Query&#32;type&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;check&#32;if&#32;the&#32;query&#32;is&#32;indeed&#32;of&#32;type&#32;Select&#32;or&#32;Ask|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-18)|Identifier|`wrong-query-type`|
|[Section top](#pass-outcome-number-18)|Title|Accurate&#32;query&#32;type|
|[Section top](#pass-outcome-number-18)|Description|The&#32;query&#32;is&#32;of&#32;type&#32;Select&#32;or&#32;Ask|

***
### Pass Outcome number 19

[Jump to summary definition](#summary-Pass-19)	|	[Previous Pass outcome](#pass-outcome-number-18)	|	[Next Pass outcome](#pass-outcome-number-20)

:white_check_mark:Pass outcome
#### Subject detail
|Name|question-manufacturing-environments-discover-signifiers-q1|
|----|----|
|Title|competency&#32;question&#32;domains/manufacturing-environments/discover-signifiers/q1.rq&#32;from&#32;branch&#32;main|
|Composition|- [Competency question manufacturing-environments/discover-signifiers/q1](https://github.com/HyperAgents/hmas/blob/main/domains/manufacturing-environments/discover-signifiers/q1.rq.ttl)|

#### Criterion detail
|Identifier|[syntax](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#syntax)|
|----|----|
|Title|Syntax&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;check&#32;wether&#32;the&#32;test&#32;subject&#32;is&#32;syntaxically&#32;correct&#32;or&#32;not.|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-19)|Identifier|`syntax-error`|
|[Section top](#pass-outcome-number-19)|Title|Correct&#32;syntax|
|[Section top](#pass-outcome-number-19)|Description|Test&#32;subject&#32;has&#32;a&#32;correct&#32;syntax|

***
### Pass Outcome number 20

[Jump to summary definition](#summary-Pass-20)	|	[Previous Pass outcome](#pass-outcome-number-19)	|	[Next Pass outcome](#pass-outcome-number-21)

:white_check_mark:Pass outcome
#### Subject detail
|Name|question-manufacturing-environments-discover-signifiers-q1|
|----|----|
|Title|competency&#32;question&#32;domains/manufacturing-environments/discover-signifiers/q1.rq&#32;from&#32;branch&#32;main|
|Composition|- [Competency question manufacturing-environments/discover-signifiers/q1](https://github.com/HyperAgents/hmas/blob/main/domains/manufacturing-environments/discover-signifiers/q1.rq.ttl)|

#### Criterion detail
|Identifier|[uri-validity](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#uri-validity)|
|----|----|
|Title|URI&#32;validity&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;check&#32;if&#32;all&#32;the&#32;URIs&#32;of&#32;the&#32;resource&#32;are&#32;well-formed|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-20)|Identifier|`invalid-uri`|
|[Section top](#pass-outcome-number-20)|Title|All&#32;subject&#32;URI&#32;valid|
|[Section top](#pass-outcome-number-20)|Description|All&#32;the&#32;URIs&#32;of&#32;the&#32;subject&#32;are&#32;valid|

***
### Pass Outcome number 21

[Jump to summary definition](#summary-Pass-21)	|	[Previous Pass outcome](#pass-outcome-number-20)	|	[Next Pass outcome](#pass-outcome-number-22)

:white_check_mark:Pass outcome
#### Subject detail
|Name|question-manufacturing-environments-discover-platforms-q4|
|----|----|
|Title|competency&#32;question&#32;domains/manufacturing-environments/discover-platforms/q4.rq&#32;from&#32;branch&#32;main|
|Composition|- [Competency question manufacturing-environments/discover-platforms/q4](https://github.com/HyperAgents/hmas/blob/main/domains/manufacturing-environments/discover-platforms/q4.rq.ttl)|

#### Criterion detail
|Identifier|[namespace-validity](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#namespace-validity)|
|----|----|
|Title|Prefix&#32;validity&#32;test|
|Description|A&#32;test&#32;case&#32;checking&#32;if&#32;all&#32;the&#32;prefixes&#32;are&#32;not&#32;too&#32;close&#32;from&#32;the&#32;most&#32;used&#32;existing&#32;namespaces&#32;(according&#32;to&#32;prefix&#32;cc)&#32;or&#32;an&#32;ontology&#32;namespace|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-21)|Identifier|`namespace-typo`|
|[Section top](#pass-outcome-number-21)|Title|No&#32;namespace&#32;typo|
|[Section top](#pass-outcome-number-21)|Description|It&#32;seems&#32;that&#32;none&#32;of&#32;the&#32;subject&#32;URIs&#32;have&#32;namespaces&#32;typos|

***
### Pass Outcome number 22

[Jump to summary definition](#summary-Pass-22)	|	[Previous Pass outcome](#pass-outcome-number-21)	|	[Next Pass outcome](#pass-outcome-number-23)

:white_check_mark:Pass outcome
#### Subject detail
|Name|question-manufacturing-environments-discover-platforms-q4|
|----|----|
|Title|competency&#32;question&#32;domains/manufacturing-environments/discover-platforms/q4.rq&#32;from&#32;branch&#32;main|
|Composition|- [Competency question manufacturing-environments/discover-platforms/q4](https://github.com/HyperAgents/hmas/blob/main/domains/manufacturing-environments/discover-platforms/q4.rq.ttl)|

#### Criterion detail
|Identifier|[query-type](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#query-type)|
|----|----|
|Title|Query&#32;type&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;check&#32;if&#32;the&#32;query&#32;is&#32;indeed&#32;of&#32;type&#32;Select&#32;or&#32;Ask|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-22)|Identifier|`wrong-query-type`|
|[Section top](#pass-outcome-number-22)|Title|Accurate&#32;query&#32;type|
|[Section top](#pass-outcome-number-22)|Description|The&#32;query&#32;is&#32;of&#32;type&#32;Select&#32;or&#32;Ask|

***
### Pass Outcome number 23

[Jump to summary definition](#summary-Pass-23)	|	[Previous Pass outcome](#pass-outcome-number-22)	|	[Next Pass outcome](#pass-outcome-number-24)

:white_check_mark:Pass outcome
#### Subject detail
|Name|question-manufacturing-environments-discover-platforms-q4|
|----|----|
|Title|competency&#32;question&#32;domains/manufacturing-environments/discover-platforms/q4.rq&#32;from&#32;branch&#32;main|
|Composition|- [Competency question manufacturing-environments/discover-platforms/q4](https://github.com/HyperAgents/hmas/blob/main/domains/manufacturing-environments/discover-platforms/q4.rq.ttl)|

#### Criterion detail
|Identifier|[syntax](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#syntax)|
|----|----|
|Title|Syntax&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;check&#32;wether&#32;the&#32;test&#32;subject&#32;is&#32;syntaxically&#32;correct&#32;or&#32;not.|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-23)|Identifier|`syntax-error`|
|[Section top](#pass-outcome-number-23)|Title|Correct&#32;syntax|
|[Section top](#pass-outcome-number-23)|Description|Test&#32;subject&#32;has&#32;a&#32;correct&#32;syntax|

***
### Pass Outcome number 24

[Jump to summary definition](#summary-Pass-24)	|	[Previous Pass outcome](#pass-outcome-number-23)	|	[Next Pass outcome](#pass-outcome-number-25)

:white_check_mark:Pass outcome
#### Subject detail
|Name|question-manufacturing-environments-discover-platforms-q4|
|----|----|
|Title|competency&#32;question&#32;domains/manufacturing-environments/discover-platforms/q4.rq&#32;from&#32;branch&#32;main|
|Composition|- [Competency question manufacturing-environments/discover-platforms/q4](https://github.com/HyperAgents/hmas/blob/main/domains/manufacturing-environments/discover-platforms/q4.rq.ttl)|

#### Criterion detail
|Identifier|[uri-validity](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#uri-validity)|
|----|----|
|Title|URI&#32;validity&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;check&#32;if&#32;all&#32;the&#32;URIs&#32;of&#32;the&#32;resource&#32;are&#32;well-formed|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-24)|Identifier|`invalid-uri`|
|[Section top](#pass-outcome-number-24)|Title|All&#32;subject&#32;URI&#32;valid|
|[Section top](#pass-outcome-number-24)|Description|All&#32;the&#32;URIs&#32;of&#32;the&#32;subject&#32;are&#32;valid|

***
### Pass Outcome number 25

[Jump to summary definition](#summary-Pass-25)	|	[Previous Pass outcome](#pass-outcome-number-24)	|	[Next Pass outcome](#pass-outcome-number-26)

:white_check_mark:Pass outcome
#### Subject detail
|Name|question-manufacturing-environments-discover-platforms-q3|
|----|----|
|Title|competency&#32;question&#32;domains/manufacturing-environments/discover-platforms/q3.rq&#32;from&#32;branch&#32;main|
|Composition|- [Competency question manufacturing-environments/discover-platforms/q3](https://github.com/HyperAgents/hmas/blob/main/domains/manufacturing-environments/discover-platforms/q3.rq.ttl)|

#### Criterion detail
|Identifier|[namespace-validity](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#namespace-validity)|
|----|----|
|Title|Prefix&#32;validity&#32;test|
|Description|A&#32;test&#32;case&#32;checking&#32;if&#32;all&#32;the&#32;prefixes&#32;are&#32;not&#32;too&#32;close&#32;from&#32;the&#32;most&#32;used&#32;existing&#32;namespaces&#32;(according&#32;to&#32;prefix&#32;cc)&#32;or&#32;an&#32;ontology&#32;namespace|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-25)|Identifier|`namespace-typo`|
|[Section top](#pass-outcome-number-25)|Title|No&#32;namespace&#32;typo|
|[Section top](#pass-outcome-number-25)|Description|It&#32;seems&#32;that&#32;none&#32;of&#32;the&#32;subject&#32;URIs&#32;have&#32;namespaces&#32;typos|

***
### Pass Outcome number 26

[Jump to summary definition](#summary-Pass-26)	|	[Previous Pass outcome](#pass-outcome-number-25)	|	[Next Pass outcome](#pass-outcome-number-27)

:white_check_mark:Pass outcome
#### Subject detail
|Name|question-manufacturing-environments-discover-platforms-q3|
|----|----|
|Title|competency&#32;question&#32;domains/manufacturing-environments/discover-platforms/q3.rq&#32;from&#32;branch&#32;main|
|Composition|- [Competency question manufacturing-environments/discover-platforms/q3](https://github.com/HyperAgents/hmas/blob/main/domains/manufacturing-environments/discover-platforms/q3.rq.ttl)|

#### Criterion detail
|Identifier|[query-type](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#query-type)|
|----|----|
|Title|Query&#32;type&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;check&#32;if&#32;the&#32;query&#32;is&#32;indeed&#32;of&#32;type&#32;Select&#32;or&#32;Ask|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-26)|Identifier|`wrong-query-type`|
|[Section top](#pass-outcome-number-26)|Title|Accurate&#32;query&#32;type|
|[Section top](#pass-outcome-number-26)|Description|The&#32;query&#32;is&#32;of&#32;type&#32;Select&#32;or&#32;Ask|

***
### Pass Outcome number 27

[Jump to summary definition](#summary-Pass-27)	|	[Previous Pass outcome](#pass-outcome-number-26)	|	[Next Pass outcome](#pass-outcome-number-28)

:white_check_mark:Pass outcome
#### Subject detail
|Name|question-manufacturing-environments-discover-platforms-q3|
|----|----|
|Title|competency&#32;question&#32;domains/manufacturing-environments/discover-platforms/q3.rq&#32;from&#32;branch&#32;main|
|Composition|- [Competency question manufacturing-environments/discover-platforms/q3](https://github.com/HyperAgents/hmas/blob/main/domains/manufacturing-environments/discover-platforms/q3.rq.ttl)|

#### Criterion detail
|Identifier|[syntax](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#syntax)|
|----|----|
|Title|Syntax&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;check&#32;wether&#32;the&#32;test&#32;subject&#32;is&#32;syntaxically&#32;correct&#32;or&#32;not.|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-27)|Identifier|`syntax-error`|
|[Section top](#pass-outcome-number-27)|Title|Correct&#32;syntax|
|[Section top](#pass-outcome-number-27)|Description|Test&#32;subject&#32;has&#32;a&#32;correct&#32;syntax|

***
### Pass Outcome number 28

[Jump to summary definition](#summary-Pass-28)	|	[Previous Pass outcome](#pass-outcome-number-27)	|	[Next Pass outcome](#pass-outcome-number-29)

:white_check_mark:Pass outcome
#### Subject detail
|Name|question-manufacturing-environments-discover-platforms-q3|
|----|----|
|Title|competency&#32;question&#32;domains/manufacturing-environments/discover-platforms/q3.rq&#32;from&#32;branch&#32;main|
|Composition|- [Competency question manufacturing-environments/discover-platforms/q3](https://github.com/HyperAgents/hmas/blob/main/domains/manufacturing-environments/discover-platforms/q3.rq.ttl)|

#### Criterion detail
|Identifier|[uri-validity](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#uri-validity)|
|----|----|
|Title|URI&#32;validity&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;check&#32;if&#32;all&#32;the&#32;URIs&#32;of&#32;the&#32;resource&#32;are&#32;well-formed|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-28)|Identifier|`invalid-uri`|
|[Section top](#pass-outcome-number-28)|Title|All&#32;subject&#32;URI&#32;valid|
|[Section top](#pass-outcome-number-28)|Description|All&#32;the&#32;URIs&#32;of&#32;the&#32;subject&#32;are&#32;valid|

***
### Pass Outcome number 29

[Jump to summary definition](#summary-Pass-29)	|	[Previous Pass outcome](#pass-outcome-number-28)	|	[Next Pass outcome](#pass-outcome-number-30)

:white_check_mark:Pass outcome
#### Subject detail
|Name|question-manufacturing-environments-discover-platforms-q2|
|----|----|
|Title|competency&#32;question&#32;domains/manufacturing-environments/discover-platforms/q2.rq&#32;from&#32;branch&#32;main|
|Composition|- [Competency question manufacturing-environments/discover-platforms/q2](https://github.com/HyperAgents/hmas/blob/main/domains/manufacturing-environments/discover-platforms/q2.rq.ttl)|

#### Criterion detail
|Identifier|[namespace-validity](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#namespace-validity)|
|----|----|
|Title|Prefix&#32;validity&#32;test|
|Description|A&#32;test&#32;case&#32;checking&#32;if&#32;all&#32;the&#32;prefixes&#32;are&#32;not&#32;too&#32;close&#32;from&#32;the&#32;most&#32;used&#32;existing&#32;namespaces&#32;(according&#32;to&#32;prefix&#32;cc)&#32;or&#32;an&#32;ontology&#32;namespace|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-29)|Identifier|`namespace-typo`|
|[Section top](#pass-outcome-number-29)|Title|No&#32;namespace&#32;typo|
|[Section top](#pass-outcome-number-29)|Description|It&#32;seems&#32;that&#32;none&#32;of&#32;the&#32;subject&#32;URIs&#32;have&#32;namespaces&#32;typos|

***
### Pass Outcome number 30

[Jump to summary definition](#summary-Pass-30)	|	[Previous Pass outcome](#pass-outcome-number-29)	|	[Next Pass outcome](#pass-outcome-number-31)

:white_check_mark:Pass outcome
#### Subject detail
|Name|question-manufacturing-environments-discover-platforms-q2|
|----|----|
|Title|competency&#32;question&#32;domains/manufacturing-environments/discover-platforms/q2.rq&#32;from&#32;branch&#32;main|
|Composition|- [Competency question manufacturing-environments/discover-platforms/q2](https://github.com/HyperAgents/hmas/blob/main/domains/manufacturing-environments/discover-platforms/q2.rq.ttl)|

#### Criterion detail
|Identifier|[query-type](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#query-type)|
|----|----|
|Title|Query&#32;type&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;check&#32;if&#32;the&#32;query&#32;is&#32;indeed&#32;of&#32;type&#32;Select&#32;or&#32;Ask|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-30)|Identifier|`wrong-query-type`|
|[Section top](#pass-outcome-number-30)|Title|Accurate&#32;query&#32;type|
|[Section top](#pass-outcome-number-30)|Description|The&#32;query&#32;is&#32;of&#32;type&#32;Select&#32;or&#32;Ask|

***
### Pass Outcome number 31

[Jump to summary definition](#summary-Pass-31)	|	[Previous Pass outcome](#pass-outcome-number-30)	|	[Next Pass outcome](#pass-outcome-number-32)

:white_check_mark:Pass outcome
#### Subject detail
|Name|question-manufacturing-environments-discover-platforms-q2|
|----|----|
|Title|competency&#32;question&#32;domains/manufacturing-environments/discover-platforms/q2.rq&#32;from&#32;branch&#32;main|
|Composition|- [Competency question manufacturing-environments/discover-platforms/q2](https://github.com/HyperAgents/hmas/blob/main/domains/manufacturing-environments/discover-platforms/q2.rq.ttl)|

#### Criterion detail
|Identifier|[syntax](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#syntax)|
|----|----|
|Title|Syntax&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;check&#32;wether&#32;the&#32;test&#32;subject&#32;is&#32;syntaxically&#32;correct&#32;or&#32;not.|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-31)|Identifier|`syntax-error`|
|[Section top](#pass-outcome-number-31)|Title|Correct&#32;syntax|
|[Section top](#pass-outcome-number-31)|Description|Test&#32;subject&#32;has&#32;a&#32;correct&#32;syntax|

***
### Pass Outcome number 32

[Jump to summary definition](#summary-Pass-32)	|	[Previous Pass outcome](#pass-outcome-number-31)	|	[Next Pass outcome](#pass-outcome-number-33)

:white_check_mark:Pass outcome
#### Subject detail
|Name|question-manufacturing-environments-discover-platforms-q2|
|----|----|
|Title|competency&#32;question&#32;domains/manufacturing-environments/discover-platforms/q2.rq&#32;from&#32;branch&#32;main|
|Composition|- [Competency question manufacturing-environments/discover-platforms/q2](https://github.com/HyperAgents/hmas/blob/main/domains/manufacturing-environments/discover-platforms/q2.rq.ttl)|

#### Criterion detail
|Identifier|[uri-validity](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#uri-validity)|
|----|----|
|Title|URI&#32;validity&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;check&#32;if&#32;all&#32;the&#32;URIs&#32;of&#32;the&#32;resource&#32;are&#32;well-formed|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-32)|Identifier|`invalid-uri`|
|[Section top](#pass-outcome-number-32)|Title|All&#32;subject&#32;URI&#32;valid|
|[Section top](#pass-outcome-number-32)|Description|All&#32;the&#32;URIs&#32;of&#32;the&#32;subject&#32;are&#32;valid|

***
### Pass Outcome number 33

[Jump to summary definition](#summary-Pass-33)	|	[Previous Pass outcome](#pass-outcome-number-32)	|	[Next Pass outcome](#pass-outcome-number-34)

:white_check_mark:Pass outcome
#### Subject detail
|Name|question-manufacturing-environments-discover-platforms-q1|
|----|----|
|Title|competency&#32;question&#32;domains/manufacturing-environments/discover-platforms/q1.rq&#32;from&#32;branch&#32;main|
|Composition|- [Competency question manufacturing-environments/discover-platforms/q1](https://github.com/HyperAgents/hmas/blob/main/domains/manufacturing-environments/discover-platforms/q1.rq.ttl)|

#### Criterion detail
|Identifier|[namespace-validity](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#namespace-validity)|
|----|----|
|Title|Prefix&#32;validity&#32;test|
|Description|A&#32;test&#32;case&#32;checking&#32;if&#32;all&#32;the&#32;prefixes&#32;are&#32;not&#32;too&#32;close&#32;from&#32;the&#32;most&#32;used&#32;existing&#32;namespaces&#32;(according&#32;to&#32;prefix&#32;cc)&#32;or&#32;an&#32;ontology&#32;namespace|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-33)|Identifier|`namespace-typo`|
|[Section top](#pass-outcome-number-33)|Title|No&#32;namespace&#32;typo|
|[Section top](#pass-outcome-number-33)|Description|It&#32;seems&#32;that&#32;none&#32;of&#32;the&#32;subject&#32;URIs&#32;have&#32;namespaces&#32;typos|

***
### Pass Outcome number 34

[Jump to summary definition](#summary-Pass-34)	|	[Previous Pass outcome](#pass-outcome-number-33)	|	[Next Pass outcome](#pass-outcome-number-35)

:white_check_mark:Pass outcome
#### Subject detail
|Name|question-manufacturing-environments-discover-platforms-q1|
|----|----|
|Title|competency&#32;question&#32;domains/manufacturing-environments/discover-platforms/q1.rq&#32;from&#32;branch&#32;main|
|Composition|- [Competency question manufacturing-environments/discover-platforms/q1](https://github.com/HyperAgents/hmas/blob/main/domains/manufacturing-environments/discover-platforms/q1.rq.ttl)|

#### Criterion detail
|Identifier|[query-type](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#query-type)|
|----|----|
|Title|Query&#32;type&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;check&#32;if&#32;the&#32;query&#32;is&#32;indeed&#32;of&#32;type&#32;Select&#32;or&#32;Ask|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-34)|Identifier|`wrong-query-type`|
|[Section top](#pass-outcome-number-34)|Title|Accurate&#32;query&#32;type|
|[Section top](#pass-outcome-number-34)|Description|The&#32;query&#32;is&#32;of&#32;type&#32;Select&#32;or&#32;Ask|

***
### Pass Outcome number 35

[Jump to summary definition](#summary-Pass-35)	|	[Previous Pass outcome](#pass-outcome-number-34)	|	[Next Pass outcome](#pass-outcome-number-36)

:white_check_mark:Pass outcome
#### Subject detail
|Name|question-manufacturing-environments-discover-platforms-q1|
|----|----|
|Title|competency&#32;question&#32;domains/manufacturing-environments/discover-platforms/q1.rq&#32;from&#32;branch&#32;main|
|Composition|- [Competency question manufacturing-environments/discover-platforms/q1](https://github.com/HyperAgents/hmas/blob/main/domains/manufacturing-environments/discover-platforms/q1.rq.ttl)|

#### Criterion detail
|Identifier|[syntax](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#syntax)|
|----|----|
|Title|Syntax&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;check&#32;wether&#32;the&#32;test&#32;subject&#32;is&#32;syntaxically&#32;correct&#32;or&#32;not.|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-35)|Identifier|`syntax-error`|
|[Section top](#pass-outcome-number-35)|Title|Correct&#32;syntax|
|[Section top](#pass-outcome-number-35)|Description|Test&#32;subject&#32;has&#32;a&#32;correct&#32;syntax|

***
### Pass Outcome number 36

[Jump to summary definition](#summary-Pass-36)	|	[Previous Pass outcome](#pass-outcome-number-35)	|	[Next Pass outcome](#pass-outcome-number-37)

:white_check_mark:Pass outcome
#### Subject detail
|Name|question-manufacturing-environments-discover-platforms-q1|
|----|----|
|Title|competency&#32;question&#32;domains/manufacturing-environments/discover-platforms/q1.rq&#32;from&#32;branch&#32;main|
|Composition|- [Competency question manufacturing-environments/discover-platforms/q1](https://github.com/HyperAgents/hmas/blob/main/domains/manufacturing-environments/discover-platforms/q1.rq.ttl)|

#### Criterion detail
|Identifier|[uri-validity](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#uri-validity)|
|----|----|
|Title|URI&#32;validity&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;check&#32;if&#32;all&#32;the&#32;URIs&#32;of&#32;the&#32;resource&#32;are&#32;well-formed|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-36)|Identifier|`invalid-uri`|
|[Section top](#pass-outcome-number-36)|Title|All&#32;subject&#32;URI&#32;valid|
|[Section top](#pass-outcome-number-36)|Description|All&#32;the&#32;URIs&#32;of&#32;the&#32;subject&#32;are&#32;valid|

***
### Pass Outcome number 37

[Jump to summary definition](#summary-Pass-37)	|	[Previous Pass outcome](#pass-outcome-number-36)	|	[Next Pass outcome](#pass-outcome-number-38)

:white_check_mark:Pass outcome
#### Subject detail
|Name|question-manufacturing-environments-discover-organization-q3|
|----|----|
|Title|competency&#32;question&#32;domains/manufacturing-environments/discover-organization/q3.rq&#32;from&#32;branch&#32;main|
|Composition|- [Competency question manufacturing-environments/discover-organization/q3](https://github.com/HyperAgents/hmas/blob/main/domains/manufacturing-environments/discover-organization/q3.rq.ttl)|

#### Criterion detail
|Identifier|[namespace-validity](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#namespace-validity)|
|----|----|
|Title|Prefix&#32;validity&#32;test|
|Description|A&#32;test&#32;case&#32;checking&#32;if&#32;all&#32;the&#32;prefixes&#32;are&#32;not&#32;too&#32;close&#32;from&#32;the&#32;most&#32;used&#32;existing&#32;namespaces&#32;(according&#32;to&#32;prefix&#32;cc)&#32;or&#32;an&#32;ontology&#32;namespace|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-37)|Identifier|`namespace-typo`|
|[Section top](#pass-outcome-number-37)|Title|No&#32;namespace&#32;typo|
|[Section top](#pass-outcome-number-37)|Description|It&#32;seems&#32;that&#32;none&#32;of&#32;the&#32;subject&#32;URIs&#32;have&#32;namespaces&#32;typos|

***
### Pass Outcome number 38

[Jump to summary definition](#summary-Pass-38)	|	[Previous Pass outcome](#pass-outcome-number-37)	|	[Next Pass outcome](#pass-outcome-number-39)

:white_check_mark:Pass outcome
#### Subject detail
|Name|question-manufacturing-environments-discover-organization-q3|
|----|----|
|Title|competency&#32;question&#32;domains/manufacturing-environments/discover-organization/q3.rq&#32;from&#32;branch&#32;main|
|Composition|- [Competency question manufacturing-environments/discover-organization/q3](https://github.com/HyperAgents/hmas/blob/main/domains/manufacturing-environments/discover-organization/q3.rq.ttl)|

#### Criterion detail
|Identifier|[query-type](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#query-type)|
|----|----|
|Title|Query&#32;type&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;check&#32;if&#32;the&#32;query&#32;is&#32;indeed&#32;of&#32;type&#32;Select&#32;or&#32;Ask|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-38)|Identifier|`wrong-query-type`|
|[Section top](#pass-outcome-number-38)|Title|Accurate&#32;query&#32;type|
|[Section top](#pass-outcome-number-38)|Description|The&#32;query&#32;is&#32;of&#32;type&#32;Select&#32;or&#32;Ask|

***
### Pass Outcome number 39

[Jump to summary definition](#summary-Pass-39)	|	[Previous Pass outcome](#pass-outcome-number-38)	|	[Next Pass outcome](#pass-outcome-number-40)

:white_check_mark:Pass outcome
#### Subject detail
|Name|question-manufacturing-environments-discover-organization-q3|
|----|----|
|Title|competency&#32;question&#32;domains/manufacturing-environments/discover-organization/q3.rq&#32;from&#32;branch&#32;main|
|Composition|- [Competency question manufacturing-environments/discover-organization/q3](https://github.com/HyperAgents/hmas/blob/main/domains/manufacturing-environments/discover-organization/q3.rq.ttl)|

#### Criterion detail
|Identifier|[syntax](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#syntax)|
|----|----|
|Title|Syntax&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;check&#32;wether&#32;the&#32;test&#32;subject&#32;is&#32;syntaxically&#32;correct&#32;or&#32;not.|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-39)|Identifier|`syntax-error`|
|[Section top](#pass-outcome-number-39)|Title|Correct&#32;syntax|
|[Section top](#pass-outcome-number-39)|Description|Test&#32;subject&#32;has&#32;a&#32;correct&#32;syntax|

***
### Pass Outcome number 40

[Jump to summary definition](#summary-Pass-40)	|	[Previous Pass outcome](#pass-outcome-number-39)	|	[Next Pass outcome](#pass-outcome-number-41)

:white_check_mark:Pass outcome
#### Subject detail
|Name|question-manufacturing-environments-discover-organization-q3|
|----|----|
|Title|competency&#32;question&#32;domains/manufacturing-environments/discover-organization/q3.rq&#32;from&#32;branch&#32;main|
|Composition|- [Competency question manufacturing-environments/discover-organization/q3](https://github.com/HyperAgents/hmas/blob/main/domains/manufacturing-environments/discover-organization/q3.rq.ttl)|

#### Criterion detail
|Identifier|[uri-validity](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#uri-validity)|
|----|----|
|Title|URI&#32;validity&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;check&#32;if&#32;all&#32;the&#32;URIs&#32;of&#32;the&#32;resource&#32;are&#32;well-formed|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-40)|Identifier|`invalid-uri`|
|[Section top](#pass-outcome-number-40)|Title|All&#32;subject&#32;URI&#32;valid|
|[Section top](#pass-outcome-number-40)|Description|All&#32;the&#32;URIs&#32;of&#32;the&#32;subject&#32;are&#32;valid|

***
### Pass Outcome number 41

[Jump to summary definition](#summary-Pass-41)	|	[Previous Pass outcome](#pass-outcome-number-40)	|	[Next Pass outcome](#pass-outcome-number-42)

:white_check_mark:Pass outcome
#### Subject detail
|Name|question-manufacturing-environments-discover-organization-q2|
|----|----|
|Title|competency&#32;question&#32;domains/manufacturing-environments/discover-organization/q2.rq&#32;from&#32;branch&#32;main|
|Composition|- [Competency question manufacturing-environments/discover-organization/q2](https://github.com/HyperAgents/hmas/blob/main/domains/manufacturing-environments/discover-organization/q2.rq.ttl)|

#### Criterion detail
|Identifier|[namespace-validity](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#namespace-validity)|
|----|----|
|Title|Prefix&#32;validity&#32;test|
|Description|A&#32;test&#32;case&#32;checking&#32;if&#32;all&#32;the&#32;prefixes&#32;are&#32;not&#32;too&#32;close&#32;from&#32;the&#32;most&#32;used&#32;existing&#32;namespaces&#32;(according&#32;to&#32;prefix&#32;cc)&#32;or&#32;an&#32;ontology&#32;namespace|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-41)|Identifier|`namespace-typo`|
|[Section top](#pass-outcome-number-41)|Title|No&#32;namespace&#32;typo|
|[Section top](#pass-outcome-number-41)|Description|It&#32;seems&#32;that&#32;none&#32;of&#32;the&#32;subject&#32;URIs&#32;have&#32;namespaces&#32;typos|

***
### Pass Outcome number 42

[Jump to summary definition](#summary-Pass-42)	|	[Previous Pass outcome](#pass-outcome-number-41)	|	[Next Pass outcome](#pass-outcome-number-43)

:white_check_mark:Pass outcome
#### Subject detail
|Name|question-manufacturing-environments-discover-organization-q2|
|----|----|
|Title|competency&#32;question&#32;domains/manufacturing-environments/discover-organization/q2.rq&#32;from&#32;branch&#32;main|
|Composition|- [Competency question manufacturing-environments/discover-organization/q2](https://github.com/HyperAgents/hmas/blob/main/domains/manufacturing-environments/discover-organization/q2.rq.ttl)|

#### Criterion detail
|Identifier|[query-type](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#query-type)|
|----|----|
|Title|Query&#32;type&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;check&#32;if&#32;the&#32;query&#32;is&#32;indeed&#32;of&#32;type&#32;Select&#32;or&#32;Ask|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-42)|Identifier|`wrong-query-type`|
|[Section top](#pass-outcome-number-42)|Title|Accurate&#32;query&#32;type|
|[Section top](#pass-outcome-number-42)|Description|The&#32;query&#32;is&#32;of&#32;type&#32;Select&#32;or&#32;Ask|

***
### Pass Outcome number 43

[Jump to summary definition](#summary-Pass-43)	|	[Previous Pass outcome](#pass-outcome-number-42)	|	[Next Pass outcome](#pass-outcome-number-44)

:white_check_mark:Pass outcome
#### Subject detail
|Name|question-manufacturing-environments-discover-organization-q2|
|----|----|
|Title|competency&#32;question&#32;domains/manufacturing-environments/discover-organization/q2.rq&#32;from&#32;branch&#32;main|
|Composition|- [Competency question manufacturing-environments/discover-organization/q2](https://github.com/HyperAgents/hmas/blob/main/domains/manufacturing-environments/discover-organization/q2.rq.ttl)|

#### Criterion detail
|Identifier|[syntax](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#syntax)|
|----|----|
|Title|Syntax&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;check&#32;wether&#32;the&#32;test&#32;subject&#32;is&#32;syntaxically&#32;correct&#32;or&#32;not.|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-43)|Identifier|`syntax-error`|
|[Section top](#pass-outcome-number-43)|Title|Correct&#32;syntax|
|[Section top](#pass-outcome-number-43)|Description|Test&#32;subject&#32;has&#32;a&#32;correct&#32;syntax|

***
### Pass Outcome number 44

[Jump to summary definition](#summary-Pass-44)	|	[Previous Pass outcome](#pass-outcome-number-43)	|	[Next Pass outcome](#pass-outcome-number-45)

:white_check_mark:Pass outcome
#### Subject detail
|Name|question-manufacturing-environments-discover-organization-q2|
|----|----|
|Title|competency&#32;question&#32;domains/manufacturing-environments/discover-organization/q2.rq&#32;from&#32;branch&#32;main|
|Composition|- [Competency question manufacturing-environments/discover-organization/q2](https://github.com/HyperAgents/hmas/blob/main/domains/manufacturing-environments/discover-organization/q2.rq.ttl)|

#### Criterion detail
|Identifier|[uri-validity](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#uri-validity)|
|----|----|
|Title|URI&#32;validity&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;check&#32;if&#32;all&#32;the&#32;URIs&#32;of&#32;the&#32;resource&#32;are&#32;well-formed|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-44)|Identifier|`invalid-uri`|
|[Section top](#pass-outcome-number-44)|Title|All&#32;subject&#32;URI&#32;valid|
|[Section top](#pass-outcome-number-44)|Description|All&#32;the&#32;URIs&#32;of&#32;the&#32;subject&#32;are&#32;valid|

***
### Pass Outcome number 45

[Jump to summary definition](#summary-Pass-45)	|	[Previous Pass outcome](#pass-outcome-number-44)	|	[Next Pass outcome](#pass-outcome-number-46)

:white_check_mark:Pass outcome
#### Subject detail
|Name|question-manufacturing-environments-discover-organization-q1|
|----|----|
|Title|competency&#32;question&#32;domains/manufacturing-environments/discover-organization/q1.rq&#32;from&#32;branch&#32;main|
|Composition|- [Competency question manufacturing-environments/discover-organization/q1](https://github.com/HyperAgents/hmas/blob/main/domains/manufacturing-environments/discover-organization/q1.rq.ttl)|

#### Criterion detail
|Identifier|[namespace-validity](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#namespace-validity)|
|----|----|
|Title|Prefix&#32;validity&#32;test|
|Description|A&#32;test&#32;case&#32;checking&#32;if&#32;all&#32;the&#32;prefixes&#32;are&#32;not&#32;too&#32;close&#32;from&#32;the&#32;most&#32;used&#32;existing&#32;namespaces&#32;(according&#32;to&#32;prefix&#32;cc)&#32;or&#32;an&#32;ontology&#32;namespace|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-45)|Identifier|`namespace-typo`|
|[Section top](#pass-outcome-number-45)|Title|No&#32;namespace&#32;typo|
|[Section top](#pass-outcome-number-45)|Description|It&#32;seems&#32;that&#32;none&#32;of&#32;the&#32;subject&#32;URIs&#32;have&#32;namespaces&#32;typos|

***
### Pass Outcome number 46

[Jump to summary definition](#summary-Pass-46)	|	[Previous Pass outcome](#pass-outcome-number-45)	|	[Next Pass outcome](#pass-outcome-number-47)

:white_check_mark:Pass outcome
#### Subject detail
|Name|question-manufacturing-environments-discover-organization-q1|
|----|----|
|Title|competency&#32;question&#32;domains/manufacturing-environments/discover-organization/q1.rq&#32;from&#32;branch&#32;main|
|Composition|- [Competency question manufacturing-environments/discover-organization/q1](https://github.com/HyperAgents/hmas/blob/main/domains/manufacturing-environments/discover-organization/q1.rq.ttl)|

#### Criterion detail
|Identifier|[query-type](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#query-type)|
|----|----|
|Title|Query&#32;type&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;check&#32;if&#32;the&#32;query&#32;is&#32;indeed&#32;of&#32;type&#32;Select&#32;or&#32;Ask|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-46)|Identifier|`wrong-query-type`|
|[Section top](#pass-outcome-number-46)|Title|Accurate&#32;query&#32;type|
|[Section top](#pass-outcome-number-46)|Description|The&#32;query&#32;is&#32;of&#32;type&#32;Select&#32;or&#32;Ask|

***
### Pass Outcome number 47

[Jump to summary definition](#summary-Pass-47)	|	[Previous Pass outcome](#pass-outcome-number-46)	|	[Next Pass outcome](#pass-outcome-number-48)

:white_check_mark:Pass outcome
#### Subject detail
|Name|question-manufacturing-environments-discover-organization-q1|
|----|----|
|Title|competency&#32;question&#32;domains/manufacturing-environments/discover-organization/q1.rq&#32;from&#32;branch&#32;main|
|Composition|- [Competency question manufacturing-environments/discover-organization/q1](https://github.com/HyperAgents/hmas/blob/main/domains/manufacturing-environments/discover-organization/q1.rq.ttl)|

#### Criterion detail
|Identifier|[syntax](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#syntax)|
|----|----|
|Title|Syntax&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;check&#32;wether&#32;the&#32;test&#32;subject&#32;is&#32;syntaxically&#32;correct&#32;or&#32;not.|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-47)|Identifier|`syntax-error`|
|[Section top](#pass-outcome-number-47)|Title|Correct&#32;syntax|
|[Section top](#pass-outcome-number-47)|Description|Test&#32;subject&#32;has&#32;a&#32;correct&#32;syntax|

***
### Pass Outcome number 48

[Jump to summary definition](#summary-Pass-48)	|	[Previous Pass outcome](#pass-outcome-number-47)	|	[Next Pass outcome](#pass-outcome-number-49)

:white_check_mark:Pass outcome
#### Subject detail
|Name|question-manufacturing-environments-discover-organization-q1|
|----|----|
|Title|competency&#32;question&#32;domains/manufacturing-environments/discover-organization/q1.rq&#32;from&#32;branch&#32;main|
|Composition|- [Competency question manufacturing-environments/discover-organization/q1](https://github.com/HyperAgents/hmas/blob/main/domains/manufacturing-environments/discover-organization/q1.rq.ttl)|

#### Criterion detail
|Identifier|[uri-validity](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#uri-validity)|
|----|----|
|Title|URI&#32;validity&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;check&#32;if&#32;all&#32;the&#32;URIs&#32;of&#32;the&#32;resource&#32;are&#32;well-formed|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-48)|Identifier|`invalid-uri`|
|[Section top](#pass-outcome-number-48)|Title|All&#32;subject&#32;URI&#32;valid|
|[Section top](#pass-outcome-number-48)|Description|All&#32;the&#32;URIs&#32;of&#32;the&#32;subject&#32;are&#32;valid|

***
### Pass Outcome number 49

[Jump to summary definition](#summary-Pass-49)	|	[Previous Pass outcome](#pass-outcome-number-48)	|	[Next Pass outcome](#pass-outcome-number-50)

:white_check_mark:Pass outcome
#### Subject detail
|Name|question-manufacturing-environments-discover-core-q7|
|----|----|
|Title|competency&#32;question&#32;domains/manufacturing-environments/discover-core/q7.rq&#32;from&#32;branch&#32;main|
|Composition|- [Competency question manufacturing-environments/discover-core/q7](https://github.com/HyperAgents/hmas/blob/main/domains/manufacturing-environments/discover-core/q7.rq.ttl)|

#### Criterion detail
|Identifier|[namespace-validity](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#namespace-validity)|
|----|----|
|Title|Prefix&#32;validity&#32;test|
|Description|A&#32;test&#32;case&#32;checking&#32;if&#32;all&#32;the&#32;prefixes&#32;are&#32;not&#32;too&#32;close&#32;from&#32;the&#32;most&#32;used&#32;existing&#32;namespaces&#32;(according&#32;to&#32;prefix&#32;cc)&#32;or&#32;an&#32;ontology&#32;namespace|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-49)|Identifier|`namespace-typo`|
|[Section top](#pass-outcome-number-49)|Title|No&#32;namespace&#32;typo|
|[Section top](#pass-outcome-number-49)|Description|It&#32;seems&#32;that&#32;none&#32;of&#32;the&#32;subject&#32;URIs&#32;have&#32;namespaces&#32;typos|

***
### Pass Outcome number 50

[Jump to summary definition](#summary-Pass-50)	|	[Previous Pass outcome](#pass-outcome-number-49)	|	[Next Pass outcome](#pass-outcome-number-51)

:white_check_mark:Pass outcome
#### Subject detail
|Name|question-manufacturing-environments-discover-core-q7|
|----|----|
|Title|competency&#32;question&#32;domains/manufacturing-environments/discover-core/q7.rq&#32;from&#32;branch&#32;main|
|Composition|- [Competency question manufacturing-environments/discover-core/q7](https://github.com/HyperAgents/hmas/blob/main/domains/manufacturing-environments/discover-core/q7.rq.ttl)|

#### Criterion detail
|Identifier|[query-type](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#query-type)|
|----|----|
|Title|Query&#32;type&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;check&#32;if&#32;the&#32;query&#32;is&#32;indeed&#32;of&#32;type&#32;Select&#32;or&#32;Ask|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-50)|Identifier|`wrong-query-type`|
|[Section top](#pass-outcome-number-50)|Title|Accurate&#32;query&#32;type|
|[Section top](#pass-outcome-number-50)|Description|The&#32;query&#32;is&#32;of&#32;type&#32;Select&#32;or&#32;Ask|

***
### Pass Outcome number 51

[Jump to summary definition](#summary-Pass-51)	|	[Previous Pass outcome](#pass-outcome-number-50)	|	[Next Pass outcome](#pass-outcome-number-52)

:white_check_mark:Pass outcome
#### Subject detail
|Name|question-manufacturing-environments-discover-core-q7|
|----|----|
|Title|competency&#32;question&#32;domains/manufacturing-environments/discover-core/q7.rq&#32;from&#32;branch&#32;main|
|Composition|- [Competency question manufacturing-environments/discover-core/q7](https://github.com/HyperAgents/hmas/blob/main/domains/manufacturing-environments/discover-core/q7.rq.ttl)|

#### Criterion detail
|Identifier|[syntax](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#syntax)|
|----|----|
|Title|Syntax&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;check&#32;wether&#32;the&#32;test&#32;subject&#32;is&#32;syntaxically&#32;correct&#32;or&#32;not.|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-51)|Identifier|`syntax-error`|
|[Section top](#pass-outcome-number-51)|Title|Correct&#32;syntax|
|[Section top](#pass-outcome-number-51)|Description|Test&#32;subject&#32;has&#32;a&#32;correct&#32;syntax|

***
### Pass Outcome number 52

[Jump to summary definition](#summary-Pass-52)	|	[Previous Pass outcome](#pass-outcome-number-51)	|	[Next Pass outcome](#pass-outcome-number-53)

:white_check_mark:Pass outcome
#### Subject detail
|Name|question-manufacturing-environments-discover-core-q7|
|----|----|
|Title|competency&#32;question&#32;domains/manufacturing-environments/discover-core/q7.rq&#32;from&#32;branch&#32;main|
|Composition|- [Competency question manufacturing-environments/discover-core/q7](https://github.com/HyperAgents/hmas/blob/main/domains/manufacturing-environments/discover-core/q7.rq.ttl)|

#### Criterion detail
|Identifier|[uri-validity](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#uri-validity)|
|----|----|
|Title|URI&#32;validity&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;check&#32;if&#32;all&#32;the&#32;URIs&#32;of&#32;the&#32;resource&#32;are&#32;well-formed|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-52)|Identifier|`invalid-uri`|
|[Section top](#pass-outcome-number-52)|Title|All&#32;subject&#32;URI&#32;valid|
|[Section top](#pass-outcome-number-52)|Description|All&#32;the&#32;URIs&#32;of&#32;the&#32;subject&#32;are&#32;valid|

***
### Pass Outcome number 53

[Jump to summary definition](#summary-Pass-53)	|	[Previous Pass outcome](#pass-outcome-number-52)	|	[Next Pass outcome](#pass-outcome-number-54)

:white_check_mark:Pass outcome
#### Subject detail
|Name|question-manufacturing-environments-discover-core-q5|
|----|----|
|Title|competency&#32;question&#32;domains/manufacturing-environments/discover-core/q5.rq&#32;from&#32;branch&#32;main|
|Composition|- [Competency question manufacturing-environments/discover-core/q5](https://github.com/HyperAgents/hmas/blob/main/domains/manufacturing-environments/discover-core/q5.rq.ttl)|

#### Criterion detail
|Identifier|[namespace-validity](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#namespace-validity)|
|----|----|
|Title|Prefix&#32;validity&#32;test|
|Description|A&#32;test&#32;case&#32;checking&#32;if&#32;all&#32;the&#32;prefixes&#32;are&#32;not&#32;too&#32;close&#32;from&#32;the&#32;most&#32;used&#32;existing&#32;namespaces&#32;(according&#32;to&#32;prefix&#32;cc)&#32;or&#32;an&#32;ontology&#32;namespace|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-53)|Identifier|`namespace-typo`|
|[Section top](#pass-outcome-number-53)|Title|No&#32;namespace&#32;typo|
|[Section top](#pass-outcome-number-53)|Description|It&#32;seems&#32;that&#32;none&#32;of&#32;the&#32;subject&#32;URIs&#32;have&#32;namespaces&#32;typos|

***
### Pass Outcome number 54

[Jump to summary definition](#summary-Pass-54)	|	[Previous Pass outcome](#pass-outcome-number-53)	|	[Next Pass outcome](#pass-outcome-number-55)

:white_check_mark:Pass outcome
#### Subject detail
|Name|question-manufacturing-environments-discover-core-q5|
|----|----|
|Title|competency&#32;question&#32;domains/manufacturing-environments/discover-core/q5.rq&#32;from&#32;branch&#32;main|
|Composition|- [Competency question manufacturing-environments/discover-core/q5](https://github.com/HyperAgents/hmas/blob/main/domains/manufacturing-environments/discover-core/q5.rq.ttl)|

#### Criterion detail
|Identifier|[query-type](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#query-type)|
|----|----|
|Title|Query&#32;type&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;check&#32;if&#32;the&#32;query&#32;is&#32;indeed&#32;of&#32;type&#32;Select&#32;or&#32;Ask|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-54)|Identifier|`wrong-query-type`|
|[Section top](#pass-outcome-number-54)|Title|Accurate&#32;query&#32;type|
|[Section top](#pass-outcome-number-54)|Description|The&#32;query&#32;is&#32;of&#32;type&#32;Select&#32;or&#32;Ask|

***
### Pass Outcome number 55

[Jump to summary definition](#summary-Pass-55)	|	[Previous Pass outcome](#pass-outcome-number-54)	|	[Next Pass outcome](#pass-outcome-number-56)

:white_check_mark:Pass outcome
#### Subject detail
|Name|question-manufacturing-environments-discover-core-q5|
|----|----|
|Title|competency&#32;question&#32;domains/manufacturing-environments/discover-core/q5.rq&#32;from&#32;branch&#32;main|
|Composition|- [Competency question manufacturing-environments/discover-core/q5](https://github.com/HyperAgents/hmas/blob/main/domains/manufacturing-environments/discover-core/q5.rq.ttl)|

#### Criterion detail
|Identifier|[syntax](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#syntax)|
|----|----|
|Title|Syntax&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;check&#32;wether&#32;the&#32;test&#32;subject&#32;is&#32;syntaxically&#32;correct&#32;or&#32;not.|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-55)|Identifier|`syntax-error`|
|[Section top](#pass-outcome-number-55)|Title|Correct&#32;syntax|
|[Section top](#pass-outcome-number-55)|Description|Test&#32;subject&#32;has&#32;a&#32;correct&#32;syntax|

***
### Pass Outcome number 56

[Jump to summary definition](#summary-Pass-56)	|	[Previous Pass outcome](#pass-outcome-number-55)	|	[Next Pass outcome](#pass-outcome-number-57)

:white_check_mark:Pass outcome
#### Subject detail
|Name|question-manufacturing-environments-discover-core-q5|
|----|----|
|Title|competency&#32;question&#32;domains/manufacturing-environments/discover-core/q5.rq&#32;from&#32;branch&#32;main|
|Composition|- [Competency question manufacturing-environments/discover-core/q5](https://github.com/HyperAgents/hmas/blob/main/domains/manufacturing-environments/discover-core/q5.rq.ttl)|

#### Criterion detail
|Identifier|[uri-validity](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#uri-validity)|
|----|----|
|Title|URI&#32;validity&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;check&#32;if&#32;all&#32;the&#32;URIs&#32;of&#32;the&#32;resource&#32;are&#32;well-formed|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-56)|Identifier|`invalid-uri`|
|[Section top](#pass-outcome-number-56)|Title|All&#32;subject&#32;URI&#32;valid|
|[Section top](#pass-outcome-number-56)|Description|All&#32;the&#32;URIs&#32;of&#32;the&#32;subject&#32;are&#32;valid|

***
### Pass Outcome number 57

[Jump to summary definition](#summary-Pass-57)	|	[Previous Pass outcome](#pass-outcome-number-56)	|	[Next Pass outcome](#pass-outcome-number-58)

:white_check_mark:Pass outcome
#### Subject detail
|Name|question-manufacturing-environments-discover-core-q4|
|----|----|
|Title|competency&#32;question&#32;domains/manufacturing-environments/discover-core/q4.rq&#32;from&#32;branch&#32;main|
|Composition|- [Competency question manufacturing-environments/discover-core/q4](https://github.com/HyperAgents/hmas/blob/main/domains/manufacturing-environments/discover-core/q4.rq.ttl)|

#### Criterion detail
|Identifier|[namespace-validity](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#namespace-validity)|
|----|----|
|Title|Prefix&#32;validity&#32;test|
|Description|A&#32;test&#32;case&#32;checking&#32;if&#32;all&#32;the&#32;prefixes&#32;are&#32;not&#32;too&#32;close&#32;from&#32;the&#32;most&#32;used&#32;existing&#32;namespaces&#32;(according&#32;to&#32;prefix&#32;cc)&#32;or&#32;an&#32;ontology&#32;namespace|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-57)|Identifier|`namespace-typo`|
|[Section top](#pass-outcome-number-57)|Title|No&#32;namespace&#32;typo|
|[Section top](#pass-outcome-number-57)|Description|It&#32;seems&#32;that&#32;none&#32;of&#32;the&#32;subject&#32;URIs&#32;have&#32;namespaces&#32;typos|

***
### Pass Outcome number 58

[Jump to summary definition](#summary-Pass-58)	|	[Previous Pass outcome](#pass-outcome-number-57)	|	[Next Pass outcome](#pass-outcome-number-59)

:white_check_mark:Pass outcome
#### Subject detail
|Name|question-manufacturing-environments-discover-core-q4|
|----|----|
|Title|competency&#32;question&#32;domains/manufacturing-environments/discover-core/q4.rq&#32;from&#32;branch&#32;main|
|Composition|- [Competency question manufacturing-environments/discover-core/q4](https://github.com/HyperAgents/hmas/blob/main/domains/manufacturing-environments/discover-core/q4.rq.ttl)|

#### Criterion detail
|Identifier|[query-type](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#query-type)|
|----|----|
|Title|Query&#32;type&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;check&#32;if&#32;the&#32;query&#32;is&#32;indeed&#32;of&#32;type&#32;Select&#32;or&#32;Ask|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-58)|Identifier|`wrong-query-type`|
|[Section top](#pass-outcome-number-58)|Title|Accurate&#32;query&#32;type|
|[Section top](#pass-outcome-number-58)|Description|The&#32;query&#32;is&#32;of&#32;type&#32;Select&#32;or&#32;Ask|

***
### Pass Outcome number 59

[Jump to summary definition](#summary-Pass-59)	|	[Previous Pass outcome](#pass-outcome-number-58)	|	[Next Pass outcome](#pass-outcome-number-60)

:white_check_mark:Pass outcome
#### Subject detail
|Name|question-manufacturing-environments-discover-core-q4|
|----|----|
|Title|competency&#32;question&#32;domains/manufacturing-environments/discover-core/q4.rq&#32;from&#32;branch&#32;main|
|Composition|- [Competency question manufacturing-environments/discover-core/q4](https://github.com/HyperAgents/hmas/blob/main/domains/manufacturing-environments/discover-core/q4.rq.ttl)|

#### Criterion detail
|Identifier|[syntax](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#syntax)|
|----|----|
|Title|Syntax&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;check&#32;wether&#32;the&#32;test&#32;subject&#32;is&#32;syntaxically&#32;correct&#32;or&#32;not.|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-59)|Identifier|`syntax-error`|
|[Section top](#pass-outcome-number-59)|Title|Correct&#32;syntax|
|[Section top](#pass-outcome-number-59)|Description|Test&#32;subject&#32;has&#32;a&#32;correct&#32;syntax|

***
### Pass Outcome number 60

[Jump to summary definition](#summary-Pass-60)	|	[Previous Pass outcome](#pass-outcome-number-59)	|	[Next Pass outcome](#pass-outcome-number-61)

:white_check_mark:Pass outcome
#### Subject detail
|Name|question-manufacturing-environments-discover-core-q4|
|----|----|
|Title|competency&#32;question&#32;domains/manufacturing-environments/discover-core/q4.rq&#32;from&#32;branch&#32;main|
|Composition|- [Competency question manufacturing-environments/discover-core/q4](https://github.com/HyperAgents/hmas/blob/main/domains/manufacturing-environments/discover-core/q4.rq.ttl)|

#### Criterion detail
|Identifier|[uri-validity](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#uri-validity)|
|----|----|
|Title|URI&#32;validity&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;check&#32;if&#32;all&#32;the&#32;URIs&#32;of&#32;the&#32;resource&#32;are&#32;well-formed|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-60)|Identifier|`invalid-uri`|
|[Section top](#pass-outcome-number-60)|Title|All&#32;subject&#32;URI&#32;valid|
|[Section top](#pass-outcome-number-60)|Description|All&#32;the&#32;URIs&#32;of&#32;the&#32;subject&#32;are&#32;valid|

***
### Pass Outcome number 61

[Jump to summary definition](#summary-Pass-61)	|	[Previous Pass outcome](#pass-outcome-number-60)	|	[Next Pass outcome](#pass-outcome-number-62)

:white_check_mark:Pass outcome
#### Subject detail
|Name|question-manufacturing-environments-discover-core-q3|
|----|----|
|Title|competency&#32;question&#32;domains/manufacturing-environments/discover-core/q3.rq&#32;from&#32;branch&#32;main|
|Composition|- [Competency question manufacturing-environments/discover-core/q3](https://github.com/HyperAgents/hmas/blob/main/domains/manufacturing-environments/discover-core/q3.rq.ttl)|

#### Criterion detail
|Identifier|[namespace-validity](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#namespace-validity)|
|----|----|
|Title|Prefix&#32;validity&#32;test|
|Description|A&#32;test&#32;case&#32;checking&#32;if&#32;all&#32;the&#32;prefixes&#32;are&#32;not&#32;too&#32;close&#32;from&#32;the&#32;most&#32;used&#32;existing&#32;namespaces&#32;(according&#32;to&#32;prefix&#32;cc)&#32;or&#32;an&#32;ontology&#32;namespace|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-61)|Identifier|`namespace-typo`|
|[Section top](#pass-outcome-number-61)|Title|No&#32;namespace&#32;typo|
|[Section top](#pass-outcome-number-61)|Description|It&#32;seems&#32;that&#32;none&#32;of&#32;the&#32;subject&#32;URIs&#32;have&#32;namespaces&#32;typos|

***
### Pass Outcome number 62

[Jump to summary definition](#summary-Pass-62)	|	[Previous Pass outcome](#pass-outcome-number-61)	|	[Next Pass outcome](#pass-outcome-number-63)

:white_check_mark:Pass outcome
#### Subject detail
|Name|question-manufacturing-environments-discover-core-q3|
|----|----|
|Title|competency&#32;question&#32;domains/manufacturing-environments/discover-core/q3.rq&#32;from&#32;branch&#32;main|
|Composition|- [Competency question manufacturing-environments/discover-core/q3](https://github.com/HyperAgents/hmas/blob/main/domains/manufacturing-environments/discover-core/q3.rq.ttl)|

#### Criterion detail
|Identifier|[query-type](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#query-type)|
|----|----|
|Title|Query&#32;type&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;check&#32;if&#32;the&#32;query&#32;is&#32;indeed&#32;of&#32;type&#32;Select&#32;or&#32;Ask|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-62)|Identifier|`wrong-query-type`|
|[Section top](#pass-outcome-number-62)|Title|Accurate&#32;query&#32;type|
|[Section top](#pass-outcome-number-62)|Description|The&#32;query&#32;is&#32;of&#32;type&#32;Select&#32;or&#32;Ask|

***
### Pass Outcome number 63

[Jump to summary definition](#summary-Pass-63)	|	[Previous Pass outcome](#pass-outcome-number-62)	|	[Next Pass outcome](#pass-outcome-number-64)

:white_check_mark:Pass outcome
#### Subject detail
|Name|question-manufacturing-environments-discover-core-q3|
|----|----|
|Title|competency&#32;question&#32;domains/manufacturing-environments/discover-core/q3.rq&#32;from&#32;branch&#32;main|
|Composition|- [Competency question manufacturing-environments/discover-core/q3](https://github.com/HyperAgents/hmas/blob/main/domains/manufacturing-environments/discover-core/q3.rq.ttl)|

#### Criterion detail
|Identifier|[syntax](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#syntax)|
|----|----|
|Title|Syntax&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;check&#32;wether&#32;the&#32;test&#32;subject&#32;is&#32;syntaxically&#32;correct&#32;or&#32;not.|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-63)|Identifier|`syntax-error`|
|[Section top](#pass-outcome-number-63)|Title|Correct&#32;syntax|
|[Section top](#pass-outcome-number-63)|Description|Test&#32;subject&#32;has&#32;a&#32;correct&#32;syntax|

***
### Pass Outcome number 64

[Jump to summary definition](#summary-Pass-64)	|	[Previous Pass outcome](#pass-outcome-number-63)	|	[Next Pass outcome](#pass-outcome-number-65)

:white_check_mark:Pass outcome
#### Subject detail
|Name|question-manufacturing-environments-discover-core-q3|
|----|----|
|Title|competency&#32;question&#32;domains/manufacturing-environments/discover-core/q3.rq&#32;from&#32;branch&#32;main|
|Composition|- [Competency question manufacturing-environments/discover-core/q3](https://github.com/HyperAgents/hmas/blob/main/domains/manufacturing-environments/discover-core/q3.rq.ttl)|

#### Criterion detail
|Identifier|[uri-validity](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#uri-validity)|
|----|----|
|Title|URI&#32;validity&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;check&#32;if&#32;all&#32;the&#32;URIs&#32;of&#32;the&#32;resource&#32;are&#32;well-formed|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-64)|Identifier|`invalid-uri`|
|[Section top](#pass-outcome-number-64)|Title|All&#32;subject&#32;URI&#32;valid|
|[Section top](#pass-outcome-number-64)|Description|All&#32;the&#32;URIs&#32;of&#32;the&#32;subject&#32;are&#32;valid|

***
### Pass Outcome number 65

[Jump to summary definition](#summary-Pass-65)	|	[Previous Pass outcome](#pass-outcome-number-64)	|	[Next Pass outcome](#pass-outcome-number-66)

:white_check_mark:Pass outcome
#### Subject detail
|Name|question-manufacturing-environments-discover-core-q2|
|----|----|
|Title|competency&#32;question&#32;domains/manufacturing-environments/discover-core/q2.rq&#32;from&#32;branch&#32;main|
|Composition|- [Competency question manufacturing-environments/discover-core/q2](https://github.com/HyperAgents/hmas/blob/main/domains/manufacturing-environments/discover-core/q2.rq.ttl)|

#### Criterion detail
|Identifier|[namespace-validity](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#namespace-validity)|
|----|----|
|Title|Prefix&#32;validity&#32;test|
|Description|A&#32;test&#32;case&#32;checking&#32;if&#32;all&#32;the&#32;prefixes&#32;are&#32;not&#32;too&#32;close&#32;from&#32;the&#32;most&#32;used&#32;existing&#32;namespaces&#32;(according&#32;to&#32;prefix&#32;cc)&#32;or&#32;an&#32;ontology&#32;namespace|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-65)|Identifier|`namespace-typo`|
|[Section top](#pass-outcome-number-65)|Title|No&#32;namespace&#32;typo|
|[Section top](#pass-outcome-number-65)|Description|It&#32;seems&#32;that&#32;none&#32;of&#32;the&#32;subject&#32;URIs&#32;have&#32;namespaces&#32;typos|

***
### Pass Outcome number 66

[Jump to summary definition](#summary-Pass-66)	|	[Previous Pass outcome](#pass-outcome-number-65)	|	[Next Pass outcome](#pass-outcome-number-67)

:white_check_mark:Pass outcome
#### Subject detail
|Name|question-manufacturing-environments-discover-core-q2|
|----|----|
|Title|competency&#32;question&#32;domains/manufacturing-environments/discover-core/q2.rq&#32;from&#32;branch&#32;main|
|Composition|- [Competency question manufacturing-environments/discover-core/q2](https://github.com/HyperAgents/hmas/blob/main/domains/manufacturing-environments/discover-core/q2.rq.ttl)|

#### Criterion detail
|Identifier|[query-type](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#query-type)|
|----|----|
|Title|Query&#32;type&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;check&#32;if&#32;the&#32;query&#32;is&#32;indeed&#32;of&#32;type&#32;Select&#32;or&#32;Ask|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-66)|Identifier|`wrong-query-type`|
|[Section top](#pass-outcome-number-66)|Title|Accurate&#32;query&#32;type|
|[Section top](#pass-outcome-number-66)|Description|The&#32;query&#32;is&#32;of&#32;type&#32;Select&#32;or&#32;Ask|

***
### Pass Outcome number 67

[Jump to summary definition](#summary-Pass-67)	|	[Previous Pass outcome](#pass-outcome-number-66)	|	[Next Pass outcome](#pass-outcome-number-68)

:white_check_mark:Pass outcome
#### Subject detail
|Name|question-manufacturing-environments-discover-core-q2|
|----|----|
|Title|competency&#32;question&#32;domains/manufacturing-environments/discover-core/q2.rq&#32;from&#32;branch&#32;main|
|Composition|- [Competency question manufacturing-environments/discover-core/q2](https://github.com/HyperAgents/hmas/blob/main/domains/manufacturing-environments/discover-core/q2.rq.ttl)|

#### Criterion detail
|Identifier|[syntax](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#syntax)|
|----|----|
|Title|Syntax&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;check&#32;wether&#32;the&#32;test&#32;subject&#32;is&#32;syntaxically&#32;correct&#32;or&#32;not.|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-67)|Identifier|`syntax-error`|
|[Section top](#pass-outcome-number-67)|Title|Correct&#32;syntax|
|[Section top](#pass-outcome-number-67)|Description|Test&#32;subject&#32;has&#32;a&#32;correct&#32;syntax|

***
### Pass Outcome number 68

[Jump to summary definition](#summary-Pass-68)	|	[Previous Pass outcome](#pass-outcome-number-67)	|	[Next Pass outcome](#pass-outcome-number-69)

:white_check_mark:Pass outcome
#### Subject detail
|Name|question-manufacturing-environments-discover-core-q2|
|----|----|
|Title|competency&#32;question&#32;domains/manufacturing-environments/discover-core/q2.rq&#32;from&#32;branch&#32;main|
|Composition|- [Competency question manufacturing-environments/discover-core/q2](https://github.com/HyperAgents/hmas/blob/main/domains/manufacturing-environments/discover-core/q2.rq.ttl)|

#### Criterion detail
|Identifier|[uri-validity](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#uri-validity)|
|----|----|
|Title|URI&#32;validity&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;check&#32;if&#32;all&#32;the&#32;URIs&#32;of&#32;the&#32;resource&#32;are&#32;well-formed|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-68)|Identifier|`invalid-uri`|
|[Section top](#pass-outcome-number-68)|Title|All&#32;subject&#32;URI&#32;valid|
|[Section top](#pass-outcome-number-68)|Description|All&#32;the&#32;URIs&#32;of&#32;the&#32;subject&#32;are&#32;valid|

***
### Pass Outcome number 69

[Jump to summary definition](#summary-Pass-69)	|	[Previous Pass outcome](#pass-outcome-number-68)	|	[Next Pass outcome](#pass-outcome-number-70)

:white_check_mark:Pass outcome
#### Subject detail
|Name|question-manufacturing-environments-discover-core-q1|
|----|----|
|Title|competency&#32;question&#32;domains/manufacturing-environments/discover-core/q1.rq&#32;from&#32;branch&#32;main|
|Composition|- [Competency question manufacturing-environments/discover-core/q1](https://github.com/HyperAgents/hmas/blob/main/domains/manufacturing-environments/discover-core/q1.rq.ttl)|

#### Criterion detail
|Identifier|[namespace-validity](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#namespace-validity)|
|----|----|
|Title|Prefix&#32;validity&#32;test|
|Description|A&#32;test&#32;case&#32;checking&#32;if&#32;all&#32;the&#32;prefixes&#32;are&#32;not&#32;too&#32;close&#32;from&#32;the&#32;most&#32;used&#32;existing&#32;namespaces&#32;(according&#32;to&#32;prefix&#32;cc)&#32;or&#32;an&#32;ontology&#32;namespace|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-69)|Identifier|`namespace-typo`|
|[Section top](#pass-outcome-number-69)|Title|No&#32;namespace&#32;typo|
|[Section top](#pass-outcome-number-69)|Description|It&#32;seems&#32;that&#32;none&#32;of&#32;the&#32;subject&#32;URIs&#32;have&#32;namespaces&#32;typos|

***
### Pass Outcome number 70

[Jump to summary definition](#summary-Pass-70)	|	[Previous Pass outcome](#pass-outcome-number-69)	|	[Next Pass outcome](#pass-outcome-number-71)

:white_check_mark:Pass outcome
#### Subject detail
|Name|question-manufacturing-environments-discover-core-q1|
|----|----|
|Title|competency&#32;question&#32;domains/manufacturing-environments/discover-core/q1.rq&#32;from&#32;branch&#32;main|
|Composition|- [Competency question manufacturing-environments/discover-core/q1](https://github.com/HyperAgents/hmas/blob/main/domains/manufacturing-environments/discover-core/q1.rq.ttl)|

#### Criterion detail
|Identifier|[query-type](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#query-type)|
|----|----|
|Title|Query&#32;type&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;check&#32;if&#32;the&#32;query&#32;is&#32;indeed&#32;of&#32;type&#32;Select&#32;or&#32;Ask|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-70)|Identifier|`wrong-query-type`|
|[Section top](#pass-outcome-number-70)|Title|Accurate&#32;query&#32;type|
|[Section top](#pass-outcome-number-70)|Description|The&#32;query&#32;is&#32;of&#32;type&#32;Select&#32;or&#32;Ask|

***
### Pass Outcome number 71

[Jump to summary definition](#summary-Pass-71)	|	[Previous Pass outcome](#pass-outcome-number-70)	|	[Next Pass outcome](#pass-outcome-number-72)

:white_check_mark:Pass outcome
#### Subject detail
|Name|question-manufacturing-environments-discover-core-q1|
|----|----|
|Title|competency&#32;question&#32;domains/manufacturing-environments/discover-core/q1.rq&#32;from&#32;branch&#32;main|
|Composition|- [Competency question manufacturing-environments/discover-core/q1](https://github.com/HyperAgents/hmas/blob/main/domains/manufacturing-environments/discover-core/q1.rq.ttl)|

#### Criterion detail
|Identifier|[syntax](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#syntax)|
|----|----|
|Title|Syntax&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;check&#32;wether&#32;the&#32;test&#32;subject&#32;is&#32;syntaxically&#32;correct&#32;or&#32;not.|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-71)|Identifier|`syntax-error`|
|[Section top](#pass-outcome-number-71)|Title|Correct&#32;syntax|
|[Section top](#pass-outcome-number-71)|Description|Test&#32;subject&#32;has&#32;a&#32;correct&#32;syntax|

***
### Pass Outcome number 72

[Jump to summary definition](#summary-Pass-72)	|	[Previous Pass outcome](#pass-outcome-number-71)	|	[Next Pass outcome](#pass-outcome-number-73)

:white_check_mark:Pass outcome
#### Subject detail
|Name|question-manufacturing-environments-discover-core-q1|
|----|----|
|Title|competency&#32;question&#32;domains/manufacturing-environments/discover-core/q1.rq&#32;from&#32;branch&#32;main|
|Composition|- [Competency question manufacturing-environments/discover-core/q1](https://github.com/HyperAgents/hmas/blob/main/domains/manufacturing-environments/discover-core/q1.rq.ttl)|

#### Criterion detail
|Identifier|[uri-validity](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#uri-validity)|
|----|----|
|Title|URI&#32;validity&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;check&#32;if&#32;all&#32;the&#32;URIs&#32;of&#32;the&#32;resource&#32;are&#32;well-formed|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-72)|Identifier|`invalid-uri`|
|[Section top](#pass-outcome-number-72)|Title|All&#32;subject&#32;URI&#32;valid|
|[Section top](#pass-outcome-number-72)|Description|All&#32;the&#32;URIs&#32;of&#32;the&#32;subject&#32;are&#32;valid|

***
### Pass Outcome number 73

[Jump to summary definition](#summary-Pass-73)	|	[Previous Pass outcome](#pass-outcome-number-72)	|	[Next Pass outcome](#pass-outcome-number-74)

:white_check_mark:Pass outcome
#### Subject detail
|Name|question-manufacturing-environments-discover-behavior-specifications-q5|
|----|----|
|Title|competency&#32;question&#32;domains/manufacturing-environments/discover-behavior-specifications/q5.rq&#32;from&#32;branch&#32;main|
|Composition|- [Competency question manufacturing-environments/discover-behavior-specifications/q5](https://github.com/HyperAgents/hmas/blob/main/domains/manufacturing-environments/discover-behavior-specifications/q5.rq.ttl)|

#### Criterion detail
|Identifier|[namespace-validity](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#namespace-validity)|
|----|----|
|Title|Prefix&#32;validity&#32;test|
|Description|A&#32;test&#32;case&#32;checking&#32;if&#32;all&#32;the&#32;prefixes&#32;are&#32;not&#32;too&#32;close&#32;from&#32;the&#32;most&#32;used&#32;existing&#32;namespaces&#32;(according&#32;to&#32;prefix&#32;cc)&#32;or&#32;an&#32;ontology&#32;namespace|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-73)|Identifier|`namespace-typo`|
|[Section top](#pass-outcome-number-73)|Title|No&#32;namespace&#32;typo|
|[Section top](#pass-outcome-number-73)|Description|It&#32;seems&#32;that&#32;none&#32;of&#32;the&#32;subject&#32;URIs&#32;have&#32;namespaces&#32;typos|

***
### Pass Outcome number 74

[Jump to summary definition](#summary-Pass-74)	|	[Previous Pass outcome](#pass-outcome-number-73)	|	[Next Pass outcome](#pass-outcome-number-75)

:white_check_mark:Pass outcome
#### Subject detail
|Name|question-manufacturing-environments-discover-behavior-specifications-q5|
|----|----|
|Title|competency&#32;question&#32;domains/manufacturing-environments/discover-behavior-specifications/q5.rq&#32;from&#32;branch&#32;main|
|Composition|- [Competency question manufacturing-environments/discover-behavior-specifications/q5](https://github.com/HyperAgents/hmas/blob/main/domains/manufacturing-environments/discover-behavior-specifications/q5.rq.ttl)|

#### Criterion detail
|Identifier|[query-type](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#query-type)|
|----|----|
|Title|Query&#32;type&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;check&#32;if&#32;the&#32;query&#32;is&#32;indeed&#32;of&#32;type&#32;Select&#32;or&#32;Ask|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-74)|Identifier|`wrong-query-type`|
|[Section top](#pass-outcome-number-74)|Title|Accurate&#32;query&#32;type|
|[Section top](#pass-outcome-number-74)|Description|The&#32;query&#32;is&#32;of&#32;type&#32;Select&#32;or&#32;Ask|

***
### Pass Outcome number 75

[Jump to summary definition](#summary-Pass-75)	|	[Previous Pass outcome](#pass-outcome-number-74)	|	[Next Pass outcome](#pass-outcome-number-76)

:white_check_mark:Pass outcome
#### Subject detail
|Name|question-manufacturing-environments-discover-behavior-specifications-q5|
|----|----|
|Title|competency&#32;question&#32;domains/manufacturing-environments/discover-behavior-specifications/q5.rq&#32;from&#32;branch&#32;main|
|Composition|- [Competency question manufacturing-environments/discover-behavior-specifications/q5](https://github.com/HyperAgents/hmas/blob/main/domains/manufacturing-environments/discover-behavior-specifications/q5.rq.ttl)|

#### Criterion detail
|Identifier|[syntax](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#syntax)|
|----|----|
|Title|Syntax&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;check&#32;wether&#32;the&#32;test&#32;subject&#32;is&#32;syntaxically&#32;correct&#32;or&#32;not.|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-75)|Identifier|`syntax-error`|
|[Section top](#pass-outcome-number-75)|Title|Correct&#32;syntax|
|[Section top](#pass-outcome-number-75)|Description|Test&#32;subject&#32;has&#32;a&#32;correct&#32;syntax|

***
### Pass Outcome number 76

[Jump to summary definition](#summary-Pass-76)	|	[Previous Pass outcome](#pass-outcome-number-75)	|	[Next Pass outcome](#pass-outcome-number-77)

:white_check_mark:Pass outcome
#### Subject detail
|Name|question-manufacturing-environments-discover-behavior-specifications-q5|
|----|----|
|Title|competency&#32;question&#32;domains/manufacturing-environments/discover-behavior-specifications/q5.rq&#32;from&#32;branch&#32;main|
|Composition|- [Competency question manufacturing-environments/discover-behavior-specifications/q5](https://github.com/HyperAgents/hmas/blob/main/domains/manufacturing-environments/discover-behavior-specifications/q5.rq.ttl)|

#### Criterion detail
|Identifier|[uri-validity](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#uri-validity)|
|----|----|
|Title|URI&#32;validity&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;check&#32;if&#32;all&#32;the&#32;URIs&#32;of&#32;the&#32;resource&#32;are&#32;well-formed|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-76)|Identifier|`invalid-uri`|
|[Section top](#pass-outcome-number-76)|Title|All&#32;subject&#32;URI&#32;valid|
|[Section top](#pass-outcome-number-76)|Description|All&#32;the&#32;URIs&#32;of&#32;the&#32;subject&#32;are&#32;valid|

***
### Pass Outcome number 77

[Jump to summary definition](#summary-Pass-77)	|	[Previous Pass outcome](#pass-outcome-number-76)	|	[Next Pass outcome](#pass-outcome-number-78)

:white_check_mark:Pass outcome
#### Subject detail
|Name|question-manufacturing-environments-discover-behavior-specifications-q4|
|----|----|
|Title|competency&#32;question&#32;domains/manufacturing-environments/discover-behavior-specifications/q4.rq&#32;from&#32;branch&#32;main|
|Composition|- [Competency question manufacturing-environments/discover-behavior-specifications/q4](https://github.com/HyperAgents/hmas/blob/main/domains/manufacturing-environments/discover-behavior-specifications/q4.rq.ttl)|

#### Criterion detail
|Identifier|[namespace-validity](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#namespace-validity)|
|----|----|
|Title|Prefix&#32;validity&#32;test|
|Description|A&#32;test&#32;case&#32;checking&#32;if&#32;all&#32;the&#32;prefixes&#32;are&#32;not&#32;too&#32;close&#32;from&#32;the&#32;most&#32;used&#32;existing&#32;namespaces&#32;(according&#32;to&#32;prefix&#32;cc)&#32;or&#32;an&#32;ontology&#32;namespace|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-77)|Identifier|`namespace-typo`|
|[Section top](#pass-outcome-number-77)|Title|No&#32;namespace&#32;typo|
|[Section top](#pass-outcome-number-77)|Description|It&#32;seems&#32;that&#32;none&#32;of&#32;the&#32;subject&#32;URIs&#32;have&#32;namespaces&#32;typos|

***
### Pass Outcome number 78

[Jump to summary definition](#summary-Pass-78)	|	[Previous Pass outcome](#pass-outcome-number-77)	|	[Next Pass outcome](#pass-outcome-number-79)

:white_check_mark:Pass outcome
#### Subject detail
|Name|question-manufacturing-environments-discover-behavior-specifications-q4|
|----|----|
|Title|competency&#32;question&#32;domains/manufacturing-environments/discover-behavior-specifications/q4.rq&#32;from&#32;branch&#32;main|
|Composition|- [Competency question manufacturing-environments/discover-behavior-specifications/q4](https://github.com/HyperAgents/hmas/blob/main/domains/manufacturing-environments/discover-behavior-specifications/q4.rq.ttl)|

#### Criterion detail
|Identifier|[query-type](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#query-type)|
|----|----|
|Title|Query&#32;type&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;check&#32;if&#32;the&#32;query&#32;is&#32;indeed&#32;of&#32;type&#32;Select&#32;or&#32;Ask|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-78)|Identifier|`wrong-query-type`|
|[Section top](#pass-outcome-number-78)|Title|Accurate&#32;query&#32;type|
|[Section top](#pass-outcome-number-78)|Description|The&#32;query&#32;is&#32;of&#32;type&#32;Select&#32;or&#32;Ask|

***
### Pass Outcome number 79

[Jump to summary definition](#summary-Pass-79)	|	[Previous Pass outcome](#pass-outcome-number-78)	|	[Next Pass outcome](#pass-outcome-number-80)

:white_check_mark:Pass outcome
#### Subject detail
|Name|question-manufacturing-environments-discover-behavior-specifications-q4|
|----|----|
|Title|competency&#32;question&#32;domains/manufacturing-environments/discover-behavior-specifications/q4.rq&#32;from&#32;branch&#32;main|
|Composition|- [Competency question manufacturing-environments/discover-behavior-specifications/q4](https://github.com/HyperAgents/hmas/blob/main/domains/manufacturing-environments/discover-behavior-specifications/q4.rq.ttl)|

#### Criterion detail
|Identifier|[syntax](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#syntax)|
|----|----|
|Title|Syntax&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;check&#32;wether&#32;the&#32;test&#32;subject&#32;is&#32;syntaxically&#32;correct&#32;or&#32;not.|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-79)|Identifier|`syntax-error`|
|[Section top](#pass-outcome-number-79)|Title|Correct&#32;syntax|
|[Section top](#pass-outcome-number-79)|Description|Test&#32;subject&#32;has&#32;a&#32;correct&#32;syntax|

***
### Pass Outcome number 80

[Jump to summary definition](#summary-Pass-80)	|	[Previous Pass outcome](#pass-outcome-number-79)	|	[Next Pass outcome](#pass-outcome-number-81)

:white_check_mark:Pass outcome
#### Subject detail
|Name|question-manufacturing-environments-discover-behavior-specifications-q4|
|----|----|
|Title|competency&#32;question&#32;domains/manufacturing-environments/discover-behavior-specifications/q4.rq&#32;from&#32;branch&#32;main|
|Composition|- [Competency question manufacturing-environments/discover-behavior-specifications/q4](https://github.com/HyperAgents/hmas/blob/main/domains/manufacturing-environments/discover-behavior-specifications/q4.rq.ttl)|

#### Criterion detail
|Identifier|[uri-validity](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#uri-validity)|
|----|----|
|Title|URI&#32;validity&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;check&#32;if&#32;all&#32;the&#32;URIs&#32;of&#32;the&#32;resource&#32;are&#32;well-formed|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-80)|Identifier|`invalid-uri`|
|[Section top](#pass-outcome-number-80)|Title|All&#32;subject&#32;URI&#32;valid|
|[Section top](#pass-outcome-number-80)|Description|All&#32;the&#32;URIs&#32;of&#32;the&#32;subject&#32;are&#32;valid|

***
### Pass Outcome number 81

[Jump to summary definition](#summary-Pass-81)	|	[Previous Pass outcome](#pass-outcome-number-80)	|	[Next Pass outcome](#pass-outcome-number-82)

:white_check_mark:Pass outcome
#### Subject detail
|Name|question-manufacturing-environments-discover-behavior-specifications-q3|
|----|----|
|Title|competency&#32;question&#32;domains/manufacturing-environments/discover-behavior-specifications/q3.rq&#32;from&#32;branch&#32;main|
|Composition|- [Competency question manufacturing-environments/discover-behavior-specifications/q3](https://github.com/HyperAgents/hmas/blob/main/domains/manufacturing-environments/discover-behavior-specifications/q3.rq.ttl)|

#### Criterion detail
|Identifier|[namespace-validity](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#namespace-validity)|
|----|----|
|Title|Prefix&#32;validity&#32;test|
|Description|A&#32;test&#32;case&#32;checking&#32;if&#32;all&#32;the&#32;prefixes&#32;are&#32;not&#32;too&#32;close&#32;from&#32;the&#32;most&#32;used&#32;existing&#32;namespaces&#32;(according&#32;to&#32;prefix&#32;cc)&#32;or&#32;an&#32;ontology&#32;namespace|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-81)|Identifier|`namespace-typo`|
|[Section top](#pass-outcome-number-81)|Title|No&#32;namespace&#32;typo|
|[Section top](#pass-outcome-number-81)|Description|It&#32;seems&#32;that&#32;none&#32;of&#32;the&#32;subject&#32;URIs&#32;have&#32;namespaces&#32;typos|

***
### Pass Outcome number 82

[Jump to summary definition](#summary-Pass-82)	|	[Previous Pass outcome](#pass-outcome-number-81)	|	[Next Pass outcome](#pass-outcome-number-83)

:white_check_mark:Pass outcome
#### Subject detail
|Name|question-manufacturing-environments-discover-behavior-specifications-q3|
|----|----|
|Title|competency&#32;question&#32;domains/manufacturing-environments/discover-behavior-specifications/q3.rq&#32;from&#32;branch&#32;main|
|Composition|- [Competency question manufacturing-environments/discover-behavior-specifications/q3](https://github.com/HyperAgents/hmas/blob/main/domains/manufacturing-environments/discover-behavior-specifications/q3.rq.ttl)|

#### Criterion detail
|Identifier|[query-type](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#query-type)|
|----|----|
|Title|Query&#32;type&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;check&#32;if&#32;the&#32;query&#32;is&#32;indeed&#32;of&#32;type&#32;Select&#32;or&#32;Ask|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-82)|Identifier|`wrong-query-type`|
|[Section top](#pass-outcome-number-82)|Title|Accurate&#32;query&#32;type|
|[Section top](#pass-outcome-number-82)|Description|The&#32;query&#32;is&#32;of&#32;type&#32;Select&#32;or&#32;Ask|

***
### Pass Outcome number 83

[Jump to summary definition](#summary-Pass-83)	|	[Previous Pass outcome](#pass-outcome-number-82)	|	[Next Pass outcome](#pass-outcome-number-84)

:white_check_mark:Pass outcome
#### Subject detail
|Name|question-manufacturing-environments-discover-behavior-specifications-q3|
|----|----|
|Title|competency&#32;question&#32;domains/manufacturing-environments/discover-behavior-specifications/q3.rq&#32;from&#32;branch&#32;main|
|Composition|- [Competency question manufacturing-environments/discover-behavior-specifications/q3](https://github.com/HyperAgents/hmas/blob/main/domains/manufacturing-environments/discover-behavior-specifications/q3.rq.ttl)|

#### Criterion detail
|Identifier|[syntax](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#syntax)|
|----|----|
|Title|Syntax&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;check&#32;wether&#32;the&#32;test&#32;subject&#32;is&#32;syntaxically&#32;correct&#32;or&#32;not.|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-83)|Identifier|`syntax-error`|
|[Section top](#pass-outcome-number-83)|Title|Correct&#32;syntax|
|[Section top](#pass-outcome-number-83)|Description|Test&#32;subject&#32;has&#32;a&#32;correct&#32;syntax|

***
### Pass Outcome number 84

[Jump to summary definition](#summary-Pass-84)	|	[Previous Pass outcome](#pass-outcome-number-83)	|	[Next Pass outcome](#pass-outcome-number-85)

:white_check_mark:Pass outcome
#### Subject detail
|Name|question-manufacturing-environments-discover-behavior-specifications-q3|
|----|----|
|Title|competency&#32;question&#32;domains/manufacturing-environments/discover-behavior-specifications/q3.rq&#32;from&#32;branch&#32;main|
|Composition|- [Competency question manufacturing-environments/discover-behavior-specifications/q3](https://github.com/HyperAgents/hmas/blob/main/domains/manufacturing-environments/discover-behavior-specifications/q3.rq.ttl)|

#### Criterion detail
|Identifier|[uri-validity](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#uri-validity)|
|----|----|
|Title|URI&#32;validity&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;check&#32;if&#32;all&#32;the&#32;URIs&#32;of&#32;the&#32;resource&#32;are&#32;well-formed|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-84)|Identifier|`invalid-uri`|
|[Section top](#pass-outcome-number-84)|Title|All&#32;subject&#32;URI&#32;valid|
|[Section top](#pass-outcome-number-84)|Description|All&#32;the&#32;URIs&#32;of&#32;the&#32;subject&#32;are&#32;valid|

***
### Pass Outcome number 85

[Jump to summary definition](#summary-Pass-85)	|	[Previous Pass outcome](#pass-outcome-number-84)	|	[Next Pass outcome](#pass-outcome-number-86)

:white_check_mark:Pass outcome
#### Subject detail
|Name|question-manufacturing-environments-discover-behavior-specifications-q2|
|----|----|
|Title|competency&#32;question&#32;domains/manufacturing-environments/discover-behavior-specifications/q2.rq&#32;from&#32;branch&#32;main|
|Composition|- [Competency question manufacturing-environments/discover-behavior-specifications/q2](https://github.com/HyperAgents/hmas/blob/main/domains/manufacturing-environments/discover-behavior-specifications/q2.rq.ttl)|

#### Criterion detail
|Identifier|[namespace-validity](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#namespace-validity)|
|----|----|
|Title|Prefix&#32;validity&#32;test|
|Description|A&#32;test&#32;case&#32;checking&#32;if&#32;all&#32;the&#32;prefixes&#32;are&#32;not&#32;too&#32;close&#32;from&#32;the&#32;most&#32;used&#32;existing&#32;namespaces&#32;(according&#32;to&#32;prefix&#32;cc)&#32;or&#32;an&#32;ontology&#32;namespace|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-85)|Identifier|`namespace-typo`|
|[Section top](#pass-outcome-number-85)|Title|No&#32;namespace&#32;typo|
|[Section top](#pass-outcome-number-85)|Description|It&#32;seems&#32;that&#32;none&#32;of&#32;the&#32;subject&#32;URIs&#32;have&#32;namespaces&#32;typos|

***
### Pass Outcome number 86

[Jump to summary definition](#summary-Pass-86)	|	[Previous Pass outcome](#pass-outcome-number-85)	|	[Next Pass outcome](#pass-outcome-number-87)

:white_check_mark:Pass outcome
#### Subject detail
|Name|question-manufacturing-environments-discover-behavior-specifications-q2|
|----|----|
|Title|competency&#32;question&#32;domains/manufacturing-environments/discover-behavior-specifications/q2.rq&#32;from&#32;branch&#32;main|
|Composition|- [Competency question manufacturing-environments/discover-behavior-specifications/q2](https://github.com/HyperAgents/hmas/blob/main/domains/manufacturing-environments/discover-behavior-specifications/q2.rq.ttl)|

#### Criterion detail
|Identifier|[query-type](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#query-type)|
|----|----|
|Title|Query&#32;type&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;check&#32;if&#32;the&#32;query&#32;is&#32;indeed&#32;of&#32;type&#32;Select&#32;or&#32;Ask|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-86)|Identifier|`wrong-query-type`|
|[Section top](#pass-outcome-number-86)|Title|Accurate&#32;query&#32;type|
|[Section top](#pass-outcome-number-86)|Description|The&#32;query&#32;is&#32;of&#32;type&#32;Select&#32;or&#32;Ask|

***
### Pass Outcome number 87

[Jump to summary definition](#summary-Pass-87)	|	[Previous Pass outcome](#pass-outcome-number-86)	|	[Next Pass outcome](#pass-outcome-number-88)

:white_check_mark:Pass outcome
#### Subject detail
|Name|question-manufacturing-environments-discover-behavior-specifications-q2|
|----|----|
|Title|competency&#32;question&#32;domains/manufacturing-environments/discover-behavior-specifications/q2.rq&#32;from&#32;branch&#32;main|
|Composition|- [Competency question manufacturing-environments/discover-behavior-specifications/q2](https://github.com/HyperAgents/hmas/blob/main/domains/manufacturing-environments/discover-behavior-specifications/q2.rq.ttl)|

#### Criterion detail
|Identifier|[syntax](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#syntax)|
|----|----|
|Title|Syntax&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;check&#32;wether&#32;the&#32;test&#32;subject&#32;is&#32;syntaxically&#32;correct&#32;or&#32;not.|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-87)|Identifier|`syntax-error`|
|[Section top](#pass-outcome-number-87)|Title|Correct&#32;syntax|
|[Section top](#pass-outcome-number-87)|Description|Test&#32;subject&#32;has&#32;a&#32;correct&#32;syntax|

***
### Pass Outcome number 88

[Jump to summary definition](#summary-Pass-88)	|	[Previous Pass outcome](#pass-outcome-number-87)	|	[Next Pass outcome](#pass-outcome-number-89)

:white_check_mark:Pass outcome
#### Subject detail
|Name|question-manufacturing-environments-discover-behavior-specifications-q2|
|----|----|
|Title|competency&#32;question&#32;domains/manufacturing-environments/discover-behavior-specifications/q2.rq&#32;from&#32;branch&#32;main|
|Composition|- [Competency question manufacturing-environments/discover-behavior-specifications/q2](https://github.com/HyperAgents/hmas/blob/main/domains/manufacturing-environments/discover-behavior-specifications/q2.rq.ttl)|

#### Criterion detail
|Identifier|[uri-validity](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#uri-validity)|
|----|----|
|Title|URI&#32;validity&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;check&#32;if&#32;all&#32;the&#32;URIs&#32;of&#32;the&#32;resource&#32;are&#32;well-formed|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-88)|Identifier|`invalid-uri`|
|[Section top](#pass-outcome-number-88)|Title|All&#32;subject&#32;URI&#32;valid|
|[Section top](#pass-outcome-number-88)|Description|All&#32;the&#32;URIs&#32;of&#32;the&#32;subject&#32;are&#32;valid|

***
### Pass Outcome number 89

[Jump to summary definition](#summary-Pass-89)	|	[Previous Pass outcome](#pass-outcome-number-88)	|	[Next Pass outcome](#pass-outcome-number-90)

:white_check_mark:Pass outcome
#### Subject detail
|Name|question-manufacturing-environments-discover-behavior-specifications-q1|
|----|----|
|Title|competency&#32;question&#32;domains/manufacturing-environments/discover-behavior-specifications/q1.rq&#32;from&#32;branch&#32;main|
|Composition|- [Competency question manufacturing-environments/discover-behavior-specifications/q1](https://github.com/HyperAgents/hmas/blob/main/domains/manufacturing-environments/discover-behavior-specifications/q1.rq.ttl)|

#### Criterion detail
|Identifier|[namespace-validity](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#namespace-validity)|
|----|----|
|Title|Prefix&#32;validity&#32;test|
|Description|A&#32;test&#32;case&#32;checking&#32;if&#32;all&#32;the&#32;prefixes&#32;are&#32;not&#32;too&#32;close&#32;from&#32;the&#32;most&#32;used&#32;existing&#32;namespaces&#32;(according&#32;to&#32;prefix&#32;cc)&#32;or&#32;an&#32;ontology&#32;namespace|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-89)|Identifier|`namespace-typo`|
|[Section top](#pass-outcome-number-89)|Title|No&#32;namespace&#32;typo|
|[Section top](#pass-outcome-number-89)|Description|It&#32;seems&#32;that&#32;none&#32;of&#32;the&#32;subject&#32;URIs&#32;have&#32;namespaces&#32;typos|

***
### Pass Outcome number 90

[Jump to summary definition](#summary-Pass-90)	|	[Previous Pass outcome](#pass-outcome-number-89)	|	[Next Pass outcome](#pass-outcome-number-91)

:white_check_mark:Pass outcome
#### Subject detail
|Name|question-manufacturing-environments-discover-behavior-specifications-q1|
|----|----|
|Title|competency&#32;question&#32;domains/manufacturing-environments/discover-behavior-specifications/q1.rq&#32;from&#32;branch&#32;main|
|Composition|- [Competency question manufacturing-environments/discover-behavior-specifications/q1](https://github.com/HyperAgents/hmas/blob/main/domains/manufacturing-environments/discover-behavior-specifications/q1.rq.ttl)|

#### Criterion detail
|Identifier|[query-type](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#query-type)|
|----|----|
|Title|Query&#32;type&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;check&#32;if&#32;the&#32;query&#32;is&#32;indeed&#32;of&#32;type&#32;Select&#32;or&#32;Ask|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-90)|Identifier|`wrong-query-type`|
|[Section top](#pass-outcome-number-90)|Title|Accurate&#32;query&#32;type|
|[Section top](#pass-outcome-number-90)|Description|The&#32;query&#32;is&#32;of&#32;type&#32;Select&#32;or&#32;Ask|

***
### Pass Outcome number 91

[Jump to summary definition](#summary-Pass-91)	|	[Previous Pass outcome](#pass-outcome-number-90)	|	[Next Pass outcome](#pass-outcome-number-92)

:white_check_mark:Pass outcome
#### Subject detail
|Name|question-manufacturing-environments-discover-behavior-specifications-q1|
|----|----|
|Title|competency&#32;question&#32;domains/manufacturing-environments/discover-behavior-specifications/q1.rq&#32;from&#32;branch&#32;main|
|Composition|- [Competency question manufacturing-environments/discover-behavior-specifications/q1](https://github.com/HyperAgents/hmas/blob/main/domains/manufacturing-environments/discover-behavior-specifications/q1.rq.ttl)|

#### Criterion detail
|Identifier|[syntax](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#syntax)|
|----|----|
|Title|Syntax&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;check&#32;wether&#32;the&#32;test&#32;subject&#32;is&#32;syntaxically&#32;correct&#32;or&#32;not.|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-91)|Identifier|`syntax-error`|
|[Section top](#pass-outcome-number-91)|Title|Correct&#32;syntax|
|[Section top](#pass-outcome-number-91)|Description|Test&#32;subject&#32;has&#32;a&#32;correct&#32;syntax|

***
### Pass Outcome number 92

[Jump to summary definition](#summary-Pass-92)	|	[Previous Pass outcome](#pass-outcome-number-91)	|	[Next Pass outcome](#pass-outcome-number-93)

:white_check_mark:Pass outcome
#### Subject detail
|Name|question-manufacturing-environments-discover-behavior-specifications-q1|
|----|----|
|Title|competency&#32;question&#32;domains/manufacturing-environments/discover-behavior-specifications/q1.rq&#32;from&#32;branch&#32;main|
|Composition|- [Competency question manufacturing-environments/discover-behavior-specifications/q1](https://github.com/HyperAgents/hmas/blob/main/domains/manufacturing-environments/discover-behavior-specifications/q1.rq.ttl)|

#### Criterion detail
|Identifier|[uri-validity](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#uri-validity)|
|----|----|
|Title|URI&#32;validity&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;check&#32;if&#32;all&#32;the&#32;URIs&#32;of&#32;the&#32;resource&#32;are&#32;well-formed|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-92)|Identifier|`invalid-uri`|
|[Section top](#pass-outcome-number-92)|Title|All&#32;subject&#32;URI&#32;valid|
|[Section top](#pass-outcome-number-92)|Description|All&#32;the&#32;URIs&#32;of&#32;the&#32;subject&#32;are&#32;valid|

***
### Pass Outcome number 93

[Jump to summary definition](#summary-Pass-93)	|	[Previous Pass outcome](#pass-outcome-number-92)	|	[Next Pass outcome](#pass-outcome-number-94)

:white_check_mark:Pass outcome
#### Subject detail
|Name|question-logistics-structure-organization-q6|
|----|----|
|Title|competency&#32;question&#32;domains/logistics/structure-organization/q6.rq&#32;from&#32;branch&#32;main|
|Composition|- [Competency question logistics/structure-organization/q6](https://github.com/HyperAgents/hmas/blob/main/domains/logistics/structure-organization/q6.rq.ttl)|

#### Criterion detail
|Identifier|[namespace-validity](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#namespace-validity)|
|----|----|
|Title|Prefix&#32;validity&#32;test|
|Description|A&#32;test&#32;case&#32;checking&#32;if&#32;all&#32;the&#32;prefixes&#32;are&#32;not&#32;too&#32;close&#32;from&#32;the&#32;most&#32;used&#32;existing&#32;namespaces&#32;(according&#32;to&#32;prefix&#32;cc)&#32;or&#32;an&#32;ontology&#32;namespace|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-93)|Identifier|`namespace-typo`|
|[Section top](#pass-outcome-number-93)|Title|No&#32;namespace&#32;typo|
|[Section top](#pass-outcome-number-93)|Description|It&#32;seems&#32;that&#32;none&#32;of&#32;the&#32;subject&#32;URIs&#32;have&#32;namespaces&#32;typos|

***
### Pass Outcome number 94

[Jump to summary definition](#summary-Pass-94)	|	[Previous Pass outcome](#pass-outcome-number-93)	|	[Next Pass outcome](#pass-outcome-number-95)

:white_check_mark:Pass outcome
#### Subject detail
|Name|question-logistics-structure-organization-q6|
|----|----|
|Title|competency&#32;question&#32;domains/logistics/structure-organization/q6.rq&#32;from&#32;branch&#32;main|
|Composition|- [Competency question logistics/structure-organization/q6](https://github.com/HyperAgents/hmas/blob/main/domains/logistics/structure-organization/q6.rq.ttl)|

#### Criterion detail
|Identifier|[query-type](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#query-type)|
|----|----|
|Title|Query&#32;type&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;check&#32;if&#32;the&#32;query&#32;is&#32;indeed&#32;of&#32;type&#32;Select&#32;or&#32;Ask|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-94)|Identifier|`wrong-query-type`|
|[Section top](#pass-outcome-number-94)|Title|Accurate&#32;query&#32;type|
|[Section top](#pass-outcome-number-94)|Description|The&#32;query&#32;is&#32;of&#32;type&#32;Select&#32;or&#32;Ask|

***
### Pass Outcome number 95

[Jump to summary definition](#summary-Pass-95)	|	[Previous Pass outcome](#pass-outcome-number-94)	|	[Next Pass outcome](#pass-outcome-number-96)

:white_check_mark:Pass outcome
#### Subject detail
|Name|question-logistics-structure-organization-q6|
|----|----|
|Title|competency&#32;question&#32;domains/logistics/structure-organization/q6.rq&#32;from&#32;branch&#32;main|
|Composition|- [Competency question logistics/structure-organization/q6](https://github.com/HyperAgents/hmas/blob/main/domains/logistics/structure-organization/q6.rq.ttl)|

#### Criterion detail
|Identifier|[syntax](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#syntax)|
|----|----|
|Title|Syntax&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;check&#32;wether&#32;the&#32;test&#32;subject&#32;is&#32;syntaxically&#32;correct&#32;or&#32;not.|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-95)|Identifier|`syntax-error`|
|[Section top](#pass-outcome-number-95)|Title|Correct&#32;syntax|
|[Section top](#pass-outcome-number-95)|Description|Test&#32;subject&#32;has&#32;a&#32;correct&#32;syntax|

***
### Pass Outcome number 96

[Jump to summary definition](#summary-Pass-96)	|	[Previous Pass outcome](#pass-outcome-number-95)	|	[Next Pass outcome](#pass-outcome-number-97)

:white_check_mark:Pass outcome
#### Subject detail
|Name|question-logistics-structure-organization-q6|
|----|----|
|Title|competency&#32;question&#32;domains/logistics/structure-organization/q6.rq&#32;from&#32;branch&#32;main|
|Composition|- [Competency question logistics/structure-organization/q6](https://github.com/HyperAgents/hmas/blob/main/domains/logistics/structure-organization/q6.rq.ttl)|

#### Criterion detail
|Identifier|[uri-validity](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#uri-validity)|
|----|----|
|Title|URI&#32;validity&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;check&#32;if&#32;all&#32;the&#32;URIs&#32;of&#32;the&#32;resource&#32;are&#32;well-formed|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-96)|Identifier|`invalid-uri`|
|[Section top](#pass-outcome-number-96)|Title|All&#32;subject&#32;URI&#32;valid|
|[Section top](#pass-outcome-number-96)|Description|All&#32;the&#32;URIs&#32;of&#32;the&#32;subject&#32;are&#32;valid|

***
### Pass Outcome number 97

[Jump to summary definition](#summary-Pass-97)	|	[Previous Pass outcome](#pass-outcome-number-96)	|	[Next Pass outcome](#pass-outcome-number-98)

:white_check_mark:Pass outcome
#### Subject detail
|Name|question-logistics-structure-organization-q5|
|----|----|
|Title|competency&#32;question&#32;domains/logistics/structure-organization/q5.rq&#32;from&#32;branch&#32;main|
|Composition|- [Competency question logistics/structure-organization/q5](https://github.com/HyperAgents/hmas/blob/main/domains/logistics/structure-organization/q5.rq.ttl)|

#### Criterion detail
|Identifier|[namespace-validity](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#namespace-validity)|
|----|----|
|Title|Prefix&#32;validity&#32;test|
|Description|A&#32;test&#32;case&#32;checking&#32;if&#32;all&#32;the&#32;prefixes&#32;are&#32;not&#32;too&#32;close&#32;from&#32;the&#32;most&#32;used&#32;existing&#32;namespaces&#32;(according&#32;to&#32;prefix&#32;cc)&#32;or&#32;an&#32;ontology&#32;namespace|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-97)|Identifier|`namespace-typo`|
|[Section top](#pass-outcome-number-97)|Title|No&#32;namespace&#32;typo|
|[Section top](#pass-outcome-number-97)|Description|It&#32;seems&#32;that&#32;none&#32;of&#32;the&#32;subject&#32;URIs&#32;have&#32;namespaces&#32;typos|

***
### Pass Outcome number 98

[Jump to summary definition](#summary-Pass-98)	|	[Previous Pass outcome](#pass-outcome-number-97)	|	[Next Pass outcome](#pass-outcome-number-99)

:white_check_mark:Pass outcome
#### Subject detail
|Name|question-logistics-structure-organization-q5|
|----|----|
|Title|competency&#32;question&#32;domains/logistics/structure-organization/q5.rq&#32;from&#32;branch&#32;main|
|Composition|- [Competency question logistics/structure-organization/q5](https://github.com/HyperAgents/hmas/blob/main/domains/logistics/structure-organization/q5.rq.ttl)|

#### Criterion detail
|Identifier|[query-type](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#query-type)|
|----|----|
|Title|Query&#32;type&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;check&#32;if&#32;the&#32;query&#32;is&#32;indeed&#32;of&#32;type&#32;Select&#32;or&#32;Ask|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-98)|Identifier|`wrong-query-type`|
|[Section top](#pass-outcome-number-98)|Title|Accurate&#32;query&#32;type|
|[Section top](#pass-outcome-number-98)|Description|The&#32;query&#32;is&#32;of&#32;type&#32;Select&#32;or&#32;Ask|

***
### Pass Outcome number 99

[Jump to summary definition](#summary-Pass-99)	|	[Previous Pass outcome](#pass-outcome-number-98)	|	[Next Pass outcome](#pass-outcome-number-100)

:white_check_mark:Pass outcome
#### Subject detail
|Name|question-logistics-structure-organization-q5|
|----|----|
|Title|competency&#32;question&#32;domains/logistics/structure-organization/q5.rq&#32;from&#32;branch&#32;main|
|Composition|- [Competency question logistics/structure-organization/q5](https://github.com/HyperAgents/hmas/blob/main/domains/logistics/structure-organization/q5.rq.ttl)|

#### Criterion detail
|Identifier|[syntax](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#syntax)|
|----|----|
|Title|Syntax&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;check&#32;wether&#32;the&#32;test&#32;subject&#32;is&#32;syntaxically&#32;correct&#32;or&#32;not.|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-99)|Identifier|`syntax-error`|
|[Section top](#pass-outcome-number-99)|Title|Correct&#32;syntax|
|[Section top](#pass-outcome-number-99)|Description|Test&#32;subject&#32;has&#32;a&#32;correct&#32;syntax|

***
### Pass Outcome number 100

[Jump to summary definition](#summary-Pass-100)	|	[Previous Pass outcome](#pass-outcome-number-99)	|	[Next Pass outcome](#pass-outcome-number-101)

:white_check_mark:Pass outcome
#### Subject detail
|Name|question-logistics-structure-organization-q5|
|----|----|
|Title|competency&#32;question&#32;domains/logistics/structure-organization/q5.rq&#32;from&#32;branch&#32;main|
|Composition|- [Competency question logistics/structure-organization/q5](https://github.com/HyperAgents/hmas/blob/main/domains/logistics/structure-organization/q5.rq.ttl)|

#### Criterion detail
|Identifier|[uri-validity](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#uri-validity)|
|----|----|
|Title|URI&#32;validity&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;check&#32;if&#32;all&#32;the&#32;URIs&#32;of&#32;the&#32;resource&#32;are&#32;well-formed|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-100)|Identifier|`invalid-uri`|
|[Section top](#pass-outcome-number-100)|Title|All&#32;subject&#32;URI&#32;valid|
|[Section top](#pass-outcome-number-100)|Description|All&#32;the&#32;URIs&#32;of&#32;the&#32;subject&#32;are&#32;valid|

***
### Pass Outcome number 101

[Jump to summary definition](#summary-Pass-101)	|	[Previous Pass outcome](#pass-outcome-number-100)	|	[Next Pass outcome](#pass-outcome-number-102)

:white_check_mark:Pass outcome
#### Subject detail
|Name|question-logistics-structure-organization-q4|
|----|----|
|Title|competency&#32;question&#32;domains/logistics/structure-organization/q4.rq&#32;from&#32;branch&#32;main|
|Composition|- [Competency question logistics/structure-organization/q4](https://github.com/HyperAgents/hmas/blob/main/domains/logistics/structure-organization/q4.rq.ttl)|

#### Criterion detail
|Identifier|[namespace-validity](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#namespace-validity)|
|----|----|
|Title|Prefix&#32;validity&#32;test|
|Description|A&#32;test&#32;case&#32;checking&#32;if&#32;all&#32;the&#32;prefixes&#32;are&#32;not&#32;too&#32;close&#32;from&#32;the&#32;most&#32;used&#32;existing&#32;namespaces&#32;(according&#32;to&#32;prefix&#32;cc)&#32;or&#32;an&#32;ontology&#32;namespace|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-101)|Identifier|`namespace-typo`|
|[Section top](#pass-outcome-number-101)|Title|No&#32;namespace&#32;typo|
|[Section top](#pass-outcome-number-101)|Description|It&#32;seems&#32;that&#32;none&#32;of&#32;the&#32;subject&#32;URIs&#32;have&#32;namespaces&#32;typos|

***
### Pass Outcome number 102

[Jump to summary definition](#summary-Pass-102)	|	[Previous Pass outcome](#pass-outcome-number-101)	|	[Next Pass outcome](#pass-outcome-number-103)

:white_check_mark:Pass outcome
#### Subject detail
|Name|question-logistics-structure-organization-q4|
|----|----|
|Title|competency&#32;question&#32;domains/logistics/structure-organization/q4.rq&#32;from&#32;branch&#32;main|
|Composition|- [Competency question logistics/structure-organization/q4](https://github.com/HyperAgents/hmas/blob/main/domains/logistics/structure-organization/q4.rq.ttl)|

#### Criterion detail
|Identifier|[query-type](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#query-type)|
|----|----|
|Title|Query&#32;type&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;check&#32;if&#32;the&#32;query&#32;is&#32;indeed&#32;of&#32;type&#32;Select&#32;or&#32;Ask|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-102)|Identifier|`wrong-query-type`|
|[Section top](#pass-outcome-number-102)|Title|Accurate&#32;query&#32;type|
|[Section top](#pass-outcome-number-102)|Description|The&#32;query&#32;is&#32;of&#32;type&#32;Select&#32;or&#32;Ask|

***
### Pass Outcome number 103

[Jump to summary definition](#summary-Pass-103)	|	[Previous Pass outcome](#pass-outcome-number-102)	|	[Next Pass outcome](#pass-outcome-number-104)

:white_check_mark:Pass outcome
#### Subject detail
|Name|question-logistics-structure-organization-q4|
|----|----|
|Title|competency&#32;question&#32;domains/logistics/structure-organization/q4.rq&#32;from&#32;branch&#32;main|
|Composition|- [Competency question logistics/structure-organization/q4](https://github.com/HyperAgents/hmas/blob/main/domains/logistics/structure-organization/q4.rq.ttl)|

#### Criterion detail
|Identifier|[syntax](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#syntax)|
|----|----|
|Title|Syntax&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;check&#32;wether&#32;the&#32;test&#32;subject&#32;is&#32;syntaxically&#32;correct&#32;or&#32;not.|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-103)|Identifier|`syntax-error`|
|[Section top](#pass-outcome-number-103)|Title|Correct&#32;syntax|
|[Section top](#pass-outcome-number-103)|Description|Test&#32;subject&#32;has&#32;a&#32;correct&#32;syntax|

***
### Pass Outcome number 104

[Jump to summary definition](#summary-Pass-104)	|	[Previous Pass outcome](#pass-outcome-number-103)	|	[Next Pass outcome](#pass-outcome-number-105)

:white_check_mark:Pass outcome
#### Subject detail
|Name|question-logistics-structure-organization-q4|
|----|----|
|Title|competency&#32;question&#32;domains/logistics/structure-organization/q4.rq&#32;from&#32;branch&#32;main|
|Composition|- [Competency question logistics/structure-organization/q4](https://github.com/HyperAgents/hmas/blob/main/domains/logistics/structure-organization/q4.rq.ttl)|

#### Criterion detail
|Identifier|[uri-validity](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#uri-validity)|
|----|----|
|Title|URI&#32;validity&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;check&#32;if&#32;all&#32;the&#32;URIs&#32;of&#32;the&#32;resource&#32;are&#32;well-formed|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-104)|Identifier|`invalid-uri`|
|[Section top](#pass-outcome-number-104)|Title|All&#32;subject&#32;URI&#32;valid|
|[Section top](#pass-outcome-number-104)|Description|All&#32;the&#32;URIs&#32;of&#32;the&#32;subject&#32;are&#32;valid|

***
### Pass Outcome number 105

[Jump to summary definition](#summary-Pass-105)	|	[Previous Pass outcome](#pass-outcome-number-104)	|	[Next Pass outcome](#pass-outcome-number-106)

:white_check_mark:Pass outcome
#### Subject detail
|Name|question-logistics-structure-organization-q3|
|----|----|
|Title|competency&#32;question&#32;domains/logistics/structure-organization/q3.rq&#32;from&#32;branch&#32;main|
|Composition|- [Competency question logistics/structure-organization/q3](https://github.com/HyperAgents/hmas/blob/main/domains/logistics/structure-organization/q3.rq.ttl)|

#### Criterion detail
|Identifier|[namespace-validity](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#namespace-validity)|
|----|----|
|Title|Prefix&#32;validity&#32;test|
|Description|A&#32;test&#32;case&#32;checking&#32;if&#32;all&#32;the&#32;prefixes&#32;are&#32;not&#32;too&#32;close&#32;from&#32;the&#32;most&#32;used&#32;existing&#32;namespaces&#32;(according&#32;to&#32;prefix&#32;cc)&#32;or&#32;an&#32;ontology&#32;namespace|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-105)|Identifier|`namespace-typo`|
|[Section top](#pass-outcome-number-105)|Title|No&#32;namespace&#32;typo|
|[Section top](#pass-outcome-number-105)|Description|It&#32;seems&#32;that&#32;none&#32;of&#32;the&#32;subject&#32;URIs&#32;have&#32;namespaces&#32;typos|

***
### Pass Outcome number 106

[Jump to summary definition](#summary-Pass-106)	|	[Previous Pass outcome](#pass-outcome-number-105)	|	[Next Pass outcome](#pass-outcome-number-107)

:white_check_mark:Pass outcome
#### Subject detail
|Name|question-logistics-structure-organization-q3|
|----|----|
|Title|competency&#32;question&#32;domains/logistics/structure-organization/q3.rq&#32;from&#32;branch&#32;main|
|Composition|- [Competency question logistics/structure-organization/q3](https://github.com/HyperAgents/hmas/blob/main/domains/logistics/structure-organization/q3.rq.ttl)|

#### Criterion detail
|Identifier|[query-type](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#query-type)|
|----|----|
|Title|Query&#32;type&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;check&#32;if&#32;the&#32;query&#32;is&#32;indeed&#32;of&#32;type&#32;Select&#32;or&#32;Ask|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-106)|Identifier|`wrong-query-type`|
|[Section top](#pass-outcome-number-106)|Title|Accurate&#32;query&#32;type|
|[Section top](#pass-outcome-number-106)|Description|The&#32;query&#32;is&#32;of&#32;type&#32;Select&#32;or&#32;Ask|

***
### Pass Outcome number 107

[Jump to summary definition](#summary-Pass-107)	|	[Previous Pass outcome](#pass-outcome-number-106)	|	[Next Pass outcome](#pass-outcome-number-108)

:white_check_mark:Pass outcome
#### Subject detail
|Name|question-logistics-structure-organization-q3|
|----|----|
|Title|competency&#32;question&#32;domains/logistics/structure-organization/q3.rq&#32;from&#32;branch&#32;main|
|Composition|- [Competency question logistics/structure-organization/q3](https://github.com/HyperAgents/hmas/blob/main/domains/logistics/structure-organization/q3.rq.ttl)|

#### Criterion detail
|Identifier|[syntax](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#syntax)|
|----|----|
|Title|Syntax&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;check&#32;wether&#32;the&#32;test&#32;subject&#32;is&#32;syntaxically&#32;correct&#32;or&#32;not.|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-107)|Identifier|`syntax-error`|
|[Section top](#pass-outcome-number-107)|Title|Correct&#32;syntax|
|[Section top](#pass-outcome-number-107)|Description|Test&#32;subject&#32;has&#32;a&#32;correct&#32;syntax|

***
### Pass Outcome number 108

[Jump to summary definition](#summary-Pass-108)	|	[Previous Pass outcome](#pass-outcome-number-107)	|	[Next Pass outcome](#pass-outcome-number-109)

:white_check_mark:Pass outcome
#### Subject detail
|Name|question-logistics-structure-organization-q3|
|----|----|
|Title|competency&#32;question&#32;domains/logistics/structure-organization/q3.rq&#32;from&#32;branch&#32;main|
|Composition|- [Competency question logistics/structure-organization/q3](https://github.com/HyperAgents/hmas/blob/main/domains/logistics/structure-organization/q3.rq.ttl)|

#### Criterion detail
|Identifier|[uri-validity](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#uri-validity)|
|----|----|
|Title|URI&#32;validity&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;check&#32;if&#32;all&#32;the&#32;URIs&#32;of&#32;the&#32;resource&#32;are&#32;well-formed|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-108)|Identifier|`invalid-uri`|
|[Section top](#pass-outcome-number-108)|Title|All&#32;subject&#32;URI&#32;valid|
|[Section top](#pass-outcome-number-108)|Description|All&#32;the&#32;URIs&#32;of&#32;the&#32;subject&#32;are&#32;valid|

***
### Pass Outcome number 109

[Jump to summary definition](#summary-Pass-109)	|	[Previous Pass outcome](#pass-outcome-number-108)	|	[Next Pass outcome](#pass-outcome-number-110)

:white_check_mark:Pass outcome
#### Subject detail
|Name|question-logistics-structure-organization-q2|
|----|----|
|Title|competency&#32;question&#32;domains/logistics/structure-organization/q2.rq&#32;from&#32;branch&#32;main|
|Composition|- [Competency question logistics/structure-organization/q2](https://github.com/HyperAgents/hmas/blob/main/domains/logistics/structure-organization/q2.rq.ttl)|

#### Criterion detail
|Identifier|[namespace-validity](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#namespace-validity)|
|----|----|
|Title|Prefix&#32;validity&#32;test|
|Description|A&#32;test&#32;case&#32;checking&#32;if&#32;all&#32;the&#32;prefixes&#32;are&#32;not&#32;too&#32;close&#32;from&#32;the&#32;most&#32;used&#32;existing&#32;namespaces&#32;(according&#32;to&#32;prefix&#32;cc)&#32;or&#32;an&#32;ontology&#32;namespace|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-109)|Identifier|`namespace-typo`|
|[Section top](#pass-outcome-number-109)|Title|No&#32;namespace&#32;typo|
|[Section top](#pass-outcome-number-109)|Description|It&#32;seems&#32;that&#32;none&#32;of&#32;the&#32;subject&#32;URIs&#32;have&#32;namespaces&#32;typos|

***
### Pass Outcome number 110

[Jump to summary definition](#summary-Pass-110)	|	[Previous Pass outcome](#pass-outcome-number-109)	|	[Next Pass outcome](#pass-outcome-number-111)

:white_check_mark:Pass outcome
#### Subject detail
|Name|question-logistics-structure-organization-q2|
|----|----|
|Title|competency&#32;question&#32;domains/logistics/structure-organization/q2.rq&#32;from&#32;branch&#32;main|
|Composition|- [Competency question logistics/structure-organization/q2](https://github.com/HyperAgents/hmas/blob/main/domains/logistics/structure-organization/q2.rq.ttl)|

#### Criterion detail
|Identifier|[query-type](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#query-type)|
|----|----|
|Title|Query&#32;type&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;check&#32;if&#32;the&#32;query&#32;is&#32;indeed&#32;of&#32;type&#32;Select&#32;or&#32;Ask|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-110)|Identifier|`wrong-query-type`|
|[Section top](#pass-outcome-number-110)|Title|Accurate&#32;query&#32;type|
|[Section top](#pass-outcome-number-110)|Description|The&#32;query&#32;is&#32;of&#32;type&#32;Select&#32;or&#32;Ask|

***
### Pass Outcome number 111

[Jump to summary definition](#summary-Pass-111)	|	[Previous Pass outcome](#pass-outcome-number-110)	|	[Next Pass outcome](#pass-outcome-number-112)

:white_check_mark:Pass outcome
#### Subject detail
|Name|question-logistics-structure-organization-q2|
|----|----|
|Title|competency&#32;question&#32;domains/logistics/structure-organization/q2.rq&#32;from&#32;branch&#32;main|
|Composition|- [Competency question logistics/structure-organization/q2](https://github.com/HyperAgents/hmas/blob/main/domains/logistics/structure-organization/q2.rq.ttl)|

#### Criterion detail
|Identifier|[syntax](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#syntax)|
|----|----|
|Title|Syntax&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;check&#32;wether&#32;the&#32;test&#32;subject&#32;is&#32;syntaxically&#32;correct&#32;or&#32;not.|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-111)|Identifier|`syntax-error`|
|[Section top](#pass-outcome-number-111)|Title|Correct&#32;syntax|
|[Section top](#pass-outcome-number-111)|Description|Test&#32;subject&#32;has&#32;a&#32;correct&#32;syntax|

***
### Pass Outcome number 112

[Jump to summary definition](#summary-Pass-112)	|	[Previous Pass outcome](#pass-outcome-number-111)	|	[Next Pass outcome](#pass-outcome-number-113)

:white_check_mark:Pass outcome
#### Subject detail
|Name|question-logistics-structure-organization-q2|
|----|----|
|Title|competency&#32;question&#32;domains/logistics/structure-organization/q2.rq&#32;from&#32;branch&#32;main|
|Composition|- [Competency question logistics/structure-organization/q2](https://github.com/HyperAgents/hmas/blob/main/domains/logistics/structure-organization/q2.rq.ttl)|

#### Criterion detail
|Identifier|[uri-validity](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#uri-validity)|
|----|----|
|Title|URI&#32;validity&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;check&#32;if&#32;all&#32;the&#32;URIs&#32;of&#32;the&#32;resource&#32;are&#32;well-formed|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-112)|Identifier|`invalid-uri`|
|[Section top](#pass-outcome-number-112)|Title|All&#32;subject&#32;URI&#32;valid|
|[Section top](#pass-outcome-number-112)|Description|All&#32;the&#32;URIs&#32;of&#32;the&#32;subject&#32;are&#32;valid|

***
### Pass Outcome number 113

[Jump to summary definition](#summary-Pass-113)	|	[Previous Pass outcome](#pass-outcome-number-112)	|	[Next Pass outcome](#pass-outcome-number-114)

:white_check_mark:Pass outcome
#### Subject detail
|Name|question-logistics-structure-organization-q1|
|----|----|
|Title|competency&#32;question&#32;domains/logistics/structure-organization/q1.rq&#32;from&#32;branch&#32;main|
|Composition|- [Competency question logistics/structure-organization/q1](https://github.com/HyperAgents/hmas/blob/main/domains/logistics/structure-organization/q1.rq.ttl)|

#### Criterion detail
|Identifier|[namespace-validity](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#namespace-validity)|
|----|----|
|Title|Prefix&#32;validity&#32;test|
|Description|A&#32;test&#32;case&#32;checking&#32;if&#32;all&#32;the&#32;prefixes&#32;are&#32;not&#32;too&#32;close&#32;from&#32;the&#32;most&#32;used&#32;existing&#32;namespaces&#32;(according&#32;to&#32;prefix&#32;cc)&#32;or&#32;an&#32;ontology&#32;namespace|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-113)|Identifier|`namespace-typo`|
|[Section top](#pass-outcome-number-113)|Title|No&#32;namespace&#32;typo|
|[Section top](#pass-outcome-number-113)|Description|It&#32;seems&#32;that&#32;none&#32;of&#32;the&#32;subject&#32;URIs&#32;have&#32;namespaces&#32;typos|

***
### Pass Outcome number 114

[Jump to summary definition](#summary-Pass-114)	|	[Previous Pass outcome](#pass-outcome-number-113)	|	[Next Pass outcome](#pass-outcome-number-115)

:white_check_mark:Pass outcome
#### Subject detail
|Name|question-logistics-structure-organization-q1|
|----|----|
|Title|competency&#32;question&#32;domains/logistics/structure-organization/q1.rq&#32;from&#32;branch&#32;main|
|Composition|- [Competency question logistics/structure-organization/q1](https://github.com/HyperAgents/hmas/blob/main/domains/logistics/structure-organization/q1.rq.ttl)|

#### Criterion detail
|Identifier|[query-type](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#query-type)|
|----|----|
|Title|Query&#32;type&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;check&#32;if&#32;the&#32;query&#32;is&#32;indeed&#32;of&#32;type&#32;Select&#32;or&#32;Ask|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-114)|Identifier|`wrong-query-type`|
|[Section top](#pass-outcome-number-114)|Title|Accurate&#32;query&#32;type|
|[Section top](#pass-outcome-number-114)|Description|The&#32;query&#32;is&#32;of&#32;type&#32;Select&#32;or&#32;Ask|

***
### Pass Outcome number 115

[Jump to summary definition](#summary-Pass-115)	|	[Previous Pass outcome](#pass-outcome-number-114)	|	[Next Pass outcome](#pass-outcome-number-116)

:white_check_mark:Pass outcome
#### Subject detail
|Name|question-logistics-structure-organization-q1|
|----|----|
|Title|competency&#32;question&#32;domains/logistics/structure-organization/q1.rq&#32;from&#32;branch&#32;main|
|Composition|- [Competency question logistics/structure-organization/q1](https://github.com/HyperAgents/hmas/blob/main/domains/logistics/structure-organization/q1.rq.ttl)|

#### Criterion detail
|Identifier|[syntax](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#syntax)|
|----|----|
|Title|Syntax&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;check&#32;wether&#32;the&#32;test&#32;subject&#32;is&#32;syntaxically&#32;correct&#32;or&#32;not.|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-115)|Identifier|`syntax-error`|
|[Section top](#pass-outcome-number-115)|Title|Correct&#32;syntax|
|[Section top](#pass-outcome-number-115)|Description|Test&#32;subject&#32;has&#32;a&#32;correct&#32;syntax|

***
### Pass Outcome number 116

[Jump to summary definition](#summary-Pass-116)	|	[Previous Pass outcome](#pass-outcome-number-115)	|	[Next Pass outcome](#pass-outcome-number-117)

:white_check_mark:Pass outcome
#### Subject detail
|Name|question-logistics-structure-organization-q1|
|----|----|
|Title|competency&#32;question&#32;domains/logistics/structure-organization/q1.rq&#32;from&#32;branch&#32;main|
|Composition|- [Competency question logistics/structure-organization/q1](https://github.com/HyperAgents/hmas/blob/main/domains/logistics/structure-organization/q1.rq.ttl)|

#### Criterion detail
|Identifier|[uri-validity](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#uri-validity)|
|----|----|
|Title|URI&#32;validity&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;check&#32;if&#32;all&#32;the&#32;URIs&#32;of&#32;the&#32;resource&#32;are&#32;well-formed|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-116)|Identifier|`invalid-uri`|
|[Section top](#pass-outcome-number-116)|Title|All&#32;subject&#32;URI&#32;valid|
|[Section top](#pass-outcome-number-116)|Description|All&#32;the&#32;URIs&#32;of&#32;the&#32;subject&#32;are&#32;valid|

***
### Pass Outcome number 117

[Jump to summary definition](#summary-Pass-117)	|	[Previous Pass outcome](#pass-outcome-number-116)	|	[Next Pass outcome](#pass-outcome-number-118)

:white_check_mark:Pass outcome
#### Subject detail
|Name|question-logistics-create-organization-q9|
|----|----|
|Title|competency&#32;question&#32;domains/logistics/create-organization/q9.rq&#32;from&#32;branch&#32;main|
|Composition|- [Competency question logistics/create-organization/q9](https://github.com/HyperAgents/hmas/blob/main/domains/logistics/create-organization/q9.rq.ttl)|

#### Criterion detail
|Identifier|[namespace-validity](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#namespace-validity)|
|----|----|
|Title|Prefix&#32;validity&#32;test|
|Description|A&#32;test&#32;case&#32;checking&#32;if&#32;all&#32;the&#32;prefixes&#32;are&#32;not&#32;too&#32;close&#32;from&#32;the&#32;most&#32;used&#32;existing&#32;namespaces&#32;(according&#32;to&#32;prefix&#32;cc)&#32;or&#32;an&#32;ontology&#32;namespace|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-117)|Identifier|`namespace-typo`|
|[Section top](#pass-outcome-number-117)|Title|No&#32;namespace&#32;typo|
|[Section top](#pass-outcome-number-117)|Description|It&#32;seems&#32;that&#32;none&#32;of&#32;the&#32;subject&#32;URIs&#32;have&#32;namespaces&#32;typos|

***
### Pass Outcome number 118

[Jump to summary definition](#summary-Pass-118)	|	[Previous Pass outcome](#pass-outcome-number-117)	|	[Next Pass outcome](#pass-outcome-number-119)

:white_check_mark:Pass outcome
#### Subject detail
|Name|question-logistics-create-organization-q9|
|----|----|
|Title|competency&#32;question&#32;domains/logistics/create-organization/q9.rq&#32;from&#32;branch&#32;main|
|Composition|- [Competency question logistics/create-organization/q9](https://github.com/HyperAgents/hmas/blob/main/domains/logistics/create-organization/q9.rq.ttl)|

#### Criterion detail
|Identifier|[query-type](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#query-type)|
|----|----|
|Title|Query&#32;type&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;check&#32;if&#32;the&#32;query&#32;is&#32;indeed&#32;of&#32;type&#32;Select&#32;or&#32;Ask|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-118)|Identifier|`wrong-query-type`|
|[Section top](#pass-outcome-number-118)|Title|Accurate&#32;query&#32;type|
|[Section top](#pass-outcome-number-118)|Description|The&#32;query&#32;is&#32;of&#32;type&#32;Select&#32;or&#32;Ask|

***
### Pass Outcome number 119

[Jump to summary definition](#summary-Pass-119)	|	[Previous Pass outcome](#pass-outcome-number-118)	|	[Next Pass outcome](#pass-outcome-number-120)

:white_check_mark:Pass outcome
#### Subject detail
|Name|question-logistics-create-organization-q9|
|----|----|
|Title|competency&#32;question&#32;domains/logistics/create-organization/q9.rq&#32;from&#32;branch&#32;main|
|Composition|- [Competency question logistics/create-organization/q9](https://github.com/HyperAgents/hmas/blob/main/domains/logistics/create-organization/q9.rq.ttl)|

#### Criterion detail
|Identifier|[syntax](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#syntax)|
|----|----|
|Title|Syntax&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;check&#32;wether&#32;the&#32;test&#32;subject&#32;is&#32;syntaxically&#32;correct&#32;or&#32;not.|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-119)|Identifier|`syntax-error`|
|[Section top](#pass-outcome-number-119)|Title|Correct&#32;syntax|
|[Section top](#pass-outcome-number-119)|Description|Test&#32;subject&#32;has&#32;a&#32;correct&#32;syntax|

***
### Pass Outcome number 120

[Jump to summary definition](#summary-Pass-120)	|	[Previous Pass outcome](#pass-outcome-number-119)	|	[Next Pass outcome](#pass-outcome-number-121)

:white_check_mark:Pass outcome
#### Subject detail
|Name|question-logistics-create-organization-q9|
|----|----|
|Title|competency&#32;question&#32;domains/logistics/create-organization/q9.rq&#32;from&#32;branch&#32;main|
|Composition|- [Competency question logistics/create-organization/q9](https://github.com/HyperAgents/hmas/blob/main/domains/logistics/create-organization/q9.rq.ttl)|

#### Criterion detail
|Identifier|[uri-validity](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#uri-validity)|
|----|----|
|Title|URI&#32;validity&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;check&#32;if&#32;all&#32;the&#32;URIs&#32;of&#32;the&#32;resource&#32;are&#32;well-formed|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-120)|Identifier|`invalid-uri`|
|[Section top](#pass-outcome-number-120)|Title|All&#32;subject&#32;URI&#32;valid|
|[Section top](#pass-outcome-number-120)|Description|All&#32;the&#32;URIs&#32;of&#32;the&#32;subject&#32;are&#32;valid|

***
### Pass Outcome number 121

[Jump to summary definition](#summary-Pass-121)	|	[Previous Pass outcome](#pass-outcome-number-120)	|	[Next Pass outcome](#pass-outcome-number-122)

:white_check_mark:Pass outcome
#### Subject detail
|Name|question-logistics-create-organization-q8|
|----|----|
|Title|competency&#32;question&#32;domains/logistics/create-organization/q8.rq&#32;from&#32;branch&#32;main|
|Composition|- [Competency question logistics/create-organization/q8](https://github.com/HyperAgents/hmas/blob/main/domains/logistics/create-organization/q8.rq.ttl)|

#### Criterion detail
|Identifier|[namespace-validity](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#namespace-validity)|
|----|----|
|Title|Prefix&#32;validity&#32;test|
|Description|A&#32;test&#32;case&#32;checking&#32;if&#32;all&#32;the&#32;prefixes&#32;are&#32;not&#32;too&#32;close&#32;from&#32;the&#32;most&#32;used&#32;existing&#32;namespaces&#32;(according&#32;to&#32;prefix&#32;cc)&#32;or&#32;an&#32;ontology&#32;namespace|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-121)|Identifier|`namespace-typo`|
|[Section top](#pass-outcome-number-121)|Title|No&#32;namespace&#32;typo|
|[Section top](#pass-outcome-number-121)|Description|It&#32;seems&#32;that&#32;none&#32;of&#32;the&#32;subject&#32;URIs&#32;have&#32;namespaces&#32;typos|

***
### Pass Outcome number 122

[Jump to summary definition](#summary-Pass-122)	|	[Previous Pass outcome](#pass-outcome-number-121)	|	[Next Pass outcome](#pass-outcome-number-123)

:white_check_mark:Pass outcome
#### Subject detail
|Name|question-logistics-create-organization-q8|
|----|----|
|Title|competency&#32;question&#32;domains/logistics/create-organization/q8.rq&#32;from&#32;branch&#32;main|
|Composition|- [Competency question logistics/create-organization/q8](https://github.com/HyperAgents/hmas/blob/main/domains/logistics/create-organization/q8.rq.ttl)|

#### Criterion detail
|Identifier|[query-type](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#query-type)|
|----|----|
|Title|Query&#32;type&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;check&#32;if&#32;the&#32;query&#32;is&#32;indeed&#32;of&#32;type&#32;Select&#32;or&#32;Ask|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-122)|Identifier|`wrong-query-type`|
|[Section top](#pass-outcome-number-122)|Title|Accurate&#32;query&#32;type|
|[Section top](#pass-outcome-number-122)|Description|The&#32;query&#32;is&#32;of&#32;type&#32;Select&#32;or&#32;Ask|

***
### Pass Outcome number 123

[Jump to summary definition](#summary-Pass-123)	|	[Previous Pass outcome](#pass-outcome-number-122)	|	[Next Pass outcome](#pass-outcome-number-124)

:white_check_mark:Pass outcome
#### Subject detail
|Name|question-logistics-create-organization-q8|
|----|----|
|Title|competency&#32;question&#32;domains/logistics/create-organization/q8.rq&#32;from&#32;branch&#32;main|
|Composition|- [Competency question logistics/create-organization/q8](https://github.com/HyperAgents/hmas/blob/main/domains/logistics/create-organization/q8.rq.ttl)|

#### Criterion detail
|Identifier|[syntax](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#syntax)|
|----|----|
|Title|Syntax&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;check&#32;wether&#32;the&#32;test&#32;subject&#32;is&#32;syntaxically&#32;correct&#32;or&#32;not.|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-123)|Identifier|`syntax-error`|
|[Section top](#pass-outcome-number-123)|Title|Correct&#32;syntax|
|[Section top](#pass-outcome-number-123)|Description|Test&#32;subject&#32;has&#32;a&#32;correct&#32;syntax|

***
### Pass Outcome number 124

[Jump to summary definition](#summary-Pass-124)	|	[Previous Pass outcome](#pass-outcome-number-123)	|	[Next Pass outcome](#pass-outcome-number-125)

:white_check_mark:Pass outcome
#### Subject detail
|Name|question-logistics-create-organization-q8|
|----|----|
|Title|competency&#32;question&#32;domains/logistics/create-organization/q8.rq&#32;from&#32;branch&#32;main|
|Composition|- [Competency question logistics/create-organization/q8](https://github.com/HyperAgents/hmas/blob/main/domains/logistics/create-organization/q8.rq.ttl)|

#### Criterion detail
|Identifier|[uri-validity](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#uri-validity)|
|----|----|
|Title|URI&#32;validity&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;check&#32;if&#32;all&#32;the&#32;URIs&#32;of&#32;the&#32;resource&#32;are&#32;well-formed|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-124)|Identifier|`invalid-uri`|
|[Section top](#pass-outcome-number-124)|Title|All&#32;subject&#32;URI&#32;valid|
|[Section top](#pass-outcome-number-124)|Description|All&#32;the&#32;URIs&#32;of&#32;the&#32;subject&#32;are&#32;valid|

***
### Pass Outcome number 125

[Jump to summary definition](#summary-Pass-125)	|	[Previous Pass outcome](#pass-outcome-number-124)	|	[Next Pass outcome](#pass-outcome-number-126)

:white_check_mark:Pass outcome
#### Subject detail
|Name|question-logistics-create-organization-q7|
|----|----|
|Title|competency&#32;question&#32;domains/logistics/create-organization/q7.rq&#32;from&#32;branch&#32;main|
|Composition|- [Competency question logistics/create-organization/q7](https://github.com/HyperAgents/hmas/blob/main/domains/logistics/create-organization/q7.rq.ttl)|

#### Criterion detail
|Identifier|[namespace-validity](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#namespace-validity)|
|----|----|
|Title|Prefix&#32;validity&#32;test|
|Description|A&#32;test&#32;case&#32;checking&#32;if&#32;all&#32;the&#32;prefixes&#32;are&#32;not&#32;too&#32;close&#32;from&#32;the&#32;most&#32;used&#32;existing&#32;namespaces&#32;(according&#32;to&#32;prefix&#32;cc)&#32;or&#32;an&#32;ontology&#32;namespace|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-125)|Identifier|`namespace-typo`|
|[Section top](#pass-outcome-number-125)|Title|No&#32;namespace&#32;typo|
|[Section top](#pass-outcome-number-125)|Description|It&#32;seems&#32;that&#32;none&#32;of&#32;the&#32;subject&#32;URIs&#32;have&#32;namespaces&#32;typos|

***
### Pass Outcome number 126

[Jump to summary definition](#summary-Pass-126)	|	[Previous Pass outcome](#pass-outcome-number-125)	|	[Next Pass outcome](#pass-outcome-number-127)

:white_check_mark:Pass outcome
#### Subject detail
|Name|question-logistics-create-organization-q7|
|----|----|
|Title|competency&#32;question&#32;domains/logistics/create-organization/q7.rq&#32;from&#32;branch&#32;main|
|Composition|- [Competency question logistics/create-organization/q7](https://github.com/HyperAgents/hmas/blob/main/domains/logistics/create-organization/q7.rq.ttl)|

#### Criterion detail
|Identifier|[query-type](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#query-type)|
|----|----|
|Title|Query&#32;type&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;check&#32;if&#32;the&#32;query&#32;is&#32;indeed&#32;of&#32;type&#32;Select&#32;or&#32;Ask|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-126)|Identifier|`wrong-query-type`|
|[Section top](#pass-outcome-number-126)|Title|Accurate&#32;query&#32;type|
|[Section top](#pass-outcome-number-126)|Description|The&#32;query&#32;is&#32;of&#32;type&#32;Select&#32;or&#32;Ask|

***
### Pass Outcome number 127

[Jump to summary definition](#summary-Pass-127)	|	[Previous Pass outcome](#pass-outcome-number-126)	|	[Next Pass outcome](#pass-outcome-number-128)

:white_check_mark:Pass outcome
#### Subject detail
|Name|question-logistics-create-organization-q7|
|----|----|
|Title|competency&#32;question&#32;domains/logistics/create-organization/q7.rq&#32;from&#32;branch&#32;main|
|Composition|- [Competency question logistics/create-organization/q7](https://github.com/HyperAgents/hmas/blob/main/domains/logistics/create-organization/q7.rq.ttl)|

#### Criterion detail
|Identifier|[syntax](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#syntax)|
|----|----|
|Title|Syntax&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;check&#32;wether&#32;the&#32;test&#32;subject&#32;is&#32;syntaxically&#32;correct&#32;or&#32;not.|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-127)|Identifier|`syntax-error`|
|[Section top](#pass-outcome-number-127)|Title|Correct&#32;syntax|
|[Section top](#pass-outcome-number-127)|Description|Test&#32;subject&#32;has&#32;a&#32;correct&#32;syntax|

***
### Pass Outcome number 128

[Jump to summary definition](#summary-Pass-128)	|	[Previous Pass outcome](#pass-outcome-number-127)	|	[Next Pass outcome](#pass-outcome-number-129)

:white_check_mark:Pass outcome
#### Subject detail
|Name|question-logistics-create-organization-q7|
|----|----|
|Title|competency&#32;question&#32;domains/logistics/create-organization/q7.rq&#32;from&#32;branch&#32;main|
|Composition|- [Competency question logistics/create-organization/q7](https://github.com/HyperAgents/hmas/blob/main/domains/logistics/create-organization/q7.rq.ttl)|

#### Criterion detail
|Identifier|[uri-validity](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#uri-validity)|
|----|----|
|Title|URI&#32;validity&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;check&#32;if&#32;all&#32;the&#32;URIs&#32;of&#32;the&#32;resource&#32;are&#32;well-formed|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-128)|Identifier|`invalid-uri`|
|[Section top](#pass-outcome-number-128)|Title|All&#32;subject&#32;URI&#32;valid|
|[Section top](#pass-outcome-number-128)|Description|All&#32;the&#32;URIs&#32;of&#32;the&#32;subject&#32;are&#32;valid|

***
### Pass Outcome number 129

[Jump to summary definition](#summary-Pass-129)	|	[Previous Pass outcome](#pass-outcome-number-128)	|	[Next Pass outcome](#pass-outcome-number-130)

:white_check_mark:Pass outcome
#### Subject detail
|Name|question-logistics-create-organization-q6|
|----|----|
|Title|competency&#32;question&#32;domains/logistics/create-organization/q6.rq&#32;from&#32;branch&#32;main|
|Composition|- [Competency question logistics/create-organization/q6](https://github.com/HyperAgents/hmas/blob/main/domains/logistics/create-organization/q6.rq.ttl)|

#### Criterion detail
|Identifier|[namespace-validity](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#namespace-validity)|
|----|----|
|Title|Prefix&#32;validity&#32;test|
|Description|A&#32;test&#32;case&#32;checking&#32;if&#32;all&#32;the&#32;prefixes&#32;are&#32;not&#32;too&#32;close&#32;from&#32;the&#32;most&#32;used&#32;existing&#32;namespaces&#32;(according&#32;to&#32;prefix&#32;cc)&#32;or&#32;an&#32;ontology&#32;namespace|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-129)|Identifier|`namespace-typo`|
|[Section top](#pass-outcome-number-129)|Title|No&#32;namespace&#32;typo|
|[Section top](#pass-outcome-number-129)|Description|It&#32;seems&#32;that&#32;none&#32;of&#32;the&#32;subject&#32;URIs&#32;have&#32;namespaces&#32;typos|

***
### Pass Outcome number 130

[Jump to summary definition](#summary-Pass-130)	|	[Previous Pass outcome](#pass-outcome-number-129)	|	[Next Pass outcome](#pass-outcome-number-131)

:white_check_mark:Pass outcome
#### Subject detail
|Name|question-logistics-create-organization-q6|
|----|----|
|Title|competency&#32;question&#32;domains/logistics/create-organization/q6.rq&#32;from&#32;branch&#32;main|
|Composition|- [Competency question logistics/create-organization/q6](https://github.com/HyperAgents/hmas/blob/main/domains/logistics/create-organization/q6.rq.ttl)|

#### Criterion detail
|Identifier|[query-type](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#query-type)|
|----|----|
|Title|Query&#32;type&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;check&#32;if&#32;the&#32;query&#32;is&#32;indeed&#32;of&#32;type&#32;Select&#32;or&#32;Ask|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-130)|Identifier|`wrong-query-type`|
|[Section top](#pass-outcome-number-130)|Title|Accurate&#32;query&#32;type|
|[Section top](#pass-outcome-number-130)|Description|The&#32;query&#32;is&#32;of&#32;type&#32;Select&#32;or&#32;Ask|

***
### Pass Outcome number 131

[Jump to summary definition](#summary-Pass-131)	|	[Previous Pass outcome](#pass-outcome-number-130)	|	[Next Pass outcome](#pass-outcome-number-132)

:white_check_mark:Pass outcome
#### Subject detail
|Name|question-logistics-create-organization-q6|
|----|----|
|Title|competency&#32;question&#32;domains/logistics/create-organization/q6.rq&#32;from&#32;branch&#32;main|
|Composition|- [Competency question logistics/create-organization/q6](https://github.com/HyperAgents/hmas/blob/main/domains/logistics/create-organization/q6.rq.ttl)|

#### Criterion detail
|Identifier|[syntax](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#syntax)|
|----|----|
|Title|Syntax&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;check&#32;wether&#32;the&#32;test&#32;subject&#32;is&#32;syntaxically&#32;correct&#32;or&#32;not.|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-131)|Identifier|`syntax-error`|
|[Section top](#pass-outcome-number-131)|Title|Correct&#32;syntax|
|[Section top](#pass-outcome-number-131)|Description|Test&#32;subject&#32;has&#32;a&#32;correct&#32;syntax|

***
### Pass Outcome number 132

[Jump to summary definition](#summary-Pass-132)	|	[Previous Pass outcome](#pass-outcome-number-131)	|	[Next Pass outcome](#pass-outcome-number-133)

:white_check_mark:Pass outcome
#### Subject detail
|Name|question-logistics-create-organization-q6|
|----|----|
|Title|competency&#32;question&#32;domains/logistics/create-organization/q6.rq&#32;from&#32;branch&#32;main|
|Composition|- [Competency question logistics/create-organization/q6](https://github.com/HyperAgents/hmas/blob/main/domains/logistics/create-organization/q6.rq.ttl)|

#### Criterion detail
|Identifier|[uri-validity](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#uri-validity)|
|----|----|
|Title|URI&#32;validity&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;check&#32;if&#32;all&#32;the&#32;URIs&#32;of&#32;the&#32;resource&#32;are&#32;well-formed|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-132)|Identifier|`invalid-uri`|
|[Section top](#pass-outcome-number-132)|Title|All&#32;subject&#32;URI&#32;valid|
|[Section top](#pass-outcome-number-132)|Description|All&#32;the&#32;URIs&#32;of&#32;the&#32;subject&#32;are&#32;valid|

***
### Pass Outcome number 133

[Jump to summary definition](#summary-Pass-133)	|	[Previous Pass outcome](#pass-outcome-number-132)	|	[Next Pass outcome](#pass-outcome-number-134)

:white_check_mark:Pass outcome
#### Subject detail
|Name|question-logistics-create-organization-q5|
|----|----|
|Title|competency&#32;question&#32;domains/logistics/create-organization/q5.rq&#32;from&#32;branch&#32;main|
|Composition|- [Competency question logistics/create-organization/q5](https://github.com/HyperAgents/hmas/blob/main/domains/logistics/create-organization/q5.rq.ttl)|

#### Criterion detail
|Identifier|[namespace-validity](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#namespace-validity)|
|----|----|
|Title|Prefix&#32;validity&#32;test|
|Description|A&#32;test&#32;case&#32;checking&#32;if&#32;all&#32;the&#32;prefixes&#32;are&#32;not&#32;too&#32;close&#32;from&#32;the&#32;most&#32;used&#32;existing&#32;namespaces&#32;(according&#32;to&#32;prefix&#32;cc)&#32;or&#32;an&#32;ontology&#32;namespace|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-133)|Identifier|`namespace-typo`|
|[Section top](#pass-outcome-number-133)|Title|No&#32;namespace&#32;typo|
|[Section top](#pass-outcome-number-133)|Description|It&#32;seems&#32;that&#32;none&#32;of&#32;the&#32;subject&#32;URIs&#32;have&#32;namespaces&#32;typos|

***
### Pass Outcome number 134

[Jump to summary definition](#summary-Pass-134)	|	[Previous Pass outcome](#pass-outcome-number-133)	|	[Next Pass outcome](#pass-outcome-number-135)

:white_check_mark:Pass outcome
#### Subject detail
|Name|question-logistics-create-organization-q5|
|----|----|
|Title|competency&#32;question&#32;domains/logistics/create-organization/q5.rq&#32;from&#32;branch&#32;main|
|Composition|- [Competency question logistics/create-organization/q5](https://github.com/HyperAgents/hmas/blob/main/domains/logistics/create-organization/q5.rq.ttl)|

#### Criterion detail
|Identifier|[query-type](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#query-type)|
|----|----|
|Title|Query&#32;type&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;check&#32;if&#32;the&#32;query&#32;is&#32;indeed&#32;of&#32;type&#32;Select&#32;or&#32;Ask|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-134)|Identifier|`wrong-query-type`|
|[Section top](#pass-outcome-number-134)|Title|Accurate&#32;query&#32;type|
|[Section top](#pass-outcome-number-134)|Description|The&#32;query&#32;is&#32;of&#32;type&#32;Select&#32;or&#32;Ask|

***
### Pass Outcome number 135

[Jump to summary definition](#summary-Pass-135)	|	[Previous Pass outcome](#pass-outcome-number-134)	|	[Next Pass outcome](#pass-outcome-number-136)

:white_check_mark:Pass outcome
#### Subject detail
|Name|question-logistics-create-organization-q5|
|----|----|
|Title|competency&#32;question&#32;domains/logistics/create-organization/q5.rq&#32;from&#32;branch&#32;main|
|Composition|- [Competency question logistics/create-organization/q5](https://github.com/HyperAgents/hmas/blob/main/domains/logistics/create-organization/q5.rq.ttl)|

#### Criterion detail
|Identifier|[syntax](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#syntax)|
|----|----|
|Title|Syntax&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;check&#32;wether&#32;the&#32;test&#32;subject&#32;is&#32;syntaxically&#32;correct&#32;or&#32;not.|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-135)|Identifier|`syntax-error`|
|[Section top](#pass-outcome-number-135)|Title|Correct&#32;syntax|
|[Section top](#pass-outcome-number-135)|Description|Test&#32;subject&#32;has&#32;a&#32;correct&#32;syntax|

***
### Pass Outcome number 136

[Jump to summary definition](#summary-Pass-136)	|	[Previous Pass outcome](#pass-outcome-number-135)	|	[Next Pass outcome](#pass-outcome-number-137)

:white_check_mark:Pass outcome
#### Subject detail
|Name|question-logistics-create-organization-q5|
|----|----|
|Title|competency&#32;question&#32;domains/logistics/create-organization/q5.rq&#32;from&#32;branch&#32;main|
|Composition|- [Competency question logistics/create-organization/q5](https://github.com/HyperAgents/hmas/blob/main/domains/logistics/create-organization/q5.rq.ttl)|

#### Criterion detail
|Identifier|[uri-validity](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#uri-validity)|
|----|----|
|Title|URI&#32;validity&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;check&#32;if&#32;all&#32;the&#32;URIs&#32;of&#32;the&#32;resource&#32;are&#32;well-formed|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-136)|Identifier|`invalid-uri`|
|[Section top](#pass-outcome-number-136)|Title|All&#32;subject&#32;URI&#32;valid|
|[Section top](#pass-outcome-number-136)|Description|All&#32;the&#32;URIs&#32;of&#32;the&#32;subject&#32;are&#32;valid|

***
### Pass Outcome number 137

[Jump to summary definition](#summary-Pass-137)	|	[Previous Pass outcome](#pass-outcome-number-136)	|	[Next Pass outcome](#pass-outcome-number-138)

:white_check_mark:Pass outcome
#### Subject detail
|Name|question-logistics-create-organization-q4|
|----|----|
|Title|competency&#32;question&#32;domains/logistics/create-organization/q4.rq&#32;from&#32;branch&#32;main|
|Composition|- [Competency question logistics/create-organization/q4](https://github.com/HyperAgents/hmas/blob/main/domains/logistics/create-organization/q4.rq.ttl)|

#### Criterion detail
|Identifier|[namespace-validity](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#namespace-validity)|
|----|----|
|Title|Prefix&#32;validity&#32;test|
|Description|A&#32;test&#32;case&#32;checking&#32;if&#32;all&#32;the&#32;prefixes&#32;are&#32;not&#32;too&#32;close&#32;from&#32;the&#32;most&#32;used&#32;existing&#32;namespaces&#32;(according&#32;to&#32;prefix&#32;cc)&#32;or&#32;an&#32;ontology&#32;namespace|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-137)|Identifier|`namespace-typo`|
|[Section top](#pass-outcome-number-137)|Title|No&#32;namespace&#32;typo|
|[Section top](#pass-outcome-number-137)|Description|It&#32;seems&#32;that&#32;none&#32;of&#32;the&#32;subject&#32;URIs&#32;have&#32;namespaces&#32;typos|

***
### Pass Outcome number 138

[Jump to summary definition](#summary-Pass-138)	|	[Previous Pass outcome](#pass-outcome-number-137)	|	[Next Pass outcome](#pass-outcome-number-139)

:white_check_mark:Pass outcome
#### Subject detail
|Name|question-logistics-create-organization-q4|
|----|----|
|Title|competency&#32;question&#32;domains/logistics/create-organization/q4.rq&#32;from&#32;branch&#32;main|
|Composition|- [Competency question logistics/create-organization/q4](https://github.com/HyperAgents/hmas/blob/main/domains/logistics/create-organization/q4.rq.ttl)|

#### Criterion detail
|Identifier|[query-type](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#query-type)|
|----|----|
|Title|Query&#32;type&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;check&#32;if&#32;the&#32;query&#32;is&#32;indeed&#32;of&#32;type&#32;Select&#32;or&#32;Ask|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-138)|Identifier|`wrong-query-type`|
|[Section top](#pass-outcome-number-138)|Title|Accurate&#32;query&#32;type|
|[Section top](#pass-outcome-number-138)|Description|The&#32;query&#32;is&#32;of&#32;type&#32;Select&#32;or&#32;Ask|

***
### Pass Outcome number 139

[Jump to summary definition](#summary-Pass-139)	|	[Previous Pass outcome](#pass-outcome-number-138)	|	[Next Pass outcome](#pass-outcome-number-140)

:white_check_mark:Pass outcome
#### Subject detail
|Name|question-logistics-create-organization-q4|
|----|----|
|Title|competency&#32;question&#32;domains/logistics/create-organization/q4.rq&#32;from&#32;branch&#32;main|
|Composition|- [Competency question logistics/create-organization/q4](https://github.com/HyperAgents/hmas/blob/main/domains/logistics/create-organization/q4.rq.ttl)|

#### Criterion detail
|Identifier|[syntax](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#syntax)|
|----|----|
|Title|Syntax&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;check&#32;wether&#32;the&#32;test&#32;subject&#32;is&#32;syntaxically&#32;correct&#32;or&#32;not.|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-139)|Identifier|`syntax-error`|
|[Section top](#pass-outcome-number-139)|Title|Correct&#32;syntax|
|[Section top](#pass-outcome-number-139)|Description|Test&#32;subject&#32;has&#32;a&#32;correct&#32;syntax|

***
### Pass Outcome number 140

[Jump to summary definition](#summary-Pass-140)	|	[Previous Pass outcome](#pass-outcome-number-139)	|	[Next Pass outcome](#pass-outcome-number-141)

:white_check_mark:Pass outcome
#### Subject detail
|Name|question-logistics-create-organization-q4|
|----|----|
|Title|competency&#32;question&#32;domains/logistics/create-organization/q4.rq&#32;from&#32;branch&#32;main|
|Composition|- [Competency question logistics/create-organization/q4](https://github.com/HyperAgents/hmas/blob/main/domains/logistics/create-organization/q4.rq.ttl)|

#### Criterion detail
|Identifier|[uri-validity](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#uri-validity)|
|----|----|
|Title|URI&#32;validity&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;check&#32;if&#32;all&#32;the&#32;URIs&#32;of&#32;the&#32;resource&#32;are&#32;well-formed|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-140)|Identifier|`invalid-uri`|
|[Section top](#pass-outcome-number-140)|Title|All&#32;subject&#32;URI&#32;valid|
|[Section top](#pass-outcome-number-140)|Description|All&#32;the&#32;URIs&#32;of&#32;the&#32;subject&#32;are&#32;valid|

***
### Pass Outcome number 141

[Jump to summary definition](#summary-Pass-141)	|	[Previous Pass outcome](#pass-outcome-number-140)	|	[Next Pass outcome](#pass-outcome-number-142)

:white_check_mark:Pass outcome
#### Subject detail
|Name|question-logistics-create-organization-q3|
|----|----|
|Title|competency&#32;question&#32;domains/logistics/create-organization/q3.rq&#32;from&#32;branch&#32;main|
|Composition|- [Competency question logistics/create-organization/q3](https://github.com/HyperAgents/hmas/blob/main/domains/logistics/create-organization/q3.rq.ttl)|

#### Criterion detail
|Identifier|[namespace-validity](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#namespace-validity)|
|----|----|
|Title|Prefix&#32;validity&#32;test|
|Description|A&#32;test&#32;case&#32;checking&#32;if&#32;all&#32;the&#32;prefixes&#32;are&#32;not&#32;too&#32;close&#32;from&#32;the&#32;most&#32;used&#32;existing&#32;namespaces&#32;(according&#32;to&#32;prefix&#32;cc)&#32;or&#32;an&#32;ontology&#32;namespace|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-141)|Identifier|`namespace-typo`|
|[Section top](#pass-outcome-number-141)|Title|No&#32;namespace&#32;typo|
|[Section top](#pass-outcome-number-141)|Description|It&#32;seems&#32;that&#32;none&#32;of&#32;the&#32;subject&#32;URIs&#32;have&#32;namespaces&#32;typos|

***
### Pass Outcome number 142

[Jump to summary definition](#summary-Pass-142)	|	[Previous Pass outcome](#pass-outcome-number-141)	|	[Next Pass outcome](#pass-outcome-number-143)

:white_check_mark:Pass outcome
#### Subject detail
|Name|question-logistics-create-organization-q3|
|----|----|
|Title|competency&#32;question&#32;domains/logistics/create-organization/q3.rq&#32;from&#32;branch&#32;main|
|Composition|- [Competency question logistics/create-organization/q3](https://github.com/HyperAgents/hmas/blob/main/domains/logistics/create-organization/q3.rq.ttl)|

#### Criterion detail
|Identifier|[query-type](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#query-type)|
|----|----|
|Title|Query&#32;type&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;check&#32;if&#32;the&#32;query&#32;is&#32;indeed&#32;of&#32;type&#32;Select&#32;or&#32;Ask|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-142)|Identifier|`wrong-query-type`|
|[Section top](#pass-outcome-number-142)|Title|Accurate&#32;query&#32;type|
|[Section top](#pass-outcome-number-142)|Description|The&#32;query&#32;is&#32;of&#32;type&#32;Select&#32;or&#32;Ask|

***
### Pass Outcome number 143

[Jump to summary definition](#summary-Pass-143)	|	[Previous Pass outcome](#pass-outcome-number-142)	|	[Next Pass outcome](#pass-outcome-number-144)

:white_check_mark:Pass outcome
#### Subject detail
|Name|question-logistics-create-organization-q3|
|----|----|
|Title|competency&#32;question&#32;domains/logistics/create-organization/q3.rq&#32;from&#32;branch&#32;main|
|Composition|- [Competency question logistics/create-organization/q3](https://github.com/HyperAgents/hmas/blob/main/domains/logistics/create-organization/q3.rq.ttl)|

#### Criterion detail
|Identifier|[syntax](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#syntax)|
|----|----|
|Title|Syntax&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;check&#32;wether&#32;the&#32;test&#32;subject&#32;is&#32;syntaxically&#32;correct&#32;or&#32;not.|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-143)|Identifier|`syntax-error`|
|[Section top](#pass-outcome-number-143)|Title|Correct&#32;syntax|
|[Section top](#pass-outcome-number-143)|Description|Test&#32;subject&#32;has&#32;a&#32;correct&#32;syntax|

***
### Pass Outcome number 144

[Jump to summary definition](#summary-Pass-144)	|	[Previous Pass outcome](#pass-outcome-number-143)	|	[Next Pass outcome](#pass-outcome-number-145)

:white_check_mark:Pass outcome
#### Subject detail
|Name|question-logistics-create-organization-q3|
|----|----|
|Title|competency&#32;question&#32;domains/logistics/create-organization/q3.rq&#32;from&#32;branch&#32;main|
|Composition|- [Competency question logistics/create-organization/q3](https://github.com/HyperAgents/hmas/blob/main/domains/logistics/create-organization/q3.rq.ttl)|

#### Criterion detail
|Identifier|[uri-validity](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#uri-validity)|
|----|----|
|Title|URI&#32;validity&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;check&#32;if&#32;all&#32;the&#32;URIs&#32;of&#32;the&#32;resource&#32;are&#32;well-formed|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-144)|Identifier|`invalid-uri`|
|[Section top](#pass-outcome-number-144)|Title|All&#32;subject&#32;URI&#32;valid|
|[Section top](#pass-outcome-number-144)|Description|All&#32;the&#32;URIs&#32;of&#32;the&#32;subject&#32;are&#32;valid|

***
### Pass Outcome number 145

[Jump to summary definition](#summary-Pass-145)	|	[Previous Pass outcome](#pass-outcome-number-144)	|	[Next Pass outcome](#pass-outcome-number-146)

:white_check_mark:Pass outcome
#### Subject detail
|Name|question-logistics-create-organization-q2|
|----|----|
|Title|competency&#32;question&#32;domains/logistics/create-organization/q2.rq&#32;from&#32;branch&#32;main|
|Composition|- [Competency question logistics/create-organization/q2](https://github.com/HyperAgents/hmas/blob/main/domains/logistics/create-organization/q2.rq.ttl)|

#### Criterion detail
|Identifier|[namespace-validity](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#namespace-validity)|
|----|----|
|Title|Prefix&#32;validity&#32;test|
|Description|A&#32;test&#32;case&#32;checking&#32;if&#32;all&#32;the&#32;prefixes&#32;are&#32;not&#32;too&#32;close&#32;from&#32;the&#32;most&#32;used&#32;existing&#32;namespaces&#32;(according&#32;to&#32;prefix&#32;cc)&#32;or&#32;an&#32;ontology&#32;namespace|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-145)|Identifier|`namespace-typo`|
|[Section top](#pass-outcome-number-145)|Title|No&#32;namespace&#32;typo|
|[Section top](#pass-outcome-number-145)|Description|It&#32;seems&#32;that&#32;none&#32;of&#32;the&#32;subject&#32;URIs&#32;have&#32;namespaces&#32;typos|

***
### Pass Outcome number 146

[Jump to summary definition](#summary-Pass-146)	|	[Previous Pass outcome](#pass-outcome-number-145)	|	[Next Pass outcome](#pass-outcome-number-147)

:white_check_mark:Pass outcome
#### Subject detail
|Name|question-logistics-create-organization-q2|
|----|----|
|Title|competency&#32;question&#32;domains/logistics/create-organization/q2.rq&#32;from&#32;branch&#32;main|
|Composition|- [Competency question logistics/create-organization/q2](https://github.com/HyperAgents/hmas/blob/main/domains/logistics/create-organization/q2.rq.ttl)|

#### Criterion detail
|Identifier|[query-type](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#query-type)|
|----|----|
|Title|Query&#32;type&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;check&#32;if&#32;the&#32;query&#32;is&#32;indeed&#32;of&#32;type&#32;Select&#32;or&#32;Ask|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-146)|Identifier|`wrong-query-type`|
|[Section top](#pass-outcome-number-146)|Title|Accurate&#32;query&#32;type|
|[Section top](#pass-outcome-number-146)|Description|The&#32;query&#32;is&#32;of&#32;type&#32;Select&#32;or&#32;Ask|

***
### Pass Outcome number 147

[Jump to summary definition](#summary-Pass-147)	|	[Previous Pass outcome](#pass-outcome-number-146)	|	[Next Pass outcome](#pass-outcome-number-148)

:white_check_mark:Pass outcome
#### Subject detail
|Name|question-logistics-create-organization-q2|
|----|----|
|Title|competency&#32;question&#32;domains/logistics/create-organization/q2.rq&#32;from&#32;branch&#32;main|
|Composition|- [Competency question logistics/create-organization/q2](https://github.com/HyperAgents/hmas/blob/main/domains/logistics/create-organization/q2.rq.ttl)|

#### Criterion detail
|Identifier|[syntax](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#syntax)|
|----|----|
|Title|Syntax&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;check&#32;wether&#32;the&#32;test&#32;subject&#32;is&#32;syntaxically&#32;correct&#32;or&#32;not.|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-147)|Identifier|`syntax-error`|
|[Section top](#pass-outcome-number-147)|Title|Correct&#32;syntax|
|[Section top](#pass-outcome-number-147)|Description|Test&#32;subject&#32;has&#32;a&#32;correct&#32;syntax|

***
### Pass Outcome number 148

[Jump to summary definition](#summary-Pass-148)	|	[Previous Pass outcome](#pass-outcome-number-147)	|	[Next Pass outcome](#pass-outcome-number-149)

:white_check_mark:Pass outcome
#### Subject detail
|Name|question-logistics-create-organization-q2|
|----|----|
|Title|competency&#32;question&#32;domains/logistics/create-organization/q2.rq&#32;from&#32;branch&#32;main|
|Composition|- [Competency question logistics/create-organization/q2](https://github.com/HyperAgents/hmas/blob/main/domains/logistics/create-organization/q2.rq.ttl)|

#### Criterion detail
|Identifier|[uri-validity](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#uri-validity)|
|----|----|
|Title|URI&#32;validity&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;check&#32;if&#32;all&#32;the&#32;URIs&#32;of&#32;the&#32;resource&#32;are&#32;well-formed|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-148)|Identifier|`invalid-uri`|
|[Section top](#pass-outcome-number-148)|Title|All&#32;subject&#32;URI&#32;valid|
|[Section top](#pass-outcome-number-148)|Description|All&#32;the&#32;URIs&#32;of&#32;the&#32;subject&#32;are&#32;valid|

***
### Pass Outcome number 149

[Jump to summary definition](#summary-Pass-149)	|	[Previous Pass outcome](#pass-outcome-number-148)	|	[Next Pass outcome](#pass-outcome-number-150)

:white_check_mark:Pass outcome
#### Subject detail
|Name|question-logistics-create-organization-q1|
|----|----|
|Title|competency&#32;question&#32;domains/logistics/create-organization/q1.rq&#32;from&#32;branch&#32;main|
|Composition|- [Competency question logistics/create-organization/q1](https://github.com/HyperAgents/hmas/blob/main/domains/logistics/create-organization/q1.rq.ttl)|

#### Criterion detail
|Identifier|[namespace-validity](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#namespace-validity)|
|----|----|
|Title|Prefix&#32;validity&#32;test|
|Description|A&#32;test&#32;case&#32;checking&#32;if&#32;all&#32;the&#32;prefixes&#32;are&#32;not&#32;too&#32;close&#32;from&#32;the&#32;most&#32;used&#32;existing&#32;namespaces&#32;(according&#32;to&#32;prefix&#32;cc)&#32;or&#32;an&#32;ontology&#32;namespace|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-149)|Identifier|`namespace-typo`|
|[Section top](#pass-outcome-number-149)|Title|No&#32;namespace&#32;typo|
|[Section top](#pass-outcome-number-149)|Description|It&#32;seems&#32;that&#32;none&#32;of&#32;the&#32;subject&#32;URIs&#32;have&#32;namespaces&#32;typos|

***
### Pass Outcome number 150

[Jump to summary definition](#summary-Pass-150)	|	[Previous Pass outcome](#pass-outcome-number-149)	|	[Next Pass outcome](#pass-outcome-number-151)

:white_check_mark:Pass outcome
#### Subject detail
|Name|question-logistics-create-organization-q1|
|----|----|
|Title|competency&#32;question&#32;domains/logistics/create-organization/q1.rq&#32;from&#32;branch&#32;main|
|Composition|- [Competency question logistics/create-organization/q1](https://github.com/HyperAgents/hmas/blob/main/domains/logistics/create-organization/q1.rq.ttl)|

#### Criterion detail
|Identifier|[query-type](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#query-type)|
|----|----|
|Title|Query&#32;type&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;check&#32;if&#32;the&#32;query&#32;is&#32;indeed&#32;of&#32;type&#32;Select&#32;or&#32;Ask|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-150)|Identifier|`wrong-query-type`|
|[Section top](#pass-outcome-number-150)|Title|Accurate&#32;query&#32;type|
|[Section top](#pass-outcome-number-150)|Description|The&#32;query&#32;is&#32;of&#32;type&#32;Select&#32;or&#32;Ask|

***
### Pass Outcome number 151

[Jump to summary definition](#summary-Pass-151)	|	[Previous Pass outcome](#pass-outcome-number-150)	|	[Next Pass outcome](#pass-outcome-number-152)

:white_check_mark:Pass outcome
#### Subject detail
|Name|question-logistics-create-organization-q1|
|----|----|
|Title|competency&#32;question&#32;domains/logistics/create-organization/q1.rq&#32;from&#32;branch&#32;main|
|Composition|- [Competency question logistics/create-organization/q1](https://github.com/HyperAgents/hmas/blob/main/domains/logistics/create-organization/q1.rq.ttl)|

#### Criterion detail
|Identifier|[syntax](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#syntax)|
|----|----|
|Title|Syntax&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;check&#32;wether&#32;the&#32;test&#32;subject&#32;is&#32;syntaxically&#32;correct&#32;or&#32;not.|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-151)|Identifier|`syntax-error`|
|[Section top](#pass-outcome-number-151)|Title|Correct&#32;syntax|
|[Section top](#pass-outcome-number-151)|Description|Test&#32;subject&#32;has&#32;a&#32;correct&#32;syntax|

***
### Pass Outcome number 152

[Jump to summary definition](#summary-Pass-152)	|	[Previous Pass outcome](#pass-outcome-number-151)	|	[Next Pass outcome](#pass-outcome-number-153)

:white_check_mark:Pass outcome
#### Subject detail
|Name|question-logistics-create-organization-q1|
|----|----|
|Title|competency&#32;question&#32;domains/logistics/create-organization/q1.rq&#32;from&#32;branch&#32;main|
|Composition|- [Competency question logistics/create-organization/q1](https://github.com/HyperAgents/hmas/blob/main/domains/logistics/create-organization/q1.rq.ttl)|

#### Criterion detail
|Identifier|[uri-validity](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#uri-validity)|
|----|----|
|Title|URI&#32;validity&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;check&#32;if&#32;all&#32;the&#32;URIs&#32;of&#32;the&#32;resource&#32;are&#32;well-formed|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-152)|Identifier|`invalid-uri`|
|[Section top](#pass-outcome-number-152)|Title|All&#32;subject&#32;URI&#32;valid|
|[Section top](#pass-outcome-number-152)|Description|All&#32;the&#32;URIs&#32;of&#32;the&#32;subject&#32;are&#32;valid|

***
### Pass Outcome number 153

[Jump to summary definition](#summary-Pass-153)	|	[Previous Pass outcome](#pass-outcome-number-152)	|	[Next Pass outcome](#pass-outcome-number-154)

:white_check_mark:Pass outcome
#### Subject detail
|Name|question-logistics-coordinate-activities-q3|
|----|----|
|Title|competency&#32;question&#32;domains/logistics/coordinate-activities/q3.rq&#32;from&#32;branch&#32;main|
|Composition|- [Competency question logistics/coordinate-activities/q3](https://github.com/HyperAgents/hmas/blob/main/domains/logistics/coordinate-activities/q3.rq.ttl)|

#### Criterion detail
|Identifier|[namespace-validity](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#namespace-validity)|
|----|----|
|Title|Prefix&#32;validity&#32;test|
|Description|A&#32;test&#32;case&#32;checking&#32;if&#32;all&#32;the&#32;prefixes&#32;are&#32;not&#32;too&#32;close&#32;from&#32;the&#32;most&#32;used&#32;existing&#32;namespaces&#32;(according&#32;to&#32;prefix&#32;cc)&#32;or&#32;an&#32;ontology&#32;namespace|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-153)|Identifier|`namespace-typo`|
|[Section top](#pass-outcome-number-153)|Title|No&#32;namespace&#32;typo|
|[Section top](#pass-outcome-number-153)|Description|It&#32;seems&#32;that&#32;none&#32;of&#32;the&#32;subject&#32;URIs&#32;have&#32;namespaces&#32;typos|

***
### Pass Outcome number 154

[Jump to summary definition](#summary-Pass-154)	|	[Previous Pass outcome](#pass-outcome-number-153)	|	[Next Pass outcome](#pass-outcome-number-155)

:white_check_mark:Pass outcome
#### Subject detail
|Name|question-logistics-coordinate-activities-q3|
|----|----|
|Title|competency&#32;question&#32;domains/logistics/coordinate-activities/q3.rq&#32;from&#32;branch&#32;main|
|Composition|- [Competency question logistics/coordinate-activities/q3](https://github.com/HyperAgents/hmas/blob/main/domains/logistics/coordinate-activities/q3.rq.ttl)|

#### Criterion detail
|Identifier|[query-type](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#query-type)|
|----|----|
|Title|Query&#32;type&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;check&#32;if&#32;the&#32;query&#32;is&#32;indeed&#32;of&#32;type&#32;Select&#32;or&#32;Ask|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-154)|Identifier|`wrong-query-type`|
|[Section top](#pass-outcome-number-154)|Title|Accurate&#32;query&#32;type|
|[Section top](#pass-outcome-number-154)|Description|The&#32;query&#32;is&#32;of&#32;type&#32;Select&#32;or&#32;Ask|

***
### Pass Outcome number 155

[Jump to summary definition](#summary-Pass-155)	|	[Previous Pass outcome](#pass-outcome-number-154)	|	[Next Pass outcome](#pass-outcome-number-156)

:white_check_mark:Pass outcome
#### Subject detail
|Name|question-logistics-coordinate-activities-q3|
|----|----|
|Title|competency&#32;question&#32;domains/logistics/coordinate-activities/q3.rq&#32;from&#32;branch&#32;main|
|Composition|- [Competency question logistics/coordinate-activities/q3](https://github.com/HyperAgents/hmas/blob/main/domains/logistics/coordinate-activities/q3.rq.ttl)|

#### Criterion detail
|Identifier|[syntax](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#syntax)|
|----|----|
|Title|Syntax&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;check&#32;wether&#32;the&#32;test&#32;subject&#32;is&#32;syntaxically&#32;correct&#32;or&#32;not.|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-155)|Identifier|`syntax-error`|
|[Section top](#pass-outcome-number-155)|Title|Correct&#32;syntax|
|[Section top](#pass-outcome-number-155)|Description|Test&#32;subject&#32;has&#32;a&#32;correct&#32;syntax|

***
### Pass Outcome number 156

[Jump to summary definition](#summary-Pass-156)	|	[Previous Pass outcome](#pass-outcome-number-155)	|	[Next Pass outcome](#pass-outcome-number-157)

:white_check_mark:Pass outcome
#### Subject detail
|Name|question-logistics-coordinate-activities-q3|
|----|----|
|Title|competency&#32;question&#32;domains/logistics/coordinate-activities/q3.rq&#32;from&#32;branch&#32;main|
|Composition|- [Competency question logistics/coordinate-activities/q3](https://github.com/HyperAgents/hmas/blob/main/domains/logistics/coordinate-activities/q3.rq.ttl)|

#### Criterion detail
|Identifier|[uri-validity](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#uri-validity)|
|----|----|
|Title|URI&#32;validity&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;check&#32;if&#32;all&#32;the&#32;URIs&#32;of&#32;the&#32;resource&#32;are&#32;well-formed|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-156)|Identifier|`invalid-uri`|
|[Section top](#pass-outcome-number-156)|Title|All&#32;subject&#32;URI&#32;valid|
|[Section top](#pass-outcome-number-156)|Description|All&#32;the&#32;URIs&#32;of&#32;the&#32;subject&#32;are&#32;valid|

***
### Pass Outcome number 157

[Jump to summary definition](#summary-Pass-157)	|	[Previous Pass outcome](#pass-outcome-number-156)	|	[Next Pass outcome](#pass-outcome-number-158)

:white_check_mark:Pass outcome
#### Subject detail
|Name|question-logistics-coordinate-activities-q2|
|----|----|
|Title|competency&#32;question&#32;domains/logistics/coordinate-activities/q2.rq&#32;from&#32;branch&#32;main|
|Composition|- [Competency question logistics/coordinate-activities/q2](https://github.com/HyperAgents/hmas/blob/main/domains/logistics/coordinate-activities/q2.rq.ttl)|

#### Criterion detail
|Identifier|[namespace-validity](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#namespace-validity)|
|----|----|
|Title|Prefix&#32;validity&#32;test|
|Description|A&#32;test&#32;case&#32;checking&#32;if&#32;all&#32;the&#32;prefixes&#32;are&#32;not&#32;too&#32;close&#32;from&#32;the&#32;most&#32;used&#32;existing&#32;namespaces&#32;(according&#32;to&#32;prefix&#32;cc)&#32;or&#32;an&#32;ontology&#32;namespace|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-157)|Identifier|`namespace-typo`|
|[Section top](#pass-outcome-number-157)|Title|No&#32;namespace&#32;typo|
|[Section top](#pass-outcome-number-157)|Description|It&#32;seems&#32;that&#32;none&#32;of&#32;the&#32;subject&#32;URIs&#32;have&#32;namespaces&#32;typos|

***
### Pass Outcome number 158

[Jump to summary definition](#summary-Pass-158)	|	[Previous Pass outcome](#pass-outcome-number-157)	|	[Next Pass outcome](#pass-outcome-number-159)

:white_check_mark:Pass outcome
#### Subject detail
|Name|question-logistics-coordinate-activities-q2|
|----|----|
|Title|competency&#32;question&#32;domains/logistics/coordinate-activities/q2.rq&#32;from&#32;branch&#32;main|
|Composition|- [Competency question logistics/coordinate-activities/q2](https://github.com/HyperAgents/hmas/blob/main/domains/logistics/coordinate-activities/q2.rq.ttl)|

#### Criterion detail
|Identifier|[query-type](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#query-type)|
|----|----|
|Title|Query&#32;type&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;check&#32;if&#32;the&#32;query&#32;is&#32;indeed&#32;of&#32;type&#32;Select&#32;or&#32;Ask|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-158)|Identifier|`wrong-query-type`|
|[Section top](#pass-outcome-number-158)|Title|Accurate&#32;query&#32;type|
|[Section top](#pass-outcome-number-158)|Description|The&#32;query&#32;is&#32;of&#32;type&#32;Select&#32;or&#32;Ask|

***
### Pass Outcome number 159

[Jump to summary definition](#summary-Pass-159)	|	[Previous Pass outcome](#pass-outcome-number-158)	|	[Next Pass outcome](#pass-outcome-number-160)

:white_check_mark:Pass outcome
#### Subject detail
|Name|question-logistics-coordinate-activities-q2|
|----|----|
|Title|competency&#32;question&#32;domains/logistics/coordinate-activities/q2.rq&#32;from&#32;branch&#32;main|
|Composition|- [Competency question logistics/coordinate-activities/q2](https://github.com/HyperAgents/hmas/blob/main/domains/logistics/coordinate-activities/q2.rq.ttl)|

#### Criterion detail
|Identifier|[syntax](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#syntax)|
|----|----|
|Title|Syntax&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;check&#32;wether&#32;the&#32;test&#32;subject&#32;is&#32;syntaxically&#32;correct&#32;or&#32;not.|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-159)|Identifier|`syntax-error`|
|[Section top](#pass-outcome-number-159)|Title|Correct&#32;syntax|
|[Section top](#pass-outcome-number-159)|Description|Test&#32;subject&#32;has&#32;a&#32;correct&#32;syntax|

***
### Pass Outcome number 160

[Jump to summary definition](#summary-Pass-160)	|	[Previous Pass outcome](#pass-outcome-number-159)	|	[Next Pass outcome](#pass-outcome-number-161)

:white_check_mark:Pass outcome
#### Subject detail
|Name|question-logistics-coordinate-activities-q2|
|----|----|
|Title|competency&#32;question&#32;domains/logistics/coordinate-activities/q2.rq&#32;from&#32;branch&#32;main|
|Composition|- [Competency question logistics/coordinate-activities/q2](https://github.com/HyperAgents/hmas/blob/main/domains/logistics/coordinate-activities/q2.rq.ttl)|

#### Criterion detail
|Identifier|[uri-validity](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#uri-validity)|
|----|----|
|Title|URI&#32;validity&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;check&#32;if&#32;all&#32;the&#32;URIs&#32;of&#32;the&#32;resource&#32;are&#32;well-formed|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-160)|Identifier|`invalid-uri`|
|[Section top](#pass-outcome-number-160)|Title|All&#32;subject&#32;URI&#32;valid|
|[Section top](#pass-outcome-number-160)|Description|All&#32;the&#32;URIs&#32;of&#32;the&#32;subject&#32;are&#32;valid|

***
### Pass Outcome number 161

[Jump to summary definition](#summary-Pass-161)	|	[Previous Pass outcome](#pass-outcome-number-160)	|	[Next Pass outcome](#pass-outcome-number-162)

:white_check_mark:Pass outcome
#### Subject detail
|Name|question-logistics-coordinate-activities-q1|
|----|----|
|Title|competency&#32;question&#32;domains/logistics/coordinate-activities/q1.rq&#32;from&#32;branch&#32;main|
|Composition|- [Competency question logistics/coordinate-activities/q1](https://github.com/HyperAgents/hmas/blob/main/domains/logistics/coordinate-activities/q1.rq.ttl)|

#### Criterion detail
|Identifier|[namespace-validity](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#namespace-validity)|
|----|----|
|Title|Prefix&#32;validity&#32;test|
|Description|A&#32;test&#32;case&#32;checking&#32;if&#32;all&#32;the&#32;prefixes&#32;are&#32;not&#32;too&#32;close&#32;from&#32;the&#32;most&#32;used&#32;existing&#32;namespaces&#32;(according&#32;to&#32;prefix&#32;cc)&#32;or&#32;an&#32;ontology&#32;namespace|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-161)|Identifier|`namespace-typo`|
|[Section top](#pass-outcome-number-161)|Title|No&#32;namespace&#32;typo|
|[Section top](#pass-outcome-number-161)|Description|It&#32;seems&#32;that&#32;none&#32;of&#32;the&#32;subject&#32;URIs&#32;have&#32;namespaces&#32;typos|

***
### Pass Outcome number 162

[Jump to summary definition](#summary-Pass-162)	|	[Previous Pass outcome](#pass-outcome-number-161)	|	[Next Pass outcome](#pass-outcome-number-163)

:white_check_mark:Pass outcome
#### Subject detail
|Name|question-logistics-coordinate-activities-q1|
|----|----|
|Title|competency&#32;question&#32;domains/logistics/coordinate-activities/q1.rq&#32;from&#32;branch&#32;main|
|Composition|- [Competency question logistics/coordinate-activities/q1](https://github.com/HyperAgents/hmas/blob/main/domains/logistics/coordinate-activities/q1.rq.ttl)|

#### Criterion detail
|Identifier|[query-type](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#query-type)|
|----|----|
|Title|Query&#32;type&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;check&#32;if&#32;the&#32;query&#32;is&#32;indeed&#32;of&#32;type&#32;Select&#32;or&#32;Ask|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-162)|Identifier|`wrong-query-type`|
|[Section top](#pass-outcome-number-162)|Title|Accurate&#32;query&#32;type|
|[Section top](#pass-outcome-number-162)|Description|The&#32;query&#32;is&#32;of&#32;type&#32;Select&#32;or&#32;Ask|

***
### Pass Outcome number 163

[Jump to summary definition](#summary-Pass-163)	|	[Previous Pass outcome](#pass-outcome-number-162)	|	[Next Pass outcome](#pass-outcome-number-164)

:white_check_mark:Pass outcome
#### Subject detail
|Name|question-logistics-coordinate-activities-q1|
|----|----|
|Title|competency&#32;question&#32;domains/logistics/coordinate-activities/q1.rq&#32;from&#32;branch&#32;main|
|Composition|- [Competency question logistics/coordinate-activities/q1](https://github.com/HyperAgents/hmas/blob/main/domains/logistics/coordinate-activities/q1.rq.ttl)|

#### Criterion detail
|Identifier|[syntax](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#syntax)|
|----|----|
|Title|Syntax&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;check&#32;wether&#32;the&#32;test&#32;subject&#32;is&#32;syntaxically&#32;correct&#32;or&#32;not.|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-163)|Identifier|`syntax-error`|
|[Section top](#pass-outcome-number-163)|Title|Correct&#32;syntax|
|[Section top](#pass-outcome-number-163)|Description|Test&#32;subject&#32;has&#32;a&#32;correct&#32;syntax|

***
### Pass Outcome number 164

[Jump to summary definition](#summary-Pass-164)	|	[Previous Pass outcome](#pass-outcome-number-163)	|	[Next Pass outcome](#pass-outcome-number-165)

:white_check_mark:Pass outcome
#### Subject detail
|Name|question-logistics-coordinate-activities-q1|
|----|----|
|Title|competency&#32;question&#32;domains/logistics/coordinate-activities/q1.rq&#32;from&#32;branch&#32;main|
|Composition|- [Competency question logistics/coordinate-activities/q1](https://github.com/HyperAgents/hmas/blob/main/domains/logistics/coordinate-activities/q1.rq.ttl)|

#### Criterion detail
|Identifier|[uri-validity](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#uri-validity)|
|----|----|
|Title|URI&#32;validity&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;check&#32;if&#32;all&#32;the&#32;URIs&#32;of&#32;the&#32;resource&#32;are&#32;well-formed|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-164)|Identifier|`invalid-uri`|
|[Section top](#pass-outcome-number-164)|Title|All&#32;subject&#32;URI&#32;valid|
|[Section top](#pass-outcome-number-164)|Description|All&#32;the&#32;URIs&#32;of&#32;the&#32;subject&#32;are&#32;valid|

***
### Pass Outcome number 165

[Jump to summary definition](#summary-Pass-165)	|	[Previous Pass outcome](#pass-outcome-number-164)	|	[Next Pass outcome](#pass-outcome-number-166)

:white_check_mark:Pass outcome
#### Subject detail
|Name|question-logistics-configure-organization-q4|
|----|----|
|Title|competency&#32;question&#32;domains/logistics/configure-organization/q4.rq&#32;from&#32;branch&#32;main|
|Composition|- [Competency question logistics/configure-organization/q4](https://github.com/HyperAgents/hmas/blob/main/domains/logistics/configure-organization/q4.rq.ttl)|

#### Criterion detail
|Identifier|[namespace-validity](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#namespace-validity)|
|----|----|
|Title|Prefix&#32;validity&#32;test|
|Description|A&#32;test&#32;case&#32;checking&#32;if&#32;all&#32;the&#32;prefixes&#32;are&#32;not&#32;too&#32;close&#32;from&#32;the&#32;most&#32;used&#32;existing&#32;namespaces&#32;(according&#32;to&#32;prefix&#32;cc)&#32;or&#32;an&#32;ontology&#32;namespace|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-165)|Identifier|`namespace-typo`|
|[Section top](#pass-outcome-number-165)|Title|No&#32;namespace&#32;typo|
|[Section top](#pass-outcome-number-165)|Description|It&#32;seems&#32;that&#32;none&#32;of&#32;the&#32;subject&#32;URIs&#32;have&#32;namespaces&#32;typos|

***
### Pass Outcome number 166

[Jump to summary definition](#summary-Pass-166)	|	[Previous Pass outcome](#pass-outcome-number-165)	|	[Next Pass outcome](#pass-outcome-number-167)

:white_check_mark:Pass outcome
#### Subject detail
|Name|question-logistics-configure-organization-q4|
|----|----|
|Title|competency&#32;question&#32;domains/logistics/configure-organization/q4.rq&#32;from&#32;branch&#32;main|
|Composition|- [Competency question logistics/configure-organization/q4](https://github.com/HyperAgents/hmas/blob/main/domains/logistics/configure-organization/q4.rq.ttl)|

#### Criterion detail
|Identifier|[query-type](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#query-type)|
|----|----|
|Title|Query&#32;type&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;check&#32;if&#32;the&#32;query&#32;is&#32;indeed&#32;of&#32;type&#32;Select&#32;or&#32;Ask|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-166)|Identifier|`wrong-query-type`|
|[Section top](#pass-outcome-number-166)|Title|Accurate&#32;query&#32;type|
|[Section top](#pass-outcome-number-166)|Description|The&#32;query&#32;is&#32;of&#32;type&#32;Select&#32;or&#32;Ask|

***
### Pass Outcome number 167

[Jump to summary definition](#summary-Pass-167)	|	[Previous Pass outcome](#pass-outcome-number-166)	|	[Next Pass outcome](#pass-outcome-number-168)

:white_check_mark:Pass outcome
#### Subject detail
|Name|question-logistics-configure-organization-q4|
|----|----|
|Title|competency&#32;question&#32;domains/logistics/configure-organization/q4.rq&#32;from&#32;branch&#32;main|
|Composition|- [Competency question logistics/configure-organization/q4](https://github.com/HyperAgents/hmas/blob/main/domains/logistics/configure-organization/q4.rq.ttl)|

#### Criterion detail
|Identifier|[syntax](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#syntax)|
|----|----|
|Title|Syntax&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;check&#32;wether&#32;the&#32;test&#32;subject&#32;is&#32;syntaxically&#32;correct&#32;or&#32;not.|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-167)|Identifier|`syntax-error`|
|[Section top](#pass-outcome-number-167)|Title|Correct&#32;syntax|
|[Section top](#pass-outcome-number-167)|Description|Test&#32;subject&#32;has&#32;a&#32;correct&#32;syntax|

***
### Pass Outcome number 168

[Jump to summary definition](#summary-Pass-168)	|	[Previous Pass outcome](#pass-outcome-number-167)	|	[Next Pass outcome](#pass-outcome-number-169)

:white_check_mark:Pass outcome
#### Subject detail
|Name|question-logistics-configure-organization-q4|
|----|----|
|Title|competency&#32;question&#32;domains/logistics/configure-organization/q4.rq&#32;from&#32;branch&#32;main|
|Composition|- [Competency question logistics/configure-organization/q4](https://github.com/HyperAgents/hmas/blob/main/domains/logistics/configure-organization/q4.rq.ttl)|

#### Criterion detail
|Identifier|[uri-validity](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#uri-validity)|
|----|----|
|Title|URI&#32;validity&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;check&#32;if&#32;all&#32;the&#32;URIs&#32;of&#32;the&#32;resource&#32;are&#32;well-formed|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-168)|Identifier|`invalid-uri`|
|[Section top](#pass-outcome-number-168)|Title|All&#32;subject&#32;URI&#32;valid|
|[Section top](#pass-outcome-number-168)|Description|All&#32;the&#32;URIs&#32;of&#32;the&#32;subject&#32;are&#32;valid|

***
### Pass Outcome number 169

[Jump to summary definition](#summary-Pass-169)	|	[Previous Pass outcome](#pass-outcome-number-168)	|	[Next Pass outcome](#pass-outcome-number-170)

:white_check_mark:Pass outcome
#### Subject detail
|Name|question-logistics-configure-organization-q3|
|----|----|
|Title|competency&#32;question&#32;domains/logistics/configure-organization/q3.rq&#32;from&#32;branch&#32;main|
|Composition|- [Competency question logistics/configure-organization/q3](https://github.com/HyperAgents/hmas/blob/main/domains/logistics/configure-organization/q3.rq.ttl)|

#### Criterion detail
|Identifier|[namespace-validity](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#namespace-validity)|
|----|----|
|Title|Prefix&#32;validity&#32;test|
|Description|A&#32;test&#32;case&#32;checking&#32;if&#32;all&#32;the&#32;prefixes&#32;are&#32;not&#32;too&#32;close&#32;from&#32;the&#32;most&#32;used&#32;existing&#32;namespaces&#32;(according&#32;to&#32;prefix&#32;cc)&#32;or&#32;an&#32;ontology&#32;namespace|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-169)|Identifier|`namespace-typo`|
|[Section top](#pass-outcome-number-169)|Title|No&#32;namespace&#32;typo|
|[Section top](#pass-outcome-number-169)|Description|It&#32;seems&#32;that&#32;none&#32;of&#32;the&#32;subject&#32;URIs&#32;have&#32;namespaces&#32;typos|

***
### Pass Outcome number 170

[Jump to summary definition](#summary-Pass-170)	|	[Previous Pass outcome](#pass-outcome-number-169)	|	[Next Pass outcome](#pass-outcome-number-171)

:white_check_mark:Pass outcome
#### Subject detail
|Name|question-logistics-configure-organization-q3|
|----|----|
|Title|competency&#32;question&#32;domains/logistics/configure-organization/q3.rq&#32;from&#32;branch&#32;main|
|Composition|- [Competency question logistics/configure-organization/q3](https://github.com/HyperAgents/hmas/blob/main/domains/logistics/configure-organization/q3.rq.ttl)|

#### Criterion detail
|Identifier|[query-type](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#query-type)|
|----|----|
|Title|Query&#32;type&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;check&#32;if&#32;the&#32;query&#32;is&#32;indeed&#32;of&#32;type&#32;Select&#32;or&#32;Ask|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-170)|Identifier|`wrong-query-type`|
|[Section top](#pass-outcome-number-170)|Title|Accurate&#32;query&#32;type|
|[Section top](#pass-outcome-number-170)|Description|The&#32;query&#32;is&#32;of&#32;type&#32;Select&#32;or&#32;Ask|

***
### Pass Outcome number 171

[Jump to summary definition](#summary-Pass-171)	|	[Previous Pass outcome](#pass-outcome-number-170)	|	[Next Pass outcome](#pass-outcome-number-172)

:white_check_mark:Pass outcome
#### Subject detail
|Name|question-logistics-configure-organization-q3|
|----|----|
|Title|competency&#32;question&#32;domains/logistics/configure-organization/q3.rq&#32;from&#32;branch&#32;main|
|Composition|- [Competency question logistics/configure-organization/q3](https://github.com/HyperAgents/hmas/blob/main/domains/logistics/configure-organization/q3.rq.ttl)|

#### Criterion detail
|Identifier|[syntax](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#syntax)|
|----|----|
|Title|Syntax&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;check&#32;wether&#32;the&#32;test&#32;subject&#32;is&#32;syntaxically&#32;correct&#32;or&#32;not.|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-171)|Identifier|`syntax-error`|
|[Section top](#pass-outcome-number-171)|Title|Correct&#32;syntax|
|[Section top](#pass-outcome-number-171)|Description|Test&#32;subject&#32;has&#32;a&#32;correct&#32;syntax|

***
### Pass Outcome number 172

[Jump to summary definition](#summary-Pass-172)	|	[Previous Pass outcome](#pass-outcome-number-171)	|	[Next Pass outcome](#pass-outcome-number-173)

:white_check_mark:Pass outcome
#### Subject detail
|Name|question-logistics-configure-organization-q3|
|----|----|
|Title|competency&#32;question&#32;domains/logistics/configure-organization/q3.rq&#32;from&#32;branch&#32;main|
|Composition|- [Competency question logistics/configure-organization/q3](https://github.com/HyperAgents/hmas/blob/main/domains/logistics/configure-organization/q3.rq.ttl)|

#### Criterion detail
|Identifier|[uri-validity](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#uri-validity)|
|----|----|
|Title|URI&#32;validity&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;check&#32;if&#32;all&#32;the&#32;URIs&#32;of&#32;the&#32;resource&#32;are&#32;well-formed|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-172)|Identifier|`invalid-uri`|
|[Section top](#pass-outcome-number-172)|Title|All&#32;subject&#32;URI&#32;valid|
|[Section top](#pass-outcome-number-172)|Description|All&#32;the&#32;URIs&#32;of&#32;the&#32;subject&#32;are&#32;valid|

***
### Pass Outcome number 173

[Jump to summary definition](#summary-Pass-173)	|	[Previous Pass outcome](#pass-outcome-number-172)	|	[Next Pass outcome](#pass-outcome-number-174)

:white_check_mark:Pass outcome
#### Subject detail
|Name|question-logistics-configure-organization-q2|
|----|----|
|Title|competency&#32;question&#32;domains/logistics/configure-organization/q2.rq&#32;from&#32;branch&#32;main|
|Composition|- [Competency question logistics/configure-organization/q2](https://github.com/HyperAgents/hmas/blob/main/domains/logistics/configure-organization/q2.rq.ttl)|

#### Criterion detail
|Identifier|[namespace-validity](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#namespace-validity)|
|----|----|
|Title|Prefix&#32;validity&#32;test|
|Description|A&#32;test&#32;case&#32;checking&#32;if&#32;all&#32;the&#32;prefixes&#32;are&#32;not&#32;too&#32;close&#32;from&#32;the&#32;most&#32;used&#32;existing&#32;namespaces&#32;(according&#32;to&#32;prefix&#32;cc)&#32;or&#32;an&#32;ontology&#32;namespace|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-173)|Identifier|`namespace-typo`|
|[Section top](#pass-outcome-number-173)|Title|No&#32;namespace&#32;typo|
|[Section top](#pass-outcome-number-173)|Description|It&#32;seems&#32;that&#32;none&#32;of&#32;the&#32;subject&#32;URIs&#32;have&#32;namespaces&#32;typos|

***
### Pass Outcome number 174

[Jump to summary definition](#summary-Pass-174)	|	[Previous Pass outcome](#pass-outcome-number-173)	|	[Next Pass outcome](#pass-outcome-number-175)

:white_check_mark:Pass outcome
#### Subject detail
|Name|question-logistics-configure-organization-q2|
|----|----|
|Title|competency&#32;question&#32;domains/logistics/configure-organization/q2.rq&#32;from&#32;branch&#32;main|
|Composition|- [Competency question logistics/configure-organization/q2](https://github.com/HyperAgents/hmas/blob/main/domains/logistics/configure-organization/q2.rq.ttl)|

#### Criterion detail
|Identifier|[query-type](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#query-type)|
|----|----|
|Title|Query&#32;type&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;check&#32;if&#32;the&#32;query&#32;is&#32;indeed&#32;of&#32;type&#32;Select&#32;or&#32;Ask|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-174)|Identifier|`wrong-query-type`|
|[Section top](#pass-outcome-number-174)|Title|Accurate&#32;query&#32;type|
|[Section top](#pass-outcome-number-174)|Description|The&#32;query&#32;is&#32;of&#32;type&#32;Select&#32;or&#32;Ask|

***
### Pass Outcome number 175

[Jump to summary definition](#summary-Pass-175)	|	[Previous Pass outcome](#pass-outcome-number-174)	|	[Next Pass outcome](#pass-outcome-number-176)

:white_check_mark:Pass outcome
#### Subject detail
|Name|question-logistics-configure-organization-q2|
|----|----|
|Title|competency&#32;question&#32;domains/logistics/configure-organization/q2.rq&#32;from&#32;branch&#32;main|
|Composition|- [Competency question logistics/configure-organization/q2](https://github.com/HyperAgents/hmas/blob/main/domains/logistics/configure-organization/q2.rq.ttl)|

#### Criterion detail
|Identifier|[syntax](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#syntax)|
|----|----|
|Title|Syntax&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;check&#32;wether&#32;the&#32;test&#32;subject&#32;is&#32;syntaxically&#32;correct&#32;or&#32;not.|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-175)|Identifier|`syntax-error`|
|[Section top](#pass-outcome-number-175)|Title|Correct&#32;syntax|
|[Section top](#pass-outcome-number-175)|Description|Test&#32;subject&#32;has&#32;a&#32;correct&#32;syntax|

***
### Pass Outcome number 176

[Jump to summary definition](#summary-Pass-176)	|	[Previous Pass outcome](#pass-outcome-number-175)	|	[Next Pass outcome](#pass-outcome-number-177)

:white_check_mark:Pass outcome
#### Subject detail
|Name|question-logistics-configure-organization-q2|
|----|----|
|Title|competency&#32;question&#32;domains/logistics/configure-organization/q2.rq&#32;from&#32;branch&#32;main|
|Composition|- [Competency question logistics/configure-organization/q2](https://github.com/HyperAgents/hmas/blob/main/domains/logistics/configure-organization/q2.rq.ttl)|

#### Criterion detail
|Identifier|[uri-validity](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#uri-validity)|
|----|----|
|Title|URI&#32;validity&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;check&#32;if&#32;all&#32;the&#32;URIs&#32;of&#32;the&#32;resource&#32;are&#32;well-formed|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-176)|Identifier|`invalid-uri`|
|[Section top](#pass-outcome-number-176)|Title|All&#32;subject&#32;URI&#32;valid|
|[Section top](#pass-outcome-number-176)|Description|All&#32;the&#32;URIs&#32;of&#32;the&#32;subject&#32;are&#32;valid|

***
### Pass Outcome number 177

[Jump to summary definition](#summary-Pass-177)	|	[Previous Pass outcome](#pass-outcome-number-176)	|	[Next Pass outcome](#pass-outcome-number-178)

:white_check_mark:Pass outcome
#### Subject detail
|Name|question-logistics-configure-organization-q1|
|----|----|
|Title|competency&#32;question&#32;domains/logistics/configure-organization/q1.rq&#32;from&#32;branch&#32;main|
|Composition|- [Competency question logistics/configure-organization/q1](https://github.com/HyperAgents/hmas/blob/main/domains/logistics/configure-organization/q1.rq.ttl)|

#### Criterion detail
|Identifier|[namespace-validity](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#namespace-validity)|
|----|----|
|Title|Prefix&#32;validity&#32;test|
|Description|A&#32;test&#32;case&#32;checking&#32;if&#32;all&#32;the&#32;prefixes&#32;are&#32;not&#32;too&#32;close&#32;from&#32;the&#32;most&#32;used&#32;existing&#32;namespaces&#32;(according&#32;to&#32;prefix&#32;cc)&#32;or&#32;an&#32;ontology&#32;namespace|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-177)|Identifier|`namespace-typo`|
|[Section top](#pass-outcome-number-177)|Title|No&#32;namespace&#32;typo|
|[Section top](#pass-outcome-number-177)|Description|It&#32;seems&#32;that&#32;none&#32;of&#32;the&#32;subject&#32;URIs&#32;have&#32;namespaces&#32;typos|

***
### Pass Outcome number 178

[Jump to summary definition](#summary-Pass-178)	|	[Previous Pass outcome](#pass-outcome-number-177)	|	[Next Pass outcome](#pass-outcome-number-179)

:white_check_mark:Pass outcome
#### Subject detail
|Name|question-logistics-configure-organization-q1|
|----|----|
|Title|competency&#32;question&#32;domains/logistics/configure-organization/q1.rq&#32;from&#32;branch&#32;main|
|Composition|- [Competency question logistics/configure-organization/q1](https://github.com/HyperAgents/hmas/blob/main/domains/logistics/configure-organization/q1.rq.ttl)|

#### Criterion detail
|Identifier|[query-type](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#query-type)|
|----|----|
|Title|Query&#32;type&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;check&#32;if&#32;the&#32;query&#32;is&#32;indeed&#32;of&#32;type&#32;Select&#32;or&#32;Ask|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-178)|Identifier|`wrong-query-type`|
|[Section top](#pass-outcome-number-178)|Title|Accurate&#32;query&#32;type|
|[Section top](#pass-outcome-number-178)|Description|The&#32;query&#32;is&#32;of&#32;type&#32;Select&#32;or&#32;Ask|

***
### Pass Outcome number 179

[Jump to summary definition](#summary-Pass-179)	|	[Previous Pass outcome](#pass-outcome-number-178)	|	[Next Pass outcome](#pass-outcome-number-180)

:white_check_mark:Pass outcome
#### Subject detail
|Name|question-logistics-configure-organization-q1|
|----|----|
|Title|competency&#32;question&#32;domains/logistics/configure-organization/q1.rq&#32;from&#32;branch&#32;main|
|Composition|- [Competency question logistics/configure-organization/q1](https://github.com/HyperAgents/hmas/blob/main/domains/logistics/configure-organization/q1.rq.ttl)|

#### Criterion detail
|Identifier|[syntax](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#syntax)|
|----|----|
|Title|Syntax&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;check&#32;wether&#32;the&#32;test&#32;subject&#32;is&#32;syntaxically&#32;correct&#32;or&#32;not.|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-179)|Identifier|`syntax-error`|
|[Section top](#pass-outcome-number-179)|Title|Correct&#32;syntax|
|[Section top](#pass-outcome-number-179)|Description|Test&#32;subject&#32;has&#32;a&#32;correct&#32;syntax|

***
### Pass Outcome number 180

[Jump to summary definition](#summary-Pass-180)	|	[Previous Pass outcome](#pass-outcome-number-179)	|	[Next Pass outcome](#pass-outcome-number-181)

:white_check_mark:Pass outcome
#### Subject detail
|Name|question-logistics-configure-organization-q1|
|----|----|
|Title|competency&#32;question&#32;domains/logistics/configure-organization/q1.rq&#32;from&#32;branch&#32;main|
|Composition|- [Competency question logistics/configure-organization/q1](https://github.com/HyperAgents/hmas/blob/main/domains/logistics/configure-organization/q1.rq.ttl)|

#### Criterion detail
|Identifier|[uri-validity](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#uri-validity)|
|----|----|
|Title|URI&#32;validity&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;check&#32;if&#32;all&#32;the&#32;URIs&#32;of&#32;the&#32;resource&#32;are&#32;well-formed|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-180)|Identifier|`invalid-uri`|
|[Section top](#pass-outcome-number-180)|Title|All&#32;subject&#32;URI&#32;valid|
|[Section top](#pass-outcome-number-180)|Description|All&#32;the&#32;URIs&#32;of&#32;the&#32;subject&#32;are&#32;valid|

***
### Pass Outcome number 181

[Jump to summary definition](#summary-Pass-181)	|	[Previous Pass outcome](#pass-outcome-number-180)	|	[Next Pass outcome](#pass-outcome-number-182)

:white_check_mark:Pass outcome
#### Subject detail
|Name|question-domain-template-scenario-template-q1|
|----|----|
|Title|competency&#32;question&#32;domains/domain-template/scenario-template/q1.rq&#32;from&#32;branch&#32;main|
|Composition|- [Competency question domain-template/scenario-template/q1](https://github.com/HyperAgents/hmas/blob/main/domains/domain-template/scenario-template/q1.rq.ttl)|

#### Criterion detail
|Identifier|[namespace-validity](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#namespace-validity)|
|----|----|
|Title|Prefix&#32;validity&#32;test|
|Description|A&#32;test&#32;case&#32;checking&#32;if&#32;all&#32;the&#32;prefixes&#32;are&#32;not&#32;too&#32;close&#32;from&#32;the&#32;most&#32;used&#32;existing&#32;namespaces&#32;(according&#32;to&#32;prefix&#32;cc)&#32;or&#32;an&#32;ontology&#32;namespace|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-181)|Identifier|`namespace-typo`|
|[Section top](#pass-outcome-number-181)|Title|No&#32;namespace&#32;typo|
|[Section top](#pass-outcome-number-181)|Description|It&#32;seems&#32;that&#32;none&#32;of&#32;the&#32;subject&#32;URIs&#32;have&#32;namespaces&#32;typos|

***
### Pass Outcome number 182

[Jump to summary definition](#summary-Pass-182)	|	[Previous Pass outcome](#pass-outcome-number-181)	|	[Next Pass outcome](#pass-outcome-number-183)

:white_check_mark:Pass outcome
#### Subject detail
|Name|question-domain-template-scenario-template-q1|
|----|----|
|Title|competency&#32;question&#32;domains/domain-template/scenario-template/q1.rq&#32;from&#32;branch&#32;main|
|Composition|- [Competency question domain-template/scenario-template/q1](https://github.com/HyperAgents/hmas/blob/main/domains/domain-template/scenario-template/q1.rq.ttl)|

#### Criterion detail
|Identifier|[query-type](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#query-type)|
|----|----|
|Title|Query&#32;type&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;check&#32;if&#32;the&#32;query&#32;is&#32;indeed&#32;of&#32;type&#32;Select&#32;or&#32;Ask|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-182)|Identifier|`wrong-query-type`|
|[Section top](#pass-outcome-number-182)|Title|Accurate&#32;query&#32;type|
|[Section top](#pass-outcome-number-182)|Description|The&#32;query&#32;is&#32;of&#32;type&#32;Select&#32;or&#32;Ask|

***
### Pass Outcome number 183

[Jump to summary definition](#summary-Pass-183)	|	[Previous Pass outcome](#pass-outcome-number-182)	|	[Next Pass outcome](#pass-outcome-number-184)

:white_check_mark:Pass outcome
#### Subject detail
|Name|question-domain-template-scenario-template-q1|
|----|----|
|Title|competency&#32;question&#32;domains/domain-template/scenario-template/q1.rq&#32;from&#32;branch&#32;main|
|Composition|- [Competency question domain-template/scenario-template/q1](https://github.com/HyperAgents/hmas/blob/main/domains/domain-template/scenario-template/q1.rq.ttl)|

#### Criterion detail
|Identifier|[syntax](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#syntax)|
|----|----|
|Title|Syntax&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;check&#32;wether&#32;the&#32;test&#32;subject&#32;is&#32;syntaxically&#32;correct&#32;or&#32;not.|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-183)|Identifier|`syntax-error`|
|[Section top](#pass-outcome-number-183)|Title|Correct&#32;syntax|
|[Section top](#pass-outcome-number-183)|Description|Test&#32;subject&#32;has&#32;a&#32;correct&#32;syntax|

***
### Pass Outcome number 184

[Jump to summary definition](#summary-Pass-184)	|	[Previous Pass outcome](#pass-outcome-number-183)	|	Next Pass outcome

:white_check_mark:Pass outcome
#### Subject detail
|Name|question-domain-template-scenario-template-q1|
|----|----|
|Title|competency&#32;question&#32;domains/domain-template/scenario-template/q1.rq&#32;from&#32;branch&#32;main|
|Composition|- [Competency question domain-template/scenario-template/q1](https://github.com/HyperAgents/hmas/blob/main/domains/domain-template/scenario-template/q1.rq.ttl)|

#### Criterion detail
|Identifier|[uri-validity](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#uri-validity)|
|----|----|
|Title|URI&#32;validity&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;check&#32;if&#32;all&#32;the&#32;URIs&#32;of&#32;the&#32;resource&#32;are&#32;well-formed|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-184)|Identifier|`invalid-uri`|
|[Section top](#pass-outcome-number-184)|Title|All&#32;subject&#32;URI&#32;valid|
|[Section top](#pass-outcome-number-184)|Description|All&#32;the&#32;URIs&#32;of&#32;the&#32;subject&#32;are&#32;valid|

***

</details>

***
