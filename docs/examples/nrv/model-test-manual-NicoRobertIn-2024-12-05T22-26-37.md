# Test Report Markdown Export

This file is an export of the RDF test report made out of [EARL vocabulary](https://www.w3.org/TR/EARL10/)

This test is powered by Corese, check the [website](https://project.inria.fr/corese/) and the [repository](https://github.com/Wimmics/corese)

The original test report is available in turtle syntax [here](./model-test-manual-NicoRobertIn-2024-12-05T22-26-37.ttl).

# Test Activity

Here is some information about the testing activity that led to this report

|Title|Model&#32;tests&#32;of&#32;[Accord-Project/aec3po](https://github.com/Accord-Project/aec3po)&#32;on&#32;branch&#32;HEAD|
|--|--|
|Description|[NicoRobertIn](https://github.com/NicoRobertIn)&#32;launch&#32;manual&#32;run&#32;of&#32;model&#32;tests&#32;against&#32;[Accord-Project/aec3po](https://github.com/Accord-Project/aec3po)&#32;on&#32;branch&#32;HEAD|
|Tester|[NicoRobertIn](https://github.com/NicoRobertIn)|
|Ontology|[Accord-Project/aec3po](https://github.com/Accord-Project/aec3po)|
|Ontology version|Local state `18368cbcc203fb9257f380b5cd29e3403851d4a9`|
|Ontology version date|2024-12-05 22:26:33|
|Ontology previous version|[ef1ac8a152d8a37bf92cdaa007ecf5573c741bc8](https://github.com/Accord-Project/aec3po/tree/ef1ac8a152d8a37bf92cdaa007ecf5573c741bc8)|
|Ontology branch|[HEAD](https://github.com/Accord-Project/aec3po/tree/HEAD)|
|Olivaw suite|[olivaw model test suite](https://github.com/Wimmics/olivaw/blob/v0.0.6/olivaw/test/model/suite.py)|
|Olivaw version|[v0.0.6](https://pypi.org/project/olivaw/0.0.6)|
|Generated turtle|[Turtle report](./model-test-manual-NicoRobertIn-2024-12-05T22-26-37.ttl)|
|Generated Markdown|[Markdown report](./model-test-manual-NicoRobertIn-2024-12-05T22-26-37.md)|

# Statistic summary

Here is a short overview for this test report

13 Outcomes

:boom:0 MajorFail, :exclamation:4 MinorFail, :warning:0 CannotTell, :grey_question:0 NotTested, :white_check_mark:9 Pass

<div  style="border-radius: 12px; height: 25px; overflow: hidden"><img src="../assets/red.png" width="0%" height="25px"/><img src="../assets/orange.png" width="30%" height="25px"/><img src="../assets/grey.png" width="0%" height="25px"/><img src="../assets/white.png" width="0%" height="25px"/><img src="../assets/green.png" width="70%" height="25px"/></div>

<br/>

The different status types are an extension of the [EARL](https://www.w3.org/TR/EARL10-Schema/) vocabulary where the nextended terms can be found in the [olivaw ontology](https://ns.inria.fr/olivaw#), each outcome type means:
* :boom: MajorFail: This is an error that is critical and consider as blocking for production
* :exclamation: MinorFail: This is an error that should be fixed, but it is cannot be considered as critical error
* :warning: CannotTell: It is unclear if the subject passed or failed the test. This happens when an automated test requires human judgement to make a definite decision.
* :grey_question: NotTested:  The test has not been carried out. Here this is because a previous test that was mandatory to be passed did not end up as Pass.
* :white_check_mark: Pass: The subject passed the test.

***


# MinorFail Outcomes

[Jump to statistic summary](#statistic-summary)	|	Previous section	|	[Next section](#pass-outcomes)

Here is the chapter related to the MinorFail outcome

:exclamation:4 MinorFail outcomes

<details>
<summary>Fold/Unfold the 4 summary and details</summary>

## MinorFail Outcomes Summary

:exclamation:4 MinorFail outcomes

|*Jump*|*Number*|*Status*|*Subject*|*Criterion*|*Title*|*Link*|
|------|--------|--------|---------|-----------|-------|------|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-1">1/4</div>|:exclamation:MinorFail|`module-src-nrv-v1`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL EL Profile incompatible|[Jump](#minorfail-outcome-number-1)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-2">2/4</div>|:exclamation:MinorFail|`module-src-nrv-v1`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL QL Profile incompatible|[Jump](#minorfail-outcome-number-2)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-3">3/4</div>|:exclamation:MinorFail|`module-src-nrv-v1`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL RL Profile incompatible|[Jump](#minorfail-outcome-number-3)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-4">4/4</div>|:exclamation:MinorFail|`module-src-nrv-v1`|[term-referencing](https://ns.inria.fr/olivaw#term-referencing)|Term not referenced to a module|[Jump](#minorfail-outcome-number-4)|

***

## MinorFail Outcomes Details

This subchapter gives more details to the :exclamation:MinorFail outcomes

### MinorFail Outcome number 1

[Jump to summary definition](#summary-MinorFail-1)	|	Previous MinorFail outcome	|	[Next MinorFail outcome](#minorfail-outcome-number-2)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-src-nrv-v1|
|----|----|
|Title|Standalone&#32;module&#32;src/nrv&lowbar;v1.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Module nrv&lowbar;v1](https://github.com/Accord-Project/aec3po/blob/HEAD/src/nrv_v1.ttl)|

#### Criterion detail
|Identifier|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|
|----|----|
|Title|Profile&#32;compatibility&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;check&#32;whether&#32;the&#32;test&#32;subject&#32;is&#32;compatible&#32;with&#32;a&#32;profile&#32;or&#32;not,&#32;and&#32;if&#32;it&#32;is&#32;not,&#32;why.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-1)|Identifier|`owl-el-profile-error`|
|[Section top](#minorfail-outcome-number-1)|Title|OWL&#32;EL&#32;Profile&#32;incompatible|
|[Section top](#minorfail-outcome-number-1)|Description|Statement&#32;not&#32;supported|
|[Section top](#minorfail-outcome-number-1)|Pointer|<pre lang="Turtle"><code>nrv:NormativeRequirement&#32;a&#32;rdfs:Class&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;Normative&#32;Requirement&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;a&#32;requirement&#32;implying,&#32;creating,&#32;or&#32;prescribing&#32;a&#32;norm.&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:subClassOf&#32; &#60;http://docs.oasis-open.org/legalruleml/ns/v1.0/metamodel#DeonticSpecification> &#32;;  &#10; &#32; &#32; &#32; &#32;owl:disjointUnionOf&#32;(&#32;nrv:CompensableRequirement&#32;nrv:NonCompensableRequirement&#32;),  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;(&#32;nrv:ViolableRequirement&#32;nrv:NonViolableRequirement&#32;),  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;(&#32;nrv:PersistentRequirement&#32;nrv:NonPersistentRequirement&#32;)&#32;.</code></pre>|

***
### MinorFail Outcome number 2

[Jump to summary definition](#summary-MinorFail-2)	|	[Previous MinorFail outcome](#minorfail-outcome-number-1)	|	[Next MinorFail outcome](#minorfail-outcome-number-3)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-src-nrv-v1|
|----|----|
|Title|Standalone&#32;module&#32;src/nrv&lowbar;v1.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Module nrv&lowbar;v1](https://github.com/Accord-Project/aec3po/blob/HEAD/src/nrv_v1.ttl)|

#### Criterion detail
|Identifier|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|
|----|----|
|Title|Profile&#32;compatibility&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;check&#32;whether&#32;the&#32;test&#32;subject&#32;is&#32;compatible&#32;with&#32;a&#32;profile&#32;or&#32;not,&#32;and&#32;if&#32;it&#32;is&#32;not,&#32;why.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-2)|Identifier|`owl-ql-profile-error`|
|[Section top](#minorfail-outcome-number-2)|Title|OWL&#32;QL&#32;Profile&#32;incompatible|
|[Section top](#minorfail-outcome-number-2)|Description|Statement&#32;not&#32;supported|
|[Section top](#minorfail-outcome-number-2)|Pointer|<pre lang="Turtle"><code>nrv:NormativeRequirement&#32;a&#32;rdfs:Class&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;Normative&#32;Requirement&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;a&#32;requirement&#32;implying,&#32;creating,&#32;or&#32;prescribing&#32;a&#32;norm.&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:subClassOf&#32; &#60;http://docs.oasis-open.org/legalruleml/ns/v1.0/metamodel#DeonticSpecification> &#32;;  &#10; &#32; &#32; &#32; &#32;owl:disjointUnionOf&#32;(&#32;nrv:CompensableRequirement&#32;nrv:NonCompensableRequirement&#32;),  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;(&#32;nrv:ViolableRequirement&#32;nrv:NonViolableRequirement&#32;),  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;(&#32;nrv:PersistentRequirement&#32;nrv:NonPersistentRequirement&#32;)&#32;.</code></pre>|

***
### MinorFail Outcome number 3

[Jump to summary definition](#summary-MinorFail-3)	|	[Previous MinorFail outcome](#minorfail-outcome-number-2)	|	[Next MinorFail outcome](#minorfail-outcome-number-4)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-src-nrv-v1|
|----|----|
|Title|Standalone&#32;module&#32;src/nrv&lowbar;v1.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Module nrv&lowbar;v1](https://github.com/Accord-Project/aec3po/blob/HEAD/src/nrv_v1.ttl)|

#### Criterion detail
|Identifier|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|
|----|----|
|Title|Profile&#32;compatibility&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;check&#32;whether&#32;the&#32;test&#32;subject&#32;is&#32;compatible&#32;with&#32;a&#32;profile&#32;or&#32;not,&#32;and&#32;if&#32;it&#32;is&#32;not,&#32;why.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-3)|Identifier|`owl-rl-profile-error`|
|[Section top](#minorfail-outcome-number-3)|Title|OWL&#32;RL&#32;Profile&#32;incompatible|
|[Section top](#minorfail-outcome-number-3)|Description|Statement&#32;not&#32;supported|
|[Section top](#minorfail-outcome-number-3)|Pointer|<pre lang="Turtle"><code>&#60;http://docs.oasis-open.org/legalruleml/ns/v1.0/metamodel#Obligation> &#32;a&#32;rdfs:Class&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;obligation&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;a&#32;Deontic&#32;Specification&#32;for&#32;a&#32;state,&#32;an&#32;act,&#32;or&#32;a&#32;course&#32;of&#32;...&#34;,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#34;a&#32;situation,&#32;an&#32;act,&#32;or&#32;a&#32;course&#32;of&#32;action(s)&#32;to&#32;which&#32;a&#32;bea...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:subClassOf&#32; &#60;http://docs.oasis-open.org/legalruleml/ns/v1.0/metamodel#DeonticSpecification>,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;nrv:CompensableRequirement,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;nrv:ViolableRequirement&#32;;  &#10; &#32; &#32; &#32; &#32;owl:unionOf&#32;(&#32;nrv:Achievement&#32;nrv:Maintenance&#32;)&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-3)|Pointer|<pre lang="Turtle"><code>nrv:NormativeRequirement&#32;a&#32;rdfs:Class&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;Normative&#32;Requirement&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;a&#32;requirement&#32;implying,&#32;creating,&#32;or&#32;prescribing&#32;a&#32;norm.&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:subClassOf&#32; &#60;http://docs.oasis-open.org/legalruleml/ns/v1.0/metamodel#DeonticSpecification> &#32;;  &#10; &#32; &#32; &#32; &#32;owl:disjointUnionOf&#32;(&#32;nrv:CompensableRequirement&#32;nrv:NonCompensableRequirement&#32;),  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;(&#32;nrv:ViolableRequirement&#32;nrv:NonViolableRequirement&#32;),  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;(&#32;nrv:PersistentRequirement&#32;nrv:NonPersistentRequirement&#32;)&#32;.</code></pre>|

***
### MinorFail Outcome number 4

[Jump to summary definition](#summary-MinorFail-4)	|	[Previous MinorFail outcome](#minorfail-outcome-number-3)	|	Next MinorFail outcome

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-src-nrv-v1|
|----|----|
|Title|Standalone&#32;module&#32;src/nrv&lowbar;v1.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Module nrv&lowbar;v1](https://github.com/Accord-Project/aec3po/blob/HEAD/src/nrv_v1.ttl)|

#### Criterion detail
|Identifier|[term-referencing](https://ns.inria.fr/olivaw#term-referencing)|
|----|----|
|Title|Term&#32;referencing&#32;test|
|Description|A&#32;test&#32;case&#32;from&#32;the&#32;Best&#32;Practices&#32;tests&#32;checking&#32;if&#32;each&#32;term&#32;of&#32;the&#32;test&#32;subject&#32;is&#32;referenced&#32;to&#32;a&#32;module&#32;through&#32;a&#32;rdfs:isDefinedBy&#32;property.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-4)|Identifier|`no-reference-module`|
|[Section top](#minorfail-outcome-number-4)|Title|Term&#32;not&#32;referenced&#32;to&#32;a&#32;module|
|[Section top](#minorfail-outcome-number-4)|Description|Subject&#32;terms&#32;not&#32;linked&#32;to&#32;a&#32;module&#32;by&#32;a&#32;rdfs:isDefinedBy&#32;property|
|[Section top](#minorfail-outcome-number-4)|Pointer|<pre lang="Turtle"><code>:NormativeRequirement&#32;a&#32;rdfs:Class&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;Normative&#32;Requirement&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;a&#32;requirement&#32;implying,&#32;creating,&#32;or&#32;prescribing&#32;a&#32;norm.&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:subClassOf&#32; &#60;http://docs.oasis-open.org/legalruleml/ns/v1.0/metamodel#DeonticSpecification> &#32;;  &#10; &#32; &#32; &#32; &#32;owl:disjointUnionOf&#32;(&#32;:CompensableRequirement&#32;:NonCompensableRequirement&#32;),  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;(&#32;:ViolableRequirement&#32;:NonViolableRequirement&#32;),  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;(&#32;:PersistentRequirement&#32;:NonPersistentRequirement&#32;)&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-4)|Pointer|<pre lang="Turtle"><code>:CompensableRequirement&#32;a&#32;rdfs:Class&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;compensable&#32;requirement&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;a&#32;requirement&#32;that&#32;can&#32;be&#32;compensated.&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:subClassOf&#32;:NormativeRequirement&#32;;  &#10; &#32; &#32; &#32; &#32;owl:disjointWith&#32;:NonCompensableRequirement&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-4)|Pointer|<pre lang="Turtle"><code>:NonCompensableRequirement&#32;a&#32;rdfs:Class&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;non&#32;compensable&#32;requirement&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;a&#32;requirement&#32;that&#32;cannot&#32;be&#32;compensated.&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:subClassOf&#32;:NormativeRequirement&#32;;  &#10; &#32; &#32; &#32; &#32;owl:disjointWith&#32;:CompensableRequirement&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-4)|Pointer|<pre lang="Turtle"><code>:ViolableRequirement&#32;a&#32;rdfs:Class&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;violable&#32;requirement&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;a&#32;requirement&#32;that&#32;can&#32;be&#32;violated.&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:subClassOf&#32;:NormativeRequirement&#32;;  &#10; &#32; &#32; &#32; &#32;owl:disjointWith&#32;:NonViolableRequirement&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-4)|Pointer|<pre lang="Turtle"><code>:NonViolableRequirement&#32;a&#32;rdfs:Class&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;non&#32;violable&#32;requirement&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;a&#32;requirement&#32;that&#32;cannot&#32;be&#32;violated.&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:subClassOf&#32;:NormativeRequirement&#32;;  &#10; &#32; &#32; &#32; &#32;owl:disjointWith&#32;:ViolableRequirement&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-4)|Pointer|<pre lang="Turtle"><code>:PersistentRequirement&#32;a&#32;rdfs:Class&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;persistent&#32;requirement&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;a&#32;requirement&#32;that&#32;needs&#32;to&#32;be&#32;obeyed&#32;for&#32;the&#32;whole&#32;duration...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:subClassOf&#32;:NormativeRequirement&#32;;  &#10; &#32; &#32; &#32; &#32;owl:disjointWith&#32;:NonPersistentRequirement&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-4)|Pointer|<pre lang="Turtle"><code>:NonPersistentRequirement&#32;a&#32;rdfs:Class&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;non&#32;persistent&#32;requirement&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;a&#32;requirement&#32;that&#32;is&#32;in&#32;force&#32;at&#32;a&#32;particular&#32;time&#32;point&#32;on...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:subClassOf&#32;:NormativeRequirement&#32;;  &#10; &#32; &#32; &#32; &#32;owl:disjointWith&#32;:PersistentRequirement&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-4)|Pointer|<pre lang="Turtle"><code>:Achievement&#32;a&#32;rdfs:Class&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;achievement&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;an&#32;obligation&#32;for&#32;which&#32;achieving&#32;the&#32;content&#32;at&#32;least&#32;once&#32;...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:subClassOf&#32; &#60;http://docs.oasis-open.org/legalruleml/ns/v1.0/metamodel#Obligation> &#32;;  &#10; &#32; &#32; &#32; &#32;owl:disjointUnionOf&#32;(&#32;:PreemptiveAchievement&#32;:NonPreemptiveAchievement&#32;),  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;(&#32;:PerdurantAchievement&#32;:NonPerdurantAchievement&#32;)&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-4)|Pointer|<pre lang="Turtle"><code>:Maintenance&#32;a&#32;rdfs:Class&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;maintenance&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;an&#32;obligation&#32;that&#32;needs&#32;to&#32;be&#32;obeyed&#32;for&#32;the&#32;whole&#32;duration...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:subClassOf&#32; &#60;http://docs.oasis-open.org/legalruleml/ns/v1.0/metamodel#Obligation> &#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-4)|Pointer|<pre lang="Turtle"><code>:Compensation&#32;a&#32;rdfs:Class&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;compensation&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;a&#32;set&#32;of&#32;penalties&#32;or&#32;sanctions&#32;imposed&#32;on&#32;the&#32;violator&#32;;&#32;fu...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:subClassOf&#32; &#60;http://docs.oasis-open.org/legalruleml/ns/v1.0/metamodel#Obligation> &#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-4)|Pointer|<pre lang="Turtle"><code>:hasCompensation&#32;a&#32;owl:ObjectProperty&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;has&#32;for&#32;compensation&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;links&#32;a&#32;compensable&#32;requirement&#32;to&#32;a&#32;compensation.&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:domain&#32;:CompensableRequirement&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:range&#32;:Compensation&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-4)|Pointer|<pre lang="Turtle"><code>:CompensatedRequirement&#32;a&#32;rdfs:Class&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;compensated&#32;requirement&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;a&#32;requirement&#32;violated&#32;in&#32;a&#32;state&#32;of&#32;affairs&#32;and&#32;compensated...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:subClassOf&#32;:CompensableRequirement&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-4)|Pointer|<pre lang="Turtle"><code>:hasViolation&#32;a&#32;owl:ObjectProperty&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;has&#32;for&#32;violation&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;links&#32;a&#32;violable&#32;requirement&#32;to&#32;a&#32;violation.&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:domain&#32;:ViolableRequirement&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:range&#32; &#60;http://docs.oasis-open.org/legalruleml/ns/v1.0/metamodel#Violation> &#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-4)|Pointer|<pre lang="Turtle"><code>:ViolatedRequirement&#32;a&#32;rdfs:Class&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;violated&#32;requirement&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;a&#32;requirement&#32;violated&#32;by&#32;a&#32;state&#32;of&#32;affairs.&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:subClassOf&#32;:ViolableRequirement&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-4)|Pointer|<pre lang="Turtle"><code>:hasCompliance&#32;a&#32;owl:ObjectProperty&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;has&#32;for&#32;compliance&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;links&#32;a&#32;violable&#32;requirement&#32;to&#32;compliance.&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:domain&#32;:ViolableRequirement&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:range&#32; &#60;http://docs.oasis-open.org/legalruleml/ns/v1.0/metamodel#Compliance> &#32;;  &#10; &#32; &#32; &#32; &#32;owl:propertyDisjointWith&#32;:hasViolation&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-4)|Pointer|<pre lang="Turtle"><code>:CompliantRequirement&#32;a&#32;rdfs:Class&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;compliant&#32;requirement&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;a&#32;requirement&#32;being&#32;compliant&#32;with&#32;a&#32;state&#32;of&#32;affairs.&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:subClassOf&#32;:ViolableRequirement&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-4)|Pointer|<pre lang="Turtle"><code>:PreemptiveAchievement&#32;a&#32;rdfs:Class&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;preemptive&#32;achievement&#32;requirement&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;an&#32;achievement&#32;requirement&#32;that&#32;can&#32;be&#32;fulfilled&#32;even&#32;before...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:subClassOf&#32;:Achievement&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-4)|Pointer|<pre lang="Turtle"><code>:NonPreemptiveAchievement&#32;a&#32;rdfs:Class&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;non&#32;preemptive&#32;achievement&#32;requirement&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;an&#32;achievement&#32;requirement&#32;that&#32;cannot&#32;be&#32;fulfilled&#32;even&#32;bef...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:subClassOf&#32;:Achievement&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-4)|Pointer|<pre lang="Turtle"><code>:PerdurantAchievement&#32;a&#32;rdfs:Class&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;perdurant&#32;achievement&#32;requirement&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;achievement&#32;requirement&#32;that&#32;persists&#32;after&#32;being&#32;violated.&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:subClassOf&#32;:Achievement&#32;;  &#10; &#32; &#32; &#32; &#32;owl:disjointWith&#32;:NonPerdurantAchievement&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-4)|Pointer|<pre lang="Turtle"><code>:NonPerdurantAchievement&#32;a&#32;rdfs:Class&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;non&#32;perdurant&#32;requirement&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;achievement&#32;requirement&#32;that&#32;does&#32;not&#32;persist&#32;after&#32;being&#32;vi...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:subClassOf&#32;:Achievement&#32;;  &#10; &#32; &#32; &#32; &#32;owl:disjointWith&#32;:PerdurantAchievement&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-4)|Pointer|<pre lang="Turtle"><code>:Punctual&#32;a&#32;rdfs:Class&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;punctual&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;an&#32;obligation&#32;for&#32;which&#32;the&#32;contents&#32;must&#32;be&#32;immediately&#32;ach...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:subClassOf&#32;:NonPersistentRequirement&#32;;  &#10; &#32; &#32; &#32; &#32;owl:disjointUnionOf&#32;(&#32;:CoOccurantPunctual&#32;:NonCoOccurantPunctual&#32;)&#32;;  &#10; &#32; &#32; &#32; &#32;owl:intersectionOf&#32;(&#32;:Achievement&#32;:Maintenance&#32;)&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-4)|Pointer|<pre lang="Turtle"><code>:CoOccurantPunctual&#32;a&#32;rdfs:Class&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;co-occurant&#32;punctual&#32;requirement&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;TODO.&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:subClassOf&#32;:Punctual&#32;;  &#10; &#32; &#32; &#32; &#32;owl:disjointWith&#32;:NonCoOccurantPunctual&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-4)|Pointer|<pre lang="Turtle"><code>:NonCoOccurantPunctual&#32;a&#32;rdfs:Class&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;non&#32;co-occurant&#32;punctual&#32;requirement&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;TODO.&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:subClassOf&#32;:Punctual&#32;;  &#10; &#32; &#32; &#32; &#32;owl:disjointWith&#32;:CoOccurantPunctual&#32;.</code></pre>|

***

</details>

***


# Pass Outcomes

[Jump to statistic summary](#statistic-summary)	|	[Previous section](#minorfail-outcomes)	|	Next section

Here is the chapter related to the Pass outcome

:white_check_mark:9 Pass outcomes

<details>
<summary>Fold/Unfold the 9 summary and details</summary>

## Pass Outcomes Summary

:white_check_mark:9 Pass outcomes

|*Jump*|*Number*|*Status*|*Subject*|*Criterion*|*Title*|*Link*|
|------|--------|--------|---------|-----------|-------|------|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-1">1/9</div>|:white_check_mark:Pass|`module-src-nrv-v1`|[bad-extension-property](https://ns.inria.fr/olivaw#bad-extension-property)|No class subproperty|[Jump](#pass-outcome-number-1)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-2">2/9</div>|:white_check_mark:Pass|`module-src-nrv-v1`|[bad-extension-property](https://ns.inria.fr/olivaw#bad-extension-property)|No property subclass|[Jump](#pass-outcome-number-2)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-3">3/9</div>|:white_check_mark:Pass|`module-src-nrv-v1`|[bad-extension-property](https://ns.inria.fr/olivaw#bad-extension-property)|No subclass of property|[Jump](#pass-outcome-number-3)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-4">4/9</div>|:white_check_mark:Pass|`module-src-nrv-v1`|[bad-extension-property](https://ns.inria.fr/olivaw#bad-extension-property)|No subproperty of class|[Jump](#pass-outcome-number-4)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-5">5/9</div>|:white_check_mark:Pass|`module-src-nrv-v1`|[domain-and-range-referencing](https://ns.inria.fr/olivaw#domain-and-range-referencing)|Domains properly defined|[Jump](#pass-outcome-number-5)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-6">6/9</div>|:white_check_mark:Pass|`module-src-nrv-v1`|[domain-and-range-referencing](https://ns.inria.fr/olivaw#domain-and-range-referencing)|Ranges properly defined|[Jump](#pass-outcome-number-6)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-7">7/9</div>|:white_check_mark:Pass|`module-src-nrv-v1`|[labeled-terms](https://ns.inria.fr/olivaw#labeled-terms)|All terms labeled|[Jump](#pass-outcome-number-7)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-8">8/9</div>|:white_check_mark:Pass|`module-src-nrv-v1`|[owl-rl-constraint](https://ns.inria.fr/olivaw#owl-rl-constraint)|OWL RL consistent|[Jump](#pass-outcome-number-8)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-9">9/9</div>|:white_check_mark:Pass|`module-src-nrv-v1`|[terms-differenciation](https://ns.inria.fr/olivaw#terms-differenciation)|Terms differenciated enough|[Jump](#pass-outcome-number-9)|

***

## Pass Outcomes Details

This subchapter gives more details to the :white_check_mark:Pass outcomes

### Pass Outcome number 1

[Jump to summary definition](#summary-Pass-1)	|	Previous Pass outcome	|	[Next Pass outcome](#pass-outcome-number-2)

:white_check_mark:Pass outcome
#### Subject detail
|Name|module-src-nrv-v1|
|----|----|
|Title|Standalone&#32;module&#32;src/nrv&lowbar;v1.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Module nrv&lowbar;v1](https://github.com/Accord-Project/aec3po/blob/HEAD/src/nrv_v1.ttl)|

#### Criterion detail
|Identifier|[bad-extension-property](https://ns.inria.fr/olivaw#bad-extension-property)|
|----|----|
|Title|Predicate&#32;extension&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;test&#32;the&#32;proper&#32;use&#32;of&#32;predicates&#32;rdfs:subClassOf&#32;and&#32;rdfs:subPropertyOf&#32;on&#32;the&#32;ontology&#32;terms|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-1)|Identifier|`class-subpropertyof`|
|[Section top](#pass-outcome-number-1)|Title|No&#32;class&#32;subproperty|
|[Section top](#pass-outcome-number-1)|Description|No&#32;ontology&#32;class&#32;is&#32;a&#32;subproperty|

***
### Pass Outcome number 2

[Jump to summary definition](#summary-Pass-2)	|	[Previous Pass outcome](#pass-outcome-number-1)	|	[Next Pass outcome](#pass-outcome-number-3)

:white_check_mark:Pass outcome
#### Subject detail
|Name|module-src-nrv-v1|
|----|----|
|Title|Standalone&#32;module&#32;src/nrv&lowbar;v1.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Module nrv&lowbar;v1](https://github.com/Accord-Project/aec3po/blob/HEAD/src/nrv_v1.ttl)|

#### Criterion detail
|Identifier|[bad-extension-property](https://ns.inria.fr/olivaw#bad-extension-property)|
|----|----|
|Title|Predicate&#32;extension&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;test&#32;the&#32;proper&#32;use&#32;of&#32;predicates&#32;rdfs:subClassOf&#32;and&#32;rdfs:subPropertyOf&#32;on&#32;the&#32;ontology&#32;terms|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-2)|Identifier|`property-subclassof`|
|[Section top](#pass-outcome-number-2)|Title|No&#32;property&#32;subclass|
|[Section top](#pass-outcome-number-2)|Description|No&#32;ontology&#32;property&#32;is&#32;a&#32;subclass|

***
### Pass Outcome number 3

[Jump to summary definition](#summary-Pass-3)	|	[Previous Pass outcome](#pass-outcome-number-2)	|	[Next Pass outcome](#pass-outcome-number-4)

:white_check_mark:Pass outcome
#### Subject detail
|Name|module-src-nrv-v1|
|----|----|
|Title|Standalone&#32;module&#32;src/nrv&lowbar;v1.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Module nrv&lowbar;v1](https://github.com/Accord-Project/aec3po/blob/HEAD/src/nrv_v1.ttl)|

#### Criterion detail
|Identifier|[bad-extension-property](https://ns.inria.fr/olivaw#bad-extension-property)|
|----|----|
|Title|Predicate&#32;extension&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;test&#32;the&#32;proper&#32;use&#32;of&#32;predicates&#32;rdfs:subClassOf&#32;and&#32;rdfs:subPropertyOf&#32;on&#32;the&#32;ontology&#32;terms|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-3)|Identifier|`subclassof-property`|
|[Section top](#pass-outcome-number-3)|Title|No&#32;subclass&#32;of&#32;property|
|[Section top](#pass-outcome-number-3)|Description|No&#32;ontology&#32;term&#32;is&#32;a&#32;subclass&#32;of&#32;a&#32;property|

***
### Pass Outcome number 4

[Jump to summary definition](#summary-Pass-4)	|	[Previous Pass outcome](#pass-outcome-number-3)	|	[Next Pass outcome](#pass-outcome-number-5)

:white_check_mark:Pass outcome
#### Subject detail
|Name|module-src-nrv-v1|
|----|----|
|Title|Standalone&#32;module&#32;src/nrv&lowbar;v1.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Module nrv&lowbar;v1](https://github.com/Accord-Project/aec3po/blob/HEAD/src/nrv_v1.ttl)|

#### Criterion detail
|Identifier|[bad-extension-property](https://ns.inria.fr/olivaw#bad-extension-property)|
|----|----|
|Title|Predicate&#32;extension&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;test&#32;the&#32;proper&#32;use&#32;of&#32;predicates&#32;rdfs:subClassOf&#32;and&#32;rdfs:subPropertyOf&#32;on&#32;the&#32;ontology&#32;terms|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-4)|Identifier|`subpropertyof-class`|
|[Section top](#pass-outcome-number-4)|Title|No&#32;subproperty&#32;of&#32;class|
|[Section top](#pass-outcome-number-4)|Description|No&#32;ontology&#32;term&#32;is&#32;a&#32;subproperty&#32;of&#32;a&#32;class|

***
### Pass Outcome number 5

[Jump to summary definition](#summary-Pass-5)	|	[Previous Pass outcome](#pass-outcome-number-4)	|	[Next Pass outcome](#pass-outcome-number-6)

:white_check_mark:Pass outcome
#### Subject detail
|Name|module-src-nrv-v1|
|----|----|
|Title|Standalone&#32;module&#32;src/nrv&lowbar;v1.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Module nrv&lowbar;v1](https://github.com/Accord-Project/aec3po/blob/HEAD/src/nrv_v1.ttl)|

#### Criterion detail
|Identifier|[domain-and-range-referencing](https://ns.inria.fr/olivaw#domain-and-range-referencing)|
|----|----|
|Title|Domain&#32;and&#32;range&#32;referencing&#32;test|
|Description|A&#32;test&#32;case&#32;from&#32;the&#32;Best&#32;Practices&#32;tests&#32;checking&#32;if&#32;all&#32;the&#32;ranges&#32;and&#32;domains&#32;from&#32;the&#32;test&#32;subject&#32;point&#32;to&#32;terms&#32;that&#32;are&#32;defined&#32;in&#32;the&#32;vocabulary.|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-5)|Identifier|`domain-out-of-vocabulary`|
|[Section top](#pass-outcome-number-5)|Title|Domains&#32;properly&#32;defined|
|[Section top](#pass-outcome-number-5)|Description|Each&#32;rdfs:domain&#32;is&#32;defined&#32;within&#32;the&#32;fragment|

***
### Pass Outcome number 6

[Jump to summary definition](#summary-Pass-6)	|	[Previous Pass outcome](#pass-outcome-number-5)	|	[Next Pass outcome](#pass-outcome-number-7)

:white_check_mark:Pass outcome
#### Subject detail
|Name|module-src-nrv-v1|
|----|----|
|Title|Standalone&#32;module&#32;src/nrv&lowbar;v1.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Module nrv&lowbar;v1](https://github.com/Accord-Project/aec3po/blob/HEAD/src/nrv_v1.ttl)|

#### Criterion detail
|Identifier|[domain-and-range-referencing](https://ns.inria.fr/olivaw#domain-and-range-referencing)|
|----|----|
|Title|Domain&#32;and&#32;range&#32;referencing&#32;test|
|Description|A&#32;test&#32;case&#32;from&#32;the&#32;Best&#32;Practices&#32;tests&#32;checking&#32;if&#32;all&#32;the&#32;ranges&#32;and&#32;domains&#32;from&#32;the&#32;test&#32;subject&#32;point&#32;to&#32;terms&#32;that&#32;are&#32;defined&#32;in&#32;the&#32;vocabulary.|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-6)|Identifier|`range-out-of-vocabulary`|
|[Section top](#pass-outcome-number-6)|Title|Ranges&#32;properly&#32;defined|
|[Section top](#pass-outcome-number-6)|Description|Each&#32;rdfs:range&#32;is&#32;defined&#32;within&#32;the&#32;fragment|

***
### Pass Outcome number 7

[Jump to summary definition](#summary-Pass-7)	|	[Previous Pass outcome](#pass-outcome-number-6)	|	[Next Pass outcome](#pass-outcome-number-8)

:white_check_mark:Pass outcome
#### Subject detail
|Name|module-src-nrv-v1|
|----|----|
|Title|Standalone&#32;module&#32;src/nrv&lowbar;v1.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Module nrv&lowbar;v1](https://github.com/Accord-Project/aec3po/blob/HEAD/src/nrv_v1.ttl)|

#### Criterion detail
|Identifier|[labeled-terms](https://ns.inria.fr/olivaw#labeled-terms)|
|----|----|
|Title|Term&#32;labeling&#32;test|
|Description|A&#32;test&#32;case&#32;from&#32;the&#32;Best&#32;Practices&#32;tests&#32;checking&#32;if&#32;all&#32;the&#32;terms&#32;of&#32;the&#32;subject&#32;have&#32;a&#32;rdfs:label&#32;property&#32;pointing&#32;to&#32;a&#32;literal&#32;in&#32;English|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-7)|Identifier|`not-labeled-term`|
|[Section top](#pass-outcome-number-7)|Title|All&#32;terms&#32;labeled|
|[Section top](#pass-outcome-number-7)|Description|All&#32;the&#32;terms&#32;defined&#32;in&#32;the&#32;subject&#32;have&#32;a&#32;rdfs:label&#32;in&#32;English|

***
### Pass Outcome number 8

[Jump to summary definition](#summary-Pass-8)	|	[Previous Pass outcome](#pass-outcome-number-7)	|	[Next Pass outcome](#pass-outcome-number-9)

:white_check_mark:Pass outcome
#### Subject detail
|Name|module-src-nrv-v1|
|----|----|
|Title|Standalone&#32;module&#32;src/nrv&lowbar;v1.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Module nrv&lowbar;v1](https://github.com/Accord-Project/aec3po/blob/HEAD/src/nrv_v1.ttl)|

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

[Jump to summary definition](#summary-Pass-9)	|	[Previous Pass outcome](#pass-outcome-number-8)	|	Next Pass outcome

:white_check_mark:Pass outcome
#### Subject detail
|Name|module-src-nrv-v1|
|----|----|
|Title|Standalone&#32;module&#32;src/nrv&lowbar;v1.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Module nrv&lowbar;v1](https://github.com/Accord-Project/aec3po/blob/HEAD/src/nrv_v1.ttl)|

#### Criterion detail
|Identifier|[terms-differenciation](https://ns.inria.fr/olivaw#terms-differenciation)|
|----|----|
|Title|Terms&#32;differenciation&#32;test|
|Description|A&#32;test&#32;case&#32;from&#32;the&#32;Best&#32;Practices&#32;tests&#32;checking&#32;if&#32;all&#32;the&#32;terms&#32;are&#32;different&#32;enough&#32;from&#32;each&#32;other&#32;according&#32;to&#32;the&#32;Levenshtein&#32;distance&#32;metric.|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-9)|Identifier|`too-close-terms`|
|[Section top](#pass-outcome-number-9)|Title|Terms&#32;differenciated&#32;enough|
|[Section top](#pass-outcome-number-9)|Description|All&#32;the&#32;terms&#32;have&#32;have&#32;a&#32;satisfying&#32;Levenshtein&#32;distance&#32;from&#32;each&#32;other&#32;term.|

***

</details>

***
