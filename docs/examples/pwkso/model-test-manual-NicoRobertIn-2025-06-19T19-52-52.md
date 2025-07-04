# Test Report Markdown Export

This file is an export of the RDF test report made out of [EARL vocabulary](https://www.w3.org/TR/EARL10/)

This test is powered by Corese, check [Corese website](https://project.inria.fr/corese/) and [Corese repository](https://github.com/Wimmics/corese)

The original test report is available in turtle syntax [here](./model-test-manual-NicoRobertIn-2025-06-19T19-52-52.ttl).

# Test Activity

Here is some information about the testing activity that led to this report

|Title|Model&#32;tests&#32;of&#32;[acimov-tools/model-test](https://github.com/acimov-tools/model-test)&#32;on&#32;branch&#32;main|
|--|--|
|Description|[NicoRobertIn](https://github.com/NicoRobertIn)&#32;launch&#32;manual&#32;run&#32;of&#32;model&#32;tests&#32;against&#32;[acimov-tools/model-test](https://github.com/acimov-tools/model-test)&#32;on&#32;branch&#32;main|
|Tester|[NicoRobertIn](https://github.com/NicoRobertIn)|
|Ontology|[acimov-tools/model-test](https://github.com/acimov-tools/model-test)|
|Ontology version|Local state `d395c4bec5f5370cedb0fdb75dfe665bbc4e2c2e`|
|Ontology version date|2025-06-19 19:52:51|
|Ontology previous version|[2d2b197be6d9148e48186fc86072618c89134cc9](https://github.com/acimov-tools/model-test/tree/2d2b197be6d9148e48186fc86072618c89134cc9)|
|Ontology branch|[main](https://github.com/acimov-tools/model-test/tree/main)|
|Olivaw suite|[olivaw model test suite](https://github.com/Wimmics/olivaw/blob/v0.0.8/olivaw/test/model/suite.py)|
|Olivaw version|[v0.0.8](https://pypi.org/project/olivaw/0.0.8)|
|Generated turtle|[Turtle report](./model-test-manual-NicoRobertIn-2025-06-19T19-52-52.ttl)|
|Generated Markdown|[Markdown report](./model-test-manual-NicoRobertIn-2025-06-19T19-52-52.md)|

# Statistic summary

Here is a short overview for this test report

16 Outcomes

:boom:0 MajorFail, :exclamation:7 MinorFail, :warning:0 CannotTell, :grey_question:0 NotTested, :white_check_mark:9 Pass

<div  style="border-radius: 12px; height: 25px; overflow: hidden"><img src="../assets/red.png" width="0%" height="25px"/><img src="../assets/orange.png" width="43%" height="25px"/><img src="../assets/grey.png" width="0%" height="25px"/><img src="../assets/white.png" width="0%" height="25px"/><img src="../assets/green.png" width="57%" height="25px"/></div>

<br/>

The different status types are an extension of the [EARL](https://www.w3.org/TR/EARL10-Schema/) vocabulary where the nextended terms can be found in the [olivaw ontology](https://ns.inria.fr/olivaw#), each outcome type means:
* :boom: MajorFail: This is an error that is critical and considered as blocking for production
* :exclamation: MinorFail: This is an error that should be fixed, but it cannot be considered as critical error
* :warning: CannotTell: It is unclear if the subject passed or failed the test. This happens when an automated test requires human judgement to make a final decision.
* :grey_question: NotTested:  The test has not been carried out. It is because some prerequisite tests did not end up as Pass.
* :white_check_mark: Pass: The subject passed the test.

***


# MinorFail Outcomes

[Jump to statistic summary](#statistic-summary)	|	Previous section	|	[Next section](#pass-outcomes)

Here is the chapter related to the MinorFail outcome

:exclamation:7 MinorFail outcomes

<details>
<summary>Fold/Unfold the 7 summary and details</summary>

## MinorFail Outcomes Summary

:exclamation:7 MinorFail outcomes

|*Jump*|*Number*|*Status*|*Subject*|*Criterion*|*Title*|*Link*|
|------|--------|--------|---------|-----------|-------|------|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-1">1/7</div>|:exclamation:MinorFail|`module-pwkso`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL EL Profile incompatible|[Jump](#minorfail-outcome-number-1)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-2">2/7</div>|:exclamation:MinorFail|`module-pwkso`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL EL Profile incompatible|[Jump](#minorfail-outcome-number-2)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-3">3/7</div>|:exclamation:MinorFail|`module-pwkso`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL QL Profile incompatible|[Jump](#minorfail-outcome-number-3)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-4">4/7</div>|:exclamation:MinorFail|`module-pwkso`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL QL Profile incompatible|[Jump](#minorfail-outcome-number-4)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-5">5/7</div>|:exclamation:MinorFail|`module-pwkso`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL RL Profile incompatible|[Jump](#minorfail-outcome-number-5)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-6">6/7</div>|:exclamation:MinorFail|`module-pwkso`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL RL Profile incompatible|[Jump](#minorfail-outcome-number-6)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-7">7/7</div>|:exclamation:MinorFail|`module-pwkso`|[term-referencing](https://ns.inria.fr/olivaw#term-referencing)|Term not referenced to a module|[Jump](#minorfail-outcome-number-7)|

***

## MinorFail Outcomes Details

This subchapter gives more details to the :exclamation:MinorFail outcomes

### MinorFail Outcome number 1

[Jump to summary definition](#summary-MinorFail-1)	|	Previous MinorFail outcome	|	[Next MinorFail outcome](#minorfail-outcome-number-2)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-pwkso|
|----|----|
|Title|Standalone&#32;module&#32;src&#92;pwkso.ttl&#32;from&#32;branch&#32;main|
|Composition|- [Module pwkso](https://github.com/acimov-tools/model-test/blob/main/src/pwkso.ttl)|

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
|[Section top](#minorfail-outcome-number-1)|Description|Class&#32;Expression&#32;not&#32;supported&#32;with&#32;rdfs:subClassOf|
|[Section top](#minorfail-outcome-number-1)|Pointer|<pre lang="Turtle"><code>pwkso:BinaryKripkeRelation&#32;rdfs:label&#32; &#34;binary&#32;Kripke&#32;relation&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;relation&#32;that&#32;links&#32;a&#32;possible&#32;world&#32;with&#32;another&#32;to&#32;represe...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:subClassOf&#32; &#91;&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:onProperty&#32;pwkso:param&#32;],  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;pwkso:KripkeRelation&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-1)|Pointer|<pre lang="Turtle"><code>pwkso:UnaryKripkeRelation&#32;rdfs:label&#32; &#34;unary&#32;Kripke&#32;relation&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;relation&#32;that&#32;links&#32;a&#32;possible&#32;world&#32;with&#32;another&#32;to&#32;represe...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:subClassOf&#32; &#91;&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:onProperty&#32;pwkso:param&#32;],  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;pwkso:KripkeRelation&#32;.</code></pre>|

***
### MinorFail Outcome number 2

[Jump to summary definition](#summary-MinorFail-2)	|	[Previous MinorFail outcome](#minorfail-outcome-number-1)	|	[Next MinorFail outcome](#minorfail-outcome-number-3)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-pwkso|
|----|----|
|Title|Standalone&#32;module&#32;src&#92;pwkso.ttl&#32;from&#32;branch&#32;main|
|Composition|- [Module pwkso](https://github.com/acimov-tools/model-test/blob/main/src/pwkso.ttl)|

#### Criterion detail
|Identifier|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|
|----|----|
|Title|Profile&#32;compatibility&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;check&#32;whether&#32;the&#32;test&#32;subject&#32;is&#32;compatible&#32;with&#32;a&#32;profile&#32;or&#32;not,&#32;and&#32;if&#32;it&#32;is&#32;not,&#32;why.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-2)|Identifier|`owl-el-profile-error`|
|[Section top](#minorfail-outcome-number-2)|Title|OWL&#32;EL&#32;Profile&#32;incompatible|
|[Section top](#minorfail-outcome-number-2)|Description|Statement&#32;not&#32;supported&#32;in&#32;a&#32;Class&#32;Expression|
|[Section top](#minorfail-outcome-number-2)|Pointer|<pre lang="Turtle"><code>&#91;]&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32;&#32; &#32;owl:onProperty&#32;pwkso:param&#32;.</code></pre>|

***
### MinorFail Outcome number 3

[Jump to summary definition](#summary-MinorFail-3)	|	[Previous MinorFail outcome](#minorfail-outcome-number-2)	|	[Next MinorFail outcome](#minorfail-outcome-number-4)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-pwkso|
|----|----|
|Title|Standalone&#32;module&#32;src&#92;pwkso.ttl&#32;from&#32;branch&#32;main|
|Composition|- [Module pwkso](https://github.com/acimov-tools/model-test/blob/main/src/pwkso.ttl)|

#### Criterion detail
|Identifier|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|
|----|----|
|Title|Profile&#32;compatibility&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;check&#32;whether&#32;the&#32;test&#32;subject&#32;is&#32;compatible&#32;with&#32;a&#32;profile&#32;or&#32;not,&#32;and&#32;if&#32;it&#32;is&#32;not,&#32;why.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-3)|Identifier|`owl-ql-profile-error`|
|[Section top](#minorfail-outcome-number-3)|Title|OWL&#32;QL&#32;Profile&#32;incompatible|
|[Section top](#minorfail-outcome-number-3)|Description|Class&#32;Expression&#32;not&#32;supported&#32;with&#32;rdfs:subClassOf|
|[Section top](#minorfail-outcome-number-3)|Pointer|<pre lang="Turtle"><code>pwkso:BinaryKripkeRelation&#32;rdfs:label&#32; &#34;binary&#32;Kripke&#32;relation&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;relation&#32;that&#32;links&#32;a&#32;possible&#32;world&#32;with&#32;another&#32;to&#32;represe...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:subClassOf&#32; &#91;&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:onProperty&#32;pwkso:param&#32;],  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;pwkso:KripkeRelation&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-3)|Pointer|<pre lang="Turtle"><code>pwkso:UnaryKripkeRelation&#32;rdfs:label&#32; &#34;unary&#32;Kripke&#32;relation&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;relation&#32;that&#32;links&#32;a&#32;possible&#32;world&#32;with&#32;another&#32;to&#32;represe...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:subClassOf&#32; &#91;&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:onProperty&#32;pwkso:param&#32;],  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;pwkso:KripkeRelation&#32;.</code></pre>|

***
### MinorFail Outcome number 4

[Jump to summary definition](#summary-MinorFail-4)	|	[Previous MinorFail outcome](#minorfail-outcome-number-3)	|	[Next MinorFail outcome](#minorfail-outcome-number-5)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-pwkso|
|----|----|
|Title|Standalone&#32;module&#32;src&#92;pwkso.ttl&#32;from&#32;branch&#32;main|
|Composition|- [Module pwkso](https://github.com/acimov-tools/model-test/blob/main/src/pwkso.ttl)|

#### Criterion detail
|Identifier|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|
|----|----|
|Title|Profile&#32;compatibility&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;check&#32;whether&#32;the&#32;test&#32;subject&#32;is&#32;compatible&#32;with&#32;a&#32;profile&#32;or&#32;not,&#32;and&#32;if&#32;it&#32;is&#32;not,&#32;why.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-4)|Identifier|`owl-ql-profile-error`|
|[Section top](#minorfail-outcome-number-4)|Title|OWL&#32;QL&#32;Profile&#32;incompatible|
|[Section top](#minorfail-outcome-number-4)|Description|Statement&#32;not&#32;supported&#32;in&#32;a&#32;Super&#32;Class&#32;Expression|
|[Section top](#minorfail-outcome-number-4)|Pointer|<pre lang="Turtle"><code>&#91;]&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32;&#32; &#32;owl:onProperty&#32;pwkso:param&#32;.</code></pre>|

***
### MinorFail Outcome number 5

[Jump to summary definition](#summary-MinorFail-5)	|	[Previous MinorFail outcome](#minorfail-outcome-number-4)	|	[Next MinorFail outcome](#minorfail-outcome-number-6)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-pwkso|
|----|----|
|Title|Standalone&#32;module&#32;src&#92;pwkso.ttl&#32;from&#32;branch&#32;main|
|Composition|- [Module pwkso](https://github.com/acimov-tools/model-test/blob/main/src/pwkso.ttl)|

#### Criterion detail
|Identifier|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|
|----|----|
|Title|Profile&#32;compatibility&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;check&#32;whether&#32;the&#32;test&#32;subject&#32;is&#32;compatible&#32;with&#32;a&#32;profile&#32;or&#32;not,&#32;and&#32;if&#32;it&#32;is&#32;not,&#32;why.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-5)|Identifier|`owl-rl-profile-error`|
|[Section top](#minorfail-outcome-number-5)|Title|OWL&#32;RL&#32;Profile&#32;incompatible|
|[Section top](#minorfail-outcome-number-5)|Description|Class&#32;Expression&#32;not&#32;supported&#32;with&#32;rdfs:subClassOf|
|[Section top](#minorfail-outcome-number-5)|Pointer|<pre lang="Turtle"><code>pwkso:BinaryKripkeRelation&#32;rdfs:label&#32; &#34;binary&#32;Kripke&#32;relation&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;relation&#32;that&#32;links&#32;a&#32;possible&#32;world&#32;with&#32;another&#32;to&#32;represe...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:subClassOf&#32; &#91;&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:onProperty&#32;pwkso:param&#32;],  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;pwkso:KripkeRelation&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-5)|Pointer|<pre lang="Turtle"><code>pwkso:UnaryKripkeRelation&#32;rdfs:label&#32; &#34;unary&#32;Kripke&#32;relation&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;relation&#32;that&#32;links&#32;a&#32;possible&#32;world&#32;with&#32;another&#32;to&#32;represe...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:subClassOf&#32; &#91;&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:onProperty&#32;pwkso:param&#32;],  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;pwkso:KripkeRelation&#32;.</code></pre>|

***
### MinorFail Outcome number 6

[Jump to summary definition](#summary-MinorFail-6)	|	[Previous MinorFail outcome](#minorfail-outcome-number-5)	|	[Next MinorFail outcome](#minorfail-outcome-number-7)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-pwkso|
|----|----|
|Title|Standalone&#32;module&#32;src&#92;pwkso.ttl&#32;from&#32;branch&#32;main|
|Composition|- [Module pwkso](https://github.com/acimov-tools/model-test/blob/main/src/pwkso.ttl)|

#### Criterion detail
|Identifier|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|
|----|----|
|Title|Profile&#32;compatibility&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;check&#32;whether&#32;the&#32;test&#32;subject&#32;is&#32;compatible&#32;with&#32;a&#32;profile&#32;or&#32;not,&#32;and&#32;if&#32;it&#32;is&#32;not,&#32;why.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-6)|Identifier|`owl-rl-profile-error`|
|[Section top](#minorfail-outcome-number-6)|Title|OWL&#32;RL&#32;Profile&#32;incompatible|
|[Section top](#minorfail-outcome-number-6)|Description|Statement&#32;not&#32;supported&#32;in&#32;a&#32;Super&#32;Class&#32;Expression|
|[Section top](#minorfail-outcome-number-6)|Pointer|<pre lang="Turtle"><code>&#91;]&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32;&#32; &#32;owl:onProperty&#32;pwkso:param&#32;.</code></pre>|

***
### MinorFail Outcome number 7

[Jump to summary definition](#summary-MinorFail-7)	|	[Previous MinorFail outcome](#minorfail-outcome-number-6)	|	Next MinorFail outcome

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-pwkso|
|----|----|
|Title|Standalone&#32;module&#32;src&#92;pwkso.ttl&#32;from&#32;branch&#32;main|
|Composition|- [Module pwkso](https://github.com/acimov-tools/model-test/blob/main/src/pwkso.ttl)|

#### Criterion detail
|Identifier|[term-referencing](https://ns.inria.fr/olivaw#term-referencing)|
|----|----|
|Title|Term&#32;referencing&#32;test|
|Description|A&#32;test&#32;case&#32;from&#32;the&#32;Best&#32;Practices&#32;tests&#32;checking&#32;if&#32;each&#32;term&#32;of&#32;the&#32;test&#32;subject&#32;is&#32;referenced&#32;to&#32;a&#32;module&#32;through&#32;a&#32;rdfs:isDefinedBy&#32;property.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-7)|Identifier|`no-reference-module`|
|[Section top](#minorfail-outcome-number-7)|Title|Term&#32;not&#32;referenced&#32;to&#32;a&#32;module|
|[Section top](#minorfail-outcome-number-7)|Description|Subject&#32;terms&#32;not&#32;linked&#32;to&#32;a&#32;module&#32;by&#32;a&#32;rdfs:isDefinedBy&#32;property|
|[Section top](#minorfail-outcome-number-7)|Pointer|<pre lang="Turtle"><code>:PossibleWorld&#32;a&#32;owl:Class&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;possible&#32;world&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;a&#32;consistent&#32;representation&#32;of&#32;how&#32;the&#32;world&#32;is,&#32;could&#32;have&#32;...&#34; &#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-7)|Pointer|<pre lang="Turtle"><code>:verifiedIn&#32;a&#32;owl:ObjectProperty&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;verified&#32;in&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;links&#32;triples&#32;to&#32;a&#32;possible&#32;world&#32;in&#32;which&#32;their&#32;associated&#32;...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:range&#32;:PossibleWorld&#32;;  &#10; &#32; &#32; &#32; &#32;owl:propertyDisjointWith&#32;:notVerifiedIn&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-7)|Pointer|<pre lang="Turtle"><code>:notVerifiedIn&#32;a&#32;owl:ObjectProperty&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;not&#32;verified&#32;in&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;links&#32;triples&#32;to&#32;a&#32;possible&#32;world&#32;in&#32;which&#32;associated&#32;formul...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:range&#32;:PossibleWorld&#32;;  &#10; &#32; &#32; &#32; &#32;owl:propertyDisjointWith&#32;:verifiedIn&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-7)|Pointer|<pre lang="Turtle"><code>:ClosedPossibleWorld&#32;a&#32;owl:Class&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;closed&#32;possible&#32;world&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;represents&#32;a&#32;possible&#32;world&#32;with&#32;the&#32;Closed-World&#32;Assumption&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:subClassOf&#32;:PossibleWorld&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-7)|Pointer|<pre lang="Turtle"><code>:OpenPossibleWorld&#32;a&#32;owl:Class&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;open&#32;possible&#32;world&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;represents&#32;a&#32;possible&#32;world&#32;with&#32;the&#32;Open-World&#32;Assumption&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:subClassOf&#32;:PossibleWorld&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-7)|Pointer|<pre lang="Turtle"><code>:KripkeRelation&#32;a&#32;owl:Class&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;Kripke&#32;relation&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;represents&#32;the&#32;Kripke&#32;relations&#32;between&#32;possible&#32;worlds.&#32;Ins...&#34; &#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-7)|Pointer|<pre lang="Turtle"><code>:param&#32;a&#32;owl:ObjectProperty&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;parameter&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;parameter&#32;of&#32;a&#32;Kripke&#32;relation&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:domain&#32;:KripkeRelation&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:range&#32;:PossibleWorld&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-7)|Pointer|<pre lang="Turtle"><code>:index&#32;a&#32;owl:ObjectProperty&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;index&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;index&#32;of&#32;a&#32;Kripke&#32;relation&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:domain&#32;:KripkeRelation&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-7)|Pointer|<pre lang="Turtle"><code>:hasRelation&#32;a&#32;owl:ObjectProperty&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;has&#32;relation&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;links&#32;a&#32;possible&#32;world&#32;to&#32;one&#32;of&#32;its&#32;N-ary&#32;relations&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:domain&#32;:PossibleWorld&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:range&#32;:KripkeRelation&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-7)|Pointer|<pre lang="Turtle"><code>:BinaryKripkeRelation&#32;rdfs:label&#32; &#34;binary&#32;Kripke&#32;relation&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;relation&#32;that&#32;links&#32;a&#32;possible&#32;world&#32;with&#32;another&#32;to&#32;represe...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:subClassOf&#32; &#91;&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:onProperty&#32;:param&#32;],  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;:KripkeRelation&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-7)|Pointer|<pre lang="Turtle"><code>:UnaryKripkeRelation&#32;rdfs:label&#32; &#34;unary&#32;Kripke&#32;relation&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;relation&#32;that&#32;links&#32;a&#32;possible&#32;world&#32;with&#32;another&#32;to&#32;represe...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:subClassOf&#32; &#91;&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:onProperty&#32;:param&#32;],  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;:KripkeRelation&#32;.</code></pre>|

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
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-1">1/9</div>|:white_check_mark:Pass|`module-pwkso`|[domain-and-range-referencing](https://ns.inria.fr/olivaw#domain-and-range-referencing)|Domains properly defined|[Jump](#pass-outcome-number-1)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-2">2/9</div>|:white_check_mark:Pass|`module-pwkso`|[domain-and-range-referencing](https://ns.inria.fr/olivaw#domain-and-range-referencing)|Ranges properly defined|[Jump](#pass-outcome-number-2)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-3">3/9</div>|:white_check_mark:Pass|`module-pwkso`|[labeled-terms](https://ns.inria.fr/olivaw#labeled-terms)|All terms labeled|[Jump](#pass-outcome-number-3)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-4">4/9</div>|:white_check_mark:Pass|`module-pwkso`|[owl-rl-constraint](https://ns.inria.fr/olivaw#owl-rl-constraint)|OWL RL consistent|[Jump](#pass-outcome-number-4)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-5">5/9</div>|:white_check_mark:Pass|`module-pwkso`|[proper-extension-predicate](https://ns.inria.fr/olivaw#proper-extension-predicate)|No class subproperty|[Jump](#pass-outcome-number-5)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-6">6/9</div>|:white_check_mark:Pass|`module-pwkso`|[proper-extension-predicate](https://ns.inria.fr/olivaw#proper-extension-predicate)|No property subclass|[Jump](#pass-outcome-number-6)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-7">7/9</div>|:white_check_mark:Pass|`module-pwkso`|[proper-extension-predicate](https://ns.inria.fr/olivaw#proper-extension-predicate)|No subclass of property|[Jump](#pass-outcome-number-7)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-8">8/9</div>|:white_check_mark:Pass|`module-pwkso`|[proper-extension-predicate](https://ns.inria.fr/olivaw#proper-extension-predicate)|No subproperty of class|[Jump](#pass-outcome-number-8)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-9">9/9</div>|:white_check_mark:Pass|`module-pwkso`|[terms-differenciation](https://ns.inria.fr/olivaw#terms-differenciation)|Terms differenciated enough|[Jump](#pass-outcome-number-9)|

***

## Pass Outcomes Details

This subchapter gives more details to the :white_check_mark:Pass outcomes

### Pass Outcome number 1

[Jump to summary definition](#summary-Pass-1)	|	Previous Pass outcome	|	[Next Pass outcome](#pass-outcome-number-2)

:white_check_mark:Pass outcome
#### Subject detail
|Name|module-pwkso|
|----|----|
|Title|Standalone&#32;module&#32;src&#92;pwkso.ttl&#32;from&#32;branch&#32;main|
|Composition|- [Module pwkso](https://github.com/acimov-tools/model-test/blob/main/src/pwkso.ttl)|

#### Criterion detail
|Identifier|[domain-and-range-referencing](https://ns.inria.fr/olivaw#domain-and-range-referencing)|
|----|----|
|Title|Domain&#32;and&#32;range&#32;referencing&#32;test|
|Description|A&#32;test&#32;case&#32;from&#32;the&#32;Best&#32;Practices&#32;tests&#32;checking&#32;if&#32;all&#32;the&#32;ranges&#32;and&#32;domains&#32;from&#32;the&#32;test&#32;subject&#32;point&#32;to&#32;terms&#32;that&#32;are&#32;defined&#32;in&#32;the&#32;vocabulary.|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-1)|Identifier|`domain-out-of-vocabulary`|
|[Section top](#pass-outcome-number-1)|Title|Domains&#32;properly&#32;defined|
|[Section top](#pass-outcome-number-1)|Description|Each&#32;rdfs:domain&#32;is&#32;defined&#32;within&#32;the&#32;fragment|

***
### Pass Outcome number 2

[Jump to summary definition](#summary-Pass-2)	|	[Previous Pass outcome](#pass-outcome-number-1)	|	[Next Pass outcome](#pass-outcome-number-3)

:white_check_mark:Pass outcome
#### Subject detail
|Name|module-pwkso|
|----|----|
|Title|Standalone&#32;module&#32;src&#92;pwkso.ttl&#32;from&#32;branch&#32;main|
|Composition|- [Module pwkso](https://github.com/acimov-tools/model-test/blob/main/src/pwkso.ttl)|

#### Criterion detail
|Identifier|[domain-and-range-referencing](https://ns.inria.fr/olivaw#domain-and-range-referencing)|
|----|----|
|Title|Domain&#32;and&#32;range&#32;referencing&#32;test|
|Description|A&#32;test&#32;case&#32;from&#32;the&#32;Best&#32;Practices&#32;tests&#32;checking&#32;if&#32;all&#32;the&#32;ranges&#32;and&#32;domains&#32;from&#32;the&#32;test&#32;subject&#32;point&#32;to&#32;terms&#32;that&#32;are&#32;defined&#32;in&#32;the&#32;vocabulary.|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-2)|Identifier|`range-out-of-vocabulary`|
|[Section top](#pass-outcome-number-2)|Title|Ranges&#32;properly&#32;defined|
|[Section top](#pass-outcome-number-2)|Description|Each&#32;rdfs:range&#32;is&#32;defined&#32;within&#32;the&#32;fragment|

***
### Pass Outcome number 3

[Jump to summary definition](#summary-Pass-3)	|	[Previous Pass outcome](#pass-outcome-number-2)	|	[Next Pass outcome](#pass-outcome-number-4)

:white_check_mark:Pass outcome
#### Subject detail
|Name|module-pwkso|
|----|----|
|Title|Standalone&#32;module&#32;src&#92;pwkso.ttl&#32;from&#32;branch&#32;main|
|Composition|- [Module pwkso](https://github.com/acimov-tools/model-test/blob/main/src/pwkso.ttl)|

#### Criterion detail
|Identifier|[labeled-terms](https://ns.inria.fr/olivaw#labeled-terms)|
|----|----|
|Title|Term&#32;labeling&#32;test|
|Description|A&#32;test&#32;case&#32;from&#32;the&#32;Best&#32;Practices&#32;tests&#32;checking&#32;if&#32;all&#32;the&#32;terms&#32;of&#32;the&#32;subject&#32;have&#32;a&#32;rdfs:label&#32;property&#32;pointing&#32;to&#32;a&#32;literal&#32;in&#32;English|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-3)|Identifier|`not-labeled-term`|
|[Section top](#pass-outcome-number-3)|Title|All&#32;terms&#32;labeled|
|[Section top](#pass-outcome-number-3)|Description|All&#32;the&#32;terms&#32;defined&#32;in&#32;the&#32;subject&#32;have&#32;a&#32;rdfs:label&#32;in&#32;English|

***
### Pass Outcome number 4

[Jump to summary definition](#summary-Pass-4)	|	[Previous Pass outcome](#pass-outcome-number-3)	|	[Next Pass outcome](#pass-outcome-number-5)

:white_check_mark:Pass outcome
#### Subject detail
|Name|module-pwkso|
|----|----|
|Title|Standalone&#32;module&#32;src&#92;pwkso.ttl&#32;from&#32;branch&#32;main|
|Composition|- [Module pwkso](https://github.com/acimov-tools/model-test/blob/main/src/pwkso.ttl)|

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
|Name|module-pwkso|
|----|----|
|Title|Standalone&#32;module&#32;src&#92;pwkso.ttl&#32;from&#32;branch&#32;main|
|Composition|- [Module pwkso](https://github.com/acimov-tools/model-test/blob/main/src/pwkso.ttl)|

#### Criterion detail
|Identifier|[proper-extension-predicate](https://ns.inria.fr/olivaw#proper-extension-predicate)|
|----|----|
|Title|Predicate&#32;extension&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;test&#32;the&#32;proper&#32;use&#32;of&#32;predicates&#32;rdfs:subClassOf&#32;and&#32;rdfs:subPropertyOf&#32;on&#32;the&#32;ontology&#32;terms|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-5)|Identifier|`class-subpropertyof`|
|[Section top](#pass-outcome-number-5)|Title|No&#32;class&#32;subproperty|
|[Section top](#pass-outcome-number-5)|Description|No&#32;ontology&#32;class&#32;is&#32;a&#32;subproperty|

***
### Pass Outcome number 6

[Jump to summary definition](#summary-Pass-6)	|	[Previous Pass outcome](#pass-outcome-number-5)	|	[Next Pass outcome](#pass-outcome-number-7)

:white_check_mark:Pass outcome
#### Subject detail
|Name|module-pwkso|
|----|----|
|Title|Standalone&#32;module&#32;src&#92;pwkso.ttl&#32;from&#32;branch&#32;main|
|Composition|- [Module pwkso](https://github.com/acimov-tools/model-test/blob/main/src/pwkso.ttl)|

#### Criterion detail
|Identifier|[proper-extension-predicate](https://ns.inria.fr/olivaw#proper-extension-predicate)|
|----|----|
|Title|Predicate&#32;extension&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;test&#32;the&#32;proper&#32;use&#32;of&#32;predicates&#32;rdfs:subClassOf&#32;and&#32;rdfs:subPropertyOf&#32;on&#32;the&#32;ontology&#32;terms|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-6)|Identifier|`property-subclassof`|
|[Section top](#pass-outcome-number-6)|Title|No&#32;property&#32;subclass|
|[Section top](#pass-outcome-number-6)|Description|No&#32;ontology&#32;property&#32;is&#32;a&#32;subclass|

***
### Pass Outcome number 7

[Jump to summary definition](#summary-Pass-7)	|	[Previous Pass outcome](#pass-outcome-number-6)	|	[Next Pass outcome](#pass-outcome-number-8)

:white_check_mark:Pass outcome
#### Subject detail
|Name|module-pwkso|
|----|----|
|Title|Standalone&#32;module&#32;src&#92;pwkso.ttl&#32;from&#32;branch&#32;main|
|Composition|- [Module pwkso](https://github.com/acimov-tools/model-test/blob/main/src/pwkso.ttl)|

#### Criterion detail
|Identifier|[proper-extension-predicate](https://ns.inria.fr/olivaw#proper-extension-predicate)|
|----|----|
|Title|Predicate&#32;extension&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;test&#32;the&#32;proper&#32;use&#32;of&#32;predicates&#32;rdfs:subClassOf&#32;and&#32;rdfs:subPropertyOf&#32;on&#32;the&#32;ontology&#32;terms|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-7)|Identifier|`subclassof-property`|
|[Section top](#pass-outcome-number-7)|Title|No&#32;subclass&#32;of&#32;property|
|[Section top](#pass-outcome-number-7)|Description|No&#32;ontology&#32;term&#32;is&#32;a&#32;subclass&#32;of&#32;a&#32;property|

***
### Pass Outcome number 8

[Jump to summary definition](#summary-Pass-8)	|	[Previous Pass outcome](#pass-outcome-number-7)	|	[Next Pass outcome](#pass-outcome-number-9)

:white_check_mark:Pass outcome
#### Subject detail
|Name|module-pwkso|
|----|----|
|Title|Standalone&#32;module&#32;src&#92;pwkso.ttl&#32;from&#32;branch&#32;main|
|Composition|- [Module pwkso](https://github.com/acimov-tools/model-test/blob/main/src/pwkso.ttl)|

#### Criterion detail
|Identifier|[proper-extension-predicate](https://ns.inria.fr/olivaw#proper-extension-predicate)|
|----|----|
|Title|Predicate&#32;extension&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;test&#32;the&#32;proper&#32;use&#32;of&#32;predicates&#32;rdfs:subClassOf&#32;and&#32;rdfs:subPropertyOf&#32;on&#32;the&#32;ontology&#32;terms|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-8)|Identifier|`subpropertyof-class`|
|[Section top](#pass-outcome-number-8)|Title|No&#32;subproperty&#32;of&#32;class|
|[Section top](#pass-outcome-number-8)|Description|No&#32;ontology&#32;term&#32;is&#32;a&#32;subproperty&#32;of&#32;a&#32;class|

***
### Pass Outcome number 9

[Jump to summary definition](#summary-Pass-9)	|	[Previous Pass outcome](#pass-outcome-number-8)	|	Next Pass outcome

:white_check_mark:Pass outcome
#### Subject detail
|Name|module-pwkso|
|----|----|
|Title|Standalone&#32;module&#32;src&#92;pwkso.ttl&#32;from&#32;branch&#32;main|
|Composition|- [Module pwkso](https://github.com/acimov-tools/model-test/blob/main/src/pwkso.ttl)|

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
