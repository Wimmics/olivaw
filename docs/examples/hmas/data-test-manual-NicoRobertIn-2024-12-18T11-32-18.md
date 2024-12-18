# Test Report Markdown Export

This file is an export of the RDF test report made out of [EARL vocabulary](https://www.w3.org/TR/EARL10/)

This test is powered by Corese, check [Corese website](https://project.inria.fr/corese/) and [Corese repository](https://github.com/Wimmics/corese)

The original test report is available in turtle syntax [here](./data-test-manual-NicoRobertIn-2024-12-18T11-32-18.ttl).

# Test Activity

Here is some information about the testing activity that led to this report

|Title|Data&#32;tests&#32;of&#32;[HyperAgents/hmas](https://github.com/HyperAgents/hmas)&#32;on&#32;branch&#32;HEAD|
|--|--|
|Description|[NicoRobertIn](https://github.com/NicoRobertIn)&#32;launch&#32;manual&#32;run&#32;of&#32;data&#32;tests&#32;against&#32;[HyperAgents/hmas](https://github.com/HyperAgents/hmas)&#32;on&#32;branch&#32;HEAD|
|Tester|[NicoRobertIn](https://github.com/NicoRobertIn)|
|Ontology|[HyperAgents/hmas](https://github.com/HyperAgents/hmas)|
|Ontology version|Local state `ca439d4144b23b3fe927509872babc8d82142fae`|
|Ontology version date|2024-12-18 11:32:12|
|Ontology previous version|[3b0b11eccd899dd65ac9c3bbf0c043e28b61b46b](https://github.com/HyperAgents/hmas/tree/3b0b11eccd899dd65ac9c3bbf0c043e28b61b46b)|
|Ontology branch|[HEAD](https://github.com/HyperAgents/hmas/tree/HEAD)|
|Olivaw suite|[olivaw data test suite](https://github.com/Wimmics/olivaw/blob/v0.0.7/olivaw/test/data/suite.py)|
|Olivaw version|[v0.0.7](https://pypi.org/project/olivaw/0.0.7)|
|Generated turtle|[Turtle report](./data-test-manual-NicoRobertIn-2024-12-18T11-32-18.ttl)|
|Generated Markdown|[Markdown report](./data-test-manual-NicoRobertIn-2024-12-18T11-32-18.md)|

# Statistic summary

Here is a short overview for this test report

55 Outcomes

:boom:1 MajorFail, :exclamation:2 MinorFail, :warning:12 CannotTell, :grey_question:0 NotTested, :white_check_mark:40 Pass

<div  style="border-radius: 12px; height: 25px; overflow: hidden"><img src="../assets/red.png" width="1%" height="25px"/><img src="../assets/orange.png" width="3%" height="25px"/><img src="../assets/grey.png" width="21%" height="25px"/><img src="../assets/white.png" width="0%" height="25px"/><img src="../assets/green.png" width="75%" height="25px"/></div>

<br/>

The different status types are an extension of the [EARL](https://www.w3.org/TR/EARL10-Schema/) vocabulary where the nextended terms can be found in the [olivaw ontology](https://ns.inria.fr/olivaw#), each outcome type means:
* :boom: MajorFail: This is an error that is critical and considered as blocking for production
* :exclamation: MinorFail: This is an error that should be fixed, but it cannot be considered as critical error
* :warning: CannotTell: It is unclear if the subject passed or failed the test. This happens when an automated test requires human judgement to make a final decision.
* :grey_question: NotTested:  The test has not been carried out. It is because some prerequisite tests did not end up as Pass.
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
|[Chapter top](#majorfail-outcomes)|<div id="summary-MajorFail-1">1/1</div>|:boom:MajorFail|`dataset-manufacturing-environments-safety-rules`|[syntax](https://ns.inria.fr/olivaw#syntax)|Test subject has syntax errors|[Jump](#majorfail-outcome-number-1)|

***

## MajorFail Outcomes Details

This subchapter gives more details to the :boom:MajorFail outcomes

### MajorFail Outcome number 1

[Jump to summary definition](#summary-MajorFail-1)	|	Previous MajorFail outcome	|	Next MajorFail outcome

:boom:MajorFail outcome
#### Subject detail
|Name|dataset-manufacturing-environments-safety-rules|
|----|----|
|Title|Standalone&#32;dataset&#32;domains/manufacturing-environments/safety-rules/dataset.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Dataset manufacturing-environments/safety-rules](https://github.com/HyperAgents/hmas/blob/HEAD/domains/manufacturing-environments/safety-rules/dataset.ttl)|

#### Criterion detail
|Identifier|[syntax](https://ns.inria.fr/olivaw#syntax)|
|----|----|
|Title|Syntax&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;check&#32;wether&#32;the&#32;test&#32;subject&#32;is&#32;syntaxically&#32;correct&#32;or&#32;not.|

#### Outcome Detail
|Jump|Type|:boom:MajorFail|
|----|----|----|
|[Section top](#majorfail-outcome-number-1)|Identifier|`syntax-error`|
|[Section top](#majorfail-outcome-number-1)|Title|Test&#32;subject&#32;has&#32;syntax&#32;errors|
|[Section top](#majorfail-outcome-number-1)|Description|Encountered&#32; &#34;.&#34; &#32;at&#32;line&#32;21,&#32;column&#32;112.|

***

</details>

***


# MinorFail Outcomes

[Jump to statistic summary](#statistic-summary)	|	[Previous section](#majorfail-outcomes)	|	[Next section](#cannottell-outcomes)

Here is the chapter related to the MinorFail outcome

:exclamation:2 MinorFail outcomes

<details>
<summary>Fold/Unfold the 2 summary and details</summary>

## MinorFail Outcomes Summary

:exclamation:2 MinorFail outcomes

|*Jump*|*Number*|*Status*|*Subject*|*Criterion*|*Title*|*Link*|
|------|--------|--------|---------|-----------|-------|------|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-1">1/2</div>|:exclamation:MinorFail|`usecase-manufacturing-dataset-v1`|[term-recognition](https://ns.inria.fr/olivaw#term-recognition)|Unknown ontology term|[Jump](#minorfail-outcome-number-1)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-2">2/2</div>|:exclamation:MinorFail|`dataset-manufacturing-environments-discover-platforms`|[term-recognition](https://ns.inria.fr/olivaw#term-recognition)|Unknown ontology term|[Jump](#minorfail-outcome-number-2)|

***

## MinorFail Outcomes Details

This subchapter gives more details to the :exclamation:MinorFail outcomes

### MinorFail Outcome number 1

[Jump to summary definition](#summary-MinorFail-1)	|	Previous MinorFail outcome	|	[Next MinorFail outcome](#minorfail-outcome-number-2)

:exclamation:MinorFail outcome
#### Subject detail
|Name|usecase-manufacturing-dataset-v1|
|----|----|
|Title|Standalone&#32;use&#32;case&#32;use-cases/manufacturing/dataset-v1.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Use case manufacturing/dataset-v1](https://github.com/HyperAgents/hmas/blob/HEAD/use-cases/manufacturing/dataset-v1.ttl)|

#### Criterion detail
|Identifier|[term-recognition](https://ns.inria.fr/olivaw#term-recognition)|
|----|----|
|Title|Term&#32;recognition&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;detect&#32;if&#32;all&#32;the&#32;terms&#32;from&#32;the&#32;subject&#32;that&#32;are&#32;from&#32;the&#32;ontology&#32;namespace&#32;are&#32;indeed&#32;defined&#32;in&#32;the&#32;ontology|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-1)|Identifier|`unknown-term`|
|[Section top](#minorfail-outcome-number-1)|Title|Unknown&#32;ontology&#32;term|
|[Section top](#minorfail-outcome-number-1)|Description|Some&#32;fragment&#32;terms&#32;are&#32;in&#32;ontology&#32;namespace&#32;but&#32;not&#32;defined&#32;in&#32;ontology|
|[Section top](#minorfail-outcome-number-1)|Pointer|<pre lang="Turtle"><code>Term&#32;not&#32;recognized:&#32; &#60;https://purl.org/hmas/Platform></code></pre>|
|[Section top](#minorfail-outcome-number-1)|Pointer|<pre lang="Turtle"><code>&#60;https://ns.inria.fr/hmas/#platform> &#32;a&#32;:Platform&#32;.</code></pre>|

***
### MinorFail Outcome number 2

[Jump to summary definition](#summary-MinorFail-2)	|	[Previous MinorFail outcome](#minorfail-outcome-number-1)	|	Next MinorFail outcome

:exclamation:MinorFail outcome
#### Subject detail
|Name|dataset-manufacturing-environments-discover-platforms|
|----|----|
|Title|Standalone&#32;dataset&#32;domains/manufacturing-environments/discover-platforms/dataset.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Dataset manufacturing-environments/discover-platforms](https://github.com/HyperAgents/hmas/blob/HEAD/domains/manufacturing-environments/discover-platforms/dataset.ttl)|

#### Criterion detail
|Identifier|[term-recognition](https://ns.inria.fr/olivaw#term-recognition)|
|----|----|
|Title|Term&#32;recognition&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;detect&#32;if&#32;all&#32;the&#32;terms&#32;from&#32;the&#32;subject&#32;that&#32;are&#32;from&#32;the&#32;ontology&#32;namespace&#32;are&#32;indeed&#32;defined&#32;in&#32;the&#32;ontology|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-2)|Identifier|`unknown-term`|
|[Section top](#minorfail-outcome-number-2)|Title|Unknown&#32;ontology&#32;term|
|[Section top](#minorfail-outcome-number-2)|Description|Some&#32;fragment&#32;terms&#32;are&#32;in&#32;ontology&#32;namespace&#32;but&#32;not&#32;defined&#32;in&#32;ontology|
|[Section top](#minorfail-outcome-number-2)|Pointer|<pre lang="Turtle"><code>Term&#32;not&#32;recognized:&#32; &#60;https://purl.org/hmas/hasResourceProfile></code></pre>|
|[Section top](#minorfail-outcome-number-2)|Pointer|<pre lang="Turtle"><code>&#60;http://example.org/platformSaintEtienne> &#32;:hasResourceProfile&#32; &#60;http://example.org/platformSaintEtienneProfile> &#32;.</code></pre>|

***

</details>

***


# CannotTell Outcomes

[Jump to statistic summary](#statistic-summary)	|	[Previous section](#minorfail-outcomes)	|	[Next section](#pass-outcomes)

Here is the chapter related to the CannotTell outcome

:warning:12 CannotTell outcomes

<details>
<summary>Fold/Unfold the 12 summary and details</summary>

## CannotTell Outcomes Summary

:warning:12 CannotTell outcomes

|*Jump*|*Number*|*Status*|*Subject*|*Criterion*|*Title*|*Link*|
|------|--------|--------|---------|-----------|-------|------|
|[Chapter top](#cannottell-outcomes)|<div id="summary-CannotTell-1">1/12</div>|:warning:CannotTell|`usecase-manufacturing-dataset-v1`|[namespace-validity](https://ns.inria.fr/olivaw#namespace-validity)|Possible namespace typo|[Jump](#cannottell-outcome-number-1)|
|[Chapter top](#cannottell-outcomes)|<div id="summary-CannotTell-2">2/12</div>|:warning:CannotTell|`usecase-manufacturing-dataset-v1`|[namespace-validity](https://ns.inria.fr/olivaw#namespace-validity)|Possible namespace typo|[Jump](#cannottell-outcome-number-2)|
|[Chapter top](#cannottell-outcomes)|<div id="summary-CannotTell-3">3/12</div>|:warning:CannotTell|`usecase-manufacturing-dataset-v1`|[namespace-validity](https://ns.inria.fr/olivaw#namespace-validity)|Possible namespace typo|[Jump](#cannottell-outcome-number-3)|
|[Chapter top](#cannottell-outcomes)|<div id="summary-CannotTell-4">4/12</div>|:warning:CannotTell|`usecase-manufacturing-dataset-v1`|[namespace-validity](https://ns.inria.fr/olivaw#namespace-validity)|Possible namespace typo|[Jump](#cannottell-outcome-number-4)|
|[Chapter top](#cannottell-outcomes)|<div id="summary-CannotTell-5">5/12</div>|:warning:CannotTell|`usecase-manufacturing-dataset-v1`|[namespace-validity](https://ns.inria.fr/olivaw#namespace-validity)|Possible namespace typo|[Jump](#cannottell-outcome-number-5)|
|[Chapter top](#cannottell-outcomes)|<div id="summary-CannotTell-6">6/12</div>|:warning:CannotTell|`usecase-manufacturing-dataset-v1`|[namespace-validity](https://ns.inria.fr/olivaw#namespace-validity)|Possible namespace typo|[Jump](#cannottell-outcome-number-6)|
|[Chapter top](#cannottell-outcomes)|<div id="summary-CannotTell-7">7/12</div>|:warning:CannotTell|`usecase-manufacturing-dataset-v1`|[namespace-validity](https://ns.inria.fr/olivaw#namespace-validity)|Possible namespace typo|[Jump](#cannottell-outcome-number-7)|
|[Chapter top](#cannottell-outcomes)|<div id="summary-CannotTell-8">8/12</div>|:warning:CannotTell|`usecase-manufacturing-dataset-v1`|[namespace-validity](https://ns.inria.fr/olivaw#namespace-validity)|Possible namespace typo|[Jump](#cannottell-outcome-number-8)|
|[Chapter top](#cannottell-outcomes)|<div id="summary-CannotTell-9">9/12</div>|:warning:CannotTell|`usecase-manufacturing-dataset-v1`|[namespace-validity](https://ns.inria.fr/olivaw#namespace-validity)|Possible namespace typo|[Jump](#cannottell-outcome-number-9)|
|[Chapter top](#cannottell-outcomes)|<div id="summary-CannotTell-10">10/12</div>|:warning:CannotTell|`usecase-manufacturing-dataset-v1`|[namespace-validity](https://ns.inria.fr/olivaw#namespace-validity)|Possible namespace typo|[Jump](#cannottell-outcome-number-10)|
|[Chapter top](#cannottell-outcomes)|<div id="summary-CannotTell-11">11/12</div>|:warning:CannotTell|`dataset-manufacturing-environments-discover-behavior-specifications`|[namespace-validity](https://ns.inria.fr/olivaw#namespace-validity)|Possible namespace typo|[Jump](#cannottell-outcome-number-11)|
|[Chapter top](#cannottell-outcomes)|<div id="summary-CannotTell-12">12/12</div>|:warning:CannotTell|`dataset-manufacturing-environments-discover-behavior-specifications`|[namespace-validity](https://ns.inria.fr/olivaw#namespace-validity)|Possible namespace typo|[Jump](#cannottell-outcome-number-12)|

***

## CannotTell Outcomes Details

This subchapter gives more details to the :warning:CannotTell outcomes

### CannotTell Outcome number 1

[Jump to summary definition](#summary-CannotTell-1)	|	Previous CannotTell outcome	|	[Next CannotTell outcome](#cannottell-outcome-number-2)

:warning:CannotTell outcome
#### Subject detail
|Name|usecase-manufacturing-dataset-v1|
|----|----|
|Title|Standalone&#32;use&#32;case&#32;use-cases/manufacturing/dataset-v1.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Use case manufacturing/dataset-v1](https://github.com/HyperAgents/hmas/blob/HEAD/use-cases/manufacturing/dataset-v1.ttl)|

#### Criterion detail
|Identifier|[namespace-validity](https://ns.inria.fr/olivaw#namespace-validity)|
|----|----|
|Title|Namespace&#32;validity&#32;test|
|Description|A&#32;test&#32;case&#32;checking&#32;if&#32;all&#32;the&#32;Namespaces&#32;are&#32;not&#32;too&#32;close&#32;from&#32;the&#32;most&#32;used&#32;existing&#32;namespaces&#32;(according&#32;to&#32;prefix&#32;cc)&#32;or&#32;an&#32;ontology&#32;namespace|

#### Outcome Detail
|Jump|Type|:warning:CannotTell|
|----|----|----|
|[Section top](#cannottell-outcome-number-1)|Identifier|`namespace-typo`|
|[Section top](#cannottell-outcome-number-1)|Title|Possible&#32;namespace&#32;typo|
|[Section top](#cannottell-outcome-number-1)|Description|The&#32;following&#32;namespace&#32;seems&#32;suspicious:  &#10; &#32;http://192.168.1.26/properties/&#32;  &#10;Was&#32;it&#32;supposed&#32;to&#32;correspond&#32;to&#32;one&#32;of&#32;these&#32;namespaces?|
|[Section top](#cannottell-outcome-number-1)|Pointer|<pre lang="Turtle"><code>Namespace&#32;usage&#32;in&#32;the&#32;subject&#32;file:</code></pre>|
|[Section top](#cannottell-outcome-number-1)|Pointer|<pre lang="Turtle"><code>&#91;]&#32;hctl:hasTarget&#32; &#60;http://192.168.1.26/properties/pmu> &#32;.</code></pre>|
|[Section top](#cannottell-outcome-number-1)|Pointer|<pre lang="Turtle"><code>Similar&#32;namespace&#32;found&#32;in&#32;file:  &#10;.&#92;use-cases&#92;manufacturing&#92;dataset-v1.ttl&#32;  &#10;Namespace&#32;found:  &#10;http://192.168.1.29/properties/</code></pre>|
|[Section top](#cannottell-outcome-number-1)|Pointer|<pre lang="Turtle"><code>&#91;]&#32;hctl:hasTarget&#32;similar-namespace:imu&#32;.</code></pre>|

***
### CannotTell Outcome number 2

[Jump to summary definition](#summary-CannotTell-2)	|	[Previous CannotTell outcome](#cannottell-outcome-number-1)	|	[Next CannotTell outcome](#cannottell-outcome-number-3)

:warning:CannotTell outcome
#### Subject detail
|Name|usecase-manufacturing-dataset-v1|
|----|----|
|Title|Standalone&#32;use&#32;case&#32;use-cases/manufacturing/dataset-v1.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Use case manufacturing/dataset-v1](https://github.com/HyperAgents/hmas/blob/HEAD/use-cases/manufacturing/dataset-v1.ttl)|

#### Criterion detail
|Identifier|[namespace-validity](https://ns.inria.fr/olivaw#namespace-validity)|
|----|----|
|Title|Namespace&#32;validity&#32;test|
|Description|A&#32;test&#32;case&#32;checking&#32;if&#32;all&#32;the&#32;Namespaces&#32;are&#32;not&#32;too&#32;close&#32;from&#32;the&#32;most&#32;used&#32;existing&#32;namespaces&#32;(according&#32;to&#32;prefix&#32;cc)&#32;or&#32;an&#32;ontology&#32;namespace|

#### Outcome Detail
|Jump|Type|:warning:CannotTell|
|----|----|----|
|[Section top](#cannottell-outcome-number-2)|Identifier|`namespace-typo`|
|[Section top](#cannottell-outcome-number-2)|Title|Possible&#32;namespace&#32;typo|
|[Section top](#cannottell-outcome-number-2)|Description|The&#32;following&#32;namespace&#32;seems&#32;suspicious:  &#10; &#32;http://www.w3.org/2011/http#&#32;  &#10;Was&#32;it&#32;supposed&#32;to&#32;correspond&#32;to&#32;one&#32;of&#32;these&#32;namespaces?|
|[Section top](#cannottell-outcome-number-2)|Pointer|<pre lang="Turtle"><code>Namespace&#32;usage&#32;in&#32;the&#32;subject&#32;file:</code></pre>|
|[Section top](#cannottell-outcome-number-2)|Pointer|<pre lang="Turtle"><code>&#91;]&#32;htv:methodName&#32; &#34;PUT&#34; &#32;.  &#10; &#91;]&#32;htv:methodName&#32; &#34;GET&#34; &#32;.  &#10; &#91;]&#32;owl:onProperty&#32;htv:methodName&#32;.  &#10; &#91;]&#32;htv:methodName&#32; &#34;PUT&#34; &#32;.  &#10; &#91;]&#32;htv:methodName&#32; &#34;GET&#34; &#32;.  &#10; &#91;]&#32;htv:methodName&#32; &#34;GET&#34; &#32;.  &#10; &#91;]&#32;htv:methodName&#32; &#34;GET&#34; &#32;.  &#10; &#91;]&#32;owl:onProperty&#32;htv:methodName&#32;.  &#10; &#91;]&#32;htv:methodName&#32; &#34;POST&#34; &#32;.  &#10; &#91;]&#32;htv:methodName&#32; &#34;POST&#34; &#32;.  &#10; &#91;]&#32;htv:methodName&#32; &#34;GET&#34; &#32;.  &#10; &#91;]&#32;owl:onProperty&#32;htv:methodName&#32;.  &#10; &#91;]&#32;htv:methodName&#32; &#34;GET&#34; &#32;.  &#10; &#91;]&#32;owl:onProperty&#32;htv:methodName&#32;.  &#10; &#91;]&#32;htv:methodName&#32; &#34;DELETE&#34; &#32;.  &#10; &#91;]&#32;htv:methodName&#32; &#34;DELETE&#34; &#32;.  &#10; &#91;]&#32;htv:methodName&#32; &#34;PUT&#34; &#32;.  &#10; &#91;]&#32;htv:methodName&#32; &#34;PUT&#34; &#32;.  &#10; &#91;]&#32;htv:methodName&#32; &#34;PUT&#34; &#32;.  &#10; &#91;]&#32;htv:methodName&#32; &#34;PUT&#34; &#32;.  &#10; &#91;]&#32;htv:methodName&#32; &#34;GET&#34; &#32;.  &#10; &#91;]&#32;htv:methodName&#32; &#34;GET&#34; &#32;.  &#10; &#91;]&#32;htv:methodName&#32; &#34;POST&#34; &#32;.  &#10; &#91;]&#32;htv:methodName&#32; &#34;GET&#34; &#32;.  &#10; &#91;]&#32;htv:methodName&#32; &#34;GET&#34; &#32;.</code></pre>|
|[Section top](#cannottell-outcome-number-2)|Pointer|<pre lang="Turtle"><code>Common&#32;namespace&#32;found&#32;  &#10;@prefix&#32;httpvoc:&#32; &#60;http://www.w3.org/2006/http#> &#32;.</code></pre>|

***
### CannotTell Outcome number 3

[Jump to summary definition](#summary-CannotTell-3)	|	[Previous CannotTell outcome](#cannottell-outcome-number-2)	|	[Next CannotTell outcome](#cannottell-outcome-number-4)

:warning:CannotTell outcome
#### Subject detail
|Name|usecase-manufacturing-dataset-v1|
|----|----|
|Title|Standalone&#32;use&#32;case&#32;use-cases/manufacturing/dataset-v1.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Use case manufacturing/dataset-v1](https://github.com/HyperAgents/hmas/blob/HEAD/use-cases/manufacturing/dataset-v1.ttl)|

#### Criterion detail
|Identifier|[namespace-validity](https://ns.inria.fr/olivaw#namespace-validity)|
|----|----|
|Title|Namespace&#32;validity&#32;test|
|Description|A&#32;test&#32;case&#32;checking&#32;if&#32;all&#32;the&#32;Namespaces&#32;are&#32;not&#32;too&#32;close&#32;from&#32;the&#32;most&#32;used&#32;existing&#32;namespaces&#32;(according&#32;to&#32;prefix&#32;cc)&#32;or&#32;an&#32;ontology&#32;namespace|

#### Outcome Detail
|Jump|Type|:warning:CannotTell|
|----|----|----|
|[Section top](#cannottell-outcome-number-3)|Identifier|`namespace-typo`|
|[Section top](#cannottell-outcome-number-3)|Title|Possible&#32;namespace&#32;typo|
|[Section top](#cannottell-outcome-number-3)|Description|The&#32;following&#32;namespace&#32;seems&#32;suspicious:  &#10; &#32;https://api.interactions.ics.unisg.ch/cherrybot1/&#32;  &#10;Was&#32;it&#32;supposed&#32;to&#32;correspond&#32;to&#32;one&#32;of&#32;these&#32;namespaces?|
|[Section top](#cannottell-outcome-number-3)|Pointer|<pre lang="Turtle"><code>Namespace&#32;usage&#32;in&#32;the&#32;subject&#32;file:</code></pre>|
|[Section top](#cannottell-outcome-number-3)|Pointer|<pre lang="Turtle"><code>&#91;]&#32;hctl:hasTarget&#32; &#60;https://api.interactions.ics.unisg.ch/cherrybot1/tcp> &#32;.  &#10; &#91;]&#32;hctl:hasTarget&#32; &#60;https://api.interactions.ics.unisg.ch/cherrybot1/operator/%7Btoken%7D> &#32;.  &#10; &#91;]&#32;hctl:hasTarget&#32; &#60;https://api.interactions.ics.unisg.ch/cherrybot1/operator> &#32;.  &#10; &#91;]&#32;hctl:hasTarget&#32; &#60;https://api.interactions.ics.unisg.ch/cherrybot1/gripper> &#32;.  &#10; &#91;]&#32;hctl:hasTarget&#32; &#60;https://api.interactions.ics.unisg.ch/cherrybot1/tcp/target> &#32;.  &#10; &#91;]&#32;hctl:hasTarget&#32; &#60;https://api.interactions.ics.unisg.ch/cherrybot1/operator> &#32;.  &#10; &#91;]&#32;hctl:hasTarget&#32; &#60;https://api.interactions.ics.unisg.ch/cherrybot1/initialize> &#32;.  &#10; &#91;]&#32;hctl:hasTarget&#32; &#60;https://api.interactions.ics.unisg.ch/cherrybot1/gripper> &#32;.  &#10; &#91;]&#32;hctl:hasTarget&#32; &#60;https://api.interactions.ics.unisg.ch/cherrybot1/tcp/target> &#32;.</code></pre>|
|[Section top](#cannottell-outcome-number-3)|Pointer|<pre lang="Turtle"><code>Similar&#32;namespace&#32;found&#32;in&#32;file:  &#10;.&#92;use-cases&#92;manufacturing&#92;dataset-v1.ttl&#32;  &#10;Namespace&#32;found:  &#10;https://api.interactions.ics.unisg.ch/cherrybot2/</code></pre>|
|[Section top](#cannottell-outcome-number-3)|Pointer|<pre lang="Turtle"><code>&#91;]&#32;hctl:hasTarget&#32;similar-namespace:initialize&#32;.  &#10; &#91;]&#32;hctl:hasTarget&#32;similar-namespace:gripper&#32;.  &#10; &#91;]&#32;hctl:hasTarget&#32; &#60;https://api.interactions.ics.unisg.ch/cherrybot2/tcp/target> &#32;.  &#10; &#91;]&#32;hctl:hasTarget&#32;similar-namespace:tcp&#32;.  &#10; &#91;]&#32;hctl:hasTarget&#32;similar-namespace:operator&#32;.  &#10; &#91;]&#32;hctl:hasTarget&#32;similar-namespace:gripper&#32;.  &#10; &#91;]&#32;hctl:hasTarget&#32; &#60;https://api.interactions.ics.unisg.ch/cherrybot2/operator/%7Btoken%7D> &#32;.  &#10; &#91;]&#32;hctl:hasTarget&#32; &#60;https://api.interactions.ics.unisg.ch/cherrybot2/tcp/target> &#32;.  &#10; &#91;]&#32;hctl:hasTarget&#32;similar-namespace:operator&#32;.</code></pre>|

***
### CannotTell Outcome number 4

[Jump to summary definition](#summary-CannotTell-4)	|	[Previous CannotTell outcome](#cannottell-outcome-number-3)	|	[Next CannotTell outcome](#cannottell-outcome-number-5)

:warning:CannotTell outcome
#### Subject detail
|Name|usecase-manufacturing-dataset-v1|
|----|----|
|Title|Standalone&#32;use&#32;case&#32;use-cases/manufacturing/dataset-v1.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Use case manufacturing/dataset-v1](https://github.com/HyperAgents/hmas/blob/HEAD/use-cases/manufacturing/dataset-v1.ttl)|

#### Criterion detail
|Identifier|[namespace-validity](https://ns.inria.fr/olivaw#namespace-validity)|
|----|----|
|Title|Namespace&#32;validity&#32;test|
|Description|A&#32;test&#32;case&#32;checking&#32;if&#32;all&#32;the&#32;Namespaces&#32;are&#32;not&#32;too&#32;close&#32;from&#32;the&#32;most&#32;used&#32;existing&#32;namespaces&#32;(according&#32;to&#32;prefix&#32;cc)&#32;or&#32;an&#32;ontology&#32;namespace|

#### Outcome Detail
|Jump|Type|:warning:CannotTell|
|----|----|----|
|[Section top](#cannottell-outcome-number-4)|Identifier|`namespace-typo`|
|[Section top](#cannottell-outcome-number-4)|Title|Possible&#32;namespace&#32;typo|
|[Section top](#cannottell-outcome-number-4)|Description|The&#32;following&#32;namespace&#32;seems&#32;suspicious:  &#10; &#32;https://api.interactions.ics.unisg.ch/cherrybot1/operator/&#32;  &#10;Was&#32;it&#32;supposed&#32;to&#32;correspond&#32;to&#32;one&#32;of&#32;these&#32;namespaces?|
|[Section top](#cannottell-outcome-number-4)|Pointer|<pre lang="Turtle"><code>Namespace&#32;usage&#32;in&#32;the&#32;subject&#32;file:</code></pre>|
|[Section top](#cannottell-outcome-number-4)|Pointer|<pre lang="Turtle"><code>&#91;]&#32;hctl:hasTarget&#32; &#60;https://api.interactions.ics.unisg.ch/cherrybot1/operator/%7Btoken%7D> &#32;.</code></pre>|
|[Section top](#cannottell-outcome-number-4)|Pointer|<pre lang="Turtle"><code>Similar&#32;namespace&#32;found&#32;in&#32;file:  &#10;.&#92;use-cases&#92;manufacturing&#92;dataset-v1.ttl&#32;  &#10;Namespace&#32;found:  &#10;https://api.interactions.ics.unisg.ch/cherrybot2/operator/</code></pre>|
|[Section top](#cannottell-outcome-number-4)|Pointer|<pre lang="Turtle"><code>&#91;]&#32;hctl:hasTarget&#32; &#60;https://api.interactions.ics.unisg.ch/cherrybot2/operator/%7Btoken%7D> &#32;.</code></pre>|

***
### CannotTell Outcome number 5

[Jump to summary definition](#summary-CannotTell-5)	|	[Previous CannotTell outcome](#cannottell-outcome-number-4)	|	[Next CannotTell outcome](#cannottell-outcome-number-6)

:warning:CannotTell outcome
#### Subject detail
|Name|usecase-manufacturing-dataset-v1|
|----|----|
|Title|Standalone&#32;use&#32;case&#32;use-cases/manufacturing/dataset-v1.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Use case manufacturing/dataset-v1](https://github.com/HyperAgents/hmas/blob/HEAD/use-cases/manufacturing/dataset-v1.ttl)|

#### Criterion detail
|Identifier|[namespace-validity](https://ns.inria.fr/olivaw#namespace-validity)|
|----|----|
|Title|Namespace&#32;validity&#32;test|
|Description|A&#32;test&#32;case&#32;checking&#32;if&#32;all&#32;the&#32;Namespaces&#32;are&#32;not&#32;too&#32;close&#32;from&#32;the&#32;most&#32;used&#32;existing&#32;namespaces&#32;(according&#32;to&#32;prefix&#32;cc)&#32;or&#32;an&#32;ontology&#32;namespace|

#### Outcome Detail
|Jump|Type|:warning:CannotTell|
|----|----|----|
|[Section top](#cannottell-outcome-number-5)|Identifier|`namespace-typo`|
|[Section top](#cannottell-outcome-number-5)|Title|Possible&#32;namespace&#32;typo|
|[Section top](#cannottell-outcome-number-5)|Description|The&#32;following&#32;namespace&#32;seems&#32;suspicious:  &#10; &#32;https://api.interactions.ics.unisg.ch/cherrybot1/tcp/&#32;  &#10;Was&#32;it&#32;supposed&#32;to&#32;correspond&#32;to&#32;one&#32;of&#32;these&#32;namespaces?|
|[Section top](#cannottell-outcome-number-5)|Pointer|<pre lang="Turtle"><code>Namespace&#32;usage&#32;in&#32;the&#32;subject&#32;file:</code></pre>|
|[Section top](#cannottell-outcome-number-5)|Pointer|<pre lang="Turtle"><code>&#91;]&#32;hctl:hasTarget&#32; &#60;https://api.interactions.ics.unisg.ch/cherrybot1/tcp/target> &#32;.  &#10; &#91;]&#32;hctl:hasTarget&#32; &#60;https://api.interactions.ics.unisg.ch/cherrybot1/tcp/target> &#32;.</code></pre>|
|[Section top](#cannottell-outcome-number-5)|Pointer|<pre lang="Turtle"><code>Similar&#32;namespace&#32;found&#32;in&#32;file:  &#10;.&#92;use-cases&#92;manufacturing&#92;dataset-v1.ttl&#32;  &#10;Namespace&#32;found:  &#10;https://api.interactions.ics.unisg.ch/cherrybot2/tcp/</code></pre>|
|[Section top](#cannottell-outcome-number-5)|Pointer|<pre lang="Turtle"><code>&#91;]&#32;hctl:hasTarget&#32;similar-namespace:target&#32;.  &#10; &#91;]&#32;hctl:hasTarget&#32;similar-namespace:target&#32;.</code></pre>|

***
### CannotTell Outcome number 6

[Jump to summary definition](#summary-CannotTell-6)	|	[Previous CannotTell outcome](#cannottell-outcome-number-5)	|	[Next CannotTell outcome](#cannottell-outcome-number-7)

:warning:CannotTell outcome
#### Subject detail
|Name|usecase-manufacturing-dataset-v1|
|----|----|
|Title|Standalone&#32;use&#32;case&#32;use-cases/manufacturing/dataset-v1.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Use case manufacturing/dataset-v1](https://github.com/HyperAgents/hmas/blob/HEAD/use-cases/manufacturing/dataset-v1.ttl)|

#### Criterion detail
|Identifier|[namespace-validity](https://ns.inria.fr/olivaw#namespace-validity)|
|----|----|
|Title|Namespace&#32;validity&#32;test|
|Description|A&#32;test&#32;case&#32;checking&#32;if&#32;all&#32;the&#32;Namespaces&#32;are&#32;not&#32;too&#32;close&#32;from&#32;the&#32;most&#32;used&#32;existing&#32;namespaces&#32;(according&#32;to&#32;prefix&#32;cc)&#32;or&#32;an&#32;ontology&#32;namespace|

#### Outcome Detail
|Jump|Type|:warning:CannotTell|
|----|----|----|
|[Section top](#cannottell-outcome-number-6)|Identifier|`namespace-typo`|
|[Section top](#cannottell-outcome-number-6)|Title|Possible&#32;namespace&#32;typo|
|[Section top](#cannottell-outcome-number-6)|Description|The&#32;following&#32;namespace&#32;seems&#32;suspicious:  &#10; &#32;https://ns.inria.fr/hmas/&#32;  &#10;Was&#32;it&#32;supposed&#32;to&#32;correspond&#32;to&#32;one&#32;of&#32;these&#32;namespaces?|
|[Section top](#cannottell-outcome-number-6)|Pointer|<pre lang="Turtle"><code>Namespace&#32;usage&#32;in&#32;the&#32;subject&#32;file:</code></pre>|
|[Section top](#cannottell-outcome-number-6)|Pointer|<pre lang="Turtle"><code>&#60;https://ns.inria.fr/hmas/#platform> &#32;a&#32;hmas:Platform&#32;;  &#10; &#32; &#32; &#32; &#32;hmas:hasProfile&#32; &#60;https://ns.inria.fr/hmas/> &#32;.  &#10;ns2:workspace&#32;a&#32;hmas:Workspace&#32;;  &#10; &#32; &#32; &#32; &#32;ns2:hasProfile&#32;ns2:&#32;;  &#10; &#32; &#32; &#32; &#32;hmas:contains&#32; &#60;https://ns.inria.fr/hmas/workspaces/cup-production-site/artifacts/robotic-arm-1#artifact>,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#60;https://ns.inria.fr/hmas/workspaces/cup-production-site/artifacts/robotic-arm-2#artifact>,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#60;https://ns.inria.fr/hmas/workspaces/cup-production-site/artifacts/truck#artifact> &#32;;  &#10; &#32; &#32; &#32; &#32;hmas:isHostedOn&#32; &#60;https://ns.inria.fr/hmas/#platformplatform> &#32;.  &#10; &#60;https://ns.inria.fr/hmas/workspaces/cup-production-site/agents/agent-b#agent> &#32;a&#32;hmas:Agent&#32;;  &#10; &#32; &#32; &#32; &#32;hmas:hasProfile&#32; &#60;https://ns.inria.fr/hmas/workspaces/cup-production-site/agents/agent-b#> &#32;;  &#10; &#32; &#32; &#32; &#32;hmas:isContainedIn&#32;ns2:Workspace&#32;;  &#10; &#32; &#32; &#32; &#32;hmas:isHostedOn&#32; &#60;https://ns.inria.fr/hmas/#platformplatform> &#32;.  &#10; &#60;https://ns.inria.fr/hmas/workspaces/cup-production-site/agents/agent-c#agent> &#32;a&#32;hmas:Agent&#32;;  &#10; &#32; &#32; &#32; &#32;hmas:hasProfile&#32; &#60;https://ns.inria.fr/hmas/workspaces/cup-production-site/agents/agent-c#> &#32;;  &#10; &#32; &#32; &#32; &#32;hmas:isContainedIn&#32;ns2:Workspace&#32;;  &#10; &#32; &#32; &#32; &#32;hmas:isHostedOn&#32; &#60;https://ns.inria.fr/hmas/#platformplatform> &#32;.  &#10; &#60;https://ns.inria.fr/hmas/workspaces/cup-production-site/agents/agent-d#agent> &#32;a&#32;hmas:Agent&#32;;  &#10; &#32; &#32; &#32; &#32;hmas:hasProfile&#32; &#60;https://ns.inria.fr/hmas/workspaces/cup-production-site/agents/agent-d#> &#32;;  &#10; &#32; &#32; &#32; &#32;hmas:isContainedIn&#32;ns2:Workspace&#32;;  &#10; &#32; &#32; &#32; &#32;hmas:isHostedOn&#32; &#60;https://ns.inria.fr/hmas/#platformplatform> &#32;.  &#10; &#60;https://ns.inria.fr/hmas/workspaces/cup-production-site/artifacts/robotic-arm-1#> &#32;a&#32;hmas:ResourceProfile&#32;;  &#10; &#32; &#32; &#32; &#32;hmas:exposesSignifier&#32; &#91;&#32;],  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#91;&#32;],  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#91;&#32;],  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#91;&#32;],  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#91;&#32;],  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#91;&#32;],  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#91;&#32;],  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#91;&#32;],  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#91;&#32;]&#32;;  &#10; &#32; &#32; &#32; &#32;hmas:isProfileOf&#32; &#60;https://ns.inria.fr/hmas/workspaces/cup-production-site/artifacts/robotic-arm-1#artifact> &#32;.  &#10; &#60;https://ns.inria.fr/hmas/workspaces/cup-production-site/artifacts/robotic-arm-2#> &#32;a&#32;hmas:ResourceProfile&#32;;  &#10; &#32; &#32; &#32; &#32;hmas:exposesSignifier&#32; &#91;&#32;],  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#91;&#32;],  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#91;&#32;],  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#91;&#32;],  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#91;&#32;],  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#91;&#32;],  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#91;&#32;],  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#91;&#32;],  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#91;&#32;]&#32;;  &#10; &#32; &#32; &#32; &#32;hmas:isProfileOf&#32; &#60;https://ns.inria.fr/hmas/workspaces/cup-production-site/artifacts/robotic-arm-2#artifact> &#32;.  &#10; &#60;https://ns.inria.fr/hmas/workspaces/cup-production-site/artifacts/truck#> &#32;a&#32;hmas:ResourceProfile&#32;;  &#10; &#32; &#32; &#32; &#32;hmas:exposesSignifier&#32; &#91;&#32;],  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#91;&#32;],  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#91;&#32;]&#32;;  &#10; &#32; &#32; &#32; &#32;hmas:isProfileOf&#32; &#60;https://ns.inria.fr/hmas/workspaces/cup-production-site/artifacts/truck#artifact> &#32;.  &#10; &#60;https://ns.inria.fr/hmas/workspaces/cup-production-site/artifacts/robotic-arm-1#artifact> &#32;a&#32;hmas:Artifact&#32;;  &#10; &#32; &#32; &#32; &#32;hmas:isHostedOn&#32; &#60;https://ns.inria.fr/hmas/#platformplatform> &#32;.  &#10; &#60;https://ns.inria.fr/hmas/workspaces/cup-production-site/artifacts/robotic-arm-2#artifact> &#32;a&#32;hmas:Artifact&#32;;  &#10; &#32; &#32; &#32; &#32;hmas:isHostedOn&#32; &#60;https://ns.inria.fr/hmas/#platformplatform> &#32;.  &#10; &#60;https://ns.inria.fr/hmas/workspaces/cup-production-site/artifacts/truck#artifact> &#32;a&#32;hmas:Artifact&#32;;  &#10; &#32; &#32; &#32; &#32;hmas:isHostedOn&#32; &#60;https://ns.inria.fr/hmas/#platformplatform> &#32;.</code></pre>|
|[Section top](#cannottell-outcome-number-6)|Pointer|<pre lang="Turtle"><code>Similar&#32;namespace&#32;found&#32;in&#32;file:  &#10;.&#92;use-cases&#92;manufacturing&#92;dataset-v1.ttl&#32;  &#10;Namespace&#32;found:  &#10;https://ns.inria.fr/hmas/#</code></pre>|
|[Section top](#cannottell-outcome-number-6)|Pointer|<pre lang="Turtle"><code>similar-namespace:platform&#32;a&#32;hmas:Platform&#32;;  &#10; &#32; &#32;&#32; &#32;hmas:hasProfile&#32; &#60;https://ns.inria.fr/hmas/> &#32;.  &#10; &#60;https://ns.inria.fr/hmas/workspaces/cup-production-site#workspace> &#32;hmas:isHostedOn&#32;similar-namespace:platformplatform&#32;.  &#10; &#60;https://ns.inria.fr/hmas/workspaces/cup-production-site/agents/agent-b#agent> &#32;hmas:isHostedOn&#32;similar-namespace:platformplatform&#32;.  &#10; &#60;https://ns.inria.fr/hmas/workspaces/cup-production-site/agents/agent-c#agent> &#32;hmas:isHostedOn&#32;similar-namespace:platformplatform&#32;.  &#10; &#60;https://ns.inria.fr/hmas/workspaces/cup-production-site/agents/agent-d#agent> &#32;hmas:isHostedOn&#32;similar-namespace:platformplatform&#32;.  &#10; &#60;https://ns.inria.fr/hmas/workspaces/cup-production-site/artifacts/robotic-arm-1#artifact> &#32;hmas:isHostedOn&#32;similar-namespace:platformplatform&#32;.  &#10; &#60;https://ns.inria.fr/hmas/workspaces/cup-production-site/artifacts/robotic-arm-2#artifact> &#32;hmas:isHostedOn&#32;similar-namespace:platformplatform&#32;.  &#10; &#60;https://ns.inria.fr/hmas/workspaces/cup-production-site/artifacts/truck#artifact> &#32;hmas:isHostedOn&#32;similar-namespace:platformplatform&#32;.</code></pre>|

***
### CannotTell Outcome number 7

[Jump to summary definition](#summary-CannotTell-7)	|	[Previous CannotTell outcome](#cannottell-outcome-number-6)	|	[Next CannotTell outcome](#cannottell-outcome-number-8)

:warning:CannotTell outcome
#### Subject detail
|Name|usecase-manufacturing-dataset-v1|
|----|----|
|Title|Standalone&#32;use&#32;case&#32;use-cases/manufacturing/dataset-v1.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Use case manufacturing/dataset-v1](https://github.com/HyperAgents/hmas/blob/HEAD/use-cases/manufacturing/dataset-v1.ttl)|

#### Criterion detail
|Identifier|[namespace-validity](https://ns.inria.fr/olivaw#namespace-validity)|
|----|----|
|Title|Namespace&#32;validity&#32;test|
|Description|A&#32;test&#32;case&#32;checking&#32;if&#32;all&#32;the&#32;Namespaces&#32;are&#32;not&#32;too&#32;close&#32;from&#32;the&#32;most&#32;used&#32;existing&#32;namespaces&#32;(according&#32;to&#32;prefix&#32;cc)&#32;or&#32;an&#32;ontology&#32;namespace|

#### Outcome Detail
|Jump|Type|:warning:CannotTell|
|----|----|----|
|[Section top](#cannottell-outcome-number-7)|Identifier|`namespace-typo`|
|[Section top](#cannottell-outcome-number-7)|Title|Possible&#32;namespace&#32;typo|
|[Section top](#cannottell-outcome-number-7)|Description|The&#32;following&#32;namespace&#32;seems&#32;suspicious:  &#10; &#32;https://ns.inria.fr/hmas/workspaces/cup-production-site/agents/agent-b#&#32;  &#10;Was&#32;it&#32;supposed&#32;to&#32;correspond&#32;to&#32;one&#32;of&#32;these&#32;namespaces?|
|[Section top](#cannottell-outcome-number-7)|Pointer|<pre lang="Turtle"><code>Namespace&#32;usage&#32;in&#32;the&#32;subject&#32;file:</code></pre>|
|[Section top](#cannottell-outcome-number-7)|Pointer|<pre lang="Turtle"><code>&#60;https://ns.inria.fr/hmas/workspaces/cup-production-site/agents/agent-b#agent> &#32;a&#32;hmas:Agent&#32;;  &#10; &#32; &#32; &#32; &#32;hmas:hasProfile&#32; &#60;https://ns.inria.fr/hmas/workspaces/cup-production-site/agents/agent-b#> &#32;;  &#10; &#32; &#32; &#32; &#32;hmas:isContainedIn&#32; &#60;https://ns.inria.fr/hmas/workspaces/cup-production-site#Workspace> &#32;;  &#10; &#32; &#32; &#32; &#32;hmas:isHostedOn&#32; &#60;https://ns.inria.fr/hmas/#platformplatform> &#32;.</code></pre>|
|[Section top](#cannottell-outcome-number-7)|Pointer|<pre lang="Turtle"><code>Similar&#32;namespace&#32;found&#32;in&#32;file:  &#10;.&#92;use-cases&#92;manufacturing&#92;dataset-v1.ttl&#32;  &#10;Namespace&#32;found:  &#10;https://ns.inria.fr/hmas/workspaces/cup-production-site/agents/agent-c#</code></pre>|
|[Section top](#cannottell-outcome-number-7)|Pointer|<pre lang="Turtle"><code>similar-namespace:agent&#32;a&#32;hmas:Agent&#32;;  &#10; &#32; &#32; &#32; &#32;hmas:hasProfile&#32;similar-namespace:&#32;;  &#10; &#32; &#32; &#32; &#32;hmas:isContainedIn&#32; &#60;https://ns.inria.fr/hmas/workspaces/cup-production-site#Workspace> &#32;;  &#10; &#32; &#32; &#32; &#32;hmas:isHostedOn&#32; &#60;https://ns.inria.fr/hmas/#platformplatform> &#32;.</code></pre>|
|[Section top](#cannottell-outcome-number-7)|Pointer|<pre lang="Turtle"><code>Similar&#32;namespace&#32;found&#32;in&#32;file:  &#10;.&#92;use-cases&#92;manufacturing&#92;dataset-v1.ttl&#32;  &#10;Namespace&#32;found:  &#10;https://ns.inria.fr/hmas/workspaces/cup-production-site/agents/agent-d#</code></pre>|

***
### CannotTell Outcome number 8

[Jump to summary definition](#summary-CannotTell-8)	|	[Previous CannotTell outcome](#cannottell-outcome-number-7)	|	[Next CannotTell outcome](#cannottell-outcome-number-9)

:warning:CannotTell outcome
#### Subject detail
|Name|usecase-manufacturing-dataset-v1|
|----|----|
|Title|Standalone&#32;use&#32;case&#32;use-cases/manufacturing/dataset-v1.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Use case manufacturing/dataset-v1](https://github.com/HyperAgents/hmas/blob/HEAD/use-cases/manufacturing/dataset-v1.ttl)|

#### Criterion detail
|Identifier|[namespace-validity](https://ns.inria.fr/olivaw#namespace-validity)|
|----|----|
|Title|Namespace&#32;validity&#32;test|
|Description|A&#32;test&#32;case&#32;checking&#32;if&#32;all&#32;the&#32;Namespaces&#32;are&#32;not&#32;too&#32;close&#32;from&#32;the&#32;most&#32;used&#32;existing&#32;namespaces&#32;(according&#32;to&#32;prefix&#32;cc)&#32;or&#32;an&#32;ontology&#32;namespace|

#### Outcome Detail
|Jump|Type|:warning:CannotTell|
|----|----|----|
|[Section top](#cannottell-outcome-number-8)|Identifier|`namespace-typo`|
|[Section top](#cannottell-outcome-number-8)|Title|Possible&#32;namespace&#32;typo|
|[Section top](#cannottell-outcome-number-8)|Description|The&#32;following&#32;namespace&#32;seems&#32;suspicious:  &#10; &#32;https://ns.inria.fr/hmas/workspaces/cup-production-site/agents/agent-c#&#32;  &#10;Was&#32;it&#32;supposed&#32;to&#32;correspond&#32;to&#32;one&#32;of&#32;these&#32;namespaces?|
|[Section top](#cannottell-outcome-number-8)|Pointer|<pre lang="Turtle"><code>Namespace&#32;usage&#32;in&#32;the&#32;subject&#32;file:</code></pre>|
|[Section top](#cannottell-outcome-number-8)|Pointer|<pre lang="Turtle"><code>&#60;https://ns.inria.fr/hmas/workspaces/cup-production-site/agents/agent-c#agent> &#32;a&#32;hmas:Agent&#32;;  &#10; &#32; &#32; &#32; &#32;hmas:hasProfile&#32; &#60;https://ns.inria.fr/hmas/workspaces/cup-production-site/agents/agent-c#> &#32;;  &#10; &#32; &#32; &#32; &#32;hmas:isContainedIn&#32; &#60;https://ns.inria.fr/hmas/workspaces/cup-production-site#Workspace> &#32;;  &#10; &#32; &#32; &#32; &#32;hmas:isHostedOn&#32; &#60;https://ns.inria.fr/hmas/#platformplatform> &#32;.</code></pre>|
|[Section top](#cannottell-outcome-number-8)|Pointer|<pre lang="Turtle"><code>Similar&#32;namespace&#32;found&#32;in&#32;file:  &#10;.&#92;use-cases&#92;manufacturing&#92;dataset-v1.ttl&#32;  &#10;Namespace&#32;found:  &#10;https://ns.inria.fr/hmas/workspaces/cup-production-site/agents/agent-d#</code></pre>|
|[Section top](#cannottell-outcome-number-8)|Pointer|<pre lang="Turtle"><code>similar-namespace:agent&#32;a&#32;hmas:Agent&#32;;  &#10; &#32; &#32; &#32; &#32;hmas:hasProfile&#32;similar-namespace:&#32;;  &#10; &#32; &#32; &#32; &#32;hmas:isContainedIn&#32; &#60;https://ns.inria.fr/hmas/workspaces/cup-production-site#Workspace> &#32;;  &#10; &#32; &#32; &#32; &#32;hmas:isHostedOn&#32; &#60;https://ns.inria.fr/hmas/#platformplatform> &#32;.</code></pre>|

***
### CannotTell Outcome number 9

[Jump to summary definition](#summary-CannotTell-9)	|	[Previous CannotTell outcome](#cannottell-outcome-number-8)	|	[Next CannotTell outcome](#cannottell-outcome-number-10)

:warning:CannotTell outcome
#### Subject detail
|Name|usecase-manufacturing-dataset-v1|
|----|----|
|Title|Standalone&#32;use&#32;case&#32;use-cases/manufacturing/dataset-v1.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Use case manufacturing/dataset-v1](https://github.com/HyperAgents/hmas/blob/HEAD/use-cases/manufacturing/dataset-v1.ttl)|

#### Criterion detail
|Identifier|[namespace-validity](https://ns.inria.fr/olivaw#namespace-validity)|
|----|----|
|Title|Namespace&#32;validity&#32;test|
|Description|A&#32;test&#32;case&#32;checking&#32;if&#32;all&#32;the&#32;Namespaces&#32;are&#32;not&#32;too&#32;close&#32;from&#32;the&#32;most&#32;used&#32;existing&#32;namespaces&#32;(according&#32;to&#32;prefix&#32;cc)&#32;or&#32;an&#32;ontology&#32;namespace|

#### Outcome Detail
|Jump|Type|:warning:CannotTell|
|----|----|----|
|[Section top](#cannottell-outcome-number-9)|Identifier|`namespace-typo`|
|[Section top](#cannottell-outcome-number-9)|Title|Possible&#32;namespace&#32;typo|
|[Section top](#cannottell-outcome-number-9)|Description|The&#32;following&#32;namespace&#32;seems&#32;suspicious:  &#10; &#32;https://ns.inria.fr/hmas/workspaces/cup-production-site/artifacts/robotic-arm-1#&#32;  &#10;Was&#32;it&#32;supposed&#32;to&#32;correspond&#32;to&#32;one&#32;of&#32;these&#32;namespaces?|
|[Section top](#cannottell-outcome-number-9)|Pointer|<pre lang="Turtle"><code>Namespace&#32;usage&#32;in&#32;the&#32;subject&#32;file:</code></pre>|
|[Section top](#cannottell-outcome-number-9)|Pointer|<pre lang="Turtle"><code>&#60;https://ns.inria.fr/hmas/workspaces/cup-production-site#workspace> &#32;hmas:contains&#32; &#60;https://ns.inria.fr/hmas/workspaces/cup-production-site/artifacts/robotic-arm-1#artifact> &#32;.  &#10; &#60;https://ns.inria.fr/hmas/workspaces/cup-production-site/artifacts/robotic-arm-1#> &#32;a&#32;hmas:ResourceProfile&#32;;  &#10; &#32; &#32; &#32; &#32;hmas:exposesSignifier&#32; &#91;&#32;],  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#91;&#32;],  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#91;&#32;],  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#91;&#32;],  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#91;&#32;],  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#91;&#32;],  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#91;&#32;],  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#91;&#32;],  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#91;&#32;]&#32;;  &#10; &#32; &#32; &#32; &#32;hmas:isProfileOf&#32; &#60;https://ns.inria.fr/hmas/workspaces/cup-production-site/artifacts/robotic-arm-1#artifact> &#32;.  &#10; &#60;https://ns.inria.fr/hmas/workspaces/cup-production-site/artifacts/robotic-arm-1#artifact> &#32;a&#32;hmas:Artifact&#32;;  &#10; &#32; &#32; &#32; &#32;hmas:isHostedOn&#32; &#60;https://ns.inria.fr/hmas/#platformplatform> &#32;.</code></pre>|
|[Section top](#cannottell-outcome-number-9)|Pointer|<pre lang="Turtle"><code>Similar&#32;namespace&#32;found&#32;in&#32;file:  &#10;.&#92;use-cases&#92;manufacturing&#92;dataset-v1.ttl&#32;  &#10;Namespace&#32;found:  &#10;https://ns.inria.fr/hmas/workspaces/cup-production-site/artifacts/robotic-arm-2#</code></pre>|
|[Section top](#cannottell-outcome-number-9)|Pointer|<pre lang="Turtle"><code>&#60;https://ns.inria.fr/hmas/workspaces/cup-production-site#workspace> &#32;hmas:contains&#32;similar-namespace:artifact&#32;.  &#10;similar-namespace:&#32;a&#32;hmas:ResourceProfile&#32;;  &#10; &#32; &#32; &#32; &#32;hmas:exposesSignifier&#32; &#91;&#32;],  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#91;&#32;],  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#91;&#32;],  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#91;&#32;],  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#91;&#32;],  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#91;&#32;],  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#91;&#32;],  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#91;&#32;],  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#91;&#32;]&#32;;  &#10; &#32; &#32; &#32; &#32;hmas:isProfileOf&#32;similar-namespace:artifact&#32;.  &#10;similar-namespace:artifact&#32;a&#32;hmas:Artifact&#32;;  &#10; &#32; &#32; &#32; &#32;hmas:isHostedOn&#32; &#60;https://ns.inria.fr/hmas/#platformplatform> &#32;.</code></pre>|

***
### CannotTell Outcome number 10

[Jump to summary definition](#summary-CannotTell-10)	|	[Previous CannotTell outcome](#cannottell-outcome-number-9)	|	[Next CannotTell outcome](#cannottell-outcome-number-11)

:warning:CannotTell outcome
#### Subject detail
|Name|usecase-manufacturing-dataset-v1|
|----|----|
|Title|Standalone&#32;use&#32;case&#32;use-cases/manufacturing/dataset-v1.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Use case manufacturing/dataset-v1](https://github.com/HyperAgents/hmas/blob/HEAD/use-cases/manufacturing/dataset-v1.ttl)|

#### Criterion detail
|Identifier|[namespace-validity](https://ns.inria.fr/olivaw#namespace-validity)|
|----|----|
|Title|Namespace&#32;validity&#32;test|
|Description|A&#32;test&#32;case&#32;checking&#32;if&#32;all&#32;the&#32;Namespaces&#32;are&#32;not&#32;too&#32;close&#32;from&#32;the&#32;most&#32;used&#32;existing&#32;namespaces&#32;(according&#32;to&#32;prefix&#32;cc)&#32;or&#32;an&#32;ontology&#32;namespace|

#### Outcome Detail
|Jump|Type|:warning:CannotTell|
|----|----|----|
|[Section top](#cannottell-outcome-number-10)|Identifier|`namespace-typo`|
|[Section top](#cannottell-outcome-number-10)|Title|Possible&#32;namespace&#32;typo|
|[Section top](#cannottell-outcome-number-10)|Description|The&#32;following&#32;namespace&#32;seems&#32;suspicious:  &#10; &#32;https://www.example.org/&#32;  &#10;Was&#32;it&#32;supposed&#32;to&#32;correspond&#32;to&#32;one&#32;of&#32;these&#32;namespaces?|
|[Section top](#cannottell-outcome-number-10)|Pointer|<pre lang="Turtle"><code>Namespace&#32;usage&#32;in&#32;the&#32;subject&#32;file:</code></pre>|
|[Section top](#cannottell-outcome-number-10)|Pointer|<pre lang="Turtle"><code>&#60;https://www.example.org/canBeFriendwithShape> &#32;a&#32;sh:NodeShape&#32;;  &#10; &#32; &#32; &#32; &#32;sh:sparql&#32; &#91;&#32;sh:prefixes&#32; &#60;https://www.example.org/> &#32;]&#32;;  &#10; &#32; &#32; &#32; &#32;sh:targetNode&#32;hmas:Membership&#32;.</code></pre>|
|[Section top](#cannottell-outcome-number-10)|Pointer|<pre lang="Turtle"><code>Common&#32;namespace&#32;found&#32;  &#10;@prefix&#32;eg:&#32; &#60;http://www.example.org/> &#32;.</code></pre>|

***
### CannotTell Outcome number 11

[Jump to summary definition](#summary-CannotTell-11)	|	[Previous CannotTell outcome](#cannottell-outcome-number-10)	|	[Next CannotTell outcome](#cannottell-outcome-number-12)

:warning:CannotTell outcome
#### Subject detail
|Name|dataset-manufacturing-environments-discover-behavior-specifications|
|----|----|
|Title|Standalone&#32;dataset&#32;domains/manufacturing-environments/discover-behavior-specifications/dataset.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Dataset manufacturing-environments/discover-behavior-specifications](https://github.com/HyperAgents/hmas/blob/HEAD/domains/manufacturing-environments/discover-behavior-specifications/dataset.ttl)|

#### Criterion detail
|Identifier|[namespace-validity](https://ns.inria.fr/olivaw#namespace-validity)|
|----|----|
|Title|Namespace&#32;validity&#32;test|
|Description|A&#32;test&#32;case&#32;checking&#32;if&#32;all&#32;the&#32;Namespaces&#32;are&#32;not&#32;too&#32;close&#32;from&#32;the&#32;most&#32;used&#32;existing&#32;namespaces&#32;(according&#32;to&#32;prefix&#32;cc)&#32;or&#32;an&#32;ontology&#32;namespace|

#### Outcome Detail
|Jump|Type|:warning:CannotTell|
|----|----|----|
|[Section top](#cannottell-outcome-number-11)|Identifier|`namespace-typo`|
|[Section top](#cannottell-outcome-number-11)|Title|Possible&#32;namespace&#32;typo|
|[Section top](#cannottell-outcome-number-11)|Description|The&#32;following&#32;namespace&#32;seems&#32;suspicious:  &#10; &#32;http://www.w3.org/2011/http#&#32;  &#10;Was&#32;it&#32;supposed&#32;to&#32;correspond&#32;to&#32;one&#32;of&#32;these&#32;namespaces?|
|[Section top](#cannottell-outcome-number-11)|Pointer|<pre lang="Turtle"><code>Namespace&#32;usage&#32;in&#32;the&#32;subject&#32;file:</code></pre>|
|[Section top](#cannottell-outcome-number-11)|Pointer|<pre lang="Turtle"><code>&#60;http://example.org/coapForm> &#32;htv:methodName&#32; &#34;PUT&#34; &#32;.  &#10; &#60;http://example.org/httpForm> &#32;htv:methodName&#32; &#34;PUT&#34; &#32;.</code></pre>|
|[Section top](#cannottell-outcome-number-11)|Pointer|<pre lang="Turtle"><code>Common&#32;namespace&#32;found&#32;  &#10;@prefix&#32;httpvoc:&#32; &#60;http://www.w3.org/2006/http#> &#32;.</code></pre>|

***
### CannotTell Outcome number 12

[Jump to summary definition](#summary-CannotTell-12)	|	[Previous CannotTell outcome](#cannottell-outcome-number-11)	|	Next CannotTell outcome

:warning:CannotTell outcome
#### Subject detail
|Name|dataset-manufacturing-environments-discover-behavior-specifications|
|----|----|
|Title|Standalone&#32;dataset&#32;domains/manufacturing-environments/discover-behavior-specifications/dataset.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Dataset manufacturing-environments/discover-behavior-specifications](https://github.com/HyperAgents/hmas/blob/HEAD/domains/manufacturing-environments/discover-behavior-specifications/dataset.ttl)|

#### Criterion detail
|Identifier|[namespace-validity](https://ns.inria.fr/olivaw#namespace-validity)|
|----|----|
|Title|Namespace&#32;validity&#32;test|
|Description|A&#32;test&#32;case&#32;checking&#32;if&#32;all&#32;the&#32;Namespaces&#32;are&#32;not&#32;too&#32;close&#32;from&#32;the&#32;most&#32;used&#32;existing&#32;namespaces&#32;(according&#32;to&#32;prefix&#32;cc)&#32;or&#32;an&#32;ontology&#32;namespace|

#### Outcome Detail
|Jump|Type|:warning:CannotTell|
|----|----|----|
|[Section top](#cannottell-outcome-number-12)|Identifier|`namespace-typo`|
|[Section top](#cannottell-outcome-number-12)|Title|Possible&#32;namespace&#32;typo|
|[Section top](#cannottell-outcome-number-12)|Description|The&#32;following&#32;namespace&#32;seems&#32;suspicious:  &#10; &#32;https://www.w3.org/2001/XMLSchema#&#32;  &#10;Was&#32;it&#32;supposed&#32;to&#32;correspond&#32;to&#32;one&#32;of&#32;these&#32;namespaces?|
|[Section top](#cannottell-outcome-number-12)|Pointer|<pre lang="Turtle"><code>Namespace&#32;usage&#32;in&#32;the&#32;subject&#32;file:</code></pre>|
|[Section top](#cannottell-outcome-number-12)|Pointer|<pre lang="Turtle"><code>&#91;]&#32;sh:datatype&#32; &#60;https://www.w3.org/2001/XMLSchema#integer> &#32;.</code></pre>|
|[Section top](#cannottell-outcome-number-12)|Pointer|<pre lang="Turtle"><code>Common&#32;namespace&#32;found&#32;  &#10;@prefix&#32;xsd:&#32; &#60;http://www.w3.org/2001/XMLSchema#> &#32;.</code></pre>|

***

</details>

***


# Pass Outcomes

[Jump to statistic summary](#statistic-summary)	|	[Previous section](#cannottell-outcomes)	|	Next section

Here is the chapter related to the Pass outcome

:white_check_mark:40 Pass outcomes

<details>
<summary>Fold/Unfold the 40 summary and details</summary>

## Pass Outcomes Summary

:white_check_mark:40 Pass outcomes

|*Jump*|*Number*|*Status*|*Subject*|*Criterion*|*Title*|*Link*|
|------|--------|--------|---------|-----------|-------|------|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-1">1/40</div>|:white_check_mark:Pass|`usecase-manufacturing-dataset-v1`|[owl-rl-constraint](https://ns.inria.fr/olivaw#owl-rl-constraint)|OWL RL consistent|[Jump](#pass-outcome-number-1)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-2">2/40</div>|:white_check_mark:Pass|`usecase-manufacturing-dataset-v1`|[syntax](https://ns.inria.fr/olivaw#syntax)|Correct syntax|[Jump](#pass-outcome-number-2)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-3">3/40</div>|:white_check_mark:Pass|`dataset-manufacturing-environments-discover-signifiers`|[namespace-validity](https://ns.inria.fr/olivaw#namespace-validity)|No namespace typo|[Jump](#pass-outcome-number-3)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-4">4/40</div>|:white_check_mark:Pass|`dataset-manufacturing-environments-discover-signifiers`|[owl-rl-constraint](https://ns.inria.fr/olivaw#owl-rl-constraint)|OWL RL consistent|[Jump](#pass-outcome-number-4)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-5">5/40</div>|:white_check_mark:Pass|`dataset-manufacturing-environments-discover-signifiers`|[syntax](https://ns.inria.fr/olivaw#syntax)|Correct syntax|[Jump](#pass-outcome-number-5)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-6">6/40</div>|:white_check_mark:Pass|`dataset-manufacturing-environments-discover-signifiers`|[term-recognition](https://ns.inria.fr/olivaw#term-recognition)|Every term exists|[Jump](#pass-outcome-number-6)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-7">7/40</div>|:white_check_mark:Pass|`dataset-manufacturing-environments-discover-platforms`|[namespace-validity](https://ns.inria.fr/olivaw#namespace-validity)|No namespace typo|[Jump](#pass-outcome-number-7)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-8">8/40</div>|:white_check_mark:Pass|`dataset-manufacturing-environments-discover-platforms`|[owl-rl-constraint](https://ns.inria.fr/olivaw#owl-rl-constraint)|OWL RL consistent|[Jump](#pass-outcome-number-8)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-9">9/40</div>|:white_check_mark:Pass|`dataset-manufacturing-environments-discover-platforms`|[syntax](https://ns.inria.fr/olivaw#syntax)|Correct syntax|[Jump](#pass-outcome-number-9)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-10">10/40</div>|:white_check_mark:Pass|`dataset-manufacturing-environments-discover-organization`|[namespace-validity](https://ns.inria.fr/olivaw#namespace-validity)|No namespace typo|[Jump](#pass-outcome-number-10)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-11">11/40</div>|:white_check_mark:Pass|`dataset-manufacturing-environments-discover-organization`|[owl-rl-constraint](https://ns.inria.fr/olivaw#owl-rl-constraint)|OWL RL consistent|[Jump](#pass-outcome-number-11)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-12">12/40</div>|:white_check_mark:Pass|`dataset-manufacturing-environments-discover-organization`|[syntax](https://ns.inria.fr/olivaw#syntax)|Correct syntax|[Jump](#pass-outcome-number-12)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-13">13/40</div>|:white_check_mark:Pass|`dataset-manufacturing-environments-discover-organization`|[term-recognition](https://ns.inria.fr/olivaw#term-recognition)|Every term exists|[Jump](#pass-outcome-number-13)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-14">14/40</div>|:white_check_mark:Pass|`dataset-manufacturing-environments-discover-core`|[namespace-validity](https://ns.inria.fr/olivaw#namespace-validity)|No namespace typo|[Jump](#pass-outcome-number-14)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-15">15/40</div>|:white_check_mark:Pass|`dataset-manufacturing-environments-discover-core`|[owl-rl-constraint](https://ns.inria.fr/olivaw#owl-rl-constraint)|OWL RL consistent|[Jump](#pass-outcome-number-15)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-16">16/40</div>|:white_check_mark:Pass|`dataset-manufacturing-environments-discover-core`|[syntax](https://ns.inria.fr/olivaw#syntax)|Correct syntax|[Jump](#pass-outcome-number-16)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-17">17/40</div>|:white_check_mark:Pass|`dataset-manufacturing-environments-discover-core`|[term-recognition](https://ns.inria.fr/olivaw#term-recognition)|Every term exists|[Jump](#pass-outcome-number-17)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-18">18/40</div>|:white_check_mark:Pass|`dataset-manufacturing-environments-discover-behavior-specifications`|[owl-rl-constraint](https://ns.inria.fr/olivaw#owl-rl-constraint)|OWL RL consistent|[Jump](#pass-outcome-number-18)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-19">19/40</div>|:white_check_mark:Pass|`dataset-manufacturing-environments-discover-behavior-specifications`|[syntax](https://ns.inria.fr/olivaw#syntax)|Correct syntax|[Jump](#pass-outcome-number-19)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-20">20/40</div>|:white_check_mark:Pass|`dataset-manufacturing-environments-discover-behavior-specifications`|[term-recognition](https://ns.inria.fr/olivaw#term-recognition)|Every term exists|[Jump](#pass-outcome-number-20)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-21">21/40</div>|:white_check_mark:Pass|`dataset-logistics-structure-organization`|[namespace-validity](https://ns.inria.fr/olivaw#namespace-validity)|No namespace typo|[Jump](#pass-outcome-number-21)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-22">22/40</div>|:white_check_mark:Pass|`dataset-logistics-structure-organization`|[owl-rl-constraint](https://ns.inria.fr/olivaw#owl-rl-constraint)|OWL RL consistent|[Jump](#pass-outcome-number-22)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-23">23/40</div>|:white_check_mark:Pass|`dataset-logistics-structure-organization`|[syntax](https://ns.inria.fr/olivaw#syntax)|Correct syntax|[Jump](#pass-outcome-number-23)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-24">24/40</div>|:white_check_mark:Pass|`dataset-logistics-structure-organization`|[term-recognition](https://ns.inria.fr/olivaw#term-recognition)|Every term exists|[Jump](#pass-outcome-number-24)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-25">25/40</div>|:white_check_mark:Pass|`dataset-logistics-create-organization`|[namespace-validity](https://ns.inria.fr/olivaw#namespace-validity)|No namespace typo|[Jump](#pass-outcome-number-25)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-26">26/40</div>|:white_check_mark:Pass|`dataset-logistics-create-organization`|[owl-rl-constraint](https://ns.inria.fr/olivaw#owl-rl-constraint)|OWL RL consistent|[Jump](#pass-outcome-number-26)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-27">27/40</div>|:white_check_mark:Pass|`dataset-logistics-create-organization`|[syntax](https://ns.inria.fr/olivaw#syntax)|Correct syntax|[Jump](#pass-outcome-number-27)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-28">28/40</div>|:white_check_mark:Pass|`dataset-logistics-create-organization`|[term-recognition](https://ns.inria.fr/olivaw#term-recognition)|Every term exists|[Jump](#pass-outcome-number-28)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-29">29/40</div>|:white_check_mark:Pass|`dataset-logistics-coordinate-activities`|[namespace-validity](https://ns.inria.fr/olivaw#namespace-validity)|No namespace typo|[Jump](#pass-outcome-number-29)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-30">30/40</div>|:white_check_mark:Pass|`dataset-logistics-coordinate-activities`|[owl-rl-constraint](https://ns.inria.fr/olivaw#owl-rl-constraint)|OWL RL consistent|[Jump](#pass-outcome-number-30)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-31">31/40</div>|:white_check_mark:Pass|`dataset-logistics-coordinate-activities`|[syntax](https://ns.inria.fr/olivaw#syntax)|Correct syntax|[Jump](#pass-outcome-number-31)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-32">32/40</div>|:white_check_mark:Pass|`dataset-logistics-coordinate-activities`|[term-recognition](https://ns.inria.fr/olivaw#term-recognition)|Every term exists|[Jump](#pass-outcome-number-32)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-33">33/40</div>|:white_check_mark:Pass|`dataset-logistics-configure-organization`|[namespace-validity](https://ns.inria.fr/olivaw#namespace-validity)|No namespace typo|[Jump](#pass-outcome-number-33)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-34">34/40</div>|:white_check_mark:Pass|`dataset-logistics-configure-organization`|[owl-rl-constraint](https://ns.inria.fr/olivaw#owl-rl-constraint)|OWL RL consistent|[Jump](#pass-outcome-number-34)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-35">35/40</div>|:white_check_mark:Pass|`dataset-logistics-configure-organization`|[syntax](https://ns.inria.fr/olivaw#syntax)|Correct syntax|[Jump](#pass-outcome-number-35)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-36">36/40</div>|:white_check_mark:Pass|`dataset-logistics-configure-organization`|[term-recognition](https://ns.inria.fr/olivaw#term-recognition)|Every term exists|[Jump](#pass-outcome-number-36)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-37">37/40</div>|:white_check_mark:Pass|`dataset-domain-template-scenario-template`|[namespace-validity](https://ns.inria.fr/olivaw#namespace-validity)|No namespace typo|[Jump](#pass-outcome-number-37)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-38">38/40</div>|:white_check_mark:Pass|`dataset-domain-template-scenario-template`|[owl-rl-constraint](https://ns.inria.fr/olivaw#owl-rl-constraint)|OWL RL consistent|[Jump](#pass-outcome-number-38)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-39">39/40</div>|:white_check_mark:Pass|`dataset-domain-template-scenario-template`|[syntax](https://ns.inria.fr/olivaw#syntax)|Correct syntax|[Jump](#pass-outcome-number-39)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-40">40/40</div>|:white_check_mark:Pass|`dataset-domain-template-scenario-template`|[term-recognition](https://ns.inria.fr/olivaw#term-recognition)|Every term exists|[Jump](#pass-outcome-number-40)|

***

## Pass Outcomes Details

This subchapter gives more details to the :white_check_mark:Pass outcomes

### Pass Outcome number 1

[Jump to summary definition](#summary-Pass-1)	|	Previous Pass outcome	|	[Next Pass outcome](#pass-outcome-number-2)

:white_check_mark:Pass outcome
#### Subject detail
|Name|usecase-manufacturing-dataset-v1|
|----|----|
|Title|Standalone&#32;use&#32;case&#32;use-cases/manufacturing/dataset-v1.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Use case manufacturing/dataset-v1](https://github.com/HyperAgents/hmas/blob/HEAD/use-cases/manufacturing/dataset-v1.ttl)|

#### Criterion detail
|Identifier|[owl-rl-constraint](https://ns.inria.fr/olivaw#owl-rl-constraint)|
|----|----|
|Title|OWL&#32;RL&#32;Constraint&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;check&#32;wether&#32;the&#32;test&#32;subject&#32;is&#32;syntaxically&#32;correct&#32;or&#32;not.|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-1)|Identifier|`owl-rl-constraint-violation`|
|[Section top](#pass-outcome-number-1)|Title|OWL&#32;RL&#32;consistent|
|[Section top](#pass-outcome-number-1)|Description|The&#32;provided&#32;graph&#32;is&#32;consistent&#32;for&#32;any&#32;OWL&#32;RL&#32;constraint|

***
### Pass Outcome number 2

[Jump to summary definition](#summary-Pass-2)	|	[Previous Pass outcome](#pass-outcome-number-1)	|	[Next Pass outcome](#pass-outcome-number-3)

:white_check_mark:Pass outcome
#### Subject detail
|Name|usecase-manufacturing-dataset-v1|
|----|----|
|Title|Standalone&#32;use&#32;case&#32;use-cases/manufacturing/dataset-v1.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Use case manufacturing/dataset-v1](https://github.com/HyperAgents/hmas/blob/HEAD/use-cases/manufacturing/dataset-v1.ttl)|

#### Criterion detail
|Identifier|[syntax](https://ns.inria.fr/olivaw#syntax)|
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
|Name|dataset-manufacturing-environments-discover-signifiers|
|----|----|
|Title|Standalone&#32;dataset&#32;domains/manufacturing-environments/discover-signifiers/dataset.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Dataset manufacturing-environments/discover-signifiers](https://github.com/HyperAgents/hmas/blob/HEAD/domains/manufacturing-environments/discover-signifiers/dataset.ttl)|

#### Criterion detail
|Identifier|[namespace-validity](https://ns.inria.fr/olivaw#namespace-validity)|
|----|----|
|Title|Namespace&#32;validity&#32;test|
|Description|A&#32;test&#32;case&#32;checking&#32;if&#32;all&#32;the&#32;Namespaces&#32;are&#32;not&#32;too&#32;close&#32;from&#32;the&#32;most&#32;used&#32;existing&#32;namespaces&#32;(according&#32;to&#32;prefix&#32;cc)&#32;or&#32;an&#32;ontology&#32;namespace|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-3)|Identifier|`namespace-typo`|
|[Section top](#pass-outcome-number-3)|Title|No&#32;namespace&#32;typo|
|[Section top](#pass-outcome-number-3)|Description|It&#32;seems&#32;that&#32;none&#32;of&#32;the&#32;subject&#32;URIs&#32;have&#32;namespaces&#32;typos|

***
### Pass Outcome number 4

[Jump to summary definition](#summary-Pass-4)	|	[Previous Pass outcome](#pass-outcome-number-3)	|	[Next Pass outcome](#pass-outcome-number-5)

:white_check_mark:Pass outcome
#### Subject detail
|Name|dataset-manufacturing-environments-discover-signifiers|
|----|----|
|Title|Standalone&#32;dataset&#32;domains/manufacturing-environments/discover-signifiers/dataset.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Dataset manufacturing-environments/discover-signifiers](https://github.com/HyperAgents/hmas/blob/HEAD/domains/manufacturing-environments/discover-signifiers/dataset.ttl)|

#### Criterion detail
|Identifier|[owl-rl-constraint](https://ns.inria.fr/olivaw#owl-rl-constraint)|
|----|----|
|Title|OWL&#32;RL&#32;Constraint&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;check&#32;wether&#32;the&#32;test&#32;subject&#32;is&#32;syntaxically&#32;correct&#32;or&#32;not.|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-4)|Identifier|`owl-rl-constraint-violation`|
|[Section top](#pass-outcome-number-4)|Title|OWL&#32;RL&#32;consistent|
|[Section top](#pass-outcome-number-4)|Description|The&#32;provided&#32;graph&#32;is&#32;consistent&#32;for&#32;any&#32;OWL&#32;RL&#32;constraint|

***
### Pass Outcome number 5

[Jump to summary definition](#summary-Pass-5)	|	[Previous Pass outcome](#pass-outcome-number-4)	|	[Next Pass outcome](#pass-outcome-number-6)

:white_check_mark:Pass outcome
#### Subject detail
|Name|dataset-manufacturing-environments-discover-signifiers|
|----|----|
|Title|Standalone&#32;dataset&#32;domains/manufacturing-environments/discover-signifiers/dataset.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Dataset manufacturing-environments/discover-signifiers](https://github.com/HyperAgents/hmas/blob/HEAD/domains/manufacturing-environments/discover-signifiers/dataset.ttl)|

#### Criterion detail
|Identifier|[syntax](https://ns.inria.fr/olivaw#syntax)|
|----|----|
|Title|Syntax&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;check&#32;wether&#32;the&#32;test&#32;subject&#32;is&#32;syntaxically&#32;correct&#32;or&#32;not.|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-5)|Identifier|`syntax-error`|
|[Section top](#pass-outcome-number-5)|Title|Correct&#32;syntax|
|[Section top](#pass-outcome-number-5)|Description|Test&#32;subject&#32;has&#32;a&#32;correct&#32;syntax|

***
### Pass Outcome number 6

[Jump to summary definition](#summary-Pass-6)	|	[Previous Pass outcome](#pass-outcome-number-5)	|	[Next Pass outcome](#pass-outcome-number-7)

:white_check_mark:Pass outcome
#### Subject detail
|Name|dataset-manufacturing-environments-discover-signifiers|
|----|----|
|Title|Standalone&#32;dataset&#32;domains/manufacturing-environments/discover-signifiers/dataset.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Dataset manufacturing-environments/discover-signifiers](https://github.com/HyperAgents/hmas/blob/HEAD/domains/manufacturing-environments/discover-signifiers/dataset.ttl)|

#### Criterion detail
|Identifier|[term-recognition](https://ns.inria.fr/olivaw#term-recognition)|
|----|----|
|Title|Term&#32;recognition&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;detect&#32;if&#32;all&#32;the&#32;terms&#32;from&#32;the&#32;subject&#32;that&#32;are&#32;from&#32;the&#32;ontology&#32;namespace&#32;are&#32;indeed&#32;defined&#32;in&#32;the&#32;ontology|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-6)|Identifier|`unknown-term`|
|[Section top](#pass-outcome-number-6)|Title|Every&#32;term&#32;exists|
|[Section top](#pass-outcome-number-6)|Description|All&#32;the&#32;ontologic&#32;terms&#32;in&#32;the&#32;subject&#32;are&#32;defined&#32;in&#32;the&#32;ontology|

***
### Pass Outcome number 7

[Jump to summary definition](#summary-Pass-7)	|	[Previous Pass outcome](#pass-outcome-number-6)	|	[Next Pass outcome](#pass-outcome-number-8)

:white_check_mark:Pass outcome
#### Subject detail
|Name|dataset-manufacturing-environments-discover-platforms|
|----|----|
|Title|Standalone&#32;dataset&#32;domains/manufacturing-environments/discover-platforms/dataset.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Dataset manufacturing-environments/discover-platforms](https://github.com/HyperAgents/hmas/blob/HEAD/domains/manufacturing-environments/discover-platforms/dataset.ttl)|

#### Criterion detail
|Identifier|[namespace-validity](https://ns.inria.fr/olivaw#namespace-validity)|
|----|----|
|Title|Namespace&#32;validity&#32;test|
|Description|A&#32;test&#32;case&#32;checking&#32;if&#32;all&#32;the&#32;Namespaces&#32;are&#32;not&#32;too&#32;close&#32;from&#32;the&#32;most&#32;used&#32;existing&#32;namespaces&#32;(according&#32;to&#32;prefix&#32;cc)&#32;or&#32;an&#32;ontology&#32;namespace|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-7)|Identifier|`namespace-typo`|
|[Section top](#pass-outcome-number-7)|Title|No&#32;namespace&#32;typo|
|[Section top](#pass-outcome-number-7)|Description|It&#32;seems&#32;that&#32;none&#32;of&#32;the&#32;subject&#32;URIs&#32;have&#32;namespaces&#32;typos|

***
### Pass Outcome number 8

[Jump to summary definition](#summary-Pass-8)	|	[Previous Pass outcome](#pass-outcome-number-7)	|	[Next Pass outcome](#pass-outcome-number-9)

:white_check_mark:Pass outcome
#### Subject detail
|Name|dataset-manufacturing-environments-discover-platforms|
|----|----|
|Title|Standalone&#32;dataset&#32;domains/manufacturing-environments/discover-platforms/dataset.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Dataset manufacturing-environments/discover-platforms](https://github.com/HyperAgents/hmas/blob/HEAD/domains/manufacturing-environments/discover-platforms/dataset.ttl)|

#### Criterion detail
|Identifier|[owl-rl-constraint](https://ns.inria.fr/olivaw#owl-rl-constraint)|
|----|----|
|Title|OWL&#32;RL&#32;Constraint&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;check&#32;wether&#32;the&#32;test&#32;subject&#32;is&#32;syntaxically&#32;correct&#32;or&#32;not.|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-8)|Identifier|`owl-rl-constraint-violation`|
|[Section top](#pass-outcome-number-8)|Title|OWL&#32;RL&#32;consistent|
|[Section top](#pass-outcome-number-8)|Description|The&#32;provided&#32;graph&#32;is&#32;consistent&#32;for&#32;any&#32;OWL&#32;RL&#32;constraint|

***
### Pass Outcome number 9

[Jump to summary definition](#summary-Pass-9)	|	[Previous Pass outcome](#pass-outcome-number-8)	|	[Next Pass outcome](#pass-outcome-number-10)

:white_check_mark:Pass outcome
#### Subject detail
|Name|dataset-manufacturing-environments-discover-platforms|
|----|----|
|Title|Standalone&#32;dataset&#32;domains/manufacturing-environments/discover-platforms/dataset.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Dataset manufacturing-environments/discover-platforms](https://github.com/HyperAgents/hmas/blob/HEAD/domains/manufacturing-environments/discover-platforms/dataset.ttl)|

#### Criterion detail
|Identifier|[syntax](https://ns.inria.fr/olivaw#syntax)|
|----|----|
|Title|Syntax&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;check&#32;wether&#32;the&#32;test&#32;subject&#32;is&#32;syntaxically&#32;correct&#32;or&#32;not.|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-9)|Identifier|`syntax-error`|
|[Section top](#pass-outcome-number-9)|Title|Correct&#32;syntax|
|[Section top](#pass-outcome-number-9)|Description|Test&#32;subject&#32;has&#32;a&#32;correct&#32;syntax|

***
### Pass Outcome number 10

[Jump to summary definition](#summary-Pass-10)	|	[Previous Pass outcome](#pass-outcome-number-9)	|	[Next Pass outcome](#pass-outcome-number-11)

:white_check_mark:Pass outcome
#### Subject detail
|Name|dataset-manufacturing-environments-discover-organization|
|----|----|
|Title|Standalone&#32;dataset&#32;domains/manufacturing-environments/discover-organization/dataset.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Dataset manufacturing-environments/discover-organization](https://github.com/HyperAgents/hmas/blob/HEAD/domains/manufacturing-environments/discover-organization/dataset.ttl)|

#### Criterion detail
|Identifier|[namespace-validity](https://ns.inria.fr/olivaw#namespace-validity)|
|----|----|
|Title|Namespace&#32;validity&#32;test|
|Description|A&#32;test&#32;case&#32;checking&#32;if&#32;all&#32;the&#32;Namespaces&#32;are&#32;not&#32;too&#32;close&#32;from&#32;the&#32;most&#32;used&#32;existing&#32;namespaces&#32;(according&#32;to&#32;prefix&#32;cc)&#32;or&#32;an&#32;ontology&#32;namespace|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-10)|Identifier|`namespace-typo`|
|[Section top](#pass-outcome-number-10)|Title|No&#32;namespace&#32;typo|
|[Section top](#pass-outcome-number-10)|Description|It&#32;seems&#32;that&#32;none&#32;of&#32;the&#32;subject&#32;URIs&#32;have&#32;namespaces&#32;typos|

***
### Pass Outcome number 11

[Jump to summary definition](#summary-Pass-11)	|	[Previous Pass outcome](#pass-outcome-number-10)	|	[Next Pass outcome](#pass-outcome-number-12)

:white_check_mark:Pass outcome
#### Subject detail
|Name|dataset-manufacturing-environments-discover-organization|
|----|----|
|Title|Standalone&#32;dataset&#32;domains/manufacturing-environments/discover-organization/dataset.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Dataset manufacturing-environments/discover-organization](https://github.com/HyperAgents/hmas/blob/HEAD/domains/manufacturing-environments/discover-organization/dataset.ttl)|

#### Criterion detail
|Identifier|[owl-rl-constraint](https://ns.inria.fr/olivaw#owl-rl-constraint)|
|----|----|
|Title|OWL&#32;RL&#32;Constraint&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;check&#32;wether&#32;the&#32;test&#32;subject&#32;is&#32;syntaxically&#32;correct&#32;or&#32;not.|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-11)|Identifier|`owl-rl-constraint-violation`|
|[Section top](#pass-outcome-number-11)|Title|OWL&#32;RL&#32;consistent|
|[Section top](#pass-outcome-number-11)|Description|The&#32;provided&#32;graph&#32;is&#32;consistent&#32;for&#32;any&#32;OWL&#32;RL&#32;constraint|

***
### Pass Outcome number 12

[Jump to summary definition](#summary-Pass-12)	|	[Previous Pass outcome](#pass-outcome-number-11)	|	[Next Pass outcome](#pass-outcome-number-13)

:white_check_mark:Pass outcome
#### Subject detail
|Name|dataset-manufacturing-environments-discover-organization|
|----|----|
|Title|Standalone&#32;dataset&#32;domains/manufacturing-environments/discover-organization/dataset.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Dataset manufacturing-environments/discover-organization](https://github.com/HyperAgents/hmas/blob/HEAD/domains/manufacturing-environments/discover-organization/dataset.ttl)|

#### Criterion detail
|Identifier|[syntax](https://ns.inria.fr/olivaw#syntax)|
|----|----|
|Title|Syntax&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;check&#32;wether&#32;the&#32;test&#32;subject&#32;is&#32;syntaxically&#32;correct&#32;or&#32;not.|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-12)|Identifier|`syntax-error`|
|[Section top](#pass-outcome-number-12)|Title|Correct&#32;syntax|
|[Section top](#pass-outcome-number-12)|Description|Test&#32;subject&#32;has&#32;a&#32;correct&#32;syntax|

***
### Pass Outcome number 13

[Jump to summary definition](#summary-Pass-13)	|	[Previous Pass outcome](#pass-outcome-number-12)	|	[Next Pass outcome](#pass-outcome-number-14)

:white_check_mark:Pass outcome
#### Subject detail
|Name|dataset-manufacturing-environments-discover-organization|
|----|----|
|Title|Standalone&#32;dataset&#32;domains/manufacturing-environments/discover-organization/dataset.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Dataset manufacturing-environments/discover-organization](https://github.com/HyperAgents/hmas/blob/HEAD/domains/manufacturing-environments/discover-organization/dataset.ttl)|

#### Criterion detail
|Identifier|[term-recognition](https://ns.inria.fr/olivaw#term-recognition)|
|----|----|
|Title|Term&#32;recognition&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;detect&#32;if&#32;all&#32;the&#32;terms&#32;from&#32;the&#32;subject&#32;that&#32;are&#32;from&#32;the&#32;ontology&#32;namespace&#32;are&#32;indeed&#32;defined&#32;in&#32;the&#32;ontology|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-13)|Identifier|`unknown-term`|
|[Section top](#pass-outcome-number-13)|Title|Every&#32;term&#32;exists|
|[Section top](#pass-outcome-number-13)|Description|All&#32;the&#32;ontologic&#32;terms&#32;in&#32;the&#32;subject&#32;are&#32;defined&#32;in&#32;the&#32;ontology|

***
### Pass Outcome number 14

[Jump to summary definition](#summary-Pass-14)	|	[Previous Pass outcome](#pass-outcome-number-13)	|	[Next Pass outcome](#pass-outcome-number-15)

:white_check_mark:Pass outcome
#### Subject detail
|Name|dataset-manufacturing-environments-discover-core|
|----|----|
|Title|Standalone&#32;dataset&#32;domains/manufacturing-environments/discover-core/dataset.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Dataset manufacturing-environments/discover-core](https://github.com/HyperAgents/hmas/blob/HEAD/domains/manufacturing-environments/discover-core/dataset.ttl)|

#### Criterion detail
|Identifier|[namespace-validity](https://ns.inria.fr/olivaw#namespace-validity)|
|----|----|
|Title|Namespace&#32;validity&#32;test|
|Description|A&#32;test&#32;case&#32;checking&#32;if&#32;all&#32;the&#32;Namespaces&#32;are&#32;not&#32;too&#32;close&#32;from&#32;the&#32;most&#32;used&#32;existing&#32;namespaces&#32;(according&#32;to&#32;prefix&#32;cc)&#32;or&#32;an&#32;ontology&#32;namespace|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-14)|Identifier|`namespace-typo`|
|[Section top](#pass-outcome-number-14)|Title|No&#32;namespace&#32;typo|
|[Section top](#pass-outcome-number-14)|Description|It&#32;seems&#32;that&#32;none&#32;of&#32;the&#32;subject&#32;URIs&#32;have&#32;namespaces&#32;typos|

***
### Pass Outcome number 15

[Jump to summary definition](#summary-Pass-15)	|	[Previous Pass outcome](#pass-outcome-number-14)	|	[Next Pass outcome](#pass-outcome-number-16)

:white_check_mark:Pass outcome
#### Subject detail
|Name|dataset-manufacturing-environments-discover-core|
|----|----|
|Title|Standalone&#32;dataset&#32;domains/manufacturing-environments/discover-core/dataset.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Dataset manufacturing-environments/discover-core](https://github.com/HyperAgents/hmas/blob/HEAD/domains/manufacturing-environments/discover-core/dataset.ttl)|

#### Criterion detail
|Identifier|[owl-rl-constraint](https://ns.inria.fr/olivaw#owl-rl-constraint)|
|----|----|
|Title|OWL&#32;RL&#32;Constraint&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;check&#32;wether&#32;the&#32;test&#32;subject&#32;is&#32;syntaxically&#32;correct&#32;or&#32;not.|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-15)|Identifier|`owl-rl-constraint-violation`|
|[Section top](#pass-outcome-number-15)|Title|OWL&#32;RL&#32;consistent|
|[Section top](#pass-outcome-number-15)|Description|The&#32;provided&#32;graph&#32;is&#32;consistent&#32;for&#32;any&#32;OWL&#32;RL&#32;constraint|

***
### Pass Outcome number 16

[Jump to summary definition](#summary-Pass-16)	|	[Previous Pass outcome](#pass-outcome-number-15)	|	[Next Pass outcome](#pass-outcome-number-17)

:white_check_mark:Pass outcome
#### Subject detail
|Name|dataset-manufacturing-environments-discover-core|
|----|----|
|Title|Standalone&#32;dataset&#32;domains/manufacturing-environments/discover-core/dataset.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Dataset manufacturing-environments/discover-core](https://github.com/HyperAgents/hmas/blob/HEAD/domains/manufacturing-environments/discover-core/dataset.ttl)|

#### Criterion detail
|Identifier|[syntax](https://ns.inria.fr/olivaw#syntax)|
|----|----|
|Title|Syntax&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;check&#32;wether&#32;the&#32;test&#32;subject&#32;is&#32;syntaxically&#32;correct&#32;or&#32;not.|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-16)|Identifier|`syntax-error`|
|[Section top](#pass-outcome-number-16)|Title|Correct&#32;syntax|
|[Section top](#pass-outcome-number-16)|Description|Test&#32;subject&#32;has&#32;a&#32;correct&#32;syntax|

***
### Pass Outcome number 17

[Jump to summary definition](#summary-Pass-17)	|	[Previous Pass outcome](#pass-outcome-number-16)	|	[Next Pass outcome](#pass-outcome-number-18)

:white_check_mark:Pass outcome
#### Subject detail
|Name|dataset-manufacturing-environments-discover-core|
|----|----|
|Title|Standalone&#32;dataset&#32;domains/manufacturing-environments/discover-core/dataset.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Dataset manufacturing-environments/discover-core](https://github.com/HyperAgents/hmas/blob/HEAD/domains/manufacturing-environments/discover-core/dataset.ttl)|

#### Criterion detail
|Identifier|[term-recognition](https://ns.inria.fr/olivaw#term-recognition)|
|----|----|
|Title|Term&#32;recognition&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;detect&#32;if&#32;all&#32;the&#32;terms&#32;from&#32;the&#32;subject&#32;that&#32;are&#32;from&#32;the&#32;ontology&#32;namespace&#32;are&#32;indeed&#32;defined&#32;in&#32;the&#32;ontology|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-17)|Identifier|`unknown-term`|
|[Section top](#pass-outcome-number-17)|Title|Every&#32;term&#32;exists|
|[Section top](#pass-outcome-number-17)|Description|All&#32;the&#32;ontologic&#32;terms&#32;in&#32;the&#32;subject&#32;are&#32;defined&#32;in&#32;the&#32;ontology|

***
### Pass Outcome number 18

[Jump to summary definition](#summary-Pass-18)	|	[Previous Pass outcome](#pass-outcome-number-17)	|	[Next Pass outcome](#pass-outcome-number-19)

:white_check_mark:Pass outcome
#### Subject detail
|Name|dataset-manufacturing-environments-discover-behavior-specifications|
|----|----|
|Title|Standalone&#32;dataset&#32;domains/manufacturing-environments/discover-behavior-specifications/dataset.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Dataset manufacturing-environments/discover-behavior-specifications](https://github.com/HyperAgents/hmas/blob/HEAD/domains/manufacturing-environments/discover-behavior-specifications/dataset.ttl)|

#### Criterion detail
|Identifier|[owl-rl-constraint](https://ns.inria.fr/olivaw#owl-rl-constraint)|
|----|----|
|Title|OWL&#32;RL&#32;Constraint&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;check&#32;wether&#32;the&#32;test&#32;subject&#32;is&#32;syntaxically&#32;correct&#32;or&#32;not.|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-18)|Identifier|`owl-rl-constraint-violation`|
|[Section top](#pass-outcome-number-18)|Title|OWL&#32;RL&#32;consistent|
|[Section top](#pass-outcome-number-18)|Description|The&#32;provided&#32;graph&#32;is&#32;consistent&#32;for&#32;any&#32;OWL&#32;RL&#32;constraint|

***
### Pass Outcome number 19

[Jump to summary definition](#summary-Pass-19)	|	[Previous Pass outcome](#pass-outcome-number-18)	|	[Next Pass outcome](#pass-outcome-number-20)

:white_check_mark:Pass outcome
#### Subject detail
|Name|dataset-manufacturing-environments-discover-behavior-specifications|
|----|----|
|Title|Standalone&#32;dataset&#32;domains/manufacturing-environments/discover-behavior-specifications/dataset.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Dataset manufacturing-environments/discover-behavior-specifications](https://github.com/HyperAgents/hmas/blob/HEAD/domains/manufacturing-environments/discover-behavior-specifications/dataset.ttl)|

#### Criterion detail
|Identifier|[syntax](https://ns.inria.fr/olivaw#syntax)|
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
|Name|dataset-manufacturing-environments-discover-behavior-specifications|
|----|----|
|Title|Standalone&#32;dataset&#32;domains/manufacturing-environments/discover-behavior-specifications/dataset.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Dataset manufacturing-environments/discover-behavior-specifications](https://github.com/HyperAgents/hmas/blob/HEAD/domains/manufacturing-environments/discover-behavior-specifications/dataset.ttl)|

#### Criterion detail
|Identifier|[term-recognition](https://ns.inria.fr/olivaw#term-recognition)|
|----|----|
|Title|Term&#32;recognition&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;detect&#32;if&#32;all&#32;the&#32;terms&#32;from&#32;the&#32;subject&#32;that&#32;are&#32;from&#32;the&#32;ontology&#32;namespace&#32;are&#32;indeed&#32;defined&#32;in&#32;the&#32;ontology|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-20)|Identifier|`unknown-term`|
|[Section top](#pass-outcome-number-20)|Title|Every&#32;term&#32;exists|
|[Section top](#pass-outcome-number-20)|Description|All&#32;the&#32;ontologic&#32;terms&#32;in&#32;the&#32;subject&#32;are&#32;defined&#32;in&#32;the&#32;ontology|

***
### Pass Outcome number 21

[Jump to summary definition](#summary-Pass-21)	|	[Previous Pass outcome](#pass-outcome-number-20)	|	[Next Pass outcome](#pass-outcome-number-22)

:white_check_mark:Pass outcome
#### Subject detail
|Name|dataset-logistics-structure-organization|
|----|----|
|Title|Standalone&#32;dataset&#32;domains/logistics/structure-organization/dataset.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Dataset logistics/structure-organization](https://github.com/HyperAgents/hmas/blob/HEAD/domains/logistics/structure-organization/dataset.ttl)|

#### Criterion detail
|Identifier|[namespace-validity](https://ns.inria.fr/olivaw#namespace-validity)|
|----|----|
|Title|Namespace&#32;validity&#32;test|
|Description|A&#32;test&#32;case&#32;checking&#32;if&#32;all&#32;the&#32;Namespaces&#32;are&#32;not&#32;too&#32;close&#32;from&#32;the&#32;most&#32;used&#32;existing&#32;namespaces&#32;(according&#32;to&#32;prefix&#32;cc)&#32;or&#32;an&#32;ontology&#32;namespace|

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
|Name|dataset-logistics-structure-organization|
|----|----|
|Title|Standalone&#32;dataset&#32;domains/logistics/structure-organization/dataset.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Dataset logistics/structure-organization](https://github.com/HyperAgents/hmas/blob/HEAD/domains/logistics/structure-organization/dataset.ttl)|

#### Criterion detail
|Identifier|[owl-rl-constraint](https://ns.inria.fr/olivaw#owl-rl-constraint)|
|----|----|
|Title|OWL&#32;RL&#32;Constraint&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;check&#32;wether&#32;the&#32;test&#32;subject&#32;is&#32;syntaxically&#32;correct&#32;or&#32;not.|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-22)|Identifier|`owl-rl-constraint-violation`|
|[Section top](#pass-outcome-number-22)|Title|OWL&#32;RL&#32;consistent|
|[Section top](#pass-outcome-number-22)|Description|The&#32;provided&#32;graph&#32;is&#32;consistent&#32;for&#32;any&#32;OWL&#32;RL&#32;constraint|

***
### Pass Outcome number 23

[Jump to summary definition](#summary-Pass-23)	|	[Previous Pass outcome](#pass-outcome-number-22)	|	[Next Pass outcome](#pass-outcome-number-24)

:white_check_mark:Pass outcome
#### Subject detail
|Name|dataset-logistics-structure-organization|
|----|----|
|Title|Standalone&#32;dataset&#32;domains/logistics/structure-organization/dataset.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Dataset logistics/structure-organization](https://github.com/HyperAgents/hmas/blob/HEAD/domains/logistics/structure-organization/dataset.ttl)|

#### Criterion detail
|Identifier|[syntax](https://ns.inria.fr/olivaw#syntax)|
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
|Name|dataset-logistics-structure-organization|
|----|----|
|Title|Standalone&#32;dataset&#32;domains/logistics/structure-organization/dataset.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Dataset logistics/structure-organization](https://github.com/HyperAgents/hmas/blob/HEAD/domains/logistics/structure-organization/dataset.ttl)|

#### Criterion detail
|Identifier|[term-recognition](https://ns.inria.fr/olivaw#term-recognition)|
|----|----|
|Title|Term&#32;recognition&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;detect&#32;if&#32;all&#32;the&#32;terms&#32;from&#32;the&#32;subject&#32;that&#32;are&#32;from&#32;the&#32;ontology&#32;namespace&#32;are&#32;indeed&#32;defined&#32;in&#32;the&#32;ontology|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-24)|Identifier|`unknown-term`|
|[Section top](#pass-outcome-number-24)|Title|Every&#32;term&#32;exists|
|[Section top](#pass-outcome-number-24)|Description|All&#32;the&#32;ontologic&#32;terms&#32;in&#32;the&#32;subject&#32;are&#32;defined&#32;in&#32;the&#32;ontology|

***
### Pass Outcome number 25

[Jump to summary definition](#summary-Pass-25)	|	[Previous Pass outcome](#pass-outcome-number-24)	|	[Next Pass outcome](#pass-outcome-number-26)

:white_check_mark:Pass outcome
#### Subject detail
|Name|dataset-logistics-create-organization|
|----|----|
|Title|Standalone&#32;dataset&#32;domains/logistics/create-organization/dataset.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Dataset logistics/create-organization](https://github.com/HyperAgents/hmas/blob/HEAD/domains/logistics/create-organization/dataset.ttl)|

#### Criterion detail
|Identifier|[namespace-validity](https://ns.inria.fr/olivaw#namespace-validity)|
|----|----|
|Title|Namespace&#32;validity&#32;test|
|Description|A&#32;test&#32;case&#32;checking&#32;if&#32;all&#32;the&#32;Namespaces&#32;are&#32;not&#32;too&#32;close&#32;from&#32;the&#32;most&#32;used&#32;existing&#32;namespaces&#32;(according&#32;to&#32;prefix&#32;cc)&#32;or&#32;an&#32;ontology&#32;namespace|

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
|Name|dataset-logistics-create-organization|
|----|----|
|Title|Standalone&#32;dataset&#32;domains/logistics/create-organization/dataset.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Dataset logistics/create-organization](https://github.com/HyperAgents/hmas/blob/HEAD/domains/logistics/create-organization/dataset.ttl)|

#### Criterion detail
|Identifier|[owl-rl-constraint](https://ns.inria.fr/olivaw#owl-rl-constraint)|
|----|----|
|Title|OWL&#32;RL&#32;Constraint&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;check&#32;wether&#32;the&#32;test&#32;subject&#32;is&#32;syntaxically&#32;correct&#32;or&#32;not.|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-26)|Identifier|`owl-rl-constraint-violation`|
|[Section top](#pass-outcome-number-26)|Title|OWL&#32;RL&#32;consistent|
|[Section top](#pass-outcome-number-26)|Description|The&#32;provided&#32;graph&#32;is&#32;consistent&#32;for&#32;any&#32;OWL&#32;RL&#32;constraint|

***
### Pass Outcome number 27

[Jump to summary definition](#summary-Pass-27)	|	[Previous Pass outcome](#pass-outcome-number-26)	|	[Next Pass outcome](#pass-outcome-number-28)

:white_check_mark:Pass outcome
#### Subject detail
|Name|dataset-logistics-create-organization|
|----|----|
|Title|Standalone&#32;dataset&#32;domains/logistics/create-organization/dataset.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Dataset logistics/create-organization](https://github.com/HyperAgents/hmas/blob/HEAD/domains/logistics/create-organization/dataset.ttl)|

#### Criterion detail
|Identifier|[syntax](https://ns.inria.fr/olivaw#syntax)|
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
|Name|dataset-logistics-create-organization|
|----|----|
|Title|Standalone&#32;dataset&#32;domains/logistics/create-organization/dataset.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Dataset logistics/create-organization](https://github.com/HyperAgents/hmas/blob/HEAD/domains/logistics/create-organization/dataset.ttl)|

#### Criterion detail
|Identifier|[term-recognition](https://ns.inria.fr/olivaw#term-recognition)|
|----|----|
|Title|Term&#32;recognition&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;detect&#32;if&#32;all&#32;the&#32;terms&#32;from&#32;the&#32;subject&#32;that&#32;are&#32;from&#32;the&#32;ontology&#32;namespace&#32;are&#32;indeed&#32;defined&#32;in&#32;the&#32;ontology|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-28)|Identifier|`unknown-term`|
|[Section top](#pass-outcome-number-28)|Title|Every&#32;term&#32;exists|
|[Section top](#pass-outcome-number-28)|Description|All&#32;the&#32;ontologic&#32;terms&#32;in&#32;the&#32;subject&#32;are&#32;defined&#32;in&#32;the&#32;ontology|

***
### Pass Outcome number 29

[Jump to summary definition](#summary-Pass-29)	|	[Previous Pass outcome](#pass-outcome-number-28)	|	[Next Pass outcome](#pass-outcome-number-30)

:white_check_mark:Pass outcome
#### Subject detail
|Name|dataset-logistics-coordinate-activities|
|----|----|
|Title|Standalone&#32;dataset&#32;domains/logistics/coordinate-activities/dataset.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Dataset logistics/coordinate-activities](https://github.com/HyperAgents/hmas/blob/HEAD/domains/logistics/coordinate-activities/dataset.ttl)|

#### Criterion detail
|Identifier|[namespace-validity](https://ns.inria.fr/olivaw#namespace-validity)|
|----|----|
|Title|Namespace&#32;validity&#32;test|
|Description|A&#32;test&#32;case&#32;checking&#32;if&#32;all&#32;the&#32;Namespaces&#32;are&#32;not&#32;too&#32;close&#32;from&#32;the&#32;most&#32;used&#32;existing&#32;namespaces&#32;(according&#32;to&#32;prefix&#32;cc)&#32;or&#32;an&#32;ontology&#32;namespace|

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
|Name|dataset-logistics-coordinate-activities|
|----|----|
|Title|Standalone&#32;dataset&#32;domains/logistics/coordinate-activities/dataset.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Dataset logistics/coordinate-activities](https://github.com/HyperAgents/hmas/blob/HEAD/domains/logistics/coordinate-activities/dataset.ttl)|

#### Criterion detail
|Identifier|[owl-rl-constraint](https://ns.inria.fr/olivaw#owl-rl-constraint)|
|----|----|
|Title|OWL&#32;RL&#32;Constraint&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;check&#32;wether&#32;the&#32;test&#32;subject&#32;is&#32;syntaxically&#32;correct&#32;or&#32;not.|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-30)|Identifier|`owl-rl-constraint-violation`|
|[Section top](#pass-outcome-number-30)|Title|OWL&#32;RL&#32;consistent|
|[Section top](#pass-outcome-number-30)|Description|The&#32;provided&#32;graph&#32;is&#32;consistent&#32;for&#32;any&#32;OWL&#32;RL&#32;constraint|

***
### Pass Outcome number 31

[Jump to summary definition](#summary-Pass-31)	|	[Previous Pass outcome](#pass-outcome-number-30)	|	[Next Pass outcome](#pass-outcome-number-32)

:white_check_mark:Pass outcome
#### Subject detail
|Name|dataset-logistics-coordinate-activities|
|----|----|
|Title|Standalone&#32;dataset&#32;domains/logistics/coordinate-activities/dataset.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Dataset logistics/coordinate-activities](https://github.com/HyperAgents/hmas/blob/HEAD/domains/logistics/coordinate-activities/dataset.ttl)|

#### Criterion detail
|Identifier|[syntax](https://ns.inria.fr/olivaw#syntax)|
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
|Name|dataset-logistics-coordinate-activities|
|----|----|
|Title|Standalone&#32;dataset&#32;domains/logistics/coordinate-activities/dataset.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Dataset logistics/coordinate-activities](https://github.com/HyperAgents/hmas/blob/HEAD/domains/logistics/coordinate-activities/dataset.ttl)|

#### Criterion detail
|Identifier|[term-recognition](https://ns.inria.fr/olivaw#term-recognition)|
|----|----|
|Title|Term&#32;recognition&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;detect&#32;if&#32;all&#32;the&#32;terms&#32;from&#32;the&#32;subject&#32;that&#32;are&#32;from&#32;the&#32;ontology&#32;namespace&#32;are&#32;indeed&#32;defined&#32;in&#32;the&#32;ontology|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-32)|Identifier|`unknown-term`|
|[Section top](#pass-outcome-number-32)|Title|Every&#32;term&#32;exists|
|[Section top](#pass-outcome-number-32)|Description|All&#32;the&#32;ontologic&#32;terms&#32;in&#32;the&#32;subject&#32;are&#32;defined&#32;in&#32;the&#32;ontology|

***
### Pass Outcome number 33

[Jump to summary definition](#summary-Pass-33)	|	[Previous Pass outcome](#pass-outcome-number-32)	|	[Next Pass outcome](#pass-outcome-number-34)

:white_check_mark:Pass outcome
#### Subject detail
|Name|dataset-logistics-configure-organization|
|----|----|
|Title|Standalone&#32;dataset&#32;domains/logistics/configure-organization/dataset.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Dataset logistics/configure-organization](https://github.com/HyperAgents/hmas/blob/HEAD/domains/logistics/configure-organization/dataset.ttl)|

#### Criterion detail
|Identifier|[namespace-validity](https://ns.inria.fr/olivaw#namespace-validity)|
|----|----|
|Title|Namespace&#32;validity&#32;test|
|Description|A&#32;test&#32;case&#32;checking&#32;if&#32;all&#32;the&#32;Namespaces&#32;are&#32;not&#32;too&#32;close&#32;from&#32;the&#32;most&#32;used&#32;existing&#32;namespaces&#32;(according&#32;to&#32;prefix&#32;cc)&#32;or&#32;an&#32;ontology&#32;namespace|

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
|Name|dataset-logistics-configure-organization|
|----|----|
|Title|Standalone&#32;dataset&#32;domains/logistics/configure-organization/dataset.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Dataset logistics/configure-organization](https://github.com/HyperAgents/hmas/blob/HEAD/domains/logistics/configure-organization/dataset.ttl)|

#### Criterion detail
|Identifier|[owl-rl-constraint](https://ns.inria.fr/olivaw#owl-rl-constraint)|
|----|----|
|Title|OWL&#32;RL&#32;Constraint&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;check&#32;wether&#32;the&#32;test&#32;subject&#32;is&#32;syntaxically&#32;correct&#32;or&#32;not.|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-34)|Identifier|`owl-rl-constraint-violation`|
|[Section top](#pass-outcome-number-34)|Title|OWL&#32;RL&#32;consistent|
|[Section top](#pass-outcome-number-34)|Description|The&#32;provided&#32;graph&#32;is&#32;consistent&#32;for&#32;any&#32;OWL&#32;RL&#32;constraint|

***
### Pass Outcome number 35

[Jump to summary definition](#summary-Pass-35)	|	[Previous Pass outcome](#pass-outcome-number-34)	|	[Next Pass outcome](#pass-outcome-number-36)

:white_check_mark:Pass outcome
#### Subject detail
|Name|dataset-logistics-configure-organization|
|----|----|
|Title|Standalone&#32;dataset&#32;domains/logistics/configure-organization/dataset.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Dataset logistics/configure-organization](https://github.com/HyperAgents/hmas/blob/HEAD/domains/logistics/configure-organization/dataset.ttl)|

#### Criterion detail
|Identifier|[syntax](https://ns.inria.fr/olivaw#syntax)|
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
|Name|dataset-logistics-configure-organization|
|----|----|
|Title|Standalone&#32;dataset&#32;domains/logistics/configure-organization/dataset.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Dataset logistics/configure-organization](https://github.com/HyperAgents/hmas/blob/HEAD/domains/logistics/configure-organization/dataset.ttl)|

#### Criterion detail
|Identifier|[term-recognition](https://ns.inria.fr/olivaw#term-recognition)|
|----|----|
|Title|Term&#32;recognition&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;detect&#32;if&#32;all&#32;the&#32;terms&#32;from&#32;the&#32;subject&#32;that&#32;are&#32;from&#32;the&#32;ontology&#32;namespace&#32;are&#32;indeed&#32;defined&#32;in&#32;the&#32;ontology|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-36)|Identifier|`unknown-term`|
|[Section top](#pass-outcome-number-36)|Title|Every&#32;term&#32;exists|
|[Section top](#pass-outcome-number-36)|Description|All&#32;the&#32;ontologic&#32;terms&#32;in&#32;the&#32;subject&#32;are&#32;defined&#32;in&#32;the&#32;ontology|

***
### Pass Outcome number 37

[Jump to summary definition](#summary-Pass-37)	|	[Previous Pass outcome](#pass-outcome-number-36)	|	[Next Pass outcome](#pass-outcome-number-38)

:white_check_mark:Pass outcome
#### Subject detail
|Name|dataset-domain-template-scenario-template|
|----|----|
|Title|Standalone&#32;dataset&#32;domains/domain-template/scenario-template/dataset.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Dataset domain-template/scenario-template](https://github.com/HyperAgents/hmas/blob/HEAD/domains/domain-template/scenario-template/dataset.ttl)|

#### Criterion detail
|Identifier|[namespace-validity](https://ns.inria.fr/olivaw#namespace-validity)|
|----|----|
|Title|Namespace&#32;validity&#32;test|
|Description|A&#32;test&#32;case&#32;checking&#32;if&#32;all&#32;the&#32;Namespaces&#32;are&#32;not&#32;too&#32;close&#32;from&#32;the&#32;most&#32;used&#32;existing&#32;namespaces&#32;(according&#32;to&#32;prefix&#32;cc)&#32;or&#32;an&#32;ontology&#32;namespace|

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
|Name|dataset-domain-template-scenario-template|
|----|----|
|Title|Standalone&#32;dataset&#32;domains/domain-template/scenario-template/dataset.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Dataset domain-template/scenario-template](https://github.com/HyperAgents/hmas/blob/HEAD/domains/domain-template/scenario-template/dataset.ttl)|

#### Criterion detail
|Identifier|[owl-rl-constraint](https://ns.inria.fr/olivaw#owl-rl-constraint)|
|----|----|
|Title|OWL&#32;RL&#32;Constraint&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;check&#32;wether&#32;the&#32;test&#32;subject&#32;is&#32;syntaxically&#32;correct&#32;or&#32;not.|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-38)|Identifier|`owl-rl-constraint-violation`|
|[Section top](#pass-outcome-number-38)|Title|OWL&#32;RL&#32;consistent|
|[Section top](#pass-outcome-number-38)|Description|The&#32;provided&#32;graph&#32;is&#32;consistent&#32;for&#32;any&#32;OWL&#32;RL&#32;constraint|

***
### Pass Outcome number 39

[Jump to summary definition](#summary-Pass-39)	|	[Previous Pass outcome](#pass-outcome-number-38)	|	[Next Pass outcome](#pass-outcome-number-40)

:white_check_mark:Pass outcome
#### Subject detail
|Name|dataset-domain-template-scenario-template|
|----|----|
|Title|Standalone&#32;dataset&#32;domains/domain-template/scenario-template/dataset.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Dataset domain-template/scenario-template](https://github.com/HyperAgents/hmas/blob/HEAD/domains/domain-template/scenario-template/dataset.ttl)|

#### Criterion detail
|Identifier|[syntax](https://ns.inria.fr/olivaw#syntax)|
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

[Jump to summary definition](#summary-Pass-40)	|	[Previous Pass outcome](#pass-outcome-number-39)	|	Next Pass outcome

:white_check_mark:Pass outcome
#### Subject detail
|Name|dataset-domain-template-scenario-template|
|----|----|
|Title|Standalone&#32;dataset&#32;domains/domain-template/scenario-template/dataset.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Dataset domain-template/scenario-template](https://github.com/HyperAgents/hmas/blob/HEAD/domains/domain-template/scenario-template/dataset.ttl)|

#### Criterion detail
|Identifier|[term-recognition](https://ns.inria.fr/olivaw#term-recognition)|
|----|----|
|Title|Term&#32;recognition&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;detect&#32;if&#32;all&#32;the&#32;terms&#32;from&#32;the&#32;subject&#32;that&#32;are&#32;from&#32;the&#32;ontology&#32;namespace&#32;are&#32;indeed&#32;defined&#32;in&#32;the&#32;ontology|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-40)|Identifier|`unknown-term`|
|[Section top](#pass-outcome-number-40)|Title|Every&#32;term&#32;exists|
|[Section top](#pass-outcome-number-40)|Description|All&#32;the&#32;ontologic&#32;terms&#32;in&#32;the&#32;subject&#32;are&#32;defined&#32;in&#32;the&#32;ontology|

***

</details>

***
