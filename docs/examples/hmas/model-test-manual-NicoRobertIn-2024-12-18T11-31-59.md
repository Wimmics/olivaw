# Test Report Markdown Export

This file is an export of the RDF test report made out of [EARL vocabulary](https://www.w3.org/TR/EARL10/)

This test is powered by Corese, check [Corese website](https://project.inria.fr/corese/) and [Corese repository](https://github.com/Wimmics/corese)

The original test report is available in turtle syntax [here](./model-test-manual-NicoRobertIn-2024-12-18T11-31-59.ttl).

# Test Activity

Here is some information about the testing activity that led to this report

|Title|Model&#32;tests&#32;of&#32;[HyperAgents/hmas](https://github.com/HyperAgents/hmas)&#32;on&#32;branch&#32;HEAD|
|--|--|
|Description|[NicoRobertIn](https://github.com/NicoRobertIn)&#32;launch&#32;manual&#32;run&#32;of&#32;model&#32;tests&#32;against&#32;[HyperAgents/hmas](https://github.com/HyperAgents/hmas)&#32;on&#32;branch&#32;HEAD|
|Tester|[NicoRobertIn](https://github.com/NicoRobertIn)|
|Ontology|[HyperAgents/hmas](https://github.com/HyperAgents/hmas)|
|Ontology version|Local state `ca439d4144b23b3fe927509872babc8d82142fae`|
|Ontology version date|2024-12-18 11:31:48|
|Ontology previous version|[3b0b11eccd899dd65ac9c3bbf0c043e28b61b46b](https://github.com/HyperAgents/hmas/tree/3b0b11eccd899dd65ac9c3bbf0c043e28b61b46b)|
|Ontology branch|[HEAD](https://github.com/HyperAgents/hmas/tree/HEAD)|
|Olivaw suite|[olivaw model test suite](https://github.com/Wimmics/olivaw/blob/v0.0.7/olivaw/test/model/suite.py)|
|Olivaw version|[v0.0.7](https://pypi.org/project/olivaw/0.0.7)|
|Generated turtle|[Turtle report](./model-test-manual-NicoRobertIn-2024-12-18T11-31-59.ttl)|
|Generated Markdown|[Markdown report](./model-test-manual-NicoRobertIn-2024-12-18T11-31-59.md)|

# Statistic summary

Here is a short overview for this test report

319 Outcomes

:boom:3 MajorFail, :exclamation:55 MinorFail, :warning:0 CannotTell, :grey_question:0 NotTested, :white_check_mark:261 Pass

<div  style="border-radius: 12px; height: 25px; overflow: hidden"><img src="../assets/red.png" width="1%" height="25px"/><img src="../assets/orange.png" width="17%" height="25px"/><img src="../assets/grey.png" width="0%" height="25px"/><img src="../assets/white.png" width="0%" height="25px"/><img src="../assets/green.png" width="82%" height="25px"/></div>

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
|[Chapter top](#majorfail-outcomes)|<div id="summary-MajorFail-1">1/3</div>|:boom:MajorFail|`module-src-meta`|[syntax](https://ns.inria.fr/olivaw#syntax)|Test subject has syntax errors|[Jump](#majorfail-outcome-number-1)|
|[Chapter top](#majorfail-outcomes)|<div id="summary-MajorFail-2">2/3</div>|:boom:MajorFail|`modelet-manufacturing-environments-safety-rules`|[syntax](https://ns.inria.fr/olivaw#syntax)|Test subject has syntax errors|[Jump](#majorfail-outcome-number-2)|
|[Chapter top](#majorfail-outcomes)|<div id="summary-MajorFail-3">3/3</div>|:boom:MajorFail|`modelet-logistics-structure-organization`|[syntax](https://ns.inria.fr/olivaw#syntax)|Test subject has syntax errors|[Jump](#majorfail-outcome-number-3)|

***

## MajorFail Outcomes Details

This subchapter gives more details to the :boom:MajorFail outcomes

### MajorFail Outcome number 1

[Jump to summary definition](#summary-MajorFail-1)	|	Previous MajorFail outcome	|	[Next MajorFail outcome](#majorfail-outcome-number-2)

:boom:MajorFail outcome
#### Subject detail
|Name|module-src-meta|
|----|----|
|Title|Standalone&#32;module&#32;src/meta.ttl&#32;from&#32;branch&#32;HEAD|
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
|Title|Standalone&#32;modelet&#32;domains/manufacturing-environments/safety-rules/onto.ttl&#32;from&#32;branch&#32;HEAD|
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
|Title|Standalone&#32;modelet&#32;domains/logistics/structure-organization/onto.ttl&#32;from&#32;branch&#32;HEAD|
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

[Jump to statistic summary](#statistic-summary)	|	[Previous section](#majorfail-outcomes)	|	[Next section](#pass-outcomes)

Here is the chapter related to the MinorFail outcome

:exclamation:55 MinorFail outcomes

<details>
<summary>Fold/Unfold the 55 summary and details</summary>

## MinorFail Outcomes Summary

:exclamation:55 MinorFail outcomes

|*Jump*|*Number*|*Status*|*Subject*|*Criterion*|*Title*|*Link*|
|------|--------|--------|---------|-----------|-------|------|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-1">1/55</div>|:exclamation:MinorFail|`module-src-regulation-modelet-logistics-create-organization`|[terms-differenciation](https://ns.inria.fr/olivaw#terms-differenciation)|Too close terms|[Jump](#minorfail-outcome-number-1)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-2">2/55</div>|:exclamation:MinorFail|`module-src-regulation-modelet-logistics-coordinate-activities`|[terms-differenciation](https://ns.inria.fr/olivaw#terms-differenciation)|Too close terms|[Jump](#minorfail-outcome-number-2)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-3">3/55</div>|:exclamation:MinorFail|`module-src-regulation-modelet-logistics-configure-organization`|[terms-differenciation](https://ns.inria.fr/olivaw#terms-differenciation)|Too close terms|[Jump](#minorfail-outcome-number-3)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-4">4/55</div>|:exclamation:MinorFail|`module-src-regulation`|[terms-differenciation](https://ns.inria.fr/olivaw#terms-differenciation)|Too close terms|[Jump](#minorfail-outcome-number-4)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-5">5/55</div>|:exclamation:MinorFail|`module-src-fipa`|[term-referencing](https://ns.inria.fr/olivaw#term-referencing)|Term not referenced to a module|[Jump](#minorfail-outcome-number-5)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-6">6/55</div>|:exclamation:MinorFail|`module-src-core-modelet-manufacturing-environments-discover-signifiers`|[labeled-terms](https://ns.inria.fr/olivaw#labeled-terms)|Terms not labeled|[Jump](#minorfail-outcome-number-6)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-7">7/55</div>|:exclamation:MinorFail|`module-src-core-modelet-manufacturing-environments-discover-signifiers`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL EL Profile incompatible|[Jump](#minorfail-outcome-number-7)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-8">8/55</div>|:exclamation:MinorFail|`module-src-core-modelet-manufacturing-environments-discover-signifiers`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL EL Profile incompatible|[Jump](#minorfail-outcome-number-8)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-9">9/55</div>|:exclamation:MinorFail|`module-src-core-modelet-manufacturing-environments-discover-signifiers`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL QL Profile incompatible|[Jump](#minorfail-outcome-number-9)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-10">10/55</div>|:exclamation:MinorFail|`module-src-core-modelet-manufacturing-environments-discover-signifiers`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL QL Profile incompatible|[Jump](#minorfail-outcome-number-10)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-11">11/55</div>|:exclamation:MinorFail|`module-src-core-modelet-manufacturing-environments-discover-platforms`|[labeled-terms](https://ns.inria.fr/olivaw#labeled-terms)|Terms not labeled|[Jump](#minorfail-outcome-number-11)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-12">12/55</div>|:exclamation:MinorFail|`module-src-core-modelet-manufacturing-environments-discover-platforms`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL EL Profile incompatible|[Jump](#minorfail-outcome-number-12)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-13">13/55</div>|:exclamation:MinorFail|`module-src-core-modelet-manufacturing-environments-discover-platforms`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL EL Profile incompatible|[Jump](#minorfail-outcome-number-13)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-14">14/55</div>|:exclamation:MinorFail|`module-src-core-modelet-manufacturing-environments-discover-platforms`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL QL Profile incompatible|[Jump](#minorfail-outcome-number-14)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-15">15/55</div>|:exclamation:MinorFail|`module-src-core-modelet-manufacturing-environments-discover-platforms`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL QL Profile incompatible|[Jump](#minorfail-outcome-number-15)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-16">16/55</div>|:exclamation:MinorFail|`module-src-core-modelet-manufacturing-environments-discover-organization`|[labeled-terms](https://ns.inria.fr/olivaw#labeled-terms)|Terms not labeled|[Jump](#minorfail-outcome-number-16)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-17">17/55</div>|:exclamation:MinorFail|`module-src-core-modelet-manufacturing-environments-discover-organization`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL EL Profile incompatible|[Jump](#minorfail-outcome-number-17)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-18">18/55</div>|:exclamation:MinorFail|`module-src-core-modelet-manufacturing-environments-discover-organization`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL EL Profile incompatible|[Jump](#minorfail-outcome-number-18)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-19">19/55</div>|:exclamation:MinorFail|`module-src-core-modelet-manufacturing-environments-discover-organization`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL QL Profile incompatible|[Jump](#minorfail-outcome-number-19)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-20">20/55</div>|:exclamation:MinorFail|`module-src-core-modelet-manufacturing-environments-discover-organization`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL QL Profile incompatible|[Jump](#minorfail-outcome-number-20)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-21">21/55</div>|:exclamation:MinorFail|`module-src-core-modelet-manufacturing-environments-discover-core`|[labeled-terms](https://ns.inria.fr/olivaw#labeled-terms)|Terms not labeled|[Jump](#minorfail-outcome-number-21)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-22">22/55</div>|:exclamation:MinorFail|`module-src-core-modelet-manufacturing-environments-discover-core`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL EL Profile incompatible|[Jump](#minorfail-outcome-number-22)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-23">23/55</div>|:exclamation:MinorFail|`module-src-core-modelet-manufacturing-environments-discover-core`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL EL Profile incompatible|[Jump](#minorfail-outcome-number-23)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-24">24/55</div>|:exclamation:MinorFail|`module-src-core-modelet-manufacturing-environments-discover-core`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL QL Profile incompatible|[Jump](#minorfail-outcome-number-24)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-25">25/55</div>|:exclamation:MinorFail|`module-src-core-modelet-manufacturing-environments-discover-core`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL QL Profile incompatible|[Jump](#minorfail-outcome-number-25)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-26">26/55</div>|:exclamation:MinorFail|`module-src-core`|[labeled-terms](https://ns.inria.fr/olivaw#labeled-terms)|Terms not labeled|[Jump](#minorfail-outcome-number-26)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-27">27/55</div>|:exclamation:MinorFail|`module-src-core`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL EL Profile incompatible|[Jump](#minorfail-outcome-number-27)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-28">28/55</div>|:exclamation:MinorFail|`module-src-core`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL EL Profile incompatible|[Jump](#minorfail-outcome-number-28)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-29">29/55</div>|:exclamation:MinorFail|`module-src-core`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL QL Profile incompatible|[Jump](#minorfail-outcome-number-29)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-30">30/55</div>|:exclamation:MinorFail|`module-src-core`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL QL Profile incompatible|[Jump](#minorfail-outcome-number-30)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-31">31/55</div>|:exclamation:MinorFail|`module-src-alignment-interaction-td`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL QL Profile incompatible|[Jump](#minorfail-outcome-number-31)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-32">32/55</div>|:exclamation:MinorFail|`module-src-alignment-interaction-td`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL QL Profile incompatible|[Jump](#minorfail-outcome-number-32)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-33">33/55</div>|:exclamation:MinorFail|`modelet-manufacturing-environments-discover-signifiers`|[labeled-terms](https://ns.inria.fr/olivaw#labeled-terms)|Terms not labeled|[Jump](#minorfail-outcome-number-33)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-34">34/55</div>|:exclamation:MinorFail|`modelet-manufacturing-environments-discover-signifiers`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL EL Profile incompatible|[Jump](#minorfail-outcome-number-34)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-35">35/55</div>|:exclamation:MinorFail|`modelet-manufacturing-environments-discover-signifiers`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL QL Profile incompatible|[Jump](#minorfail-outcome-number-35)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-36">36/55</div>|:exclamation:MinorFail|`modelet-manufacturing-environments-discover-platforms`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL EL Profile incompatible|[Jump](#minorfail-outcome-number-36)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-37">37/55</div>|:exclamation:MinorFail|`modelet-manufacturing-environments-discover-core`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL EL Profile incompatible|[Jump](#minorfail-outcome-number-37)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-38">38/55</div>|:exclamation:MinorFail|`modelet-manufacturing-environments-discover-core`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL QL Profile incompatible|[Jump](#minorfail-outcome-number-38)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-39">39/55</div>|:exclamation:MinorFail|`modelet-logistics-configure-organization`|[terms-differenciation](https://ns.inria.fr/olivaw#terms-differenciation)|Too close terms|[Jump](#minorfail-outcome-number-39)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-40">40/55</div>|:exclamation:MinorFail|`all-modules`|[labeled-terms](https://ns.inria.fr/olivaw#labeled-terms)|Terms not labeled|[Jump](#minorfail-outcome-number-40)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-41">41/55</div>|:exclamation:MinorFail|`all-modules`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL EL Profile incompatible|[Jump](#minorfail-outcome-number-41)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-42">42/55</div>|:exclamation:MinorFail|`all-modules`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL EL Profile incompatible|[Jump](#minorfail-outcome-number-42)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-43">43/55</div>|:exclamation:MinorFail|`all-modules`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL QL Profile incompatible|[Jump](#minorfail-outcome-number-43)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-44">44/55</div>|:exclamation:MinorFail|`all-modules`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL QL Profile incompatible|[Jump](#minorfail-outcome-number-44)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-45">45/55</div>|:exclamation:MinorFail|`all-modules`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL QL Profile incompatible|[Jump](#minorfail-outcome-number-45)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-46">46/55</div>|:exclamation:MinorFail|`all-modules`|[term-referencing](https://ns.inria.fr/olivaw#term-referencing)|Term not referenced to a module|[Jump](#minorfail-outcome-number-46)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-47">47/55</div>|:exclamation:MinorFail|`all-modules`|[terms-differenciation](https://ns.inria.fr/olivaw#terms-differenciation)|Too close terms|[Jump](#minorfail-outcome-number-47)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-48">48/55</div>|:exclamation:MinorFail|`all-fragments`|[labeled-terms](https://ns.inria.fr/olivaw#labeled-terms)|Terms not labeled|[Jump](#minorfail-outcome-number-48)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-49">49/55</div>|:exclamation:MinorFail|`all-fragments`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL EL Profile incompatible|[Jump](#minorfail-outcome-number-49)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-50">50/55</div>|:exclamation:MinorFail|`all-fragments`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL EL Profile incompatible|[Jump](#minorfail-outcome-number-50)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-51">51/55</div>|:exclamation:MinorFail|`all-fragments`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL QL Profile incompatible|[Jump](#minorfail-outcome-number-51)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-52">52/55</div>|:exclamation:MinorFail|`all-fragments`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL QL Profile incompatible|[Jump](#minorfail-outcome-number-52)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-53">53/55</div>|:exclamation:MinorFail|`all-fragments`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL QL Profile incompatible|[Jump](#minorfail-outcome-number-53)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-54">54/55</div>|:exclamation:MinorFail|`all-fragments`|[term-referencing](https://ns.inria.fr/olivaw#term-referencing)|Term not referenced to a module|[Jump](#minorfail-outcome-number-54)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-55">55/55</div>|:exclamation:MinorFail|`all-fragments`|[terms-differenciation](https://ns.inria.fr/olivaw#terms-differenciation)|Too close terms|[Jump](#minorfail-outcome-number-55)|

***

## MinorFail Outcomes Details

This subchapter gives more details to the :exclamation:MinorFail outcomes

### MinorFail Outcome number 1

[Jump to summary definition](#summary-MinorFail-1)	|	Previous MinorFail outcome	|	[Next MinorFail outcome](#minorfail-outcome-number-2)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-src-regulation-modelet-logistics-create-organization|
|----|----|
|Title|Merged&#32;module&#32;src/regulation.ttl&#32;from&#32;branch&#32;HEAD&#32;with&#32;related&#32;terms&#32;from&#32;the&#32;fragments&#32;domains/logistics/create-organization/onto.ttl|
|Composition|- [Modelet logistics/create-organization](https://github.com/HyperAgents/hmas/blob/HEAD/domains/logistics/create-organization/onto.ttl)<br/>- [Module regulation](https://github.com/HyperAgents/hmas/blob/HEAD/src/regulation.ttl)|

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
|Name|module-src-regulation-modelet-logistics-coordinate-activities|
|----|----|
|Title|Merged&#32;module&#32;src/regulation.ttl&#32;from&#32;branch&#32;HEAD&#32;with&#32;related&#32;terms&#32;from&#32;the&#32;fragments&#32;domains/logistics/coordinate-activities/onto.ttl|
|Composition|- [Modelet logistics/coordinate-activities](https://github.com/HyperAgents/hmas/blob/HEAD/domains/logistics/coordinate-activities/onto.ttl)<br/>- [Module regulation](https://github.com/HyperAgents/hmas/blob/HEAD/src/regulation.ttl)|

#### Criterion detail
|Identifier|[terms-differenciation](https://ns.inria.fr/olivaw#terms-differenciation)|
|----|----|
|Title|Terms&#32;differenciation&#32;test|
|Description|A&#32;test&#32;case&#32;from&#32;the&#32;Best&#32;Practices&#32;tests&#32;checking&#32;if&#32;all&#32;the&#32;terms&#32;are&#32;different&#32;enough&#32;from&#32;each&#32;other&#32;according&#32;to&#32;the&#32;Levenshtein&#32;distance&#32;metric.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-2)|Identifier|`too-close-terms`|
|[Section top](#minorfail-outcome-number-2)|Title|Too&#32;close&#32;terms|
|[Section top](#minorfail-outcome-number-2)|Description|Some&#32;terms&#32;are&#32;too&#32;similar|
|[Section top](#minorfail-outcome-number-2)|Pointer|<pre lang="Turtle"><code>:isAccessTo&#32;a&#32;owl:ObjectProperty&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;is&#32;access&#32;to&#34;@en,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#34;est&#32;l'accès&#32;à&#34;@fr&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;A&#32;relation&#32;that&#32;refers&#32;to&#32;an&#32;Artifact&#32;involved&#32;in&#32;an&#32;Access.&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:domain&#32;:Access&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32;:regulation&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:range&#32;:Artifact&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-2)|Pointer|<pre lang="Turtle"><code>:isAccessOf&#32;a&#32;owl:ObjectProperty&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;is&#32;access&#32;of&#34;@en,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#34;est&#32;l'accès&#32;de&#34;@fr&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;A&#32;relation&#32;that&#32;refers&#32;to&#32;an&#32;Agent&#32;involved&#32;in&#32;an&#32;Access.&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:domain&#32;:Access&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32;:regulation&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:range&#32;:Agent&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-2)|Pointer|<pre lang="Turtle"><code>:isAccessFor&#32;a&#32;owl:ObjectProperty&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;is&#32;access&#32;for&#34;@en,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#34;est&#32;l'accès&#32;pour&#34;@fr&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;A&#32;relation&#32;that&#32;refers&#32;to&#32;a&#32;Usage&#32;involved&#32;in&#32;an&#32;Access.&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:domain&#32;:Access&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32;:regulation&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:range&#32;:Usage&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-2)|Pointer|<pre lang="Turtle"><code>:isMembershipOf&#32;a&#32;owl:ObjectProperty&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;is&#32;membership&#32;of&#34;@en,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#34;est&#32;l'appartenance&#32;à&#34;@fr&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;A&#32;relation&#32;that&#32;refers&#32;to&#32;the&#32;Agent&#32;involved&#32;in&#32;a&#32;Membership...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:domain&#32;:Membership&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32;:regulation&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:range&#32;:Agent&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-2)|Pointer|<pre lang="Turtle"><code>:isMembershipIn&#32;a&#32;owl:ObjectProperty&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;is&#32;membership&#32;in&#34;@en,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#34;est&#32;l'appartenance&#32;à&#34;@fr&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;A&#32;relation&#32;that&#32;refers&#32;to&#32;the&#32;Group&#32;involved&#32;in&#32;a&#32;Membership...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:domain&#32;:Membership&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32;:regulation&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:range&#32;:Group&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-2)|Pointer|<pre lang="Turtle"><code>:isUsageOf&#32;a&#32;owl:ObjectProperty&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;is&#32;usage&#32;of&#34;@en,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#34;est&#32;un&#32;usage&#32;de&#34;@fr&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;A&#32;relation&#32;that&#32;refers&#32;to&#32;a&#32;Facility&#32;involved&#32;in&#32;a&#32;Usage.&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:domain&#32;:Usage&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32;:regulation&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:range&#32;:Facility&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-2)|Pointer|<pre lang="Turtle"><code>:isUsageIn&#32;a&#32;owl:ObjectProperty&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;is&#32;usage&#32;in&#34;@en,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#34;est&#32;un&#32;usage&#32;dans&#34;@fr&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;A&#32;relation&#32;that&#32;refers&#32;to&#32;a&#32;Setting&#32;involved&#32;in&#32;a&#32;Usage.&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:domain&#32;:Usage&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32;:regulation&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:range&#32;:Setting&#32;.</code></pre>|

***
### MinorFail Outcome number 3

[Jump to summary definition](#summary-MinorFail-3)	|	[Previous MinorFail outcome](#minorfail-outcome-number-2)	|	[Next MinorFail outcome](#minorfail-outcome-number-4)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-src-regulation-modelet-logistics-configure-organization|
|----|----|
|Title|Merged&#32;module&#32;src/regulation.ttl&#32;from&#32;branch&#32;HEAD&#32;with&#32;related&#32;terms&#32;from&#32;the&#32;fragments&#32;domains/logistics/configure-organization/onto.ttl|
|Composition|- [Modelet logistics/configure-organization](https://github.com/HyperAgents/hmas/blob/HEAD/domains/logistics/configure-organization/onto.ttl)<br/>- [Module regulation](https://github.com/HyperAgents/hmas/blob/HEAD/src/regulation.ttl)|

#### Criterion detail
|Identifier|[terms-differenciation](https://ns.inria.fr/olivaw#terms-differenciation)|
|----|----|
|Title|Terms&#32;differenciation&#32;test|
|Description|A&#32;test&#32;case&#32;from&#32;the&#32;Best&#32;Practices&#32;tests&#32;checking&#32;if&#32;all&#32;the&#32;terms&#32;are&#32;different&#32;enough&#32;from&#32;each&#32;other&#32;according&#32;to&#32;the&#32;Levenshtein&#32;distance&#32;metric.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-3)|Identifier|`too-close-terms`|
|[Section top](#minorfail-outcome-number-3)|Title|Too&#32;close&#32;terms|
|[Section top](#minorfail-outcome-number-3)|Description|Some&#32;terms&#32;are&#32;too&#32;similar|
|[Section top](#minorfail-outcome-number-3)|Pointer|<pre lang="Turtle"><code>:isAccessTo&#32;a&#32;owl:ObjectProperty&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;is&#32;access&#32;to&#34;@en,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#34;est&#32;l'accès&#32;à&#34;@fr&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;A&#32;relation&#32;that&#32;refers&#32;to&#32;an&#32;Artifact&#32;involved&#32;in&#32;an&#32;Access.&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:domain&#32;:Access&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32;:regulation&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:range&#32;:Artifact&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-3)|Pointer|<pre lang="Turtle"><code>:isAccessOf&#32;a&#32;owl:ObjectProperty&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;is&#32;access&#32;of&#34;@en,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#34;est&#32;l'accès&#32;de&#34;@fr&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;A&#32;relation&#32;that&#32;refers&#32;to&#32;an&#32;Agent&#32;involved&#32;in&#32;an&#32;Access.&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:domain&#32;:Access&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32;:regulation&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:range&#32;:Agent&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-3)|Pointer|<pre lang="Turtle"><code>:isAccessFor&#32;a&#32;owl:ObjectProperty&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;is&#32;access&#32;for&#34;@en,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#34;est&#32;l'accès&#32;pour&#34;@fr&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;A&#32;relation&#32;that&#32;refers&#32;to&#32;a&#32;Usage&#32;involved&#32;in&#32;an&#32;Access.&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:domain&#32;:Access&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32;:regulation&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:range&#32;:Usage&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-3)|Pointer|<pre lang="Turtle"><code>:isMembershipOf&#32;a&#32;owl:ObjectProperty&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;is&#32;membership&#32;of&#34;@en,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#34;est&#32;l'appartenance&#32;à&#34;@fr&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;A&#32;relation&#32;that&#32;refers&#32;to&#32;the&#32;Agent&#32;involved&#32;in&#32;a&#32;Membership...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:domain&#32;:Membership&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32;:regulation&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:range&#32;:Agent&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-3)|Pointer|<pre lang="Turtle"><code>:isMembershipIn&#32;a&#32;owl:ObjectProperty&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;is&#32;membership&#32;in&#34;@en,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#34;est&#32;l'appartenance&#32;à&#34;@fr&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;A&#32;relation&#32;that&#32;refers&#32;to&#32;the&#32;Group&#32;involved&#32;in&#32;a&#32;Membership...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:domain&#32;:Membership&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32;:regulation&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:range&#32;:Group&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-3)|Pointer|<pre lang="Turtle"><code>:isUsageOf&#32;a&#32;owl:ObjectProperty&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;is&#32;usage&#32;of&#34;@en,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#34;est&#32;un&#32;usage&#32;de&#34;@fr&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;A&#32;relation&#32;that&#32;refers&#32;to&#32;a&#32;Facility&#32;involved&#32;in&#32;a&#32;Usage.&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:domain&#32;:Usage&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32;:regulation&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:range&#32;:Facility&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-3)|Pointer|<pre lang="Turtle"><code>:isUsageIn&#32;a&#32;owl:ObjectProperty&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;is&#32;usage&#32;in&#34;@en,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#34;est&#32;un&#32;usage&#32;dans&#34;@fr&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;A&#32;relation&#32;that&#32;refers&#32;to&#32;a&#32;Setting&#32;involved&#32;in&#32;a&#32;Usage.&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:domain&#32;:Usage&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32;:regulation&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:range&#32;:Setting&#32;.</code></pre>|

***
### MinorFail Outcome number 4

[Jump to summary definition](#summary-MinorFail-4)	|	[Previous MinorFail outcome](#minorfail-outcome-number-3)	|	[Next MinorFail outcome](#minorfail-outcome-number-5)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-src-regulation|
|----|----|
|Title|Standalone&#32;module&#32;src/regulation.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Module regulation](https://github.com/HyperAgents/hmas/blob/HEAD/src/regulation.ttl)|

#### Criterion detail
|Identifier|[terms-differenciation](https://ns.inria.fr/olivaw#terms-differenciation)|
|----|----|
|Title|Terms&#32;differenciation&#32;test|
|Description|A&#32;test&#32;case&#32;from&#32;the&#32;Best&#32;Practices&#32;tests&#32;checking&#32;if&#32;all&#32;the&#32;terms&#32;are&#32;different&#32;enough&#32;from&#32;each&#32;other&#32;according&#32;to&#32;the&#32;Levenshtein&#32;distance&#32;metric.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-4)|Identifier|`too-close-terms`|
|[Section top](#minorfail-outcome-number-4)|Title|Too&#32;close&#32;terms|
|[Section top](#minorfail-outcome-number-4)|Description|Some&#32;terms&#32;are&#32;too&#32;similar|
|[Section top](#minorfail-outcome-number-4)|Pointer|<pre lang="Turtle"><code>:isAccessTo&#32;a&#32;owl:ObjectProperty&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;is&#32;access&#32;to&#34;@en,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#34;est&#32;l'accès&#32;à&#34;@fr&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;A&#32;relation&#32;that&#32;refers&#32;to&#32;an&#32;Artifact&#32;involved&#32;in&#32;an&#32;Access.&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:domain&#32;:Access&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32;:regulation&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:range&#32;:Artifact&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-4)|Pointer|<pre lang="Turtle"><code>:isAccessOf&#32;a&#32;owl:ObjectProperty&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;is&#32;access&#32;of&#34;@en,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#34;est&#32;l'accès&#32;de&#34;@fr&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;A&#32;relation&#32;that&#32;refers&#32;to&#32;an&#32;Agent&#32;involved&#32;in&#32;an&#32;Access.&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:domain&#32;:Access&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32;:regulation&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:range&#32;:Agent&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-4)|Pointer|<pre lang="Turtle"><code>:isAccessFor&#32;a&#32;owl:ObjectProperty&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;is&#32;access&#32;for&#34;@en,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#34;est&#32;l'accès&#32;pour&#34;@fr&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;A&#32;relation&#32;that&#32;refers&#32;to&#32;a&#32;Usage&#32;involved&#32;in&#32;an&#32;Access.&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:domain&#32;:Access&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32;:regulation&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:range&#32;:Usage&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-4)|Pointer|<pre lang="Turtle"><code>:isMembershipOf&#32;a&#32;owl:ObjectProperty&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;is&#32;membership&#32;of&#34;@en,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#34;est&#32;l'appartenance&#32;à&#34;@fr&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;A&#32;relation&#32;that&#32;refers&#32;to&#32;the&#32;Agent&#32;involved&#32;in&#32;a&#32;Membership...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:domain&#32;:Membership&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32;:regulation&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:range&#32;:Agent&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-4)|Pointer|<pre lang="Turtle"><code>:isMembershipIn&#32;a&#32;owl:ObjectProperty&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;is&#32;membership&#32;in&#34;@en,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#34;est&#32;l'appartenance&#32;à&#34;@fr&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;A&#32;relation&#32;that&#32;refers&#32;to&#32;the&#32;Group&#32;involved&#32;in&#32;a&#32;Membership...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:domain&#32;:Membership&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32;:regulation&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:range&#32;:Group&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-4)|Pointer|<pre lang="Turtle"><code>:isUsageOf&#32;a&#32;owl:ObjectProperty&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;is&#32;usage&#32;of&#34;@en,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#34;est&#32;un&#32;usage&#32;de&#34;@fr&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;A&#32;relation&#32;that&#32;refers&#32;to&#32;a&#32;Facility&#32;involved&#32;in&#32;a&#32;Usage.&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:domain&#32;:Usage&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32;:regulation&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:range&#32;:Facility&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-4)|Pointer|<pre lang="Turtle"><code>:isUsageIn&#32;a&#32;owl:ObjectProperty&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;is&#32;usage&#32;in&#34;@en,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#34;est&#32;un&#32;usage&#32;dans&#34;@fr&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;A&#32;relation&#32;that&#32;refers&#32;to&#32;a&#32;Setting&#32;involved&#32;in&#32;a&#32;Usage.&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:domain&#32;:Usage&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32;:regulation&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:range&#32;:Setting&#32;.</code></pre>|

***
### MinorFail Outcome number 5

[Jump to summary definition](#summary-MinorFail-5)	|	[Previous MinorFail outcome](#minorfail-outcome-number-4)	|	[Next MinorFail outcome](#minorfail-outcome-number-6)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-src-fipa|
|----|----|
|Title|Standalone&#32;module&#32;src/fipa.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Module fipa](https://github.com/HyperAgents/hmas/blob/HEAD/src/fipa.ttl)|

#### Criterion detail
|Identifier|[term-referencing](https://ns.inria.fr/olivaw#term-referencing)|
|----|----|
|Title|Term&#32;referencing&#32;test|
|Description|A&#32;test&#32;case&#32;from&#32;the&#32;Best&#32;Practices&#32;tests&#32;checking&#32;if&#32;each&#32;term&#32;of&#32;the&#32;test&#32;subject&#32;is&#32;referenced&#32;to&#32;a&#32;module&#32;through&#32;a&#32;rdfs:isDefinedBy&#32;property.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-5)|Identifier|`no-reference-module`|
|[Section top](#minorfail-outcome-number-5)|Title|Term&#32;not&#32;referenced&#32;to&#32;a&#32;module|
|[Section top](#minorfail-outcome-number-5)|Description|Subject&#32;terms&#32;not&#32;linked&#32;to&#32;a&#32;module&#32;by&#32;a&#32;rdfs:isDefinedBy&#32;property|
|[Section top](#minorfail-outcome-number-5)|Pointer|<pre lang="Turtle"><code>:hasServiceName&#32;a&#32;owl:ObjectProperty&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;has&#32;Service&#32;Name&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:domain&#32;:APService&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-5)|Pointer|<pre lang="Turtle"><code>:APService&#32;a&#32;owl:Class&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;Agent&#32;Platform&#32;Service&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;A&#32;service&#32;exposed&#32;by&#32;a&#32;FIPA&#32;Agent&#32;Platform&#32;as&#32;defined&#32;by&#32;the...&#34; &#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-5)|Pointer|<pre lang="Turtle"><code>:hasServiceType&#32;a&#32;owl:ObjectProperty&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;has&#32;Service&#32;Type&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:domain&#32;:APService&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-5)|Pointer|<pre lang="Turtle"><code>:AgentIdentifierDescription&#32;a&#32;owl:Class&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;Agent&#32;Identifier&#32;Description&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;A&#32;resource&#32;profile&#32;that&#32;describes&#32;an&#32;agent&#32;using&#32;the&#32;Agent&#32;I...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:subClassOf&#32; &#60;https://ci.mines-stetienne.fr/hmas#ResourceProfile> &#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-5)|Pointer|<pre lang="Turtle"><code>:AgentPlatformDescription&#32;a&#32;owl:Class&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;Agent&#32;Platform&#32;Description&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;A&#32;resource&#32;profile&#32;that&#32;descripe&#32;a&#32;FIPA&#32;Agent&#32;Platform&#32;using...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:subClassOf&#32; &#60;https://ci.mines-stetienne.fr/hmas#ResourceProfile> &#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-5)|Pointer|<pre lang="Turtle"><code>:FIPAAgentPlatform&#32;a&#32;owl:Class&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;FIPA&#32;Agent&#32;Platform&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;A&#32;platform&#32;that&#32;conforms&#32;to&#32;the&#32;FIPA&#32;Abstract&#32;Architecture&#32;S...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:subClassOf&#32; &#60;https://ci.mines-stetienne.fr/hmas#Platform> &#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-5)|Pointer|<pre lang="Turtle"><code>:HTTPMessageTransportService&#32;a&#32;owl:Class&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;HTTP&#32;Message&#32;Transport&#32;Service&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;An&#32;HTTP-based&#32;message&#32;transport&#32;service&#32;that&#32;confirms&#32;to&#32;the...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:subClassOf&#32;:MessageTransportService&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-5)|Pointer|<pre lang="Turtle"><code>:MessageTransportService&#32;a&#32;owl:Class&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;Message&#32;Transport&#32;Service&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;A&#32;service&#32;for&#32;transporting&#32;messages&#32;among&#32;agents&#32;that&#32;confor...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:subClassOf&#32;:APService&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-5)|Pointer|<pre lang="Turtle"><code>:IIOPMessageTransportService&#32;a&#32;owl:Class&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;IIOP&#32;Message&#32;Transport&#32;Service&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;An&#32;HTTP-based&#32;message&#32;transport&#32;service&#32;that&#32;confirms&#32;to&#32;the...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:subClassOf&#32;:MessageTransportService&#32;.</code></pre>|

***
### MinorFail Outcome number 6

[Jump to summary definition](#summary-MinorFail-6)	|	[Previous MinorFail outcome](#minorfail-outcome-number-5)	|	[Next MinorFail outcome](#minorfail-outcome-number-7)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-src-core-modelet-manufacturing-environments-discover-signifiers|
|----|----|
|Title|Merged&#32;module&#32;src/core.ttl&#32;from&#32;branch&#32;HEAD&#32;with&#32;related&#32;terms&#32;from&#32;the&#32;fragments&#32;domains/manufacturing-environments/discover-signifiers/onto.ttl|
|Composition|- [Modelet manufacturing-environments/discover-signifiers](https://github.com/HyperAgents/hmas/blob/HEAD/domains/manufacturing-environments/discover-signifiers/onto.ttl)<br/>- [Module core](https://github.com/HyperAgents/hmas/blob/HEAD/src/core.ttl)|

#### Criterion detail
|Identifier|[labeled-terms](https://ns.inria.fr/olivaw#labeled-terms)|
|----|----|
|Title|Term&#32;labeling&#32;test|
|Description|A&#32;test&#32;case&#32;from&#32;the&#32;Best&#32;Practices&#32;tests&#32;checking&#32;if&#32;all&#32;the&#32;terms&#32;of&#32;the&#32;subject&#32;have&#32;a&#32;rdfs:label&#32;property&#32;pointing&#32;to&#32;a&#32;literal&#32;in&#32;English|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-6)|Identifier|`not-labeled-term`|
|[Section top](#minorfail-outcome-number-6)|Title|Terms&#32;not&#32;labeled|
|[Section top](#minorfail-outcome-number-6)|Description|The&#32;following&#32;terms&#32;have&#32;no&#32;rdfs:label&#32;to&#32;define&#32;it&#32;in&#32;natural&#32;language|
|[Section top](#minorfail-outcome-number-6)|Pointer|<pre lang="Turtle"><code>:Affordance&#32;a&#32;skos:Concept&#32;;  &#10; &#32; &#32; &#32; &#32;dc:references&#32; &#91;&#32;a&#32;owl:NamedIndividual&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;Chemero&#32;and&#32;Turvey,&#32;2007&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;dc:bibliographicCitation&#32; &#34;Chemero,&#32;A.,&#32;&&#32;Turvey,&#32;M.&#32;T.&#32;(2007).&#32;Complexity,&#32;hypersets,&#32;...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;dc:identifier&#32; &#60;https://doi.org/10.1162/biot.2007.2.1.23> &#32;],  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#91;&#32;a&#32;owl:NamedIndividual&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;Norman,&#32;2013&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;dc:bibliographicCitation&#32; &#34;Norman,&#32;D.&#32;(2013).&#32;The&#32;design&#32;of&#32;everyday&#32;things:&#32;Revised&#32;an...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;dc:identifier&#32; &#60;https://mitpress.mit.edu/9780262640374/> &#32;],  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#91;&#32;rdfs:label&#32; &#34;Chemero&#32;and&#32;Turvey,&#32;2007&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;dc:bibliographicCitation&#32; &#34;Chemero,&#32;A.,&#32;&&#32;Turvey,&#32;M.&#32;T.&#32;(2007).&#32;Complexity,&#32;hypersets,&#32;...&#34; &#32;],  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#91;&#32;rdfs:label&#32; &#34;Norman,&#32;2013&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;dc:bibliographicCitation&#32; &#34;Norman,&#32;D.&#32;(2013).&#32;The&#32;design&#32;of&#32;everyday&#32;things:&#32;Revised&#32;an...&#34; &#32;]&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32;:core&#32;;  &#10; &#32; &#32; &#32; &#32;skos:definition&#32; &#34;A&#32;behavior&#32;possibility&#32;that&#32;is&#32;a&#32;relationship&#32;between&#32;an&#32;abi...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;skos:editorialNote&#32; &#34;The&#32;concept&#32;has&#32;been&#32;considered&#32;as&#32;a&#32;candidate&#32;term&#32;for&#32;repr...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;skos:historyNote&#32; &#34;The&#32;definition&#32;of&#32;the&#32;concept&#32;follows&#32;affordance&#32;theorists&#32; &#91;...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;skos:prefLabel&#32; &#34;affordance&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;skos:related&#32;:Signifier&#32;.</code></pre>|

***
### MinorFail Outcome number 7

[Jump to summary definition](#summary-MinorFail-7)	|	[Previous MinorFail outcome](#minorfail-outcome-number-6)	|	[Next MinorFail outcome](#minorfail-outcome-number-8)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-src-core-modelet-manufacturing-environments-discover-signifiers|
|----|----|
|Title|Merged&#32;module&#32;src/core.ttl&#32;from&#32;branch&#32;HEAD&#32;with&#32;related&#32;terms&#32;from&#32;the&#32;fragments&#32;domains/manufacturing-environments/discover-signifiers/onto.ttl|
|Composition|- [Modelet manufacturing-environments/discover-signifiers](https://github.com/HyperAgents/hmas/blob/HEAD/domains/manufacturing-environments/discover-signifiers/onto.ttl)<br/>- [Module core](https://github.com/HyperAgents/hmas/blob/HEAD/src/core.ttl)|

#### Criterion detail
|Identifier|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|
|----|----|
|Title|Profile&#32;compatibility&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;check&#32;whether&#32;the&#32;test&#32;subject&#32;is&#32;compatible&#32;with&#32;a&#32;profile&#32;or&#32;not,&#32;and&#32;if&#32;it&#32;is&#32;not,&#32;why.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-7)|Identifier|`owl-el-profile-error`|
|[Section top](#minorfail-outcome-number-7)|Title|OWL&#32;EL&#32;Profile&#32;incompatible|
|[Section top](#minorfail-outcome-number-7)|Description|Anonymous&#32;individuals&#32;are&#32;not&#32;supported|
|[Section top](#minorfail-outcome-number-7)|Pointer|<pre lang="Turtle"><code>&#91;]&#32;a&#32;owl:NamedIndividual&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;Chemero&#32;and&#32;Turvey,&#32;2007&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;dc:bibliographicCitation&#32; &#34;Chemero,&#32;A.,&#32;&&#32;Turvey,&#32;M.&#32;T.&#32;(2007).&#32;Complexity,&#32;hypersets,&#32;...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;dc:identifier&#32; &#60;https://doi.org/10.1162/biot.2007.2.1.23> &#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-7)|Pointer|<pre lang="Turtle"><code>&#91;]&#32;a&#32;owl:NamedIndividual&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;Norman,&#32;2013&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;dc:bibliographicCitation&#32; &#34;Norman,&#32;D.&#32;(2013).&#32;The&#32;design&#32;of&#32;everyday&#32;things:&#32;Revised&#32;an...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;dc:identifier&#32; &#60;https://mitpress.mit.edu/9780262640374/> &#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-7)|Pointer|<pre lang="Turtle"><code>&#91;]&#32;rdfs:label&#32; &#34;Chemero&#32;and&#32;Turvey,&#32;2007&#34;@en&#32;;  &#10; &#32; &#32;&#32; &#32;dc:bibliographicCitation&#32; &#34;Chemero,&#32;A.,&#32;&&#32;Turvey,&#32;M.&#32;T.&#32;(2007).&#32;Complexity,&#32;hypersets,&#32;...&#34; &#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-7)|Pointer|<pre lang="Turtle"><code>&#91;]&#32;rdfs:label&#32; &#34;Norman,&#32;2013&#34;@en&#32;;  &#10; &#32; &#32;&#32; &#32;dc:bibliographicCitation&#32; &#34;Norman,&#32;D.&#32;(2013).&#32;The&#32;design&#32;of&#32;everyday&#32;things:&#32;Revised&#32;an...&#34; &#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-7)|Pointer|<pre lang="Turtle"><code>hmas:Affordance&#32;a&#32;skos:Concept&#32;;  &#10; &#32; &#32; &#32; &#32;dc:references&#32; &#91;&#32;a&#32;owl:NamedIndividual&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;Chemero&#32;and&#32;Turvey,&#32;2007&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;dc:bibliographicCitation&#32; &#34;Chemero,&#32;A.,&#32;&&#32;Turvey,&#32;M.&#32;T.&#32;(2007).&#32;Complexity,&#32;hypersets,&#32;...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;dc:identifier&#32; &#60;https://doi.org/10.1162/biot.2007.2.1.23> &#32;],  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#91;&#32;a&#32;owl:NamedIndividual&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;Norman,&#32;2013&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;dc:bibliographicCitation&#32; &#34;Norman,&#32;D.&#32;(2013).&#32;The&#32;design&#32;of&#32;everyday&#32;things:&#32;Revised&#32;an...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;dc:identifier&#32; &#60;https://mitpress.mit.edu/9780262640374/> &#32;],  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#91;&#32;rdfs:label&#32; &#34;Chemero&#32;and&#32;Turvey,&#32;2007&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;dc:bibliographicCitation&#32; &#34;Chemero,&#32;A.,&#32;&&#32;Turvey,&#32;M.&#32;T.&#32;(2007).&#32;Complexity,&#32;hypersets,&#32;...&#34; &#32;],  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#91;&#32;rdfs:label&#32; &#34;Norman,&#32;2013&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;dc:bibliographicCitation&#32; &#34;Norman,&#32;D.&#32;(2013).&#32;The&#32;design&#32;of&#32;everyday&#32;things:&#32;Revised&#32;an...&#34; &#32;]&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32;hmas:core&#32;;  &#10; &#32; &#32; &#32; &#32;skos:definition&#32; &#34;A&#32;behavior&#32;possibility&#32;that&#32;is&#32;a&#32;relationship&#32;between&#32;an&#32;abi...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;skos:editorialNote&#32; &#34;The&#32;concept&#32;has&#32;been&#32;considered&#32;as&#32;a&#32;candidate&#32;term&#32;for&#32;repr...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;skos:historyNote&#32; &#34;The&#32;definition&#32;of&#32;the&#32;concept&#32;follows&#32;affordance&#32;theorists&#32; &#91;...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;skos:prefLabel&#32; &#34;affordance&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;skos:related&#32;hmas:Signifier&#32;.</code></pre>|

***
### MinorFail Outcome number 8

[Jump to summary definition](#summary-MinorFail-8)	|	[Previous MinorFail outcome](#minorfail-outcome-number-7)	|	[Next MinorFail outcome](#minorfail-outcome-number-9)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-src-core-modelet-manufacturing-environments-discover-signifiers|
|----|----|
|Title|Merged&#32;module&#32;src/core.ttl&#32;from&#32;branch&#32;HEAD&#32;with&#32;related&#32;terms&#32;from&#32;the&#32;fragments&#32;domains/manufacturing-environments/discover-signifiers/onto.ttl|
|Composition|- [Modelet manufacturing-environments/discover-signifiers](https://github.com/HyperAgents/hmas/blob/HEAD/domains/manufacturing-environments/discover-signifiers/onto.ttl)<br/>- [Module core](https://github.com/HyperAgents/hmas/blob/HEAD/src/core.ttl)|

#### Criterion detail
|Identifier|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|
|----|----|
|Title|Profile&#32;compatibility&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;check&#32;whether&#32;the&#32;test&#32;subject&#32;is&#32;compatible&#32;with&#32;a&#32;profile&#32;or&#32;not,&#32;and&#32;if&#32;it&#32;is&#32;not,&#32;why.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-8)|Identifier|`owl-el-profile-error`|
|[Section top](#minorfail-outcome-number-8)|Title|OWL&#32;EL&#32;Profile&#32;incompatible|
|[Section top](#minorfail-outcome-number-8)|Description|Statement&#32;not&#32;supported|
|[Section top](#minorfail-outcome-number-8)|Pointer|<pre lang="Turtle"><code>hmas:hasProfile&#32;a&#32;owl:AsymmetricProperty,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:ObjectProperty&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;has&#32;for&#32;profile&#34;@en,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#34;a&#32;pour&#32;profil&#34;@fr&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;A&#32;relation&#32;that&#32;links&#32;a&#32;resource&#32;to&#32;its&#32;profile.&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32;hmas:core&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:range&#32;hmas:ResourceProfile&#32;;  &#10; &#32; &#32; &#32; &#32;owl:inverseOf&#32;hmas:isProfileOf&#32;.</code></pre>|

***
### MinorFail Outcome number 9

[Jump to summary definition](#summary-MinorFail-9)	|	[Previous MinorFail outcome](#minorfail-outcome-number-8)	|	[Next MinorFail outcome](#minorfail-outcome-number-10)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-src-core-modelet-manufacturing-environments-discover-signifiers|
|----|----|
|Title|Merged&#32;module&#32;src/core.ttl&#32;from&#32;branch&#32;HEAD&#32;with&#32;related&#32;terms&#32;from&#32;the&#32;fragments&#32;domains/manufacturing-environments/discover-signifiers/onto.ttl|
|Composition|- [Modelet manufacturing-environments/discover-signifiers](https://github.com/HyperAgents/hmas/blob/HEAD/domains/manufacturing-environments/discover-signifiers/onto.ttl)<br/>- [Module core](https://github.com/HyperAgents/hmas/blob/HEAD/src/core.ttl)|

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
|[Section top](#minorfail-outcome-number-9)|Description|Anonymous&#32;individuals&#32;are&#32;not&#32;supported|
|[Section top](#minorfail-outcome-number-9)|Pointer|<pre lang="Turtle"><code>&#91;]&#32;a&#32;owl:NamedIndividual&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;Chemero&#32;and&#32;Turvey,&#32;2007&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;dc:bibliographicCitation&#32; &#34;Chemero,&#32;A.,&#32;&&#32;Turvey,&#32;M.&#32;T.&#32;(2007).&#32;Complexity,&#32;hypersets,&#32;...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;dc:identifier&#32; &#60;https://doi.org/10.1162/biot.2007.2.1.23> &#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-9)|Pointer|<pre lang="Turtle"><code>&#91;]&#32;a&#32;owl:NamedIndividual&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;Norman,&#32;2013&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;dc:bibliographicCitation&#32; &#34;Norman,&#32;D.&#32;(2013).&#32;The&#32;design&#32;of&#32;everyday&#32;things:&#32;Revised&#32;an...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;dc:identifier&#32; &#60;https://mitpress.mit.edu/9780262640374/> &#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-9)|Pointer|<pre lang="Turtle"><code>&#91;]&#32;rdfs:label&#32; &#34;Chemero&#32;and&#32;Turvey,&#32;2007&#34;@en&#32;;  &#10; &#32; &#32;&#32; &#32;dc:bibliographicCitation&#32; &#34;Chemero,&#32;A.,&#32;&&#32;Turvey,&#32;M.&#32;T.&#32;(2007).&#32;Complexity,&#32;hypersets,&#32;...&#34; &#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-9)|Pointer|<pre lang="Turtle"><code>&#91;]&#32;rdfs:label&#32; &#34;Norman,&#32;2013&#34;@en&#32;;  &#10; &#32; &#32;&#32; &#32;dc:bibliographicCitation&#32; &#34;Norman,&#32;D.&#32;(2013).&#32;The&#32;design&#32;of&#32;everyday&#32;things:&#32;Revised&#32;an...&#34; &#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-9)|Pointer|<pre lang="Turtle"><code>hmas:Affordance&#32;a&#32;skos:Concept&#32;;  &#10; &#32; &#32; &#32; &#32;dc:references&#32; &#91;&#32;a&#32;owl:NamedIndividual&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;Chemero&#32;and&#32;Turvey,&#32;2007&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;dc:bibliographicCitation&#32; &#34;Chemero,&#32;A.,&#32;&&#32;Turvey,&#32;M.&#32;T.&#32;(2007).&#32;Complexity,&#32;hypersets,&#32;...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;dc:identifier&#32; &#60;https://doi.org/10.1162/biot.2007.2.1.23> &#32;],  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#91;&#32;a&#32;owl:NamedIndividual&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;Norman,&#32;2013&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;dc:bibliographicCitation&#32; &#34;Norman,&#32;D.&#32;(2013).&#32;The&#32;design&#32;of&#32;everyday&#32;things:&#32;Revised&#32;an...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;dc:identifier&#32; &#60;https://mitpress.mit.edu/9780262640374/> &#32;],  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#91;&#32;rdfs:label&#32; &#34;Chemero&#32;and&#32;Turvey,&#32;2007&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;dc:bibliographicCitation&#32; &#34;Chemero,&#32;A.,&#32;&&#32;Turvey,&#32;M.&#32;T.&#32;(2007).&#32;Complexity,&#32;hypersets,&#32;...&#34; &#32;],  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#91;&#32;rdfs:label&#32; &#34;Norman,&#32;2013&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;dc:bibliographicCitation&#32; &#34;Norman,&#32;D.&#32;(2013).&#32;The&#32;design&#32;of&#32;everyday&#32;things:&#32;Revised&#32;an...&#34; &#32;]&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32;hmas:core&#32;;  &#10; &#32; &#32; &#32; &#32;skos:definition&#32; &#34;A&#32;behavior&#32;possibility&#32;that&#32;is&#32;a&#32;relationship&#32;between&#32;an&#32;abi...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;skos:editorialNote&#32; &#34;The&#32;concept&#32;has&#32;been&#32;considered&#32;as&#32;a&#32;candidate&#32;term&#32;for&#32;repr...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;skos:historyNote&#32; &#34;The&#32;definition&#32;of&#32;the&#32;concept&#32;follows&#32;affordance&#32;theorists&#32; &#91;...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;skos:prefLabel&#32; &#34;affordance&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;skos:related&#32;hmas:Signifier&#32;.</code></pre>|

***
### MinorFail Outcome number 10

[Jump to summary definition](#summary-MinorFail-10)	|	[Previous MinorFail outcome](#minorfail-outcome-number-9)	|	[Next MinorFail outcome](#minorfail-outcome-number-11)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-src-core-modelet-manufacturing-environments-discover-signifiers|
|----|----|
|Title|Merged&#32;module&#32;src/core.ttl&#32;from&#32;branch&#32;HEAD&#32;with&#32;related&#32;terms&#32;from&#32;the&#32;fragments&#32;domains/manufacturing-environments/discover-signifiers/onto.ttl|
|Composition|- [Modelet manufacturing-environments/discover-signifiers](https://github.com/HyperAgents/hmas/blob/HEAD/domains/manufacturing-environments/discover-signifiers/onto.ttl)<br/>- [Module core](https://github.com/HyperAgents/hmas/blob/HEAD/src/core.ttl)|

#### Criterion detail
|Identifier|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|
|----|----|
|Title|Profile&#32;compatibility&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;check&#32;whether&#32;the&#32;test&#32;subject&#32;is&#32;compatible&#32;with&#32;a&#32;profile&#32;or&#32;not,&#32;and&#32;if&#32;it&#32;is&#32;not,&#32;why.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-10)|Identifier|`owl-ql-profile-error`|
|[Section top](#minorfail-outcome-number-10)|Title|OWL&#32;QL&#32;Profile&#32;incompatible|
|[Section top](#minorfail-outcome-number-10)|Description|Statement&#32;not&#32;supported|
|[Section top](#minorfail-outcome-number-10)|Pointer|<pre lang="Turtle"><code>hmas:transitivelyContains&#32;a&#32;owl:ObjectProperty,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:TransitiveProperty&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;transitively&#32;contains&#34;@en,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#34;contient&#32;transitivement&#34;@fr&#32;;  &#10; &#32; &#32; &#32; &#32;dc:source&#32; &#60;https://github.com/HyperAgents/ns.hyperagents.org/issues/8#issuecomment-1025991719> &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;Links&#32;all&#32;the&#32;resources&#32;that&#32;are&#32;logically&#32;contained&#32;in&#32;a&#32;wo...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:domain&#32;hmas:Workspace&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32;hmas:core&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:seeAlso&#32; &#60;https://github.com/HyperAgents/ns.hyperagents.org/issues/18>,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#60;https://github.com/HyperAgents/ns.hyperagents.org/issues/39> &#32;;  &#10; &#32; &#32; &#32; &#32;owl:inverseOf&#32;hmas:isTransitivelyContainedIn&#32;.</code></pre>|

***
### MinorFail Outcome number 11

[Jump to summary definition](#summary-MinorFail-11)	|	[Previous MinorFail outcome](#minorfail-outcome-number-10)	|	[Next MinorFail outcome](#minorfail-outcome-number-12)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-src-core-modelet-manufacturing-environments-discover-platforms|
|----|----|
|Title|Merged&#32;module&#32;src/core.ttl&#32;from&#32;branch&#32;HEAD&#32;with&#32;related&#32;terms&#32;from&#32;the&#32;fragments&#32;domains/manufacturing-environments/discover-platforms/onto.ttl|
|Composition|- [Modelet manufacturing-environments/discover-platforms](https://github.com/HyperAgents/hmas/blob/HEAD/domains/manufacturing-environments/discover-platforms/onto.ttl)<br/>- [Module core](https://github.com/HyperAgents/hmas/blob/HEAD/src/core.ttl)|

#### Criterion detail
|Identifier|[labeled-terms](https://ns.inria.fr/olivaw#labeled-terms)|
|----|----|
|Title|Term&#32;labeling&#32;test|
|Description|A&#32;test&#32;case&#32;from&#32;the&#32;Best&#32;Practices&#32;tests&#32;checking&#32;if&#32;all&#32;the&#32;terms&#32;of&#32;the&#32;subject&#32;have&#32;a&#32;rdfs:label&#32;property&#32;pointing&#32;to&#32;a&#32;literal&#32;in&#32;English|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-11)|Identifier|`not-labeled-term`|
|[Section top](#minorfail-outcome-number-11)|Title|Terms&#32;not&#32;labeled|
|[Section top](#minorfail-outcome-number-11)|Description|The&#32;following&#32;terms&#32;have&#32;no&#32;rdfs:label&#32;to&#32;define&#32;it&#32;in&#32;natural&#32;language|
|[Section top](#minorfail-outcome-number-11)|Pointer|<pre lang="Turtle"><code>:Affordance&#32;a&#32;skos:Concept&#32;;  &#10; &#32; &#32; &#32; &#32;dc:references&#32; &#91;&#32;a&#32;owl:NamedIndividual&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;Chemero&#32;and&#32;Turvey,&#32;2007&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;dc:bibliographicCitation&#32; &#34;Chemero,&#32;A.,&#32;&&#32;Turvey,&#32;M.&#32;T.&#32;(2007).&#32;Complexity,&#32;hypersets,&#32;...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;dc:identifier&#32; &#60;https://doi.org/10.1162/biot.2007.2.1.23> &#32;],  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#91;&#32;a&#32;owl:NamedIndividual&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;Norman,&#32;2013&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;dc:bibliographicCitation&#32; &#34;Norman,&#32;D.&#32;(2013).&#32;The&#32;design&#32;of&#32;everyday&#32;things:&#32;Revised&#32;an...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;dc:identifier&#32; &#60;https://mitpress.mit.edu/9780262640374/> &#32;]&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32;:core&#32;;  &#10; &#32; &#32; &#32; &#32;skos:definition&#32; &#34;A&#32;behavior&#32;possibility&#32;that&#32;is&#32;a&#32;relationship&#32;between&#32;an&#32;abi...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;skos:editorialNote&#32; &#34;The&#32;concept&#32;has&#32;been&#32;considered&#32;as&#32;a&#32;candidate&#32;term&#32;for&#32;repr...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;skos:historyNote&#32; &#34;The&#32;definition&#32;of&#32;the&#32;concept&#32;follows&#32;affordance&#32;theorists&#32; &#91;...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;skos:prefLabel&#32; &#34;affordance&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;skos:related&#32;:Signifier&#32;.</code></pre>|

***
### MinorFail Outcome number 12

[Jump to summary definition](#summary-MinorFail-12)	|	[Previous MinorFail outcome](#minorfail-outcome-number-11)	|	[Next MinorFail outcome](#minorfail-outcome-number-13)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-src-core-modelet-manufacturing-environments-discover-platforms|
|----|----|
|Title|Merged&#32;module&#32;src/core.ttl&#32;from&#32;branch&#32;HEAD&#32;with&#32;related&#32;terms&#32;from&#32;the&#32;fragments&#32;domains/manufacturing-environments/discover-platforms/onto.ttl|
|Composition|- [Modelet manufacturing-environments/discover-platforms](https://github.com/HyperAgents/hmas/blob/HEAD/domains/manufacturing-environments/discover-platforms/onto.ttl)<br/>- [Module core](https://github.com/HyperAgents/hmas/blob/HEAD/src/core.ttl)|

#### Criterion detail
|Identifier|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|
|----|----|
|Title|Profile&#32;compatibility&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;check&#32;whether&#32;the&#32;test&#32;subject&#32;is&#32;compatible&#32;with&#32;a&#32;profile&#32;or&#32;not,&#32;and&#32;if&#32;it&#32;is&#32;not,&#32;why.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-12)|Identifier|`owl-el-profile-error`|
|[Section top](#minorfail-outcome-number-12)|Title|OWL&#32;EL&#32;Profile&#32;incompatible|
|[Section top](#minorfail-outcome-number-12)|Description|Anonymous&#32;individuals&#32;are&#32;not&#32;supported|
|[Section top](#minorfail-outcome-number-12)|Pointer|<pre lang="Turtle"><code>&#91;]&#32;a&#32;owl:NamedIndividual&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;Chemero&#32;and&#32;Turvey,&#32;2007&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;dc:bibliographicCitation&#32; &#34;Chemero,&#32;A.,&#32;&&#32;Turvey,&#32;M.&#32;T.&#32;(2007).&#32;Complexity,&#32;hypersets,&#32;...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;dc:identifier&#32; &#60;https://doi.org/10.1162/biot.2007.2.1.23> &#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-12)|Pointer|<pre lang="Turtle"><code>&#91;]&#32;a&#32;owl:NamedIndividual&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;Norman,&#32;2013&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;dc:bibliographicCitation&#32; &#34;Norman,&#32;D.&#32;(2013).&#32;The&#32;design&#32;of&#32;everyday&#32;things:&#32;Revised&#32;an...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;dc:identifier&#32; &#60;https://mitpress.mit.edu/9780262640374/> &#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-12)|Pointer|<pre lang="Turtle"><code>hmas:Affordance&#32;a&#32;skos:Concept&#32;;  &#10; &#32; &#32; &#32; &#32;dc:references&#32; &#91;&#32;a&#32;owl:NamedIndividual&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;Chemero&#32;and&#32;Turvey,&#32;2007&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;dc:bibliographicCitation&#32; &#34;Chemero,&#32;A.,&#32;&&#32;Turvey,&#32;M.&#32;T.&#32;(2007).&#32;Complexity,&#32;hypersets,&#32;...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;dc:identifier&#32; &#60;https://doi.org/10.1162/biot.2007.2.1.23> &#32;],  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#91;&#32;a&#32;owl:NamedIndividual&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;Norman,&#32;2013&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;dc:bibliographicCitation&#32; &#34;Norman,&#32;D.&#32;(2013).&#32;The&#32;design&#32;of&#32;everyday&#32;things:&#32;Revised&#32;an...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;dc:identifier&#32; &#60;https://mitpress.mit.edu/9780262640374/> &#32;]&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32;hmas:core&#32;;  &#10; &#32; &#32; &#32; &#32;skos:definition&#32; &#34;A&#32;behavior&#32;possibility&#32;that&#32;is&#32;a&#32;relationship&#32;between&#32;an&#32;abi...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;skos:editorialNote&#32; &#34;The&#32;concept&#32;has&#32;been&#32;considered&#32;as&#32;a&#32;candidate&#32;term&#32;for&#32;repr...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;skos:historyNote&#32; &#34;The&#32;definition&#32;of&#32;the&#32;concept&#32;follows&#32;affordance&#32;theorists&#32; &#91;...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;skos:prefLabel&#32; &#34;affordance&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;skos:related&#32;hmas:Signifier&#32;.</code></pre>|

***
### MinorFail Outcome number 13

[Jump to summary definition](#summary-MinorFail-13)	|	[Previous MinorFail outcome](#minorfail-outcome-number-12)	|	[Next MinorFail outcome](#minorfail-outcome-number-14)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-src-core-modelet-manufacturing-environments-discover-platforms|
|----|----|
|Title|Merged&#32;module&#32;src/core.ttl&#32;from&#32;branch&#32;HEAD&#32;with&#32;related&#32;terms&#32;from&#32;the&#32;fragments&#32;domains/manufacturing-environments/discover-platforms/onto.ttl|
|Composition|- [Modelet manufacturing-environments/discover-platforms](https://github.com/HyperAgents/hmas/blob/HEAD/domains/manufacturing-environments/discover-platforms/onto.ttl)<br/>- [Module core](https://github.com/HyperAgents/hmas/blob/HEAD/src/core.ttl)|

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
|[Section top](#minorfail-outcome-number-13)|Pointer|<pre lang="Turtle"><code>hmas:hasProfile&#32;a&#32;owl:AsymmetricProperty,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:ObjectProperty&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;has&#32;for&#32;profile&#34;@en,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#34;a&#32;pour&#32;profil&#34;@fr&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;A&#32;relation&#32;that&#32;links&#32;a&#32;resource&#32;to&#32;its&#32;profile.&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32;hmas:core&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:range&#32;hmas:ResourceProfile&#32;;  &#10; &#32; &#32; &#32; &#32;owl:inverseOf&#32;hmas:isProfileOf&#32;.</code></pre>|

***
### MinorFail Outcome number 14

[Jump to summary definition](#summary-MinorFail-14)	|	[Previous MinorFail outcome](#minorfail-outcome-number-13)	|	[Next MinorFail outcome](#minorfail-outcome-number-15)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-src-core-modelet-manufacturing-environments-discover-platforms|
|----|----|
|Title|Merged&#32;module&#32;src/core.ttl&#32;from&#32;branch&#32;HEAD&#32;with&#32;related&#32;terms&#32;from&#32;the&#32;fragments&#32;domains/manufacturing-environments/discover-platforms/onto.ttl|
|Composition|- [Modelet manufacturing-environments/discover-platforms](https://github.com/HyperAgents/hmas/blob/HEAD/domains/manufacturing-environments/discover-platforms/onto.ttl)<br/>- [Module core](https://github.com/HyperAgents/hmas/blob/HEAD/src/core.ttl)|

#### Criterion detail
|Identifier|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|
|----|----|
|Title|Profile&#32;compatibility&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;check&#32;whether&#32;the&#32;test&#32;subject&#32;is&#32;compatible&#32;with&#32;a&#32;profile&#32;or&#32;not,&#32;and&#32;if&#32;it&#32;is&#32;not,&#32;why.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-14)|Identifier|`owl-ql-profile-error`|
|[Section top](#minorfail-outcome-number-14)|Title|OWL&#32;QL&#32;Profile&#32;incompatible|
|[Section top](#minorfail-outcome-number-14)|Description|Anonymous&#32;individuals&#32;are&#32;not&#32;supported|
|[Section top](#minorfail-outcome-number-14)|Pointer|<pre lang="Turtle"><code>&#91;]&#32;a&#32;owl:NamedIndividual&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;Chemero&#32;and&#32;Turvey,&#32;2007&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;dc:bibliographicCitation&#32; &#34;Chemero,&#32;A.,&#32;&&#32;Turvey,&#32;M.&#32;T.&#32;(2007).&#32;Complexity,&#32;hypersets,&#32;...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;dc:identifier&#32; &#60;https://doi.org/10.1162/biot.2007.2.1.23> &#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-14)|Pointer|<pre lang="Turtle"><code>&#91;]&#32;a&#32;owl:NamedIndividual&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;Norman,&#32;2013&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;dc:bibliographicCitation&#32; &#34;Norman,&#32;D.&#32;(2013).&#32;The&#32;design&#32;of&#32;everyday&#32;things:&#32;Revised&#32;an...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;dc:identifier&#32; &#60;https://mitpress.mit.edu/9780262640374/> &#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-14)|Pointer|<pre lang="Turtle"><code>hmas:Affordance&#32;a&#32;skos:Concept&#32;;  &#10; &#32; &#32; &#32; &#32;dc:references&#32; &#91;&#32;a&#32;owl:NamedIndividual&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;Chemero&#32;and&#32;Turvey,&#32;2007&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;dc:bibliographicCitation&#32; &#34;Chemero,&#32;A.,&#32;&&#32;Turvey,&#32;M.&#32;T.&#32;(2007).&#32;Complexity,&#32;hypersets,&#32;...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;dc:identifier&#32; &#60;https://doi.org/10.1162/biot.2007.2.1.23> &#32;],  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#91;&#32;a&#32;owl:NamedIndividual&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;Norman,&#32;2013&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;dc:bibliographicCitation&#32; &#34;Norman,&#32;D.&#32;(2013).&#32;The&#32;design&#32;of&#32;everyday&#32;things:&#32;Revised&#32;an...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;dc:identifier&#32; &#60;https://mitpress.mit.edu/9780262640374/> &#32;]&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32;hmas:core&#32;;  &#10; &#32; &#32; &#32; &#32;skos:definition&#32; &#34;A&#32;behavior&#32;possibility&#32;that&#32;is&#32;a&#32;relationship&#32;between&#32;an&#32;abi...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;skos:editorialNote&#32; &#34;The&#32;concept&#32;has&#32;been&#32;considered&#32;as&#32;a&#32;candidate&#32;term&#32;for&#32;repr...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;skos:historyNote&#32; &#34;The&#32;definition&#32;of&#32;the&#32;concept&#32;follows&#32;affordance&#32;theorists&#32; &#91;...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;skos:prefLabel&#32; &#34;affordance&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;skos:related&#32;hmas:Signifier&#32;.</code></pre>|

***
### MinorFail Outcome number 15

[Jump to summary definition](#summary-MinorFail-15)	|	[Previous MinorFail outcome](#minorfail-outcome-number-14)	|	[Next MinorFail outcome](#minorfail-outcome-number-16)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-src-core-modelet-manufacturing-environments-discover-platforms|
|----|----|
|Title|Merged&#32;module&#32;src/core.ttl&#32;from&#32;branch&#32;HEAD&#32;with&#32;related&#32;terms&#32;from&#32;the&#32;fragments&#32;domains/manufacturing-environments/discover-platforms/onto.ttl|
|Composition|- [Modelet manufacturing-environments/discover-platforms](https://github.com/HyperAgents/hmas/blob/HEAD/domains/manufacturing-environments/discover-platforms/onto.ttl)<br/>- [Module core](https://github.com/HyperAgents/hmas/blob/HEAD/src/core.ttl)|

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
|[Section top](#minorfail-outcome-number-15)|Pointer|<pre lang="Turtle"><code>hmas:transitivelyContains&#32;a&#32;owl:ObjectProperty,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:TransitiveProperty&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;transitively&#32;contains&#34;@en,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#34;contient&#32;transitivement&#34;@fr&#32;;  &#10; &#32; &#32; &#32; &#32;dc:source&#32; &#60;https://github.com/HyperAgents/ns.hyperagents.org/issues/8#issuecomment-1025991719> &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;Links&#32;all&#32;the&#32;resources&#32;that&#32;are&#32;logically&#32;contained&#32;in&#32;a&#32;wo...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:domain&#32;hmas:Workspace&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32;hmas:core&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:seeAlso&#32; &#60;https://github.com/HyperAgents/ns.hyperagents.org/issues/18>,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#60;https://github.com/HyperAgents/ns.hyperagents.org/issues/39> &#32;;  &#10; &#32; &#32; &#32; &#32;owl:inverseOf&#32;hmas:isTransitivelyContainedIn&#32;.</code></pre>|

***
### MinorFail Outcome number 16

[Jump to summary definition](#summary-MinorFail-16)	|	[Previous MinorFail outcome](#minorfail-outcome-number-15)	|	[Next MinorFail outcome](#minorfail-outcome-number-17)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-src-core-modelet-manufacturing-environments-discover-organization|
|----|----|
|Title|Merged&#32;module&#32;src/core.ttl&#32;from&#32;branch&#32;HEAD&#32;with&#32;related&#32;terms&#32;from&#32;the&#32;fragments&#32;domains/manufacturing-environments/discover-organization/onto.ttl|
|Composition|- [Modelet manufacturing-environments/discover-organization](https://github.com/HyperAgents/hmas/blob/HEAD/domains/manufacturing-environments/discover-organization/onto.ttl)<br/>- [Module core](https://github.com/HyperAgents/hmas/blob/HEAD/src/core.ttl)|

#### Criterion detail
|Identifier|[labeled-terms](https://ns.inria.fr/olivaw#labeled-terms)|
|----|----|
|Title|Term&#32;labeling&#32;test|
|Description|A&#32;test&#32;case&#32;from&#32;the&#32;Best&#32;Practices&#32;tests&#32;checking&#32;if&#32;all&#32;the&#32;terms&#32;of&#32;the&#32;subject&#32;have&#32;a&#32;rdfs:label&#32;property&#32;pointing&#32;to&#32;a&#32;literal&#32;in&#32;English|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-16)|Identifier|`not-labeled-term`|
|[Section top](#minorfail-outcome-number-16)|Title|Terms&#32;not&#32;labeled|
|[Section top](#minorfail-outcome-number-16)|Description|The&#32;following&#32;terms&#32;have&#32;no&#32;rdfs:label&#32;to&#32;define&#32;it&#32;in&#32;natural&#32;language|
|[Section top](#minorfail-outcome-number-16)|Pointer|<pre lang="Turtle"><code>:Affordance&#32;a&#32;skos:Concept&#32;;  &#10; &#32; &#32; &#32; &#32;dc:references&#32; &#91;&#32;a&#32;owl:NamedIndividual&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;Chemero&#32;and&#32;Turvey,&#32;2007&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;dc:bibliographicCitation&#32; &#34;Chemero,&#32;A.,&#32;&&#32;Turvey,&#32;M.&#32;T.&#32;(2007).&#32;Complexity,&#32;hypersets,&#32;...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;dc:identifier&#32; &#60;https://doi.org/10.1162/biot.2007.2.1.23> &#32;],  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#91;&#32;a&#32;owl:NamedIndividual&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;Norman,&#32;2013&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;dc:bibliographicCitation&#32; &#34;Norman,&#32;D.&#32;(2013).&#32;The&#32;design&#32;of&#32;everyday&#32;things:&#32;Revised&#32;an...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;dc:identifier&#32; &#60;https://mitpress.mit.edu/9780262640374/> &#32;]&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32;:core&#32;;  &#10; &#32; &#32; &#32; &#32;skos:definition&#32; &#34;A&#32;behavior&#32;possibility&#32;that&#32;is&#32;a&#32;relationship&#32;between&#32;an&#32;abi...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;skos:editorialNote&#32; &#34;The&#32;concept&#32;has&#32;been&#32;considered&#32;as&#32;a&#32;candidate&#32;term&#32;for&#32;repr...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;skos:historyNote&#32; &#34;The&#32;definition&#32;of&#32;the&#32;concept&#32;follows&#32;affordance&#32;theorists&#32; &#91;...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;skos:prefLabel&#32; &#34;affordance&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;skos:related&#32;:Signifier&#32;.</code></pre>|

***
### MinorFail Outcome number 17

[Jump to summary definition](#summary-MinorFail-17)	|	[Previous MinorFail outcome](#minorfail-outcome-number-16)	|	[Next MinorFail outcome](#minorfail-outcome-number-18)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-src-core-modelet-manufacturing-environments-discover-organization|
|----|----|
|Title|Merged&#32;module&#32;src/core.ttl&#32;from&#32;branch&#32;HEAD&#32;with&#32;related&#32;terms&#32;from&#32;the&#32;fragments&#32;domains/manufacturing-environments/discover-organization/onto.ttl|
|Composition|- [Modelet manufacturing-environments/discover-organization](https://github.com/HyperAgents/hmas/blob/HEAD/domains/manufacturing-environments/discover-organization/onto.ttl)<br/>- [Module core](https://github.com/HyperAgents/hmas/blob/HEAD/src/core.ttl)|

#### Criterion detail
|Identifier|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|
|----|----|
|Title|Profile&#32;compatibility&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;check&#32;whether&#32;the&#32;test&#32;subject&#32;is&#32;compatible&#32;with&#32;a&#32;profile&#32;or&#32;not,&#32;and&#32;if&#32;it&#32;is&#32;not,&#32;why.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-17)|Identifier|`owl-el-profile-error`|
|[Section top](#minorfail-outcome-number-17)|Title|OWL&#32;EL&#32;Profile&#32;incompatible|
|[Section top](#minorfail-outcome-number-17)|Description|Anonymous&#32;individuals&#32;are&#32;not&#32;supported|
|[Section top](#minorfail-outcome-number-17)|Pointer|<pre lang="Turtle"><code>&#91;]&#32;a&#32;owl:NamedIndividual&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;Chemero&#32;and&#32;Turvey,&#32;2007&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;dc:bibliographicCitation&#32; &#34;Chemero,&#32;A.,&#32;&&#32;Turvey,&#32;M.&#32;T.&#32;(2007).&#32;Complexity,&#32;hypersets,&#32;...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;dc:identifier&#32; &#60;https://doi.org/10.1162/biot.2007.2.1.23> &#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-17)|Pointer|<pre lang="Turtle"><code>&#91;]&#32;a&#32;owl:NamedIndividual&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;Norman,&#32;2013&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;dc:bibliographicCitation&#32; &#34;Norman,&#32;D.&#32;(2013).&#32;The&#32;design&#32;of&#32;everyday&#32;things:&#32;Revised&#32;an...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;dc:identifier&#32; &#60;https://mitpress.mit.edu/9780262640374/> &#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-17)|Pointer|<pre lang="Turtle"><code>hmas:Affordance&#32;a&#32;skos:Concept&#32;;  &#10; &#32; &#32; &#32; &#32;dc:references&#32; &#91;&#32;a&#32;owl:NamedIndividual&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;Chemero&#32;and&#32;Turvey,&#32;2007&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;dc:bibliographicCitation&#32; &#34;Chemero,&#32;A.,&#32;&&#32;Turvey,&#32;M.&#32;T.&#32;(2007).&#32;Complexity,&#32;hypersets,&#32;...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;dc:identifier&#32; &#60;https://doi.org/10.1162/biot.2007.2.1.23> &#32;],  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#91;&#32;a&#32;owl:NamedIndividual&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;Norman,&#32;2013&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;dc:bibliographicCitation&#32; &#34;Norman,&#32;D.&#32;(2013).&#32;The&#32;design&#32;of&#32;everyday&#32;things:&#32;Revised&#32;an...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;dc:identifier&#32; &#60;https://mitpress.mit.edu/9780262640374/> &#32;]&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32;hmas:core&#32;;  &#10; &#32; &#32; &#32; &#32;skos:definition&#32; &#34;A&#32;behavior&#32;possibility&#32;that&#32;is&#32;a&#32;relationship&#32;between&#32;an&#32;abi...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;skos:editorialNote&#32; &#34;The&#32;concept&#32;has&#32;been&#32;considered&#32;as&#32;a&#32;candidate&#32;term&#32;for&#32;repr...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;skos:historyNote&#32; &#34;The&#32;definition&#32;of&#32;the&#32;concept&#32;follows&#32;affordance&#32;theorists&#32; &#91;...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;skos:prefLabel&#32; &#34;affordance&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;skos:related&#32;hmas:Signifier&#32;.</code></pre>|

***
### MinorFail Outcome number 18

[Jump to summary definition](#summary-MinorFail-18)	|	[Previous MinorFail outcome](#minorfail-outcome-number-17)	|	[Next MinorFail outcome](#minorfail-outcome-number-19)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-src-core-modelet-manufacturing-environments-discover-organization|
|----|----|
|Title|Merged&#32;module&#32;src/core.ttl&#32;from&#32;branch&#32;HEAD&#32;with&#32;related&#32;terms&#32;from&#32;the&#32;fragments&#32;domains/manufacturing-environments/discover-organization/onto.ttl|
|Composition|- [Modelet manufacturing-environments/discover-organization](https://github.com/HyperAgents/hmas/blob/HEAD/domains/manufacturing-environments/discover-organization/onto.ttl)<br/>- [Module core](https://github.com/HyperAgents/hmas/blob/HEAD/src/core.ttl)|

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
|[Section top](#minorfail-outcome-number-18)|Description|Statement&#32;not&#32;supported|
|[Section top](#minorfail-outcome-number-18)|Pointer|<pre lang="Turtle"><code>hmas:hasProfile&#32;a&#32;owl:AsymmetricProperty,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:ObjectProperty&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;has&#32;for&#32;profile&#34;@en,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#34;a&#32;pour&#32;profil&#34;@fr&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;A&#32;relation&#32;that&#32;links&#32;a&#32;resource&#32;to&#32;its&#32;profile.&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32;hmas:core&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:range&#32;hmas:ResourceProfile&#32;;  &#10; &#32; &#32; &#32; &#32;owl:inverseOf&#32;hmas:isProfileOf&#32;.</code></pre>|

***
### MinorFail Outcome number 19

[Jump to summary definition](#summary-MinorFail-19)	|	[Previous MinorFail outcome](#minorfail-outcome-number-18)	|	[Next MinorFail outcome](#minorfail-outcome-number-20)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-src-core-modelet-manufacturing-environments-discover-organization|
|----|----|
|Title|Merged&#32;module&#32;src/core.ttl&#32;from&#32;branch&#32;HEAD&#32;with&#32;related&#32;terms&#32;from&#32;the&#32;fragments&#32;domains/manufacturing-environments/discover-organization/onto.ttl|
|Composition|- [Modelet manufacturing-environments/discover-organization](https://github.com/HyperAgents/hmas/blob/HEAD/domains/manufacturing-environments/discover-organization/onto.ttl)<br/>- [Module core](https://github.com/HyperAgents/hmas/blob/HEAD/src/core.ttl)|

#### Criterion detail
|Identifier|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|
|----|----|
|Title|Profile&#32;compatibility&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;check&#32;whether&#32;the&#32;test&#32;subject&#32;is&#32;compatible&#32;with&#32;a&#32;profile&#32;or&#32;not,&#32;and&#32;if&#32;it&#32;is&#32;not,&#32;why.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-19)|Identifier|`owl-ql-profile-error`|
|[Section top](#minorfail-outcome-number-19)|Title|OWL&#32;QL&#32;Profile&#32;incompatible|
|[Section top](#minorfail-outcome-number-19)|Description|Anonymous&#32;individuals&#32;are&#32;not&#32;supported|
|[Section top](#minorfail-outcome-number-19)|Pointer|<pre lang="Turtle"><code>&#91;]&#32;a&#32;owl:NamedIndividual&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;Chemero&#32;and&#32;Turvey,&#32;2007&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;dc:bibliographicCitation&#32; &#34;Chemero,&#32;A.,&#32;&&#32;Turvey,&#32;M.&#32;T.&#32;(2007).&#32;Complexity,&#32;hypersets,&#32;...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;dc:identifier&#32; &#60;https://doi.org/10.1162/biot.2007.2.1.23> &#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-19)|Pointer|<pre lang="Turtle"><code>&#91;]&#32;a&#32;owl:NamedIndividual&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;Norman,&#32;2013&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;dc:bibliographicCitation&#32; &#34;Norman,&#32;D.&#32;(2013).&#32;The&#32;design&#32;of&#32;everyday&#32;things:&#32;Revised&#32;an...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;dc:identifier&#32; &#60;https://mitpress.mit.edu/9780262640374/> &#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-19)|Pointer|<pre lang="Turtle"><code>hmas:Affordance&#32;a&#32;skos:Concept&#32;;  &#10; &#32; &#32; &#32; &#32;dc:references&#32; &#91;&#32;a&#32;owl:NamedIndividual&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;Chemero&#32;and&#32;Turvey,&#32;2007&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;dc:bibliographicCitation&#32; &#34;Chemero,&#32;A.,&#32;&&#32;Turvey,&#32;M.&#32;T.&#32;(2007).&#32;Complexity,&#32;hypersets,&#32;...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;dc:identifier&#32; &#60;https://doi.org/10.1162/biot.2007.2.1.23> &#32;],  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#91;&#32;a&#32;owl:NamedIndividual&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;Norman,&#32;2013&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;dc:bibliographicCitation&#32; &#34;Norman,&#32;D.&#32;(2013).&#32;The&#32;design&#32;of&#32;everyday&#32;things:&#32;Revised&#32;an...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;dc:identifier&#32; &#60;https://mitpress.mit.edu/9780262640374/> &#32;]&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32;hmas:core&#32;;  &#10; &#32; &#32; &#32; &#32;skos:definition&#32; &#34;A&#32;behavior&#32;possibility&#32;that&#32;is&#32;a&#32;relationship&#32;between&#32;an&#32;abi...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;skos:editorialNote&#32; &#34;The&#32;concept&#32;has&#32;been&#32;considered&#32;as&#32;a&#32;candidate&#32;term&#32;for&#32;repr...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;skos:historyNote&#32; &#34;The&#32;definition&#32;of&#32;the&#32;concept&#32;follows&#32;affordance&#32;theorists&#32; &#91;...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;skos:prefLabel&#32; &#34;affordance&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;skos:related&#32;hmas:Signifier&#32;.</code></pre>|

***
### MinorFail Outcome number 20

[Jump to summary definition](#summary-MinorFail-20)	|	[Previous MinorFail outcome](#minorfail-outcome-number-19)	|	[Next MinorFail outcome](#minorfail-outcome-number-21)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-src-core-modelet-manufacturing-environments-discover-organization|
|----|----|
|Title|Merged&#32;module&#32;src/core.ttl&#32;from&#32;branch&#32;HEAD&#32;with&#32;related&#32;terms&#32;from&#32;the&#32;fragments&#32;domains/manufacturing-environments/discover-organization/onto.ttl|
|Composition|- [Modelet manufacturing-environments/discover-organization](https://github.com/HyperAgents/hmas/blob/HEAD/domains/manufacturing-environments/discover-organization/onto.ttl)<br/>- [Module core](https://github.com/HyperAgents/hmas/blob/HEAD/src/core.ttl)|

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
|[Section top](#minorfail-outcome-number-20)|Description|Statement&#32;not&#32;supported|
|[Section top](#minorfail-outcome-number-20)|Pointer|<pre lang="Turtle"><code>hmas:transitivelyContains&#32;a&#32;owl:ObjectProperty,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:TransitiveProperty&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;transitively&#32;contains&#34;@en,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#34;contient&#32;transitivement&#34;@fr&#32;;  &#10; &#32; &#32; &#32; &#32;dc:source&#32; &#60;https://github.com/HyperAgents/ns.hyperagents.org/issues/8#issuecomment-1025991719> &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;Links&#32;all&#32;the&#32;resources&#32;that&#32;are&#32;logically&#32;contained&#32;in&#32;a&#32;wo...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:domain&#32;hmas:Workspace&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32;hmas:core&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:seeAlso&#32; &#60;https://github.com/HyperAgents/ns.hyperagents.org/issues/18>,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#60;https://github.com/HyperAgents/ns.hyperagents.org/issues/39> &#32;;  &#10; &#32; &#32; &#32; &#32;owl:inverseOf&#32;hmas:isTransitivelyContainedIn&#32;.</code></pre>|

***
### MinorFail Outcome number 21

[Jump to summary definition](#summary-MinorFail-21)	|	[Previous MinorFail outcome](#minorfail-outcome-number-20)	|	[Next MinorFail outcome](#minorfail-outcome-number-22)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-src-core-modelet-manufacturing-environments-discover-core|
|----|----|
|Title|Merged&#32;module&#32;src/core.ttl&#32;from&#32;branch&#32;HEAD&#32;with&#32;related&#32;terms&#32;from&#32;the&#32;fragments&#32;domains/manufacturing-environments/discover-core/onto.ttl|
|Composition|- [Modelet manufacturing-environments/discover-core](https://github.com/HyperAgents/hmas/blob/HEAD/domains/manufacturing-environments/discover-core/onto.ttl)<br/>- [Module core](https://github.com/HyperAgents/hmas/blob/HEAD/src/core.ttl)|

#### Criterion detail
|Identifier|[labeled-terms](https://ns.inria.fr/olivaw#labeled-terms)|
|----|----|
|Title|Term&#32;labeling&#32;test|
|Description|A&#32;test&#32;case&#32;from&#32;the&#32;Best&#32;Practices&#32;tests&#32;checking&#32;if&#32;all&#32;the&#32;terms&#32;of&#32;the&#32;subject&#32;have&#32;a&#32;rdfs:label&#32;property&#32;pointing&#32;to&#32;a&#32;literal&#32;in&#32;English|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-21)|Identifier|`not-labeled-term`|
|[Section top](#minorfail-outcome-number-21)|Title|Terms&#32;not&#32;labeled|
|[Section top](#minorfail-outcome-number-21)|Description|The&#32;following&#32;terms&#32;have&#32;no&#32;rdfs:label&#32;to&#32;define&#32;it&#32;in&#32;natural&#32;language|
|[Section top](#minorfail-outcome-number-21)|Pointer|<pre lang="Turtle"><code>:Affordance&#32;a&#32;skos:Concept&#32;;  &#10; &#32; &#32; &#32; &#32;dc:references&#32; &#91;&#32;a&#32;owl:NamedIndividual&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;Chemero&#32;and&#32;Turvey,&#32;2007&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;dc:bibliographicCitation&#32; &#34;Chemero,&#32;A.,&#32;&&#32;Turvey,&#32;M.&#32;T.&#32;(2007).&#32;Complexity,&#32;hypersets,&#32;...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;dc:identifier&#32; &#60;https://doi.org/10.1162/biot.2007.2.1.23> &#32;],  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#91;&#32;a&#32;owl:NamedIndividual&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;Norman,&#32;2013&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;dc:bibliographicCitation&#32; &#34;Norman,&#32;D.&#32;(2013).&#32;The&#32;design&#32;of&#32;everyday&#32;things:&#32;Revised&#32;an...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;dc:identifier&#32; &#60;https://mitpress.mit.edu/9780262640374/> &#32;]&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32;:core&#32;;  &#10; &#32; &#32; &#32; &#32;skos:definition&#32; &#34;A&#32;behavior&#32;possibility&#32;that&#32;is&#32;a&#32;relationship&#32;between&#32;an&#32;abi...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;skos:editorialNote&#32; &#34;The&#32;concept&#32;has&#32;been&#32;considered&#32;as&#32;a&#32;candidate&#32;term&#32;for&#32;repr...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;skos:historyNote&#32; &#34;The&#32;definition&#32;of&#32;the&#32;concept&#32;follows&#32;affordance&#32;theorists&#32; &#91;...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;skos:prefLabel&#32; &#34;affordance&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;skos:related&#32;:Signifier&#32;.</code></pre>|

***
### MinorFail Outcome number 22

[Jump to summary definition](#summary-MinorFail-22)	|	[Previous MinorFail outcome](#minorfail-outcome-number-21)	|	[Next MinorFail outcome](#minorfail-outcome-number-23)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-src-core-modelet-manufacturing-environments-discover-core|
|----|----|
|Title|Merged&#32;module&#32;src/core.ttl&#32;from&#32;branch&#32;HEAD&#32;with&#32;related&#32;terms&#32;from&#32;the&#32;fragments&#32;domains/manufacturing-environments/discover-core/onto.ttl|
|Composition|- [Modelet manufacturing-environments/discover-core](https://github.com/HyperAgents/hmas/blob/HEAD/domains/manufacturing-environments/discover-core/onto.ttl)<br/>- [Module core](https://github.com/HyperAgents/hmas/blob/HEAD/src/core.ttl)|

#### Criterion detail
|Identifier|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|
|----|----|
|Title|Profile&#32;compatibility&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;check&#32;whether&#32;the&#32;test&#32;subject&#32;is&#32;compatible&#32;with&#32;a&#32;profile&#32;or&#32;not,&#32;and&#32;if&#32;it&#32;is&#32;not,&#32;why.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-22)|Identifier|`owl-el-profile-error`|
|[Section top](#minorfail-outcome-number-22)|Title|OWL&#32;EL&#32;Profile&#32;incompatible|
|[Section top](#minorfail-outcome-number-22)|Description|Anonymous&#32;individuals&#32;are&#32;not&#32;supported|
|[Section top](#minorfail-outcome-number-22)|Pointer|<pre lang="Turtle"><code>&#91;]&#32;a&#32;owl:NamedIndividual&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;Chemero&#32;and&#32;Turvey,&#32;2007&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;dc:bibliographicCitation&#32; &#34;Chemero,&#32;A.,&#32;&&#32;Turvey,&#32;M.&#32;T.&#32;(2007).&#32;Complexity,&#32;hypersets,&#32;...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;dc:identifier&#32; &#60;https://doi.org/10.1162/biot.2007.2.1.23> &#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-22)|Pointer|<pre lang="Turtle"><code>&#91;]&#32;a&#32;owl:NamedIndividual&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;Norman,&#32;2013&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;dc:bibliographicCitation&#32; &#34;Norman,&#32;D.&#32;(2013).&#32;The&#32;design&#32;of&#32;everyday&#32;things:&#32;Revised&#32;an...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;dc:identifier&#32; &#60;https://mitpress.mit.edu/9780262640374/> &#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-22)|Pointer|<pre lang="Turtle"><code>hmas:Affordance&#32;a&#32;skos:Concept&#32;;  &#10; &#32; &#32; &#32; &#32;dc:references&#32; &#91;&#32;a&#32;owl:NamedIndividual&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;Chemero&#32;and&#32;Turvey,&#32;2007&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;dc:bibliographicCitation&#32; &#34;Chemero,&#32;A.,&#32;&&#32;Turvey,&#32;M.&#32;T.&#32;(2007).&#32;Complexity,&#32;hypersets,&#32;...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;dc:identifier&#32; &#60;https://doi.org/10.1162/biot.2007.2.1.23> &#32;],  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#91;&#32;a&#32;owl:NamedIndividual&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;Norman,&#32;2013&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;dc:bibliographicCitation&#32; &#34;Norman,&#32;D.&#32;(2013).&#32;The&#32;design&#32;of&#32;everyday&#32;things:&#32;Revised&#32;an...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;dc:identifier&#32; &#60;https://mitpress.mit.edu/9780262640374/> &#32;]&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32;hmas:core&#32;;  &#10; &#32; &#32; &#32; &#32;skos:definition&#32; &#34;A&#32;behavior&#32;possibility&#32;that&#32;is&#32;a&#32;relationship&#32;between&#32;an&#32;abi...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;skos:editorialNote&#32; &#34;The&#32;concept&#32;has&#32;been&#32;considered&#32;as&#32;a&#32;candidate&#32;term&#32;for&#32;repr...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;skos:historyNote&#32; &#34;The&#32;definition&#32;of&#32;the&#32;concept&#32;follows&#32;affordance&#32;theorists&#32; &#91;...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;skos:prefLabel&#32; &#34;affordance&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;skos:related&#32;hmas:Signifier&#32;.</code></pre>|

***
### MinorFail Outcome number 23

[Jump to summary definition](#summary-MinorFail-23)	|	[Previous MinorFail outcome](#minorfail-outcome-number-22)	|	[Next MinorFail outcome](#minorfail-outcome-number-24)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-src-core-modelet-manufacturing-environments-discover-core|
|----|----|
|Title|Merged&#32;module&#32;src/core.ttl&#32;from&#32;branch&#32;HEAD&#32;with&#32;related&#32;terms&#32;from&#32;the&#32;fragments&#32;domains/manufacturing-environments/discover-core/onto.ttl|
|Composition|- [Modelet manufacturing-environments/discover-core](https://github.com/HyperAgents/hmas/blob/HEAD/domains/manufacturing-environments/discover-core/onto.ttl)<br/>- [Module core](https://github.com/HyperAgents/hmas/blob/HEAD/src/core.ttl)|

#### Criterion detail
|Identifier|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|
|----|----|
|Title|Profile&#32;compatibility&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;check&#32;whether&#32;the&#32;test&#32;subject&#32;is&#32;compatible&#32;with&#32;a&#32;profile&#32;or&#32;not,&#32;and&#32;if&#32;it&#32;is&#32;not,&#32;why.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-23)|Identifier|`owl-el-profile-error`|
|[Section top](#minorfail-outcome-number-23)|Title|OWL&#32;EL&#32;Profile&#32;incompatible|
|[Section top](#minorfail-outcome-number-23)|Description|Statement&#32;not&#32;supported|
|[Section top](#minorfail-outcome-number-23)|Pointer|<pre lang="Turtle"><code>hmas:hasProfile&#32;a&#32;owl:AsymmetricProperty,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:ObjectProperty&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;has&#32;for&#32;profile&#34;@en,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#34;has&#32;profile&#34;@en,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#34;a&#32;pour&#32;profil&#34;@fr&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;A&#32;relation&#32;that&#32;links&#32;a&#32;resource&#32;to&#32;its&#32;profile.&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32;hmas:core&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:range&#32;hmas:ResourceProfile&#32;;  &#10; &#32; &#32; &#32; &#32;owl:inverseOf&#32;hmas:isProfileOf&#32;.</code></pre>|

***
### MinorFail Outcome number 24

[Jump to summary definition](#summary-MinorFail-24)	|	[Previous MinorFail outcome](#minorfail-outcome-number-23)	|	[Next MinorFail outcome](#minorfail-outcome-number-25)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-src-core-modelet-manufacturing-environments-discover-core|
|----|----|
|Title|Merged&#32;module&#32;src/core.ttl&#32;from&#32;branch&#32;HEAD&#32;with&#32;related&#32;terms&#32;from&#32;the&#32;fragments&#32;domains/manufacturing-environments/discover-core/onto.ttl|
|Composition|- [Modelet manufacturing-environments/discover-core](https://github.com/HyperAgents/hmas/blob/HEAD/domains/manufacturing-environments/discover-core/onto.ttl)<br/>- [Module core](https://github.com/HyperAgents/hmas/blob/HEAD/src/core.ttl)|

#### Criterion detail
|Identifier|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|
|----|----|
|Title|Profile&#32;compatibility&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;check&#32;whether&#32;the&#32;test&#32;subject&#32;is&#32;compatible&#32;with&#32;a&#32;profile&#32;or&#32;not,&#32;and&#32;if&#32;it&#32;is&#32;not,&#32;why.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-24)|Identifier|`owl-ql-profile-error`|
|[Section top](#minorfail-outcome-number-24)|Title|OWL&#32;QL&#32;Profile&#32;incompatible|
|[Section top](#minorfail-outcome-number-24)|Description|Anonymous&#32;individuals&#32;are&#32;not&#32;supported|
|[Section top](#minorfail-outcome-number-24)|Pointer|<pre lang="Turtle"><code>&#91;]&#32;a&#32;owl:NamedIndividual&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;Chemero&#32;and&#32;Turvey,&#32;2007&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;dc:bibliographicCitation&#32; &#34;Chemero,&#32;A.,&#32;&&#32;Turvey,&#32;M.&#32;T.&#32;(2007).&#32;Complexity,&#32;hypersets,&#32;...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;dc:identifier&#32; &#60;https://doi.org/10.1162/biot.2007.2.1.23> &#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-24)|Pointer|<pre lang="Turtle"><code>&#91;]&#32;a&#32;owl:NamedIndividual&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;Norman,&#32;2013&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;dc:bibliographicCitation&#32; &#34;Norman,&#32;D.&#32;(2013).&#32;The&#32;design&#32;of&#32;everyday&#32;things:&#32;Revised&#32;an...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;dc:identifier&#32; &#60;https://mitpress.mit.edu/9780262640374/> &#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-24)|Pointer|<pre lang="Turtle"><code>hmas:Affordance&#32;a&#32;skos:Concept&#32;;  &#10; &#32; &#32; &#32; &#32;dc:references&#32; &#91;&#32;a&#32;owl:NamedIndividual&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;Chemero&#32;and&#32;Turvey,&#32;2007&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;dc:bibliographicCitation&#32; &#34;Chemero,&#32;A.,&#32;&&#32;Turvey,&#32;M.&#32;T.&#32;(2007).&#32;Complexity,&#32;hypersets,&#32;...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;dc:identifier&#32; &#60;https://doi.org/10.1162/biot.2007.2.1.23> &#32;],  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#91;&#32;a&#32;owl:NamedIndividual&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;Norman,&#32;2013&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;dc:bibliographicCitation&#32; &#34;Norman,&#32;D.&#32;(2013).&#32;The&#32;design&#32;of&#32;everyday&#32;things:&#32;Revised&#32;an...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;dc:identifier&#32; &#60;https://mitpress.mit.edu/9780262640374/> &#32;]&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32;hmas:core&#32;;  &#10; &#32; &#32; &#32; &#32;skos:definition&#32; &#34;A&#32;behavior&#32;possibility&#32;that&#32;is&#32;a&#32;relationship&#32;between&#32;an&#32;abi...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;skos:editorialNote&#32; &#34;The&#32;concept&#32;has&#32;been&#32;considered&#32;as&#32;a&#32;candidate&#32;term&#32;for&#32;repr...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;skos:historyNote&#32; &#34;The&#32;definition&#32;of&#32;the&#32;concept&#32;follows&#32;affordance&#32;theorists&#32; &#91;...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;skos:prefLabel&#32; &#34;affordance&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;skos:related&#32;hmas:Signifier&#32;.</code></pre>|

***
### MinorFail Outcome number 25

[Jump to summary definition](#summary-MinorFail-25)	|	[Previous MinorFail outcome](#minorfail-outcome-number-24)	|	[Next MinorFail outcome](#minorfail-outcome-number-26)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-src-core-modelet-manufacturing-environments-discover-core|
|----|----|
|Title|Merged&#32;module&#32;src/core.ttl&#32;from&#32;branch&#32;HEAD&#32;with&#32;related&#32;terms&#32;from&#32;the&#32;fragments&#32;domains/manufacturing-environments/discover-core/onto.ttl|
|Composition|- [Modelet manufacturing-environments/discover-core](https://github.com/HyperAgents/hmas/blob/HEAD/domains/manufacturing-environments/discover-core/onto.ttl)<br/>- [Module core](https://github.com/HyperAgents/hmas/blob/HEAD/src/core.ttl)|

#### Criterion detail
|Identifier|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|
|----|----|
|Title|Profile&#32;compatibility&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;check&#32;whether&#32;the&#32;test&#32;subject&#32;is&#32;compatible&#32;with&#32;a&#32;profile&#32;or&#32;not,&#32;and&#32;if&#32;it&#32;is&#32;not,&#32;why.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-25)|Identifier|`owl-ql-profile-error`|
|[Section top](#minorfail-outcome-number-25)|Title|OWL&#32;QL&#32;Profile&#32;incompatible|
|[Section top](#minorfail-outcome-number-25)|Description|Statement&#32;not&#32;supported|
|[Section top](#minorfail-outcome-number-25)|Pointer|<pre lang="Turtle"><code>hmas:transitivelyContains&#32;a&#32;owl:ObjectProperty,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:TransitiveProperty&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;transitively&#32;contains&#34;@en,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#34;transitivelyContains&#34;@en,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#34;contient&#32;transitivement&#34;@fr&#32;;  &#10; &#32; &#32; &#32; &#32;dc:source&#32; &#60;https://github.com/HyperAgents/ns.hyperagents.org/issues/8#issuecomment-1025991719> &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;Links&#32;all&#32;the&#32;resources&#32;that&#32;are&#32;logically&#32;contained&#32;in&#32;a&#32;wo...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:domain&#32;hmas:Workspace&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32;hmas:core&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:seeAlso&#32; &#60;https://github.com/HyperAgents/ns.hyperagents.org/issues/18>,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#60;https://github.com/HyperAgents/ns.hyperagents.org/issues/39> &#32;;  &#10; &#32; &#32; &#32; &#32;owl:inverseOf&#32;hmas:isTransitivelyContainedIn&#32;.</code></pre>|

***
### MinorFail Outcome number 26

[Jump to summary definition](#summary-MinorFail-26)	|	[Previous MinorFail outcome](#minorfail-outcome-number-25)	|	[Next MinorFail outcome](#minorfail-outcome-number-27)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-src-core|
|----|----|
|Title|Standalone&#32;module&#32;src/core.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Module core](https://github.com/HyperAgents/hmas/blob/HEAD/src/core.ttl)|

#### Criterion detail
|Identifier|[labeled-terms](https://ns.inria.fr/olivaw#labeled-terms)|
|----|----|
|Title|Term&#32;labeling&#32;test|
|Description|A&#32;test&#32;case&#32;from&#32;the&#32;Best&#32;Practices&#32;tests&#32;checking&#32;if&#32;all&#32;the&#32;terms&#32;of&#32;the&#32;subject&#32;have&#32;a&#32;rdfs:label&#32;property&#32;pointing&#32;to&#32;a&#32;literal&#32;in&#32;English|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-26)|Identifier|`not-labeled-term`|
|[Section top](#minorfail-outcome-number-26)|Title|Terms&#32;not&#32;labeled|
|[Section top](#minorfail-outcome-number-26)|Description|The&#32;following&#32;terms&#32;have&#32;no&#32;rdfs:label&#32;to&#32;define&#32;it&#32;in&#32;natural&#32;language|
|[Section top](#minorfail-outcome-number-26)|Pointer|<pre lang="Turtle"><code>:Affordance&#32;a&#32;skos:Concept&#32;;  &#10; &#32; &#32; &#32; &#32;dc:references&#32; &#91;&#32;a&#32;owl:NamedIndividual&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;Chemero&#32;and&#32;Turvey,&#32;2007&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;dc:bibliographicCitation&#32; &#34;Chemero,&#32;A.,&#32;&&#32;Turvey,&#32;M.&#32;T.&#32;(2007).&#32;Complexity,&#32;hypersets,&#32;...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;dc:identifier&#32; &#60;https://doi.org/10.1162/biot.2007.2.1.23> &#32;],  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#91;&#32;a&#32;owl:NamedIndividual&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;Norman,&#32;2013&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;dc:bibliographicCitation&#32; &#34;Norman,&#32;D.&#32;(2013).&#32;The&#32;design&#32;of&#32;everyday&#32;things:&#32;Revised&#32;an...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;dc:identifier&#32; &#60;https://mitpress.mit.edu/9780262640374/> &#32;]&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32;:core&#32;;  &#10; &#32; &#32; &#32; &#32;skos:definition&#32; &#34;A&#32;behavior&#32;possibility&#32;that&#32;is&#32;a&#32;relationship&#32;between&#32;an&#32;abi...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;skos:editorialNote&#32; &#34;The&#32;concept&#32;has&#32;been&#32;considered&#32;as&#32;a&#32;candidate&#32;term&#32;for&#32;repr...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;skos:historyNote&#32; &#34;The&#32;definition&#32;of&#32;the&#32;concept&#32;follows&#32;affordance&#32;theorists&#32; &#91;...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;skos:prefLabel&#32; &#34;affordance&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;skos:related&#32;:Signifier&#32;.</code></pre>|

***
### MinorFail Outcome number 27

[Jump to summary definition](#summary-MinorFail-27)	|	[Previous MinorFail outcome](#minorfail-outcome-number-26)	|	[Next MinorFail outcome](#minorfail-outcome-number-28)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-src-core|
|----|----|
|Title|Standalone&#32;module&#32;src/core.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Module core](https://github.com/HyperAgents/hmas/blob/HEAD/src/core.ttl)|

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
|[Section top](#minorfail-outcome-number-27)|Description|Anonymous&#32;individuals&#32;are&#32;not&#32;supported|
|[Section top](#minorfail-outcome-number-27)|Pointer|<pre lang="Turtle"><code>&#91;]&#32;a&#32;owl:NamedIndividual&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;Chemero&#32;and&#32;Turvey,&#32;2007&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;dc:bibliographicCitation&#32; &#34;Chemero,&#32;A.,&#32;&&#32;Turvey,&#32;M.&#32;T.&#32;(2007).&#32;Complexity,&#32;hypersets,&#32;...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;dc:identifier&#32; &#60;https://doi.org/10.1162/biot.2007.2.1.23> &#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-27)|Pointer|<pre lang="Turtle"><code>&#91;]&#32;a&#32;owl:NamedIndividual&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;Norman,&#32;2013&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;dc:bibliographicCitation&#32; &#34;Norman,&#32;D.&#32;(2013).&#32;The&#32;design&#32;of&#32;everyday&#32;things:&#32;Revised&#32;an...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;dc:identifier&#32; &#60;https://mitpress.mit.edu/9780262640374/> &#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-27)|Pointer|<pre lang="Turtle"><code>hmas:Affordance&#32;a&#32;skos:Concept&#32;;  &#10; &#32; &#32; &#32; &#32;dc:references&#32; &#91;&#32;a&#32;owl:NamedIndividual&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;Chemero&#32;and&#32;Turvey,&#32;2007&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;dc:bibliographicCitation&#32; &#34;Chemero,&#32;A.,&#32;&&#32;Turvey,&#32;M.&#32;T.&#32;(2007).&#32;Complexity,&#32;hypersets,&#32;...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;dc:identifier&#32; &#60;https://doi.org/10.1162/biot.2007.2.1.23> &#32;],  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#91;&#32;a&#32;owl:NamedIndividual&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;Norman,&#32;2013&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;dc:bibliographicCitation&#32; &#34;Norman,&#32;D.&#32;(2013).&#32;The&#32;design&#32;of&#32;everyday&#32;things:&#32;Revised&#32;an...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;dc:identifier&#32; &#60;https://mitpress.mit.edu/9780262640374/> &#32;]&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32;hmas:core&#32;;  &#10; &#32; &#32; &#32; &#32;skos:definition&#32; &#34;A&#32;behavior&#32;possibility&#32;that&#32;is&#32;a&#32;relationship&#32;between&#32;an&#32;abi...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;skos:editorialNote&#32; &#34;The&#32;concept&#32;has&#32;been&#32;considered&#32;as&#32;a&#32;candidate&#32;term&#32;for&#32;repr...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;skos:historyNote&#32; &#34;The&#32;definition&#32;of&#32;the&#32;concept&#32;follows&#32;affordance&#32;theorists&#32; &#91;...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;skos:prefLabel&#32; &#34;affordance&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;skos:related&#32;hmas:Signifier&#32;.</code></pre>|

***
### MinorFail Outcome number 28

[Jump to summary definition](#summary-MinorFail-28)	|	[Previous MinorFail outcome](#minorfail-outcome-number-27)	|	[Next MinorFail outcome](#minorfail-outcome-number-29)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-src-core|
|----|----|
|Title|Standalone&#32;module&#32;src/core.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Module core](https://github.com/HyperAgents/hmas/blob/HEAD/src/core.ttl)|

#### Criterion detail
|Identifier|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|
|----|----|
|Title|Profile&#32;compatibility&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;check&#32;whether&#32;the&#32;test&#32;subject&#32;is&#32;compatible&#32;with&#32;a&#32;profile&#32;or&#32;not,&#32;and&#32;if&#32;it&#32;is&#32;not,&#32;why.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-28)|Identifier|`owl-el-profile-error`|
|[Section top](#minorfail-outcome-number-28)|Title|OWL&#32;EL&#32;Profile&#32;incompatible|
|[Section top](#minorfail-outcome-number-28)|Description|Statement&#32;not&#32;supported|
|[Section top](#minorfail-outcome-number-28)|Pointer|<pre lang="Turtle"><code>hmas:hasProfile&#32;a&#32;owl:AsymmetricProperty,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:ObjectProperty&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;has&#32;for&#32;profile&#34;@en,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#34;a&#32;pour&#32;profil&#34;@fr&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;A&#32;relation&#32;that&#32;links&#32;a&#32;resource&#32;to&#32;its&#32;profile.&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32;hmas:core&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:range&#32;hmas:ResourceProfile&#32;;  &#10; &#32; &#32; &#32; &#32;owl:inverseOf&#32;hmas:isProfileOf&#32;.</code></pre>|

***
### MinorFail Outcome number 29

[Jump to summary definition](#summary-MinorFail-29)	|	[Previous MinorFail outcome](#minorfail-outcome-number-28)	|	[Next MinorFail outcome](#minorfail-outcome-number-30)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-src-core|
|----|----|
|Title|Standalone&#32;module&#32;src/core.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Module core](https://github.com/HyperAgents/hmas/blob/HEAD/src/core.ttl)|

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
|[Section top](#minorfail-outcome-number-29)|Description|Anonymous&#32;individuals&#32;are&#32;not&#32;supported|
|[Section top](#minorfail-outcome-number-29)|Pointer|<pre lang="Turtle"><code>&#91;]&#32;a&#32;owl:NamedIndividual&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;Chemero&#32;and&#32;Turvey,&#32;2007&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;dc:bibliographicCitation&#32; &#34;Chemero,&#32;A.,&#32;&&#32;Turvey,&#32;M.&#32;T.&#32;(2007).&#32;Complexity,&#32;hypersets,&#32;...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;dc:identifier&#32; &#60;https://doi.org/10.1162/biot.2007.2.1.23> &#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-29)|Pointer|<pre lang="Turtle"><code>&#91;]&#32;a&#32;owl:NamedIndividual&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;Norman,&#32;2013&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;dc:bibliographicCitation&#32; &#34;Norman,&#32;D.&#32;(2013).&#32;The&#32;design&#32;of&#32;everyday&#32;things:&#32;Revised&#32;an...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;dc:identifier&#32; &#60;https://mitpress.mit.edu/9780262640374/> &#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-29)|Pointer|<pre lang="Turtle"><code>hmas:Affordance&#32;a&#32;skos:Concept&#32;;  &#10; &#32; &#32; &#32; &#32;dc:references&#32; &#91;&#32;a&#32;owl:NamedIndividual&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;Chemero&#32;and&#32;Turvey,&#32;2007&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;dc:bibliographicCitation&#32; &#34;Chemero,&#32;A.,&#32;&&#32;Turvey,&#32;M.&#32;T.&#32;(2007).&#32;Complexity,&#32;hypersets,&#32;...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;dc:identifier&#32; &#60;https://doi.org/10.1162/biot.2007.2.1.23> &#32;],  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#91;&#32;a&#32;owl:NamedIndividual&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;Norman,&#32;2013&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;dc:bibliographicCitation&#32; &#34;Norman,&#32;D.&#32;(2013).&#32;The&#32;design&#32;of&#32;everyday&#32;things:&#32;Revised&#32;an...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;dc:identifier&#32; &#60;https://mitpress.mit.edu/9780262640374/> &#32;]&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32;hmas:core&#32;;  &#10; &#32; &#32; &#32; &#32;skos:definition&#32; &#34;A&#32;behavior&#32;possibility&#32;that&#32;is&#32;a&#32;relationship&#32;between&#32;an&#32;abi...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;skos:editorialNote&#32; &#34;The&#32;concept&#32;has&#32;been&#32;considered&#32;as&#32;a&#32;candidate&#32;term&#32;for&#32;repr...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;skos:historyNote&#32; &#34;The&#32;definition&#32;of&#32;the&#32;concept&#32;follows&#32;affordance&#32;theorists&#32; &#91;...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;skos:prefLabel&#32; &#34;affordance&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;skos:related&#32;hmas:Signifier&#32;.</code></pre>|

***
### MinorFail Outcome number 30

[Jump to summary definition](#summary-MinorFail-30)	|	[Previous MinorFail outcome](#minorfail-outcome-number-29)	|	[Next MinorFail outcome](#minorfail-outcome-number-31)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-src-core|
|----|----|
|Title|Standalone&#32;module&#32;src/core.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Module core](https://github.com/HyperAgents/hmas/blob/HEAD/src/core.ttl)|

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
|[Section top](#minorfail-outcome-number-30)|Description|Statement&#32;not&#32;supported|
|[Section top](#minorfail-outcome-number-30)|Pointer|<pre lang="Turtle"><code>hmas:transitivelyContains&#32;a&#32;owl:ObjectProperty,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:TransitiveProperty&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;transitively&#32;contains&#34;@en,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#34;contient&#32;transitivement&#34;@fr&#32;;  &#10; &#32; &#32; &#32; &#32;dc:source&#32; &#60;https://github.com/HyperAgents/ns.hyperagents.org/issues/8#issuecomment-1025991719> &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;Links&#32;all&#32;the&#32;resources&#32;that&#32;are&#32;logically&#32;contained&#32;in&#32;a&#32;wo...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:domain&#32;hmas:Workspace&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32;hmas:core&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:seeAlso&#32; &#60;https://github.com/HyperAgents/ns.hyperagents.org/issues/18>,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#60;https://github.com/HyperAgents/ns.hyperagents.org/issues/39> &#32;;  &#10; &#32; &#32; &#32; &#32;owl:inverseOf&#32;hmas:isTransitivelyContainedIn&#32;.</code></pre>|

***
### MinorFail Outcome number 31

[Jump to summary definition](#summary-MinorFail-31)	|	[Previous MinorFail outcome](#minorfail-outcome-number-30)	|	[Next MinorFail outcome](#minorfail-outcome-number-32)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-src-alignment-interaction-td|
|----|----|
|Title|Standalone&#32;module&#32;src/alignment/interaction-td.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Module alignment/interaction-td](https://github.com/HyperAgents/hmas/blob/HEAD/src/alignment/interaction-td.ttl)|

#### Criterion detail
|Identifier|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|
|----|----|
|Title|Profile&#32;compatibility&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;check&#32;whether&#32;the&#32;test&#32;subject&#32;is&#32;compatible&#32;with&#32;a&#32;profile&#32;or&#32;not,&#32;and&#32;if&#32;it&#32;is&#32;not,&#32;why.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-31)|Identifier|`owl-ql-profile-error`|
|[Section top](#minorfail-outcome-number-31)|Title|OWL&#32;QL&#32;Profile&#32;incompatible|
|[Section top](#minorfail-outcome-number-31)|Description|Class&#32;Expression&#32;not&#32;supported&#32;with&#32;rdfs:subClassOf|
|[Section top](#minorfail-outcome-number-31)|Pointer|<pre lang="Turtle"><code>&#60;https://www.w3.org/2019/wot/td#InteractionAffordance> &#32;rdfs:comment&#32; &#34;Using&#32;a&#32;TD&#32;Interaction&#32;Affordance&#32;results&#32;in&#32;an&#32;action&#32;execu...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:subClassOf&#32; &#91;&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:hasValue&#32;hmas:ActionExecution&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:onProperty&#32;sh:class&#32;]&#32;.</code></pre>|

***
### MinorFail Outcome number 32

[Jump to summary definition](#summary-MinorFail-32)	|	[Previous MinorFail outcome](#minorfail-outcome-number-31)	|	[Next MinorFail outcome](#minorfail-outcome-number-33)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-src-alignment-interaction-td|
|----|----|
|Title|Standalone&#32;module&#32;src/alignment/interaction-td.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Module alignment/interaction-td](https://github.com/HyperAgents/hmas/blob/HEAD/src/alignment/interaction-td.ttl)|

#### Criterion detail
|Identifier|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|
|----|----|
|Title|Profile&#32;compatibility&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;check&#32;whether&#32;the&#32;test&#32;subject&#32;is&#32;compatible&#32;with&#32;a&#32;profile&#32;or&#32;not,&#32;and&#32;if&#32;it&#32;is&#32;not,&#32;why.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-32)|Identifier|`owl-ql-profile-error`|
|[Section top](#minorfail-outcome-number-32)|Title|OWL&#32;QL&#32;Profile&#32;incompatible|
|[Section top](#minorfail-outcome-number-32)|Description|Statement&#32;not&#32;supported  &#10;Statement&#32;not&#32;supported&#32;in&#32;a&#32;Super&#32;Class&#32;Expression|
|[Section top](#minorfail-outcome-number-32)|Pointer|<pre lang="Turtle"><code>&#91;]&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32;owl:hasValue&#32;hmas:ActionExecution&#32;;  &#10; &#32; &#32; &#32; &#32;owl:onProperty&#32;sh:class&#32;.</code></pre>|

***
### MinorFail Outcome number 33

[Jump to summary definition](#summary-MinorFail-33)	|	[Previous MinorFail outcome](#minorfail-outcome-number-32)	|	[Next MinorFail outcome](#minorfail-outcome-number-34)

:exclamation:MinorFail outcome
#### Subject detail
|Name|modelet-manufacturing-environments-discover-signifiers|
|----|----|
|Title|Standalone&#32;modelet&#32;domains/manufacturing-environments/discover-signifiers/onto.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Modelet manufacturing-environments/discover-signifiers](https://github.com/HyperAgents/hmas/blob/HEAD/domains/manufacturing-environments/discover-signifiers/onto.ttl)|

#### Criterion detail
|Identifier|[labeled-terms](https://ns.inria.fr/olivaw#labeled-terms)|
|----|----|
|Title|Term&#32;labeling&#32;test|
|Description|A&#32;test&#32;case&#32;from&#32;the&#32;Best&#32;Practices&#32;tests&#32;checking&#32;if&#32;all&#32;the&#32;terms&#32;of&#32;the&#32;subject&#32;have&#32;a&#32;rdfs:label&#32;property&#32;pointing&#32;to&#32;a&#32;literal&#32;in&#32;English|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-33)|Identifier|`not-labeled-term`|
|[Section top](#minorfail-outcome-number-33)|Title|Terms&#32;not&#32;labeled|
|[Section top](#minorfail-outcome-number-33)|Description|The&#32;following&#32;terms&#32;have&#32;no&#32;rdfs:label&#32;to&#32;define&#32;it&#32;in&#32;natural&#32;language|
|[Section top](#minorfail-outcome-number-33)|Pointer|<pre lang="Turtle"><code>:Affordance&#32;a&#32;skos:Concept&#32;;  &#10; &#32; &#32; &#32; &#32;dc:references&#32; &#91;&#32;rdfs:label&#32; &#34;Chemero&#32;and&#32;Turvey,&#32;2007&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;dc:bibliographicCitation&#32; &#34;Chemero,&#32;A.,&#32;&&#32;Turvey,&#32;M.&#32;T.&#32;(2007).&#32;Complexity,&#32;hypersets,&#32;...&#34; &#32;],  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#91;&#32;rdfs:label&#32; &#34;Norman,&#32;2013&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;dc:bibliographicCitation&#32; &#34;Norman,&#32;D.&#32;(2013).&#32;The&#32;design&#32;of&#32;everyday&#32;things:&#32;Revised&#32;an...&#34; &#32;]&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32;:core&#32;;  &#10; &#32; &#32; &#32; &#32;skos:definition&#32; &#34;A&#32;behavior&#32;possibility&#32;that&#32;is&#32;a&#32;relationship&#32;between&#32;an&#32;abi...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;skos:editorialNote&#32; &#34;The&#32;concept&#32;has&#32;been&#32;considered&#32;as&#32;a&#32;candidate&#32;term&#32;for&#32;repr...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;skos:historyNote&#32; &#34;The&#32;definition&#32;of&#32;the&#32;concept&#32;follows&#32;affordance&#32;theorists&#32; &#91;...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;skos:prefLabel&#32; &#34;affordance&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;skos:related&#32;:Signifier&#32;.</code></pre>|

***
### MinorFail Outcome number 34

[Jump to summary definition](#summary-MinorFail-34)	|	[Previous MinorFail outcome](#minorfail-outcome-number-33)	|	[Next MinorFail outcome](#minorfail-outcome-number-35)

:exclamation:MinorFail outcome
#### Subject detail
|Name|modelet-manufacturing-environments-discover-signifiers|
|----|----|
|Title|Standalone&#32;modelet&#32;domains/manufacturing-environments/discover-signifiers/onto.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Modelet manufacturing-environments/discover-signifiers](https://github.com/HyperAgents/hmas/blob/HEAD/domains/manufacturing-environments/discover-signifiers/onto.ttl)|

#### Criterion detail
|Identifier|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|
|----|----|
|Title|Profile&#32;compatibility&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;check&#32;whether&#32;the&#32;test&#32;subject&#32;is&#32;compatible&#32;with&#32;a&#32;profile&#32;or&#32;not,&#32;and&#32;if&#32;it&#32;is&#32;not,&#32;why.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-34)|Identifier|`owl-el-profile-error`|
|[Section top](#minorfail-outcome-number-34)|Title|OWL&#32;EL&#32;Profile&#32;incompatible|
|[Section top](#minorfail-outcome-number-34)|Description|Anonymous&#32;individuals&#32;are&#32;not&#32;supported|
|[Section top](#minorfail-outcome-number-34)|Pointer|<pre lang="Turtle"><code>&#91;]&#32;rdfs:label&#32; &#34;Chemero&#32;and&#32;Turvey,&#32;2007&#34;@en&#32;;  &#10; &#32; &#32;&#32; &#32;dc:bibliographicCitation&#32; &#34;Chemero,&#32;A.,&#32;&&#32;Turvey,&#32;M.&#32;T.&#32;(2007).&#32;Complexity,&#32;hypersets,&#32;...&#34; &#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-34)|Pointer|<pre lang="Turtle"><code>&#91;]&#32;rdfs:label&#32; &#34;Norman,&#32;2013&#34;@en&#32;;  &#10; &#32; &#32;&#32; &#32;dc:bibliographicCitation&#32; &#34;Norman,&#32;D.&#32;(2013).&#32;The&#32;design&#32;of&#32;everyday&#32;things:&#32;Revised&#32;an...&#34; &#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-34)|Pointer|<pre lang="Turtle"><code>hmas:Affordance&#32;a&#32;skos:Concept&#32;;  &#10; &#32; &#32; &#32; &#32;dc:references&#32; &#91;&#32;rdfs:label&#32; &#34;Chemero&#32;and&#32;Turvey,&#32;2007&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;dc:bibliographicCitation&#32; &#34;Chemero,&#32;A.,&#32;&&#32;Turvey,&#32;M.&#32;T.&#32;(2007).&#32;Complexity,&#32;hypersets,&#32;...&#34; &#32;],  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#91;&#32;rdfs:label&#32; &#34;Norman,&#32;2013&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;dc:bibliographicCitation&#32; &#34;Norman,&#32;D.&#32;(2013).&#32;The&#32;design&#32;of&#32;everyday&#32;things:&#32;Revised&#32;an...&#34; &#32;]&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32;hmas:core&#32;;  &#10; &#32; &#32; &#32; &#32;skos:definition&#32; &#34;A&#32;behavior&#32;possibility&#32;that&#32;is&#32;a&#32;relationship&#32;between&#32;an&#32;abi...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;skos:editorialNote&#32; &#34;The&#32;concept&#32;has&#32;been&#32;considered&#32;as&#32;a&#32;candidate&#32;term&#32;for&#32;repr...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;skos:historyNote&#32; &#34;The&#32;definition&#32;of&#32;the&#32;concept&#32;follows&#32;affordance&#32;theorists&#32; &#91;...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;skos:prefLabel&#32; &#34;affordance&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;skos:related&#32;hmas:Signifier&#32;.</code></pre>|

***
### MinorFail Outcome number 35

[Jump to summary definition](#summary-MinorFail-35)	|	[Previous MinorFail outcome](#minorfail-outcome-number-34)	|	[Next MinorFail outcome](#minorfail-outcome-number-36)

:exclamation:MinorFail outcome
#### Subject detail
|Name|modelet-manufacturing-environments-discover-signifiers|
|----|----|
|Title|Standalone&#32;modelet&#32;domains/manufacturing-environments/discover-signifiers/onto.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Modelet manufacturing-environments/discover-signifiers](https://github.com/HyperAgents/hmas/blob/HEAD/domains/manufacturing-environments/discover-signifiers/onto.ttl)|

#### Criterion detail
|Identifier|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|
|----|----|
|Title|Profile&#32;compatibility&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;check&#32;whether&#32;the&#32;test&#32;subject&#32;is&#32;compatible&#32;with&#32;a&#32;profile&#32;or&#32;not,&#32;and&#32;if&#32;it&#32;is&#32;not,&#32;why.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-35)|Identifier|`owl-ql-profile-error`|
|[Section top](#minorfail-outcome-number-35)|Title|OWL&#32;QL&#32;Profile&#32;incompatible|
|[Section top](#minorfail-outcome-number-35)|Description|Anonymous&#32;individuals&#32;are&#32;not&#32;supported|
|[Section top](#minorfail-outcome-number-35)|Pointer|<pre lang="Turtle"><code>&#91;]&#32;rdfs:label&#32; &#34;Chemero&#32;and&#32;Turvey,&#32;2007&#34;@en&#32;;  &#10; &#32; &#32;&#32; &#32;dc:bibliographicCitation&#32; &#34;Chemero,&#32;A.,&#32;&&#32;Turvey,&#32;M.&#32;T.&#32;(2007).&#32;Complexity,&#32;hypersets,&#32;...&#34; &#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-35)|Pointer|<pre lang="Turtle"><code>&#91;]&#32;rdfs:label&#32; &#34;Norman,&#32;2013&#34;@en&#32;;  &#10; &#32; &#32;&#32; &#32;dc:bibliographicCitation&#32; &#34;Norman,&#32;D.&#32;(2013).&#32;The&#32;design&#32;of&#32;everyday&#32;things:&#32;Revised&#32;an...&#34; &#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-35)|Pointer|<pre lang="Turtle"><code>hmas:Affordance&#32;a&#32;skos:Concept&#32;;  &#10; &#32; &#32; &#32; &#32;dc:references&#32; &#91;&#32;rdfs:label&#32; &#34;Chemero&#32;and&#32;Turvey,&#32;2007&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;dc:bibliographicCitation&#32; &#34;Chemero,&#32;A.,&#32;&&#32;Turvey,&#32;M.&#32;T.&#32;(2007).&#32;Complexity,&#32;hypersets,&#32;...&#34; &#32;],  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#91;&#32;rdfs:label&#32; &#34;Norman,&#32;2013&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;dc:bibliographicCitation&#32; &#34;Norman,&#32;D.&#32;(2013).&#32;The&#32;design&#32;of&#32;everyday&#32;things:&#32;Revised&#32;an...&#34; &#32;]&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32;hmas:core&#32;;  &#10; &#32; &#32; &#32; &#32;skos:definition&#32; &#34;A&#32;behavior&#32;possibility&#32;that&#32;is&#32;a&#32;relationship&#32;between&#32;an&#32;abi...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;skos:editorialNote&#32; &#34;The&#32;concept&#32;has&#32;been&#32;considered&#32;as&#32;a&#32;candidate&#32;term&#32;for&#32;repr...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;skos:historyNote&#32; &#34;The&#32;definition&#32;of&#32;the&#32;concept&#32;follows&#32;affordance&#32;theorists&#32; &#91;...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;skos:prefLabel&#32; &#34;affordance&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;skos:related&#32;hmas:Signifier&#32;.</code></pre>|

***
### MinorFail Outcome number 36

[Jump to summary definition](#summary-MinorFail-36)	|	[Previous MinorFail outcome](#minorfail-outcome-number-35)	|	[Next MinorFail outcome](#minorfail-outcome-number-37)

:exclamation:MinorFail outcome
#### Subject detail
|Name|modelet-manufacturing-environments-discover-platforms|
|----|----|
|Title|Standalone&#32;modelet&#32;domains/manufacturing-environments/discover-platforms/onto.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Modelet manufacturing-environments/discover-platforms](https://github.com/HyperAgents/hmas/blob/HEAD/domains/manufacturing-environments/discover-platforms/onto.ttl)|

#### Criterion detail
|Identifier|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|
|----|----|
|Title|Profile&#32;compatibility&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;check&#32;whether&#32;the&#32;test&#32;subject&#32;is&#32;compatible&#32;with&#32;a&#32;profile&#32;or&#32;not,&#32;and&#32;if&#32;it&#32;is&#32;not,&#32;why.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-36)|Identifier|`owl-el-profile-error`|
|[Section top](#minorfail-outcome-number-36)|Title|OWL&#32;EL&#32;Profile&#32;incompatible|
|[Section top](#minorfail-outcome-number-36)|Description|Statement&#32;not&#32;supported|
|[Section top](#minorfail-outcome-number-36)|Pointer|<pre lang="Turtle"><code>hmas:hosts&#32;a&#32;owl:AsymmetricProperty,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:ObjectProperty&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;hosts&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;dc:source&#32; &#60;https://github.com/HyperAgents/ns.hyperagents.org/issues/8#issuecomment-1025991719> &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;A&#32;relation&#32;that&#32;refers&#32;to&#32;an&#32;information&#32;resource&#32;or&#32;a&#32;proce...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:domain&#32;hmas:HypermediaMASPlatform&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32;hmas:core&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:range&#32;hmas:Hostable&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:seeAlso&#32; &#60;https://github.com/HyperAgents/ns.hyperagents.org/issues/18>,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#60;https://github.com/HyperAgents/ns.hyperagents.org/issues/49> &#32;.</code></pre>|

***
### MinorFail Outcome number 37

[Jump to summary definition](#summary-MinorFail-37)	|	[Previous MinorFail outcome](#minorfail-outcome-number-36)	|	[Next MinorFail outcome](#minorfail-outcome-number-38)

:exclamation:MinorFail outcome
#### Subject detail
|Name|modelet-manufacturing-environments-discover-core|
|----|----|
|Title|Standalone&#32;modelet&#32;domains/manufacturing-environments/discover-core/onto.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Modelet manufacturing-environments/discover-core](https://github.com/HyperAgents/hmas/blob/HEAD/domains/manufacturing-environments/discover-core/onto.ttl)|

#### Criterion detail
|Identifier|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|
|----|----|
|Title|Profile&#32;compatibility&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;check&#32;whether&#32;the&#32;test&#32;subject&#32;is&#32;compatible&#32;with&#32;a&#32;profile&#32;or&#32;not,&#32;and&#32;if&#32;it&#32;is&#32;not,&#32;why.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-37)|Identifier|`owl-el-profile-error`|
|[Section top](#minorfail-outcome-number-37)|Title|OWL&#32;EL&#32;Profile&#32;incompatible|
|[Section top](#minorfail-outcome-number-37)|Description|Statement&#32;not&#32;supported|
|[Section top](#minorfail-outcome-number-37)|Pointer|<pre lang="Turtle"><code>hmas:hasProfile&#32;a&#32;owl:AsymmetricProperty,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:ObjectProperty&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;has&#32;profile&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;A&#32;relation&#32;that&#32;links&#32;a&#32;resource&#32;to&#32;its&#32;profile.&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32;hmas:core&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:range&#32;hmas:ResourceProfile&#32;;  &#10; &#32; &#32; &#32; &#32;owl:inverseOf&#32;hmas:isProfileOf&#32;.</code></pre>|

***
### MinorFail Outcome number 38

[Jump to summary definition](#summary-MinorFail-38)	|	[Previous MinorFail outcome](#minorfail-outcome-number-37)	|	[Next MinorFail outcome](#minorfail-outcome-number-39)

:exclamation:MinorFail outcome
#### Subject detail
|Name|modelet-manufacturing-environments-discover-core|
|----|----|
|Title|Standalone&#32;modelet&#32;domains/manufacturing-environments/discover-core/onto.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Modelet manufacturing-environments/discover-core](https://github.com/HyperAgents/hmas/blob/HEAD/domains/manufacturing-environments/discover-core/onto.ttl)|

#### Criterion detail
|Identifier|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|
|----|----|
|Title|Profile&#32;compatibility&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;check&#32;whether&#32;the&#32;test&#32;subject&#32;is&#32;compatible&#32;with&#32;a&#32;profile&#32;or&#32;not,&#32;and&#32;if&#32;it&#32;is&#32;not,&#32;why.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-38)|Identifier|`owl-ql-profile-error`|
|[Section top](#minorfail-outcome-number-38)|Title|OWL&#32;QL&#32;Profile&#32;incompatible|
|[Section top](#minorfail-outcome-number-38)|Description|Statement&#32;not&#32;supported|
|[Section top](#minorfail-outcome-number-38)|Pointer|<pre lang="Turtle"><code>hmas:transitivelyContains&#32;a&#32;owl:ObjectProperty,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:TransitiveProperty&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;transitivelyContains&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;Links&#32;all&#32;the&#32;resources&#32;that&#32;are&#32;logically&#32;contained&#32;in&#32;a&#32;wo...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:domain&#32;hmas:Workspace&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32;hmas:core&#32;;  &#10; &#32; &#32; &#32; &#32;owl:inverseOf&#32;hmas:isTransitivelyContainedIn&#32;.</code></pre>|

***
### MinorFail Outcome number 39

[Jump to summary definition](#summary-MinorFail-39)	|	[Previous MinorFail outcome](#minorfail-outcome-number-38)	|	[Next MinorFail outcome](#minorfail-outcome-number-40)

:exclamation:MinorFail outcome
#### Subject detail
|Name|modelet-logistics-configure-organization|
|----|----|
|Title|Standalone&#32;modelet&#32;domains/logistics/configure-organization/onto.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Modelet logistics/configure-organization](https://github.com/HyperAgents/hmas/blob/HEAD/domains/logistics/configure-organization/onto.ttl)|

#### Criterion detail
|Identifier|[terms-differenciation](https://ns.inria.fr/olivaw#terms-differenciation)|
|----|----|
|Title|Terms&#32;differenciation&#32;test|
|Description|A&#32;test&#32;case&#32;from&#32;the&#32;Best&#32;Practices&#32;tests&#32;checking&#32;if&#32;all&#32;the&#32;terms&#32;are&#32;different&#32;enough&#32;from&#32;each&#32;other&#32;according&#32;to&#32;the&#32;Levenshtein&#32;distance&#32;metric.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-39)|Identifier|`too-close-terms`|
|[Section top](#minorfail-outcome-number-39)|Title|Too&#32;close&#32;terms|
|[Section top](#minorfail-outcome-number-39)|Description|Some&#32;terms&#32;are&#32;too&#32;similar|
|[Section top](#minorfail-outcome-number-39)|Pointer|<pre lang="Turtle"><code>:isAccessTo&#32;a&#32;owl:ObjectProperty&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;is&#32;access&#32;to&#34;@en,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#34;est&#32;l'accès&#32;à&#34;@fr&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;A&#32;relation&#32;that&#32;refers&#32;to&#32;an&#32;Artifact&#32;involved&#32;in&#32;an&#32;Access.&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:domain&#32;:Access&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32;:regulation&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:range&#32;:Artifact&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-39)|Pointer|<pre lang="Turtle"><code>:isAccessOf&#32;a&#32;owl:ObjectProperty&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;is&#32;access&#32;of&#34;@en,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#34;est&#32;l'accès&#32;de&#34;@fr&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;A&#32;relation&#32;that&#32;refers&#32;to&#32;an&#32;Agent&#32;involved&#32;in&#32;an&#32;Access.&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:domain&#32;:Access&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32;:regulation&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:range&#32;:Agent&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-39)|Pointer|<pre lang="Turtle"><code>:isAccessFor&#32;a&#32;owl:ObjectProperty&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;is&#32;access&#32;for&#34;@en,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#34;est&#32;l'accès&#32;pour&#34;@fr&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;A&#32;relation&#32;that&#32;refers&#32;to&#32;a&#32;Usage&#32;involved&#32;in&#32;an&#32;Access.&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:domain&#32;:Access&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32;:regulation&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:range&#32;:Usage&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-39)|Pointer|<pre lang="Turtle"><code>:isUsageOf&#32;a&#32;owl:ObjectProperty&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;is&#32;usage&#32;of&#34;@en,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#34;est&#32;un&#32;usage&#32;de&#34;@fr&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;A&#32;relation&#32;that&#32;refers&#32;to&#32;a&#32;Facility&#32;involved&#32;in&#32;a&#32;Usage.&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:domain&#32;:Usage&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32;:regulation&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:range&#32;:Facility&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-39)|Pointer|<pre lang="Turtle"><code>:isUsageIn&#32;a&#32;owl:ObjectProperty&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;is&#32;usage&#32;in&#34;@en,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#34;est&#32;un&#32;usage&#32;dans&#34;@fr&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;A&#32;relation&#32;that&#32;refers&#32;to&#32;a&#32;Setting&#32;involved&#32;in&#32;a&#32;Usage.&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:domain&#32;:Usage&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32;:regulation&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:range&#32;:Setting&#32;.</code></pre>|

***
### MinorFail Outcome number 40

[Jump to summary definition](#summary-MinorFail-40)	|	[Previous MinorFail outcome](#minorfail-outcome-number-39)	|	[Next MinorFail outcome](#minorfail-outcome-number-41)

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
|[Section top](#minorfail-outcome-number-40)|Identifier|`not-labeled-term`|
|[Section top](#minorfail-outcome-number-40)|Title|Terms&#32;not&#32;labeled|
|[Section top](#minorfail-outcome-number-40)|Description|The&#32;following&#32;terms&#32;have&#32;no&#32;rdfs:label&#32;to&#32;define&#32;it&#32;in&#32;natural&#32;language|
|[Section top](#minorfail-outcome-number-40)|Pointer|<pre lang="Turtle"><code>:Affordance&#32;a&#32;skos:Concept&#32;;  &#10; &#32; &#32; &#32; &#32;dc:references&#32; &#91;&#32;a&#32;owl:NamedIndividual&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;Chemero&#32;and&#32;Turvey,&#32;2007&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;dc:bibliographicCitation&#32; &#34;Chemero,&#32;A.,&#32;&&#32;Turvey,&#32;M.&#32;T.&#32;(2007).&#32;Complexity,&#32;hypersets,&#32;...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;dc:identifier&#32; &#60;https://doi.org/10.1162/biot.2007.2.1.23> &#32;],  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#91;&#32;a&#32;owl:NamedIndividual&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;Norman,&#32;2013&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;dc:bibliographicCitation&#32; &#34;Norman,&#32;D.&#32;(2013).&#32;The&#32;design&#32;of&#32;everyday&#32;things:&#32;Revised&#32;an...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;dc:identifier&#32; &#60;https://mitpress.mit.edu/9780262640374/> &#32;]&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32;:core&#32;;  &#10; &#32; &#32; &#32; &#32;skos:definition&#32; &#34;A&#32;behavior&#32;possibility&#32;that&#32;is&#32;a&#32;relationship&#32;between&#32;an&#32;abi...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;skos:editorialNote&#32; &#34;The&#32;concept&#32;has&#32;been&#32;considered&#32;as&#32;a&#32;candidate&#32;term&#32;for&#32;repr...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;skos:historyNote&#32; &#34;The&#32;definition&#32;of&#32;the&#32;concept&#32;follows&#32;affordance&#32;theorists&#32; &#91;...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;skos:prefLabel&#32; &#34;affordance&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;skos:related&#32;:Signifier&#32;.</code></pre>|

***
### MinorFail Outcome number 41

[Jump to summary definition](#summary-MinorFail-41)	|	[Previous MinorFail outcome](#minorfail-outcome-number-40)	|	[Next MinorFail outcome](#minorfail-outcome-number-42)

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
|[Section top](#minorfail-outcome-number-41)|Identifier|`owl-el-profile-error`|
|[Section top](#minorfail-outcome-number-41)|Title|OWL&#32;EL&#32;Profile&#32;incompatible|
|[Section top](#minorfail-outcome-number-41)|Description|Anonymous&#32;individuals&#32;are&#32;not&#32;supported|
|[Section top](#minorfail-outcome-number-41)|Pointer|<pre lang="Turtle"><code>&#91;]&#32;a&#32;owl:NamedIndividual&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;Chemero&#32;and&#32;Turvey,&#32;2007&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;dc:bibliographicCitation&#32; &#34;Chemero,&#32;A.,&#32;&&#32;Turvey,&#32;M.&#32;T.&#32;(2007).&#32;Complexity,&#32;hypersets,&#32;...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;dc:identifier&#32; &#60;https://doi.org/10.1162/biot.2007.2.1.23> &#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-41)|Pointer|<pre lang="Turtle"><code>&#91;]&#32;a&#32;owl:NamedIndividual&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;Norman,&#32;2013&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;dc:bibliographicCitation&#32; &#34;Norman,&#32;D.&#32;(2013).&#32;The&#32;design&#32;of&#32;everyday&#32;things:&#32;Revised&#32;an...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;dc:identifier&#32; &#60;https://mitpress.mit.edu/9780262640374/> &#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-41)|Pointer|<pre lang="Turtle"><code>hmas:Affordance&#32;a&#32;skos:Concept&#32;;  &#10; &#32; &#32; &#32; &#32;dc:references&#32; &#91;&#32;a&#32;owl:NamedIndividual&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;Chemero&#32;and&#32;Turvey,&#32;2007&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;dc:bibliographicCitation&#32; &#34;Chemero,&#32;A.,&#32;&&#32;Turvey,&#32;M.&#32;T.&#32;(2007).&#32;Complexity,&#32;hypersets,&#32;...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;dc:identifier&#32; &#60;https://doi.org/10.1162/biot.2007.2.1.23> &#32;],  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#91;&#32;a&#32;owl:NamedIndividual&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;Norman,&#32;2013&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;dc:bibliographicCitation&#32; &#34;Norman,&#32;D.&#32;(2013).&#32;The&#32;design&#32;of&#32;everyday&#32;things:&#32;Revised&#32;an...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;dc:identifier&#32; &#60;https://mitpress.mit.edu/9780262640374/> &#32;]&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32;hmas:core&#32;;  &#10; &#32; &#32; &#32; &#32;skos:definition&#32; &#34;A&#32;behavior&#32;possibility&#32;that&#32;is&#32;a&#32;relationship&#32;between&#32;an&#32;abi...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;skos:editorialNote&#32; &#34;The&#32;concept&#32;has&#32;been&#32;considered&#32;as&#32;a&#32;candidate&#32;term&#32;for&#32;repr...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;skos:historyNote&#32; &#34;The&#32;definition&#32;of&#32;the&#32;concept&#32;follows&#32;affordance&#32;theorists&#32; &#91;...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;skos:prefLabel&#32; &#34;affordance&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;skos:related&#32;hmas:Signifier&#32;.</code></pre>|

***
### MinorFail Outcome number 42

[Jump to summary definition](#summary-MinorFail-42)	|	[Previous MinorFail outcome](#minorfail-outcome-number-41)	|	[Next MinorFail outcome](#minorfail-outcome-number-43)

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
|[Section top](#minorfail-outcome-number-42)|Identifier|`owl-el-profile-error`|
|[Section top](#minorfail-outcome-number-42)|Title|OWL&#32;EL&#32;Profile&#32;incompatible|
|[Section top](#minorfail-outcome-number-42)|Description|Statement&#32;not&#32;supported|
|[Section top](#minorfail-outcome-number-42)|Pointer|<pre lang="Turtle"><code>hmas:hasProfile&#32;a&#32;owl:AsymmetricProperty,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:ObjectProperty&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;has&#32;for&#32;profile&#34;@en,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#34;a&#32;pour&#32;profil&#34;@fr&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;A&#32;relation&#32;that&#32;links&#32;a&#32;resource&#32;to&#32;its&#32;profile.&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32;hmas:core&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:range&#32;hmas:ResourceProfile&#32;;  &#10; &#32; &#32; &#32; &#32;owl:inverseOf&#32;hmas:isProfileOf&#32;.</code></pre>|

***
### MinorFail Outcome number 43

[Jump to summary definition](#summary-MinorFail-43)	|	[Previous MinorFail outcome](#minorfail-outcome-number-42)	|	[Next MinorFail outcome](#minorfail-outcome-number-44)

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
|[Section top](#minorfail-outcome-number-43)|Identifier|`owl-ql-profile-error`|
|[Section top](#minorfail-outcome-number-43)|Title|OWL&#32;QL&#32;Profile&#32;incompatible|
|[Section top](#minorfail-outcome-number-43)|Description|Anonymous&#32;individuals&#32;are&#32;not&#32;supported|
|[Section top](#minorfail-outcome-number-43)|Pointer|<pre lang="Turtle"><code>&#91;]&#32;a&#32;owl:NamedIndividual&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;Chemero&#32;and&#32;Turvey,&#32;2007&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;dc:bibliographicCitation&#32; &#34;Chemero,&#32;A.,&#32;&&#32;Turvey,&#32;M.&#32;T.&#32;(2007).&#32;Complexity,&#32;hypersets,&#32;...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;dc:identifier&#32; &#60;https://doi.org/10.1162/biot.2007.2.1.23> &#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-43)|Pointer|<pre lang="Turtle"><code>&#91;]&#32;a&#32;owl:NamedIndividual&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;Norman,&#32;2013&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;dc:bibliographicCitation&#32; &#34;Norman,&#32;D.&#32;(2013).&#32;The&#32;design&#32;of&#32;everyday&#32;things:&#32;Revised&#32;an...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;dc:identifier&#32; &#60;https://mitpress.mit.edu/9780262640374/> &#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-43)|Pointer|<pre lang="Turtle"><code>hmas:Affordance&#32;a&#32;skos:Concept&#32;;  &#10; &#32; &#32; &#32; &#32;dc:references&#32; &#91;&#32;a&#32;owl:NamedIndividual&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;Chemero&#32;and&#32;Turvey,&#32;2007&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;dc:bibliographicCitation&#32; &#34;Chemero,&#32;A.,&#32;&&#32;Turvey,&#32;M.&#32;T.&#32;(2007).&#32;Complexity,&#32;hypersets,&#32;...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;dc:identifier&#32; &#60;https://doi.org/10.1162/biot.2007.2.1.23> &#32;],  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#91;&#32;a&#32;owl:NamedIndividual&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;Norman,&#32;2013&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;dc:bibliographicCitation&#32; &#34;Norman,&#32;D.&#32;(2013).&#32;The&#32;design&#32;of&#32;everyday&#32;things:&#32;Revised&#32;an...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;dc:identifier&#32; &#60;https://mitpress.mit.edu/9780262640374/> &#32;]&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32;hmas:core&#32;;  &#10; &#32; &#32; &#32; &#32;skos:definition&#32; &#34;A&#32;behavior&#32;possibility&#32;that&#32;is&#32;a&#32;relationship&#32;between&#32;an&#32;abi...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;skos:editorialNote&#32; &#34;The&#32;concept&#32;has&#32;been&#32;considered&#32;as&#32;a&#32;candidate&#32;term&#32;for&#32;repr...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;skos:historyNote&#32; &#34;The&#32;definition&#32;of&#32;the&#32;concept&#32;follows&#32;affordance&#32;theorists&#32; &#91;...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;skos:prefLabel&#32; &#34;affordance&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;skos:related&#32;hmas:Signifier&#32;.</code></pre>|

***
### MinorFail Outcome number 44

[Jump to summary definition](#summary-MinorFail-44)	|	[Previous MinorFail outcome](#minorfail-outcome-number-43)	|	[Next MinorFail outcome](#minorfail-outcome-number-45)

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
|[Section top](#minorfail-outcome-number-44)|Identifier|`owl-ql-profile-error`|
|[Section top](#minorfail-outcome-number-44)|Title|OWL&#32;QL&#32;Profile&#32;incompatible|
|[Section top](#minorfail-outcome-number-44)|Description|Class&#32;Expression&#32;not&#32;supported&#32;with&#32;rdfs:subClassOf|
|[Section top](#minorfail-outcome-number-44)|Pointer|<pre lang="Turtle"><code>&#60;https://www.w3.org/2019/wot/td#InteractionAffordance> &#32;rdfs:comment&#32; &#34;Using&#32;a&#32;TD&#32;Interaction&#32;Affordance&#32;results&#32;in&#32;an&#32;action&#32;execu...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:subClassOf&#32; &#91;&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:hasValue&#32;hmas:ActionExecution&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:onProperty&#32;sh:class&#32;]&#32;.</code></pre>|

***
### MinorFail Outcome number 45

[Jump to summary definition](#summary-MinorFail-45)	|	[Previous MinorFail outcome](#minorfail-outcome-number-44)	|	[Next MinorFail outcome](#minorfail-outcome-number-46)

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
|[Section top](#minorfail-outcome-number-45)|Identifier|`owl-ql-profile-error`|
|[Section top](#minorfail-outcome-number-45)|Title|OWL&#32;QL&#32;Profile&#32;incompatible|
|[Section top](#minorfail-outcome-number-45)|Description|Statement&#32;not&#32;supported  &#10;Statement&#32;not&#32;supported&#32;in&#32;a&#32;Super&#32;Class&#32;Expression|
|[Section top](#minorfail-outcome-number-45)|Pointer|<pre lang="Turtle"><code>&#91;]&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32;owl:hasValue&#32;hmas:ActionExecution&#32;;  &#10; &#32; &#32; &#32; &#32;owl:onProperty&#32;sh:class&#32;.</code></pre>|

***
### MinorFail Outcome number 46

[Jump to summary definition](#summary-MinorFail-46)	|	[Previous MinorFail outcome](#minorfail-outcome-number-45)	|	[Next MinorFail outcome](#minorfail-outcome-number-47)

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
|[Section top](#minorfail-outcome-number-46)|Identifier|`no-reference-module`|
|[Section top](#minorfail-outcome-number-46)|Title|Term&#32;not&#32;referenced&#32;to&#32;a&#32;module|
|[Section top](#minorfail-outcome-number-46)|Description|Subject&#32;terms&#32;not&#32;linked&#32;to&#32;a&#32;module&#32;by&#32;a&#32;rdfs:isDefinedBy&#32;property|
|[Section top](#minorfail-outcome-number-46)|Pointer|<pre lang="Turtle"><code>:hasServiceName&#32;a&#32;owl:ObjectProperty&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;has&#32;Service&#32;Name&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:domain&#32;:APService&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-46)|Pointer|<pre lang="Turtle"><code>:APService&#32;a&#32;owl:Class&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;Agent&#32;Platform&#32;Service&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;A&#32;service&#32;exposed&#32;by&#32;a&#32;FIPA&#32;Agent&#32;Platform&#32;as&#32;defined&#32;by&#32;the...&#34; &#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-46)|Pointer|<pre lang="Turtle"><code>:hasServiceType&#32;a&#32;owl:ObjectProperty&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;has&#32;Service&#32;Type&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:domain&#32;:APService&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-46)|Pointer|<pre lang="Turtle"><code>:AgentIdentifierDescription&#32;a&#32;owl:Class&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;Agent&#32;Identifier&#32;Description&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;A&#32;resource&#32;profile&#32;that&#32;describes&#32;an&#32;agent&#32;using&#32;the&#32;Agent&#32;I...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:subClassOf&#32; &#60;https://ci.mines-stetienne.fr/hmas#ResourceProfile> &#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-46)|Pointer|<pre lang="Turtle"><code>:AgentPlatformDescription&#32;a&#32;owl:Class&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;Agent&#32;Platform&#32;Description&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;A&#32;resource&#32;profile&#32;that&#32;descripe&#32;a&#32;FIPA&#32;Agent&#32;Platform&#32;using...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:subClassOf&#32; &#60;https://ci.mines-stetienne.fr/hmas#ResourceProfile> &#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-46)|Pointer|<pre lang="Turtle"><code>:FIPAAgentPlatform&#32;a&#32;owl:Class&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;FIPA&#32;Agent&#32;Platform&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;A&#32;platform&#32;that&#32;conforms&#32;to&#32;the&#32;FIPA&#32;Abstract&#32;Architecture&#32;S...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:subClassOf&#32; &#60;https://ci.mines-stetienne.fr/hmas#Platform> &#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-46)|Pointer|<pre lang="Turtle"><code>:HTTPMessageTransportService&#32;a&#32;owl:Class&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;HTTP&#32;Message&#32;Transport&#32;Service&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;An&#32;HTTP-based&#32;message&#32;transport&#32;service&#32;that&#32;confirms&#32;to&#32;the...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:subClassOf&#32;:MessageTransportService&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-46)|Pointer|<pre lang="Turtle"><code>:MessageTransportService&#32;a&#32;owl:Class&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;Message&#32;Transport&#32;Service&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;A&#32;service&#32;for&#32;transporting&#32;messages&#32;among&#32;agents&#32;that&#32;confor...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:subClassOf&#32;:APService&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-46)|Pointer|<pre lang="Turtle"><code>:IIOPMessageTransportService&#32;a&#32;owl:Class&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;IIOP&#32;Message&#32;Transport&#32;Service&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;An&#32;HTTP-based&#32;message&#32;transport&#32;service&#32;that&#32;confirms&#32;to&#32;the...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:subClassOf&#32;:MessageTransportService&#32;.</code></pre>|

***
### MinorFail Outcome number 47

[Jump to summary definition](#summary-MinorFail-47)	|	[Previous MinorFail outcome](#minorfail-outcome-number-46)	|	[Next MinorFail outcome](#minorfail-outcome-number-48)

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
|[Section top](#minorfail-outcome-number-47)|Identifier|`too-close-terms`|
|[Section top](#minorfail-outcome-number-47)|Title|Too&#32;close&#32;terms|
|[Section top](#minorfail-outcome-number-47)|Description|Some&#32;terms&#32;are&#32;too&#32;similar|
|[Section top](#minorfail-outcome-number-47)|Pointer|<pre lang="Turtle"><code>:isAccessTo&#32;a&#32;owl:ObjectProperty&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;is&#32;access&#32;to&#34;@en,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#34;est&#32;l'accès&#32;à&#34;@fr&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;A&#32;relation&#32;that&#32;refers&#32;to&#32;an&#32;Artifact&#32;involved&#32;in&#32;an&#32;Access.&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:domain&#32;:Access&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32;:regulation&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:range&#32;:Artifact&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-47)|Pointer|<pre lang="Turtle"><code>:isAccessOf&#32;a&#32;owl:ObjectProperty&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;is&#32;access&#32;of&#34;@en,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#34;est&#32;l'accès&#32;de&#34;@fr&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;A&#32;relation&#32;that&#32;refers&#32;to&#32;an&#32;Agent&#32;involved&#32;in&#32;an&#32;Access.&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:domain&#32;:Access&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32;:regulation&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:range&#32;:Agent&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-47)|Pointer|<pre lang="Turtle"><code>:isAccessFor&#32;a&#32;owl:ObjectProperty&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;is&#32;access&#32;for&#34;@en,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#34;est&#32;l'accès&#32;pour&#34;@fr&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;A&#32;relation&#32;that&#32;refers&#32;to&#32;a&#32;Usage&#32;involved&#32;in&#32;an&#32;Access.&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:domain&#32;:Access&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32;:regulation&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:range&#32;:Usage&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-47)|Pointer|<pre lang="Turtle"><code>:isMembershipOf&#32;a&#32;owl:ObjectProperty&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;is&#32;membership&#32;of&#34;@en,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#34;est&#32;l'appartenance&#32;à&#34;@fr&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;A&#32;relation&#32;that&#32;refers&#32;to&#32;the&#32;Agent&#32;involved&#32;in&#32;a&#32;Membership...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:domain&#32;:Membership&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32;:regulation&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:range&#32;:Agent&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-47)|Pointer|<pre lang="Turtle"><code>:isMembershipIn&#32;a&#32;owl:ObjectProperty&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;is&#32;membership&#32;in&#34;@en,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#34;est&#32;l'appartenance&#32;à&#34;@fr&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;A&#32;relation&#32;that&#32;refers&#32;to&#32;the&#32;Group&#32;involved&#32;in&#32;a&#32;Membership...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:domain&#32;:Membership&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32;:regulation&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:range&#32;:Group&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-47)|Pointer|<pre lang="Turtle"><code>:isUsageOf&#32;a&#32;owl:ObjectProperty&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;is&#32;usage&#32;of&#34;@en,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#34;est&#32;un&#32;usage&#32;de&#34;@fr&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;A&#32;relation&#32;that&#32;refers&#32;to&#32;a&#32;Facility&#32;involved&#32;in&#32;a&#32;Usage.&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:domain&#32;:Usage&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32;:regulation&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:range&#32;:Facility&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-47)|Pointer|<pre lang="Turtle"><code>:isUsageIn&#32;a&#32;owl:ObjectProperty&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;is&#32;usage&#32;in&#34;@en,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#34;est&#32;un&#32;usage&#32;dans&#34;@fr&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;A&#32;relation&#32;that&#32;refers&#32;to&#32;a&#32;Setting&#32;involved&#32;in&#32;a&#32;Usage.&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:domain&#32;:Usage&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32;:regulation&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:range&#32;:Setting&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-47)|Pointer|<pre lang="Turtle"><code>:signifies&#32;a&#32;owl:ObjectProperty&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;signifies&#34;@en,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#34;signifie&#34;@fr&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;A&#32;relation&#32;between&#32;a&#32;signifier&#32;and&#32;the&#32;specification&#32;of&#32;a&#32;be...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:domain&#32;:Signifier&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32;:interaction&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-47)|Pointer|<pre lang="Turtle"><code>:Signifier&#32;a&#32;owl:Class&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;signifier&#34;@en,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#34;signifiant&#34;@fr&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;A&#32;perceivable&#32;sign/cue&#32;that&#32;can&#32;be&#32;interpreted&#32;meaningfully&#32;...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32;:core&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:seeAlso&#32; &#60;https://github.com/HyperAgents/ns.hyperagents.org/issues/13#issuecomment-1028904491>,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#60;https://github.com/HyperAgents/ns.hyperagents.org/issues/41> &#32;;  &#10; &#32; &#32; &#32; &#32;skos:note&#32; &#34;:Signifier&#32;works&#32;as&#32;a&#32;bridge&#32;between&#32;the&#32;Core&#32;and&#32;the&#32;Intera...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;skos:related&#32;:Affordance&#32;.</code></pre>|

***
### MinorFail Outcome number 48

[Jump to summary definition](#summary-MinorFail-48)	|	[Previous MinorFail outcome](#minorfail-outcome-number-47)	|	[Next MinorFail outcome](#minorfail-outcome-number-49)

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
|[Section top](#minorfail-outcome-number-48)|Identifier|`not-labeled-term`|
|[Section top](#minorfail-outcome-number-48)|Title|Terms&#32;not&#32;labeled|
|[Section top](#minorfail-outcome-number-48)|Description|The&#32;following&#32;terms&#32;have&#32;no&#32;rdfs:label&#32;to&#32;define&#32;it&#32;in&#32;natural&#32;language|
|[Section top](#minorfail-outcome-number-48)|Pointer|<pre lang="Turtle"><code>:Affordance&#32;a&#32;skos:Concept&#32;;  &#10; &#32; &#32; &#32; &#32;dc:references&#32; &#91;&#32;a&#32;owl:NamedIndividual&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;Chemero&#32;and&#32;Turvey,&#32;2007&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;dc:bibliographicCitation&#32; &#34;Chemero,&#32;A.,&#32;&&#32;Turvey,&#32;M.&#32;T.&#32;(2007).&#32;Complexity,&#32;hypersets,&#32;...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;dc:identifier&#32; &#60;https://doi.org/10.1162/biot.2007.2.1.23> &#32;],  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#91;&#32;a&#32;owl:NamedIndividual&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;Norman,&#32;2013&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;dc:bibliographicCitation&#32; &#34;Norman,&#32;D.&#32;(2013).&#32;The&#32;design&#32;of&#32;everyday&#32;things:&#32;Revised&#32;an...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;dc:identifier&#32; &#60;https://mitpress.mit.edu/9780262640374/> &#32;],  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#91;&#32;rdfs:label&#32; &#34;Chemero&#32;and&#32;Turvey,&#32;2007&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;dc:bibliographicCitation&#32; &#34;Chemero,&#32;A.,&#32;&&#32;Turvey,&#32;M.&#32;T.&#32;(2007).&#32;Complexity,&#32;hypersets,&#32;...&#34; &#32;],  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#91;&#32;rdfs:label&#32; &#34;Norman,&#32;2013&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;dc:bibliographicCitation&#32; &#34;Norman,&#32;D.&#32;(2013).&#32;The&#32;design&#32;of&#32;everyday&#32;things:&#32;Revised&#32;an...&#34; &#32;]&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32;:core&#32;;  &#10; &#32; &#32; &#32; &#32;skos:definition&#32; &#34;A&#32;behavior&#32;possibility&#32;that&#32;is&#32;a&#32;relationship&#32;between&#32;an&#32;abi...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;skos:editorialNote&#32; &#34;The&#32;concept&#32;has&#32;been&#32;considered&#32;as&#32;a&#32;candidate&#32;term&#32;for&#32;repr...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;skos:historyNote&#32; &#34;The&#32;definition&#32;of&#32;the&#32;concept&#32;follows&#32;affordance&#32;theorists&#32; &#91;...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;skos:prefLabel&#32; &#34;affordance&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;skos:related&#32;:Signifier&#32;.</code></pre>|

***
### MinorFail Outcome number 49

[Jump to summary definition](#summary-MinorFail-49)	|	[Previous MinorFail outcome](#minorfail-outcome-number-48)	|	[Next MinorFail outcome](#minorfail-outcome-number-50)

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
|[Section top](#minorfail-outcome-number-49)|Identifier|`owl-el-profile-error`|
|[Section top](#minorfail-outcome-number-49)|Title|OWL&#32;EL&#32;Profile&#32;incompatible|
|[Section top](#minorfail-outcome-number-49)|Description|Anonymous&#32;individuals&#32;are&#32;not&#32;supported|
|[Section top](#minorfail-outcome-number-49)|Pointer|<pre lang="Turtle"><code>&#91;]&#32;a&#32;owl:NamedIndividual&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;Chemero&#32;and&#32;Turvey,&#32;2007&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;dc:bibliographicCitation&#32; &#34;Chemero,&#32;A.,&#32;&&#32;Turvey,&#32;M.&#32;T.&#32;(2007).&#32;Complexity,&#32;hypersets,&#32;...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;dc:identifier&#32; &#60;https://doi.org/10.1162/biot.2007.2.1.23> &#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-49)|Pointer|<pre lang="Turtle"><code>&#91;]&#32;a&#32;owl:NamedIndividual&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;Norman,&#32;2013&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;dc:bibliographicCitation&#32; &#34;Norman,&#32;D.&#32;(2013).&#32;The&#32;design&#32;of&#32;everyday&#32;things:&#32;Revised&#32;an...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;dc:identifier&#32; &#60;https://mitpress.mit.edu/9780262640374/> &#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-49)|Pointer|<pre lang="Turtle"><code>&#91;]&#32;rdfs:label&#32; &#34;Chemero&#32;and&#32;Turvey,&#32;2007&#34;@en&#32;;  &#10; &#32; &#32;&#32; &#32;dc:bibliographicCitation&#32; &#34;Chemero,&#32;A.,&#32;&&#32;Turvey,&#32;M.&#32;T.&#32;(2007).&#32;Complexity,&#32;hypersets,&#32;...&#34; &#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-49)|Pointer|<pre lang="Turtle"><code>&#91;]&#32;rdfs:label&#32; &#34;Norman,&#32;2013&#34;@en&#32;;  &#10; &#32; &#32;&#32; &#32;dc:bibliographicCitation&#32; &#34;Norman,&#32;D.&#32;(2013).&#32;The&#32;design&#32;of&#32;everyday&#32;things:&#32;Revised&#32;an...&#34; &#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-49)|Pointer|<pre lang="Turtle"><code>hmas:Affordance&#32;a&#32;skos:Concept&#32;;  &#10; &#32; &#32; &#32; &#32;dc:references&#32; &#91;&#32;a&#32;owl:NamedIndividual&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;Chemero&#32;and&#32;Turvey,&#32;2007&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;dc:bibliographicCitation&#32; &#34;Chemero,&#32;A.,&#32;&&#32;Turvey,&#32;M.&#32;T.&#32;(2007).&#32;Complexity,&#32;hypersets,&#32;...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;dc:identifier&#32; &#60;https://doi.org/10.1162/biot.2007.2.1.23> &#32;],  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#91;&#32;a&#32;owl:NamedIndividual&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;Norman,&#32;2013&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;dc:bibliographicCitation&#32; &#34;Norman,&#32;D.&#32;(2013).&#32;The&#32;design&#32;of&#32;everyday&#32;things:&#32;Revised&#32;an...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;dc:identifier&#32; &#60;https://mitpress.mit.edu/9780262640374/> &#32;],  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#91;&#32;rdfs:label&#32; &#34;Chemero&#32;and&#32;Turvey,&#32;2007&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;dc:bibliographicCitation&#32; &#34;Chemero,&#32;A.,&#32;&&#32;Turvey,&#32;M.&#32;T.&#32;(2007).&#32;Complexity,&#32;hypersets,&#32;...&#34; &#32;],  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#91;&#32;rdfs:label&#32; &#34;Norman,&#32;2013&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;dc:bibliographicCitation&#32; &#34;Norman,&#32;D.&#32;(2013).&#32;The&#32;design&#32;of&#32;everyday&#32;things:&#32;Revised&#32;an...&#34; &#32;]&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32;hmas:core&#32;;  &#10; &#32; &#32; &#32; &#32;skos:definition&#32; &#34;A&#32;behavior&#32;possibility&#32;that&#32;is&#32;a&#32;relationship&#32;between&#32;an&#32;abi...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;skos:editorialNote&#32; &#34;The&#32;concept&#32;has&#32;been&#32;considered&#32;as&#32;a&#32;candidate&#32;term&#32;for&#32;repr...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;skos:historyNote&#32; &#34;The&#32;definition&#32;of&#32;the&#32;concept&#32;follows&#32;affordance&#32;theorists&#32; &#91;...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;skos:prefLabel&#32; &#34;affordance&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;skos:related&#32;hmas:Signifier&#32;.</code></pre>|

***
### MinorFail Outcome number 50

[Jump to summary definition](#summary-MinorFail-50)	|	[Previous MinorFail outcome](#minorfail-outcome-number-49)	|	[Next MinorFail outcome](#minorfail-outcome-number-51)

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
|[Section top](#minorfail-outcome-number-50)|Identifier|`owl-el-profile-error`|
|[Section top](#minorfail-outcome-number-50)|Title|OWL&#32;EL&#32;Profile&#32;incompatible|
|[Section top](#minorfail-outcome-number-50)|Description|Statement&#32;not&#32;supported|
|[Section top](#minorfail-outcome-number-50)|Pointer|<pre lang="Turtle"><code>hmas:hasProfile&#32;a&#32;owl:AsymmetricProperty,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:ObjectProperty&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;has&#32;for&#32;profile&#34;@en,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#34;has&#32;profile&#34;@en,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#34;a&#32;pour&#32;profil&#34;@fr&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;A&#32;relation&#32;that&#32;links&#32;a&#32;resource&#32;to&#32;its&#32;profile.&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32;hmas:core&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:range&#32;hmas:ResourceProfile&#32;;  &#10; &#32; &#32; &#32; &#32;owl:inverseOf&#32;hmas:isProfileOf&#32;.</code></pre>|

***
### MinorFail Outcome number 51

[Jump to summary definition](#summary-MinorFail-51)	|	[Previous MinorFail outcome](#minorfail-outcome-number-50)	|	[Next MinorFail outcome](#minorfail-outcome-number-52)

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
|[Section top](#minorfail-outcome-number-51)|Identifier|`owl-ql-profile-error`|
|[Section top](#minorfail-outcome-number-51)|Title|OWL&#32;QL&#32;Profile&#32;incompatible|
|[Section top](#minorfail-outcome-number-51)|Description|Anonymous&#32;individuals&#32;are&#32;not&#32;supported|
|[Section top](#minorfail-outcome-number-51)|Pointer|<pre lang="Turtle"><code>&#91;]&#32;a&#32;owl:NamedIndividual&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;Chemero&#32;and&#32;Turvey,&#32;2007&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;dc:bibliographicCitation&#32; &#34;Chemero,&#32;A.,&#32;&&#32;Turvey,&#32;M.&#32;T.&#32;(2007).&#32;Complexity,&#32;hypersets,&#32;...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;dc:identifier&#32; &#60;https://doi.org/10.1162/biot.2007.2.1.23> &#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-51)|Pointer|<pre lang="Turtle"><code>&#91;]&#32;a&#32;owl:NamedIndividual&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;Norman,&#32;2013&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;dc:bibliographicCitation&#32; &#34;Norman,&#32;D.&#32;(2013).&#32;The&#32;design&#32;of&#32;everyday&#32;things:&#32;Revised&#32;an...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;dc:identifier&#32; &#60;https://mitpress.mit.edu/9780262640374/> &#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-51)|Pointer|<pre lang="Turtle"><code>&#91;]&#32;rdfs:label&#32; &#34;Chemero&#32;and&#32;Turvey,&#32;2007&#34;@en&#32;;  &#10; &#32; &#32;&#32; &#32;dc:bibliographicCitation&#32; &#34;Chemero,&#32;A.,&#32;&&#32;Turvey,&#32;M.&#32;T.&#32;(2007).&#32;Complexity,&#32;hypersets,&#32;...&#34; &#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-51)|Pointer|<pre lang="Turtle"><code>&#91;]&#32;rdfs:label&#32; &#34;Norman,&#32;2013&#34;@en&#32;;  &#10; &#32; &#32;&#32; &#32;dc:bibliographicCitation&#32; &#34;Norman,&#32;D.&#32;(2013).&#32;The&#32;design&#32;of&#32;everyday&#32;things:&#32;Revised&#32;an...&#34; &#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-51)|Pointer|<pre lang="Turtle"><code>hmas:Affordance&#32;a&#32;skos:Concept&#32;;  &#10; &#32; &#32; &#32; &#32;dc:references&#32; &#91;&#32;a&#32;owl:NamedIndividual&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;Chemero&#32;and&#32;Turvey,&#32;2007&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;dc:bibliographicCitation&#32; &#34;Chemero,&#32;A.,&#32;&&#32;Turvey,&#32;M.&#32;T.&#32;(2007).&#32;Complexity,&#32;hypersets,&#32;...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;dc:identifier&#32; &#60;https://doi.org/10.1162/biot.2007.2.1.23> &#32;],  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#91;&#32;a&#32;owl:NamedIndividual&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;Norman,&#32;2013&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;dc:bibliographicCitation&#32; &#34;Norman,&#32;D.&#32;(2013).&#32;The&#32;design&#32;of&#32;everyday&#32;things:&#32;Revised&#32;an...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;dc:identifier&#32; &#60;https://mitpress.mit.edu/9780262640374/> &#32;],  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#91;&#32;rdfs:label&#32; &#34;Chemero&#32;and&#32;Turvey,&#32;2007&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;dc:bibliographicCitation&#32; &#34;Chemero,&#32;A.,&#32;&&#32;Turvey,&#32;M.&#32;T.&#32;(2007).&#32;Complexity,&#32;hypersets,&#32;...&#34; &#32;],  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#91;&#32;rdfs:label&#32; &#34;Norman,&#32;2013&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;dc:bibliographicCitation&#32; &#34;Norman,&#32;D.&#32;(2013).&#32;The&#32;design&#32;of&#32;everyday&#32;things:&#32;Revised&#32;an...&#34; &#32;]&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32;hmas:core&#32;;  &#10; &#32; &#32; &#32; &#32;skos:definition&#32; &#34;A&#32;behavior&#32;possibility&#32;that&#32;is&#32;a&#32;relationship&#32;between&#32;an&#32;abi...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;skos:editorialNote&#32; &#34;The&#32;concept&#32;has&#32;been&#32;considered&#32;as&#32;a&#32;candidate&#32;term&#32;for&#32;repr...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;skos:historyNote&#32; &#34;The&#32;definition&#32;of&#32;the&#32;concept&#32;follows&#32;affordance&#32;theorists&#32; &#91;...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;skos:prefLabel&#32; &#34;affordance&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;skos:related&#32;hmas:Signifier&#32;.</code></pre>|

***
### MinorFail Outcome number 52

[Jump to summary definition](#summary-MinorFail-52)	|	[Previous MinorFail outcome](#minorfail-outcome-number-51)	|	[Next MinorFail outcome](#minorfail-outcome-number-53)

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
|[Section top](#minorfail-outcome-number-52)|Identifier|`owl-ql-profile-error`|
|[Section top](#minorfail-outcome-number-52)|Title|OWL&#32;QL&#32;Profile&#32;incompatible|
|[Section top](#minorfail-outcome-number-52)|Description|Class&#32;Expression&#32;not&#32;supported&#32;with&#32;rdfs:subClassOf|
|[Section top](#minorfail-outcome-number-52)|Pointer|<pre lang="Turtle"><code>&#60;https://www.w3.org/2019/wot/td#InteractionAffordance> &#32;rdfs:comment&#32; &#34;Using&#32;a&#32;TD&#32;Interaction&#32;Affordance&#32;results&#32;in&#32;an&#32;action&#32;execu...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:subClassOf&#32; &#91;&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:hasValue&#32;hmas:ActionExecution&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:onProperty&#32;sh:class&#32;]&#32;.</code></pre>|

***
### MinorFail Outcome number 53

[Jump to summary definition](#summary-MinorFail-53)	|	[Previous MinorFail outcome](#minorfail-outcome-number-52)	|	[Next MinorFail outcome](#minorfail-outcome-number-54)

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
|[Section top](#minorfail-outcome-number-53)|Identifier|`owl-ql-profile-error`|
|[Section top](#minorfail-outcome-number-53)|Title|OWL&#32;QL&#32;Profile&#32;incompatible|
|[Section top](#minorfail-outcome-number-53)|Description|Statement&#32;not&#32;supported  &#10;Statement&#32;not&#32;supported&#32;in&#32;a&#32;Super&#32;Class&#32;Expression|
|[Section top](#minorfail-outcome-number-53)|Pointer|<pre lang="Turtle"><code>&#91;]&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32;owl:hasValue&#32;hmas:ActionExecution&#32;;  &#10; &#32; &#32; &#32; &#32;owl:onProperty&#32;sh:class&#32;.</code></pre>|

***
### MinorFail Outcome number 54

[Jump to summary definition](#summary-MinorFail-54)	|	[Previous MinorFail outcome](#minorfail-outcome-number-53)	|	[Next MinorFail outcome](#minorfail-outcome-number-55)

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
|[Section top](#minorfail-outcome-number-54)|Identifier|`no-reference-module`|
|[Section top](#minorfail-outcome-number-54)|Title|Term&#32;not&#32;referenced&#32;to&#32;a&#32;module|
|[Section top](#minorfail-outcome-number-54)|Description|Subject&#32;terms&#32;not&#32;linked&#32;to&#32;a&#32;module&#32;by&#32;a&#32;rdfs:isDefinedBy&#32;property|
|[Section top](#minorfail-outcome-number-54)|Pointer|<pre lang="Turtle"><code>:hasServiceName&#32;a&#32;owl:ObjectProperty&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;has&#32;Service&#32;Name&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:domain&#32;:APService&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-54)|Pointer|<pre lang="Turtle"><code>:APService&#32;a&#32;owl:Class&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;Agent&#32;Platform&#32;Service&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;A&#32;service&#32;exposed&#32;by&#32;a&#32;FIPA&#32;Agent&#32;Platform&#32;as&#32;defined&#32;by&#32;the...&#34; &#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-54)|Pointer|<pre lang="Turtle"><code>:hasServiceType&#32;a&#32;owl:ObjectProperty&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;has&#32;Service&#32;Type&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:domain&#32;:APService&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-54)|Pointer|<pre lang="Turtle"><code>:AgentIdentifierDescription&#32;a&#32;owl:Class&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;Agent&#32;Identifier&#32;Description&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;A&#32;resource&#32;profile&#32;that&#32;describes&#32;an&#32;agent&#32;using&#32;the&#32;Agent&#32;I...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:subClassOf&#32; &#60;https://ci.mines-stetienne.fr/hmas#ResourceProfile> &#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-54)|Pointer|<pre lang="Turtle"><code>:AgentPlatformDescription&#32;a&#32;owl:Class&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;Agent&#32;Platform&#32;Description&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;A&#32;resource&#32;profile&#32;that&#32;descripe&#32;a&#32;FIPA&#32;Agent&#32;Platform&#32;using...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:subClassOf&#32; &#60;https://ci.mines-stetienne.fr/hmas#ResourceProfile> &#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-54)|Pointer|<pre lang="Turtle"><code>:FIPAAgentPlatform&#32;a&#32;owl:Class&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;FIPA&#32;Agent&#32;Platform&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;A&#32;platform&#32;that&#32;conforms&#32;to&#32;the&#32;FIPA&#32;Abstract&#32;Architecture&#32;S...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:subClassOf&#32; &#60;https://ci.mines-stetienne.fr/hmas#Platform> &#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-54)|Pointer|<pre lang="Turtle"><code>:HTTPMessageTransportService&#32;a&#32;owl:Class&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;HTTP&#32;Message&#32;Transport&#32;Service&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;An&#32;HTTP-based&#32;message&#32;transport&#32;service&#32;that&#32;confirms&#32;to&#32;the...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:subClassOf&#32;:MessageTransportService&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-54)|Pointer|<pre lang="Turtle"><code>:MessageTransportService&#32;a&#32;owl:Class&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;Message&#32;Transport&#32;Service&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;A&#32;service&#32;for&#32;transporting&#32;messages&#32;among&#32;agents&#32;that&#32;confor...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:subClassOf&#32;:APService&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-54)|Pointer|<pre lang="Turtle"><code>:IIOPMessageTransportService&#32;a&#32;owl:Class&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;IIOP&#32;Message&#32;Transport&#32;Service&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;An&#32;HTTP-based&#32;message&#32;transport&#32;service&#32;that&#32;confirms&#32;to&#32;the...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:subClassOf&#32;:MessageTransportService&#32;.</code></pre>|

***
### MinorFail Outcome number 55

[Jump to summary definition](#summary-MinorFail-55)	|	[Previous MinorFail outcome](#minorfail-outcome-number-54)	|	Next MinorFail outcome

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
|[Section top](#minorfail-outcome-number-55)|Identifier|`too-close-terms`|
|[Section top](#minorfail-outcome-number-55)|Title|Too&#32;close&#32;terms|
|[Section top](#minorfail-outcome-number-55)|Description|Some&#32;terms&#32;are&#32;too&#32;similar|
|[Section top](#minorfail-outcome-number-55)|Pointer|<pre lang="Turtle"><code>:isAccessTo&#32;a&#32;owl:ObjectProperty&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;is&#32;access&#32;to&#34;@en,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#34;est&#32;l'accès&#32;à&#34;@fr&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;A&#32;relation&#32;that&#32;refers&#32;to&#32;an&#32;Artifact&#32;involved&#32;in&#32;an&#32;Access.&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:domain&#32;:Access&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32;:regulation&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:range&#32;:Artifact&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-55)|Pointer|<pre lang="Turtle"><code>:isAccessOf&#32;a&#32;owl:ObjectProperty&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;is&#32;access&#32;of&#34;@en,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#34;est&#32;l'accès&#32;de&#34;@fr&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;A&#32;relation&#32;that&#32;refers&#32;to&#32;an&#32;Agent&#32;involved&#32;in&#32;an&#32;Access.&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:domain&#32;:Access&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32;:regulation&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:range&#32;:Agent&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-55)|Pointer|<pre lang="Turtle"><code>:isAccessFor&#32;a&#32;owl:ObjectProperty&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;is&#32;access&#32;for&#34;@en,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#34;est&#32;l'accès&#32;pour&#34;@fr&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;A&#32;relation&#32;that&#32;refers&#32;to&#32;a&#32;Usage&#32;involved&#32;in&#32;an&#32;Access.&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:domain&#32;:Access&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32;:regulation&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:range&#32;:Usage&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-55)|Pointer|<pre lang="Turtle"><code>:isMembershipOf&#32;a&#32;owl:ObjectProperty&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;is&#32;membership&#32;of&#34;@en,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#34;est&#32;l'appartenance&#32;à&#34;@fr&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;A&#32;relation&#32;that&#32;refers&#32;to&#32;the&#32;Agent&#32;involved&#32;in&#32;a&#32;Membership...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:domain&#32;:Membership&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32;:regulation&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:range&#32;:Agent&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-55)|Pointer|<pre lang="Turtle"><code>:isMembershipIn&#32;a&#32;owl:ObjectProperty&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;is&#32;membership&#32;in&#34;@en,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#34;est&#32;l'appartenance&#32;à&#34;@fr&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;A&#32;relation&#32;that&#32;refers&#32;to&#32;the&#32;Group&#32;involved&#32;in&#32;a&#32;Membership...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:domain&#32;:Membership&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32;:regulation&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:range&#32;:Group&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-55)|Pointer|<pre lang="Turtle"><code>:isUsageOf&#32;a&#32;owl:ObjectProperty&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;is&#32;usage&#32;of&#34;@en,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#34;est&#32;un&#32;usage&#32;de&#34;@fr&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;A&#32;relation&#32;that&#32;refers&#32;to&#32;a&#32;Facility&#32;involved&#32;in&#32;a&#32;Usage.&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:domain&#32;:Usage&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32;:regulation&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:range&#32;:Facility&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-55)|Pointer|<pre lang="Turtle"><code>:isUsageIn&#32;a&#32;owl:ObjectProperty&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;is&#32;usage&#32;in&#34;@en,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#34;est&#32;un&#32;usage&#32;dans&#34;@fr&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;A&#32;relation&#32;that&#32;refers&#32;to&#32;a&#32;Setting&#32;involved&#32;in&#32;a&#32;Usage.&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:domain&#32;:Usage&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32;:regulation&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:range&#32;:Setting&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-55)|Pointer|<pre lang="Turtle"><code>:signifies&#32;a&#32;owl:ObjectProperty&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;signifies&#34;@en,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#34;signifie&#34;@fr&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;A&#32;relation&#32;between&#32;a&#32;signifier&#32;and&#32;the&#32;specification&#32;of&#32;a&#32;be...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:domain&#32;:Signifier&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32;:interaction&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-55)|Pointer|<pre lang="Turtle"><code>:Signifier&#32;a&#32;owl:Class&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;Signifier&#34;@en,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#34;signifier&#34;@en,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#34;Signifiant&#34;@fr,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#34;signifiant&#34;@fr&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;A&#32;perceivable&#32;sign/cue&#32;that&#32;can&#32;be&#32;interpreted&#32;meaningfully&#32;...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32;:core&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:seeAlso&#32; &#60;https://github.com/HyperAgents/ns.hyperagents.org/issues/13#issuecomment-1028904491>,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#60;https://github.com/HyperAgents/ns.hyperagents.org/issues/41> &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:subClassOf&#32;:Hostable&#32;;  &#10; &#32; &#32; &#32; &#32;skos:note&#32; &#34;:Signifier&#32;works&#32;as&#32;a&#32;bridge&#32;between&#32;the&#32;Core&#32;and&#32;the&#32;Intera...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;skos:related&#32;:Affordance,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;:Signifier&#32;.</code></pre>|

***

</details>

***


# Pass Outcomes

[Jump to statistic summary](#statistic-summary)	|	[Previous section](#minorfail-outcomes)	|	Next section

Here is the chapter related to the Pass outcome

:white_check_mark:261 Pass outcomes

<details>
<summary>Fold/Unfold the 261 summary and details</summary>

## Pass Outcomes Summary

:white_check_mark:261 Pass outcomes

|*Jump*|*Number*|*Status*|*Subject*|*Criterion*|*Title*|*Link*|
|------|--------|--------|---------|-----------|-------|------|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-1">1/261</div>|:white_check_mark:Pass|`module-src-regulation-modelet-logistics-create-organization`|[domain-and-range-referencing](https://ns.inria.fr/olivaw#domain-and-range-referencing)|Domains properly defined|[Jump](#pass-outcome-number-1)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-2">2/261</div>|:white_check_mark:Pass|`module-src-regulation-modelet-logistics-create-organization`|[domain-and-range-referencing](https://ns.inria.fr/olivaw#domain-and-range-referencing)|Ranges properly defined|[Jump](#pass-outcome-number-2)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-3">3/261</div>|:white_check_mark:Pass|`module-src-regulation-modelet-logistics-create-organization`|[labeled-terms](https://ns.inria.fr/olivaw#labeled-terms)|All terms labeled|[Jump](#pass-outcome-number-3)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-4">4/261</div>|:white_check_mark:Pass|`module-src-regulation-modelet-logistics-create-organization`|[owl-rl-constraint](https://ns.inria.fr/olivaw#owl-rl-constraint)|OWL RL consistent|[Jump](#pass-outcome-number-4)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-5">5/261</div>|:white_check_mark:Pass|`module-src-regulation-modelet-logistics-create-organization`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL EL Profile compatible|[Jump](#pass-outcome-number-5)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-6">6/261</div>|:white_check_mark:Pass|`module-src-regulation-modelet-logistics-create-organization`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL QL Profile compatible|[Jump](#pass-outcome-number-6)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-7">7/261</div>|:white_check_mark:Pass|`module-src-regulation-modelet-logistics-create-organization`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL RL Profile compatible|[Jump](#pass-outcome-number-7)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-8">8/261</div>|:white_check_mark:Pass|`module-src-regulation-modelet-logistics-create-organization`|[proper-extension-predicate](https://ns.inria.fr/olivaw#proper-extension-predicate)|No class subproperty|[Jump](#pass-outcome-number-8)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-9">9/261</div>|:white_check_mark:Pass|`module-src-regulation-modelet-logistics-create-organization`|[proper-extension-predicate](https://ns.inria.fr/olivaw#proper-extension-predicate)|No property subclass|[Jump](#pass-outcome-number-9)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-10">10/261</div>|:white_check_mark:Pass|`module-src-regulation-modelet-logistics-create-organization`|[proper-extension-predicate](https://ns.inria.fr/olivaw#proper-extension-predicate)|No subclass of property|[Jump](#pass-outcome-number-10)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-11">11/261</div>|:white_check_mark:Pass|`module-src-regulation-modelet-logistics-create-organization`|[proper-extension-predicate](https://ns.inria.fr/olivaw#proper-extension-predicate)|No subproperty of class|[Jump](#pass-outcome-number-11)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-12">12/261</div>|:white_check_mark:Pass|`module-src-regulation-modelet-logistics-create-organization`|[term-referencing](https://ns.inria.fr/olivaw#term-referencing)|Any term is referenced|[Jump](#pass-outcome-number-12)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-13">13/261</div>|:white_check_mark:Pass|`module-src-regulation-modelet-logistics-coordinate-activities`|[domain-and-range-referencing](https://ns.inria.fr/olivaw#domain-and-range-referencing)|Domains properly defined|[Jump](#pass-outcome-number-13)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-14">14/261</div>|:white_check_mark:Pass|`module-src-regulation-modelet-logistics-coordinate-activities`|[domain-and-range-referencing](https://ns.inria.fr/olivaw#domain-and-range-referencing)|Ranges properly defined|[Jump](#pass-outcome-number-14)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-15">15/261</div>|:white_check_mark:Pass|`module-src-regulation-modelet-logistics-coordinate-activities`|[labeled-terms](https://ns.inria.fr/olivaw#labeled-terms)|All terms labeled|[Jump](#pass-outcome-number-15)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-16">16/261</div>|:white_check_mark:Pass|`module-src-regulation-modelet-logistics-coordinate-activities`|[owl-rl-constraint](https://ns.inria.fr/olivaw#owl-rl-constraint)|OWL RL consistent|[Jump](#pass-outcome-number-16)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-17">17/261</div>|:white_check_mark:Pass|`module-src-regulation-modelet-logistics-coordinate-activities`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL EL Profile compatible|[Jump](#pass-outcome-number-17)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-18">18/261</div>|:white_check_mark:Pass|`module-src-regulation-modelet-logistics-coordinate-activities`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL QL Profile compatible|[Jump](#pass-outcome-number-18)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-19">19/261</div>|:white_check_mark:Pass|`module-src-regulation-modelet-logistics-coordinate-activities`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL RL Profile compatible|[Jump](#pass-outcome-number-19)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-20">20/261</div>|:white_check_mark:Pass|`module-src-regulation-modelet-logistics-coordinate-activities`|[proper-extension-predicate](https://ns.inria.fr/olivaw#proper-extension-predicate)|No class subproperty|[Jump](#pass-outcome-number-20)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-21">21/261</div>|:white_check_mark:Pass|`module-src-regulation-modelet-logistics-coordinate-activities`|[proper-extension-predicate](https://ns.inria.fr/olivaw#proper-extension-predicate)|No property subclass|[Jump](#pass-outcome-number-21)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-22">22/261</div>|:white_check_mark:Pass|`module-src-regulation-modelet-logistics-coordinate-activities`|[proper-extension-predicate](https://ns.inria.fr/olivaw#proper-extension-predicate)|No subclass of property|[Jump](#pass-outcome-number-22)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-23">23/261</div>|:white_check_mark:Pass|`module-src-regulation-modelet-logistics-coordinate-activities`|[proper-extension-predicate](https://ns.inria.fr/olivaw#proper-extension-predicate)|No subproperty of class|[Jump](#pass-outcome-number-23)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-24">24/261</div>|:white_check_mark:Pass|`module-src-regulation-modelet-logistics-coordinate-activities`|[term-referencing](https://ns.inria.fr/olivaw#term-referencing)|Any term is referenced|[Jump](#pass-outcome-number-24)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-25">25/261</div>|:white_check_mark:Pass|`module-src-regulation-modelet-logistics-configure-organization`|[domain-and-range-referencing](https://ns.inria.fr/olivaw#domain-and-range-referencing)|Domains properly defined|[Jump](#pass-outcome-number-25)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-26">26/261</div>|:white_check_mark:Pass|`module-src-regulation-modelet-logistics-configure-organization`|[domain-and-range-referencing](https://ns.inria.fr/olivaw#domain-and-range-referencing)|Ranges properly defined|[Jump](#pass-outcome-number-26)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-27">27/261</div>|:white_check_mark:Pass|`module-src-regulation-modelet-logistics-configure-organization`|[labeled-terms](https://ns.inria.fr/olivaw#labeled-terms)|All terms labeled|[Jump](#pass-outcome-number-27)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-28">28/261</div>|:white_check_mark:Pass|`module-src-regulation-modelet-logistics-configure-organization`|[owl-rl-constraint](https://ns.inria.fr/olivaw#owl-rl-constraint)|OWL RL consistent|[Jump](#pass-outcome-number-28)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-29">29/261</div>|:white_check_mark:Pass|`module-src-regulation-modelet-logistics-configure-organization`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL EL Profile compatible|[Jump](#pass-outcome-number-29)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-30">30/261</div>|:white_check_mark:Pass|`module-src-regulation-modelet-logistics-configure-organization`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL QL Profile compatible|[Jump](#pass-outcome-number-30)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-31">31/261</div>|:white_check_mark:Pass|`module-src-regulation-modelet-logistics-configure-organization`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL RL Profile compatible|[Jump](#pass-outcome-number-31)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-32">32/261</div>|:white_check_mark:Pass|`module-src-regulation-modelet-logistics-configure-organization`|[proper-extension-predicate](https://ns.inria.fr/olivaw#proper-extension-predicate)|No class subproperty|[Jump](#pass-outcome-number-32)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-33">33/261</div>|:white_check_mark:Pass|`module-src-regulation-modelet-logistics-configure-organization`|[proper-extension-predicate](https://ns.inria.fr/olivaw#proper-extension-predicate)|No property subclass|[Jump](#pass-outcome-number-33)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-34">34/261</div>|:white_check_mark:Pass|`module-src-regulation-modelet-logistics-configure-organization`|[proper-extension-predicate](https://ns.inria.fr/olivaw#proper-extension-predicate)|No subclass of property|[Jump](#pass-outcome-number-34)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-35">35/261</div>|:white_check_mark:Pass|`module-src-regulation-modelet-logistics-configure-organization`|[proper-extension-predicate](https://ns.inria.fr/olivaw#proper-extension-predicate)|No subproperty of class|[Jump](#pass-outcome-number-35)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-36">36/261</div>|:white_check_mark:Pass|`module-src-regulation-modelet-logistics-configure-organization`|[term-referencing](https://ns.inria.fr/olivaw#term-referencing)|Any term is referenced|[Jump](#pass-outcome-number-36)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-37">37/261</div>|:white_check_mark:Pass|`module-src-regulation`|[domain-and-range-referencing](https://ns.inria.fr/olivaw#domain-and-range-referencing)|Domains properly defined|[Jump](#pass-outcome-number-37)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-38">38/261</div>|:white_check_mark:Pass|`module-src-regulation`|[domain-and-range-referencing](https://ns.inria.fr/olivaw#domain-and-range-referencing)|Ranges properly defined|[Jump](#pass-outcome-number-38)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-39">39/261</div>|:white_check_mark:Pass|`module-src-regulation`|[labeled-terms](https://ns.inria.fr/olivaw#labeled-terms)|All terms labeled|[Jump](#pass-outcome-number-39)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-40">40/261</div>|:white_check_mark:Pass|`module-src-regulation`|[owl-rl-constraint](https://ns.inria.fr/olivaw#owl-rl-constraint)|OWL RL consistent|[Jump](#pass-outcome-number-40)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-41">41/261</div>|:white_check_mark:Pass|`module-src-regulation`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL EL Profile compatible|[Jump](#pass-outcome-number-41)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-42">42/261</div>|:white_check_mark:Pass|`module-src-regulation`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL QL Profile compatible|[Jump](#pass-outcome-number-42)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-43">43/261</div>|:white_check_mark:Pass|`module-src-regulation`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL RL Profile compatible|[Jump](#pass-outcome-number-43)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-44">44/261</div>|:white_check_mark:Pass|`module-src-regulation`|[proper-extension-predicate](https://ns.inria.fr/olivaw#proper-extension-predicate)|No class subproperty|[Jump](#pass-outcome-number-44)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-45">45/261</div>|:white_check_mark:Pass|`module-src-regulation`|[proper-extension-predicate](https://ns.inria.fr/olivaw#proper-extension-predicate)|No property subclass|[Jump](#pass-outcome-number-45)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-46">46/261</div>|:white_check_mark:Pass|`module-src-regulation`|[proper-extension-predicate](https://ns.inria.fr/olivaw#proper-extension-predicate)|No subclass of property|[Jump](#pass-outcome-number-46)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-47">47/261</div>|:white_check_mark:Pass|`module-src-regulation`|[proper-extension-predicate](https://ns.inria.fr/olivaw#proper-extension-predicate)|No subproperty of class|[Jump](#pass-outcome-number-47)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-48">48/261</div>|:white_check_mark:Pass|`module-src-regulation`|[term-referencing](https://ns.inria.fr/olivaw#term-referencing)|Any term is referenced|[Jump](#pass-outcome-number-48)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-49">49/261</div>|:white_check_mark:Pass|`module-src-interaction-modelet-manufacturing-environments-discover-behavior-specifications`|[domain-and-range-referencing](https://ns.inria.fr/olivaw#domain-and-range-referencing)|Domains properly defined|[Jump](#pass-outcome-number-49)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-50">50/261</div>|:white_check_mark:Pass|`module-src-interaction-modelet-manufacturing-environments-discover-behavior-specifications`|[domain-and-range-referencing](https://ns.inria.fr/olivaw#domain-and-range-referencing)|Ranges properly defined|[Jump](#pass-outcome-number-50)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-51">51/261</div>|:white_check_mark:Pass|`module-src-interaction-modelet-manufacturing-environments-discover-behavior-specifications`|[labeled-terms](https://ns.inria.fr/olivaw#labeled-terms)|All terms labeled|[Jump](#pass-outcome-number-51)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-52">52/261</div>|:white_check_mark:Pass|`module-src-interaction-modelet-manufacturing-environments-discover-behavior-specifications`|[owl-rl-constraint](https://ns.inria.fr/olivaw#owl-rl-constraint)|OWL RL consistent|[Jump](#pass-outcome-number-52)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-53">53/261</div>|:white_check_mark:Pass|`module-src-interaction-modelet-manufacturing-environments-discover-behavior-specifications`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL EL Profile compatible|[Jump](#pass-outcome-number-53)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-54">54/261</div>|:white_check_mark:Pass|`module-src-interaction-modelet-manufacturing-environments-discover-behavior-specifications`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL QL Profile compatible|[Jump](#pass-outcome-number-54)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-55">55/261</div>|:white_check_mark:Pass|`module-src-interaction-modelet-manufacturing-environments-discover-behavior-specifications`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL RL Profile compatible|[Jump](#pass-outcome-number-55)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-56">56/261</div>|:white_check_mark:Pass|`module-src-interaction-modelet-manufacturing-environments-discover-behavior-specifications`|[proper-extension-predicate](https://ns.inria.fr/olivaw#proper-extension-predicate)|No class subproperty|[Jump](#pass-outcome-number-56)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-57">57/261</div>|:white_check_mark:Pass|`module-src-interaction-modelet-manufacturing-environments-discover-behavior-specifications`|[proper-extension-predicate](https://ns.inria.fr/olivaw#proper-extension-predicate)|No property subclass|[Jump](#pass-outcome-number-57)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-58">58/261</div>|:white_check_mark:Pass|`module-src-interaction-modelet-manufacturing-environments-discover-behavior-specifications`|[proper-extension-predicate](https://ns.inria.fr/olivaw#proper-extension-predicate)|No subclass of property|[Jump](#pass-outcome-number-58)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-59">59/261</div>|:white_check_mark:Pass|`module-src-interaction-modelet-manufacturing-environments-discover-behavior-specifications`|[proper-extension-predicate](https://ns.inria.fr/olivaw#proper-extension-predicate)|No subproperty of class|[Jump](#pass-outcome-number-59)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-60">60/261</div>|:white_check_mark:Pass|`module-src-interaction-modelet-manufacturing-environments-discover-behavior-specifications`|[term-referencing](https://ns.inria.fr/olivaw#term-referencing)|Any term is referenced|[Jump](#pass-outcome-number-60)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-61">61/261</div>|:white_check_mark:Pass|`module-src-interaction-modelet-manufacturing-environments-discover-behavior-specifications`|[terms-differenciation](https://ns.inria.fr/olivaw#terms-differenciation)|Terms differenciated enough|[Jump](#pass-outcome-number-61)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-62">62/261</div>|:white_check_mark:Pass|`module-src-interaction`|[domain-and-range-referencing](https://ns.inria.fr/olivaw#domain-and-range-referencing)|Domains properly defined|[Jump](#pass-outcome-number-62)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-63">63/261</div>|:white_check_mark:Pass|`module-src-interaction`|[domain-and-range-referencing](https://ns.inria.fr/olivaw#domain-and-range-referencing)|Ranges properly defined|[Jump](#pass-outcome-number-63)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-64">64/261</div>|:white_check_mark:Pass|`module-src-interaction`|[labeled-terms](https://ns.inria.fr/olivaw#labeled-terms)|All terms labeled|[Jump](#pass-outcome-number-64)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-65">65/261</div>|:white_check_mark:Pass|`module-src-interaction`|[owl-rl-constraint](https://ns.inria.fr/olivaw#owl-rl-constraint)|OWL RL consistent|[Jump](#pass-outcome-number-65)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-66">66/261</div>|:white_check_mark:Pass|`module-src-interaction`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL EL Profile compatible|[Jump](#pass-outcome-number-66)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-67">67/261</div>|:white_check_mark:Pass|`module-src-interaction`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL QL Profile compatible|[Jump](#pass-outcome-number-67)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-68">68/261</div>|:white_check_mark:Pass|`module-src-interaction`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL RL Profile compatible|[Jump](#pass-outcome-number-68)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-69">69/261</div>|:white_check_mark:Pass|`module-src-interaction`|[proper-extension-predicate](https://ns.inria.fr/olivaw#proper-extension-predicate)|No class subproperty|[Jump](#pass-outcome-number-69)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-70">70/261</div>|:white_check_mark:Pass|`module-src-interaction`|[proper-extension-predicate](https://ns.inria.fr/olivaw#proper-extension-predicate)|No property subclass|[Jump](#pass-outcome-number-70)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-71">71/261</div>|:white_check_mark:Pass|`module-src-interaction`|[proper-extension-predicate](https://ns.inria.fr/olivaw#proper-extension-predicate)|No subclass of property|[Jump](#pass-outcome-number-71)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-72">72/261</div>|:white_check_mark:Pass|`module-src-interaction`|[proper-extension-predicate](https://ns.inria.fr/olivaw#proper-extension-predicate)|No subproperty of class|[Jump](#pass-outcome-number-72)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-73">73/261</div>|:white_check_mark:Pass|`module-src-interaction`|[term-referencing](https://ns.inria.fr/olivaw#term-referencing)|Any term is referenced|[Jump](#pass-outcome-number-73)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-74">74/261</div>|:white_check_mark:Pass|`module-src-interaction`|[terms-differenciation](https://ns.inria.fr/olivaw#terms-differenciation)|Terms differenciated enough|[Jump](#pass-outcome-number-74)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-75">75/261</div>|:white_check_mark:Pass|`module-src-fipa`|[domain-and-range-referencing](https://ns.inria.fr/olivaw#domain-and-range-referencing)|Domains properly defined|[Jump](#pass-outcome-number-75)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-76">76/261</div>|:white_check_mark:Pass|`module-src-fipa`|[domain-and-range-referencing](https://ns.inria.fr/olivaw#domain-and-range-referencing)|Ranges properly defined|[Jump](#pass-outcome-number-76)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-77">77/261</div>|:white_check_mark:Pass|`module-src-fipa`|[labeled-terms](https://ns.inria.fr/olivaw#labeled-terms)|All terms labeled|[Jump](#pass-outcome-number-77)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-78">78/261</div>|:white_check_mark:Pass|`module-src-fipa`|[owl-rl-constraint](https://ns.inria.fr/olivaw#owl-rl-constraint)|OWL RL consistent|[Jump](#pass-outcome-number-78)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-79">79/261</div>|:white_check_mark:Pass|`module-src-fipa`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL EL Profile compatible|[Jump](#pass-outcome-number-79)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-80">80/261</div>|:white_check_mark:Pass|`module-src-fipa`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL QL Profile compatible|[Jump](#pass-outcome-number-80)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-81">81/261</div>|:white_check_mark:Pass|`module-src-fipa`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL RL Profile compatible|[Jump](#pass-outcome-number-81)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-82">82/261</div>|:white_check_mark:Pass|`module-src-fipa`|[proper-extension-predicate](https://ns.inria.fr/olivaw#proper-extension-predicate)|No class subproperty|[Jump](#pass-outcome-number-82)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-83">83/261</div>|:white_check_mark:Pass|`module-src-fipa`|[proper-extension-predicate](https://ns.inria.fr/olivaw#proper-extension-predicate)|No property subclass|[Jump](#pass-outcome-number-83)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-84">84/261</div>|:white_check_mark:Pass|`module-src-fipa`|[proper-extension-predicate](https://ns.inria.fr/olivaw#proper-extension-predicate)|No subclass of property|[Jump](#pass-outcome-number-84)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-85">85/261</div>|:white_check_mark:Pass|`module-src-fipa`|[proper-extension-predicate](https://ns.inria.fr/olivaw#proper-extension-predicate)|No subproperty of class|[Jump](#pass-outcome-number-85)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-86">86/261</div>|:white_check_mark:Pass|`module-src-fipa`|[terms-differenciation](https://ns.inria.fr/olivaw#terms-differenciation)|Terms differenciated enough|[Jump](#pass-outcome-number-86)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-87">87/261</div>|:white_check_mark:Pass|`module-src-core-modelet-manufacturing-environments-discover-signifiers`|[domain-and-range-referencing](https://ns.inria.fr/olivaw#domain-and-range-referencing)|Domains properly defined|[Jump](#pass-outcome-number-87)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-88">88/261</div>|:white_check_mark:Pass|`module-src-core-modelet-manufacturing-environments-discover-signifiers`|[domain-and-range-referencing](https://ns.inria.fr/olivaw#domain-and-range-referencing)|Ranges properly defined|[Jump](#pass-outcome-number-88)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-89">89/261</div>|:white_check_mark:Pass|`module-src-core-modelet-manufacturing-environments-discover-signifiers`|[owl-rl-constraint](https://ns.inria.fr/olivaw#owl-rl-constraint)|OWL RL consistent|[Jump](#pass-outcome-number-89)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-90">90/261</div>|:white_check_mark:Pass|`module-src-core-modelet-manufacturing-environments-discover-signifiers`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL RL Profile compatible|[Jump](#pass-outcome-number-90)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-91">91/261</div>|:white_check_mark:Pass|`module-src-core-modelet-manufacturing-environments-discover-signifiers`|[proper-extension-predicate](https://ns.inria.fr/olivaw#proper-extension-predicate)|No class subproperty|[Jump](#pass-outcome-number-91)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-92">92/261</div>|:white_check_mark:Pass|`module-src-core-modelet-manufacturing-environments-discover-signifiers`|[proper-extension-predicate](https://ns.inria.fr/olivaw#proper-extension-predicate)|No property subclass|[Jump](#pass-outcome-number-92)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-93">93/261</div>|:white_check_mark:Pass|`module-src-core-modelet-manufacturing-environments-discover-signifiers`|[proper-extension-predicate](https://ns.inria.fr/olivaw#proper-extension-predicate)|No subclass of property|[Jump](#pass-outcome-number-93)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-94">94/261</div>|:white_check_mark:Pass|`module-src-core-modelet-manufacturing-environments-discover-signifiers`|[proper-extension-predicate](https://ns.inria.fr/olivaw#proper-extension-predicate)|No subproperty of class|[Jump](#pass-outcome-number-94)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-95">95/261</div>|:white_check_mark:Pass|`module-src-core-modelet-manufacturing-environments-discover-signifiers`|[term-referencing](https://ns.inria.fr/olivaw#term-referencing)|Any term is referenced|[Jump](#pass-outcome-number-95)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-96">96/261</div>|:white_check_mark:Pass|`module-src-core-modelet-manufacturing-environments-discover-signifiers`|[terms-differenciation](https://ns.inria.fr/olivaw#terms-differenciation)|Terms differenciated enough|[Jump](#pass-outcome-number-96)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-97">97/261</div>|:white_check_mark:Pass|`module-src-core-modelet-manufacturing-environments-discover-platforms`|[domain-and-range-referencing](https://ns.inria.fr/olivaw#domain-and-range-referencing)|Domains properly defined|[Jump](#pass-outcome-number-97)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-98">98/261</div>|:white_check_mark:Pass|`module-src-core-modelet-manufacturing-environments-discover-platforms`|[domain-and-range-referencing](https://ns.inria.fr/olivaw#domain-and-range-referencing)|Ranges properly defined|[Jump](#pass-outcome-number-98)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-99">99/261</div>|:white_check_mark:Pass|`module-src-core-modelet-manufacturing-environments-discover-platforms`|[owl-rl-constraint](https://ns.inria.fr/olivaw#owl-rl-constraint)|OWL RL consistent|[Jump](#pass-outcome-number-99)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-100">100/261</div>|:white_check_mark:Pass|`module-src-core-modelet-manufacturing-environments-discover-platforms`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL RL Profile compatible|[Jump](#pass-outcome-number-100)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-101">101/261</div>|:white_check_mark:Pass|`module-src-core-modelet-manufacturing-environments-discover-platforms`|[proper-extension-predicate](https://ns.inria.fr/olivaw#proper-extension-predicate)|No class subproperty|[Jump](#pass-outcome-number-101)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-102">102/261</div>|:white_check_mark:Pass|`module-src-core-modelet-manufacturing-environments-discover-platforms`|[proper-extension-predicate](https://ns.inria.fr/olivaw#proper-extension-predicate)|No property subclass|[Jump](#pass-outcome-number-102)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-103">103/261</div>|:white_check_mark:Pass|`module-src-core-modelet-manufacturing-environments-discover-platforms`|[proper-extension-predicate](https://ns.inria.fr/olivaw#proper-extension-predicate)|No subclass of property|[Jump](#pass-outcome-number-103)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-104">104/261</div>|:white_check_mark:Pass|`module-src-core-modelet-manufacturing-environments-discover-platforms`|[proper-extension-predicate](https://ns.inria.fr/olivaw#proper-extension-predicate)|No subproperty of class|[Jump](#pass-outcome-number-104)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-105">105/261</div>|:white_check_mark:Pass|`module-src-core-modelet-manufacturing-environments-discover-platforms`|[term-referencing](https://ns.inria.fr/olivaw#term-referencing)|Any term is referenced|[Jump](#pass-outcome-number-105)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-106">106/261</div>|:white_check_mark:Pass|`module-src-core-modelet-manufacturing-environments-discover-platforms`|[terms-differenciation](https://ns.inria.fr/olivaw#terms-differenciation)|Terms differenciated enough|[Jump](#pass-outcome-number-106)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-107">107/261</div>|:white_check_mark:Pass|`module-src-core-modelet-manufacturing-environments-discover-organization`|[domain-and-range-referencing](https://ns.inria.fr/olivaw#domain-and-range-referencing)|Domains properly defined|[Jump](#pass-outcome-number-107)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-108">108/261</div>|:white_check_mark:Pass|`module-src-core-modelet-manufacturing-environments-discover-organization`|[domain-and-range-referencing](https://ns.inria.fr/olivaw#domain-and-range-referencing)|Ranges properly defined|[Jump](#pass-outcome-number-108)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-109">109/261</div>|:white_check_mark:Pass|`module-src-core-modelet-manufacturing-environments-discover-organization`|[owl-rl-constraint](https://ns.inria.fr/olivaw#owl-rl-constraint)|OWL RL consistent|[Jump](#pass-outcome-number-109)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-110">110/261</div>|:white_check_mark:Pass|`module-src-core-modelet-manufacturing-environments-discover-organization`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL RL Profile compatible|[Jump](#pass-outcome-number-110)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-111">111/261</div>|:white_check_mark:Pass|`module-src-core-modelet-manufacturing-environments-discover-organization`|[proper-extension-predicate](https://ns.inria.fr/olivaw#proper-extension-predicate)|No class subproperty|[Jump](#pass-outcome-number-111)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-112">112/261</div>|:white_check_mark:Pass|`module-src-core-modelet-manufacturing-environments-discover-organization`|[proper-extension-predicate](https://ns.inria.fr/olivaw#proper-extension-predicate)|No property subclass|[Jump](#pass-outcome-number-112)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-113">113/261</div>|:white_check_mark:Pass|`module-src-core-modelet-manufacturing-environments-discover-organization`|[proper-extension-predicate](https://ns.inria.fr/olivaw#proper-extension-predicate)|No subclass of property|[Jump](#pass-outcome-number-113)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-114">114/261</div>|:white_check_mark:Pass|`module-src-core-modelet-manufacturing-environments-discover-organization`|[proper-extension-predicate](https://ns.inria.fr/olivaw#proper-extension-predicate)|No subproperty of class|[Jump](#pass-outcome-number-114)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-115">115/261</div>|:white_check_mark:Pass|`module-src-core-modelet-manufacturing-environments-discover-organization`|[term-referencing](https://ns.inria.fr/olivaw#term-referencing)|Any term is referenced|[Jump](#pass-outcome-number-115)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-116">116/261</div>|:white_check_mark:Pass|`module-src-core-modelet-manufacturing-environments-discover-organization`|[terms-differenciation](https://ns.inria.fr/olivaw#terms-differenciation)|Terms differenciated enough|[Jump](#pass-outcome-number-116)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-117">117/261</div>|:white_check_mark:Pass|`module-src-core-modelet-manufacturing-environments-discover-core`|[domain-and-range-referencing](https://ns.inria.fr/olivaw#domain-and-range-referencing)|Domains properly defined|[Jump](#pass-outcome-number-117)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-118">118/261</div>|:white_check_mark:Pass|`module-src-core-modelet-manufacturing-environments-discover-core`|[domain-and-range-referencing](https://ns.inria.fr/olivaw#domain-and-range-referencing)|Ranges properly defined|[Jump](#pass-outcome-number-118)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-119">119/261</div>|:white_check_mark:Pass|`module-src-core-modelet-manufacturing-environments-discover-core`|[owl-rl-constraint](https://ns.inria.fr/olivaw#owl-rl-constraint)|OWL RL consistent|[Jump](#pass-outcome-number-119)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-120">120/261</div>|:white_check_mark:Pass|`module-src-core-modelet-manufacturing-environments-discover-core`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL RL Profile compatible|[Jump](#pass-outcome-number-120)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-121">121/261</div>|:white_check_mark:Pass|`module-src-core-modelet-manufacturing-environments-discover-core`|[proper-extension-predicate](https://ns.inria.fr/olivaw#proper-extension-predicate)|No class subproperty|[Jump](#pass-outcome-number-121)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-122">122/261</div>|:white_check_mark:Pass|`module-src-core-modelet-manufacturing-environments-discover-core`|[proper-extension-predicate](https://ns.inria.fr/olivaw#proper-extension-predicate)|No property subclass|[Jump](#pass-outcome-number-122)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-123">123/261</div>|:white_check_mark:Pass|`module-src-core-modelet-manufacturing-environments-discover-core`|[proper-extension-predicate](https://ns.inria.fr/olivaw#proper-extension-predicate)|No subclass of property|[Jump](#pass-outcome-number-123)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-124">124/261</div>|:white_check_mark:Pass|`module-src-core-modelet-manufacturing-environments-discover-core`|[proper-extension-predicate](https://ns.inria.fr/olivaw#proper-extension-predicate)|No subproperty of class|[Jump](#pass-outcome-number-124)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-125">125/261</div>|:white_check_mark:Pass|`module-src-core-modelet-manufacturing-environments-discover-core`|[term-referencing](https://ns.inria.fr/olivaw#term-referencing)|Any term is referenced|[Jump](#pass-outcome-number-125)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-126">126/261</div>|:white_check_mark:Pass|`module-src-core-modelet-manufacturing-environments-discover-core`|[terms-differenciation](https://ns.inria.fr/olivaw#terms-differenciation)|Terms differenciated enough|[Jump](#pass-outcome-number-126)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-127">127/261</div>|:white_check_mark:Pass|`module-src-core`|[domain-and-range-referencing](https://ns.inria.fr/olivaw#domain-and-range-referencing)|Domains properly defined|[Jump](#pass-outcome-number-127)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-128">128/261</div>|:white_check_mark:Pass|`module-src-core`|[domain-and-range-referencing](https://ns.inria.fr/olivaw#domain-and-range-referencing)|Ranges properly defined|[Jump](#pass-outcome-number-128)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-129">129/261</div>|:white_check_mark:Pass|`module-src-core`|[owl-rl-constraint](https://ns.inria.fr/olivaw#owl-rl-constraint)|OWL RL consistent|[Jump](#pass-outcome-number-129)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-130">130/261</div>|:white_check_mark:Pass|`module-src-core`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL RL Profile compatible|[Jump](#pass-outcome-number-130)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-131">131/261</div>|:white_check_mark:Pass|`module-src-core`|[proper-extension-predicate](https://ns.inria.fr/olivaw#proper-extension-predicate)|No class subproperty|[Jump](#pass-outcome-number-131)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-132">132/261</div>|:white_check_mark:Pass|`module-src-core`|[proper-extension-predicate](https://ns.inria.fr/olivaw#proper-extension-predicate)|No property subclass|[Jump](#pass-outcome-number-132)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-133">133/261</div>|:white_check_mark:Pass|`module-src-core`|[proper-extension-predicate](https://ns.inria.fr/olivaw#proper-extension-predicate)|No subclass of property|[Jump](#pass-outcome-number-133)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-134">134/261</div>|:white_check_mark:Pass|`module-src-core`|[proper-extension-predicate](https://ns.inria.fr/olivaw#proper-extension-predicate)|No subproperty of class|[Jump](#pass-outcome-number-134)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-135">135/261</div>|:white_check_mark:Pass|`module-src-core`|[term-referencing](https://ns.inria.fr/olivaw#term-referencing)|Any term is referenced|[Jump](#pass-outcome-number-135)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-136">136/261</div>|:white_check_mark:Pass|`module-src-core`|[terms-differenciation](https://ns.inria.fr/olivaw#terms-differenciation)|Terms differenciated enough|[Jump](#pass-outcome-number-136)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-137">137/261</div>|:white_check_mark:Pass|`module-src-alignment-interaction-td`|[domain-and-range-referencing](https://ns.inria.fr/olivaw#domain-and-range-referencing)|Domains properly defined|[Jump](#pass-outcome-number-137)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-138">138/261</div>|:white_check_mark:Pass|`module-src-alignment-interaction-td`|[domain-and-range-referencing](https://ns.inria.fr/olivaw#domain-and-range-referencing)|Ranges properly defined|[Jump](#pass-outcome-number-138)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-139">139/261</div>|:white_check_mark:Pass|`module-src-alignment-interaction-td`|[labeled-terms](https://ns.inria.fr/olivaw#labeled-terms)|All terms labeled|[Jump](#pass-outcome-number-139)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-140">140/261</div>|:white_check_mark:Pass|`module-src-alignment-interaction-td`|[owl-rl-constraint](https://ns.inria.fr/olivaw#owl-rl-constraint)|OWL RL consistent|[Jump](#pass-outcome-number-140)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-141">141/261</div>|:white_check_mark:Pass|`module-src-alignment-interaction-td`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL EL Profile compatible|[Jump](#pass-outcome-number-141)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-142">142/261</div>|:white_check_mark:Pass|`module-src-alignment-interaction-td`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL RL Profile compatible|[Jump](#pass-outcome-number-142)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-143">143/261</div>|:white_check_mark:Pass|`module-src-alignment-interaction-td`|[proper-extension-predicate](https://ns.inria.fr/olivaw#proper-extension-predicate)|No class subproperty|[Jump](#pass-outcome-number-143)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-144">144/261</div>|:white_check_mark:Pass|`module-src-alignment-interaction-td`|[proper-extension-predicate](https://ns.inria.fr/olivaw#proper-extension-predicate)|No property subclass|[Jump](#pass-outcome-number-144)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-145">145/261</div>|:white_check_mark:Pass|`module-src-alignment-interaction-td`|[proper-extension-predicate](https://ns.inria.fr/olivaw#proper-extension-predicate)|No subclass of property|[Jump](#pass-outcome-number-145)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-146">146/261</div>|:white_check_mark:Pass|`module-src-alignment-interaction-td`|[proper-extension-predicate](https://ns.inria.fr/olivaw#proper-extension-predicate)|No subproperty of class|[Jump](#pass-outcome-number-146)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-147">147/261</div>|:white_check_mark:Pass|`module-src-alignment-interaction-td`|[term-referencing](https://ns.inria.fr/olivaw#term-referencing)|Any term is referenced|[Jump](#pass-outcome-number-147)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-148">148/261</div>|:white_check_mark:Pass|`module-src-alignment-interaction-td`|[terms-differenciation](https://ns.inria.fr/olivaw#terms-differenciation)|Terms differenciated enough|[Jump](#pass-outcome-number-148)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-149">149/261</div>|:white_check_mark:Pass|`modelet-manufacturing-environments-discover-signifiers`|[domain-and-range-referencing](https://ns.inria.fr/olivaw#domain-and-range-referencing)|Domains properly defined|[Jump](#pass-outcome-number-149)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-150">150/261</div>|:white_check_mark:Pass|`modelet-manufacturing-environments-discover-signifiers`|[domain-and-range-referencing](https://ns.inria.fr/olivaw#domain-and-range-referencing)|Ranges properly defined|[Jump](#pass-outcome-number-150)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-151">151/261</div>|:white_check_mark:Pass|`modelet-manufacturing-environments-discover-signifiers`|[owl-rl-constraint](https://ns.inria.fr/olivaw#owl-rl-constraint)|OWL RL consistent|[Jump](#pass-outcome-number-151)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-152">152/261</div>|:white_check_mark:Pass|`modelet-manufacturing-environments-discover-signifiers`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL RL Profile compatible|[Jump](#pass-outcome-number-152)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-153">153/261</div>|:white_check_mark:Pass|`modelet-manufacturing-environments-discover-signifiers`|[proper-extension-predicate](https://ns.inria.fr/olivaw#proper-extension-predicate)|No class subproperty|[Jump](#pass-outcome-number-153)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-154">154/261</div>|:white_check_mark:Pass|`modelet-manufacturing-environments-discover-signifiers`|[proper-extension-predicate](https://ns.inria.fr/olivaw#proper-extension-predicate)|No property subclass|[Jump](#pass-outcome-number-154)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-155">155/261</div>|:white_check_mark:Pass|`modelet-manufacturing-environments-discover-signifiers`|[proper-extension-predicate](https://ns.inria.fr/olivaw#proper-extension-predicate)|No subclass of property|[Jump](#pass-outcome-number-155)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-156">156/261</div>|:white_check_mark:Pass|`modelet-manufacturing-environments-discover-signifiers`|[proper-extension-predicate](https://ns.inria.fr/olivaw#proper-extension-predicate)|No subproperty of class|[Jump](#pass-outcome-number-156)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-157">157/261</div>|:white_check_mark:Pass|`modelet-manufacturing-environments-discover-signifiers`|[term-referencing](https://ns.inria.fr/olivaw#term-referencing)|Any term is referenced|[Jump](#pass-outcome-number-157)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-158">158/261</div>|:white_check_mark:Pass|`modelet-manufacturing-environments-discover-signifiers`|[terms-differenciation](https://ns.inria.fr/olivaw#terms-differenciation)|Terms differenciated enough|[Jump](#pass-outcome-number-158)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-159">159/261</div>|:white_check_mark:Pass|`modelet-manufacturing-environments-discover-platforms`|[domain-and-range-referencing](https://ns.inria.fr/olivaw#domain-and-range-referencing)|Domains properly defined|[Jump](#pass-outcome-number-159)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-160">160/261</div>|:white_check_mark:Pass|`modelet-manufacturing-environments-discover-platforms`|[domain-and-range-referencing](https://ns.inria.fr/olivaw#domain-and-range-referencing)|Ranges properly defined|[Jump](#pass-outcome-number-160)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-161">161/261</div>|:white_check_mark:Pass|`modelet-manufacturing-environments-discover-platforms`|[labeled-terms](https://ns.inria.fr/olivaw#labeled-terms)|All terms labeled|[Jump](#pass-outcome-number-161)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-162">162/261</div>|:white_check_mark:Pass|`modelet-manufacturing-environments-discover-platforms`|[owl-rl-constraint](https://ns.inria.fr/olivaw#owl-rl-constraint)|OWL RL consistent|[Jump](#pass-outcome-number-162)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-163">163/261</div>|:white_check_mark:Pass|`modelet-manufacturing-environments-discover-platforms`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL QL Profile compatible|[Jump](#pass-outcome-number-163)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-164">164/261</div>|:white_check_mark:Pass|`modelet-manufacturing-environments-discover-platforms`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL RL Profile compatible|[Jump](#pass-outcome-number-164)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-165">165/261</div>|:white_check_mark:Pass|`modelet-manufacturing-environments-discover-platforms`|[proper-extension-predicate](https://ns.inria.fr/olivaw#proper-extension-predicate)|No class subproperty|[Jump](#pass-outcome-number-165)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-166">166/261</div>|:white_check_mark:Pass|`modelet-manufacturing-environments-discover-platforms`|[proper-extension-predicate](https://ns.inria.fr/olivaw#proper-extension-predicate)|No property subclass|[Jump](#pass-outcome-number-166)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-167">167/261</div>|:white_check_mark:Pass|`modelet-manufacturing-environments-discover-platforms`|[proper-extension-predicate](https://ns.inria.fr/olivaw#proper-extension-predicate)|No subclass of property|[Jump](#pass-outcome-number-167)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-168">168/261</div>|:white_check_mark:Pass|`modelet-manufacturing-environments-discover-platforms`|[proper-extension-predicate](https://ns.inria.fr/olivaw#proper-extension-predicate)|No subproperty of class|[Jump](#pass-outcome-number-168)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-169">169/261</div>|:white_check_mark:Pass|`modelet-manufacturing-environments-discover-platforms`|[term-referencing](https://ns.inria.fr/olivaw#term-referencing)|Any term is referenced|[Jump](#pass-outcome-number-169)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-170">170/261</div>|:white_check_mark:Pass|`modelet-manufacturing-environments-discover-platforms`|[terms-differenciation](https://ns.inria.fr/olivaw#terms-differenciation)|Terms differenciated enough|[Jump](#pass-outcome-number-170)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-171">171/261</div>|:white_check_mark:Pass|`modelet-manufacturing-environments-discover-organization`|[domain-and-range-referencing](https://ns.inria.fr/olivaw#domain-and-range-referencing)|Domains properly defined|[Jump](#pass-outcome-number-171)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-172">172/261</div>|:white_check_mark:Pass|`modelet-manufacturing-environments-discover-organization`|[domain-and-range-referencing](https://ns.inria.fr/olivaw#domain-and-range-referencing)|Ranges properly defined|[Jump](#pass-outcome-number-172)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-173">173/261</div>|:white_check_mark:Pass|`modelet-manufacturing-environments-discover-organization`|[labeled-terms](https://ns.inria.fr/olivaw#labeled-terms)|All terms labeled|[Jump](#pass-outcome-number-173)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-174">174/261</div>|:white_check_mark:Pass|`modelet-manufacturing-environments-discover-organization`|[owl-rl-constraint](https://ns.inria.fr/olivaw#owl-rl-constraint)|OWL RL consistent|[Jump](#pass-outcome-number-174)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-175">175/261</div>|:white_check_mark:Pass|`modelet-manufacturing-environments-discover-organization`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL EL Profile compatible|[Jump](#pass-outcome-number-175)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-176">176/261</div>|:white_check_mark:Pass|`modelet-manufacturing-environments-discover-organization`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL QL Profile compatible|[Jump](#pass-outcome-number-176)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-177">177/261</div>|:white_check_mark:Pass|`modelet-manufacturing-environments-discover-organization`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL RL Profile compatible|[Jump](#pass-outcome-number-177)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-178">178/261</div>|:white_check_mark:Pass|`modelet-manufacturing-environments-discover-organization`|[proper-extension-predicate](https://ns.inria.fr/olivaw#proper-extension-predicate)|No class subproperty|[Jump](#pass-outcome-number-178)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-179">179/261</div>|:white_check_mark:Pass|`modelet-manufacturing-environments-discover-organization`|[proper-extension-predicate](https://ns.inria.fr/olivaw#proper-extension-predicate)|No property subclass|[Jump](#pass-outcome-number-179)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-180">180/261</div>|:white_check_mark:Pass|`modelet-manufacturing-environments-discover-organization`|[proper-extension-predicate](https://ns.inria.fr/olivaw#proper-extension-predicate)|No subclass of property|[Jump](#pass-outcome-number-180)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-181">181/261</div>|:white_check_mark:Pass|`modelet-manufacturing-environments-discover-organization`|[proper-extension-predicate](https://ns.inria.fr/olivaw#proper-extension-predicate)|No subproperty of class|[Jump](#pass-outcome-number-181)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-182">182/261</div>|:white_check_mark:Pass|`modelet-manufacturing-environments-discover-organization`|[term-referencing](https://ns.inria.fr/olivaw#term-referencing)|Any term is referenced|[Jump](#pass-outcome-number-182)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-183">183/261</div>|:white_check_mark:Pass|`modelet-manufacturing-environments-discover-organization`|[terms-differenciation](https://ns.inria.fr/olivaw#terms-differenciation)|Terms differenciated enough|[Jump](#pass-outcome-number-183)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-184">184/261</div>|:white_check_mark:Pass|`modelet-manufacturing-environments-discover-core`|[domain-and-range-referencing](https://ns.inria.fr/olivaw#domain-and-range-referencing)|Domains properly defined|[Jump](#pass-outcome-number-184)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-185">185/261</div>|:white_check_mark:Pass|`modelet-manufacturing-environments-discover-core`|[domain-and-range-referencing](https://ns.inria.fr/olivaw#domain-and-range-referencing)|Ranges properly defined|[Jump](#pass-outcome-number-185)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-186">186/261</div>|:white_check_mark:Pass|`modelet-manufacturing-environments-discover-core`|[labeled-terms](https://ns.inria.fr/olivaw#labeled-terms)|All terms labeled|[Jump](#pass-outcome-number-186)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-187">187/261</div>|:white_check_mark:Pass|`modelet-manufacturing-environments-discover-core`|[owl-rl-constraint](https://ns.inria.fr/olivaw#owl-rl-constraint)|OWL RL consistent|[Jump](#pass-outcome-number-187)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-188">188/261</div>|:white_check_mark:Pass|`modelet-manufacturing-environments-discover-core`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL RL Profile compatible|[Jump](#pass-outcome-number-188)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-189">189/261</div>|:white_check_mark:Pass|`modelet-manufacturing-environments-discover-core`|[proper-extension-predicate](https://ns.inria.fr/olivaw#proper-extension-predicate)|No class subproperty|[Jump](#pass-outcome-number-189)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-190">190/261</div>|:white_check_mark:Pass|`modelet-manufacturing-environments-discover-core`|[proper-extension-predicate](https://ns.inria.fr/olivaw#proper-extension-predicate)|No property subclass|[Jump](#pass-outcome-number-190)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-191">191/261</div>|:white_check_mark:Pass|`modelet-manufacturing-environments-discover-core`|[proper-extension-predicate](https://ns.inria.fr/olivaw#proper-extension-predicate)|No subclass of property|[Jump](#pass-outcome-number-191)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-192">192/261</div>|:white_check_mark:Pass|`modelet-manufacturing-environments-discover-core`|[proper-extension-predicate](https://ns.inria.fr/olivaw#proper-extension-predicate)|No subproperty of class|[Jump](#pass-outcome-number-192)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-193">193/261</div>|:white_check_mark:Pass|`modelet-manufacturing-environments-discover-core`|[term-referencing](https://ns.inria.fr/olivaw#term-referencing)|Any term is referenced|[Jump](#pass-outcome-number-193)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-194">194/261</div>|:white_check_mark:Pass|`modelet-manufacturing-environments-discover-core`|[terms-differenciation](https://ns.inria.fr/olivaw#terms-differenciation)|Terms differenciated enough|[Jump](#pass-outcome-number-194)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-195">195/261</div>|:white_check_mark:Pass|`modelet-manufacturing-environments-discover-behavior-specifications`|[domain-and-range-referencing](https://ns.inria.fr/olivaw#domain-and-range-referencing)|Domains properly defined|[Jump](#pass-outcome-number-195)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-196">196/261</div>|:white_check_mark:Pass|`modelet-manufacturing-environments-discover-behavior-specifications`|[domain-and-range-referencing](https://ns.inria.fr/olivaw#domain-and-range-referencing)|Ranges properly defined|[Jump](#pass-outcome-number-196)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-197">197/261</div>|:white_check_mark:Pass|`modelet-manufacturing-environments-discover-behavior-specifications`|[labeled-terms](https://ns.inria.fr/olivaw#labeled-terms)|All terms labeled|[Jump](#pass-outcome-number-197)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-198">198/261</div>|:white_check_mark:Pass|`modelet-manufacturing-environments-discover-behavior-specifications`|[owl-rl-constraint](https://ns.inria.fr/olivaw#owl-rl-constraint)|OWL RL consistent|[Jump](#pass-outcome-number-198)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-199">199/261</div>|:white_check_mark:Pass|`modelet-manufacturing-environments-discover-behavior-specifications`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL EL Profile compatible|[Jump](#pass-outcome-number-199)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-200">200/261</div>|:white_check_mark:Pass|`modelet-manufacturing-environments-discover-behavior-specifications`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL QL Profile compatible|[Jump](#pass-outcome-number-200)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-201">201/261</div>|:white_check_mark:Pass|`modelet-manufacturing-environments-discover-behavior-specifications`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL RL Profile compatible|[Jump](#pass-outcome-number-201)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-202">202/261</div>|:white_check_mark:Pass|`modelet-manufacturing-environments-discover-behavior-specifications`|[proper-extension-predicate](https://ns.inria.fr/olivaw#proper-extension-predicate)|No class subproperty|[Jump](#pass-outcome-number-202)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-203">203/261</div>|:white_check_mark:Pass|`modelet-manufacturing-environments-discover-behavior-specifications`|[proper-extension-predicate](https://ns.inria.fr/olivaw#proper-extension-predicate)|No property subclass|[Jump](#pass-outcome-number-203)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-204">204/261</div>|:white_check_mark:Pass|`modelet-manufacturing-environments-discover-behavior-specifications`|[proper-extension-predicate](https://ns.inria.fr/olivaw#proper-extension-predicate)|No subclass of property|[Jump](#pass-outcome-number-204)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-205">205/261</div>|:white_check_mark:Pass|`modelet-manufacturing-environments-discover-behavior-specifications`|[proper-extension-predicate](https://ns.inria.fr/olivaw#proper-extension-predicate)|No subproperty of class|[Jump](#pass-outcome-number-205)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-206">206/261</div>|:white_check_mark:Pass|`modelet-manufacturing-environments-discover-behavior-specifications`|[term-referencing](https://ns.inria.fr/olivaw#term-referencing)|Any term is referenced|[Jump](#pass-outcome-number-206)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-207">207/261</div>|:white_check_mark:Pass|`modelet-manufacturing-environments-discover-behavior-specifications`|[terms-differenciation](https://ns.inria.fr/olivaw#terms-differenciation)|Terms differenciated enough|[Jump](#pass-outcome-number-207)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-208">208/261</div>|:white_check_mark:Pass|`modelet-logistics-create-organization`|[domain-and-range-referencing](https://ns.inria.fr/olivaw#domain-and-range-referencing)|Domains properly defined|[Jump](#pass-outcome-number-208)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-209">209/261</div>|:white_check_mark:Pass|`modelet-logistics-create-organization`|[domain-and-range-referencing](https://ns.inria.fr/olivaw#domain-and-range-referencing)|Ranges properly defined|[Jump](#pass-outcome-number-209)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-210">210/261</div>|:white_check_mark:Pass|`modelet-logistics-create-organization`|[labeled-terms](https://ns.inria.fr/olivaw#labeled-terms)|All terms labeled|[Jump](#pass-outcome-number-210)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-211">211/261</div>|:white_check_mark:Pass|`modelet-logistics-create-organization`|[owl-rl-constraint](https://ns.inria.fr/olivaw#owl-rl-constraint)|OWL RL consistent|[Jump](#pass-outcome-number-211)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-212">212/261</div>|:white_check_mark:Pass|`modelet-logistics-create-organization`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL EL Profile compatible|[Jump](#pass-outcome-number-212)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-213">213/261</div>|:white_check_mark:Pass|`modelet-logistics-create-organization`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL QL Profile compatible|[Jump](#pass-outcome-number-213)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-214">214/261</div>|:white_check_mark:Pass|`modelet-logistics-create-organization`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL RL Profile compatible|[Jump](#pass-outcome-number-214)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-215">215/261</div>|:white_check_mark:Pass|`modelet-logistics-create-organization`|[proper-extension-predicate](https://ns.inria.fr/olivaw#proper-extension-predicate)|No class subproperty|[Jump](#pass-outcome-number-215)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-216">216/261</div>|:white_check_mark:Pass|`modelet-logistics-create-organization`|[proper-extension-predicate](https://ns.inria.fr/olivaw#proper-extension-predicate)|No property subclass|[Jump](#pass-outcome-number-216)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-217">217/261</div>|:white_check_mark:Pass|`modelet-logistics-create-organization`|[proper-extension-predicate](https://ns.inria.fr/olivaw#proper-extension-predicate)|No subclass of property|[Jump](#pass-outcome-number-217)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-218">218/261</div>|:white_check_mark:Pass|`modelet-logistics-create-organization`|[proper-extension-predicate](https://ns.inria.fr/olivaw#proper-extension-predicate)|No subproperty of class|[Jump](#pass-outcome-number-218)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-219">219/261</div>|:white_check_mark:Pass|`modelet-logistics-create-organization`|[term-referencing](https://ns.inria.fr/olivaw#term-referencing)|Any term is referenced|[Jump](#pass-outcome-number-219)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-220">220/261</div>|:white_check_mark:Pass|`modelet-logistics-create-organization`|[terms-differenciation](https://ns.inria.fr/olivaw#terms-differenciation)|Terms differenciated enough|[Jump](#pass-outcome-number-220)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-221">221/261</div>|:white_check_mark:Pass|`modelet-logistics-coordinate-activities`|[domain-and-range-referencing](https://ns.inria.fr/olivaw#domain-and-range-referencing)|Domains properly defined|[Jump](#pass-outcome-number-221)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-222">222/261</div>|:white_check_mark:Pass|`modelet-logistics-coordinate-activities`|[domain-and-range-referencing](https://ns.inria.fr/olivaw#domain-and-range-referencing)|Ranges properly defined|[Jump](#pass-outcome-number-222)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-223">223/261</div>|:white_check_mark:Pass|`modelet-logistics-coordinate-activities`|[labeled-terms](https://ns.inria.fr/olivaw#labeled-terms)|All terms labeled|[Jump](#pass-outcome-number-223)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-224">224/261</div>|:white_check_mark:Pass|`modelet-logistics-coordinate-activities`|[owl-rl-constraint](https://ns.inria.fr/olivaw#owl-rl-constraint)|OWL RL consistent|[Jump](#pass-outcome-number-224)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-225">225/261</div>|:white_check_mark:Pass|`modelet-logistics-coordinate-activities`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL EL Profile compatible|[Jump](#pass-outcome-number-225)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-226">226/261</div>|:white_check_mark:Pass|`modelet-logistics-coordinate-activities`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL QL Profile compatible|[Jump](#pass-outcome-number-226)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-227">227/261</div>|:white_check_mark:Pass|`modelet-logistics-coordinate-activities`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL RL Profile compatible|[Jump](#pass-outcome-number-227)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-228">228/261</div>|:white_check_mark:Pass|`modelet-logistics-coordinate-activities`|[proper-extension-predicate](https://ns.inria.fr/olivaw#proper-extension-predicate)|No class subproperty|[Jump](#pass-outcome-number-228)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-229">229/261</div>|:white_check_mark:Pass|`modelet-logistics-coordinate-activities`|[proper-extension-predicate](https://ns.inria.fr/olivaw#proper-extension-predicate)|No property subclass|[Jump](#pass-outcome-number-229)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-230">230/261</div>|:white_check_mark:Pass|`modelet-logistics-coordinate-activities`|[proper-extension-predicate](https://ns.inria.fr/olivaw#proper-extension-predicate)|No subclass of property|[Jump](#pass-outcome-number-230)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-231">231/261</div>|:white_check_mark:Pass|`modelet-logistics-coordinate-activities`|[proper-extension-predicate](https://ns.inria.fr/olivaw#proper-extension-predicate)|No subproperty of class|[Jump](#pass-outcome-number-231)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-232">232/261</div>|:white_check_mark:Pass|`modelet-logistics-coordinate-activities`|[term-referencing](https://ns.inria.fr/olivaw#term-referencing)|Any term is referenced|[Jump](#pass-outcome-number-232)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-233">233/261</div>|:white_check_mark:Pass|`modelet-logistics-coordinate-activities`|[terms-differenciation](https://ns.inria.fr/olivaw#terms-differenciation)|Terms differenciated enough|[Jump](#pass-outcome-number-233)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-234">234/261</div>|:white_check_mark:Pass|`modelet-logistics-configure-organization`|[domain-and-range-referencing](https://ns.inria.fr/olivaw#domain-and-range-referencing)|Domains properly defined|[Jump](#pass-outcome-number-234)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-235">235/261</div>|:white_check_mark:Pass|`modelet-logistics-configure-organization`|[domain-and-range-referencing](https://ns.inria.fr/olivaw#domain-and-range-referencing)|Ranges properly defined|[Jump](#pass-outcome-number-235)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-236">236/261</div>|:white_check_mark:Pass|`modelet-logistics-configure-organization`|[labeled-terms](https://ns.inria.fr/olivaw#labeled-terms)|All terms labeled|[Jump](#pass-outcome-number-236)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-237">237/261</div>|:white_check_mark:Pass|`modelet-logistics-configure-organization`|[owl-rl-constraint](https://ns.inria.fr/olivaw#owl-rl-constraint)|OWL RL consistent|[Jump](#pass-outcome-number-237)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-238">238/261</div>|:white_check_mark:Pass|`modelet-logistics-configure-organization`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL EL Profile compatible|[Jump](#pass-outcome-number-238)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-239">239/261</div>|:white_check_mark:Pass|`modelet-logistics-configure-organization`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL QL Profile compatible|[Jump](#pass-outcome-number-239)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-240">240/261</div>|:white_check_mark:Pass|`modelet-logistics-configure-organization`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL RL Profile compatible|[Jump](#pass-outcome-number-240)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-241">241/261</div>|:white_check_mark:Pass|`modelet-logistics-configure-organization`|[proper-extension-predicate](https://ns.inria.fr/olivaw#proper-extension-predicate)|No class subproperty|[Jump](#pass-outcome-number-241)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-242">242/261</div>|:white_check_mark:Pass|`modelet-logistics-configure-organization`|[proper-extension-predicate](https://ns.inria.fr/olivaw#proper-extension-predicate)|No property subclass|[Jump](#pass-outcome-number-242)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-243">243/261</div>|:white_check_mark:Pass|`modelet-logistics-configure-organization`|[proper-extension-predicate](https://ns.inria.fr/olivaw#proper-extension-predicate)|No subclass of property|[Jump](#pass-outcome-number-243)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-244">244/261</div>|:white_check_mark:Pass|`modelet-logistics-configure-organization`|[proper-extension-predicate](https://ns.inria.fr/olivaw#proper-extension-predicate)|No subproperty of class|[Jump](#pass-outcome-number-244)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-245">245/261</div>|:white_check_mark:Pass|`modelet-logistics-configure-organization`|[term-referencing](https://ns.inria.fr/olivaw#term-referencing)|Any term is referenced|[Jump](#pass-outcome-number-245)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-246">246/261</div>|:white_check_mark:Pass|`all-modules`|[domain-and-range-referencing](https://ns.inria.fr/olivaw#domain-and-range-referencing)|Domains properly defined|[Jump](#pass-outcome-number-246)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-247">247/261</div>|:white_check_mark:Pass|`all-modules`|[domain-and-range-referencing](https://ns.inria.fr/olivaw#domain-and-range-referencing)|Ranges properly defined|[Jump](#pass-outcome-number-247)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-248">248/261</div>|:white_check_mark:Pass|`all-modules`|[owl-rl-constraint](https://ns.inria.fr/olivaw#owl-rl-constraint)|OWL RL consistent|[Jump](#pass-outcome-number-248)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-249">249/261</div>|:white_check_mark:Pass|`all-modules`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL RL Profile compatible|[Jump](#pass-outcome-number-249)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-250">250/261</div>|:white_check_mark:Pass|`all-modules`|[proper-extension-predicate](https://ns.inria.fr/olivaw#proper-extension-predicate)|No class subproperty|[Jump](#pass-outcome-number-250)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-251">251/261</div>|:white_check_mark:Pass|`all-modules`|[proper-extension-predicate](https://ns.inria.fr/olivaw#proper-extension-predicate)|No property subclass|[Jump](#pass-outcome-number-251)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-252">252/261</div>|:white_check_mark:Pass|`all-modules`|[proper-extension-predicate](https://ns.inria.fr/olivaw#proper-extension-predicate)|No subclass of property|[Jump](#pass-outcome-number-252)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-253">253/261</div>|:white_check_mark:Pass|`all-modules`|[proper-extension-predicate](https://ns.inria.fr/olivaw#proper-extension-predicate)|No subproperty of class|[Jump](#pass-outcome-number-253)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-254">254/261</div>|:white_check_mark:Pass|`all-fragments`|[domain-and-range-referencing](https://ns.inria.fr/olivaw#domain-and-range-referencing)|Domains properly defined|[Jump](#pass-outcome-number-254)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-255">255/261</div>|:white_check_mark:Pass|`all-fragments`|[domain-and-range-referencing](https://ns.inria.fr/olivaw#domain-and-range-referencing)|Ranges properly defined|[Jump](#pass-outcome-number-255)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-256">256/261</div>|:white_check_mark:Pass|`all-fragments`|[owl-rl-constraint](https://ns.inria.fr/olivaw#owl-rl-constraint)|OWL RL consistent|[Jump](#pass-outcome-number-256)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-257">257/261</div>|:white_check_mark:Pass|`all-fragments`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL RL Profile compatible|[Jump](#pass-outcome-number-257)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-258">258/261</div>|:white_check_mark:Pass|`all-fragments`|[proper-extension-predicate](https://ns.inria.fr/olivaw#proper-extension-predicate)|No class subproperty|[Jump](#pass-outcome-number-258)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-259">259/261</div>|:white_check_mark:Pass|`all-fragments`|[proper-extension-predicate](https://ns.inria.fr/olivaw#proper-extension-predicate)|No property subclass|[Jump](#pass-outcome-number-259)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-260">260/261</div>|:white_check_mark:Pass|`all-fragments`|[proper-extension-predicate](https://ns.inria.fr/olivaw#proper-extension-predicate)|No subclass of property|[Jump](#pass-outcome-number-260)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-261">261/261</div>|:white_check_mark:Pass|`all-fragments`|[proper-extension-predicate](https://ns.inria.fr/olivaw#proper-extension-predicate)|No subproperty of class|[Jump](#pass-outcome-number-261)|

***

## Pass Outcomes Details

This subchapter gives more details to the :white_check_mark:Pass outcomes

### Pass Outcome number 1

[Jump to summary definition](#summary-Pass-1)	|	Previous Pass outcome	|	[Next Pass outcome](#pass-outcome-number-2)

:white_check_mark:Pass outcome
#### Subject detail
|Name|module-src-regulation-modelet-logistics-create-organization|
|----|----|
|Title|Merged&#32;module&#32;src/regulation.ttl&#32;from&#32;branch&#32;HEAD&#32;with&#32;related&#32;terms&#32;from&#32;the&#32;fragments&#32;domains/logistics/create-organization/onto.ttl|
|Composition|- [Modelet logistics/create-organization](https://github.com/HyperAgents/hmas/blob/HEAD/domains/logistics/create-organization/onto.ttl)<br/>- [Module regulation](https://github.com/HyperAgents/hmas/blob/HEAD/src/regulation.ttl)|

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
|Name|module-src-regulation-modelet-logistics-create-organization|
|----|----|
|Title|Merged&#32;module&#32;src/regulation.ttl&#32;from&#32;branch&#32;HEAD&#32;with&#32;related&#32;terms&#32;from&#32;the&#32;fragments&#32;domains/logistics/create-organization/onto.ttl|
|Composition|- [Modelet logistics/create-organization](https://github.com/HyperAgents/hmas/blob/HEAD/domains/logistics/create-organization/onto.ttl)<br/>- [Module regulation](https://github.com/HyperAgents/hmas/blob/HEAD/src/regulation.ttl)|

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
|Name|module-src-regulation-modelet-logistics-create-organization|
|----|----|
|Title|Merged&#32;module&#32;src/regulation.ttl&#32;from&#32;branch&#32;HEAD&#32;with&#32;related&#32;terms&#32;from&#32;the&#32;fragments&#32;domains/logistics/create-organization/onto.ttl|
|Composition|- [Modelet logistics/create-organization](https://github.com/HyperAgents/hmas/blob/HEAD/domains/logistics/create-organization/onto.ttl)<br/>- [Module regulation](https://github.com/HyperAgents/hmas/blob/HEAD/src/regulation.ttl)|

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
|Name|module-src-regulation-modelet-logistics-create-organization|
|----|----|
|Title|Merged&#32;module&#32;src/regulation.ttl&#32;from&#32;branch&#32;HEAD&#32;with&#32;related&#32;terms&#32;from&#32;the&#32;fragments&#32;domains/logistics/create-organization/onto.ttl|
|Composition|- [Modelet logistics/create-organization](https://github.com/HyperAgents/hmas/blob/HEAD/domains/logistics/create-organization/onto.ttl)<br/>- [Module regulation](https://github.com/HyperAgents/hmas/blob/HEAD/src/regulation.ttl)|

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
|Name|module-src-regulation-modelet-logistics-create-organization|
|----|----|
|Title|Merged&#32;module&#32;src/regulation.ttl&#32;from&#32;branch&#32;HEAD&#32;with&#32;related&#32;terms&#32;from&#32;the&#32;fragments&#32;domains/logistics/create-organization/onto.ttl|
|Composition|- [Modelet logistics/create-organization](https://github.com/HyperAgents/hmas/blob/HEAD/domains/logistics/create-organization/onto.ttl)<br/>- [Module regulation](https://github.com/HyperAgents/hmas/blob/HEAD/src/regulation.ttl)|

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
|Name|module-src-regulation-modelet-logistics-create-organization|
|----|----|
|Title|Merged&#32;module&#32;src/regulation.ttl&#32;from&#32;branch&#32;HEAD&#32;with&#32;related&#32;terms&#32;from&#32;the&#32;fragments&#32;domains/logistics/create-organization/onto.ttl|
|Composition|- [Modelet logistics/create-organization](https://github.com/HyperAgents/hmas/blob/HEAD/domains/logistics/create-organization/onto.ttl)<br/>- [Module regulation](https://github.com/HyperAgents/hmas/blob/HEAD/src/regulation.ttl)|

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
|Name|module-src-regulation-modelet-logistics-create-organization|
|----|----|
|Title|Merged&#32;module&#32;src/regulation.ttl&#32;from&#32;branch&#32;HEAD&#32;with&#32;related&#32;terms&#32;from&#32;the&#32;fragments&#32;domains/logistics/create-organization/onto.ttl|
|Composition|- [Modelet logistics/create-organization](https://github.com/HyperAgents/hmas/blob/HEAD/domains/logistics/create-organization/onto.ttl)<br/>- [Module regulation](https://github.com/HyperAgents/hmas/blob/HEAD/src/regulation.ttl)|

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
|Name|module-src-regulation-modelet-logistics-create-organization|
|----|----|
|Title|Merged&#32;module&#32;src/regulation.ttl&#32;from&#32;branch&#32;HEAD&#32;with&#32;related&#32;terms&#32;from&#32;the&#32;fragments&#32;domains/logistics/create-organization/onto.ttl|
|Composition|- [Modelet logistics/create-organization](https://github.com/HyperAgents/hmas/blob/HEAD/domains/logistics/create-organization/onto.ttl)<br/>- [Module regulation](https://github.com/HyperAgents/hmas/blob/HEAD/src/regulation.ttl)|

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
|Name|module-src-regulation-modelet-logistics-create-organization|
|----|----|
|Title|Merged&#32;module&#32;src/regulation.ttl&#32;from&#32;branch&#32;HEAD&#32;with&#32;related&#32;terms&#32;from&#32;the&#32;fragments&#32;domains/logistics/create-organization/onto.ttl|
|Composition|- [Modelet logistics/create-organization](https://github.com/HyperAgents/hmas/blob/HEAD/domains/logistics/create-organization/onto.ttl)<br/>- [Module regulation](https://github.com/HyperAgents/hmas/blob/HEAD/src/regulation.ttl)|

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
|Name|module-src-regulation-modelet-logistics-create-organization|
|----|----|
|Title|Merged&#32;module&#32;src/regulation.ttl&#32;from&#32;branch&#32;HEAD&#32;with&#32;related&#32;terms&#32;from&#32;the&#32;fragments&#32;domains/logistics/create-organization/onto.ttl|
|Composition|- [Modelet logistics/create-organization](https://github.com/HyperAgents/hmas/blob/HEAD/domains/logistics/create-organization/onto.ttl)<br/>- [Module regulation](https://github.com/HyperAgents/hmas/blob/HEAD/src/regulation.ttl)|

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
|Name|module-src-regulation-modelet-logistics-create-organization|
|----|----|
|Title|Merged&#32;module&#32;src/regulation.ttl&#32;from&#32;branch&#32;HEAD&#32;with&#32;related&#32;terms&#32;from&#32;the&#32;fragments&#32;domains/logistics/create-organization/onto.ttl|
|Composition|- [Modelet logistics/create-organization](https://github.com/HyperAgents/hmas/blob/HEAD/domains/logistics/create-organization/onto.ttl)<br/>- [Module regulation](https://github.com/HyperAgents/hmas/blob/HEAD/src/regulation.ttl)|

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
|Name|module-src-regulation-modelet-logistics-create-organization|
|----|----|
|Title|Merged&#32;module&#32;src/regulation.ttl&#32;from&#32;branch&#32;HEAD&#32;with&#32;related&#32;terms&#32;from&#32;the&#32;fragments&#32;domains/logistics/create-organization/onto.ttl|
|Composition|- [Modelet logistics/create-organization](https://github.com/HyperAgents/hmas/blob/HEAD/domains/logistics/create-organization/onto.ttl)<br/>- [Module regulation](https://github.com/HyperAgents/hmas/blob/HEAD/src/regulation.ttl)|

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
|Name|module-src-regulation-modelet-logistics-coordinate-activities|
|----|----|
|Title|Merged&#32;module&#32;src/regulation.ttl&#32;from&#32;branch&#32;HEAD&#32;with&#32;related&#32;terms&#32;from&#32;the&#32;fragments&#32;domains/logistics/coordinate-activities/onto.ttl|
|Composition|- [Modelet logistics/coordinate-activities](https://github.com/HyperAgents/hmas/blob/HEAD/domains/logistics/coordinate-activities/onto.ttl)<br/>- [Module regulation](https://github.com/HyperAgents/hmas/blob/HEAD/src/regulation.ttl)|

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
|Name|module-src-regulation-modelet-logistics-coordinate-activities|
|----|----|
|Title|Merged&#32;module&#32;src/regulation.ttl&#32;from&#32;branch&#32;HEAD&#32;with&#32;related&#32;terms&#32;from&#32;the&#32;fragments&#32;domains/logistics/coordinate-activities/onto.ttl|
|Composition|- [Modelet logistics/coordinate-activities](https://github.com/HyperAgents/hmas/blob/HEAD/domains/logistics/coordinate-activities/onto.ttl)<br/>- [Module regulation](https://github.com/HyperAgents/hmas/blob/HEAD/src/regulation.ttl)|

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
|Name|module-src-regulation-modelet-logistics-coordinate-activities|
|----|----|
|Title|Merged&#32;module&#32;src/regulation.ttl&#32;from&#32;branch&#32;HEAD&#32;with&#32;related&#32;terms&#32;from&#32;the&#32;fragments&#32;domains/logistics/coordinate-activities/onto.ttl|
|Composition|- [Modelet logistics/coordinate-activities](https://github.com/HyperAgents/hmas/blob/HEAD/domains/logistics/coordinate-activities/onto.ttl)<br/>- [Module regulation](https://github.com/HyperAgents/hmas/blob/HEAD/src/regulation.ttl)|

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
|Name|module-src-regulation-modelet-logistics-coordinate-activities|
|----|----|
|Title|Merged&#32;module&#32;src/regulation.ttl&#32;from&#32;branch&#32;HEAD&#32;with&#32;related&#32;terms&#32;from&#32;the&#32;fragments&#32;domains/logistics/coordinate-activities/onto.ttl|
|Composition|- [Modelet logistics/coordinate-activities](https://github.com/HyperAgents/hmas/blob/HEAD/domains/logistics/coordinate-activities/onto.ttl)<br/>- [Module regulation](https://github.com/HyperAgents/hmas/blob/HEAD/src/regulation.ttl)|

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
|Name|module-src-regulation-modelet-logistics-coordinate-activities|
|----|----|
|Title|Merged&#32;module&#32;src/regulation.ttl&#32;from&#32;branch&#32;HEAD&#32;with&#32;related&#32;terms&#32;from&#32;the&#32;fragments&#32;domains/logistics/coordinate-activities/onto.ttl|
|Composition|- [Modelet logistics/coordinate-activities](https://github.com/HyperAgents/hmas/blob/HEAD/domains/logistics/coordinate-activities/onto.ttl)<br/>- [Module regulation](https://github.com/HyperAgents/hmas/blob/HEAD/src/regulation.ttl)|

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
|Name|module-src-regulation-modelet-logistics-coordinate-activities|
|----|----|
|Title|Merged&#32;module&#32;src/regulation.ttl&#32;from&#32;branch&#32;HEAD&#32;with&#32;related&#32;terms&#32;from&#32;the&#32;fragments&#32;domains/logistics/coordinate-activities/onto.ttl|
|Composition|- [Modelet logistics/coordinate-activities](https://github.com/HyperAgents/hmas/blob/HEAD/domains/logistics/coordinate-activities/onto.ttl)<br/>- [Module regulation](https://github.com/HyperAgents/hmas/blob/HEAD/src/regulation.ttl)|

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
|Name|module-src-regulation-modelet-logistics-coordinate-activities|
|----|----|
|Title|Merged&#32;module&#32;src/regulation.ttl&#32;from&#32;branch&#32;HEAD&#32;with&#32;related&#32;terms&#32;from&#32;the&#32;fragments&#32;domains/logistics/coordinate-activities/onto.ttl|
|Composition|- [Modelet logistics/coordinate-activities](https://github.com/HyperAgents/hmas/blob/HEAD/domains/logistics/coordinate-activities/onto.ttl)<br/>- [Module regulation](https://github.com/HyperAgents/hmas/blob/HEAD/src/regulation.ttl)|

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
|Name|module-src-regulation-modelet-logistics-coordinate-activities|
|----|----|
|Title|Merged&#32;module&#32;src/regulation.ttl&#32;from&#32;branch&#32;HEAD&#32;with&#32;related&#32;terms&#32;from&#32;the&#32;fragments&#32;domains/logistics/coordinate-activities/onto.ttl|
|Composition|- [Modelet logistics/coordinate-activities](https://github.com/HyperAgents/hmas/blob/HEAD/domains/logistics/coordinate-activities/onto.ttl)<br/>- [Module regulation](https://github.com/HyperAgents/hmas/blob/HEAD/src/regulation.ttl)|

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
|Name|module-src-regulation-modelet-logistics-coordinate-activities|
|----|----|
|Title|Merged&#32;module&#32;src/regulation.ttl&#32;from&#32;branch&#32;HEAD&#32;with&#32;related&#32;terms&#32;from&#32;the&#32;fragments&#32;domains/logistics/coordinate-activities/onto.ttl|
|Composition|- [Modelet logistics/coordinate-activities](https://github.com/HyperAgents/hmas/blob/HEAD/domains/logistics/coordinate-activities/onto.ttl)<br/>- [Module regulation](https://github.com/HyperAgents/hmas/blob/HEAD/src/regulation.ttl)|

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
|Name|module-src-regulation-modelet-logistics-coordinate-activities|
|----|----|
|Title|Merged&#32;module&#32;src/regulation.ttl&#32;from&#32;branch&#32;HEAD&#32;with&#32;related&#32;terms&#32;from&#32;the&#32;fragments&#32;domains/logistics/coordinate-activities/onto.ttl|
|Composition|- [Modelet logistics/coordinate-activities](https://github.com/HyperAgents/hmas/blob/HEAD/domains/logistics/coordinate-activities/onto.ttl)<br/>- [Module regulation](https://github.com/HyperAgents/hmas/blob/HEAD/src/regulation.ttl)|

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
|Name|module-src-regulation-modelet-logistics-coordinate-activities|
|----|----|
|Title|Merged&#32;module&#32;src/regulation.ttl&#32;from&#32;branch&#32;HEAD&#32;with&#32;related&#32;terms&#32;from&#32;the&#32;fragments&#32;domains/logistics/coordinate-activities/onto.ttl|
|Composition|- [Modelet logistics/coordinate-activities](https://github.com/HyperAgents/hmas/blob/HEAD/domains/logistics/coordinate-activities/onto.ttl)<br/>- [Module regulation](https://github.com/HyperAgents/hmas/blob/HEAD/src/regulation.ttl)|

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
|Name|module-src-regulation-modelet-logistics-coordinate-activities|
|----|----|
|Title|Merged&#32;module&#32;src/regulation.ttl&#32;from&#32;branch&#32;HEAD&#32;with&#32;related&#32;terms&#32;from&#32;the&#32;fragments&#32;domains/logistics/coordinate-activities/onto.ttl|
|Composition|- [Modelet logistics/coordinate-activities](https://github.com/HyperAgents/hmas/blob/HEAD/domains/logistics/coordinate-activities/onto.ttl)<br/>- [Module regulation](https://github.com/HyperAgents/hmas/blob/HEAD/src/regulation.ttl)|

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
|Name|module-src-regulation-modelet-logistics-configure-organization|
|----|----|
|Title|Merged&#32;module&#32;src/regulation.ttl&#32;from&#32;branch&#32;HEAD&#32;with&#32;related&#32;terms&#32;from&#32;the&#32;fragments&#32;domains/logistics/configure-organization/onto.ttl|
|Composition|- [Modelet logistics/configure-organization](https://github.com/HyperAgents/hmas/blob/HEAD/domains/logistics/configure-organization/onto.ttl)<br/>- [Module regulation](https://github.com/HyperAgents/hmas/blob/HEAD/src/regulation.ttl)|

#### Criterion detail
|Identifier|[domain-and-range-referencing](https://ns.inria.fr/olivaw#domain-and-range-referencing)|
|----|----|
|Title|Domain&#32;and&#32;range&#32;referencing&#32;test|
|Description|A&#32;test&#32;case&#32;from&#32;the&#32;Best&#32;Practices&#32;tests&#32;checking&#32;if&#32;all&#32;the&#32;ranges&#32;and&#32;domains&#32;from&#32;the&#32;test&#32;subject&#32;point&#32;to&#32;terms&#32;that&#32;are&#32;defined&#32;in&#32;the&#32;vocabulary.|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-25)|Identifier|`domain-out-of-vocabulary`|
|[Section top](#pass-outcome-number-25)|Title|Domains&#32;properly&#32;defined|
|[Section top](#pass-outcome-number-25)|Description|Each&#32;rdfs:domain&#32;is&#32;defined&#32;within&#32;the&#32;fragment|

***
### Pass Outcome number 26

[Jump to summary definition](#summary-Pass-26)	|	[Previous Pass outcome](#pass-outcome-number-25)	|	[Next Pass outcome](#pass-outcome-number-27)

:white_check_mark:Pass outcome
#### Subject detail
|Name|module-src-regulation-modelet-logistics-configure-organization|
|----|----|
|Title|Merged&#32;module&#32;src/regulation.ttl&#32;from&#32;branch&#32;HEAD&#32;with&#32;related&#32;terms&#32;from&#32;the&#32;fragments&#32;domains/logistics/configure-organization/onto.ttl|
|Composition|- [Modelet logistics/configure-organization](https://github.com/HyperAgents/hmas/blob/HEAD/domains/logistics/configure-organization/onto.ttl)<br/>- [Module regulation](https://github.com/HyperAgents/hmas/blob/HEAD/src/regulation.ttl)|

#### Criterion detail
|Identifier|[domain-and-range-referencing](https://ns.inria.fr/olivaw#domain-and-range-referencing)|
|----|----|
|Title|Domain&#32;and&#32;range&#32;referencing&#32;test|
|Description|A&#32;test&#32;case&#32;from&#32;the&#32;Best&#32;Practices&#32;tests&#32;checking&#32;if&#32;all&#32;the&#32;ranges&#32;and&#32;domains&#32;from&#32;the&#32;test&#32;subject&#32;point&#32;to&#32;terms&#32;that&#32;are&#32;defined&#32;in&#32;the&#32;vocabulary.|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-26)|Identifier|`range-out-of-vocabulary`|
|[Section top](#pass-outcome-number-26)|Title|Ranges&#32;properly&#32;defined|
|[Section top](#pass-outcome-number-26)|Description|Each&#32;rdfs:range&#32;is&#32;defined&#32;within&#32;the&#32;fragment|

***
### Pass Outcome number 27

[Jump to summary definition](#summary-Pass-27)	|	[Previous Pass outcome](#pass-outcome-number-26)	|	[Next Pass outcome](#pass-outcome-number-28)

:white_check_mark:Pass outcome
#### Subject detail
|Name|module-src-regulation-modelet-logistics-configure-organization|
|----|----|
|Title|Merged&#32;module&#32;src/regulation.ttl&#32;from&#32;branch&#32;HEAD&#32;with&#32;related&#32;terms&#32;from&#32;the&#32;fragments&#32;domains/logistics/configure-organization/onto.ttl|
|Composition|- [Modelet logistics/configure-organization](https://github.com/HyperAgents/hmas/blob/HEAD/domains/logistics/configure-organization/onto.ttl)<br/>- [Module regulation](https://github.com/HyperAgents/hmas/blob/HEAD/src/regulation.ttl)|

#### Criterion detail
|Identifier|[labeled-terms](https://ns.inria.fr/olivaw#labeled-terms)|
|----|----|
|Title|Term&#32;labeling&#32;test|
|Description|A&#32;test&#32;case&#32;from&#32;the&#32;Best&#32;Practices&#32;tests&#32;checking&#32;if&#32;all&#32;the&#32;terms&#32;of&#32;the&#32;subject&#32;have&#32;a&#32;rdfs:label&#32;property&#32;pointing&#32;to&#32;a&#32;literal&#32;in&#32;English|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-27)|Identifier|`not-labeled-term`|
|[Section top](#pass-outcome-number-27)|Title|All&#32;terms&#32;labeled|
|[Section top](#pass-outcome-number-27)|Description|All&#32;the&#32;terms&#32;defined&#32;in&#32;the&#32;subject&#32;have&#32;a&#32;rdfs:label&#32;in&#32;English|

***
### Pass Outcome number 28

[Jump to summary definition](#summary-Pass-28)	|	[Previous Pass outcome](#pass-outcome-number-27)	|	[Next Pass outcome](#pass-outcome-number-29)

:white_check_mark:Pass outcome
#### Subject detail
|Name|module-src-regulation-modelet-logistics-configure-organization|
|----|----|
|Title|Merged&#32;module&#32;src/regulation.ttl&#32;from&#32;branch&#32;HEAD&#32;with&#32;related&#32;terms&#32;from&#32;the&#32;fragments&#32;domains/logistics/configure-organization/onto.ttl|
|Composition|- [Modelet logistics/configure-organization](https://github.com/HyperAgents/hmas/blob/HEAD/domains/logistics/configure-organization/onto.ttl)<br/>- [Module regulation](https://github.com/HyperAgents/hmas/blob/HEAD/src/regulation.ttl)|

#### Criterion detail
|Identifier|[owl-rl-constraint](https://ns.inria.fr/olivaw#owl-rl-constraint)|
|----|----|
|Title|OWL&#32;RL&#32;Constraint&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;check&#32;wether&#32;the&#32;test&#32;subject&#32;is&#32;syntaxically&#32;correct&#32;or&#32;not.|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-28)|Identifier|`owl-rl-constraint-violation`|
|[Section top](#pass-outcome-number-28)|Title|OWL&#32;RL&#32;consistent|
|[Section top](#pass-outcome-number-28)|Description|The&#32;provided&#32;graph&#32;is&#32;consistent&#32;for&#32;any&#32;OWL&#32;RL&#32;constraint|

***
### Pass Outcome number 29

[Jump to summary definition](#summary-Pass-29)	|	[Previous Pass outcome](#pass-outcome-number-28)	|	[Next Pass outcome](#pass-outcome-number-30)

:white_check_mark:Pass outcome
#### Subject detail
|Name|module-src-regulation-modelet-logistics-configure-organization|
|----|----|
|Title|Merged&#32;module&#32;src/regulation.ttl&#32;from&#32;branch&#32;HEAD&#32;with&#32;related&#32;terms&#32;from&#32;the&#32;fragments&#32;domains/logistics/configure-organization/onto.ttl|
|Composition|- [Modelet logistics/configure-organization](https://github.com/HyperAgents/hmas/blob/HEAD/domains/logistics/configure-organization/onto.ttl)<br/>- [Module regulation](https://github.com/HyperAgents/hmas/blob/HEAD/src/regulation.ttl)|

#### Criterion detail
|Identifier|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|
|----|----|
|Title|Profile&#32;compatibility&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;check&#32;whether&#32;the&#32;test&#32;subject&#32;is&#32;compatible&#32;with&#32;a&#32;profile&#32;or&#32;not,&#32;and&#32;if&#32;it&#32;is&#32;not,&#32;why.|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-29)|Identifier|`owl-el-profile-error`|
|[Section top](#pass-outcome-number-29)|Title|OWL&#32;EL&#32;Profile&#32;compatible|
|[Section top](#pass-outcome-number-29)|Description|The&#32;subject&#32;is&#32;included&#32;in&#32;the&#32;OWL&#32;EL&#32;sublanguage|

***
### Pass Outcome number 30

[Jump to summary definition](#summary-Pass-30)	|	[Previous Pass outcome](#pass-outcome-number-29)	|	[Next Pass outcome](#pass-outcome-number-31)

:white_check_mark:Pass outcome
#### Subject detail
|Name|module-src-regulation-modelet-logistics-configure-organization|
|----|----|
|Title|Merged&#32;module&#32;src/regulation.ttl&#32;from&#32;branch&#32;HEAD&#32;with&#32;related&#32;terms&#32;from&#32;the&#32;fragments&#32;domains/logistics/configure-organization/onto.ttl|
|Composition|- [Modelet logistics/configure-organization](https://github.com/HyperAgents/hmas/blob/HEAD/domains/logistics/configure-organization/onto.ttl)<br/>- [Module regulation](https://github.com/HyperAgents/hmas/blob/HEAD/src/regulation.ttl)|

#### Criterion detail
|Identifier|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|
|----|----|
|Title|Profile&#32;compatibility&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;check&#32;whether&#32;the&#32;test&#32;subject&#32;is&#32;compatible&#32;with&#32;a&#32;profile&#32;or&#32;not,&#32;and&#32;if&#32;it&#32;is&#32;not,&#32;why.|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-30)|Identifier|`owl-ql-profile-error`|
|[Section top](#pass-outcome-number-30)|Title|OWL&#32;QL&#32;Profile&#32;compatible|
|[Section top](#pass-outcome-number-30)|Description|The&#32;subject&#32;is&#32;included&#32;in&#32;the&#32;OWL&#32;QL&#32;sublanguage|

***
### Pass Outcome number 31

[Jump to summary definition](#summary-Pass-31)	|	[Previous Pass outcome](#pass-outcome-number-30)	|	[Next Pass outcome](#pass-outcome-number-32)

:white_check_mark:Pass outcome
#### Subject detail
|Name|module-src-regulation-modelet-logistics-configure-organization|
|----|----|
|Title|Merged&#32;module&#32;src/regulation.ttl&#32;from&#32;branch&#32;HEAD&#32;with&#32;related&#32;terms&#32;from&#32;the&#32;fragments&#32;domains/logistics/configure-organization/onto.ttl|
|Composition|- [Modelet logistics/configure-organization](https://github.com/HyperAgents/hmas/blob/HEAD/domains/logistics/configure-organization/onto.ttl)<br/>- [Module regulation](https://github.com/HyperAgents/hmas/blob/HEAD/src/regulation.ttl)|

#### Criterion detail
|Identifier|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|
|----|----|
|Title|Profile&#32;compatibility&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;check&#32;whether&#32;the&#32;test&#32;subject&#32;is&#32;compatible&#32;with&#32;a&#32;profile&#32;or&#32;not,&#32;and&#32;if&#32;it&#32;is&#32;not,&#32;why.|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-31)|Identifier|`owl-rl-profile-error`|
|[Section top](#pass-outcome-number-31)|Title|OWL&#32;RL&#32;Profile&#32;compatible|
|[Section top](#pass-outcome-number-31)|Description|The&#32;subject&#32;is&#32;included&#32;in&#32;the&#32;OWL&#32;RL&#32;sublanguage|

***
### Pass Outcome number 32

[Jump to summary definition](#summary-Pass-32)	|	[Previous Pass outcome](#pass-outcome-number-31)	|	[Next Pass outcome](#pass-outcome-number-33)

:white_check_mark:Pass outcome
#### Subject detail
|Name|module-src-regulation-modelet-logistics-configure-organization|
|----|----|
|Title|Merged&#32;module&#32;src/regulation.ttl&#32;from&#32;branch&#32;HEAD&#32;with&#32;related&#32;terms&#32;from&#32;the&#32;fragments&#32;domains/logistics/configure-organization/onto.ttl|
|Composition|- [Modelet logistics/configure-organization](https://github.com/HyperAgents/hmas/blob/HEAD/domains/logistics/configure-organization/onto.ttl)<br/>- [Module regulation](https://github.com/HyperAgents/hmas/blob/HEAD/src/regulation.ttl)|

#### Criterion detail
|Identifier|[proper-extension-predicate](https://ns.inria.fr/olivaw#proper-extension-predicate)|
|----|----|
|Title|Predicate&#32;extension&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;test&#32;the&#32;proper&#32;use&#32;of&#32;predicates&#32;rdfs:subClassOf&#32;and&#32;rdfs:subPropertyOf&#32;on&#32;the&#32;ontology&#32;terms|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-32)|Identifier|`class-subpropertyof`|
|[Section top](#pass-outcome-number-32)|Title|No&#32;class&#32;subproperty|
|[Section top](#pass-outcome-number-32)|Description|No&#32;ontology&#32;class&#32;is&#32;a&#32;subproperty|

***
### Pass Outcome number 33

[Jump to summary definition](#summary-Pass-33)	|	[Previous Pass outcome](#pass-outcome-number-32)	|	[Next Pass outcome](#pass-outcome-number-34)

:white_check_mark:Pass outcome
#### Subject detail
|Name|module-src-regulation-modelet-logistics-configure-organization|
|----|----|
|Title|Merged&#32;module&#32;src/regulation.ttl&#32;from&#32;branch&#32;HEAD&#32;with&#32;related&#32;terms&#32;from&#32;the&#32;fragments&#32;domains/logistics/configure-organization/onto.ttl|
|Composition|- [Modelet logistics/configure-organization](https://github.com/HyperAgents/hmas/blob/HEAD/domains/logistics/configure-organization/onto.ttl)<br/>- [Module regulation](https://github.com/HyperAgents/hmas/blob/HEAD/src/regulation.ttl)|

#### Criterion detail
|Identifier|[proper-extension-predicate](https://ns.inria.fr/olivaw#proper-extension-predicate)|
|----|----|
|Title|Predicate&#32;extension&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;test&#32;the&#32;proper&#32;use&#32;of&#32;predicates&#32;rdfs:subClassOf&#32;and&#32;rdfs:subPropertyOf&#32;on&#32;the&#32;ontology&#32;terms|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-33)|Identifier|`property-subclassof`|
|[Section top](#pass-outcome-number-33)|Title|No&#32;property&#32;subclass|
|[Section top](#pass-outcome-number-33)|Description|No&#32;ontology&#32;property&#32;is&#32;a&#32;subclass|

***
### Pass Outcome number 34

[Jump to summary definition](#summary-Pass-34)	|	[Previous Pass outcome](#pass-outcome-number-33)	|	[Next Pass outcome](#pass-outcome-number-35)

:white_check_mark:Pass outcome
#### Subject detail
|Name|module-src-regulation-modelet-logistics-configure-organization|
|----|----|
|Title|Merged&#32;module&#32;src/regulation.ttl&#32;from&#32;branch&#32;HEAD&#32;with&#32;related&#32;terms&#32;from&#32;the&#32;fragments&#32;domains/logistics/configure-organization/onto.ttl|
|Composition|- [Modelet logistics/configure-organization](https://github.com/HyperAgents/hmas/blob/HEAD/domains/logistics/configure-organization/onto.ttl)<br/>- [Module regulation](https://github.com/HyperAgents/hmas/blob/HEAD/src/regulation.ttl)|

#### Criterion detail
|Identifier|[proper-extension-predicate](https://ns.inria.fr/olivaw#proper-extension-predicate)|
|----|----|
|Title|Predicate&#32;extension&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;test&#32;the&#32;proper&#32;use&#32;of&#32;predicates&#32;rdfs:subClassOf&#32;and&#32;rdfs:subPropertyOf&#32;on&#32;the&#32;ontology&#32;terms|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-34)|Identifier|`subclassof-property`|
|[Section top](#pass-outcome-number-34)|Title|No&#32;subclass&#32;of&#32;property|
|[Section top](#pass-outcome-number-34)|Description|No&#32;ontology&#32;term&#32;is&#32;a&#32;subclass&#32;of&#32;a&#32;property|

***
### Pass Outcome number 35

[Jump to summary definition](#summary-Pass-35)	|	[Previous Pass outcome](#pass-outcome-number-34)	|	[Next Pass outcome](#pass-outcome-number-36)

:white_check_mark:Pass outcome
#### Subject detail
|Name|module-src-regulation-modelet-logistics-configure-organization|
|----|----|
|Title|Merged&#32;module&#32;src/regulation.ttl&#32;from&#32;branch&#32;HEAD&#32;with&#32;related&#32;terms&#32;from&#32;the&#32;fragments&#32;domains/logistics/configure-organization/onto.ttl|
|Composition|- [Modelet logistics/configure-organization](https://github.com/HyperAgents/hmas/blob/HEAD/domains/logistics/configure-organization/onto.ttl)<br/>- [Module regulation](https://github.com/HyperAgents/hmas/blob/HEAD/src/regulation.ttl)|

#### Criterion detail
|Identifier|[proper-extension-predicate](https://ns.inria.fr/olivaw#proper-extension-predicate)|
|----|----|
|Title|Predicate&#32;extension&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;test&#32;the&#32;proper&#32;use&#32;of&#32;predicates&#32;rdfs:subClassOf&#32;and&#32;rdfs:subPropertyOf&#32;on&#32;the&#32;ontology&#32;terms|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-35)|Identifier|`subpropertyof-class`|
|[Section top](#pass-outcome-number-35)|Title|No&#32;subproperty&#32;of&#32;class|
|[Section top](#pass-outcome-number-35)|Description|No&#32;ontology&#32;term&#32;is&#32;a&#32;subproperty&#32;of&#32;a&#32;class|

***
### Pass Outcome number 36

[Jump to summary definition](#summary-Pass-36)	|	[Previous Pass outcome](#pass-outcome-number-35)	|	[Next Pass outcome](#pass-outcome-number-37)

:white_check_mark:Pass outcome
#### Subject detail
|Name|module-src-regulation-modelet-logistics-configure-organization|
|----|----|
|Title|Merged&#32;module&#32;src/regulation.ttl&#32;from&#32;branch&#32;HEAD&#32;with&#32;related&#32;terms&#32;from&#32;the&#32;fragments&#32;domains/logistics/configure-organization/onto.ttl|
|Composition|- [Modelet logistics/configure-organization](https://github.com/HyperAgents/hmas/blob/HEAD/domains/logistics/configure-organization/onto.ttl)<br/>- [Module regulation](https://github.com/HyperAgents/hmas/blob/HEAD/src/regulation.ttl)|

#### Criterion detail
|Identifier|[term-referencing](https://ns.inria.fr/olivaw#term-referencing)|
|----|----|
|Title|Term&#32;referencing&#32;test|
|Description|A&#32;test&#32;case&#32;from&#32;the&#32;Best&#32;Practices&#32;tests&#32;checking&#32;if&#32;each&#32;term&#32;of&#32;the&#32;test&#32;subject&#32;is&#32;referenced&#32;to&#32;a&#32;module&#32;through&#32;a&#32;rdfs:isDefinedBy&#32;property.|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-36)|Identifier|`no-reference-module`|
|[Section top](#pass-outcome-number-36)|Title|Any&#32;term&#32;is&#32;referenced|
|[Section top](#pass-outcome-number-36)|Description|Each&#32;term&#32;of&#32;the&#32;test&#32;subject&#32;is&#32;linked&#32;to&#32;a&#32;module&#32;by&#32;a&#32;rdfs:isDefinedBy&#32;property|

***
### Pass Outcome number 37

[Jump to summary definition](#summary-Pass-37)	|	[Previous Pass outcome](#pass-outcome-number-36)	|	[Next Pass outcome](#pass-outcome-number-38)

:white_check_mark:Pass outcome
#### Subject detail
|Name|module-src-regulation|
|----|----|
|Title|Standalone&#32;module&#32;src/regulation.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Module regulation](https://github.com/HyperAgents/hmas/blob/HEAD/src/regulation.ttl)|

#### Criterion detail
|Identifier|[domain-and-range-referencing](https://ns.inria.fr/olivaw#domain-and-range-referencing)|
|----|----|
|Title|Domain&#32;and&#32;range&#32;referencing&#32;test|
|Description|A&#32;test&#32;case&#32;from&#32;the&#32;Best&#32;Practices&#32;tests&#32;checking&#32;if&#32;all&#32;the&#32;ranges&#32;and&#32;domains&#32;from&#32;the&#32;test&#32;subject&#32;point&#32;to&#32;terms&#32;that&#32;are&#32;defined&#32;in&#32;the&#32;vocabulary.|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-37)|Identifier|`domain-out-of-vocabulary`|
|[Section top](#pass-outcome-number-37)|Title|Domains&#32;properly&#32;defined|
|[Section top](#pass-outcome-number-37)|Description|Each&#32;rdfs:domain&#32;is&#32;defined&#32;within&#32;the&#32;fragment|

***
### Pass Outcome number 38

[Jump to summary definition](#summary-Pass-38)	|	[Previous Pass outcome](#pass-outcome-number-37)	|	[Next Pass outcome](#pass-outcome-number-39)

:white_check_mark:Pass outcome
#### Subject detail
|Name|module-src-regulation|
|----|----|
|Title|Standalone&#32;module&#32;src/regulation.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Module regulation](https://github.com/HyperAgents/hmas/blob/HEAD/src/regulation.ttl)|

#### Criterion detail
|Identifier|[domain-and-range-referencing](https://ns.inria.fr/olivaw#domain-and-range-referencing)|
|----|----|
|Title|Domain&#32;and&#32;range&#32;referencing&#32;test|
|Description|A&#32;test&#32;case&#32;from&#32;the&#32;Best&#32;Practices&#32;tests&#32;checking&#32;if&#32;all&#32;the&#32;ranges&#32;and&#32;domains&#32;from&#32;the&#32;test&#32;subject&#32;point&#32;to&#32;terms&#32;that&#32;are&#32;defined&#32;in&#32;the&#32;vocabulary.|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-38)|Identifier|`range-out-of-vocabulary`|
|[Section top](#pass-outcome-number-38)|Title|Ranges&#32;properly&#32;defined|
|[Section top](#pass-outcome-number-38)|Description|Each&#32;rdfs:range&#32;is&#32;defined&#32;within&#32;the&#32;fragment|

***
### Pass Outcome number 39

[Jump to summary definition](#summary-Pass-39)	|	[Previous Pass outcome](#pass-outcome-number-38)	|	[Next Pass outcome](#pass-outcome-number-40)

:white_check_mark:Pass outcome
#### Subject detail
|Name|module-src-regulation|
|----|----|
|Title|Standalone&#32;module&#32;src/regulation.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Module regulation](https://github.com/HyperAgents/hmas/blob/HEAD/src/regulation.ttl)|

#### Criterion detail
|Identifier|[labeled-terms](https://ns.inria.fr/olivaw#labeled-terms)|
|----|----|
|Title|Term&#32;labeling&#32;test|
|Description|A&#32;test&#32;case&#32;from&#32;the&#32;Best&#32;Practices&#32;tests&#32;checking&#32;if&#32;all&#32;the&#32;terms&#32;of&#32;the&#32;subject&#32;have&#32;a&#32;rdfs:label&#32;property&#32;pointing&#32;to&#32;a&#32;literal&#32;in&#32;English|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-39)|Identifier|`not-labeled-term`|
|[Section top](#pass-outcome-number-39)|Title|All&#32;terms&#32;labeled|
|[Section top](#pass-outcome-number-39)|Description|All&#32;the&#32;terms&#32;defined&#32;in&#32;the&#32;subject&#32;have&#32;a&#32;rdfs:label&#32;in&#32;English|

***
### Pass Outcome number 40

[Jump to summary definition](#summary-Pass-40)	|	[Previous Pass outcome](#pass-outcome-number-39)	|	[Next Pass outcome](#pass-outcome-number-41)

:white_check_mark:Pass outcome
#### Subject detail
|Name|module-src-regulation|
|----|----|
|Title|Standalone&#32;module&#32;src/regulation.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Module regulation](https://github.com/HyperAgents/hmas/blob/HEAD/src/regulation.ttl)|

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
|Name|module-src-regulation|
|----|----|
|Title|Standalone&#32;module&#32;src/regulation.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Module regulation](https://github.com/HyperAgents/hmas/blob/HEAD/src/regulation.ttl)|

#### Criterion detail
|Identifier|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|
|----|----|
|Title|Profile&#32;compatibility&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;check&#32;whether&#32;the&#32;test&#32;subject&#32;is&#32;compatible&#32;with&#32;a&#32;profile&#32;or&#32;not,&#32;and&#32;if&#32;it&#32;is&#32;not,&#32;why.|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-41)|Identifier|`owl-el-profile-error`|
|[Section top](#pass-outcome-number-41)|Title|OWL&#32;EL&#32;Profile&#32;compatible|
|[Section top](#pass-outcome-number-41)|Description|The&#32;subject&#32;is&#32;included&#32;in&#32;the&#32;OWL&#32;EL&#32;sublanguage|

***
### Pass Outcome number 42

[Jump to summary definition](#summary-Pass-42)	|	[Previous Pass outcome](#pass-outcome-number-41)	|	[Next Pass outcome](#pass-outcome-number-43)

:white_check_mark:Pass outcome
#### Subject detail
|Name|module-src-regulation|
|----|----|
|Title|Standalone&#32;module&#32;src/regulation.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Module regulation](https://github.com/HyperAgents/hmas/blob/HEAD/src/regulation.ttl)|

#### Criterion detail
|Identifier|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|
|----|----|
|Title|Profile&#32;compatibility&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;check&#32;whether&#32;the&#32;test&#32;subject&#32;is&#32;compatible&#32;with&#32;a&#32;profile&#32;or&#32;not,&#32;and&#32;if&#32;it&#32;is&#32;not,&#32;why.|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-42)|Identifier|`owl-ql-profile-error`|
|[Section top](#pass-outcome-number-42)|Title|OWL&#32;QL&#32;Profile&#32;compatible|
|[Section top](#pass-outcome-number-42)|Description|The&#32;subject&#32;is&#32;included&#32;in&#32;the&#32;OWL&#32;QL&#32;sublanguage|

***
### Pass Outcome number 43

[Jump to summary definition](#summary-Pass-43)	|	[Previous Pass outcome](#pass-outcome-number-42)	|	[Next Pass outcome](#pass-outcome-number-44)

:white_check_mark:Pass outcome
#### Subject detail
|Name|module-src-regulation|
|----|----|
|Title|Standalone&#32;module&#32;src/regulation.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Module regulation](https://github.com/HyperAgents/hmas/blob/HEAD/src/regulation.ttl)|

#### Criterion detail
|Identifier|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|
|----|----|
|Title|Profile&#32;compatibility&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;check&#32;whether&#32;the&#32;test&#32;subject&#32;is&#32;compatible&#32;with&#32;a&#32;profile&#32;or&#32;not,&#32;and&#32;if&#32;it&#32;is&#32;not,&#32;why.|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-43)|Identifier|`owl-rl-profile-error`|
|[Section top](#pass-outcome-number-43)|Title|OWL&#32;RL&#32;Profile&#32;compatible|
|[Section top](#pass-outcome-number-43)|Description|The&#32;subject&#32;is&#32;included&#32;in&#32;the&#32;OWL&#32;RL&#32;sublanguage|

***
### Pass Outcome number 44

[Jump to summary definition](#summary-Pass-44)	|	[Previous Pass outcome](#pass-outcome-number-43)	|	[Next Pass outcome](#pass-outcome-number-45)

:white_check_mark:Pass outcome
#### Subject detail
|Name|module-src-regulation|
|----|----|
|Title|Standalone&#32;module&#32;src/regulation.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Module regulation](https://github.com/HyperAgents/hmas/blob/HEAD/src/regulation.ttl)|

#### Criterion detail
|Identifier|[proper-extension-predicate](https://ns.inria.fr/olivaw#proper-extension-predicate)|
|----|----|
|Title|Predicate&#32;extension&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;test&#32;the&#32;proper&#32;use&#32;of&#32;predicates&#32;rdfs:subClassOf&#32;and&#32;rdfs:subPropertyOf&#32;on&#32;the&#32;ontology&#32;terms|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-44)|Identifier|`class-subpropertyof`|
|[Section top](#pass-outcome-number-44)|Title|No&#32;class&#32;subproperty|
|[Section top](#pass-outcome-number-44)|Description|No&#32;ontology&#32;class&#32;is&#32;a&#32;subproperty|

***
### Pass Outcome number 45

[Jump to summary definition](#summary-Pass-45)	|	[Previous Pass outcome](#pass-outcome-number-44)	|	[Next Pass outcome](#pass-outcome-number-46)

:white_check_mark:Pass outcome
#### Subject detail
|Name|module-src-regulation|
|----|----|
|Title|Standalone&#32;module&#32;src/regulation.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Module regulation](https://github.com/HyperAgents/hmas/blob/HEAD/src/regulation.ttl)|

#### Criterion detail
|Identifier|[proper-extension-predicate](https://ns.inria.fr/olivaw#proper-extension-predicate)|
|----|----|
|Title|Predicate&#32;extension&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;test&#32;the&#32;proper&#32;use&#32;of&#32;predicates&#32;rdfs:subClassOf&#32;and&#32;rdfs:subPropertyOf&#32;on&#32;the&#32;ontology&#32;terms|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-45)|Identifier|`property-subclassof`|
|[Section top](#pass-outcome-number-45)|Title|No&#32;property&#32;subclass|
|[Section top](#pass-outcome-number-45)|Description|No&#32;ontology&#32;property&#32;is&#32;a&#32;subclass|

***
### Pass Outcome number 46

[Jump to summary definition](#summary-Pass-46)	|	[Previous Pass outcome](#pass-outcome-number-45)	|	[Next Pass outcome](#pass-outcome-number-47)

:white_check_mark:Pass outcome
#### Subject detail
|Name|module-src-regulation|
|----|----|
|Title|Standalone&#32;module&#32;src/regulation.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Module regulation](https://github.com/HyperAgents/hmas/blob/HEAD/src/regulation.ttl)|

#### Criterion detail
|Identifier|[proper-extension-predicate](https://ns.inria.fr/olivaw#proper-extension-predicate)|
|----|----|
|Title|Predicate&#32;extension&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;test&#32;the&#32;proper&#32;use&#32;of&#32;predicates&#32;rdfs:subClassOf&#32;and&#32;rdfs:subPropertyOf&#32;on&#32;the&#32;ontology&#32;terms|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-46)|Identifier|`subclassof-property`|
|[Section top](#pass-outcome-number-46)|Title|No&#32;subclass&#32;of&#32;property|
|[Section top](#pass-outcome-number-46)|Description|No&#32;ontology&#32;term&#32;is&#32;a&#32;subclass&#32;of&#32;a&#32;property|

***
### Pass Outcome number 47

[Jump to summary definition](#summary-Pass-47)	|	[Previous Pass outcome](#pass-outcome-number-46)	|	[Next Pass outcome](#pass-outcome-number-48)

:white_check_mark:Pass outcome
#### Subject detail
|Name|module-src-regulation|
|----|----|
|Title|Standalone&#32;module&#32;src/regulation.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Module regulation](https://github.com/HyperAgents/hmas/blob/HEAD/src/regulation.ttl)|

#### Criterion detail
|Identifier|[proper-extension-predicate](https://ns.inria.fr/olivaw#proper-extension-predicate)|
|----|----|
|Title|Predicate&#32;extension&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;test&#32;the&#32;proper&#32;use&#32;of&#32;predicates&#32;rdfs:subClassOf&#32;and&#32;rdfs:subPropertyOf&#32;on&#32;the&#32;ontology&#32;terms|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-47)|Identifier|`subpropertyof-class`|
|[Section top](#pass-outcome-number-47)|Title|No&#32;subproperty&#32;of&#32;class|
|[Section top](#pass-outcome-number-47)|Description|No&#32;ontology&#32;term&#32;is&#32;a&#32;subproperty&#32;of&#32;a&#32;class|

***
### Pass Outcome number 48

[Jump to summary definition](#summary-Pass-48)	|	[Previous Pass outcome](#pass-outcome-number-47)	|	[Next Pass outcome](#pass-outcome-number-49)

:white_check_mark:Pass outcome
#### Subject detail
|Name|module-src-regulation|
|----|----|
|Title|Standalone&#32;module&#32;src/regulation.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Module regulation](https://github.com/HyperAgents/hmas/blob/HEAD/src/regulation.ttl)|

#### Criterion detail
|Identifier|[term-referencing](https://ns.inria.fr/olivaw#term-referencing)|
|----|----|
|Title|Term&#32;referencing&#32;test|
|Description|A&#32;test&#32;case&#32;from&#32;the&#32;Best&#32;Practices&#32;tests&#32;checking&#32;if&#32;each&#32;term&#32;of&#32;the&#32;test&#32;subject&#32;is&#32;referenced&#32;to&#32;a&#32;module&#32;through&#32;a&#32;rdfs:isDefinedBy&#32;property.|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-48)|Identifier|`no-reference-module`|
|[Section top](#pass-outcome-number-48)|Title|Any&#32;term&#32;is&#32;referenced|
|[Section top](#pass-outcome-number-48)|Description|Each&#32;term&#32;of&#32;the&#32;test&#32;subject&#32;is&#32;linked&#32;to&#32;a&#32;module&#32;by&#32;a&#32;rdfs:isDefinedBy&#32;property|

***
### Pass Outcome number 49

[Jump to summary definition](#summary-Pass-49)	|	[Previous Pass outcome](#pass-outcome-number-48)	|	[Next Pass outcome](#pass-outcome-number-50)

:white_check_mark:Pass outcome
#### Subject detail
|Name|module-src-interaction-modelet-manufacturing-environments-discover-behavior-specifications|
|----|----|
|Title|Merged&#32;module&#32;src/interaction.ttl&#32;from&#32;branch&#32;HEAD&#32;with&#32;related&#32;terms&#32;from&#32;the&#32;fragments&#32;domains/manufacturing-environments/discover-behavior-specifications/onto.ttl|
|Composition|- [Modelet manufacturing-environments/discover-behavior-specifications](https://github.com/HyperAgents/hmas/blob/HEAD/domains/manufacturing-environments/discover-behavior-specifications/onto.ttl)<br/>- [Module interaction](https://github.com/HyperAgents/hmas/blob/HEAD/src/interaction.ttl)|

#### Criterion detail
|Identifier|[domain-and-range-referencing](https://ns.inria.fr/olivaw#domain-and-range-referencing)|
|----|----|
|Title|Domain&#32;and&#32;range&#32;referencing&#32;test|
|Description|A&#32;test&#32;case&#32;from&#32;the&#32;Best&#32;Practices&#32;tests&#32;checking&#32;if&#32;all&#32;the&#32;ranges&#32;and&#32;domains&#32;from&#32;the&#32;test&#32;subject&#32;point&#32;to&#32;terms&#32;that&#32;are&#32;defined&#32;in&#32;the&#32;vocabulary.|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-49)|Identifier|`domain-out-of-vocabulary`|
|[Section top](#pass-outcome-number-49)|Title|Domains&#32;properly&#32;defined|
|[Section top](#pass-outcome-number-49)|Description|Each&#32;rdfs:domain&#32;is&#32;defined&#32;within&#32;the&#32;fragment|

***
### Pass Outcome number 50

[Jump to summary definition](#summary-Pass-50)	|	[Previous Pass outcome](#pass-outcome-number-49)	|	[Next Pass outcome](#pass-outcome-number-51)

:white_check_mark:Pass outcome
#### Subject detail
|Name|module-src-interaction-modelet-manufacturing-environments-discover-behavior-specifications|
|----|----|
|Title|Merged&#32;module&#32;src/interaction.ttl&#32;from&#32;branch&#32;HEAD&#32;with&#32;related&#32;terms&#32;from&#32;the&#32;fragments&#32;domains/manufacturing-environments/discover-behavior-specifications/onto.ttl|
|Composition|- [Modelet manufacturing-environments/discover-behavior-specifications](https://github.com/HyperAgents/hmas/blob/HEAD/domains/manufacturing-environments/discover-behavior-specifications/onto.ttl)<br/>- [Module interaction](https://github.com/HyperAgents/hmas/blob/HEAD/src/interaction.ttl)|

#### Criterion detail
|Identifier|[domain-and-range-referencing](https://ns.inria.fr/olivaw#domain-and-range-referencing)|
|----|----|
|Title|Domain&#32;and&#32;range&#32;referencing&#32;test|
|Description|A&#32;test&#32;case&#32;from&#32;the&#32;Best&#32;Practices&#32;tests&#32;checking&#32;if&#32;all&#32;the&#32;ranges&#32;and&#32;domains&#32;from&#32;the&#32;test&#32;subject&#32;point&#32;to&#32;terms&#32;that&#32;are&#32;defined&#32;in&#32;the&#32;vocabulary.|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-50)|Identifier|`range-out-of-vocabulary`|
|[Section top](#pass-outcome-number-50)|Title|Ranges&#32;properly&#32;defined|
|[Section top](#pass-outcome-number-50)|Description|Each&#32;rdfs:range&#32;is&#32;defined&#32;within&#32;the&#32;fragment|

***
### Pass Outcome number 51

[Jump to summary definition](#summary-Pass-51)	|	[Previous Pass outcome](#pass-outcome-number-50)	|	[Next Pass outcome](#pass-outcome-number-52)

:white_check_mark:Pass outcome
#### Subject detail
|Name|module-src-interaction-modelet-manufacturing-environments-discover-behavior-specifications|
|----|----|
|Title|Merged&#32;module&#32;src/interaction.ttl&#32;from&#32;branch&#32;HEAD&#32;with&#32;related&#32;terms&#32;from&#32;the&#32;fragments&#32;domains/manufacturing-environments/discover-behavior-specifications/onto.ttl|
|Composition|- [Modelet manufacturing-environments/discover-behavior-specifications](https://github.com/HyperAgents/hmas/blob/HEAD/domains/manufacturing-environments/discover-behavior-specifications/onto.ttl)<br/>- [Module interaction](https://github.com/HyperAgents/hmas/blob/HEAD/src/interaction.ttl)|

#### Criterion detail
|Identifier|[labeled-terms](https://ns.inria.fr/olivaw#labeled-terms)|
|----|----|
|Title|Term&#32;labeling&#32;test|
|Description|A&#32;test&#32;case&#32;from&#32;the&#32;Best&#32;Practices&#32;tests&#32;checking&#32;if&#32;all&#32;the&#32;terms&#32;of&#32;the&#32;subject&#32;have&#32;a&#32;rdfs:label&#32;property&#32;pointing&#32;to&#32;a&#32;literal&#32;in&#32;English|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-51)|Identifier|`not-labeled-term`|
|[Section top](#pass-outcome-number-51)|Title|All&#32;terms&#32;labeled|
|[Section top](#pass-outcome-number-51)|Description|All&#32;the&#32;terms&#32;defined&#32;in&#32;the&#32;subject&#32;have&#32;a&#32;rdfs:label&#32;in&#32;English|

***
### Pass Outcome number 52

[Jump to summary definition](#summary-Pass-52)	|	[Previous Pass outcome](#pass-outcome-number-51)	|	[Next Pass outcome](#pass-outcome-number-53)

:white_check_mark:Pass outcome
#### Subject detail
|Name|module-src-interaction-modelet-manufacturing-environments-discover-behavior-specifications|
|----|----|
|Title|Merged&#32;module&#32;src/interaction.ttl&#32;from&#32;branch&#32;HEAD&#32;with&#32;related&#32;terms&#32;from&#32;the&#32;fragments&#32;domains/manufacturing-environments/discover-behavior-specifications/onto.ttl|
|Composition|- [Modelet manufacturing-environments/discover-behavior-specifications](https://github.com/HyperAgents/hmas/blob/HEAD/domains/manufacturing-environments/discover-behavior-specifications/onto.ttl)<br/>- [Module interaction](https://github.com/HyperAgents/hmas/blob/HEAD/src/interaction.ttl)|

#### Criterion detail
|Identifier|[owl-rl-constraint](https://ns.inria.fr/olivaw#owl-rl-constraint)|
|----|----|
|Title|OWL&#32;RL&#32;Constraint&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;check&#32;wether&#32;the&#32;test&#32;subject&#32;is&#32;syntaxically&#32;correct&#32;or&#32;not.|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-52)|Identifier|`owl-rl-constraint-violation`|
|[Section top](#pass-outcome-number-52)|Title|OWL&#32;RL&#32;consistent|
|[Section top](#pass-outcome-number-52)|Description|The&#32;provided&#32;graph&#32;is&#32;consistent&#32;for&#32;any&#32;OWL&#32;RL&#32;constraint|

***
### Pass Outcome number 53

[Jump to summary definition](#summary-Pass-53)	|	[Previous Pass outcome](#pass-outcome-number-52)	|	[Next Pass outcome](#pass-outcome-number-54)

:white_check_mark:Pass outcome
#### Subject detail
|Name|module-src-interaction-modelet-manufacturing-environments-discover-behavior-specifications|
|----|----|
|Title|Merged&#32;module&#32;src/interaction.ttl&#32;from&#32;branch&#32;HEAD&#32;with&#32;related&#32;terms&#32;from&#32;the&#32;fragments&#32;domains/manufacturing-environments/discover-behavior-specifications/onto.ttl|
|Composition|- [Modelet manufacturing-environments/discover-behavior-specifications](https://github.com/HyperAgents/hmas/blob/HEAD/domains/manufacturing-environments/discover-behavior-specifications/onto.ttl)<br/>- [Module interaction](https://github.com/HyperAgents/hmas/blob/HEAD/src/interaction.ttl)|

#### Criterion detail
|Identifier|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|
|----|----|
|Title|Profile&#32;compatibility&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;check&#32;whether&#32;the&#32;test&#32;subject&#32;is&#32;compatible&#32;with&#32;a&#32;profile&#32;or&#32;not,&#32;and&#32;if&#32;it&#32;is&#32;not,&#32;why.|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-53)|Identifier|`owl-el-profile-error`|
|[Section top](#pass-outcome-number-53)|Title|OWL&#32;EL&#32;Profile&#32;compatible|
|[Section top](#pass-outcome-number-53)|Description|The&#32;subject&#32;is&#32;included&#32;in&#32;the&#32;OWL&#32;EL&#32;sublanguage|

***
### Pass Outcome number 54

[Jump to summary definition](#summary-Pass-54)	|	[Previous Pass outcome](#pass-outcome-number-53)	|	[Next Pass outcome](#pass-outcome-number-55)

:white_check_mark:Pass outcome
#### Subject detail
|Name|module-src-interaction-modelet-manufacturing-environments-discover-behavior-specifications|
|----|----|
|Title|Merged&#32;module&#32;src/interaction.ttl&#32;from&#32;branch&#32;HEAD&#32;with&#32;related&#32;terms&#32;from&#32;the&#32;fragments&#32;domains/manufacturing-environments/discover-behavior-specifications/onto.ttl|
|Composition|- [Modelet manufacturing-environments/discover-behavior-specifications](https://github.com/HyperAgents/hmas/blob/HEAD/domains/manufacturing-environments/discover-behavior-specifications/onto.ttl)<br/>- [Module interaction](https://github.com/HyperAgents/hmas/blob/HEAD/src/interaction.ttl)|

#### Criterion detail
|Identifier|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|
|----|----|
|Title|Profile&#32;compatibility&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;check&#32;whether&#32;the&#32;test&#32;subject&#32;is&#32;compatible&#32;with&#32;a&#32;profile&#32;or&#32;not,&#32;and&#32;if&#32;it&#32;is&#32;not,&#32;why.|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-54)|Identifier|`owl-ql-profile-error`|
|[Section top](#pass-outcome-number-54)|Title|OWL&#32;QL&#32;Profile&#32;compatible|
|[Section top](#pass-outcome-number-54)|Description|The&#32;subject&#32;is&#32;included&#32;in&#32;the&#32;OWL&#32;QL&#32;sublanguage|

***
### Pass Outcome number 55

[Jump to summary definition](#summary-Pass-55)	|	[Previous Pass outcome](#pass-outcome-number-54)	|	[Next Pass outcome](#pass-outcome-number-56)

:white_check_mark:Pass outcome
#### Subject detail
|Name|module-src-interaction-modelet-manufacturing-environments-discover-behavior-specifications|
|----|----|
|Title|Merged&#32;module&#32;src/interaction.ttl&#32;from&#32;branch&#32;HEAD&#32;with&#32;related&#32;terms&#32;from&#32;the&#32;fragments&#32;domains/manufacturing-environments/discover-behavior-specifications/onto.ttl|
|Composition|- [Modelet manufacturing-environments/discover-behavior-specifications](https://github.com/HyperAgents/hmas/blob/HEAD/domains/manufacturing-environments/discover-behavior-specifications/onto.ttl)<br/>- [Module interaction](https://github.com/HyperAgents/hmas/blob/HEAD/src/interaction.ttl)|

#### Criterion detail
|Identifier|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|
|----|----|
|Title|Profile&#32;compatibility&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;check&#32;whether&#32;the&#32;test&#32;subject&#32;is&#32;compatible&#32;with&#32;a&#32;profile&#32;or&#32;not,&#32;and&#32;if&#32;it&#32;is&#32;not,&#32;why.|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-55)|Identifier|`owl-rl-profile-error`|
|[Section top](#pass-outcome-number-55)|Title|OWL&#32;RL&#32;Profile&#32;compatible|
|[Section top](#pass-outcome-number-55)|Description|The&#32;subject&#32;is&#32;included&#32;in&#32;the&#32;OWL&#32;RL&#32;sublanguage|

***
### Pass Outcome number 56

[Jump to summary definition](#summary-Pass-56)	|	[Previous Pass outcome](#pass-outcome-number-55)	|	[Next Pass outcome](#pass-outcome-number-57)

:white_check_mark:Pass outcome
#### Subject detail
|Name|module-src-interaction-modelet-manufacturing-environments-discover-behavior-specifications|
|----|----|
|Title|Merged&#32;module&#32;src/interaction.ttl&#32;from&#32;branch&#32;HEAD&#32;with&#32;related&#32;terms&#32;from&#32;the&#32;fragments&#32;domains/manufacturing-environments/discover-behavior-specifications/onto.ttl|
|Composition|- [Modelet manufacturing-environments/discover-behavior-specifications](https://github.com/HyperAgents/hmas/blob/HEAD/domains/manufacturing-environments/discover-behavior-specifications/onto.ttl)<br/>- [Module interaction](https://github.com/HyperAgents/hmas/blob/HEAD/src/interaction.ttl)|

#### Criterion detail
|Identifier|[proper-extension-predicate](https://ns.inria.fr/olivaw#proper-extension-predicate)|
|----|----|
|Title|Predicate&#32;extension&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;test&#32;the&#32;proper&#32;use&#32;of&#32;predicates&#32;rdfs:subClassOf&#32;and&#32;rdfs:subPropertyOf&#32;on&#32;the&#32;ontology&#32;terms|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-56)|Identifier|`class-subpropertyof`|
|[Section top](#pass-outcome-number-56)|Title|No&#32;class&#32;subproperty|
|[Section top](#pass-outcome-number-56)|Description|No&#32;ontology&#32;class&#32;is&#32;a&#32;subproperty|

***
### Pass Outcome number 57

[Jump to summary definition](#summary-Pass-57)	|	[Previous Pass outcome](#pass-outcome-number-56)	|	[Next Pass outcome](#pass-outcome-number-58)

:white_check_mark:Pass outcome
#### Subject detail
|Name|module-src-interaction-modelet-manufacturing-environments-discover-behavior-specifications|
|----|----|
|Title|Merged&#32;module&#32;src/interaction.ttl&#32;from&#32;branch&#32;HEAD&#32;with&#32;related&#32;terms&#32;from&#32;the&#32;fragments&#32;domains/manufacturing-environments/discover-behavior-specifications/onto.ttl|
|Composition|- [Modelet manufacturing-environments/discover-behavior-specifications](https://github.com/HyperAgents/hmas/blob/HEAD/domains/manufacturing-environments/discover-behavior-specifications/onto.ttl)<br/>- [Module interaction](https://github.com/HyperAgents/hmas/blob/HEAD/src/interaction.ttl)|

#### Criterion detail
|Identifier|[proper-extension-predicate](https://ns.inria.fr/olivaw#proper-extension-predicate)|
|----|----|
|Title|Predicate&#32;extension&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;test&#32;the&#32;proper&#32;use&#32;of&#32;predicates&#32;rdfs:subClassOf&#32;and&#32;rdfs:subPropertyOf&#32;on&#32;the&#32;ontology&#32;terms|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-57)|Identifier|`property-subclassof`|
|[Section top](#pass-outcome-number-57)|Title|No&#32;property&#32;subclass|
|[Section top](#pass-outcome-number-57)|Description|No&#32;ontology&#32;property&#32;is&#32;a&#32;subclass|

***
### Pass Outcome number 58

[Jump to summary definition](#summary-Pass-58)	|	[Previous Pass outcome](#pass-outcome-number-57)	|	[Next Pass outcome](#pass-outcome-number-59)

:white_check_mark:Pass outcome
#### Subject detail
|Name|module-src-interaction-modelet-manufacturing-environments-discover-behavior-specifications|
|----|----|
|Title|Merged&#32;module&#32;src/interaction.ttl&#32;from&#32;branch&#32;HEAD&#32;with&#32;related&#32;terms&#32;from&#32;the&#32;fragments&#32;domains/manufacturing-environments/discover-behavior-specifications/onto.ttl|
|Composition|- [Modelet manufacturing-environments/discover-behavior-specifications](https://github.com/HyperAgents/hmas/blob/HEAD/domains/manufacturing-environments/discover-behavior-specifications/onto.ttl)<br/>- [Module interaction](https://github.com/HyperAgents/hmas/blob/HEAD/src/interaction.ttl)|

#### Criterion detail
|Identifier|[proper-extension-predicate](https://ns.inria.fr/olivaw#proper-extension-predicate)|
|----|----|
|Title|Predicate&#32;extension&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;test&#32;the&#32;proper&#32;use&#32;of&#32;predicates&#32;rdfs:subClassOf&#32;and&#32;rdfs:subPropertyOf&#32;on&#32;the&#32;ontology&#32;terms|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-58)|Identifier|`subclassof-property`|
|[Section top](#pass-outcome-number-58)|Title|No&#32;subclass&#32;of&#32;property|
|[Section top](#pass-outcome-number-58)|Description|No&#32;ontology&#32;term&#32;is&#32;a&#32;subclass&#32;of&#32;a&#32;property|

***
### Pass Outcome number 59

[Jump to summary definition](#summary-Pass-59)	|	[Previous Pass outcome](#pass-outcome-number-58)	|	[Next Pass outcome](#pass-outcome-number-60)

:white_check_mark:Pass outcome
#### Subject detail
|Name|module-src-interaction-modelet-manufacturing-environments-discover-behavior-specifications|
|----|----|
|Title|Merged&#32;module&#32;src/interaction.ttl&#32;from&#32;branch&#32;HEAD&#32;with&#32;related&#32;terms&#32;from&#32;the&#32;fragments&#32;domains/manufacturing-environments/discover-behavior-specifications/onto.ttl|
|Composition|- [Modelet manufacturing-environments/discover-behavior-specifications](https://github.com/HyperAgents/hmas/blob/HEAD/domains/manufacturing-environments/discover-behavior-specifications/onto.ttl)<br/>- [Module interaction](https://github.com/HyperAgents/hmas/blob/HEAD/src/interaction.ttl)|

#### Criterion detail
|Identifier|[proper-extension-predicate](https://ns.inria.fr/olivaw#proper-extension-predicate)|
|----|----|
|Title|Predicate&#32;extension&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;test&#32;the&#32;proper&#32;use&#32;of&#32;predicates&#32;rdfs:subClassOf&#32;and&#32;rdfs:subPropertyOf&#32;on&#32;the&#32;ontology&#32;terms|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-59)|Identifier|`subpropertyof-class`|
|[Section top](#pass-outcome-number-59)|Title|No&#32;subproperty&#32;of&#32;class|
|[Section top](#pass-outcome-number-59)|Description|No&#32;ontology&#32;term&#32;is&#32;a&#32;subproperty&#32;of&#32;a&#32;class|

***
### Pass Outcome number 60

[Jump to summary definition](#summary-Pass-60)	|	[Previous Pass outcome](#pass-outcome-number-59)	|	[Next Pass outcome](#pass-outcome-number-61)

:white_check_mark:Pass outcome
#### Subject detail
|Name|module-src-interaction-modelet-manufacturing-environments-discover-behavior-specifications|
|----|----|
|Title|Merged&#32;module&#32;src/interaction.ttl&#32;from&#32;branch&#32;HEAD&#32;with&#32;related&#32;terms&#32;from&#32;the&#32;fragments&#32;domains/manufacturing-environments/discover-behavior-specifications/onto.ttl|
|Composition|- [Modelet manufacturing-environments/discover-behavior-specifications](https://github.com/HyperAgents/hmas/blob/HEAD/domains/manufacturing-environments/discover-behavior-specifications/onto.ttl)<br/>- [Module interaction](https://github.com/HyperAgents/hmas/blob/HEAD/src/interaction.ttl)|

#### Criterion detail
|Identifier|[term-referencing](https://ns.inria.fr/olivaw#term-referencing)|
|----|----|
|Title|Term&#32;referencing&#32;test|
|Description|A&#32;test&#32;case&#32;from&#32;the&#32;Best&#32;Practices&#32;tests&#32;checking&#32;if&#32;each&#32;term&#32;of&#32;the&#32;test&#32;subject&#32;is&#32;referenced&#32;to&#32;a&#32;module&#32;through&#32;a&#32;rdfs:isDefinedBy&#32;property.|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-60)|Identifier|`no-reference-module`|
|[Section top](#pass-outcome-number-60)|Title|Any&#32;term&#32;is&#32;referenced|
|[Section top](#pass-outcome-number-60)|Description|Each&#32;term&#32;of&#32;the&#32;test&#32;subject&#32;is&#32;linked&#32;to&#32;a&#32;module&#32;by&#32;a&#32;rdfs:isDefinedBy&#32;property|

***
### Pass Outcome number 61

[Jump to summary definition](#summary-Pass-61)	|	[Previous Pass outcome](#pass-outcome-number-60)	|	[Next Pass outcome](#pass-outcome-number-62)

:white_check_mark:Pass outcome
#### Subject detail
|Name|module-src-interaction-modelet-manufacturing-environments-discover-behavior-specifications|
|----|----|
|Title|Merged&#32;module&#32;src/interaction.ttl&#32;from&#32;branch&#32;HEAD&#32;with&#32;related&#32;terms&#32;from&#32;the&#32;fragments&#32;domains/manufacturing-environments/discover-behavior-specifications/onto.ttl|
|Composition|- [Modelet manufacturing-environments/discover-behavior-specifications](https://github.com/HyperAgents/hmas/blob/HEAD/domains/manufacturing-environments/discover-behavior-specifications/onto.ttl)<br/>- [Module interaction](https://github.com/HyperAgents/hmas/blob/HEAD/src/interaction.ttl)|

#### Criterion detail
|Identifier|[terms-differenciation](https://ns.inria.fr/olivaw#terms-differenciation)|
|----|----|
|Title|Terms&#32;differenciation&#32;test|
|Description|A&#32;test&#32;case&#32;from&#32;the&#32;Best&#32;Practices&#32;tests&#32;checking&#32;if&#32;all&#32;the&#32;terms&#32;are&#32;different&#32;enough&#32;from&#32;each&#32;other&#32;according&#32;to&#32;the&#32;Levenshtein&#32;distance&#32;metric.|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-61)|Identifier|`too-close-terms`|
|[Section top](#pass-outcome-number-61)|Title|Terms&#32;differenciated&#32;enough|
|[Section top](#pass-outcome-number-61)|Description|All&#32;the&#32;terms&#32;have&#32;have&#32;a&#32;satisfying&#32;Levenshtein&#32;distance&#32;from&#32;each&#32;other&#32;term.|

***
### Pass Outcome number 62

[Jump to summary definition](#summary-Pass-62)	|	[Previous Pass outcome](#pass-outcome-number-61)	|	[Next Pass outcome](#pass-outcome-number-63)

:white_check_mark:Pass outcome
#### Subject detail
|Name|module-src-interaction|
|----|----|
|Title|Standalone&#32;module&#32;src/interaction.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Module interaction](https://github.com/HyperAgents/hmas/blob/HEAD/src/interaction.ttl)|

#### Criterion detail
|Identifier|[domain-and-range-referencing](https://ns.inria.fr/olivaw#domain-and-range-referencing)|
|----|----|
|Title|Domain&#32;and&#32;range&#32;referencing&#32;test|
|Description|A&#32;test&#32;case&#32;from&#32;the&#32;Best&#32;Practices&#32;tests&#32;checking&#32;if&#32;all&#32;the&#32;ranges&#32;and&#32;domains&#32;from&#32;the&#32;test&#32;subject&#32;point&#32;to&#32;terms&#32;that&#32;are&#32;defined&#32;in&#32;the&#32;vocabulary.|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-62)|Identifier|`domain-out-of-vocabulary`|
|[Section top](#pass-outcome-number-62)|Title|Domains&#32;properly&#32;defined|
|[Section top](#pass-outcome-number-62)|Description|Each&#32;rdfs:domain&#32;is&#32;defined&#32;within&#32;the&#32;fragment|

***
### Pass Outcome number 63

[Jump to summary definition](#summary-Pass-63)	|	[Previous Pass outcome](#pass-outcome-number-62)	|	[Next Pass outcome](#pass-outcome-number-64)

:white_check_mark:Pass outcome
#### Subject detail
|Name|module-src-interaction|
|----|----|
|Title|Standalone&#32;module&#32;src/interaction.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Module interaction](https://github.com/HyperAgents/hmas/blob/HEAD/src/interaction.ttl)|

#### Criterion detail
|Identifier|[domain-and-range-referencing](https://ns.inria.fr/olivaw#domain-and-range-referencing)|
|----|----|
|Title|Domain&#32;and&#32;range&#32;referencing&#32;test|
|Description|A&#32;test&#32;case&#32;from&#32;the&#32;Best&#32;Practices&#32;tests&#32;checking&#32;if&#32;all&#32;the&#32;ranges&#32;and&#32;domains&#32;from&#32;the&#32;test&#32;subject&#32;point&#32;to&#32;terms&#32;that&#32;are&#32;defined&#32;in&#32;the&#32;vocabulary.|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-63)|Identifier|`range-out-of-vocabulary`|
|[Section top](#pass-outcome-number-63)|Title|Ranges&#32;properly&#32;defined|
|[Section top](#pass-outcome-number-63)|Description|Each&#32;rdfs:range&#32;is&#32;defined&#32;within&#32;the&#32;fragment|

***
### Pass Outcome number 64

[Jump to summary definition](#summary-Pass-64)	|	[Previous Pass outcome](#pass-outcome-number-63)	|	[Next Pass outcome](#pass-outcome-number-65)

:white_check_mark:Pass outcome
#### Subject detail
|Name|module-src-interaction|
|----|----|
|Title|Standalone&#32;module&#32;src/interaction.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Module interaction](https://github.com/HyperAgents/hmas/blob/HEAD/src/interaction.ttl)|

#### Criterion detail
|Identifier|[labeled-terms](https://ns.inria.fr/olivaw#labeled-terms)|
|----|----|
|Title|Term&#32;labeling&#32;test|
|Description|A&#32;test&#32;case&#32;from&#32;the&#32;Best&#32;Practices&#32;tests&#32;checking&#32;if&#32;all&#32;the&#32;terms&#32;of&#32;the&#32;subject&#32;have&#32;a&#32;rdfs:label&#32;property&#32;pointing&#32;to&#32;a&#32;literal&#32;in&#32;English|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-64)|Identifier|`not-labeled-term`|
|[Section top](#pass-outcome-number-64)|Title|All&#32;terms&#32;labeled|
|[Section top](#pass-outcome-number-64)|Description|All&#32;the&#32;terms&#32;defined&#32;in&#32;the&#32;subject&#32;have&#32;a&#32;rdfs:label&#32;in&#32;English|

***
### Pass Outcome number 65

[Jump to summary definition](#summary-Pass-65)	|	[Previous Pass outcome](#pass-outcome-number-64)	|	[Next Pass outcome](#pass-outcome-number-66)

:white_check_mark:Pass outcome
#### Subject detail
|Name|module-src-interaction|
|----|----|
|Title|Standalone&#32;module&#32;src/interaction.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Module interaction](https://github.com/HyperAgents/hmas/blob/HEAD/src/interaction.ttl)|

#### Criterion detail
|Identifier|[owl-rl-constraint](https://ns.inria.fr/olivaw#owl-rl-constraint)|
|----|----|
|Title|OWL&#32;RL&#32;Constraint&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;check&#32;wether&#32;the&#32;test&#32;subject&#32;is&#32;syntaxically&#32;correct&#32;or&#32;not.|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-65)|Identifier|`owl-rl-constraint-violation`|
|[Section top](#pass-outcome-number-65)|Title|OWL&#32;RL&#32;consistent|
|[Section top](#pass-outcome-number-65)|Description|The&#32;provided&#32;graph&#32;is&#32;consistent&#32;for&#32;any&#32;OWL&#32;RL&#32;constraint|

***
### Pass Outcome number 66

[Jump to summary definition](#summary-Pass-66)	|	[Previous Pass outcome](#pass-outcome-number-65)	|	[Next Pass outcome](#pass-outcome-number-67)

:white_check_mark:Pass outcome
#### Subject detail
|Name|module-src-interaction|
|----|----|
|Title|Standalone&#32;module&#32;src/interaction.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Module interaction](https://github.com/HyperAgents/hmas/blob/HEAD/src/interaction.ttl)|

#### Criterion detail
|Identifier|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|
|----|----|
|Title|Profile&#32;compatibility&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;check&#32;whether&#32;the&#32;test&#32;subject&#32;is&#32;compatible&#32;with&#32;a&#32;profile&#32;or&#32;not,&#32;and&#32;if&#32;it&#32;is&#32;not,&#32;why.|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-66)|Identifier|`owl-el-profile-error`|
|[Section top](#pass-outcome-number-66)|Title|OWL&#32;EL&#32;Profile&#32;compatible|
|[Section top](#pass-outcome-number-66)|Description|The&#32;subject&#32;is&#32;included&#32;in&#32;the&#32;OWL&#32;EL&#32;sublanguage|

***
### Pass Outcome number 67

[Jump to summary definition](#summary-Pass-67)	|	[Previous Pass outcome](#pass-outcome-number-66)	|	[Next Pass outcome](#pass-outcome-number-68)

:white_check_mark:Pass outcome
#### Subject detail
|Name|module-src-interaction|
|----|----|
|Title|Standalone&#32;module&#32;src/interaction.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Module interaction](https://github.com/HyperAgents/hmas/blob/HEAD/src/interaction.ttl)|

#### Criterion detail
|Identifier|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|
|----|----|
|Title|Profile&#32;compatibility&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;check&#32;whether&#32;the&#32;test&#32;subject&#32;is&#32;compatible&#32;with&#32;a&#32;profile&#32;or&#32;not,&#32;and&#32;if&#32;it&#32;is&#32;not,&#32;why.|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-67)|Identifier|`owl-ql-profile-error`|
|[Section top](#pass-outcome-number-67)|Title|OWL&#32;QL&#32;Profile&#32;compatible|
|[Section top](#pass-outcome-number-67)|Description|The&#32;subject&#32;is&#32;included&#32;in&#32;the&#32;OWL&#32;QL&#32;sublanguage|

***
### Pass Outcome number 68

[Jump to summary definition](#summary-Pass-68)	|	[Previous Pass outcome](#pass-outcome-number-67)	|	[Next Pass outcome](#pass-outcome-number-69)

:white_check_mark:Pass outcome
#### Subject detail
|Name|module-src-interaction|
|----|----|
|Title|Standalone&#32;module&#32;src/interaction.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Module interaction](https://github.com/HyperAgents/hmas/blob/HEAD/src/interaction.ttl)|

#### Criterion detail
|Identifier|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|
|----|----|
|Title|Profile&#32;compatibility&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;check&#32;whether&#32;the&#32;test&#32;subject&#32;is&#32;compatible&#32;with&#32;a&#32;profile&#32;or&#32;not,&#32;and&#32;if&#32;it&#32;is&#32;not,&#32;why.|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-68)|Identifier|`owl-rl-profile-error`|
|[Section top](#pass-outcome-number-68)|Title|OWL&#32;RL&#32;Profile&#32;compatible|
|[Section top](#pass-outcome-number-68)|Description|The&#32;subject&#32;is&#32;included&#32;in&#32;the&#32;OWL&#32;RL&#32;sublanguage|

***
### Pass Outcome number 69

[Jump to summary definition](#summary-Pass-69)	|	[Previous Pass outcome](#pass-outcome-number-68)	|	[Next Pass outcome](#pass-outcome-number-70)

:white_check_mark:Pass outcome
#### Subject detail
|Name|module-src-interaction|
|----|----|
|Title|Standalone&#32;module&#32;src/interaction.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Module interaction](https://github.com/HyperAgents/hmas/blob/HEAD/src/interaction.ttl)|

#### Criterion detail
|Identifier|[proper-extension-predicate](https://ns.inria.fr/olivaw#proper-extension-predicate)|
|----|----|
|Title|Predicate&#32;extension&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;test&#32;the&#32;proper&#32;use&#32;of&#32;predicates&#32;rdfs:subClassOf&#32;and&#32;rdfs:subPropertyOf&#32;on&#32;the&#32;ontology&#32;terms|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-69)|Identifier|`class-subpropertyof`|
|[Section top](#pass-outcome-number-69)|Title|No&#32;class&#32;subproperty|
|[Section top](#pass-outcome-number-69)|Description|No&#32;ontology&#32;class&#32;is&#32;a&#32;subproperty|

***
### Pass Outcome number 70

[Jump to summary definition](#summary-Pass-70)	|	[Previous Pass outcome](#pass-outcome-number-69)	|	[Next Pass outcome](#pass-outcome-number-71)

:white_check_mark:Pass outcome
#### Subject detail
|Name|module-src-interaction|
|----|----|
|Title|Standalone&#32;module&#32;src/interaction.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Module interaction](https://github.com/HyperAgents/hmas/blob/HEAD/src/interaction.ttl)|

#### Criterion detail
|Identifier|[proper-extension-predicate](https://ns.inria.fr/olivaw#proper-extension-predicate)|
|----|----|
|Title|Predicate&#32;extension&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;test&#32;the&#32;proper&#32;use&#32;of&#32;predicates&#32;rdfs:subClassOf&#32;and&#32;rdfs:subPropertyOf&#32;on&#32;the&#32;ontology&#32;terms|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-70)|Identifier|`property-subclassof`|
|[Section top](#pass-outcome-number-70)|Title|No&#32;property&#32;subclass|
|[Section top](#pass-outcome-number-70)|Description|No&#32;ontology&#32;property&#32;is&#32;a&#32;subclass|

***
### Pass Outcome number 71

[Jump to summary definition](#summary-Pass-71)	|	[Previous Pass outcome](#pass-outcome-number-70)	|	[Next Pass outcome](#pass-outcome-number-72)

:white_check_mark:Pass outcome
#### Subject detail
|Name|module-src-interaction|
|----|----|
|Title|Standalone&#32;module&#32;src/interaction.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Module interaction](https://github.com/HyperAgents/hmas/blob/HEAD/src/interaction.ttl)|

#### Criterion detail
|Identifier|[proper-extension-predicate](https://ns.inria.fr/olivaw#proper-extension-predicate)|
|----|----|
|Title|Predicate&#32;extension&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;test&#32;the&#32;proper&#32;use&#32;of&#32;predicates&#32;rdfs:subClassOf&#32;and&#32;rdfs:subPropertyOf&#32;on&#32;the&#32;ontology&#32;terms|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-71)|Identifier|`subclassof-property`|
|[Section top](#pass-outcome-number-71)|Title|No&#32;subclass&#32;of&#32;property|
|[Section top](#pass-outcome-number-71)|Description|No&#32;ontology&#32;term&#32;is&#32;a&#32;subclass&#32;of&#32;a&#32;property|

***
### Pass Outcome number 72

[Jump to summary definition](#summary-Pass-72)	|	[Previous Pass outcome](#pass-outcome-number-71)	|	[Next Pass outcome](#pass-outcome-number-73)

:white_check_mark:Pass outcome
#### Subject detail
|Name|module-src-interaction|
|----|----|
|Title|Standalone&#32;module&#32;src/interaction.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Module interaction](https://github.com/HyperAgents/hmas/blob/HEAD/src/interaction.ttl)|

#### Criterion detail
|Identifier|[proper-extension-predicate](https://ns.inria.fr/olivaw#proper-extension-predicate)|
|----|----|
|Title|Predicate&#32;extension&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;test&#32;the&#32;proper&#32;use&#32;of&#32;predicates&#32;rdfs:subClassOf&#32;and&#32;rdfs:subPropertyOf&#32;on&#32;the&#32;ontology&#32;terms|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-72)|Identifier|`subpropertyof-class`|
|[Section top](#pass-outcome-number-72)|Title|No&#32;subproperty&#32;of&#32;class|
|[Section top](#pass-outcome-number-72)|Description|No&#32;ontology&#32;term&#32;is&#32;a&#32;subproperty&#32;of&#32;a&#32;class|

***
### Pass Outcome number 73

[Jump to summary definition](#summary-Pass-73)	|	[Previous Pass outcome](#pass-outcome-number-72)	|	[Next Pass outcome](#pass-outcome-number-74)

:white_check_mark:Pass outcome
#### Subject detail
|Name|module-src-interaction|
|----|----|
|Title|Standalone&#32;module&#32;src/interaction.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Module interaction](https://github.com/HyperAgents/hmas/blob/HEAD/src/interaction.ttl)|

#### Criterion detail
|Identifier|[term-referencing](https://ns.inria.fr/olivaw#term-referencing)|
|----|----|
|Title|Term&#32;referencing&#32;test|
|Description|A&#32;test&#32;case&#32;from&#32;the&#32;Best&#32;Practices&#32;tests&#32;checking&#32;if&#32;each&#32;term&#32;of&#32;the&#32;test&#32;subject&#32;is&#32;referenced&#32;to&#32;a&#32;module&#32;through&#32;a&#32;rdfs:isDefinedBy&#32;property.|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-73)|Identifier|`no-reference-module`|
|[Section top](#pass-outcome-number-73)|Title|Any&#32;term&#32;is&#32;referenced|
|[Section top](#pass-outcome-number-73)|Description|Each&#32;term&#32;of&#32;the&#32;test&#32;subject&#32;is&#32;linked&#32;to&#32;a&#32;module&#32;by&#32;a&#32;rdfs:isDefinedBy&#32;property|

***
### Pass Outcome number 74

[Jump to summary definition](#summary-Pass-74)	|	[Previous Pass outcome](#pass-outcome-number-73)	|	[Next Pass outcome](#pass-outcome-number-75)

:white_check_mark:Pass outcome
#### Subject detail
|Name|module-src-interaction|
|----|----|
|Title|Standalone&#32;module&#32;src/interaction.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Module interaction](https://github.com/HyperAgents/hmas/blob/HEAD/src/interaction.ttl)|

#### Criterion detail
|Identifier|[terms-differenciation](https://ns.inria.fr/olivaw#terms-differenciation)|
|----|----|
|Title|Terms&#32;differenciation&#32;test|
|Description|A&#32;test&#32;case&#32;from&#32;the&#32;Best&#32;Practices&#32;tests&#32;checking&#32;if&#32;all&#32;the&#32;terms&#32;are&#32;different&#32;enough&#32;from&#32;each&#32;other&#32;according&#32;to&#32;the&#32;Levenshtein&#32;distance&#32;metric.|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-74)|Identifier|`too-close-terms`|
|[Section top](#pass-outcome-number-74)|Title|Terms&#32;differenciated&#32;enough|
|[Section top](#pass-outcome-number-74)|Description|All&#32;the&#32;terms&#32;have&#32;have&#32;a&#32;satisfying&#32;Levenshtein&#32;distance&#32;from&#32;each&#32;other&#32;term.|

***
### Pass Outcome number 75

[Jump to summary definition](#summary-Pass-75)	|	[Previous Pass outcome](#pass-outcome-number-74)	|	[Next Pass outcome](#pass-outcome-number-76)

:white_check_mark:Pass outcome
#### Subject detail
|Name|module-src-fipa|
|----|----|
|Title|Standalone&#32;module&#32;src/fipa.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Module fipa](https://github.com/HyperAgents/hmas/blob/HEAD/src/fipa.ttl)|

#### Criterion detail
|Identifier|[domain-and-range-referencing](https://ns.inria.fr/olivaw#domain-and-range-referencing)|
|----|----|
|Title|Domain&#32;and&#32;range&#32;referencing&#32;test|
|Description|A&#32;test&#32;case&#32;from&#32;the&#32;Best&#32;Practices&#32;tests&#32;checking&#32;if&#32;all&#32;the&#32;ranges&#32;and&#32;domains&#32;from&#32;the&#32;test&#32;subject&#32;point&#32;to&#32;terms&#32;that&#32;are&#32;defined&#32;in&#32;the&#32;vocabulary.|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-75)|Identifier|`domain-out-of-vocabulary`|
|[Section top](#pass-outcome-number-75)|Title|Domains&#32;properly&#32;defined|
|[Section top](#pass-outcome-number-75)|Description|Each&#32;rdfs:domain&#32;is&#32;defined&#32;within&#32;the&#32;fragment|

***
### Pass Outcome number 76

[Jump to summary definition](#summary-Pass-76)	|	[Previous Pass outcome](#pass-outcome-number-75)	|	[Next Pass outcome](#pass-outcome-number-77)

:white_check_mark:Pass outcome
#### Subject detail
|Name|module-src-fipa|
|----|----|
|Title|Standalone&#32;module&#32;src/fipa.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Module fipa](https://github.com/HyperAgents/hmas/blob/HEAD/src/fipa.ttl)|

#### Criterion detail
|Identifier|[domain-and-range-referencing](https://ns.inria.fr/olivaw#domain-and-range-referencing)|
|----|----|
|Title|Domain&#32;and&#32;range&#32;referencing&#32;test|
|Description|A&#32;test&#32;case&#32;from&#32;the&#32;Best&#32;Practices&#32;tests&#32;checking&#32;if&#32;all&#32;the&#32;ranges&#32;and&#32;domains&#32;from&#32;the&#32;test&#32;subject&#32;point&#32;to&#32;terms&#32;that&#32;are&#32;defined&#32;in&#32;the&#32;vocabulary.|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-76)|Identifier|`range-out-of-vocabulary`|
|[Section top](#pass-outcome-number-76)|Title|Ranges&#32;properly&#32;defined|
|[Section top](#pass-outcome-number-76)|Description|Each&#32;rdfs:range&#32;is&#32;defined&#32;within&#32;the&#32;fragment|

***
### Pass Outcome number 77

[Jump to summary definition](#summary-Pass-77)	|	[Previous Pass outcome](#pass-outcome-number-76)	|	[Next Pass outcome](#pass-outcome-number-78)

:white_check_mark:Pass outcome
#### Subject detail
|Name|module-src-fipa|
|----|----|
|Title|Standalone&#32;module&#32;src/fipa.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Module fipa](https://github.com/HyperAgents/hmas/blob/HEAD/src/fipa.ttl)|

#### Criterion detail
|Identifier|[labeled-terms](https://ns.inria.fr/olivaw#labeled-terms)|
|----|----|
|Title|Term&#32;labeling&#32;test|
|Description|A&#32;test&#32;case&#32;from&#32;the&#32;Best&#32;Practices&#32;tests&#32;checking&#32;if&#32;all&#32;the&#32;terms&#32;of&#32;the&#32;subject&#32;have&#32;a&#32;rdfs:label&#32;property&#32;pointing&#32;to&#32;a&#32;literal&#32;in&#32;English|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-77)|Identifier|`not-labeled-term`|
|[Section top](#pass-outcome-number-77)|Title|All&#32;terms&#32;labeled|
|[Section top](#pass-outcome-number-77)|Description|All&#32;the&#32;terms&#32;defined&#32;in&#32;the&#32;subject&#32;have&#32;a&#32;rdfs:label&#32;in&#32;English|

***
### Pass Outcome number 78

[Jump to summary definition](#summary-Pass-78)	|	[Previous Pass outcome](#pass-outcome-number-77)	|	[Next Pass outcome](#pass-outcome-number-79)

:white_check_mark:Pass outcome
#### Subject detail
|Name|module-src-fipa|
|----|----|
|Title|Standalone&#32;module&#32;src/fipa.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Module fipa](https://github.com/HyperAgents/hmas/blob/HEAD/src/fipa.ttl)|

#### Criterion detail
|Identifier|[owl-rl-constraint](https://ns.inria.fr/olivaw#owl-rl-constraint)|
|----|----|
|Title|OWL&#32;RL&#32;Constraint&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;check&#32;wether&#32;the&#32;test&#32;subject&#32;is&#32;syntaxically&#32;correct&#32;or&#32;not.|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-78)|Identifier|`owl-rl-constraint-violation`|
|[Section top](#pass-outcome-number-78)|Title|OWL&#32;RL&#32;consistent|
|[Section top](#pass-outcome-number-78)|Description|The&#32;provided&#32;graph&#32;is&#32;consistent&#32;for&#32;any&#32;OWL&#32;RL&#32;constraint|

***
### Pass Outcome number 79

[Jump to summary definition](#summary-Pass-79)	|	[Previous Pass outcome](#pass-outcome-number-78)	|	[Next Pass outcome](#pass-outcome-number-80)

:white_check_mark:Pass outcome
#### Subject detail
|Name|module-src-fipa|
|----|----|
|Title|Standalone&#32;module&#32;src/fipa.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Module fipa](https://github.com/HyperAgents/hmas/blob/HEAD/src/fipa.ttl)|

#### Criterion detail
|Identifier|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|
|----|----|
|Title|Profile&#32;compatibility&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;check&#32;whether&#32;the&#32;test&#32;subject&#32;is&#32;compatible&#32;with&#32;a&#32;profile&#32;or&#32;not,&#32;and&#32;if&#32;it&#32;is&#32;not,&#32;why.|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-79)|Identifier|`owl-el-profile-error`|
|[Section top](#pass-outcome-number-79)|Title|OWL&#32;EL&#32;Profile&#32;compatible|
|[Section top](#pass-outcome-number-79)|Description|The&#32;subject&#32;is&#32;included&#32;in&#32;the&#32;OWL&#32;EL&#32;sublanguage|

***
### Pass Outcome number 80

[Jump to summary definition](#summary-Pass-80)	|	[Previous Pass outcome](#pass-outcome-number-79)	|	[Next Pass outcome](#pass-outcome-number-81)

:white_check_mark:Pass outcome
#### Subject detail
|Name|module-src-fipa|
|----|----|
|Title|Standalone&#32;module&#32;src/fipa.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Module fipa](https://github.com/HyperAgents/hmas/blob/HEAD/src/fipa.ttl)|

#### Criterion detail
|Identifier|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|
|----|----|
|Title|Profile&#32;compatibility&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;check&#32;whether&#32;the&#32;test&#32;subject&#32;is&#32;compatible&#32;with&#32;a&#32;profile&#32;or&#32;not,&#32;and&#32;if&#32;it&#32;is&#32;not,&#32;why.|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-80)|Identifier|`owl-ql-profile-error`|
|[Section top](#pass-outcome-number-80)|Title|OWL&#32;QL&#32;Profile&#32;compatible|
|[Section top](#pass-outcome-number-80)|Description|The&#32;subject&#32;is&#32;included&#32;in&#32;the&#32;OWL&#32;QL&#32;sublanguage|

***
### Pass Outcome number 81

[Jump to summary definition](#summary-Pass-81)	|	[Previous Pass outcome](#pass-outcome-number-80)	|	[Next Pass outcome](#pass-outcome-number-82)

:white_check_mark:Pass outcome
#### Subject detail
|Name|module-src-fipa|
|----|----|
|Title|Standalone&#32;module&#32;src/fipa.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Module fipa](https://github.com/HyperAgents/hmas/blob/HEAD/src/fipa.ttl)|

#### Criterion detail
|Identifier|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|
|----|----|
|Title|Profile&#32;compatibility&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;check&#32;whether&#32;the&#32;test&#32;subject&#32;is&#32;compatible&#32;with&#32;a&#32;profile&#32;or&#32;not,&#32;and&#32;if&#32;it&#32;is&#32;not,&#32;why.|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-81)|Identifier|`owl-rl-profile-error`|
|[Section top](#pass-outcome-number-81)|Title|OWL&#32;RL&#32;Profile&#32;compatible|
|[Section top](#pass-outcome-number-81)|Description|The&#32;subject&#32;is&#32;included&#32;in&#32;the&#32;OWL&#32;RL&#32;sublanguage|

***
### Pass Outcome number 82

[Jump to summary definition](#summary-Pass-82)	|	[Previous Pass outcome](#pass-outcome-number-81)	|	[Next Pass outcome](#pass-outcome-number-83)

:white_check_mark:Pass outcome
#### Subject detail
|Name|module-src-fipa|
|----|----|
|Title|Standalone&#32;module&#32;src/fipa.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Module fipa](https://github.com/HyperAgents/hmas/blob/HEAD/src/fipa.ttl)|

#### Criterion detail
|Identifier|[proper-extension-predicate](https://ns.inria.fr/olivaw#proper-extension-predicate)|
|----|----|
|Title|Predicate&#32;extension&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;test&#32;the&#32;proper&#32;use&#32;of&#32;predicates&#32;rdfs:subClassOf&#32;and&#32;rdfs:subPropertyOf&#32;on&#32;the&#32;ontology&#32;terms|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-82)|Identifier|`class-subpropertyof`|
|[Section top](#pass-outcome-number-82)|Title|No&#32;class&#32;subproperty|
|[Section top](#pass-outcome-number-82)|Description|No&#32;ontology&#32;class&#32;is&#32;a&#32;subproperty|

***
### Pass Outcome number 83

[Jump to summary definition](#summary-Pass-83)	|	[Previous Pass outcome](#pass-outcome-number-82)	|	[Next Pass outcome](#pass-outcome-number-84)

:white_check_mark:Pass outcome
#### Subject detail
|Name|module-src-fipa|
|----|----|
|Title|Standalone&#32;module&#32;src/fipa.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Module fipa](https://github.com/HyperAgents/hmas/blob/HEAD/src/fipa.ttl)|

#### Criterion detail
|Identifier|[proper-extension-predicate](https://ns.inria.fr/olivaw#proper-extension-predicate)|
|----|----|
|Title|Predicate&#32;extension&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;test&#32;the&#32;proper&#32;use&#32;of&#32;predicates&#32;rdfs:subClassOf&#32;and&#32;rdfs:subPropertyOf&#32;on&#32;the&#32;ontology&#32;terms|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-83)|Identifier|`property-subclassof`|
|[Section top](#pass-outcome-number-83)|Title|No&#32;property&#32;subclass|
|[Section top](#pass-outcome-number-83)|Description|No&#32;ontology&#32;property&#32;is&#32;a&#32;subclass|

***
### Pass Outcome number 84

[Jump to summary definition](#summary-Pass-84)	|	[Previous Pass outcome](#pass-outcome-number-83)	|	[Next Pass outcome](#pass-outcome-number-85)

:white_check_mark:Pass outcome
#### Subject detail
|Name|module-src-fipa|
|----|----|
|Title|Standalone&#32;module&#32;src/fipa.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Module fipa](https://github.com/HyperAgents/hmas/blob/HEAD/src/fipa.ttl)|

#### Criterion detail
|Identifier|[proper-extension-predicate](https://ns.inria.fr/olivaw#proper-extension-predicate)|
|----|----|
|Title|Predicate&#32;extension&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;test&#32;the&#32;proper&#32;use&#32;of&#32;predicates&#32;rdfs:subClassOf&#32;and&#32;rdfs:subPropertyOf&#32;on&#32;the&#32;ontology&#32;terms|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-84)|Identifier|`subclassof-property`|
|[Section top](#pass-outcome-number-84)|Title|No&#32;subclass&#32;of&#32;property|
|[Section top](#pass-outcome-number-84)|Description|No&#32;ontology&#32;term&#32;is&#32;a&#32;subclass&#32;of&#32;a&#32;property|

***
### Pass Outcome number 85

[Jump to summary definition](#summary-Pass-85)	|	[Previous Pass outcome](#pass-outcome-number-84)	|	[Next Pass outcome](#pass-outcome-number-86)

:white_check_mark:Pass outcome
#### Subject detail
|Name|module-src-fipa|
|----|----|
|Title|Standalone&#32;module&#32;src/fipa.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Module fipa](https://github.com/HyperAgents/hmas/blob/HEAD/src/fipa.ttl)|

#### Criterion detail
|Identifier|[proper-extension-predicate](https://ns.inria.fr/olivaw#proper-extension-predicate)|
|----|----|
|Title|Predicate&#32;extension&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;test&#32;the&#32;proper&#32;use&#32;of&#32;predicates&#32;rdfs:subClassOf&#32;and&#32;rdfs:subPropertyOf&#32;on&#32;the&#32;ontology&#32;terms|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-85)|Identifier|`subpropertyof-class`|
|[Section top](#pass-outcome-number-85)|Title|No&#32;subproperty&#32;of&#32;class|
|[Section top](#pass-outcome-number-85)|Description|No&#32;ontology&#32;term&#32;is&#32;a&#32;subproperty&#32;of&#32;a&#32;class|

***
### Pass Outcome number 86

[Jump to summary definition](#summary-Pass-86)	|	[Previous Pass outcome](#pass-outcome-number-85)	|	[Next Pass outcome](#pass-outcome-number-87)

:white_check_mark:Pass outcome
#### Subject detail
|Name|module-src-fipa|
|----|----|
|Title|Standalone&#32;module&#32;src/fipa.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Module fipa](https://github.com/HyperAgents/hmas/blob/HEAD/src/fipa.ttl)|

#### Criterion detail
|Identifier|[terms-differenciation](https://ns.inria.fr/olivaw#terms-differenciation)|
|----|----|
|Title|Terms&#32;differenciation&#32;test|
|Description|A&#32;test&#32;case&#32;from&#32;the&#32;Best&#32;Practices&#32;tests&#32;checking&#32;if&#32;all&#32;the&#32;terms&#32;are&#32;different&#32;enough&#32;from&#32;each&#32;other&#32;according&#32;to&#32;the&#32;Levenshtein&#32;distance&#32;metric.|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-86)|Identifier|`too-close-terms`|
|[Section top](#pass-outcome-number-86)|Title|Terms&#32;differenciated&#32;enough|
|[Section top](#pass-outcome-number-86)|Description|All&#32;the&#32;terms&#32;have&#32;have&#32;a&#32;satisfying&#32;Levenshtein&#32;distance&#32;from&#32;each&#32;other&#32;term.|

***
### Pass Outcome number 87

[Jump to summary definition](#summary-Pass-87)	|	[Previous Pass outcome](#pass-outcome-number-86)	|	[Next Pass outcome](#pass-outcome-number-88)

:white_check_mark:Pass outcome
#### Subject detail
|Name|module-src-core-modelet-manufacturing-environments-discover-signifiers|
|----|----|
|Title|Merged&#32;module&#32;src/core.ttl&#32;from&#32;branch&#32;HEAD&#32;with&#32;related&#32;terms&#32;from&#32;the&#32;fragments&#32;domains/manufacturing-environments/discover-signifiers/onto.ttl|
|Composition|- [Modelet manufacturing-environments/discover-signifiers](https://github.com/HyperAgents/hmas/blob/HEAD/domains/manufacturing-environments/discover-signifiers/onto.ttl)<br/>- [Module core](https://github.com/HyperAgents/hmas/blob/HEAD/src/core.ttl)|

#### Criterion detail
|Identifier|[domain-and-range-referencing](https://ns.inria.fr/olivaw#domain-and-range-referencing)|
|----|----|
|Title|Domain&#32;and&#32;range&#32;referencing&#32;test|
|Description|A&#32;test&#32;case&#32;from&#32;the&#32;Best&#32;Practices&#32;tests&#32;checking&#32;if&#32;all&#32;the&#32;ranges&#32;and&#32;domains&#32;from&#32;the&#32;test&#32;subject&#32;point&#32;to&#32;terms&#32;that&#32;are&#32;defined&#32;in&#32;the&#32;vocabulary.|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-87)|Identifier|`domain-out-of-vocabulary`|
|[Section top](#pass-outcome-number-87)|Title|Domains&#32;properly&#32;defined|
|[Section top](#pass-outcome-number-87)|Description|Each&#32;rdfs:domain&#32;is&#32;defined&#32;within&#32;the&#32;fragment|

***
### Pass Outcome number 88

[Jump to summary definition](#summary-Pass-88)	|	[Previous Pass outcome](#pass-outcome-number-87)	|	[Next Pass outcome](#pass-outcome-number-89)

:white_check_mark:Pass outcome
#### Subject detail
|Name|module-src-core-modelet-manufacturing-environments-discover-signifiers|
|----|----|
|Title|Merged&#32;module&#32;src/core.ttl&#32;from&#32;branch&#32;HEAD&#32;with&#32;related&#32;terms&#32;from&#32;the&#32;fragments&#32;domains/manufacturing-environments/discover-signifiers/onto.ttl|
|Composition|- [Modelet manufacturing-environments/discover-signifiers](https://github.com/HyperAgents/hmas/blob/HEAD/domains/manufacturing-environments/discover-signifiers/onto.ttl)<br/>- [Module core](https://github.com/HyperAgents/hmas/blob/HEAD/src/core.ttl)|

#### Criterion detail
|Identifier|[domain-and-range-referencing](https://ns.inria.fr/olivaw#domain-and-range-referencing)|
|----|----|
|Title|Domain&#32;and&#32;range&#32;referencing&#32;test|
|Description|A&#32;test&#32;case&#32;from&#32;the&#32;Best&#32;Practices&#32;tests&#32;checking&#32;if&#32;all&#32;the&#32;ranges&#32;and&#32;domains&#32;from&#32;the&#32;test&#32;subject&#32;point&#32;to&#32;terms&#32;that&#32;are&#32;defined&#32;in&#32;the&#32;vocabulary.|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-88)|Identifier|`range-out-of-vocabulary`|
|[Section top](#pass-outcome-number-88)|Title|Ranges&#32;properly&#32;defined|
|[Section top](#pass-outcome-number-88)|Description|Each&#32;rdfs:range&#32;is&#32;defined&#32;within&#32;the&#32;fragment|

***
### Pass Outcome number 89

[Jump to summary definition](#summary-Pass-89)	|	[Previous Pass outcome](#pass-outcome-number-88)	|	[Next Pass outcome](#pass-outcome-number-90)

:white_check_mark:Pass outcome
#### Subject detail
|Name|module-src-core-modelet-manufacturing-environments-discover-signifiers|
|----|----|
|Title|Merged&#32;module&#32;src/core.ttl&#32;from&#32;branch&#32;HEAD&#32;with&#32;related&#32;terms&#32;from&#32;the&#32;fragments&#32;domains/manufacturing-environments/discover-signifiers/onto.ttl|
|Composition|- [Modelet manufacturing-environments/discover-signifiers](https://github.com/HyperAgents/hmas/blob/HEAD/domains/manufacturing-environments/discover-signifiers/onto.ttl)<br/>- [Module core](https://github.com/HyperAgents/hmas/blob/HEAD/src/core.ttl)|

#### Criterion detail
|Identifier|[owl-rl-constraint](https://ns.inria.fr/olivaw#owl-rl-constraint)|
|----|----|
|Title|OWL&#32;RL&#32;Constraint&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;check&#32;wether&#32;the&#32;test&#32;subject&#32;is&#32;syntaxically&#32;correct&#32;or&#32;not.|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-89)|Identifier|`owl-rl-constraint-violation`|
|[Section top](#pass-outcome-number-89)|Title|OWL&#32;RL&#32;consistent|
|[Section top](#pass-outcome-number-89)|Description|The&#32;provided&#32;graph&#32;is&#32;consistent&#32;for&#32;any&#32;OWL&#32;RL&#32;constraint|

***
### Pass Outcome number 90

[Jump to summary definition](#summary-Pass-90)	|	[Previous Pass outcome](#pass-outcome-number-89)	|	[Next Pass outcome](#pass-outcome-number-91)

:white_check_mark:Pass outcome
#### Subject detail
|Name|module-src-core-modelet-manufacturing-environments-discover-signifiers|
|----|----|
|Title|Merged&#32;module&#32;src/core.ttl&#32;from&#32;branch&#32;HEAD&#32;with&#32;related&#32;terms&#32;from&#32;the&#32;fragments&#32;domains/manufacturing-environments/discover-signifiers/onto.ttl|
|Composition|- [Modelet manufacturing-environments/discover-signifiers](https://github.com/HyperAgents/hmas/blob/HEAD/domains/manufacturing-environments/discover-signifiers/onto.ttl)<br/>- [Module core](https://github.com/HyperAgents/hmas/blob/HEAD/src/core.ttl)|

#### Criterion detail
|Identifier|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|
|----|----|
|Title|Profile&#32;compatibility&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;check&#32;whether&#32;the&#32;test&#32;subject&#32;is&#32;compatible&#32;with&#32;a&#32;profile&#32;or&#32;not,&#32;and&#32;if&#32;it&#32;is&#32;not,&#32;why.|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-90)|Identifier|`owl-rl-profile-error`|
|[Section top](#pass-outcome-number-90)|Title|OWL&#32;RL&#32;Profile&#32;compatible|
|[Section top](#pass-outcome-number-90)|Description|The&#32;subject&#32;is&#32;included&#32;in&#32;the&#32;OWL&#32;RL&#32;sublanguage|

***
### Pass Outcome number 91

[Jump to summary definition](#summary-Pass-91)	|	[Previous Pass outcome](#pass-outcome-number-90)	|	[Next Pass outcome](#pass-outcome-number-92)

:white_check_mark:Pass outcome
#### Subject detail
|Name|module-src-core-modelet-manufacturing-environments-discover-signifiers|
|----|----|
|Title|Merged&#32;module&#32;src/core.ttl&#32;from&#32;branch&#32;HEAD&#32;with&#32;related&#32;terms&#32;from&#32;the&#32;fragments&#32;domains/manufacturing-environments/discover-signifiers/onto.ttl|
|Composition|- [Modelet manufacturing-environments/discover-signifiers](https://github.com/HyperAgents/hmas/blob/HEAD/domains/manufacturing-environments/discover-signifiers/onto.ttl)<br/>- [Module core](https://github.com/HyperAgents/hmas/blob/HEAD/src/core.ttl)|

#### Criterion detail
|Identifier|[proper-extension-predicate](https://ns.inria.fr/olivaw#proper-extension-predicate)|
|----|----|
|Title|Predicate&#32;extension&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;test&#32;the&#32;proper&#32;use&#32;of&#32;predicates&#32;rdfs:subClassOf&#32;and&#32;rdfs:subPropertyOf&#32;on&#32;the&#32;ontology&#32;terms|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-91)|Identifier|`class-subpropertyof`|
|[Section top](#pass-outcome-number-91)|Title|No&#32;class&#32;subproperty|
|[Section top](#pass-outcome-number-91)|Description|No&#32;ontology&#32;class&#32;is&#32;a&#32;subproperty|

***
### Pass Outcome number 92

[Jump to summary definition](#summary-Pass-92)	|	[Previous Pass outcome](#pass-outcome-number-91)	|	[Next Pass outcome](#pass-outcome-number-93)

:white_check_mark:Pass outcome
#### Subject detail
|Name|module-src-core-modelet-manufacturing-environments-discover-signifiers|
|----|----|
|Title|Merged&#32;module&#32;src/core.ttl&#32;from&#32;branch&#32;HEAD&#32;with&#32;related&#32;terms&#32;from&#32;the&#32;fragments&#32;domains/manufacturing-environments/discover-signifiers/onto.ttl|
|Composition|- [Modelet manufacturing-environments/discover-signifiers](https://github.com/HyperAgents/hmas/blob/HEAD/domains/manufacturing-environments/discover-signifiers/onto.ttl)<br/>- [Module core](https://github.com/HyperAgents/hmas/blob/HEAD/src/core.ttl)|

#### Criterion detail
|Identifier|[proper-extension-predicate](https://ns.inria.fr/olivaw#proper-extension-predicate)|
|----|----|
|Title|Predicate&#32;extension&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;test&#32;the&#32;proper&#32;use&#32;of&#32;predicates&#32;rdfs:subClassOf&#32;and&#32;rdfs:subPropertyOf&#32;on&#32;the&#32;ontology&#32;terms|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-92)|Identifier|`property-subclassof`|
|[Section top](#pass-outcome-number-92)|Title|No&#32;property&#32;subclass|
|[Section top](#pass-outcome-number-92)|Description|No&#32;ontology&#32;property&#32;is&#32;a&#32;subclass|

***
### Pass Outcome number 93

[Jump to summary definition](#summary-Pass-93)	|	[Previous Pass outcome](#pass-outcome-number-92)	|	[Next Pass outcome](#pass-outcome-number-94)

:white_check_mark:Pass outcome
#### Subject detail
|Name|module-src-core-modelet-manufacturing-environments-discover-signifiers|
|----|----|
|Title|Merged&#32;module&#32;src/core.ttl&#32;from&#32;branch&#32;HEAD&#32;with&#32;related&#32;terms&#32;from&#32;the&#32;fragments&#32;domains/manufacturing-environments/discover-signifiers/onto.ttl|
|Composition|- [Modelet manufacturing-environments/discover-signifiers](https://github.com/HyperAgents/hmas/blob/HEAD/domains/manufacturing-environments/discover-signifiers/onto.ttl)<br/>- [Module core](https://github.com/HyperAgents/hmas/blob/HEAD/src/core.ttl)|

#### Criterion detail
|Identifier|[proper-extension-predicate](https://ns.inria.fr/olivaw#proper-extension-predicate)|
|----|----|
|Title|Predicate&#32;extension&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;test&#32;the&#32;proper&#32;use&#32;of&#32;predicates&#32;rdfs:subClassOf&#32;and&#32;rdfs:subPropertyOf&#32;on&#32;the&#32;ontology&#32;terms|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-93)|Identifier|`subclassof-property`|
|[Section top](#pass-outcome-number-93)|Title|No&#32;subclass&#32;of&#32;property|
|[Section top](#pass-outcome-number-93)|Description|No&#32;ontology&#32;term&#32;is&#32;a&#32;subclass&#32;of&#32;a&#32;property|

***
### Pass Outcome number 94

[Jump to summary definition](#summary-Pass-94)	|	[Previous Pass outcome](#pass-outcome-number-93)	|	[Next Pass outcome](#pass-outcome-number-95)

:white_check_mark:Pass outcome
#### Subject detail
|Name|module-src-core-modelet-manufacturing-environments-discover-signifiers|
|----|----|
|Title|Merged&#32;module&#32;src/core.ttl&#32;from&#32;branch&#32;HEAD&#32;with&#32;related&#32;terms&#32;from&#32;the&#32;fragments&#32;domains/manufacturing-environments/discover-signifiers/onto.ttl|
|Composition|- [Modelet manufacturing-environments/discover-signifiers](https://github.com/HyperAgents/hmas/blob/HEAD/domains/manufacturing-environments/discover-signifiers/onto.ttl)<br/>- [Module core](https://github.com/HyperAgents/hmas/blob/HEAD/src/core.ttl)|

#### Criterion detail
|Identifier|[proper-extension-predicate](https://ns.inria.fr/olivaw#proper-extension-predicate)|
|----|----|
|Title|Predicate&#32;extension&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;test&#32;the&#32;proper&#32;use&#32;of&#32;predicates&#32;rdfs:subClassOf&#32;and&#32;rdfs:subPropertyOf&#32;on&#32;the&#32;ontology&#32;terms|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-94)|Identifier|`subpropertyof-class`|
|[Section top](#pass-outcome-number-94)|Title|No&#32;subproperty&#32;of&#32;class|
|[Section top](#pass-outcome-number-94)|Description|No&#32;ontology&#32;term&#32;is&#32;a&#32;subproperty&#32;of&#32;a&#32;class|

***
### Pass Outcome number 95

[Jump to summary definition](#summary-Pass-95)	|	[Previous Pass outcome](#pass-outcome-number-94)	|	[Next Pass outcome](#pass-outcome-number-96)

:white_check_mark:Pass outcome
#### Subject detail
|Name|module-src-core-modelet-manufacturing-environments-discover-signifiers|
|----|----|
|Title|Merged&#32;module&#32;src/core.ttl&#32;from&#32;branch&#32;HEAD&#32;with&#32;related&#32;terms&#32;from&#32;the&#32;fragments&#32;domains/manufacturing-environments/discover-signifiers/onto.ttl|
|Composition|- [Modelet manufacturing-environments/discover-signifiers](https://github.com/HyperAgents/hmas/blob/HEAD/domains/manufacturing-environments/discover-signifiers/onto.ttl)<br/>- [Module core](https://github.com/HyperAgents/hmas/blob/HEAD/src/core.ttl)|

#### Criterion detail
|Identifier|[term-referencing](https://ns.inria.fr/olivaw#term-referencing)|
|----|----|
|Title|Term&#32;referencing&#32;test|
|Description|A&#32;test&#32;case&#32;from&#32;the&#32;Best&#32;Practices&#32;tests&#32;checking&#32;if&#32;each&#32;term&#32;of&#32;the&#32;test&#32;subject&#32;is&#32;referenced&#32;to&#32;a&#32;module&#32;through&#32;a&#32;rdfs:isDefinedBy&#32;property.|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-95)|Identifier|`no-reference-module`|
|[Section top](#pass-outcome-number-95)|Title|Any&#32;term&#32;is&#32;referenced|
|[Section top](#pass-outcome-number-95)|Description|Each&#32;term&#32;of&#32;the&#32;test&#32;subject&#32;is&#32;linked&#32;to&#32;a&#32;module&#32;by&#32;a&#32;rdfs:isDefinedBy&#32;property|

***
### Pass Outcome number 96

[Jump to summary definition](#summary-Pass-96)	|	[Previous Pass outcome](#pass-outcome-number-95)	|	[Next Pass outcome](#pass-outcome-number-97)

:white_check_mark:Pass outcome
#### Subject detail
|Name|module-src-core-modelet-manufacturing-environments-discover-signifiers|
|----|----|
|Title|Merged&#32;module&#32;src/core.ttl&#32;from&#32;branch&#32;HEAD&#32;with&#32;related&#32;terms&#32;from&#32;the&#32;fragments&#32;domains/manufacturing-environments/discover-signifiers/onto.ttl|
|Composition|- [Modelet manufacturing-environments/discover-signifiers](https://github.com/HyperAgents/hmas/blob/HEAD/domains/manufacturing-environments/discover-signifiers/onto.ttl)<br/>- [Module core](https://github.com/HyperAgents/hmas/blob/HEAD/src/core.ttl)|

#### Criterion detail
|Identifier|[terms-differenciation](https://ns.inria.fr/olivaw#terms-differenciation)|
|----|----|
|Title|Terms&#32;differenciation&#32;test|
|Description|A&#32;test&#32;case&#32;from&#32;the&#32;Best&#32;Practices&#32;tests&#32;checking&#32;if&#32;all&#32;the&#32;terms&#32;are&#32;different&#32;enough&#32;from&#32;each&#32;other&#32;according&#32;to&#32;the&#32;Levenshtein&#32;distance&#32;metric.|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-96)|Identifier|`too-close-terms`|
|[Section top](#pass-outcome-number-96)|Title|Terms&#32;differenciated&#32;enough|
|[Section top](#pass-outcome-number-96)|Description|All&#32;the&#32;terms&#32;have&#32;have&#32;a&#32;satisfying&#32;Levenshtein&#32;distance&#32;from&#32;each&#32;other&#32;term.|

***
### Pass Outcome number 97

[Jump to summary definition](#summary-Pass-97)	|	[Previous Pass outcome](#pass-outcome-number-96)	|	[Next Pass outcome](#pass-outcome-number-98)

:white_check_mark:Pass outcome
#### Subject detail
|Name|module-src-core-modelet-manufacturing-environments-discover-platforms|
|----|----|
|Title|Merged&#32;module&#32;src/core.ttl&#32;from&#32;branch&#32;HEAD&#32;with&#32;related&#32;terms&#32;from&#32;the&#32;fragments&#32;domains/manufacturing-environments/discover-platforms/onto.ttl|
|Composition|- [Modelet manufacturing-environments/discover-platforms](https://github.com/HyperAgents/hmas/blob/HEAD/domains/manufacturing-environments/discover-platforms/onto.ttl)<br/>- [Module core](https://github.com/HyperAgents/hmas/blob/HEAD/src/core.ttl)|

#### Criterion detail
|Identifier|[domain-and-range-referencing](https://ns.inria.fr/olivaw#domain-and-range-referencing)|
|----|----|
|Title|Domain&#32;and&#32;range&#32;referencing&#32;test|
|Description|A&#32;test&#32;case&#32;from&#32;the&#32;Best&#32;Practices&#32;tests&#32;checking&#32;if&#32;all&#32;the&#32;ranges&#32;and&#32;domains&#32;from&#32;the&#32;test&#32;subject&#32;point&#32;to&#32;terms&#32;that&#32;are&#32;defined&#32;in&#32;the&#32;vocabulary.|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-97)|Identifier|`domain-out-of-vocabulary`|
|[Section top](#pass-outcome-number-97)|Title|Domains&#32;properly&#32;defined|
|[Section top](#pass-outcome-number-97)|Description|Each&#32;rdfs:domain&#32;is&#32;defined&#32;within&#32;the&#32;fragment|

***
### Pass Outcome number 98

[Jump to summary definition](#summary-Pass-98)	|	[Previous Pass outcome](#pass-outcome-number-97)	|	[Next Pass outcome](#pass-outcome-number-99)

:white_check_mark:Pass outcome
#### Subject detail
|Name|module-src-core-modelet-manufacturing-environments-discover-platforms|
|----|----|
|Title|Merged&#32;module&#32;src/core.ttl&#32;from&#32;branch&#32;HEAD&#32;with&#32;related&#32;terms&#32;from&#32;the&#32;fragments&#32;domains/manufacturing-environments/discover-platforms/onto.ttl|
|Composition|- [Modelet manufacturing-environments/discover-platforms](https://github.com/HyperAgents/hmas/blob/HEAD/domains/manufacturing-environments/discover-platforms/onto.ttl)<br/>- [Module core](https://github.com/HyperAgents/hmas/blob/HEAD/src/core.ttl)|

#### Criterion detail
|Identifier|[domain-and-range-referencing](https://ns.inria.fr/olivaw#domain-and-range-referencing)|
|----|----|
|Title|Domain&#32;and&#32;range&#32;referencing&#32;test|
|Description|A&#32;test&#32;case&#32;from&#32;the&#32;Best&#32;Practices&#32;tests&#32;checking&#32;if&#32;all&#32;the&#32;ranges&#32;and&#32;domains&#32;from&#32;the&#32;test&#32;subject&#32;point&#32;to&#32;terms&#32;that&#32;are&#32;defined&#32;in&#32;the&#32;vocabulary.|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-98)|Identifier|`range-out-of-vocabulary`|
|[Section top](#pass-outcome-number-98)|Title|Ranges&#32;properly&#32;defined|
|[Section top](#pass-outcome-number-98)|Description|Each&#32;rdfs:range&#32;is&#32;defined&#32;within&#32;the&#32;fragment|

***
### Pass Outcome number 99

[Jump to summary definition](#summary-Pass-99)	|	[Previous Pass outcome](#pass-outcome-number-98)	|	[Next Pass outcome](#pass-outcome-number-100)

:white_check_mark:Pass outcome
#### Subject detail
|Name|module-src-core-modelet-manufacturing-environments-discover-platforms|
|----|----|
|Title|Merged&#32;module&#32;src/core.ttl&#32;from&#32;branch&#32;HEAD&#32;with&#32;related&#32;terms&#32;from&#32;the&#32;fragments&#32;domains/manufacturing-environments/discover-platforms/onto.ttl|
|Composition|- [Modelet manufacturing-environments/discover-platforms](https://github.com/HyperAgents/hmas/blob/HEAD/domains/manufacturing-environments/discover-platforms/onto.ttl)<br/>- [Module core](https://github.com/HyperAgents/hmas/blob/HEAD/src/core.ttl)|

#### Criterion detail
|Identifier|[owl-rl-constraint](https://ns.inria.fr/olivaw#owl-rl-constraint)|
|----|----|
|Title|OWL&#32;RL&#32;Constraint&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;check&#32;wether&#32;the&#32;test&#32;subject&#32;is&#32;syntaxically&#32;correct&#32;or&#32;not.|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-99)|Identifier|`owl-rl-constraint-violation`|
|[Section top](#pass-outcome-number-99)|Title|OWL&#32;RL&#32;consistent|
|[Section top](#pass-outcome-number-99)|Description|The&#32;provided&#32;graph&#32;is&#32;consistent&#32;for&#32;any&#32;OWL&#32;RL&#32;constraint|

***
### Pass Outcome number 100

[Jump to summary definition](#summary-Pass-100)	|	[Previous Pass outcome](#pass-outcome-number-99)	|	[Next Pass outcome](#pass-outcome-number-101)

:white_check_mark:Pass outcome
#### Subject detail
|Name|module-src-core-modelet-manufacturing-environments-discover-platforms|
|----|----|
|Title|Merged&#32;module&#32;src/core.ttl&#32;from&#32;branch&#32;HEAD&#32;with&#32;related&#32;terms&#32;from&#32;the&#32;fragments&#32;domains/manufacturing-environments/discover-platforms/onto.ttl|
|Composition|- [Modelet manufacturing-environments/discover-platforms](https://github.com/HyperAgents/hmas/blob/HEAD/domains/manufacturing-environments/discover-platforms/onto.ttl)<br/>- [Module core](https://github.com/HyperAgents/hmas/blob/HEAD/src/core.ttl)|

#### Criterion detail
|Identifier|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|
|----|----|
|Title|Profile&#32;compatibility&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;check&#32;whether&#32;the&#32;test&#32;subject&#32;is&#32;compatible&#32;with&#32;a&#32;profile&#32;or&#32;not,&#32;and&#32;if&#32;it&#32;is&#32;not,&#32;why.|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-100)|Identifier|`owl-rl-profile-error`|
|[Section top](#pass-outcome-number-100)|Title|OWL&#32;RL&#32;Profile&#32;compatible|
|[Section top](#pass-outcome-number-100)|Description|The&#32;subject&#32;is&#32;included&#32;in&#32;the&#32;OWL&#32;RL&#32;sublanguage|

***
### Pass Outcome number 101

[Jump to summary definition](#summary-Pass-101)	|	[Previous Pass outcome](#pass-outcome-number-100)	|	[Next Pass outcome](#pass-outcome-number-102)

:white_check_mark:Pass outcome
#### Subject detail
|Name|module-src-core-modelet-manufacturing-environments-discover-platforms|
|----|----|
|Title|Merged&#32;module&#32;src/core.ttl&#32;from&#32;branch&#32;HEAD&#32;with&#32;related&#32;terms&#32;from&#32;the&#32;fragments&#32;domains/manufacturing-environments/discover-platforms/onto.ttl|
|Composition|- [Modelet manufacturing-environments/discover-platforms](https://github.com/HyperAgents/hmas/blob/HEAD/domains/manufacturing-environments/discover-platforms/onto.ttl)<br/>- [Module core](https://github.com/HyperAgents/hmas/blob/HEAD/src/core.ttl)|

#### Criterion detail
|Identifier|[proper-extension-predicate](https://ns.inria.fr/olivaw#proper-extension-predicate)|
|----|----|
|Title|Predicate&#32;extension&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;test&#32;the&#32;proper&#32;use&#32;of&#32;predicates&#32;rdfs:subClassOf&#32;and&#32;rdfs:subPropertyOf&#32;on&#32;the&#32;ontology&#32;terms|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-101)|Identifier|`class-subpropertyof`|
|[Section top](#pass-outcome-number-101)|Title|No&#32;class&#32;subproperty|
|[Section top](#pass-outcome-number-101)|Description|No&#32;ontology&#32;class&#32;is&#32;a&#32;subproperty|

***
### Pass Outcome number 102

[Jump to summary definition](#summary-Pass-102)	|	[Previous Pass outcome](#pass-outcome-number-101)	|	[Next Pass outcome](#pass-outcome-number-103)

:white_check_mark:Pass outcome
#### Subject detail
|Name|module-src-core-modelet-manufacturing-environments-discover-platforms|
|----|----|
|Title|Merged&#32;module&#32;src/core.ttl&#32;from&#32;branch&#32;HEAD&#32;with&#32;related&#32;terms&#32;from&#32;the&#32;fragments&#32;domains/manufacturing-environments/discover-platforms/onto.ttl|
|Composition|- [Modelet manufacturing-environments/discover-platforms](https://github.com/HyperAgents/hmas/blob/HEAD/domains/manufacturing-environments/discover-platforms/onto.ttl)<br/>- [Module core](https://github.com/HyperAgents/hmas/blob/HEAD/src/core.ttl)|

#### Criterion detail
|Identifier|[proper-extension-predicate](https://ns.inria.fr/olivaw#proper-extension-predicate)|
|----|----|
|Title|Predicate&#32;extension&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;test&#32;the&#32;proper&#32;use&#32;of&#32;predicates&#32;rdfs:subClassOf&#32;and&#32;rdfs:subPropertyOf&#32;on&#32;the&#32;ontology&#32;terms|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-102)|Identifier|`property-subclassof`|
|[Section top](#pass-outcome-number-102)|Title|No&#32;property&#32;subclass|
|[Section top](#pass-outcome-number-102)|Description|No&#32;ontology&#32;property&#32;is&#32;a&#32;subclass|

***
### Pass Outcome number 103

[Jump to summary definition](#summary-Pass-103)	|	[Previous Pass outcome](#pass-outcome-number-102)	|	[Next Pass outcome](#pass-outcome-number-104)

:white_check_mark:Pass outcome
#### Subject detail
|Name|module-src-core-modelet-manufacturing-environments-discover-platforms|
|----|----|
|Title|Merged&#32;module&#32;src/core.ttl&#32;from&#32;branch&#32;HEAD&#32;with&#32;related&#32;terms&#32;from&#32;the&#32;fragments&#32;domains/manufacturing-environments/discover-platforms/onto.ttl|
|Composition|- [Modelet manufacturing-environments/discover-platforms](https://github.com/HyperAgents/hmas/blob/HEAD/domains/manufacturing-environments/discover-platforms/onto.ttl)<br/>- [Module core](https://github.com/HyperAgents/hmas/blob/HEAD/src/core.ttl)|

#### Criterion detail
|Identifier|[proper-extension-predicate](https://ns.inria.fr/olivaw#proper-extension-predicate)|
|----|----|
|Title|Predicate&#32;extension&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;test&#32;the&#32;proper&#32;use&#32;of&#32;predicates&#32;rdfs:subClassOf&#32;and&#32;rdfs:subPropertyOf&#32;on&#32;the&#32;ontology&#32;terms|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-103)|Identifier|`subclassof-property`|
|[Section top](#pass-outcome-number-103)|Title|No&#32;subclass&#32;of&#32;property|
|[Section top](#pass-outcome-number-103)|Description|No&#32;ontology&#32;term&#32;is&#32;a&#32;subclass&#32;of&#32;a&#32;property|

***
### Pass Outcome number 104

[Jump to summary definition](#summary-Pass-104)	|	[Previous Pass outcome](#pass-outcome-number-103)	|	[Next Pass outcome](#pass-outcome-number-105)

:white_check_mark:Pass outcome
#### Subject detail
|Name|module-src-core-modelet-manufacturing-environments-discover-platforms|
|----|----|
|Title|Merged&#32;module&#32;src/core.ttl&#32;from&#32;branch&#32;HEAD&#32;with&#32;related&#32;terms&#32;from&#32;the&#32;fragments&#32;domains/manufacturing-environments/discover-platforms/onto.ttl|
|Composition|- [Modelet manufacturing-environments/discover-platforms](https://github.com/HyperAgents/hmas/blob/HEAD/domains/manufacturing-environments/discover-platforms/onto.ttl)<br/>- [Module core](https://github.com/HyperAgents/hmas/blob/HEAD/src/core.ttl)|

#### Criterion detail
|Identifier|[proper-extension-predicate](https://ns.inria.fr/olivaw#proper-extension-predicate)|
|----|----|
|Title|Predicate&#32;extension&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;test&#32;the&#32;proper&#32;use&#32;of&#32;predicates&#32;rdfs:subClassOf&#32;and&#32;rdfs:subPropertyOf&#32;on&#32;the&#32;ontology&#32;terms|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-104)|Identifier|`subpropertyof-class`|
|[Section top](#pass-outcome-number-104)|Title|No&#32;subproperty&#32;of&#32;class|
|[Section top](#pass-outcome-number-104)|Description|No&#32;ontology&#32;term&#32;is&#32;a&#32;subproperty&#32;of&#32;a&#32;class|

***
### Pass Outcome number 105

[Jump to summary definition](#summary-Pass-105)	|	[Previous Pass outcome](#pass-outcome-number-104)	|	[Next Pass outcome](#pass-outcome-number-106)

:white_check_mark:Pass outcome
#### Subject detail
|Name|module-src-core-modelet-manufacturing-environments-discover-platforms|
|----|----|
|Title|Merged&#32;module&#32;src/core.ttl&#32;from&#32;branch&#32;HEAD&#32;with&#32;related&#32;terms&#32;from&#32;the&#32;fragments&#32;domains/manufacturing-environments/discover-platforms/onto.ttl|
|Composition|- [Modelet manufacturing-environments/discover-platforms](https://github.com/HyperAgents/hmas/blob/HEAD/domains/manufacturing-environments/discover-platforms/onto.ttl)<br/>- [Module core](https://github.com/HyperAgents/hmas/blob/HEAD/src/core.ttl)|

#### Criterion detail
|Identifier|[term-referencing](https://ns.inria.fr/olivaw#term-referencing)|
|----|----|
|Title|Term&#32;referencing&#32;test|
|Description|A&#32;test&#32;case&#32;from&#32;the&#32;Best&#32;Practices&#32;tests&#32;checking&#32;if&#32;each&#32;term&#32;of&#32;the&#32;test&#32;subject&#32;is&#32;referenced&#32;to&#32;a&#32;module&#32;through&#32;a&#32;rdfs:isDefinedBy&#32;property.|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-105)|Identifier|`no-reference-module`|
|[Section top](#pass-outcome-number-105)|Title|Any&#32;term&#32;is&#32;referenced|
|[Section top](#pass-outcome-number-105)|Description|Each&#32;term&#32;of&#32;the&#32;test&#32;subject&#32;is&#32;linked&#32;to&#32;a&#32;module&#32;by&#32;a&#32;rdfs:isDefinedBy&#32;property|

***
### Pass Outcome number 106

[Jump to summary definition](#summary-Pass-106)	|	[Previous Pass outcome](#pass-outcome-number-105)	|	[Next Pass outcome](#pass-outcome-number-107)

:white_check_mark:Pass outcome
#### Subject detail
|Name|module-src-core-modelet-manufacturing-environments-discover-platforms|
|----|----|
|Title|Merged&#32;module&#32;src/core.ttl&#32;from&#32;branch&#32;HEAD&#32;with&#32;related&#32;terms&#32;from&#32;the&#32;fragments&#32;domains/manufacturing-environments/discover-platforms/onto.ttl|
|Composition|- [Modelet manufacturing-environments/discover-platforms](https://github.com/HyperAgents/hmas/blob/HEAD/domains/manufacturing-environments/discover-platforms/onto.ttl)<br/>- [Module core](https://github.com/HyperAgents/hmas/blob/HEAD/src/core.ttl)|

#### Criterion detail
|Identifier|[terms-differenciation](https://ns.inria.fr/olivaw#terms-differenciation)|
|----|----|
|Title|Terms&#32;differenciation&#32;test|
|Description|A&#32;test&#32;case&#32;from&#32;the&#32;Best&#32;Practices&#32;tests&#32;checking&#32;if&#32;all&#32;the&#32;terms&#32;are&#32;different&#32;enough&#32;from&#32;each&#32;other&#32;according&#32;to&#32;the&#32;Levenshtein&#32;distance&#32;metric.|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-106)|Identifier|`too-close-terms`|
|[Section top](#pass-outcome-number-106)|Title|Terms&#32;differenciated&#32;enough|
|[Section top](#pass-outcome-number-106)|Description|All&#32;the&#32;terms&#32;have&#32;have&#32;a&#32;satisfying&#32;Levenshtein&#32;distance&#32;from&#32;each&#32;other&#32;term.|

***
### Pass Outcome number 107

[Jump to summary definition](#summary-Pass-107)	|	[Previous Pass outcome](#pass-outcome-number-106)	|	[Next Pass outcome](#pass-outcome-number-108)

:white_check_mark:Pass outcome
#### Subject detail
|Name|module-src-core-modelet-manufacturing-environments-discover-organization|
|----|----|
|Title|Merged&#32;module&#32;src/core.ttl&#32;from&#32;branch&#32;HEAD&#32;with&#32;related&#32;terms&#32;from&#32;the&#32;fragments&#32;domains/manufacturing-environments/discover-organization/onto.ttl|
|Composition|- [Modelet manufacturing-environments/discover-organization](https://github.com/HyperAgents/hmas/blob/HEAD/domains/manufacturing-environments/discover-organization/onto.ttl)<br/>- [Module core](https://github.com/HyperAgents/hmas/blob/HEAD/src/core.ttl)|

#### Criterion detail
|Identifier|[domain-and-range-referencing](https://ns.inria.fr/olivaw#domain-and-range-referencing)|
|----|----|
|Title|Domain&#32;and&#32;range&#32;referencing&#32;test|
|Description|A&#32;test&#32;case&#32;from&#32;the&#32;Best&#32;Practices&#32;tests&#32;checking&#32;if&#32;all&#32;the&#32;ranges&#32;and&#32;domains&#32;from&#32;the&#32;test&#32;subject&#32;point&#32;to&#32;terms&#32;that&#32;are&#32;defined&#32;in&#32;the&#32;vocabulary.|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-107)|Identifier|`domain-out-of-vocabulary`|
|[Section top](#pass-outcome-number-107)|Title|Domains&#32;properly&#32;defined|
|[Section top](#pass-outcome-number-107)|Description|Each&#32;rdfs:domain&#32;is&#32;defined&#32;within&#32;the&#32;fragment|

***
### Pass Outcome number 108

[Jump to summary definition](#summary-Pass-108)	|	[Previous Pass outcome](#pass-outcome-number-107)	|	[Next Pass outcome](#pass-outcome-number-109)

:white_check_mark:Pass outcome
#### Subject detail
|Name|module-src-core-modelet-manufacturing-environments-discover-organization|
|----|----|
|Title|Merged&#32;module&#32;src/core.ttl&#32;from&#32;branch&#32;HEAD&#32;with&#32;related&#32;terms&#32;from&#32;the&#32;fragments&#32;domains/manufacturing-environments/discover-organization/onto.ttl|
|Composition|- [Modelet manufacturing-environments/discover-organization](https://github.com/HyperAgents/hmas/blob/HEAD/domains/manufacturing-environments/discover-organization/onto.ttl)<br/>- [Module core](https://github.com/HyperAgents/hmas/blob/HEAD/src/core.ttl)|

#### Criterion detail
|Identifier|[domain-and-range-referencing](https://ns.inria.fr/olivaw#domain-and-range-referencing)|
|----|----|
|Title|Domain&#32;and&#32;range&#32;referencing&#32;test|
|Description|A&#32;test&#32;case&#32;from&#32;the&#32;Best&#32;Practices&#32;tests&#32;checking&#32;if&#32;all&#32;the&#32;ranges&#32;and&#32;domains&#32;from&#32;the&#32;test&#32;subject&#32;point&#32;to&#32;terms&#32;that&#32;are&#32;defined&#32;in&#32;the&#32;vocabulary.|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-108)|Identifier|`range-out-of-vocabulary`|
|[Section top](#pass-outcome-number-108)|Title|Ranges&#32;properly&#32;defined|
|[Section top](#pass-outcome-number-108)|Description|Each&#32;rdfs:range&#32;is&#32;defined&#32;within&#32;the&#32;fragment|

***
### Pass Outcome number 109

[Jump to summary definition](#summary-Pass-109)	|	[Previous Pass outcome](#pass-outcome-number-108)	|	[Next Pass outcome](#pass-outcome-number-110)

:white_check_mark:Pass outcome
#### Subject detail
|Name|module-src-core-modelet-manufacturing-environments-discover-organization|
|----|----|
|Title|Merged&#32;module&#32;src/core.ttl&#32;from&#32;branch&#32;HEAD&#32;with&#32;related&#32;terms&#32;from&#32;the&#32;fragments&#32;domains/manufacturing-environments/discover-organization/onto.ttl|
|Composition|- [Modelet manufacturing-environments/discover-organization](https://github.com/HyperAgents/hmas/blob/HEAD/domains/manufacturing-environments/discover-organization/onto.ttl)<br/>- [Module core](https://github.com/HyperAgents/hmas/blob/HEAD/src/core.ttl)|

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
|Name|module-src-core-modelet-manufacturing-environments-discover-organization|
|----|----|
|Title|Merged&#32;module&#32;src/core.ttl&#32;from&#32;branch&#32;HEAD&#32;with&#32;related&#32;terms&#32;from&#32;the&#32;fragments&#32;domains/manufacturing-environments/discover-organization/onto.ttl|
|Composition|- [Modelet manufacturing-environments/discover-organization](https://github.com/HyperAgents/hmas/blob/HEAD/domains/manufacturing-environments/discover-organization/onto.ttl)<br/>- [Module core](https://github.com/HyperAgents/hmas/blob/HEAD/src/core.ttl)|

#### Criterion detail
|Identifier|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|
|----|----|
|Title|Profile&#32;compatibility&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;check&#32;whether&#32;the&#32;test&#32;subject&#32;is&#32;compatible&#32;with&#32;a&#32;profile&#32;or&#32;not,&#32;and&#32;if&#32;it&#32;is&#32;not,&#32;why.|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-110)|Identifier|`owl-rl-profile-error`|
|[Section top](#pass-outcome-number-110)|Title|OWL&#32;RL&#32;Profile&#32;compatible|
|[Section top](#pass-outcome-number-110)|Description|The&#32;subject&#32;is&#32;included&#32;in&#32;the&#32;OWL&#32;RL&#32;sublanguage|

***
### Pass Outcome number 111

[Jump to summary definition](#summary-Pass-111)	|	[Previous Pass outcome](#pass-outcome-number-110)	|	[Next Pass outcome](#pass-outcome-number-112)

:white_check_mark:Pass outcome
#### Subject detail
|Name|module-src-core-modelet-manufacturing-environments-discover-organization|
|----|----|
|Title|Merged&#32;module&#32;src/core.ttl&#32;from&#32;branch&#32;HEAD&#32;with&#32;related&#32;terms&#32;from&#32;the&#32;fragments&#32;domains/manufacturing-environments/discover-organization/onto.ttl|
|Composition|- [Modelet manufacturing-environments/discover-organization](https://github.com/HyperAgents/hmas/blob/HEAD/domains/manufacturing-environments/discover-organization/onto.ttl)<br/>- [Module core](https://github.com/HyperAgents/hmas/blob/HEAD/src/core.ttl)|

#### Criterion detail
|Identifier|[proper-extension-predicate](https://ns.inria.fr/olivaw#proper-extension-predicate)|
|----|----|
|Title|Predicate&#32;extension&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;test&#32;the&#32;proper&#32;use&#32;of&#32;predicates&#32;rdfs:subClassOf&#32;and&#32;rdfs:subPropertyOf&#32;on&#32;the&#32;ontology&#32;terms|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-111)|Identifier|`class-subpropertyof`|
|[Section top](#pass-outcome-number-111)|Title|No&#32;class&#32;subproperty|
|[Section top](#pass-outcome-number-111)|Description|No&#32;ontology&#32;class&#32;is&#32;a&#32;subproperty|

***
### Pass Outcome number 112

[Jump to summary definition](#summary-Pass-112)	|	[Previous Pass outcome](#pass-outcome-number-111)	|	[Next Pass outcome](#pass-outcome-number-113)

:white_check_mark:Pass outcome
#### Subject detail
|Name|module-src-core-modelet-manufacturing-environments-discover-organization|
|----|----|
|Title|Merged&#32;module&#32;src/core.ttl&#32;from&#32;branch&#32;HEAD&#32;with&#32;related&#32;terms&#32;from&#32;the&#32;fragments&#32;domains/manufacturing-environments/discover-organization/onto.ttl|
|Composition|- [Modelet manufacturing-environments/discover-organization](https://github.com/HyperAgents/hmas/blob/HEAD/domains/manufacturing-environments/discover-organization/onto.ttl)<br/>- [Module core](https://github.com/HyperAgents/hmas/blob/HEAD/src/core.ttl)|

#### Criterion detail
|Identifier|[proper-extension-predicate](https://ns.inria.fr/olivaw#proper-extension-predicate)|
|----|----|
|Title|Predicate&#32;extension&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;test&#32;the&#32;proper&#32;use&#32;of&#32;predicates&#32;rdfs:subClassOf&#32;and&#32;rdfs:subPropertyOf&#32;on&#32;the&#32;ontology&#32;terms|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-112)|Identifier|`property-subclassof`|
|[Section top](#pass-outcome-number-112)|Title|No&#32;property&#32;subclass|
|[Section top](#pass-outcome-number-112)|Description|No&#32;ontology&#32;property&#32;is&#32;a&#32;subclass|

***
### Pass Outcome number 113

[Jump to summary definition](#summary-Pass-113)	|	[Previous Pass outcome](#pass-outcome-number-112)	|	[Next Pass outcome](#pass-outcome-number-114)

:white_check_mark:Pass outcome
#### Subject detail
|Name|module-src-core-modelet-manufacturing-environments-discover-organization|
|----|----|
|Title|Merged&#32;module&#32;src/core.ttl&#32;from&#32;branch&#32;HEAD&#32;with&#32;related&#32;terms&#32;from&#32;the&#32;fragments&#32;domains/manufacturing-environments/discover-organization/onto.ttl|
|Composition|- [Modelet manufacturing-environments/discover-organization](https://github.com/HyperAgents/hmas/blob/HEAD/domains/manufacturing-environments/discover-organization/onto.ttl)<br/>- [Module core](https://github.com/HyperAgents/hmas/blob/HEAD/src/core.ttl)|

#### Criterion detail
|Identifier|[proper-extension-predicate](https://ns.inria.fr/olivaw#proper-extension-predicate)|
|----|----|
|Title|Predicate&#32;extension&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;test&#32;the&#32;proper&#32;use&#32;of&#32;predicates&#32;rdfs:subClassOf&#32;and&#32;rdfs:subPropertyOf&#32;on&#32;the&#32;ontology&#32;terms|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-113)|Identifier|`subclassof-property`|
|[Section top](#pass-outcome-number-113)|Title|No&#32;subclass&#32;of&#32;property|
|[Section top](#pass-outcome-number-113)|Description|No&#32;ontology&#32;term&#32;is&#32;a&#32;subclass&#32;of&#32;a&#32;property|

***
### Pass Outcome number 114

[Jump to summary definition](#summary-Pass-114)	|	[Previous Pass outcome](#pass-outcome-number-113)	|	[Next Pass outcome](#pass-outcome-number-115)

:white_check_mark:Pass outcome
#### Subject detail
|Name|module-src-core-modelet-manufacturing-environments-discover-organization|
|----|----|
|Title|Merged&#32;module&#32;src/core.ttl&#32;from&#32;branch&#32;HEAD&#32;with&#32;related&#32;terms&#32;from&#32;the&#32;fragments&#32;domains/manufacturing-environments/discover-organization/onto.ttl|
|Composition|- [Modelet manufacturing-environments/discover-organization](https://github.com/HyperAgents/hmas/blob/HEAD/domains/manufacturing-environments/discover-organization/onto.ttl)<br/>- [Module core](https://github.com/HyperAgents/hmas/blob/HEAD/src/core.ttl)|

#### Criterion detail
|Identifier|[proper-extension-predicate](https://ns.inria.fr/olivaw#proper-extension-predicate)|
|----|----|
|Title|Predicate&#32;extension&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;test&#32;the&#32;proper&#32;use&#32;of&#32;predicates&#32;rdfs:subClassOf&#32;and&#32;rdfs:subPropertyOf&#32;on&#32;the&#32;ontology&#32;terms|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-114)|Identifier|`subpropertyof-class`|
|[Section top](#pass-outcome-number-114)|Title|No&#32;subproperty&#32;of&#32;class|
|[Section top](#pass-outcome-number-114)|Description|No&#32;ontology&#32;term&#32;is&#32;a&#32;subproperty&#32;of&#32;a&#32;class|

***
### Pass Outcome number 115

[Jump to summary definition](#summary-Pass-115)	|	[Previous Pass outcome](#pass-outcome-number-114)	|	[Next Pass outcome](#pass-outcome-number-116)

:white_check_mark:Pass outcome
#### Subject detail
|Name|module-src-core-modelet-manufacturing-environments-discover-organization|
|----|----|
|Title|Merged&#32;module&#32;src/core.ttl&#32;from&#32;branch&#32;HEAD&#32;with&#32;related&#32;terms&#32;from&#32;the&#32;fragments&#32;domains/manufacturing-environments/discover-organization/onto.ttl|
|Composition|- [Modelet manufacturing-environments/discover-organization](https://github.com/HyperAgents/hmas/blob/HEAD/domains/manufacturing-environments/discover-organization/onto.ttl)<br/>- [Module core](https://github.com/HyperAgents/hmas/blob/HEAD/src/core.ttl)|

#### Criterion detail
|Identifier|[term-referencing](https://ns.inria.fr/olivaw#term-referencing)|
|----|----|
|Title|Term&#32;referencing&#32;test|
|Description|A&#32;test&#32;case&#32;from&#32;the&#32;Best&#32;Practices&#32;tests&#32;checking&#32;if&#32;each&#32;term&#32;of&#32;the&#32;test&#32;subject&#32;is&#32;referenced&#32;to&#32;a&#32;module&#32;through&#32;a&#32;rdfs:isDefinedBy&#32;property.|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-115)|Identifier|`no-reference-module`|
|[Section top](#pass-outcome-number-115)|Title|Any&#32;term&#32;is&#32;referenced|
|[Section top](#pass-outcome-number-115)|Description|Each&#32;term&#32;of&#32;the&#32;test&#32;subject&#32;is&#32;linked&#32;to&#32;a&#32;module&#32;by&#32;a&#32;rdfs:isDefinedBy&#32;property|

***
### Pass Outcome number 116

[Jump to summary definition](#summary-Pass-116)	|	[Previous Pass outcome](#pass-outcome-number-115)	|	[Next Pass outcome](#pass-outcome-number-117)

:white_check_mark:Pass outcome
#### Subject detail
|Name|module-src-core-modelet-manufacturing-environments-discover-organization|
|----|----|
|Title|Merged&#32;module&#32;src/core.ttl&#32;from&#32;branch&#32;HEAD&#32;with&#32;related&#32;terms&#32;from&#32;the&#32;fragments&#32;domains/manufacturing-environments/discover-organization/onto.ttl|
|Composition|- [Modelet manufacturing-environments/discover-organization](https://github.com/HyperAgents/hmas/blob/HEAD/domains/manufacturing-environments/discover-organization/onto.ttl)<br/>- [Module core](https://github.com/HyperAgents/hmas/blob/HEAD/src/core.ttl)|

#### Criterion detail
|Identifier|[terms-differenciation](https://ns.inria.fr/olivaw#terms-differenciation)|
|----|----|
|Title|Terms&#32;differenciation&#32;test|
|Description|A&#32;test&#32;case&#32;from&#32;the&#32;Best&#32;Practices&#32;tests&#32;checking&#32;if&#32;all&#32;the&#32;terms&#32;are&#32;different&#32;enough&#32;from&#32;each&#32;other&#32;according&#32;to&#32;the&#32;Levenshtein&#32;distance&#32;metric.|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-116)|Identifier|`too-close-terms`|
|[Section top](#pass-outcome-number-116)|Title|Terms&#32;differenciated&#32;enough|
|[Section top](#pass-outcome-number-116)|Description|All&#32;the&#32;terms&#32;have&#32;have&#32;a&#32;satisfying&#32;Levenshtein&#32;distance&#32;from&#32;each&#32;other&#32;term.|

***
### Pass Outcome number 117

[Jump to summary definition](#summary-Pass-117)	|	[Previous Pass outcome](#pass-outcome-number-116)	|	[Next Pass outcome](#pass-outcome-number-118)

:white_check_mark:Pass outcome
#### Subject detail
|Name|module-src-core-modelet-manufacturing-environments-discover-core|
|----|----|
|Title|Merged&#32;module&#32;src/core.ttl&#32;from&#32;branch&#32;HEAD&#32;with&#32;related&#32;terms&#32;from&#32;the&#32;fragments&#32;domains/manufacturing-environments/discover-core/onto.ttl|
|Composition|- [Modelet manufacturing-environments/discover-core](https://github.com/HyperAgents/hmas/blob/HEAD/domains/manufacturing-environments/discover-core/onto.ttl)<br/>- [Module core](https://github.com/HyperAgents/hmas/blob/HEAD/src/core.ttl)|

#### Criterion detail
|Identifier|[domain-and-range-referencing](https://ns.inria.fr/olivaw#domain-and-range-referencing)|
|----|----|
|Title|Domain&#32;and&#32;range&#32;referencing&#32;test|
|Description|A&#32;test&#32;case&#32;from&#32;the&#32;Best&#32;Practices&#32;tests&#32;checking&#32;if&#32;all&#32;the&#32;ranges&#32;and&#32;domains&#32;from&#32;the&#32;test&#32;subject&#32;point&#32;to&#32;terms&#32;that&#32;are&#32;defined&#32;in&#32;the&#32;vocabulary.|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-117)|Identifier|`domain-out-of-vocabulary`|
|[Section top](#pass-outcome-number-117)|Title|Domains&#32;properly&#32;defined|
|[Section top](#pass-outcome-number-117)|Description|Each&#32;rdfs:domain&#32;is&#32;defined&#32;within&#32;the&#32;fragment|

***
### Pass Outcome number 118

[Jump to summary definition](#summary-Pass-118)	|	[Previous Pass outcome](#pass-outcome-number-117)	|	[Next Pass outcome](#pass-outcome-number-119)

:white_check_mark:Pass outcome
#### Subject detail
|Name|module-src-core-modelet-manufacturing-environments-discover-core|
|----|----|
|Title|Merged&#32;module&#32;src/core.ttl&#32;from&#32;branch&#32;HEAD&#32;with&#32;related&#32;terms&#32;from&#32;the&#32;fragments&#32;domains/manufacturing-environments/discover-core/onto.ttl|
|Composition|- [Modelet manufacturing-environments/discover-core](https://github.com/HyperAgents/hmas/blob/HEAD/domains/manufacturing-environments/discover-core/onto.ttl)<br/>- [Module core](https://github.com/HyperAgents/hmas/blob/HEAD/src/core.ttl)|

#### Criterion detail
|Identifier|[domain-and-range-referencing](https://ns.inria.fr/olivaw#domain-and-range-referencing)|
|----|----|
|Title|Domain&#32;and&#32;range&#32;referencing&#32;test|
|Description|A&#32;test&#32;case&#32;from&#32;the&#32;Best&#32;Practices&#32;tests&#32;checking&#32;if&#32;all&#32;the&#32;ranges&#32;and&#32;domains&#32;from&#32;the&#32;test&#32;subject&#32;point&#32;to&#32;terms&#32;that&#32;are&#32;defined&#32;in&#32;the&#32;vocabulary.|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-118)|Identifier|`range-out-of-vocabulary`|
|[Section top](#pass-outcome-number-118)|Title|Ranges&#32;properly&#32;defined|
|[Section top](#pass-outcome-number-118)|Description|Each&#32;rdfs:range&#32;is&#32;defined&#32;within&#32;the&#32;fragment|

***
### Pass Outcome number 119

[Jump to summary definition](#summary-Pass-119)	|	[Previous Pass outcome](#pass-outcome-number-118)	|	[Next Pass outcome](#pass-outcome-number-120)

:white_check_mark:Pass outcome
#### Subject detail
|Name|module-src-core-modelet-manufacturing-environments-discover-core|
|----|----|
|Title|Merged&#32;module&#32;src/core.ttl&#32;from&#32;branch&#32;HEAD&#32;with&#32;related&#32;terms&#32;from&#32;the&#32;fragments&#32;domains/manufacturing-environments/discover-core/onto.ttl|
|Composition|- [Modelet manufacturing-environments/discover-core](https://github.com/HyperAgents/hmas/blob/HEAD/domains/manufacturing-environments/discover-core/onto.ttl)<br/>- [Module core](https://github.com/HyperAgents/hmas/blob/HEAD/src/core.ttl)|

#### Criterion detail
|Identifier|[owl-rl-constraint](https://ns.inria.fr/olivaw#owl-rl-constraint)|
|----|----|
|Title|OWL&#32;RL&#32;Constraint&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;check&#32;wether&#32;the&#32;test&#32;subject&#32;is&#32;syntaxically&#32;correct&#32;or&#32;not.|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-119)|Identifier|`owl-rl-constraint-violation`|
|[Section top](#pass-outcome-number-119)|Title|OWL&#32;RL&#32;consistent|
|[Section top](#pass-outcome-number-119)|Description|The&#32;provided&#32;graph&#32;is&#32;consistent&#32;for&#32;any&#32;OWL&#32;RL&#32;constraint|

***
### Pass Outcome number 120

[Jump to summary definition](#summary-Pass-120)	|	[Previous Pass outcome](#pass-outcome-number-119)	|	[Next Pass outcome](#pass-outcome-number-121)

:white_check_mark:Pass outcome
#### Subject detail
|Name|module-src-core-modelet-manufacturing-environments-discover-core|
|----|----|
|Title|Merged&#32;module&#32;src/core.ttl&#32;from&#32;branch&#32;HEAD&#32;with&#32;related&#32;terms&#32;from&#32;the&#32;fragments&#32;domains/manufacturing-environments/discover-core/onto.ttl|
|Composition|- [Modelet manufacturing-environments/discover-core](https://github.com/HyperAgents/hmas/blob/HEAD/domains/manufacturing-environments/discover-core/onto.ttl)<br/>- [Module core](https://github.com/HyperAgents/hmas/blob/HEAD/src/core.ttl)|

#### Criterion detail
|Identifier|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|
|----|----|
|Title|Profile&#32;compatibility&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;check&#32;whether&#32;the&#32;test&#32;subject&#32;is&#32;compatible&#32;with&#32;a&#32;profile&#32;or&#32;not,&#32;and&#32;if&#32;it&#32;is&#32;not,&#32;why.|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-120)|Identifier|`owl-rl-profile-error`|
|[Section top](#pass-outcome-number-120)|Title|OWL&#32;RL&#32;Profile&#32;compatible|
|[Section top](#pass-outcome-number-120)|Description|The&#32;subject&#32;is&#32;included&#32;in&#32;the&#32;OWL&#32;RL&#32;sublanguage|

***
### Pass Outcome number 121

[Jump to summary definition](#summary-Pass-121)	|	[Previous Pass outcome](#pass-outcome-number-120)	|	[Next Pass outcome](#pass-outcome-number-122)

:white_check_mark:Pass outcome
#### Subject detail
|Name|module-src-core-modelet-manufacturing-environments-discover-core|
|----|----|
|Title|Merged&#32;module&#32;src/core.ttl&#32;from&#32;branch&#32;HEAD&#32;with&#32;related&#32;terms&#32;from&#32;the&#32;fragments&#32;domains/manufacturing-environments/discover-core/onto.ttl|
|Composition|- [Modelet manufacturing-environments/discover-core](https://github.com/HyperAgents/hmas/blob/HEAD/domains/manufacturing-environments/discover-core/onto.ttl)<br/>- [Module core](https://github.com/HyperAgents/hmas/blob/HEAD/src/core.ttl)|

#### Criterion detail
|Identifier|[proper-extension-predicate](https://ns.inria.fr/olivaw#proper-extension-predicate)|
|----|----|
|Title|Predicate&#32;extension&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;test&#32;the&#32;proper&#32;use&#32;of&#32;predicates&#32;rdfs:subClassOf&#32;and&#32;rdfs:subPropertyOf&#32;on&#32;the&#32;ontology&#32;terms|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-121)|Identifier|`class-subpropertyof`|
|[Section top](#pass-outcome-number-121)|Title|No&#32;class&#32;subproperty|
|[Section top](#pass-outcome-number-121)|Description|No&#32;ontology&#32;class&#32;is&#32;a&#32;subproperty|

***
### Pass Outcome number 122

[Jump to summary definition](#summary-Pass-122)	|	[Previous Pass outcome](#pass-outcome-number-121)	|	[Next Pass outcome](#pass-outcome-number-123)

:white_check_mark:Pass outcome
#### Subject detail
|Name|module-src-core-modelet-manufacturing-environments-discover-core|
|----|----|
|Title|Merged&#32;module&#32;src/core.ttl&#32;from&#32;branch&#32;HEAD&#32;with&#32;related&#32;terms&#32;from&#32;the&#32;fragments&#32;domains/manufacturing-environments/discover-core/onto.ttl|
|Composition|- [Modelet manufacturing-environments/discover-core](https://github.com/HyperAgents/hmas/blob/HEAD/domains/manufacturing-environments/discover-core/onto.ttl)<br/>- [Module core](https://github.com/HyperAgents/hmas/blob/HEAD/src/core.ttl)|

#### Criterion detail
|Identifier|[proper-extension-predicate](https://ns.inria.fr/olivaw#proper-extension-predicate)|
|----|----|
|Title|Predicate&#32;extension&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;test&#32;the&#32;proper&#32;use&#32;of&#32;predicates&#32;rdfs:subClassOf&#32;and&#32;rdfs:subPropertyOf&#32;on&#32;the&#32;ontology&#32;terms|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-122)|Identifier|`property-subclassof`|
|[Section top](#pass-outcome-number-122)|Title|No&#32;property&#32;subclass|
|[Section top](#pass-outcome-number-122)|Description|No&#32;ontology&#32;property&#32;is&#32;a&#32;subclass|

***
### Pass Outcome number 123

[Jump to summary definition](#summary-Pass-123)	|	[Previous Pass outcome](#pass-outcome-number-122)	|	[Next Pass outcome](#pass-outcome-number-124)

:white_check_mark:Pass outcome
#### Subject detail
|Name|module-src-core-modelet-manufacturing-environments-discover-core|
|----|----|
|Title|Merged&#32;module&#32;src/core.ttl&#32;from&#32;branch&#32;HEAD&#32;with&#32;related&#32;terms&#32;from&#32;the&#32;fragments&#32;domains/manufacturing-environments/discover-core/onto.ttl|
|Composition|- [Modelet manufacturing-environments/discover-core](https://github.com/HyperAgents/hmas/blob/HEAD/domains/manufacturing-environments/discover-core/onto.ttl)<br/>- [Module core](https://github.com/HyperAgents/hmas/blob/HEAD/src/core.ttl)|

#### Criterion detail
|Identifier|[proper-extension-predicate](https://ns.inria.fr/olivaw#proper-extension-predicate)|
|----|----|
|Title|Predicate&#32;extension&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;test&#32;the&#32;proper&#32;use&#32;of&#32;predicates&#32;rdfs:subClassOf&#32;and&#32;rdfs:subPropertyOf&#32;on&#32;the&#32;ontology&#32;terms|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-123)|Identifier|`subclassof-property`|
|[Section top](#pass-outcome-number-123)|Title|No&#32;subclass&#32;of&#32;property|
|[Section top](#pass-outcome-number-123)|Description|No&#32;ontology&#32;term&#32;is&#32;a&#32;subclass&#32;of&#32;a&#32;property|

***
### Pass Outcome number 124

[Jump to summary definition](#summary-Pass-124)	|	[Previous Pass outcome](#pass-outcome-number-123)	|	[Next Pass outcome](#pass-outcome-number-125)

:white_check_mark:Pass outcome
#### Subject detail
|Name|module-src-core-modelet-manufacturing-environments-discover-core|
|----|----|
|Title|Merged&#32;module&#32;src/core.ttl&#32;from&#32;branch&#32;HEAD&#32;with&#32;related&#32;terms&#32;from&#32;the&#32;fragments&#32;domains/manufacturing-environments/discover-core/onto.ttl|
|Composition|- [Modelet manufacturing-environments/discover-core](https://github.com/HyperAgents/hmas/blob/HEAD/domains/manufacturing-environments/discover-core/onto.ttl)<br/>- [Module core](https://github.com/HyperAgents/hmas/blob/HEAD/src/core.ttl)|

#### Criterion detail
|Identifier|[proper-extension-predicate](https://ns.inria.fr/olivaw#proper-extension-predicate)|
|----|----|
|Title|Predicate&#32;extension&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;test&#32;the&#32;proper&#32;use&#32;of&#32;predicates&#32;rdfs:subClassOf&#32;and&#32;rdfs:subPropertyOf&#32;on&#32;the&#32;ontology&#32;terms|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-124)|Identifier|`subpropertyof-class`|
|[Section top](#pass-outcome-number-124)|Title|No&#32;subproperty&#32;of&#32;class|
|[Section top](#pass-outcome-number-124)|Description|No&#32;ontology&#32;term&#32;is&#32;a&#32;subproperty&#32;of&#32;a&#32;class|

***
### Pass Outcome number 125

[Jump to summary definition](#summary-Pass-125)	|	[Previous Pass outcome](#pass-outcome-number-124)	|	[Next Pass outcome](#pass-outcome-number-126)

:white_check_mark:Pass outcome
#### Subject detail
|Name|module-src-core-modelet-manufacturing-environments-discover-core|
|----|----|
|Title|Merged&#32;module&#32;src/core.ttl&#32;from&#32;branch&#32;HEAD&#32;with&#32;related&#32;terms&#32;from&#32;the&#32;fragments&#32;domains/manufacturing-environments/discover-core/onto.ttl|
|Composition|- [Modelet manufacturing-environments/discover-core](https://github.com/HyperAgents/hmas/blob/HEAD/domains/manufacturing-environments/discover-core/onto.ttl)<br/>- [Module core](https://github.com/HyperAgents/hmas/blob/HEAD/src/core.ttl)|

#### Criterion detail
|Identifier|[term-referencing](https://ns.inria.fr/olivaw#term-referencing)|
|----|----|
|Title|Term&#32;referencing&#32;test|
|Description|A&#32;test&#32;case&#32;from&#32;the&#32;Best&#32;Practices&#32;tests&#32;checking&#32;if&#32;each&#32;term&#32;of&#32;the&#32;test&#32;subject&#32;is&#32;referenced&#32;to&#32;a&#32;module&#32;through&#32;a&#32;rdfs:isDefinedBy&#32;property.|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-125)|Identifier|`no-reference-module`|
|[Section top](#pass-outcome-number-125)|Title|Any&#32;term&#32;is&#32;referenced|
|[Section top](#pass-outcome-number-125)|Description|Each&#32;term&#32;of&#32;the&#32;test&#32;subject&#32;is&#32;linked&#32;to&#32;a&#32;module&#32;by&#32;a&#32;rdfs:isDefinedBy&#32;property|

***
### Pass Outcome number 126

[Jump to summary definition](#summary-Pass-126)	|	[Previous Pass outcome](#pass-outcome-number-125)	|	[Next Pass outcome](#pass-outcome-number-127)

:white_check_mark:Pass outcome
#### Subject detail
|Name|module-src-core-modelet-manufacturing-environments-discover-core|
|----|----|
|Title|Merged&#32;module&#32;src/core.ttl&#32;from&#32;branch&#32;HEAD&#32;with&#32;related&#32;terms&#32;from&#32;the&#32;fragments&#32;domains/manufacturing-environments/discover-core/onto.ttl|
|Composition|- [Modelet manufacturing-environments/discover-core](https://github.com/HyperAgents/hmas/blob/HEAD/domains/manufacturing-environments/discover-core/onto.ttl)<br/>- [Module core](https://github.com/HyperAgents/hmas/blob/HEAD/src/core.ttl)|

#### Criterion detail
|Identifier|[terms-differenciation](https://ns.inria.fr/olivaw#terms-differenciation)|
|----|----|
|Title|Terms&#32;differenciation&#32;test|
|Description|A&#32;test&#32;case&#32;from&#32;the&#32;Best&#32;Practices&#32;tests&#32;checking&#32;if&#32;all&#32;the&#32;terms&#32;are&#32;different&#32;enough&#32;from&#32;each&#32;other&#32;according&#32;to&#32;the&#32;Levenshtein&#32;distance&#32;metric.|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-126)|Identifier|`too-close-terms`|
|[Section top](#pass-outcome-number-126)|Title|Terms&#32;differenciated&#32;enough|
|[Section top](#pass-outcome-number-126)|Description|All&#32;the&#32;terms&#32;have&#32;have&#32;a&#32;satisfying&#32;Levenshtein&#32;distance&#32;from&#32;each&#32;other&#32;term.|

***
### Pass Outcome number 127

[Jump to summary definition](#summary-Pass-127)	|	[Previous Pass outcome](#pass-outcome-number-126)	|	[Next Pass outcome](#pass-outcome-number-128)

:white_check_mark:Pass outcome
#### Subject detail
|Name|module-src-core|
|----|----|
|Title|Standalone&#32;module&#32;src/core.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Module core](https://github.com/HyperAgents/hmas/blob/HEAD/src/core.ttl)|

#### Criterion detail
|Identifier|[domain-and-range-referencing](https://ns.inria.fr/olivaw#domain-and-range-referencing)|
|----|----|
|Title|Domain&#32;and&#32;range&#32;referencing&#32;test|
|Description|A&#32;test&#32;case&#32;from&#32;the&#32;Best&#32;Practices&#32;tests&#32;checking&#32;if&#32;all&#32;the&#32;ranges&#32;and&#32;domains&#32;from&#32;the&#32;test&#32;subject&#32;point&#32;to&#32;terms&#32;that&#32;are&#32;defined&#32;in&#32;the&#32;vocabulary.|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-127)|Identifier|`domain-out-of-vocabulary`|
|[Section top](#pass-outcome-number-127)|Title|Domains&#32;properly&#32;defined|
|[Section top](#pass-outcome-number-127)|Description|Each&#32;rdfs:domain&#32;is&#32;defined&#32;within&#32;the&#32;fragment|

***
### Pass Outcome number 128

[Jump to summary definition](#summary-Pass-128)	|	[Previous Pass outcome](#pass-outcome-number-127)	|	[Next Pass outcome](#pass-outcome-number-129)

:white_check_mark:Pass outcome
#### Subject detail
|Name|module-src-core|
|----|----|
|Title|Standalone&#32;module&#32;src/core.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Module core](https://github.com/HyperAgents/hmas/blob/HEAD/src/core.ttl)|

#### Criterion detail
|Identifier|[domain-and-range-referencing](https://ns.inria.fr/olivaw#domain-and-range-referencing)|
|----|----|
|Title|Domain&#32;and&#32;range&#32;referencing&#32;test|
|Description|A&#32;test&#32;case&#32;from&#32;the&#32;Best&#32;Practices&#32;tests&#32;checking&#32;if&#32;all&#32;the&#32;ranges&#32;and&#32;domains&#32;from&#32;the&#32;test&#32;subject&#32;point&#32;to&#32;terms&#32;that&#32;are&#32;defined&#32;in&#32;the&#32;vocabulary.|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-128)|Identifier|`range-out-of-vocabulary`|
|[Section top](#pass-outcome-number-128)|Title|Ranges&#32;properly&#32;defined|
|[Section top](#pass-outcome-number-128)|Description|Each&#32;rdfs:range&#32;is&#32;defined&#32;within&#32;the&#32;fragment|

***
### Pass Outcome number 129

[Jump to summary definition](#summary-Pass-129)	|	[Previous Pass outcome](#pass-outcome-number-128)	|	[Next Pass outcome](#pass-outcome-number-130)

:white_check_mark:Pass outcome
#### Subject detail
|Name|module-src-core|
|----|----|
|Title|Standalone&#32;module&#32;src/core.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Module core](https://github.com/HyperAgents/hmas/blob/HEAD/src/core.ttl)|

#### Criterion detail
|Identifier|[owl-rl-constraint](https://ns.inria.fr/olivaw#owl-rl-constraint)|
|----|----|
|Title|OWL&#32;RL&#32;Constraint&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;check&#32;wether&#32;the&#32;test&#32;subject&#32;is&#32;syntaxically&#32;correct&#32;or&#32;not.|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-129)|Identifier|`owl-rl-constraint-violation`|
|[Section top](#pass-outcome-number-129)|Title|OWL&#32;RL&#32;consistent|
|[Section top](#pass-outcome-number-129)|Description|The&#32;provided&#32;graph&#32;is&#32;consistent&#32;for&#32;any&#32;OWL&#32;RL&#32;constraint|

***
### Pass Outcome number 130

[Jump to summary definition](#summary-Pass-130)	|	[Previous Pass outcome](#pass-outcome-number-129)	|	[Next Pass outcome](#pass-outcome-number-131)

:white_check_mark:Pass outcome
#### Subject detail
|Name|module-src-core|
|----|----|
|Title|Standalone&#32;module&#32;src/core.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Module core](https://github.com/HyperAgents/hmas/blob/HEAD/src/core.ttl)|

#### Criterion detail
|Identifier|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|
|----|----|
|Title|Profile&#32;compatibility&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;check&#32;whether&#32;the&#32;test&#32;subject&#32;is&#32;compatible&#32;with&#32;a&#32;profile&#32;or&#32;not,&#32;and&#32;if&#32;it&#32;is&#32;not,&#32;why.|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-130)|Identifier|`owl-rl-profile-error`|
|[Section top](#pass-outcome-number-130)|Title|OWL&#32;RL&#32;Profile&#32;compatible|
|[Section top](#pass-outcome-number-130)|Description|The&#32;subject&#32;is&#32;included&#32;in&#32;the&#32;OWL&#32;RL&#32;sublanguage|

***
### Pass Outcome number 131

[Jump to summary definition](#summary-Pass-131)	|	[Previous Pass outcome](#pass-outcome-number-130)	|	[Next Pass outcome](#pass-outcome-number-132)

:white_check_mark:Pass outcome
#### Subject detail
|Name|module-src-core|
|----|----|
|Title|Standalone&#32;module&#32;src/core.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Module core](https://github.com/HyperAgents/hmas/blob/HEAD/src/core.ttl)|

#### Criterion detail
|Identifier|[proper-extension-predicate](https://ns.inria.fr/olivaw#proper-extension-predicate)|
|----|----|
|Title|Predicate&#32;extension&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;test&#32;the&#32;proper&#32;use&#32;of&#32;predicates&#32;rdfs:subClassOf&#32;and&#32;rdfs:subPropertyOf&#32;on&#32;the&#32;ontology&#32;terms|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-131)|Identifier|`class-subpropertyof`|
|[Section top](#pass-outcome-number-131)|Title|No&#32;class&#32;subproperty|
|[Section top](#pass-outcome-number-131)|Description|No&#32;ontology&#32;class&#32;is&#32;a&#32;subproperty|

***
### Pass Outcome number 132

[Jump to summary definition](#summary-Pass-132)	|	[Previous Pass outcome](#pass-outcome-number-131)	|	[Next Pass outcome](#pass-outcome-number-133)

:white_check_mark:Pass outcome
#### Subject detail
|Name|module-src-core|
|----|----|
|Title|Standalone&#32;module&#32;src/core.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Module core](https://github.com/HyperAgents/hmas/blob/HEAD/src/core.ttl)|

#### Criterion detail
|Identifier|[proper-extension-predicate](https://ns.inria.fr/olivaw#proper-extension-predicate)|
|----|----|
|Title|Predicate&#32;extension&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;test&#32;the&#32;proper&#32;use&#32;of&#32;predicates&#32;rdfs:subClassOf&#32;and&#32;rdfs:subPropertyOf&#32;on&#32;the&#32;ontology&#32;terms|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-132)|Identifier|`property-subclassof`|
|[Section top](#pass-outcome-number-132)|Title|No&#32;property&#32;subclass|
|[Section top](#pass-outcome-number-132)|Description|No&#32;ontology&#32;property&#32;is&#32;a&#32;subclass|

***
### Pass Outcome number 133

[Jump to summary definition](#summary-Pass-133)	|	[Previous Pass outcome](#pass-outcome-number-132)	|	[Next Pass outcome](#pass-outcome-number-134)

:white_check_mark:Pass outcome
#### Subject detail
|Name|module-src-core|
|----|----|
|Title|Standalone&#32;module&#32;src/core.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Module core](https://github.com/HyperAgents/hmas/blob/HEAD/src/core.ttl)|

#### Criterion detail
|Identifier|[proper-extension-predicate](https://ns.inria.fr/olivaw#proper-extension-predicate)|
|----|----|
|Title|Predicate&#32;extension&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;test&#32;the&#32;proper&#32;use&#32;of&#32;predicates&#32;rdfs:subClassOf&#32;and&#32;rdfs:subPropertyOf&#32;on&#32;the&#32;ontology&#32;terms|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-133)|Identifier|`subclassof-property`|
|[Section top](#pass-outcome-number-133)|Title|No&#32;subclass&#32;of&#32;property|
|[Section top](#pass-outcome-number-133)|Description|No&#32;ontology&#32;term&#32;is&#32;a&#32;subclass&#32;of&#32;a&#32;property|

***
### Pass Outcome number 134

[Jump to summary definition](#summary-Pass-134)	|	[Previous Pass outcome](#pass-outcome-number-133)	|	[Next Pass outcome](#pass-outcome-number-135)

:white_check_mark:Pass outcome
#### Subject detail
|Name|module-src-core|
|----|----|
|Title|Standalone&#32;module&#32;src/core.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Module core](https://github.com/HyperAgents/hmas/blob/HEAD/src/core.ttl)|

#### Criterion detail
|Identifier|[proper-extension-predicate](https://ns.inria.fr/olivaw#proper-extension-predicate)|
|----|----|
|Title|Predicate&#32;extension&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;test&#32;the&#32;proper&#32;use&#32;of&#32;predicates&#32;rdfs:subClassOf&#32;and&#32;rdfs:subPropertyOf&#32;on&#32;the&#32;ontology&#32;terms|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-134)|Identifier|`subpropertyof-class`|
|[Section top](#pass-outcome-number-134)|Title|No&#32;subproperty&#32;of&#32;class|
|[Section top](#pass-outcome-number-134)|Description|No&#32;ontology&#32;term&#32;is&#32;a&#32;subproperty&#32;of&#32;a&#32;class|

***
### Pass Outcome number 135

[Jump to summary definition](#summary-Pass-135)	|	[Previous Pass outcome](#pass-outcome-number-134)	|	[Next Pass outcome](#pass-outcome-number-136)

:white_check_mark:Pass outcome
#### Subject detail
|Name|module-src-core|
|----|----|
|Title|Standalone&#32;module&#32;src/core.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Module core](https://github.com/HyperAgents/hmas/blob/HEAD/src/core.ttl)|

#### Criterion detail
|Identifier|[term-referencing](https://ns.inria.fr/olivaw#term-referencing)|
|----|----|
|Title|Term&#32;referencing&#32;test|
|Description|A&#32;test&#32;case&#32;from&#32;the&#32;Best&#32;Practices&#32;tests&#32;checking&#32;if&#32;each&#32;term&#32;of&#32;the&#32;test&#32;subject&#32;is&#32;referenced&#32;to&#32;a&#32;module&#32;through&#32;a&#32;rdfs:isDefinedBy&#32;property.|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-135)|Identifier|`no-reference-module`|
|[Section top](#pass-outcome-number-135)|Title|Any&#32;term&#32;is&#32;referenced|
|[Section top](#pass-outcome-number-135)|Description|Each&#32;term&#32;of&#32;the&#32;test&#32;subject&#32;is&#32;linked&#32;to&#32;a&#32;module&#32;by&#32;a&#32;rdfs:isDefinedBy&#32;property|

***
### Pass Outcome number 136

[Jump to summary definition](#summary-Pass-136)	|	[Previous Pass outcome](#pass-outcome-number-135)	|	[Next Pass outcome](#pass-outcome-number-137)

:white_check_mark:Pass outcome
#### Subject detail
|Name|module-src-core|
|----|----|
|Title|Standalone&#32;module&#32;src/core.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Module core](https://github.com/HyperAgents/hmas/blob/HEAD/src/core.ttl)|

#### Criterion detail
|Identifier|[terms-differenciation](https://ns.inria.fr/olivaw#terms-differenciation)|
|----|----|
|Title|Terms&#32;differenciation&#32;test|
|Description|A&#32;test&#32;case&#32;from&#32;the&#32;Best&#32;Practices&#32;tests&#32;checking&#32;if&#32;all&#32;the&#32;terms&#32;are&#32;different&#32;enough&#32;from&#32;each&#32;other&#32;according&#32;to&#32;the&#32;Levenshtein&#32;distance&#32;metric.|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-136)|Identifier|`too-close-terms`|
|[Section top](#pass-outcome-number-136)|Title|Terms&#32;differenciated&#32;enough|
|[Section top](#pass-outcome-number-136)|Description|All&#32;the&#32;terms&#32;have&#32;have&#32;a&#32;satisfying&#32;Levenshtein&#32;distance&#32;from&#32;each&#32;other&#32;term.|

***
### Pass Outcome number 137

[Jump to summary definition](#summary-Pass-137)	|	[Previous Pass outcome](#pass-outcome-number-136)	|	[Next Pass outcome](#pass-outcome-number-138)

:white_check_mark:Pass outcome
#### Subject detail
|Name|module-src-alignment-interaction-td|
|----|----|
|Title|Standalone&#32;module&#32;src/alignment/interaction-td.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Module alignment/interaction-td](https://github.com/HyperAgents/hmas/blob/HEAD/src/alignment/interaction-td.ttl)|

#### Criterion detail
|Identifier|[domain-and-range-referencing](https://ns.inria.fr/olivaw#domain-and-range-referencing)|
|----|----|
|Title|Domain&#32;and&#32;range&#32;referencing&#32;test|
|Description|A&#32;test&#32;case&#32;from&#32;the&#32;Best&#32;Practices&#32;tests&#32;checking&#32;if&#32;all&#32;the&#32;ranges&#32;and&#32;domains&#32;from&#32;the&#32;test&#32;subject&#32;point&#32;to&#32;terms&#32;that&#32;are&#32;defined&#32;in&#32;the&#32;vocabulary.|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-137)|Identifier|`domain-out-of-vocabulary`|
|[Section top](#pass-outcome-number-137)|Title|Domains&#32;properly&#32;defined|
|[Section top](#pass-outcome-number-137)|Description|Each&#32;rdfs:domain&#32;is&#32;defined&#32;within&#32;the&#32;fragment|

***
### Pass Outcome number 138

[Jump to summary definition](#summary-Pass-138)	|	[Previous Pass outcome](#pass-outcome-number-137)	|	[Next Pass outcome](#pass-outcome-number-139)

:white_check_mark:Pass outcome
#### Subject detail
|Name|module-src-alignment-interaction-td|
|----|----|
|Title|Standalone&#32;module&#32;src/alignment/interaction-td.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Module alignment/interaction-td](https://github.com/HyperAgents/hmas/blob/HEAD/src/alignment/interaction-td.ttl)|

#### Criterion detail
|Identifier|[domain-and-range-referencing](https://ns.inria.fr/olivaw#domain-and-range-referencing)|
|----|----|
|Title|Domain&#32;and&#32;range&#32;referencing&#32;test|
|Description|A&#32;test&#32;case&#32;from&#32;the&#32;Best&#32;Practices&#32;tests&#32;checking&#32;if&#32;all&#32;the&#32;ranges&#32;and&#32;domains&#32;from&#32;the&#32;test&#32;subject&#32;point&#32;to&#32;terms&#32;that&#32;are&#32;defined&#32;in&#32;the&#32;vocabulary.|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-138)|Identifier|`range-out-of-vocabulary`|
|[Section top](#pass-outcome-number-138)|Title|Ranges&#32;properly&#32;defined|
|[Section top](#pass-outcome-number-138)|Description|Each&#32;rdfs:range&#32;is&#32;defined&#32;within&#32;the&#32;fragment|

***
### Pass Outcome number 139

[Jump to summary definition](#summary-Pass-139)	|	[Previous Pass outcome](#pass-outcome-number-138)	|	[Next Pass outcome](#pass-outcome-number-140)

:white_check_mark:Pass outcome
#### Subject detail
|Name|module-src-alignment-interaction-td|
|----|----|
|Title|Standalone&#32;module&#32;src/alignment/interaction-td.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Module alignment/interaction-td](https://github.com/HyperAgents/hmas/blob/HEAD/src/alignment/interaction-td.ttl)|

#### Criterion detail
|Identifier|[labeled-terms](https://ns.inria.fr/olivaw#labeled-terms)|
|----|----|
|Title|Term&#32;labeling&#32;test|
|Description|A&#32;test&#32;case&#32;from&#32;the&#32;Best&#32;Practices&#32;tests&#32;checking&#32;if&#32;all&#32;the&#32;terms&#32;of&#32;the&#32;subject&#32;have&#32;a&#32;rdfs:label&#32;property&#32;pointing&#32;to&#32;a&#32;literal&#32;in&#32;English|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-139)|Identifier|`not-labeled-term`|
|[Section top](#pass-outcome-number-139)|Title|All&#32;terms&#32;labeled|
|[Section top](#pass-outcome-number-139)|Description|All&#32;the&#32;terms&#32;defined&#32;in&#32;the&#32;subject&#32;have&#32;a&#32;rdfs:label&#32;in&#32;English|

***
### Pass Outcome number 140

[Jump to summary definition](#summary-Pass-140)	|	[Previous Pass outcome](#pass-outcome-number-139)	|	[Next Pass outcome](#pass-outcome-number-141)

:white_check_mark:Pass outcome
#### Subject detail
|Name|module-src-alignment-interaction-td|
|----|----|
|Title|Standalone&#32;module&#32;src/alignment/interaction-td.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Module alignment/interaction-td](https://github.com/HyperAgents/hmas/blob/HEAD/src/alignment/interaction-td.ttl)|

#### Criterion detail
|Identifier|[owl-rl-constraint](https://ns.inria.fr/olivaw#owl-rl-constraint)|
|----|----|
|Title|OWL&#32;RL&#32;Constraint&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;check&#32;wether&#32;the&#32;test&#32;subject&#32;is&#32;syntaxically&#32;correct&#32;or&#32;not.|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-140)|Identifier|`owl-rl-constraint-violation`|
|[Section top](#pass-outcome-number-140)|Title|OWL&#32;RL&#32;consistent|
|[Section top](#pass-outcome-number-140)|Description|The&#32;provided&#32;graph&#32;is&#32;consistent&#32;for&#32;any&#32;OWL&#32;RL&#32;constraint|

***
### Pass Outcome number 141

[Jump to summary definition](#summary-Pass-141)	|	[Previous Pass outcome](#pass-outcome-number-140)	|	[Next Pass outcome](#pass-outcome-number-142)

:white_check_mark:Pass outcome
#### Subject detail
|Name|module-src-alignment-interaction-td|
|----|----|
|Title|Standalone&#32;module&#32;src/alignment/interaction-td.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Module alignment/interaction-td](https://github.com/HyperAgents/hmas/blob/HEAD/src/alignment/interaction-td.ttl)|

#### Criterion detail
|Identifier|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|
|----|----|
|Title|Profile&#32;compatibility&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;check&#32;whether&#32;the&#32;test&#32;subject&#32;is&#32;compatible&#32;with&#32;a&#32;profile&#32;or&#32;not,&#32;and&#32;if&#32;it&#32;is&#32;not,&#32;why.|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-141)|Identifier|`owl-el-profile-error`|
|[Section top](#pass-outcome-number-141)|Title|OWL&#32;EL&#32;Profile&#32;compatible|
|[Section top](#pass-outcome-number-141)|Description|Statement&#32;not&#32;supported  &#10;Statement&#32;not&#32;supported&#32;in&#32;a&#32;Super&#32;Class&#32;Expression|

***
### Pass Outcome number 142

[Jump to summary definition](#summary-Pass-142)	|	[Previous Pass outcome](#pass-outcome-number-141)	|	[Next Pass outcome](#pass-outcome-number-143)

:white_check_mark:Pass outcome
#### Subject detail
|Name|module-src-alignment-interaction-td|
|----|----|
|Title|Standalone&#32;module&#32;src/alignment/interaction-td.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Module alignment/interaction-td](https://github.com/HyperAgents/hmas/blob/HEAD/src/alignment/interaction-td.ttl)|

#### Criterion detail
|Identifier|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|
|----|----|
|Title|Profile&#32;compatibility&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;check&#32;whether&#32;the&#32;test&#32;subject&#32;is&#32;compatible&#32;with&#32;a&#32;profile&#32;or&#32;not,&#32;and&#32;if&#32;it&#32;is&#32;not,&#32;why.|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-142)|Identifier|`owl-rl-profile-error`|
|[Section top](#pass-outcome-number-142)|Title|OWL&#32;RL&#32;Profile&#32;compatible|
|[Section top](#pass-outcome-number-142)|Description|The&#32;subject&#32;is&#32;included&#32;in&#32;the&#32;OWL&#32;RL&#32;sublanguage|

***
### Pass Outcome number 143

[Jump to summary definition](#summary-Pass-143)	|	[Previous Pass outcome](#pass-outcome-number-142)	|	[Next Pass outcome](#pass-outcome-number-144)

:white_check_mark:Pass outcome
#### Subject detail
|Name|module-src-alignment-interaction-td|
|----|----|
|Title|Standalone&#32;module&#32;src/alignment/interaction-td.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Module alignment/interaction-td](https://github.com/HyperAgents/hmas/blob/HEAD/src/alignment/interaction-td.ttl)|

#### Criterion detail
|Identifier|[proper-extension-predicate](https://ns.inria.fr/olivaw#proper-extension-predicate)|
|----|----|
|Title|Predicate&#32;extension&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;test&#32;the&#32;proper&#32;use&#32;of&#32;predicates&#32;rdfs:subClassOf&#32;and&#32;rdfs:subPropertyOf&#32;on&#32;the&#32;ontology&#32;terms|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-143)|Identifier|`class-subpropertyof`|
|[Section top](#pass-outcome-number-143)|Title|No&#32;class&#32;subproperty|
|[Section top](#pass-outcome-number-143)|Description|No&#32;ontology&#32;class&#32;is&#32;a&#32;subproperty|

***
### Pass Outcome number 144

[Jump to summary definition](#summary-Pass-144)	|	[Previous Pass outcome](#pass-outcome-number-143)	|	[Next Pass outcome](#pass-outcome-number-145)

:white_check_mark:Pass outcome
#### Subject detail
|Name|module-src-alignment-interaction-td|
|----|----|
|Title|Standalone&#32;module&#32;src/alignment/interaction-td.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Module alignment/interaction-td](https://github.com/HyperAgents/hmas/blob/HEAD/src/alignment/interaction-td.ttl)|

#### Criterion detail
|Identifier|[proper-extension-predicate](https://ns.inria.fr/olivaw#proper-extension-predicate)|
|----|----|
|Title|Predicate&#32;extension&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;test&#32;the&#32;proper&#32;use&#32;of&#32;predicates&#32;rdfs:subClassOf&#32;and&#32;rdfs:subPropertyOf&#32;on&#32;the&#32;ontology&#32;terms|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-144)|Identifier|`property-subclassof`|
|[Section top](#pass-outcome-number-144)|Title|No&#32;property&#32;subclass|
|[Section top](#pass-outcome-number-144)|Description|No&#32;ontology&#32;property&#32;is&#32;a&#32;subclass|

***
### Pass Outcome number 145

[Jump to summary definition](#summary-Pass-145)	|	[Previous Pass outcome](#pass-outcome-number-144)	|	[Next Pass outcome](#pass-outcome-number-146)

:white_check_mark:Pass outcome
#### Subject detail
|Name|module-src-alignment-interaction-td|
|----|----|
|Title|Standalone&#32;module&#32;src/alignment/interaction-td.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Module alignment/interaction-td](https://github.com/HyperAgents/hmas/blob/HEAD/src/alignment/interaction-td.ttl)|

#### Criterion detail
|Identifier|[proper-extension-predicate](https://ns.inria.fr/olivaw#proper-extension-predicate)|
|----|----|
|Title|Predicate&#32;extension&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;test&#32;the&#32;proper&#32;use&#32;of&#32;predicates&#32;rdfs:subClassOf&#32;and&#32;rdfs:subPropertyOf&#32;on&#32;the&#32;ontology&#32;terms|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-145)|Identifier|`subclassof-property`|
|[Section top](#pass-outcome-number-145)|Title|No&#32;subclass&#32;of&#32;property|
|[Section top](#pass-outcome-number-145)|Description|No&#32;ontology&#32;term&#32;is&#32;a&#32;subclass&#32;of&#32;a&#32;property|

***
### Pass Outcome number 146

[Jump to summary definition](#summary-Pass-146)	|	[Previous Pass outcome](#pass-outcome-number-145)	|	[Next Pass outcome](#pass-outcome-number-147)

:white_check_mark:Pass outcome
#### Subject detail
|Name|module-src-alignment-interaction-td|
|----|----|
|Title|Standalone&#32;module&#32;src/alignment/interaction-td.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Module alignment/interaction-td](https://github.com/HyperAgents/hmas/blob/HEAD/src/alignment/interaction-td.ttl)|

#### Criterion detail
|Identifier|[proper-extension-predicate](https://ns.inria.fr/olivaw#proper-extension-predicate)|
|----|----|
|Title|Predicate&#32;extension&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;test&#32;the&#32;proper&#32;use&#32;of&#32;predicates&#32;rdfs:subClassOf&#32;and&#32;rdfs:subPropertyOf&#32;on&#32;the&#32;ontology&#32;terms|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-146)|Identifier|`subpropertyof-class`|
|[Section top](#pass-outcome-number-146)|Title|No&#32;subproperty&#32;of&#32;class|
|[Section top](#pass-outcome-number-146)|Description|No&#32;ontology&#32;term&#32;is&#32;a&#32;subproperty&#32;of&#32;a&#32;class|

***
### Pass Outcome number 147

[Jump to summary definition](#summary-Pass-147)	|	[Previous Pass outcome](#pass-outcome-number-146)	|	[Next Pass outcome](#pass-outcome-number-148)

:white_check_mark:Pass outcome
#### Subject detail
|Name|module-src-alignment-interaction-td|
|----|----|
|Title|Standalone&#32;module&#32;src/alignment/interaction-td.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Module alignment/interaction-td](https://github.com/HyperAgents/hmas/blob/HEAD/src/alignment/interaction-td.ttl)|

#### Criterion detail
|Identifier|[term-referencing](https://ns.inria.fr/olivaw#term-referencing)|
|----|----|
|Title|Term&#32;referencing&#32;test|
|Description|A&#32;test&#32;case&#32;from&#32;the&#32;Best&#32;Practices&#32;tests&#32;checking&#32;if&#32;each&#32;term&#32;of&#32;the&#32;test&#32;subject&#32;is&#32;referenced&#32;to&#32;a&#32;module&#32;through&#32;a&#32;rdfs:isDefinedBy&#32;property.|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-147)|Identifier|`no-reference-module`|
|[Section top](#pass-outcome-number-147)|Title|Any&#32;term&#32;is&#32;referenced|
|[Section top](#pass-outcome-number-147)|Description|Each&#32;term&#32;of&#32;the&#32;test&#32;subject&#32;is&#32;linked&#32;to&#32;a&#32;module&#32;by&#32;a&#32;rdfs:isDefinedBy&#32;property|

***
### Pass Outcome number 148

[Jump to summary definition](#summary-Pass-148)	|	[Previous Pass outcome](#pass-outcome-number-147)	|	[Next Pass outcome](#pass-outcome-number-149)

:white_check_mark:Pass outcome
#### Subject detail
|Name|module-src-alignment-interaction-td|
|----|----|
|Title|Standalone&#32;module&#32;src/alignment/interaction-td.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Module alignment/interaction-td](https://github.com/HyperAgents/hmas/blob/HEAD/src/alignment/interaction-td.ttl)|

#### Criterion detail
|Identifier|[terms-differenciation](https://ns.inria.fr/olivaw#terms-differenciation)|
|----|----|
|Title|Terms&#32;differenciation&#32;test|
|Description|A&#32;test&#32;case&#32;from&#32;the&#32;Best&#32;Practices&#32;tests&#32;checking&#32;if&#32;all&#32;the&#32;terms&#32;are&#32;different&#32;enough&#32;from&#32;each&#32;other&#32;according&#32;to&#32;the&#32;Levenshtein&#32;distance&#32;metric.|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-148)|Identifier|`too-close-terms`|
|[Section top](#pass-outcome-number-148)|Title|Terms&#32;differenciated&#32;enough|
|[Section top](#pass-outcome-number-148)|Description|All&#32;the&#32;terms&#32;have&#32;have&#32;a&#32;satisfying&#32;Levenshtein&#32;distance&#32;from&#32;each&#32;other&#32;term.|

***
### Pass Outcome number 149

[Jump to summary definition](#summary-Pass-149)	|	[Previous Pass outcome](#pass-outcome-number-148)	|	[Next Pass outcome](#pass-outcome-number-150)

:white_check_mark:Pass outcome
#### Subject detail
|Name|modelet-manufacturing-environments-discover-signifiers|
|----|----|
|Title|Standalone&#32;modelet&#32;domains/manufacturing-environments/discover-signifiers/onto.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Modelet manufacturing-environments/discover-signifiers](https://github.com/HyperAgents/hmas/blob/HEAD/domains/manufacturing-environments/discover-signifiers/onto.ttl)|

#### Criterion detail
|Identifier|[domain-and-range-referencing](https://ns.inria.fr/olivaw#domain-and-range-referencing)|
|----|----|
|Title|Domain&#32;and&#32;range&#32;referencing&#32;test|
|Description|A&#32;test&#32;case&#32;from&#32;the&#32;Best&#32;Practices&#32;tests&#32;checking&#32;if&#32;all&#32;the&#32;ranges&#32;and&#32;domains&#32;from&#32;the&#32;test&#32;subject&#32;point&#32;to&#32;terms&#32;that&#32;are&#32;defined&#32;in&#32;the&#32;vocabulary.|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-149)|Identifier|`domain-out-of-vocabulary`|
|[Section top](#pass-outcome-number-149)|Title|Domains&#32;properly&#32;defined|
|[Section top](#pass-outcome-number-149)|Description|Each&#32;rdfs:domain&#32;is&#32;defined&#32;within&#32;the&#32;fragment|

***
### Pass Outcome number 150

[Jump to summary definition](#summary-Pass-150)	|	[Previous Pass outcome](#pass-outcome-number-149)	|	[Next Pass outcome](#pass-outcome-number-151)

:white_check_mark:Pass outcome
#### Subject detail
|Name|modelet-manufacturing-environments-discover-signifiers|
|----|----|
|Title|Standalone&#32;modelet&#32;domains/manufacturing-environments/discover-signifiers/onto.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Modelet manufacturing-environments/discover-signifiers](https://github.com/HyperAgents/hmas/blob/HEAD/domains/manufacturing-environments/discover-signifiers/onto.ttl)|

#### Criterion detail
|Identifier|[domain-and-range-referencing](https://ns.inria.fr/olivaw#domain-and-range-referencing)|
|----|----|
|Title|Domain&#32;and&#32;range&#32;referencing&#32;test|
|Description|A&#32;test&#32;case&#32;from&#32;the&#32;Best&#32;Practices&#32;tests&#32;checking&#32;if&#32;all&#32;the&#32;ranges&#32;and&#32;domains&#32;from&#32;the&#32;test&#32;subject&#32;point&#32;to&#32;terms&#32;that&#32;are&#32;defined&#32;in&#32;the&#32;vocabulary.|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-150)|Identifier|`range-out-of-vocabulary`|
|[Section top](#pass-outcome-number-150)|Title|Ranges&#32;properly&#32;defined|
|[Section top](#pass-outcome-number-150)|Description|Each&#32;rdfs:range&#32;is&#32;defined&#32;within&#32;the&#32;fragment|

***
### Pass Outcome number 151

[Jump to summary definition](#summary-Pass-151)	|	[Previous Pass outcome](#pass-outcome-number-150)	|	[Next Pass outcome](#pass-outcome-number-152)

:white_check_mark:Pass outcome
#### Subject detail
|Name|modelet-manufacturing-environments-discover-signifiers|
|----|----|
|Title|Standalone&#32;modelet&#32;domains/manufacturing-environments/discover-signifiers/onto.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Modelet manufacturing-environments/discover-signifiers](https://github.com/HyperAgents/hmas/blob/HEAD/domains/manufacturing-environments/discover-signifiers/onto.ttl)|

#### Criterion detail
|Identifier|[owl-rl-constraint](https://ns.inria.fr/olivaw#owl-rl-constraint)|
|----|----|
|Title|OWL&#32;RL&#32;Constraint&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;check&#32;wether&#32;the&#32;test&#32;subject&#32;is&#32;syntaxically&#32;correct&#32;or&#32;not.|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-151)|Identifier|`owl-rl-constraint-violation`|
|[Section top](#pass-outcome-number-151)|Title|OWL&#32;RL&#32;consistent|
|[Section top](#pass-outcome-number-151)|Description|The&#32;provided&#32;graph&#32;is&#32;consistent&#32;for&#32;any&#32;OWL&#32;RL&#32;constraint|

***
### Pass Outcome number 152

[Jump to summary definition](#summary-Pass-152)	|	[Previous Pass outcome](#pass-outcome-number-151)	|	[Next Pass outcome](#pass-outcome-number-153)

:white_check_mark:Pass outcome
#### Subject detail
|Name|modelet-manufacturing-environments-discover-signifiers|
|----|----|
|Title|Standalone&#32;modelet&#32;domains/manufacturing-environments/discover-signifiers/onto.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Modelet manufacturing-environments/discover-signifiers](https://github.com/HyperAgents/hmas/blob/HEAD/domains/manufacturing-environments/discover-signifiers/onto.ttl)|

#### Criterion detail
|Identifier|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|
|----|----|
|Title|Profile&#32;compatibility&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;check&#32;whether&#32;the&#32;test&#32;subject&#32;is&#32;compatible&#32;with&#32;a&#32;profile&#32;or&#32;not,&#32;and&#32;if&#32;it&#32;is&#32;not,&#32;why.|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-152)|Identifier|`owl-rl-profile-error`|
|[Section top](#pass-outcome-number-152)|Title|OWL&#32;RL&#32;Profile&#32;compatible|
|[Section top](#pass-outcome-number-152)|Description|The&#32;subject&#32;is&#32;included&#32;in&#32;the&#32;OWL&#32;RL&#32;sublanguage|

***
### Pass Outcome number 153

[Jump to summary definition](#summary-Pass-153)	|	[Previous Pass outcome](#pass-outcome-number-152)	|	[Next Pass outcome](#pass-outcome-number-154)

:white_check_mark:Pass outcome
#### Subject detail
|Name|modelet-manufacturing-environments-discover-signifiers|
|----|----|
|Title|Standalone&#32;modelet&#32;domains/manufacturing-environments/discover-signifiers/onto.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Modelet manufacturing-environments/discover-signifiers](https://github.com/HyperAgents/hmas/blob/HEAD/domains/manufacturing-environments/discover-signifiers/onto.ttl)|

#### Criterion detail
|Identifier|[proper-extension-predicate](https://ns.inria.fr/olivaw#proper-extension-predicate)|
|----|----|
|Title|Predicate&#32;extension&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;test&#32;the&#32;proper&#32;use&#32;of&#32;predicates&#32;rdfs:subClassOf&#32;and&#32;rdfs:subPropertyOf&#32;on&#32;the&#32;ontology&#32;terms|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-153)|Identifier|`class-subpropertyof`|
|[Section top](#pass-outcome-number-153)|Title|No&#32;class&#32;subproperty|
|[Section top](#pass-outcome-number-153)|Description|No&#32;ontology&#32;class&#32;is&#32;a&#32;subproperty|

***
### Pass Outcome number 154

[Jump to summary definition](#summary-Pass-154)	|	[Previous Pass outcome](#pass-outcome-number-153)	|	[Next Pass outcome](#pass-outcome-number-155)

:white_check_mark:Pass outcome
#### Subject detail
|Name|modelet-manufacturing-environments-discover-signifiers|
|----|----|
|Title|Standalone&#32;modelet&#32;domains/manufacturing-environments/discover-signifiers/onto.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Modelet manufacturing-environments/discover-signifiers](https://github.com/HyperAgents/hmas/blob/HEAD/domains/manufacturing-environments/discover-signifiers/onto.ttl)|

#### Criterion detail
|Identifier|[proper-extension-predicate](https://ns.inria.fr/olivaw#proper-extension-predicate)|
|----|----|
|Title|Predicate&#32;extension&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;test&#32;the&#32;proper&#32;use&#32;of&#32;predicates&#32;rdfs:subClassOf&#32;and&#32;rdfs:subPropertyOf&#32;on&#32;the&#32;ontology&#32;terms|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-154)|Identifier|`property-subclassof`|
|[Section top](#pass-outcome-number-154)|Title|No&#32;property&#32;subclass|
|[Section top](#pass-outcome-number-154)|Description|No&#32;ontology&#32;property&#32;is&#32;a&#32;subclass|

***
### Pass Outcome number 155

[Jump to summary definition](#summary-Pass-155)	|	[Previous Pass outcome](#pass-outcome-number-154)	|	[Next Pass outcome](#pass-outcome-number-156)

:white_check_mark:Pass outcome
#### Subject detail
|Name|modelet-manufacturing-environments-discover-signifiers|
|----|----|
|Title|Standalone&#32;modelet&#32;domains/manufacturing-environments/discover-signifiers/onto.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Modelet manufacturing-environments/discover-signifiers](https://github.com/HyperAgents/hmas/blob/HEAD/domains/manufacturing-environments/discover-signifiers/onto.ttl)|

#### Criterion detail
|Identifier|[proper-extension-predicate](https://ns.inria.fr/olivaw#proper-extension-predicate)|
|----|----|
|Title|Predicate&#32;extension&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;test&#32;the&#32;proper&#32;use&#32;of&#32;predicates&#32;rdfs:subClassOf&#32;and&#32;rdfs:subPropertyOf&#32;on&#32;the&#32;ontology&#32;terms|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-155)|Identifier|`subclassof-property`|
|[Section top](#pass-outcome-number-155)|Title|No&#32;subclass&#32;of&#32;property|
|[Section top](#pass-outcome-number-155)|Description|No&#32;ontology&#32;term&#32;is&#32;a&#32;subclass&#32;of&#32;a&#32;property|

***
### Pass Outcome number 156

[Jump to summary definition](#summary-Pass-156)	|	[Previous Pass outcome](#pass-outcome-number-155)	|	[Next Pass outcome](#pass-outcome-number-157)

:white_check_mark:Pass outcome
#### Subject detail
|Name|modelet-manufacturing-environments-discover-signifiers|
|----|----|
|Title|Standalone&#32;modelet&#32;domains/manufacturing-environments/discover-signifiers/onto.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Modelet manufacturing-environments/discover-signifiers](https://github.com/HyperAgents/hmas/blob/HEAD/domains/manufacturing-environments/discover-signifiers/onto.ttl)|

#### Criterion detail
|Identifier|[proper-extension-predicate](https://ns.inria.fr/olivaw#proper-extension-predicate)|
|----|----|
|Title|Predicate&#32;extension&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;test&#32;the&#32;proper&#32;use&#32;of&#32;predicates&#32;rdfs:subClassOf&#32;and&#32;rdfs:subPropertyOf&#32;on&#32;the&#32;ontology&#32;terms|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-156)|Identifier|`subpropertyof-class`|
|[Section top](#pass-outcome-number-156)|Title|No&#32;subproperty&#32;of&#32;class|
|[Section top](#pass-outcome-number-156)|Description|No&#32;ontology&#32;term&#32;is&#32;a&#32;subproperty&#32;of&#32;a&#32;class|

***
### Pass Outcome number 157

[Jump to summary definition](#summary-Pass-157)	|	[Previous Pass outcome](#pass-outcome-number-156)	|	[Next Pass outcome](#pass-outcome-number-158)

:white_check_mark:Pass outcome
#### Subject detail
|Name|modelet-manufacturing-environments-discover-signifiers|
|----|----|
|Title|Standalone&#32;modelet&#32;domains/manufacturing-environments/discover-signifiers/onto.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Modelet manufacturing-environments/discover-signifiers](https://github.com/HyperAgents/hmas/blob/HEAD/domains/manufacturing-environments/discover-signifiers/onto.ttl)|

#### Criterion detail
|Identifier|[term-referencing](https://ns.inria.fr/olivaw#term-referencing)|
|----|----|
|Title|Term&#32;referencing&#32;test|
|Description|A&#32;test&#32;case&#32;from&#32;the&#32;Best&#32;Practices&#32;tests&#32;checking&#32;if&#32;each&#32;term&#32;of&#32;the&#32;test&#32;subject&#32;is&#32;referenced&#32;to&#32;a&#32;module&#32;through&#32;a&#32;rdfs:isDefinedBy&#32;property.|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-157)|Identifier|`no-reference-module`|
|[Section top](#pass-outcome-number-157)|Title|Any&#32;term&#32;is&#32;referenced|
|[Section top](#pass-outcome-number-157)|Description|Each&#32;term&#32;of&#32;the&#32;test&#32;subject&#32;is&#32;linked&#32;to&#32;a&#32;module&#32;by&#32;a&#32;rdfs:isDefinedBy&#32;property|

***
### Pass Outcome number 158

[Jump to summary definition](#summary-Pass-158)	|	[Previous Pass outcome](#pass-outcome-number-157)	|	[Next Pass outcome](#pass-outcome-number-159)

:white_check_mark:Pass outcome
#### Subject detail
|Name|modelet-manufacturing-environments-discover-signifiers|
|----|----|
|Title|Standalone&#32;modelet&#32;domains/manufacturing-environments/discover-signifiers/onto.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Modelet manufacturing-environments/discover-signifiers](https://github.com/HyperAgents/hmas/blob/HEAD/domains/manufacturing-environments/discover-signifiers/onto.ttl)|

#### Criterion detail
|Identifier|[terms-differenciation](https://ns.inria.fr/olivaw#terms-differenciation)|
|----|----|
|Title|Terms&#32;differenciation&#32;test|
|Description|A&#32;test&#32;case&#32;from&#32;the&#32;Best&#32;Practices&#32;tests&#32;checking&#32;if&#32;all&#32;the&#32;terms&#32;are&#32;different&#32;enough&#32;from&#32;each&#32;other&#32;according&#32;to&#32;the&#32;Levenshtein&#32;distance&#32;metric.|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-158)|Identifier|`too-close-terms`|
|[Section top](#pass-outcome-number-158)|Title|Terms&#32;differenciated&#32;enough|
|[Section top](#pass-outcome-number-158)|Description|All&#32;the&#32;terms&#32;have&#32;have&#32;a&#32;satisfying&#32;Levenshtein&#32;distance&#32;from&#32;each&#32;other&#32;term.|

***
### Pass Outcome number 159

[Jump to summary definition](#summary-Pass-159)	|	[Previous Pass outcome](#pass-outcome-number-158)	|	[Next Pass outcome](#pass-outcome-number-160)

:white_check_mark:Pass outcome
#### Subject detail
|Name|modelet-manufacturing-environments-discover-platforms|
|----|----|
|Title|Standalone&#32;modelet&#32;domains/manufacturing-environments/discover-platforms/onto.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Modelet manufacturing-environments/discover-platforms](https://github.com/HyperAgents/hmas/blob/HEAD/domains/manufacturing-environments/discover-platforms/onto.ttl)|

#### Criterion detail
|Identifier|[domain-and-range-referencing](https://ns.inria.fr/olivaw#domain-and-range-referencing)|
|----|----|
|Title|Domain&#32;and&#32;range&#32;referencing&#32;test|
|Description|A&#32;test&#32;case&#32;from&#32;the&#32;Best&#32;Practices&#32;tests&#32;checking&#32;if&#32;all&#32;the&#32;ranges&#32;and&#32;domains&#32;from&#32;the&#32;test&#32;subject&#32;point&#32;to&#32;terms&#32;that&#32;are&#32;defined&#32;in&#32;the&#32;vocabulary.|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-159)|Identifier|`domain-out-of-vocabulary`|
|[Section top](#pass-outcome-number-159)|Title|Domains&#32;properly&#32;defined|
|[Section top](#pass-outcome-number-159)|Description|Each&#32;rdfs:domain&#32;is&#32;defined&#32;within&#32;the&#32;fragment|

***
### Pass Outcome number 160

[Jump to summary definition](#summary-Pass-160)	|	[Previous Pass outcome](#pass-outcome-number-159)	|	[Next Pass outcome](#pass-outcome-number-161)

:white_check_mark:Pass outcome
#### Subject detail
|Name|modelet-manufacturing-environments-discover-platforms|
|----|----|
|Title|Standalone&#32;modelet&#32;domains/manufacturing-environments/discover-platforms/onto.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Modelet manufacturing-environments/discover-platforms](https://github.com/HyperAgents/hmas/blob/HEAD/domains/manufacturing-environments/discover-platforms/onto.ttl)|

#### Criterion detail
|Identifier|[domain-and-range-referencing](https://ns.inria.fr/olivaw#domain-and-range-referencing)|
|----|----|
|Title|Domain&#32;and&#32;range&#32;referencing&#32;test|
|Description|A&#32;test&#32;case&#32;from&#32;the&#32;Best&#32;Practices&#32;tests&#32;checking&#32;if&#32;all&#32;the&#32;ranges&#32;and&#32;domains&#32;from&#32;the&#32;test&#32;subject&#32;point&#32;to&#32;terms&#32;that&#32;are&#32;defined&#32;in&#32;the&#32;vocabulary.|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-160)|Identifier|`range-out-of-vocabulary`|
|[Section top](#pass-outcome-number-160)|Title|Ranges&#32;properly&#32;defined|
|[Section top](#pass-outcome-number-160)|Description|Each&#32;rdfs:range&#32;is&#32;defined&#32;within&#32;the&#32;fragment|

***
### Pass Outcome number 161

[Jump to summary definition](#summary-Pass-161)	|	[Previous Pass outcome](#pass-outcome-number-160)	|	[Next Pass outcome](#pass-outcome-number-162)

:white_check_mark:Pass outcome
#### Subject detail
|Name|modelet-manufacturing-environments-discover-platforms|
|----|----|
|Title|Standalone&#32;modelet&#32;domains/manufacturing-environments/discover-platforms/onto.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Modelet manufacturing-environments/discover-platforms](https://github.com/HyperAgents/hmas/blob/HEAD/domains/manufacturing-environments/discover-platforms/onto.ttl)|

#### Criterion detail
|Identifier|[labeled-terms](https://ns.inria.fr/olivaw#labeled-terms)|
|----|----|
|Title|Term&#32;labeling&#32;test|
|Description|A&#32;test&#32;case&#32;from&#32;the&#32;Best&#32;Practices&#32;tests&#32;checking&#32;if&#32;all&#32;the&#32;terms&#32;of&#32;the&#32;subject&#32;have&#32;a&#32;rdfs:label&#32;property&#32;pointing&#32;to&#32;a&#32;literal&#32;in&#32;English|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-161)|Identifier|`not-labeled-term`|
|[Section top](#pass-outcome-number-161)|Title|All&#32;terms&#32;labeled|
|[Section top](#pass-outcome-number-161)|Description|All&#32;the&#32;terms&#32;defined&#32;in&#32;the&#32;subject&#32;have&#32;a&#32;rdfs:label&#32;in&#32;English|

***
### Pass Outcome number 162

[Jump to summary definition](#summary-Pass-162)	|	[Previous Pass outcome](#pass-outcome-number-161)	|	[Next Pass outcome](#pass-outcome-number-163)

:white_check_mark:Pass outcome
#### Subject detail
|Name|modelet-manufacturing-environments-discover-platforms|
|----|----|
|Title|Standalone&#32;modelet&#32;domains/manufacturing-environments/discover-platforms/onto.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Modelet manufacturing-environments/discover-platforms](https://github.com/HyperAgents/hmas/blob/HEAD/domains/manufacturing-environments/discover-platforms/onto.ttl)|

#### Criterion detail
|Identifier|[owl-rl-constraint](https://ns.inria.fr/olivaw#owl-rl-constraint)|
|----|----|
|Title|OWL&#32;RL&#32;Constraint&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;check&#32;wether&#32;the&#32;test&#32;subject&#32;is&#32;syntaxically&#32;correct&#32;or&#32;not.|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-162)|Identifier|`owl-rl-constraint-violation`|
|[Section top](#pass-outcome-number-162)|Title|OWL&#32;RL&#32;consistent|
|[Section top](#pass-outcome-number-162)|Description|The&#32;provided&#32;graph&#32;is&#32;consistent&#32;for&#32;any&#32;OWL&#32;RL&#32;constraint|

***
### Pass Outcome number 163

[Jump to summary definition](#summary-Pass-163)	|	[Previous Pass outcome](#pass-outcome-number-162)	|	[Next Pass outcome](#pass-outcome-number-164)

:white_check_mark:Pass outcome
#### Subject detail
|Name|modelet-manufacturing-environments-discover-platforms|
|----|----|
|Title|Standalone&#32;modelet&#32;domains/manufacturing-environments/discover-platforms/onto.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Modelet manufacturing-environments/discover-platforms](https://github.com/HyperAgents/hmas/blob/HEAD/domains/manufacturing-environments/discover-platforms/onto.ttl)|

#### Criterion detail
|Identifier|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|
|----|----|
|Title|Profile&#32;compatibility&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;check&#32;whether&#32;the&#32;test&#32;subject&#32;is&#32;compatible&#32;with&#32;a&#32;profile&#32;or&#32;not,&#32;and&#32;if&#32;it&#32;is&#32;not,&#32;why.|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-163)|Identifier|`owl-ql-profile-error`|
|[Section top](#pass-outcome-number-163)|Title|OWL&#32;QL&#32;Profile&#32;compatible|
|[Section top](#pass-outcome-number-163)|Description|The&#32;subject&#32;is&#32;included&#32;in&#32;the&#32;OWL&#32;QL&#32;sublanguage|

***
### Pass Outcome number 164

[Jump to summary definition](#summary-Pass-164)	|	[Previous Pass outcome](#pass-outcome-number-163)	|	[Next Pass outcome](#pass-outcome-number-165)

:white_check_mark:Pass outcome
#### Subject detail
|Name|modelet-manufacturing-environments-discover-platforms|
|----|----|
|Title|Standalone&#32;modelet&#32;domains/manufacturing-environments/discover-platforms/onto.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Modelet manufacturing-environments/discover-platforms](https://github.com/HyperAgents/hmas/blob/HEAD/domains/manufacturing-environments/discover-platforms/onto.ttl)|

#### Criterion detail
|Identifier|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|
|----|----|
|Title|Profile&#32;compatibility&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;check&#32;whether&#32;the&#32;test&#32;subject&#32;is&#32;compatible&#32;with&#32;a&#32;profile&#32;or&#32;not,&#32;and&#32;if&#32;it&#32;is&#32;not,&#32;why.|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-164)|Identifier|`owl-rl-profile-error`|
|[Section top](#pass-outcome-number-164)|Title|OWL&#32;RL&#32;Profile&#32;compatible|
|[Section top](#pass-outcome-number-164)|Description|The&#32;subject&#32;is&#32;included&#32;in&#32;the&#32;OWL&#32;RL&#32;sublanguage|

***
### Pass Outcome number 165

[Jump to summary definition](#summary-Pass-165)	|	[Previous Pass outcome](#pass-outcome-number-164)	|	[Next Pass outcome](#pass-outcome-number-166)

:white_check_mark:Pass outcome
#### Subject detail
|Name|modelet-manufacturing-environments-discover-platforms|
|----|----|
|Title|Standalone&#32;modelet&#32;domains/manufacturing-environments/discover-platforms/onto.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Modelet manufacturing-environments/discover-platforms](https://github.com/HyperAgents/hmas/blob/HEAD/domains/manufacturing-environments/discover-platforms/onto.ttl)|

#### Criterion detail
|Identifier|[proper-extension-predicate](https://ns.inria.fr/olivaw#proper-extension-predicate)|
|----|----|
|Title|Predicate&#32;extension&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;test&#32;the&#32;proper&#32;use&#32;of&#32;predicates&#32;rdfs:subClassOf&#32;and&#32;rdfs:subPropertyOf&#32;on&#32;the&#32;ontology&#32;terms|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-165)|Identifier|`class-subpropertyof`|
|[Section top](#pass-outcome-number-165)|Title|No&#32;class&#32;subproperty|
|[Section top](#pass-outcome-number-165)|Description|No&#32;ontology&#32;class&#32;is&#32;a&#32;subproperty|

***
### Pass Outcome number 166

[Jump to summary definition](#summary-Pass-166)	|	[Previous Pass outcome](#pass-outcome-number-165)	|	[Next Pass outcome](#pass-outcome-number-167)

:white_check_mark:Pass outcome
#### Subject detail
|Name|modelet-manufacturing-environments-discover-platforms|
|----|----|
|Title|Standalone&#32;modelet&#32;domains/manufacturing-environments/discover-platforms/onto.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Modelet manufacturing-environments/discover-platforms](https://github.com/HyperAgents/hmas/blob/HEAD/domains/manufacturing-environments/discover-platforms/onto.ttl)|

#### Criterion detail
|Identifier|[proper-extension-predicate](https://ns.inria.fr/olivaw#proper-extension-predicate)|
|----|----|
|Title|Predicate&#32;extension&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;test&#32;the&#32;proper&#32;use&#32;of&#32;predicates&#32;rdfs:subClassOf&#32;and&#32;rdfs:subPropertyOf&#32;on&#32;the&#32;ontology&#32;terms|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-166)|Identifier|`property-subclassof`|
|[Section top](#pass-outcome-number-166)|Title|No&#32;property&#32;subclass|
|[Section top](#pass-outcome-number-166)|Description|No&#32;ontology&#32;property&#32;is&#32;a&#32;subclass|

***
### Pass Outcome number 167

[Jump to summary definition](#summary-Pass-167)	|	[Previous Pass outcome](#pass-outcome-number-166)	|	[Next Pass outcome](#pass-outcome-number-168)

:white_check_mark:Pass outcome
#### Subject detail
|Name|modelet-manufacturing-environments-discover-platforms|
|----|----|
|Title|Standalone&#32;modelet&#32;domains/manufacturing-environments/discover-platforms/onto.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Modelet manufacturing-environments/discover-platforms](https://github.com/HyperAgents/hmas/blob/HEAD/domains/manufacturing-environments/discover-platforms/onto.ttl)|

#### Criterion detail
|Identifier|[proper-extension-predicate](https://ns.inria.fr/olivaw#proper-extension-predicate)|
|----|----|
|Title|Predicate&#32;extension&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;test&#32;the&#32;proper&#32;use&#32;of&#32;predicates&#32;rdfs:subClassOf&#32;and&#32;rdfs:subPropertyOf&#32;on&#32;the&#32;ontology&#32;terms|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-167)|Identifier|`subclassof-property`|
|[Section top](#pass-outcome-number-167)|Title|No&#32;subclass&#32;of&#32;property|
|[Section top](#pass-outcome-number-167)|Description|No&#32;ontology&#32;term&#32;is&#32;a&#32;subclass&#32;of&#32;a&#32;property|

***
### Pass Outcome number 168

[Jump to summary definition](#summary-Pass-168)	|	[Previous Pass outcome](#pass-outcome-number-167)	|	[Next Pass outcome](#pass-outcome-number-169)

:white_check_mark:Pass outcome
#### Subject detail
|Name|modelet-manufacturing-environments-discover-platforms|
|----|----|
|Title|Standalone&#32;modelet&#32;domains/manufacturing-environments/discover-platforms/onto.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Modelet manufacturing-environments/discover-platforms](https://github.com/HyperAgents/hmas/blob/HEAD/domains/manufacturing-environments/discover-platforms/onto.ttl)|

#### Criterion detail
|Identifier|[proper-extension-predicate](https://ns.inria.fr/olivaw#proper-extension-predicate)|
|----|----|
|Title|Predicate&#32;extension&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;test&#32;the&#32;proper&#32;use&#32;of&#32;predicates&#32;rdfs:subClassOf&#32;and&#32;rdfs:subPropertyOf&#32;on&#32;the&#32;ontology&#32;terms|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-168)|Identifier|`subpropertyof-class`|
|[Section top](#pass-outcome-number-168)|Title|No&#32;subproperty&#32;of&#32;class|
|[Section top](#pass-outcome-number-168)|Description|No&#32;ontology&#32;term&#32;is&#32;a&#32;subproperty&#32;of&#32;a&#32;class|

***
### Pass Outcome number 169

[Jump to summary definition](#summary-Pass-169)	|	[Previous Pass outcome](#pass-outcome-number-168)	|	[Next Pass outcome](#pass-outcome-number-170)

:white_check_mark:Pass outcome
#### Subject detail
|Name|modelet-manufacturing-environments-discover-platforms|
|----|----|
|Title|Standalone&#32;modelet&#32;domains/manufacturing-environments/discover-platforms/onto.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Modelet manufacturing-environments/discover-platforms](https://github.com/HyperAgents/hmas/blob/HEAD/domains/manufacturing-environments/discover-platforms/onto.ttl)|

#### Criterion detail
|Identifier|[term-referencing](https://ns.inria.fr/olivaw#term-referencing)|
|----|----|
|Title|Term&#32;referencing&#32;test|
|Description|A&#32;test&#32;case&#32;from&#32;the&#32;Best&#32;Practices&#32;tests&#32;checking&#32;if&#32;each&#32;term&#32;of&#32;the&#32;test&#32;subject&#32;is&#32;referenced&#32;to&#32;a&#32;module&#32;through&#32;a&#32;rdfs:isDefinedBy&#32;property.|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-169)|Identifier|`no-reference-module`|
|[Section top](#pass-outcome-number-169)|Title|Any&#32;term&#32;is&#32;referenced|
|[Section top](#pass-outcome-number-169)|Description|Each&#32;term&#32;of&#32;the&#32;test&#32;subject&#32;is&#32;linked&#32;to&#32;a&#32;module&#32;by&#32;a&#32;rdfs:isDefinedBy&#32;property|

***
### Pass Outcome number 170

[Jump to summary definition](#summary-Pass-170)	|	[Previous Pass outcome](#pass-outcome-number-169)	|	[Next Pass outcome](#pass-outcome-number-171)

:white_check_mark:Pass outcome
#### Subject detail
|Name|modelet-manufacturing-environments-discover-platforms|
|----|----|
|Title|Standalone&#32;modelet&#32;domains/manufacturing-environments/discover-platforms/onto.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Modelet manufacturing-environments/discover-platforms](https://github.com/HyperAgents/hmas/blob/HEAD/domains/manufacturing-environments/discover-platforms/onto.ttl)|

#### Criterion detail
|Identifier|[terms-differenciation](https://ns.inria.fr/olivaw#terms-differenciation)|
|----|----|
|Title|Terms&#32;differenciation&#32;test|
|Description|A&#32;test&#32;case&#32;from&#32;the&#32;Best&#32;Practices&#32;tests&#32;checking&#32;if&#32;all&#32;the&#32;terms&#32;are&#32;different&#32;enough&#32;from&#32;each&#32;other&#32;according&#32;to&#32;the&#32;Levenshtein&#32;distance&#32;metric.|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-170)|Identifier|`too-close-terms`|
|[Section top](#pass-outcome-number-170)|Title|Terms&#32;differenciated&#32;enough|
|[Section top](#pass-outcome-number-170)|Description|All&#32;the&#32;terms&#32;have&#32;have&#32;a&#32;satisfying&#32;Levenshtein&#32;distance&#32;from&#32;each&#32;other&#32;term.|

***
### Pass Outcome number 171

[Jump to summary definition](#summary-Pass-171)	|	[Previous Pass outcome](#pass-outcome-number-170)	|	[Next Pass outcome](#pass-outcome-number-172)

:white_check_mark:Pass outcome
#### Subject detail
|Name|modelet-manufacturing-environments-discover-organization|
|----|----|
|Title|Standalone&#32;modelet&#32;domains/manufacturing-environments/discover-organization/onto.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Modelet manufacturing-environments/discover-organization](https://github.com/HyperAgents/hmas/blob/HEAD/domains/manufacturing-environments/discover-organization/onto.ttl)|

#### Criterion detail
|Identifier|[domain-and-range-referencing](https://ns.inria.fr/olivaw#domain-and-range-referencing)|
|----|----|
|Title|Domain&#32;and&#32;range&#32;referencing&#32;test|
|Description|A&#32;test&#32;case&#32;from&#32;the&#32;Best&#32;Practices&#32;tests&#32;checking&#32;if&#32;all&#32;the&#32;ranges&#32;and&#32;domains&#32;from&#32;the&#32;test&#32;subject&#32;point&#32;to&#32;terms&#32;that&#32;are&#32;defined&#32;in&#32;the&#32;vocabulary.|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-171)|Identifier|`domain-out-of-vocabulary`|
|[Section top](#pass-outcome-number-171)|Title|Domains&#32;properly&#32;defined|
|[Section top](#pass-outcome-number-171)|Description|Each&#32;rdfs:domain&#32;is&#32;defined&#32;within&#32;the&#32;fragment|

***
### Pass Outcome number 172

[Jump to summary definition](#summary-Pass-172)	|	[Previous Pass outcome](#pass-outcome-number-171)	|	[Next Pass outcome](#pass-outcome-number-173)

:white_check_mark:Pass outcome
#### Subject detail
|Name|modelet-manufacturing-environments-discover-organization|
|----|----|
|Title|Standalone&#32;modelet&#32;domains/manufacturing-environments/discover-organization/onto.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Modelet manufacturing-environments/discover-organization](https://github.com/HyperAgents/hmas/blob/HEAD/domains/manufacturing-environments/discover-organization/onto.ttl)|

#### Criterion detail
|Identifier|[domain-and-range-referencing](https://ns.inria.fr/olivaw#domain-and-range-referencing)|
|----|----|
|Title|Domain&#32;and&#32;range&#32;referencing&#32;test|
|Description|A&#32;test&#32;case&#32;from&#32;the&#32;Best&#32;Practices&#32;tests&#32;checking&#32;if&#32;all&#32;the&#32;ranges&#32;and&#32;domains&#32;from&#32;the&#32;test&#32;subject&#32;point&#32;to&#32;terms&#32;that&#32;are&#32;defined&#32;in&#32;the&#32;vocabulary.|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-172)|Identifier|`range-out-of-vocabulary`|
|[Section top](#pass-outcome-number-172)|Title|Ranges&#32;properly&#32;defined|
|[Section top](#pass-outcome-number-172)|Description|Each&#32;rdfs:range&#32;is&#32;defined&#32;within&#32;the&#32;fragment|

***
### Pass Outcome number 173

[Jump to summary definition](#summary-Pass-173)	|	[Previous Pass outcome](#pass-outcome-number-172)	|	[Next Pass outcome](#pass-outcome-number-174)

:white_check_mark:Pass outcome
#### Subject detail
|Name|modelet-manufacturing-environments-discover-organization|
|----|----|
|Title|Standalone&#32;modelet&#32;domains/manufacturing-environments/discover-organization/onto.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Modelet manufacturing-environments/discover-organization](https://github.com/HyperAgents/hmas/blob/HEAD/domains/manufacturing-environments/discover-organization/onto.ttl)|

#### Criterion detail
|Identifier|[labeled-terms](https://ns.inria.fr/olivaw#labeled-terms)|
|----|----|
|Title|Term&#32;labeling&#32;test|
|Description|A&#32;test&#32;case&#32;from&#32;the&#32;Best&#32;Practices&#32;tests&#32;checking&#32;if&#32;all&#32;the&#32;terms&#32;of&#32;the&#32;subject&#32;have&#32;a&#32;rdfs:label&#32;property&#32;pointing&#32;to&#32;a&#32;literal&#32;in&#32;English|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-173)|Identifier|`not-labeled-term`|
|[Section top](#pass-outcome-number-173)|Title|All&#32;terms&#32;labeled|
|[Section top](#pass-outcome-number-173)|Description|All&#32;the&#32;terms&#32;defined&#32;in&#32;the&#32;subject&#32;have&#32;a&#32;rdfs:label&#32;in&#32;English|

***
### Pass Outcome number 174

[Jump to summary definition](#summary-Pass-174)	|	[Previous Pass outcome](#pass-outcome-number-173)	|	[Next Pass outcome](#pass-outcome-number-175)

:white_check_mark:Pass outcome
#### Subject detail
|Name|modelet-manufacturing-environments-discover-organization|
|----|----|
|Title|Standalone&#32;modelet&#32;domains/manufacturing-environments/discover-organization/onto.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Modelet manufacturing-environments/discover-organization](https://github.com/HyperAgents/hmas/blob/HEAD/domains/manufacturing-environments/discover-organization/onto.ttl)|

#### Criterion detail
|Identifier|[owl-rl-constraint](https://ns.inria.fr/olivaw#owl-rl-constraint)|
|----|----|
|Title|OWL&#32;RL&#32;Constraint&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;check&#32;wether&#32;the&#32;test&#32;subject&#32;is&#32;syntaxically&#32;correct&#32;or&#32;not.|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-174)|Identifier|`owl-rl-constraint-violation`|
|[Section top](#pass-outcome-number-174)|Title|OWL&#32;RL&#32;consistent|
|[Section top](#pass-outcome-number-174)|Description|The&#32;provided&#32;graph&#32;is&#32;consistent&#32;for&#32;any&#32;OWL&#32;RL&#32;constraint|

***
### Pass Outcome number 175

[Jump to summary definition](#summary-Pass-175)	|	[Previous Pass outcome](#pass-outcome-number-174)	|	[Next Pass outcome](#pass-outcome-number-176)

:white_check_mark:Pass outcome
#### Subject detail
|Name|modelet-manufacturing-environments-discover-organization|
|----|----|
|Title|Standalone&#32;modelet&#32;domains/manufacturing-environments/discover-organization/onto.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Modelet manufacturing-environments/discover-organization](https://github.com/HyperAgents/hmas/blob/HEAD/domains/manufacturing-environments/discover-organization/onto.ttl)|

#### Criterion detail
|Identifier|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|
|----|----|
|Title|Profile&#32;compatibility&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;check&#32;whether&#32;the&#32;test&#32;subject&#32;is&#32;compatible&#32;with&#32;a&#32;profile&#32;or&#32;not,&#32;and&#32;if&#32;it&#32;is&#32;not,&#32;why.|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-175)|Identifier|`owl-el-profile-error`|
|[Section top](#pass-outcome-number-175)|Title|OWL&#32;EL&#32;Profile&#32;compatible|
|[Section top](#pass-outcome-number-175)|Description|The&#32;subject&#32;is&#32;included&#32;in&#32;the&#32;OWL&#32;EL&#32;sublanguage|

***
### Pass Outcome number 176

[Jump to summary definition](#summary-Pass-176)	|	[Previous Pass outcome](#pass-outcome-number-175)	|	[Next Pass outcome](#pass-outcome-number-177)

:white_check_mark:Pass outcome
#### Subject detail
|Name|modelet-manufacturing-environments-discover-organization|
|----|----|
|Title|Standalone&#32;modelet&#32;domains/manufacturing-environments/discover-organization/onto.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Modelet manufacturing-environments/discover-organization](https://github.com/HyperAgents/hmas/blob/HEAD/domains/manufacturing-environments/discover-organization/onto.ttl)|

#### Criterion detail
|Identifier|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|
|----|----|
|Title|Profile&#32;compatibility&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;check&#32;whether&#32;the&#32;test&#32;subject&#32;is&#32;compatible&#32;with&#32;a&#32;profile&#32;or&#32;not,&#32;and&#32;if&#32;it&#32;is&#32;not,&#32;why.|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-176)|Identifier|`owl-ql-profile-error`|
|[Section top](#pass-outcome-number-176)|Title|OWL&#32;QL&#32;Profile&#32;compatible|
|[Section top](#pass-outcome-number-176)|Description|The&#32;subject&#32;is&#32;included&#32;in&#32;the&#32;OWL&#32;QL&#32;sublanguage|

***
### Pass Outcome number 177

[Jump to summary definition](#summary-Pass-177)	|	[Previous Pass outcome](#pass-outcome-number-176)	|	[Next Pass outcome](#pass-outcome-number-178)

:white_check_mark:Pass outcome
#### Subject detail
|Name|modelet-manufacturing-environments-discover-organization|
|----|----|
|Title|Standalone&#32;modelet&#32;domains/manufacturing-environments/discover-organization/onto.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Modelet manufacturing-environments/discover-organization](https://github.com/HyperAgents/hmas/blob/HEAD/domains/manufacturing-environments/discover-organization/onto.ttl)|

#### Criterion detail
|Identifier|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|
|----|----|
|Title|Profile&#32;compatibility&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;check&#32;whether&#32;the&#32;test&#32;subject&#32;is&#32;compatible&#32;with&#32;a&#32;profile&#32;or&#32;not,&#32;and&#32;if&#32;it&#32;is&#32;not,&#32;why.|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-177)|Identifier|`owl-rl-profile-error`|
|[Section top](#pass-outcome-number-177)|Title|OWL&#32;RL&#32;Profile&#32;compatible|
|[Section top](#pass-outcome-number-177)|Description|The&#32;subject&#32;is&#32;included&#32;in&#32;the&#32;OWL&#32;RL&#32;sublanguage|

***
### Pass Outcome number 178

[Jump to summary definition](#summary-Pass-178)	|	[Previous Pass outcome](#pass-outcome-number-177)	|	[Next Pass outcome](#pass-outcome-number-179)

:white_check_mark:Pass outcome
#### Subject detail
|Name|modelet-manufacturing-environments-discover-organization|
|----|----|
|Title|Standalone&#32;modelet&#32;domains/manufacturing-environments/discover-organization/onto.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Modelet manufacturing-environments/discover-organization](https://github.com/HyperAgents/hmas/blob/HEAD/domains/manufacturing-environments/discover-organization/onto.ttl)|

#### Criterion detail
|Identifier|[proper-extension-predicate](https://ns.inria.fr/olivaw#proper-extension-predicate)|
|----|----|
|Title|Predicate&#32;extension&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;test&#32;the&#32;proper&#32;use&#32;of&#32;predicates&#32;rdfs:subClassOf&#32;and&#32;rdfs:subPropertyOf&#32;on&#32;the&#32;ontology&#32;terms|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-178)|Identifier|`class-subpropertyof`|
|[Section top](#pass-outcome-number-178)|Title|No&#32;class&#32;subproperty|
|[Section top](#pass-outcome-number-178)|Description|No&#32;ontology&#32;class&#32;is&#32;a&#32;subproperty|

***
### Pass Outcome number 179

[Jump to summary definition](#summary-Pass-179)	|	[Previous Pass outcome](#pass-outcome-number-178)	|	[Next Pass outcome](#pass-outcome-number-180)

:white_check_mark:Pass outcome
#### Subject detail
|Name|modelet-manufacturing-environments-discover-organization|
|----|----|
|Title|Standalone&#32;modelet&#32;domains/manufacturing-environments/discover-organization/onto.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Modelet manufacturing-environments/discover-organization](https://github.com/HyperAgents/hmas/blob/HEAD/domains/manufacturing-environments/discover-organization/onto.ttl)|

#### Criterion detail
|Identifier|[proper-extension-predicate](https://ns.inria.fr/olivaw#proper-extension-predicate)|
|----|----|
|Title|Predicate&#32;extension&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;test&#32;the&#32;proper&#32;use&#32;of&#32;predicates&#32;rdfs:subClassOf&#32;and&#32;rdfs:subPropertyOf&#32;on&#32;the&#32;ontology&#32;terms|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-179)|Identifier|`property-subclassof`|
|[Section top](#pass-outcome-number-179)|Title|No&#32;property&#32;subclass|
|[Section top](#pass-outcome-number-179)|Description|No&#32;ontology&#32;property&#32;is&#32;a&#32;subclass|

***
### Pass Outcome number 180

[Jump to summary definition](#summary-Pass-180)	|	[Previous Pass outcome](#pass-outcome-number-179)	|	[Next Pass outcome](#pass-outcome-number-181)

:white_check_mark:Pass outcome
#### Subject detail
|Name|modelet-manufacturing-environments-discover-organization|
|----|----|
|Title|Standalone&#32;modelet&#32;domains/manufacturing-environments/discover-organization/onto.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Modelet manufacturing-environments/discover-organization](https://github.com/HyperAgents/hmas/blob/HEAD/domains/manufacturing-environments/discover-organization/onto.ttl)|

#### Criterion detail
|Identifier|[proper-extension-predicate](https://ns.inria.fr/olivaw#proper-extension-predicate)|
|----|----|
|Title|Predicate&#32;extension&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;test&#32;the&#32;proper&#32;use&#32;of&#32;predicates&#32;rdfs:subClassOf&#32;and&#32;rdfs:subPropertyOf&#32;on&#32;the&#32;ontology&#32;terms|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-180)|Identifier|`subclassof-property`|
|[Section top](#pass-outcome-number-180)|Title|No&#32;subclass&#32;of&#32;property|
|[Section top](#pass-outcome-number-180)|Description|No&#32;ontology&#32;term&#32;is&#32;a&#32;subclass&#32;of&#32;a&#32;property|

***
### Pass Outcome number 181

[Jump to summary definition](#summary-Pass-181)	|	[Previous Pass outcome](#pass-outcome-number-180)	|	[Next Pass outcome](#pass-outcome-number-182)

:white_check_mark:Pass outcome
#### Subject detail
|Name|modelet-manufacturing-environments-discover-organization|
|----|----|
|Title|Standalone&#32;modelet&#32;domains/manufacturing-environments/discover-organization/onto.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Modelet manufacturing-environments/discover-organization](https://github.com/HyperAgents/hmas/blob/HEAD/domains/manufacturing-environments/discover-organization/onto.ttl)|

#### Criterion detail
|Identifier|[proper-extension-predicate](https://ns.inria.fr/olivaw#proper-extension-predicate)|
|----|----|
|Title|Predicate&#32;extension&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;test&#32;the&#32;proper&#32;use&#32;of&#32;predicates&#32;rdfs:subClassOf&#32;and&#32;rdfs:subPropertyOf&#32;on&#32;the&#32;ontology&#32;terms|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-181)|Identifier|`subpropertyof-class`|
|[Section top](#pass-outcome-number-181)|Title|No&#32;subproperty&#32;of&#32;class|
|[Section top](#pass-outcome-number-181)|Description|No&#32;ontology&#32;term&#32;is&#32;a&#32;subproperty&#32;of&#32;a&#32;class|

***
### Pass Outcome number 182

[Jump to summary definition](#summary-Pass-182)	|	[Previous Pass outcome](#pass-outcome-number-181)	|	[Next Pass outcome](#pass-outcome-number-183)

:white_check_mark:Pass outcome
#### Subject detail
|Name|modelet-manufacturing-environments-discover-organization|
|----|----|
|Title|Standalone&#32;modelet&#32;domains/manufacturing-environments/discover-organization/onto.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Modelet manufacturing-environments/discover-organization](https://github.com/HyperAgents/hmas/blob/HEAD/domains/manufacturing-environments/discover-organization/onto.ttl)|

#### Criterion detail
|Identifier|[term-referencing](https://ns.inria.fr/olivaw#term-referencing)|
|----|----|
|Title|Term&#32;referencing&#32;test|
|Description|A&#32;test&#32;case&#32;from&#32;the&#32;Best&#32;Practices&#32;tests&#32;checking&#32;if&#32;each&#32;term&#32;of&#32;the&#32;test&#32;subject&#32;is&#32;referenced&#32;to&#32;a&#32;module&#32;through&#32;a&#32;rdfs:isDefinedBy&#32;property.|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-182)|Identifier|`no-reference-module`|
|[Section top](#pass-outcome-number-182)|Title|Any&#32;term&#32;is&#32;referenced|
|[Section top](#pass-outcome-number-182)|Description|Each&#32;term&#32;of&#32;the&#32;test&#32;subject&#32;is&#32;linked&#32;to&#32;a&#32;module&#32;by&#32;a&#32;rdfs:isDefinedBy&#32;property|

***
### Pass Outcome number 183

[Jump to summary definition](#summary-Pass-183)	|	[Previous Pass outcome](#pass-outcome-number-182)	|	[Next Pass outcome](#pass-outcome-number-184)

:white_check_mark:Pass outcome
#### Subject detail
|Name|modelet-manufacturing-environments-discover-organization|
|----|----|
|Title|Standalone&#32;modelet&#32;domains/manufacturing-environments/discover-organization/onto.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Modelet manufacturing-environments/discover-organization](https://github.com/HyperAgents/hmas/blob/HEAD/domains/manufacturing-environments/discover-organization/onto.ttl)|

#### Criterion detail
|Identifier|[terms-differenciation](https://ns.inria.fr/olivaw#terms-differenciation)|
|----|----|
|Title|Terms&#32;differenciation&#32;test|
|Description|A&#32;test&#32;case&#32;from&#32;the&#32;Best&#32;Practices&#32;tests&#32;checking&#32;if&#32;all&#32;the&#32;terms&#32;are&#32;different&#32;enough&#32;from&#32;each&#32;other&#32;according&#32;to&#32;the&#32;Levenshtein&#32;distance&#32;metric.|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-183)|Identifier|`too-close-terms`|
|[Section top](#pass-outcome-number-183)|Title|Terms&#32;differenciated&#32;enough|
|[Section top](#pass-outcome-number-183)|Description|All&#32;the&#32;terms&#32;have&#32;have&#32;a&#32;satisfying&#32;Levenshtein&#32;distance&#32;from&#32;each&#32;other&#32;term.|

***
### Pass Outcome number 184

[Jump to summary definition](#summary-Pass-184)	|	[Previous Pass outcome](#pass-outcome-number-183)	|	[Next Pass outcome](#pass-outcome-number-185)

:white_check_mark:Pass outcome
#### Subject detail
|Name|modelet-manufacturing-environments-discover-core|
|----|----|
|Title|Standalone&#32;modelet&#32;domains/manufacturing-environments/discover-core/onto.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Modelet manufacturing-environments/discover-core](https://github.com/HyperAgents/hmas/blob/HEAD/domains/manufacturing-environments/discover-core/onto.ttl)|

#### Criterion detail
|Identifier|[domain-and-range-referencing](https://ns.inria.fr/olivaw#domain-and-range-referencing)|
|----|----|
|Title|Domain&#32;and&#32;range&#32;referencing&#32;test|
|Description|A&#32;test&#32;case&#32;from&#32;the&#32;Best&#32;Practices&#32;tests&#32;checking&#32;if&#32;all&#32;the&#32;ranges&#32;and&#32;domains&#32;from&#32;the&#32;test&#32;subject&#32;point&#32;to&#32;terms&#32;that&#32;are&#32;defined&#32;in&#32;the&#32;vocabulary.|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-184)|Identifier|`domain-out-of-vocabulary`|
|[Section top](#pass-outcome-number-184)|Title|Domains&#32;properly&#32;defined|
|[Section top](#pass-outcome-number-184)|Description|Each&#32;rdfs:domain&#32;is&#32;defined&#32;within&#32;the&#32;fragment|

***
### Pass Outcome number 185

[Jump to summary definition](#summary-Pass-185)	|	[Previous Pass outcome](#pass-outcome-number-184)	|	[Next Pass outcome](#pass-outcome-number-186)

:white_check_mark:Pass outcome
#### Subject detail
|Name|modelet-manufacturing-environments-discover-core|
|----|----|
|Title|Standalone&#32;modelet&#32;domains/manufacturing-environments/discover-core/onto.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Modelet manufacturing-environments/discover-core](https://github.com/HyperAgents/hmas/blob/HEAD/domains/manufacturing-environments/discover-core/onto.ttl)|

#### Criterion detail
|Identifier|[domain-and-range-referencing](https://ns.inria.fr/olivaw#domain-and-range-referencing)|
|----|----|
|Title|Domain&#32;and&#32;range&#32;referencing&#32;test|
|Description|A&#32;test&#32;case&#32;from&#32;the&#32;Best&#32;Practices&#32;tests&#32;checking&#32;if&#32;all&#32;the&#32;ranges&#32;and&#32;domains&#32;from&#32;the&#32;test&#32;subject&#32;point&#32;to&#32;terms&#32;that&#32;are&#32;defined&#32;in&#32;the&#32;vocabulary.|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-185)|Identifier|`range-out-of-vocabulary`|
|[Section top](#pass-outcome-number-185)|Title|Ranges&#32;properly&#32;defined|
|[Section top](#pass-outcome-number-185)|Description|Each&#32;rdfs:range&#32;is&#32;defined&#32;within&#32;the&#32;fragment|

***
### Pass Outcome number 186

[Jump to summary definition](#summary-Pass-186)	|	[Previous Pass outcome](#pass-outcome-number-185)	|	[Next Pass outcome](#pass-outcome-number-187)

:white_check_mark:Pass outcome
#### Subject detail
|Name|modelet-manufacturing-environments-discover-core|
|----|----|
|Title|Standalone&#32;modelet&#32;domains/manufacturing-environments/discover-core/onto.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Modelet manufacturing-environments/discover-core](https://github.com/HyperAgents/hmas/blob/HEAD/domains/manufacturing-environments/discover-core/onto.ttl)|

#### Criterion detail
|Identifier|[labeled-terms](https://ns.inria.fr/olivaw#labeled-terms)|
|----|----|
|Title|Term&#32;labeling&#32;test|
|Description|A&#32;test&#32;case&#32;from&#32;the&#32;Best&#32;Practices&#32;tests&#32;checking&#32;if&#32;all&#32;the&#32;terms&#32;of&#32;the&#32;subject&#32;have&#32;a&#32;rdfs:label&#32;property&#32;pointing&#32;to&#32;a&#32;literal&#32;in&#32;English|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-186)|Identifier|`not-labeled-term`|
|[Section top](#pass-outcome-number-186)|Title|All&#32;terms&#32;labeled|
|[Section top](#pass-outcome-number-186)|Description|All&#32;the&#32;terms&#32;defined&#32;in&#32;the&#32;subject&#32;have&#32;a&#32;rdfs:label&#32;in&#32;English|

***
### Pass Outcome number 187

[Jump to summary definition](#summary-Pass-187)	|	[Previous Pass outcome](#pass-outcome-number-186)	|	[Next Pass outcome](#pass-outcome-number-188)

:white_check_mark:Pass outcome
#### Subject detail
|Name|modelet-manufacturing-environments-discover-core|
|----|----|
|Title|Standalone&#32;modelet&#32;domains/manufacturing-environments/discover-core/onto.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Modelet manufacturing-environments/discover-core](https://github.com/HyperAgents/hmas/blob/HEAD/domains/manufacturing-environments/discover-core/onto.ttl)|

#### Criterion detail
|Identifier|[owl-rl-constraint](https://ns.inria.fr/olivaw#owl-rl-constraint)|
|----|----|
|Title|OWL&#32;RL&#32;Constraint&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;check&#32;wether&#32;the&#32;test&#32;subject&#32;is&#32;syntaxically&#32;correct&#32;or&#32;not.|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-187)|Identifier|`owl-rl-constraint-violation`|
|[Section top](#pass-outcome-number-187)|Title|OWL&#32;RL&#32;consistent|
|[Section top](#pass-outcome-number-187)|Description|The&#32;provided&#32;graph&#32;is&#32;consistent&#32;for&#32;any&#32;OWL&#32;RL&#32;constraint|

***
### Pass Outcome number 188

[Jump to summary definition](#summary-Pass-188)	|	[Previous Pass outcome](#pass-outcome-number-187)	|	[Next Pass outcome](#pass-outcome-number-189)

:white_check_mark:Pass outcome
#### Subject detail
|Name|modelet-manufacturing-environments-discover-core|
|----|----|
|Title|Standalone&#32;modelet&#32;domains/manufacturing-environments/discover-core/onto.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Modelet manufacturing-environments/discover-core](https://github.com/HyperAgents/hmas/blob/HEAD/domains/manufacturing-environments/discover-core/onto.ttl)|

#### Criterion detail
|Identifier|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|
|----|----|
|Title|Profile&#32;compatibility&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;check&#32;whether&#32;the&#32;test&#32;subject&#32;is&#32;compatible&#32;with&#32;a&#32;profile&#32;or&#32;not,&#32;and&#32;if&#32;it&#32;is&#32;not,&#32;why.|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-188)|Identifier|`owl-rl-profile-error`|
|[Section top](#pass-outcome-number-188)|Title|OWL&#32;RL&#32;Profile&#32;compatible|
|[Section top](#pass-outcome-number-188)|Description|The&#32;subject&#32;is&#32;included&#32;in&#32;the&#32;OWL&#32;RL&#32;sublanguage|

***
### Pass Outcome number 189

[Jump to summary definition](#summary-Pass-189)	|	[Previous Pass outcome](#pass-outcome-number-188)	|	[Next Pass outcome](#pass-outcome-number-190)

:white_check_mark:Pass outcome
#### Subject detail
|Name|modelet-manufacturing-environments-discover-core|
|----|----|
|Title|Standalone&#32;modelet&#32;domains/manufacturing-environments/discover-core/onto.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Modelet manufacturing-environments/discover-core](https://github.com/HyperAgents/hmas/blob/HEAD/domains/manufacturing-environments/discover-core/onto.ttl)|

#### Criterion detail
|Identifier|[proper-extension-predicate](https://ns.inria.fr/olivaw#proper-extension-predicate)|
|----|----|
|Title|Predicate&#32;extension&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;test&#32;the&#32;proper&#32;use&#32;of&#32;predicates&#32;rdfs:subClassOf&#32;and&#32;rdfs:subPropertyOf&#32;on&#32;the&#32;ontology&#32;terms|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-189)|Identifier|`class-subpropertyof`|
|[Section top](#pass-outcome-number-189)|Title|No&#32;class&#32;subproperty|
|[Section top](#pass-outcome-number-189)|Description|No&#32;ontology&#32;class&#32;is&#32;a&#32;subproperty|

***
### Pass Outcome number 190

[Jump to summary definition](#summary-Pass-190)	|	[Previous Pass outcome](#pass-outcome-number-189)	|	[Next Pass outcome](#pass-outcome-number-191)

:white_check_mark:Pass outcome
#### Subject detail
|Name|modelet-manufacturing-environments-discover-core|
|----|----|
|Title|Standalone&#32;modelet&#32;domains/manufacturing-environments/discover-core/onto.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Modelet manufacturing-environments/discover-core](https://github.com/HyperAgents/hmas/blob/HEAD/domains/manufacturing-environments/discover-core/onto.ttl)|

#### Criterion detail
|Identifier|[proper-extension-predicate](https://ns.inria.fr/olivaw#proper-extension-predicate)|
|----|----|
|Title|Predicate&#32;extension&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;test&#32;the&#32;proper&#32;use&#32;of&#32;predicates&#32;rdfs:subClassOf&#32;and&#32;rdfs:subPropertyOf&#32;on&#32;the&#32;ontology&#32;terms|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-190)|Identifier|`property-subclassof`|
|[Section top](#pass-outcome-number-190)|Title|No&#32;property&#32;subclass|
|[Section top](#pass-outcome-number-190)|Description|No&#32;ontology&#32;property&#32;is&#32;a&#32;subclass|

***
### Pass Outcome number 191

[Jump to summary definition](#summary-Pass-191)	|	[Previous Pass outcome](#pass-outcome-number-190)	|	[Next Pass outcome](#pass-outcome-number-192)

:white_check_mark:Pass outcome
#### Subject detail
|Name|modelet-manufacturing-environments-discover-core|
|----|----|
|Title|Standalone&#32;modelet&#32;domains/manufacturing-environments/discover-core/onto.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Modelet manufacturing-environments/discover-core](https://github.com/HyperAgents/hmas/blob/HEAD/domains/manufacturing-environments/discover-core/onto.ttl)|

#### Criterion detail
|Identifier|[proper-extension-predicate](https://ns.inria.fr/olivaw#proper-extension-predicate)|
|----|----|
|Title|Predicate&#32;extension&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;test&#32;the&#32;proper&#32;use&#32;of&#32;predicates&#32;rdfs:subClassOf&#32;and&#32;rdfs:subPropertyOf&#32;on&#32;the&#32;ontology&#32;terms|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-191)|Identifier|`subclassof-property`|
|[Section top](#pass-outcome-number-191)|Title|No&#32;subclass&#32;of&#32;property|
|[Section top](#pass-outcome-number-191)|Description|No&#32;ontology&#32;term&#32;is&#32;a&#32;subclass&#32;of&#32;a&#32;property|

***
### Pass Outcome number 192

[Jump to summary definition](#summary-Pass-192)	|	[Previous Pass outcome](#pass-outcome-number-191)	|	[Next Pass outcome](#pass-outcome-number-193)

:white_check_mark:Pass outcome
#### Subject detail
|Name|modelet-manufacturing-environments-discover-core|
|----|----|
|Title|Standalone&#32;modelet&#32;domains/manufacturing-environments/discover-core/onto.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Modelet manufacturing-environments/discover-core](https://github.com/HyperAgents/hmas/blob/HEAD/domains/manufacturing-environments/discover-core/onto.ttl)|

#### Criterion detail
|Identifier|[proper-extension-predicate](https://ns.inria.fr/olivaw#proper-extension-predicate)|
|----|----|
|Title|Predicate&#32;extension&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;test&#32;the&#32;proper&#32;use&#32;of&#32;predicates&#32;rdfs:subClassOf&#32;and&#32;rdfs:subPropertyOf&#32;on&#32;the&#32;ontology&#32;terms|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-192)|Identifier|`subpropertyof-class`|
|[Section top](#pass-outcome-number-192)|Title|No&#32;subproperty&#32;of&#32;class|
|[Section top](#pass-outcome-number-192)|Description|No&#32;ontology&#32;term&#32;is&#32;a&#32;subproperty&#32;of&#32;a&#32;class|

***
### Pass Outcome number 193

[Jump to summary definition](#summary-Pass-193)	|	[Previous Pass outcome](#pass-outcome-number-192)	|	[Next Pass outcome](#pass-outcome-number-194)

:white_check_mark:Pass outcome
#### Subject detail
|Name|modelet-manufacturing-environments-discover-core|
|----|----|
|Title|Standalone&#32;modelet&#32;domains/manufacturing-environments/discover-core/onto.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Modelet manufacturing-environments/discover-core](https://github.com/HyperAgents/hmas/blob/HEAD/domains/manufacturing-environments/discover-core/onto.ttl)|

#### Criterion detail
|Identifier|[term-referencing](https://ns.inria.fr/olivaw#term-referencing)|
|----|----|
|Title|Term&#32;referencing&#32;test|
|Description|A&#32;test&#32;case&#32;from&#32;the&#32;Best&#32;Practices&#32;tests&#32;checking&#32;if&#32;each&#32;term&#32;of&#32;the&#32;test&#32;subject&#32;is&#32;referenced&#32;to&#32;a&#32;module&#32;through&#32;a&#32;rdfs:isDefinedBy&#32;property.|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-193)|Identifier|`no-reference-module`|
|[Section top](#pass-outcome-number-193)|Title|Any&#32;term&#32;is&#32;referenced|
|[Section top](#pass-outcome-number-193)|Description|Each&#32;term&#32;of&#32;the&#32;test&#32;subject&#32;is&#32;linked&#32;to&#32;a&#32;module&#32;by&#32;a&#32;rdfs:isDefinedBy&#32;property|

***
### Pass Outcome number 194

[Jump to summary definition](#summary-Pass-194)	|	[Previous Pass outcome](#pass-outcome-number-193)	|	[Next Pass outcome](#pass-outcome-number-195)

:white_check_mark:Pass outcome
#### Subject detail
|Name|modelet-manufacturing-environments-discover-core|
|----|----|
|Title|Standalone&#32;modelet&#32;domains/manufacturing-environments/discover-core/onto.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Modelet manufacturing-environments/discover-core](https://github.com/HyperAgents/hmas/blob/HEAD/domains/manufacturing-environments/discover-core/onto.ttl)|

#### Criterion detail
|Identifier|[terms-differenciation](https://ns.inria.fr/olivaw#terms-differenciation)|
|----|----|
|Title|Terms&#32;differenciation&#32;test|
|Description|A&#32;test&#32;case&#32;from&#32;the&#32;Best&#32;Practices&#32;tests&#32;checking&#32;if&#32;all&#32;the&#32;terms&#32;are&#32;different&#32;enough&#32;from&#32;each&#32;other&#32;according&#32;to&#32;the&#32;Levenshtein&#32;distance&#32;metric.|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-194)|Identifier|`too-close-terms`|
|[Section top](#pass-outcome-number-194)|Title|Terms&#32;differenciated&#32;enough|
|[Section top](#pass-outcome-number-194)|Description|All&#32;the&#32;terms&#32;have&#32;have&#32;a&#32;satisfying&#32;Levenshtein&#32;distance&#32;from&#32;each&#32;other&#32;term.|

***
### Pass Outcome number 195

[Jump to summary definition](#summary-Pass-195)	|	[Previous Pass outcome](#pass-outcome-number-194)	|	[Next Pass outcome](#pass-outcome-number-196)

:white_check_mark:Pass outcome
#### Subject detail
|Name|modelet-manufacturing-environments-discover-behavior-specifications|
|----|----|
|Title|Standalone&#32;modelet&#32;domains/manufacturing-environments/discover-behavior-specifications/onto.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Modelet manufacturing-environments/discover-behavior-specifications](https://github.com/HyperAgents/hmas/blob/HEAD/domains/manufacturing-environments/discover-behavior-specifications/onto.ttl)|

#### Criterion detail
|Identifier|[domain-and-range-referencing](https://ns.inria.fr/olivaw#domain-and-range-referencing)|
|----|----|
|Title|Domain&#32;and&#32;range&#32;referencing&#32;test|
|Description|A&#32;test&#32;case&#32;from&#32;the&#32;Best&#32;Practices&#32;tests&#32;checking&#32;if&#32;all&#32;the&#32;ranges&#32;and&#32;domains&#32;from&#32;the&#32;test&#32;subject&#32;point&#32;to&#32;terms&#32;that&#32;are&#32;defined&#32;in&#32;the&#32;vocabulary.|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-195)|Identifier|`domain-out-of-vocabulary`|
|[Section top](#pass-outcome-number-195)|Title|Domains&#32;properly&#32;defined|
|[Section top](#pass-outcome-number-195)|Description|Each&#32;rdfs:domain&#32;is&#32;defined&#32;within&#32;the&#32;fragment|

***
### Pass Outcome number 196

[Jump to summary definition](#summary-Pass-196)	|	[Previous Pass outcome](#pass-outcome-number-195)	|	[Next Pass outcome](#pass-outcome-number-197)

:white_check_mark:Pass outcome
#### Subject detail
|Name|modelet-manufacturing-environments-discover-behavior-specifications|
|----|----|
|Title|Standalone&#32;modelet&#32;domains/manufacturing-environments/discover-behavior-specifications/onto.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Modelet manufacturing-environments/discover-behavior-specifications](https://github.com/HyperAgents/hmas/blob/HEAD/domains/manufacturing-environments/discover-behavior-specifications/onto.ttl)|

#### Criterion detail
|Identifier|[domain-and-range-referencing](https://ns.inria.fr/olivaw#domain-and-range-referencing)|
|----|----|
|Title|Domain&#32;and&#32;range&#32;referencing&#32;test|
|Description|A&#32;test&#32;case&#32;from&#32;the&#32;Best&#32;Practices&#32;tests&#32;checking&#32;if&#32;all&#32;the&#32;ranges&#32;and&#32;domains&#32;from&#32;the&#32;test&#32;subject&#32;point&#32;to&#32;terms&#32;that&#32;are&#32;defined&#32;in&#32;the&#32;vocabulary.|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-196)|Identifier|`range-out-of-vocabulary`|
|[Section top](#pass-outcome-number-196)|Title|Ranges&#32;properly&#32;defined|
|[Section top](#pass-outcome-number-196)|Description|Each&#32;rdfs:range&#32;is&#32;defined&#32;within&#32;the&#32;fragment|

***
### Pass Outcome number 197

[Jump to summary definition](#summary-Pass-197)	|	[Previous Pass outcome](#pass-outcome-number-196)	|	[Next Pass outcome](#pass-outcome-number-198)

:white_check_mark:Pass outcome
#### Subject detail
|Name|modelet-manufacturing-environments-discover-behavior-specifications|
|----|----|
|Title|Standalone&#32;modelet&#32;domains/manufacturing-environments/discover-behavior-specifications/onto.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Modelet manufacturing-environments/discover-behavior-specifications](https://github.com/HyperAgents/hmas/blob/HEAD/domains/manufacturing-environments/discover-behavior-specifications/onto.ttl)|

#### Criterion detail
|Identifier|[labeled-terms](https://ns.inria.fr/olivaw#labeled-terms)|
|----|----|
|Title|Term&#32;labeling&#32;test|
|Description|A&#32;test&#32;case&#32;from&#32;the&#32;Best&#32;Practices&#32;tests&#32;checking&#32;if&#32;all&#32;the&#32;terms&#32;of&#32;the&#32;subject&#32;have&#32;a&#32;rdfs:label&#32;property&#32;pointing&#32;to&#32;a&#32;literal&#32;in&#32;English|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-197)|Identifier|`not-labeled-term`|
|[Section top](#pass-outcome-number-197)|Title|All&#32;terms&#32;labeled|
|[Section top](#pass-outcome-number-197)|Description|All&#32;the&#32;terms&#32;defined&#32;in&#32;the&#32;subject&#32;have&#32;a&#32;rdfs:label&#32;in&#32;English|

***
### Pass Outcome number 198

[Jump to summary definition](#summary-Pass-198)	|	[Previous Pass outcome](#pass-outcome-number-197)	|	[Next Pass outcome](#pass-outcome-number-199)

:white_check_mark:Pass outcome
#### Subject detail
|Name|modelet-manufacturing-environments-discover-behavior-specifications|
|----|----|
|Title|Standalone&#32;modelet&#32;domains/manufacturing-environments/discover-behavior-specifications/onto.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Modelet manufacturing-environments/discover-behavior-specifications](https://github.com/HyperAgents/hmas/blob/HEAD/domains/manufacturing-environments/discover-behavior-specifications/onto.ttl)|

#### Criterion detail
|Identifier|[owl-rl-constraint](https://ns.inria.fr/olivaw#owl-rl-constraint)|
|----|----|
|Title|OWL&#32;RL&#32;Constraint&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;check&#32;wether&#32;the&#32;test&#32;subject&#32;is&#32;syntaxically&#32;correct&#32;or&#32;not.|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-198)|Identifier|`owl-rl-constraint-violation`|
|[Section top](#pass-outcome-number-198)|Title|OWL&#32;RL&#32;consistent|
|[Section top](#pass-outcome-number-198)|Description|The&#32;provided&#32;graph&#32;is&#32;consistent&#32;for&#32;any&#32;OWL&#32;RL&#32;constraint|

***
### Pass Outcome number 199

[Jump to summary definition](#summary-Pass-199)	|	[Previous Pass outcome](#pass-outcome-number-198)	|	[Next Pass outcome](#pass-outcome-number-200)

:white_check_mark:Pass outcome
#### Subject detail
|Name|modelet-manufacturing-environments-discover-behavior-specifications|
|----|----|
|Title|Standalone&#32;modelet&#32;domains/manufacturing-environments/discover-behavior-specifications/onto.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Modelet manufacturing-environments/discover-behavior-specifications](https://github.com/HyperAgents/hmas/blob/HEAD/domains/manufacturing-environments/discover-behavior-specifications/onto.ttl)|

#### Criterion detail
|Identifier|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|
|----|----|
|Title|Profile&#32;compatibility&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;check&#32;whether&#32;the&#32;test&#32;subject&#32;is&#32;compatible&#32;with&#32;a&#32;profile&#32;or&#32;not,&#32;and&#32;if&#32;it&#32;is&#32;not,&#32;why.|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-199)|Identifier|`owl-el-profile-error`|
|[Section top](#pass-outcome-number-199)|Title|OWL&#32;EL&#32;Profile&#32;compatible|
|[Section top](#pass-outcome-number-199)|Description|The&#32;subject&#32;is&#32;included&#32;in&#32;the&#32;OWL&#32;EL&#32;sublanguage|

***
### Pass Outcome number 200

[Jump to summary definition](#summary-Pass-200)	|	[Previous Pass outcome](#pass-outcome-number-199)	|	[Next Pass outcome](#pass-outcome-number-201)

:white_check_mark:Pass outcome
#### Subject detail
|Name|modelet-manufacturing-environments-discover-behavior-specifications|
|----|----|
|Title|Standalone&#32;modelet&#32;domains/manufacturing-environments/discover-behavior-specifications/onto.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Modelet manufacturing-environments/discover-behavior-specifications](https://github.com/HyperAgents/hmas/blob/HEAD/domains/manufacturing-environments/discover-behavior-specifications/onto.ttl)|

#### Criterion detail
|Identifier|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|
|----|----|
|Title|Profile&#32;compatibility&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;check&#32;whether&#32;the&#32;test&#32;subject&#32;is&#32;compatible&#32;with&#32;a&#32;profile&#32;or&#32;not,&#32;and&#32;if&#32;it&#32;is&#32;not,&#32;why.|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-200)|Identifier|`owl-ql-profile-error`|
|[Section top](#pass-outcome-number-200)|Title|OWL&#32;QL&#32;Profile&#32;compatible|
|[Section top](#pass-outcome-number-200)|Description|The&#32;subject&#32;is&#32;included&#32;in&#32;the&#32;OWL&#32;QL&#32;sublanguage|

***
### Pass Outcome number 201

[Jump to summary definition](#summary-Pass-201)	|	[Previous Pass outcome](#pass-outcome-number-200)	|	[Next Pass outcome](#pass-outcome-number-202)

:white_check_mark:Pass outcome
#### Subject detail
|Name|modelet-manufacturing-environments-discover-behavior-specifications|
|----|----|
|Title|Standalone&#32;modelet&#32;domains/manufacturing-environments/discover-behavior-specifications/onto.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Modelet manufacturing-environments/discover-behavior-specifications](https://github.com/HyperAgents/hmas/blob/HEAD/domains/manufacturing-environments/discover-behavior-specifications/onto.ttl)|

#### Criterion detail
|Identifier|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|
|----|----|
|Title|Profile&#32;compatibility&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;check&#32;whether&#32;the&#32;test&#32;subject&#32;is&#32;compatible&#32;with&#32;a&#32;profile&#32;or&#32;not,&#32;and&#32;if&#32;it&#32;is&#32;not,&#32;why.|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-201)|Identifier|`owl-rl-profile-error`|
|[Section top](#pass-outcome-number-201)|Title|OWL&#32;RL&#32;Profile&#32;compatible|
|[Section top](#pass-outcome-number-201)|Description|The&#32;subject&#32;is&#32;included&#32;in&#32;the&#32;OWL&#32;RL&#32;sublanguage|

***
### Pass Outcome number 202

[Jump to summary definition](#summary-Pass-202)	|	[Previous Pass outcome](#pass-outcome-number-201)	|	[Next Pass outcome](#pass-outcome-number-203)

:white_check_mark:Pass outcome
#### Subject detail
|Name|modelet-manufacturing-environments-discover-behavior-specifications|
|----|----|
|Title|Standalone&#32;modelet&#32;domains/manufacturing-environments/discover-behavior-specifications/onto.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Modelet manufacturing-environments/discover-behavior-specifications](https://github.com/HyperAgents/hmas/blob/HEAD/domains/manufacturing-environments/discover-behavior-specifications/onto.ttl)|

#### Criterion detail
|Identifier|[proper-extension-predicate](https://ns.inria.fr/olivaw#proper-extension-predicate)|
|----|----|
|Title|Predicate&#32;extension&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;test&#32;the&#32;proper&#32;use&#32;of&#32;predicates&#32;rdfs:subClassOf&#32;and&#32;rdfs:subPropertyOf&#32;on&#32;the&#32;ontology&#32;terms|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-202)|Identifier|`class-subpropertyof`|
|[Section top](#pass-outcome-number-202)|Title|No&#32;class&#32;subproperty|
|[Section top](#pass-outcome-number-202)|Description|No&#32;ontology&#32;class&#32;is&#32;a&#32;subproperty|

***
### Pass Outcome number 203

[Jump to summary definition](#summary-Pass-203)	|	[Previous Pass outcome](#pass-outcome-number-202)	|	[Next Pass outcome](#pass-outcome-number-204)

:white_check_mark:Pass outcome
#### Subject detail
|Name|modelet-manufacturing-environments-discover-behavior-specifications|
|----|----|
|Title|Standalone&#32;modelet&#32;domains/manufacturing-environments/discover-behavior-specifications/onto.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Modelet manufacturing-environments/discover-behavior-specifications](https://github.com/HyperAgents/hmas/blob/HEAD/domains/manufacturing-environments/discover-behavior-specifications/onto.ttl)|

#### Criterion detail
|Identifier|[proper-extension-predicate](https://ns.inria.fr/olivaw#proper-extension-predicate)|
|----|----|
|Title|Predicate&#32;extension&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;test&#32;the&#32;proper&#32;use&#32;of&#32;predicates&#32;rdfs:subClassOf&#32;and&#32;rdfs:subPropertyOf&#32;on&#32;the&#32;ontology&#32;terms|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-203)|Identifier|`property-subclassof`|
|[Section top](#pass-outcome-number-203)|Title|No&#32;property&#32;subclass|
|[Section top](#pass-outcome-number-203)|Description|No&#32;ontology&#32;property&#32;is&#32;a&#32;subclass|

***
### Pass Outcome number 204

[Jump to summary definition](#summary-Pass-204)	|	[Previous Pass outcome](#pass-outcome-number-203)	|	[Next Pass outcome](#pass-outcome-number-205)

:white_check_mark:Pass outcome
#### Subject detail
|Name|modelet-manufacturing-environments-discover-behavior-specifications|
|----|----|
|Title|Standalone&#32;modelet&#32;domains/manufacturing-environments/discover-behavior-specifications/onto.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Modelet manufacturing-environments/discover-behavior-specifications](https://github.com/HyperAgents/hmas/blob/HEAD/domains/manufacturing-environments/discover-behavior-specifications/onto.ttl)|

#### Criterion detail
|Identifier|[proper-extension-predicate](https://ns.inria.fr/olivaw#proper-extension-predicate)|
|----|----|
|Title|Predicate&#32;extension&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;test&#32;the&#32;proper&#32;use&#32;of&#32;predicates&#32;rdfs:subClassOf&#32;and&#32;rdfs:subPropertyOf&#32;on&#32;the&#32;ontology&#32;terms|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-204)|Identifier|`subclassof-property`|
|[Section top](#pass-outcome-number-204)|Title|No&#32;subclass&#32;of&#32;property|
|[Section top](#pass-outcome-number-204)|Description|No&#32;ontology&#32;term&#32;is&#32;a&#32;subclass&#32;of&#32;a&#32;property|

***
### Pass Outcome number 205

[Jump to summary definition](#summary-Pass-205)	|	[Previous Pass outcome](#pass-outcome-number-204)	|	[Next Pass outcome](#pass-outcome-number-206)

:white_check_mark:Pass outcome
#### Subject detail
|Name|modelet-manufacturing-environments-discover-behavior-specifications|
|----|----|
|Title|Standalone&#32;modelet&#32;domains/manufacturing-environments/discover-behavior-specifications/onto.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Modelet manufacturing-environments/discover-behavior-specifications](https://github.com/HyperAgents/hmas/blob/HEAD/domains/manufacturing-environments/discover-behavior-specifications/onto.ttl)|

#### Criterion detail
|Identifier|[proper-extension-predicate](https://ns.inria.fr/olivaw#proper-extension-predicate)|
|----|----|
|Title|Predicate&#32;extension&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;test&#32;the&#32;proper&#32;use&#32;of&#32;predicates&#32;rdfs:subClassOf&#32;and&#32;rdfs:subPropertyOf&#32;on&#32;the&#32;ontology&#32;terms|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-205)|Identifier|`subpropertyof-class`|
|[Section top](#pass-outcome-number-205)|Title|No&#32;subproperty&#32;of&#32;class|
|[Section top](#pass-outcome-number-205)|Description|No&#32;ontology&#32;term&#32;is&#32;a&#32;subproperty&#32;of&#32;a&#32;class|

***
### Pass Outcome number 206

[Jump to summary definition](#summary-Pass-206)	|	[Previous Pass outcome](#pass-outcome-number-205)	|	[Next Pass outcome](#pass-outcome-number-207)

:white_check_mark:Pass outcome
#### Subject detail
|Name|modelet-manufacturing-environments-discover-behavior-specifications|
|----|----|
|Title|Standalone&#32;modelet&#32;domains/manufacturing-environments/discover-behavior-specifications/onto.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Modelet manufacturing-environments/discover-behavior-specifications](https://github.com/HyperAgents/hmas/blob/HEAD/domains/manufacturing-environments/discover-behavior-specifications/onto.ttl)|

#### Criterion detail
|Identifier|[term-referencing](https://ns.inria.fr/olivaw#term-referencing)|
|----|----|
|Title|Term&#32;referencing&#32;test|
|Description|A&#32;test&#32;case&#32;from&#32;the&#32;Best&#32;Practices&#32;tests&#32;checking&#32;if&#32;each&#32;term&#32;of&#32;the&#32;test&#32;subject&#32;is&#32;referenced&#32;to&#32;a&#32;module&#32;through&#32;a&#32;rdfs:isDefinedBy&#32;property.|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-206)|Identifier|`no-reference-module`|
|[Section top](#pass-outcome-number-206)|Title|Any&#32;term&#32;is&#32;referenced|
|[Section top](#pass-outcome-number-206)|Description|Each&#32;term&#32;of&#32;the&#32;test&#32;subject&#32;is&#32;linked&#32;to&#32;a&#32;module&#32;by&#32;a&#32;rdfs:isDefinedBy&#32;property|

***
### Pass Outcome number 207

[Jump to summary definition](#summary-Pass-207)	|	[Previous Pass outcome](#pass-outcome-number-206)	|	[Next Pass outcome](#pass-outcome-number-208)

:white_check_mark:Pass outcome
#### Subject detail
|Name|modelet-manufacturing-environments-discover-behavior-specifications|
|----|----|
|Title|Standalone&#32;modelet&#32;domains/manufacturing-environments/discover-behavior-specifications/onto.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Modelet manufacturing-environments/discover-behavior-specifications](https://github.com/HyperAgents/hmas/blob/HEAD/domains/manufacturing-environments/discover-behavior-specifications/onto.ttl)|

#### Criterion detail
|Identifier|[terms-differenciation](https://ns.inria.fr/olivaw#terms-differenciation)|
|----|----|
|Title|Terms&#32;differenciation&#32;test|
|Description|A&#32;test&#32;case&#32;from&#32;the&#32;Best&#32;Practices&#32;tests&#32;checking&#32;if&#32;all&#32;the&#32;terms&#32;are&#32;different&#32;enough&#32;from&#32;each&#32;other&#32;according&#32;to&#32;the&#32;Levenshtein&#32;distance&#32;metric.|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-207)|Identifier|`too-close-terms`|
|[Section top](#pass-outcome-number-207)|Title|Terms&#32;differenciated&#32;enough|
|[Section top](#pass-outcome-number-207)|Description|All&#32;the&#32;terms&#32;have&#32;have&#32;a&#32;satisfying&#32;Levenshtein&#32;distance&#32;from&#32;each&#32;other&#32;term.|

***
### Pass Outcome number 208

[Jump to summary definition](#summary-Pass-208)	|	[Previous Pass outcome](#pass-outcome-number-207)	|	[Next Pass outcome](#pass-outcome-number-209)

:white_check_mark:Pass outcome
#### Subject detail
|Name|modelet-logistics-create-organization|
|----|----|
|Title|Standalone&#32;modelet&#32;domains/logistics/create-organization/onto.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Modelet logistics/create-organization](https://github.com/HyperAgents/hmas/blob/HEAD/domains/logistics/create-organization/onto.ttl)|

#### Criterion detail
|Identifier|[domain-and-range-referencing](https://ns.inria.fr/olivaw#domain-and-range-referencing)|
|----|----|
|Title|Domain&#32;and&#32;range&#32;referencing&#32;test|
|Description|A&#32;test&#32;case&#32;from&#32;the&#32;Best&#32;Practices&#32;tests&#32;checking&#32;if&#32;all&#32;the&#32;ranges&#32;and&#32;domains&#32;from&#32;the&#32;test&#32;subject&#32;point&#32;to&#32;terms&#32;that&#32;are&#32;defined&#32;in&#32;the&#32;vocabulary.|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-208)|Identifier|`domain-out-of-vocabulary`|
|[Section top](#pass-outcome-number-208)|Title|Domains&#32;properly&#32;defined|
|[Section top](#pass-outcome-number-208)|Description|Each&#32;rdfs:domain&#32;is&#32;defined&#32;within&#32;the&#32;fragment|

***
### Pass Outcome number 209

[Jump to summary definition](#summary-Pass-209)	|	[Previous Pass outcome](#pass-outcome-number-208)	|	[Next Pass outcome](#pass-outcome-number-210)

:white_check_mark:Pass outcome
#### Subject detail
|Name|modelet-logistics-create-organization|
|----|----|
|Title|Standalone&#32;modelet&#32;domains/logistics/create-organization/onto.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Modelet logistics/create-organization](https://github.com/HyperAgents/hmas/blob/HEAD/domains/logistics/create-organization/onto.ttl)|

#### Criterion detail
|Identifier|[domain-and-range-referencing](https://ns.inria.fr/olivaw#domain-and-range-referencing)|
|----|----|
|Title|Domain&#32;and&#32;range&#32;referencing&#32;test|
|Description|A&#32;test&#32;case&#32;from&#32;the&#32;Best&#32;Practices&#32;tests&#32;checking&#32;if&#32;all&#32;the&#32;ranges&#32;and&#32;domains&#32;from&#32;the&#32;test&#32;subject&#32;point&#32;to&#32;terms&#32;that&#32;are&#32;defined&#32;in&#32;the&#32;vocabulary.|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-209)|Identifier|`range-out-of-vocabulary`|
|[Section top](#pass-outcome-number-209)|Title|Ranges&#32;properly&#32;defined|
|[Section top](#pass-outcome-number-209)|Description|Each&#32;rdfs:range&#32;is&#32;defined&#32;within&#32;the&#32;fragment|

***
### Pass Outcome number 210

[Jump to summary definition](#summary-Pass-210)	|	[Previous Pass outcome](#pass-outcome-number-209)	|	[Next Pass outcome](#pass-outcome-number-211)

:white_check_mark:Pass outcome
#### Subject detail
|Name|modelet-logistics-create-organization|
|----|----|
|Title|Standalone&#32;modelet&#32;domains/logistics/create-organization/onto.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Modelet logistics/create-organization](https://github.com/HyperAgents/hmas/blob/HEAD/domains/logistics/create-organization/onto.ttl)|

#### Criterion detail
|Identifier|[labeled-terms](https://ns.inria.fr/olivaw#labeled-terms)|
|----|----|
|Title|Term&#32;labeling&#32;test|
|Description|A&#32;test&#32;case&#32;from&#32;the&#32;Best&#32;Practices&#32;tests&#32;checking&#32;if&#32;all&#32;the&#32;terms&#32;of&#32;the&#32;subject&#32;have&#32;a&#32;rdfs:label&#32;property&#32;pointing&#32;to&#32;a&#32;literal&#32;in&#32;English|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-210)|Identifier|`not-labeled-term`|
|[Section top](#pass-outcome-number-210)|Title|All&#32;terms&#32;labeled|
|[Section top](#pass-outcome-number-210)|Description|All&#32;the&#32;terms&#32;defined&#32;in&#32;the&#32;subject&#32;have&#32;a&#32;rdfs:label&#32;in&#32;English|

***
### Pass Outcome number 211

[Jump to summary definition](#summary-Pass-211)	|	[Previous Pass outcome](#pass-outcome-number-210)	|	[Next Pass outcome](#pass-outcome-number-212)

:white_check_mark:Pass outcome
#### Subject detail
|Name|modelet-logistics-create-organization|
|----|----|
|Title|Standalone&#32;modelet&#32;domains/logistics/create-organization/onto.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Modelet logistics/create-organization](https://github.com/HyperAgents/hmas/blob/HEAD/domains/logistics/create-organization/onto.ttl)|

#### Criterion detail
|Identifier|[owl-rl-constraint](https://ns.inria.fr/olivaw#owl-rl-constraint)|
|----|----|
|Title|OWL&#32;RL&#32;Constraint&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;check&#32;wether&#32;the&#32;test&#32;subject&#32;is&#32;syntaxically&#32;correct&#32;or&#32;not.|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-211)|Identifier|`owl-rl-constraint-violation`|
|[Section top](#pass-outcome-number-211)|Title|OWL&#32;RL&#32;consistent|
|[Section top](#pass-outcome-number-211)|Description|The&#32;provided&#32;graph&#32;is&#32;consistent&#32;for&#32;any&#32;OWL&#32;RL&#32;constraint|

***
### Pass Outcome number 212

[Jump to summary definition](#summary-Pass-212)	|	[Previous Pass outcome](#pass-outcome-number-211)	|	[Next Pass outcome](#pass-outcome-number-213)

:white_check_mark:Pass outcome
#### Subject detail
|Name|modelet-logistics-create-organization|
|----|----|
|Title|Standalone&#32;modelet&#32;domains/logistics/create-organization/onto.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Modelet logistics/create-organization](https://github.com/HyperAgents/hmas/blob/HEAD/domains/logistics/create-organization/onto.ttl)|

#### Criterion detail
|Identifier|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|
|----|----|
|Title|Profile&#32;compatibility&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;check&#32;whether&#32;the&#32;test&#32;subject&#32;is&#32;compatible&#32;with&#32;a&#32;profile&#32;or&#32;not,&#32;and&#32;if&#32;it&#32;is&#32;not,&#32;why.|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-212)|Identifier|`owl-el-profile-error`|
|[Section top](#pass-outcome-number-212)|Title|OWL&#32;EL&#32;Profile&#32;compatible|
|[Section top](#pass-outcome-number-212)|Description|The&#32;subject&#32;is&#32;included&#32;in&#32;the&#32;OWL&#32;EL&#32;sublanguage|

***
### Pass Outcome number 213

[Jump to summary definition](#summary-Pass-213)	|	[Previous Pass outcome](#pass-outcome-number-212)	|	[Next Pass outcome](#pass-outcome-number-214)

:white_check_mark:Pass outcome
#### Subject detail
|Name|modelet-logistics-create-organization|
|----|----|
|Title|Standalone&#32;modelet&#32;domains/logistics/create-organization/onto.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Modelet logistics/create-organization](https://github.com/HyperAgents/hmas/blob/HEAD/domains/logistics/create-organization/onto.ttl)|

#### Criterion detail
|Identifier|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|
|----|----|
|Title|Profile&#32;compatibility&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;check&#32;whether&#32;the&#32;test&#32;subject&#32;is&#32;compatible&#32;with&#32;a&#32;profile&#32;or&#32;not,&#32;and&#32;if&#32;it&#32;is&#32;not,&#32;why.|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-213)|Identifier|`owl-ql-profile-error`|
|[Section top](#pass-outcome-number-213)|Title|OWL&#32;QL&#32;Profile&#32;compatible|
|[Section top](#pass-outcome-number-213)|Description|The&#32;subject&#32;is&#32;included&#32;in&#32;the&#32;OWL&#32;QL&#32;sublanguage|

***
### Pass Outcome number 214

[Jump to summary definition](#summary-Pass-214)	|	[Previous Pass outcome](#pass-outcome-number-213)	|	[Next Pass outcome](#pass-outcome-number-215)

:white_check_mark:Pass outcome
#### Subject detail
|Name|modelet-logistics-create-organization|
|----|----|
|Title|Standalone&#32;modelet&#32;domains/logistics/create-organization/onto.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Modelet logistics/create-organization](https://github.com/HyperAgents/hmas/blob/HEAD/domains/logistics/create-organization/onto.ttl)|

#### Criterion detail
|Identifier|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|
|----|----|
|Title|Profile&#32;compatibility&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;check&#32;whether&#32;the&#32;test&#32;subject&#32;is&#32;compatible&#32;with&#32;a&#32;profile&#32;or&#32;not,&#32;and&#32;if&#32;it&#32;is&#32;not,&#32;why.|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-214)|Identifier|`owl-rl-profile-error`|
|[Section top](#pass-outcome-number-214)|Title|OWL&#32;RL&#32;Profile&#32;compatible|
|[Section top](#pass-outcome-number-214)|Description|The&#32;subject&#32;is&#32;included&#32;in&#32;the&#32;OWL&#32;RL&#32;sublanguage|

***
### Pass Outcome number 215

[Jump to summary definition](#summary-Pass-215)	|	[Previous Pass outcome](#pass-outcome-number-214)	|	[Next Pass outcome](#pass-outcome-number-216)

:white_check_mark:Pass outcome
#### Subject detail
|Name|modelet-logistics-create-organization|
|----|----|
|Title|Standalone&#32;modelet&#32;domains/logistics/create-organization/onto.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Modelet logistics/create-organization](https://github.com/HyperAgents/hmas/blob/HEAD/domains/logistics/create-organization/onto.ttl)|

#### Criterion detail
|Identifier|[proper-extension-predicate](https://ns.inria.fr/olivaw#proper-extension-predicate)|
|----|----|
|Title|Predicate&#32;extension&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;test&#32;the&#32;proper&#32;use&#32;of&#32;predicates&#32;rdfs:subClassOf&#32;and&#32;rdfs:subPropertyOf&#32;on&#32;the&#32;ontology&#32;terms|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-215)|Identifier|`class-subpropertyof`|
|[Section top](#pass-outcome-number-215)|Title|No&#32;class&#32;subproperty|
|[Section top](#pass-outcome-number-215)|Description|No&#32;ontology&#32;class&#32;is&#32;a&#32;subproperty|

***
### Pass Outcome number 216

[Jump to summary definition](#summary-Pass-216)	|	[Previous Pass outcome](#pass-outcome-number-215)	|	[Next Pass outcome](#pass-outcome-number-217)

:white_check_mark:Pass outcome
#### Subject detail
|Name|modelet-logistics-create-organization|
|----|----|
|Title|Standalone&#32;modelet&#32;domains/logistics/create-organization/onto.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Modelet logistics/create-organization](https://github.com/HyperAgents/hmas/blob/HEAD/domains/logistics/create-organization/onto.ttl)|

#### Criterion detail
|Identifier|[proper-extension-predicate](https://ns.inria.fr/olivaw#proper-extension-predicate)|
|----|----|
|Title|Predicate&#32;extension&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;test&#32;the&#32;proper&#32;use&#32;of&#32;predicates&#32;rdfs:subClassOf&#32;and&#32;rdfs:subPropertyOf&#32;on&#32;the&#32;ontology&#32;terms|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-216)|Identifier|`property-subclassof`|
|[Section top](#pass-outcome-number-216)|Title|No&#32;property&#32;subclass|
|[Section top](#pass-outcome-number-216)|Description|No&#32;ontology&#32;property&#32;is&#32;a&#32;subclass|

***
### Pass Outcome number 217

[Jump to summary definition](#summary-Pass-217)	|	[Previous Pass outcome](#pass-outcome-number-216)	|	[Next Pass outcome](#pass-outcome-number-218)

:white_check_mark:Pass outcome
#### Subject detail
|Name|modelet-logistics-create-organization|
|----|----|
|Title|Standalone&#32;modelet&#32;domains/logistics/create-organization/onto.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Modelet logistics/create-organization](https://github.com/HyperAgents/hmas/blob/HEAD/domains/logistics/create-organization/onto.ttl)|

#### Criterion detail
|Identifier|[proper-extension-predicate](https://ns.inria.fr/olivaw#proper-extension-predicate)|
|----|----|
|Title|Predicate&#32;extension&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;test&#32;the&#32;proper&#32;use&#32;of&#32;predicates&#32;rdfs:subClassOf&#32;and&#32;rdfs:subPropertyOf&#32;on&#32;the&#32;ontology&#32;terms|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-217)|Identifier|`subclassof-property`|
|[Section top](#pass-outcome-number-217)|Title|No&#32;subclass&#32;of&#32;property|
|[Section top](#pass-outcome-number-217)|Description|No&#32;ontology&#32;term&#32;is&#32;a&#32;subclass&#32;of&#32;a&#32;property|

***
### Pass Outcome number 218

[Jump to summary definition](#summary-Pass-218)	|	[Previous Pass outcome](#pass-outcome-number-217)	|	[Next Pass outcome](#pass-outcome-number-219)

:white_check_mark:Pass outcome
#### Subject detail
|Name|modelet-logistics-create-organization|
|----|----|
|Title|Standalone&#32;modelet&#32;domains/logistics/create-organization/onto.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Modelet logistics/create-organization](https://github.com/HyperAgents/hmas/blob/HEAD/domains/logistics/create-organization/onto.ttl)|

#### Criterion detail
|Identifier|[proper-extension-predicate](https://ns.inria.fr/olivaw#proper-extension-predicate)|
|----|----|
|Title|Predicate&#32;extension&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;test&#32;the&#32;proper&#32;use&#32;of&#32;predicates&#32;rdfs:subClassOf&#32;and&#32;rdfs:subPropertyOf&#32;on&#32;the&#32;ontology&#32;terms|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-218)|Identifier|`subpropertyof-class`|
|[Section top](#pass-outcome-number-218)|Title|No&#32;subproperty&#32;of&#32;class|
|[Section top](#pass-outcome-number-218)|Description|No&#32;ontology&#32;term&#32;is&#32;a&#32;subproperty&#32;of&#32;a&#32;class|

***
### Pass Outcome number 219

[Jump to summary definition](#summary-Pass-219)	|	[Previous Pass outcome](#pass-outcome-number-218)	|	[Next Pass outcome](#pass-outcome-number-220)

:white_check_mark:Pass outcome
#### Subject detail
|Name|modelet-logistics-create-organization|
|----|----|
|Title|Standalone&#32;modelet&#32;domains/logistics/create-organization/onto.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Modelet logistics/create-organization](https://github.com/HyperAgents/hmas/blob/HEAD/domains/logistics/create-organization/onto.ttl)|

#### Criterion detail
|Identifier|[term-referencing](https://ns.inria.fr/olivaw#term-referencing)|
|----|----|
|Title|Term&#32;referencing&#32;test|
|Description|A&#32;test&#32;case&#32;from&#32;the&#32;Best&#32;Practices&#32;tests&#32;checking&#32;if&#32;each&#32;term&#32;of&#32;the&#32;test&#32;subject&#32;is&#32;referenced&#32;to&#32;a&#32;module&#32;through&#32;a&#32;rdfs:isDefinedBy&#32;property.|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-219)|Identifier|`no-reference-module`|
|[Section top](#pass-outcome-number-219)|Title|Any&#32;term&#32;is&#32;referenced|
|[Section top](#pass-outcome-number-219)|Description|Each&#32;term&#32;of&#32;the&#32;test&#32;subject&#32;is&#32;linked&#32;to&#32;a&#32;module&#32;by&#32;a&#32;rdfs:isDefinedBy&#32;property|

***
### Pass Outcome number 220

[Jump to summary definition](#summary-Pass-220)	|	[Previous Pass outcome](#pass-outcome-number-219)	|	[Next Pass outcome](#pass-outcome-number-221)

:white_check_mark:Pass outcome
#### Subject detail
|Name|modelet-logistics-create-organization|
|----|----|
|Title|Standalone&#32;modelet&#32;domains/logistics/create-organization/onto.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Modelet logistics/create-organization](https://github.com/HyperAgents/hmas/blob/HEAD/domains/logistics/create-organization/onto.ttl)|

#### Criterion detail
|Identifier|[terms-differenciation](https://ns.inria.fr/olivaw#terms-differenciation)|
|----|----|
|Title|Terms&#32;differenciation&#32;test|
|Description|A&#32;test&#32;case&#32;from&#32;the&#32;Best&#32;Practices&#32;tests&#32;checking&#32;if&#32;all&#32;the&#32;terms&#32;are&#32;different&#32;enough&#32;from&#32;each&#32;other&#32;according&#32;to&#32;the&#32;Levenshtein&#32;distance&#32;metric.|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-220)|Identifier|`too-close-terms`|
|[Section top](#pass-outcome-number-220)|Title|Terms&#32;differenciated&#32;enough|
|[Section top](#pass-outcome-number-220)|Description|All&#32;the&#32;terms&#32;have&#32;have&#32;a&#32;satisfying&#32;Levenshtein&#32;distance&#32;from&#32;each&#32;other&#32;term.|

***
### Pass Outcome number 221

[Jump to summary definition](#summary-Pass-221)	|	[Previous Pass outcome](#pass-outcome-number-220)	|	[Next Pass outcome](#pass-outcome-number-222)

:white_check_mark:Pass outcome
#### Subject detail
|Name|modelet-logistics-coordinate-activities|
|----|----|
|Title|Standalone&#32;modelet&#32;domains/logistics/coordinate-activities/onto.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Modelet logistics/coordinate-activities](https://github.com/HyperAgents/hmas/blob/HEAD/domains/logistics/coordinate-activities/onto.ttl)|

#### Criterion detail
|Identifier|[domain-and-range-referencing](https://ns.inria.fr/olivaw#domain-and-range-referencing)|
|----|----|
|Title|Domain&#32;and&#32;range&#32;referencing&#32;test|
|Description|A&#32;test&#32;case&#32;from&#32;the&#32;Best&#32;Practices&#32;tests&#32;checking&#32;if&#32;all&#32;the&#32;ranges&#32;and&#32;domains&#32;from&#32;the&#32;test&#32;subject&#32;point&#32;to&#32;terms&#32;that&#32;are&#32;defined&#32;in&#32;the&#32;vocabulary.|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-221)|Identifier|`domain-out-of-vocabulary`|
|[Section top](#pass-outcome-number-221)|Title|Domains&#32;properly&#32;defined|
|[Section top](#pass-outcome-number-221)|Description|Each&#32;rdfs:domain&#32;is&#32;defined&#32;within&#32;the&#32;fragment|

***
### Pass Outcome number 222

[Jump to summary definition](#summary-Pass-222)	|	[Previous Pass outcome](#pass-outcome-number-221)	|	[Next Pass outcome](#pass-outcome-number-223)

:white_check_mark:Pass outcome
#### Subject detail
|Name|modelet-logistics-coordinate-activities|
|----|----|
|Title|Standalone&#32;modelet&#32;domains/logistics/coordinate-activities/onto.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Modelet logistics/coordinate-activities](https://github.com/HyperAgents/hmas/blob/HEAD/domains/logistics/coordinate-activities/onto.ttl)|

#### Criterion detail
|Identifier|[domain-and-range-referencing](https://ns.inria.fr/olivaw#domain-and-range-referencing)|
|----|----|
|Title|Domain&#32;and&#32;range&#32;referencing&#32;test|
|Description|A&#32;test&#32;case&#32;from&#32;the&#32;Best&#32;Practices&#32;tests&#32;checking&#32;if&#32;all&#32;the&#32;ranges&#32;and&#32;domains&#32;from&#32;the&#32;test&#32;subject&#32;point&#32;to&#32;terms&#32;that&#32;are&#32;defined&#32;in&#32;the&#32;vocabulary.|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-222)|Identifier|`range-out-of-vocabulary`|
|[Section top](#pass-outcome-number-222)|Title|Ranges&#32;properly&#32;defined|
|[Section top](#pass-outcome-number-222)|Description|Each&#32;rdfs:range&#32;is&#32;defined&#32;within&#32;the&#32;fragment|

***
### Pass Outcome number 223

[Jump to summary definition](#summary-Pass-223)	|	[Previous Pass outcome](#pass-outcome-number-222)	|	[Next Pass outcome](#pass-outcome-number-224)

:white_check_mark:Pass outcome
#### Subject detail
|Name|modelet-logistics-coordinate-activities|
|----|----|
|Title|Standalone&#32;modelet&#32;domains/logistics/coordinate-activities/onto.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Modelet logistics/coordinate-activities](https://github.com/HyperAgents/hmas/blob/HEAD/domains/logistics/coordinate-activities/onto.ttl)|

#### Criterion detail
|Identifier|[labeled-terms](https://ns.inria.fr/olivaw#labeled-terms)|
|----|----|
|Title|Term&#32;labeling&#32;test|
|Description|A&#32;test&#32;case&#32;from&#32;the&#32;Best&#32;Practices&#32;tests&#32;checking&#32;if&#32;all&#32;the&#32;terms&#32;of&#32;the&#32;subject&#32;have&#32;a&#32;rdfs:label&#32;property&#32;pointing&#32;to&#32;a&#32;literal&#32;in&#32;English|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-223)|Identifier|`not-labeled-term`|
|[Section top](#pass-outcome-number-223)|Title|All&#32;terms&#32;labeled|
|[Section top](#pass-outcome-number-223)|Description|All&#32;the&#32;terms&#32;defined&#32;in&#32;the&#32;subject&#32;have&#32;a&#32;rdfs:label&#32;in&#32;English|

***
### Pass Outcome number 224

[Jump to summary definition](#summary-Pass-224)	|	[Previous Pass outcome](#pass-outcome-number-223)	|	[Next Pass outcome](#pass-outcome-number-225)

:white_check_mark:Pass outcome
#### Subject detail
|Name|modelet-logistics-coordinate-activities|
|----|----|
|Title|Standalone&#32;modelet&#32;domains/logistics/coordinate-activities/onto.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Modelet logistics/coordinate-activities](https://github.com/HyperAgents/hmas/blob/HEAD/domains/logistics/coordinate-activities/onto.ttl)|

#### Criterion detail
|Identifier|[owl-rl-constraint](https://ns.inria.fr/olivaw#owl-rl-constraint)|
|----|----|
|Title|OWL&#32;RL&#32;Constraint&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;check&#32;wether&#32;the&#32;test&#32;subject&#32;is&#32;syntaxically&#32;correct&#32;or&#32;not.|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-224)|Identifier|`owl-rl-constraint-violation`|
|[Section top](#pass-outcome-number-224)|Title|OWL&#32;RL&#32;consistent|
|[Section top](#pass-outcome-number-224)|Description|The&#32;provided&#32;graph&#32;is&#32;consistent&#32;for&#32;any&#32;OWL&#32;RL&#32;constraint|

***
### Pass Outcome number 225

[Jump to summary definition](#summary-Pass-225)	|	[Previous Pass outcome](#pass-outcome-number-224)	|	[Next Pass outcome](#pass-outcome-number-226)

:white_check_mark:Pass outcome
#### Subject detail
|Name|modelet-logistics-coordinate-activities|
|----|----|
|Title|Standalone&#32;modelet&#32;domains/logistics/coordinate-activities/onto.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Modelet logistics/coordinate-activities](https://github.com/HyperAgents/hmas/blob/HEAD/domains/logistics/coordinate-activities/onto.ttl)|

#### Criterion detail
|Identifier|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|
|----|----|
|Title|Profile&#32;compatibility&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;check&#32;whether&#32;the&#32;test&#32;subject&#32;is&#32;compatible&#32;with&#32;a&#32;profile&#32;or&#32;not,&#32;and&#32;if&#32;it&#32;is&#32;not,&#32;why.|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-225)|Identifier|`owl-el-profile-error`|
|[Section top](#pass-outcome-number-225)|Title|OWL&#32;EL&#32;Profile&#32;compatible|
|[Section top](#pass-outcome-number-225)|Description|The&#32;subject&#32;is&#32;included&#32;in&#32;the&#32;OWL&#32;EL&#32;sublanguage|

***
### Pass Outcome number 226

[Jump to summary definition](#summary-Pass-226)	|	[Previous Pass outcome](#pass-outcome-number-225)	|	[Next Pass outcome](#pass-outcome-number-227)

:white_check_mark:Pass outcome
#### Subject detail
|Name|modelet-logistics-coordinate-activities|
|----|----|
|Title|Standalone&#32;modelet&#32;domains/logistics/coordinate-activities/onto.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Modelet logistics/coordinate-activities](https://github.com/HyperAgents/hmas/blob/HEAD/domains/logistics/coordinate-activities/onto.ttl)|

#### Criterion detail
|Identifier|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|
|----|----|
|Title|Profile&#32;compatibility&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;check&#32;whether&#32;the&#32;test&#32;subject&#32;is&#32;compatible&#32;with&#32;a&#32;profile&#32;or&#32;not,&#32;and&#32;if&#32;it&#32;is&#32;not,&#32;why.|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-226)|Identifier|`owl-ql-profile-error`|
|[Section top](#pass-outcome-number-226)|Title|OWL&#32;QL&#32;Profile&#32;compatible|
|[Section top](#pass-outcome-number-226)|Description|The&#32;subject&#32;is&#32;included&#32;in&#32;the&#32;OWL&#32;QL&#32;sublanguage|

***
### Pass Outcome number 227

[Jump to summary definition](#summary-Pass-227)	|	[Previous Pass outcome](#pass-outcome-number-226)	|	[Next Pass outcome](#pass-outcome-number-228)

:white_check_mark:Pass outcome
#### Subject detail
|Name|modelet-logistics-coordinate-activities|
|----|----|
|Title|Standalone&#32;modelet&#32;domains/logistics/coordinate-activities/onto.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Modelet logistics/coordinate-activities](https://github.com/HyperAgents/hmas/blob/HEAD/domains/logistics/coordinate-activities/onto.ttl)|

#### Criterion detail
|Identifier|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|
|----|----|
|Title|Profile&#32;compatibility&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;check&#32;whether&#32;the&#32;test&#32;subject&#32;is&#32;compatible&#32;with&#32;a&#32;profile&#32;or&#32;not,&#32;and&#32;if&#32;it&#32;is&#32;not,&#32;why.|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-227)|Identifier|`owl-rl-profile-error`|
|[Section top](#pass-outcome-number-227)|Title|OWL&#32;RL&#32;Profile&#32;compatible|
|[Section top](#pass-outcome-number-227)|Description|The&#32;subject&#32;is&#32;included&#32;in&#32;the&#32;OWL&#32;RL&#32;sublanguage|

***
### Pass Outcome number 228

[Jump to summary definition](#summary-Pass-228)	|	[Previous Pass outcome](#pass-outcome-number-227)	|	[Next Pass outcome](#pass-outcome-number-229)

:white_check_mark:Pass outcome
#### Subject detail
|Name|modelet-logistics-coordinate-activities|
|----|----|
|Title|Standalone&#32;modelet&#32;domains/logistics/coordinate-activities/onto.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Modelet logistics/coordinate-activities](https://github.com/HyperAgents/hmas/blob/HEAD/domains/logistics/coordinate-activities/onto.ttl)|

#### Criterion detail
|Identifier|[proper-extension-predicate](https://ns.inria.fr/olivaw#proper-extension-predicate)|
|----|----|
|Title|Predicate&#32;extension&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;test&#32;the&#32;proper&#32;use&#32;of&#32;predicates&#32;rdfs:subClassOf&#32;and&#32;rdfs:subPropertyOf&#32;on&#32;the&#32;ontology&#32;terms|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-228)|Identifier|`class-subpropertyof`|
|[Section top](#pass-outcome-number-228)|Title|No&#32;class&#32;subproperty|
|[Section top](#pass-outcome-number-228)|Description|No&#32;ontology&#32;class&#32;is&#32;a&#32;subproperty|

***
### Pass Outcome number 229

[Jump to summary definition](#summary-Pass-229)	|	[Previous Pass outcome](#pass-outcome-number-228)	|	[Next Pass outcome](#pass-outcome-number-230)

:white_check_mark:Pass outcome
#### Subject detail
|Name|modelet-logistics-coordinate-activities|
|----|----|
|Title|Standalone&#32;modelet&#32;domains/logistics/coordinate-activities/onto.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Modelet logistics/coordinate-activities](https://github.com/HyperAgents/hmas/blob/HEAD/domains/logistics/coordinate-activities/onto.ttl)|

#### Criterion detail
|Identifier|[proper-extension-predicate](https://ns.inria.fr/olivaw#proper-extension-predicate)|
|----|----|
|Title|Predicate&#32;extension&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;test&#32;the&#32;proper&#32;use&#32;of&#32;predicates&#32;rdfs:subClassOf&#32;and&#32;rdfs:subPropertyOf&#32;on&#32;the&#32;ontology&#32;terms|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-229)|Identifier|`property-subclassof`|
|[Section top](#pass-outcome-number-229)|Title|No&#32;property&#32;subclass|
|[Section top](#pass-outcome-number-229)|Description|No&#32;ontology&#32;property&#32;is&#32;a&#32;subclass|

***
### Pass Outcome number 230

[Jump to summary definition](#summary-Pass-230)	|	[Previous Pass outcome](#pass-outcome-number-229)	|	[Next Pass outcome](#pass-outcome-number-231)

:white_check_mark:Pass outcome
#### Subject detail
|Name|modelet-logistics-coordinate-activities|
|----|----|
|Title|Standalone&#32;modelet&#32;domains/logistics/coordinate-activities/onto.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Modelet logistics/coordinate-activities](https://github.com/HyperAgents/hmas/blob/HEAD/domains/logistics/coordinate-activities/onto.ttl)|

#### Criterion detail
|Identifier|[proper-extension-predicate](https://ns.inria.fr/olivaw#proper-extension-predicate)|
|----|----|
|Title|Predicate&#32;extension&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;test&#32;the&#32;proper&#32;use&#32;of&#32;predicates&#32;rdfs:subClassOf&#32;and&#32;rdfs:subPropertyOf&#32;on&#32;the&#32;ontology&#32;terms|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-230)|Identifier|`subclassof-property`|
|[Section top](#pass-outcome-number-230)|Title|No&#32;subclass&#32;of&#32;property|
|[Section top](#pass-outcome-number-230)|Description|No&#32;ontology&#32;term&#32;is&#32;a&#32;subclass&#32;of&#32;a&#32;property|

***
### Pass Outcome number 231

[Jump to summary definition](#summary-Pass-231)	|	[Previous Pass outcome](#pass-outcome-number-230)	|	[Next Pass outcome](#pass-outcome-number-232)

:white_check_mark:Pass outcome
#### Subject detail
|Name|modelet-logistics-coordinate-activities|
|----|----|
|Title|Standalone&#32;modelet&#32;domains/logistics/coordinate-activities/onto.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Modelet logistics/coordinate-activities](https://github.com/HyperAgents/hmas/blob/HEAD/domains/logistics/coordinate-activities/onto.ttl)|

#### Criterion detail
|Identifier|[proper-extension-predicate](https://ns.inria.fr/olivaw#proper-extension-predicate)|
|----|----|
|Title|Predicate&#32;extension&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;test&#32;the&#32;proper&#32;use&#32;of&#32;predicates&#32;rdfs:subClassOf&#32;and&#32;rdfs:subPropertyOf&#32;on&#32;the&#32;ontology&#32;terms|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-231)|Identifier|`subpropertyof-class`|
|[Section top](#pass-outcome-number-231)|Title|No&#32;subproperty&#32;of&#32;class|
|[Section top](#pass-outcome-number-231)|Description|No&#32;ontology&#32;term&#32;is&#32;a&#32;subproperty&#32;of&#32;a&#32;class|

***
### Pass Outcome number 232

[Jump to summary definition](#summary-Pass-232)	|	[Previous Pass outcome](#pass-outcome-number-231)	|	[Next Pass outcome](#pass-outcome-number-233)

:white_check_mark:Pass outcome
#### Subject detail
|Name|modelet-logistics-coordinate-activities|
|----|----|
|Title|Standalone&#32;modelet&#32;domains/logistics/coordinate-activities/onto.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Modelet logistics/coordinate-activities](https://github.com/HyperAgents/hmas/blob/HEAD/domains/logistics/coordinate-activities/onto.ttl)|

#### Criterion detail
|Identifier|[term-referencing](https://ns.inria.fr/olivaw#term-referencing)|
|----|----|
|Title|Term&#32;referencing&#32;test|
|Description|A&#32;test&#32;case&#32;from&#32;the&#32;Best&#32;Practices&#32;tests&#32;checking&#32;if&#32;each&#32;term&#32;of&#32;the&#32;test&#32;subject&#32;is&#32;referenced&#32;to&#32;a&#32;module&#32;through&#32;a&#32;rdfs:isDefinedBy&#32;property.|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-232)|Identifier|`no-reference-module`|
|[Section top](#pass-outcome-number-232)|Title|Any&#32;term&#32;is&#32;referenced|
|[Section top](#pass-outcome-number-232)|Description|Each&#32;term&#32;of&#32;the&#32;test&#32;subject&#32;is&#32;linked&#32;to&#32;a&#32;module&#32;by&#32;a&#32;rdfs:isDefinedBy&#32;property|

***
### Pass Outcome number 233

[Jump to summary definition](#summary-Pass-233)	|	[Previous Pass outcome](#pass-outcome-number-232)	|	[Next Pass outcome](#pass-outcome-number-234)

:white_check_mark:Pass outcome
#### Subject detail
|Name|modelet-logistics-coordinate-activities|
|----|----|
|Title|Standalone&#32;modelet&#32;domains/logistics/coordinate-activities/onto.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Modelet logistics/coordinate-activities](https://github.com/HyperAgents/hmas/blob/HEAD/domains/logistics/coordinate-activities/onto.ttl)|

#### Criterion detail
|Identifier|[terms-differenciation](https://ns.inria.fr/olivaw#terms-differenciation)|
|----|----|
|Title|Terms&#32;differenciation&#32;test|
|Description|A&#32;test&#32;case&#32;from&#32;the&#32;Best&#32;Practices&#32;tests&#32;checking&#32;if&#32;all&#32;the&#32;terms&#32;are&#32;different&#32;enough&#32;from&#32;each&#32;other&#32;according&#32;to&#32;the&#32;Levenshtein&#32;distance&#32;metric.|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-233)|Identifier|`too-close-terms`|
|[Section top](#pass-outcome-number-233)|Title|Terms&#32;differenciated&#32;enough|
|[Section top](#pass-outcome-number-233)|Description|All&#32;the&#32;terms&#32;have&#32;have&#32;a&#32;satisfying&#32;Levenshtein&#32;distance&#32;from&#32;each&#32;other&#32;term.|

***
### Pass Outcome number 234

[Jump to summary definition](#summary-Pass-234)	|	[Previous Pass outcome](#pass-outcome-number-233)	|	[Next Pass outcome](#pass-outcome-number-235)

:white_check_mark:Pass outcome
#### Subject detail
|Name|modelet-logistics-configure-organization|
|----|----|
|Title|Standalone&#32;modelet&#32;domains/logistics/configure-organization/onto.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Modelet logistics/configure-organization](https://github.com/HyperAgents/hmas/blob/HEAD/domains/logistics/configure-organization/onto.ttl)|

#### Criterion detail
|Identifier|[domain-and-range-referencing](https://ns.inria.fr/olivaw#domain-and-range-referencing)|
|----|----|
|Title|Domain&#32;and&#32;range&#32;referencing&#32;test|
|Description|A&#32;test&#32;case&#32;from&#32;the&#32;Best&#32;Practices&#32;tests&#32;checking&#32;if&#32;all&#32;the&#32;ranges&#32;and&#32;domains&#32;from&#32;the&#32;test&#32;subject&#32;point&#32;to&#32;terms&#32;that&#32;are&#32;defined&#32;in&#32;the&#32;vocabulary.|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-234)|Identifier|`domain-out-of-vocabulary`|
|[Section top](#pass-outcome-number-234)|Title|Domains&#32;properly&#32;defined|
|[Section top](#pass-outcome-number-234)|Description|Each&#32;rdfs:domain&#32;is&#32;defined&#32;within&#32;the&#32;fragment|

***
### Pass Outcome number 235

[Jump to summary definition](#summary-Pass-235)	|	[Previous Pass outcome](#pass-outcome-number-234)	|	[Next Pass outcome](#pass-outcome-number-236)

:white_check_mark:Pass outcome
#### Subject detail
|Name|modelet-logistics-configure-organization|
|----|----|
|Title|Standalone&#32;modelet&#32;domains/logistics/configure-organization/onto.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Modelet logistics/configure-organization](https://github.com/HyperAgents/hmas/blob/HEAD/domains/logistics/configure-organization/onto.ttl)|

#### Criterion detail
|Identifier|[domain-and-range-referencing](https://ns.inria.fr/olivaw#domain-and-range-referencing)|
|----|----|
|Title|Domain&#32;and&#32;range&#32;referencing&#32;test|
|Description|A&#32;test&#32;case&#32;from&#32;the&#32;Best&#32;Practices&#32;tests&#32;checking&#32;if&#32;all&#32;the&#32;ranges&#32;and&#32;domains&#32;from&#32;the&#32;test&#32;subject&#32;point&#32;to&#32;terms&#32;that&#32;are&#32;defined&#32;in&#32;the&#32;vocabulary.|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-235)|Identifier|`range-out-of-vocabulary`|
|[Section top](#pass-outcome-number-235)|Title|Ranges&#32;properly&#32;defined|
|[Section top](#pass-outcome-number-235)|Description|Each&#32;rdfs:range&#32;is&#32;defined&#32;within&#32;the&#32;fragment|

***
### Pass Outcome number 236

[Jump to summary definition](#summary-Pass-236)	|	[Previous Pass outcome](#pass-outcome-number-235)	|	[Next Pass outcome](#pass-outcome-number-237)

:white_check_mark:Pass outcome
#### Subject detail
|Name|modelet-logistics-configure-organization|
|----|----|
|Title|Standalone&#32;modelet&#32;domains/logistics/configure-organization/onto.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Modelet logistics/configure-organization](https://github.com/HyperAgents/hmas/blob/HEAD/domains/logistics/configure-organization/onto.ttl)|

#### Criterion detail
|Identifier|[labeled-terms](https://ns.inria.fr/olivaw#labeled-terms)|
|----|----|
|Title|Term&#32;labeling&#32;test|
|Description|A&#32;test&#32;case&#32;from&#32;the&#32;Best&#32;Practices&#32;tests&#32;checking&#32;if&#32;all&#32;the&#32;terms&#32;of&#32;the&#32;subject&#32;have&#32;a&#32;rdfs:label&#32;property&#32;pointing&#32;to&#32;a&#32;literal&#32;in&#32;English|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-236)|Identifier|`not-labeled-term`|
|[Section top](#pass-outcome-number-236)|Title|All&#32;terms&#32;labeled|
|[Section top](#pass-outcome-number-236)|Description|All&#32;the&#32;terms&#32;defined&#32;in&#32;the&#32;subject&#32;have&#32;a&#32;rdfs:label&#32;in&#32;English|

***
### Pass Outcome number 237

[Jump to summary definition](#summary-Pass-237)	|	[Previous Pass outcome](#pass-outcome-number-236)	|	[Next Pass outcome](#pass-outcome-number-238)

:white_check_mark:Pass outcome
#### Subject detail
|Name|modelet-logistics-configure-organization|
|----|----|
|Title|Standalone&#32;modelet&#32;domains/logistics/configure-organization/onto.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Modelet logistics/configure-organization](https://github.com/HyperAgents/hmas/blob/HEAD/domains/logistics/configure-organization/onto.ttl)|

#### Criterion detail
|Identifier|[owl-rl-constraint](https://ns.inria.fr/olivaw#owl-rl-constraint)|
|----|----|
|Title|OWL&#32;RL&#32;Constraint&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;check&#32;wether&#32;the&#32;test&#32;subject&#32;is&#32;syntaxically&#32;correct&#32;or&#32;not.|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-237)|Identifier|`owl-rl-constraint-violation`|
|[Section top](#pass-outcome-number-237)|Title|OWL&#32;RL&#32;consistent|
|[Section top](#pass-outcome-number-237)|Description|The&#32;provided&#32;graph&#32;is&#32;consistent&#32;for&#32;any&#32;OWL&#32;RL&#32;constraint|

***
### Pass Outcome number 238

[Jump to summary definition](#summary-Pass-238)	|	[Previous Pass outcome](#pass-outcome-number-237)	|	[Next Pass outcome](#pass-outcome-number-239)

:white_check_mark:Pass outcome
#### Subject detail
|Name|modelet-logistics-configure-organization|
|----|----|
|Title|Standalone&#32;modelet&#32;domains/logistics/configure-organization/onto.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Modelet logistics/configure-organization](https://github.com/HyperAgents/hmas/blob/HEAD/domains/logistics/configure-organization/onto.ttl)|

#### Criterion detail
|Identifier|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|
|----|----|
|Title|Profile&#32;compatibility&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;check&#32;whether&#32;the&#32;test&#32;subject&#32;is&#32;compatible&#32;with&#32;a&#32;profile&#32;or&#32;not,&#32;and&#32;if&#32;it&#32;is&#32;not,&#32;why.|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-238)|Identifier|`owl-el-profile-error`|
|[Section top](#pass-outcome-number-238)|Title|OWL&#32;EL&#32;Profile&#32;compatible|
|[Section top](#pass-outcome-number-238)|Description|The&#32;subject&#32;is&#32;included&#32;in&#32;the&#32;OWL&#32;EL&#32;sublanguage|

***
### Pass Outcome number 239

[Jump to summary definition](#summary-Pass-239)	|	[Previous Pass outcome](#pass-outcome-number-238)	|	[Next Pass outcome](#pass-outcome-number-240)

:white_check_mark:Pass outcome
#### Subject detail
|Name|modelet-logistics-configure-organization|
|----|----|
|Title|Standalone&#32;modelet&#32;domains/logistics/configure-organization/onto.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Modelet logistics/configure-organization](https://github.com/HyperAgents/hmas/blob/HEAD/domains/logistics/configure-organization/onto.ttl)|

#### Criterion detail
|Identifier|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|
|----|----|
|Title|Profile&#32;compatibility&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;check&#32;whether&#32;the&#32;test&#32;subject&#32;is&#32;compatible&#32;with&#32;a&#32;profile&#32;or&#32;not,&#32;and&#32;if&#32;it&#32;is&#32;not,&#32;why.|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-239)|Identifier|`owl-ql-profile-error`|
|[Section top](#pass-outcome-number-239)|Title|OWL&#32;QL&#32;Profile&#32;compatible|
|[Section top](#pass-outcome-number-239)|Description|The&#32;subject&#32;is&#32;included&#32;in&#32;the&#32;OWL&#32;QL&#32;sublanguage|

***
### Pass Outcome number 240

[Jump to summary definition](#summary-Pass-240)	|	[Previous Pass outcome](#pass-outcome-number-239)	|	[Next Pass outcome](#pass-outcome-number-241)

:white_check_mark:Pass outcome
#### Subject detail
|Name|modelet-logistics-configure-organization|
|----|----|
|Title|Standalone&#32;modelet&#32;domains/logistics/configure-organization/onto.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Modelet logistics/configure-organization](https://github.com/HyperAgents/hmas/blob/HEAD/domains/logistics/configure-organization/onto.ttl)|

#### Criterion detail
|Identifier|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|
|----|----|
|Title|Profile&#32;compatibility&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;check&#32;whether&#32;the&#32;test&#32;subject&#32;is&#32;compatible&#32;with&#32;a&#32;profile&#32;or&#32;not,&#32;and&#32;if&#32;it&#32;is&#32;not,&#32;why.|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-240)|Identifier|`owl-rl-profile-error`|
|[Section top](#pass-outcome-number-240)|Title|OWL&#32;RL&#32;Profile&#32;compatible|
|[Section top](#pass-outcome-number-240)|Description|The&#32;subject&#32;is&#32;included&#32;in&#32;the&#32;OWL&#32;RL&#32;sublanguage|

***
### Pass Outcome number 241

[Jump to summary definition](#summary-Pass-241)	|	[Previous Pass outcome](#pass-outcome-number-240)	|	[Next Pass outcome](#pass-outcome-number-242)

:white_check_mark:Pass outcome
#### Subject detail
|Name|modelet-logistics-configure-organization|
|----|----|
|Title|Standalone&#32;modelet&#32;domains/logistics/configure-organization/onto.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Modelet logistics/configure-organization](https://github.com/HyperAgents/hmas/blob/HEAD/domains/logistics/configure-organization/onto.ttl)|

#### Criterion detail
|Identifier|[proper-extension-predicate](https://ns.inria.fr/olivaw#proper-extension-predicate)|
|----|----|
|Title|Predicate&#32;extension&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;test&#32;the&#32;proper&#32;use&#32;of&#32;predicates&#32;rdfs:subClassOf&#32;and&#32;rdfs:subPropertyOf&#32;on&#32;the&#32;ontology&#32;terms|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-241)|Identifier|`class-subpropertyof`|
|[Section top](#pass-outcome-number-241)|Title|No&#32;class&#32;subproperty|
|[Section top](#pass-outcome-number-241)|Description|No&#32;ontology&#32;class&#32;is&#32;a&#32;subproperty|

***
### Pass Outcome number 242

[Jump to summary definition](#summary-Pass-242)	|	[Previous Pass outcome](#pass-outcome-number-241)	|	[Next Pass outcome](#pass-outcome-number-243)

:white_check_mark:Pass outcome
#### Subject detail
|Name|modelet-logistics-configure-organization|
|----|----|
|Title|Standalone&#32;modelet&#32;domains/logistics/configure-organization/onto.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Modelet logistics/configure-organization](https://github.com/HyperAgents/hmas/blob/HEAD/domains/logistics/configure-organization/onto.ttl)|

#### Criterion detail
|Identifier|[proper-extension-predicate](https://ns.inria.fr/olivaw#proper-extension-predicate)|
|----|----|
|Title|Predicate&#32;extension&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;test&#32;the&#32;proper&#32;use&#32;of&#32;predicates&#32;rdfs:subClassOf&#32;and&#32;rdfs:subPropertyOf&#32;on&#32;the&#32;ontology&#32;terms|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-242)|Identifier|`property-subclassof`|
|[Section top](#pass-outcome-number-242)|Title|No&#32;property&#32;subclass|
|[Section top](#pass-outcome-number-242)|Description|No&#32;ontology&#32;property&#32;is&#32;a&#32;subclass|

***
### Pass Outcome number 243

[Jump to summary definition](#summary-Pass-243)	|	[Previous Pass outcome](#pass-outcome-number-242)	|	[Next Pass outcome](#pass-outcome-number-244)

:white_check_mark:Pass outcome
#### Subject detail
|Name|modelet-logistics-configure-organization|
|----|----|
|Title|Standalone&#32;modelet&#32;domains/logistics/configure-organization/onto.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Modelet logistics/configure-organization](https://github.com/HyperAgents/hmas/blob/HEAD/domains/logistics/configure-organization/onto.ttl)|

#### Criterion detail
|Identifier|[proper-extension-predicate](https://ns.inria.fr/olivaw#proper-extension-predicate)|
|----|----|
|Title|Predicate&#32;extension&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;test&#32;the&#32;proper&#32;use&#32;of&#32;predicates&#32;rdfs:subClassOf&#32;and&#32;rdfs:subPropertyOf&#32;on&#32;the&#32;ontology&#32;terms|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-243)|Identifier|`subclassof-property`|
|[Section top](#pass-outcome-number-243)|Title|No&#32;subclass&#32;of&#32;property|
|[Section top](#pass-outcome-number-243)|Description|No&#32;ontology&#32;term&#32;is&#32;a&#32;subclass&#32;of&#32;a&#32;property|

***
### Pass Outcome number 244

[Jump to summary definition](#summary-Pass-244)	|	[Previous Pass outcome](#pass-outcome-number-243)	|	[Next Pass outcome](#pass-outcome-number-245)

:white_check_mark:Pass outcome
#### Subject detail
|Name|modelet-logistics-configure-organization|
|----|----|
|Title|Standalone&#32;modelet&#32;domains/logistics/configure-organization/onto.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Modelet logistics/configure-organization](https://github.com/HyperAgents/hmas/blob/HEAD/domains/logistics/configure-organization/onto.ttl)|

#### Criterion detail
|Identifier|[proper-extension-predicate](https://ns.inria.fr/olivaw#proper-extension-predicate)|
|----|----|
|Title|Predicate&#32;extension&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;test&#32;the&#32;proper&#32;use&#32;of&#32;predicates&#32;rdfs:subClassOf&#32;and&#32;rdfs:subPropertyOf&#32;on&#32;the&#32;ontology&#32;terms|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-244)|Identifier|`subpropertyof-class`|
|[Section top](#pass-outcome-number-244)|Title|No&#32;subproperty&#32;of&#32;class|
|[Section top](#pass-outcome-number-244)|Description|No&#32;ontology&#32;term&#32;is&#32;a&#32;subproperty&#32;of&#32;a&#32;class|

***
### Pass Outcome number 245

[Jump to summary definition](#summary-Pass-245)	|	[Previous Pass outcome](#pass-outcome-number-244)	|	[Next Pass outcome](#pass-outcome-number-246)

:white_check_mark:Pass outcome
#### Subject detail
|Name|modelet-logistics-configure-organization|
|----|----|
|Title|Standalone&#32;modelet&#32;domains/logistics/configure-organization/onto.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Modelet logistics/configure-organization](https://github.com/HyperAgents/hmas/blob/HEAD/domains/logistics/configure-organization/onto.ttl)|

#### Criterion detail
|Identifier|[term-referencing](https://ns.inria.fr/olivaw#term-referencing)|
|----|----|
|Title|Term&#32;referencing&#32;test|
|Description|A&#32;test&#32;case&#32;from&#32;the&#32;Best&#32;Practices&#32;tests&#32;checking&#32;if&#32;each&#32;term&#32;of&#32;the&#32;test&#32;subject&#32;is&#32;referenced&#32;to&#32;a&#32;module&#32;through&#32;a&#32;rdfs:isDefinedBy&#32;property.|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-245)|Identifier|`no-reference-module`|
|[Section top](#pass-outcome-number-245)|Title|Any&#32;term&#32;is&#32;referenced|
|[Section top](#pass-outcome-number-245)|Description|Each&#32;term&#32;of&#32;the&#32;test&#32;subject&#32;is&#32;linked&#32;to&#32;a&#32;module&#32;by&#32;a&#32;rdfs:isDefinedBy&#32;property|

***
### Pass Outcome number 246

[Jump to summary definition](#summary-Pass-246)	|	[Previous Pass outcome](#pass-outcome-number-245)	|	[Next Pass outcome](#pass-outcome-number-247)

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
|[Section top](#pass-outcome-number-246)|Identifier|`domain-out-of-vocabulary`|
|[Section top](#pass-outcome-number-246)|Title|Domains&#32;properly&#32;defined|
|[Section top](#pass-outcome-number-246)|Description|Each&#32;rdfs:domain&#32;is&#32;defined&#32;within&#32;the&#32;fragment|

***
### Pass Outcome number 247

[Jump to summary definition](#summary-Pass-247)	|	[Previous Pass outcome](#pass-outcome-number-246)	|	[Next Pass outcome](#pass-outcome-number-248)

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
|[Section top](#pass-outcome-number-247)|Identifier|`range-out-of-vocabulary`|
|[Section top](#pass-outcome-number-247)|Title|Ranges&#32;properly&#32;defined|
|[Section top](#pass-outcome-number-247)|Description|Each&#32;rdfs:range&#32;is&#32;defined&#32;within&#32;the&#32;fragment|

***
### Pass Outcome number 248

[Jump to summary definition](#summary-Pass-248)	|	[Previous Pass outcome](#pass-outcome-number-247)	|	[Next Pass outcome](#pass-outcome-number-249)

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
|[Section top](#pass-outcome-number-248)|Identifier|`owl-rl-constraint-violation`|
|[Section top](#pass-outcome-number-248)|Title|OWL&#32;RL&#32;consistent|
|[Section top](#pass-outcome-number-248)|Description|The&#32;provided&#32;graph&#32;is&#32;consistent&#32;for&#32;any&#32;OWL&#32;RL&#32;constraint|

***
### Pass Outcome number 249

[Jump to summary definition](#summary-Pass-249)	|	[Previous Pass outcome](#pass-outcome-number-248)	|	[Next Pass outcome](#pass-outcome-number-250)

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
|[Section top](#pass-outcome-number-249)|Identifier|`owl-rl-profile-error`|
|[Section top](#pass-outcome-number-249)|Title|OWL&#32;RL&#32;Profile&#32;compatible|
|[Section top](#pass-outcome-number-249)|Description|The&#32;subject&#32;is&#32;included&#32;in&#32;the&#32;OWL&#32;RL&#32;sublanguage|

***
### Pass Outcome number 250

[Jump to summary definition](#summary-Pass-250)	|	[Previous Pass outcome](#pass-outcome-number-249)	|	[Next Pass outcome](#pass-outcome-number-251)

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
|[Section top](#pass-outcome-number-250)|Identifier|`class-subpropertyof`|
|[Section top](#pass-outcome-number-250)|Title|No&#32;class&#32;subproperty|
|[Section top](#pass-outcome-number-250)|Description|No&#32;ontology&#32;class&#32;is&#32;a&#32;subproperty|

***
### Pass Outcome number 251

[Jump to summary definition](#summary-Pass-251)	|	[Previous Pass outcome](#pass-outcome-number-250)	|	[Next Pass outcome](#pass-outcome-number-252)

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
|[Section top](#pass-outcome-number-251)|Identifier|`property-subclassof`|
|[Section top](#pass-outcome-number-251)|Title|No&#32;property&#32;subclass|
|[Section top](#pass-outcome-number-251)|Description|No&#32;ontology&#32;property&#32;is&#32;a&#32;subclass|

***
### Pass Outcome number 252

[Jump to summary definition](#summary-Pass-252)	|	[Previous Pass outcome](#pass-outcome-number-251)	|	[Next Pass outcome](#pass-outcome-number-253)

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
|[Section top](#pass-outcome-number-252)|Identifier|`subclassof-property`|
|[Section top](#pass-outcome-number-252)|Title|No&#32;subclass&#32;of&#32;property|
|[Section top](#pass-outcome-number-252)|Description|No&#32;ontology&#32;term&#32;is&#32;a&#32;subclass&#32;of&#32;a&#32;property|

***
### Pass Outcome number 253

[Jump to summary definition](#summary-Pass-253)	|	[Previous Pass outcome](#pass-outcome-number-252)	|	[Next Pass outcome](#pass-outcome-number-254)

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
|[Section top](#pass-outcome-number-253)|Identifier|`subpropertyof-class`|
|[Section top](#pass-outcome-number-253)|Title|No&#32;subproperty&#32;of&#32;class|
|[Section top](#pass-outcome-number-253)|Description|No&#32;ontology&#32;term&#32;is&#32;a&#32;subproperty&#32;of&#32;a&#32;class|

***
### Pass Outcome number 254

[Jump to summary definition](#summary-Pass-254)	|	[Previous Pass outcome](#pass-outcome-number-253)	|	[Next Pass outcome](#pass-outcome-number-255)

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
|[Section top](#pass-outcome-number-254)|Identifier|`domain-out-of-vocabulary`|
|[Section top](#pass-outcome-number-254)|Title|Domains&#32;properly&#32;defined|
|[Section top](#pass-outcome-number-254)|Description|Each&#32;rdfs:domain&#32;is&#32;defined&#32;within&#32;the&#32;fragment|

***
### Pass Outcome number 255

[Jump to summary definition](#summary-Pass-255)	|	[Previous Pass outcome](#pass-outcome-number-254)	|	[Next Pass outcome](#pass-outcome-number-256)

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
|[Section top](#pass-outcome-number-255)|Identifier|`range-out-of-vocabulary`|
|[Section top](#pass-outcome-number-255)|Title|Ranges&#32;properly&#32;defined|
|[Section top](#pass-outcome-number-255)|Description|Each&#32;rdfs:range&#32;is&#32;defined&#32;within&#32;the&#32;fragment|

***
### Pass Outcome number 256

[Jump to summary definition](#summary-Pass-256)	|	[Previous Pass outcome](#pass-outcome-number-255)	|	[Next Pass outcome](#pass-outcome-number-257)

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
|[Section top](#pass-outcome-number-256)|Identifier|`owl-rl-constraint-violation`|
|[Section top](#pass-outcome-number-256)|Title|OWL&#32;RL&#32;consistent|
|[Section top](#pass-outcome-number-256)|Description|The&#32;provided&#32;graph&#32;is&#32;consistent&#32;for&#32;any&#32;OWL&#32;RL&#32;constraint|

***
### Pass Outcome number 257

[Jump to summary definition](#summary-Pass-257)	|	[Previous Pass outcome](#pass-outcome-number-256)	|	[Next Pass outcome](#pass-outcome-number-258)

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
|[Section top](#pass-outcome-number-257)|Identifier|`owl-rl-profile-error`|
|[Section top](#pass-outcome-number-257)|Title|OWL&#32;RL&#32;Profile&#32;compatible|
|[Section top](#pass-outcome-number-257)|Description|The&#32;subject&#32;is&#32;included&#32;in&#32;the&#32;OWL&#32;RL&#32;sublanguage|

***
### Pass Outcome number 258

[Jump to summary definition](#summary-Pass-258)	|	[Previous Pass outcome](#pass-outcome-number-257)	|	[Next Pass outcome](#pass-outcome-number-259)

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
|[Section top](#pass-outcome-number-258)|Identifier|`class-subpropertyof`|
|[Section top](#pass-outcome-number-258)|Title|No&#32;class&#32;subproperty|
|[Section top](#pass-outcome-number-258)|Description|No&#32;ontology&#32;class&#32;is&#32;a&#32;subproperty|

***
### Pass Outcome number 259

[Jump to summary definition](#summary-Pass-259)	|	[Previous Pass outcome](#pass-outcome-number-258)	|	[Next Pass outcome](#pass-outcome-number-260)

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
|[Section top](#pass-outcome-number-259)|Identifier|`property-subclassof`|
|[Section top](#pass-outcome-number-259)|Title|No&#32;property&#32;subclass|
|[Section top](#pass-outcome-number-259)|Description|No&#32;ontology&#32;property&#32;is&#32;a&#32;subclass|

***
### Pass Outcome number 260

[Jump to summary definition](#summary-Pass-260)	|	[Previous Pass outcome](#pass-outcome-number-259)	|	[Next Pass outcome](#pass-outcome-number-261)

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
|[Section top](#pass-outcome-number-260)|Identifier|`subclassof-property`|
|[Section top](#pass-outcome-number-260)|Title|No&#32;subclass&#32;of&#32;property|
|[Section top](#pass-outcome-number-260)|Description|No&#32;ontology&#32;term&#32;is&#32;a&#32;subclass&#32;of&#32;a&#32;property|

***
### Pass Outcome number 261

[Jump to summary definition](#summary-Pass-261)	|	[Previous Pass outcome](#pass-outcome-number-260)	|	Next Pass outcome

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
|[Section top](#pass-outcome-number-261)|Identifier|`subpropertyof-class`|
|[Section top](#pass-outcome-number-261)|Title|No&#32;subproperty&#32;of&#32;class|
|[Section top](#pass-outcome-number-261)|Description|No&#32;ontology&#32;term&#32;is&#32;a&#32;subproperty&#32;of&#32;a&#32;class|

***

</details>

***
