# Test Report Markdown Export

This file is an export of the RDF test report made out of [EARL vocabulary](https://www.w3.org/TR/EARL10/)

This test is powered by Corese, check [Corese website](https://project.inria.fr/corese/) and [Corese repository](https://github.com/Wimmics/corese)

The original test report is available in turtle syntax [here](./model-test-manual-NicoRobertIn-2025-06-19T19-20-11.ttl).

# Test Activity

Here is some information about the testing activity that led to this report

|Title|Model&#32;tests&#32;of&#32;[HyperAgents/hmas](https://github.com/HyperAgents/hmas)&#32;on&#32;branch&#32;HEAD|
|--|--|
|Description|[NicoRobertIn](https://github.com/NicoRobertIn)&#32;launch&#32;manual&#32;run&#32;of&#32;model&#32;tests&#32;against&#32;[HyperAgents/hmas](https://github.com/HyperAgents/hmas)&#32;on&#32;branch&#32;HEAD|
|Tester|[NicoRobertIn](https://github.com/NicoRobertIn)|
|Ontology|[HyperAgents/hmas](https://github.com/HyperAgents/hmas)|
|Ontology version|Local state `ca439d4144b23b3fe927509872babc8d82142fae`|
|Ontology version date|2025-06-19 19:20:03|
|Ontology previous version|[90fbedb96dc5645974226dd1c5a7b30e8ea8c3c8](https://github.com/HyperAgents/hmas/tree/90fbedb96dc5645974226dd1c5a7b30e8ea8c3c8)|
|Ontology branch|[HEAD](https://github.com/HyperAgents/hmas/tree/HEAD)|
|Olivaw suite|[olivaw model test suite](https://github.com/Wimmics/olivaw/blob/v0.0.8/olivaw/test/model/suite.py)|
|Olivaw version|[v0.0.8](https://pypi.org/project/olivaw/0.0.8)|
|Generated turtle|[Turtle report](./model-test-manual-NicoRobertIn-2025-06-19T19-20-11.ttl)|
|Generated Markdown|[Markdown report](./model-test-manual-NicoRobertIn-2025-06-19T19-20-11.md)|

# Statistic summary

Here is a short overview for this test report

237 Outcomes

:boom:3 MajorFail, :exclamation:32 MinorFail, :warning:0 CannotTell, :grey_question:30 NotTested, :white_check_mark:172 Pass

<div  style="border-radius: 12px; height: 25px; overflow: hidden"><img src="../assets/red.png" width="1%" height="25px"/><img src="../assets/orange.png" width="13%" height="25px"/><img src="../assets/grey.png" width="0%" height="25px"/><img src="../assets/white.png" width="12%" height="25px"/><img src="../assets/green.png" width="74%" height="25px"/></div>

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

:boom:3 MajorFail outcomes

<details>
<summary>Fold/Unfold the 3 summary and details</summary>

## MajorFail Outcomes Summary

:boom:3 MajorFail outcomes

|*Jump*|*Number*|*Status*|*Subject*|*Criterion*|*Title*|*Link*|
|------|--------|--------|---------|-----------|-------|------|
|[Chapter top](#majorfail-outcomes)|<div id="summary-MajorFail-1">1/3</div>|:boom:MajorFail|`module-meta`|[syntax](https://ns.inria.fr/olivaw#syntax)|Test subject has syntax errors|[Jump](#majorfail-outcome-number-1)|
|[Chapter top](#majorfail-outcomes)|<div id="summary-MajorFail-2">2/3</div>|:boom:MajorFail|`modelet-manufacturing-environments-safety-rules`|[syntax](https://ns.inria.fr/olivaw#syntax)|Test subject has syntax errors|[Jump](#majorfail-outcome-number-2)|
|[Chapter top](#majorfail-outcomes)|<div id="summary-MajorFail-3">3/3</div>|:boom:MajorFail|`modelet-logistics-structure-organization`|[syntax](https://ns.inria.fr/olivaw#syntax)|Test subject has syntax errors|[Jump](#majorfail-outcome-number-3)|

***

## MajorFail Outcomes Details

This subchapter gives more details to the :boom:MajorFail outcomes

### MajorFail Outcome number 1

[Jump to summary definition](#summary-MajorFail-1)	|	Previous MajorFail outcome	|	[Next MajorFail outcome](#majorfail-outcome-number-2)

:boom:MajorFail outcome
#### Subject detail
|Name|module-meta|
|----|----|
|Title|Standalone&#32;module&#32;src&#92;meta.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Module meta](https://github.com/HyperAgents/hmas/blob/HEAD/src/meta.ttl)|

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
|[Section top](#majorfail-outcome-number-1)|Description|The&#32;subject&#32;has&#32;turtle&#32;syntax&#32;errors&#32;that&#32;makes&#32;it&#32;unprocessable&#32;by&#32;an&#32;engine|
|[Section top](#majorfail-outcome-number-1)|Pointer|<pre lang="Turtle"><code>Undefined&#32;prefix:&#32;dcterms:source</code></pre>|
|[Section top](#majorfail-outcome-number-1)|Pointer|<pre lang="Turtle"><code>Undefined&#32;prefix:&#32;doco:Glossary</code></pre>|

***
### MajorFail Outcome number 2

[Jump to summary definition](#summary-MajorFail-2)	|	[Previous MajorFail outcome](#majorfail-outcome-number-1)	|	[Next MajorFail outcome](#majorfail-outcome-number-3)

:boom:MajorFail outcome
#### Subject detail
|Name|modelet-manufacturing-environments-safety-rules|
|----|----|
|Title|Standalone&#32;modelet&#32;domains&#92;manufacturing-environments&#92;safety-rules&#92;onto.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Modelet manufacturing-environments/safety-rules](https://github.com/HyperAgents/hmas/blob/HEAD/domains/manufacturing-environments/safety-rules/onto.ttl)|

#### Criterion detail
|Identifier|[syntax](https://ns.inria.fr/olivaw#syntax)|
|----|----|
|Title|Syntax&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;check&#32;wether&#32;the&#32;test&#32;subject&#32;is&#32;syntaxically&#32;correct&#32;or&#32;not.|

#### Outcome Detail
|Jump|Type|:boom:MajorFail|
|----|----|----|
|[Section top](#majorfail-outcome-number-2)|Identifier|`syntax-error`|
|[Section top](#majorfail-outcome-number-2)|Title|Test&#32;subject&#32;has&#32;syntax&#32;errors|
|[Section top](#majorfail-outcome-number-2)|Description|The&#32;subject&#32;has&#32;turtle&#32;syntax&#32;errors&#32;that&#32;makes&#32;it&#32;unprocessable&#32;by&#32;an&#32;engine|
|[Section top](#majorfail-outcome-number-2)|Pointer|<pre lang="Turtle"><code>Encountered&#32; &#34;&#92; &#34;Associates&#32;exceptions&#32;to&#32;a&#32;context&#32;of&#32;application&#32;of&#32;a&#32;norm&#92; &#34;&#34; &#32;at&#32;line&#32;82,&#32;column&#32;30.</code></pre>|

***
### MajorFail Outcome number 3

[Jump to summary definition](#summary-MajorFail-3)	|	[Previous MajorFail outcome](#majorfail-outcome-number-2)	|	Next MajorFail outcome

:boom:MajorFail outcome
#### Subject detail
|Name|modelet-logistics-structure-organization|
|----|----|
|Title|Standalone&#32;modelet&#32;domains&#92;logistics&#92;structure-organization&#92;onto.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Modelet logistics/structure-organization](https://github.com/HyperAgents/hmas/blob/HEAD/domains/logistics/structure-organization/onto.ttl)|

#### Criterion detail
|Identifier|[syntax](https://ns.inria.fr/olivaw#syntax)|
|----|----|
|Title|Syntax&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;check&#32;wether&#32;the&#32;test&#32;subject&#32;is&#32;syntaxically&#32;correct&#32;or&#32;not.|

#### Outcome Detail
|Jump|Type|:boom:MajorFail|
|----|----|----|
|[Section top](#majorfail-outcome-number-3)|Identifier|`syntax-error`|
|[Section top](#majorfail-outcome-number-3)|Title|Test&#32;subject&#32;has&#32;syntax&#32;errors|
|[Section top](#majorfail-outcome-number-3)|Description|The&#32;subject&#32;has&#32;turtle&#32;syntax&#32;errors&#32;that&#32;makes&#32;it&#32;unprocessable&#32;by&#32;an&#32;engine|
|[Section top](#majorfail-outcome-number-3)|Pointer|<pre lang="Turtle"><code>at&#32;line&#32;18&#32;of&#32; &#60;>:  &#10;Bad&#32;syntax&#32;(Prefix&#32; &#34;skos:&#34; &#32;not&#32;bound)&#32;at&#32;&Hat;&#32;in:  &#10; &#34;...b'&#32;Agents&#32;in&#32;an&#32;Organization&#32;that&#32;belong&#32;together.&#34;@en&#32;;&#92;r&#92;n&#32; &#32; &#32; &#32;'&Hat;b'skos:example&#32; &#34;In&#32;a&#32;human&#32;organization,&#32;a&#32;HR&#32;department&#32;is&#32;se'...&#34;</code></pre>|

***

</details>

***


# MinorFail Outcomes

[Jump to statistic summary](#statistic-summary)	|	[Previous section](#majorfail-outcomes)	|	[Next section](#nottested-outcomes)

Here is the chapter related to the MinorFail outcome

:exclamation:32 MinorFail outcomes

<details>
<summary>Fold/Unfold the 32 summary and details</summary>

## MinorFail Outcomes Summary

:exclamation:32 MinorFail outcomes

|*Jump*|*Number*|*Status*|*Subject*|*Criterion*|*Title*|*Link*|
|------|--------|--------|---------|-----------|-------|------|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-1">1/32</div>|:exclamation:MinorFail|`module-regulation`|[terms-differenciation](https://ns.inria.fr/olivaw#terms-differenciation)|Too close terms|[Jump](#minorfail-outcome-number-1)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-2">2/32</div>|:exclamation:MinorFail|`module-fipa`|[term-referencing](https://ns.inria.fr/olivaw#term-referencing)|Term not referenced to a module|[Jump](#minorfail-outcome-number-2)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-3">3/32</div>|:exclamation:MinorFail|`module-core`|[labeled-terms](https://ns.inria.fr/olivaw#labeled-terms)|Terms not labeled|[Jump](#minorfail-outcome-number-3)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-4">4/32</div>|:exclamation:MinorFail|`module-core`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL EL Profile incompatible|[Jump](#minorfail-outcome-number-4)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-5">5/32</div>|:exclamation:MinorFail|`module-core`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL EL Profile incompatible|[Jump](#minorfail-outcome-number-5)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-6">6/32</div>|:exclamation:MinorFail|`module-core`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL QL Profile incompatible|[Jump](#minorfail-outcome-number-6)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-7">7/32</div>|:exclamation:MinorFail|`module-core`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL QL Profile incompatible|[Jump](#minorfail-outcome-number-7)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-8">8/32</div>|:exclamation:MinorFail|`module-alignment-interaction-td`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL QL Profile incompatible|[Jump](#minorfail-outcome-number-8)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-9">9/32</div>|:exclamation:MinorFail|`module-alignment-interaction-td`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL QL Profile incompatible|[Jump](#minorfail-outcome-number-9)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-10">10/32</div>|:exclamation:MinorFail|`modelet-manufacturing-environments-discover-signifiers`|[labeled-terms](https://ns.inria.fr/olivaw#labeled-terms)|Terms not labeled|[Jump](#minorfail-outcome-number-10)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-11">11/32</div>|:exclamation:MinorFail|`modelet-manufacturing-environments-discover-signifiers`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL EL Profile incompatible|[Jump](#minorfail-outcome-number-11)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-12">12/32</div>|:exclamation:MinorFail|`modelet-manufacturing-environments-discover-signifiers`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL QL Profile incompatible|[Jump](#minorfail-outcome-number-12)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-13">13/32</div>|:exclamation:MinorFail|`modelet-manufacturing-environments-discover-platforms`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL EL Profile incompatible|[Jump](#minorfail-outcome-number-13)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-14">14/32</div>|:exclamation:MinorFail|`modelet-manufacturing-environments-discover-core`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL EL Profile incompatible|[Jump](#minorfail-outcome-number-14)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-15">15/32</div>|:exclamation:MinorFail|`modelet-manufacturing-environments-discover-core`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL QL Profile incompatible|[Jump](#minorfail-outcome-number-15)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-16">16/32</div>|:exclamation:MinorFail|`modelet-logistics-configure-organization`|[terms-differenciation](https://ns.inria.fr/olivaw#terms-differenciation)|Too close terms|[Jump](#minorfail-outcome-number-16)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-17">17/32</div>|:exclamation:MinorFail|`all-modules`|[labeled-terms](https://ns.inria.fr/olivaw#labeled-terms)|Terms not labeled|[Jump](#minorfail-outcome-number-17)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-18">18/32</div>|:exclamation:MinorFail|`all-modules`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL EL Profile incompatible|[Jump](#minorfail-outcome-number-18)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-19">19/32</div>|:exclamation:MinorFail|`all-modules`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL EL Profile incompatible|[Jump](#minorfail-outcome-number-19)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-20">20/32</div>|:exclamation:MinorFail|`all-modules`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL QL Profile incompatible|[Jump](#minorfail-outcome-number-20)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-21">21/32</div>|:exclamation:MinorFail|`all-modules`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL QL Profile incompatible|[Jump](#minorfail-outcome-number-21)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-22">22/32</div>|:exclamation:MinorFail|`all-modules`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL QL Profile incompatible|[Jump](#minorfail-outcome-number-22)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-23">23/32</div>|:exclamation:MinorFail|`all-modules`|[term-referencing](https://ns.inria.fr/olivaw#term-referencing)|Term not referenced to a module|[Jump](#minorfail-outcome-number-23)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-24">24/32</div>|:exclamation:MinorFail|`all-modules`|[terms-differenciation](https://ns.inria.fr/olivaw#terms-differenciation)|Too close terms|[Jump](#minorfail-outcome-number-24)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-25">25/32</div>|:exclamation:MinorFail|`all-fragments`|[labeled-terms](https://ns.inria.fr/olivaw#labeled-terms)|Terms not labeled|[Jump](#minorfail-outcome-number-25)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-26">26/32</div>|:exclamation:MinorFail|`all-fragments`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL EL Profile incompatible|[Jump](#minorfail-outcome-number-26)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-27">27/32</div>|:exclamation:MinorFail|`all-fragments`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL EL Profile incompatible|[Jump](#minorfail-outcome-number-27)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-28">28/32</div>|:exclamation:MinorFail|`all-fragments`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL QL Profile incompatible|[Jump](#minorfail-outcome-number-28)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-29">29/32</div>|:exclamation:MinorFail|`all-fragments`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL QL Profile incompatible|[Jump](#minorfail-outcome-number-29)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-30">30/32</div>|:exclamation:MinorFail|`all-fragments`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL QL Profile incompatible|[Jump](#minorfail-outcome-number-30)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-31">31/32</div>|:exclamation:MinorFail|`all-fragments`|[term-referencing](https://ns.inria.fr/olivaw#term-referencing)|Term not referenced to a module|[Jump](#minorfail-outcome-number-31)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-32">32/32</div>|:exclamation:MinorFail|`all-fragments`|[terms-differenciation](https://ns.inria.fr/olivaw#terms-differenciation)|Too close terms|[Jump](#minorfail-outcome-number-32)|

***

## MinorFail Outcomes Details

This subchapter gives more details to the :exclamation:MinorFail outcomes

### MinorFail Outcome number 1

[Jump to summary definition](#summary-MinorFail-1)	|	Previous MinorFail outcome	|	[Next MinorFail outcome](#minorfail-outcome-number-2)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-regulation|
|----|----|
|Title|Standalone&#32;module&#32;src&#92;regulation.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Module regulation](https://github.com/HyperAgents/hmas/blob/HEAD/src/regulation.ttl)|

#### Criterion detail
|Identifier|[terms-differenciation](https://ns.inria.fr/olivaw#terms-differenciation)|
|----|----|
|Title|Terms&#32;differenciation&#32;test|
|Description|A&#32;test&#32;case&#32;from&#32;the&#32;Best&#32;Practices&#32;tests&#32;checking&#32;if&#32;all&#32;the&#32;terms&#32;are&#32;different&#32;enough&#32;from&#32;each&#32;other&#32;according&#32;to&#32;the&#32;Levenshtein&#32;distance&#32;metric.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-1)|Identifier|`too-close-terms`|
|[Section top](#minorfail-outcome-number-1)|Title|Too&#32;close&#32;terms|
|[Section top](#minorfail-outcome-number-1)|Description|Some&#32;terms&#32;are&#32;too&#32;similar|
|[Section top](#minorfail-outcome-number-1)|Pointer|<pre lang="Turtle"><code>:isAccessTo&#32;a&#32;owl:ObjectProperty&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;is&#32;access&#32;to&#34;@en,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#34;est&#32;l'accès&#32;à&#34;@fr&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;A&#32;relation&#32;that&#32;refers&#32;to&#32;an&#32;Artifact&#32;involved&#32;in&#32;an&#32;Access.&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:domain&#32;:Access&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32;:regulation&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:range&#32;:Artifact&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-1)|Pointer|<pre lang="Turtle"><code>:isAccessOf&#32;a&#32;owl:ObjectProperty&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;is&#32;access&#32;of&#34;@en,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#34;est&#32;l'accès&#32;de&#34;@fr&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;A&#32;relation&#32;that&#32;refers&#32;to&#32;an&#32;Agent&#32;involved&#32;in&#32;an&#32;Access.&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:domain&#32;:Access&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32;:regulation&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:range&#32;:Agent&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-1)|Pointer|<pre lang="Turtle"><code>:isAccessFor&#32;a&#32;owl:ObjectProperty&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;is&#32;access&#32;for&#34;@en,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#34;est&#32;l'accès&#32;pour&#34;@fr&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;A&#32;relation&#32;that&#32;refers&#32;to&#32;a&#32;Usage&#32;involved&#32;in&#32;an&#32;Access.&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:domain&#32;:Access&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32;:regulation&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:range&#32;:Usage&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-1)|Pointer|<pre lang="Turtle"><code>:isMembershipOf&#32;a&#32;owl:ObjectProperty&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;is&#32;membership&#32;of&#34;@en,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#34;est&#32;l'appartenance&#32;à&#34;@fr&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;A&#32;relation&#32;that&#32;refers&#32;to&#32;the&#32;Agent&#32;involved&#32;in&#32;a&#32;Membership...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:domain&#32;:Membership&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32;:regulation&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:range&#32;:Agent&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-1)|Pointer|<pre lang="Turtle"><code>:isMembershipIn&#32;a&#32;owl:ObjectProperty&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;is&#32;membership&#32;in&#34;@en,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#34;est&#32;l'appartenance&#32;à&#34;@fr&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;A&#32;relation&#32;that&#32;refers&#32;to&#32;the&#32;Group&#32;involved&#32;in&#32;a&#32;Membership...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:domain&#32;:Membership&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32;:regulation&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:range&#32;:Group&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-1)|Pointer|<pre lang="Turtle"><code>:isUsageOf&#32;a&#32;owl:ObjectProperty&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;is&#32;usage&#32;of&#34;@en,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#34;est&#32;un&#32;usage&#32;de&#34;@fr&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;A&#32;relation&#32;that&#32;refers&#32;to&#32;a&#32;Facility&#32;involved&#32;in&#32;a&#32;Usage.&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:domain&#32;:Usage&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32;:regulation&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:range&#32;:Facility&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-1)|Pointer|<pre lang="Turtle"><code>:isUsageIn&#32;a&#32;owl:ObjectProperty&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;is&#32;usage&#32;in&#34;@en,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#34;est&#32;un&#32;usage&#32;dans&#34;@fr&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;A&#32;relation&#32;that&#32;refers&#32;to&#32;a&#32;Setting&#32;involved&#32;in&#32;a&#32;Usage.&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:domain&#32;:Usage&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32;:regulation&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:range&#32;:Setting&#32;.</code></pre>|

***
### MinorFail Outcome number 2

[Jump to summary definition](#summary-MinorFail-2)	|	[Previous MinorFail outcome](#minorfail-outcome-number-1)	|	[Next MinorFail outcome](#minorfail-outcome-number-3)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-fipa|
|----|----|
|Title|Standalone&#32;module&#32;src&#92;fipa.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Module fipa](https://github.com/HyperAgents/hmas/blob/HEAD/src/fipa.ttl)|

#### Criterion detail
|Identifier|[term-referencing](https://ns.inria.fr/olivaw#term-referencing)|
|----|----|
|Title|Term&#32;referencing&#32;test|
|Description|A&#32;test&#32;case&#32;from&#32;the&#32;Best&#32;Practices&#32;tests&#32;checking&#32;if&#32;each&#32;term&#32;of&#32;the&#32;test&#32;subject&#32;is&#32;referenced&#32;to&#32;a&#32;module&#32;through&#32;a&#32;rdfs:isDefinedBy&#32;property.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-2)|Identifier|`no-reference-module`|
|[Section top](#minorfail-outcome-number-2)|Title|Term&#32;not&#32;referenced&#32;to&#32;a&#32;module|
|[Section top](#minorfail-outcome-number-2)|Description|Subject&#32;terms&#32;not&#32;linked&#32;to&#32;a&#32;module&#32;by&#32;a&#32;rdfs:isDefinedBy&#32;property|
|[Section top](#minorfail-outcome-number-2)|Pointer|<pre lang="Turtle"><code>:hasServiceName&#32;a&#32;owl:ObjectProperty&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;has&#32;Service&#32;Name&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:domain&#32;:APService&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-2)|Pointer|<pre lang="Turtle"><code>:APService&#32;a&#32;owl:Class&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;Agent&#32;Platform&#32;Service&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;A&#32;service&#32;exposed&#32;by&#32;a&#32;FIPA&#32;Agent&#32;Platform&#32;as&#32;defined&#32;by&#32;the...&#34; &#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-2)|Pointer|<pre lang="Turtle"><code>:hasServiceType&#32;a&#32;owl:ObjectProperty&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;has&#32;Service&#32;Type&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:domain&#32;:APService&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-2)|Pointer|<pre lang="Turtle"><code>:AgentIdentifierDescription&#32;a&#32;owl:Class&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;Agent&#32;Identifier&#32;Description&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;A&#32;resource&#32;profile&#32;that&#32;describes&#32;an&#32;agent&#32;using&#32;the&#32;Agent&#32;I...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:subClassOf&#32; &#60;https://ci.mines-stetienne.fr/hmas#ResourceProfile> &#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-2)|Pointer|<pre lang="Turtle"><code>:AgentPlatformDescription&#32;a&#32;owl:Class&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;Agent&#32;Platform&#32;Description&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;A&#32;resource&#32;profile&#32;that&#32;descripe&#32;a&#32;FIPA&#32;Agent&#32;Platform&#32;using...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:subClassOf&#32; &#60;https://ci.mines-stetienne.fr/hmas#ResourceProfile> &#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-2)|Pointer|<pre lang="Turtle"><code>:FIPAAgentPlatform&#32;a&#32;owl:Class&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;FIPA&#32;Agent&#32;Platform&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;A&#32;platform&#32;that&#32;conforms&#32;to&#32;the&#32;FIPA&#32;Abstract&#32;Architecture&#32;S...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:subClassOf&#32; &#60;https://ci.mines-stetienne.fr/hmas#Platform> &#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-2)|Pointer|<pre lang="Turtle"><code>:HTTPMessageTransportService&#32;a&#32;owl:Class&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;HTTP&#32;Message&#32;Transport&#32;Service&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;An&#32;HTTP-based&#32;message&#32;transport&#32;service&#32;that&#32;confirms&#32;to&#32;the...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:subClassOf&#32;:MessageTransportService&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-2)|Pointer|<pre lang="Turtle"><code>:MessageTransportService&#32;a&#32;owl:Class&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;Message&#32;Transport&#32;Service&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;A&#32;service&#32;for&#32;transporting&#32;messages&#32;among&#32;agents&#32;that&#32;confor...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:subClassOf&#32;:APService&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-2)|Pointer|<pre lang="Turtle"><code>:IIOPMessageTransportService&#32;a&#32;owl:Class&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;IIOP&#32;Message&#32;Transport&#32;Service&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;An&#32;HTTP-based&#32;message&#32;transport&#32;service&#32;that&#32;confirms&#32;to&#32;the...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:subClassOf&#32;:MessageTransportService&#32;.</code></pre>|

***
### MinorFail Outcome number 3

[Jump to summary definition](#summary-MinorFail-3)	|	[Previous MinorFail outcome](#minorfail-outcome-number-2)	|	[Next MinorFail outcome](#minorfail-outcome-number-4)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-core|
|----|----|
|Title|Standalone&#32;module&#32;src&#92;core.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Module core](https://github.com/HyperAgents/hmas/blob/HEAD/src/core.ttl)|

#### Criterion detail
|Identifier|[labeled-terms](https://ns.inria.fr/olivaw#labeled-terms)|
|----|----|
|Title|Term&#32;labeling&#32;test|
|Description|A&#32;test&#32;case&#32;from&#32;the&#32;Best&#32;Practices&#32;tests&#32;checking&#32;if&#32;all&#32;the&#32;terms&#32;of&#32;the&#32;subject&#32;have&#32;a&#32;rdfs:label&#32;property&#32;pointing&#32;to&#32;a&#32;literal&#32;in&#32;English|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-3)|Identifier|`not-labeled-term`|
|[Section top](#minorfail-outcome-number-3)|Title|Terms&#32;not&#32;labeled|
|[Section top](#minorfail-outcome-number-3)|Description|The&#32;following&#32;terms&#32;have&#32;no&#32;rdfs:label&#32;to&#32;define&#32;it&#32;in&#32;natural&#32;language|
|[Section top](#minorfail-outcome-number-3)|Pointer|<pre lang="Turtle"><code>:Affordance&#32;a&#32;skos:Concept&#32;;  &#10; &#32; &#32; &#32; &#32;dc:references&#32; &#91;&#32;a&#32;owl:NamedIndividual&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;Chemero&#32;and&#32;Turvey,&#32;2007&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;dc:bibliographicCitation&#32; &#34;Chemero,&#32;A.,&#32;&&#32;Turvey,&#32;M.&#32;T.&#32;(2007).&#32;Complexity,&#32;hypersets,&#32;...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;dc:identifier&#32; &#60;https://doi.org/10.1162/biot.2007.2.1.23> &#32;],  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#91;&#32;a&#32;owl:NamedIndividual&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;Norman,&#32;2013&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;dc:bibliographicCitation&#32; &#34;Norman,&#32;D.&#32;(2013).&#32;The&#32;design&#32;of&#32;everyday&#32;things:&#32;Revised&#32;an...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;dc:identifier&#32; &#60;https://mitpress.mit.edu/9780262640374/> &#32;]&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32;:core&#32;;  &#10; &#32; &#32; &#32; &#32;skos:definition&#32; &#34;A&#32;behavior&#32;possibility&#32;that&#32;is&#32;a&#32;relationship&#32;between&#32;an&#32;abi...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;skos:editorialNote&#32; &#34;The&#32;concept&#32;has&#32;been&#32;considered&#32;as&#32;a&#32;candidate&#32;term&#32;for&#32;repr...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;skos:historyNote&#32; &#34;The&#32;definition&#32;of&#32;the&#32;concept&#32;follows&#32;affordance&#32;theorists&#32; &#91;...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;skos:prefLabel&#32; &#34;affordance&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;skos:related&#32;:Signifier&#32;.</code></pre>|

***
### MinorFail Outcome number 4

[Jump to summary definition](#summary-MinorFail-4)	|	[Previous MinorFail outcome](#minorfail-outcome-number-3)	|	[Next MinorFail outcome](#minorfail-outcome-number-5)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-core|
|----|----|
|Title|Standalone&#32;module&#32;src&#92;core.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Module core](https://github.com/HyperAgents/hmas/blob/HEAD/src/core.ttl)|

#### Criterion detail
|Identifier|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|
|----|----|
|Title|Profile&#32;compatibility&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;check&#32;whether&#32;the&#32;test&#32;subject&#32;is&#32;compatible&#32;with&#32;a&#32;profile&#32;or&#32;not,&#32;and&#32;if&#32;it&#32;is&#32;not,&#32;why.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-4)|Identifier|`owl-el-profile-error`|
|[Section top](#minorfail-outcome-number-4)|Title|OWL&#32;EL&#32;Profile&#32;incompatible|
|[Section top](#minorfail-outcome-number-4)|Description|Anonymous&#32;individuals&#32;are&#32;not&#32;supported|
|[Section top](#minorfail-outcome-number-4)|Pointer|<pre lang="Turtle"><code>&#91;]&#32;a&#32;owl:NamedIndividual&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;Chemero&#32;and&#32;Turvey,&#32;2007&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;dc:bibliographicCitation&#32; &#34;Chemero,&#32;A.,&#32;&&#32;Turvey,&#32;M.&#32;T.&#32;(2007).&#32;Complexity,&#32;hypersets,&#32;...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;dc:identifier&#32; &#60;https://doi.org/10.1162/biot.2007.2.1.23> &#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-4)|Pointer|<pre lang="Turtle"><code>&#91;]&#32;a&#32;owl:NamedIndividual&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;Norman,&#32;2013&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;dc:bibliographicCitation&#32; &#34;Norman,&#32;D.&#32;(2013).&#32;The&#32;design&#32;of&#32;everyday&#32;things:&#32;Revised&#32;an...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;dc:identifier&#32; &#60;https://mitpress.mit.edu/9780262640374/> &#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-4)|Pointer|<pre lang="Turtle"><code>hmas:Affordance&#32;a&#32;skos:Concept&#32;;  &#10; &#32; &#32; &#32; &#32;dc:references&#32; &#91;&#32;a&#32;owl:NamedIndividual&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;Chemero&#32;and&#32;Turvey,&#32;2007&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;dc:bibliographicCitation&#32; &#34;Chemero,&#32;A.,&#32;&&#32;Turvey,&#32;M.&#32;T.&#32;(2007).&#32;Complexity,&#32;hypersets,&#32;...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;dc:identifier&#32; &#60;https://doi.org/10.1162/biot.2007.2.1.23> &#32;],  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#91;&#32;a&#32;owl:NamedIndividual&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;Norman,&#32;2013&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;dc:bibliographicCitation&#32; &#34;Norman,&#32;D.&#32;(2013).&#32;The&#32;design&#32;of&#32;everyday&#32;things:&#32;Revised&#32;an...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;dc:identifier&#32; &#60;https://mitpress.mit.edu/9780262640374/> &#32;]&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32;hmas:core&#32;;  &#10; &#32; &#32; &#32; &#32;skos:definition&#32; &#34;A&#32;behavior&#32;possibility&#32;that&#32;is&#32;a&#32;relationship&#32;between&#32;an&#32;abi...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;skos:editorialNote&#32; &#34;The&#32;concept&#32;has&#32;been&#32;considered&#32;as&#32;a&#32;candidate&#32;term&#32;for&#32;repr...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;skos:historyNote&#32; &#34;The&#32;definition&#32;of&#32;the&#32;concept&#32;follows&#32;affordance&#32;theorists&#32; &#91;...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;skos:prefLabel&#32; &#34;affordance&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;skos:related&#32;hmas:Signifier&#32;.</code></pre>|

***
### MinorFail Outcome number 5

[Jump to summary definition](#summary-MinorFail-5)	|	[Previous MinorFail outcome](#minorfail-outcome-number-4)	|	[Next MinorFail outcome](#minorfail-outcome-number-6)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-core|
|----|----|
|Title|Standalone&#32;module&#32;src&#92;core.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Module core](https://github.com/HyperAgents/hmas/blob/HEAD/src/core.ttl)|

#### Criterion detail
|Identifier|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|
|----|----|
|Title|Profile&#32;compatibility&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;check&#32;whether&#32;the&#32;test&#32;subject&#32;is&#32;compatible&#32;with&#32;a&#32;profile&#32;or&#32;not,&#32;and&#32;if&#32;it&#32;is&#32;not,&#32;why.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-5)|Identifier|`owl-el-profile-error`|
|[Section top](#minorfail-outcome-number-5)|Title|OWL&#32;EL&#32;Profile&#32;incompatible|
|[Section top](#minorfail-outcome-number-5)|Description|Statement&#32;not&#32;supported|
|[Section top](#minorfail-outcome-number-5)|Pointer|<pre lang="Turtle"><code>hmas:hasProfile&#32;a&#32;owl:AsymmetricProperty,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:ObjectProperty&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;has&#32;for&#32;profile&#34;@en,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#34;a&#32;pour&#32;profil&#34;@fr&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;A&#32;relation&#32;that&#32;links&#32;a&#32;resource&#32;to&#32;its&#32;profile.&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32;hmas:core&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:range&#32;hmas:ResourceProfile&#32;;  &#10; &#32; &#32; &#32; &#32;owl:inverseOf&#32;hmas:isProfileOf&#32;.</code></pre>|

***
### MinorFail Outcome number 6

[Jump to summary definition](#summary-MinorFail-6)	|	[Previous MinorFail outcome](#minorfail-outcome-number-5)	|	[Next MinorFail outcome](#minorfail-outcome-number-7)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-core|
|----|----|
|Title|Standalone&#32;module&#32;src&#92;core.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Module core](https://github.com/HyperAgents/hmas/blob/HEAD/src/core.ttl)|

#### Criterion detail
|Identifier|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|
|----|----|
|Title|Profile&#32;compatibility&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;check&#32;whether&#32;the&#32;test&#32;subject&#32;is&#32;compatible&#32;with&#32;a&#32;profile&#32;or&#32;not,&#32;and&#32;if&#32;it&#32;is&#32;not,&#32;why.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-6)|Identifier|`owl-ql-profile-error`|
|[Section top](#minorfail-outcome-number-6)|Title|OWL&#32;QL&#32;Profile&#32;incompatible|
|[Section top](#minorfail-outcome-number-6)|Description|Anonymous&#32;individuals&#32;are&#32;not&#32;supported|
|[Section top](#minorfail-outcome-number-6)|Pointer|<pre lang="Turtle"><code>&#91;]&#32;a&#32;owl:NamedIndividual&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;Chemero&#32;and&#32;Turvey,&#32;2007&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;dc:bibliographicCitation&#32; &#34;Chemero,&#32;A.,&#32;&&#32;Turvey,&#32;M.&#32;T.&#32;(2007).&#32;Complexity,&#32;hypersets,&#32;...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;dc:identifier&#32; &#60;https://doi.org/10.1162/biot.2007.2.1.23> &#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-6)|Pointer|<pre lang="Turtle"><code>&#91;]&#32;a&#32;owl:NamedIndividual&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;Norman,&#32;2013&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;dc:bibliographicCitation&#32; &#34;Norman,&#32;D.&#32;(2013).&#32;The&#32;design&#32;of&#32;everyday&#32;things:&#32;Revised&#32;an...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;dc:identifier&#32; &#60;https://mitpress.mit.edu/9780262640374/> &#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-6)|Pointer|<pre lang="Turtle"><code>hmas:Affordance&#32;a&#32;skos:Concept&#32;;  &#10; &#32; &#32; &#32; &#32;dc:references&#32; &#91;&#32;a&#32;owl:NamedIndividual&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;Chemero&#32;and&#32;Turvey,&#32;2007&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;dc:bibliographicCitation&#32; &#34;Chemero,&#32;A.,&#32;&&#32;Turvey,&#32;M.&#32;T.&#32;(2007).&#32;Complexity,&#32;hypersets,&#32;...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;dc:identifier&#32; &#60;https://doi.org/10.1162/biot.2007.2.1.23> &#32;],  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#91;&#32;a&#32;owl:NamedIndividual&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;Norman,&#32;2013&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;dc:bibliographicCitation&#32; &#34;Norman,&#32;D.&#32;(2013).&#32;The&#32;design&#32;of&#32;everyday&#32;things:&#32;Revised&#32;an...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;dc:identifier&#32; &#60;https://mitpress.mit.edu/9780262640374/> &#32;]&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32;hmas:core&#32;;  &#10; &#32; &#32; &#32; &#32;skos:definition&#32; &#34;A&#32;behavior&#32;possibility&#32;that&#32;is&#32;a&#32;relationship&#32;between&#32;an&#32;abi...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;skos:editorialNote&#32; &#34;The&#32;concept&#32;has&#32;been&#32;considered&#32;as&#32;a&#32;candidate&#32;term&#32;for&#32;repr...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;skos:historyNote&#32; &#34;The&#32;definition&#32;of&#32;the&#32;concept&#32;follows&#32;affordance&#32;theorists&#32; &#91;...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;skos:prefLabel&#32; &#34;affordance&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;skos:related&#32;hmas:Signifier&#32;.</code></pre>|

***
### MinorFail Outcome number 7

[Jump to summary definition](#summary-MinorFail-7)	|	[Previous MinorFail outcome](#minorfail-outcome-number-6)	|	[Next MinorFail outcome](#minorfail-outcome-number-8)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-core|
|----|----|
|Title|Standalone&#32;module&#32;src&#92;core.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Module core](https://github.com/HyperAgents/hmas/blob/HEAD/src/core.ttl)|

#### Criterion detail
|Identifier|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|
|----|----|
|Title|Profile&#32;compatibility&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;check&#32;whether&#32;the&#32;test&#32;subject&#32;is&#32;compatible&#32;with&#32;a&#32;profile&#32;or&#32;not,&#32;and&#32;if&#32;it&#32;is&#32;not,&#32;why.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-7)|Identifier|`owl-ql-profile-error`|
|[Section top](#minorfail-outcome-number-7)|Title|OWL&#32;QL&#32;Profile&#32;incompatible|
|[Section top](#minorfail-outcome-number-7)|Description|Statement&#32;not&#32;supported|
|[Section top](#minorfail-outcome-number-7)|Pointer|<pre lang="Turtle"><code>hmas:transitivelyContains&#32;a&#32;owl:ObjectProperty,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:TransitiveProperty&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;transitively&#32;contains&#34;@en,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#34;contient&#32;transitivement&#34;@fr&#32;;  &#10; &#32; &#32; &#32; &#32;dc:source&#32; &#60;https://github.com/HyperAgents/ns.hyperagents.org/issues/8#issuecomment-1025991719> &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;Links&#32;all&#32;the&#32;resources&#32;that&#32;are&#32;logically&#32;contained&#32;in&#32;a&#32;wo...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:domain&#32;hmas:Workspace&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32;hmas:core&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:seeAlso&#32; &#60;https://github.com/HyperAgents/ns.hyperagents.org/issues/18>,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#60;https://github.com/HyperAgents/ns.hyperagents.org/issues/39> &#32;;  &#10; &#32; &#32; &#32; &#32;owl:inverseOf&#32;hmas:isTransitivelyContainedIn&#32;.</code></pre>|

***
### MinorFail Outcome number 8

[Jump to summary definition](#summary-MinorFail-8)	|	[Previous MinorFail outcome](#minorfail-outcome-number-7)	|	[Next MinorFail outcome](#minorfail-outcome-number-9)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-alignment-interaction-td|
|----|----|
|Title|Standalone&#32;module&#32;src&#92;alignment&#92;interaction-td.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Module alignment/interaction-td](https://github.com/HyperAgents/hmas/blob/HEAD/src/alignment/interaction-td.ttl)|

#### Criterion detail
|Identifier|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|
|----|----|
|Title|Profile&#32;compatibility&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;check&#32;whether&#32;the&#32;test&#32;subject&#32;is&#32;compatible&#32;with&#32;a&#32;profile&#32;or&#32;not,&#32;and&#32;if&#32;it&#32;is&#32;not,&#32;why.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-8)|Identifier|`owl-ql-profile-error`|
|[Section top](#minorfail-outcome-number-8)|Title|OWL&#32;QL&#32;Profile&#32;incompatible|
|[Section top](#minorfail-outcome-number-8)|Description|Class&#32;Expression&#32;not&#32;supported&#32;with&#32;rdfs:subClassOf|
|[Section top](#minorfail-outcome-number-8)|Pointer|<pre lang="Turtle"><code>&#60;https://www.w3.org/2019/wot/td#InteractionAffordance> &#32;rdfs:comment&#32; &#34;Using&#32;a&#32;TD&#32;Interaction&#32;Affordance&#32;results&#32;in&#32;an&#32;action&#32;execu...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:subClassOf&#32; &#91;&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:hasValue&#32;hmas:ActionExecution&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:onProperty&#32;sh:class&#32;]&#32;.</code></pre>|

***
### MinorFail Outcome number 9

[Jump to summary definition](#summary-MinorFail-9)	|	[Previous MinorFail outcome](#minorfail-outcome-number-8)	|	[Next MinorFail outcome](#minorfail-outcome-number-10)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-alignment-interaction-td|
|----|----|
|Title|Standalone&#32;module&#32;src&#92;alignment&#92;interaction-td.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Module alignment/interaction-td](https://github.com/HyperAgents/hmas/blob/HEAD/src/alignment/interaction-td.ttl)|

#### Criterion detail
|Identifier|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|
|----|----|
|Title|Profile&#32;compatibility&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;check&#32;whether&#32;the&#32;test&#32;subject&#32;is&#32;compatible&#32;with&#32;a&#32;profile&#32;or&#32;not,&#32;and&#32;if&#32;it&#32;is&#32;not,&#32;why.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-9)|Identifier|`owl-ql-profile-error`|
|[Section top](#minorfail-outcome-number-9)|Title|OWL&#32;QL&#32;Profile&#32;incompatible|
|[Section top](#minorfail-outcome-number-9)|Description|Statement&#32;not&#32;supported  &#10;Statement&#32;not&#32;supported&#32;in&#32;a&#32;Super&#32;Class&#32;Expression|
|[Section top](#minorfail-outcome-number-9)|Pointer|<pre lang="Turtle"><code>&#91;]&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32;owl:hasValue&#32;hmas:ActionExecution&#32;;  &#10; &#32; &#32; &#32; &#32;owl:onProperty&#32;sh:class&#32;.</code></pre>|

***
### MinorFail Outcome number 10

[Jump to summary definition](#summary-MinorFail-10)	|	[Previous MinorFail outcome](#minorfail-outcome-number-9)	|	[Next MinorFail outcome](#minorfail-outcome-number-11)

:exclamation:MinorFail outcome
#### Subject detail
|Name|modelet-manufacturing-environments-discover-signifiers|
|----|----|
|Title|Standalone&#32;modelet&#32;domains&#92;manufacturing-environments&#92;discover-signifiers&#92;onto.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Modelet manufacturing-environments/discover-signifiers](https://github.com/HyperAgents/hmas/blob/HEAD/domains/manufacturing-environments/discover-signifiers/onto.ttl)|

#### Criterion detail
|Identifier|[labeled-terms](https://ns.inria.fr/olivaw#labeled-terms)|
|----|----|
|Title|Term&#32;labeling&#32;test|
|Description|A&#32;test&#32;case&#32;from&#32;the&#32;Best&#32;Practices&#32;tests&#32;checking&#32;if&#32;all&#32;the&#32;terms&#32;of&#32;the&#32;subject&#32;have&#32;a&#32;rdfs:label&#32;property&#32;pointing&#32;to&#32;a&#32;literal&#32;in&#32;English|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-10)|Identifier|`not-labeled-term`|
|[Section top](#minorfail-outcome-number-10)|Title|Terms&#32;not&#32;labeled|
|[Section top](#minorfail-outcome-number-10)|Description|The&#32;following&#32;terms&#32;have&#32;no&#32;rdfs:label&#32;to&#32;define&#32;it&#32;in&#32;natural&#32;language|
|[Section top](#minorfail-outcome-number-10)|Pointer|<pre lang="Turtle"><code>:Affordance&#32;a&#32;skos:Concept&#32;;  &#10; &#32; &#32; &#32; &#32;dc:references&#32; &#91;&#32;rdfs:label&#32; &#34;Chemero&#32;and&#32;Turvey,&#32;2007&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;dc:bibliographicCitation&#32; &#34;Chemero,&#32;A.,&#32;&&#32;Turvey,&#32;M.&#32;T.&#32;(2007).&#32;Complexity,&#32;hypersets,&#32;...&#34; &#32;],  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#91;&#32;rdfs:label&#32; &#34;Norman,&#32;2013&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;dc:bibliographicCitation&#32; &#34;Norman,&#32;D.&#32;(2013).&#32;The&#32;design&#32;of&#32;everyday&#32;things:&#32;Revised&#32;an...&#34; &#32;]&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32;:core&#32;;  &#10; &#32; &#32; &#32; &#32;skos:definition&#32; &#34;A&#32;behavior&#32;possibility&#32;that&#32;is&#32;a&#32;relationship&#32;between&#32;an&#32;abi...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;skos:editorialNote&#32; &#34;The&#32;concept&#32;has&#32;been&#32;considered&#32;as&#32;a&#32;candidate&#32;term&#32;for&#32;repr...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;skos:historyNote&#32; &#34;The&#32;definition&#32;of&#32;the&#32;concept&#32;follows&#32;affordance&#32;theorists&#32; &#91;...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;skos:prefLabel&#32; &#34;affordance&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;skos:related&#32;:Signifier&#32;.</code></pre>|

***
### MinorFail Outcome number 11

[Jump to summary definition](#summary-MinorFail-11)	|	[Previous MinorFail outcome](#minorfail-outcome-number-10)	|	[Next MinorFail outcome](#minorfail-outcome-number-12)

:exclamation:MinorFail outcome
#### Subject detail
|Name|modelet-manufacturing-environments-discover-signifiers|
|----|----|
|Title|Standalone&#32;modelet&#32;domains&#92;manufacturing-environments&#92;discover-signifiers&#92;onto.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Modelet manufacturing-environments/discover-signifiers](https://github.com/HyperAgents/hmas/blob/HEAD/domains/manufacturing-environments/discover-signifiers/onto.ttl)|

#### Criterion detail
|Identifier|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|
|----|----|
|Title|Profile&#32;compatibility&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;check&#32;whether&#32;the&#32;test&#32;subject&#32;is&#32;compatible&#32;with&#32;a&#32;profile&#32;or&#32;not,&#32;and&#32;if&#32;it&#32;is&#32;not,&#32;why.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-11)|Identifier|`owl-el-profile-error`|
|[Section top](#minorfail-outcome-number-11)|Title|OWL&#32;EL&#32;Profile&#32;incompatible|
|[Section top](#minorfail-outcome-number-11)|Description|Anonymous&#32;individuals&#32;are&#32;not&#32;supported|
|[Section top](#minorfail-outcome-number-11)|Pointer|<pre lang="Turtle"><code>&#91;]&#32;rdfs:label&#32; &#34;Chemero&#32;and&#32;Turvey,&#32;2007&#34;@en&#32;;  &#10; &#32; &#32;&#32; &#32;dc:bibliographicCitation&#32; &#34;Chemero,&#32;A.,&#32;&&#32;Turvey,&#32;M.&#32;T.&#32;(2007).&#32;Complexity,&#32;hypersets,&#32;...&#34; &#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-11)|Pointer|<pre lang="Turtle"><code>&#91;]&#32;rdfs:label&#32; &#34;Norman,&#32;2013&#34;@en&#32;;  &#10; &#32; &#32;&#32; &#32;dc:bibliographicCitation&#32; &#34;Norman,&#32;D.&#32;(2013).&#32;The&#32;design&#32;of&#32;everyday&#32;things:&#32;Revised&#32;an...&#34; &#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-11)|Pointer|<pre lang="Turtle"><code>hmas:Affordance&#32;a&#32;skos:Concept&#32;;  &#10; &#32; &#32; &#32; &#32;dc:references&#32; &#91;&#32;rdfs:label&#32; &#34;Chemero&#32;and&#32;Turvey,&#32;2007&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;dc:bibliographicCitation&#32; &#34;Chemero,&#32;A.,&#32;&&#32;Turvey,&#32;M.&#32;T.&#32;(2007).&#32;Complexity,&#32;hypersets,&#32;...&#34; &#32;],  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#91;&#32;rdfs:label&#32; &#34;Norman,&#32;2013&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;dc:bibliographicCitation&#32; &#34;Norman,&#32;D.&#32;(2013).&#32;The&#32;design&#32;of&#32;everyday&#32;things:&#32;Revised&#32;an...&#34; &#32;]&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32;hmas:core&#32;;  &#10; &#32; &#32; &#32; &#32;skos:definition&#32; &#34;A&#32;behavior&#32;possibility&#32;that&#32;is&#32;a&#32;relationship&#32;between&#32;an&#32;abi...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;skos:editorialNote&#32; &#34;The&#32;concept&#32;has&#32;been&#32;considered&#32;as&#32;a&#32;candidate&#32;term&#32;for&#32;repr...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;skos:historyNote&#32; &#34;The&#32;definition&#32;of&#32;the&#32;concept&#32;follows&#32;affordance&#32;theorists&#32; &#91;...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;skos:prefLabel&#32; &#34;affordance&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;skos:related&#32;hmas:Signifier&#32;.</code></pre>|

***
### MinorFail Outcome number 12

[Jump to summary definition](#summary-MinorFail-12)	|	[Previous MinorFail outcome](#minorfail-outcome-number-11)	|	[Next MinorFail outcome](#minorfail-outcome-number-13)

:exclamation:MinorFail outcome
#### Subject detail
|Name|modelet-manufacturing-environments-discover-signifiers|
|----|----|
|Title|Standalone&#32;modelet&#32;domains&#92;manufacturing-environments&#92;discover-signifiers&#92;onto.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Modelet manufacturing-environments/discover-signifiers](https://github.com/HyperAgents/hmas/blob/HEAD/domains/manufacturing-environments/discover-signifiers/onto.ttl)|

#### Criterion detail
|Identifier|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|
|----|----|
|Title|Profile&#32;compatibility&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;check&#32;whether&#32;the&#32;test&#32;subject&#32;is&#32;compatible&#32;with&#32;a&#32;profile&#32;or&#32;not,&#32;and&#32;if&#32;it&#32;is&#32;not,&#32;why.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-12)|Identifier|`owl-ql-profile-error`|
|[Section top](#minorfail-outcome-number-12)|Title|OWL&#32;QL&#32;Profile&#32;incompatible|
|[Section top](#minorfail-outcome-number-12)|Description|Anonymous&#32;individuals&#32;are&#32;not&#32;supported|
|[Section top](#minorfail-outcome-number-12)|Pointer|<pre lang="Turtle"><code>&#91;]&#32;rdfs:label&#32; &#34;Chemero&#32;and&#32;Turvey,&#32;2007&#34;@en&#32;;  &#10; &#32; &#32;&#32; &#32;dc:bibliographicCitation&#32; &#34;Chemero,&#32;A.,&#32;&&#32;Turvey,&#32;M.&#32;T.&#32;(2007).&#32;Complexity,&#32;hypersets,&#32;...&#34; &#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-12)|Pointer|<pre lang="Turtle"><code>&#91;]&#32;rdfs:label&#32; &#34;Norman,&#32;2013&#34;@en&#32;;  &#10; &#32; &#32;&#32; &#32;dc:bibliographicCitation&#32; &#34;Norman,&#32;D.&#32;(2013).&#32;The&#32;design&#32;of&#32;everyday&#32;things:&#32;Revised&#32;an...&#34; &#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-12)|Pointer|<pre lang="Turtle"><code>hmas:Affordance&#32;a&#32;skos:Concept&#32;;  &#10; &#32; &#32; &#32; &#32;dc:references&#32; &#91;&#32;rdfs:label&#32; &#34;Chemero&#32;and&#32;Turvey,&#32;2007&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;dc:bibliographicCitation&#32; &#34;Chemero,&#32;A.,&#32;&&#32;Turvey,&#32;M.&#32;T.&#32;(2007).&#32;Complexity,&#32;hypersets,&#32;...&#34; &#32;],  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#91;&#32;rdfs:label&#32; &#34;Norman,&#32;2013&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;dc:bibliographicCitation&#32; &#34;Norman,&#32;D.&#32;(2013).&#32;The&#32;design&#32;of&#32;everyday&#32;things:&#32;Revised&#32;an...&#34; &#32;]&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32;hmas:core&#32;;  &#10; &#32; &#32; &#32; &#32;skos:definition&#32; &#34;A&#32;behavior&#32;possibility&#32;that&#32;is&#32;a&#32;relationship&#32;between&#32;an&#32;abi...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;skos:editorialNote&#32; &#34;The&#32;concept&#32;has&#32;been&#32;considered&#32;as&#32;a&#32;candidate&#32;term&#32;for&#32;repr...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;skos:historyNote&#32; &#34;The&#32;definition&#32;of&#32;the&#32;concept&#32;follows&#32;affordance&#32;theorists&#32; &#91;...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;skos:prefLabel&#32; &#34;affordance&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;skos:related&#32;hmas:Signifier&#32;.</code></pre>|

***
### MinorFail Outcome number 13

[Jump to summary definition](#summary-MinorFail-13)	|	[Previous MinorFail outcome](#minorfail-outcome-number-12)	|	[Next MinorFail outcome](#minorfail-outcome-number-14)

:exclamation:MinorFail outcome
#### Subject detail
|Name|modelet-manufacturing-environments-discover-platforms|
|----|----|
|Title|Standalone&#32;modelet&#32;domains&#92;manufacturing-environments&#92;discover-platforms&#92;onto.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Modelet manufacturing-environments/discover-platforms](https://github.com/HyperAgents/hmas/blob/HEAD/domains/manufacturing-environments/discover-platforms/onto.ttl)|

#### Criterion detail
|Identifier|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|
|----|----|
|Title|Profile&#32;compatibility&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;check&#32;whether&#32;the&#32;test&#32;subject&#32;is&#32;compatible&#32;with&#32;a&#32;profile&#32;or&#32;not,&#32;and&#32;if&#32;it&#32;is&#32;not,&#32;why.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-13)|Identifier|`owl-el-profile-error`|
|[Section top](#minorfail-outcome-number-13)|Title|OWL&#32;EL&#32;Profile&#32;incompatible|
|[Section top](#minorfail-outcome-number-13)|Description|Statement&#32;not&#32;supported|
|[Section top](#minorfail-outcome-number-13)|Pointer|<pre lang="Turtle"><code>hmas:hosts&#32;a&#32;owl:AsymmetricProperty,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:ObjectProperty&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;hosts&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;dc:source&#32; &#60;https://github.com/HyperAgents/ns.hyperagents.org/issues/8#issuecomment-1025991719> &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;A&#32;relation&#32;that&#32;refers&#32;to&#32;an&#32;information&#32;resource&#32;or&#32;a&#32;proce...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:domain&#32;hmas:HypermediaMASPlatform&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32;hmas:core&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:range&#32;hmas:Hostable&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:seeAlso&#32; &#60;https://github.com/HyperAgents/ns.hyperagents.org/issues/18>,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#60;https://github.com/HyperAgents/ns.hyperagents.org/issues/49> &#32;.</code></pre>|

***
### MinorFail Outcome number 14

[Jump to summary definition](#summary-MinorFail-14)	|	[Previous MinorFail outcome](#minorfail-outcome-number-13)	|	[Next MinorFail outcome](#minorfail-outcome-number-15)

:exclamation:MinorFail outcome
#### Subject detail
|Name|modelet-manufacturing-environments-discover-core|
|----|----|
|Title|Standalone&#32;modelet&#32;domains&#92;manufacturing-environments&#92;discover-core&#92;onto.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Modelet manufacturing-environments/discover-core](https://github.com/HyperAgents/hmas/blob/HEAD/domains/manufacturing-environments/discover-core/onto.ttl)|

#### Criterion detail
|Identifier|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|
|----|----|
|Title|Profile&#32;compatibility&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;check&#32;whether&#32;the&#32;test&#32;subject&#32;is&#32;compatible&#32;with&#32;a&#32;profile&#32;or&#32;not,&#32;and&#32;if&#32;it&#32;is&#32;not,&#32;why.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-14)|Identifier|`owl-el-profile-error`|
|[Section top](#minorfail-outcome-number-14)|Title|OWL&#32;EL&#32;Profile&#32;incompatible|
|[Section top](#minorfail-outcome-number-14)|Description|Statement&#32;not&#32;supported|
|[Section top](#minorfail-outcome-number-14)|Pointer|<pre lang="Turtle"><code>hmas:hasProfile&#32;a&#32;owl:AsymmetricProperty,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:ObjectProperty&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;has&#32;profile&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;A&#32;relation&#32;that&#32;links&#32;a&#32;resource&#32;to&#32;its&#32;profile.&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32;hmas:core&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:range&#32;hmas:ResourceProfile&#32;;  &#10; &#32; &#32; &#32; &#32;owl:inverseOf&#32;hmas:isProfileOf&#32;.</code></pre>|

***
### MinorFail Outcome number 15

[Jump to summary definition](#summary-MinorFail-15)	|	[Previous MinorFail outcome](#minorfail-outcome-number-14)	|	[Next MinorFail outcome](#minorfail-outcome-number-16)

:exclamation:MinorFail outcome
#### Subject detail
|Name|modelet-manufacturing-environments-discover-core|
|----|----|
|Title|Standalone&#32;modelet&#32;domains&#92;manufacturing-environments&#92;discover-core&#92;onto.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Modelet manufacturing-environments/discover-core](https://github.com/HyperAgents/hmas/blob/HEAD/domains/manufacturing-environments/discover-core/onto.ttl)|

#### Criterion detail
|Identifier|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|
|----|----|
|Title|Profile&#32;compatibility&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;check&#32;whether&#32;the&#32;test&#32;subject&#32;is&#32;compatible&#32;with&#32;a&#32;profile&#32;or&#32;not,&#32;and&#32;if&#32;it&#32;is&#32;not,&#32;why.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-15)|Identifier|`owl-ql-profile-error`|
|[Section top](#minorfail-outcome-number-15)|Title|OWL&#32;QL&#32;Profile&#32;incompatible|
|[Section top](#minorfail-outcome-number-15)|Description|Statement&#32;not&#32;supported|
|[Section top](#minorfail-outcome-number-15)|Pointer|<pre lang="Turtle"><code>hmas:transitivelyContains&#32;a&#32;owl:ObjectProperty,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:TransitiveProperty&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;transitivelyContains&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;Links&#32;all&#32;the&#32;resources&#32;that&#32;are&#32;logically&#32;contained&#32;in&#32;a&#32;wo...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:domain&#32;hmas:Workspace&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32;hmas:core&#32;;  &#10; &#32; &#32; &#32; &#32;owl:inverseOf&#32;hmas:isTransitivelyContainedIn&#32;.</code></pre>|

***
### MinorFail Outcome number 16

[Jump to summary definition](#summary-MinorFail-16)	|	[Previous MinorFail outcome](#minorfail-outcome-number-15)	|	[Next MinorFail outcome](#minorfail-outcome-number-17)

:exclamation:MinorFail outcome
#### Subject detail
|Name|modelet-logistics-configure-organization|
|----|----|
|Title|Standalone&#32;modelet&#32;domains&#92;logistics&#92;configure-organization&#92;onto.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Modelet logistics/configure-organization](https://github.com/HyperAgents/hmas/blob/HEAD/domains/logistics/configure-organization/onto.ttl)|

#### Criterion detail
|Identifier|[terms-differenciation](https://ns.inria.fr/olivaw#terms-differenciation)|
|----|----|
|Title|Terms&#32;differenciation&#32;test|
|Description|A&#32;test&#32;case&#32;from&#32;the&#32;Best&#32;Practices&#32;tests&#32;checking&#32;if&#32;all&#32;the&#32;terms&#32;are&#32;different&#32;enough&#32;from&#32;each&#32;other&#32;according&#32;to&#32;the&#32;Levenshtein&#32;distance&#32;metric.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-16)|Identifier|`too-close-terms`|
|[Section top](#minorfail-outcome-number-16)|Title|Too&#32;close&#32;terms|
|[Section top](#minorfail-outcome-number-16)|Description|Some&#32;terms&#32;are&#32;too&#32;similar|
|[Section top](#minorfail-outcome-number-16)|Pointer|<pre lang="Turtle"><code>:isAccessTo&#32;a&#32;owl:ObjectProperty&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;is&#32;access&#32;to&#34;@en,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#34;est&#32;l'accès&#32;à&#34;@fr&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;A&#32;relation&#32;that&#32;refers&#32;to&#32;an&#32;Artifact&#32;involved&#32;in&#32;an&#32;Access.&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:domain&#32;:Access&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32;:regulation&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:range&#32;:Artifact&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-16)|Pointer|<pre lang="Turtle"><code>:isAccessOf&#32;a&#32;owl:ObjectProperty&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;is&#32;access&#32;of&#34;@en,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#34;est&#32;l'accès&#32;de&#34;@fr&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;A&#32;relation&#32;that&#32;refers&#32;to&#32;an&#32;Agent&#32;involved&#32;in&#32;an&#32;Access.&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:domain&#32;:Access&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32;:regulation&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:range&#32;:Agent&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-16)|Pointer|<pre lang="Turtle"><code>:isAccessFor&#32;a&#32;owl:ObjectProperty&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;is&#32;access&#32;for&#34;@en,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#34;est&#32;l'accès&#32;pour&#34;@fr&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;A&#32;relation&#32;that&#32;refers&#32;to&#32;a&#32;Usage&#32;involved&#32;in&#32;an&#32;Access.&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:domain&#32;:Access&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32;:regulation&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:range&#32;:Usage&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-16)|Pointer|<pre lang="Turtle"><code>:isUsageOf&#32;a&#32;owl:ObjectProperty&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;is&#32;usage&#32;of&#34;@en,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#34;est&#32;un&#32;usage&#32;de&#34;@fr&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;A&#32;relation&#32;that&#32;refers&#32;to&#32;a&#32;Facility&#32;involved&#32;in&#32;a&#32;Usage.&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:domain&#32;:Usage&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32;:regulation&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:range&#32;:Facility&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-16)|Pointer|<pre lang="Turtle"><code>:isUsageIn&#32;a&#32;owl:ObjectProperty&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;is&#32;usage&#32;in&#34;@en,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#34;est&#32;un&#32;usage&#32;dans&#34;@fr&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;A&#32;relation&#32;that&#32;refers&#32;to&#32;a&#32;Setting&#32;involved&#32;in&#32;a&#32;Usage.&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:domain&#32;:Usage&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32;:regulation&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:range&#32;:Setting&#32;.</code></pre>|

***
### MinorFail Outcome number 17

[Jump to summary definition](#summary-MinorFail-17)	|	[Previous MinorFail outcome](#minorfail-outcome-number-16)	|	[Next MinorFail outcome](#minorfail-outcome-number-18)

:exclamation:MinorFail outcome
#### Subject detail
|Name|all-modules|
|----|----|
|Title|All&#32;the&#32;modules&#32;from&#32;branch&#32;HEAD&#32;that&#32;are&#32;syntaxically&#32;correct&#32;as&#32;well&#32;as&#32;their&#32;recursive&#32;imports|
|Composition|- [Module alignment/interaction-td](https://github.com/HyperAgents/hmas/blob/HEAD/src/alignment/interaction-td.ttl)<br/>- [Module core](https://github.com/HyperAgents/hmas/blob/HEAD/src/core.ttl)<br/>- [Module fipa](https://github.com/HyperAgents/hmas/blob/HEAD/src/fipa.ttl)<br/>- [Module interaction](https://github.com/HyperAgents/hmas/blob/HEAD/src/interaction.ttl)<br/>- [Module regulation](https://github.com/HyperAgents/hmas/blob/HEAD/src/regulation.ttl)|

#### Criterion detail
|Identifier|[labeled-terms](https://ns.inria.fr/olivaw#labeled-terms)|
|----|----|
|Title|Term&#32;labeling&#32;test|
|Description|A&#32;test&#32;case&#32;from&#32;the&#32;Best&#32;Practices&#32;tests&#32;checking&#32;if&#32;all&#32;the&#32;terms&#32;of&#32;the&#32;subject&#32;have&#32;a&#32;rdfs:label&#32;property&#32;pointing&#32;to&#32;a&#32;literal&#32;in&#32;English|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-17)|Identifier|`not-labeled-term`|
|[Section top](#minorfail-outcome-number-17)|Title|Terms&#32;not&#32;labeled|
|[Section top](#minorfail-outcome-number-17)|Description|The&#32;following&#32;terms&#32;have&#32;no&#32;rdfs:label&#32;to&#32;define&#32;it&#32;in&#32;natural&#32;language|
|[Section top](#minorfail-outcome-number-17)|Pointer|<pre lang="Turtle"><code>:Affordance&#32;a&#32;skos:Concept&#32;;  &#10; &#32; &#32; &#32; &#32;dc:references&#32; &#91;&#32;a&#32;owl:NamedIndividual&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;Chemero&#32;and&#32;Turvey,&#32;2007&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;dc:bibliographicCitation&#32; &#34;Chemero,&#32;A.,&#32;&&#32;Turvey,&#32;M.&#32;T.&#32;(2007).&#32;Complexity,&#32;hypersets,&#32;...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;dc:identifier&#32; &#60;https://doi.org/10.1162/biot.2007.2.1.23> &#32;],  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#91;&#32;a&#32;owl:NamedIndividual&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;Norman,&#32;2013&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;dc:bibliographicCitation&#32; &#34;Norman,&#32;D.&#32;(2013).&#32;The&#32;design&#32;of&#32;everyday&#32;things:&#32;Revised&#32;an...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;dc:identifier&#32; &#60;https://mitpress.mit.edu/9780262640374/> &#32;]&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32;:core&#32;;  &#10; &#32; &#32; &#32; &#32;skos:definition&#32; &#34;A&#32;behavior&#32;possibility&#32;that&#32;is&#32;a&#32;relationship&#32;between&#32;an&#32;abi...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;skos:editorialNote&#32; &#34;The&#32;concept&#32;has&#32;been&#32;considered&#32;as&#32;a&#32;candidate&#32;term&#32;for&#32;repr...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;skos:historyNote&#32; &#34;The&#32;definition&#32;of&#32;the&#32;concept&#32;follows&#32;affordance&#32;theorists&#32; &#91;...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;skos:prefLabel&#32; &#34;affordance&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;skos:related&#32;:Signifier&#32;.</code></pre>|

***
### MinorFail Outcome number 18

[Jump to summary definition](#summary-MinorFail-18)	|	[Previous MinorFail outcome](#minorfail-outcome-number-17)	|	[Next MinorFail outcome](#minorfail-outcome-number-19)

:exclamation:MinorFail outcome
#### Subject detail
|Name|all-modules|
|----|----|
|Title|All&#32;the&#32;modules&#32;from&#32;branch&#32;HEAD&#32;that&#32;are&#32;syntaxically&#32;correct&#32;as&#32;well&#32;as&#32;their&#32;recursive&#32;imports|
|Composition|- [Module alignment/interaction-td](https://github.com/HyperAgents/hmas/blob/HEAD/src/alignment/interaction-td.ttl)<br/>- [Module core](https://github.com/HyperAgents/hmas/blob/HEAD/src/core.ttl)<br/>- [Module fipa](https://github.com/HyperAgents/hmas/blob/HEAD/src/fipa.ttl)<br/>- [Module interaction](https://github.com/HyperAgents/hmas/blob/HEAD/src/interaction.ttl)<br/>- [Module regulation](https://github.com/HyperAgents/hmas/blob/HEAD/src/regulation.ttl)|

#### Criterion detail
|Identifier|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|
|----|----|
|Title|Profile&#32;compatibility&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;check&#32;whether&#32;the&#32;test&#32;subject&#32;is&#32;compatible&#32;with&#32;a&#32;profile&#32;or&#32;not,&#32;and&#32;if&#32;it&#32;is&#32;not,&#32;why.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-18)|Identifier|`owl-el-profile-error`|
|[Section top](#minorfail-outcome-number-18)|Title|OWL&#32;EL&#32;Profile&#32;incompatible|
|[Section top](#minorfail-outcome-number-18)|Description|Anonymous&#32;individuals&#32;are&#32;not&#32;supported|
|[Section top](#minorfail-outcome-number-18)|Pointer|<pre lang="Turtle"><code>&#91;]&#32;a&#32;owl:NamedIndividual&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;Chemero&#32;and&#32;Turvey,&#32;2007&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;dc:bibliographicCitation&#32; &#34;Chemero,&#32;A.,&#32;&&#32;Turvey,&#32;M.&#32;T.&#32;(2007).&#32;Complexity,&#32;hypersets,&#32;...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;dc:identifier&#32; &#60;https://doi.org/10.1162/biot.2007.2.1.23> &#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-18)|Pointer|<pre lang="Turtle"><code>&#91;]&#32;a&#32;owl:NamedIndividual&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;Norman,&#32;2013&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;dc:bibliographicCitation&#32; &#34;Norman,&#32;D.&#32;(2013).&#32;The&#32;design&#32;of&#32;everyday&#32;things:&#32;Revised&#32;an...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;dc:identifier&#32; &#60;https://mitpress.mit.edu/9780262640374/> &#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-18)|Pointer|<pre lang="Turtle"><code>hmas:Affordance&#32;a&#32;skos:Concept&#32;;  &#10; &#32; &#32; &#32; &#32;dc:references&#32; &#91;&#32;a&#32;owl:NamedIndividual&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;Chemero&#32;and&#32;Turvey,&#32;2007&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;dc:bibliographicCitation&#32; &#34;Chemero,&#32;A.,&#32;&&#32;Turvey,&#32;M.&#32;T.&#32;(2007).&#32;Complexity,&#32;hypersets,&#32;...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;dc:identifier&#32; &#60;https://doi.org/10.1162/biot.2007.2.1.23> &#32;],  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#91;&#32;a&#32;owl:NamedIndividual&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;Norman,&#32;2013&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;dc:bibliographicCitation&#32; &#34;Norman,&#32;D.&#32;(2013).&#32;The&#32;design&#32;of&#32;everyday&#32;things:&#32;Revised&#32;an...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;dc:identifier&#32; &#60;https://mitpress.mit.edu/9780262640374/> &#32;]&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32;hmas:core&#32;;  &#10; &#32; &#32; &#32; &#32;skos:definition&#32; &#34;A&#32;behavior&#32;possibility&#32;that&#32;is&#32;a&#32;relationship&#32;between&#32;an&#32;abi...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;skos:editorialNote&#32; &#34;The&#32;concept&#32;has&#32;been&#32;considered&#32;as&#32;a&#32;candidate&#32;term&#32;for&#32;repr...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;skos:historyNote&#32; &#34;The&#32;definition&#32;of&#32;the&#32;concept&#32;follows&#32;affordance&#32;theorists&#32; &#91;...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;skos:prefLabel&#32; &#34;affordance&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;skos:related&#32;hmas:Signifier&#32;.</code></pre>|

***
### MinorFail Outcome number 19

[Jump to summary definition](#summary-MinorFail-19)	|	[Previous MinorFail outcome](#minorfail-outcome-number-18)	|	[Next MinorFail outcome](#minorfail-outcome-number-20)

:exclamation:MinorFail outcome
#### Subject detail
|Name|all-modules|
|----|----|
|Title|All&#32;the&#32;modules&#32;from&#32;branch&#32;HEAD&#32;that&#32;are&#32;syntaxically&#32;correct&#32;as&#32;well&#32;as&#32;their&#32;recursive&#32;imports|
|Composition|- [Module alignment/interaction-td](https://github.com/HyperAgents/hmas/blob/HEAD/src/alignment/interaction-td.ttl)<br/>- [Module core](https://github.com/HyperAgents/hmas/blob/HEAD/src/core.ttl)<br/>- [Module fipa](https://github.com/HyperAgents/hmas/blob/HEAD/src/fipa.ttl)<br/>- [Module interaction](https://github.com/HyperAgents/hmas/blob/HEAD/src/interaction.ttl)<br/>- [Module regulation](https://github.com/HyperAgents/hmas/blob/HEAD/src/regulation.ttl)|

#### Criterion detail
|Identifier|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|
|----|----|
|Title|Profile&#32;compatibility&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;check&#32;whether&#32;the&#32;test&#32;subject&#32;is&#32;compatible&#32;with&#32;a&#32;profile&#32;or&#32;not,&#32;and&#32;if&#32;it&#32;is&#32;not,&#32;why.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-19)|Identifier|`owl-el-profile-error`|
|[Section top](#minorfail-outcome-number-19)|Title|OWL&#32;EL&#32;Profile&#32;incompatible|
|[Section top](#minorfail-outcome-number-19)|Description|Statement&#32;not&#32;supported|
|[Section top](#minorfail-outcome-number-19)|Pointer|<pre lang="Turtle"><code>hmas:hasProfile&#32;a&#32;owl:AsymmetricProperty,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:ObjectProperty&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;has&#32;for&#32;profile&#34;@en,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#34;a&#32;pour&#32;profil&#34;@fr&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;A&#32;relation&#32;that&#32;links&#32;a&#32;resource&#32;to&#32;its&#32;profile.&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32;hmas:core&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:range&#32;hmas:ResourceProfile&#32;;  &#10; &#32; &#32; &#32; &#32;owl:inverseOf&#32;hmas:isProfileOf&#32;.</code></pre>|

***
### MinorFail Outcome number 20

[Jump to summary definition](#summary-MinorFail-20)	|	[Previous MinorFail outcome](#minorfail-outcome-number-19)	|	[Next MinorFail outcome](#minorfail-outcome-number-21)

:exclamation:MinorFail outcome
#### Subject detail
|Name|all-modules|
|----|----|
|Title|All&#32;the&#32;modules&#32;from&#32;branch&#32;HEAD&#32;that&#32;are&#32;syntaxically&#32;correct&#32;as&#32;well&#32;as&#32;their&#32;recursive&#32;imports|
|Composition|- [Module alignment/interaction-td](https://github.com/HyperAgents/hmas/blob/HEAD/src/alignment/interaction-td.ttl)<br/>- [Module core](https://github.com/HyperAgents/hmas/blob/HEAD/src/core.ttl)<br/>- [Module fipa](https://github.com/HyperAgents/hmas/blob/HEAD/src/fipa.ttl)<br/>- [Module interaction](https://github.com/HyperAgents/hmas/blob/HEAD/src/interaction.ttl)<br/>- [Module regulation](https://github.com/HyperAgents/hmas/blob/HEAD/src/regulation.ttl)|

#### Criterion detail
|Identifier|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|
|----|----|
|Title|Profile&#32;compatibility&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;check&#32;whether&#32;the&#32;test&#32;subject&#32;is&#32;compatible&#32;with&#32;a&#32;profile&#32;or&#32;not,&#32;and&#32;if&#32;it&#32;is&#32;not,&#32;why.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-20)|Identifier|`owl-ql-profile-error`|
|[Section top](#minorfail-outcome-number-20)|Title|OWL&#32;QL&#32;Profile&#32;incompatible|
|[Section top](#minorfail-outcome-number-20)|Description|Anonymous&#32;individuals&#32;are&#32;not&#32;supported|
|[Section top](#minorfail-outcome-number-20)|Pointer|<pre lang="Turtle"><code>&#91;]&#32;a&#32;owl:NamedIndividual&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;Chemero&#32;and&#32;Turvey,&#32;2007&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;dc:bibliographicCitation&#32; &#34;Chemero,&#32;A.,&#32;&&#32;Turvey,&#32;M.&#32;T.&#32;(2007).&#32;Complexity,&#32;hypersets,&#32;...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;dc:identifier&#32; &#60;https://doi.org/10.1162/biot.2007.2.1.23> &#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-20)|Pointer|<pre lang="Turtle"><code>&#91;]&#32;a&#32;owl:NamedIndividual&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;Norman,&#32;2013&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;dc:bibliographicCitation&#32; &#34;Norman,&#32;D.&#32;(2013).&#32;The&#32;design&#32;of&#32;everyday&#32;things:&#32;Revised&#32;an...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;dc:identifier&#32; &#60;https://mitpress.mit.edu/9780262640374/> &#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-20)|Pointer|<pre lang="Turtle"><code>hmas:Affordance&#32;a&#32;skos:Concept&#32;;  &#10; &#32; &#32; &#32; &#32;dc:references&#32; &#91;&#32;a&#32;owl:NamedIndividual&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;Chemero&#32;and&#32;Turvey,&#32;2007&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;dc:bibliographicCitation&#32; &#34;Chemero,&#32;A.,&#32;&&#32;Turvey,&#32;M.&#32;T.&#32;(2007).&#32;Complexity,&#32;hypersets,&#32;...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;dc:identifier&#32; &#60;https://doi.org/10.1162/biot.2007.2.1.23> &#32;],  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#91;&#32;a&#32;owl:NamedIndividual&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;Norman,&#32;2013&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;dc:bibliographicCitation&#32; &#34;Norman,&#32;D.&#32;(2013).&#32;The&#32;design&#32;of&#32;everyday&#32;things:&#32;Revised&#32;an...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;dc:identifier&#32; &#60;https://mitpress.mit.edu/9780262640374/> &#32;]&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32;hmas:core&#32;;  &#10; &#32; &#32; &#32; &#32;skos:definition&#32; &#34;A&#32;behavior&#32;possibility&#32;that&#32;is&#32;a&#32;relationship&#32;between&#32;an&#32;abi...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;skos:editorialNote&#32; &#34;The&#32;concept&#32;has&#32;been&#32;considered&#32;as&#32;a&#32;candidate&#32;term&#32;for&#32;repr...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;skos:historyNote&#32; &#34;The&#32;definition&#32;of&#32;the&#32;concept&#32;follows&#32;affordance&#32;theorists&#32; &#91;...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;skos:prefLabel&#32; &#34;affordance&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;skos:related&#32;hmas:Signifier&#32;.</code></pre>|

***
### MinorFail Outcome number 21

[Jump to summary definition](#summary-MinorFail-21)	|	[Previous MinorFail outcome](#minorfail-outcome-number-20)	|	[Next MinorFail outcome](#minorfail-outcome-number-22)

:exclamation:MinorFail outcome
#### Subject detail
|Name|all-modules|
|----|----|
|Title|All&#32;the&#32;modules&#32;from&#32;branch&#32;HEAD&#32;that&#32;are&#32;syntaxically&#32;correct&#32;as&#32;well&#32;as&#32;their&#32;recursive&#32;imports|
|Composition|- [Module alignment/interaction-td](https://github.com/HyperAgents/hmas/blob/HEAD/src/alignment/interaction-td.ttl)<br/>- [Module core](https://github.com/HyperAgents/hmas/blob/HEAD/src/core.ttl)<br/>- [Module fipa](https://github.com/HyperAgents/hmas/blob/HEAD/src/fipa.ttl)<br/>- [Module interaction](https://github.com/HyperAgents/hmas/blob/HEAD/src/interaction.ttl)<br/>- [Module regulation](https://github.com/HyperAgents/hmas/blob/HEAD/src/regulation.ttl)|

#### Criterion detail
|Identifier|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|
|----|----|
|Title|Profile&#32;compatibility&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;check&#32;whether&#32;the&#32;test&#32;subject&#32;is&#32;compatible&#32;with&#32;a&#32;profile&#32;or&#32;not,&#32;and&#32;if&#32;it&#32;is&#32;not,&#32;why.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-21)|Identifier|`owl-ql-profile-error`|
|[Section top](#minorfail-outcome-number-21)|Title|OWL&#32;QL&#32;Profile&#32;incompatible|
|[Section top](#minorfail-outcome-number-21)|Description|Class&#32;Expression&#32;not&#32;supported&#32;with&#32;rdfs:subClassOf|
|[Section top](#minorfail-outcome-number-21)|Pointer|<pre lang="Turtle"><code>&#60;https://www.w3.org/2019/wot/td#InteractionAffordance> &#32;rdfs:comment&#32; &#34;Using&#32;a&#32;TD&#32;Interaction&#32;Affordance&#32;results&#32;in&#32;an&#32;action&#32;execu...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:subClassOf&#32; &#91;&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:hasValue&#32;hmas:ActionExecution&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:onProperty&#32;sh:class&#32;]&#32;.</code></pre>|

***
### MinorFail Outcome number 22

[Jump to summary definition](#summary-MinorFail-22)	|	[Previous MinorFail outcome](#minorfail-outcome-number-21)	|	[Next MinorFail outcome](#minorfail-outcome-number-23)

:exclamation:MinorFail outcome
#### Subject detail
|Name|all-modules|
|----|----|
|Title|All&#32;the&#32;modules&#32;from&#32;branch&#32;HEAD&#32;that&#32;are&#32;syntaxically&#32;correct&#32;as&#32;well&#32;as&#32;their&#32;recursive&#32;imports|
|Composition|- [Module alignment/interaction-td](https://github.com/HyperAgents/hmas/blob/HEAD/src/alignment/interaction-td.ttl)<br/>- [Module core](https://github.com/HyperAgents/hmas/blob/HEAD/src/core.ttl)<br/>- [Module fipa](https://github.com/HyperAgents/hmas/blob/HEAD/src/fipa.ttl)<br/>- [Module interaction](https://github.com/HyperAgents/hmas/blob/HEAD/src/interaction.ttl)<br/>- [Module regulation](https://github.com/HyperAgents/hmas/blob/HEAD/src/regulation.ttl)|

#### Criterion detail
|Identifier|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|
|----|----|
|Title|Profile&#32;compatibility&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;check&#32;whether&#32;the&#32;test&#32;subject&#32;is&#32;compatible&#32;with&#32;a&#32;profile&#32;or&#32;not,&#32;and&#32;if&#32;it&#32;is&#32;not,&#32;why.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-22)|Identifier|`owl-ql-profile-error`|
|[Section top](#minorfail-outcome-number-22)|Title|OWL&#32;QL&#32;Profile&#32;incompatible|
|[Section top](#minorfail-outcome-number-22)|Description|Statement&#32;not&#32;supported  &#10;Statement&#32;not&#32;supported&#32;in&#32;a&#32;Super&#32;Class&#32;Expression|
|[Section top](#minorfail-outcome-number-22)|Pointer|<pre lang="Turtle"><code>&#91;]&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32;owl:hasValue&#32;hmas:ActionExecution&#32;;  &#10; &#32; &#32; &#32; &#32;owl:onProperty&#32;sh:class&#32;.</code></pre>|

***
### MinorFail Outcome number 23

[Jump to summary definition](#summary-MinorFail-23)	|	[Previous MinorFail outcome](#minorfail-outcome-number-22)	|	[Next MinorFail outcome](#minorfail-outcome-number-24)

:exclamation:MinorFail outcome
#### Subject detail
|Name|all-modules|
|----|----|
|Title|All&#32;the&#32;modules&#32;from&#32;branch&#32;HEAD&#32;that&#32;are&#32;syntaxically&#32;correct&#32;as&#32;well&#32;as&#32;their&#32;recursive&#32;imports|
|Composition|- [Module alignment/interaction-td](https://github.com/HyperAgents/hmas/blob/HEAD/src/alignment/interaction-td.ttl)<br/>- [Module core](https://github.com/HyperAgents/hmas/blob/HEAD/src/core.ttl)<br/>- [Module fipa](https://github.com/HyperAgents/hmas/blob/HEAD/src/fipa.ttl)<br/>- [Module interaction](https://github.com/HyperAgents/hmas/blob/HEAD/src/interaction.ttl)<br/>- [Module regulation](https://github.com/HyperAgents/hmas/blob/HEAD/src/regulation.ttl)|

#### Criterion detail
|Identifier|[term-referencing](https://ns.inria.fr/olivaw#term-referencing)|
|----|----|
|Title|Term&#32;referencing&#32;test|
|Description|A&#32;test&#32;case&#32;from&#32;the&#32;Best&#32;Practices&#32;tests&#32;checking&#32;if&#32;each&#32;term&#32;of&#32;the&#32;test&#32;subject&#32;is&#32;referenced&#32;to&#32;a&#32;module&#32;through&#32;a&#32;rdfs:isDefinedBy&#32;property.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-23)|Identifier|`no-reference-module`|
|[Section top](#minorfail-outcome-number-23)|Title|Term&#32;not&#32;referenced&#32;to&#32;a&#32;module|
|[Section top](#minorfail-outcome-number-23)|Description|Subject&#32;terms&#32;not&#32;linked&#32;to&#32;a&#32;module&#32;by&#32;a&#32;rdfs:isDefinedBy&#32;property|
|[Section top](#minorfail-outcome-number-23)|Pointer|<pre lang="Turtle"><code>:hasServiceName&#32;a&#32;owl:ObjectProperty&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;has&#32;Service&#32;Name&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:domain&#32;:APService&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-23)|Pointer|<pre lang="Turtle"><code>:APService&#32;a&#32;owl:Class&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;Agent&#32;Platform&#32;Service&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;A&#32;service&#32;exposed&#32;by&#32;a&#32;FIPA&#32;Agent&#32;Platform&#32;as&#32;defined&#32;by&#32;the...&#34; &#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-23)|Pointer|<pre lang="Turtle"><code>:hasServiceType&#32;a&#32;owl:ObjectProperty&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;has&#32;Service&#32;Type&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:domain&#32;:APService&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-23)|Pointer|<pre lang="Turtle"><code>:AgentIdentifierDescription&#32;a&#32;owl:Class&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;Agent&#32;Identifier&#32;Description&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;A&#32;resource&#32;profile&#32;that&#32;describes&#32;an&#32;agent&#32;using&#32;the&#32;Agent&#32;I...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:subClassOf&#32; &#60;https://ci.mines-stetienne.fr/hmas#ResourceProfile> &#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-23)|Pointer|<pre lang="Turtle"><code>:AgentPlatformDescription&#32;a&#32;owl:Class&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;Agent&#32;Platform&#32;Description&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;A&#32;resource&#32;profile&#32;that&#32;descripe&#32;a&#32;FIPA&#32;Agent&#32;Platform&#32;using...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:subClassOf&#32; &#60;https://ci.mines-stetienne.fr/hmas#ResourceProfile> &#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-23)|Pointer|<pre lang="Turtle"><code>:FIPAAgentPlatform&#32;a&#32;owl:Class&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;FIPA&#32;Agent&#32;Platform&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;A&#32;platform&#32;that&#32;conforms&#32;to&#32;the&#32;FIPA&#32;Abstract&#32;Architecture&#32;S...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:subClassOf&#32; &#60;https://ci.mines-stetienne.fr/hmas#Platform> &#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-23)|Pointer|<pre lang="Turtle"><code>:HTTPMessageTransportService&#32;a&#32;owl:Class&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;HTTP&#32;Message&#32;Transport&#32;Service&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;An&#32;HTTP-based&#32;message&#32;transport&#32;service&#32;that&#32;confirms&#32;to&#32;the...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:subClassOf&#32;:MessageTransportService&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-23)|Pointer|<pre lang="Turtle"><code>:MessageTransportService&#32;a&#32;owl:Class&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;Message&#32;Transport&#32;Service&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;A&#32;service&#32;for&#32;transporting&#32;messages&#32;among&#32;agents&#32;that&#32;confor...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:subClassOf&#32;:APService&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-23)|Pointer|<pre lang="Turtle"><code>:IIOPMessageTransportService&#32;a&#32;owl:Class&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;IIOP&#32;Message&#32;Transport&#32;Service&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;An&#32;HTTP-based&#32;message&#32;transport&#32;service&#32;that&#32;confirms&#32;to&#32;the...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:subClassOf&#32;:MessageTransportService&#32;.</code></pre>|

***
### MinorFail Outcome number 24

[Jump to summary definition](#summary-MinorFail-24)	|	[Previous MinorFail outcome](#minorfail-outcome-number-23)	|	[Next MinorFail outcome](#minorfail-outcome-number-25)

:exclamation:MinorFail outcome
#### Subject detail
|Name|all-modules|
|----|----|
|Title|All&#32;the&#32;modules&#32;from&#32;branch&#32;HEAD&#32;that&#32;are&#32;syntaxically&#32;correct&#32;as&#32;well&#32;as&#32;their&#32;recursive&#32;imports|
|Composition|- [Module alignment/interaction-td](https://github.com/HyperAgents/hmas/blob/HEAD/src/alignment/interaction-td.ttl)<br/>- [Module core](https://github.com/HyperAgents/hmas/blob/HEAD/src/core.ttl)<br/>- [Module fipa](https://github.com/HyperAgents/hmas/blob/HEAD/src/fipa.ttl)<br/>- [Module interaction](https://github.com/HyperAgents/hmas/blob/HEAD/src/interaction.ttl)<br/>- [Module regulation](https://github.com/HyperAgents/hmas/blob/HEAD/src/regulation.ttl)|

#### Criterion detail
|Identifier|[terms-differenciation](https://ns.inria.fr/olivaw#terms-differenciation)|
|----|----|
|Title|Terms&#32;differenciation&#32;test|
|Description|A&#32;test&#32;case&#32;from&#32;the&#32;Best&#32;Practices&#32;tests&#32;checking&#32;if&#32;all&#32;the&#32;terms&#32;are&#32;different&#32;enough&#32;from&#32;each&#32;other&#32;according&#32;to&#32;the&#32;Levenshtein&#32;distance&#32;metric.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-24)|Identifier|`too-close-terms`|
|[Section top](#minorfail-outcome-number-24)|Title|Too&#32;close&#32;terms|
|[Section top](#minorfail-outcome-number-24)|Description|Some&#32;terms&#32;are&#32;too&#32;similar|
|[Section top](#minorfail-outcome-number-24)|Pointer|<pre lang="Turtle"><code>:isAccessTo&#32;a&#32;owl:ObjectProperty&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;is&#32;access&#32;to&#34;@en,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#34;est&#32;l'accès&#32;à&#34;@fr&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;A&#32;relation&#32;that&#32;refers&#32;to&#32;an&#32;Artifact&#32;involved&#32;in&#32;an&#32;Access.&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:domain&#32;:Access&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32;:regulation&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:range&#32;:Artifact&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-24)|Pointer|<pre lang="Turtle"><code>:isAccessOf&#32;a&#32;owl:ObjectProperty&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;is&#32;access&#32;of&#34;@en,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#34;est&#32;l'accès&#32;de&#34;@fr&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;A&#32;relation&#32;that&#32;refers&#32;to&#32;an&#32;Agent&#32;involved&#32;in&#32;an&#32;Access.&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:domain&#32;:Access&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32;:regulation&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:range&#32;:Agent&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-24)|Pointer|<pre lang="Turtle"><code>:isAccessFor&#32;a&#32;owl:ObjectProperty&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;is&#32;access&#32;for&#34;@en,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#34;est&#32;l'accès&#32;pour&#34;@fr&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;A&#32;relation&#32;that&#32;refers&#32;to&#32;a&#32;Usage&#32;involved&#32;in&#32;an&#32;Access.&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:domain&#32;:Access&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32;:regulation&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:range&#32;:Usage&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-24)|Pointer|<pre lang="Turtle"><code>:isMembershipOf&#32;a&#32;owl:ObjectProperty&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;is&#32;membership&#32;of&#34;@en,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#34;est&#32;l'appartenance&#32;à&#34;@fr&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;A&#32;relation&#32;that&#32;refers&#32;to&#32;the&#32;Agent&#32;involved&#32;in&#32;a&#32;Membership...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:domain&#32;:Membership&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32;:regulation&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:range&#32;:Agent&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-24)|Pointer|<pre lang="Turtle"><code>:isMembershipIn&#32;a&#32;owl:ObjectProperty&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;is&#32;membership&#32;in&#34;@en,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#34;est&#32;l'appartenance&#32;à&#34;@fr&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;A&#32;relation&#32;that&#32;refers&#32;to&#32;the&#32;Group&#32;involved&#32;in&#32;a&#32;Membership...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:domain&#32;:Membership&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32;:regulation&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:range&#32;:Group&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-24)|Pointer|<pre lang="Turtle"><code>:isUsageOf&#32;a&#32;owl:ObjectProperty&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;is&#32;usage&#32;of&#34;@en,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#34;est&#32;un&#32;usage&#32;de&#34;@fr&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;A&#32;relation&#32;that&#32;refers&#32;to&#32;a&#32;Facility&#32;involved&#32;in&#32;a&#32;Usage.&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:domain&#32;:Usage&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32;:regulation&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:range&#32;:Facility&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-24)|Pointer|<pre lang="Turtle"><code>:isUsageIn&#32;a&#32;owl:ObjectProperty&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;is&#32;usage&#32;in&#34;@en,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#34;est&#32;un&#32;usage&#32;dans&#34;@fr&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;A&#32;relation&#32;that&#32;refers&#32;to&#32;a&#32;Setting&#32;involved&#32;in&#32;a&#32;Usage.&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:domain&#32;:Usage&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32;:regulation&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:range&#32;:Setting&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-24)|Pointer|<pre lang="Turtle"><code>:signifies&#32;a&#32;owl:ObjectProperty&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;signifies&#34;@en,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#34;signifie&#34;@fr&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;A&#32;relation&#32;between&#32;a&#32;signifier&#32;and&#32;the&#32;specification&#32;of&#32;a&#32;be...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:domain&#32;:Signifier&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32;:interaction&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-24)|Pointer|<pre lang="Turtle"><code>:Signifier&#32;a&#32;owl:Class&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;signifier&#34;@en,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#34;signifiant&#34;@fr&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;A&#32;perceivable&#32;sign/cue&#32;that&#32;can&#32;be&#32;interpreted&#32;meaningfully&#32;...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32;:core&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:seeAlso&#32; &#60;https://github.com/HyperAgents/ns.hyperagents.org/issues/13#issuecomment-1028904491>,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#60;https://github.com/HyperAgents/ns.hyperagents.org/issues/41> &#32;;  &#10; &#32; &#32; &#32; &#32;skos:note&#32; &#34;:Signifier&#32;works&#32;as&#32;a&#32;bridge&#32;between&#32;the&#32;Core&#32;and&#32;the&#32;Intera...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;skos:related&#32;:Affordance&#32;.</code></pre>|

***
### MinorFail Outcome number 25

[Jump to summary definition](#summary-MinorFail-25)	|	[Previous MinorFail outcome](#minorfail-outcome-number-24)	|	[Next MinorFail outcome](#minorfail-outcome-number-26)

:exclamation:MinorFail outcome
#### Subject detail
|Name|all-fragments|
|----|----|
|Title|All&#32;the&#32;fragments&#32;from&#32;branch&#32;HEAD&#32;that&#32;are&#32;syntaxically&#32;correct&#32;as&#32;well&#32;as&#32;their&#32;recursive&#32;imports|
|Composition|- [Modelet logistics/configure-organization](https://github.com/HyperAgents/hmas/blob/HEAD/domains/logistics/configure-organization/onto.ttl)<br/>- [Modelet logistics/coordinate-activities](https://github.com/HyperAgents/hmas/blob/HEAD/domains/logistics/coordinate-activities/onto.ttl)<br/>- [Modelet logistics/create-organization](https://github.com/HyperAgents/hmas/blob/HEAD/domains/logistics/create-organization/onto.ttl)<br/>- [Modelet manufacturing-environments/discover-behavior-specifications](https://github.com/HyperAgents/hmas/blob/HEAD/domains/manufacturing-environments/discover-behavior-specifications/onto.ttl)<br/>- [Modelet manufacturing-environments/discover-core](https://github.com/HyperAgents/hmas/blob/HEAD/domains/manufacturing-environments/discover-core/onto.ttl)<br/>- [Modelet manufacturing-environments/discover-organization](https://github.com/HyperAgents/hmas/blob/HEAD/domains/manufacturing-environments/discover-organization/onto.ttl)<br/>- [Modelet manufacturing-environments/discover-platforms](https://github.com/HyperAgents/hmas/blob/HEAD/domains/manufacturing-environments/discover-platforms/onto.ttl)<br/>- [Modelet manufacturing-environments/discover-signifiers](https://github.com/HyperAgents/hmas/blob/HEAD/domains/manufacturing-environments/discover-signifiers/onto.ttl)<br/>- [Module alignment/interaction-td](https://github.com/HyperAgents/hmas/blob/HEAD/src/alignment/interaction-td.ttl)<br/>- [Module core](https://github.com/HyperAgents/hmas/blob/HEAD/src/core.ttl)<br/>- [Module fipa](https://github.com/HyperAgents/hmas/blob/HEAD/src/fipa.ttl)<br/>- [Module interaction](https://github.com/HyperAgents/hmas/blob/HEAD/src/interaction.ttl)<br/>- [Module regulation](https://github.com/HyperAgents/hmas/blob/HEAD/src/regulation.ttl)|

#### Criterion detail
|Identifier|[labeled-terms](https://ns.inria.fr/olivaw#labeled-terms)|
|----|----|
|Title|Term&#32;labeling&#32;test|
|Description|A&#32;test&#32;case&#32;from&#32;the&#32;Best&#32;Practices&#32;tests&#32;checking&#32;if&#32;all&#32;the&#32;terms&#32;of&#32;the&#32;subject&#32;have&#32;a&#32;rdfs:label&#32;property&#32;pointing&#32;to&#32;a&#32;literal&#32;in&#32;English|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-25)|Identifier|`not-labeled-term`|
|[Section top](#minorfail-outcome-number-25)|Title|Terms&#32;not&#32;labeled|
|[Section top](#minorfail-outcome-number-25)|Description|The&#32;following&#32;terms&#32;have&#32;no&#32;rdfs:label&#32;to&#32;define&#32;it&#32;in&#32;natural&#32;language|
|[Section top](#minorfail-outcome-number-25)|Pointer|<pre lang="Turtle"><code>:Affordance&#32;a&#32;skos:Concept&#32;;  &#10; &#32; &#32; &#32; &#32;dc:references&#32; &#91;&#32;a&#32;owl:NamedIndividual&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;Chemero&#32;and&#32;Turvey,&#32;2007&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;dc:bibliographicCitation&#32; &#34;Chemero,&#32;A.,&#32;&&#32;Turvey,&#32;M.&#32;T.&#32;(2007).&#32;Complexity,&#32;hypersets,&#32;...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;dc:identifier&#32; &#60;https://doi.org/10.1162/biot.2007.2.1.23> &#32;],  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#91;&#32;a&#32;owl:NamedIndividual&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;Norman,&#32;2013&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;dc:bibliographicCitation&#32; &#34;Norman,&#32;D.&#32;(2013).&#32;The&#32;design&#32;of&#32;everyday&#32;things:&#32;Revised&#32;an...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;dc:identifier&#32; &#60;https://mitpress.mit.edu/9780262640374/> &#32;],  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#91;&#32;rdfs:label&#32; &#34;Chemero&#32;and&#32;Turvey,&#32;2007&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;dc:bibliographicCitation&#32; &#34;Chemero,&#32;A.,&#32;&&#32;Turvey,&#32;M.&#32;T.&#32;(2007).&#32;Complexity,&#32;hypersets,&#32;...&#34; &#32;],  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#91;&#32;rdfs:label&#32; &#34;Norman,&#32;2013&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;dc:bibliographicCitation&#32; &#34;Norman,&#32;D.&#32;(2013).&#32;The&#32;design&#32;of&#32;everyday&#32;things:&#32;Revised&#32;an...&#34; &#32;]&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32;:core&#32;;  &#10; &#32; &#32; &#32; &#32;skos:definition&#32; &#34;A&#32;behavior&#32;possibility&#32;that&#32;is&#32;a&#32;relationship&#32;between&#32;an&#32;abi...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;skos:editorialNote&#32; &#34;The&#32;concept&#32;has&#32;been&#32;considered&#32;as&#32;a&#32;candidate&#32;term&#32;for&#32;repr...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;skos:historyNote&#32; &#34;The&#32;definition&#32;of&#32;the&#32;concept&#32;follows&#32;affordance&#32;theorists&#32; &#91;...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;skos:prefLabel&#32; &#34;affordance&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;skos:related&#32;:Signifier&#32;.</code></pre>|

***
### MinorFail Outcome number 26

[Jump to summary definition](#summary-MinorFail-26)	|	[Previous MinorFail outcome](#minorfail-outcome-number-25)	|	[Next MinorFail outcome](#minorfail-outcome-number-27)

:exclamation:MinorFail outcome
#### Subject detail
|Name|all-fragments|
|----|----|
|Title|All&#32;the&#32;fragments&#32;from&#32;branch&#32;HEAD&#32;that&#32;are&#32;syntaxically&#32;correct&#32;as&#32;well&#32;as&#32;their&#32;recursive&#32;imports|
|Composition|- [Modelet logistics/configure-organization](https://github.com/HyperAgents/hmas/blob/HEAD/domains/logistics/configure-organization/onto.ttl)<br/>- [Modelet logistics/coordinate-activities](https://github.com/HyperAgents/hmas/blob/HEAD/domains/logistics/coordinate-activities/onto.ttl)<br/>- [Modelet logistics/create-organization](https://github.com/HyperAgents/hmas/blob/HEAD/domains/logistics/create-organization/onto.ttl)<br/>- [Modelet manufacturing-environments/discover-behavior-specifications](https://github.com/HyperAgents/hmas/blob/HEAD/domains/manufacturing-environments/discover-behavior-specifications/onto.ttl)<br/>- [Modelet manufacturing-environments/discover-core](https://github.com/HyperAgents/hmas/blob/HEAD/domains/manufacturing-environments/discover-core/onto.ttl)<br/>- [Modelet manufacturing-environments/discover-organization](https://github.com/HyperAgents/hmas/blob/HEAD/domains/manufacturing-environments/discover-organization/onto.ttl)<br/>- [Modelet manufacturing-environments/discover-platforms](https://github.com/HyperAgents/hmas/blob/HEAD/domains/manufacturing-environments/discover-platforms/onto.ttl)<br/>- [Modelet manufacturing-environments/discover-signifiers](https://github.com/HyperAgents/hmas/blob/HEAD/domains/manufacturing-environments/discover-signifiers/onto.ttl)<br/>- [Module alignment/interaction-td](https://github.com/HyperAgents/hmas/blob/HEAD/src/alignment/interaction-td.ttl)<br/>- [Module core](https://github.com/HyperAgents/hmas/blob/HEAD/src/core.ttl)<br/>- [Module fipa](https://github.com/HyperAgents/hmas/blob/HEAD/src/fipa.ttl)<br/>- [Module interaction](https://github.com/HyperAgents/hmas/blob/HEAD/src/interaction.ttl)<br/>- [Module regulation](https://github.com/HyperAgents/hmas/blob/HEAD/src/regulation.ttl)|

#### Criterion detail
|Identifier|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|
|----|----|
|Title|Profile&#32;compatibility&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;check&#32;whether&#32;the&#32;test&#32;subject&#32;is&#32;compatible&#32;with&#32;a&#32;profile&#32;or&#32;not,&#32;and&#32;if&#32;it&#32;is&#32;not,&#32;why.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-26)|Identifier|`owl-el-profile-error`|
|[Section top](#minorfail-outcome-number-26)|Title|OWL&#32;EL&#32;Profile&#32;incompatible|
|[Section top](#minorfail-outcome-number-26)|Description|Anonymous&#32;individuals&#32;are&#32;not&#32;supported|
|[Section top](#minorfail-outcome-number-26)|Pointer|<pre lang="Turtle"><code>&#91;]&#32;a&#32;owl:NamedIndividual&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;Chemero&#32;and&#32;Turvey,&#32;2007&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;dc:bibliographicCitation&#32; &#34;Chemero,&#32;A.,&#32;&&#32;Turvey,&#32;M.&#32;T.&#32;(2007).&#32;Complexity,&#32;hypersets,&#32;...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;dc:identifier&#32; &#60;https://doi.org/10.1162/biot.2007.2.1.23> &#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-26)|Pointer|<pre lang="Turtle"><code>&#91;]&#32;a&#32;owl:NamedIndividual&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;Norman,&#32;2013&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;dc:bibliographicCitation&#32; &#34;Norman,&#32;D.&#32;(2013).&#32;The&#32;design&#32;of&#32;everyday&#32;things:&#32;Revised&#32;an...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;dc:identifier&#32; &#60;https://mitpress.mit.edu/9780262640374/> &#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-26)|Pointer|<pre lang="Turtle"><code>&#91;]&#32;rdfs:label&#32; &#34;Chemero&#32;and&#32;Turvey,&#32;2007&#34;@en&#32;;  &#10; &#32; &#32;&#32; &#32;dc:bibliographicCitation&#32; &#34;Chemero,&#32;A.,&#32;&&#32;Turvey,&#32;M.&#32;T.&#32;(2007).&#32;Complexity,&#32;hypersets,&#32;...&#34; &#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-26)|Pointer|<pre lang="Turtle"><code>&#91;]&#32;rdfs:label&#32; &#34;Norman,&#32;2013&#34;@en&#32;;  &#10; &#32; &#32;&#32; &#32;dc:bibliographicCitation&#32; &#34;Norman,&#32;D.&#32;(2013).&#32;The&#32;design&#32;of&#32;everyday&#32;things:&#32;Revised&#32;an...&#34; &#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-26)|Pointer|<pre lang="Turtle"><code>hmas:Affordance&#32;a&#32;skos:Concept&#32;;  &#10; &#32; &#32; &#32; &#32;dc:references&#32; &#91;&#32;a&#32;owl:NamedIndividual&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;Chemero&#32;and&#32;Turvey,&#32;2007&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;dc:bibliographicCitation&#32; &#34;Chemero,&#32;A.,&#32;&&#32;Turvey,&#32;M.&#32;T.&#32;(2007).&#32;Complexity,&#32;hypersets,&#32;...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;dc:identifier&#32; &#60;https://doi.org/10.1162/biot.2007.2.1.23> &#32;],  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#91;&#32;a&#32;owl:NamedIndividual&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;Norman,&#32;2013&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;dc:bibliographicCitation&#32; &#34;Norman,&#32;D.&#32;(2013).&#32;The&#32;design&#32;of&#32;everyday&#32;things:&#32;Revised&#32;an...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;dc:identifier&#32; &#60;https://mitpress.mit.edu/9780262640374/> &#32;],  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#91;&#32;rdfs:label&#32; &#34;Chemero&#32;and&#32;Turvey,&#32;2007&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;dc:bibliographicCitation&#32; &#34;Chemero,&#32;A.,&#32;&&#32;Turvey,&#32;M.&#32;T.&#32;(2007).&#32;Complexity,&#32;hypersets,&#32;...&#34; &#32;],  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#91;&#32;rdfs:label&#32; &#34;Norman,&#32;2013&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;dc:bibliographicCitation&#32; &#34;Norman,&#32;D.&#32;(2013).&#32;The&#32;design&#32;of&#32;everyday&#32;things:&#32;Revised&#32;an...&#34; &#32;]&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32;hmas:core&#32;;  &#10; &#32; &#32; &#32; &#32;skos:definition&#32; &#34;A&#32;behavior&#32;possibility&#32;that&#32;is&#32;a&#32;relationship&#32;between&#32;an&#32;abi...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;skos:editorialNote&#32; &#34;The&#32;concept&#32;has&#32;been&#32;considered&#32;as&#32;a&#32;candidate&#32;term&#32;for&#32;repr...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;skos:historyNote&#32; &#34;The&#32;definition&#32;of&#32;the&#32;concept&#32;follows&#32;affordance&#32;theorists&#32; &#91;...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;skos:prefLabel&#32; &#34;affordance&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;skos:related&#32;hmas:Signifier&#32;.</code></pre>|

***
### MinorFail Outcome number 27

[Jump to summary definition](#summary-MinorFail-27)	|	[Previous MinorFail outcome](#minorfail-outcome-number-26)	|	[Next MinorFail outcome](#minorfail-outcome-number-28)

:exclamation:MinorFail outcome
#### Subject detail
|Name|all-fragments|
|----|----|
|Title|All&#32;the&#32;fragments&#32;from&#32;branch&#32;HEAD&#32;that&#32;are&#32;syntaxically&#32;correct&#32;as&#32;well&#32;as&#32;their&#32;recursive&#32;imports|
|Composition|- [Modelet logistics/configure-organization](https://github.com/HyperAgents/hmas/blob/HEAD/domains/logistics/configure-organization/onto.ttl)<br/>- [Modelet logistics/coordinate-activities](https://github.com/HyperAgents/hmas/blob/HEAD/domains/logistics/coordinate-activities/onto.ttl)<br/>- [Modelet logistics/create-organization](https://github.com/HyperAgents/hmas/blob/HEAD/domains/logistics/create-organization/onto.ttl)<br/>- [Modelet manufacturing-environments/discover-behavior-specifications](https://github.com/HyperAgents/hmas/blob/HEAD/domains/manufacturing-environments/discover-behavior-specifications/onto.ttl)<br/>- [Modelet manufacturing-environments/discover-core](https://github.com/HyperAgents/hmas/blob/HEAD/domains/manufacturing-environments/discover-core/onto.ttl)<br/>- [Modelet manufacturing-environments/discover-organization](https://github.com/HyperAgents/hmas/blob/HEAD/domains/manufacturing-environments/discover-organization/onto.ttl)<br/>- [Modelet manufacturing-environments/discover-platforms](https://github.com/HyperAgents/hmas/blob/HEAD/domains/manufacturing-environments/discover-platforms/onto.ttl)<br/>- [Modelet manufacturing-environments/discover-signifiers](https://github.com/HyperAgents/hmas/blob/HEAD/domains/manufacturing-environments/discover-signifiers/onto.ttl)<br/>- [Module alignment/interaction-td](https://github.com/HyperAgents/hmas/blob/HEAD/src/alignment/interaction-td.ttl)<br/>- [Module core](https://github.com/HyperAgents/hmas/blob/HEAD/src/core.ttl)<br/>- [Module fipa](https://github.com/HyperAgents/hmas/blob/HEAD/src/fipa.ttl)<br/>- [Module interaction](https://github.com/HyperAgents/hmas/blob/HEAD/src/interaction.ttl)<br/>- [Module regulation](https://github.com/HyperAgents/hmas/blob/HEAD/src/regulation.ttl)|

#### Criterion detail
|Identifier|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|
|----|----|
|Title|Profile&#32;compatibility&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;check&#32;whether&#32;the&#32;test&#32;subject&#32;is&#32;compatible&#32;with&#32;a&#32;profile&#32;or&#32;not,&#32;and&#32;if&#32;it&#32;is&#32;not,&#32;why.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-27)|Identifier|`owl-el-profile-error`|
|[Section top](#minorfail-outcome-number-27)|Title|OWL&#32;EL&#32;Profile&#32;incompatible|
|[Section top](#minorfail-outcome-number-27)|Description|Statement&#32;not&#32;supported|
|[Section top](#minorfail-outcome-number-27)|Pointer|<pre lang="Turtle"><code>hmas:hasProfile&#32;a&#32;owl:AsymmetricProperty,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:ObjectProperty&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;has&#32;for&#32;profile&#34;@en,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#34;has&#32;profile&#34;@en,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#34;a&#32;pour&#32;profil&#34;@fr&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;A&#32;relation&#32;that&#32;links&#32;a&#32;resource&#32;to&#32;its&#32;profile.&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32;hmas:core&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:range&#32;hmas:ResourceProfile&#32;;  &#10; &#32; &#32; &#32; &#32;owl:inverseOf&#32;hmas:isProfileOf&#32;.</code></pre>|

***
### MinorFail Outcome number 28

[Jump to summary definition](#summary-MinorFail-28)	|	[Previous MinorFail outcome](#minorfail-outcome-number-27)	|	[Next MinorFail outcome](#minorfail-outcome-number-29)

:exclamation:MinorFail outcome
#### Subject detail
|Name|all-fragments|
|----|----|
|Title|All&#32;the&#32;fragments&#32;from&#32;branch&#32;HEAD&#32;that&#32;are&#32;syntaxically&#32;correct&#32;as&#32;well&#32;as&#32;their&#32;recursive&#32;imports|
|Composition|- [Modelet logistics/configure-organization](https://github.com/HyperAgents/hmas/blob/HEAD/domains/logistics/configure-organization/onto.ttl)<br/>- [Modelet logistics/coordinate-activities](https://github.com/HyperAgents/hmas/blob/HEAD/domains/logistics/coordinate-activities/onto.ttl)<br/>- [Modelet logistics/create-organization](https://github.com/HyperAgents/hmas/blob/HEAD/domains/logistics/create-organization/onto.ttl)<br/>- [Modelet manufacturing-environments/discover-behavior-specifications](https://github.com/HyperAgents/hmas/blob/HEAD/domains/manufacturing-environments/discover-behavior-specifications/onto.ttl)<br/>- [Modelet manufacturing-environments/discover-core](https://github.com/HyperAgents/hmas/blob/HEAD/domains/manufacturing-environments/discover-core/onto.ttl)<br/>- [Modelet manufacturing-environments/discover-organization](https://github.com/HyperAgents/hmas/blob/HEAD/domains/manufacturing-environments/discover-organization/onto.ttl)<br/>- [Modelet manufacturing-environments/discover-platforms](https://github.com/HyperAgents/hmas/blob/HEAD/domains/manufacturing-environments/discover-platforms/onto.ttl)<br/>- [Modelet manufacturing-environments/discover-signifiers](https://github.com/HyperAgents/hmas/blob/HEAD/domains/manufacturing-environments/discover-signifiers/onto.ttl)<br/>- [Module alignment/interaction-td](https://github.com/HyperAgents/hmas/blob/HEAD/src/alignment/interaction-td.ttl)<br/>- [Module core](https://github.com/HyperAgents/hmas/blob/HEAD/src/core.ttl)<br/>- [Module fipa](https://github.com/HyperAgents/hmas/blob/HEAD/src/fipa.ttl)<br/>- [Module interaction](https://github.com/HyperAgents/hmas/blob/HEAD/src/interaction.ttl)<br/>- [Module regulation](https://github.com/HyperAgents/hmas/blob/HEAD/src/regulation.ttl)|

#### Criterion detail
|Identifier|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|
|----|----|
|Title|Profile&#32;compatibility&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;check&#32;whether&#32;the&#32;test&#32;subject&#32;is&#32;compatible&#32;with&#32;a&#32;profile&#32;or&#32;not,&#32;and&#32;if&#32;it&#32;is&#32;not,&#32;why.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-28)|Identifier|`owl-ql-profile-error`|
|[Section top](#minorfail-outcome-number-28)|Title|OWL&#32;QL&#32;Profile&#32;incompatible|
|[Section top](#minorfail-outcome-number-28)|Description|Anonymous&#32;individuals&#32;are&#32;not&#32;supported|
|[Section top](#minorfail-outcome-number-28)|Pointer|<pre lang="Turtle"><code>&#91;]&#32;a&#32;owl:NamedIndividual&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;Chemero&#32;and&#32;Turvey,&#32;2007&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;dc:bibliographicCitation&#32; &#34;Chemero,&#32;A.,&#32;&&#32;Turvey,&#32;M.&#32;T.&#32;(2007).&#32;Complexity,&#32;hypersets,&#32;...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;dc:identifier&#32; &#60;https://doi.org/10.1162/biot.2007.2.1.23> &#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-28)|Pointer|<pre lang="Turtle"><code>&#91;]&#32;a&#32;owl:NamedIndividual&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;Norman,&#32;2013&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;dc:bibliographicCitation&#32; &#34;Norman,&#32;D.&#32;(2013).&#32;The&#32;design&#32;of&#32;everyday&#32;things:&#32;Revised&#32;an...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;dc:identifier&#32; &#60;https://mitpress.mit.edu/9780262640374/> &#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-28)|Pointer|<pre lang="Turtle"><code>&#91;]&#32;rdfs:label&#32; &#34;Chemero&#32;and&#32;Turvey,&#32;2007&#34;@en&#32;;  &#10; &#32; &#32;&#32; &#32;dc:bibliographicCitation&#32; &#34;Chemero,&#32;A.,&#32;&&#32;Turvey,&#32;M.&#32;T.&#32;(2007).&#32;Complexity,&#32;hypersets,&#32;...&#34; &#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-28)|Pointer|<pre lang="Turtle"><code>&#91;]&#32;rdfs:label&#32; &#34;Norman,&#32;2013&#34;@en&#32;;  &#10; &#32; &#32;&#32; &#32;dc:bibliographicCitation&#32; &#34;Norman,&#32;D.&#32;(2013).&#32;The&#32;design&#32;of&#32;everyday&#32;things:&#32;Revised&#32;an...&#34; &#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-28)|Pointer|<pre lang="Turtle"><code>hmas:Affordance&#32;a&#32;skos:Concept&#32;;  &#10; &#32; &#32; &#32; &#32;dc:references&#32; &#91;&#32;a&#32;owl:NamedIndividual&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;Chemero&#32;and&#32;Turvey,&#32;2007&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;dc:bibliographicCitation&#32; &#34;Chemero,&#32;A.,&#32;&&#32;Turvey,&#32;M.&#32;T.&#32;(2007).&#32;Complexity,&#32;hypersets,&#32;...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;dc:identifier&#32; &#60;https://doi.org/10.1162/biot.2007.2.1.23> &#32;],  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#91;&#32;a&#32;owl:NamedIndividual&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;Norman,&#32;2013&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;dc:bibliographicCitation&#32; &#34;Norman,&#32;D.&#32;(2013).&#32;The&#32;design&#32;of&#32;everyday&#32;things:&#32;Revised&#32;an...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;dc:identifier&#32; &#60;https://mitpress.mit.edu/9780262640374/> &#32;],  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#91;&#32;rdfs:label&#32; &#34;Chemero&#32;and&#32;Turvey,&#32;2007&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;dc:bibliographicCitation&#32; &#34;Chemero,&#32;A.,&#32;&&#32;Turvey,&#32;M.&#32;T.&#32;(2007).&#32;Complexity,&#32;hypersets,&#32;...&#34; &#32;],  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#91;&#32;rdfs:label&#32; &#34;Norman,&#32;2013&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;dc:bibliographicCitation&#32; &#34;Norman,&#32;D.&#32;(2013).&#32;The&#32;design&#32;of&#32;everyday&#32;things:&#32;Revised&#32;an...&#34; &#32;]&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32;hmas:core&#32;;  &#10; &#32; &#32; &#32; &#32;skos:definition&#32; &#34;A&#32;behavior&#32;possibility&#32;that&#32;is&#32;a&#32;relationship&#32;between&#32;an&#32;abi...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;skos:editorialNote&#32; &#34;The&#32;concept&#32;has&#32;been&#32;considered&#32;as&#32;a&#32;candidate&#32;term&#32;for&#32;repr...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;skos:historyNote&#32; &#34;The&#32;definition&#32;of&#32;the&#32;concept&#32;follows&#32;affordance&#32;theorists&#32; &#91;...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;skos:prefLabel&#32; &#34;affordance&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;skos:related&#32;hmas:Signifier&#32;.</code></pre>|

***
### MinorFail Outcome number 29

[Jump to summary definition](#summary-MinorFail-29)	|	[Previous MinorFail outcome](#minorfail-outcome-number-28)	|	[Next MinorFail outcome](#minorfail-outcome-number-30)

:exclamation:MinorFail outcome
#### Subject detail
|Name|all-fragments|
|----|----|
|Title|All&#32;the&#32;fragments&#32;from&#32;branch&#32;HEAD&#32;that&#32;are&#32;syntaxically&#32;correct&#32;as&#32;well&#32;as&#32;their&#32;recursive&#32;imports|
|Composition|- [Modelet logistics/configure-organization](https://github.com/HyperAgents/hmas/blob/HEAD/domains/logistics/configure-organization/onto.ttl)<br/>- [Modelet logistics/coordinate-activities](https://github.com/HyperAgents/hmas/blob/HEAD/domains/logistics/coordinate-activities/onto.ttl)<br/>- [Modelet logistics/create-organization](https://github.com/HyperAgents/hmas/blob/HEAD/domains/logistics/create-organization/onto.ttl)<br/>- [Modelet manufacturing-environments/discover-behavior-specifications](https://github.com/HyperAgents/hmas/blob/HEAD/domains/manufacturing-environments/discover-behavior-specifications/onto.ttl)<br/>- [Modelet manufacturing-environments/discover-core](https://github.com/HyperAgents/hmas/blob/HEAD/domains/manufacturing-environments/discover-core/onto.ttl)<br/>- [Modelet manufacturing-environments/discover-organization](https://github.com/HyperAgents/hmas/blob/HEAD/domains/manufacturing-environments/discover-organization/onto.ttl)<br/>- [Modelet manufacturing-environments/discover-platforms](https://github.com/HyperAgents/hmas/blob/HEAD/domains/manufacturing-environments/discover-platforms/onto.ttl)<br/>- [Modelet manufacturing-environments/discover-signifiers](https://github.com/HyperAgents/hmas/blob/HEAD/domains/manufacturing-environments/discover-signifiers/onto.ttl)<br/>- [Module alignment/interaction-td](https://github.com/HyperAgents/hmas/blob/HEAD/src/alignment/interaction-td.ttl)<br/>- [Module core](https://github.com/HyperAgents/hmas/blob/HEAD/src/core.ttl)<br/>- [Module fipa](https://github.com/HyperAgents/hmas/blob/HEAD/src/fipa.ttl)<br/>- [Module interaction](https://github.com/HyperAgents/hmas/blob/HEAD/src/interaction.ttl)<br/>- [Module regulation](https://github.com/HyperAgents/hmas/blob/HEAD/src/regulation.ttl)|

#### Criterion detail
|Identifier|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|
|----|----|
|Title|Profile&#32;compatibility&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;check&#32;whether&#32;the&#32;test&#32;subject&#32;is&#32;compatible&#32;with&#32;a&#32;profile&#32;or&#32;not,&#32;and&#32;if&#32;it&#32;is&#32;not,&#32;why.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-29)|Identifier|`owl-ql-profile-error`|
|[Section top](#minorfail-outcome-number-29)|Title|OWL&#32;QL&#32;Profile&#32;incompatible|
|[Section top](#minorfail-outcome-number-29)|Description|Class&#32;Expression&#32;not&#32;supported&#32;with&#32;rdfs:subClassOf|
|[Section top](#minorfail-outcome-number-29)|Pointer|<pre lang="Turtle"><code>&#60;https://www.w3.org/2019/wot/td#InteractionAffordance> &#32;rdfs:comment&#32; &#34;Using&#32;a&#32;TD&#32;Interaction&#32;Affordance&#32;results&#32;in&#32;an&#32;action&#32;execu...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:subClassOf&#32; &#91;&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:hasValue&#32;hmas:ActionExecution&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:onProperty&#32;sh:class&#32;]&#32;.</code></pre>|

***
### MinorFail Outcome number 30

[Jump to summary definition](#summary-MinorFail-30)	|	[Previous MinorFail outcome](#minorfail-outcome-number-29)	|	[Next MinorFail outcome](#minorfail-outcome-number-31)

:exclamation:MinorFail outcome
#### Subject detail
|Name|all-fragments|
|----|----|
|Title|All&#32;the&#32;fragments&#32;from&#32;branch&#32;HEAD&#32;that&#32;are&#32;syntaxically&#32;correct&#32;as&#32;well&#32;as&#32;their&#32;recursive&#32;imports|
|Composition|- [Modelet logistics/configure-organization](https://github.com/HyperAgents/hmas/blob/HEAD/domains/logistics/configure-organization/onto.ttl)<br/>- [Modelet logistics/coordinate-activities](https://github.com/HyperAgents/hmas/blob/HEAD/domains/logistics/coordinate-activities/onto.ttl)<br/>- [Modelet logistics/create-organization](https://github.com/HyperAgents/hmas/blob/HEAD/domains/logistics/create-organization/onto.ttl)<br/>- [Modelet manufacturing-environments/discover-behavior-specifications](https://github.com/HyperAgents/hmas/blob/HEAD/domains/manufacturing-environments/discover-behavior-specifications/onto.ttl)<br/>- [Modelet manufacturing-environments/discover-core](https://github.com/HyperAgents/hmas/blob/HEAD/domains/manufacturing-environments/discover-core/onto.ttl)<br/>- [Modelet manufacturing-environments/discover-organization](https://github.com/HyperAgents/hmas/blob/HEAD/domains/manufacturing-environments/discover-organization/onto.ttl)<br/>- [Modelet manufacturing-environments/discover-platforms](https://github.com/HyperAgents/hmas/blob/HEAD/domains/manufacturing-environments/discover-platforms/onto.ttl)<br/>- [Modelet manufacturing-environments/discover-signifiers](https://github.com/HyperAgents/hmas/blob/HEAD/domains/manufacturing-environments/discover-signifiers/onto.ttl)<br/>- [Module alignment/interaction-td](https://github.com/HyperAgents/hmas/blob/HEAD/src/alignment/interaction-td.ttl)<br/>- [Module core](https://github.com/HyperAgents/hmas/blob/HEAD/src/core.ttl)<br/>- [Module fipa](https://github.com/HyperAgents/hmas/blob/HEAD/src/fipa.ttl)<br/>- [Module interaction](https://github.com/HyperAgents/hmas/blob/HEAD/src/interaction.ttl)<br/>- [Module regulation](https://github.com/HyperAgents/hmas/blob/HEAD/src/regulation.ttl)|

#### Criterion detail
|Identifier|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|
|----|----|
|Title|Profile&#32;compatibility&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;check&#32;whether&#32;the&#32;test&#32;subject&#32;is&#32;compatible&#32;with&#32;a&#32;profile&#32;or&#32;not,&#32;and&#32;if&#32;it&#32;is&#32;not,&#32;why.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-30)|Identifier|`owl-ql-profile-error`|
|[Section top](#minorfail-outcome-number-30)|Title|OWL&#32;QL&#32;Profile&#32;incompatible|
|[Section top](#minorfail-outcome-number-30)|Description|Statement&#32;not&#32;supported  &#10;Statement&#32;not&#32;supported&#32;in&#32;a&#32;Super&#32;Class&#32;Expression|
|[Section top](#minorfail-outcome-number-30)|Pointer|<pre lang="Turtle"><code>&#91;]&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32;owl:hasValue&#32;hmas:ActionExecution&#32;;  &#10; &#32; &#32; &#32; &#32;owl:onProperty&#32;sh:class&#32;.</code></pre>|

***
### MinorFail Outcome number 31

[Jump to summary definition](#summary-MinorFail-31)	|	[Previous MinorFail outcome](#minorfail-outcome-number-30)	|	[Next MinorFail outcome](#minorfail-outcome-number-32)

:exclamation:MinorFail outcome
#### Subject detail
|Name|all-fragments|
|----|----|
|Title|All&#32;the&#32;fragments&#32;from&#32;branch&#32;HEAD&#32;that&#32;are&#32;syntaxically&#32;correct&#32;as&#32;well&#32;as&#32;their&#32;recursive&#32;imports|
|Composition|- [Modelet logistics/configure-organization](https://github.com/HyperAgents/hmas/blob/HEAD/domains/logistics/configure-organization/onto.ttl)<br/>- [Modelet logistics/coordinate-activities](https://github.com/HyperAgents/hmas/blob/HEAD/domains/logistics/coordinate-activities/onto.ttl)<br/>- [Modelet logistics/create-organization](https://github.com/HyperAgents/hmas/blob/HEAD/domains/logistics/create-organization/onto.ttl)<br/>- [Modelet manufacturing-environments/discover-behavior-specifications](https://github.com/HyperAgents/hmas/blob/HEAD/domains/manufacturing-environments/discover-behavior-specifications/onto.ttl)<br/>- [Modelet manufacturing-environments/discover-core](https://github.com/HyperAgents/hmas/blob/HEAD/domains/manufacturing-environments/discover-core/onto.ttl)<br/>- [Modelet manufacturing-environments/discover-organization](https://github.com/HyperAgents/hmas/blob/HEAD/domains/manufacturing-environments/discover-organization/onto.ttl)<br/>- [Modelet manufacturing-environments/discover-platforms](https://github.com/HyperAgents/hmas/blob/HEAD/domains/manufacturing-environments/discover-platforms/onto.ttl)<br/>- [Modelet manufacturing-environments/discover-signifiers](https://github.com/HyperAgents/hmas/blob/HEAD/domains/manufacturing-environments/discover-signifiers/onto.ttl)<br/>- [Module alignment/interaction-td](https://github.com/HyperAgents/hmas/blob/HEAD/src/alignment/interaction-td.ttl)<br/>- [Module core](https://github.com/HyperAgents/hmas/blob/HEAD/src/core.ttl)<br/>- [Module fipa](https://github.com/HyperAgents/hmas/blob/HEAD/src/fipa.ttl)<br/>- [Module interaction](https://github.com/HyperAgents/hmas/blob/HEAD/src/interaction.ttl)<br/>- [Module regulation](https://github.com/HyperAgents/hmas/blob/HEAD/src/regulation.ttl)|

#### Criterion detail
|Identifier|[term-referencing](https://ns.inria.fr/olivaw#term-referencing)|
|----|----|
|Title|Term&#32;referencing&#32;test|
|Description|A&#32;test&#32;case&#32;from&#32;the&#32;Best&#32;Practices&#32;tests&#32;checking&#32;if&#32;each&#32;term&#32;of&#32;the&#32;test&#32;subject&#32;is&#32;referenced&#32;to&#32;a&#32;module&#32;through&#32;a&#32;rdfs:isDefinedBy&#32;property.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-31)|Identifier|`no-reference-module`|
|[Section top](#minorfail-outcome-number-31)|Title|Term&#32;not&#32;referenced&#32;to&#32;a&#32;module|
|[Section top](#minorfail-outcome-number-31)|Description|Subject&#32;terms&#32;not&#32;linked&#32;to&#32;a&#32;module&#32;by&#32;a&#32;rdfs:isDefinedBy&#32;property|
|[Section top](#minorfail-outcome-number-31)|Pointer|<pre lang="Turtle"><code>:hasServiceName&#32;a&#32;owl:ObjectProperty&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;has&#32;Service&#32;Name&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:domain&#32;:APService&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-31)|Pointer|<pre lang="Turtle"><code>:APService&#32;a&#32;owl:Class&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;Agent&#32;Platform&#32;Service&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;A&#32;service&#32;exposed&#32;by&#32;a&#32;FIPA&#32;Agent&#32;Platform&#32;as&#32;defined&#32;by&#32;the...&#34; &#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-31)|Pointer|<pre lang="Turtle"><code>:hasServiceType&#32;a&#32;owl:ObjectProperty&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;has&#32;Service&#32;Type&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:domain&#32;:APService&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-31)|Pointer|<pre lang="Turtle"><code>:AgentIdentifierDescription&#32;a&#32;owl:Class&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;Agent&#32;Identifier&#32;Description&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;A&#32;resource&#32;profile&#32;that&#32;describes&#32;an&#32;agent&#32;using&#32;the&#32;Agent&#32;I...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:subClassOf&#32; &#60;https://ci.mines-stetienne.fr/hmas#ResourceProfile> &#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-31)|Pointer|<pre lang="Turtle"><code>:AgentPlatformDescription&#32;a&#32;owl:Class&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;Agent&#32;Platform&#32;Description&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;A&#32;resource&#32;profile&#32;that&#32;descripe&#32;a&#32;FIPA&#32;Agent&#32;Platform&#32;using...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:subClassOf&#32; &#60;https://ci.mines-stetienne.fr/hmas#ResourceProfile> &#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-31)|Pointer|<pre lang="Turtle"><code>:FIPAAgentPlatform&#32;a&#32;owl:Class&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;FIPA&#32;Agent&#32;Platform&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;A&#32;platform&#32;that&#32;conforms&#32;to&#32;the&#32;FIPA&#32;Abstract&#32;Architecture&#32;S...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:subClassOf&#32; &#60;https://ci.mines-stetienne.fr/hmas#Platform> &#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-31)|Pointer|<pre lang="Turtle"><code>:HTTPMessageTransportService&#32;a&#32;owl:Class&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;HTTP&#32;Message&#32;Transport&#32;Service&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;An&#32;HTTP-based&#32;message&#32;transport&#32;service&#32;that&#32;confirms&#32;to&#32;the...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:subClassOf&#32;:MessageTransportService&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-31)|Pointer|<pre lang="Turtle"><code>:MessageTransportService&#32;a&#32;owl:Class&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;Message&#32;Transport&#32;Service&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;A&#32;service&#32;for&#32;transporting&#32;messages&#32;among&#32;agents&#32;that&#32;confor...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:subClassOf&#32;:APService&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-31)|Pointer|<pre lang="Turtle"><code>:IIOPMessageTransportService&#32;a&#32;owl:Class&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;IIOP&#32;Message&#32;Transport&#32;Service&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;An&#32;HTTP-based&#32;message&#32;transport&#32;service&#32;that&#32;confirms&#32;to&#32;the...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:subClassOf&#32;:MessageTransportService&#32;.</code></pre>|

***
### MinorFail Outcome number 32

[Jump to summary definition](#summary-MinorFail-32)	|	[Previous MinorFail outcome](#minorfail-outcome-number-31)	|	Next MinorFail outcome

:exclamation:MinorFail outcome
#### Subject detail
|Name|all-fragments|
|----|----|
|Title|All&#32;the&#32;fragments&#32;from&#32;branch&#32;HEAD&#32;that&#32;are&#32;syntaxically&#32;correct&#32;as&#32;well&#32;as&#32;their&#32;recursive&#32;imports|
|Composition|- [Modelet logistics/configure-organization](https://github.com/HyperAgents/hmas/blob/HEAD/domains/logistics/configure-organization/onto.ttl)<br/>- [Modelet logistics/coordinate-activities](https://github.com/HyperAgents/hmas/blob/HEAD/domains/logistics/coordinate-activities/onto.ttl)<br/>- [Modelet logistics/create-organization](https://github.com/HyperAgents/hmas/blob/HEAD/domains/logistics/create-organization/onto.ttl)<br/>- [Modelet manufacturing-environments/discover-behavior-specifications](https://github.com/HyperAgents/hmas/blob/HEAD/domains/manufacturing-environments/discover-behavior-specifications/onto.ttl)<br/>- [Modelet manufacturing-environments/discover-core](https://github.com/HyperAgents/hmas/blob/HEAD/domains/manufacturing-environments/discover-core/onto.ttl)<br/>- [Modelet manufacturing-environments/discover-organization](https://github.com/HyperAgents/hmas/blob/HEAD/domains/manufacturing-environments/discover-organization/onto.ttl)<br/>- [Modelet manufacturing-environments/discover-platforms](https://github.com/HyperAgents/hmas/blob/HEAD/domains/manufacturing-environments/discover-platforms/onto.ttl)<br/>- [Modelet manufacturing-environments/discover-signifiers](https://github.com/HyperAgents/hmas/blob/HEAD/domains/manufacturing-environments/discover-signifiers/onto.ttl)<br/>- [Module alignment/interaction-td](https://github.com/HyperAgents/hmas/blob/HEAD/src/alignment/interaction-td.ttl)<br/>- [Module core](https://github.com/HyperAgents/hmas/blob/HEAD/src/core.ttl)<br/>- [Module fipa](https://github.com/HyperAgents/hmas/blob/HEAD/src/fipa.ttl)<br/>- [Module interaction](https://github.com/HyperAgents/hmas/blob/HEAD/src/interaction.ttl)<br/>- [Module regulation](https://github.com/HyperAgents/hmas/blob/HEAD/src/regulation.ttl)|

#### Criterion detail
|Identifier|[terms-differenciation](https://ns.inria.fr/olivaw#terms-differenciation)|
|----|----|
|Title|Terms&#32;differenciation&#32;test|
|Description|A&#32;test&#32;case&#32;from&#32;the&#32;Best&#32;Practices&#32;tests&#32;checking&#32;if&#32;all&#32;the&#32;terms&#32;are&#32;different&#32;enough&#32;from&#32;each&#32;other&#32;according&#32;to&#32;the&#32;Levenshtein&#32;distance&#32;metric.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-32)|Identifier|`too-close-terms`|
|[Section top](#minorfail-outcome-number-32)|Title|Too&#32;close&#32;terms|
|[Section top](#minorfail-outcome-number-32)|Description|Some&#32;terms&#32;are&#32;too&#32;similar|
|[Section top](#minorfail-outcome-number-32)|Pointer|<pre lang="Turtle"><code>:isAccessTo&#32;a&#32;owl:ObjectProperty&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;is&#32;access&#32;to&#34;@en,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#34;est&#32;l'accès&#32;à&#34;@fr&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;A&#32;relation&#32;that&#32;refers&#32;to&#32;an&#32;Artifact&#32;involved&#32;in&#32;an&#32;Access.&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:domain&#32;:Access&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32;:regulation&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:range&#32;:Artifact&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-32)|Pointer|<pre lang="Turtle"><code>:isAccessOf&#32;a&#32;owl:ObjectProperty&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;is&#32;access&#32;of&#34;@en,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#34;est&#32;l'accès&#32;de&#34;@fr&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;A&#32;relation&#32;that&#32;refers&#32;to&#32;an&#32;Agent&#32;involved&#32;in&#32;an&#32;Access.&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:domain&#32;:Access&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32;:regulation&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:range&#32;:Agent&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-32)|Pointer|<pre lang="Turtle"><code>:isAccessFor&#32;a&#32;owl:ObjectProperty&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;is&#32;access&#32;for&#34;@en,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#34;est&#32;l'accès&#32;pour&#34;@fr&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;A&#32;relation&#32;that&#32;refers&#32;to&#32;a&#32;Usage&#32;involved&#32;in&#32;an&#32;Access.&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:domain&#32;:Access&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32;:regulation&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:range&#32;:Usage&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-32)|Pointer|<pre lang="Turtle"><code>:isMembershipOf&#32;a&#32;owl:ObjectProperty&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;is&#32;membership&#32;of&#34;@en,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#34;est&#32;l'appartenance&#32;à&#34;@fr&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;A&#32;relation&#32;that&#32;refers&#32;to&#32;the&#32;Agent&#32;involved&#32;in&#32;a&#32;Membership...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:domain&#32;:Membership&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32;:regulation&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:range&#32;:Agent&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-32)|Pointer|<pre lang="Turtle"><code>:isMembershipIn&#32;a&#32;owl:ObjectProperty&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;is&#32;membership&#32;in&#34;@en,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#34;est&#32;l'appartenance&#32;à&#34;@fr&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;A&#32;relation&#32;that&#32;refers&#32;to&#32;the&#32;Group&#32;involved&#32;in&#32;a&#32;Membership...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:domain&#32;:Membership&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32;:regulation&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:range&#32;:Group&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-32)|Pointer|<pre lang="Turtle"><code>:isUsageOf&#32;a&#32;owl:ObjectProperty&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;is&#32;usage&#32;of&#34;@en,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#34;est&#32;un&#32;usage&#32;de&#34;@fr&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;A&#32;relation&#32;that&#32;refers&#32;to&#32;a&#32;Facility&#32;involved&#32;in&#32;a&#32;Usage.&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:domain&#32;:Usage&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32;:regulation&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:range&#32;:Facility&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-32)|Pointer|<pre lang="Turtle"><code>:isUsageIn&#32;a&#32;owl:ObjectProperty&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;is&#32;usage&#32;in&#34;@en,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#34;est&#32;un&#32;usage&#32;dans&#34;@fr&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;A&#32;relation&#32;that&#32;refers&#32;to&#32;a&#32;Setting&#32;involved&#32;in&#32;a&#32;Usage.&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:domain&#32;:Usage&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32;:regulation&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:range&#32;:Setting&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-32)|Pointer|<pre lang="Turtle"><code>:signifies&#32;a&#32;owl:ObjectProperty&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;signifies&#34;@en,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#34;signifie&#34;@fr&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;A&#32;relation&#32;between&#32;a&#32;signifier&#32;and&#32;the&#32;specification&#32;of&#32;a&#32;be...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:domain&#32;:Signifier&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32;:interaction&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-32)|Pointer|<pre lang="Turtle"><code>:Signifier&#32;a&#32;owl:Class&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;Signifier&#34;@en,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#34;signifier&#34;@en,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#34;Signifiant&#34;@fr,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#34;signifiant&#34;@fr&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;A&#32;perceivable&#32;sign/cue&#32;that&#32;can&#32;be&#32;interpreted&#32;meaningfully&#32;...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32;:core&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:seeAlso&#32; &#60;https://github.com/HyperAgents/ns.hyperagents.org/issues/13#issuecomment-1028904491>,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#60;https://github.com/HyperAgents/ns.hyperagents.org/issues/41> &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:subClassOf&#32;:Hostable&#32;;  &#10; &#32; &#32; &#32; &#32;skos:note&#32; &#34;:Signifier&#32;works&#32;as&#32;a&#32;bridge&#32;between&#32;the&#32;Core&#32;and&#32;the&#32;Intera...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;skos:related&#32;:Affordance&#32;.</code></pre>|

***

</details>

***


# NotTested Outcomes

[Jump to statistic summary](#statistic-summary)	|	[Previous section](#minorfail-outcomes)	|	[Next section](#pass-outcomes)

Here is the chapter related to the NotTested outcome

:grey_question:30 NotTested outcomes

<details>
<summary>Fold/Unfold the 30 summary and details</summary>

## NotTested Outcomes Summary

:grey_question:30 NotTested outcomes

|*Jump*|*Number*|*Status*|*Subject*|*Criterion*|*Title*|*Link*|
|------|--------|--------|---------|-----------|-------|------|
|[Chapter top](#nottested-outcomes)|<div id="summary-NotTested-1">1/30</div>|:grey_question:NotTested|`module-meta`|[domain-and-range-referencing](https://ns.inria.fr/olivaw#domain-and-range-referencing)|The test could not be run|[Jump](#nottested-outcome-number-1)|
|[Chapter top](#nottested-outcomes)|<div id="summary-NotTested-2">2/30</div>|:grey_question:NotTested|`module-meta`|[domain-and-range-referencing](https://ns.inria.fr/olivaw#domain-and-range-referencing)|The test could not be run|[Jump](#nottested-outcome-number-2)|
|[Chapter top](#nottested-outcomes)|<div id="summary-NotTested-3">3/30</div>|:grey_question:NotTested|`module-meta`|[labeled-terms](https://ns.inria.fr/olivaw#labeled-terms)|The test could not be run|[Jump](#nottested-outcome-number-3)|
|[Chapter top](#nottested-outcomes)|<div id="summary-NotTested-4">4/30</div>|:grey_question:NotTested|`module-meta`|[labeled-terms](https://ns.inria.fr/olivaw#labeled-terms)|The test could not be run|[Jump](#nottested-outcome-number-4)|
|[Chapter top](#nottested-outcomes)|<div id="summary-NotTested-5">5/30</div>|:grey_question:NotTested|`module-meta`|[owl-rl-constraint](https://ns.inria.fr/olivaw#owl-rl-constraint)|The test could not be run|[Jump](#nottested-outcome-number-5)|
|[Chapter top](#nottested-outcomes)|<div id="summary-NotTested-6">6/30</div>|:grey_question:NotTested|`module-meta`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|The test could not be run|[Jump](#nottested-outcome-number-6)|
|[Chapter top](#nottested-outcomes)|<div id="summary-NotTested-7">7/30</div>|:grey_question:NotTested|`module-meta`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|The test could not be run|[Jump](#nottested-outcome-number-7)|
|[Chapter top](#nottested-outcomes)|<div id="summary-NotTested-8">8/30</div>|:grey_question:NotTested|`module-meta`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|The test could not be run|[Jump](#nottested-outcome-number-8)|
|[Chapter top](#nottested-outcomes)|<div id="summary-NotTested-9">9/30</div>|:grey_question:NotTested|`module-meta`|[term-referencing](https://ns.inria.fr/olivaw#term-referencing)|The test could not be run|[Jump](#nottested-outcome-number-9)|
|[Chapter top](#nottested-outcomes)|<div id="summary-NotTested-10">10/30</div>|:grey_question:NotTested|`module-meta`|[terms-differenciation](https://ns.inria.fr/olivaw#terms-differenciation)|The test could not be run|[Jump](#nottested-outcome-number-10)|
|[Chapter top](#nottested-outcomes)|<div id="summary-NotTested-11">11/30</div>|:grey_question:NotTested|`modelet-manufacturing-environments-safety-rules`|[domain-and-range-referencing](https://ns.inria.fr/olivaw#domain-and-range-referencing)|The test could not be run|[Jump](#nottested-outcome-number-11)|
|[Chapter top](#nottested-outcomes)|<div id="summary-NotTested-12">12/30</div>|:grey_question:NotTested|`modelet-manufacturing-environments-safety-rules`|[domain-and-range-referencing](https://ns.inria.fr/olivaw#domain-and-range-referencing)|The test could not be run|[Jump](#nottested-outcome-number-12)|
|[Chapter top](#nottested-outcomes)|<div id="summary-NotTested-13">13/30</div>|:grey_question:NotTested|`modelet-manufacturing-environments-safety-rules`|[labeled-terms](https://ns.inria.fr/olivaw#labeled-terms)|The test could not be run|[Jump](#nottested-outcome-number-13)|
|[Chapter top](#nottested-outcomes)|<div id="summary-NotTested-14">14/30</div>|:grey_question:NotTested|`modelet-manufacturing-environments-safety-rules`|[labeled-terms](https://ns.inria.fr/olivaw#labeled-terms)|The test could not be run|[Jump](#nottested-outcome-number-14)|
|[Chapter top](#nottested-outcomes)|<div id="summary-NotTested-15">15/30</div>|:grey_question:NotTested|`modelet-manufacturing-environments-safety-rules`|[owl-rl-constraint](https://ns.inria.fr/olivaw#owl-rl-constraint)|The test could not be run|[Jump](#nottested-outcome-number-15)|
|[Chapter top](#nottested-outcomes)|<div id="summary-NotTested-16">16/30</div>|:grey_question:NotTested|`modelet-manufacturing-environments-safety-rules`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|The test could not be run|[Jump](#nottested-outcome-number-16)|
|[Chapter top](#nottested-outcomes)|<div id="summary-NotTested-17">17/30</div>|:grey_question:NotTested|`modelet-manufacturing-environments-safety-rules`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|The test could not be run|[Jump](#nottested-outcome-number-17)|
|[Chapter top](#nottested-outcomes)|<div id="summary-NotTested-18">18/30</div>|:grey_question:NotTested|`modelet-manufacturing-environments-safety-rules`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|The test could not be run|[Jump](#nottested-outcome-number-18)|
|[Chapter top](#nottested-outcomes)|<div id="summary-NotTested-19">19/30</div>|:grey_question:NotTested|`modelet-manufacturing-environments-safety-rules`|[term-referencing](https://ns.inria.fr/olivaw#term-referencing)|The test could not be run|[Jump](#nottested-outcome-number-19)|
|[Chapter top](#nottested-outcomes)|<div id="summary-NotTested-20">20/30</div>|:grey_question:NotTested|`modelet-manufacturing-environments-safety-rules`|[terms-differenciation](https://ns.inria.fr/olivaw#terms-differenciation)|The test could not be run|[Jump](#nottested-outcome-number-20)|
|[Chapter top](#nottested-outcomes)|<div id="summary-NotTested-21">21/30</div>|:grey_question:NotTested|`modelet-logistics-structure-organization`|[domain-and-range-referencing](https://ns.inria.fr/olivaw#domain-and-range-referencing)|The test could not be run|[Jump](#nottested-outcome-number-21)|
|[Chapter top](#nottested-outcomes)|<div id="summary-NotTested-22">22/30</div>|:grey_question:NotTested|`modelet-logistics-structure-organization`|[domain-and-range-referencing](https://ns.inria.fr/olivaw#domain-and-range-referencing)|The test could not be run|[Jump](#nottested-outcome-number-22)|
|[Chapter top](#nottested-outcomes)|<div id="summary-NotTested-23">23/30</div>|:grey_question:NotTested|`modelet-logistics-structure-organization`|[labeled-terms](https://ns.inria.fr/olivaw#labeled-terms)|The test could not be run|[Jump](#nottested-outcome-number-23)|
|[Chapter top](#nottested-outcomes)|<div id="summary-NotTested-24">24/30</div>|:grey_question:NotTested|`modelet-logistics-structure-organization`|[labeled-terms](https://ns.inria.fr/olivaw#labeled-terms)|The test could not be run|[Jump](#nottested-outcome-number-24)|
|[Chapter top](#nottested-outcomes)|<div id="summary-NotTested-25">25/30</div>|:grey_question:NotTested|`modelet-logistics-structure-organization`|[owl-rl-constraint](https://ns.inria.fr/olivaw#owl-rl-constraint)|The test could not be run|[Jump](#nottested-outcome-number-25)|
|[Chapter top](#nottested-outcomes)|<div id="summary-NotTested-26">26/30</div>|:grey_question:NotTested|`modelet-logistics-structure-organization`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|The test could not be run|[Jump](#nottested-outcome-number-26)|
|[Chapter top](#nottested-outcomes)|<div id="summary-NotTested-27">27/30</div>|:grey_question:NotTested|`modelet-logistics-structure-organization`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|The test could not be run|[Jump](#nottested-outcome-number-27)|
|[Chapter top](#nottested-outcomes)|<div id="summary-NotTested-28">28/30</div>|:grey_question:NotTested|`modelet-logistics-structure-organization`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|The test could not be run|[Jump](#nottested-outcome-number-28)|
|[Chapter top](#nottested-outcomes)|<div id="summary-NotTested-29">29/30</div>|:grey_question:NotTested|`modelet-logistics-structure-organization`|[term-referencing](https://ns.inria.fr/olivaw#term-referencing)|The test could not be run|[Jump](#nottested-outcome-number-29)|
|[Chapter top](#nottested-outcomes)|<div id="summary-NotTested-30">30/30</div>|:grey_question:NotTested|`modelet-logistics-structure-organization`|[terms-differenciation](https://ns.inria.fr/olivaw#terms-differenciation)|The test could not be run|[Jump](#nottested-outcome-number-30)|

***

## NotTested Outcomes Details

This subchapter gives more details to the :grey_question:NotTested outcomes

### NotTested Outcome number 1

[Jump to summary definition](#summary-NotTested-1)	|	Previous NotTested outcome	|	[Next NotTested outcome](#nottested-outcome-number-2)

:grey_question:NotTested outcome
#### Subject detail
|Name|module-meta|
|----|----|
|Title|Standalone&#32;module&#32;src&#92;meta.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Module meta](https://github.com/HyperAgents/hmas/blob/HEAD/src/meta.ttl)|

#### Criterion detail
|Identifier|[domain-and-range-referencing](https://ns.inria.fr/olivaw#domain-and-range-referencing)|
|----|----|
|Title|Domain&#32;and&#32;range&#32;referencing&#32;test|
|Description|A&#32;test&#32;case&#32;from&#32;the&#32;Best&#32;Practices&#32;tests&#32;checking&#32;if&#32;all&#32;the&#32;ranges&#32;and&#32;domains&#32;from&#32;the&#32;test&#32;subject&#32;point&#32;to&#32;terms&#32;that&#32;are&#32;defined&#32;in&#32;the&#32;vocabulary.|

#### Outcome Detail
|Jump|Type|:grey_question:NotTested|
|----|----|----|
|[Section top](#nottested-outcome-number-1)|Identifier|`domain-out-of-vocabulary`|
|[Section top](#nottested-outcome-number-1)|Title|The&#32;test&#32;could&#32;not&#32;be&#32;run|
|[Section top](#nottested-outcome-number-1)|Description|The&#32;syntax&#32;of&#32;the&#32;subject&#32;and&#32;any&#32;of&#32;its&#32;imports&#32;must&#32;be&#32;syntaxically&#32;correct|

***
### NotTested Outcome number 2

[Jump to summary definition](#summary-NotTested-2)	|	[Previous NotTested outcome](#nottested-outcome-number-1)	|	[Next NotTested outcome](#nottested-outcome-number-3)

:grey_question:NotTested outcome
#### Subject detail
|Name|module-meta|
|----|----|
|Title|Standalone&#32;module&#32;src&#92;meta.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Module meta](https://github.com/HyperAgents/hmas/blob/HEAD/src/meta.ttl)|

#### Criterion detail
|Identifier|[domain-and-range-referencing](https://ns.inria.fr/olivaw#domain-and-range-referencing)|
|----|----|
|Title|Domain&#32;and&#32;range&#32;referencing&#32;test|
|Description|A&#32;test&#32;case&#32;from&#32;the&#32;Best&#32;Practices&#32;tests&#32;checking&#32;if&#32;all&#32;the&#32;ranges&#32;and&#32;domains&#32;from&#32;the&#32;test&#32;subject&#32;point&#32;to&#32;terms&#32;that&#32;are&#32;defined&#32;in&#32;the&#32;vocabulary.|

#### Outcome Detail
|Jump|Type|:grey_question:NotTested|
|----|----|----|
|[Section top](#nottested-outcome-number-2)|Identifier|`range-out-of-vocabulary`|
|[Section top](#nottested-outcome-number-2)|Title|The&#32;test&#32;could&#32;not&#32;be&#32;run|
|[Section top](#nottested-outcome-number-2)|Description|The&#32;syntax&#32;of&#32;the&#32;subject&#32;and&#32;any&#32;of&#32;its&#32;imports&#32;must&#32;be&#32;syntaxically&#32;correct|

***
### NotTested Outcome number 3

[Jump to summary definition](#summary-NotTested-3)	|	[Previous NotTested outcome](#nottested-outcome-number-2)	|	[Next NotTested outcome](#nottested-outcome-number-4)

:grey_question:NotTested outcome
#### Subject detail
|Name|module-meta|
|----|----|
|Title|Standalone&#32;module&#32;src&#92;meta.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Module meta](https://github.com/HyperAgents/hmas/blob/HEAD/src/meta.ttl)|

#### Criterion detail
|Identifier|[labeled-terms](https://ns.inria.fr/olivaw#labeled-terms)|
|----|----|
|Title|Term&#32;labeling&#32;test|
|Description|A&#32;test&#32;case&#32;from&#32;the&#32;Best&#32;Practices&#32;tests&#32;checking&#32;if&#32;all&#32;the&#32;terms&#32;of&#32;the&#32;subject&#32;have&#32;a&#32;rdfs:label&#32;property&#32;pointing&#32;to&#32;a&#32;literal&#32;in&#32;English|

#### Outcome Detail
|Jump|Type|:grey_question:NotTested|
|----|----|----|
|[Section top](#nottested-outcome-number-3)|Identifier|`not-labeled-term`|
|[Section top](#nottested-outcome-number-3)|Title|The&#32;test&#32;could&#32;not&#32;be&#32;run|
|[Section top](#nottested-outcome-number-3)|Description|The&#32;subject&#32;and&#32;its&#32;recursive&#32;imports&#32;must&#32;be&#32;syntaxically&#32;correct|

***
### NotTested Outcome number 4

[Jump to summary definition](#summary-NotTested-4)	|	[Previous NotTested outcome](#nottested-outcome-number-3)	|	[Next NotTested outcome](#nottested-outcome-number-5)

:grey_question:NotTested outcome
#### Subject detail
|Name|module-meta|
|----|----|
|Title|Standalone&#32;module&#32;src&#92;meta.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Module meta](https://github.com/HyperAgents/hmas/blob/HEAD/src/meta.ttl)|

#### Criterion detail
|Identifier|[labeled-terms](https://ns.inria.fr/olivaw#labeled-terms)|
|----|----|
|Title|Term&#32;labeling&#32;test|
|Description|A&#32;test&#32;case&#32;from&#32;the&#32;Best&#32;Practices&#32;tests&#32;checking&#32;if&#32;all&#32;the&#32;terms&#32;of&#32;the&#32;subject&#32;have&#32;a&#32;rdfs:label&#32;property&#32;pointing&#32;to&#32;a&#32;literal&#32;in&#32;English|

#### Outcome Detail
|Jump|Type|:grey_question:NotTested|
|----|----|----|
|[Section top](#nottested-outcome-number-4)|Identifier|`not-labeled-term`|
|[Section top](#nottested-outcome-number-4)|Title|The&#32;test&#32;could&#32;not&#32;be&#32;run|
|[Section top](#nottested-outcome-number-4)|Description|The&#32;subject&#32;and&#32;its&#32;recursive&#32;imports&#32;must&#32;be&#32;syntaxically&#32;correct|

***
### NotTested Outcome number 5

[Jump to summary definition](#summary-NotTested-5)	|	[Previous NotTested outcome](#nottested-outcome-number-4)	|	[Next NotTested outcome](#nottested-outcome-number-6)

:grey_question:NotTested outcome
#### Subject detail
|Name|module-meta|
|----|----|
|Title|Standalone&#32;module&#32;src&#92;meta.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Module meta](https://github.com/HyperAgents/hmas/blob/HEAD/src/meta.ttl)|

#### Criterion detail
|Identifier|[owl-rl-constraint](https://ns.inria.fr/olivaw#owl-rl-constraint)|
|----|----|
|Title|OWL&#32;RL&#32;Constraint&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;check&#32;wether&#32;the&#32;test&#32;subject&#32;is&#32;syntaxically&#32;correct&#32;or&#32;not.|

#### Outcome Detail
|Jump|Type|:grey_question:NotTested|
|----|----|----|
|[Section top](#nottested-outcome-number-5)|Identifier|`owl-rl-constraint-violation`|
|[Section top](#nottested-outcome-number-5)|Title|The&#32;test&#32;could&#32;not&#32;be&#32;run|
|[Section top](#nottested-outcome-number-5)|Description|The&#32;subject&#32;and&#32;its&#32;recursive&#32;imports&#32;must&#32;be&#32;syntaxically&#32;correct|

***
### NotTested Outcome number 6

[Jump to summary definition](#summary-NotTested-6)	|	[Previous NotTested outcome](#nottested-outcome-number-5)	|	[Next NotTested outcome](#nottested-outcome-number-7)

:grey_question:NotTested outcome
#### Subject detail
|Name|module-meta|
|----|----|
|Title|Standalone&#32;module&#32;src&#92;meta.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Module meta](https://github.com/HyperAgents/hmas/blob/HEAD/src/meta.ttl)|

#### Criterion detail
|Identifier|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|
|----|----|
|Title|Profile&#32;compatibility&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;check&#32;whether&#32;the&#32;test&#32;subject&#32;is&#32;compatible&#32;with&#32;a&#32;profile&#32;or&#32;not,&#32;and&#32;if&#32;it&#32;is&#32;not,&#32;why.|

#### Outcome Detail
|Jump|Type|:grey_question:NotTested|
|----|----|----|
|[Section top](#nottested-outcome-number-6)|Identifier|`owl-el-profile-error`|
|[Section top](#nottested-outcome-number-6)|Title|The&#32;test&#32;could&#32;not&#32;be&#32;run|
|[Section top](#nottested-outcome-number-6)|Description|The&#32;subject&#32;must&#32;be&#32;syntaxically&#32;correct|

***
### NotTested Outcome number 7

[Jump to summary definition](#summary-NotTested-7)	|	[Previous NotTested outcome](#nottested-outcome-number-6)	|	[Next NotTested outcome](#nottested-outcome-number-8)

:grey_question:NotTested outcome
#### Subject detail
|Name|module-meta|
|----|----|
|Title|Standalone&#32;module&#32;src&#92;meta.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Module meta](https://github.com/HyperAgents/hmas/blob/HEAD/src/meta.ttl)|

#### Criterion detail
|Identifier|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|
|----|----|
|Title|Profile&#32;compatibility&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;check&#32;whether&#32;the&#32;test&#32;subject&#32;is&#32;compatible&#32;with&#32;a&#32;profile&#32;or&#32;not,&#32;and&#32;if&#32;it&#32;is&#32;not,&#32;why.|

#### Outcome Detail
|Jump|Type|:grey_question:NotTested|
|----|----|----|
|[Section top](#nottested-outcome-number-7)|Identifier|`owl-ql-profile-error`|
|[Section top](#nottested-outcome-number-7)|Title|The&#32;test&#32;could&#32;not&#32;be&#32;run|
|[Section top](#nottested-outcome-number-7)|Description|The&#32;subject&#32;must&#32;be&#32;syntaxically&#32;correct|

***
### NotTested Outcome number 8

[Jump to summary definition](#summary-NotTested-8)	|	[Previous NotTested outcome](#nottested-outcome-number-7)	|	[Next NotTested outcome](#nottested-outcome-number-9)

:grey_question:NotTested outcome
#### Subject detail
|Name|module-meta|
|----|----|
|Title|Standalone&#32;module&#32;src&#92;meta.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Module meta](https://github.com/HyperAgents/hmas/blob/HEAD/src/meta.ttl)|

#### Criterion detail
|Identifier|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|
|----|----|
|Title|Profile&#32;compatibility&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;check&#32;whether&#32;the&#32;test&#32;subject&#32;is&#32;compatible&#32;with&#32;a&#32;profile&#32;or&#32;not,&#32;and&#32;if&#32;it&#32;is&#32;not,&#32;why.|

#### Outcome Detail
|Jump|Type|:grey_question:NotTested|
|----|----|----|
|[Section top](#nottested-outcome-number-8)|Identifier|`owl-rl-profile-error`|
|[Section top](#nottested-outcome-number-8)|Title|The&#32;test&#32;could&#32;not&#32;be&#32;run|
|[Section top](#nottested-outcome-number-8)|Description|The&#32;subject&#32;must&#32;be&#32;syntaxically&#32;correct|

***
### NotTested Outcome number 9

[Jump to summary definition](#summary-NotTested-9)	|	[Previous NotTested outcome](#nottested-outcome-number-8)	|	[Next NotTested outcome](#nottested-outcome-number-10)

:grey_question:NotTested outcome
#### Subject detail
|Name|module-meta|
|----|----|
|Title|Standalone&#32;module&#32;src&#92;meta.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Module meta](https://github.com/HyperAgents/hmas/blob/HEAD/src/meta.ttl)|

#### Criterion detail
|Identifier|[term-referencing](https://ns.inria.fr/olivaw#term-referencing)|
|----|----|
|Title|Term&#32;referencing&#32;test|
|Description|A&#32;test&#32;case&#32;from&#32;the&#32;Best&#32;Practices&#32;tests&#32;checking&#32;if&#32;each&#32;term&#32;of&#32;the&#32;test&#32;subject&#32;is&#32;referenced&#32;to&#32;a&#32;module&#32;through&#32;a&#32;rdfs:isDefinedBy&#32;property.|

#### Outcome Detail
|Jump|Type|:grey_question:NotTested|
|----|----|----|
|[Section top](#nottested-outcome-number-9)|Identifier|`no-reference-module`|
|[Section top](#nottested-outcome-number-9)|Title|The&#32;test&#32;could&#32;not&#32;be&#32;run|
|[Section top](#nottested-outcome-number-9)|Description|The&#32;subject&#32;syntax&#32;must&#32;be&#32;correct|

***
### NotTested Outcome number 10

[Jump to summary definition](#summary-NotTested-10)	|	[Previous NotTested outcome](#nottested-outcome-number-9)	|	[Next NotTested outcome](#nottested-outcome-number-11)

:grey_question:NotTested outcome
#### Subject detail
|Name|module-meta|
|----|----|
|Title|Standalone&#32;module&#32;src&#92;meta.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Module meta](https://github.com/HyperAgents/hmas/blob/HEAD/src/meta.ttl)|

#### Criterion detail
|Identifier|[terms-differenciation](https://ns.inria.fr/olivaw#terms-differenciation)|
|----|----|
|Title|Terms&#32;differenciation&#32;test|
|Description|A&#32;test&#32;case&#32;from&#32;the&#32;Best&#32;Practices&#32;tests&#32;checking&#32;if&#32;all&#32;the&#32;terms&#32;are&#32;different&#32;enough&#32;from&#32;each&#32;other&#32;according&#32;to&#32;the&#32;Levenshtein&#32;distance&#32;metric.|

#### Outcome Detail
|Jump|Type|:grey_question:NotTested|
|----|----|----|
|[Section top](#nottested-outcome-number-10)|Identifier|`too-close-terms`|
|[Section top](#nottested-outcome-number-10)|Title|The&#32;test&#32;could&#32;not&#32;be&#32;run|
|[Section top](#nottested-outcome-number-10)|Description|The&#32;subject&#32;needs&#32;to&#32;be&#32;syntaxically&#32;correct|

***
### NotTested Outcome number 11

[Jump to summary definition](#summary-NotTested-11)	|	[Previous NotTested outcome](#nottested-outcome-number-10)	|	[Next NotTested outcome](#nottested-outcome-number-12)

:grey_question:NotTested outcome
#### Subject detail
|Name|modelet-manufacturing-environments-safety-rules|
|----|----|
|Title|Standalone&#32;modelet&#32;domains&#92;manufacturing-environments&#92;safety-rules&#92;onto.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Modelet manufacturing-environments/safety-rules](https://github.com/HyperAgents/hmas/blob/HEAD/domains/manufacturing-environments/safety-rules/onto.ttl)|

#### Criterion detail
|Identifier|[domain-and-range-referencing](https://ns.inria.fr/olivaw#domain-and-range-referencing)|
|----|----|
|Title|Domain&#32;and&#32;range&#32;referencing&#32;test|
|Description|A&#32;test&#32;case&#32;from&#32;the&#32;Best&#32;Practices&#32;tests&#32;checking&#32;if&#32;all&#32;the&#32;ranges&#32;and&#32;domains&#32;from&#32;the&#32;test&#32;subject&#32;point&#32;to&#32;terms&#32;that&#32;are&#32;defined&#32;in&#32;the&#32;vocabulary.|

#### Outcome Detail
|Jump|Type|:grey_question:NotTested|
|----|----|----|
|[Section top](#nottested-outcome-number-11)|Identifier|`domain-out-of-vocabulary`|
|[Section top](#nottested-outcome-number-11)|Title|The&#32;test&#32;could&#32;not&#32;be&#32;run|
|[Section top](#nottested-outcome-number-11)|Description|The&#32;syntax&#32;of&#32;the&#32;subject&#32;and&#32;any&#32;of&#32;its&#32;imports&#32;must&#32;be&#32;syntaxically&#32;correct|

***
### NotTested Outcome number 12

[Jump to summary definition](#summary-NotTested-12)	|	[Previous NotTested outcome](#nottested-outcome-number-11)	|	[Next NotTested outcome](#nottested-outcome-number-13)

:grey_question:NotTested outcome
#### Subject detail
|Name|modelet-manufacturing-environments-safety-rules|
|----|----|
|Title|Standalone&#32;modelet&#32;domains&#92;manufacturing-environments&#92;safety-rules&#92;onto.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Modelet manufacturing-environments/safety-rules](https://github.com/HyperAgents/hmas/blob/HEAD/domains/manufacturing-environments/safety-rules/onto.ttl)|

#### Criterion detail
|Identifier|[domain-and-range-referencing](https://ns.inria.fr/olivaw#domain-and-range-referencing)|
|----|----|
|Title|Domain&#32;and&#32;range&#32;referencing&#32;test|
|Description|A&#32;test&#32;case&#32;from&#32;the&#32;Best&#32;Practices&#32;tests&#32;checking&#32;if&#32;all&#32;the&#32;ranges&#32;and&#32;domains&#32;from&#32;the&#32;test&#32;subject&#32;point&#32;to&#32;terms&#32;that&#32;are&#32;defined&#32;in&#32;the&#32;vocabulary.|

#### Outcome Detail
|Jump|Type|:grey_question:NotTested|
|----|----|----|
|[Section top](#nottested-outcome-number-12)|Identifier|`range-out-of-vocabulary`|
|[Section top](#nottested-outcome-number-12)|Title|The&#32;test&#32;could&#32;not&#32;be&#32;run|
|[Section top](#nottested-outcome-number-12)|Description|The&#32;syntax&#32;of&#32;the&#32;subject&#32;and&#32;any&#32;of&#32;its&#32;imports&#32;must&#32;be&#32;syntaxically&#32;correct|

***
### NotTested Outcome number 13

[Jump to summary definition](#summary-NotTested-13)	|	[Previous NotTested outcome](#nottested-outcome-number-12)	|	[Next NotTested outcome](#nottested-outcome-number-14)

:grey_question:NotTested outcome
#### Subject detail
|Name|modelet-manufacturing-environments-safety-rules|
|----|----|
|Title|Standalone&#32;modelet&#32;domains&#92;manufacturing-environments&#92;safety-rules&#92;onto.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Modelet manufacturing-environments/safety-rules](https://github.com/HyperAgents/hmas/blob/HEAD/domains/manufacturing-environments/safety-rules/onto.ttl)|

#### Criterion detail
|Identifier|[labeled-terms](https://ns.inria.fr/olivaw#labeled-terms)|
|----|----|
|Title|Term&#32;labeling&#32;test|
|Description|A&#32;test&#32;case&#32;from&#32;the&#32;Best&#32;Practices&#32;tests&#32;checking&#32;if&#32;all&#32;the&#32;terms&#32;of&#32;the&#32;subject&#32;have&#32;a&#32;rdfs:label&#32;property&#32;pointing&#32;to&#32;a&#32;literal&#32;in&#32;English|

#### Outcome Detail
|Jump|Type|:grey_question:NotTested|
|----|----|----|
|[Section top](#nottested-outcome-number-13)|Identifier|`not-labeled-term`|
|[Section top](#nottested-outcome-number-13)|Title|The&#32;test&#32;could&#32;not&#32;be&#32;run|
|[Section top](#nottested-outcome-number-13)|Description|The&#32;subject&#32;and&#32;its&#32;recursive&#32;imports&#32;must&#32;be&#32;syntaxically&#32;correct|

***
### NotTested Outcome number 14

[Jump to summary definition](#summary-NotTested-14)	|	[Previous NotTested outcome](#nottested-outcome-number-13)	|	[Next NotTested outcome](#nottested-outcome-number-15)

:grey_question:NotTested outcome
#### Subject detail
|Name|modelet-manufacturing-environments-safety-rules|
|----|----|
|Title|Standalone&#32;modelet&#32;domains&#92;manufacturing-environments&#92;safety-rules&#92;onto.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Modelet manufacturing-environments/safety-rules](https://github.com/HyperAgents/hmas/blob/HEAD/domains/manufacturing-environments/safety-rules/onto.ttl)|

#### Criterion detail
|Identifier|[labeled-terms](https://ns.inria.fr/olivaw#labeled-terms)|
|----|----|
|Title|Term&#32;labeling&#32;test|
|Description|A&#32;test&#32;case&#32;from&#32;the&#32;Best&#32;Practices&#32;tests&#32;checking&#32;if&#32;all&#32;the&#32;terms&#32;of&#32;the&#32;subject&#32;have&#32;a&#32;rdfs:label&#32;property&#32;pointing&#32;to&#32;a&#32;literal&#32;in&#32;English|

#### Outcome Detail
|Jump|Type|:grey_question:NotTested|
|----|----|----|
|[Section top](#nottested-outcome-number-14)|Identifier|`not-labeled-term`|
|[Section top](#nottested-outcome-number-14)|Title|The&#32;test&#32;could&#32;not&#32;be&#32;run|
|[Section top](#nottested-outcome-number-14)|Description|The&#32;subject&#32;and&#32;its&#32;recursive&#32;imports&#32;must&#32;be&#32;syntaxically&#32;correct|

***
### NotTested Outcome number 15

[Jump to summary definition](#summary-NotTested-15)	|	[Previous NotTested outcome](#nottested-outcome-number-14)	|	[Next NotTested outcome](#nottested-outcome-number-16)

:grey_question:NotTested outcome
#### Subject detail
|Name|modelet-manufacturing-environments-safety-rules|
|----|----|
|Title|Standalone&#32;modelet&#32;domains&#92;manufacturing-environments&#92;safety-rules&#92;onto.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Modelet manufacturing-environments/safety-rules](https://github.com/HyperAgents/hmas/blob/HEAD/domains/manufacturing-environments/safety-rules/onto.ttl)|

#### Criterion detail
|Identifier|[owl-rl-constraint](https://ns.inria.fr/olivaw#owl-rl-constraint)|
|----|----|
|Title|OWL&#32;RL&#32;Constraint&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;check&#32;wether&#32;the&#32;test&#32;subject&#32;is&#32;syntaxically&#32;correct&#32;or&#32;not.|

#### Outcome Detail
|Jump|Type|:grey_question:NotTested|
|----|----|----|
|[Section top](#nottested-outcome-number-15)|Identifier|`owl-rl-constraint-violation`|
|[Section top](#nottested-outcome-number-15)|Title|The&#32;test&#32;could&#32;not&#32;be&#32;run|
|[Section top](#nottested-outcome-number-15)|Description|The&#32;subject&#32;and&#32;its&#32;recursive&#32;imports&#32;must&#32;be&#32;syntaxically&#32;correct|

***
### NotTested Outcome number 16

[Jump to summary definition](#summary-NotTested-16)	|	[Previous NotTested outcome](#nottested-outcome-number-15)	|	[Next NotTested outcome](#nottested-outcome-number-17)

:grey_question:NotTested outcome
#### Subject detail
|Name|modelet-manufacturing-environments-safety-rules|
|----|----|
|Title|Standalone&#32;modelet&#32;domains&#92;manufacturing-environments&#92;safety-rules&#92;onto.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Modelet manufacturing-environments/safety-rules](https://github.com/HyperAgents/hmas/blob/HEAD/domains/manufacturing-environments/safety-rules/onto.ttl)|

#### Criterion detail
|Identifier|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|
|----|----|
|Title|Profile&#32;compatibility&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;check&#32;whether&#32;the&#32;test&#32;subject&#32;is&#32;compatible&#32;with&#32;a&#32;profile&#32;or&#32;not,&#32;and&#32;if&#32;it&#32;is&#32;not,&#32;why.|

#### Outcome Detail
|Jump|Type|:grey_question:NotTested|
|----|----|----|
|[Section top](#nottested-outcome-number-16)|Identifier|`owl-el-profile-error`|
|[Section top](#nottested-outcome-number-16)|Title|The&#32;test&#32;could&#32;not&#32;be&#32;run|
|[Section top](#nottested-outcome-number-16)|Description|The&#32;subject&#32;must&#32;be&#32;syntaxically&#32;correct|

***
### NotTested Outcome number 17

[Jump to summary definition](#summary-NotTested-17)	|	[Previous NotTested outcome](#nottested-outcome-number-16)	|	[Next NotTested outcome](#nottested-outcome-number-18)

:grey_question:NotTested outcome
#### Subject detail
|Name|modelet-manufacturing-environments-safety-rules|
|----|----|
|Title|Standalone&#32;modelet&#32;domains&#92;manufacturing-environments&#92;safety-rules&#92;onto.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Modelet manufacturing-environments/safety-rules](https://github.com/HyperAgents/hmas/blob/HEAD/domains/manufacturing-environments/safety-rules/onto.ttl)|

#### Criterion detail
|Identifier|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|
|----|----|
|Title|Profile&#32;compatibility&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;check&#32;whether&#32;the&#32;test&#32;subject&#32;is&#32;compatible&#32;with&#32;a&#32;profile&#32;or&#32;not,&#32;and&#32;if&#32;it&#32;is&#32;not,&#32;why.|

#### Outcome Detail
|Jump|Type|:grey_question:NotTested|
|----|----|----|
|[Section top](#nottested-outcome-number-17)|Identifier|`owl-ql-profile-error`|
|[Section top](#nottested-outcome-number-17)|Title|The&#32;test&#32;could&#32;not&#32;be&#32;run|
|[Section top](#nottested-outcome-number-17)|Description|The&#32;subject&#32;must&#32;be&#32;syntaxically&#32;correct|

***
### NotTested Outcome number 18

[Jump to summary definition](#summary-NotTested-18)	|	[Previous NotTested outcome](#nottested-outcome-number-17)	|	[Next NotTested outcome](#nottested-outcome-number-19)

:grey_question:NotTested outcome
#### Subject detail
|Name|modelet-manufacturing-environments-safety-rules|
|----|----|
|Title|Standalone&#32;modelet&#32;domains&#92;manufacturing-environments&#92;safety-rules&#92;onto.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Modelet manufacturing-environments/safety-rules](https://github.com/HyperAgents/hmas/blob/HEAD/domains/manufacturing-environments/safety-rules/onto.ttl)|

#### Criterion detail
|Identifier|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|
|----|----|
|Title|Profile&#32;compatibility&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;check&#32;whether&#32;the&#32;test&#32;subject&#32;is&#32;compatible&#32;with&#32;a&#32;profile&#32;or&#32;not,&#32;and&#32;if&#32;it&#32;is&#32;not,&#32;why.|

#### Outcome Detail
|Jump|Type|:grey_question:NotTested|
|----|----|----|
|[Section top](#nottested-outcome-number-18)|Identifier|`owl-rl-profile-error`|
|[Section top](#nottested-outcome-number-18)|Title|The&#32;test&#32;could&#32;not&#32;be&#32;run|
|[Section top](#nottested-outcome-number-18)|Description|The&#32;subject&#32;must&#32;be&#32;syntaxically&#32;correct|

***
### NotTested Outcome number 19

[Jump to summary definition](#summary-NotTested-19)	|	[Previous NotTested outcome](#nottested-outcome-number-18)	|	[Next NotTested outcome](#nottested-outcome-number-20)

:grey_question:NotTested outcome
#### Subject detail
|Name|modelet-manufacturing-environments-safety-rules|
|----|----|
|Title|Standalone&#32;modelet&#32;domains&#92;manufacturing-environments&#92;safety-rules&#92;onto.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Modelet manufacturing-environments/safety-rules](https://github.com/HyperAgents/hmas/blob/HEAD/domains/manufacturing-environments/safety-rules/onto.ttl)|

#### Criterion detail
|Identifier|[term-referencing](https://ns.inria.fr/olivaw#term-referencing)|
|----|----|
|Title|Term&#32;referencing&#32;test|
|Description|A&#32;test&#32;case&#32;from&#32;the&#32;Best&#32;Practices&#32;tests&#32;checking&#32;if&#32;each&#32;term&#32;of&#32;the&#32;test&#32;subject&#32;is&#32;referenced&#32;to&#32;a&#32;module&#32;through&#32;a&#32;rdfs:isDefinedBy&#32;property.|

#### Outcome Detail
|Jump|Type|:grey_question:NotTested|
|----|----|----|
|[Section top](#nottested-outcome-number-19)|Identifier|`no-reference-module`|
|[Section top](#nottested-outcome-number-19)|Title|The&#32;test&#32;could&#32;not&#32;be&#32;run|
|[Section top](#nottested-outcome-number-19)|Description|The&#32;subject&#32;syntax&#32;must&#32;be&#32;correct|

***
### NotTested Outcome number 20

[Jump to summary definition](#summary-NotTested-20)	|	[Previous NotTested outcome](#nottested-outcome-number-19)	|	[Next NotTested outcome](#nottested-outcome-number-21)

:grey_question:NotTested outcome
#### Subject detail
|Name|modelet-manufacturing-environments-safety-rules|
|----|----|
|Title|Standalone&#32;modelet&#32;domains&#92;manufacturing-environments&#92;safety-rules&#92;onto.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Modelet manufacturing-environments/safety-rules](https://github.com/HyperAgents/hmas/blob/HEAD/domains/manufacturing-environments/safety-rules/onto.ttl)|

#### Criterion detail
|Identifier|[terms-differenciation](https://ns.inria.fr/olivaw#terms-differenciation)|
|----|----|
|Title|Terms&#32;differenciation&#32;test|
|Description|A&#32;test&#32;case&#32;from&#32;the&#32;Best&#32;Practices&#32;tests&#32;checking&#32;if&#32;all&#32;the&#32;terms&#32;are&#32;different&#32;enough&#32;from&#32;each&#32;other&#32;according&#32;to&#32;the&#32;Levenshtein&#32;distance&#32;metric.|

#### Outcome Detail
|Jump|Type|:grey_question:NotTested|
|----|----|----|
|[Section top](#nottested-outcome-number-20)|Identifier|`too-close-terms`|
|[Section top](#nottested-outcome-number-20)|Title|The&#32;test&#32;could&#32;not&#32;be&#32;run|
|[Section top](#nottested-outcome-number-20)|Description|The&#32;subject&#32;needs&#32;to&#32;be&#32;syntaxically&#32;correct|

***
### NotTested Outcome number 21

[Jump to summary definition](#summary-NotTested-21)	|	[Previous NotTested outcome](#nottested-outcome-number-20)	|	[Next NotTested outcome](#nottested-outcome-number-22)

:grey_question:NotTested outcome
#### Subject detail
|Name|modelet-logistics-structure-organization|
|----|----|
|Title|Standalone&#32;modelet&#32;domains&#92;logistics&#92;structure-organization&#92;onto.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Modelet logistics/structure-organization](https://github.com/HyperAgents/hmas/blob/HEAD/domains/logistics/structure-organization/onto.ttl)|

#### Criterion detail
|Identifier|[domain-and-range-referencing](https://ns.inria.fr/olivaw#domain-and-range-referencing)|
|----|----|
|Title|Domain&#32;and&#32;range&#32;referencing&#32;test|
|Description|A&#32;test&#32;case&#32;from&#32;the&#32;Best&#32;Practices&#32;tests&#32;checking&#32;if&#32;all&#32;the&#32;ranges&#32;and&#32;domains&#32;from&#32;the&#32;test&#32;subject&#32;point&#32;to&#32;terms&#32;that&#32;are&#32;defined&#32;in&#32;the&#32;vocabulary.|

#### Outcome Detail
|Jump|Type|:grey_question:NotTested|
|----|----|----|
|[Section top](#nottested-outcome-number-21)|Identifier|`domain-out-of-vocabulary`|
|[Section top](#nottested-outcome-number-21)|Title|The&#32;test&#32;could&#32;not&#32;be&#32;run|
|[Section top](#nottested-outcome-number-21)|Description|The&#32;syntax&#32;of&#32;the&#32;subject&#32;and&#32;any&#32;of&#32;its&#32;imports&#32;must&#32;be&#32;syntaxically&#32;correct|

***
### NotTested Outcome number 22

[Jump to summary definition](#summary-NotTested-22)	|	[Previous NotTested outcome](#nottested-outcome-number-21)	|	[Next NotTested outcome](#nottested-outcome-number-23)

:grey_question:NotTested outcome
#### Subject detail
|Name|modelet-logistics-structure-organization|
|----|----|
|Title|Standalone&#32;modelet&#32;domains&#92;logistics&#92;structure-organization&#92;onto.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Modelet logistics/structure-organization](https://github.com/HyperAgents/hmas/blob/HEAD/domains/logistics/structure-organization/onto.ttl)|

#### Criterion detail
|Identifier|[domain-and-range-referencing](https://ns.inria.fr/olivaw#domain-and-range-referencing)|
|----|----|
|Title|Domain&#32;and&#32;range&#32;referencing&#32;test|
|Description|A&#32;test&#32;case&#32;from&#32;the&#32;Best&#32;Practices&#32;tests&#32;checking&#32;if&#32;all&#32;the&#32;ranges&#32;and&#32;domains&#32;from&#32;the&#32;test&#32;subject&#32;point&#32;to&#32;terms&#32;that&#32;are&#32;defined&#32;in&#32;the&#32;vocabulary.|

#### Outcome Detail
|Jump|Type|:grey_question:NotTested|
|----|----|----|
|[Section top](#nottested-outcome-number-22)|Identifier|`range-out-of-vocabulary`|
|[Section top](#nottested-outcome-number-22)|Title|The&#32;test&#32;could&#32;not&#32;be&#32;run|
|[Section top](#nottested-outcome-number-22)|Description|The&#32;syntax&#32;of&#32;the&#32;subject&#32;and&#32;any&#32;of&#32;its&#32;imports&#32;must&#32;be&#32;syntaxically&#32;correct|

***
### NotTested Outcome number 23

[Jump to summary definition](#summary-NotTested-23)	|	[Previous NotTested outcome](#nottested-outcome-number-22)	|	[Next NotTested outcome](#nottested-outcome-number-24)

:grey_question:NotTested outcome
#### Subject detail
|Name|modelet-logistics-structure-organization|
|----|----|
|Title|Standalone&#32;modelet&#32;domains&#92;logistics&#92;structure-organization&#92;onto.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Modelet logistics/structure-organization](https://github.com/HyperAgents/hmas/blob/HEAD/domains/logistics/structure-organization/onto.ttl)|

#### Criterion detail
|Identifier|[labeled-terms](https://ns.inria.fr/olivaw#labeled-terms)|
|----|----|
|Title|Term&#32;labeling&#32;test|
|Description|A&#32;test&#32;case&#32;from&#32;the&#32;Best&#32;Practices&#32;tests&#32;checking&#32;if&#32;all&#32;the&#32;terms&#32;of&#32;the&#32;subject&#32;have&#32;a&#32;rdfs:label&#32;property&#32;pointing&#32;to&#32;a&#32;literal&#32;in&#32;English|

#### Outcome Detail
|Jump|Type|:grey_question:NotTested|
|----|----|----|
|[Section top](#nottested-outcome-number-23)|Identifier|`not-labeled-term`|
|[Section top](#nottested-outcome-number-23)|Title|The&#32;test&#32;could&#32;not&#32;be&#32;run|
|[Section top](#nottested-outcome-number-23)|Description|The&#32;subject&#32;and&#32;its&#32;recursive&#32;imports&#32;must&#32;be&#32;syntaxically&#32;correct|

***
### NotTested Outcome number 24

[Jump to summary definition](#summary-NotTested-24)	|	[Previous NotTested outcome](#nottested-outcome-number-23)	|	[Next NotTested outcome](#nottested-outcome-number-25)

:grey_question:NotTested outcome
#### Subject detail
|Name|modelet-logistics-structure-organization|
|----|----|
|Title|Standalone&#32;modelet&#32;domains&#92;logistics&#92;structure-organization&#92;onto.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Modelet logistics/structure-organization](https://github.com/HyperAgents/hmas/blob/HEAD/domains/logistics/structure-organization/onto.ttl)|

#### Criterion detail
|Identifier|[labeled-terms](https://ns.inria.fr/olivaw#labeled-terms)|
|----|----|
|Title|Term&#32;labeling&#32;test|
|Description|A&#32;test&#32;case&#32;from&#32;the&#32;Best&#32;Practices&#32;tests&#32;checking&#32;if&#32;all&#32;the&#32;terms&#32;of&#32;the&#32;subject&#32;have&#32;a&#32;rdfs:label&#32;property&#32;pointing&#32;to&#32;a&#32;literal&#32;in&#32;English|

#### Outcome Detail
|Jump|Type|:grey_question:NotTested|
|----|----|----|
|[Section top](#nottested-outcome-number-24)|Identifier|`not-labeled-term`|
|[Section top](#nottested-outcome-number-24)|Title|The&#32;test&#32;could&#32;not&#32;be&#32;run|
|[Section top](#nottested-outcome-number-24)|Description|The&#32;subject&#32;and&#32;its&#32;recursive&#32;imports&#32;must&#32;be&#32;syntaxically&#32;correct|

***
### NotTested Outcome number 25

[Jump to summary definition](#summary-NotTested-25)	|	[Previous NotTested outcome](#nottested-outcome-number-24)	|	[Next NotTested outcome](#nottested-outcome-number-26)

:grey_question:NotTested outcome
#### Subject detail
|Name|modelet-logistics-structure-organization|
|----|----|
|Title|Standalone&#32;modelet&#32;domains&#92;logistics&#92;structure-organization&#92;onto.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Modelet logistics/structure-organization](https://github.com/HyperAgents/hmas/blob/HEAD/domains/logistics/structure-organization/onto.ttl)|

#### Criterion detail
|Identifier|[owl-rl-constraint](https://ns.inria.fr/olivaw#owl-rl-constraint)|
|----|----|
|Title|OWL&#32;RL&#32;Constraint&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;check&#32;wether&#32;the&#32;test&#32;subject&#32;is&#32;syntaxically&#32;correct&#32;or&#32;not.|

#### Outcome Detail
|Jump|Type|:grey_question:NotTested|
|----|----|----|
|[Section top](#nottested-outcome-number-25)|Identifier|`owl-rl-constraint-violation`|
|[Section top](#nottested-outcome-number-25)|Title|The&#32;test&#32;could&#32;not&#32;be&#32;run|
|[Section top](#nottested-outcome-number-25)|Description|The&#32;subject&#32;and&#32;its&#32;recursive&#32;imports&#32;must&#32;be&#32;syntaxically&#32;correct|

***
### NotTested Outcome number 26

[Jump to summary definition](#summary-NotTested-26)	|	[Previous NotTested outcome](#nottested-outcome-number-25)	|	[Next NotTested outcome](#nottested-outcome-number-27)

:grey_question:NotTested outcome
#### Subject detail
|Name|modelet-logistics-structure-organization|
|----|----|
|Title|Standalone&#32;modelet&#32;domains&#92;logistics&#92;structure-organization&#92;onto.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Modelet logistics/structure-organization](https://github.com/HyperAgents/hmas/blob/HEAD/domains/logistics/structure-organization/onto.ttl)|

#### Criterion detail
|Identifier|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|
|----|----|
|Title|Profile&#32;compatibility&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;check&#32;whether&#32;the&#32;test&#32;subject&#32;is&#32;compatible&#32;with&#32;a&#32;profile&#32;or&#32;not,&#32;and&#32;if&#32;it&#32;is&#32;not,&#32;why.|

#### Outcome Detail
|Jump|Type|:grey_question:NotTested|
|----|----|----|
|[Section top](#nottested-outcome-number-26)|Identifier|`owl-el-profile-error`|
|[Section top](#nottested-outcome-number-26)|Title|The&#32;test&#32;could&#32;not&#32;be&#32;run|
|[Section top](#nottested-outcome-number-26)|Description|The&#32;subject&#32;must&#32;be&#32;syntaxically&#32;correct|

***
### NotTested Outcome number 27

[Jump to summary definition](#summary-NotTested-27)	|	[Previous NotTested outcome](#nottested-outcome-number-26)	|	[Next NotTested outcome](#nottested-outcome-number-28)

:grey_question:NotTested outcome
#### Subject detail
|Name|modelet-logistics-structure-organization|
|----|----|
|Title|Standalone&#32;modelet&#32;domains&#92;logistics&#92;structure-organization&#92;onto.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Modelet logistics/structure-organization](https://github.com/HyperAgents/hmas/blob/HEAD/domains/logistics/structure-organization/onto.ttl)|

#### Criterion detail
|Identifier|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|
|----|----|
|Title|Profile&#32;compatibility&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;check&#32;whether&#32;the&#32;test&#32;subject&#32;is&#32;compatible&#32;with&#32;a&#32;profile&#32;or&#32;not,&#32;and&#32;if&#32;it&#32;is&#32;not,&#32;why.|

#### Outcome Detail
|Jump|Type|:grey_question:NotTested|
|----|----|----|
|[Section top](#nottested-outcome-number-27)|Identifier|`owl-ql-profile-error`|
|[Section top](#nottested-outcome-number-27)|Title|The&#32;test&#32;could&#32;not&#32;be&#32;run|
|[Section top](#nottested-outcome-number-27)|Description|The&#32;subject&#32;must&#32;be&#32;syntaxically&#32;correct|

***
### NotTested Outcome number 28

[Jump to summary definition](#summary-NotTested-28)	|	[Previous NotTested outcome](#nottested-outcome-number-27)	|	[Next NotTested outcome](#nottested-outcome-number-29)

:grey_question:NotTested outcome
#### Subject detail
|Name|modelet-logistics-structure-organization|
|----|----|
|Title|Standalone&#32;modelet&#32;domains&#92;logistics&#92;structure-organization&#92;onto.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Modelet logistics/structure-organization](https://github.com/HyperAgents/hmas/blob/HEAD/domains/logistics/structure-organization/onto.ttl)|

#### Criterion detail
|Identifier|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|
|----|----|
|Title|Profile&#32;compatibility&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;check&#32;whether&#32;the&#32;test&#32;subject&#32;is&#32;compatible&#32;with&#32;a&#32;profile&#32;or&#32;not,&#32;and&#32;if&#32;it&#32;is&#32;not,&#32;why.|

#### Outcome Detail
|Jump|Type|:grey_question:NotTested|
|----|----|----|
|[Section top](#nottested-outcome-number-28)|Identifier|`owl-rl-profile-error`|
|[Section top](#nottested-outcome-number-28)|Title|The&#32;test&#32;could&#32;not&#32;be&#32;run|
|[Section top](#nottested-outcome-number-28)|Description|The&#32;subject&#32;must&#32;be&#32;syntaxically&#32;correct|

***
### NotTested Outcome number 29

[Jump to summary definition](#summary-NotTested-29)	|	[Previous NotTested outcome](#nottested-outcome-number-28)	|	[Next NotTested outcome](#nottested-outcome-number-30)

:grey_question:NotTested outcome
#### Subject detail
|Name|modelet-logistics-structure-organization|
|----|----|
|Title|Standalone&#32;modelet&#32;domains&#92;logistics&#92;structure-organization&#92;onto.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Modelet logistics/structure-organization](https://github.com/HyperAgents/hmas/blob/HEAD/domains/logistics/structure-organization/onto.ttl)|

#### Criterion detail
|Identifier|[term-referencing](https://ns.inria.fr/olivaw#term-referencing)|
|----|----|
|Title|Term&#32;referencing&#32;test|
|Description|A&#32;test&#32;case&#32;from&#32;the&#32;Best&#32;Practices&#32;tests&#32;checking&#32;if&#32;each&#32;term&#32;of&#32;the&#32;test&#32;subject&#32;is&#32;referenced&#32;to&#32;a&#32;module&#32;through&#32;a&#32;rdfs:isDefinedBy&#32;property.|

#### Outcome Detail
|Jump|Type|:grey_question:NotTested|
|----|----|----|
|[Section top](#nottested-outcome-number-29)|Identifier|`no-reference-module`|
|[Section top](#nottested-outcome-number-29)|Title|The&#32;test&#32;could&#32;not&#32;be&#32;run|
|[Section top](#nottested-outcome-number-29)|Description|The&#32;subject&#32;syntax&#32;must&#32;be&#32;correct|

***
### NotTested Outcome number 30

[Jump to summary definition](#summary-NotTested-30)	|	[Previous NotTested outcome](#nottested-outcome-number-29)	|	Next NotTested outcome

:grey_question:NotTested outcome
#### Subject detail
|Name|modelet-logistics-structure-organization|
|----|----|
|Title|Standalone&#32;modelet&#32;domains&#92;logistics&#92;structure-organization&#92;onto.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Modelet logistics/structure-organization](https://github.com/HyperAgents/hmas/blob/HEAD/domains/logistics/structure-organization/onto.ttl)|

#### Criterion detail
|Identifier|[terms-differenciation](https://ns.inria.fr/olivaw#terms-differenciation)|
|----|----|
|Title|Terms&#32;differenciation&#32;test|
|Description|A&#32;test&#32;case&#32;from&#32;the&#32;Best&#32;Practices&#32;tests&#32;checking&#32;if&#32;all&#32;the&#32;terms&#32;are&#32;different&#32;enough&#32;from&#32;each&#32;other&#32;according&#32;to&#32;the&#32;Levenshtein&#32;distance&#32;metric.|

#### Outcome Detail
|Jump|Type|:grey_question:NotTested|
|----|----|----|
|[Section top](#nottested-outcome-number-30)|Identifier|`too-close-terms`|
|[Section top](#nottested-outcome-number-30)|Title|The&#32;test&#32;could&#32;not&#32;be&#32;run|
|[Section top](#nottested-outcome-number-30)|Description|The&#32;subject&#32;needs&#32;to&#32;be&#32;syntaxically&#32;correct|

***

</details>

***


# Pass Outcomes

[Jump to statistic summary](#statistic-summary)	|	[Previous section](#nottested-outcomes)	|	Next section

Here is the chapter related to the Pass outcome

:white_check_mark:172 Pass outcomes

<details>
<summary>Fold/Unfold the 172 summary and details</summary>

## Pass Outcomes Summary

:white_check_mark:172 Pass outcomes

|*Jump*|*Number*|*Status*|*Subject*|*Criterion*|*Title*|*Link*|
|------|--------|--------|---------|-----------|-------|------|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-1">1/172</div>|:white_check_mark:Pass|`module-regulation`|[domain-and-range-referencing](https://ns.inria.fr/olivaw#domain-and-range-referencing)|Domains properly defined|[Jump](#pass-outcome-number-1)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-2">2/172</div>|:white_check_mark:Pass|`module-regulation`|[domain-and-range-referencing](https://ns.inria.fr/olivaw#domain-and-range-referencing)|Ranges properly defined|[Jump](#pass-outcome-number-2)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-3">3/172</div>|:white_check_mark:Pass|`module-regulation`|[labeled-terms](https://ns.inria.fr/olivaw#labeled-terms)|All terms labeled|[Jump](#pass-outcome-number-3)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-4">4/172</div>|:white_check_mark:Pass|`module-regulation`|[owl-rl-constraint](https://ns.inria.fr/olivaw#owl-rl-constraint)|OWL RL consistent|[Jump](#pass-outcome-number-4)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-5">5/172</div>|:white_check_mark:Pass|`module-regulation`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL EL Profile compatible|[Jump](#pass-outcome-number-5)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-6">6/172</div>|:white_check_mark:Pass|`module-regulation`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL QL Profile compatible|[Jump](#pass-outcome-number-6)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-7">7/172</div>|:white_check_mark:Pass|`module-regulation`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL RL Profile compatible|[Jump](#pass-outcome-number-7)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-8">8/172</div>|:white_check_mark:Pass|`module-regulation`|[proper-extension-predicate](https://ns.inria.fr/olivaw#proper-extension-predicate)|No class subproperty|[Jump](#pass-outcome-number-8)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-9">9/172</div>|:white_check_mark:Pass|`module-regulation`|[proper-extension-predicate](https://ns.inria.fr/olivaw#proper-extension-predicate)|No property subclass|[Jump](#pass-outcome-number-9)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-10">10/172</div>|:white_check_mark:Pass|`module-regulation`|[proper-extension-predicate](https://ns.inria.fr/olivaw#proper-extension-predicate)|No subclass of property|[Jump](#pass-outcome-number-10)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-11">11/172</div>|:white_check_mark:Pass|`module-regulation`|[proper-extension-predicate](https://ns.inria.fr/olivaw#proper-extension-predicate)|No subproperty of class|[Jump](#pass-outcome-number-11)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-12">12/172</div>|:white_check_mark:Pass|`module-regulation`|[term-referencing](https://ns.inria.fr/olivaw#term-referencing)|Any term is referenced|[Jump](#pass-outcome-number-12)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-13">13/172</div>|:white_check_mark:Pass|`module-interaction`|[domain-and-range-referencing](https://ns.inria.fr/olivaw#domain-and-range-referencing)|Domains properly defined|[Jump](#pass-outcome-number-13)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-14">14/172</div>|:white_check_mark:Pass|`module-interaction`|[domain-and-range-referencing](https://ns.inria.fr/olivaw#domain-and-range-referencing)|Ranges properly defined|[Jump](#pass-outcome-number-14)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-15">15/172</div>|:white_check_mark:Pass|`module-interaction`|[labeled-terms](https://ns.inria.fr/olivaw#labeled-terms)|All terms labeled|[Jump](#pass-outcome-number-15)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-16">16/172</div>|:white_check_mark:Pass|`module-interaction`|[owl-rl-constraint](https://ns.inria.fr/olivaw#owl-rl-constraint)|OWL RL consistent|[Jump](#pass-outcome-number-16)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-17">17/172</div>|:white_check_mark:Pass|`module-interaction`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL EL Profile compatible|[Jump](#pass-outcome-number-17)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-18">18/172</div>|:white_check_mark:Pass|`module-interaction`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL QL Profile compatible|[Jump](#pass-outcome-number-18)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-19">19/172</div>|:white_check_mark:Pass|`module-interaction`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL RL Profile compatible|[Jump](#pass-outcome-number-19)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-20">20/172</div>|:white_check_mark:Pass|`module-interaction`|[proper-extension-predicate](https://ns.inria.fr/olivaw#proper-extension-predicate)|No class subproperty|[Jump](#pass-outcome-number-20)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-21">21/172</div>|:white_check_mark:Pass|`module-interaction`|[proper-extension-predicate](https://ns.inria.fr/olivaw#proper-extension-predicate)|No property subclass|[Jump](#pass-outcome-number-21)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-22">22/172</div>|:white_check_mark:Pass|`module-interaction`|[proper-extension-predicate](https://ns.inria.fr/olivaw#proper-extension-predicate)|No subclass of property|[Jump](#pass-outcome-number-22)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-23">23/172</div>|:white_check_mark:Pass|`module-interaction`|[proper-extension-predicate](https://ns.inria.fr/olivaw#proper-extension-predicate)|No subproperty of class|[Jump](#pass-outcome-number-23)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-24">24/172</div>|:white_check_mark:Pass|`module-interaction`|[term-referencing](https://ns.inria.fr/olivaw#term-referencing)|Any term is referenced|[Jump](#pass-outcome-number-24)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-25">25/172</div>|:white_check_mark:Pass|`module-interaction`|[terms-differenciation](https://ns.inria.fr/olivaw#terms-differenciation)|Terms differenciated enough|[Jump](#pass-outcome-number-25)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-26">26/172</div>|:white_check_mark:Pass|`module-fipa`|[domain-and-range-referencing](https://ns.inria.fr/olivaw#domain-and-range-referencing)|Domains properly defined|[Jump](#pass-outcome-number-26)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-27">27/172</div>|:white_check_mark:Pass|`module-fipa`|[domain-and-range-referencing](https://ns.inria.fr/olivaw#domain-and-range-referencing)|Ranges properly defined|[Jump](#pass-outcome-number-27)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-28">28/172</div>|:white_check_mark:Pass|`module-fipa`|[labeled-terms](https://ns.inria.fr/olivaw#labeled-terms)|All terms labeled|[Jump](#pass-outcome-number-28)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-29">29/172</div>|:white_check_mark:Pass|`module-fipa`|[owl-rl-constraint](https://ns.inria.fr/olivaw#owl-rl-constraint)|OWL RL consistent|[Jump](#pass-outcome-number-29)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-30">30/172</div>|:white_check_mark:Pass|`module-fipa`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL EL Profile compatible|[Jump](#pass-outcome-number-30)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-31">31/172</div>|:white_check_mark:Pass|`module-fipa`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL QL Profile compatible|[Jump](#pass-outcome-number-31)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-32">32/172</div>|:white_check_mark:Pass|`module-fipa`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL RL Profile compatible|[Jump](#pass-outcome-number-32)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-33">33/172</div>|:white_check_mark:Pass|`module-fipa`|[proper-extension-predicate](https://ns.inria.fr/olivaw#proper-extension-predicate)|No class subproperty|[Jump](#pass-outcome-number-33)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-34">34/172</div>|:white_check_mark:Pass|`module-fipa`|[proper-extension-predicate](https://ns.inria.fr/olivaw#proper-extension-predicate)|No property subclass|[Jump](#pass-outcome-number-34)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-35">35/172</div>|:white_check_mark:Pass|`module-fipa`|[proper-extension-predicate](https://ns.inria.fr/olivaw#proper-extension-predicate)|No subclass of property|[Jump](#pass-outcome-number-35)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-36">36/172</div>|:white_check_mark:Pass|`module-fipa`|[proper-extension-predicate](https://ns.inria.fr/olivaw#proper-extension-predicate)|No subproperty of class|[Jump](#pass-outcome-number-36)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-37">37/172</div>|:white_check_mark:Pass|`module-fipa`|[terms-differenciation](https://ns.inria.fr/olivaw#terms-differenciation)|Terms differenciated enough|[Jump](#pass-outcome-number-37)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-38">38/172</div>|:white_check_mark:Pass|`module-core`|[domain-and-range-referencing](https://ns.inria.fr/olivaw#domain-and-range-referencing)|Domains properly defined|[Jump](#pass-outcome-number-38)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-39">39/172</div>|:white_check_mark:Pass|`module-core`|[domain-and-range-referencing](https://ns.inria.fr/olivaw#domain-and-range-referencing)|Ranges properly defined|[Jump](#pass-outcome-number-39)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-40">40/172</div>|:white_check_mark:Pass|`module-core`|[owl-rl-constraint](https://ns.inria.fr/olivaw#owl-rl-constraint)|OWL RL consistent|[Jump](#pass-outcome-number-40)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-41">41/172</div>|:white_check_mark:Pass|`module-core`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL RL Profile compatible|[Jump](#pass-outcome-number-41)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-42">42/172</div>|:white_check_mark:Pass|`module-core`|[proper-extension-predicate](https://ns.inria.fr/olivaw#proper-extension-predicate)|No class subproperty|[Jump](#pass-outcome-number-42)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-43">43/172</div>|:white_check_mark:Pass|`module-core`|[proper-extension-predicate](https://ns.inria.fr/olivaw#proper-extension-predicate)|No property subclass|[Jump](#pass-outcome-number-43)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-44">44/172</div>|:white_check_mark:Pass|`module-core`|[proper-extension-predicate](https://ns.inria.fr/olivaw#proper-extension-predicate)|No subclass of property|[Jump](#pass-outcome-number-44)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-45">45/172</div>|:white_check_mark:Pass|`module-core`|[proper-extension-predicate](https://ns.inria.fr/olivaw#proper-extension-predicate)|No subproperty of class|[Jump](#pass-outcome-number-45)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-46">46/172</div>|:white_check_mark:Pass|`module-core`|[term-referencing](https://ns.inria.fr/olivaw#term-referencing)|Any term is referenced|[Jump](#pass-outcome-number-46)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-47">47/172</div>|:white_check_mark:Pass|`module-core`|[terms-differenciation](https://ns.inria.fr/olivaw#terms-differenciation)|Terms differenciated enough|[Jump](#pass-outcome-number-47)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-48">48/172</div>|:white_check_mark:Pass|`module-alignment-interaction-td`|[domain-and-range-referencing](https://ns.inria.fr/olivaw#domain-and-range-referencing)|Domains properly defined|[Jump](#pass-outcome-number-48)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-49">49/172</div>|:white_check_mark:Pass|`module-alignment-interaction-td`|[domain-and-range-referencing](https://ns.inria.fr/olivaw#domain-and-range-referencing)|Ranges properly defined|[Jump](#pass-outcome-number-49)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-50">50/172</div>|:white_check_mark:Pass|`module-alignment-interaction-td`|[labeled-terms](https://ns.inria.fr/olivaw#labeled-terms)|All terms labeled|[Jump](#pass-outcome-number-50)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-51">51/172</div>|:white_check_mark:Pass|`module-alignment-interaction-td`|[owl-rl-constraint](https://ns.inria.fr/olivaw#owl-rl-constraint)|OWL RL consistent|[Jump](#pass-outcome-number-51)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-52">52/172</div>|:white_check_mark:Pass|`module-alignment-interaction-td`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL EL Profile compatible|[Jump](#pass-outcome-number-52)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-53">53/172</div>|:white_check_mark:Pass|`module-alignment-interaction-td`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL RL Profile compatible|[Jump](#pass-outcome-number-53)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-54">54/172</div>|:white_check_mark:Pass|`module-alignment-interaction-td`|[proper-extension-predicate](https://ns.inria.fr/olivaw#proper-extension-predicate)|No class subproperty|[Jump](#pass-outcome-number-54)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-55">55/172</div>|:white_check_mark:Pass|`module-alignment-interaction-td`|[proper-extension-predicate](https://ns.inria.fr/olivaw#proper-extension-predicate)|No property subclass|[Jump](#pass-outcome-number-55)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-56">56/172</div>|:white_check_mark:Pass|`module-alignment-interaction-td`|[proper-extension-predicate](https://ns.inria.fr/olivaw#proper-extension-predicate)|No subclass of property|[Jump](#pass-outcome-number-56)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-57">57/172</div>|:white_check_mark:Pass|`module-alignment-interaction-td`|[proper-extension-predicate](https://ns.inria.fr/olivaw#proper-extension-predicate)|No subproperty of class|[Jump](#pass-outcome-number-57)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-58">58/172</div>|:white_check_mark:Pass|`module-alignment-interaction-td`|[term-referencing](https://ns.inria.fr/olivaw#term-referencing)|Any term is referenced|[Jump](#pass-outcome-number-58)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-59">59/172</div>|:white_check_mark:Pass|`module-alignment-interaction-td`|[terms-differenciation](https://ns.inria.fr/olivaw#terms-differenciation)|Terms differenciated enough|[Jump](#pass-outcome-number-59)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-60">60/172</div>|:white_check_mark:Pass|`modelet-manufacturing-environments-discover-signifiers`|[domain-and-range-referencing](https://ns.inria.fr/olivaw#domain-and-range-referencing)|Domains properly defined|[Jump](#pass-outcome-number-60)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-61">61/172</div>|:white_check_mark:Pass|`modelet-manufacturing-environments-discover-signifiers`|[domain-and-range-referencing](https://ns.inria.fr/olivaw#domain-and-range-referencing)|Ranges properly defined|[Jump](#pass-outcome-number-61)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-62">62/172</div>|:white_check_mark:Pass|`modelet-manufacturing-environments-discover-signifiers`|[owl-rl-constraint](https://ns.inria.fr/olivaw#owl-rl-constraint)|OWL RL consistent|[Jump](#pass-outcome-number-62)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-63">63/172</div>|:white_check_mark:Pass|`modelet-manufacturing-environments-discover-signifiers`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL RL Profile compatible|[Jump](#pass-outcome-number-63)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-64">64/172</div>|:white_check_mark:Pass|`modelet-manufacturing-environments-discover-signifiers`|[proper-extension-predicate](https://ns.inria.fr/olivaw#proper-extension-predicate)|No class subproperty|[Jump](#pass-outcome-number-64)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-65">65/172</div>|:white_check_mark:Pass|`modelet-manufacturing-environments-discover-signifiers`|[proper-extension-predicate](https://ns.inria.fr/olivaw#proper-extension-predicate)|No property subclass|[Jump](#pass-outcome-number-65)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-66">66/172</div>|:white_check_mark:Pass|`modelet-manufacturing-environments-discover-signifiers`|[proper-extension-predicate](https://ns.inria.fr/olivaw#proper-extension-predicate)|No subclass of property|[Jump](#pass-outcome-number-66)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-67">67/172</div>|:white_check_mark:Pass|`modelet-manufacturing-environments-discover-signifiers`|[proper-extension-predicate](https://ns.inria.fr/olivaw#proper-extension-predicate)|No subproperty of class|[Jump](#pass-outcome-number-67)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-68">68/172</div>|:white_check_mark:Pass|`modelet-manufacturing-environments-discover-signifiers`|[term-referencing](https://ns.inria.fr/olivaw#term-referencing)|Any term is referenced|[Jump](#pass-outcome-number-68)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-69">69/172</div>|:white_check_mark:Pass|`modelet-manufacturing-environments-discover-signifiers`|[terms-differenciation](https://ns.inria.fr/olivaw#terms-differenciation)|Terms differenciated enough|[Jump](#pass-outcome-number-69)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-70">70/172</div>|:white_check_mark:Pass|`modelet-manufacturing-environments-discover-platforms`|[domain-and-range-referencing](https://ns.inria.fr/olivaw#domain-and-range-referencing)|Domains properly defined|[Jump](#pass-outcome-number-70)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-71">71/172</div>|:white_check_mark:Pass|`modelet-manufacturing-environments-discover-platforms`|[domain-and-range-referencing](https://ns.inria.fr/olivaw#domain-and-range-referencing)|Ranges properly defined|[Jump](#pass-outcome-number-71)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-72">72/172</div>|:white_check_mark:Pass|`modelet-manufacturing-environments-discover-platforms`|[labeled-terms](https://ns.inria.fr/olivaw#labeled-terms)|All terms labeled|[Jump](#pass-outcome-number-72)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-73">73/172</div>|:white_check_mark:Pass|`modelet-manufacturing-environments-discover-platforms`|[owl-rl-constraint](https://ns.inria.fr/olivaw#owl-rl-constraint)|OWL RL consistent|[Jump](#pass-outcome-number-73)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-74">74/172</div>|:white_check_mark:Pass|`modelet-manufacturing-environments-discover-platforms`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL QL Profile compatible|[Jump](#pass-outcome-number-74)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-75">75/172</div>|:white_check_mark:Pass|`modelet-manufacturing-environments-discover-platforms`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL RL Profile compatible|[Jump](#pass-outcome-number-75)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-76">76/172</div>|:white_check_mark:Pass|`modelet-manufacturing-environments-discover-platforms`|[proper-extension-predicate](https://ns.inria.fr/olivaw#proper-extension-predicate)|No class subproperty|[Jump](#pass-outcome-number-76)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-77">77/172</div>|:white_check_mark:Pass|`modelet-manufacturing-environments-discover-platforms`|[proper-extension-predicate](https://ns.inria.fr/olivaw#proper-extension-predicate)|No property subclass|[Jump](#pass-outcome-number-77)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-78">78/172</div>|:white_check_mark:Pass|`modelet-manufacturing-environments-discover-platforms`|[proper-extension-predicate](https://ns.inria.fr/olivaw#proper-extension-predicate)|No subclass of property|[Jump](#pass-outcome-number-78)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-79">79/172</div>|:white_check_mark:Pass|`modelet-manufacturing-environments-discover-platforms`|[proper-extension-predicate](https://ns.inria.fr/olivaw#proper-extension-predicate)|No subproperty of class|[Jump](#pass-outcome-number-79)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-80">80/172</div>|:white_check_mark:Pass|`modelet-manufacturing-environments-discover-platforms`|[term-referencing](https://ns.inria.fr/olivaw#term-referencing)|Any term is referenced|[Jump](#pass-outcome-number-80)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-81">81/172</div>|:white_check_mark:Pass|`modelet-manufacturing-environments-discover-platforms`|[terms-differenciation](https://ns.inria.fr/olivaw#terms-differenciation)|Terms differenciated enough|[Jump](#pass-outcome-number-81)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-82">82/172</div>|:white_check_mark:Pass|`modelet-manufacturing-environments-discover-organization`|[domain-and-range-referencing](https://ns.inria.fr/olivaw#domain-and-range-referencing)|Domains properly defined|[Jump](#pass-outcome-number-82)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-83">83/172</div>|:white_check_mark:Pass|`modelet-manufacturing-environments-discover-organization`|[domain-and-range-referencing](https://ns.inria.fr/olivaw#domain-and-range-referencing)|Ranges properly defined|[Jump](#pass-outcome-number-83)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-84">84/172</div>|:white_check_mark:Pass|`modelet-manufacturing-environments-discover-organization`|[labeled-terms](https://ns.inria.fr/olivaw#labeled-terms)|All terms labeled|[Jump](#pass-outcome-number-84)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-85">85/172</div>|:white_check_mark:Pass|`modelet-manufacturing-environments-discover-organization`|[owl-rl-constraint](https://ns.inria.fr/olivaw#owl-rl-constraint)|OWL RL consistent|[Jump](#pass-outcome-number-85)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-86">86/172</div>|:white_check_mark:Pass|`modelet-manufacturing-environments-discover-organization`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL EL Profile compatible|[Jump](#pass-outcome-number-86)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-87">87/172</div>|:white_check_mark:Pass|`modelet-manufacturing-environments-discover-organization`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL QL Profile compatible|[Jump](#pass-outcome-number-87)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-88">88/172</div>|:white_check_mark:Pass|`modelet-manufacturing-environments-discover-organization`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL RL Profile compatible|[Jump](#pass-outcome-number-88)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-89">89/172</div>|:white_check_mark:Pass|`modelet-manufacturing-environments-discover-organization`|[proper-extension-predicate](https://ns.inria.fr/olivaw#proper-extension-predicate)|No class subproperty|[Jump](#pass-outcome-number-89)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-90">90/172</div>|:white_check_mark:Pass|`modelet-manufacturing-environments-discover-organization`|[proper-extension-predicate](https://ns.inria.fr/olivaw#proper-extension-predicate)|No property subclass|[Jump](#pass-outcome-number-90)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-91">91/172</div>|:white_check_mark:Pass|`modelet-manufacturing-environments-discover-organization`|[proper-extension-predicate](https://ns.inria.fr/olivaw#proper-extension-predicate)|No subclass of property|[Jump](#pass-outcome-number-91)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-92">92/172</div>|:white_check_mark:Pass|`modelet-manufacturing-environments-discover-organization`|[proper-extension-predicate](https://ns.inria.fr/olivaw#proper-extension-predicate)|No subproperty of class|[Jump](#pass-outcome-number-92)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-93">93/172</div>|:white_check_mark:Pass|`modelet-manufacturing-environments-discover-organization`|[term-referencing](https://ns.inria.fr/olivaw#term-referencing)|Any term is referenced|[Jump](#pass-outcome-number-93)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-94">94/172</div>|:white_check_mark:Pass|`modelet-manufacturing-environments-discover-organization`|[terms-differenciation](https://ns.inria.fr/olivaw#terms-differenciation)|Terms differenciated enough|[Jump](#pass-outcome-number-94)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-95">95/172</div>|:white_check_mark:Pass|`modelet-manufacturing-environments-discover-core`|[domain-and-range-referencing](https://ns.inria.fr/olivaw#domain-and-range-referencing)|Domains properly defined|[Jump](#pass-outcome-number-95)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-96">96/172</div>|:white_check_mark:Pass|`modelet-manufacturing-environments-discover-core`|[domain-and-range-referencing](https://ns.inria.fr/olivaw#domain-and-range-referencing)|Ranges properly defined|[Jump](#pass-outcome-number-96)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-97">97/172</div>|:white_check_mark:Pass|`modelet-manufacturing-environments-discover-core`|[labeled-terms](https://ns.inria.fr/olivaw#labeled-terms)|All terms labeled|[Jump](#pass-outcome-number-97)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-98">98/172</div>|:white_check_mark:Pass|`modelet-manufacturing-environments-discover-core`|[owl-rl-constraint](https://ns.inria.fr/olivaw#owl-rl-constraint)|OWL RL consistent|[Jump](#pass-outcome-number-98)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-99">99/172</div>|:white_check_mark:Pass|`modelet-manufacturing-environments-discover-core`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL RL Profile compatible|[Jump](#pass-outcome-number-99)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-100">100/172</div>|:white_check_mark:Pass|`modelet-manufacturing-environments-discover-core`|[proper-extension-predicate](https://ns.inria.fr/olivaw#proper-extension-predicate)|No class subproperty|[Jump](#pass-outcome-number-100)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-101">101/172</div>|:white_check_mark:Pass|`modelet-manufacturing-environments-discover-core`|[proper-extension-predicate](https://ns.inria.fr/olivaw#proper-extension-predicate)|No property subclass|[Jump](#pass-outcome-number-101)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-102">102/172</div>|:white_check_mark:Pass|`modelet-manufacturing-environments-discover-core`|[proper-extension-predicate](https://ns.inria.fr/olivaw#proper-extension-predicate)|No subclass of property|[Jump](#pass-outcome-number-102)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-103">103/172</div>|:white_check_mark:Pass|`modelet-manufacturing-environments-discover-core`|[proper-extension-predicate](https://ns.inria.fr/olivaw#proper-extension-predicate)|No subproperty of class|[Jump](#pass-outcome-number-103)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-104">104/172</div>|:white_check_mark:Pass|`modelet-manufacturing-environments-discover-core`|[term-referencing](https://ns.inria.fr/olivaw#term-referencing)|Any term is referenced|[Jump](#pass-outcome-number-104)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-105">105/172</div>|:white_check_mark:Pass|`modelet-manufacturing-environments-discover-core`|[terms-differenciation](https://ns.inria.fr/olivaw#terms-differenciation)|Terms differenciated enough|[Jump](#pass-outcome-number-105)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-106">106/172</div>|:white_check_mark:Pass|`modelet-manufacturing-environments-discover-behavior-specifications`|[domain-and-range-referencing](https://ns.inria.fr/olivaw#domain-and-range-referencing)|Domains properly defined|[Jump](#pass-outcome-number-106)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-107">107/172</div>|:white_check_mark:Pass|`modelet-manufacturing-environments-discover-behavior-specifications`|[domain-and-range-referencing](https://ns.inria.fr/olivaw#domain-and-range-referencing)|Ranges properly defined|[Jump](#pass-outcome-number-107)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-108">108/172</div>|:white_check_mark:Pass|`modelet-manufacturing-environments-discover-behavior-specifications`|[labeled-terms](https://ns.inria.fr/olivaw#labeled-terms)|All terms labeled|[Jump](#pass-outcome-number-108)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-109">109/172</div>|:white_check_mark:Pass|`modelet-manufacturing-environments-discover-behavior-specifications`|[owl-rl-constraint](https://ns.inria.fr/olivaw#owl-rl-constraint)|OWL RL consistent|[Jump](#pass-outcome-number-109)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-110">110/172</div>|:white_check_mark:Pass|`modelet-manufacturing-environments-discover-behavior-specifications`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL EL Profile compatible|[Jump](#pass-outcome-number-110)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-111">111/172</div>|:white_check_mark:Pass|`modelet-manufacturing-environments-discover-behavior-specifications`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL QL Profile compatible|[Jump](#pass-outcome-number-111)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-112">112/172</div>|:white_check_mark:Pass|`modelet-manufacturing-environments-discover-behavior-specifications`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL RL Profile compatible|[Jump](#pass-outcome-number-112)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-113">113/172</div>|:white_check_mark:Pass|`modelet-manufacturing-environments-discover-behavior-specifications`|[proper-extension-predicate](https://ns.inria.fr/olivaw#proper-extension-predicate)|No class subproperty|[Jump](#pass-outcome-number-113)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-114">114/172</div>|:white_check_mark:Pass|`modelet-manufacturing-environments-discover-behavior-specifications`|[proper-extension-predicate](https://ns.inria.fr/olivaw#proper-extension-predicate)|No property subclass|[Jump](#pass-outcome-number-114)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-115">115/172</div>|:white_check_mark:Pass|`modelet-manufacturing-environments-discover-behavior-specifications`|[proper-extension-predicate](https://ns.inria.fr/olivaw#proper-extension-predicate)|No subclass of property|[Jump](#pass-outcome-number-115)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-116">116/172</div>|:white_check_mark:Pass|`modelet-manufacturing-environments-discover-behavior-specifications`|[proper-extension-predicate](https://ns.inria.fr/olivaw#proper-extension-predicate)|No subproperty of class|[Jump](#pass-outcome-number-116)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-117">117/172</div>|:white_check_mark:Pass|`modelet-manufacturing-environments-discover-behavior-specifications`|[term-referencing](https://ns.inria.fr/olivaw#term-referencing)|Any term is referenced|[Jump](#pass-outcome-number-117)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-118">118/172</div>|:white_check_mark:Pass|`modelet-manufacturing-environments-discover-behavior-specifications`|[terms-differenciation](https://ns.inria.fr/olivaw#terms-differenciation)|Terms differenciated enough|[Jump](#pass-outcome-number-118)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-119">119/172</div>|:white_check_mark:Pass|`modelet-logistics-create-organization`|[domain-and-range-referencing](https://ns.inria.fr/olivaw#domain-and-range-referencing)|Domains properly defined|[Jump](#pass-outcome-number-119)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-120">120/172</div>|:white_check_mark:Pass|`modelet-logistics-create-organization`|[domain-and-range-referencing](https://ns.inria.fr/olivaw#domain-and-range-referencing)|Ranges properly defined|[Jump](#pass-outcome-number-120)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-121">121/172</div>|:white_check_mark:Pass|`modelet-logistics-create-organization`|[labeled-terms](https://ns.inria.fr/olivaw#labeled-terms)|All terms labeled|[Jump](#pass-outcome-number-121)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-122">122/172</div>|:white_check_mark:Pass|`modelet-logistics-create-organization`|[owl-rl-constraint](https://ns.inria.fr/olivaw#owl-rl-constraint)|OWL RL consistent|[Jump](#pass-outcome-number-122)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-123">123/172</div>|:white_check_mark:Pass|`modelet-logistics-create-organization`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL EL Profile compatible|[Jump](#pass-outcome-number-123)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-124">124/172</div>|:white_check_mark:Pass|`modelet-logistics-create-organization`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL QL Profile compatible|[Jump](#pass-outcome-number-124)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-125">125/172</div>|:white_check_mark:Pass|`modelet-logistics-create-organization`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL RL Profile compatible|[Jump](#pass-outcome-number-125)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-126">126/172</div>|:white_check_mark:Pass|`modelet-logistics-create-organization`|[proper-extension-predicate](https://ns.inria.fr/olivaw#proper-extension-predicate)|No class subproperty|[Jump](#pass-outcome-number-126)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-127">127/172</div>|:white_check_mark:Pass|`modelet-logistics-create-organization`|[proper-extension-predicate](https://ns.inria.fr/olivaw#proper-extension-predicate)|No property subclass|[Jump](#pass-outcome-number-127)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-128">128/172</div>|:white_check_mark:Pass|`modelet-logistics-create-organization`|[proper-extension-predicate](https://ns.inria.fr/olivaw#proper-extension-predicate)|No subclass of property|[Jump](#pass-outcome-number-128)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-129">129/172</div>|:white_check_mark:Pass|`modelet-logistics-create-organization`|[proper-extension-predicate](https://ns.inria.fr/olivaw#proper-extension-predicate)|No subproperty of class|[Jump](#pass-outcome-number-129)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-130">130/172</div>|:white_check_mark:Pass|`modelet-logistics-create-organization`|[term-referencing](https://ns.inria.fr/olivaw#term-referencing)|Any term is referenced|[Jump](#pass-outcome-number-130)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-131">131/172</div>|:white_check_mark:Pass|`modelet-logistics-create-organization`|[terms-differenciation](https://ns.inria.fr/olivaw#terms-differenciation)|Terms differenciated enough|[Jump](#pass-outcome-number-131)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-132">132/172</div>|:white_check_mark:Pass|`modelet-logistics-coordinate-activities`|[domain-and-range-referencing](https://ns.inria.fr/olivaw#domain-and-range-referencing)|Domains properly defined|[Jump](#pass-outcome-number-132)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-133">133/172</div>|:white_check_mark:Pass|`modelet-logistics-coordinate-activities`|[domain-and-range-referencing](https://ns.inria.fr/olivaw#domain-and-range-referencing)|Ranges properly defined|[Jump](#pass-outcome-number-133)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-134">134/172</div>|:white_check_mark:Pass|`modelet-logistics-coordinate-activities`|[labeled-terms](https://ns.inria.fr/olivaw#labeled-terms)|All terms labeled|[Jump](#pass-outcome-number-134)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-135">135/172</div>|:white_check_mark:Pass|`modelet-logistics-coordinate-activities`|[owl-rl-constraint](https://ns.inria.fr/olivaw#owl-rl-constraint)|OWL RL consistent|[Jump](#pass-outcome-number-135)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-136">136/172</div>|:white_check_mark:Pass|`modelet-logistics-coordinate-activities`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL EL Profile compatible|[Jump](#pass-outcome-number-136)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-137">137/172</div>|:white_check_mark:Pass|`modelet-logistics-coordinate-activities`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL QL Profile compatible|[Jump](#pass-outcome-number-137)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-138">138/172</div>|:white_check_mark:Pass|`modelet-logistics-coordinate-activities`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL RL Profile compatible|[Jump](#pass-outcome-number-138)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-139">139/172</div>|:white_check_mark:Pass|`modelet-logistics-coordinate-activities`|[proper-extension-predicate](https://ns.inria.fr/olivaw#proper-extension-predicate)|No class subproperty|[Jump](#pass-outcome-number-139)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-140">140/172</div>|:white_check_mark:Pass|`modelet-logistics-coordinate-activities`|[proper-extension-predicate](https://ns.inria.fr/olivaw#proper-extension-predicate)|No property subclass|[Jump](#pass-outcome-number-140)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-141">141/172</div>|:white_check_mark:Pass|`modelet-logistics-coordinate-activities`|[proper-extension-predicate](https://ns.inria.fr/olivaw#proper-extension-predicate)|No subclass of property|[Jump](#pass-outcome-number-141)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-142">142/172</div>|:white_check_mark:Pass|`modelet-logistics-coordinate-activities`|[proper-extension-predicate](https://ns.inria.fr/olivaw#proper-extension-predicate)|No subproperty of class|[Jump](#pass-outcome-number-142)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-143">143/172</div>|:white_check_mark:Pass|`modelet-logistics-coordinate-activities`|[term-referencing](https://ns.inria.fr/olivaw#term-referencing)|Any term is referenced|[Jump](#pass-outcome-number-143)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-144">144/172</div>|:white_check_mark:Pass|`modelet-logistics-coordinate-activities`|[terms-differenciation](https://ns.inria.fr/olivaw#terms-differenciation)|Terms differenciated enough|[Jump](#pass-outcome-number-144)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-145">145/172</div>|:white_check_mark:Pass|`modelet-logistics-configure-organization`|[domain-and-range-referencing](https://ns.inria.fr/olivaw#domain-and-range-referencing)|Domains properly defined|[Jump](#pass-outcome-number-145)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-146">146/172</div>|:white_check_mark:Pass|`modelet-logistics-configure-organization`|[domain-and-range-referencing](https://ns.inria.fr/olivaw#domain-and-range-referencing)|Ranges properly defined|[Jump](#pass-outcome-number-146)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-147">147/172</div>|:white_check_mark:Pass|`modelet-logistics-configure-organization`|[labeled-terms](https://ns.inria.fr/olivaw#labeled-terms)|All terms labeled|[Jump](#pass-outcome-number-147)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-148">148/172</div>|:white_check_mark:Pass|`modelet-logistics-configure-organization`|[owl-rl-constraint](https://ns.inria.fr/olivaw#owl-rl-constraint)|OWL RL consistent|[Jump](#pass-outcome-number-148)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-149">149/172</div>|:white_check_mark:Pass|`modelet-logistics-configure-organization`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL EL Profile compatible|[Jump](#pass-outcome-number-149)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-150">150/172</div>|:white_check_mark:Pass|`modelet-logistics-configure-organization`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL QL Profile compatible|[Jump](#pass-outcome-number-150)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-151">151/172</div>|:white_check_mark:Pass|`modelet-logistics-configure-organization`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL RL Profile compatible|[Jump](#pass-outcome-number-151)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-152">152/172</div>|:white_check_mark:Pass|`modelet-logistics-configure-organization`|[proper-extension-predicate](https://ns.inria.fr/olivaw#proper-extension-predicate)|No class subproperty|[Jump](#pass-outcome-number-152)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-153">153/172</div>|:white_check_mark:Pass|`modelet-logistics-configure-organization`|[proper-extension-predicate](https://ns.inria.fr/olivaw#proper-extension-predicate)|No property subclass|[Jump](#pass-outcome-number-153)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-154">154/172</div>|:white_check_mark:Pass|`modelet-logistics-configure-organization`|[proper-extension-predicate](https://ns.inria.fr/olivaw#proper-extension-predicate)|No subclass of property|[Jump](#pass-outcome-number-154)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-155">155/172</div>|:white_check_mark:Pass|`modelet-logistics-configure-organization`|[proper-extension-predicate](https://ns.inria.fr/olivaw#proper-extension-predicate)|No subproperty of class|[Jump](#pass-outcome-number-155)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-156">156/172</div>|:white_check_mark:Pass|`modelet-logistics-configure-organization`|[term-referencing](https://ns.inria.fr/olivaw#term-referencing)|Any term is referenced|[Jump](#pass-outcome-number-156)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-157">157/172</div>|:white_check_mark:Pass|`all-modules`|[domain-and-range-referencing](https://ns.inria.fr/olivaw#domain-and-range-referencing)|Domains properly defined|[Jump](#pass-outcome-number-157)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-158">158/172</div>|:white_check_mark:Pass|`all-modules`|[domain-and-range-referencing](https://ns.inria.fr/olivaw#domain-and-range-referencing)|Ranges properly defined|[Jump](#pass-outcome-number-158)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-159">159/172</div>|:white_check_mark:Pass|`all-modules`|[owl-rl-constraint](https://ns.inria.fr/olivaw#owl-rl-constraint)|OWL RL consistent|[Jump](#pass-outcome-number-159)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-160">160/172</div>|:white_check_mark:Pass|`all-modules`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL RL Profile compatible|[Jump](#pass-outcome-number-160)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-161">161/172</div>|:white_check_mark:Pass|`all-modules`|[proper-extension-predicate](https://ns.inria.fr/olivaw#proper-extension-predicate)|No class subproperty|[Jump](#pass-outcome-number-161)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-162">162/172</div>|:white_check_mark:Pass|`all-modules`|[proper-extension-predicate](https://ns.inria.fr/olivaw#proper-extension-predicate)|No property subclass|[Jump](#pass-outcome-number-162)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-163">163/172</div>|:white_check_mark:Pass|`all-modules`|[proper-extension-predicate](https://ns.inria.fr/olivaw#proper-extension-predicate)|No subclass of property|[Jump](#pass-outcome-number-163)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-164">164/172</div>|:white_check_mark:Pass|`all-modules`|[proper-extension-predicate](https://ns.inria.fr/olivaw#proper-extension-predicate)|No subproperty of class|[Jump](#pass-outcome-number-164)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-165">165/172</div>|:white_check_mark:Pass|`all-fragments`|[domain-and-range-referencing](https://ns.inria.fr/olivaw#domain-and-range-referencing)|Domains properly defined|[Jump](#pass-outcome-number-165)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-166">166/172</div>|:white_check_mark:Pass|`all-fragments`|[domain-and-range-referencing](https://ns.inria.fr/olivaw#domain-and-range-referencing)|Ranges properly defined|[Jump](#pass-outcome-number-166)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-167">167/172</div>|:white_check_mark:Pass|`all-fragments`|[owl-rl-constraint](https://ns.inria.fr/olivaw#owl-rl-constraint)|OWL RL consistent|[Jump](#pass-outcome-number-167)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-168">168/172</div>|:white_check_mark:Pass|`all-fragments`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL RL Profile compatible|[Jump](#pass-outcome-number-168)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-169">169/172</div>|:white_check_mark:Pass|`all-fragments`|[proper-extension-predicate](https://ns.inria.fr/olivaw#proper-extension-predicate)|No class subproperty|[Jump](#pass-outcome-number-169)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-170">170/172</div>|:white_check_mark:Pass|`all-fragments`|[proper-extension-predicate](https://ns.inria.fr/olivaw#proper-extension-predicate)|No property subclass|[Jump](#pass-outcome-number-170)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-171">171/172</div>|:white_check_mark:Pass|`all-fragments`|[proper-extension-predicate](https://ns.inria.fr/olivaw#proper-extension-predicate)|No subclass of property|[Jump](#pass-outcome-number-171)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-172">172/172</div>|:white_check_mark:Pass|`all-fragments`|[proper-extension-predicate](https://ns.inria.fr/olivaw#proper-extension-predicate)|No subproperty of class|[Jump](#pass-outcome-number-172)|

***

## Pass Outcomes Details

This subchapter gives more details to the :white_check_mark:Pass outcomes

### Pass Outcome number 1

[Jump to summary definition](#summary-Pass-1)	|	Previous Pass outcome	|	[Next Pass outcome](#pass-outcome-number-2)

:white_check_mark:Pass outcome
#### Subject detail
|Name|module-regulation|
|----|----|
|Title|Standalone&#32;module&#32;src&#92;regulation.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Module regulation](https://github.com/HyperAgents/hmas/blob/HEAD/src/regulation.ttl)|

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
|Name|module-regulation|
|----|----|
|Title|Standalone&#32;module&#32;src&#92;regulation.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Module regulation](https://github.com/HyperAgents/hmas/blob/HEAD/src/regulation.ttl)|

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
|Name|module-regulation|
|----|----|
|Title|Standalone&#32;module&#32;src&#92;regulation.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Module regulation](https://github.com/HyperAgents/hmas/blob/HEAD/src/regulation.ttl)|

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
|Name|module-regulation|
|----|----|
|Title|Standalone&#32;module&#32;src&#92;regulation.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Module regulation](https://github.com/HyperAgents/hmas/blob/HEAD/src/regulation.ttl)|

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
|Name|module-regulation|
|----|----|
|Title|Standalone&#32;module&#32;src&#92;regulation.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Module regulation](https://github.com/HyperAgents/hmas/blob/HEAD/src/regulation.ttl)|

#### Criterion detail
|Identifier|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|
|----|----|
|Title|Profile&#32;compatibility&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;check&#32;whether&#32;the&#32;test&#32;subject&#32;is&#32;compatible&#32;with&#32;a&#32;profile&#32;or&#32;not,&#32;and&#32;if&#32;it&#32;is&#32;not,&#32;why.|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-5)|Identifier|`owl-el-profile-error`|
|[Section top](#pass-outcome-number-5)|Title|OWL&#32;EL&#32;Profile&#32;compatible|
|[Section top](#pass-outcome-number-5)|Description|The&#32;subject&#32;is&#32;included&#32;in&#32;the&#32;OWL&#32;EL&#32;sublanguage|

***
### Pass Outcome number 6

[Jump to summary definition](#summary-Pass-6)	|	[Previous Pass outcome](#pass-outcome-number-5)	|	[Next Pass outcome](#pass-outcome-number-7)

:white_check_mark:Pass outcome
#### Subject detail
|Name|module-regulation|
|----|----|
|Title|Standalone&#32;module&#32;src&#92;regulation.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Module regulation](https://github.com/HyperAgents/hmas/blob/HEAD/src/regulation.ttl)|

#### Criterion detail
|Identifier|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|
|----|----|
|Title|Profile&#32;compatibility&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;check&#32;whether&#32;the&#32;test&#32;subject&#32;is&#32;compatible&#32;with&#32;a&#32;profile&#32;or&#32;not,&#32;and&#32;if&#32;it&#32;is&#32;not,&#32;why.|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-6)|Identifier|`owl-ql-profile-error`|
|[Section top](#pass-outcome-number-6)|Title|OWL&#32;QL&#32;Profile&#32;compatible|
|[Section top](#pass-outcome-number-6)|Description|The&#32;subject&#32;is&#32;included&#32;in&#32;the&#32;OWL&#32;QL&#32;sublanguage|

***
### Pass Outcome number 7

[Jump to summary definition](#summary-Pass-7)	|	[Previous Pass outcome](#pass-outcome-number-6)	|	[Next Pass outcome](#pass-outcome-number-8)

:white_check_mark:Pass outcome
#### Subject detail
|Name|module-regulation|
|----|----|
|Title|Standalone&#32;module&#32;src&#92;regulation.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Module regulation](https://github.com/HyperAgents/hmas/blob/HEAD/src/regulation.ttl)|

#### Criterion detail
|Identifier|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|
|----|----|
|Title|Profile&#32;compatibility&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;check&#32;whether&#32;the&#32;test&#32;subject&#32;is&#32;compatible&#32;with&#32;a&#32;profile&#32;or&#32;not,&#32;and&#32;if&#32;it&#32;is&#32;not,&#32;why.|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-7)|Identifier|`owl-rl-profile-error`|
|[Section top](#pass-outcome-number-7)|Title|OWL&#32;RL&#32;Profile&#32;compatible|
|[Section top](#pass-outcome-number-7)|Description|The&#32;subject&#32;is&#32;included&#32;in&#32;the&#32;OWL&#32;RL&#32;sublanguage|

***
### Pass Outcome number 8

[Jump to summary definition](#summary-Pass-8)	|	[Previous Pass outcome](#pass-outcome-number-7)	|	[Next Pass outcome](#pass-outcome-number-9)

:white_check_mark:Pass outcome
#### Subject detail
|Name|module-regulation|
|----|----|
|Title|Standalone&#32;module&#32;src&#92;regulation.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Module regulation](https://github.com/HyperAgents/hmas/blob/HEAD/src/regulation.ttl)|

#### Criterion detail
|Identifier|[proper-extension-predicate](https://ns.inria.fr/olivaw#proper-extension-predicate)|
|----|----|
|Title|Predicate&#32;extension&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;test&#32;the&#32;proper&#32;use&#32;of&#32;predicates&#32;rdfs:subClassOf&#32;and&#32;rdfs:subPropertyOf&#32;on&#32;the&#32;ontology&#32;terms|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-8)|Identifier|`class-subpropertyof`|
|[Section top](#pass-outcome-number-8)|Title|No&#32;class&#32;subproperty|
|[Section top](#pass-outcome-number-8)|Description|No&#32;ontology&#32;class&#32;is&#32;a&#32;subproperty|

***
### Pass Outcome number 9

[Jump to summary definition](#summary-Pass-9)	|	[Previous Pass outcome](#pass-outcome-number-8)	|	[Next Pass outcome](#pass-outcome-number-10)

:white_check_mark:Pass outcome
#### Subject detail
|Name|module-regulation|
|----|----|
|Title|Standalone&#32;module&#32;src&#92;regulation.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Module regulation](https://github.com/HyperAgents/hmas/blob/HEAD/src/regulation.ttl)|

#### Criterion detail
|Identifier|[proper-extension-predicate](https://ns.inria.fr/olivaw#proper-extension-predicate)|
|----|----|
|Title|Predicate&#32;extension&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;test&#32;the&#32;proper&#32;use&#32;of&#32;predicates&#32;rdfs:subClassOf&#32;and&#32;rdfs:subPropertyOf&#32;on&#32;the&#32;ontology&#32;terms|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-9)|Identifier|`property-subclassof`|
|[Section top](#pass-outcome-number-9)|Title|No&#32;property&#32;subclass|
|[Section top](#pass-outcome-number-9)|Description|No&#32;ontology&#32;property&#32;is&#32;a&#32;subclass|

***
### Pass Outcome number 10

[Jump to summary definition](#summary-Pass-10)	|	[Previous Pass outcome](#pass-outcome-number-9)	|	[Next Pass outcome](#pass-outcome-number-11)

:white_check_mark:Pass outcome
#### Subject detail
|Name|module-regulation|
|----|----|
|Title|Standalone&#32;module&#32;src&#92;regulation.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Module regulation](https://github.com/HyperAgents/hmas/blob/HEAD/src/regulation.ttl)|

#### Criterion detail
|Identifier|[proper-extension-predicate](https://ns.inria.fr/olivaw#proper-extension-predicate)|
|----|----|
|Title|Predicate&#32;extension&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;test&#32;the&#32;proper&#32;use&#32;of&#32;predicates&#32;rdfs:subClassOf&#32;and&#32;rdfs:subPropertyOf&#32;on&#32;the&#32;ontology&#32;terms|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-10)|Identifier|`subclassof-property`|
|[Section top](#pass-outcome-number-10)|Title|No&#32;subclass&#32;of&#32;property|
|[Section top](#pass-outcome-number-10)|Description|No&#32;ontology&#32;term&#32;is&#32;a&#32;subclass&#32;of&#32;a&#32;property|

***
### Pass Outcome number 11

[Jump to summary definition](#summary-Pass-11)	|	[Previous Pass outcome](#pass-outcome-number-10)	|	[Next Pass outcome](#pass-outcome-number-12)

:white_check_mark:Pass outcome
#### Subject detail
|Name|module-regulation|
|----|----|
|Title|Standalone&#32;module&#32;src&#92;regulation.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Module regulation](https://github.com/HyperAgents/hmas/blob/HEAD/src/regulation.ttl)|

#### Criterion detail
|Identifier|[proper-extension-predicate](https://ns.inria.fr/olivaw#proper-extension-predicate)|
|----|----|
|Title|Predicate&#32;extension&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;test&#32;the&#32;proper&#32;use&#32;of&#32;predicates&#32;rdfs:subClassOf&#32;and&#32;rdfs:subPropertyOf&#32;on&#32;the&#32;ontology&#32;terms|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-11)|Identifier|`subpropertyof-class`|
|[Section top](#pass-outcome-number-11)|Title|No&#32;subproperty&#32;of&#32;class|
|[Section top](#pass-outcome-number-11)|Description|No&#32;ontology&#32;term&#32;is&#32;a&#32;subproperty&#32;of&#32;a&#32;class|

***
### Pass Outcome number 12

[Jump to summary definition](#summary-Pass-12)	|	[Previous Pass outcome](#pass-outcome-number-11)	|	[Next Pass outcome](#pass-outcome-number-13)

:white_check_mark:Pass outcome
#### Subject detail
|Name|module-regulation|
|----|----|
|Title|Standalone&#32;module&#32;src&#92;regulation.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Module regulation](https://github.com/HyperAgents/hmas/blob/HEAD/src/regulation.ttl)|

#### Criterion detail
|Identifier|[term-referencing](https://ns.inria.fr/olivaw#term-referencing)|
|----|----|
|Title|Term&#32;referencing&#32;test|
|Description|A&#32;test&#32;case&#32;from&#32;the&#32;Best&#32;Practices&#32;tests&#32;checking&#32;if&#32;each&#32;term&#32;of&#32;the&#32;test&#32;subject&#32;is&#32;referenced&#32;to&#32;a&#32;module&#32;through&#32;a&#32;rdfs:isDefinedBy&#32;property.|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-12)|Identifier|`no-reference-module`|
|[Section top](#pass-outcome-number-12)|Title|Any&#32;term&#32;is&#32;referenced|
|[Section top](#pass-outcome-number-12)|Description|Each&#32;term&#32;of&#32;the&#32;test&#32;subject&#32;is&#32;linked&#32;to&#32;a&#32;module&#32;by&#32;a&#32;rdfs:isDefinedBy&#32;property|

***
### Pass Outcome number 13

[Jump to summary definition](#summary-Pass-13)	|	[Previous Pass outcome](#pass-outcome-number-12)	|	[Next Pass outcome](#pass-outcome-number-14)

:white_check_mark:Pass outcome
#### Subject detail
|Name|module-interaction|
|----|----|
|Title|Standalone&#32;module&#32;src&#92;interaction.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Module interaction](https://github.com/HyperAgents/hmas/blob/HEAD/src/interaction.ttl)|

#### Criterion detail
|Identifier|[domain-and-range-referencing](https://ns.inria.fr/olivaw#domain-and-range-referencing)|
|----|----|
|Title|Domain&#32;and&#32;range&#32;referencing&#32;test|
|Description|A&#32;test&#32;case&#32;from&#32;the&#32;Best&#32;Practices&#32;tests&#32;checking&#32;if&#32;all&#32;the&#32;ranges&#32;and&#32;domains&#32;from&#32;the&#32;test&#32;subject&#32;point&#32;to&#32;terms&#32;that&#32;are&#32;defined&#32;in&#32;the&#32;vocabulary.|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-13)|Identifier|`domain-out-of-vocabulary`|
|[Section top](#pass-outcome-number-13)|Title|Domains&#32;properly&#32;defined|
|[Section top](#pass-outcome-number-13)|Description|Each&#32;rdfs:domain&#32;is&#32;defined&#32;within&#32;the&#32;fragment|

***
### Pass Outcome number 14

[Jump to summary definition](#summary-Pass-14)	|	[Previous Pass outcome](#pass-outcome-number-13)	|	[Next Pass outcome](#pass-outcome-number-15)

:white_check_mark:Pass outcome
#### Subject detail
|Name|module-interaction|
|----|----|
|Title|Standalone&#32;module&#32;src&#92;interaction.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Module interaction](https://github.com/HyperAgents/hmas/blob/HEAD/src/interaction.ttl)|

#### Criterion detail
|Identifier|[domain-and-range-referencing](https://ns.inria.fr/olivaw#domain-and-range-referencing)|
|----|----|
|Title|Domain&#32;and&#32;range&#32;referencing&#32;test|
|Description|A&#32;test&#32;case&#32;from&#32;the&#32;Best&#32;Practices&#32;tests&#32;checking&#32;if&#32;all&#32;the&#32;ranges&#32;and&#32;domains&#32;from&#32;the&#32;test&#32;subject&#32;point&#32;to&#32;terms&#32;that&#32;are&#32;defined&#32;in&#32;the&#32;vocabulary.|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-14)|Identifier|`range-out-of-vocabulary`|
|[Section top](#pass-outcome-number-14)|Title|Ranges&#32;properly&#32;defined|
|[Section top](#pass-outcome-number-14)|Description|Each&#32;rdfs:range&#32;is&#32;defined&#32;within&#32;the&#32;fragment|

***
### Pass Outcome number 15

[Jump to summary definition](#summary-Pass-15)	|	[Previous Pass outcome](#pass-outcome-number-14)	|	[Next Pass outcome](#pass-outcome-number-16)

:white_check_mark:Pass outcome
#### Subject detail
|Name|module-interaction|
|----|----|
|Title|Standalone&#32;module&#32;src&#92;interaction.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Module interaction](https://github.com/HyperAgents/hmas/blob/HEAD/src/interaction.ttl)|

#### Criterion detail
|Identifier|[labeled-terms](https://ns.inria.fr/olivaw#labeled-terms)|
|----|----|
|Title|Term&#32;labeling&#32;test|
|Description|A&#32;test&#32;case&#32;from&#32;the&#32;Best&#32;Practices&#32;tests&#32;checking&#32;if&#32;all&#32;the&#32;terms&#32;of&#32;the&#32;subject&#32;have&#32;a&#32;rdfs:label&#32;property&#32;pointing&#32;to&#32;a&#32;literal&#32;in&#32;English|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-15)|Identifier|`not-labeled-term`|
|[Section top](#pass-outcome-number-15)|Title|All&#32;terms&#32;labeled|
|[Section top](#pass-outcome-number-15)|Description|All&#32;the&#32;terms&#32;defined&#32;in&#32;the&#32;subject&#32;have&#32;a&#32;rdfs:label&#32;in&#32;English|

***
### Pass Outcome number 16

[Jump to summary definition](#summary-Pass-16)	|	[Previous Pass outcome](#pass-outcome-number-15)	|	[Next Pass outcome](#pass-outcome-number-17)

:white_check_mark:Pass outcome
#### Subject detail
|Name|module-interaction|
|----|----|
|Title|Standalone&#32;module&#32;src&#92;interaction.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Module interaction](https://github.com/HyperAgents/hmas/blob/HEAD/src/interaction.ttl)|

#### Criterion detail
|Identifier|[owl-rl-constraint](https://ns.inria.fr/olivaw#owl-rl-constraint)|
|----|----|
|Title|OWL&#32;RL&#32;Constraint&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;check&#32;wether&#32;the&#32;test&#32;subject&#32;is&#32;syntaxically&#32;correct&#32;or&#32;not.|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-16)|Identifier|`owl-rl-constraint-violation`|
|[Section top](#pass-outcome-number-16)|Title|OWL&#32;RL&#32;consistent|
|[Section top](#pass-outcome-number-16)|Description|The&#32;provided&#32;graph&#32;is&#32;consistent&#32;for&#32;any&#32;OWL&#32;RL&#32;constraint|

***
### Pass Outcome number 17

[Jump to summary definition](#summary-Pass-17)	|	[Previous Pass outcome](#pass-outcome-number-16)	|	[Next Pass outcome](#pass-outcome-number-18)

:white_check_mark:Pass outcome
#### Subject detail
|Name|module-interaction|
|----|----|
|Title|Standalone&#32;module&#32;src&#92;interaction.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Module interaction](https://github.com/HyperAgents/hmas/blob/HEAD/src/interaction.ttl)|

#### Criterion detail
|Identifier|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|
|----|----|
|Title|Profile&#32;compatibility&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;check&#32;whether&#32;the&#32;test&#32;subject&#32;is&#32;compatible&#32;with&#32;a&#32;profile&#32;or&#32;not,&#32;and&#32;if&#32;it&#32;is&#32;not,&#32;why.|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-17)|Identifier|`owl-el-profile-error`|
|[Section top](#pass-outcome-number-17)|Title|OWL&#32;EL&#32;Profile&#32;compatible|
|[Section top](#pass-outcome-number-17)|Description|The&#32;subject&#32;is&#32;included&#32;in&#32;the&#32;OWL&#32;EL&#32;sublanguage|

***
### Pass Outcome number 18

[Jump to summary definition](#summary-Pass-18)	|	[Previous Pass outcome](#pass-outcome-number-17)	|	[Next Pass outcome](#pass-outcome-number-19)

:white_check_mark:Pass outcome
#### Subject detail
|Name|module-interaction|
|----|----|
|Title|Standalone&#32;module&#32;src&#92;interaction.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Module interaction](https://github.com/HyperAgents/hmas/blob/HEAD/src/interaction.ttl)|

#### Criterion detail
|Identifier|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|
|----|----|
|Title|Profile&#32;compatibility&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;check&#32;whether&#32;the&#32;test&#32;subject&#32;is&#32;compatible&#32;with&#32;a&#32;profile&#32;or&#32;not,&#32;and&#32;if&#32;it&#32;is&#32;not,&#32;why.|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-18)|Identifier|`owl-ql-profile-error`|
|[Section top](#pass-outcome-number-18)|Title|OWL&#32;QL&#32;Profile&#32;compatible|
|[Section top](#pass-outcome-number-18)|Description|The&#32;subject&#32;is&#32;included&#32;in&#32;the&#32;OWL&#32;QL&#32;sublanguage|

***
### Pass Outcome number 19

[Jump to summary definition](#summary-Pass-19)	|	[Previous Pass outcome](#pass-outcome-number-18)	|	[Next Pass outcome](#pass-outcome-number-20)

:white_check_mark:Pass outcome
#### Subject detail
|Name|module-interaction|
|----|----|
|Title|Standalone&#32;module&#32;src&#92;interaction.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Module interaction](https://github.com/HyperAgents/hmas/blob/HEAD/src/interaction.ttl)|

#### Criterion detail
|Identifier|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|
|----|----|
|Title|Profile&#32;compatibility&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;check&#32;whether&#32;the&#32;test&#32;subject&#32;is&#32;compatible&#32;with&#32;a&#32;profile&#32;or&#32;not,&#32;and&#32;if&#32;it&#32;is&#32;not,&#32;why.|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-19)|Identifier|`owl-rl-profile-error`|
|[Section top](#pass-outcome-number-19)|Title|OWL&#32;RL&#32;Profile&#32;compatible|
|[Section top](#pass-outcome-number-19)|Description|The&#32;subject&#32;is&#32;included&#32;in&#32;the&#32;OWL&#32;RL&#32;sublanguage|

***
### Pass Outcome number 20

[Jump to summary definition](#summary-Pass-20)	|	[Previous Pass outcome](#pass-outcome-number-19)	|	[Next Pass outcome](#pass-outcome-number-21)

:white_check_mark:Pass outcome
#### Subject detail
|Name|module-interaction|
|----|----|
|Title|Standalone&#32;module&#32;src&#92;interaction.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Module interaction](https://github.com/HyperAgents/hmas/blob/HEAD/src/interaction.ttl)|

#### Criterion detail
|Identifier|[proper-extension-predicate](https://ns.inria.fr/olivaw#proper-extension-predicate)|
|----|----|
|Title|Predicate&#32;extension&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;test&#32;the&#32;proper&#32;use&#32;of&#32;predicates&#32;rdfs:subClassOf&#32;and&#32;rdfs:subPropertyOf&#32;on&#32;the&#32;ontology&#32;terms|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-20)|Identifier|`class-subpropertyof`|
|[Section top](#pass-outcome-number-20)|Title|No&#32;class&#32;subproperty|
|[Section top](#pass-outcome-number-20)|Description|No&#32;ontology&#32;class&#32;is&#32;a&#32;subproperty|

***
### Pass Outcome number 21

[Jump to summary definition](#summary-Pass-21)	|	[Previous Pass outcome](#pass-outcome-number-20)	|	[Next Pass outcome](#pass-outcome-number-22)

:white_check_mark:Pass outcome
#### Subject detail
|Name|module-interaction|
|----|----|
|Title|Standalone&#32;module&#32;src&#92;interaction.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Module interaction](https://github.com/HyperAgents/hmas/blob/HEAD/src/interaction.ttl)|

#### Criterion detail
|Identifier|[proper-extension-predicate](https://ns.inria.fr/olivaw#proper-extension-predicate)|
|----|----|
|Title|Predicate&#32;extension&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;test&#32;the&#32;proper&#32;use&#32;of&#32;predicates&#32;rdfs:subClassOf&#32;and&#32;rdfs:subPropertyOf&#32;on&#32;the&#32;ontology&#32;terms|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-21)|Identifier|`property-subclassof`|
|[Section top](#pass-outcome-number-21)|Title|No&#32;property&#32;subclass|
|[Section top](#pass-outcome-number-21)|Description|No&#32;ontology&#32;property&#32;is&#32;a&#32;subclass|

***
### Pass Outcome number 22

[Jump to summary definition](#summary-Pass-22)	|	[Previous Pass outcome](#pass-outcome-number-21)	|	[Next Pass outcome](#pass-outcome-number-23)

:white_check_mark:Pass outcome
#### Subject detail
|Name|module-interaction|
|----|----|
|Title|Standalone&#32;module&#32;src&#92;interaction.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Module interaction](https://github.com/HyperAgents/hmas/blob/HEAD/src/interaction.ttl)|

#### Criterion detail
|Identifier|[proper-extension-predicate](https://ns.inria.fr/olivaw#proper-extension-predicate)|
|----|----|
|Title|Predicate&#32;extension&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;test&#32;the&#32;proper&#32;use&#32;of&#32;predicates&#32;rdfs:subClassOf&#32;and&#32;rdfs:subPropertyOf&#32;on&#32;the&#32;ontology&#32;terms|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-22)|Identifier|`subclassof-property`|
|[Section top](#pass-outcome-number-22)|Title|No&#32;subclass&#32;of&#32;property|
|[Section top](#pass-outcome-number-22)|Description|No&#32;ontology&#32;term&#32;is&#32;a&#32;subclass&#32;of&#32;a&#32;property|

***
### Pass Outcome number 23

[Jump to summary definition](#summary-Pass-23)	|	[Previous Pass outcome](#pass-outcome-number-22)	|	[Next Pass outcome](#pass-outcome-number-24)

:white_check_mark:Pass outcome
#### Subject detail
|Name|module-interaction|
|----|----|
|Title|Standalone&#32;module&#32;src&#92;interaction.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Module interaction](https://github.com/HyperAgents/hmas/blob/HEAD/src/interaction.ttl)|

#### Criterion detail
|Identifier|[proper-extension-predicate](https://ns.inria.fr/olivaw#proper-extension-predicate)|
|----|----|
|Title|Predicate&#32;extension&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;test&#32;the&#32;proper&#32;use&#32;of&#32;predicates&#32;rdfs:subClassOf&#32;and&#32;rdfs:subPropertyOf&#32;on&#32;the&#32;ontology&#32;terms|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-23)|Identifier|`subpropertyof-class`|
|[Section top](#pass-outcome-number-23)|Title|No&#32;subproperty&#32;of&#32;class|
|[Section top](#pass-outcome-number-23)|Description|No&#32;ontology&#32;term&#32;is&#32;a&#32;subproperty&#32;of&#32;a&#32;class|

***
### Pass Outcome number 24

[Jump to summary definition](#summary-Pass-24)	|	[Previous Pass outcome](#pass-outcome-number-23)	|	[Next Pass outcome](#pass-outcome-number-25)

:white_check_mark:Pass outcome
#### Subject detail
|Name|module-interaction|
|----|----|
|Title|Standalone&#32;module&#32;src&#92;interaction.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Module interaction](https://github.com/HyperAgents/hmas/blob/HEAD/src/interaction.ttl)|

#### Criterion detail
|Identifier|[term-referencing](https://ns.inria.fr/olivaw#term-referencing)|
|----|----|
|Title|Term&#32;referencing&#32;test|
|Description|A&#32;test&#32;case&#32;from&#32;the&#32;Best&#32;Practices&#32;tests&#32;checking&#32;if&#32;each&#32;term&#32;of&#32;the&#32;test&#32;subject&#32;is&#32;referenced&#32;to&#32;a&#32;module&#32;through&#32;a&#32;rdfs:isDefinedBy&#32;property.|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-24)|Identifier|`no-reference-module`|
|[Section top](#pass-outcome-number-24)|Title|Any&#32;term&#32;is&#32;referenced|
|[Section top](#pass-outcome-number-24)|Description|Each&#32;term&#32;of&#32;the&#32;test&#32;subject&#32;is&#32;linked&#32;to&#32;a&#32;module&#32;by&#32;a&#32;rdfs:isDefinedBy&#32;property|

***
### Pass Outcome number 25

[Jump to summary definition](#summary-Pass-25)	|	[Previous Pass outcome](#pass-outcome-number-24)	|	[Next Pass outcome](#pass-outcome-number-26)

:white_check_mark:Pass outcome
#### Subject detail
|Name|module-interaction|
|----|----|
|Title|Standalone&#32;module&#32;src&#92;interaction.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Module interaction](https://github.com/HyperAgents/hmas/blob/HEAD/src/interaction.ttl)|

#### Criterion detail
|Identifier|[terms-differenciation](https://ns.inria.fr/olivaw#terms-differenciation)|
|----|----|
|Title|Terms&#32;differenciation&#32;test|
|Description|A&#32;test&#32;case&#32;from&#32;the&#32;Best&#32;Practices&#32;tests&#32;checking&#32;if&#32;all&#32;the&#32;terms&#32;are&#32;different&#32;enough&#32;from&#32;each&#32;other&#32;according&#32;to&#32;the&#32;Levenshtein&#32;distance&#32;metric.|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-25)|Identifier|`too-close-terms`|
|[Section top](#pass-outcome-number-25)|Title|Terms&#32;differenciated&#32;enough|
|[Section top](#pass-outcome-number-25)|Description|All&#32;the&#32;terms&#32;have&#32;have&#32;a&#32;satisfying&#32;Levenshtein&#32;distance&#32;from&#32;each&#32;other&#32;term.|

***
### Pass Outcome number 26

[Jump to summary definition](#summary-Pass-26)	|	[Previous Pass outcome](#pass-outcome-number-25)	|	[Next Pass outcome](#pass-outcome-number-27)

:white_check_mark:Pass outcome
#### Subject detail
|Name|module-fipa|
|----|----|
|Title|Standalone&#32;module&#32;src&#92;fipa.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Module fipa](https://github.com/HyperAgents/hmas/blob/HEAD/src/fipa.ttl)|

#### Criterion detail
|Identifier|[domain-and-range-referencing](https://ns.inria.fr/olivaw#domain-and-range-referencing)|
|----|----|
|Title|Domain&#32;and&#32;range&#32;referencing&#32;test|
|Description|A&#32;test&#32;case&#32;from&#32;the&#32;Best&#32;Practices&#32;tests&#32;checking&#32;if&#32;all&#32;the&#32;ranges&#32;and&#32;domains&#32;from&#32;the&#32;test&#32;subject&#32;point&#32;to&#32;terms&#32;that&#32;are&#32;defined&#32;in&#32;the&#32;vocabulary.|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-26)|Identifier|`domain-out-of-vocabulary`|
|[Section top](#pass-outcome-number-26)|Title|Domains&#32;properly&#32;defined|
|[Section top](#pass-outcome-number-26)|Description|Each&#32;rdfs:domain&#32;is&#32;defined&#32;within&#32;the&#32;fragment|

***
### Pass Outcome number 27

[Jump to summary definition](#summary-Pass-27)	|	[Previous Pass outcome](#pass-outcome-number-26)	|	[Next Pass outcome](#pass-outcome-number-28)

:white_check_mark:Pass outcome
#### Subject detail
|Name|module-fipa|
|----|----|
|Title|Standalone&#32;module&#32;src&#92;fipa.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Module fipa](https://github.com/HyperAgents/hmas/blob/HEAD/src/fipa.ttl)|

#### Criterion detail
|Identifier|[domain-and-range-referencing](https://ns.inria.fr/olivaw#domain-and-range-referencing)|
|----|----|
|Title|Domain&#32;and&#32;range&#32;referencing&#32;test|
|Description|A&#32;test&#32;case&#32;from&#32;the&#32;Best&#32;Practices&#32;tests&#32;checking&#32;if&#32;all&#32;the&#32;ranges&#32;and&#32;domains&#32;from&#32;the&#32;test&#32;subject&#32;point&#32;to&#32;terms&#32;that&#32;are&#32;defined&#32;in&#32;the&#32;vocabulary.|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-27)|Identifier|`range-out-of-vocabulary`|
|[Section top](#pass-outcome-number-27)|Title|Ranges&#32;properly&#32;defined|
|[Section top](#pass-outcome-number-27)|Description|Each&#32;rdfs:range&#32;is&#32;defined&#32;within&#32;the&#32;fragment|

***
### Pass Outcome number 28

[Jump to summary definition](#summary-Pass-28)	|	[Previous Pass outcome](#pass-outcome-number-27)	|	[Next Pass outcome](#pass-outcome-number-29)

:white_check_mark:Pass outcome
#### Subject detail
|Name|module-fipa|
|----|----|
|Title|Standalone&#32;module&#32;src&#92;fipa.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Module fipa](https://github.com/HyperAgents/hmas/blob/HEAD/src/fipa.ttl)|

#### Criterion detail
|Identifier|[labeled-terms](https://ns.inria.fr/olivaw#labeled-terms)|
|----|----|
|Title|Term&#32;labeling&#32;test|
|Description|A&#32;test&#32;case&#32;from&#32;the&#32;Best&#32;Practices&#32;tests&#32;checking&#32;if&#32;all&#32;the&#32;terms&#32;of&#32;the&#32;subject&#32;have&#32;a&#32;rdfs:label&#32;property&#32;pointing&#32;to&#32;a&#32;literal&#32;in&#32;English|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-28)|Identifier|`not-labeled-term`|
|[Section top](#pass-outcome-number-28)|Title|All&#32;terms&#32;labeled|
|[Section top](#pass-outcome-number-28)|Description|All&#32;the&#32;terms&#32;defined&#32;in&#32;the&#32;subject&#32;have&#32;a&#32;rdfs:label&#32;in&#32;English|

***
### Pass Outcome number 29

[Jump to summary definition](#summary-Pass-29)	|	[Previous Pass outcome](#pass-outcome-number-28)	|	[Next Pass outcome](#pass-outcome-number-30)

:white_check_mark:Pass outcome
#### Subject detail
|Name|module-fipa|
|----|----|
|Title|Standalone&#32;module&#32;src&#92;fipa.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Module fipa](https://github.com/HyperAgents/hmas/blob/HEAD/src/fipa.ttl)|

#### Criterion detail
|Identifier|[owl-rl-constraint](https://ns.inria.fr/olivaw#owl-rl-constraint)|
|----|----|
|Title|OWL&#32;RL&#32;Constraint&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;check&#32;wether&#32;the&#32;test&#32;subject&#32;is&#32;syntaxically&#32;correct&#32;or&#32;not.|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-29)|Identifier|`owl-rl-constraint-violation`|
|[Section top](#pass-outcome-number-29)|Title|OWL&#32;RL&#32;consistent|
|[Section top](#pass-outcome-number-29)|Description|The&#32;provided&#32;graph&#32;is&#32;consistent&#32;for&#32;any&#32;OWL&#32;RL&#32;constraint|

***
### Pass Outcome number 30

[Jump to summary definition](#summary-Pass-30)	|	[Previous Pass outcome](#pass-outcome-number-29)	|	[Next Pass outcome](#pass-outcome-number-31)

:white_check_mark:Pass outcome
#### Subject detail
|Name|module-fipa|
|----|----|
|Title|Standalone&#32;module&#32;src&#92;fipa.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Module fipa](https://github.com/HyperAgents/hmas/blob/HEAD/src/fipa.ttl)|

#### Criterion detail
|Identifier|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|
|----|----|
|Title|Profile&#32;compatibility&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;check&#32;whether&#32;the&#32;test&#32;subject&#32;is&#32;compatible&#32;with&#32;a&#32;profile&#32;or&#32;not,&#32;and&#32;if&#32;it&#32;is&#32;not,&#32;why.|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-30)|Identifier|`owl-el-profile-error`|
|[Section top](#pass-outcome-number-30)|Title|OWL&#32;EL&#32;Profile&#32;compatible|
|[Section top](#pass-outcome-number-30)|Description|The&#32;subject&#32;is&#32;included&#32;in&#32;the&#32;OWL&#32;EL&#32;sublanguage|

***
### Pass Outcome number 31

[Jump to summary definition](#summary-Pass-31)	|	[Previous Pass outcome](#pass-outcome-number-30)	|	[Next Pass outcome](#pass-outcome-number-32)

:white_check_mark:Pass outcome
#### Subject detail
|Name|module-fipa|
|----|----|
|Title|Standalone&#32;module&#32;src&#92;fipa.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Module fipa](https://github.com/HyperAgents/hmas/blob/HEAD/src/fipa.ttl)|

#### Criterion detail
|Identifier|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|
|----|----|
|Title|Profile&#32;compatibility&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;check&#32;whether&#32;the&#32;test&#32;subject&#32;is&#32;compatible&#32;with&#32;a&#32;profile&#32;or&#32;not,&#32;and&#32;if&#32;it&#32;is&#32;not,&#32;why.|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-31)|Identifier|`owl-ql-profile-error`|
|[Section top](#pass-outcome-number-31)|Title|OWL&#32;QL&#32;Profile&#32;compatible|
|[Section top](#pass-outcome-number-31)|Description|The&#32;subject&#32;is&#32;included&#32;in&#32;the&#32;OWL&#32;QL&#32;sublanguage|

***
### Pass Outcome number 32

[Jump to summary definition](#summary-Pass-32)	|	[Previous Pass outcome](#pass-outcome-number-31)	|	[Next Pass outcome](#pass-outcome-number-33)

:white_check_mark:Pass outcome
#### Subject detail
|Name|module-fipa|
|----|----|
|Title|Standalone&#32;module&#32;src&#92;fipa.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Module fipa](https://github.com/HyperAgents/hmas/blob/HEAD/src/fipa.ttl)|

#### Criterion detail
|Identifier|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|
|----|----|
|Title|Profile&#32;compatibility&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;check&#32;whether&#32;the&#32;test&#32;subject&#32;is&#32;compatible&#32;with&#32;a&#32;profile&#32;or&#32;not,&#32;and&#32;if&#32;it&#32;is&#32;not,&#32;why.|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-32)|Identifier|`owl-rl-profile-error`|
|[Section top](#pass-outcome-number-32)|Title|OWL&#32;RL&#32;Profile&#32;compatible|
|[Section top](#pass-outcome-number-32)|Description|The&#32;subject&#32;is&#32;included&#32;in&#32;the&#32;OWL&#32;RL&#32;sublanguage|

***
### Pass Outcome number 33

[Jump to summary definition](#summary-Pass-33)	|	[Previous Pass outcome](#pass-outcome-number-32)	|	[Next Pass outcome](#pass-outcome-number-34)

:white_check_mark:Pass outcome
#### Subject detail
|Name|module-fipa|
|----|----|
|Title|Standalone&#32;module&#32;src&#92;fipa.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Module fipa](https://github.com/HyperAgents/hmas/blob/HEAD/src/fipa.ttl)|

#### Criterion detail
|Identifier|[proper-extension-predicate](https://ns.inria.fr/olivaw#proper-extension-predicate)|
|----|----|
|Title|Predicate&#32;extension&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;test&#32;the&#32;proper&#32;use&#32;of&#32;predicates&#32;rdfs:subClassOf&#32;and&#32;rdfs:subPropertyOf&#32;on&#32;the&#32;ontology&#32;terms|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-33)|Identifier|`class-subpropertyof`|
|[Section top](#pass-outcome-number-33)|Title|No&#32;class&#32;subproperty|
|[Section top](#pass-outcome-number-33)|Description|No&#32;ontology&#32;class&#32;is&#32;a&#32;subproperty|

***
### Pass Outcome number 34

[Jump to summary definition](#summary-Pass-34)	|	[Previous Pass outcome](#pass-outcome-number-33)	|	[Next Pass outcome](#pass-outcome-number-35)

:white_check_mark:Pass outcome
#### Subject detail
|Name|module-fipa|
|----|----|
|Title|Standalone&#32;module&#32;src&#92;fipa.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Module fipa](https://github.com/HyperAgents/hmas/blob/HEAD/src/fipa.ttl)|

#### Criterion detail
|Identifier|[proper-extension-predicate](https://ns.inria.fr/olivaw#proper-extension-predicate)|
|----|----|
|Title|Predicate&#32;extension&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;test&#32;the&#32;proper&#32;use&#32;of&#32;predicates&#32;rdfs:subClassOf&#32;and&#32;rdfs:subPropertyOf&#32;on&#32;the&#32;ontology&#32;terms|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-34)|Identifier|`property-subclassof`|
|[Section top](#pass-outcome-number-34)|Title|No&#32;property&#32;subclass|
|[Section top](#pass-outcome-number-34)|Description|No&#32;ontology&#32;property&#32;is&#32;a&#32;subclass|

***
### Pass Outcome number 35

[Jump to summary definition](#summary-Pass-35)	|	[Previous Pass outcome](#pass-outcome-number-34)	|	[Next Pass outcome](#pass-outcome-number-36)

:white_check_mark:Pass outcome
#### Subject detail
|Name|module-fipa|
|----|----|
|Title|Standalone&#32;module&#32;src&#92;fipa.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Module fipa](https://github.com/HyperAgents/hmas/blob/HEAD/src/fipa.ttl)|

#### Criterion detail
|Identifier|[proper-extension-predicate](https://ns.inria.fr/olivaw#proper-extension-predicate)|
|----|----|
|Title|Predicate&#32;extension&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;test&#32;the&#32;proper&#32;use&#32;of&#32;predicates&#32;rdfs:subClassOf&#32;and&#32;rdfs:subPropertyOf&#32;on&#32;the&#32;ontology&#32;terms|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-35)|Identifier|`subclassof-property`|
|[Section top](#pass-outcome-number-35)|Title|No&#32;subclass&#32;of&#32;property|
|[Section top](#pass-outcome-number-35)|Description|No&#32;ontology&#32;term&#32;is&#32;a&#32;subclass&#32;of&#32;a&#32;property|

***
### Pass Outcome number 36

[Jump to summary definition](#summary-Pass-36)	|	[Previous Pass outcome](#pass-outcome-number-35)	|	[Next Pass outcome](#pass-outcome-number-37)

:white_check_mark:Pass outcome
#### Subject detail
|Name|module-fipa|
|----|----|
|Title|Standalone&#32;module&#32;src&#92;fipa.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Module fipa](https://github.com/HyperAgents/hmas/blob/HEAD/src/fipa.ttl)|

#### Criterion detail
|Identifier|[proper-extension-predicate](https://ns.inria.fr/olivaw#proper-extension-predicate)|
|----|----|
|Title|Predicate&#32;extension&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;test&#32;the&#32;proper&#32;use&#32;of&#32;predicates&#32;rdfs:subClassOf&#32;and&#32;rdfs:subPropertyOf&#32;on&#32;the&#32;ontology&#32;terms|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-36)|Identifier|`subpropertyof-class`|
|[Section top](#pass-outcome-number-36)|Title|No&#32;subproperty&#32;of&#32;class|
|[Section top](#pass-outcome-number-36)|Description|No&#32;ontology&#32;term&#32;is&#32;a&#32;subproperty&#32;of&#32;a&#32;class|

***
### Pass Outcome number 37

[Jump to summary definition](#summary-Pass-37)	|	[Previous Pass outcome](#pass-outcome-number-36)	|	[Next Pass outcome](#pass-outcome-number-38)

:white_check_mark:Pass outcome
#### Subject detail
|Name|module-fipa|
|----|----|
|Title|Standalone&#32;module&#32;src&#92;fipa.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Module fipa](https://github.com/HyperAgents/hmas/blob/HEAD/src/fipa.ttl)|

#### Criterion detail
|Identifier|[terms-differenciation](https://ns.inria.fr/olivaw#terms-differenciation)|
|----|----|
|Title|Terms&#32;differenciation&#32;test|
|Description|A&#32;test&#32;case&#32;from&#32;the&#32;Best&#32;Practices&#32;tests&#32;checking&#32;if&#32;all&#32;the&#32;terms&#32;are&#32;different&#32;enough&#32;from&#32;each&#32;other&#32;according&#32;to&#32;the&#32;Levenshtein&#32;distance&#32;metric.|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-37)|Identifier|`too-close-terms`|
|[Section top](#pass-outcome-number-37)|Title|Terms&#32;differenciated&#32;enough|
|[Section top](#pass-outcome-number-37)|Description|All&#32;the&#32;terms&#32;have&#32;have&#32;a&#32;satisfying&#32;Levenshtein&#32;distance&#32;from&#32;each&#32;other&#32;term.|

***
### Pass Outcome number 38

[Jump to summary definition](#summary-Pass-38)	|	[Previous Pass outcome](#pass-outcome-number-37)	|	[Next Pass outcome](#pass-outcome-number-39)

:white_check_mark:Pass outcome
#### Subject detail
|Name|module-core|
|----|----|
|Title|Standalone&#32;module&#32;src&#92;core.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Module core](https://github.com/HyperAgents/hmas/blob/HEAD/src/core.ttl)|

#### Criterion detail
|Identifier|[domain-and-range-referencing](https://ns.inria.fr/olivaw#domain-and-range-referencing)|
|----|----|
|Title|Domain&#32;and&#32;range&#32;referencing&#32;test|
|Description|A&#32;test&#32;case&#32;from&#32;the&#32;Best&#32;Practices&#32;tests&#32;checking&#32;if&#32;all&#32;the&#32;ranges&#32;and&#32;domains&#32;from&#32;the&#32;test&#32;subject&#32;point&#32;to&#32;terms&#32;that&#32;are&#32;defined&#32;in&#32;the&#32;vocabulary.|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-38)|Identifier|`domain-out-of-vocabulary`|
|[Section top](#pass-outcome-number-38)|Title|Domains&#32;properly&#32;defined|
|[Section top](#pass-outcome-number-38)|Description|Each&#32;rdfs:domain&#32;is&#32;defined&#32;within&#32;the&#32;fragment|

***
### Pass Outcome number 39

[Jump to summary definition](#summary-Pass-39)	|	[Previous Pass outcome](#pass-outcome-number-38)	|	[Next Pass outcome](#pass-outcome-number-40)

:white_check_mark:Pass outcome
#### Subject detail
|Name|module-core|
|----|----|
|Title|Standalone&#32;module&#32;src&#92;core.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Module core](https://github.com/HyperAgents/hmas/blob/HEAD/src/core.ttl)|

#### Criterion detail
|Identifier|[domain-and-range-referencing](https://ns.inria.fr/olivaw#domain-and-range-referencing)|
|----|----|
|Title|Domain&#32;and&#32;range&#32;referencing&#32;test|
|Description|A&#32;test&#32;case&#32;from&#32;the&#32;Best&#32;Practices&#32;tests&#32;checking&#32;if&#32;all&#32;the&#32;ranges&#32;and&#32;domains&#32;from&#32;the&#32;test&#32;subject&#32;point&#32;to&#32;terms&#32;that&#32;are&#32;defined&#32;in&#32;the&#32;vocabulary.|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-39)|Identifier|`range-out-of-vocabulary`|
|[Section top](#pass-outcome-number-39)|Title|Ranges&#32;properly&#32;defined|
|[Section top](#pass-outcome-number-39)|Description|Each&#32;rdfs:range&#32;is&#32;defined&#32;within&#32;the&#32;fragment|

***
### Pass Outcome number 40

[Jump to summary definition](#summary-Pass-40)	|	[Previous Pass outcome](#pass-outcome-number-39)	|	[Next Pass outcome](#pass-outcome-number-41)

:white_check_mark:Pass outcome
#### Subject detail
|Name|module-core|
|----|----|
|Title|Standalone&#32;module&#32;src&#92;core.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Module core](https://github.com/HyperAgents/hmas/blob/HEAD/src/core.ttl)|

#### Criterion detail
|Identifier|[owl-rl-constraint](https://ns.inria.fr/olivaw#owl-rl-constraint)|
|----|----|
|Title|OWL&#32;RL&#32;Constraint&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;check&#32;wether&#32;the&#32;test&#32;subject&#32;is&#32;syntaxically&#32;correct&#32;or&#32;not.|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-40)|Identifier|`owl-rl-constraint-violation`|
|[Section top](#pass-outcome-number-40)|Title|OWL&#32;RL&#32;consistent|
|[Section top](#pass-outcome-number-40)|Description|The&#32;provided&#32;graph&#32;is&#32;consistent&#32;for&#32;any&#32;OWL&#32;RL&#32;constraint|

***
### Pass Outcome number 41

[Jump to summary definition](#summary-Pass-41)	|	[Previous Pass outcome](#pass-outcome-number-40)	|	[Next Pass outcome](#pass-outcome-number-42)

:white_check_mark:Pass outcome
#### Subject detail
|Name|module-core|
|----|----|
|Title|Standalone&#32;module&#32;src&#92;core.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Module core](https://github.com/HyperAgents/hmas/blob/HEAD/src/core.ttl)|

#### Criterion detail
|Identifier|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|
|----|----|
|Title|Profile&#32;compatibility&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;check&#32;whether&#32;the&#32;test&#32;subject&#32;is&#32;compatible&#32;with&#32;a&#32;profile&#32;or&#32;not,&#32;and&#32;if&#32;it&#32;is&#32;not,&#32;why.|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-41)|Identifier|`owl-rl-profile-error`|
|[Section top](#pass-outcome-number-41)|Title|OWL&#32;RL&#32;Profile&#32;compatible|
|[Section top](#pass-outcome-number-41)|Description|The&#32;subject&#32;is&#32;included&#32;in&#32;the&#32;OWL&#32;RL&#32;sublanguage|

***
### Pass Outcome number 42

[Jump to summary definition](#summary-Pass-42)	|	[Previous Pass outcome](#pass-outcome-number-41)	|	[Next Pass outcome](#pass-outcome-number-43)

:white_check_mark:Pass outcome
#### Subject detail
|Name|module-core|
|----|----|
|Title|Standalone&#32;module&#32;src&#92;core.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Module core](https://github.com/HyperAgents/hmas/blob/HEAD/src/core.ttl)|

#### Criterion detail
|Identifier|[proper-extension-predicate](https://ns.inria.fr/olivaw#proper-extension-predicate)|
|----|----|
|Title|Predicate&#32;extension&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;test&#32;the&#32;proper&#32;use&#32;of&#32;predicates&#32;rdfs:subClassOf&#32;and&#32;rdfs:subPropertyOf&#32;on&#32;the&#32;ontology&#32;terms|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-42)|Identifier|`class-subpropertyof`|
|[Section top](#pass-outcome-number-42)|Title|No&#32;class&#32;subproperty|
|[Section top](#pass-outcome-number-42)|Description|No&#32;ontology&#32;class&#32;is&#32;a&#32;subproperty|

***
### Pass Outcome number 43

[Jump to summary definition](#summary-Pass-43)	|	[Previous Pass outcome](#pass-outcome-number-42)	|	[Next Pass outcome](#pass-outcome-number-44)

:white_check_mark:Pass outcome
#### Subject detail
|Name|module-core|
|----|----|
|Title|Standalone&#32;module&#32;src&#92;core.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Module core](https://github.com/HyperAgents/hmas/blob/HEAD/src/core.ttl)|

#### Criterion detail
|Identifier|[proper-extension-predicate](https://ns.inria.fr/olivaw#proper-extension-predicate)|
|----|----|
|Title|Predicate&#32;extension&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;test&#32;the&#32;proper&#32;use&#32;of&#32;predicates&#32;rdfs:subClassOf&#32;and&#32;rdfs:subPropertyOf&#32;on&#32;the&#32;ontology&#32;terms|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-43)|Identifier|`property-subclassof`|
|[Section top](#pass-outcome-number-43)|Title|No&#32;property&#32;subclass|
|[Section top](#pass-outcome-number-43)|Description|No&#32;ontology&#32;property&#32;is&#32;a&#32;subclass|

***
### Pass Outcome number 44

[Jump to summary definition](#summary-Pass-44)	|	[Previous Pass outcome](#pass-outcome-number-43)	|	[Next Pass outcome](#pass-outcome-number-45)

:white_check_mark:Pass outcome
#### Subject detail
|Name|module-core|
|----|----|
|Title|Standalone&#32;module&#32;src&#92;core.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Module core](https://github.com/HyperAgents/hmas/blob/HEAD/src/core.ttl)|

#### Criterion detail
|Identifier|[proper-extension-predicate](https://ns.inria.fr/olivaw#proper-extension-predicate)|
|----|----|
|Title|Predicate&#32;extension&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;test&#32;the&#32;proper&#32;use&#32;of&#32;predicates&#32;rdfs:subClassOf&#32;and&#32;rdfs:subPropertyOf&#32;on&#32;the&#32;ontology&#32;terms|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-44)|Identifier|`subclassof-property`|
|[Section top](#pass-outcome-number-44)|Title|No&#32;subclass&#32;of&#32;property|
|[Section top](#pass-outcome-number-44)|Description|No&#32;ontology&#32;term&#32;is&#32;a&#32;subclass&#32;of&#32;a&#32;property|

***
### Pass Outcome number 45

[Jump to summary definition](#summary-Pass-45)	|	[Previous Pass outcome](#pass-outcome-number-44)	|	[Next Pass outcome](#pass-outcome-number-46)

:white_check_mark:Pass outcome
#### Subject detail
|Name|module-core|
|----|----|
|Title|Standalone&#32;module&#32;src&#92;core.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Module core](https://github.com/HyperAgents/hmas/blob/HEAD/src/core.ttl)|

#### Criterion detail
|Identifier|[proper-extension-predicate](https://ns.inria.fr/olivaw#proper-extension-predicate)|
|----|----|
|Title|Predicate&#32;extension&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;test&#32;the&#32;proper&#32;use&#32;of&#32;predicates&#32;rdfs:subClassOf&#32;and&#32;rdfs:subPropertyOf&#32;on&#32;the&#32;ontology&#32;terms|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-45)|Identifier|`subpropertyof-class`|
|[Section top](#pass-outcome-number-45)|Title|No&#32;subproperty&#32;of&#32;class|
|[Section top](#pass-outcome-number-45)|Description|No&#32;ontology&#32;term&#32;is&#32;a&#32;subproperty&#32;of&#32;a&#32;class|

***
### Pass Outcome number 46

[Jump to summary definition](#summary-Pass-46)	|	[Previous Pass outcome](#pass-outcome-number-45)	|	[Next Pass outcome](#pass-outcome-number-47)

:white_check_mark:Pass outcome
#### Subject detail
|Name|module-core|
|----|----|
|Title|Standalone&#32;module&#32;src&#92;core.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Module core](https://github.com/HyperAgents/hmas/blob/HEAD/src/core.ttl)|

#### Criterion detail
|Identifier|[term-referencing](https://ns.inria.fr/olivaw#term-referencing)|
|----|----|
|Title|Term&#32;referencing&#32;test|
|Description|A&#32;test&#32;case&#32;from&#32;the&#32;Best&#32;Practices&#32;tests&#32;checking&#32;if&#32;each&#32;term&#32;of&#32;the&#32;test&#32;subject&#32;is&#32;referenced&#32;to&#32;a&#32;module&#32;through&#32;a&#32;rdfs:isDefinedBy&#32;property.|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-46)|Identifier|`no-reference-module`|
|[Section top](#pass-outcome-number-46)|Title|Any&#32;term&#32;is&#32;referenced|
|[Section top](#pass-outcome-number-46)|Description|Each&#32;term&#32;of&#32;the&#32;test&#32;subject&#32;is&#32;linked&#32;to&#32;a&#32;module&#32;by&#32;a&#32;rdfs:isDefinedBy&#32;property|

***
### Pass Outcome number 47

[Jump to summary definition](#summary-Pass-47)	|	[Previous Pass outcome](#pass-outcome-number-46)	|	[Next Pass outcome](#pass-outcome-number-48)

:white_check_mark:Pass outcome
#### Subject detail
|Name|module-core|
|----|----|
|Title|Standalone&#32;module&#32;src&#92;core.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Module core](https://github.com/HyperAgents/hmas/blob/HEAD/src/core.ttl)|

#### Criterion detail
|Identifier|[terms-differenciation](https://ns.inria.fr/olivaw#terms-differenciation)|
|----|----|
|Title|Terms&#32;differenciation&#32;test|
|Description|A&#32;test&#32;case&#32;from&#32;the&#32;Best&#32;Practices&#32;tests&#32;checking&#32;if&#32;all&#32;the&#32;terms&#32;are&#32;different&#32;enough&#32;from&#32;each&#32;other&#32;according&#32;to&#32;the&#32;Levenshtein&#32;distance&#32;metric.|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-47)|Identifier|`too-close-terms`|
|[Section top](#pass-outcome-number-47)|Title|Terms&#32;differenciated&#32;enough|
|[Section top](#pass-outcome-number-47)|Description|All&#32;the&#32;terms&#32;have&#32;have&#32;a&#32;satisfying&#32;Levenshtein&#32;distance&#32;from&#32;each&#32;other&#32;term.|

***
### Pass Outcome number 48

[Jump to summary definition](#summary-Pass-48)	|	[Previous Pass outcome](#pass-outcome-number-47)	|	[Next Pass outcome](#pass-outcome-number-49)

:white_check_mark:Pass outcome
#### Subject detail
|Name|module-alignment-interaction-td|
|----|----|
|Title|Standalone&#32;module&#32;src&#92;alignment&#92;interaction-td.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Module alignment/interaction-td](https://github.com/HyperAgents/hmas/blob/HEAD/src/alignment/interaction-td.ttl)|

#### Criterion detail
|Identifier|[domain-and-range-referencing](https://ns.inria.fr/olivaw#domain-and-range-referencing)|
|----|----|
|Title|Domain&#32;and&#32;range&#32;referencing&#32;test|
|Description|A&#32;test&#32;case&#32;from&#32;the&#32;Best&#32;Practices&#32;tests&#32;checking&#32;if&#32;all&#32;the&#32;ranges&#32;and&#32;domains&#32;from&#32;the&#32;test&#32;subject&#32;point&#32;to&#32;terms&#32;that&#32;are&#32;defined&#32;in&#32;the&#32;vocabulary.|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-48)|Identifier|`domain-out-of-vocabulary`|
|[Section top](#pass-outcome-number-48)|Title|Domains&#32;properly&#32;defined|
|[Section top](#pass-outcome-number-48)|Description|Each&#32;rdfs:domain&#32;is&#32;defined&#32;within&#32;the&#32;fragment|

***
### Pass Outcome number 49

[Jump to summary definition](#summary-Pass-49)	|	[Previous Pass outcome](#pass-outcome-number-48)	|	[Next Pass outcome](#pass-outcome-number-50)

:white_check_mark:Pass outcome
#### Subject detail
|Name|module-alignment-interaction-td|
|----|----|
|Title|Standalone&#32;module&#32;src&#92;alignment&#92;interaction-td.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Module alignment/interaction-td](https://github.com/HyperAgents/hmas/blob/HEAD/src/alignment/interaction-td.ttl)|

#### Criterion detail
|Identifier|[domain-and-range-referencing](https://ns.inria.fr/olivaw#domain-and-range-referencing)|
|----|----|
|Title|Domain&#32;and&#32;range&#32;referencing&#32;test|
|Description|A&#32;test&#32;case&#32;from&#32;the&#32;Best&#32;Practices&#32;tests&#32;checking&#32;if&#32;all&#32;the&#32;ranges&#32;and&#32;domains&#32;from&#32;the&#32;test&#32;subject&#32;point&#32;to&#32;terms&#32;that&#32;are&#32;defined&#32;in&#32;the&#32;vocabulary.|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-49)|Identifier|`range-out-of-vocabulary`|
|[Section top](#pass-outcome-number-49)|Title|Ranges&#32;properly&#32;defined|
|[Section top](#pass-outcome-number-49)|Description|Each&#32;rdfs:range&#32;is&#32;defined&#32;within&#32;the&#32;fragment|

***
### Pass Outcome number 50

[Jump to summary definition](#summary-Pass-50)	|	[Previous Pass outcome](#pass-outcome-number-49)	|	[Next Pass outcome](#pass-outcome-number-51)

:white_check_mark:Pass outcome
#### Subject detail
|Name|module-alignment-interaction-td|
|----|----|
|Title|Standalone&#32;module&#32;src&#92;alignment&#92;interaction-td.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Module alignment/interaction-td](https://github.com/HyperAgents/hmas/blob/HEAD/src/alignment/interaction-td.ttl)|

#### Criterion detail
|Identifier|[labeled-terms](https://ns.inria.fr/olivaw#labeled-terms)|
|----|----|
|Title|Term&#32;labeling&#32;test|
|Description|A&#32;test&#32;case&#32;from&#32;the&#32;Best&#32;Practices&#32;tests&#32;checking&#32;if&#32;all&#32;the&#32;terms&#32;of&#32;the&#32;subject&#32;have&#32;a&#32;rdfs:label&#32;property&#32;pointing&#32;to&#32;a&#32;literal&#32;in&#32;English|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-50)|Identifier|`not-labeled-term`|
|[Section top](#pass-outcome-number-50)|Title|All&#32;terms&#32;labeled|
|[Section top](#pass-outcome-number-50)|Description|All&#32;the&#32;terms&#32;defined&#32;in&#32;the&#32;subject&#32;have&#32;a&#32;rdfs:label&#32;in&#32;English|

***
### Pass Outcome number 51

[Jump to summary definition](#summary-Pass-51)	|	[Previous Pass outcome](#pass-outcome-number-50)	|	[Next Pass outcome](#pass-outcome-number-52)

:white_check_mark:Pass outcome
#### Subject detail
|Name|module-alignment-interaction-td|
|----|----|
|Title|Standalone&#32;module&#32;src&#92;alignment&#92;interaction-td.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Module alignment/interaction-td](https://github.com/HyperAgents/hmas/blob/HEAD/src/alignment/interaction-td.ttl)|

#### Criterion detail
|Identifier|[owl-rl-constraint](https://ns.inria.fr/olivaw#owl-rl-constraint)|
|----|----|
|Title|OWL&#32;RL&#32;Constraint&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;check&#32;wether&#32;the&#32;test&#32;subject&#32;is&#32;syntaxically&#32;correct&#32;or&#32;not.|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-51)|Identifier|`owl-rl-constraint-violation`|
|[Section top](#pass-outcome-number-51)|Title|OWL&#32;RL&#32;consistent|
|[Section top](#pass-outcome-number-51)|Description|The&#32;provided&#32;graph&#32;is&#32;consistent&#32;for&#32;any&#32;OWL&#32;RL&#32;constraint|

***
### Pass Outcome number 52

[Jump to summary definition](#summary-Pass-52)	|	[Previous Pass outcome](#pass-outcome-number-51)	|	[Next Pass outcome](#pass-outcome-number-53)

:white_check_mark:Pass outcome
#### Subject detail
|Name|module-alignment-interaction-td|
|----|----|
|Title|Standalone&#32;module&#32;src&#92;alignment&#92;interaction-td.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Module alignment/interaction-td](https://github.com/HyperAgents/hmas/blob/HEAD/src/alignment/interaction-td.ttl)|

#### Criterion detail
|Identifier|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|
|----|----|
|Title|Profile&#32;compatibility&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;check&#32;whether&#32;the&#32;test&#32;subject&#32;is&#32;compatible&#32;with&#32;a&#32;profile&#32;or&#32;not,&#32;and&#32;if&#32;it&#32;is&#32;not,&#32;why.|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-52)|Identifier|`owl-el-profile-error`|
|[Section top](#pass-outcome-number-52)|Title|OWL&#32;EL&#32;Profile&#32;compatible|
|[Section top](#pass-outcome-number-52)|Description|Statement&#32;not&#32;supported  &#10;Statement&#32;not&#32;supported&#32;in&#32;a&#32;Super&#32;Class&#32;Expression|

***
### Pass Outcome number 53

[Jump to summary definition](#summary-Pass-53)	|	[Previous Pass outcome](#pass-outcome-number-52)	|	[Next Pass outcome](#pass-outcome-number-54)

:white_check_mark:Pass outcome
#### Subject detail
|Name|module-alignment-interaction-td|
|----|----|
|Title|Standalone&#32;module&#32;src&#92;alignment&#92;interaction-td.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Module alignment/interaction-td](https://github.com/HyperAgents/hmas/blob/HEAD/src/alignment/interaction-td.ttl)|

#### Criterion detail
|Identifier|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|
|----|----|
|Title|Profile&#32;compatibility&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;check&#32;whether&#32;the&#32;test&#32;subject&#32;is&#32;compatible&#32;with&#32;a&#32;profile&#32;or&#32;not,&#32;and&#32;if&#32;it&#32;is&#32;not,&#32;why.|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-53)|Identifier|`owl-rl-profile-error`|
|[Section top](#pass-outcome-number-53)|Title|OWL&#32;RL&#32;Profile&#32;compatible|
|[Section top](#pass-outcome-number-53)|Description|The&#32;subject&#32;is&#32;included&#32;in&#32;the&#32;OWL&#32;RL&#32;sublanguage|

***
### Pass Outcome number 54

[Jump to summary definition](#summary-Pass-54)	|	[Previous Pass outcome](#pass-outcome-number-53)	|	[Next Pass outcome](#pass-outcome-number-55)

:white_check_mark:Pass outcome
#### Subject detail
|Name|module-alignment-interaction-td|
|----|----|
|Title|Standalone&#32;module&#32;src&#92;alignment&#92;interaction-td.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Module alignment/interaction-td](https://github.com/HyperAgents/hmas/blob/HEAD/src/alignment/interaction-td.ttl)|

#### Criterion detail
|Identifier|[proper-extension-predicate](https://ns.inria.fr/olivaw#proper-extension-predicate)|
|----|----|
|Title|Predicate&#32;extension&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;test&#32;the&#32;proper&#32;use&#32;of&#32;predicates&#32;rdfs:subClassOf&#32;and&#32;rdfs:subPropertyOf&#32;on&#32;the&#32;ontology&#32;terms|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-54)|Identifier|`class-subpropertyof`|
|[Section top](#pass-outcome-number-54)|Title|No&#32;class&#32;subproperty|
|[Section top](#pass-outcome-number-54)|Description|No&#32;ontology&#32;class&#32;is&#32;a&#32;subproperty|

***
### Pass Outcome number 55

[Jump to summary definition](#summary-Pass-55)	|	[Previous Pass outcome](#pass-outcome-number-54)	|	[Next Pass outcome](#pass-outcome-number-56)

:white_check_mark:Pass outcome
#### Subject detail
|Name|module-alignment-interaction-td|
|----|----|
|Title|Standalone&#32;module&#32;src&#92;alignment&#92;interaction-td.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Module alignment/interaction-td](https://github.com/HyperAgents/hmas/blob/HEAD/src/alignment/interaction-td.ttl)|

#### Criterion detail
|Identifier|[proper-extension-predicate](https://ns.inria.fr/olivaw#proper-extension-predicate)|
|----|----|
|Title|Predicate&#32;extension&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;test&#32;the&#32;proper&#32;use&#32;of&#32;predicates&#32;rdfs:subClassOf&#32;and&#32;rdfs:subPropertyOf&#32;on&#32;the&#32;ontology&#32;terms|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-55)|Identifier|`property-subclassof`|
|[Section top](#pass-outcome-number-55)|Title|No&#32;property&#32;subclass|
|[Section top](#pass-outcome-number-55)|Description|No&#32;ontology&#32;property&#32;is&#32;a&#32;subclass|

***
### Pass Outcome number 56

[Jump to summary definition](#summary-Pass-56)	|	[Previous Pass outcome](#pass-outcome-number-55)	|	[Next Pass outcome](#pass-outcome-number-57)

:white_check_mark:Pass outcome
#### Subject detail
|Name|module-alignment-interaction-td|
|----|----|
|Title|Standalone&#32;module&#32;src&#92;alignment&#92;interaction-td.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Module alignment/interaction-td](https://github.com/HyperAgents/hmas/blob/HEAD/src/alignment/interaction-td.ttl)|

#### Criterion detail
|Identifier|[proper-extension-predicate](https://ns.inria.fr/olivaw#proper-extension-predicate)|
|----|----|
|Title|Predicate&#32;extension&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;test&#32;the&#32;proper&#32;use&#32;of&#32;predicates&#32;rdfs:subClassOf&#32;and&#32;rdfs:subPropertyOf&#32;on&#32;the&#32;ontology&#32;terms|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-56)|Identifier|`subclassof-property`|
|[Section top](#pass-outcome-number-56)|Title|No&#32;subclass&#32;of&#32;property|
|[Section top](#pass-outcome-number-56)|Description|No&#32;ontology&#32;term&#32;is&#32;a&#32;subclass&#32;of&#32;a&#32;property|

***
### Pass Outcome number 57

[Jump to summary definition](#summary-Pass-57)	|	[Previous Pass outcome](#pass-outcome-number-56)	|	[Next Pass outcome](#pass-outcome-number-58)

:white_check_mark:Pass outcome
#### Subject detail
|Name|module-alignment-interaction-td|
|----|----|
|Title|Standalone&#32;module&#32;src&#92;alignment&#92;interaction-td.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Module alignment/interaction-td](https://github.com/HyperAgents/hmas/blob/HEAD/src/alignment/interaction-td.ttl)|

#### Criterion detail
|Identifier|[proper-extension-predicate](https://ns.inria.fr/olivaw#proper-extension-predicate)|
|----|----|
|Title|Predicate&#32;extension&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;test&#32;the&#32;proper&#32;use&#32;of&#32;predicates&#32;rdfs:subClassOf&#32;and&#32;rdfs:subPropertyOf&#32;on&#32;the&#32;ontology&#32;terms|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-57)|Identifier|`subpropertyof-class`|
|[Section top](#pass-outcome-number-57)|Title|No&#32;subproperty&#32;of&#32;class|
|[Section top](#pass-outcome-number-57)|Description|No&#32;ontology&#32;term&#32;is&#32;a&#32;subproperty&#32;of&#32;a&#32;class|

***
### Pass Outcome number 58

[Jump to summary definition](#summary-Pass-58)	|	[Previous Pass outcome](#pass-outcome-number-57)	|	[Next Pass outcome](#pass-outcome-number-59)

:white_check_mark:Pass outcome
#### Subject detail
|Name|module-alignment-interaction-td|
|----|----|
|Title|Standalone&#32;module&#32;src&#92;alignment&#92;interaction-td.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Module alignment/interaction-td](https://github.com/HyperAgents/hmas/blob/HEAD/src/alignment/interaction-td.ttl)|

#### Criterion detail
|Identifier|[term-referencing](https://ns.inria.fr/olivaw#term-referencing)|
|----|----|
|Title|Term&#32;referencing&#32;test|
|Description|A&#32;test&#32;case&#32;from&#32;the&#32;Best&#32;Practices&#32;tests&#32;checking&#32;if&#32;each&#32;term&#32;of&#32;the&#32;test&#32;subject&#32;is&#32;referenced&#32;to&#32;a&#32;module&#32;through&#32;a&#32;rdfs:isDefinedBy&#32;property.|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-58)|Identifier|`no-reference-module`|
|[Section top](#pass-outcome-number-58)|Title|Any&#32;term&#32;is&#32;referenced|
|[Section top](#pass-outcome-number-58)|Description|Each&#32;term&#32;of&#32;the&#32;test&#32;subject&#32;is&#32;linked&#32;to&#32;a&#32;module&#32;by&#32;a&#32;rdfs:isDefinedBy&#32;property|

***
### Pass Outcome number 59

[Jump to summary definition](#summary-Pass-59)	|	[Previous Pass outcome](#pass-outcome-number-58)	|	[Next Pass outcome](#pass-outcome-number-60)

:white_check_mark:Pass outcome
#### Subject detail
|Name|module-alignment-interaction-td|
|----|----|
|Title|Standalone&#32;module&#32;src&#92;alignment&#92;interaction-td.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Module alignment/interaction-td](https://github.com/HyperAgents/hmas/blob/HEAD/src/alignment/interaction-td.ttl)|

#### Criterion detail
|Identifier|[terms-differenciation](https://ns.inria.fr/olivaw#terms-differenciation)|
|----|----|
|Title|Terms&#32;differenciation&#32;test|
|Description|A&#32;test&#32;case&#32;from&#32;the&#32;Best&#32;Practices&#32;tests&#32;checking&#32;if&#32;all&#32;the&#32;terms&#32;are&#32;different&#32;enough&#32;from&#32;each&#32;other&#32;according&#32;to&#32;the&#32;Levenshtein&#32;distance&#32;metric.|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-59)|Identifier|`too-close-terms`|
|[Section top](#pass-outcome-number-59)|Title|Terms&#32;differenciated&#32;enough|
|[Section top](#pass-outcome-number-59)|Description|All&#32;the&#32;terms&#32;have&#32;have&#32;a&#32;satisfying&#32;Levenshtein&#32;distance&#32;from&#32;each&#32;other&#32;term.|

***
### Pass Outcome number 60

[Jump to summary definition](#summary-Pass-60)	|	[Previous Pass outcome](#pass-outcome-number-59)	|	[Next Pass outcome](#pass-outcome-number-61)

:white_check_mark:Pass outcome
#### Subject detail
|Name|modelet-manufacturing-environments-discover-signifiers|
|----|----|
|Title|Standalone&#32;modelet&#32;domains&#92;manufacturing-environments&#92;discover-signifiers&#92;onto.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Modelet manufacturing-environments/discover-signifiers](https://github.com/HyperAgents/hmas/blob/HEAD/domains/manufacturing-environments/discover-signifiers/onto.ttl)|

#### Criterion detail
|Identifier|[domain-and-range-referencing](https://ns.inria.fr/olivaw#domain-and-range-referencing)|
|----|----|
|Title|Domain&#32;and&#32;range&#32;referencing&#32;test|
|Description|A&#32;test&#32;case&#32;from&#32;the&#32;Best&#32;Practices&#32;tests&#32;checking&#32;if&#32;all&#32;the&#32;ranges&#32;and&#32;domains&#32;from&#32;the&#32;test&#32;subject&#32;point&#32;to&#32;terms&#32;that&#32;are&#32;defined&#32;in&#32;the&#32;vocabulary.|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-60)|Identifier|`domain-out-of-vocabulary`|
|[Section top](#pass-outcome-number-60)|Title|Domains&#32;properly&#32;defined|
|[Section top](#pass-outcome-number-60)|Description|Each&#32;rdfs:domain&#32;is&#32;defined&#32;within&#32;the&#32;fragment|

***
### Pass Outcome number 61

[Jump to summary definition](#summary-Pass-61)	|	[Previous Pass outcome](#pass-outcome-number-60)	|	[Next Pass outcome](#pass-outcome-number-62)

:white_check_mark:Pass outcome
#### Subject detail
|Name|modelet-manufacturing-environments-discover-signifiers|
|----|----|
|Title|Standalone&#32;modelet&#32;domains&#92;manufacturing-environments&#92;discover-signifiers&#92;onto.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Modelet manufacturing-environments/discover-signifiers](https://github.com/HyperAgents/hmas/blob/HEAD/domains/manufacturing-environments/discover-signifiers/onto.ttl)|

#### Criterion detail
|Identifier|[domain-and-range-referencing](https://ns.inria.fr/olivaw#domain-and-range-referencing)|
|----|----|
|Title|Domain&#32;and&#32;range&#32;referencing&#32;test|
|Description|A&#32;test&#32;case&#32;from&#32;the&#32;Best&#32;Practices&#32;tests&#32;checking&#32;if&#32;all&#32;the&#32;ranges&#32;and&#32;domains&#32;from&#32;the&#32;test&#32;subject&#32;point&#32;to&#32;terms&#32;that&#32;are&#32;defined&#32;in&#32;the&#32;vocabulary.|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-61)|Identifier|`range-out-of-vocabulary`|
|[Section top](#pass-outcome-number-61)|Title|Ranges&#32;properly&#32;defined|
|[Section top](#pass-outcome-number-61)|Description|Each&#32;rdfs:range&#32;is&#32;defined&#32;within&#32;the&#32;fragment|

***
### Pass Outcome number 62

[Jump to summary definition](#summary-Pass-62)	|	[Previous Pass outcome](#pass-outcome-number-61)	|	[Next Pass outcome](#pass-outcome-number-63)

:white_check_mark:Pass outcome
#### Subject detail
|Name|modelet-manufacturing-environments-discover-signifiers|
|----|----|
|Title|Standalone&#32;modelet&#32;domains&#92;manufacturing-environments&#92;discover-signifiers&#92;onto.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Modelet manufacturing-environments/discover-signifiers](https://github.com/HyperAgents/hmas/blob/HEAD/domains/manufacturing-environments/discover-signifiers/onto.ttl)|

#### Criterion detail
|Identifier|[owl-rl-constraint](https://ns.inria.fr/olivaw#owl-rl-constraint)|
|----|----|
|Title|OWL&#32;RL&#32;Constraint&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;check&#32;wether&#32;the&#32;test&#32;subject&#32;is&#32;syntaxically&#32;correct&#32;or&#32;not.|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-62)|Identifier|`owl-rl-constraint-violation`|
|[Section top](#pass-outcome-number-62)|Title|OWL&#32;RL&#32;consistent|
|[Section top](#pass-outcome-number-62)|Description|The&#32;provided&#32;graph&#32;is&#32;consistent&#32;for&#32;any&#32;OWL&#32;RL&#32;constraint|

***
### Pass Outcome number 63

[Jump to summary definition](#summary-Pass-63)	|	[Previous Pass outcome](#pass-outcome-number-62)	|	[Next Pass outcome](#pass-outcome-number-64)

:white_check_mark:Pass outcome
#### Subject detail
|Name|modelet-manufacturing-environments-discover-signifiers|
|----|----|
|Title|Standalone&#32;modelet&#32;domains&#92;manufacturing-environments&#92;discover-signifiers&#92;onto.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Modelet manufacturing-environments/discover-signifiers](https://github.com/HyperAgents/hmas/blob/HEAD/domains/manufacturing-environments/discover-signifiers/onto.ttl)|

#### Criterion detail
|Identifier|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|
|----|----|
|Title|Profile&#32;compatibility&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;check&#32;whether&#32;the&#32;test&#32;subject&#32;is&#32;compatible&#32;with&#32;a&#32;profile&#32;or&#32;not,&#32;and&#32;if&#32;it&#32;is&#32;not,&#32;why.|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-63)|Identifier|`owl-rl-profile-error`|
|[Section top](#pass-outcome-number-63)|Title|OWL&#32;RL&#32;Profile&#32;compatible|
|[Section top](#pass-outcome-number-63)|Description|The&#32;subject&#32;is&#32;included&#32;in&#32;the&#32;OWL&#32;RL&#32;sublanguage|

***
### Pass Outcome number 64

[Jump to summary definition](#summary-Pass-64)	|	[Previous Pass outcome](#pass-outcome-number-63)	|	[Next Pass outcome](#pass-outcome-number-65)

:white_check_mark:Pass outcome
#### Subject detail
|Name|modelet-manufacturing-environments-discover-signifiers|
|----|----|
|Title|Standalone&#32;modelet&#32;domains&#92;manufacturing-environments&#92;discover-signifiers&#92;onto.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Modelet manufacturing-environments/discover-signifiers](https://github.com/HyperAgents/hmas/blob/HEAD/domains/manufacturing-environments/discover-signifiers/onto.ttl)|

#### Criterion detail
|Identifier|[proper-extension-predicate](https://ns.inria.fr/olivaw#proper-extension-predicate)|
|----|----|
|Title|Predicate&#32;extension&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;test&#32;the&#32;proper&#32;use&#32;of&#32;predicates&#32;rdfs:subClassOf&#32;and&#32;rdfs:subPropertyOf&#32;on&#32;the&#32;ontology&#32;terms|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-64)|Identifier|`class-subpropertyof`|
|[Section top](#pass-outcome-number-64)|Title|No&#32;class&#32;subproperty|
|[Section top](#pass-outcome-number-64)|Description|No&#32;ontology&#32;class&#32;is&#32;a&#32;subproperty|

***
### Pass Outcome number 65

[Jump to summary definition](#summary-Pass-65)	|	[Previous Pass outcome](#pass-outcome-number-64)	|	[Next Pass outcome](#pass-outcome-number-66)

:white_check_mark:Pass outcome
#### Subject detail
|Name|modelet-manufacturing-environments-discover-signifiers|
|----|----|
|Title|Standalone&#32;modelet&#32;domains&#92;manufacturing-environments&#92;discover-signifiers&#92;onto.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Modelet manufacturing-environments/discover-signifiers](https://github.com/HyperAgents/hmas/blob/HEAD/domains/manufacturing-environments/discover-signifiers/onto.ttl)|

#### Criterion detail
|Identifier|[proper-extension-predicate](https://ns.inria.fr/olivaw#proper-extension-predicate)|
|----|----|
|Title|Predicate&#32;extension&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;test&#32;the&#32;proper&#32;use&#32;of&#32;predicates&#32;rdfs:subClassOf&#32;and&#32;rdfs:subPropertyOf&#32;on&#32;the&#32;ontology&#32;terms|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-65)|Identifier|`property-subclassof`|
|[Section top](#pass-outcome-number-65)|Title|No&#32;property&#32;subclass|
|[Section top](#pass-outcome-number-65)|Description|No&#32;ontology&#32;property&#32;is&#32;a&#32;subclass|

***
### Pass Outcome number 66

[Jump to summary definition](#summary-Pass-66)	|	[Previous Pass outcome](#pass-outcome-number-65)	|	[Next Pass outcome](#pass-outcome-number-67)

:white_check_mark:Pass outcome
#### Subject detail
|Name|modelet-manufacturing-environments-discover-signifiers|
|----|----|
|Title|Standalone&#32;modelet&#32;domains&#92;manufacturing-environments&#92;discover-signifiers&#92;onto.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Modelet manufacturing-environments/discover-signifiers](https://github.com/HyperAgents/hmas/blob/HEAD/domains/manufacturing-environments/discover-signifiers/onto.ttl)|

#### Criterion detail
|Identifier|[proper-extension-predicate](https://ns.inria.fr/olivaw#proper-extension-predicate)|
|----|----|
|Title|Predicate&#32;extension&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;test&#32;the&#32;proper&#32;use&#32;of&#32;predicates&#32;rdfs:subClassOf&#32;and&#32;rdfs:subPropertyOf&#32;on&#32;the&#32;ontology&#32;terms|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-66)|Identifier|`subclassof-property`|
|[Section top](#pass-outcome-number-66)|Title|No&#32;subclass&#32;of&#32;property|
|[Section top](#pass-outcome-number-66)|Description|No&#32;ontology&#32;term&#32;is&#32;a&#32;subclass&#32;of&#32;a&#32;property|

***
### Pass Outcome number 67

[Jump to summary definition](#summary-Pass-67)	|	[Previous Pass outcome](#pass-outcome-number-66)	|	[Next Pass outcome](#pass-outcome-number-68)

:white_check_mark:Pass outcome
#### Subject detail
|Name|modelet-manufacturing-environments-discover-signifiers|
|----|----|
|Title|Standalone&#32;modelet&#32;domains&#92;manufacturing-environments&#92;discover-signifiers&#92;onto.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Modelet manufacturing-environments/discover-signifiers](https://github.com/HyperAgents/hmas/blob/HEAD/domains/manufacturing-environments/discover-signifiers/onto.ttl)|

#### Criterion detail
|Identifier|[proper-extension-predicate](https://ns.inria.fr/olivaw#proper-extension-predicate)|
|----|----|
|Title|Predicate&#32;extension&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;test&#32;the&#32;proper&#32;use&#32;of&#32;predicates&#32;rdfs:subClassOf&#32;and&#32;rdfs:subPropertyOf&#32;on&#32;the&#32;ontology&#32;terms|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-67)|Identifier|`subpropertyof-class`|
|[Section top](#pass-outcome-number-67)|Title|No&#32;subproperty&#32;of&#32;class|
|[Section top](#pass-outcome-number-67)|Description|No&#32;ontology&#32;term&#32;is&#32;a&#32;subproperty&#32;of&#32;a&#32;class|

***
### Pass Outcome number 68

[Jump to summary definition](#summary-Pass-68)	|	[Previous Pass outcome](#pass-outcome-number-67)	|	[Next Pass outcome](#pass-outcome-number-69)

:white_check_mark:Pass outcome
#### Subject detail
|Name|modelet-manufacturing-environments-discover-signifiers|
|----|----|
|Title|Standalone&#32;modelet&#32;domains&#92;manufacturing-environments&#92;discover-signifiers&#92;onto.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Modelet manufacturing-environments/discover-signifiers](https://github.com/HyperAgents/hmas/blob/HEAD/domains/manufacturing-environments/discover-signifiers/onto.ttl)|

#### Criterion detail
|Identifier|[term-referencing](https://ns.inria.fr/olivaw#term-referencing)|
|----|----|
|Title|Term&#32;referencing&#32;test|
|Description|A&#32;test&#32;case&#32;from&#32;the&#32;Best&#32;Practices&#32;tests&#32;checking&#32;if&#32;each&#32;term&#32;of&#32;the&#32;test&#32;subject&#32;is&#32;referenced&#32;to&#32;a&#32;module&#32;through&#32;a&#32;rdfs:isDefinedBy&#32;property.|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-68)|Identifier|`no-reference-module`|
|[Section top](#pass-outcome-number-68)|Title|Any&#32;term&#32;is&#32;referenced|
|[Section top](#pass-outcome-number-68)|Description|Each&#32;term&#32;of&#32;the&#32;test&#32;subject&#32;is&#32;linked&#32;to&#32;a&#32;module&#32;by&#32;a&#32;rdfs:isDefinedBy&#32;property|

***
### Pass Outcome number 69

[Jump to summary definition](#summary-Pass-69)	|	[Previous Pass outcome](#pass-outcome-number-68)	|	[Next Pass outcome](#pass-outcome-number-70)

:white_check_mark:Pass outcome
#### Subject detail
|Name|modelet-manufacturing-environments-discover-signifiers|
|----|----|
|Title|Standalone&#32;modelet&#32;domains&#92;manufacturing-environments&#92;discover-signifiers&#92;onto.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Modelet manufacturing-environments/discover-signifiers](https://github.com/HyperAgents/hmas/blob/HEAD/domains/manufacturing-environments/discover-signifiers/onto.ttl)|

#### Criterion detail
|Identifier|[terms-differenciation](https://ns.inria.fr/olivaw#terms-differenciation)|
|----|----|
|Title|Terms&#32;differenciation&#32;test|
|Description|A&#32;test&#32;case&#32;from&#32;the&#32;Best&#32;Practices&#32;tests&#32;checking&#32;if&#32;all&#32;the&#32;terms&#32;are&#32;different&#32;enough&#32;from&#32;each&#32;other&#32;according&#32;to&#32;the&#32;Levenshtein&#32;distance&#32;metric.|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-69)|Identifier|`too-close-terms`|
|[Section top](#pass-outcome-number-69)|Title|Terms&#32;differenciated&#32;enough|
|[Section top](#pass-outcome-number-69)|Description|All&#32;the&#32;terms&#32;have&#32;have&#32;a&#32;satisfying&#32;Levenshtein&#32;distance&#32;from&#32;each&#32;other&#32;term.|

***
### Pass Outcome number 70

[Jump to summary definition](#summary-Pass-70)	|	[Previous Pass outcome](#pass-outcome-number-69)	|	[Next Pass outcome](#pass-outcome-number-71)

:white_check_mark:Pass outcome
#### Subject detail
|Name|modelet-manufacturing-environments-discover-platforms|
|----|----|
|Title|Standalone&#32;modelet&#32;domains&#92;manufacturing-environments&#92;discover-platforms&#92;onto.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Modelet manufacturing-environments/discover-platforms](https://github.com/HyperAgents/hmas/blob/HEAD/domains/manufacturing-environments/discover-platforms/onto.ttl)|

#### Criterion detail
|Identifier|[domain-and-range-referencing](https://ns.inria.fr/olivaw#domain-and-range-referencing)|
|----|----|
|Title|Domain&#32;and&#32;range&#32;referencing&#32;test|
|Description|A&#32;test&#32;case&#32;from&#32;the&#32;Best&#32;Practices&#32;tests&#32;checking&#32;if&#32;all&#32;the&#32;ranges&#32;and&#32;domains&#32;from&#32;the&#32;test&#32;subject&#32;point&#32;to&#32;terms&#32;that&#32;are&#32;defined&#32;in&#32;the&#32;vocabulary.|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-70)|Identifier|`domain-out-of-vocabulary`|
|[Section top](#pass-outcome-number-70)|Title|Domains&#32;properly&#32;defined|
|[Section top](#pass-outcome-number-70)|Description|Each&#32;rdfs:domain&#32;is&#32;defined&#32;within&#32;the&#32;fragment|

***
### Pass Outcome number 71

[Jump to summary definition](#summary-Pass-71)	|	[Previous Pass outcome](#pass-outcome-number-70)	|	[Next Pass outcome](#pass-outcome-number-72)

:white_check_mark:Pass outcome
#### Subject detail
|Name|modelet-manufacturing-environments-discover-platforms|
|----|----|
|Title|Standalone&#32;modelet&#32;domains&#92;manufacturing-environments&#92;discover-platforms&#92;onto.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Modelet manufacturing-environments/discover-platforms](https://github.com/HyperAgents/hmas/blob/HEAD/domains/manufacturing-environments/discover-platforms/onto.ttl)|

#### Criterion detail
|Identifier|[domain-and-range-referencing](https://ns.inria.fr/olivaw#domain-and-range-referencing)|
|----|----|
|Title|Domain&#32;and&#32;range&#32;referencing&#32;test|
|Description|A&#32;test&#32;case&#32;from&#32;the&#32;Best&#32;Practices&#32;tests&#32;checking&#32;if&#32;all&#32;the&#32;ranges&#32;and&#32;domains&#32;from&#32;the&#32;test&#32;subject&#32;point&#32;to&#32;terms&#32;that&#32;are&#32;defined&#32;in&#32;the&#32;vocabulary.|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-71)|Identifier|`range-out-of-vocabulary`|
|[Section top](#pass-outcome-number-71)|Title|Ranges&#32;properly&#32;defined|
|[Section top](#pass-outcome-number-71)|Description|Each&#32;rdfs:range&#32;is&#32;defined&#32;within&#32;the&#32;fragment|

***
### Pass Outcome number 72

[Jump to summary definition](#summary-Pass-72)	|	[Previous Pass outcome](#pass-outcome-number-71)	|	[Next Pass outcome](#pass-outcome-number-73)

:white_check_mark:Pass outcome
#### Subject detail
|Name|modelet-manufacturing-environments-discover-platforms|
|----|----|
|Title|Standalone&#32;modelet&#32;domains&#92;manufacturing-environments&#92;discover-platforms&#92;onto.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Modelet manufacturing-environments/discover-platforms](https://github.com/HyperAgents/hmas/blob/HEAD/domains/manufacturing-environments/discover-platforms/onto.ttl)|

#### Criterion detail
|Identifier|[labeled-terms](https://ns.inria.fr/olivaw#labeled-terms)|
|----|----|
|Title|Term&#32;labeling&#32;test|
|Description|A&#32;test&#32;case&#32;from&#32;the&#32;Best&#32;Practices&#32;tests&#32;checking&#32;if&#32;all&#32;the&#32;terms&#32;of&#32;the&#32;subject&#32;have&#32;a&#32;rdfs:label&#32;property&#32;pointing&#32;to&#32;a&#32;literal&#32;in&#32;English|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-72)|Identifier|`not-labeled-term`|
|[Section top](#pass-outcome-number-72)|Title|All&#32;terms&#32;labeled|
|[Section top](#pass-outcome-number-72)|Description|All&#32;the&#32;terms&#32;defined&#32;in&#32;the&#32;subject&#32;have&#32;a&#32;rdfs:label&#32;in&#32;English|

***
### Pass Outcome number 73

[Jump to summary definition](#summary-Pass-73)	|	[Previous Pass outcome](#pass-outcome-number-72)	|	[Next Pass outcome](#pass-outcome-number-74)

:white_check_mark:Pass outcome
#### Subject detail
|Name|modelet-manufacturing-environments-discover-platforms|
|----|----|
|Title|Standalone&#32;modelet&#32;domains&#92;manufacturing-environments&#92;discover-platforms&#92;onto.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Modelet manufacturing-environments/discover-platforms](https://github.com/HyperAgents/hmas/blob/HEAD/domains/manufacturing-environments/discover-platforms/onto.ttl)|

#### Criterion detail
|Identifier|[owl-rl-constraint](https://ns.inria.fr/olivaw#owl-rl-constraint)|
|----|----|
|Title|OWL&#32;RL&#32;Constraint&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;check&#32;wether&#32;the&#32;test&#32;subject&#32;is&#32;syntaxically&#32;correct&#32;or&#32;not.|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-73)|Identifier|`owl-rl-constraint-violation`|
|[Section top](#pass-outcome-number-73)|Title|OWL&#32;RL&#32;consistent|
|[Section top](#pass-outcome-number-73)|Description|The&#32;provided&#32;graph&#32;is&#32;consistent&#32;for&#32;any&#32;OWL&#32;RL&#32;constraint|

***
### Pass Outcome number 74

[Jump to summary definition](#summary-Pass-74)	|	[Previous Pass outcome](#pass-outcome-number-73)	|	[Next Pass outcome](#pass-outcome-number-75)

:white_check_mark:Pass outcome
#### Subject detail
|Name|modelet-manufacturing-environments-discover-platforms|
|----|----|
|Title|Standalone&#32;modelet&#32;domains&#92;manufacturing-environments&#92;discover-platforms&#92;onto.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Modelet manufacturing-environments/discover-platforms](https://github.com/HyperAgents/hmas/blob/HEAD/domains/manufacturing-environments/discover-platforms/onto.ttl)|

#### Criterion detail
|Identifier|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|
|----|----|
|Title|Profile&#32;compatibility&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;check&#32;whether&#32;the&#32;test&#32;subject&#32;is&#32;compatible&#32;with&#32;a&#32;profile&#32;or&#32;not,&#32;and&#32;if&#32;it&#32;is&#32;not,&#32;why.|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-74)|Identifier|`owl-ql-profile-error`|
|[Section top](#pass-outcome-number-74)|Title|OWL&#32;QL&#32;Profile&#32;compatible|
|[Section top](#pass-outcome-number-74)|Description|The&#32;subject&#32;is&#32;included&#32;in&#32;the&#32;OWL&#32;QL&#32;sublanguage|

***
### Pass Outcome number 75

[Jump to summary definition](#summary-Pass-75)	|	[Previous Pass outcome](#pass-outcome-number-74)	|	[Next Pass outcome](#pass-outcome-number-76)

:white_check_mark:Pass outcome
#### Subject detail
|Name|modelet-manufacturing-environments-discover-platforms|
|----|----|
|Title|Standalone&#32;modelet&#32;domains&#92;manufacturing-environments&#92;discover-platforms&#92;onto.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Modelet manufacturing-environments/discover-platforms](https://github.com/HyperAgents/hmas/blob/HEAD/domains/manufacturing-environments/discover-platforms/onto.ttl)|

#### Criterion detail
|Identifier|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|
|----|----|
|Title|Profile&#32;compatibility&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;check&#32;whether&#32;the&#32;test&#32;subject&#32;is&#32;compatible&#32;with&#32;a&#32;profile&#32;or&#32;not,&#32;and&#32;if&#32;it&#32;is&#32;not,&#32;why.|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-75)|Identifier|`owl-rl-profile-error`|
|[Section top](#pass-outcome-number-75)|Title|OWL&#32;RL&#32;Profile&#32;compatible|
|[Section top](#pass-outcome-number-75)|Description|The&#32;subject&#32;is&#32;included&#32;in&#32;the&#32;OWL&#32;RL&#32;sublanguage|

***
### Pass Outcome number 76

[Jump to summary definition](#summary-Pass-76)	|	[Previous Pass outcome](#pass-outcome-number-75)	|	[Next Pass outcome](#pass-outcome-number-77)

:white_check_mark:Pass outcome
#### Subject detail
|Name|modelet-manufacturing-environments-discover-platforms|
|----|----|
|Title|Standalone&#32;modelet&#32;domains&#92;manufacturing-environments&#92;discover-platforms&#92;onto.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Modelet manufacturing-environments/discover-platforms](https://github.com/HyperAgents/hmas/blob/HEAD/domains/manufacturing-environments/discover-platforms/onto.ttl)|

#### Criterion detail
|Identifier|[proper-extension-predicate](https://ns.inria.fr/olivaw#proper-extension-predicate)|
|----|----|
|Title|Predicate&#32;extension&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;test&#32;the&#32;proper&#32;use&#32;of&#32;predicates&#32;rdfs:subClassOf&#32;and&#32;rdfs:subPropertyOf&#32;on&#32;the&#32;ontology&#32;terms|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-76)|Identifier|`class-subpropertyof`|
|[Section top](#pass-outcome-number-76)|Title|No&#32;class&#32;subproperty|
|[Section top](#pass-outcome-number-76)|Description|No&#32;ontology&#32;class&#32;is&#32;a&#32;subproperty|

***
### Pass Outcome number 77

[Jump to summary definition](#summary-Pass-77)	|	[Previous Pass outcome](#pass-outcome-number-76)	|	[Next Pass outcome](#pass-outcome-number-78)

:white_check_mark:Pass outcome
#### Subject detail
|Name|modelet-manufacturing-environments-discover-platforms|
|----|----|
|Title|Standalone&#32;modelet&#32;domains&#92;manufacturing-environments&#92;discover-platforms&#92;onto.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Modelet manufacturing-environments/discover-platforms](https://github.com/HyperAgents/hmas/blob/HEAD/domains/manufacturing-environments/discover-platforms/onto.ttl)|

#### Criterion detail
|Identifier|[proper-extension-predicate](https://ns.inria.fr/olivaw#proper-extension-predicate)|
|----|----|
|Title|Predicate&#32;extension&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;test&#32;the&#32;proper&#32;use&#32;of&#32;predicates&#32;rdfs:subClassOf&#32;and&#32;rdfs:subPropertyOf&#32;on&#32;the&#32;ontology&#32;terms|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-77)|Identifier|`property-subclassof`|
|[Section top](#pass-outcome-number-77)|Title|No&#32;property&#32;subclass|
|[Section top](#pass-outcome-number-77)|Description|No&#32;ontology&#32;property&#32;is&#32;a&#32;subclass|

***
### Pass Outcome number 78

[Jump to summary definition](#summary-Pass-78)	|	[Previous Pass outcome](#pass-outcome-number-77)	|	[Next Pass outcome](#pass-outcome-number-79)

:white_check_mark:Pass outcome
#### Subject detail
|Name|modelet-manufacturing-environments-discover-platforms|
|----|----|
|Title|Standalone&#32;modelet&#32;domains&#92;manufacturing-environments&#92;discover-platforms&#92;onto.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Modelet manufacturing-environments/discover-platforms](https://github.com/HyperAgents/hmas/blob/HEAD/domains/manufacturing-environments/discover-platforms/onto.ttl)|

#### Criterion detail
|Identifier|[proper-extension-predicate](https://ns.inria.fr/olivaw#proper-extension-predicate)|
|----|----|
|Title|Predicate&#32;extension&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;test&#32;the&#32;proper&#32;use&#32;of&#32;predicates&#32;rdfs:subClassOf&#32;and&#32;rdfs:subPropertyOf&#32;on&#32;the&#32;ontology&#32;terms|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-78)|Identifier|`subclassof-property`|
|[Section top](#pass-outcome-number-78)|Title|No&#32;subclass&#32;of&#32;property|
|[Section top](#pass-outcome-number-78)|Description|No&#32;ontology&#32;term&#32;is&#32;a&#32;subclass&#32;of&#32;a&#32;property|

***
### Pass Outcome number 79

[Jump to summary definition](#summary-Pass-79)	|	[Previous Pass outcome](#pass-outcome-number-78)	|	[Next Pass outcome](#pass-outcome-number-80)

:white_check_mark:Pass outcome
#### Subject detail
|Name|modelet-manufacturing-environments-discover-platforms|
|----|----|
|Title|Standalone&#32;modelet&#32;domains&#92;manufacturing-environments&#92;discover-platforms&#92;onto.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Modelet manufacturing-environments/discover-platforms](https://github.com/HyperAgents/hmas/blob/HEAD/domains/manufacturing-environments/discover-platforms/onto.ttl)|

#### Criterion detail
|Identifier|[proper-extension-predicate](https://ns.inria.fr/olivaw#proper-extension-predicate)|
|----|----|
|Title|Predicate&#32;extension&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;test&#32;the&#32;proper&#32;use&#32;of&#32;predicates&#32;rdfs:subClassOf&#32;and&#32;rdfs:subPropertyOf&#32;on&#32;the&#32;ontology&#32;terms|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-79)|Identifier|`subpropertyof-class`|
|[Section top](#pass-outcome-number-79)|Title|No&#32;subproperty&#32;of&#32;class|
|[Section top](#pass-outcome-number-79)|Description|No&#32;ontology&#32;term&#32;is&#32;a&#32;subproperty&#32;of&#32;a&#32;class|

***
### Pass Outcome number 80

[Jump to summary definition](#summary-Pass-80)	|	[Previous Pass outcome](#pass-outcome-number-79)	|	[Next Pass outcome](#pass-outcome-number-81)

:white_check_mark:Pass outcome
#### Subject detail
|Name|modelet-manufacturing-environments-discover-platforms|
|----|----|
|Title|Standalone&#32;modelet&#32;domains&#92;manufacturing-environments&#92;discover-platforms&#92;onto.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Modelet manufacturing-environments/discover-platforms](https://github.com/HyperAgents/hmas/blob/HEAD/domains/manufacturing-environments/discover-platforms/onto.ttl)|

#### Criterion detail
|Identifier|[term-referencing](https://ns.inria.fr/olivaw#term-referencing)|
|----|----|
|Title|Term&#32;referencing&#32;test|
|Description|A&#32;test&#32;case&#32;from&#32;the&#32;Best&#32;Practices&#32;tests&#32;checking&#32;if&#32;each&#32;term&#32;of&#32;the&#32;test&#32;subject&#32;is&#32;referenced&#32;to&#32;a&#32;module&#32;through&#32;a&#32;rdfs:isDefinedBy&#32;property.|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-80)|Identifier|`no-reference-module`|
|[Section top](#pass-outcome-number-80)|Title|Any&#32;term&#32;is&#32;referenced|
|[Section top](#pass-outcome-number-80)|Description|Each&#32;term&#32;of&#32;the&#32;test&#32;subject&#32;is&#32;linked&#32;to&#32;a&#32;module&#32;by&#32;a&#32;rdfs:isDefinedBy&#32;property|

***
### Pass Outcome number 81

[Jump to summary definition](#summary-Pass-81)	|	[Previous Pass outcome](#pass-outcome-number-80)	|	[Next Pass outcome](#pass-outcome-number-82)

:white_check_mark:Pass outcome
#### Subject detail
|Name|modelet-manufacturing-environments-discover-platforms|
|----|----|
|Title|Standalone&#32;modelet&#32;domains&#92;manufacturing-environments&#92;discover-platforms&#92;onto.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Modelet manufacturing-environments/discover-platforms](https://github.com/HyperAgents/hmas/blob/HEAD/domains/manufacturing-environments/discover-platforms/onto.ttl)|

#### Criterion detail
|Identifier|[terms-differenciation](https://ns.inria.fr/olivaw#terms-differenciation)|
|----|----|
|Title|Terms&#32;differenciation&#32;test|
|Description|A&#32;test&#32;case&#32;from&#32;the&#32;Best&#32;Practices&#32;tests&#32;checking&#32;if&#32;all&#32;the&#32;terms&#32;are&#32;different&#32;enough&#32;from&#32;each&#32;other&#32;according&#32;to&#32;the&#32;Levenshtein&#32;distance&#32;metric.|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-81)|Identifier|`too-close-terms`|
|[Section top](#pass-outcome-number-81)|Title|Terms&#32;differenciated&#32;enough|
|[Section top](#pass-outcome-number-81)|Description|All&#32;the&#32;terms&#32;have&#32;have&#32;a&#32;satisfying&#32;Levenshtein&#32;distance&#32;from&#32;each&#32;other&#32;term.|

***
### Pass Outcome number 82

[Jump to summary definition](#summary-Pass-82)	|	[Previous Pass outcome](#pass-outcome-number-81)	|	[Next Pass outcome](#pass-outcome-number-83)

:white_check_mark:Pass outcome
#### Subject detail
|Name|modelet-manufacturing-environments-discover-organization|
|----|----|
|Title|Standalone&#32;modelet&#32;domains&#92;manufacturing-environments&#92;discover-organization&#92;onto.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Modelet manufacturing-environments/discover-organization](https://github.com/HyperAgents/hmas/blob/HEAD/domains/manufacturing-environments/discover-organization/onto.ttl)|

#### Criterion detail
|Identifier|[domain-and-range-referencing](https://ns.inria.fr/olivaw#domain-and-range-referencing)|
|----|----|
|Title|Domain&#32;and&#32;range&#32;referencing&#32;test|
|Description|A&#32;test&#32;case&#32;from&#32;the&#32;Best&#32;Practices&#32;tests&#32;checking&#32;if&#32;all&#32;the&#32;ranges&#32;and&#32;domains&#32;from&#32;the&#32;test&#32;subject&#32;point&#32;to&#32;terms&#32;that&#32;are&#32;defined&#32;in&#32;the&#32;vocabulary.|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-82)|Identifier|`domain-out-of-vocabulary`|
|[Section top](#pass-outcome-number-82)|Title|Domains&#32;properly&#32;defined|
|[Section top](#pass-outcome-number-82)|Description|Each&#32;rdfs:domain&#32;is&#32;defined&#32;within&#32;the&#32;fragment|

***
### Pass Outcome number 83

[Jump to summary definition](#summary-Pass-83)	|	[Previous Pass outcome](#pass-outcome-number-82)	|	[Next Pass outcome](#pass-outcome-number-84)

:white_check_mark:Pass outcome
#### Subject detail
|Name|modelet-manufacturing-environments-discover-organization|
|----|----|
|Title|Standalone&#32;modelet&#32;domains&#92;manufacturing-environments&#92;discover-organization&#92;onto.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Modelet manufacturing-environments/discover-organization](https://github.com/HyperAgents/hmas/blob/HEAD/domains/manufacturing-environments/discover-organization/onto.ttl)|

#### Criterion detail
|Identifier|[domain-and-range-referencing](https://ns.inria.fr/olivaw#domain-and-range-referencing)|
|----|----|
|Title|Domain&#32;and&#32;range&#32;referencing&#32;test|
|Description|A&#32;test&#32;case&#32;from&#32;the&#32;Best&#32;Practices&#32;tests&#32;checking&#32;if&#32;all&#32;the&#32;ranges&#32;and&#32;domains&#32;from&#32;the&#32;test&#32;subject&#32;point&#32;to&#32;terms&#32;that&#32;are&#32;defined&#32;in&#32;the&#32;vocabulary.|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-83)|Identifier|`range-out-of-vocabulary`|
|[Section top](#pass-outcome-number-83)|Title|Ranges&#32;properly&#32;defined|
|[Section top](#pass-outcome-number-83)|Description|Each&#32;rdfs:range&#32;is&#32;defined&#32;within&#32;the&#32;fragment|

***
### Pass Outcome number 84

[Jump to summary definition](#summary-Pass-84)	|	[Previous Pass outcome](#pass-outcome-number-83)	|	[Next Pass outcome](#pass-outcome-number-85)

:white_check_mark:Pass outcome
#### Subject detail
|Name|modelet-manufacturing-environments-discover-organization|
|----|----|
|Title|Standalone&#32;modelet&#32;domains&#92;manufacturing-environments&#92;discover-organization&#92;onto.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Modelet manufacturing-environments/discover-organization](https://github.com/HyperAgents/hmas/blob/HEAD/domains/manufacturing-environments/discover-organization/onto.ttl)|

#### Criterion detail
|Identifier|[labeled-terms](https://ns.inria.fr/olivaw#labeled-terms)|
|----|----|
|Title|Term&#32;labeling&#32;test|
|Description|A&#32;test&#32;case&#32;from&#32;the&#32;Best&#32;Practices&#32;tests&#32;checking&#32;if&#32;all&#32;the&#32;terms&#32;of&#32;the&#32;subject&#32;have&#32;a&#32;rdfs:label&#32;property&#32;pointing&#32;to&#32;a&#32;literal&#32;in&#32;English|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-84)|Identifier|`not-labeled-term`|
|[Section top](#pass-outcome-number-84)|Title|All&#32;terms&#32;labeled|
|[Section top](#pass-outcome-number-84)|Description|All&#32;the&#32;terms&#32;defined&#32;in&#32;the&#32;subject&#32;have&#32;a&#32;rdfs:label&#32;in&#32;English|

***
### Pass Outcome number 85

[Jump to summary definition](#summary-Pass-85)	|	[Previous Pass outcome](#pass-outcome-number-84)	|	[Next Pass outcome](#pass-outcome-number-86)

:white_check_mark:Pass outcome
#### Subject detail
|Name|modelet-manufacturing-environments-discover-organization|
|----|----|
|Title|Standalone&#32;modelet&#32;domains&#92;manufacturing-environments&#92;discover-organization&#92;onto.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Modelet manufacturing-environments/discover-organization](https://github.com/HyperAgents/hmas/blob/HEAD/domains/manufacturing-environments/discover-organization/onto.ttl)|

#### Criterion detail
|Identifier|[owl-rl-constraint](https://ns.inria.fr/olivaw#owl-rl-constraint)|
|----|----|
|Title|OWL&#32;RL&#32;Constraint&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;check&#32;wether&#32;the&#32;test&#32;subject&#32;is&#32;syntaxically&#32;correct&#32;or&#32;not.|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-85)|Identifier|`owl-rl-constraint-violation`|
|[Section top](#pass-outcome-number-85)|Title|OWL&#32;RL&#32;consistent|
|[Section top](#pass-outcome-number-85)|Description|The&#32;provided&#32;graph&#32;is&#32;consistent&#32;for&#32;any&#32;OWL&#32;RL&#32;constraint|

***
### Pass Outcome number 86

[Jump to summary definition](#summary-Pass-86)	|	[Previous Pass outcome](#pass-outcome-number-85)	|	[Next Pass outcome](#pass-outcome-number-87)

:white_check_mark:Pass outcome
#### Subject detail
|Name|modelet-manufacturing-environments-discover-organization|
|----|----|
|Title|Standalone&#32;modelet&#32;domains&#92;manufacturing-environments&#92;discover-organization&#92;onto.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Modelet manufacturing-environments/discover-organization](https://github.com/HyperAgents/hmas/blob/HEAD/domains/manufacturing-environments/discover-organization/onto.ttl)|

#### Criterion detail
|Identifier|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|
|----|----|
|Title|Profile&#32;compatibility&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;check&#32;whether&#32;the&#32;test&#32;subject&#32;is&#32;compatible&#32;with&#32;a&#32;profile&#32;or&#32;not,&#32;and&#32;if&#32;it&#32;is&#32;not,&#32;why.|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-86)|Identifier|`owl-el-profile-error`|
|[Section top](#pass-outcome-number-86)|Title|OWL&#32;EL&#32;Profile&#32;compatible|
|[Section top](#pass-outcome-number-86)|Description|The&#32;subject&#32;is&#32;included&#32;in&#32;the&#32;OWL&#32;EL&#32;sublanguage|

***
### Pass Outcome number 87

[Jump to summary definition](#summary-Pass-87)	|	[Previous Pass outcome](#pass-outcome-number-86)	|	[Next Pass outcome](#pass-outcome-number-88)

:white_check_mark:Pass outcome
#### Subject detail
|Name|modelet-manufacturing-environments-discover-organization|
|----|----|
|Title|Standalone&#32;modelet&#32;domains&#92;manufacturing-environments&#92;discover-organization&#92;onto.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Modelet manufacturing-environments/discover-organization](https://github.com/HyperAgents/hmas/blob/HEAD/domains/manufacturing-environments/discover-organization/onto.ttl)|

#### Criterion detail
|Identifier|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|
|----|----|
|Title|Profile&#32;compatibility&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;check&#32;whether&#32;the&#32;test&#32;subject&#32;is&#32;compatible&#32;with&#32;a&#32;profile&#32;or&#32;not,&#32;and&#32;if&#32;it&#32;is&#32;not,&#32;why.|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-87)|Identifier|`owl-ql-profile-error`|
|[Section top](#pass-outcome-number-87)|Title|OWL&#32;QL&#32;Profile&#32;compatible|
|[Section top](#pass-outcome-number-87)|Description|The&#32;subject&#32;is&#32;included&#32;in&#32;the&#32;OWL&#32;QL&#32;sublanguage|

***
### Pass Outcome number 88

[Jump to summary definition](#summary-Pass-88)	|	[Previous Pass outcome](#pass-outcome-number-87)	|	[Next Pass outcome](#pass-outcome-number-89)

:white_check_mark:Pass outcome
#### Subject detail
|Name|modelet-manufacturing-environments-discover-organization|
|----|----|
|Title|Standalone&#32;modelet&#32;domains&#92;manufacturing-environments&#92;discover-organization&#92;onto.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Modelet manufacturing-environments/discover-organization](https://github.com/HyperAgents/hmas/blob/HEAD/domains/manufacturing-environments/discover-organization/onto.ttl)|

#### Criterion detail
|Identifier|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|
|----|----|
|Title|Profile&#32;compatibility&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;check&#32;whether&#32;the&#32;test&#32;subject&#32;is&#32;compatible&#32;with&#32;a&#32;profile&#32;or&#32;not,&#32;and&#32;if&#32;it&#32;is&#32;not,&#32;why.|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-88)|Identifier|`owl-rl-profile-error`|
|[Section top](#pass-outcome-number-88)|Title|OWL&#32;RL&#32;Profile&#32;compatible|
|[Section top](#pass-outcome-number-88)|Description|The&#32;subject&#32;is&#32;included&#32;in&#32;the&#32;OWL&#32;RL&#32;sublanguage|

***
### Pass Outcome number 89

[Jump to summary definition](#summary-Pass-89)	|	[Previous Pass outcome](#pass-outcome-number-88)	|	[Next Pass outcome](#pass-outcome-number-90)

:white_check_mark:Pass outcome
#### Subject detail
|Name|modelet-manufacturing-environments-discover-organization|
|----|----|
|Title|Standalone&#32;modelet&#32;domains&#92;manufacturing-environments&#92;discover-organization&#92;onto.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Modelet manufacturing-environments/discover-organization](https://github.com/HyperAgents/hmas/blob/HEAD/domains/manufacturing-environments/discover-organization/onto.ttl)|

#### Criterion detail
|Identifier|[proper-extension-predicate](https://ns.inria.fr/olivaw#proper-extension-predicate)|
|----|----|
|Title|Predicate&#32;extension&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;test&#32;the&#32;proper&#32;use&#32;of&#32;predicates&#32;rdfs:subClassOf&#32;and&#32;rdfs:subPropertyOf&#32;on&#32;the&#32;ontology&#32;terms|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-89)|Identifier|`class-subpropertyof`|
|[Section top](#pass-outcome-number-89)|Title|No&#32;class&#32;subproperty|
|[Section top](#pass-outcome-number-89)|Description|No&#32;ontology&#32;class&#32;is&#32;a&#32;subproperty|

***
### Pass Outcome number 90

[Jump to summary definition](#summary-Pass-90)	|	[Previous Pass outcome](#pass-outcome-number-89)	|	[Next Pass outcome](#pass-outcome-number-91)

:white_check_mark:Pass outcome
#### Subject detail
|Name|modelet-manufacturing-environments-discover-organization|
|----|----|
|Title|Standalone&#32;modelet&#32;domains&#92;manufacturing-environments&#92;discover-organization&#92;onto.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Modelet manufacturing-environments/discover-organization](https://github.com/HyperAgents/hmas/blob/HEAD/domains/manufacturing-environments/discover-organization/onto.ttl)|

#### Criterion detail
|Identifier|[proper-extension-predicate](https://ns.inria.fr/olivaw#proper-extension-predicate)|
|----|----|
|Title|Predicate&#32;extension&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;test&#32;the&#32;proper&#32;use&#32;of&#32;predicates&#32;rdfs:subClassOf&#32;and&#32;rdfs:subPropertyOf&#32;on&#32;the&#32;ontology&#32;terms|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-90)|Identifier|`property-subclassof`|
|[Section top](#pass-outcome-number-90)|Title|No&#32;property&#32;subclass|
|[Section top](#pass-outcome-number-90)|Description|No&#32;ontology&#32;property&#32;is&#32;a&#32;subclass|

***
### Pass Outcome number 91

[Jump to summary definition](#summary-Pass-91)	|	[Previous Pass outcome](#pass-outcome-number-90)	|	[Next Pass outcome](#pass-outcome-number-92)

:white_check_mark:Pass outcome
#### Subject detail
|Name|modelet-manufacturing-environments-discover-organization|
|----|----|
|Title|Standalone&#32;modelet&#32;domains&#92;manufacturing-environments&#92;discover-organization&#92;onto.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Modelet manufacturing-environments/discover-organization](https://github.com/HyperAgents/hmas/blob/HEAD/domains/manufacturing-environments/discover-organization/onto.ttl)|

#### Criterion detail
|Identifier|[proper-extension-predicate](https://ns.inria.fr/olivaw#proper-extension-predicate)|
|----|----|
|Title|Predicate&#32;extension&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;test&#32;the&#32;proper&#32;use&#32;of&#32;predicates&#32;rdfs:subClassOf&#32;and&#32;rdfs:subPropertyOf&#32;on&#32;the&#32;ontology&#32;terms|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-91)|Identifier|`subclassof-property`|
|[Section top](#pass-outcome-number-91)|Title|No&#32;subclass&#32;of&#32;property|
|[Section top](#pass-outcome-number-91)|Description|No&#32;ontology&#32;term&#32;is&#32;a&#32;subclass&#32;of&#32;a&#32;property|

***
### Pass Outcome number 92

[Jump to summary definition](#summary-Pass-92)	|	[Previous Pass outcome](#pass-outcome-number-91)	|	[Next Pass outcome](#pass-outcome-number-93)

:white_check_mark:Pass outcome
#### Subject detail
|Name|modelet-manufacturing-environments-discover-organization|
|----|----|
|Title|Standalone&#32;modelet&#32;domains&#92;manufacturing-environments&#92;discover-organization&#92;onto.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Modelet manufacturing-environments/discover-organization](https://github.com/HyperAgents/hmas/blob/HEAD/domains/manufacturing-environments/discover-organization/onto.ttl)|

#### Criterion detail
|Identifier|[proper-extension-predicate](https://ns.inria.fr/olivaw#proper-extension-predicate)|
|----|----|
|Title|Predicate&#32;extension&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;test&#32;the&#32;proper&#32;use&#32;of&#32;predicates&#32;rdfs:subClassOf&#32;and&#32;rdfs:subPropertyOf&#32;on&#32;the&#32;ontology&#32;terms|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-92)|Identifier|`subpropertyof-class`|
|[Section top](#pass-outcome-number-92)|Title|No&#32;subproperty&#32;of&#32;class|
|[Section top](#pass-outcome-number-92)|Description|No&#32;ontology&#32;term&#32;is&#32;a&#32;subproperty&#32;of&#32;a&#32;class|

***
### Pass Outcome number 93

[Jump to summary definition](#summary-Pass-93)	|	[Previous Pass outcome](#pass-outcome-number-92)	|	[Next Pass outcome](#pass-outcome-number-94)

:white_check_mark:Pass outcome
#### Subject detail
|Name|modelet-manufacturing-environments-discover-organization|
|----|----|
|Title|Standalone&#32;modelet&#32;domains&#92;manufacturing-environments&#92;discover-organization&#92;onto.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Modelet manufacturing-environments/discover-organization](https://github.com/HyperAgents/hmas/blob/HEAD/domains/manufacturing-environments/discover-organization/onto.ttl)|

#### Criterion detail
|Identifier|[term-referencing](https://ns.inria.fr/olivaw#term-referencing)|
|----|----|
|Title|Term&#32;referencing&#32;test|
|Description|A&#32;test&#32;case&#32;from&#32;the&#32;Best&#32;Practices&#32;tests&#32;checking&#32;if&#32;each&#32;term&#32;of&#32;the&#32;test&#32;subject&#32;is&#32;referenced&#32;to&#32;a&#32;module&#32;through&#32;a&#32;rdfs:isDefinedBy&#32;property.|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-93)|Identifier|`no-reference-module`|
|[Section top](#pass-outcome-number-93)|Title|Any&#32;term&#32;is&#32;referenced|
|[Section top](#pass-outcome-number-93)|Description|Each&#32;term&#32;of&#32;the&#32;test&#32;subject&#32;is&#32;linked&#32;to&#32;a&#32;module&#32;by&#32;a&#32;rdfs:isDefinedBy&#32;property|

***
### Pass Outcome number 94

[Jump to summary definition](#summary-Pass-94)	|	[Previous Pass outcome](#pass-outcome-number-93)	|	[Next Pass outcome](#pass-outcome-number-95)

:white_check_mark:Pass outcome
#### Subject detail
|Name|modelet-manufacturing-environments-discover-organization|
|----|----|
|Title|Standalone&#32;modelet&#32;domains&#92;manufacturing-environments&#92;discover-organization&#92;onto.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Modelet manufacturing-environments/discover-organization](https://github.com/HyperAgents/hmas/blob/HEAD/domains/manufacturing-environments/discover-organization/onto.ttl)|

#### Criterion detail
|Identifier|[terms-differenciation](https://ns.inria.fr/olivaw#terms-differenciation)|
|----|----|
|Title|Terms&#32;differenciation&#32;test|
|Description|A&#32;test&#32;case&#32;from&#32;the&#32;Best&#32;Practices&#32;tests&#32;checking&#32;if&#32;all&#32;the&#32;terms&#32;are&#32;different&#32;enough&#32;from&#32;each&#32;other&#32;according&#32;to&#32;the&#32;Levenshtein&#32;distance&#32;metric.|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-94)|Identifier|`too-close-terms`|
|[Section top](#pass-outcome-number-94)|Title|Terms&#32;differenciated&#32;enough|
|[Section top](#pass-outcome-number-94)|Description|All&#32;the&#32;terms&#32;have&#32;have&#32;a&#32;satisfying&#32;Levenshtein&#32;distance&#32;from&#32;each&#32;other&#32;term.|

***
### Pass Outcome number 95

[Jump to summary definition](#summary-Pass-95)	|	[Previous Pass outcome](#pass-outcome-number-94)	|	[Next Pass outcome](#pass-outcome-number-96)

:white_check_mark:Pass outcome
#### Subject detail
|Name|modelet-manufacturing-environments-discover-core|
|----|----|
|Title|Standalone&#32;modelet&#32;domains&#92;manufacturing-environments&#92;discover-core&#92;onto.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Modelet manufacturing-environments/discover-core](https://github.com/HyperAgents/hmas/blob/HEAD/domains/manufacturing-environments/discover-core/onto.ttl)|

#### Criterion detail
|Identifier|[domain-and-range-referencing](https://ns.inria.fr/olivaw#domain-and-range-referencing)|
|----|----|
|Title|Domain&#32;and&#32;range&#32;referencing&#32;test|
|Description|A&#32;test&#32;case&#32;from&#32;the&#32;Best&#32;Practices&#32;tests&#32;checking&#32;if&#32;all&#32;the&#32;ranges&#32;and&#32;domains&#32;from&#32;the&#32;test&#32;subject&#32;point&#32;to&#32;terms&#32;that&#32;are&#32;defined&#32;in&#32;the&#32;vocabulary.|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-95)|Identifier|`domain-out-of-vocabulary`|
|[Section top](#pass-outcome-number-95)|Title|Domains&#32;properly&#32;defined|
|[Section top](#pass-outcome-number-95)|Description|Each&#32;rdfs:domain&#32;is&#32;defined&#32;within&#32;the&#32;fragment|

***
### Pass Outcome number 96

[Jump to summary definition](#summary-Pass-96)	|	[Previous Pass outcome](#pass-outcome-number-95)	|	[Next Pass outcome](#pass-outcome-number-97)

:white_check_mark:Pass outcome
#### Subject detail
|Name|modelet-manufacturing-environments-discover-core|
|----|----|
|Title|Standalone&#32;modelet&#32;domains&#92;manufacturing-environments&#92;discover-core&#92;onto.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Modelet manufacturing-environments/discover-core](https://github.com/HyperAgents/hmas/blob/HEAD/domains/manufacturing-environments/discover-core/onto.ttl)|

#### Criterion detail
|Identifier|[domain-and-range-referencing](https://ns.inria.fr/olivaw#domain-and-range-referencing)|
|----|----|
|Title|Domain&#32;and&#32;range&#32;referencing&#32;test|
|Description|A&#32;test&#32;case&#32;from&#32;the&#32;Best&#32;Practices&#32;tests&#32;checking&#32;if&#32;all&#32;the&#32;ranges&#32;and&#32;domains&#32;from&#32;the&#32;test&#32;subject&#32;point&#32;to&#32;terms&#32;that&#32;are&#32;defined&#32;in&#32;the&#32;vocabulary.|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-96)|Identifier|`range-out-of-vocabulary`|
|[Section top](#pass-outcome-number-96)|Title|Ranges&#32;properly&#32;defined|
|[Section top](#pass-outcome-number-96)|Description|Each&#32;rdfs:range&#32;is&#32;defined&#32;within&#32;the&#32;fragment|

***
### Pass Outcome number 97

[Jump to summary definition](#summary-Pass-97)	|	[Previous Pass outcome](#pass-outcome-number-96)	|	[Next Pass outcome](#pass-outcome-number-98)

:white_check_mark:Pass outcome
#### Subject detail
|Name|modelet-manufacturing-environments-discover-core|
|----|----|
|Title|Standalone&#32;modelet&#32;domains&#92;manufacturing-environments&#92;discover-core&#92;onto.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Modelet manufacturing-environments/discover-core](https://github.com/HyperAgents/hmas/blob/HEAD/domains/manufacturing-environments/discover-core/onto.ttl)|

#### Criterion detail
|Identifier|[labeled-terms](https://ns.inria.fr/olivaw#labeled-terms)|
|----|----|
|Title|Term&#32;labeling&#32;test|
|Description|A&#32;test&#32;case&#32;from&#32;the&#32;Best&#32;Practices&#32;tests&#32;checking&#32;if&#32;all&#32;the&#32;terms&#32;of&#32;the&#32;subject&#32;have&#32;a&#32;rdfs:label&#32;property&#32;pointing&#32;to&#32;a&#32;literal&#32;in&#32;English|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-97)|Identifier|`not-labeled-term`|
|[Section top](#pass-outcome-number-97)|Title|All&#32;terms&#32;labeled|
|[Section top](#pass-outcome-number-97)|Description|All&#32;the&#32;terms&#32;defined&#32;in&#32;the&#32;subject&#32;have&#32;a&#32;rdfs:label&#32;in&#32;English|

***
### Pass Outcome number 98

[Jump to summary definition](#summary-Pass-98)	|	[Previous Pass outcome](#pass-outcome-number-97)	|	[Next Pass outcome](#pass-outcome-number-99)

:white_check_mark:Pass outcome
#### Subject detail
|Name|modelet-manufacturing-environments-discover-core|
|----|----|
|Title|Standalone&#32;modelet&#32;domains&#92;manufacturing-environments&#92;discover-core&#92;onto.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Modelet manufacturing-environments/discover-core](https://github.com/HyperAgents/hmas/blob/HEAD/domains/manufacturing-environments/discover-core/onto.ttl)|

#### Criterion detail
|Identifier|[owl-rl-constraint](https://ns.inria.fr/olivaw#owl-rl-constraint)|
|----|----|
|Title|OWL&#32;RL&#32;Constraint&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;check&#32;wether&#32;the&#32;test&#32;subject&#32;is&#32;syntaxically&#32;correct&#32;or&#32;not.|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-98)|Identifier|`owl-rl-constraint-violation`|
|[Section top](#pass-outcome-number-98)|Title|OWL&#32;RL&#32;consistent|
|[Section top](#pass-outcome-number-98)|Description|The&#32;provided&#32;graph&#32;is&#32;consistent&#32;for&#32;any&#32;OWL&#32;RL&#32;constraint|

***
### Pass Outcome number 99

[Jump to summary definition](#summary-Pass-99)	|	[Previous Pass outcome](#pass-outcome-number-98)	|	[Next Pass outcome](#pass-outcome-number-100)

:white_check_mark:Pass outcome
#### Subject detail
|Name|modelet-manufacturing-environments-discover-core|
|----|----|
|Title|Standalone&#32;modelet&#32;domains&#92;manufacturing-environments&#92;discover-core&#92;onto.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Modelet manufacturing-environments/discover-core](https://github.com/HyperAgents/hmas/blob/HEAD/domains/manufacturing-environments/discover-core/onto.ttl)|

#### Criterion detail
|Identifier|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|
|----|----|
|Title|Profile&#32;compatibility&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;check&#32;whether&#32;the&#32;test&#32;subject&#32;is&#32;compatible&#32;with&#32;a&#32;profile&#32;or&#32;not,&#32;and&#32;if&#32;it&#32;is&#32;not,&#32;why.|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-99)|Identifier|`owl-rl-profile-error`|
|[Section top](#pass-outcome-number-99)|Title|OWL&#32;RL&#32;Profile&#32;compatible|
|[Section top](#pass-outcome-number-99)|Description|The&#32;subject&#32;is&#32;included&#32;in&#32;the&#32;OWL&#32;RL&#32;sublanguage|

***
### Pass Outcome number 100

[Jump to summary definition](#summary-Pass-100)	|	[Previous Pass outcome](#pass-outcome-number-99)	|	[Next Pass outcome](#pass-outcome-number-101)

:white_check_mark:Pass outcome
#### Subject detail
|Name|modelet-manufacturing-environments-discover-core|
|----|----|
|Title|Standalone&#32;modelet&#32;domains&#92;manufacturing-environments&#92;discover-core&#92;onto.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Modelet manufacturing-environments/discover-core](https://github.com/HyperAgents/hmas/blob/HEAD/domains/manufacturing-environments/discover-core/onto.ttl)|

#### Criterion detail
|Identifier|[proper-extension-predicate](https://ns.inria.fr/olivaw#proper-extension-predicate)|
|----|----|
|Title|Predicate&#32;extension&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;test&#32;the&#32;proper&#32;use&#32;of&#32;predicates&#32;rdfs:subClassOf&#32;and&#32;rdfs:subPropertyOf&#32;on&#32;the&#32;ontology&#32;terms|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-100)|Identifier|`class-subpropertyof`|
|[Section top](#pass-outcome-number-100)|Title|No&#32;class&#32;subproperty|
|[Section top](#pass-outcome-number-100)|Description|No&#32;ontology&#32;class&#32;is&#32;a&#32;subproperty|

***
### Pass Outcome number 101

[Jump to summary definition](#summary-Pass-101)	|	[Previous Pass outcome](#pass-outcome-number-100)	|	[Next Pass outcome](#pass-outcome-number-102)

:white_check_mark:Pass outcome
#### Subject detail
|Name|modelet-manufacturing-environments-discover-core|
|----|----|
|Title|Standalone&#32;modelet&#32;domains&#92;manufacturing-environments&#92;discover-core&#92;onto.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Modelet manufacturing-environments/discover-core](https://github.com/HyperAgents/hmas/blob/HEAD/domains/manufacturing-environments/discover-core/onto.ttl)|

#### Criterion detail
|Identifier|[proper-extension-predicate](https://ns.inria.fr/olivaw#proper-extension-predicate)|
|----|----|
|Title|Predicate&#32;extension&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;test&#32;the&#32;proper&#32;use&#32;of&#32;predicates&#32;rdfs:subClassOf&#32;and&#32;rdfs:subPropertyOf&#32;on&#32;the&#32;ontology&#32;terms|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-101)|Identifier|`property-subclassof`|
|[Section top](#pass-outcome-number-101)|Title|No&#32;property&#32;subclass|
|[Section top](#pass-outcome-number-101)|Description|No&#32;ontology&#32;property&#32;is&#32;a&#32;subclass|

***
### Pass Outcome number 102

[Jump to summary definition](#summary-Pass-102)	|	[Previous Pass outcome](#pass-outcome-number-101)	|	[Next Pass outcome](#pass-outcome-number-103)

:white_check_mark:Pass outcome
#### Subject detail
|Name|modelet-manufacturing-environments-discover-core|
|----|----|
|Title|Standalone&#32;modelet&#32;domains&#92;manufacturing-environments&#92;discover-core&#92;onto.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Modelet manufacturing-environments/discover-core](https://github.com/HyperAgents/hmas/blob/HEAD/domains/manufacturing-environments/discover-core/onto.ttl)|

#### Criterion detail
|Identifier|[proper-extension-predicate](https://ns.inria.fr/olivaw#proper-extension-predicate)|
|----|----|
|Title|Predicate&#32;extension&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;test&#32;the&#32;proper&#32;use&#32;of&#32;predicates&#32;rdfs:subClassOf&#32;and&#32;rdfs:subPropertyOf&#32;on&#32;the&#32;ontology&#32;terms|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-102)|Identifier|`subclassof-property`|
|[Section top](#pass-outcome-number-102)|Title|No&#32;subclass&#32;of&#32;property|
|[Section top](#pass-outcome-number-102)|Description|No&#32;ontology&#32;term&#32;is&#32;a&#32;subclass&#32;of&#32;a&#32;property|

***
### Pass Outcome number 103

[Jump to summary definition](#summary-Pass-103)	|	[Previous Pass outcome](#pass-outcome-number-102)	|	[Next Pass outcome](#pass-outcome-number-104)

:white_check_mark:Pass outcome
#### Subject detail
|Name|modelet-manufacturing-environments-discover-core|
|----|----|
|Title|Standalone&#32;modelet&#32;domains&#92;manufacturing-environments&#92;discover-core&#92;onto.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Modelet manufacturing-environments/discover-core](https://github.com/HyperAgents/hmas/blob/HEAD/domains/manufacturing-environments/discover-core/onto.ttl)|

#### Criterion detail
|Identifier|[proper-extension-predicate](https://ns.inria.fr/olivaw#proper-extension-predicate)|
|----|----|
|Title|Predicate&#32;extension&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;test&#32;the&#32;proper&#32;use&#32;of&#32;predicates&#32;rdfs:subClassOf&#32;and&#32;rdfs:subPropertyOf&#32;on&#32;the&#32;ontology&#32;terms|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-103)|Identifier|`subpropertyof-class`|
|[Section top](#pass-outcome-number-103)|Title|No&#32;subproperty&#32;of&#32;class|
|[Section top](#pass-outcome-number-103)|Description|No&#32;ontology&#32;term&#32;is&#32;a&#32;subproperty&#32;of&#32;a&#32;class|

***
### Pass Outcome number 104

[Jump to summary definition](#summary-Pass-104)	|	[Previous Pass outcome](#pass-outcome-number-103)	|	[Next Pass outcome](#pass-outcome-number-105)

:white_check_mark:Pass outcome
#### Subject detail
|Name|modelet-manufacturing-environments-discover-core|
|----|----|
|Title|Standalone&#32;modelet&#32;domains&#92;manufacturing-environments&#92;discover-core&#92;onto.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Modelet manufacturing-environments/discover-core](https://github.com/HyperAgents/hmas/blob/HEAD/domains/manufacturing-environments/discover-core/onto.ttl)|

#### Criterion detail
|Identifier|[term-referencing](https://ns.inria.fr/olivaw#term-referencing)|
|----|----|
|Title|Term&#32;referencing&#32;test|
|Description|A&#32;test&#32;case&#32;from&#32;the&#32;Best&#32;Practices&#32;tests&#32;checking&#32;if&#32;each&#32;term&#32;of&#32;the&#32;test&#32;subject&#32;is&#32;referenced&#32;to&#32;a&#32;module&#32;through&#32;a&#32;rdfs:isDefinedBy&#32;property.|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-104)|Identifier|`no-reference-module`|
|[Section top](#pass-outcome-number-104)|Title|Any&#32;term&#32;is&#32;referenced|
|[Section top](#pass-outcome-number-104)|Description|Each&#32;term&#32;of&#32;the&#32;test&#32;subject&#32;is&#32;linked&#32;to&#32;a&#32;module&#32;by&#32;a&#32;rdfs:isDefinedBy&#32;property|

***
### Pass Outcome number 105

[Jump to summary definition](#summary-Pass-105)	|	[Previous Pass outcome](#pass-outcome-number-104)	|	[Next Pass outcome](#pass-outcome-number-106)

:white_check_mark:Pass outcome
#### Subject detail
|Name|modelet-manufacturing-environments-discover-core|
|----|----|
|Title|Standalone&#32;modelet&#32;domains&#92;manufacturing-environments&#92;discover-core&#92;onto.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Modelet manufacturing-environments/discover-core](https://github.com/HyperAgents/hmas/blob/HEAD/domains/manufacturing-environments/discover-core/onto.ttl)|

#### Criterion detail
|Identifier|[terms-differenciation](https://ns.inria.fr/olivaw#terms-differenciation)|
|----|----|
|Title|Terms&#32;differenciation&#32;test|
|Description|A&#32;test&#32;case&#32;from&#32;the&#32;Best&#32;Practices&#32;tests&#32;checking&#32;if&#32;all&#32;the&#32;terms&#32;are&#32;different&#32;enough&#32;from&#32;each&#32;other&#32;according&#32;to&#32;the&#32;Levenshtein&#32;distance&#32;metric.|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-105)|Identifier|`too-close-terms`|
|[Section top](#pass-outcome-number-105)|Title|Terms&#32;differenciated&#32;enough|
|[Section top](#pass-outcome-number-105)|Description|All&#32;the&#32;terms&#32;have&#32;have&#32;a&#32;satisfying&#32;Levenshtein&#32;distance&#32;from&#32;each&#32;other&#32;term.|

***
### Pass Outcome number 106

[Jump to summary definition](#summary-Pass-106)	|	[Previous Pass outcome](#pass-outcome-number-105)	|	[Next Pass outcome](#pass-outcome-number-107)

:white_check_mark:Pass outcome
#### Subject detail
|Name|modelet-manufacturing-environments-discover-behavior-specifications|
|----|----|
|Title|Standalone&#32;modelet&#32;domains&#92;manufacturing-environments&#92;discover-behavior-specifications&#92;onto.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Modelet manufacturing-environments/discover-behavior-specifications](https://github.com/HyperAgents/hmas/blob/HEAD/domains/manufacturing-environments/discover-behavior-specifications/onto.ttl)|

#### Criterion detail
|Identifier|[domain-and-range-referencing](https://ns.inria.fr/olivaw#domain-and-range-referencing)|
|----|----|
|Title|Domain&#32;and&#32;range&#32;referencing&#32;test|
|Description|A&#32;test&#32;case&#32;from&#32;the&#32;Best&#32;Practices&#32;tests&#32;checking&#32;if&#32;all&#32;the&#32;ranges&#32;and&#32;domains&#32;from&#32;the&#32;test&#32;subject&#32;point&#32;to&#32;terms&#32;that&#32;are&#32;defined&#32;in&#32;the&#32;vocabulary.|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-106)|Identifier|`domain-out-of-vocabulary`|
|[Section top](#pass-outcome-number-106)|Title|Domains&#32;properly&#32;defined|
|[Section top](#pass-outcome-number-106)|Description|Each&#32;rdfs:domain&#32;is&#32;defined&#32;within&#32;the&#32;fragment|

***
### Pass Outcome number 107

[Jump to summary definition](#summary-Pass-107)	|	[Previous Pass outcome](#pass-outcome-number-106)	|	[Next Pass outcome](#pass-outcome-number-108)

:white_check_mark:Pass outcome
#### Subject detail
|Name|modelet-manufacturing-environments-discover-behavior-specifications|
|----|----|
|Title|Standalone&#32;modelet&#32;domains&#92;manufacturing-environments&#92;discover-behavior-specifications&#92;onto.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Modelet manufacturing-environments/discover-behavior-specifications](https://github.com/HyperAgents/hmas/blob/HEAD/domains/manufacturing-environments/discover-behavior-specifications/onto.ttl)|

#### Criterion detail
|Identifier|[domain-and-range-referencing](https://ns.inria.fr/olivaw#domain-and-range-referencing)|
|----|----|
|Title|Domain&#32;and&#32;range&#32;referencing&#32;test|
|Description|A&#32;test&#32;case&#32;from&#32;the&#32;Best&#32;Practices&#32;tests&#32;checking&#32;if&#32;all&#32;the&#32;ranges&#32;and&#32;domains&#32;from&#32;the&#32;test&#32;subject&#32;point&#32;to&#32;terms&#32;that&#32;are&#32;defined&#32;in&#32;the&#32;vocabulary.|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-107)|Identifier|`range-out-of-vocabulary`|
|[Section top](#pass-outcome-number-107)|Title|Ranges&#32;properly&#32;defined|
|[Section top](#pass-outcome-number-107)|Description|Each&#32;rdfs:range&#32;is&#32;defined&#32;within&#32;the&#32;fragment|

***
### Pass Outcome number 108

[Jump to summary definition](#summary-Pass-108)	|	[Previous Pass outcome](#pass-outcome-number-107)	|	[Next Pass outcome](#pass-outcome-number-109)

:white_check_mark:Pass outcome
#### Subject detail
|Name|modelet-manufacturing-environments-discover-behavior-specifications|
|----|----|
|Title|Standalone&#32;modelet&#32;domains&#92;manufacturing-environments&#92;discover-behavior-specifications&#92;onto.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Modelet manufacturing-environments/discover-behavior-specifications](https://github.com/HyperAgents/hmas/blob/HEAD/domains/manufacturing-environments/discover-behavior-specifications/onto.ttl)|

#### Criterion detail
|Identifier|[labeled-terms](https://ns.inria.fr/olivaw#labeled-terms)|
|----|----|
|Title|Term&#32;labeling&#32;test|
|Description|A&#32;test&#32;case&#32;from&#32;the&#32;Best&#32;Practices&#32;tests&#32;checking&#32;if&#32;all&#32;the&#32;terms&#32;of&#32;the&#32;subject&#32;have&#32;a&#32;rdfs:label&#32;property&#32;pointing&#32;to&#32;a&#32;literal&#32;in&#32;English|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-108)|Identifier|`not-labeled-term`|
|[Section top](#pass-outcome-number-108)|Title|All&#32;terms&#32;labeled|
|[Section top](#pass-outcome-number-108)|Description|All&#32;the&#32;terms&#32;defined&#32;in&#32;the&#32;subject&#32;have&#32;a&#32;rdfs:label&#32;in&#32;English|

***
### Pass Outcome number 109

[Jump to summary definition](#summary-Pass-109)	|	[Previous Pass outcome](#pass-outcome-number-108)	|	[Next Pass outcome](#pass-outcome-number-110)

:white_check_mark:Pass outcome
#### Subject detail
|Name|modelet-manufacturing-environments-discover-behavior-specifications|
|----|----|
|Title|Standalone&#32;modelet&#32;domains&#92;manufacturing-environments&#92;discover-behavior-specifications&#92;onto.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Modelet manufacturing-environments/discover-behavior-specifications](https://github.com/HyperAgents/hmas/blob/HEAD/domains/manufacturing-environments/discover-behavior-specifications/onto.ttl)|

#### Criterion detail
|Identifier|[owl-rl-constraint](https://ns.inria.fr/olivaw#owl-rl-constraint)|
|----|----|
|Title|OWL&#32;RL&#32;Constraint&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;check&#32;wether&#32;the&#32;test&#32;subject&#32;is&#32;syntaxically&#32;correct&#32;or&#32;not.|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-109)|Identifier|`owl-rl-constraint-violation`|
|[Section top](#pass-outcome-number-109)|Title|OWL&#32;RL&#32;consistent|
|[Section top](#pass-outcome-number-109)|Description|The&#32;provided&#32;graph&#32;is&#32;consistent&#32;for&#32;any&#32;OWL&#32;RL&#32;constraint|

***
### Pass Outcome number 110

[Jump to summary definition](#summary-Pass-110)	|	[Previous Pass outcome](#pass-outcome-number-109)	|	[Next Pass outcome](#pass-outcome-number-111)

:white_check_mark:Pass outcome
#### Subject detail
|Name|modelet-manufacturing-environments-discover-behavior-specifications|
|----|----|
|Title|Standalone&#32;modelet&#32;domains&#92;manufacturing-environments&#92;discover-behavior-specifications&#92;onto.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Modelet manufacturing-environments/discover-behavior-specifications](https://github.com/HyperAgents/hmas/blob/HEAD/domains/manufacturing-environments/discover-behavior-specifications/onto.ttl)|

#### Criterion detail
|Identifier|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|
|----|----|
|Title|Profile&#32;compatibility&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;check&#32;whether&#32;the&#32;test&#32;subject&#32;is&#32;compatible&#32;with&#32;a&#32;profile&#32;or&#32;not,&#32;and&#32;if&#32;it&#32;is&#32;not,&#32;why.|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-110)|Identifier|`owl-el-profile-error`|
|[Section top](#pass-outcome-number-110)|Title|OWL&#32;EL&#32;Profile&#32;compatible|
|[Section top](#pass-outcome-number-110)|Description|The&#32;subject&#32;is&#32;included&#32;in&#32;the&#32;OWL&#32;EL&#32;sublanguage|

***
### Pass Outcome number 111

[Jump to summary definition](#summary-Pass-111)	|	[Previous Pass outcome](#pass-outcome-number-110)	|	[Next Pass outcome](#pass-outcome-number-112)

:white_check_mark:Pass outcome
#### Subject detail
|Name|modelet-manufacturing-environments-discover-behavior-specifications|
|----|----|
|Title|Standalone&#32;modelet&#32;domains&#92;manufacturing-environments&#92;discover-behavior-specifications&#92;onto.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Modelet manufacturing-environments/discover-behavior-specifications](https://github.com/HyperAgents/hmas/blob/HEAD/domains/manufacturing-environments/discover-behavior-specifications/onto.ttl)|

#### Criterion detail
|Identifier|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|
|----|----|
|Title|Profile&#32;compatibility&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;check&#32;whether&#32;the&#32;test&#32;subject&#32;is&#32;compatible&#32;with&#32;a&#32;profile&#32;or&#32;not,&#32;and&#32;if&#32;it&#32;is&#32;not,&#32;why.|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-111)|Identifier|`owl-ql-profile-error`|
|[Section top](#pass-outcome-number-111)|Title|OWL&#32;QL&#32;Profile&#32;compatible|
|[Section top](#pass-outcome-number-111)|Description|The&#32;subject&#32;is&#32;included&#32;in&#32;the&#32;OWL&#32;QL&#32;sublanguage|

***
### Pass Outcome number 112

[Jump to summary definition](#summary-Pass-112)	|	[Previous Pass outcome](#pass-outcome-number-111)	|	[Next Pass outcome](#pass-outcome-number-113)

:white_check_mark:Pass outcome
#### Subject detail
|Name|modelet-manufacturing-environments-discover-behavior-specifications|
|----|----|
|Title|Standalone&#32;modelet&#32;domains&#92;manufacturing-environments&#92;discover-behavior-specifications&#92;onto.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Modelet manufacturing-environments/discover-behavior-specifications](https://github.com/HyperAgents/hmas/blob/HEAD/domains/manufacturing-environments/discover-behavior-specifications/onto.ttl)|

#### Criterion detail
|Identifier|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|
|----|----|
|Title|Profile&#32;compatibility&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;check&#32;whether&#32;the&#32;test&#32;subject&#32;is&#32;compatible&#32;with&#32;a&#32;profile&#32;or&#32;not,&#32;and&#32;if&#32;it&#32;is&#32;not,&#32;why.|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-112)|Identifier|`owl-rl-profile-error`|
|[Section top](#pass-outcome-number-112)|Title|OWL&#32;RL&#32;Profile&#32;compatible|
|[Section top](#pass-outcome-number-112)|Description|The&#32;subject&#32;is&#32;included&#32;in&#32;the&#32;OWL&#32;RL&#32;sublanguage|

***
### Pass Outcome number 113

[Jump to summary definition](#summary-Pass-113)	|	[Previous Pass outcome](#pass-outcome-number-112)	|	[Next Pass outcome](#pass-outcome-number-114)

:white_check_mark:Pass outcome
#### Subject detail
|Name|modelet-manufacturing-environments-discover-behavior-specifications|
|----|----|
|Title|Standalone&#32;modelet&#32;domains&#92;manufacturing-environments&#92;discover-behavior-specifications&#92;onto.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Modelet manufacturing-environments/discover-behavior-specifications](https://github.com/HyperAgents/hmas/blob/HEAD/domains/manufacturing-environments/discover-behavior-specifications/onto.ttl)|

#### Criterion detail
|Identifier|[proper-extension-predicate](https://ns.inria.fr/olivaw#proper-extension-predicate)|
|----|----|
|Title|Predicate&#32;extension&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;test&#32;the&#32;proper&#32;use&#32;of&#32;predicates&#32;rdfs:subClassOf&#32;and&#32;rdfs:subPropertyOf&#32;on&#32;the&#32;ontology&#32;terms|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-113)|Identifier|`class-subpropertyof`|
|[Section top](#pass-outcome-number-113)|Title|No&#32;class&#32;subproperty|
|[Section top](#pass-outcome-number-113)|Description|No&#32;ontology&#32;class&#32;is&#32;a&#32;subproperty|

***
### Pass Outcome number 114

[Jump to summary definition](#summary-Pass-114)	|	[Previous Pass outcome](#pass-outcome-number-113)	|	[Next Pass outcome](#pass-outcome-number-115)

:white_check_mark:Pass outcome
#### Subject detail
|Name|modelet-manufacturing-environments-discover-behavior-specifications|
|----|----|
|Title|Standalone&#32;modelet&#32;domains&#92;manufacturing-environments&#92;discover-behavior-specifications&#92;onto.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Modelet manufacturing-environments/discover-behavior-specifications](https://github.com/HyperAgents/hmas/blob/HEAD/domains/manufacturing-environments/discover-behavior-specifications/onto.ttl)|

#### Criterion detail
|Identifier|[proper-extension-predicate](https://ns.inria.fr/olivaw#proper-extension-predicate)|
|----|----|
|Title|Predicate&#32;extension&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;test&#32;the&#32;proper&#32;use&#32;of&#32;predicates&#32;rdfs:subClassOf&#32;and&#32;rdfs:subPropertyOf&#32;on&#32;the&#32;ontology&#32;terms|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-114)|Identifier|`property-subclassof`|
|[Section top](#pass-outcome-number-114)|Title|No&#32;property&#32;subclass|
|[Section top](#pass-outcome-number-114)|Description|No&#32;ontology&#32;property&#32;is&#32;a&#32;subclass|

***
### Pass Outcome number 115

[Jump to summary definition](#summary-Pass-115)	|	[Previous Pass outcome](#pass-outcome-number-114)	|	[Next Pass outcome](#pass-outcome-number-116)

:white_check_mark:Pass outcome
#### Subject detail
|Name|modelet-manufacturing-environments-discover-behavior-specifications|
|----|----|
|Title|Standalone&#32;modelet&#32;domains&#92;manufacturing-environments&#92;discover-behavior-specifications&#92;onto.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Modelet manufacturing-environments/discover-behavior-specifications](https://github.com/HyperAgents/hmas/blob/HEAD/domains/manufacturing-environments/discover-behavior-specifications/onto.ttl)|

#### Criterion detail
|Identifier|[proper-extension-predicate](https://ns.inria.fr/olivaw#proper-extension-predicate)|
|----|----|
|Title|Predicate&#32;extension&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;test&#32;the&#32;proper&#32;use&#32;of&#32;predicates&#32;rdfs:subClassOf&#32;and&#32;rdfs:subPropertyOf&#32;on&#32;the&#32;ontology&#32;terms|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-115)|Identifier|`subclassof-property`|
|[Section top](#pass-outcome-number-115)|Title|No&#32;subclass&#32;of&#32;property|
|[Section top](#pass-outcome-number-115)|Description|No&#32;ontology&#32;term&#32;is&#32;a&#32;subclass&#32;of&#32;a&#32;property|

***
### Pass Outcome number 116

[Jump to summary definition](#summary-Pass-116)	|	[Previous Pass outcome](#pass-outcome-number-115)	|	[Next Pass outcome](#pass-outcome-number-117)

:white_check_mark:Pass outcome
#### Subject detail
|Name|modelet-manufacturing-environments-discover-behavior-specifications|
|----|----|
|Title|Standalone&#32;modelet&#32;domains&#92;manufacturing-environments&#92;discover-behavior-specifications&#92;onto.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Modelet manufacturing-environments/discover-behavior-specifications](https://github.com/HyperAgents/hmas/blob/HEAD/domains/manufacturing-environments/discover-behavior-specifications/onto.ttl)|

#### Criterion detail
|Identifier|[proper-extension-predicate](https://ns.inria.fr/olivaw#proper-extension-predicate)|
|----|----|
|Title|Predicate&#32;extension&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;test&#32;the&#32;proper&#32;use&#32;of&#32;predicates&#32;rdfs:subClassOf&#32;and&#32;rdfs:subPropertyOf&#32;on&#32;the&#32;ontology&#32;terms|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-116)|Identifier|`subpropertyof-class`|
|[Section top](#pass-outcome-number-116)|Title|No&#32;subproperty&#32;of&#32;class|
|[Section top](#pass-outcome-number-116)|Description|No&#32;ontology&#32;term&#32;is&#32;a&#32;subproperty&#32;of&#32;a&#32;class|

***
### Pass Outcome number 117

[Jump to summary definition](#summary-Pass-117)	|	[Previous Pass outcome](#pass-outcome-number-116)	|	[Next Pass outcome](#pass-outcome-number-118)

:white_check_mark:Pass outcome
#### Subject detail
|Name|modelet-manufacturing-environments-discover-behavior-specifications|
|----|----|
|Title|Standalone&#32;modelet&#32;domains&#92;manufacturing-environments&#92;discover-behavior-specifications&#92;onto.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Modelet manufacturing-environments/discover-behavior-specifications](https://github.com/HyperAgents/hmas/blob/HEAD/domains/manufacturing-environments/discover-behavior-specifications/onto.ttl)|

#### Criterion detail
|Identifier|[term-referencing](https://ns.inria.fr/olivaw#term-referencing)|
|----|----|
|Title|Term&#32;referencing&#32;test|
|Description|A&#32;test&#32;case&#32;from&#32;the&#32;Best&#32;Practices&#32;tests&#32;checking&#32;if&#32;each&#32;term&#32;of&#32;the&#32;test&#32;subject&#32;is&#32;referenced&#32;to&#32;a&#32;module&#32;through&#32;a&#32;rdfs:isDefinedBy&#32;property.|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-117)|Identifier|`no-reference-module`|
|[Section top](#pass-outcome-number-117)|Title|Any&#32;term&#32;is&#32;referenced|
|[Section top](#pass-outcome-number-117)|Description|Each&#32;term&#32;of&#32;the&#32;test&#32;subject&#32;is&#32;linked&#32;to&#32;a&#32;module&#32;by&#32;a&#32;rdfs:isDefinedBy&#32;property|

***
### Pass Outcome number 118

[Jump to summary definition](#summary-Pass-118)	|	[Previous Pass outcome](#pass-outcome-number-117)	|	[Next Pass outcome](#pass-outcome-number-119)

:white_check_mark:Pass outcome
#### Subject detail
|Name|modelet-manufacturing-environments-discover-behavior-specifications|
|----|----|
|Title|Standalone&#32;modelet&#32;domains&#92;manufacturing-environments&#92;discover-behavior-specifications&#92;onto.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Modelet manufacturing-environments/discover-behavior-specifications](https://github.com/HyperAgents/hmas/blob/HEAD/domains/manufacturing-environments/discover-behavior-specifications/onto.ttl)|

#### Criterion detail
|Identifier|[terms-differenciation](https://ns.inria.fr/olivaw#terms-differenciation)|
|----|----|
|Title|Terms&#32;differenciation&#32;test|
|Description|A&#32;test&#32;case&#32;from&#32;the&#32;Best&#32;Practices&#32;tests&#32;checking&#32;if&#32;all&#32;the&#32;terms&#32;are&#32;different&#32;enough&#32;from&#32;each&#32;other&#32;according&#32;to&#32;the&#32;Levenshtein&#32;distance&#32;metric.|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-118)|Identifier|`too-close-terms`|
|[Section top](#pass-outcome-number-118)|Title|Terms&#32;differenciated&#32;enough|
|[Section top](#pass-outcome-number-118)|Description|All&#32;the&#32;terms&#32;have&#32;have&#32;a&#32;satisfying&#32;Levenshtein&#32;distance&#32;from&#32;each&#32;other&#32;term.|

***
### Pass Outcome number 119

[Jump to summary definition](#summary-Pass-119)	|	[Previous Pass outcome](#pass-outcome-number-118)	|	[Next Pass outcome](#pass-outcome-number-120)

:white_check_mark:Pass outcome
#### Subject detail
|Name|modelet-logistics-create-organization|
|----|----|
|Title|Standalone&#32;modelet&#32;domains&#92;logistics&#92;create-organization&#92;onto.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Modelet logistics/create-organization](https://github.com/HyperAgents/hmas/blob/HEAD/domains/logistics/create-organization/onto.ttl)|

#### Criterion detail
|Identifier|[domain-and-range-referencing](https://ns.inria.fr/olivaw#domain-and-range-referencing)|
|----|----|
|Title|Domain&#32;and&#32;range&#32;referencing&#32;test|
|Description|A&#32;test&#32;case&#32;from&#32;the&#32;Best&#32;Practices&#32;tests&#32;checking&#32;if&#32;all&#32;the&#32;ranges&#32;and&#32;domains&#32;from&#32;the&#32;test&#32;subject&#32;point&#32;to&#32;terms&#32;that&#32;are&#32;defined&#32;in&#32;the&#32;vocabulary.|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-119)|Identifier|`domain-out-of-vocabulary`|
|[Section top](#pass-outcome-number-119)|Title|Domains&#32;properly&#32;defined|
|[Section top](#pass-outcome-number-119)|Description|Each&#32;rdfs:domain&#32;is&#32;defined&#32;within&#32;the&#32;fragment|

***
### Pass Outcome number 120

[Jump to summary definition](#summary-Pass-120)	|	[Previous Pass outcome](#pass-outcome-number-119)	|	[Next Pass outcome](#pass-outcome-number-121)

:white_check_mark:Pass outcome
#### Subject detail
|Name|modelet-logistics-create-organization|
|----|----|
|Title|Standalone&#32;modelet&#32;domains&#92;logistics&#92;create-organization&#92;onto.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Modelet logistics/create-organization](https://github.com/HyperAgents/hmas/blob/HEAD/domains/logistics/create-organization/onto.ttl)|

#### Criterion detail
|Identifier|[domain-and-range-referencing](https://ns.inria.fr/olivaw#domain-and-range-referencing)|
|----|----|
|Title|Domain&#32;and&#32;range&#32;referencing&#32;test|
|Description|A&#32;test&#32;case&#32;from&#32;the&#32;Best&#32;Practices&#32;tests&#32;checking&#32;if&#32;all&#32;the&#32;ranges&#32;and&#32;domains&#32;from&#32;the&#32;test&#32;subject&#32;point&#32;to&#32;terms&#32;that&#32;are&#32;defined&#32;in&#32;the&#32;vocabulary.|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-120)|Identifier|`range-out-of-vocabulary`|
|[Section top](#pass-outcome-number-120)|Title|Ranges&#32;properly&#32;defined|
|[Section top](#pass-outcome-number-120)|Description|Each&#32;rdfs:range&#32;is&#32;defined&#32;within&#32;the&#32;fragment|

***
### Pass Outcome number 121

[Jump to summary definition](#summary-Pass-121)	|	[Previous Pass outcome](#pass-outcome-number-120)	|	[Next Pass outcome](#pass-outcome-number-122)

:white_check_mark:Pass outcome
#### Subject detail
|Name|modelet-logistics-create-organization|
|----|----|
|Title|Standalone&#32;modelet&#32;domains&#92;logistics&#92;create-organization&#92;onto.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Modelet logistics/create-organization](https://github.com/HyperAgents/hmas/blob/HEAD/domains/logistics/create-organization/onto.ttl)|

#### Criterion detail
|Identifier|[labeled-terms](https://ns.inria.fr/olivaw#labeled-terms)|
|----|----|
|Title|Term&#32;labeling&#32;test|
|Description|A&#32;test&#32;case&#32;from&#32;the&#32;Best&#32;Practices&#32;tests&#32;checking&#32;if&#32;all&#32;the&#32;terms&#32;of&#32;the&#32;subject&#32;have&#32;a&#32;rdfs:label&#32;property&#32;pointing&#32;to&#32;a&#32;literal&#32;in&#32;English|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-121)|Identifier|`not-labeled-term`|
|[Section top](#pass-outcome-number-121)|Title|All&#32;terms&#32;labeled|
|[Section top](#pass-outcome-number-121)|Description|All&#32;the&#32;terms&#32;defined&#32;in&#32;the&#32;subject&#32;have&#32;a&#32;rdfs:label&#32;in&#32;English|

***
### Pass Outcome number 122

[Jump to summary definition](#summary-Pass-122)	|	[Previous Pass outcome](#pass-outcome-number-121)	|	[Next Pass outcome](#pass-outcome-number-123)

:white_check_mark:Pass outcome
#### Subject detail
|Name|modelet-logistics-create-organization|
|----|----|
|Title|Standalone&#32;modelet&#32;domains&#92;logistics&#92;create-organization&#92;onto.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Modelet logistics/create-organization](https://github.com/HyperAgents/hmas/blob/HEAD/domains/logistics/create-organization/onto.ttl)|

#### Criterion detail
|Identifier|[owl-rl-constraint](https://ns.inria.fr/olivaw#owl-rl-constraint)|
|----|----|
|Title|OWL&#32;RL&#32;Constraint&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;check&#32;wether&#32;the&#32;test&#32;subject&#32;is&#32;syntaxically&#32;correct&#32;or&#32;not.|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-122)|Identifier|`owl-rl-constraint-violation`|
|[Section top](#pass-outcome-number-122)|Title|OWL&#32;RL&#32;consistent|
|[Section top](#pass-outcome-number-122)|Description|The&#32;provided&#32;graph&#32;is&#32;consistent&#32;for&#32;any&#32;OWL&#32;RL&#32;constraint|

***
### Pass Outcome number 123

[Jump to summary definition](#summary-Pass-123)	|	[Previous Pass outcome](#pass-outcome-number-122)	|	[Next Pass outcome](#pass-outcome-number-124)

:white_check_mark:Pass outcome
#### Subject detail
|Name|modelet-logistics-create-organization|
|----|----|
|Title|Standalone&#32;modelet&#32;domains&#92;logistics&#92;create-organization&#92;onto.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Modelet logistics/create-organization](https://github.com/HyperAgents/hmas/blob/HEAD/domains/logistics/create-organization/onto.ttl)|

#### Criterion detail
|Identifier|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|
|----|----|
|Title|Profile&#32;compatibility&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;check&#32;whether&#32;the&#32;test&#32;subject&#32;is&#32;compatible&#32;with&#32;a&#32;profile&#32;or&#32;not,&#32;and&#32;if&#32;it&#32;is&#32;not,&#32;why.|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-123)|Identifier|`owl-el-profile-error`|
|[Section top](#pass-outcome-number-123)|Title|OWL&#32;EL&#32;Profile&#32;compatible|
|[Section top](#pass-outcome-number-123)|Description|The&#32;subject&#32;is&#32;included&#32;in&#32;the&#32;OWL&#32;EL&#32;sublanguage|

***
### Pass Outcome number 124

[Jump to summary definition](#summary-Pass-124)	|	[Previous Pass outcome](#pass-outcome-number-123)	|	[Next Pass outcome](#pass-outcome-number-125)

:white_check_mark:Pass outcome
#### Subject detail
|Name|modelet-logistics-create-organization|
|----|----|
|Title|Standalone&#32;modelet&#32;domains&#92;logistics&#92;create-organization&#92;onto.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Modelet logistics/create-organization](https://github.com/HyperAgents/hmas/blob/HEAD/domains/logistics/create-organization/onto.ttl)|

#### Criterion detail
|Identifier|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|
|----|----|
|Title|Profile&#32;compatibility&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;check&#32;whether&#32;the&#32;test&#32;subject&#32;is&#32;compatible&#32;with&#32;a&#32;profile&#32;or&#32;not,&#32;and&#32;if&#32;it&#32;is&#32;not,&#32;why.|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-124)|Identifier|`owl-ql-profile-error`|
|[Section top](#pass-outcome-number-124)|Title|OWL&#32;QL&#32;Profile&#32;compatible|
|[Section top](#pass-outcome-number-124)|Description|The&#32;subject&#32;is&#32;included&#32;in&#32;the&#32;OWL&#32;QL&#32;sublanguage|

***
### Pass Outcome number 125

[Jump to summary definition](#summary-Pass-125)	|	[Previous Pass outcome](#pass-outcome-number-124)	|	[Next Pass outcome](#pass-outcome-number-126)

:white_check_mark:Pass outcome
#### Subject detail
|Name|modelet-logistics-create-organization|
|----|----|
|Title|Standalone&#32;modelet&#32;domains&#92;logistics&#92;create-organization&#92;onto.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Modelet logistics/create-organization](https://github.com/HyperAgents/hmas/blob/HEAD/domains/logistics/create-organization/onto.ttl)|

#### Criterion detail
|Identifier|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|
|----|----|
|Title|Profile&#32;compatibility&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;check&#32;whether&#32;the&#32;test&#32;subject&#32;is&#32;compatible&#32;with&#32;a&#32;profile&#32;or&#32;not,&#32;and&#32;if&#32;it&#32;is&#32;not,&#32;why.|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-125)|Identifier|`owl-rl-profile-error`|
|[Section top](#pass-outcome-number-125)|Title|OWL&#32;RL&#32;Profile&#32;compatible|
|[Section top](#pass-outcome-number-125)|Description|The&#32;subject&#32;is&#32;included&#32;in&#32;the&#32;OWL&#32;RL&#32;sublanguage|

***
### Pass Outcome number 126

[Jump to summary definition](#summary-Pass-126)	|	[Previous Pass outcome](#pass-outcome-number-125)	|	[Next Pass outcome](#pass-outcome-number-127)

:white_check_mark:Pass outcome
#### Subject detail
|Name|modelet-logistics-create-organization|
|----|----|
|Title|Standalone&#32;modelet&#32;domains&#92;logistics&#92;create-organization&#92;onto.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Modelet logistics/create-organization](https://github.com/HyperAgents/hmas/blob/HEAD/domains/logistics/create-organization/onto.ttl)|

#### Criterion detail
|Identifier|[proper-extension-predicate](https://ns.inria.fr/olivaw#proper-extension-predicate)|
|----|----|
|Title|Predicate&#32;extension&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;test&#32;the&#32;proper&#32;use&#32;of&#32;predicates&#32;rdfs:subClassOf&#32;and&#32;rdfs:subPropertyOf&#32;on&#32;the&#32;ontology&#32;terms|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-126)|Identifier|`class-subpropertyof`|
|[Section top](#pass-outcome-number-126)|Title|No&#32;class&#32;subproperty|
|[Section top](#pass-outcome-number-126)|Description|No&#32;ontology&#32;class&#32;is&#32;a&#32;subproperty|

***
### Pass Outcome number 127

[Jump to summary definition](#summary-Pass-127)	|	[Previous Pass outcome](#pass-outcome-number-126)	|	[Next Pass outcome](#pass-outcome-number-128)

:white_check_mark:Pass outcome
#### Subject detail
|Name|modelet-logistics-create-organization|
|----|----|
|Title|Standalone&#32;modelet&#32;domains&#92;logistics&#92;create-organization&#92;onto.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Modelet logistics/create-organization](https://github.com/HyperAgents/hmas/blob/HEAD/domains/logistics/create-organization/onto.ttl)|

#### Criterion detail
|Identifier|[proper-extension-predicate](https://ns.inria.fr/olivaw#proper-extension-predicate)|
|----|----|
|Title|Predicate&#32;extension&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;test&#32;the&#32;proper&#32;use&#32;of&#32;predicates&#32;rdfs:subClassOf&#32;and&#32;rdfs:subPropertyOf&#32;on&#32;the&#32;ontology&#32;terms|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-127)|Identifier|`property-subclassof`|
|[Section top](#pass-outcome-number-127)|Title|No&#32;property&#32;subclass|
|[Section top](#pass-outcome-number-127)|Description|No&#32;ontology&#32;property&#32;is&#32;a&#32;subclass|

***
### Pass Outcome number 128

[Jump to summary definition](#summary-Pass-128)	|	[Previous Pass outcome](#pass-outcome-number-127)	|	[Next Pass outcome](#pass-outcome-number-129)

:white_check_mark:Pass outcome
#### Subject detail
|Name|modelet-logistics-create-organization|
|----|----|
|Title|Standalone&#32;modelet&#32;domains&#92;logistics&#92;create-organization&#92;onto.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Modelet logistics/create-organization](https://github.com/HyperAgents/hmas/blob/HEAD/domains/logistics/create-organization/onto.ttl)|

#### Criterion detail
|Identifier|[proper-extension-predicate](https://ns.inria.fr/olivaw#proper-extension-predicate)|
|----|----|
|Title|Predicate&#32;extension&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;test&#32;the&#32;proper&#32;use&#32;of&#32;predicates&#32;rdfs:subClassOf&#32;and&#32;rdfs:subPropertyOf&#32;on&#32;the&#32;ontology&#32;terms|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-128)|Identifier|`subclassof-property`|
|[Section top](#pass-outcome-number-128)|Title|No&#32;subclass&#32;of&#32;property|
|[Section top](#pass-outcome-number-128)|Description|No&#32;ontology&#32;term&#32;is&#32;a&#32;subclass&#32;of&#32;a&#32;property|

***
### Pass Outcome number 129

[Jump to summary definition](#summary-Pass-129)	|	[Previous Pass outcome](#pass-outcome-number-128)	|	[Next Pass outcome](#pass-outcome-number-130)

:white_check_mark:Pass outcome
#### Subject detail
|Name|modelet-logistics-create-organization|
|----|----|
|Title|Standalone&#32;modelet&#32;domains&#92;logistics&#92;create-organization&#92;onto.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Modelet logistics/create-organization](https://github.com/HyperAgents/hmas/blob/HEAD/domains/logistics/create-organization/onto.ttl)|

#### Criterion detail
|Identifier|[proper-extension-predicate](https://ns.inria.fr/olivaw#proper-extension-predicate)|
|----|----|
|Title|Predicate&#32;extension&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;test&#32;the&#32;proper&#32;use&#32;of&#32;predicates&#32;rdfs:subClassOf&#32;and&#32;rdfs:subPropertyOf&#32;on&#32;the&#32;ontology&#32;terms|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-129)|Identifier|`subpropertyof-class`|
|[Section top](#pass-outcome-number-129)|Title|No&#32;subproperty&#32;of&#32;class|
|[Section top](#pass-outcome-number-129)|Description|No&#32;ontology&#32;term&#32;is&#32;a&#32;subproperty&#32;of&#32;a&#32;class|

***
### Pass Outcome number 130

[Jump to summary definition](#summary-Pass-130)	|	[Previous Pass outcome](#pass-outcome-number-129)	|	[Next Pass outcome](#pass-outcome-number-131)

:white_check_mark:Pass outcome
#### Subject detail
|Name|modelet-logistics-create-organization|
|----|----|
|Title|Standalone&#32;modelet&#32;domains&#92;logistics&#92;create-organization&#92;onto.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Modelet logistics/create-organization](https://github.com/HyperAgents/hmas/blob/HEAD/domains/logistics/create-organization/onto.ttl)|

#### Criterion detail
|Identifier|[term-referencing](https://ns.inria.fr/olivaw#term-referencing)|
|----|----|
|Title|Term&#32;referencing&#32;test|
|Description|A&#32;test&#32;case&#32;from&#32;the&#32;Best&#32;Practices&#32;tests&#32;checking&#32;if&#32;each&#32;term&#32;of&#32;the&#32;test&#32;subject&#32;is&#32;referenced&#32;to&#32;a&#32;module&#32;through&#32;a&#32;rdfs:isDefinedBy&#32;property.|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-130)|Identifier|`no-reference-module`|
|[Section top](#pass-outcome-number-130)|Title|Any&#32;term&#32;is&#32;referenced|
|[Section top](#pass-outcome-number-130)|Description|Each&#32;term&#32;of&#32;the&#32;test&#32;subject&#32;is&#32;linked&#32;to&#32;a&#32;module&#32;by&#32;a&#32;rdfs:isDefinedBy&#32;property|

***
### Pass Outcome number 131

[Jump to summary definition](#summary-Pass-131)	|	[Previous Pass outcome](#pass-outcome-number-130)	|	[Next Pass outcome](#pass-outcome-number-132)

:white_check_mark:Pass outcome
#### Subject detail
|Name|modelet-logistics-create-organization|
|----|----|
|Title|Standalone&#32;modelet&#32;domains&#92;logistics&#92;create-organization&#92;onto.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Modelet logistics/create-organization](https://github.com/HyperAgents/hmas/blob/HEAD/domains/logistics/create-organization/onto.ttl)|

#### Criterion detail
|Identifier|[terms-differenciation](https://ns.inria.fr/olivaw#terms-differenciation)|
|----|----|
|Title|Terms&#32;differenciation&#32;test|
|Description|A&#32;test&#32;case&#32;from&#32;the&#32;Best&#32;Practices&#32;tests&#32;checking&#32;if&#32;all&#32;the&#32;terms&#32;are&#32;different&#32;enough&#32;from&#32;each&#32;other&#32;according&#32;to&#32;the&#32;Levenshtein&#32;distance&#32;metric.|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-131)|Identifier|`too-close-terms`|
|[Section top](#pass-outcome-number-131)|Title|Terms&#32;differenciated&#32;enough|
|[Section top](#pass-outcome-number-131)|Description|All&#32;the&#32;terms&#32;have&#32;have&#32;a&#32;satisfying&#32;Levenshtein&#32;distance&#32;from&#32;each&#32;other&#32;term.|

***
### Pass Outcome number 132

[Jump to summary definition](#summary-Pass-132)	|	[Previous Pass outcome](#pass-outcome-number-131)	|	[Next Pass outcome](#pass-outcome-number-133)

:white_check_mark:Pass outcome
#### Subject detail
|Name|modelet-logistics-coordinate-activities|
|----|----|
|Title|Standalone&#32;modelet&#32;domains&#92;logistics&#92;coordinate-activities&#92;onto.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Modelet logistics/coordinate-activities](https://github.com/HyperAgents/hmas/blob/HEAD/domains/logistics/coordinate-activities/onto.ttl)|

#### Criterion detail
|Identifier|[domain-and-range-referencing](https://ns.inria.fr/olivaw#domain-and-range-referencing)|
|----|----|
|Title|Domain&#32;and&#32;range&#32;referencing&#32;test|
|Description|A&#32;test&#32;case&#32;from&#32;the&#32;Best&#32;Practices&#32;tests&#32;checking&#32;if&#32;all&#32;the&#32;ranges&#32;and&#32;domains&#32;from&#32;the&#32;test&#32;subject&#32;point&#32;to&#32;terms&#32;that&#32;are&#32;defined&#32;in&#32;the&#32;vocabulary.|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-132)|Identifier|`domain-out-of-vocabulary`|
|[Section top](#pass-outcome-number-132)|Title|Domains&#32;properly&#32;defined|
|[Section top](#pass-outcome-number-132)|Description|Each&#32;rdfs:domain&#32;is&#32;defined&#32;within&#32;the&#32;fragment|

***
### Pass Outcome number 133

[Jump to summary definition](#summary-Pass-133)	|	[Previous Pass outcome](#pass-outcome-number-132)	|	[Next Pass outcome](#pass-outcome-number-134)

:white_check_mark:Pass outcome
#### Subject detail
|Name|modelet-logistics-coordinate-activities|
|----|----|
|Title|Standalone&#32;modelet&#32;domains&#92;logistics&#92;coordinate-activities&#92;onto.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Modelet logistics/coordinate-activities](https://github.com/HyperAgents/hmas/blob/HEAD/domains/logistics/coordinate-activities/onto.ttl)|

#### Criterion detail
|Identifier|[domain-and-range-referencing](https://ns.inria.fr/olivaw#domain-and-range-referencing)|
|----|----|
|Title|Domain&#32;and&#32;range&#32;referencing&#32;test|
|Description|A&#32;test&#32;case&#32;from&#32;the&#32;Best&#32;Practices&#32;tests&#32;checking&#32;if&#32;all&#32;the&#32;ranges&#32;and&#32;domains&#32;from&#32;the&#32;test&#32;subject&#32;point&#32;to&#32;terms&#32;that&#32;are&#32;defined&#32;in&#32;the&#32;vocabulary.|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-133)|Identifier|`range-out-of-vocabulary`|
|[Section top](#pass-outcome-number-133)|Title|Ranges&#32;properly&#32;defined|
|[Section top](#pass-outcome-number-133)|Description|Each&#32;rdfs:range&#32;is&#32;defined&#32;within&#32;the&#32;fragment|

***
### Pass Outcome number 134

[Jump to summary definition](#summary-Pass-134)	|	[Previous Pass outcome](#pass-outcome-number-133)	|	[Next Pass outcome](#pass-outcome-number-135)

:white_check_mark:Pass outcome
#### Subject detail
|Name|modelet-logistics-coordinate-activities|
|----|----|
|Title|Standalone&#32;modelet&#32;domains&#92;logistics&#92;coordinate-activities&#92;onto.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Modelet logistics/coordinate-activities](https://github.com/HyperAgents/hmas/blob/HEAD/domains/logistics/coordinate-activities/onto.ttl)|

#### Criterion detail
|Identifier|[labeled-terms](https://ns.inria.fr/olivaw#labeled-terms)|
|----|----|
|Title|Term&#32;labeling&#32;test|
|Description|A&#32;test&#32;case&#32;from&#32;the&#32;Best&#32;Practices&#32;tests&#32;checking&#32;if&#32;all&#32;the&#32;terms&#32;of&#32;the&#32;subject&#32;have&#32;a&#32;rdfs:label&#32;property&#32;pointing&#32;to&#32;a&#32;literal&#32;in&#32;English|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-134)|Identifier|`not-labeled-term`|
|[Section top](#pass-outcome-number-134)|Title|All&#32;terms&#32;labeled|
|[Section top](#pass-outcome-number-134)|Description|All&#32;the&#32;terms&#32;defined&#32;in&#32;the&#32;subject&#32;have&#32;a&#32;rdfs:label&#32;in&#32;English|

***
### Pass Outcome number 135

[Jump to summary definition](#summary-Pass-135)	|	[Previous Pass outcome](#pass-outcome-number-134)	|	[Next Pass outcome](#pass-outcome-number-136)

:white_check_mark:Pass outcome
#### Subject detail
|Name|modelet-logistics-coordinate-activities|
|----|----|
|Title|Standalone&#32;modelet&#32;domains&#92;logistics&#92;coordinate-activities&#92;onto.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Modelet logistics/coordinate-activities](https://github.com/HyperAgents/hmas/blob/HEAD/domains/logistics/coordinate-activities/onto.ttl)|

#### Criterion detail
|Identifier|[owl-rl-constraint](https://ns.inria.fr/olivaw#owl-rl-constraint)|
|----|----|
|Title|OWL&#32;RL&#32;Constraint&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;check&#32;wether&#32;the&#32;test&#32;subject&#32;is&#32;syntaxically&#32;correct&#32;or&#32;not.|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-135)|Identifier|`owl-rl-constraint-violation`|
|[Section top](#pass-outcome-number-135)|Title|OWL&#32;RL&#32;consistent|
|[Section top](#pass-outcome-number-135)|Description|The&#32;provided&#32;graph&#32;is&#32;consistent&#32;for&#32;any&#32;OWL&#32;RL&#32;constraint|

***
### Pass Outcome number 136

[Jump to summary definition](#summary-Pass-136)	|	[Previous Pass outcome](#pass-outcome-number-135)	|	[Next Pass outcome](#pass-outcome-number-137)

:white_check_mark:Pass outcome
#### Subject detail
|Name|modelet-logistics-coordinate-activities|
|----|----|
|Title|Standalone&#32;modelet&#32;domains&#92;logistics&#92;coordinate-activities&#92;onto.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Modelet logistics/coordinate-activities](https://github.com/HyperAgents/hmas/blob/HEAD/domains/logistics/coordinate-activities/onto.ttl)|

#### Criterion detail
|Identifier|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|
|----|----|
|Title|Profile&#32;compatibility&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;check&#32;whether&#32;the&#32;test&#32;subject&#32;is&#32;compatible&#32;with&#32;a&#32;profile&#32;or&#32;not,&#32;and&#32;if&#32;it&#32;is&#32;not,&#32;why.|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-136)|Identifier|`owl-el-profile-error`|
|[Section top](#pass-outcome-number-136)|Title|OWL&#32;EL&#32;Profile&#32;compatible|
|[Section top](#pass-outcome-number-136)|Description|The&#32;subject&#32;is&#32;included&#32;in&#32;the&#32;OWL&#32;EL&#32;sublanguage|

***
### Pass Outcome number 137

[Jump to summary definition](#summary-Pass-137)	|	[Previous Pass outcome](#pass-outcome-number-136)	|	[Next Pass outcome](#pass-outcome-number-138)

:white_check_mark:Pass outcome
#### Subject detail
|Name|modelet-logistics-coordinate-activities|
|----|----|
|Title|Standalone&#32;modelet&#32;domains&#92;logistics&#92;coordinate-activities&#92;onto.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Modelet logistics/coordinate-activities](https://github.com/HyperAgents/hmas/blob/HEAD/domains/logistics/coordinate-activities/onto.ttl)|

#### Criterion detail
|Identifier|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|
|----|----|
|Title|Profile&#32;compatibility&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;check&#32;whether&#32;the&#32;test&#32;subject&#32;is&#32;compatible&#32;with&#32;a&#32;profile&#32;or&#32;not,&#32;and&#32;if&#32;it&#32;is&#32;not,&#32;why.|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-137)|Identifier|`owl-ql-profile-error`|
|[Section top](#pass-outcome-number-137)|Title|OWL&#32;QL&#32;Profile&#32;compatible|
|[Section top](#pass-outcome-number-137)|Description|The&#32;subject&#32;is&#32;included&#32;in&#32;the&#32;OWL&#32;QL&#32;sublanguage|

***
### Pass Outcome number 138

[Jump to summary definition](#summary-Pass-138)	|	[Previous Pass outcome](#pass-outcome-number-137)	|	[Next Pass outcome](#pass-outcome-number-139)

:white_check_mark:Pass outcome
#### Subject detail
|Name|modelet-logistics-coordinate-activities|
|----|----|
|Title|Standalone&#32;modelet&#32;domains&#92;logistics&#92;coordinate-activities&#92;onto.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Modelet logistics/coordinate-activities](https://github.com/HyperAgents/hmas/blob/HEAD/domains/logistics/coordinate-activities/onto.ttl)|

#### Criterion detail
|Identifier|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|
|----|----|
|Title|Profile&#32;compatibility&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;check&#32;whether&#32;the&#32;test&#32;subject&#32;is&#32;compatible&#32;with&#32;a&#32;profile&#32;or&#32;not,&#32;and&#32;if&#32;it&#32;is&#32;not,&#32;why.|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-138)|Identifier|`owl-rl-profile-error`|
|[Section top](#pass-outcome-number-138)|Title|OWL&#32;RL&#32;Profile&#32;compatible|
|[Section top](#pass-outcome-number-138)|Description|The&#32;subject&#32;is&#32;included&#32;in&#32;the&#32;OWL&#32;RL&#32;sublanguage|

***
### Pass Outcome number 139

[Jump to summary definition](#summary-Pass-139)	|	[Previous Pass outcome](#pass-outcome-number-138)	|	[Next Pass outcome](#pass-outcome-number-140)

:white_check_mark:Pass outcome
#### Subject detail
|Name|modelet-logistics-coordinate-activities|
|----|----|
|Title|Standalone&#32;modelet&#32;domains&#92;logistics&#92;coordinate-activities&#92;onto.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Modelet logistics/coordinate-activities](https://github.com/HyperAgents/hmas/blob/HEAD/domains/logistics/coordinate-activities/onto.ttl)|

#### Criterion detail
|Identifier|[proper-extension-predicate](https://ns.inria.fr/olivaw#proper-extension-predicate)|
|----|----|
|Title|Predicate&#32;extension&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;test&#32;the&#32;proper&#32;use&#32;of&#32;predicates&#32;rdfs:subClassOf&#32;and&#32;rdfs:subPropertyOf&#32;on&#32;the&#32;ontology&#32;terms|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-139)|Identifier|`class-subpropertyof`|
|[Section top](#pass-outcome-number-139)|Title|No&#32;class&#32;subproperty|
|[Section top](#pass-outcome-number-139)|Description|No&#32;ontology&#32;class&#32;is&#32;a&#32;subproperty|

***
### Pass Outcome number 140

[Jump to summary definition](#summary-Pass-140)	|	[Previous Pass outcome](#pass-outcome-number-139)	|	[Next Pass outcome](#pass-outcome-number-141)

:white_check_mark:Pass outcome
#### Subject detail
|Name|modelet-logistics-coordinate-activities|
|----|----|
|Title|Standalone&#32;modelet&#32;domains&#92;logistics&#92;coordinate-activities&#92;onto.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Modelet logistics/coordinate-activities](https://github.com/HyperAgents/hmas/blob/HEAD/domains/logistics/coordinate-activities/onto.ttl)|

#### Criterion detail
|Identifier|[proper-extension-predicate](https://ns.inria.fr/olivaw#proper-extension-predicate)|
|----|----|
|Title|Predicate&#32;extension&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;test&#32;the&#32;proper&#32;use&#32;of&#32;predicates&#32;rdfs:subClassOf&#32;and&#32;rdfs:subPropertyOf&#32;on&#32;the&#32;ontology&#32;terms|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-140)|Identifier|`property-subclassof`|
|[Section top](#pass-outcome-number-140)|Title|No&#32;property&#32;subclass|
|[Section top](#pass-outcome-number-140)|Description|No&#32;ontology&#32;property&#32;is&#32;a&#32;subclass|

***
### Pass Outcome number 141

[Jump to summary definition](#summary-Pass-141)	|	[Previous Pass outcome](#pass-outcome-number-140)	|	[Next Pass outcome](#pass-outcome-number-142)

:white_check_mark:Pass outcome
#### Subject detail
|Name|modelet-logistics-coordinate-activities|
|----|----|
|Title|Standalone&#32;modelet&#32;domains&#92;logistics&#92;coordinate-activities&#92;onto.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Modelet logistics/coordinate-activities](https://github.com/HyperAgents/hmas/blob/HEAD/domains/logistics/coordinate-activities/onto.ttl)|

#### Criterion detail
|Identifier|[proper-extension-predicate](https://ns.inria.fr/olivaw#proper-extension-predicate)|
|----|----|
|Title|Predicate&#32;extension&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;test&#32;the&#32;proper&#32;use&#32;of&#32;predicates&#32;rdfs:subClassOf&#32;and&#32;rdfs:subPropertyOf&#32;on&#32;the&#32;ontology&#32;terms|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-141)|Identifier|`subclassof-property`|
|[Section top](#pass-outcome-number-141)|Title|No&#32;subclass&#32;of&#32;property|
|[Section top](#pass-outcome-number-141)|Description|No&#32;ontology&#32;term&#32;is&#32;a&#32;subclass&#32;of&#32;a&#32;property|

***
### Pass Outcome number 142

[Jump to summary definition](#summary-Pass-142)	|	[Previous Pass outcome](#pass-outcome-number-141)	|	[Next Pass outcome](#pass-outcome-number-143)

:white_check_mark:Pass outcome
#### Subject detail
|Name|modelet-logistics-coordinate-activities|
|----|----|
|Title|Standalone&#32;modelet&#32;domains&#92;logistics&#92;coordinate-activities&#92;onto.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Modelet logistics/coordinate-activities](https://github.com/HyperAgents/hmas/blob/HEAD/domains/logistics/coordinate-activities/onto.ttl)|

#### Criterion detail
|Identifier|[proper-extension-predicate](https://ns.inria.fr/olivaw#proper-extension-predicate)|
|----|----|
|Title|Predicate&#32;extension&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;test&#32;the&#32;proper&#32;use&#32;of&#32;predicates&#32;rdfs:subClassOf&#32;and&#32;rdfs:subPropertyOf&#32;on&#32;the&#32;ontology&#32;terms|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-142)|Identifier|`subpropertyof-class`|
|[Section top](#pass-outcome-number-142)|Title|No&#32;subproperty&#32;of&#32;class|
|[Section top](#pass-outcome-number-142)|Description|No&#32;ontology&#32;term&#32;is&#32;a&#32;subproperty&#32;of&#32;a&#32;class|

***
### Pass Outcome number 143

[Jump to summary definition](#summary-Pass-143)	|	[Previous Pass outcome](#pass-outcome-number-142)	|	[Next Pass outcome](#pass-outcome-number-144)

:white_check_mark:Pass outcome
#### Subject detail
|Name|modelet-logistics-coordinate-activities|
|----|----|
|Title|Standalone&#32;modelet&#32;domains&#92;logistics&#92;coordinate-activities&#92;onto.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Modelet logistics/coordinate-activities](https://github.com/HyperAgents/hmas/blob/HEAD/domains/logistics/coordinate-activities/onto.ttl)|

#### Criterion detail
|Identifier|[term-referencing](https://ns.inria.fr/olivaw#term-referencing)|
|----|----|
|Title|Term&#32;referencing&#32;test|
|Description|A&#32;test&#32;case&#32;from&#32;the&#32;Best&#32;Practices&#32;tests&#32;checking&#32;if&#32;each&#32;term&#32;of&#32;the&#32;test&#32;subject&#32;is&#32;referenced&#32;to&#32;a&#32;module&#32;through&#32;a&#32;rdfs:isDefinedBy&#32;property.|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-143)|Identifier|`no-reference-module`|
|[Section top](#pass-outcome-number-143)|Title|Any&#32;term&#32;is&#32;referenced|
|[Section top](#pass-outcome-number-143)|Description|Each&#32;term&#32;of&#32;the&#32;test&#32;subject&#32;is&#32;linked&#32;to&#32;a&#32;module&#32;by&#32;a&#32;rdfs:isDefinedBy&#32;property|

***
### Pass Outcome number 144

[Jump to summary definition](#summary-Pass-144)	|	[Previous Pass outcome](#pass-outcome-number-143)	|	[Next Pass outcome](#pass-outcome-number-145)

:white_check_mark:Pass outcome
#### Subject detail
|Name|modelet-logistics-coordinate-activities|
|----|----|
|Title|Standalone&#32;modelet&#32;domains&#92;logistics&#92;coordinate-activities&#92;onto.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Modelet logistics/coordinate-activities](https://github.com/HyperAgents/hmas/blob/HEAD/domains/logistics/coordinate-activities/onto.ttl)|

#### Criterion detail
|Identifier|[terms-differenciation](https://ns.inria.fr/olivaw#terms-differenciation)|
|----|----|
|Title|Terms&#32;differenciation&#32;test|
|Description|A&#32;test&#32;case&#32;from&#32;the&#32;Best&#32;Practices&#32;tests&#32;checking&#32;if&#32;all&#32;the&#32;terms&#32;are&#32;different&#32;enough&#32;from&#32;each&#32;other&#32;according&#32;to&#32;the&#32;Levenshtein&#32;distance&#32;metric.|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-144)|Identifier|`too-close-terms`|
|[Section top](#pass-outcome-number-144)|Title|Terms&#32;differenciated&#32;enough|
|[Section top](#pass-outcome-number-144)|Description|All&#32;the&#32;terms&#32;have&#32;have&#32;a&#32;satisfying&#32;Levenshtein&#32;distance&#32;from&#32;each&#32;other&#32;term.|

***
### Pass Outcome number 145

[Jump to summary definition](#summary-Pass-145)	|	[Previous Pass outcome](#pass-outcome-number-144)	|	[Next Pass outcome](#pass-outcome-number-146)

:white_check_mark:Pass outcome
#### Subject detail
|Name|modelet-logistics-configure-organization|
|----|----|
|Title|Standalone&#32;modelet&#32;domains&#92;logistics&#92;configure-organization&#92;onto.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Modelet logistics/configure-organization](https://github.com/HyperAgents/hmas/blob/HEAD/domains/logistics/configure-organization/onto.ttl)|

#### Criterion detail
|Identifier|[domain-and-range-referencing](https://ns.inria.fr/olivaw#domain-and-range-referencing)|
|----|----|
|Title|Domain&#32;and&#32;range&#32;referencing&#32;test|
|Description|A&#32;test&#32;case&#32;from&#32;the&#32;Best&#32;Practices&#32;tests&#32;checking&#32;if&#32;all&#32;the&#32;ranges&#32;and&#32;domains&#32;from&#32;the&#32;test&#32;subject&#32;point&#32;to&#32;terms&#32;that&#32;are&#32;defined&#32;in&#32;the&#32;vocabulary.|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-145)|Identifier|`domain-out-of-vocabulary`|
|[Section top](#pass-outcome-number-145)|Title|Domains&#32;properly&#32;defined|
|[Section top](#pass-outcome-number-145)|Description|Each&#32;rdfs:domain&#32;is&#32;defined&#32;within&#32;the&#32;fragment|

***
### Pass Outcome number 146

[Jump to summary definition](#summary-Pass-146)	|	[Previous Pass outcome](#pass-outcome-number-145)	|	[Next Pass outcome](#pass-outcome-number-147)

:white_check_mark:Pass outcome
#### Subject detail
|Name|modelet-logistics-configure-organization|
|----|----|
|Title|Standalone&#32;modelet&#32;domains&#92;logistics&#92;configure-organization&#92;onto.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Modelet logistics/configure-organization](https://github.com/HyperAgents/hmas/blob/HEAD/domains/logistics/configure-organization/onto.ttl)|

#### Criterion detail
|Identifier|[domain-and-range-referencing](https://ns.inria.fr/olivaw#domain-and-range-referencing)|
|----|----|
|Title|Domain&#32;and&#32;range&#32;referencing&#32;test|
|Description|A&#32;test&#32;case&#32;from&#32;the&#32;Best&#32;Practices&#32;tests&#32;checking&#32;if&#32;all&#32;the&#32;ranges&#32;and&#32;domains&#32;from&#32;the&#32;test&#32;subject&#32;point&#32;to&#32;terms&#32;that&#32;are&#32;defined&#32;in&#32;the&#32;vocabulary.|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-146)|Identifier|`range-out-of-vocabulary`|
|[Section top](#pass-outcome-number-146)|Title|Ranges&#32;properly&#32;defined|
|[Section top](#pass-outcome-number-146)|Description|Each&#32;rdfs:range&#32;is&#32;defined&#32;within&#32;the&#32;fragment|

***
### Pass Outcome number 147

[Jump to summary definition](#summary-Pass-147)	|	[Previous Pass outcome](#pass-outcome-number-146)	|	[Next Pass outcome](#pass-outcome-number-148)

:white_check_mark:Pass outcome
#### Subject detail
|Name|modelet-logistics-configure-organization|
|----|----|
|Title|Standalone&#32;modelet&#32;domains&#92;logistics&#92;configure-organization&#92;onto.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Modelet logistics/configure-organization](https://github.com/HyperAgents/hmas/blob/HEAD/domains/logistics/configure-organization/onto.ttl)|

#### Criterion detail
|Identifier|[labeled-terms](https://ns.inria.fr/olivaw#labeled-terms)|
|----|----|
|Title|Term&#32;labeling&#32;test|
|Description|A&#32;test&#32;case&#32;from&#32;the&#32;Best&#32;Practices&#32;tests&#32;checking&#32;if&#32;all&#32;the&#32;terms&#32;of&#32;the&#32;subject&#32;have&#32;a&#32;rdfs:label&#32;property&#32;pointing&#32;to&#32;a&#32;literal&#32;in&#32;English|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-147)|Identifier|`not-labeled-term`|
|[Section top](#pass-outcome-number-147)|Title|All&#32;terms&#32;labeled|
|[Section top](#pass-outcome-number-147)|Description|All&#32;the&#32;terms&#32;defined&#32;in&#32;the&#32;subject&#32;have&#32;a&#32;rdfs:label&#32;in&#32;English|

***
### Pass Outcome number 148

[Jump to summary definition](#summary-Pass-148)	|	[Previous Pass outcome](#pass-outcome-number-147)	|	[Next Pass outcome](#pass-outcome-number-149)

:white_check_mark:Pass outcome
#### Subject detail
|Name|modelet-logistics-configure-organization|
|----|----|
|Title|Standalone&#32;modelet&#32;domains&#92;logistics&#92;configure-organization&#92;onto.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Modelet logistics/configure-organization](https://github.com/HyperAgents/hmas/blob/HEAD/domains/logistics/configure-organization/onto.ttl)|

#### Criterion detail
|Identifier|[owl-rl-constraint](https://ns.inria.fr/olivaw#owl-rl-constraint)|
|----|----|
|Title|OWL&#32;RL&#32;Constraint&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;check&#32;wether&#32;the&#32;test&#32;subject&#32;is&#32;syntaxically&#32;correct&#32;or&#32;not.|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-148)|Identifier|`owl-rl-constraint-violation`|
|[Section top](#pass-outcome-number-148)|Title|OWL&#32;RL&#32;consistent|
|[Section top](#pass-outcome-number-148)|Description|The&#32;provided&#32;graph&#32;is&#32;consistent&#32;for&#32;any&#32;OWL&#32;RL&#32;constraint|

***
### Pass Outcome number 149

[Jump to summary definition](#summary-Pass-149)	|	[Previous Pass outcome](#pass-outcome-number-148)	|	[Next Pass outcome](#pass-outcome-number-150)

:white_check_mark:Pass outcome
#### Subject detail
|Name|modelet-logistics-configure-organization|
|----|----|
|Title|Standalone&#32;modelet&#32;domains&#92;logistics&#92;configure-organization&#92;onto.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Modelet logistics/configure-organization](https://github.com/HyperAgents/hmas/blob/HEAD/domains/logistics/configure-organization/onto.ttl)|

#### Criterion detail
|Identifier|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|
|----|----|
|Title|Profile&#32;compatibility&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;check&#32;whether&#32;the&#32;test&#32;subject&#32;is&#32;compatible&#32;with&#32;a&#32;profile&#32;or&#32;not,&#32;and&#32;if&#32;it&#32;is&#32;not,&#32;why.|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-149)|Identifier|`owl-el-profile-error`|
|[Section top](#pass-outcome-number-149)|Title|OWL&#32;EL&#32;Profile&#32;compatible|
|[Section top](#pass-outcome-number-149)|Description|The&#32;subject&#32;is&#32;included&#32;in&#32;the&#32;OWL&#32;EL&#32;sublanguage|

***
### Pass Outcome number 150

[Jump to summary definition](#summary-Pass-150)	|	[Previous Pass outcome](#pass-outcome-number-149)	|	[Next Pass outcome](#pass-outcome-number-151)

:white_check_mark:Pass outcome
#### Subject detail
|Name|modelet-logistics-configure-organization|
|----|----|
|Title|Standalone&#32;modelet&#32;domains&#92;logistics&#92;configure-organization&#92;onto.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Modelet logistics/configure-organization](https://github.com/HyperAgents/hmas/blob/HEAD/domains/logistics/configure-organization/onto.ttl)|

#### Criterion detail
|Identifier|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|
|----|----|
|Title|Profile&#32;compatibility&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;check&#32;whether&#32;the&#32;test&#32;subject&#32;is&#32;compatible&#32;with&#32;a&#32;profile&#32;or&#32;not,&#32;and&#32;if&#32;it&#32;is&#32;not,&#32;why.|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-150)|Identifier|`owl-ql-profile-error`|
|[Section top](#pass-outcome-number-150)|Title|OWL&#32;QL&#32;Profile&#32;compatible|
|[Section top](#pass-outcome-number-150)|Description|The&#32;subject&#32;is&#32;included&#32;in&#32;the&#32;OWL&#32;QL&#32;sublanguage|

***
### Pass Outcome number 151

[Jump to summary definition](#summary-Pass-151)	|	[Previous Pass outcome](#pass-outcome-number-150)	|	[Next Pass outcome](#pass-outcome-number-152)

:white_check_mark:Pass outcome
#### Subject detail
|Name|modelet-logistics-configure-organization|
|----|----|
|Title|Standalone&#32;modelet&#32;domains&#92;logistics&#92;configure-organization&#92;onto.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Modelet logistics/configure-organization](https://github.com/HyperAgents/hmas/blob/HEAD/domains/logistics/configure-organization/onto.ttl)|

#### Criterion detail
|Identifier|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|
|----|----|
|Title|Profile&#32;compatibility&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;check&#32;whether&#32;the&#32;test&#32;subject&#32;is&#32;compatible&#32;with&#32;a&#32;profile&#32;or&#32;not,&#32;and&#32;if&#32;it&#32;is&#32;not,&#32;why.|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-151)|Identifier|`owl-rl-profile-error`|
|[Section top](#pass-outcome-number-151)|Title|OWL&#32;RL&#32;Profile&#32;compatible|
|[Section top](#pass-outcome-number-151)|Description|The&#32;subject&#32;is&#32;included&#32;in&#32;the&#32;OWL&#32;RL&#32;sublanguage|

***
### Pass Outcome number 152

[Jump to summary definition](#summary-Pass-152)	|	[Previous Pass outcome](#pass-outcome-number-151)	|	[Next Pass outcome](#pass-outcome-number-153)

:white_check_mark:Pass outcome
#### Subject detail
|Name|modelet-logistics-configure-organization|
|----|----|
|Title|Standalone&#32;modelet&#32;domains&#92;logistics&#92;configure-organization&#92;onto.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Modelet logistics/configure-organization](https://github.com/HyperAgents/hmas/blob/HEAD/domains/logistics/configure-organization/onto.ttl)|

#### Criterion detail
|Identifier|[proper-extension-predicate](https://ns.inria.fr/olivaw#proper-extension-predicate)|
|----|----|
|Title|Predicate&#32;extension&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;test&#32;the&#32;proper&#32;use&#32;of&#32;predicates&#32;rdfs:subClassOf&#32;and&#32;rdfs:subPropertyOf&#32;on&#32;the&#32;ontology&#32;terms|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-152)|Identifier|`class-subpropertyof`|
|[Section top](#pass-outcome-number-152)|Title|No&#32;class&#32;subproperty|
|[Section top](#pass-outcome-number-152)|Description|No&#32;ontology&#32;class&#32;is&#32;a&#32;subproperty|

***
### Pass Outcome number 153

[Jump to summary definition](#summary-Pass-153)	|	[Previous Pass outcome](#pass-outcome-number-152)	|	[Next Pass outcome](#pass-outcome-number-154)

:white_check_mark:Pass outcome
#### Subject detail
|Name|modelet-logistics-configure-organization|
|----|----|
|Title|Standalone&#32;modelet&#32;domains&#92;logistics&#92;configure-organization&#92;onto.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Modelet logistics/configure-organization](https://github.com/HyperAgents/hmas/blob/HEAD/domains/logistics/configure-organization/onto.ttl)|

#### Criterion detail
|Identifier|[proper-extension-predicate](https://ns.inria.fr/olivaw#proper-extension-predicate)|
|----|----|
|Title|Predicate&#32;extension&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;test&#32;the&#32;proper&#32;use&#32;of&#32;predicates&#32;rdfs:subClassOf&#32;and&#32;rdfs:subPropertyOf&#32;on&#32;the&#32;ontology&#32;terms|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-153)|Identifier|`property-subclassof`|
|[Section top](#pass-outcome-number-153)|Title|No&#32;property&#32;subclass|
|[Section top](#pass-outcome-number-153)|Description|No&#32;ontology&#32;property&#32;is&#32;a&#32;subclass|

***
### Pass Outcome number 154

[Jump to summary definition](#summary-Pass-154)	|	[Previous Pass outcome](#pass-outcome-number-153)	|	[Next Pass outcome](#pass-outcome-number-155)

:white_check_mark:Pass outcome
#### Subject detail
|Name|modelet-logistics-configure-organization|
|----|----|
|Title|Standalone&#32;modelet&#32;domains&#92;logistics&#92;configure-organization&#92;onto.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Modelet logistics/configure-organization](https://github.com/HyperAgents/hmas/blob/HEAD/domains/logistics/configure-organization/onto.ttl)|

#### Criterion detail
|Identifier|[proper-extension-predicate](https://ns.inria.fr/olivaw#proper-extension-predicate)|
|----|----|
|Title|Predicate&#32;extension&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;test&#32;the&#32;proper&#32;use&#32;of&#32;predicates&#32;rdfs:subClassOf&#32;and&#32;rdfs:subPropertyOf&#32;on&#32;the&#32;ontology&#32;terms|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-154)|Identifier|`subclassof-property`|
|[Section top](#pass-outcome-number-154)|Title|No&#32;subclass&#32;of&#32;property|
|[Section top](#pass-outcome-number-154)|Description|No&#32;ontology&#32;term&#32;is&#32;a&#32;subclass&#32;of&#32;a&#32;property|

***
### Pass Outcome number 155

[Jump to summary definition](#summary-Pass-155)	|	[Previous Pass outcome](#pass-outcome-number-154)	|	[Next Pass outcome](#pass-outcome-number-156)

:white_check_mark:Pass outcome
#### Subject detail
|Name|modelet-logistics-configure-organization|
|----|----|
|Title|Standalone&#32;modelet&#32;domains&#92;logistics&#92;configure-organization&#92;onto.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Modelet logistics/configure-organization](https://github.com/HyperAgents/hmas/blob/HEAD/domains/logistics/configure-organization/onto.ttl)|

#### Criterion detail
|Identifier|[proper-extension-predicate](https://ns.inria.fr/olivaw#proper-extension-predicate)|
|----|----|
|Title|Predicate&#32;extension&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;test&#32;the&#32;proper&#32;use&#32;of&#32;predicates&#32;rdfs:subClassOf&#32;and&#32;rdfs:subPropertyOf&#32;on&#32;the&#32;ontology&#32;terms|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-155)|Identifier|`subpropertyof-class`|
|[Section top](#pass-outcome-number-155)|Title|No&#32;subproperty&#32;of&#32;class|
|[Section top](#pass-outcome-number-155)|Description|No&#32;ontology&#32;term&#32;is&#32;a&#32;subproperty&#32;of&#32;a&#32;class|

***
### Pass Outcome number 156

[Jump to summary definition](#summary-Pass-156)	|	[Previous Pass outcome](#pass-outcome-number-155)	|	[Next Pass outcome](#pass-outcome-number-157)

:white_check_mark:Pass outcome
#### Subject detail
|Name|modelet-logistics-configure-organization|
|----|----|
|Title|Standalone&#32;modelet&#32;domains&#92;logistics&#92;configure-organization&#92;onto.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Modelet logistics/configure-organization](https://github.com/HyperAgents/hmas/blob/HEAD/domains/logistics/configure-organization/onto.ttl)|

#### Criterion detail
|Identifier|[term-referencing](https://ns.inria.fr/olivaw#term-referencing)|
|----|----|
|Title|Term&#32;referencing&#32;test|
|Description|A&#32;test&#32;case&#32;from&#32;the&#32;Best&#32;Practices&#32;tests&#32;checking&#32;if&#32;each&#32;term&#32;of&#32;the&#32;test&#32;subject&#32;is&#32;referenced&#32;to&#32;a&#32;module&#32;through&#32;a&#32;rdfs:isDefinedBy&#32;property.|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-156)|Identifier|`no-reference-module`|
|[Section top](#pass-outcome-number-156)|Title|Any&#32;term&#32;is&#32;referenced|
|[Section top](#pass-outcome-number-156)|Description|Each&#32;term&#32;of&#32;the&#32;test&#32;subject&#32;is&#32;linked&#32;to&#32;a&#32;module&#32;by&#32;a&#32;rdfs:isDefinedBy&#32;property|

***
### Pass Outcome number 157

[Jump to summary definition](#summary-Pass-157)	|	[Previous Pass outcome](#pass-outcome-number-156)	|	[Next Pass outcome](#pass-outcome-number-158)

:white_check_mark:Pass outcome
#### Subject detail
|Name|all-modules|
|----|----|
|Title|All&#32;the&#32;modules&#32;from&#32;branch&#32;HEAD&#32;that&#32;are&#32;syntaxically&#32;correct&#32;as&#32;well&#32;as&#32;their&#32;recursive&#32;imports|
|Composition|- [Module alignment/interaction-td](https://github.com/HyperAgents/hmas/blob/HEAD/src/alignment/interaction-td.ttl)<br/>- [Module core](https://github.com/HyperAgents/hmas/blob/HEAD/src/core.ttl)<br/>- [Module fipa](https://github.com/HyperAgents/hmas/blob/HEAD/src/fipa.ttl)<br/>- [Module interaction](https://github.com/HyperAgents/hmas/blob/HEAD/src/interaction.ttl)<br/>- [Module regulation](https://github.com/HyperAgents/hmas/blob/HEAD/src/regulation.ttl)|

#### Criterion detail
|Identifier|[domain-and-range-referencing](https://ns.inria.fr/olivaw#domain-and-range-referencing)|
|----|----|
|Title|Domain&#32;and&#32;range&#32;referencing&#32;test|
|Description|A&#32;test&#32;case&#32;from&#32;the&#32;Best&#32;Practices&#32;tests&#32;checking&#32;if&#32;all&#32;the&#32;ranges&#32;and&#32;domains&#32;from&#32;the&#32;test&#32;subject&#32;point&#32;to&#32;terms&#32;that&#32;are&#32;defined&#32;in&#32;the&#32;vocabulary.|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-157)|Identifier|`domain-out-of-vocabulary`|
|[Section top](#pass-outcome-number-157)|Title|Domains&#32;properly&#32;defined|
|[Section top](#pass-outcome-number-157)|Description|Each&#32;rdfs:domain&#32;is&#32;defined&#32;within&#32;the&#32;fragment|

***
### Pass Outcome number 158

[Jump to summary definition](#summary-Pass-158)	|	[Previous Pass outcome](#pass-outcome-number-157)	|	[Next Pass outcome](#pass-outcome-number-159)

:white_check_mark:Pass outcome
#### Subject detail
|Name|all-modules|
|----|----|
|Title|All&#32;the&#32;modules&#32;from&#32;branch&#32;HEAD&#32;that&#32;are&#32;syntaxically&#32;correct&#32;as&#32;well&#32;as&#32;their&#32;recursive&#32;imports|
|Composition|- [Module alignment/interaction-td](https://github.com/HyperAgents/hmas/blob/HEAD/src/alignment/interaction-td.ttl)<br/>- [Module core](https://github.com/HyperAgents/hmas/blob/HEAD/src/core.ttl)<br/>- [Module fipa](https://github.com/HyperAgents/hmas/blob/HEAD/src/fipa.ttl)<br/>- [Module interaction](https://github.com/HyperAgents/hmas/blob/HEAD/src/interaction.ttl)<br/>- [Module regulation](https://github.com/HyperAgents/hmas/blob/HEAD/src/regulation.ttl)|

#### Criterion detail
|Identifier|[domain-and-range-referencing](https://ns.inria.fr/olivaw#domain-and-range-referencing)|
|----|----|
|Title|Domain&#32;and&#32;range&#32;referencing&#32;test|
|Description|A&#32;test&#32;case&#32;from&#32;the&#32;Best&#32;Practices&#32;tests&#32;checking&#32;if&#32;all&#32;the&#32;ranges&#32;and&#32;domains&#32;from&#32;the&#32;test&#32;subject&#32;point&#32;to&#32;terms&#32;that&#32;are&#32;defined&#32;in&#32;the&#32;vocabulary.|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-158)|Identifier|`range-out-of-vocabulary`|
|[Section top](#pass-outcome-number-158)|Title|Ranges&#32;properly&#32;defined|
|[Section top](#pass-outcome-number-158)|Description|Each&#32;rdfs:range&#32;is&#32;defined&#32;within&#32;the&#32;fragment|

***
### Pass Outcome number 159

[Jump to summary definition](#summary-Pass-159)	|	[Previous Pass outcome](#pass-outcome-number-158)	|	[Next Pass outcome](#pass-outcome-number-160)

:white_check_mark:Pass outcome
#### Subject detail
|Name|all-modules|
|----|----|
|Title|All&#32;the&#32;modules&#32;from&#32;branch&#32;HEAD&#32;that&#32;are&#32;syntaxically&#32;correct&#32;as&#32;well&#32;as&#32;their&#32;recursive&#32;imports|
|Composition|- [Module alignment/interaction-td](https://github.com/HyperAgents/hmas/blob/HEAD/src/alignment/interaction-td.ttl)<br/>- [Module core](https://github.com/HyperAgents/hmas/blob/HEAD/src/core.ttl)<br/>- [Module fipa](https://github.com/HyperAgents/hmas/blob/HEAD/src/fipa.ttl)<br/>- [Module interaction](https://github.com/HyperAgents/hmas/blob/HEAD/src/interaction.ttl)<br/>- [Module regulation](https://github.com/HyperAgents/hmas/blob/HEAD/src/regulation.ttl)|

#### Criterion detail
|Identifier|[owl-rl-constraint](https://ns.inria.fr/olivaw#owl-rl-constraint)|
|----|----|
|Title|OWL&#32;RL&#32;Constraint&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;check&#32;wether&#32;the&#32;test&#32;subject&#32;is&#32;syntaxically&#32;correct&#32;or&#32;not.|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-159)|Identifier|`owl-rl-constraint-violation`|
|[Section top](#pass-outcome-number-159)|Title|OWL&#32;RL&#32;consistent|
|[Section top](#pass-outcome-number-159)|Description|The&#32;provided&#32;graph&#32;is&#32;consistent&#32;for&#32;any&#32;OWL&#32;RL&#32;constraint|

***
### Pass Outcome number 160

[Jump to summary definition](#summary-Pass-160)	|	[Previous Pass outcome](#pass-outcome-number-159)	|	[Next Pass outcome](#pass-outcome-number-161)

:white_check_mark:Pass outcome
#### Subject detail
|Name|all-modules|
|----|----|
|Title|All&#32;the&#32;modules&#32;from&#32;branch&#32;HEAD&#32;that&#32;are&#32;syntaxically&#32;correct&#32;as&#32;well&#32;as&#32;their&#32;recursive&#32;imports|
|Composition|- [Module alignment/interaction-td](https://github.com/HyperAgents/hmas/blob/HEAD/src/alignment/interaction-td.ttl)<br/>- [Module core](https://github.com/HyperAgents/hmas/blob/HEAD/src/core.ttl)<br/>- [Module fipa](https://github.com/HyperAgents/hmas/blob/HEAD/src/fipa.ttl)<br/>- [Module interaction](https://github.com/HyperAgents/hmas/blob/HEAD/src/interaction.ttl)<br/>- [Module regulation](https://github.com/HyperAgents/hmas/blob/HEAD/src/regulation.ttl)|

#### Criterion detail
|Identifier|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|
|----|----|
|Title|Profile&#32;compatibility&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;check&#32;whether&#32;the&#32;test&#32;subject&#32;is&#32;compatible&#32;with&#32;a&#32;profile&#32;or&#32;not,&#32;and&#32;if&#32;it&#32;is&#32;not,&#32;why.|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-160)|Identifier|`owl-rl-profile-error`|
|[Section top](#pass-outcome-number-160)|Title|OWL&#32;RL&#32;Profile&#32;compatible|
|[Section top](#pass-outcome-number-160)|Description|The&#32;subject&#32;is&#32;included&#32;in&#32;the&#32;OWL&#32;RL&#32;sublanguage|

***
### Pass Outcome number 161

[Jump to summary definition](#summary-Pass-161)	|	[Previous Pass outcome](#pass-outcome-number-160)	|	[Next Pass outcome](#pass-outcome-number-162)

:white_check_mark:Pass outcome
#### Subject detail
|Name|all-modules|
|----|----|
|Title|All&#32;the&#32;modules&#32;from&#32;branch&#32;HEAD&#32;that&#32;are&#32;syntaxically&#32;correct&#32;as&#32;well&#32;as&#32;their&#32;recursive&#32;imports|
|Composition|- [Module alignment/interaction-td](https://github.com/HyperAgents/hmas/blob/HEAD/src/alignment/interaction-td.ttl)<br/>- [Module core](https://github.com/HyperAgents/hmas/blob/HEAD/src/core.ttl)<br/>- [Module fipa](https://github.com/HyperAgents/hmas/blob/HEAD/src/fipa.ttl)<br/>- [Module interaction](https://github.com/HyperAgents/hmas/blob/HEAD/src/interaction.ttl)<br/>- [Module regulation](https://github.com/HyperAgents/hmas/blob/HEAD/src/regulation.ttl)|

#### Criterion detail
|Identifier|[proper-extension-predicate](https://ns.inria.fr/olivaw#proper-extension-predicate)|
|----|----|
|Title|Predicate&#32;extension&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;test&#32;the&#32;proper&#32;use&#32;of&#32;predicates&#32;rdfs:subClassOf&#32;and&#32;rdfs:subPropertyOf&#32;on&#32;the&#32;ontology&#32;terms|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-161)|Identifier|`class-subpropertyof`|
|[Section top](#pass-outcome-number-161)|Title|No&#32;class&#32;subproperty|
|[Section top](#pass-outcome-number-161)|Description|No&#32;ontology&#32;class&#32;is&#32;a&#32;subproperty|

***
### Pass Outcome number 162

[Jump to summary definition](#summary-Pass-162)	|	[Previous Pass outcome](#pass-outcome-number-161)	|	[Next Pass outcome](#pass-outcome-number-163)

:white_check_mark:Pass outcome
#### Subject detail
|Name|all-modules|
|----|----|
|Title|All&#32;the&#32;modules&#32;from&#32;branch&#32;HEAD&#32;that&#32;are&#32;syntaxically&#32;correct&#32;as&#32;well&#32;as&#32;their&#32;recursive&#32;imports|
|Composition|- [Module alignment/interaction-td](https://github.com/HyperAgents/hmas/blob/HEAD/src/alignment/interaction-td.ttl)<br/>- [Module core](https://github.com/HyperAgents/hmas/blob/HEAD/src/core.ttl)<br/>- [Module fipa](https://github.com/HyperAgents/hmas/blob/HEAD/src/fipa.ttl)<br/>- [Module interaction](https://github.com/HyperAgents/hmas/blob/HEAD/src/interaction.ttl)<br/>- [Module regulation](https://github.com/HyperAgents/hmas/blob/HEAD/src/regulation.ttl)|

#### Criterion detail
|Identifier|[proper-extension-predicate](https://ns.inria.fr/olivaw#proper-extension-predicate)|
|----|----|
|Title|Predicate&#32;extension&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;test&#32;the&#32;proper&#32;use&#32;of&#32;predicates&#32;rdfs:subClassOf&#32;and&#32;rdfs:subPropertyOf&#32;on&#32;the&#32;ontology&#32;terms|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-162)|Identifier|`property-subclassof`|
|[Section top](#pass-outcome-number-162)|Title|No&#32;property&#32;subclass|
|[Section top](#pass-outcome-number-162)|Description|No&#32;ontology&#32;property&#32;is&#32;a&#32;subclass|

***
### Pass Outcome number 163

[Jump to summary definition](#summary-Pass-163)	|	[Previous Pass outcome](#pass-outcome-number-162)	|	[Next Pass outcome](#pass-outcome-number-164)

:white_check_mark:Pass outcome
#### Subject detail
|Name|all-modules|
|----|----|
|Title|All&#32;the&#32;modules&#32;from&#32;branch&#32;HEAD&#32;that&#32;are&#32;syntaxically&#32;correct&#32;as&#32;well&#32;as&#32;their&#32;recursive&#32;imports|
|Composition|- [Module alignment/interaction-td](https://github.com/HyperAgents/hmas/blob/HEAD/src/alignment/interaction-td.ttl)<br/>- [Module core](https://github.com/HyperAgents/hmas/blob/HEAD/src/core.ttl)<br/>- [Module fipa](https://github.com/HyperAgents/hmas/blob/HEAD/src/fipa.ttl)<br/>- [Module interaction](https://github.com/HyperAgents/hmas/blob/HEAD/src/interaction.ttl)<br/>- [Module regulation](https://github.com/HyperAgents/hmas/blob/HEAD/src/regulation.ttl)|

#### Criterion detail
|Identifier|[proper-extension-predicate](https://ns.inria.fr/olivaw#proper-extension-predicate)|
|----|----|
|Title|Predicate&#32;extension&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;test&#32;the&#32;proper&#32;use&#32;of&#32;predicates&#32;rdfs:subClassOf&#32;and&#32;rdfs:subPropertyOf&#32;on&#32;the&#32;ontology&#32;terms|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-163)|Identifier|`subclassof-property`|
|[Section top](#pass-outcome-number-163)|Title|No&#32;subclass&#32;of&#32;property|
|[Section top](#pass-outcome-number-163)|Description|No&#32;ontology&#32;term&#32;is&#32;a&#32;subclass&#32;of&#32;a&#32;property|

***
### Pass Outcome number 164

[Jump to summary definition](#summary-Pass-164)	|	[Previous Pass outcome](#pass-outcome-number-163)	|	[Next Pass outcome](#pass-outcome-number-165)

:white_check_mark:Pass outcome
#### Subject detail
|Name|all-modules|
|----|----|
|Title|All&#32;the&#32;modules&#32;from&#32;branch&#32;HEAD&#32;that&#32;are&#32;syntaxically&#32;correct&#32;as&#32;well&#32;as&#32;their&#32;recursive&#32;imports|
|Composition|- [Module alignment/interaction-td](https://github.com/HyperAgents/hmas/blob/HEAD/src/alignment/interaction-td.ttl)<br/>- [Module core](https://github.com/HyperAgents/hmas/blob/HEAD/src/core.ttl)<br/>- [Module fipa](https://github.com/HyperAgents/hmas/blob/HEAD/src/fipa.ttl)<br/>- [Module interaction](https://github.com/HyperAgents/hmas/blob/HEAD/src/interaction.ttl)<br/>- [Module regulation](https://github.com/HyperAgents/hmas/blob/HEAD/src/regulation.ttl)|

#### Criterion detail
|Identifier|[proper-extension-predicate](https://ns.inria.fr/olivaw#proper-extension-predicate)|
|----|----|
|Title|Predicate&#32;extension&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;test&#32;the&#32;proper&#32;use&#32;of&#32;predicates&#32;rdfs:subClassOf&#32;and&#32;rdfs:subPropertyOf&#32;on&#32;the&#32;ontology&#32;terms|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-164)|Identifier|`subpropertyof-class`|
|[Section top](#pass-outcome-number-164)|Title|No&#32;subproperty&#32;of&#32;class|
|[Section top](#pass-outcome-number-164)|Description|No&#32;ontology&#32;term&#32;is&#32;a&#32;subproperty&#32;of&#32;a&#32;class|

***
### Pass Outcome number 165

[Jump to summary definition](#summary-Pass-165)	|	[Previous Pass outcome](#pass-outcome-number-164)	|	[Next Pass outcome](#pass-outcome-number-166)

:white_check_mark:Pass outcome
#### Subject detail
|Name|all-fragments|
|----|----|
|Title|All&#32;the&#32;fragments&#32;from&#32;branch&#32;HEAD&#32;that&#32;are&#32;syntaxically&#32;correct&#32;as&#32;well&#32;as&#32;their&#32;recursive&#32;imports|
|Composition|- [Modelet logistics/configure-organization](https://github.com/HyperAgents/hmas/blob/HEAD/domains/logistics/configure-organization/onto.ttl)<br/>- [Modelet logistics/coordinate-activities](https://github.com/HyperAgents/hmas/blob/HEAD/domains/logistics/coordinate-activities/onto.ttl)<br/>- [Modelet logistics/create-organization](https://github.com/HyperAgents/hmas/blob/HEAD/domains/logistics/create-organization/onto.ttl)<br/>- [Modelet manufacturing-environments/discover-behavior-specifications](https://github.com/HyperAgents/hmas/blob/HEAD/domains/manufacturing-environments/discover-behavior-specifications/onto.ttl)<br/>- [Modelet manufacturing-environments/discover-core](https://github.com/HyperAgents/hmas/blob/HEAD/domains/manufacturing-environments/discover-core/onto.ttl)<br/>- [Modelet manufacturing-environments/discover-organization](https://github.com/HyperAgents/hmas/blob/HEAD/domains/manufacturing-environments/discover-organization/onto.ttl)<br/>- [Modelet manufacturing-environments/discover-platforms](https://github.com/HyperAgents/hmas/blob/HEAD/domains/manufacturing-environments/discover-platforms/onto.ttl)<br/>- [Modelet manufacturing-environments/discover-signifiers](https://github.com/HyperAgents/hmas/blob/HEAD/domains/manufacturing-environments/discover-signifiers/onto.ttl)<br/>- [Module alignment/interaction-td](https://github.com/HyperAgents/hmas/blob/HEAD/src/alignment/interaction-td.ttl)<br/>- [Module core](https://github.com/HyperAgents/hmas/blob/HEAD/src/core.ttl)<br/>- [Module fipa](https://github.com/HyperAgents/hmas/blob/HEAD/src/fipa.ttl)<br/>- [Module interaction](https://github.com/HyperAgents/hmas/blob/HEAD/src/interaction.ttl)<br/>- [Module regulation](https://github.com/HyperAgents/hmas/blob/HEAD/src/regulation.ttl)|

#### Criterion detail
|Identifier|[domain-and-range-referencing](https://ns.inria.fr/olivaw#domain-and-range-referencing)|
|----|----|
|Title|Domain&#32;and&#32;range&#32;referencing&#32;test|
|Description|A&#32;test&#32;case&#32;from&#32;the&#32;Best&#32;Practices&#32;tests&#32;checking&#32;if&#32;all&#32;the&#32;ranges&#32;and&#32;domains&#32;from&#32;the&#32;test&#32;subject&#32;point&#32;to&#32;terms&#32;that&#32;are&#32;defined&#32;in&#32;the&#32;vocabulary.|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-165)|Identifier|`domain-out-of-vocabulary`|
|[Section top](#pass-outcome-number-165)|Title|Domains&#32;properly&#32;defined|
|[Section top](#pass-outcome-number-165)|Description|Each&#32;rdfs:domain&#32;is&#32;defined&#32;within&#32;the&#32;fragment|

***
### Pass Outcome number 166

[Jump to summary definition](#summary-Pass-166)	|	[Previous Pass outcome](#pass-outcome-number-165)	|	[Next Pass outcome](#pass-outcome-number-167)

:white_check_mark:Pass outcome
#### Subject detail
|Name|all-fragments|
|----|----|
|Title|All&#32;the&#32;fragments&#32;from&#32;branch&#32;HEAD&#32;that&#32;are&#32;syntaxically&#32;correct&#32;as&#32;well&#32;as&#32;their&#32;recursive&#32;imports|
|Composition|- [Modelet logistics/configure-organization](https://github.com/HyperAgents/hmas/blob/HEAD/domains/logistics/configure-organization/onto.ttl)<br/>- [Modelet logistics/coordinate-activities](https://github.com/HyperAgents/hmas/blob/HEAD/domains/logistics/coordinate-activities/onto.ttl)<br/>- [Modelet logistics/create-organization](https://github.com/HyperAgents/hmas/blob/HEAD/domains/logistics/create-organization/onto.ttl)<br/>- [Modelet manufacturing-environments/discover-behavior-specifications](https://github.com/HyperAgents/hmas/blob/HEAD/domains/manufacturing-environments/discover-behavior-specifications/onto.ttl)<br/>- [Modelet manufacturing-environments/discover-core](https://github.com/HyperAgents/hmas/blob/HEAD/domains/manufacturing-environments/discover-core/onto.ttl)<br/>- [Modelet manufacturing-environments/discover-organization](https://github.com/HyperAgents/hmas/blob/HEAD/domains/manufacturing-environments/discover-organization/onto.ttl)<br/>- [Modelet manufacturing-environments/discover-platforms](https://github.com/HyperAgents/hmas/blob/HEAD/domains/manufacturing-environments/discover-platforms/onto.ttl)<br/>- [Modelet manufacturing-environments/discover-signifiers](https://github.com/HyperAgents/hmas/blob/HEAD/domains/manufacturing-environments/discover-signifiers/onto.ttl)<br/>- [Module alignment/interaction-td](https://github.com/HyperAgents/hmas/blob/HEAD/src/alignment/interaction-td.ttl)<br/>- [Module core](https://github.com/HyperAgents/hmas/blob/HEAD/src/core.ttl)<br/>- [Module fipa](https://github.com/HyperAgents/hmas/blob/HEAD/src/fipa.ttl)<br/>- [Module interaction](https://github.com/HyperAgents/hmas/blob/HEAD/src/interaction.ttl)<br/>- [Module regulation](https://github.com/HyperAgents/hmas/blob/HEAD/src/regulation.ttl)|

#### Criterion detail
|Identifier|[domain-and-range-referencing](https://ns.inria.fr/olivaw#domain-and-range-referencing)|
|----|----|
|Title|Domain&#32;and&#32;range&#32;referencing&#32;test|
|Description|A&#32;test&#32;case&#32;from&#32;the&#32;Best&#32;Practices&#32;tests&#32;checking&#32;if&#32;all&#32;the&#32;ranges&#32;and&#32;domains&#32;from&#32;the&#32;test&#32;subject&#32;point&#32;to&#32;terms&#32;that&#32;are&#32;defined&#32;in&#32;the&#32;vocabulary.|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-166)|Identifier|`range-out-of-vocabulary`|
|[Section top](#pass-outcome-number-166)|Title|Ranges&#32;properly&#32;defined|
|[Section top](#pass-outcome-number-166)|Description|Each&#32;rdfs:range&#32;is&#32;defined&#32;within&#32;the&#32;fragment|

***
### Pass Outcome number 167

[Jump to summary definition](#summary-Pass-167)	|	[Previous Pass outcome](#pass-outcome-number-166)	|	[Next Pass outcome](#pass-outcome-number-168)

:white_check_mark:Pass outcome
#### Subject detail
|Name|all-fragments|
|----|----|
|Title|All&#32;the&#32;fragments&#32;from&#32;branch&#32;HEAD&#32;that&#32;are&#32;syntaxically&#32;correct&#32;as&#32;well&#32;as&#32;their&#32;recursive&#32;imports|
|Composition|- [Modelet logistics/configure-organization](https://github.com/HyperAgents/hmas/blob/HEAD/domains/logistics/configure-organization/onto.ttl)<br/>- [Modelet logistics/coordinate-activities](https://github.com/HyperAgents/hmas/blob/HEAD/domains/logistics/coordinate-activities/onto.ttl)<br/>- [Modelet logistics/create-organization](https://github.com/HyperAgents/hmas/blob/HEAD/domains/logistics/create-organization/onto.ttl)<br/>- [Modelet manufacturing-environments/discover-behavior-specifications](https://github.com/HyperAgents/hmas/blob/HEAD/domains/manufacturing-environments/discover-behavior-specifications/onto.ttl)<br/>- [Modelet manufacturing-environments/discover-core](https://github.com/HyperAgents/hmas/blob/HEAD/domains/manufacturing-environments/discover-core/onto.ttl)<br/>- [Modelet manufacturing-environments/discover-organization](https://github.com/HyperAgents/hmas/blob/HEAD/domains/manufacturing-environments/discover-organization/onto.ttl)<br/>- [Modelet manufacturing-environments/discover-platforms](https://github.com/HyperAgents/hmas/blob/HEAD/domains/manufacturing-environments/discover-platforms/onto.ttl)<br/>- [Modelet manufacturing-environments/discover-signifiers](https://github.com/HyperAgents/hmas/blob/HEAD/domains/manufacturing-environments/discover-signifiers/onto.ttl)<br/>- [Module alignment/interaction-td](https://github.com/HyperAgents/hmas/blob/HEAD/src/alignment/interaction-td.ttl)<br/>- [Module core](https://github.com/HyperAgents/hmas/blob/HEAD/src/core.ttl)<br/>- [Module fipa](https://github.com/HyperAgents/hmas/blob/HEAD/src/fipa.ttl)<br/>- [Module interaction](https://github.com/HyperAgents/hmas/blob/HEAD/src/interaction.ttl)<br/>- [Module regulation](https://github.com/HyperAgents/hmas/blob/HEAD/src/regulation.ttl)|

#### Criterion detail
|Identifier|[owl-rl-constraint](https://ns.inria.fr/olivaw#owl-rl-constraint)|
|----|----|
|Title|OWL&#32;RL&#32;Constraint&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;check&#32;wether&#32;the&#32;test&#32;subject&#32;is&#32;syntaxically&#32;correct&#32;or&#32;not.|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-167)|Identifier|`owl-rl-constraint-violation`|
|[Section top](#pass-outcome-number-167)|Title|OWL&#32;RL&#32;consistent|
|[Section top](#pass-outcome-number-167)|Description|The&#32;provided&#32;graph&#32;is&#32;consistent&#32;for&#32;any&#32;OWL&#32;RL&#32;constraint|

***
### Pass Outcome number 168

[Jump to summary definition](#summary-Pass-168)	|	[Previous Pass outcome](#pass-outcome-number-167)	|	[Next Pass outcome](#pass-outcome-number-169)

:white_check_mark:Pass outcome
#### Subject detail
|Name|all-fragments|
|----|----|
|Title|All&#32;the&#32;fragments&#32;from&#32;branch&#32;HEAD&#32;that&#32;are&#32;syntaxically&#32;correct&#32;as&#32;well&#32;as&#32;their&#32;recursive&#32;imports|
|Composition|- [Modelet logistics/configure-organization](https://github.com/HyperAgents/hmas/blob/HEAD/domains/logistics/configure-organization/onto.ttl)<br/>- [Modelet logistics/coordinate-activities](https://github.com/HyperAgents/hmas/blob/HEAD/domains/logistics/coordinate-activities/onto.ttl)<br/>- [Modelet logistics/create-organization](https://github.com/HyperAgents/hmas/blob/HEAD/domains/logistics/create-organization/onto.ttl)<br/>- [Modelet manufacturing-environments/discover-behavior-specifications](https://github.com/HyperAgents/hmas/blob/HEAD/domains/manufacturing-environments/discover-behavior-specifications/onto.ttl)<br/>- [Modelet manufacturing-environments/discover-core](https://github.com/HyperAgents/hmas/blob/HEAD/domains/manufacturing-environments/discover-core/onto.ttl)<br/>- [Modelet manufacturing-environments/discover-organization](https://github.com/HyperAgents/hmas/blob/HEAD/domains/manufacturing-environments/discover-organization/onto.ttl)<br/>- [Modelet manufacturing-environments/discover-platforms](https://github.com/HyperAgents/hmas/blob/HEAD/domains/manufacturing-environments/discover-platforms/onto.ttl)<br/>- [Modelet manufacturing-environments/discover-signifiers](https://github.com/HyperAgents/hmas/blob/HEAD/domains/manufacturing-environments/discover-signifiers/onto.ttl)<br/>- [Module alignment/interaction-td](https://github.com/HyperAgents/hmas/blob/HEAD/src/alignment/interaction-td.ttl)<br/>- [Module core](https://github.com/HyperAgents/hmas/blob/HEAD/src/core.ttl)<br/>- [Module fipa](https://github.com/HyperAgents/hmas/blob/HEAD/src/fipa.ttl)<br/>- [Module interaction](https://github.com/HyperAgents/hmas/blob/HEAD/src/interaction.ttl)<br/>- [Module regulation](https://github.com/HyperAgents/hmas/blob/HEAD/src/regulation.ttl)|

#### Criterion detail
|Identifier|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|
|----|----|
|Title|Profile&#32;compatibility&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;check&#32;whether&#32;the&#32;test&#32;subject&#32;is&#32;compatible&#32;with&#32;a&#32;profile&#32;or&#32;not,&#32;and&#32;if&#32;it&#32;is&#32;not,&#32;why.|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-168)|Identifier|`owl-rl-profile-error`|
|[Section top](#pass-outcome-number-168)|Title|OWL&#32;RL&#32;Profile&#32;compatible|
|[Section top](#pass-outcome-number-168)|Description|The&#32;subject&#32;is&#32;included&#32;in&#32;the&#32;OWL&#32;RL&#32;sublanguage|

***
### Pass Outcome number 169

[Jump to summary definition](#summary-Pass-169)	|	[Previous Pass outcome](#pass-outcome-number-168)	|	[Next Pass outcome](#pass-outcome-number-170)

:white_check_mark:Pass outcome
#### Subject detail
|Name|all-fragments|
|----|----|
|Title|All&#32;the&#32;fragments&#32;from&#32;branch&#32;HEAD&#32;that&#32;are&#32;syntaxically&#32;correct&#32;as&#32;well&#32;as&#32;their&#32;recursive&#32;imports|
|Composition|- [Modelet logistics/configure-organization](https://github.com/HyperAgents/hmas/blob/HEAD/domains/logistics/configure-organization/onto.ttl)<br/>- [Modelet logistics/coordinate-activities](https://github.com/HyperAgents/hmas/blob/HEAD/domains/logistics/coordinate-activities/onto.ttl)<br/>- [Modelet logistics/create-organization](https://github.com/HyperAgents/hmas/blob/HEAD/domains/logistics/create-organization/onto.ttl)<br/>- [Modelet manufacturing-environments/discover-behavior-specifications](https://github.com/HyperAgents/hmas/blob/HEAD/domains/manufacturing-environments/discover-behavior-specifications/onto.ttl)<br/>- [Modelet manufacturing-environments/discover-core](https://github.com/HyperAgents/hmas/blob/HEAD/domains/manufacturing-environments/discover-core/onto.ttl)<br/>- [Modelet manufacturing-environments/discover-organization](https://github.com/HyperAgents/hmas/blob/HEAD/domains/manufacturing-environments/discover-organization/onto.ttl)<br/>- [Modelet manufacturing-environments/discover-platforms](https://github.com/HyperAgents/hmas/blob/HEAD/domains/manufacturing-environments/discover-platforms/onto.ttl)<br/>- [Modelet manufacturing-environments/discover-signifiers](https://github.com/HyperAgents/hmas/blob/HEAD/domains/manufacturing-environments/discover-signifiers/onto.ttl)<br/>- [Module alignment/interaction-td](https://github.com/HyperAgents/hmas/blob/HEAD/src/alignment/interaction-td.ttl)<br/>- [Module core](https://github.com/HyperAgents/hmas/blob/HEAD/src/core.ttl)<br/>- [Module fipa](https://github.com/HyperAgents/hmas/blob/HEAD/src/fipa.ttl)<br/>- [Module interaction](https://github.com/HyperAgents/hmas/blob/HEAD/src/interaction.ttl)<br/>- [Module regulation](https://github.com/HyperAgents/hmas/blob/HEAD/src/regulation.ttl)|

#### Criterion detail
|Identifier|[proper-extension-predicate](https://ns.inria.fr/olivaw#proper-extension-predicate)|
|----|----|
|Title|Predicate&#32;extension&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;test&#32;the&#32;proper&#32;use&#32;of&#32;predicates&#32;rdfs:subClassOf&#32;and&#32;rdfs:subPropertyOf&#32;on&#32;the&#32;ontology&#32;terms|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-169)|Identifier|`class-subpropertyof`|
|[Section top](#pass-outcome-number-169)|Title|No&#32;class&#32;subproperty|
|[Section top](#pass-outcome-number-169)|Description|No&#32;ontology&#32;class&#32;is&#32;a&#32;subproperty|

***
### Pass Outcome number 170

[Jump to summary definition](#summary-Pass-170)	|	[Previous Pass outcome](#pass-outcome-number-169)	|	[Next Pass outcome](#pass-outcome-number-171)

:white_check_mark:Pass outcome
#### Subject detail
|Name|all-fragments|
|----|----|
|Title|All&#32;the&#32;fragments&#32;from&#32;branch&#32;HEAD&#32;that&#32;are&#32;syntaxically&#32;correct&#32;as&#32;well&#32;as&#32;their&#32;recursive&#32;imports|
|Composition|- [Modelet logistics/configure-organization](https://github.com/HyperAgents/hmas/blob/HEAD/domains/logistics/configure-organization/onto.ttl)<br/>- [Modelet logistics/coordinate-activities](https://github.com/HyperAgents/hmas/blob/HEAD/domains/logistics/coordinate-activities/onto.ttl)<br/>- [Modelet logistics/create-organization](https://github.com/HyperAgents/hmas/blob/HEAD/domains/logistics/create-organization/onto.ttl)<br/>- [Modelet manufacturing-environments/discover-behavior-specifications](https://github.com/HyperAgents/hmas/blob/HEAD/domains/manufacturing-environments/discover-behavior-specifications/onto.ttl)<br/>- [Modelet manufacturing-environments/discover-core](https://github.com/HyperAgents/hmas/blob/HEAD/domains/manufacturing-environments/discover-core/onto.ttl)<br/>- [Modelet manufacturing-environments/discover-organization](https://github.com/HyperAgents/hmas/blob/HEAD/domains/manufacturing-environments/discover-organization/onto.ttl)<br/>- [Modelet manufacturing-environments/discover-platforms](https://github.com/HyperAgents/hmas/blob/HEAD/domains/manufacturing-environments/discover-platforms/onto.ttl)<br/>- [Modelet manufacturing-environments/discover-signifiers](https://github.com/HyperAgents/hmas/blob/HEAD/domains/manufacturing-environments/discover-signifiers/onto.ttl)<br/>- [Module alignment/interaction-td](https://github.com/HyperAgents/hmas/blob/HEAD/src/alignment/interaction-td.ttl)<br/>- [Module core](https://github.com/HyperAgents/hmas/blob/HEAD/src/core.ttl)<br/>- [Module fipa](https://github.com/HyperAgents/hmas/blob/HEAD/src/fipa.ttl)<br/>- [Module interaction](https://github.com/HyperAgents/hmas/blob/HEAD/src/interaction.ttl)<br/>- [Module regulation](https://github.com/HyperAgents/hmas/blob/HEAD/src/regulation.ttl)|

#### Criterion detail
|Identifier|[proper-extension-predicate](https://ns.inria.fr/olivaw#proper-extension-predicate)|
|----|----|
|Title|Predicate&#32;extension&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;test&#32;the&#32;proper&#32;use&#32;of&#32;predicates&#32;rdfs:subClassOf&#32;and&#32;rdfs:subPropertyOf&#32;on&#32;the&#32;ontology&#32;terms|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-170)|Identifier|`property-subclassof`|
|[Section top](#pass-outcome-number-170)|Title|No&#32;property&#32;subclass|
|[Section top](#pass-outcome-number-170)|Description|No&#32;ontology&#32;property&#32;is&#32;a&#32;subclass|

***
### Pass Outcome number 171

[Jump to summary definition](#summary-Pass-171)	|	[Previous Pass outcome](#pass-outcome-number-170)	|	[Next Pass outcome](#pass-outcome-number-172)

:white_check_mark:Pass outcome
#### Subject detail
|Name|all-fragments|
|----|----|
|Title|All&#32;the&#32;fragments&#32;from&#32;branch&#32;HEAD&#32;that&#32;are&#32;syntaxically&#32;correct&#32;as&#32;well&#32;as&#32;their&#32;recursive&#32;imports|
|Composition|- [Modelet logistics/configure-organization](https://github.com/HyperAgents/hmas/blob/HEAD/domains/logistics/configure-organization/onto.ttl)<br/>- [Modelet logistics/coordinate-activities](https://github.com/HyperAgents/hmas/blob/HEAD/domains/logistics/coordinate-activities/onto.ttl)<br/>- [Modelet logistics/create-organization](https://github.com/HyperAgents/hmas/blob/HEAD/domains/logistics/create-organization/onto.ttl)<br/>- [Modelet manufacturing-environments/discover-behavior-specifications](https://github.com/HyperAgents/hmas/blob/HEAD/domains/manufacturing-environments/discover-behavior-specifications/onto.ttl)<br/>- [Modelet manufacturing-environments/discover-core](https://github.com/HyperAgents/hmas/blob/HEAD/domains/manufacturing-environments/discover-core/onto.ttl)<br/>- [Modelet manufacturing-environments/discover-organization](https://github.com/HyperAgents/hmas/blob/HEAD/domains/manufacturing-environments/discover-organization/onto.ttl)<br/>- [Modelet manufacturing-environments/discover-platforms](https://github.com/HyperAgents/hmas/blob/HEAD/domains/manufacturing-environments/discover-platforms/onto.ttl)<br/>- [Modelet manufacturing-environments/discover-signifiers](https://github.com/HyperAgents/hmas/blob/HEAD/domains/manufacturing-environments/discover-signifiers/onto.ttl)<br/>- [Module alignment/interaction-td](https://github.com/HyperAgents/hmas/blob/HEAD/src/alignment/interaction-td.ttl)<br/>- [Module core](https://github.com/HyperAgents/hmas/blob/HEAD/src/core.ttl)<br/>- [Module fipa](https://github.com/HyperAgents/hmas/blob/HEAD/src/fipa.ttl)<br/>- [Module interaction](https://github.com/HyperAgents/hmas/blob/HEAD/src/interaction.ttl)<br/>- [Module regulation](https://github.com/HyperAgents/hmas/blob/HEAD/src/regulation.ttl)|

#### Criterion detail
|Identifier|[proper-extension-predicate](https://ns.inria.fr/olivaw#proper-extension-predicate)|
|----|----|
|Title|Predicate&#32;extension&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;test&#32;the&#32;proper&#32;use&#32;of&#32;predicates&#32;rdfs:subClassOf&#32;and&#32;rdfs:subPropertyOf&#32;on&#32;the&#32;ontology&#32;terms|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-171)|Identifier|`subclassof-property`|
|[Section top](#pass-outcome-number-171)|Title|No&#32;subclass&#32;of&#32;property|
|[Section top](#pass-outcome-number-171)|Description|No&#32;ontology&#32;term&#32;is&#32;a&#32;subclass&#32;of&#32;a&#32;property|

***
### Pass Outcome number 172

[Jump to summary definition](#summary-Pass-172)	|	[Previous Pass outcome](#pass-outcome-number-171)	|	Next Pass outcome

:white_check_mark:Pass outcome
#### Subject detail
|Name|all-fragments|
|----|----|
|Title|All&#32;the&#32;fragments&#32;from&#32;branch&#32;HEAD&#32;that&#32;are&#32;syntaxically&#32;correct&#32;as&#32;well&#32;as&#32;their&#32;recursive&#32;imports|
|Composition|- [Modelet logistics/configure-organization](https://github.com/HyperAgents/hmas/blob/HEAD/domains/logistics/configure-organization/onto.ttl)<br/>- [Modelet logistics/coordinate-activities](https://github.com/HyperAgents/hmas/blob/HEAD/domains/logistics/coordinate-activities/onto.ttl)<br/>- [Modelet logistics/create-organization](https://github.com/HyperAgents/hmas/blob/HEAD/domains/logistics/create-organization/onto.ttl)<br/>- [Modelet manufacturing-environments/discover-behavior-specifications](https://github.com/HyperAgents/hmas/blob/HEAD/domains/manufacturing-environments/discover-behavior-specifications/onto.ttl)<br/>- [Modelet manufacturing-environments/discover-core](https://github.com/HyperAgents/hmas/blob/HEAD/domains/manufacturing-environments/discover-core/onto.ttl)<br/>- [Modelet manufacturing-environments/discover-organization](https://github.com/HyperAgents/hmas/blob/HEAD/domains/manufacturing-environments/discover-organization/onto.ttl)<br/>- [Modelet manufacturing-environments/discover-platforms](https://github.com/HyperAgents/hmas/blob/HEAD/domains/manufacturing-environments/discover-platforms/onto.ttl)<br/>- [Modelet manufacturing-environments/discover-signifiers](https://github.com/HyperAgents/hmas/blob/HEAD/domains/manufacturing-environments/discover-signifiers/onto.ttl)<br/>- [Module alignment/interaction-td](https://github.com/HyperAgents/hmas/blob/HEAD/src/alignment/interaction-td.ttl)<br/>- [Module core](https://github.com/HyperAgents/hmas/blob/HEAD/src/core.ttl)<br/>- [Module fipa](https://github.com/HyperAgents/hmas/blob/HEAD/src/fipa.ttl)<br/>- [Module interaction](https://github.com/HyperAgents/hmas/blob/HEAD/src/interaction.ttl)<br/>- [Module regulation](https://github.com/HyperAgents/hmas/blob/HEAD/src/regulation.ttl)|

#### Criterion detail
|Identifier|[proper-extension-predicate](https://ns.inria.fr/olivaw#proper-extension-predicate)|
|----|----|
|Title|Predicate&#32;extension&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;test&#32;the&#32;proper&#32;use&#32;of&#32;predicates&#32;rdfs:subClassOf&#32;and&#32;rdfs:subPropertyOf&#32;on&#32;the&#32;ontology&#32;terms|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-172)|Identifier|`subpropertyof-class`|
|[Section top](#pass-outcome-number-172)|Title|No&#32;subproperty&#32;of&#32;class|
|[Section top](#pass-outcome-number-172)|Description|No&#32;ontology&#32;term&#32;is&#32;a&#32;subproperty&#32;of&#32;a&#32;class|

***

</details>

***
