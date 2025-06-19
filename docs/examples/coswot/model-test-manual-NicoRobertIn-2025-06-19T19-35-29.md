# Test Report Markdown Export

This file is an export of the RDF test report made out of [EARL vocabulary](https://www.w3.org/TR/EARL10/)

This test is powered by Corese, check [Corese website](https://project.inria.fr/corese/) and [Corese repository](https://github.com/Wimmics/corese)

The original test report is available in turtle syntax [here](./model-test-manual-NicoRobertIn-2025-06-19T19-35-29.ttl).

# Test Activity

Here is some information about the testing activity that led to this report

|Title|Model&#32;tests&#32;of&#32;[coswot/coswot-acimov](https://gitlab.com/coswot/coswot-acimov)&#32;on&#32;branch&#32;HEAD|
|--|--|
|Description|[NicoRobertIn](https://gitlab.com/NicoRobertIn)&#32;launch&#32;manual&#32;run&#32;of&#32;model&#32;tests&#32;against&#32;[coswot/coswot-acimov](https://gitlab.com/coswot/coswot-acimov)&#32;on&#32;branch&#32;HEAD|
|Tester|[NicoRobertIn](https://gitlab.com/NicoRobertIn)|
|Ontology|[coswot/coswot-acimov](https://gitlab.com/coswot/coswot-acimov)|
|Ontology version|Local state `670b8b9deb7d477a8da2101ed629b62c496ab55e`|
|Ontology version date|2025-06-19 19:35:10|
|Ontology previous version|[abddb3954038f8ebb62eb063ecc491b961923828](https://gitlab.com/coswot/coswot-acimov/tree/abddb3954038f8ebb62eb063ecc491b961923828)|
|Ontology branch|[HEAD](https://gitlab.com/coswot/coswot-acimov/tree/HEAD)|
|Olivaw suite|[olivaw model test suite](https://github.com/Wimmics/olivaw/blob/v0.0.8/olivaw/test/model/suite.py)|
|Olivaw version|[v0.0.8](https://pypi.org/project/olivaw/0.0.8)|
|Generated turtle|[Turtle report](./model-test-manual-NicoRobertIn-2025-06-19T19-35-29.ttl)|
|Generated Markdown|[Markdown report](./model-test-manual-NicoRobertIn-2025-06-19T19-35-29.md)|

# Statistic summary

Here is a short overview for this test report

382 Outcomes

:boom:1 MajorFail, :exclamation:160 MinorFail, :warning:0 CannotTell, :grey_question:10 NotTested, :white_check_mark:211 Pass

<div  style="border-radius: 12px; height: 25px; overflow: hidden"><img src="../assets/red.png" width="1%" height="25px"/><img src="../assets/orange.png" width="41%" height="25px"/><img src="../assets/grey.png" width="0%" height="25px"/><img src="../assets/white.png" width="2%" height="25px"/><img src="../assets/green.png" width="56%" height="25px"/></div>

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
|[Chapter top](#majorfail-outcomes)|<div id="summary-MajorFail-1">1/1</div>|:boom:MajorFail|`module-coswot-saref`|[syntax](https://ns.inria.fr/olivaw#syntax)|Test subject has syntax errors|[Jump](#majorfail-outcome-number-1)|

***

## MajorFail Outcomes Details

This subchapter gives more details to the :boom:MajorFail outcomes

### MajorFail Outcome number 1

[Jump to summary definition](#summary-MajorFail-1)	|	Previous MajorFail outcome	|	Next MajorFail outcome

:boom:MajorFail outcome
#### Subject detail
|Name|module-coswot-saref|
|----|----|
|Title|Standalone&#32;module&#32;core&#92;coswot-saref.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- https://gitlab.com/coswot/coswot-acimov/blob/HEAD/core/coswot-saref.ttl|

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
|[Section top](#majorfail-outcome-number-1)|Pointer|<pre lang="Turtle"><code>Encountered&#32; &#34;.&#34; &#32;at&#32;line&#32;113,&#32;column&#32;36.</code></pre>|

***

</details>

***


# MinorFail Outcomes

[Jump to statistic summary](#statistic-summary)	|	[Previous section](#majorfail-outcomes)	|	[Next section](#nottested-outcomes)

Here is the chapter related to the MinorFail outcome

:exclamation:160 MinorFail outcomes

<details>
<summary>Fold/Unfold the 160 summary and details</summary>

## MinorFail Outcomes Summary

:exclamation:160 MinorFail outcomes

|*Jump*|*Number*|*Status*|*Subject*|*Criterion*|*Title*|*Link*|
|------|--------|--------|---------|-----------|-------|------|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-1">1/160</div>|:exclamation:MinorFail|`module-systems-ontology`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL EL Profile incompatible|[Jump](#minorfail-outcome-number-1)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-2">2/160</div>|:exclamation:MinorFail|`module-systems-ontology`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL QL Profile incompatible|[Jump](#minorfail-outcome-number-2)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-3">3/160</div>|:exclamation:MinorFail|`module-systems-ontology`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL RL Profile incompatible|[Jump](#minorfail-outcome-number-3)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-4">4/160</div>|:exclamation:MinorFail|`module-systems-ontology`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL RL Profile incompatible|[Jump](#minorfail-outcome-number-4)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-5">5/160</div>|:exclamation:MinorFail|`module-states-ontology-catalog`|[domain-and-range-referencing](https://ns.inria.fr/olivaw#domain-and-range-referencing)|Domain out of vocabulary|[Jump](#minorfail-outcome-number-5)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-6">6/160</div>|:exclamation:MinorFail|`module-states-ontology-catalog`|[domain-and-range-referencing](https://ns.inria.fr/olivaw#domain-and-range-referencing)|Range out of vocabulary|[Jump](#minorfail-outcome-number-6)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-7">7/160</div>|:exclamation:MinorFail|`module-states-ontology-catalog`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL EL Profile incompatible|[Jump](#minorfail-outcome-number-7)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-8">8/160</div>|:exclamation:MinorFail|`module-states-ontology-catalog`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL EL Profile incompatible|[Jump](#minorfail-outcome-number-8)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-9">9/160</div>|:exclamation:MinorFail|`module-states-ontology-catalog`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL QL Profile incompatible|[Jump](#minorfail-outcome-number-9)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-10">10/160</div>|:exclamation:MinorFail|`module-states-ontology-catalog`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL QL Profile incompatible|[Jump](#minorfail-outcome-number-10)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-11">11/160</div>|:exclamation:MinorFail|`module-states-ontology-catalog`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL QL Profile incompatible|[Jump](#minorfail-outcome-number-11)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-12">12/160</div>|:exclamation:MinorFail|`module-states-ontology`|[domain-and-range-referencing](https://ns.inria.fr/olivaw#domain-and-range-referencing)|Domain out of vocabulary|[Jump](#minorfail-outcome-number-12)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-13">13/160</div>|:exclamation:MinorFail|`module-states-ontology`|[domain-and-range-referencing](https://ns.inria.fr/olivaw#domain-and-range-referencing)|Range out of vocabulary|[Jump](#minorfail-outcome-number-13)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-14">14/160</div>|:exclamation:MinorFail|`module-states-ontology`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL EL Profile incompatible|[Jump](#minorfail-outcome-number-14)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-15">15/160</div>|:exclamation:MinorFail|`module-states-ontology`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL EL Profile incompatible|[Jump](#minorfail-outcome-number-15)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-16">16/160</div>|:exclamation:MinorFail|`module-states-ontology`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL EL Profile incompatible|[Jump](#minorfail-outcome-number-16)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-17">17/160</div>|:exclamation:MinorFail|`module-states-ontology`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL EL Profile incompatible|[Jump](#minorfail-outcome-number-17)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-18">18/160</div>|:exclamation:MinorFail|`module-states-ontology`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL QL Profile incompatible|[Jump](#minorfail-outcome-number-18)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-19">19/160</div>|:exclamation:MinorFail|`module-states-ontology`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL QL Profile incompatible|[Jump](#minorfail-outcome-number-19)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-20">20/160</div>|:exclamation:MinorFail|`module-states-ontology`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL QL Profile incompatible|[Jump](#minorfail-outcome-number-20)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-21">21/160</div>|:exclamation:MinorFail|`module-states-ontology`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL QL Profile incompatible|[Jump](#minorfail-outcome-number-21)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-22">22/160</div>|:exclamation:MinorFail|`module-states-ontology`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL QL Profile incompatible|[Jump](#minorfail-outcome-number-22)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-23">23/160</div>|:exclamation:MinorFail|`module-states-ontology`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL QL Profile incompatible|[Jump](#minorfail-outcome-number-23)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-24">24/160</div>|:exclamation:MinorFail|`module-states-ontology`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL RL Profile incompatible|[Jump](#minorfail-outcome-number-24)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-25">25/160</div>|:exclamation:MinorFail|`module-states-ontology`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL RL Profile incompatible|[Jump](#minorfail-outcome-number-25)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-26">26/160</div>|:exclamation:MinorFail|`module-states-ontology`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL RL Profile incompatible|[Jump](#minorfail-outcome-number-26)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-27">27/160</div>|:exclamation:MinorFail|`module-states-ontology`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL RL Profile incompatible|[Jump](#minorfail-outcome-number-27)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-28">28/160</div>|:exclamation:MinorFail|`module-services-operations-ontology`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL EL Profile incompatible|[Jump](#minorfail-outcome-number-28)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-29">29/160</div>|:exclamation:MinorFail|`module-services-operations-ontology`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL EL Profile incompatible|[Jump](#minorfail-outcome-number-29)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-30">30/160</div>|:exclamation:MinorFail|`module-services-operations-ontology`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL EL Profile incompatible|[Jump](#minorfail-outcome-number-30)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-31">31/160</div>|:exclamation:MinorFail|`module-services-operations-ontology`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL EL Profile incompatible|[Jump](#minorfail-outcome-number-31)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-32">32/160</div>|:exclamation:MinorFail|`module-services-operations-ontology`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL QL Profile incompatible|[Jump](#minorfail-outcome-number-32)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-33">33/160</div>|:exclamation:MinorFail|`module-services-operations-ontology`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL QL Profile incompatible|[Jump](#minorfail-outcome-number-33)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-34">34/160</div>|:exclamation:MinorFail|`module-services-operations-ontology`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL QL Profile incompatible|[Jump](#minorfail-outcome-number-34)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-35">35/160</div>|:exclamation:MinorFail|`module-services-operations-ontology`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL QL Profile incompatible|[Jump](#minorfail-outcome-number-35)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-36">36/160</div>|:exclamation:MinorFail|`module-services-operations-ontology`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL QL Profile incompatible|[Jump](#minorfail-outcome-number-36)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-37">37/160</div>|:exclamation:MinorFail|`module-services-operations-ontology`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL RL Profile incompatible|[Jump](#minorfail-outcome-number-37)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-38">38/160</div>|:exclamation:MinorFail|`module-services-operations-ontology`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL RL Profile incompatible|[Jump](#minorfail-outcome-number-38)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-39">39/160</div>|:exclamation:MinorFail|`module-services-operations-ontology`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL RL Profile incompatible|[Jump](#minorfail-outcome-number-39)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-40">40/160</div>|:exclamation:MinorFail|`module-services-operations-ontology`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL RL Profile incompatible|[Jump](#minorfail-outcome-number-40)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-41">41/160</div>|:exclamation:MinorFail|`module-services-operations-ontology`|[term-referencing](https://ns.inria.fr/olivaw#term-referencing)|Term not referenced to a module|[Jump](#minorfail-outcome-number-41)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-42">42/160</div>|:exclamation:MinorFail|`module-samples-ontology`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL EL Profile incompatible|[Jump](#minorfail-outcome-number-42)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-43">43/160</div>|:exclamation:MinorFail|`module-samples-ontology`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL QL Profile incompatible|[Jump](#minorfail-outcome-number-43)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-44">44/160</div>|:exclamation:MinorFail|`module-samples-ontology`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL QL Profile incompatible|[Jump](#minorfail-outcome-number-44)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-45">45/160</div>|:exclamation:MinorFail|`module-property-values-ontology`|[domain-and-range-referencing](https://ns.inria.fr/olivaw#domain-and-range-referencing)|Range out of vocabulary|[Jump](#minorfail-outcome-number-45)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-46">46/160</div>|:exclamation:MinorFail|`module-property-values-ontology`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL EL Profile incompatible|[Jump](#minorfail-outcome-number-46)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-47">47/160</div>|:exclamation:MinorFail|`module-property-values-ontology`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL EL Profile incompatible|[Jump](#minorfail-outcome-number-47)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-48">48/160</div>|:exclamation:MinorFail|`module-property-values-ontology`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL EL Profile incompatible|[Jump](#minorfail-outcome-number-48)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-49">49/160</div>|:exclamation:MinorFail|`module-property-values-ontology`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL QL Profile incompatible|[Jump](#minorfail-outcome-number-49)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-50">50/160</div>|:exclamation:MinorFail|`module-property-values-ontology`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL QL Profile incompatible|[Jump](#minorfail-outcome-number-50)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-51">51/160</div>|:exclamation:MinorFail|`module-property-values-ontology`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL QL Profile incompatible|[Jump](#minorfail-outcome-number-51)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-52">52/160</div>|:exclamation:MinorFail|`module-property-values-ontology`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL QL Profile incompatible|[Jump](#minorfail-outcome-number-52)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-53">53/160</div>|:exclamation:MinorFail|`module-property-values-ontology`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL RL Profile incompatible|[Jump](#minorfail-outcome-number-53)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-54">54/160</div>|:exclamation:MinorFail|`module-property-values-ontology`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL RL Profile incompatible|[Jump](#minorfail-outcome-number-54)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-55">55/160</div>|:exclamation:MinorFail|`module-property-values-ontology`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL RL Profile incompatible|[Jump](#minorfail-outcome-number-55)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-56">56/160</div>|:exclamation:MinorFail|`module-properties-ontology-catalogs`|[domain-and-range-referencing](https://ns.inria.fr/olivaw#domain-and-range-referencing)|Domain out of vocabulary|[Jump](#minorfail-outcome-number-56)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-57">57/160</div>|:exclamation:MinorFail|`module-properties-ontology-catalogs`|[domain-and-range-referencing](https://ns.inria.fr/olivaw#domain-and-range-referencing)|Range out of vocabulary|[Jump](#minorfail-outcome-number-57)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-58">58/160</div>|:exclamation:MinorFail|`module-properties-ontology-catalogs`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL EL Profile incompatible|[Jump](#minorfail-outcome-number-58)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-59">59/160</div>|:exclamation:MinorFail|`module-properties-ontology-catalogs`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL EL Profile incompatible|[Jump](#minorfail-outcome-number-59)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-60">60/160</div>|:exclamation:MinorFail|`module-properties-ontology-catalogs`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL QL Profile incompatible|[Jump](#minorfail-outcome-number-60)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-61">61/160</div>|:exclamation:MinorFail|`module-properties-ontology-catalogs`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL QL Profile incompatible|[Jump](#minorfail-outcome-number-61)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-62">62/160</div>|:exclamation:MinorFail|`module-properties-ontology-catalogs`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL QL Profile incompatible|[Jump](#minorfail-outcome-number-62)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-63">63/160</div>|:exclamation:MinorFail|`module-properties-ontology`|[domain-and-range-referencing](https://ns.inria.fr/olivaw#domain-and-range-referencing)|Domain out of vocabulary|[Jump](#minorfail-outcome-number-63)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-64">64/160</div>|:exclamation:MinorFail|`module-properties-ontology`|[domain-and-range-referencing](https://ns.inria.fr/olivaw#domain-and-range-referencing)|Range out of vocabulary|[Jump](#minorfail-outcome-number-64)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-65">65/160</div>|:exclamation:MinorFail|`module-properties-ontology`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL EL Profile incompatible|[Jump](#minorfail-outcome-number-65)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-66">66/160</div>|:exclamation:MinorFail|`module-properties-ontology`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL EL Profile incompatible|[Jump](#minorfail-outcome-number-66)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-67">67/160</div>|:exclamation:MinorFail|`module-properties-ontology`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL EL Profile incompatible|[Jump](#minorfail-outcome-number-67)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-68">68/160</div>|:exclamation:MinorFail|`module-properties-ontology`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL QL Profile incompatible|[Jump](#minorfail-outcome-number-68)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-69">69/160</div>|:exclamation:MinorFail|`module-properties-ontology`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL QL Profile incompatible|[Jump](#minorfail-outcome-number-69)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-70">70/160</div>|:exclamation:MinorFail|`module-properties-ontology`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL QL Profile incompatible|[Jump](#minorfail-outcome-number-70)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-71">71/160</div>|:exclamation:MinorFail|`module-properties-ontology`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL QL Profile incompatible|[Jump](#minorfail-outcome-number-71)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-72">72/160</div>|:exclamation:MinorFail|`module-properties-ontology`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL RL Profile incompatible|[Jump](#minorfail-outcome-number-72)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-73">73/160</div>|:exclamation:MinorFail|`module-properties-ontology`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL RL Profile incompatible|[Jump](#minorfail-outcome-number-73)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-74">74/160</div>|:exclamation:MinorFail|`module-properties-ontology`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL RL Profile incompatible|[Jump](#minorfail-outcome-number-74)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-75">75/160</div>|:exclamation:MinorFail|`module-procedures-ontology`|[domain-and-range-referencing](https://ns.inria.fr/olivaw#domain-and-range-referencing)|Range out of vocabulary|[Jump](#minorfail-outcome-number-75)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-76">76/160</div>|:exclamation:MinorFail|`module-procedures-ontology`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL EL Profile incompatible|[Jump](#minorfail-outcome-number-76)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-77">77/160</div>|:exclamation:MinorFail|`module-procedures-ontology`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL EL Profile incompatible|[Jump](#minorfail-outcome-number-77)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-78">78/160</div>|:exclamation:MinorFail|`module-procedures-ontology`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL QL Profile incompatible|[Jump](#minorfail-outcome-number-78)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-79">79/160</div>|:exclamation:MinorFail|`module-procedures-ontology`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL QL Profile incompatible|[Jump](#minorfail-outcome-number-79)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-80">80/160</div>|:exclamation:MinorFail|`module-procedures-ontology`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL QL Profile incompatible|[Jump](#minorfail-outcome-number-80)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-81">81/160</div>|:exclamation:MinorFail|`module-procedures-ontology`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL RL Profile incompatible|[Jump](#minorfail-outcome-number-81)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-82">82/160</div>|:exclamation:MinorFail|`module-procedures-ontology`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL RL Profile incompatible|[Jump](#minorfail-outcome-number-82)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-83">83/160</div>|:exclamation:MinorFail|`module-observations-ontology`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL EL Profile incompatible|[Jump](#minorfail-outcome-number-83)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-84">84/160</div>|:exclamation:MinorFail|`module-observations-ontology`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL EL Profile incompatible|[Jump](#minorfail-outcome-number-84)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-85">85/160</div>|:exclamation:MinorFail|`module-observations-ontology`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL EL Profile incompatible|[Jump](#minorfail-outcome-number-85)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-86">86/160</div>|:exclamation:MinorFail|`module-observations-ontology`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL EL Profile incompatible|[Jump](#minorfail-outcome-number-86)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-87">87/160</div>|:exclamation:MinorFail|`module-observations-ontology`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL QL Profile incompatible|[Jump](#minorfail-outcome-number-87)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-88">88/160</div>|:exclamation:MinorFail|`module-observations-ontology`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL QL Profile incompatible|[Jump](#minorfail-outcome-number-88)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-89">89/160</div>|:exclamation:MinorFail|`module-observations-ontology`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL QL Profile incompatible|[Jump](#minorfail-outcome-number-89)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-90">90/160</div>|:exclamation:MinorFail|`module-observations-ontology`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL QL Profile incompatible|[Jump](#minorfail-outcome-number-90)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-91">91/160</div>|:exclamation:MinorFail|`module-observations-ontology`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL RL Profile incompatible|[Jump](#minorfail-outcome-number-91)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-92">92/160</div>|:exclamation:MinorFail|`module-observations-ontology`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL RL Profile incompatible|[Jump](#minorfail-outcome-number-92)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-93">93/160</div>|:exclamation:MinorFail|`module-observations-ontology`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL RL Profile incompatible|[Jump](#minorfail-outcome-number-93)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-94">94/160</div>|:exclamation:MinorFail|`module-observations-ontology`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL RL Profile incompatible|[Jump](#minorfail-outcome-number-94)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-95">95/160</div>|:exclamation:MinorFail|`module-functions-commands-ontology`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL EL Profile incompatible|[Jump](#minorfail-outcome-number-95)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-96">96/160</div>|:exclamation:MinorFail|`module-functions-commands-ontology`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL EL Profile incompatible|[Jump](#minorfail-outcome-number-96)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-97">97/160</div>|:exclamation:MinorFail|`module-functions-commands-ontology`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL EL Profile incompatible|[Jump](#minorfail-outcome-number-97)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-98">98/160</div>|:exclamation:MinorFail|`module-functions-commands-ontology`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL QL Profile incompatible|[Jump](#minorfail-outcome-number-98)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-99">99/160</div>|:exclamation:MinorFail|`module-functions-commands-ontology`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL QL Profile incompatible|[Jump](#minorfail-outcome-number-99)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-100">100/160</div>|:exclamation:MinorFail|`module-functions-commands-ontology`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL QL Profile incompatible|[Jump](#minorfail-outcome-number-100)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-101">101/160</div>|:exclamation:MinorFail|`module-functions-commands-ontology`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL QL Profile incompatible|[Jump](#minorfail-outcome-number-101)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-102">102/160</div>|:exclamation:MinorFail|`module-functions-commands-ontology`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL RL Profile incompatible|[Jump](#minorfail-outcome-number-102)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-103">103/160</div>|:exclamation:MinorFail|`module-functions-commands-ontology`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL RL Profile incompatible|[Jump](#minorfail-outcome-number-103)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-104">104/160</div>|:exclamation:MinorFail|`module-functions-commands-ontology`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL RL Profile incompatible|[Jump](#minorfail-outcome-number-104)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-105">105/160</div>|:exclamation:MinorFail|`module-functions-commands-ontology`|[term-referencing](https://ns.inria.fr/olivaw#term-referencing)|Term not referenced to a module|[Jump](#minorfail-outcome-number-105)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-106">106/160</div>|:exclamation:MinorFail|`module-features-ontology-catalogs`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL EL Profile incompatible|[Jump](#minorfail-outcome-number-106)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-107">107/160</div>|:exclamation:MinorFail|`module-features-ontology-catalogs`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL EL Profile incompatible|[Jump](#minorfail-outcome-number-107)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-108">108/160</div>|:exclamation:MinorFail|`module-features-ontology-catalogs`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL QL Profile incompatible|[Jump](#minorfail-outcome-number-108)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-109">109/160</div>|:exclamation:MinorFail|`module-features-ontology-catalogs`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL QL Profile incompatible|[Jump](#minorfail-outcome-number-109)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-110">110/160</div>|:exclamation:MinorFail|`module-features-ontology`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL EL Profile incompatible|[Jump](#minorfail-outcome-number-110)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-111">111/160</div>|:exclamation:MinorFail|`module-features-ontology`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL EL Profile incompatible|[Jump](#minorfail-outcome-number-111)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-112">112/160</div>|:exclamation:MinorFail|`module-features-ontology`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL EL Profile incompatible|[Jump](#minorfail-outcome-number-112)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-113">113/160</div>|:exclamation:MinorFail|`module-features-ontology`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL QL Profile incompatible|[Jump](#minorfail-outcome-number-113)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-114">114/160</div>|:exclamation:MinorFail|`module-features-ontology`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL QL Profile incompatible|[Jump](#minorfail-outcome-number-114)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-115">115/160</div>|:exclamation:MinorFail|`module-features-ontology`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL QL Profile incompatible|[Jump](#minorfail-outcome-number-115)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-116">116/160</div>|:exclamation:MinorFail|`module-features-ontology`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL QL Profile incompatible|[Jump](#minorfail-outcome-number-116)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-117">117/160</div>|:exclamation:MinorFail|`module-features-ontology`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL RL Profile incompatible|[Jump](#minorfail-outcome-number-117)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-118">118/160</div>|:exclamation:MinorFail|`module-features-ontology`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL RL Profile incompatible|[Jump](#minorfail-outcome-number-118)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-119">119/160</div>|:exclamation:MinorFail|`module-features-ontology`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL RL Profile incompatible|[Jump](#minorfail-outcome-number-119)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-120">120/160</div>|:exclamation:MinorFail|`module-devices-ontology`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL EL Profile incompatible|[Jump](#minorfail-outcome-number-120)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-121">121/160</div>|:exclamation:MinorFail|`module-devices-ontology`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL EL Profile incompatible|[Jump](#minorfail-outcome-number-121)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-122">122/160</div>|:exclamation:MinorFail|`module-devices-ontology`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL EL Profile incompatible|[Jump](#minorfail-outcome-number-122)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-123">123/160</div>|:exclamation:MinorFail|`module-devices-ontology`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL EL Profile incompatible|[Jump](#minorfail-outcome-number-123)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-124">124/160</div>|:exclamation:MinorFail|`module-devices-ontology`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL QL Profile incompatible|[Jump](#minorfail-outcome-number-124)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-125">125/160</div>|:exclamation:MinorFail|`module-devices-ontology`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL QL Profile incompatible|[Jump](#minorfail-outcome-number-125)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-126">126/160</div>|:exclamation:MinorFail|`module-devices-ontology`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL QL Profile incompatible|[Jump](#minorfail-outcome-number-126)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-127">127/160</div>|:exclamation:MinorFail|`module-devices-ontology`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL QL Profile incompatible|[Jump](#minorfail-outcome-number-127)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-128">128/160</div>|:exclamation:MinorFail|`module-devices-ontology`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL RL Profile incompatible|[Jump](#minorfail-outcome-number-128)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-129">129/160</div>|:exclamation:MinorFail|`module-devices-ontology`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL RL Profile incompatible|[Jump](#minorfail-outcome-number-129)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-130">130/160</div>|:exclamation:MinorFail|`module-devices-ontology`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL RL Profile incompatible|[Jump](#minorfail-outcome-number-130)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-131">131/160</div>|:exclamation:MinorFail|`module-devices-ontology`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL RL Profile incompatible|[Jump](#minorfail-outcome-number-131)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-132">132/160</div>|:exclamation:MinorFail|`module-coswot-sosa`|[term-referencing](https://ns.inria.fr/olivaw#term-referencing)|Term not referenced to a module|[Jump](#minorfail-outcome-number-132)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-133">133/160</div>|:exclamation:MinorFail|`module-communications-ontology`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL EL Profile incompatible|[Jump](#minorfail-outcome-number-133)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-134">134/160</div>|:exclamation:MinorFail|`module-communications-ontology`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL EL Profile incompatible|[Jump](#minorfail-outcome-number-134)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-135">135/160</div>|:exclamation:MinorFail|`module-communications-ontology`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL QL Profile incompatible|[Jump](#minorfail-outcome-number-135)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-136">136/160</div>|:exclamation:MinorFail|`module-communications-ontology`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL QL Profile incompatible|[Jump](#minorfail-outcome-number-136)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-137">137/160</div>|:exclamation:MinorFail|`module-communications-ontology`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL RL Profile incompatible|[Jump](#minorfail-outcome-number-137)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-138">138/160</div>|:exclamation:MinorFail|`module-communications-ontology`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL RL Profile incompatible|[Jump](#minorfail-outcome-number-138)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-139">139/160</div>|:exclamation:MinorFail|`module-aggregations-ontology`|[domain-and-range-referencing](https://ns.inria.fr/olivaw#domain-and-range-referencing)|Range out of vocabulary|[Jump](#minorfail-outcome-number-139)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-140">140/160</div>|:exclamation:MinorFail|`module-aggregations-ontology`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL EL Profile incompatible|[Jump](#minorfail-outcome-number-140)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-141">141/160</div>|:exclamation:MinorFail|`module-aggregations-ontology`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL EL Profile incompatible|[Jump](#minorfail-outcome-number-141)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-142">142/160</div>|:exclamation:MinorFail|`module-aggregations-ontology`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL QL Profile incompatible|[Jump](#minorfail-outcome-number-142)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-143">143/160</div>|:exclamation:MinorFail|`module-aggregations-ontology`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL QL Profile incompatible|[Jump](#minorfail-outcome-number-143)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-144">144/160</div>|:exclamation:MinorFail|`module-aggregations-ontology`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL QL Profile incompatible|[Jump](#minorfail-outcome-number-144)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-145">145/160</div>|:exclamation:MinorFail|`module-aggregations-ontology`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL RL Profile incompatible|[Jump](#minorfail-outcome-number-145)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-146">146/160</div>|:exclamation:MinorFail|`module-aggregations-ontology`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL RL Profile incompatible|[Jump](#minorfail-outcome-number-146)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-147">147/160</div>|:exclamation:MinorFail|`module-aggregations-ontology`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL RL Profile incompatible|[Jump](#minorfail-outcome-number-147)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-148">148/160</div>|:exclamation:MinorFail|`module-actuations-ontology`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL EL Profile incompatible|[Jump](#minorfail-outcome-number-148)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-149">149/160</div>|:exclamation:MinorFail|`module-actuations-ontology`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL EL Profile incompatible|[Jump](#minorfail-outcome-number-149)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-150">150/160</div>|:exclamation:MinorFail|`module-actuations-ontology`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL EL Profile incompatible|[Jump](#minorfail-outcome-number-150)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-151">151/160</div>|:exclamation:MinorFail|`module-actuations-ontology`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL EL Profile incompatible|[Jump](#minorfail-outcome-number-151)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-152">152/160</div>|:exclamation:MinorFail|`module-actuations-ontology`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL QL Profile incompatible|[Jump](#minorfail-outcome-number-152)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-153">153/160</div>|:exclamation:MinorFail|`module-actuations-ontology`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL QL Profile incompatible|[Jump](#minorfail-outcome-number-153)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-154">154/160</div>|:exclamation:MinorFail|`module-actuations-ontology`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL QL Profile incompatible|[Jump](#minorfail-outcome-number-154)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-155">155/160</div>|:exclamation:MinorFail|`module-actuations-ontology`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL QL Profile incompatible|[Jump](#minorfail-outcome-number-155)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-156">156/160</div>|:exclamation:MinorFail|`module-actuations-ontology`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL RL Profile incompatible|[Jump](#minorfail-outcome-number-156)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-157">157/160</div>|:exclamation:MinorFail|`module-actuations-ontology`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL RL Profile incompatible|[Jump](#minorfail-outcome-number-157)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-158">158/160</div>|:exclamation:MinorFail|`module-actuations-ontology`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL RL Profile incompatible|[Jump](#minorfail-outcome-number-158)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-159">159/160</div>|:exclamation:MinorFail|`module-actuations-ontology`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL RL Profile incompatible|[Jump](#minorfail-outcome-number-159)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-160">160/160</div>|:exclamation:MinorFail|`module-actuations-ontology`|[terms-differenciation](https://ns.inria.fr/olivaw#terms-differenciation)|Too close terms|[Jump](#minorfail-outcome-number-160)|

***

## MinorFail Outcomes Details

This subchapter gives more details to the :exclamation:MinorFail outcomes

### MinorFail Outcome number 1

[Jump to summary definition](#summary-MinorFail-1)	|	Previous MinorFail outcome	|	[Next MinorFail outcome](#minorfail-outcome-number-2)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-systems-ontology|
|----|----|
|Title|Standalone&#32;module&#32;core&#92;systems&#92;ontology.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- https://gitlab.com/coswot/coswot-acimov/blob/HEAD/core/systems/ontology.ttl|

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
|[Section top](#minorfail-outcome-number-1)|Pointer|<pre lang="Turtle"><code>coswot:connectedTo&#32;a&#32;owl:ObjectProperty,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:SymmetricProperty&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;connected&#32;to&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;Links&#32;a&#32;system&#32;to&#32;a&#32;system&#32;it&#32;is&#32;connected&#32;to.&#32;Connected&#32;sys...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:domain&#32;coswot:System&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32; &#60;https://w3id.org/coswot/core/systems> &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:range&#32;coswot:System&#32;.</code></pre>|

***
### MinorFail Outcome number 2

[Jump to summary definition](#summary-MinorFail-2)	|	[Previous MinorFail outcome](#minorfail-outcome-number-1)	|	[Next MinorFail outcome](#minorfail-outcome-number-3)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-systems-ontology|
|----|----|
|Title|Standalone&#32;module&#32;core&#92;systems&#92;ontology.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- https://gitlab.com/coswot/coswot-acimov/blob/HEAD/core/systems/ontology.ttl|

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
|[Section top](#minorfail-outcome-number-2)|Pointer|<pre lang="Turtle"><code>coswot:subSystemOf&#32;a&#32;owl:ObjectProperty,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:TransitiveProperty&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;sub&#32;system&#32;of&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;Links&#32;a&#32;system&#32;to&#32;its&#32;super&#32;system.&#32;Properties&#32;of&#32;subsystems...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:domain&#32;coswot:System&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32; &#60;https://w3id.org/coswot/core/systems> &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:range&#32;coswot:System&#32;;  &#10; &#32; &#32; &#32; &#32;owl:inverseOf&#32;coswot:hasSubSystem&#32;.</code></pre>|

***
### MinorFail Outcome number 3

[Jump to summary definition](#summary-MinorFail-3)	|	[Previous MinorFail outcome](#minorfail-outcome-number-2)	|	[Next MinorFail outcome](#minorfail-outcome-number-4)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-systems-ontology|
|----|----|
|Title|Standalone&#32;module&#32;core&#92;systems&#92;ontology.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- https://gitlab.com/coswot/coswot-acimov/blob/HEAD/core/systems/ontology.ttl|

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
|[Section top](#minorfail-outcome-number-3)|Description|Class&#32;Expression&#32;not&#32;supported&#32;with&#32;rdfs:subClassOf|
|[Section top](#minorfail-outcome-number-3)|Pointer|<pre lang="Turtle"><code>coswot:Connection&#32;a&#32;owl:Class&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;Connection&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;The&#32;class&#32;of&#32;connections&#32;between&#32;systems.&#32;This&#32;class&#32;qualifi...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32; &#60;https://w3id.org/coswot/core/systems> &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:subClassOf&#32; &#91;&#32;owl:onProperty&#32;coswot:connectsSystem&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:someValuesFrom&#32;coswot:System&#32;],  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;coswot:Feature&#32;;  &#10; &#32; &#32; &#32; &#32;owl:disjointWith&#32;coswot:System&#32;.</code></pre>|

***
### MinorFail Outcome number 4

[Jump to summary definition](#summary-MinorFail-4)	|	[Previous MinorFail outcome](#minorfail-outcome-number-3)	|	[Next MinorFail outcome](#minorfail-outcome-number-5)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-systems-ontology|
|----|----|
|Title|Standalone&#32;module&#32;core&#92;systems&#92;ontology.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- https://gitlab.com/coswot/coswot-acimov/blob/HEAD/core/systems/ontology.ttl|

#### Criterion detail
|Identifier|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|
|----|----|
|Title|Profile&#32;compatibility&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;check&#32;whether&#32;the&#32;test&#32;subject&#32;is&#32;compatible&#32;with&#32;a&#32;profile&#32;or&#32;not,&#32;and&#32;if&#32;it&#32;is&#32;not,&#32;why.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-4)|Identifier|`owl-rl-profile-error`|
|[Section top](#minorfail-outcome-number-4)|Title|OWL&#32;RL&#32;Profile&#32;incompatible|
|[Section top](#minorfail-outcome-number-4)|Description|Statement&#32;not&#32;supported&#32;in&#32;a&#32;Super&#32;Class&#32;Expression|
|[Section top](#minorfail-outcome-number-4)|Pointer|<pre lang="Turtle"><code>&#91;]&#32;owl:onProperty&#32;coswot:connectsSystem&#32;;  &#10; &#32; &#32;&#32; &#32;owl:someValuesFrom&#32;coswot:System&#32;.</code></pre>|

***
### MinorFail Outcome number 5

[Jump to summary definition](#summary-MinorFail-5)	|	[Previous MinorFail outcome](#minorfail-outcome-number-4)	|	[Next MinorFail outcome](#minorfail-outcome-number-6)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-states-ontology-catalog|
|----|----|
|Title|Standalone&#32;module&#32;core&#92;states&#92;ontology.catalog.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- https://gitlab.com/coswot/coswot-acimov/blob/HEAD/core/states/ontology.catalog.ttl|

#### Criterion detail
|Identifier|[domain-and-range-referencing](https://ns.inria.fr/olivaw#domain-and-range-referencing)|
|----|----|
|Title|Domain&#32;and&#32;range&#32;referencing&#32;test|
|Description|A&#32;test&#32;case&#32;from&#32;the&#32;Best&#32;Practices&#32;tests&#32;checking&#32;if&#32;all&#32;the&#32;ranges&#32;and&#32;domains&#32;from&#32;the&#32;test&#32;subject&#32;point&#32;to&#32;terms&#32;that&#32;are&#32;defined&#32;in&#32;the&#32;vocabulary.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-5)|Identifier|`domain-out-of-vocabulary`|
|[Section top](#minorfail-outcome-number-5)|Title|Domain&#32;out&#32;of&#32;vocabulary|
|[Section top](#minorfail-outcome-number-5)|Description|Some&#32;properties&#32;have&#32;a&#32;domain&#32;out&#32;of&#32;the&#32;ontology|
|[Section top](#minorfail-outcome-number-5)|Pointer|<pre lang="Turtle"><code>:isStateOf&#32;a&#32;owl:ObjectProperty&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;is&#32;state&#32;of&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;Links&#32;a&#32;state&#32;to&#32;the&#32;feature&#32;kind&#32;or&#32;feature&#32;of&#32;interest&#32;it&#32;...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:domain&#32; &#91;&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:allValuesFrom&#32;:StateKind&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:onProperty&#32;skos:broader&#32;],  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#91;&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:allValuesFrom&#32;:StateKind&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:onProperty&#32;skos:narrower&#32;],  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;skos:Concept,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;:StateKind&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32; &#60;https://w3id.org/coswot/core/states> &#32;;  &#10; &#32; &#32; &#32; &#32;owl:inverseOf&#32;:hasState&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-5)|Pointer|http://www.w3.org/2004/02/skos/core#Concept|

***
### MinorFail Outcome number 6

[Jump to summary definition](#summary-MinorFail-6)	|	[Previous MinorFail outcome](#minorfail-outcome-number-5)	|	[Next MinorFail outcome](#minorfail-outcome-number-7)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-states-ontology-catalog|
|----|----|
|Title|Standalone&#32;module&#32;core&#92;states&#92;ontology.catalog.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- https://gitlab.com/coswot/coswot-acimov/blob/HEAD/core/states/ontology.catalog.ttl|

#### Criterion detail
|Identifier|[domain-and-range-referencing](https://ns.inria.fr/olivaw#domain-and-range-referencing)|
|----|----|
|Title|Domain&#32;and&#32;range&#32;referencing&#32;test|
|Description|A&#32;test&#32;case&#32;from&#32;the&#32;Best&#32;Practices&#32;tests&#32;checking&#32;if&#32;all&#32;the&#32;ranges&#32;and&#32;domains&#32;from&#32;the&#32;test&#32;subject&#32;point&#32;to&#32;terms&#32;that&#32;are&#32;defined&#32;in&#32;the&#32;vocabulary.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-6)|Identifier|`range-out-of-vocabulary`|
|[Section top](#minorfail-outcome-number-6)|Title|Range&#32;out&#32;of&#32;vocabulary|
|[Section top](#minorfail-outcome-number-6)|Description|Some&#32;properties&#32;have&#32;a&#32;range&#32;out&#32;of&#32;the&#32;ontology|
|[Section top](#minorfail-outcome-number-6)|Pointer|<pre lang="Turtle"><code>:hasState&#32;a&#32;owl:ObjectProperty&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;has&#32;state&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;Links&#32;a&#32;feature&#32;kind&#32;or&#32;a&#32;feature&#32;of&#32;interest&#32;to&#32;one&#32;of&#32;its&#32;...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32; &#60;https://w3id.org/coswot/core/states> &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:range&#32; &#91;&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:allValuesFrom&#32;:StateKind&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:onProperty&#32;skos:broader&#32;],  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#91;&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:allValuesFrom&#32;:StateKind&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:onProperty&#32;skos:narrower&#32;],  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;skos:Concept,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;:StateKind&#32;;  &#10; &#32; &#32; &#32; &#32;owl:inverseOf&#32;:isStateOf&#32;;  &#10; &#32; &#32; &#32; &#32;owl:propertyChainAxiom&#32;(&#32;skos:broader&#32;:hasState&#32;)&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-6)|Pointer|http://www.w3.org/2004/02/skos/core#Concept|

***
### MinorFail Outcome number 7

[Jump to summary definition](#summary-MinorFail-7)	|	[Previous MinorFail outcome](#minorfail-outcome-number-6)	|	[Next MinorFail outcome](#minorfail-outcome-number-8)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-states-ontology-catalog|
|----|----|
|Title|Standalone&#32;module&#32;core&#92;states&#92;ontology.catalog.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- https://gitlab.com/coswot/coswot-acimov/blob/HEAD/core/states/ontology.catalog.ttl|

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
|[Section top](#minorfail-outcome-number-7)|Description|Class&#32;Expression&#32;not&#32;supported&#32;with&#32;rdfs:subClassOf|
|[Section top](#minorfail-outcome-number-7)|Pointer|<pre lang="Turtle"><code>coswot:StateKind&#32;a&#32;owl:Class&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;State&#32;Kind&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;Identifiable&#32;conditions&#32;that&#32;features&#32;are&#32;or&#32;may&#32;be&#32;in,&#32;and&#32;...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32; &#60;https://w3id.org/coswot/core/states> &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:subClassOf&#32; &#91;&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:allValuesFrom&#32;coswot:StateKind&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:onProperty&#32;skos:broader&#32;],  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#91;&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:allValuesFrom&#32;coswot:StateKind&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:onProperty&#32;skos:narrower&#32;],  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;skos:Concept&#32;;  &#10; &#32; &#32; &#32; &#32;skos:note&#32; &#34;Concepts&#32;from&#32;existing&#32;code&#32;lists,&#32;vocabularies,&#32;and&#32;taxonom...&#34; &#32;.</code></pre>|

***
### MinorFail Outcome number 8

[Jump to summary definition](#summary-MinorFail-8)	|	[Previous MinorFail outcome](#minorfail-outcome-number-7)	|	[Next MinorFail outcome](#minorfail-outcome-number-9)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-states-ontology-catalog|
|----|----|
|Title|Standalone&#32;module&#32;core&#92;states&#92;ontology.catalog.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- https://gitlab.com/coswot/coswot-acimov/blob/HEAD/core/states/ontology.catalog.ttl|

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
|[Section top](#minorfail-outcome-number-8)|Description|Statement&#32;not&#32;supported&#32;in&#32;a&#32;Class&#32;Expression|
|[Section top](#minorfail-outcome-number-8)|Pointer|<pre lang="Turtle"><code>&#91;]&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32;owl:allValuesFrom&#32;coswot:StateKind&#32;;  &#10; &#32; &#32; &#32; &#32;owl:onProperty&#32;skos:broader&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-8)|Pointer|<pre lang="Turtle"><code>&#91;]&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32;owl:allValuesFrom&#32;coswot:StateKind&#32;;  &#10; &#32; &#32; &#32; &#32;owl:onProperty&#32;skos:narrower&#32;.</code></pre>|

***
### MinorFail Outcome number 9

[Jump to summary definition](#summary-MinorFail-9)	|	[Previous MinorFail outcome](#minorfail-outcome-number-8)	|	[Next MinorFail outcome](#minorfail-outcome-number-10)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-states-ontology-catalog|
|----|----|
|Title|Standalone&#32;module&#32;core&#92;states&#92;ontology.catalog.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- https://gitlab.com/coswot/coswot-acimov/blob/HEAD/core/states/ontology.catalog.ttl|

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
|[Section top](#minorfail-outcome-number-9)|Description|Class&#32;Expression&#32;not&#32;supported&#32;with&#32;rdfs:subClassOf|
|[Section top](#minorfail-outcome-number-9)|Pointer|<pre lang="Turtle"><code>coswot:StateKind&#32;a&#32;owl:Class&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;State&#32;Kind&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;Identifiable&#32;conditions&#32;that&#32;features&#32;are&#32;or&#32;may&#32;be&#32;in,&#32;and&#32;...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32; &#60;https://w3id.org/coswot/core/states> &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:subClassOf&#32; &#91;&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:allValuesFrom&#32;coswot:StateKind&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:onProperty&#32;skos:broader&#32;],  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#91;&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:allValuesFrom&#32;coswot:StateKind&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:onProperty&#32;skos:narrower&#32;],  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;skos:Concept&#32;;  &#10; &#32; &#32; &#32; &#32;skos:note&#32; &#34;Concepts&#32;from&#32;existing&#32;code&#32;lists,&#32;vocabularies,&#32;and&#32;taxonom...&#34; &#32;.</code></pre>|

***
### MinorFail Outcome number 10

[Jump to summary definition](#summary-MinorFail-10)	|	[Previous MinorFail outcome](#minorfail-outcome-number-9)	|	[Next MinorFail outcome](#minorfail-outcome-number-11)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-states-ontology-catalog|
|----|----|
|Title|Standalone&#32;module&#32;core&#92;states&#92;ontology.catalog.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- https://gitlab.com/coswot/coswot-acimov/blob/HEAD/core/states/ontology.catalog.ttl|

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
|[Section top](#minorfail-outcome-number-10)|Description|Property&#32;inclusions&#32;involving&#32;property&#32;chains&#32;not&#32;supported|
|[Section top](#minorfail-outcome-number-10)|Pointer|<pre lang="Turtle"><code>coswot:hasState&#32;a&#32;owl:ObjectProperty&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;has&#32;state&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;Links&#32;a&#32;feature&#32;kind&#32;or&#32;a&#32;feature&#32;of&#32;interest&#32;to&#32;one&#32;of&#32;its&#32;...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32; &#60;https://w3id.org/coswot/core/states> &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:range&#32;coswot:StateKind&#32;;  &#10; &#32; &#32; &#32; &#32;owl:inverseOf&#32;coswot:isStateOf&#32;;  &#10; &#32; &#32; &#32; &#32;owl:propertyChainAxiom&#32;(&#32;skos:broader&#32;coswot:hasState&#32;)&#32;.</code></pre>|

***
### MinorFail Outcome number 11

[Jump to summary definition](#summary-MinorFail-11)	|	[Previous MinorFail outcome](#minorfail-outcome-number-10)	|	[Next MinorFail outcome](#minorfail-outcome-number-12)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-states-ontology-catalog|
|----|----|
|Title|Standalone&#32;module&#32;core&#92;states&#92;ontology.catalog.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- https://gitlab.com/coswot/coswot-acimov/blob/HEAD/core/states/ontology.catalog.ttl|

#### Criterion detail
|Identifier|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|
|----|----|
|Title|Profile&#32;compatibility&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;check&#32;whether&#32;the&#32;test&#32;subject&#32;is&#32;compatible&#32;with&#32;a&#32;profile&#32;or&#32;not,&#32;and&#32;if&#32;it&#32;is&#32;not,&#32;why.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-11)|Identifier|`owl-ql-profile-error`|
|[Section top](#minorfail-outcome-number-11)|Title|OWL&#32;QL&#32;Profile&#32;incompatible|
|[Section top](#minorfail-outcome-number-11)|Description|Statement&#32;not&#32;supported&#32;in&#32;a&#32;Super&#32;Class&#32;Expression|
|[Section top](#minorfail-outcome-number-11)|Pointer|<pre lang="Turtle"><code>&#91;]&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32;owl:allValuesFrom&#32;coswot:StateKind&#32;;  &#10; &#32; &#32; &#32; &#32;owl:onProperty&#32;skos:broader&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-11)|Pointer|<pre lang="Turtle"><code>&#91;]&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32;owl:allValuesFrom&#32;coswot:StateKind&#32;;  &#10; &#32; &#32; &#32; &#32;owl:onProperty&#32;skos:narrower&#32;.</code></pre>|

***
### MinorFail Outcome number 12

[Jump to summary definition](#summary-MinorFail-12)	|	[Previous MinorFail outcome](#minorfail-outcome-number-11)	|	[Next MinorFail outcome](#minorfail-outcome-number-13)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-states-ontology|
|----|----|
|Title|Standalone&#32;module&#32;core&#92;states&#92;ontology.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- https://gitlab.com/coswot/coswot-acimov/blob/HEAD/core/states/ontology.ttl|

#### Criterion detail
|Identifier|[domain-and-range-referencing](https://ns.inria.fr/olivaw#domain-and-range-referencing)|
|----|----|
|Title|Domain&#32;and&#32;range&#32;referencing&#32;test|
|Description|A&#32;test&#32;case&#32;from&#32;the&#32;Best&#32;Practices&#32;tests&#32;checking&#32;if&#32;all&#32;the&#32;ranges&#32;and&#32;domains&#32;from&#32;the&#32;test&#32;subject&#32;point&#32;to&#32;terms&#32;that&#32;are&#32;defined&#32;in&#32;the&#32;vocabulary.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-12)|Identifier|`domain-out-of-vocabulary`|
|[Section top](#minorfail-outcome-number-12)|Title|Domain&#32;out&#32;of&#32;vocabulary|
|[Section top](#minorfail-outcome-number-12)|Description|Some&#32;properties&#32;have&#32;a&#32;domain&#32;out&#32;of&#32;the&#32;ontology|
|[Section top](#minorfail-outcome-number-12)|Pointer|<pre lang="Turtle"><code>:isStateOf&#32;a&#32;owl:ObjectProperty&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;is&#32;state&#32;of&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;Links&#32;a&#32;state&#32;to&#32;the&#32;feature&#32;kind&#32;or&#32;feature&#32;of&#32;interest&#32;it&#32;...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:domain&#32; &#91;&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:allValuesFrom&#32;:StateKind&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:onProperty&#32;skos:broader&#32;],  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#91;&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:allValuesFrom&#32;:StateKind&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:onProperty&#32;skos:narrower&#32;],  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#91;&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;rdfs:subClassOf&#32;&lowbar;:nc534dd5c25d74a5fb81ec89e26267ab3b4&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:allValuesFrom&#32;owl:Nothing&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:onProperty&#32;:hasKind&#32;],  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;&lowbar;:nc534dd5c25d74a5fb81ec89e26267ab3b4,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;skos:Concept,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;:State,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;:StateKind&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32; &#60;https://w3id.org/coswot/core/states> &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:range&#32; &#91;&#32;a&#32;owl:Class&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:unionOf&#32;(&#32;:Feature&#32;:StateOfInterest&#32;)&#32;]&#32;;  &#10; &#32; &#32; &#32; &#32;owl:inverseOf&#32;:hasState&#32;.  &#10;&lowbar;:nc534dd5c25d74a5fb81ec89e26267ab3b4&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32;owl:allValuesFrom&#32;:StateKind&#32;;  &#10; &#32; &#32; &#32; &#32;owl:onProperty&#32;:hasKind&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-12)|Pointer|http://www.w3.org/2004/02/skos/core#Concept|

***
### MinorFail Outcome number 13

[Jump to summary definition](#summary-MinorFail-13)	|	[Previous MinorFail outcome](#minorfail-outcome-number-12)	|	[Next MinorFail outcome](#minorfail-outcome-number-14)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-states-ontology|
|----|----|
|Title|Standalone&#32;module&#32;core&#92;states&#92;ontology.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- https://gitlab.com/coswot/coswot-acimov/blob/HEAD/core/states/ontology.ttl|

#### Criterion detail
|Identifier|[domain-and-range-referencing](https://ns.inria.fr/olivaw#domain-and-range-referencing)|
|----|----|
|Title|Domain&#32;and&#32;range&#32;referencing&#32;test|
|Description|A&#32;test&#32;case&#32;from&#32;the&#32;Best&#32;Practices&#32;tests&#32;checking&#32;if&#32;all&#32;the&#32;ranges&#32;and&#32;domains&#32;from&#32;the&#32;test&#32;subject&#32;point&#32;to&#32;terms&#32;that&#32;are&#32;defined&#32;in&#32;the&#32;vocabulary.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-13)|Identifier|`range-out-of-vocabulary`|
|[Section top](#minorfail-outcome-number-13)|Title|Range&#32;out&#32;of&#32;vocabulary|
|[Section top](#minorfail-outcome-number-13)|Description|Some&#32;properties&#32;have&#32;a&#32;range&#32;out&#32;of&#32;the&#32;ontology|
|[Section top](#minorfail-outcome-number-13)|Pointer|<pre lang="Turtle"><code>:hasKind&#32;a&#32;owl:ObjectProperty&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;has&#32;state&#32;kind&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;links&#32;a&#32;state&#32;of&#32;interest&#32;to&#32;its&#32;kind,&#32;a&#32;state&#32;kind&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:domain&#32;&lowbar;:n67dc0a16e2c44347bd97cd6c9c77885bb1,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#91;&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:onProperty&#32;:hasKind&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:someValuesFrom&#32;:StateKind&#32;],  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#91;&#32;a&#32;owl:Class&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:unionOf&#32;(&#32;:Feature&#32;:StateOfInterest&#32;)&#32;],  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#91;&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:onProperty&#32;:isStateOfInterestOf&#32;],  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;:State,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;:StateOfInterest&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32; &#60;https://w3id.org/coswot/core/states> &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:range&#32;&lowbar;:n67dc0a16e2c44347bd97cd6c9c77885bb1,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#91;&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:allValuesFrom&#32;:StateKind&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:onProperty&#32;skos:broader&#32;],  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#91;&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:allValuesFrom&#32;:StateKind&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:onProperty&#32;skos:narrower&#32;],  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#91;&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;rdfs:subClassOf&#32;&lowbar;:n67dc0a16e2c44347bd97cd6c9c77885bb1&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:allValuesFrom&#32;owl:Nothing&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:onProperty&#32;:hasKind&#32;],  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;skos:Concept,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;:State,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;:StateKind&#32;;  &#10; &#32; &#32; &#32; &#32;owl:propertyChainAxiom&#32;(&#32;:hasKind&#32;skos:broader&#32;)&#32;.  &#10;&lowbar;:n67dc0a16e2c44347bd97cd6c9c77885bb1&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32;owl:allValuesFrom&#32;:StateKind&#32;;  &#10; &#32; &#32; &#32; &#32;owl:onProperty&#32;:hasKind&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-13)|Pointer|<pre lang="Turtle"><code>:hasState&#32;a&#32;owl:ObjectProperty&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;has&#32;state&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;Links&#32;a&#32;feature&#32;kind&#32;or&#32;a&#32;feature&#32;of&#32;interest&#32;to&#32;one&#32;of&#32;its&#32;...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:domain&#32; &#91;&#32;a&#32;owl:Class&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:unionOf&#32;(&#32;:Feature&#32;:StateOfInterest&#32;)&#32;]&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32; &#60;https://w3id.org/coswot/core/states> &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:range&#32; &#91;&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:allValuesFrom&#32;:StateKind&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:onProperty&#32;skos:broader&#32;],  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#91;&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:allValuesFrom&#32;:StateKind&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:onProperty&#32;skos:narrower&#32;],  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#91;&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;rdfs:subClassOf&#32;&lowbar;:n6b7e808b329a43a99698f67a90c21898b7&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:allValuesFrom&#32;owl:Nothing&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:onProperty&#32;:hasKind&#32;],  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;&lowbar;:n6b7e808b329a43a99698f67a90c21898b7,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;skos:Concept,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;:State,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;:StateKind&#32;;  &#10; &#32; &#32; &#32; &#32;owl:inverseOf&#32;:isStateOf&#32;;  &#10; &#32; &#32; &#32; &#32;owl:propertyChainAxiom&#32;(&#32;:hasKind&#32;:hasState&#32;),  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;(&#32;:hasStateOfInterest&#32;:hasKind&#32;),  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;(&#32;skos:broader&#32;:hasState&#32;)&#32;.  &#10;&lowbar;:n6b7e808b329a43a99698f67a90c21898b7&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32;owl:allValuesFrom&#32;:StateKind&#32;;  &#10; &#32; &#32; &#32; &#32;owl:onProperty&#32;:hasKind&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-13)|Pointer|http://www.w3.org/2004/02/skos/core#Concept|

***
### MinorFail Outcome number 14

[Jump to summary definition](#summary-MinorFail-14)	|	[Previous MinorFail outcome](#minorfail-outcome-number-13)	|	[Next MinorFail outcome](#minorfail-outcome-number-15)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-states-ontology|
|----|----|
|Title|Standalone&#32;module&#32;core&#92;states&#92;ontology.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- https://gitlab.com/coswot/coswot-acimov/blob/HEAD/core/states/ontology.ttl|

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
|[Section top](#minorfail-outcome-number-14)|Description|Class&#32;Expression&#32;not&#32;supported&#32;as&#32;object&#32;of&#32;rdfs:domain&#32;or&#32;rdfs:range|
|[Section top](#minorfail-outcome-number-14)|Pointer|<pre lang="Turtle"><code>coswot:hasState&#32;a&#32;owl:ObjectProperty&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;has&#32;state&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;Links&#32;a&#32;feature&#32;kind&#32;or&#32;a&#32;feature&#32;of&#32;interest&#32;to&#32;one&#32;of&#32;its&#32;...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:domain&#32; &#91;&#32;a&#32;owl:Class&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:unionOf&#32;(&#32;coswot:Feature&#32;coswot:StateOfInterest&#32;)&#32;]&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32; &#60;https://w3id.org/coswot/core/states> &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:range&#32;coswot:StateKind&#32;;  &#10; &#32; &#32; &#32; &#32;owl:inverseOf&#32;coswot:isStateOf&#32;;  &#10; &#32; &#32; &#32; &#32;owl:propertyChainAxiom&#32;(&#32;skos:broader&#32;coswot:hasState&#32;),  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;(&#32;coswot:hasKind&#32;coswot:hasState&#32;),  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;(&#32;coswot:hasStateOfInterest&#32;coswot:hasKind&#32;)&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-14)|Pointer|<pre lang="Turtle"><code>coswot:isStateOf&#32;a&#32;owl:ObjectProperty&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;is&#32;state&#32;of&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;Links&#32;a&#32;state&#32;to&#32;the&#32;feature&#32;kind&#32;or&#32;feature&#32;of&#32;interest&#32;it&#32;...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:domain&#32;coswot:StateKind&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32; &#60;https://w3id.org/coswot/core/states> &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:range&#32; &#91;&#32;a&#32;owl:Class&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:unionOf&#32;(&#32;coswot:Feature&#32;coswot:StateOfInterest&#32;)&#32;]&#32;;  &#10; &#32; &#32; &#32; &#32;owl:inverseOf&#32;coswot:hasState&#32;.</code></pre>|

***
### MinorFail Outcome number 15

[Jump to summary definition](#summary-MinorFail-15)	|	[Previous MinorFail outcome](#minorfail-outcome-number-14)	|	[Next MinorFail outcome](#minorfail-outcome-number-16)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-states-ontology|
|----|----|
|Title|Standalone&#32;module&#32;core&#92;states&#92;ontology.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- https://gitlab.com/coswot/coswot-acimov/blob/HEAD/core/states/ontology.ttl|

#### Criterion detail
|Identifier|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|
|----|----|
|Title|Profile&#32;compatibility&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;check&#32;whether&#32;the&#32;test&#32;subject&#32;is&#32;compatible&#32;with&#32;a&#32;profile&#32;or&#32;not,&#32;and&#32;if&#32;it&#32;is&#32;not,&#32;why.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-15)|Identifier|`owl-el-profile-error`|
|[Section top](#minorfail-outcome-number-15)|Title|OWL&#32;EL&#32;Profile&#32;incompatible|
|[Section top](#minorfail-outcome-number-15)|Description|Class&#32;Expression&#32;not&#32;supported&#32;with&#32;rdfs:subClassOf|
|[Section top](#minorfail-outcome-number-15)|Pointer|<pre lang="Turtle"><code>coswot:StateKind&#32;a&#32;owl:Class&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;State&#32;Kind&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;Identifiable&#32;conditions&#32;that&#32;features&#32;are&#32;or&#32;may&#32;be&#32;in,&#32;and&#32;...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32; &#60;https://w3id.org/coswot/core/states> &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:subClassOf&#32; &#91;&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:allValuesFrom&#32;coswot:StateKind&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:onProperty&#32;skos:broader&#32;],  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#91;&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:allValuesFrom&#32;coswot:StateKind&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:onProperty&#32;skos:narrower&#32;],  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#91;&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:allValuesFrom&#32;owl:Nothing&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:onProperty&#32;coswot:hasKind&#32;],  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#91;&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:allValuesFrom&#32;coswot:StateKind&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:onProperty&#32;skos:broader&#32;],  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#91;&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:allValuesFrom&#32;coswot:StateKind&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:onProperty&#32;skos:narrower&#32;],  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;skos:Concept,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;coswot:State&#32;;  &#10; &#32; &#32; &#32; &#32;skos:note&#32; &#34;Concepts&#32;from&#32;existing&#32;code&#32;lists,&#32;vocabularies,&#32;and&#32;taxonom...&#34; &#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-15)|Pointer|<pre lang="Turtle"><code>coswot:StateOfInterest&#32;a&#32;owl:Class&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;State&#32;of&#32;Interest&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;Identifiable&#32;conditions&#32;that&#32;features&#32;of&#32;interest&#32;are&#32;or&#32;may...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32; &#60;https://w3id.org/coswot/core/states> &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:subClassOf&#32; &#91;&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:allValuesFrom&#32;coswot:StateKind&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:onProperty&#32;coswot:hasKind&#32;],  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#91;&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:onProperty&#32;coswot:hasKind&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:someValuesFrom&#32;coswot:StateKind&#32;],  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#91;&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:onProperty&#32;coswot:isStateOfInterestOf&#32;],  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;coswot:State&#32;;  &#10; &#32; &#32; &#32; &#32;skos:note&#32; &#34;A&#32;state&#32;of&#32;interest&#32;is&#32;the&#32;state&#32;of&#32;(OP&#32;coswot:isStateOfInte...&#34;,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#34;Per&#32;convention,&#32;the&#32;IRI&#32;of&#32;states&#32;of&#32;interest&#32;should&#32;consist...&#34;,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#34;States&#32;of&#32;interest&#32;need&#32;not&#32;always&#32;be&#32;explicited.&#32;It&#32;depends...&#34; &#32;.</code></pre>|

***
### MinorFail Outcome number 16

[Jump to summary definition](#summary-MinorFail-16)	|	[Previous MinorFail outcome](#minorfail-outcome-number-15)	|	[Next MinorFail outcome](#minorfail-outcome-number-17)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-states-ontology|
|----|----|
|Title|Standalone&#32;module&#32;core&#92;states&#92;ontology.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- https://gitlab.com/coswot/coswot-acimov/blob/HEAD/core/states/ontology.ttl|

#### Criterion detail
|Identifier|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|
|----|----|
|Title|Profile&#32;compatibility&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;check&#32;whether&#32;the&#32;test&#32;subject&#32;is&#32;compatible&#32;with&#32;a&#32;profile&#32;or&#32;not,&#32;and&#32;if&#32;it&#32;is&#32;not,&#32;why.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-16)|Identifier|`owl-el-profile-error`|
|[Section top](#minorfail-outcome-number-16)|Title|OWL&#32;EL&#32;Profile&#32;incompatible|
|[Section top](#minorfail-outcome-number-16)|Description|Statement&#32;not&#32;supported|
|[Section top](#minorfail-outcome-number-16)|Pointer|<pre lang="Turtle"><code>coswot:State&#32;a&#32;owl:Class&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;State&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;Identifiable&#32;conditions&#32;that&#32;features&#32;are&#32;or&#32;may&#32;be&#32;in,&#32;and&#32;...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32; &#60;https://w3id.org/coswot/core/states> &#32;;  &#10; &#32; &#32; &#32; &#32;owl:disjointUnionOf&#32;(&#32;coswot:StateOfInterest&#32;coswot:StateKind&#32;)&#32;.</code></pre>|

***
### MinorFail Outcome number 17

[Jump to summary definition](#summary-MinorFail-17)	|	[Previous MinorFail outcome](#minorfail-outcome-number-16)	|	[Next MinorFail outcome](#minorfail-outcome-number-18)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-states-ontology|
|----|----|
|Title|Standalone&#32;module&#32;core&#92;states&#92;ontology.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- https://gitlab.com/coswot/coswot-acimov/blob/HEAD/core/states/ontology.ttl|

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
|[Section top](#minorfail-outcome-number-17)|Description|Statement&#32;not&#32;supported&#32;in&#32;a&#32;Class&#32;Expression|
|[Section top](#minorfail-outcome-number-17)|Pointer|<pre lang="Turtle"><code>&#91;]&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32;owl:allValuesFrom&#32;coswot:StateKind&#32;;  &#10; &#32; &#32; &#32; &#32;owl:onProperty&#32;skos:broader&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-17)|Pointer|<pre lang="Turtle"><code>&#91;]&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32;owl:allValuesFrom&#32;coswot:StateKind&#32;;  &#10; &#32; &#32; &#32; &#32;owl:onProperty&#32;skos:narrower&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-17)|Pointer|<pre lang="Turtle"><code>&#91;]&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32;owl:allValuesFrom&#32;owl:Nothing&#32;;  &#10; &#32; &#32; &#32; &#32;owl:onProperty&#32;coswot:hasKind&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-17)|Pointer|<pre lang="Turtle"><code>&#91;]&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32;owl:allValuesFrom&#32;coswot:StateKind&#32;;  &#10; &#32; &#32; &#32; &#32;owl:onProperty&#32;coswot:hasKind&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-17)|Pointer|<pre lang="Turtle"><code>&#91;]&#32;a&#32;owl:Class&#32;;  &#10; &#32; &#32;&#32; &#32;owl:unionOf&#32;(&#32;coswot:Feature&#32;coswot:StateOfInterest&#32;)&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-17)|Pointer|<pre lang="Turtle"><code>&#91;]&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32;&#32; &#32;owl:onProperty&#32;coswot:isStateOfInterestOf&#32;.</code></pre>|

***
### MinorFail Outcome number 18

[Jump to summary definition](#summary-MinorFail-18)	|	[Previous MinorFail outcome](#minorfail-outcome-number-17)	|	[Next MinorFail outcome](#minorfail-outcome-number-19)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-states-ontology|
|----|----|
|Title|Standalone&#32;module&#32;core&#92;states&#92;ontology.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- https://gitlab.com/coswot/coswot-acimov/blob/HEAD/core/states/ontology.ttl|

#### Criterion detail
|Identifier|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|
|----|----|
|Title|Profile&#32;compatibility&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;check&#32;whether&#32;the&#32;test&#32;subject&#32;is&#32;compatible&#32;with&#32;a&#32;profile&#32;or&#32;not,&#32;and&#32;if&#32;it&#32;is&#32;not,&#32;why.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-18)|Identifier|`owl-ql-profile-error`|
|[Section top](#minorfail-outcome-number-18)|Title|OWL&#32;QL&#32;Profile&#32;incompatible|
|[Section top](#minorfail-outcome-number-18)|Description|Class&#32;Expression&#32;not&#32;supported&#32;as&#32;object&#32;of&#32;rdfs:domain&#32;or&#32;rdfs:range|
|[Section top](#minorfail-outcome-number-18)|Pointer|<pre lang="Turtle"><code>coswot:isStateOf&#32;a&#32;owl:ObjectProperty&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;is&#32;state&#32;of&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;Links&#32;a&#32;state&#32;to&#32;the&#32;feature&#32;kind&#32;or&#32;feature&#32;of&#32;interest&#32;it&#32;...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:domain&#32;coswot:StateKind&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32; &#60;https://w3id.org/coswot/core/states> &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:range&#32; &#91;&#32;a&#32;owl:Class&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:unionOf&#32;(&#32;coswot:Feature&#32;coswot:StateOfInterest&#32;)&#32;]&#32;;  &#10; &#32; &#32; &#32; &#32;owl:inverseOf&#32;coswot:hasState&#32;.</code></pre>|

***
### MinorFail Outcome number 19

[Jump to summary definition](#summary-MinorFail-19)	|	[Previous MinorFail outcome](#minorfail-outcome-number-18)	|	[Next MinorFail outcome](#minorfail-outcome-number-20)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-states-ontology|
|----|----|
|Title|Standalone&#32;module&#32;core&#92;states&#92;ontology.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- https://gitlab.com/coswot/coswot-acimov/blob/HEAD/core/states/ontology.ttl|

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
|[Section top](#minorfail-outcome-number-19)|Description|Class&#32;Expression&#32;not&#32;supported&#32;as&#32;object&#32;of&#32;rdfs:domain&#32;or&#32;rdfs:range  &#10;Property&#32;inclusions&#32;involving&#32;property&#32;chains&#32;not&#32;supported|
|[Section top](#minorfail-outcome-number-19)|Pointer|<pre lang="Turtle"><code>coswot:hasState&#32;a&#32;owl:ObjectProperty&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;has&#32;state&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;Links&#32;a&#32;feature&#32;kind&#32;or&#32;a&#32;feature&#32;of&#32;interest&#32;to&#32;one&#32;of&#32;its&#32;...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:domain&#32; &#91;&#32;a&#32;owl:Class&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:unionOf&#32;(&#32;coswot:Feature&#32;coswot:StateOfInterest&#32;)&#32;]&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32; &#60;https://w3id.org/coswot/core/states> &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:range&#32;coswot:StateKind&#32;;  &#10; &#32; &#32; &#32; &#32;owl:inverseOf&#32;coswot:isStateOf&#32;;  &#10; &#32; &#32; &#32; &#32;owl:propertyChainAxiom&#32;(&#32;skos:broader&#32;coswot:hasState&#32;),  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;(&#32;coswot:hasKind&#32;coswot:hasState&#32;),  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;(&#32;coswot:hasStateOfInterest&#32;coswot:hasKind&#32;)&#32;.</code></pre>|

***
### MinorFail Outcome number 20

[Jump to summary definition](#summary-MinorFail-20)	|	[Previous MinorFail outcome](#minorfail-outcome-number-19)	|	[Next MinorFail outcome](#minorfail-outcome-number-21)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-states-ontology|
|----|----|
|Title|Standalone&#32;module&#32;core&#92;states&#92;ontology.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- https://gitlab.com/coswot/coswot-acimov/blob/HEAD/core/states/ontology.ttl|

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
|[Section top](#minorfail-outcome-number-20)|Description|Class&#32;Expression&#32;not&#32;supported&#32;with&#32;rdfs:subClassOf|
|[Section top](#minorfail-outcome-number-20)|Pointer|<pre lang="Turtle"><code>coswot:StateKind&#32;a&#32;owl:Class&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;State&#32;Kind&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;Identifiable&#32;conditions&#32;that&#32;features&#32;are&#32;or&#32;may&#32;be&#32;in,&#32;and&#32;...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32; &#60;https://w3id.org/coswot/core/states> &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:subClassOf&#32; &#91;&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:allValuesFrom&#32;coswot:StateKind&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:onProperty&#32;skos:broader&#32;],  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#91;&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:allValuesFrom&#32;coswot:StateKind&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:onProperty&#32;skos:narrower&#32;],  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#91;&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:allValuesFrom&#32;owl:Nothing&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:onProperty&#32;coswot:hasKind&#32;],  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#91;&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:allValuesFrom&#32;coswot:StateKind&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:onProperty&#32;skos:broader&#32;],  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#91;&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:allValuesFrom&#32;coswot:StateKind&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:onProperty&#32;skos:narrower&#32;],  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;skos:Concept,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;coswot:State&#32;;  &#10; &#32; &#32; &#32; &#32;skos:note&#32; &#34;Concepts&#32;from&#32;existing&#32;code&#32;lists,&#32;vocabularies,&#32;and&#32;taxonom...&#34; &#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-20)|Pointer|<pre lang="Turtle"><code>coswot:StateOfInterest&#32;a&#32;owl:Class&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;State&#32;of&#32;Interest&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;Identifiable&#32;conditions&#32;that&#32;features&#32;of&#32;interest&#32;are&#32;or&#32;may...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32; &#60;https://w3id.org/coswot/core/states> &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:subClassOf&#32; &#91;&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:allValuesFrom&#32;coswot:StateKind&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:onProperty&#32;coswot:hasKind&#32;],  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#91;&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:onProperty&#32;coswot:hasKind&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:someValuesFrom&#32;coswot:StateKind&#32;],  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#91;&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:onProperty&#32;coswot:isStateOfInterestOf&#32;],  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;coswot:State&#32;;  &#10; &#32; &#32; &#32; &#32;skos:note&#32; &#34;A&#32;state&#32;of&#32;interest&#32;is&#32;the&#32;state&#32;of&#32;(OP&#32;coswot:isStateOfInte...&#34;,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#34;Per&#32;convention,&#32;the&#32;IRI&#32;of&#32;states&#32;of&#32;interest&#32;should&#32;consist...&#34;,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#34;States&#32;of&#32;interest&#32;need&#32;not&#32;always&#32;be&#32;explicited.&#32;It&#32;depends...&#34; &#32;.</code></pre>|

***
### MinorFail Outcome number 21

[Jump to summary definition](#summary-MinorFail-21)	|	[Previous MinorFail outcome](#minorfail-outcome-number-20)	|	[Next MinorFail outcome](#minorfail-outcome-number-22)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-states-ontology|
|----|----|
|Title|Standalone&#32;module&#32;core&#92;states&#92;ontology.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- https://gitlab.com/coswot/coswot-acimov/blob/HEAD/core/states/ontology.ttl|

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
|[Section top](#minorfail-outcome-number-21)|Description|Property&#32;inclusions&#32;involving&#32;property&#32;chains&#32;not&#32;supported|
|[Section top](#minorfail-outcome-number-21)|Pointer|<pre lang="Turtle"><code>coswot:hasKind&#32;a&#32;owl:ObjectProperty&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;has&#32;state&#32;kind&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;links&#32;a&#32;state&#32;of&#32;interest&#32;to&#32;its&#32;kind,&#32;a&#32;state&#32;kind&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:domain&#32;coswot:StateOfInterest&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32; &#60;https://w3id.org/coswot/core/states> &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:range&#32;coswot:StateKind&#32;;  &#10; &#32; &#32; &#32; &#32;owl:propertyChainAxiom&#32;(&#32;coswot:hasKind&#32;skos:broader&#32;)&#32;.</code></pre>|

***
### MinorFail Outcome number 22

[Jump to summary definition](#summary-MinorFail-22)	|	[Previous MinorFail outcome](#minorfail-outcome-number-21)	|	[Next MinorFail outcome](#minorfail-outcome-number-23)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-states-ontology|
|----|----|
|Title|Standalone&#32;module&#32;core&#92;states&#92;ontology.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- https://gitlab.com/coswot/coswot-acimov/blob/HEAD/core/states/ontology.ttl|

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
|[Section top](#minorfail-outcome-number-22)|Description|Statement&#32;not&#32;supported|
|[Section top](#minorfail-outcome-number-22)|Pointer|<pre lang="Turtle"><code>coswot:State&#32;a&#32;owl:Class&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;State&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;Identifiable&#32;conditions&#32;that&#32;features&#32;are&#32;or&#32;may&#32;be&#32;in,&#32;and&#32;...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32; &#60;https://w3id.org/coswot/core/states> &#32;;  &#10; &#32; &#32; &#32; &#32;owl:disjointUnionOf&#32;(&#32;coswot:StateOfInterest&#32;coswot:StateKind&#32;)&#32;.</code></pre>|

***
### MinorFail Outcome number 23

[Jump to summary definition](#summary-MinorFail-23)	|	[Previous MinorFail outcome](#minorfail-outcome-number-22)	|	[Next MinorFail outcome](#minorfail-outcome-number-24)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-states-ontology|
|----|----|
|Title|Standalone&#32;module&#32;core&#92;states&#92;ontology.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- https://gitlab.com/coswot/coswot-acimov/blob/HEAD/core/states/ontology.ttl|

#### Criterion detail
|Identifier|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|
|----|----|
|Title|Profile&#32;compatibility&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;check&#32;whether&#32;the&#32;test&#32;subject&#32;is&#32;compatible&#32;with&#32;a&#32;profile&#32;or&#32;not,&#32;and&#32;if&#32;it&#32;is&#32;not,&#32;why.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-23)|Identifier|`owl-ql-profile-error`|
|[Section top](#minorfail-outcome-number-23)|Title|OWL&#32;QL&#32;Profile&#32;incompatible|
|[Section top](#minorfail-outcome-number-23)|Description|Statement&#32;not&#32;supported&#32;in&#32;a&#32;Super&#32;Class&#32;Expression|
|[Section top](#minorfail-outcome-number-23)|Pointer|<pre lang="Turtle"><code>&#91;]&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32;owl:allValuesFrom&#32;coswot:StateKind&#32;;  &#10; &#32; &#32; &#32; &#32;owl:onProperty&#32;skos:broader&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-23)|Pointer|<pre lang="Turtle"><code>&#91;]&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32;owl:allValuesFrom&#32;coswot:StateKind&#32;;  &#10; &#32; &#32; &#32; &#32;owl:onProperty&#32;skos:narrower&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-23)|Pointer|<pre lang="Turtle"><code>&#91;]&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32;owl:allValuesFrom&#32;owl:Nothing&#32;;  &#10; &#32; &#32; &#32; &#32;owl:onProperty&#32;coswot:hasKind&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-23)|Pointer|<pre lang="Turtle"><code>&#91;]&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32;owl:allValuesFrom&#32;coswot:StateKind&#32;;  &#10; &#32; &#32; &#32; &#32;owl:onProperty&#32;coswot:hasKind&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-23)|Pointer|<pre lang="Turtle"><code>&#91;]&#32;a&#32;owl:Class&#32;;  &#10; &#32; &#32;&#32; &#32;owl:unionOf&#32;(&#32;coswot:Feature&#32;coswot:StateOfInterest&#32;)&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-23)|Pointer|<pre lang="Turtle"><code>&#91;]&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32;&#32; &#32;owl:onProperty&#32;coswot:isStateOfInterestOf&#32;.</code></pre>|

***
### MinorFail Outcome number 24

[Jump to summary definition](#summary-MinorFail-24)	|	[Previous MinorFail outcome](#minorfail-outcome-number-23)	|	[Next MinorFail outcome](#minorfail-outcome-number-25)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-states-ontology|
|----|----|
|Title|Standalone&#32;module&#32;core&#92;states&#92;ontology.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- https://gitlab.com/coswot/coswot-acimov/blob/HEAD/core/states/ontology.ttl|

#### Criterion detail
|Identifier|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|
|----|----|
|Title|Profile&#32;compatibility&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;check&#32;whether&#32;the&#32;test&#32;subject&#32;is&#32;compatible&#32;with&#32;a&#32;profile&#32;or&#32;not,&#32;and&#32;if&#32;it&#32;is&#32;not,&#32;why.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-24)|Identifier|`owl-rl-profile-error`|
|[Section top](#minorfail-outcome-number-24)|Title|OWL&#32;RL&#32;Profile&#32;incompatible|
|[Section top](#minorfail-outcome-number-24)|Description|Class&#32;Expression&#32;not&#32;supported&#32;as&#32;object&#32;of&#32;rdfs:domain&#32;or&#32;rdfs:range|
|[Section top](#minorfail-outcome-number-24)|Pointer|<pre lang="Turtle"><code>coswot:hasState&#32;a&#32;owl:ObjectProperty&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;has&#32;state&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;Links&#32;a&#32;feature&#32;kind&#32;or&#32;a&#32;feature&#32;of&#32;interest&#32;to&#32;one&#32;of&#32;its&#32;...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:domain&#32; &#91;&#32;a&#32;owl:Class&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:unionOf&#32;(&#32;coswot:Feature&#32;coswot:StateOfInterest&#32;)&#32;]&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32; &#60;https://w3id.org/coswot/core/states> &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:range&#32;coswot:StateKind&#32;;  &#10; &#32; &#32; &#32; &#32;owl:inverseOf&#32;coswot:isStateOf&#32;;  &#10; &#32; &#32; &#32; &#32;owl:propertyChainAxiom&#32;(&#32;skos:broader&#32;coswot:hasState&#32;),  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;(&#32;coswot:hasKind&#32;coswot:hasState&#32;),  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;(&#32;coswot:hasStateOfInterest&#32;coswot:hasKind&#32;)&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-24)|Pointer|<pre lang="Turtle"><code>coswot:isStateOf&#32;a&#32;owl:ObjectProperty&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;is&#32;state&#32;of&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;Links&#32;a&#32;state&#32;to&#32;the&#32;feature&#32;kind&#32;or&#32;feature&#32;of&#32;interest&#32;it&#32;...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:domain&#32;coswot:StateKind&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32; &#60;https://w3id.org/coswot/core/states> &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:range&#32; &#91;&#32;a&#32;owl:Class&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:unionOf&#32;(&#32;coswot:Feature&#32;coswot:StateOfInterest&#32;)&#32;]&#32;;  &#10; &#32; &#32; &#32; &#32;owl:inverseOf&#32;coswot:hasState&#32;.</code></pre>|

***
### MinorFail Outcome number 25

[Jump to summary definition](#summary-MinorFail-25)	|	[Previous MinorFail outcome](#minorfail-outcome-number-24)	|	[Next MinorFail outcome](#minorfail-outcome-number-26)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-states-ontology|
|----|----|
|Title|Standalone&#32;module&#32;core&#92;states&#92;ontology.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- https://gitlab.com/coswot/coswot-acimov/blob/HEAD/core/states/ontology.ttl|

#### Criterion detail
|Identifier|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|
|----|----|
|Title|Profile&#32;compatibility&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;check&#32;whether&#32;the&#32;test&#32;subject&#32;is&#32;compatible&#32;with&#32;a&#32;profile&#32;or&#32;not,&#32;and&#32;if&#32;it&#32;is&#32;not,&#32;why.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-25)|Identifier|`owl-rl-profile-error`|
|[Section top](#minorfail-outcome-number-25)|Title|OWL&#32;RL&#32;Profile&#32;incompatible|
|[Section top](#minorfail-outcome-number-25)|Description|Class&#32;Expression&#32;not&#32;supported&#32;with&#32;rdfs:subClassOf|
|[Section top](#minorfail-outcome-number-25)|Pointer|<pre lang="Turtle"><code>coswot:StateOfInterest&#32;a&#32;owl:Class&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;State&#32;of&#32;Interest&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;Identifiable&#32;conditions&#32;that&#32;features&#32;of&#32;interest&#32;are&#32;or&#32;may...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32; &#60;https://w3id.org/coswot/core/states> &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:subClassOf&#32; &#91;&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:allValuesFrom&#32;coswot:StateKind&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:onProperty&#32;coswot:hasKind&#32;],  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#91;&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:onProperty&#32;coswot:hasKind&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:someValuesFrom&#32;coswot:StateKind&#32;],  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#91;&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:onProperty&#32;coswot:isStateOfInterestOf&#32;],  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;coswot:State&#32;;  &#10; &#32; &#32; &#32; &#32;skos:note&#32; &#34;A&#32;state&#32;of&#32;interest&#32;is&#32;the&#32;state&#32;of&#32;(OP&#32;coswot:isStateOfInte...&#34;,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#34;Per&#32;convention,&#32;the&#32;IRI&#32;of&#32;states&#32;of&#32;interest&#32;should&#32;consist...&#34;,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#34;States&#32;of&#32;interest&#32;need&#32;not&#32;always&#32;be&#32;explicited.&#32;It&#32;depends...&#34; &#32;.</code></pre>|

***
### MinorFail Outcome number 26

[Jump to summary definition](#summary-MinorFail-26)	|	[Previous MinorFail outcome](#minorfail-outcome-number-25)	|	[Next MinorFail outcome](#minorfail-outcome-number-27)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-states-ontology|
|----|----|
|Title|Standalone&#32;module&#32;core&#92;states&#92;ontology.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- https://gitlab.com/coswot/coswot-acimov/blob/HEAD/core/states/ontology.ttl|

#### Criterion detail
|Identifier|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|
|----|----|
|Title|Profile&#32;compatibility&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;check&#32;whether&#32;the&#32;test&#32;subject&#32;is&#32;compatible&#32;with&#32;a&#32;profile&#32;or&#32;not,&#32;and&#32;if&#32;it&#32;is&#32;not,&#32;why.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-26)|Identifier|`owl-rl-profile-error`|
|[Section top](#minorfail-outcome-number-26)|Title|OWL&#32;RL&#32;Profile&#32;incompatible|
|[Section top](#minorfail-outcome-number-26)|Description|Statement&#32;not&#32;supported|
|[Section top](#minorfail-outcome-number-26)|Pointer|<pre lang="Turtle"><code>coswot:State&#32;a&#32;owl:Class&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;State&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;Identifiable&#32;conditions&#32;that&#32;features&#32;are&#32;or&#32;may&#32;be&#32;in,&#32;and&#32;...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32; &#60;https://w3id.org/coswot/core/states> &#32;;  &#10; &#32; &#32; &#32; &#32;owl:disjointUnionOf&#32;(&#32;coswot:StateOfInterest&#32;coswot:StateKind&#32;)&#32;.</code></pre>|

***
### MinorFail Outcome number 27

[Jump to summary definition](#summary-MinorFail-27)	|	[Previous MinorFail outcome](#minorfail-outcome-number-26)	|	[Next MinorFail outcome](#minorfail-outcome-number-28)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-states-ontology|
|----|----|
|Title|Standalone&#32;module&#32;core&#92;states&#92;ontology.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- https://gitlab.com/coswot/coswot-acimov/blob/HEAD/core/states/ontology.ttl|

#### Criterion detail
|Identifier|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|
|----|----|
|Title|Profile&#32;compatibility&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;check&#32;whether&#32;the&#32;test&#32;subject&#32;is&#32;compatible&#32;with&#32;a&#32;profile&#32;or&#32;not,&#32;and&#32;if&#32;it&#32;is&#32;not,&#32;why.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-27)|Identifier|`owl-rl-profile-error`|
|[Section top](#minorfail-outcome-number-27)|Title|OWL&#32;RL&#32;Profile&#32;incompatible|
|[Section top](#minorfail-outcome-number-27)|Description|Statement&#32;not&#32;supported&#32;in&#32;a&#32;Super&#32;Class&#32;Expression|
|[Section top](#minorfail-outcome-number-27)|Pointer|<pre lang="Turtle"><code>&#91;]&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32;owl:onProperty&#32;coswot:hasKind&#32;;  &#10; &#32; &#32; &#32; &#32;owl:someValuesFrom&#32;coswot:StateKind&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-27)|Pointer|<pre lang="Turtle"><code>&#91;]&#32;a&#32;owl:Class&#32;;  &#10; &#32; &#32;&#32; &#32;owl:unionOf&#32;(&#32;coswot:Feature&#32;coswot:StateOfInterest&#32;)&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-27)|Pointer|<pre lang="Turtle"><code>&#91;]&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32;&#32; &#32;owl:onProperty&#32;coswot:isStateOfInterestOf&#32;.</code></pre>|

***
### MinorFail Outcome number 28

[Jump to summary definition](#summary-MinorFail-28)	|	[Previous MinorFail outcome](#minorfail-outcome-number-27)	|	[Next MinorFail outcome](#minorfail-outcome-number-29)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-services-operations-ontology|
|----|----|
|Title|Standalone&#32;module&#32;core&#92;services&lowbar;operations&#92;ontology.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- https://gitlab.com/coswot/coswot-acimov/blob/HEAD/core/services_operations/ontology.ttl|

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
|[Section top](#minorfail-outcome-number-28)|Description|Class&#32;Expression&#32;not&#32;supported&#32;as&#32;object&#32;of&#32;rdfs:domain&#32;or&#32;rdfs:range|
|[Section top](#minorfail-outcome-number-28)|Pointer|<pre lang="Turtle"><code>coswot:represents&#32;a&#32;owl:ObjectProperty&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;represents&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;Links&#32;a&#32;service&#32;to&#32;some&#32;function&#32;or&#32;function&#32;of&#32;interest&#32;it&#32;...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:domain&#32; &#91;&#32;a&#32;owl:Class&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:unionOf&#32;(&#32;coswot:Service&#32;coswot:Operation&#32;)&#32;]&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32; &#60;https://w3id.org/coswot/core/services&lowbar;operations> &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:range&#32; &#91;&#32;a&#32;owl:Class&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:unionOf&#32;(&#32;coswot:Function&#32;coswot:Command&#32;)&#32;]&#32;.</code></pre>|

***
### MinorFail Outcome number 29

[Jump to summary definition](#summary-MinorFail-29)	|	[Previous MinorFail outcome](#minorfail-outcome-number-28)	|	[Next MinorFail outcome](#minorfail-outcome-number-30)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-services-operations-ontology|
|----|----|
|Title|Standalone&#32;module&#32;core&#92;services&lowbar;operations&#92;ontology.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- https://gitlab.com/coswot/coswot-acimov/blob/HEAD/core/services_operations/ontology.ttl|

#### Criterion detail
|Identifier|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|
|----|----|
|Title|Profile&#32;compatibility&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;check&#32;whether&#32;the&#32;test&#32;subject&#32;is&#32;compatible&#32;with&#32;a&#32;profile&#32;or&#32;not,&#32;and&#32;if&#32;it&#32;is&#32;not,&#32;why.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-29)|Identifier|`owl-el-profile-error`|
|[Section top](#minorfail-outcome-number-29)|Title|OWL&#32;EL&#32;Profile&#32;incompatible|
|[Section top](#minorfail-outcome-number-29)|Description|Class&#32;Expression&#32;not&#32;supported&#32;with&#32;rdfs:subClassOf|
|[Section top](#minorfail-outcome-number-29)|Pointer|<pre lang="Turtle"><code>coswot:Command&#32;rdfs:subClassOf&#32; &#91;&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:allValuesFrom&#32;coswot:Operation&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:onProperty&#32; &#91;&#32;owl:inverseOf&#32;coswot:represents&#32;]&#32;]&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-29)|Pointer|<pre lang="Turtle"><code>coswot:CommandKind&#32;rdfs:subClassOf&#32; &#91;&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:allValuesFrom&#32;coswot:OperationKind&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:onProperty&#32; &#91;&#32;owl:inverseOf&#32;coswot:represents&#32;]&#32;]&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-29)|Pointer|<pre lang="Turtle"><code>coswot:DeviceKind&#32;rdfs:subClassOf&#32; &#91;&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:allValuesFrom&#32;coswot:ServiceKind&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:onProperty&#32;coswot:offers&#32;]&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-29)|Pointer|<pre lang="Turtle"><code>coswot:Function&#32;rdfs:subClassOf&#32; &#91;&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:allValuesFrom&#32;coswot:Service&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:onProperty&#32; &#91;&#32;owl:inverseOf&#32;coswot:represents&#32;]&#32;]&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-29)|Pointer|<pre lang="Turtle"><code>coswot:FunctionKind&#32;rdfs:subClassOf&#32; &#91;&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:allValuesFrom&#32;coswot:ServiceKind&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:onProperty&#32; &#91;&#32;owl:inverseOf&#32;coswot:represents&#32;]&#32;]&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-29)|Pointer|<pre lang="Turtle"><code>coswot:Operation&#32;a&#32;owl:Class&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;Operation&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;A&#32;coswot:Operation&#32;is&#32;the&#32;means&#32;of&#32;a&#32;service&#32;to&#32;communicate&#32;...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32; &#60;https://w3id.org/coswot/core/services&lowbar;operations> &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:subClassOf&#32; &#91;&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:allValuesFrom&#32;coswot:Command&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:onProperty&#32;coswot:represents&#32;],  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;coswot:Procedure&#32;;  &#10; &#32; &#32; &#32; &#32;owl:disjointUnionOf&#32;(&#32;coswot:OperationOfInterest&#32;coswot:OperationKind&#32;)&#32;;  &#10; &#32; &#32; &#32; &#32;skos:example&#32; &#34;In&#32;the&#32;set&#32;of&#32;operations&#32;exposed&#32;by&#32;a&#32;smart&#32;light&#32;bulb&#32;on&#32;a&#32;...&#34;,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#34;In&#32;the&#32;set&#32;of&#32;operations&#32;exposed&#32;by&#32;a&#32;smart&#32;washing&#32;machine&#32;...&#34;,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#34;To&#32;turn&#32;on&#32;a&#32;light,&#32;send&#32;a&#32;CoAP&#32;PUT&#32;request&#32;with&#32;CBOR&#32;conten...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;skos:note&#32; &#34;An&#32;operation&#32;may&#32;be&#32;described&#32;in&#32;terms&#32;of&#32;its&#32;inputs&#32;and&#32;out...&#34;,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#34;Typically,&#32;a&#32;device&#32;connected&#32;to&#32;a&#32;given&#32;network&#32;offers&#32;one&#32;...&#34; &#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-29)|Pointer|<pre lang="Turtle"><code>coswot:OperationExecution&#32;a&#32;owl:Class&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;Operation&#32;Execution&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;Describes&#32;the&#32;execution&#32;of&#32;an&#32;operation&#32;in&#32;a&#32;network:&#32;theâ€“...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32; &#60;https://w3id.org/coswot/core/services&lowbar;operations> &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:subClassOf&#32; &#91;&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:allValuesFrom&#32;coswot:Operation&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:onProperty&#32;coswot:isExecutionOf&#32;],  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;coswot:ProcedureExecution&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-29)|Pointer|<pre lang="Turtle"><code>coswot:OperationKind&#32;a&#32;owl:Class&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;Operation&#32;Kind&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;An&#32;operation&#32;kind&#32;describes&#32;an&#32;archetype&#32;of&#32;operation.&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32; &#60;https://w3id.org/coswot/core/services&lowbar;operations> &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:subClassOf&#32; &#91;&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:allValuesFrom&#32;coswot:OperationKind&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:onProperty&#32;skos:broader&#32;],  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#91;&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:allValuesFrom&#32;coswot:OperationKind&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:onProperty&#32;skos:narrower&#32;],  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#91;&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:allValuesFrom&#32;owl:Nothing&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:onProperty&#32;coswot:hasKind&#32;],  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#91;&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:allValuesFrom&#32;coswot:CommandKind&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:onProperty&#32;coswot:represents&#32;],  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#91;&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:allValuesFrom&#32;coswot:ServiceKind&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:onProperty&#32;coswot:isOperationOf&#32;],  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;skos:Concept,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;coswot:Operation&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-29)|Pointer|<pre lang="Turtle"><code>coswot:OperationOfInterest&#32;a&#32;owl:Class&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;Operation&#32;Of&#32;Interest&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;An&#32;operation&#32;of&#32;interest&#32;is&#32;specific&#32;to&#32;a&#32;function&#32;of&#32;intere...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32; &#60;https://w3id.org/coswot/core/services&lowbar;operations> &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:subClassOf&#32; &#91;&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:allValuesFrom&#32;coswot:OperationKind&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:onProperty&#32;coswot:hasKind&#32;],  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#91;&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:onProperty&#32;coswot:hasKind&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:someValuesFrom&#32;coswot:OperationKind&#32;],  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#91;&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:onClass&#32;coswot:CommandOfInterest&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:onProperty&#32;coswot:represents&#32;],  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#91;&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:onClass&#32;coswot:CommandOfInterest&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:onProperty&#32;coswot:represents&#32;],  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#91;&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:onProperty&#32;coswot:isOperationOf&#32;],  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;coswot:Operation&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-29)|Pointer|<pre lang="Turtle"><code>coswot:ServiceKind&#32;a&#32;owl:Class&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;Service&#32;Kind&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;A&#32;coswot:Service&#32;is&#32;a&#32;digital&#32;representation&#32;of&#32;a&#32;function&#32;i...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32; &#60;https://w3id.org/coswot/core/services&lowbar;operations> &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:subClassOf&#32; &#91;&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:allValuesFrom&#32;coswot:ServiceKind&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:onProperty&#32;skos:broader&#32;],  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#91;&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:allValuesFrom&#32;coswot:ServiceKind&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:onProperty&#32;skos:narrower&#32;],  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#91;&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:allValuesFrom&#32;owl:Nothing&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:onProperty&#32;coswot:hasKind&#32;],  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#91;&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:allValuesFrom&#32;coswot:FunctionKind&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:onProperty&#32;coswot:represents&#32;],  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#91;&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:allValuesFrom&#32;coswot:DeviceKind&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:onProperty&#32;coswot:isOfferedBy&#32;],  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#91;&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:allValuesFrom&#32;coswot:OperationKind&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:onProperty&#32;coswot:hasOperation&#32;],  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;coswot:Service&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-29)|Pointer|<pre lang="Turtle"><code>coswot:ServiceOfInterest&#32;a&#32;owl:Class&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;Service&#32;Of&#32;Interest&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;A&#32;coswot:Service&#32;is&#32;a&#32;digital&#32;representation&#32;of&#32;a&#32;function&#32;i...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32; &#60;https://w3id.org/coswot/core/services&lowbar;operations> &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:subClassOf&#32; &#91;&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:allValuesFrom&#32;coswot:ServiceKind&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:onProperty&#32;coswot:hasKind&#32;],  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#91;&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:onProperty&#32;coswot:hasKind&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:someValuesFrom&#32;coswot:ServiceKind&#32;],  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#91;&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:onClass&#32;coswot:FunctionOfInterest&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:onProperty&#32;coswot:represents&#32;],  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;coswot:Service&#32;.</code></pre>|

***
### MinorFail Outcome number 30

[Jump to summary definition](#summary-MinorFail-30)	|	[Previous MinorFail outcome](#minorfail-outcome-number-29)	|	[Next MinorFail outcome](#minorfail-outcome-number-31)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-services-operations-ontology|
|----|----|
|Title|Standalone&#32;module&#32;core&#92;services&lowbar;operations&#92;ontology.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- https://gitlab.com/coswot/coswot-acimov/blob/HEAD/core/services_operations/ontology.ttl|

#### Criterion detail
|Identifier|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|
|----|----|
|Title|Profile&#32;compatibility&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;check&#32;whether&#32;the&#32;test&#32;subject&#32;is&#32;compatible&#32;with&#32;a&#32;profile&#32;or&#32;not,&#32;and&#32;if&#32;it&#32;is&#32;not,&#32;why.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-30)|Identifier|`owl-el-profile-error`|
|[Section top](#minorfail-outcome-number-30)|Title|OWL&#32;EL&#32;Profile&#32;incompatible|
|[Section top](#minorfail-outcome-number-30)|Description|Statement&#32;not&#32;supported|
|[Section top](#minorfail-outcome-number-30)|Pointer|<pre lang="Turtle"><code>coswot:Service&#32;a&#32;owl:Class&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;Service&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;A&#32;coswot:Service&#32;is&#32;a&#32;digital&#32;representation&#32;of&#32;a&#32;function&#32;i...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32; &#60;https://w3id.org/coswot/core/services&lowbar;operations> &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:subClassOf&#32; &#91;&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:allValuesFrom&#32;coswot:Function&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:onProperty&#32;coswot:represents&#32;],  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;coswot:ProcedureCollection&#32;;  &#10; &#32; &#32; &#32; &#32;owl:disjointUnionOf&#32;(&#32;coswot:ServiceOfInterest&#32;coswot:ServiceKind&#32;)&#32;;  &#10; &#32; &#32; &#32; &#32;skos:example&#32; &#34;For&#32;example,&#32;a&#32;light&#32;switch&#32;can&#32;offer&#32;the&#32;service&#32;of&#32;remotel...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;skos:note&#32; &#34;Typically,&#32;a&#32;device&#32;connected&#32;to&#32;a&#32;given&#32;network&#32;offers&#32;one&#32;...&#34; &#32;.</code></pre>|

***
### MinorFail Outcome number 31

[Jump to summary definition](#summary-MinorFail-31)	|	[Previous MinorFail outcome](#minorfail-outcome-number-30)	|	[Next MinorFail outcome](#minorfail-outcome-number-32)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-services-operations-ontology|
|----|----|
|Title|Standalone&#32;module&#32;core&#92;services&lowbar;operations&#92;ontology.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- https://gitlab.com/coswot/coswot-acimov/blob/HEAD/core/services_operations/ontology.ttl|

#### Criterion detail
|Identifier|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|
|----|----|
|Title|Profile&#32;compatibility&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;check&#32;whether&#32;the&#32;test&#32;subject&#32;is&#32;compatible&#32;with&#32;a&#32;profile&#32;or&#32;not,&#32;and&#32;if&#32;it&#32;is&#32;not,&#32;why.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-31)|Identifier|`owl-el-profile-error`|
|[Section top](#minorfail-outcome-number-31)|Title|OWL&#32;EL&#32;Profile&#32;incompatible|
|[Section top](#minorfail-outcome-number-31)|Description|Statement&#32;not&#32;supported&#32;in&#32;a&#32;Class&#32;Expression|
|[Section top](#minorfail-outcome-number-31)|Pointer|<pre lang="Turtle"><code>&#91;]&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32;owl:allValuesFrom&#32;coswot:ServiceKind&#32;;  &#10; &#32; &#32; &#32; &#32;owl:onProperty&#32;skos:broader&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-31)|Pointer|<pre lang="Turtle"><code>&#91;]&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32;owl:allValuesFrom&#32;coswot:ServiceKind&#32;;  &#10; &#32; &#32; &#32; &#32;owl:onProperty&#32;skos:narrower&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-31)|Pointer|<pre lang="Turtle"><code>&#91;]&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32;owl:allValuesFrom&#32;owl:Nothing&#32;;  &#10; &#32; &#32; &#32; &#32;owl:onProperty&#32;coswot:hasKind&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-31)|Pointer|<pre lang="Turtle"><code>&#91;]&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32;owl:allValuesFrom&#32;coswot:ServiceKind&#32;;  &#10; &#32; &#32; &#32; &#32;owl:onProperty&#32;coswot:hasKind&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-31)|Pointer|<pre lang="Turtle"><code>&#91;]&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32;owl:allValuesFrom&#32;coswot:OperationKind&#32;;  &#10; &#32; &#32; &#32; &#32;owl:onProperty&#32;skos:broader&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-31)|Pointer|<pre lang="Turtle"><code>&#91;]&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32;owl:allValuesFrom&#32;coswot:OperationKind&#32;;  &#10; &#32; &#32; &#32; &#32;owl:onProperty&#32;skos:narrower&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-31)|Pointer|<pre lang="Turtle"><code>&#91;]&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32;owl:allValuesFrom&#32;coswot:OperationKind&#32;;  &#10; &#32; &#32; &#32; &#32;owl:onProperty&#32;coswot:hasKind&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-31)|Pointer|<pre lang="Turtle"><code>&#91;]&#32;a&#32;owl:Class&#32;;  &#10; &#32; &#32;&#32; &#32;owl:unionOf&#32;(&#32;coswot:Service&#32;coswot:Operation&#32;)&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-31)|Pointer|<pre lang="Turtle"><code>&#91;]&#32;a&#32;owl:Class&#32;;  &#10; &#32; &#32;&#32; &#32;owl:unionOf&#32;(&#32;coswot:Function&#32;coswot:Command&#32;)&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-31)|Pointer|<pre lang="Turtle"><code>&#91;]&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32;owl:allValuesFrom&#32;coswot:Function&#32;;  &#10; &#32; &#32; &#32; &#32;owl:onProperty&#32;coswot:represents&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-31)|Pointer|<pre lang="Turtle"><code>&#91;]&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32;owl:allValuesFrom&#32;coswot:Service&#32;;  &#10; &#32; &#32; &#32; &#32;owl:onProperty&#32; &#91;&#32;owl:inverseOf&#32;coswot:represents&#32;]&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-31)|Pointer|<pre lang="Turtle"><code>&#91;]&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32;owl:allValuesFrom&#32;coswot:Command&#32;;  &#10; &#32; &#32; &#32; &#32;owl:onProperty&#32;coswot:represents&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-31)|Pointer|<pre lang="Turtle"><code>&#91;]&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32;owl:allValuesFrom&#32;coswot:Operation&#32;;  &#10; &#32; &#32; &#32; &#32;owl:onProperty&#32; &#91;&#32;owl:inverseOf&#32;coswot:represents&#32;]&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-31)|Pointer|<pre lang="Turtle"><code>&#91;]&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32;owl:allValuesFrom&#32;coswot:FunctionKind&#32;;  &#10; &#32; &#32; &#32; &#32;owl:onProperty&#32;coswot:represents&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-31)|Pointer|<pre lang="Turtle"><code>&#91;]&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32;owl:allValuesFrom&#32;coswot:ServiceKind&#32;;  &#10; &#32; &#32; &#32; &#32;owl:onProperty&#32; &#91;&#32;owl:inverseOf&#32;coswot:represents&#32;]&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-31)|Pointer|<pre lang="Turtle"><code>&#91;]&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32;owl:allValuesFrom&#32;coswot:CommandKind&#32;;  &#10; &#32; &#32; &#32; &#32;owl:onProperty&#32;coswot:represents&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-31)|Pointer|<pre lang="Turtle"><code>&#91;]&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32;owl:allValuesFrom&#32;coswot:OperationKind&#32;;  &#10; &#32; &#32; &#32; &#32;owl:onProperty&#32; &#91;&#32;owl:inverseOf&#32;coswot:represents&#32;]&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-31)|Pointer|<pre lang="Turtle"><code>&#91;]&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32;owl:onClass&#32;coswot:FunctionOfInterest&#32;;  &#10; &#32; &#32; &#32; &#32;owl:onProperty&#32;coswot:represents&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-31)|Pointer|<pre lang="Turtle"><code>&#91;]&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32;owl:onClass&#32;coswot:CommandOfInterest&#32;;  &#10; &#32; &#32; &#32; &#32;owl:onProperty&#32;coswot:represents&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-31)|Pointer|<pre lang="Turtle"><code>&#91;]&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32;owl:allValuesFrom&#32;coswot:ServiceKind&#32;;  &#10; &#32; &#32; &#32; &#32;owl:onProperty&#32;coswot:offers&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-31)|Pointer|<pre lang="Turtle"><code>&#91;]&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32;owl:allValuesFrom&#32;coswot:DeviceKind&#32;;  &#10; &#32; &#32; &#32; &#32;owl:onProperty&#32;coswot:isOfferedBy&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-31)|Pointer|<pre lang="Turtle"><code>&#91;]&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32;owl:allValuesFrom&#32;coswot:OperationKind&#32;;  &#10; &#32; &#32; &#32; &#32;owl:onProperty&#32;coswot:hasOperation&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-31)|Pointer|<pre lang="Turtle"><code>&#91;]&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32;owl:allValuesFrom&#32;coswot:ServiceKind&#32;;  &#10; &#32; &#32; &#32; &#32;owl:onProperty&#32;coswot:isOperationOf&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-31)|Pointer|<pre lang="Turtle"><code>&#91;]&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32;&#32; &#32;owl:onProperty&#32;coswot:isOperationOf&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-31)|Pointer|<pre lang="Turtle"><code>&#91;]&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32;owl:allValuesFrom&#32;coswot:Operation&#32;;  &#10; &#32; &#32; &#32; &#32;owl:onProperty&#32;coswot:isExecutionOf&#32;.</code></pre>|

***
### MinorFail Outcome number 32

[Jump to summary definition](#summary-MinorFail-32)	|	[Previous MinorFail outcome](#minorfail-outcome-number-31)	|	[Next MinorFail outcome](#minorfail-outcome-number-33)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-services-operations-ontology|
|----|----|
|Title|Standalone&#32;module&#32;core&#92;services&lowbar;operations&#92;ontology.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- https://gitlab.com/coswot/coswot-acimov/blob/HEAD/core/services_operations/ontology.ttl|

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
|[Section top](#minorfail-outcome-number-32)|Description|Class&#32;Expression&#32;not&#32;supported&#32;as&#32;object&#32;of&#32;rdfs:domain&#32;or&#32;rdfs:range|
|[Section top](#minorfail-outcome-number-32)|Pointer|<pre lang="Turtle"><code>coswot:represents&#32;a&#32;owl:ObjectProperty&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;represents&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;Links&#32;a&#32;service&#32;to&#32;some&#32;function&#32;or&#32;function&#32;of&#32;interest&#32;it&#32;...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:domain&#32; &#91;&#32;a&#32;owl:Class&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:unionOf&#32;(&#32;coswot:Service&#32;coswot:Operation&#32;)&#32;]&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32; &#60;https://w3id.org/coswot/core/services&lowbar;operations> &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:range&#32; &#91;&#32;a&#32;owl:Class&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:unionOf&#32;(&#32;coswot:Function&#32;coswot:Command&#32;)&#32;]&#32;.</code></pre>|

***
### MinorFail Outcome number 33

[Jump to summary definition](#summary-MinorFail-33)	|	[Previous MinorFail outcome](#minorfail-outcome-number-32)	|	[Next MinorFail outcome](#minorfail-outcome-number-34)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-services-operations-ontology|
|----|----|
|Title|Standalone&#32;module&#32;core&#92;services&lowbar;operations&#92;ontology.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- https://gitlab.com/coswot/coswot-acimov/blob/HEAD/core/services_operations/ontology.ttl|

#### Criterion detail
|Identifier|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|
|----|----|
|Title|Profile&#32;compatibility&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;check&#32;whether&#32;the&#32;test&#32;subject&#32;is&#32;compatible&#32;with&#32;a&#32;profile&#32;or&#32;not,&#32;and&#32;if&#32;it&#32;is&#32;not,&#32;why.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-33)|Identifier|`owl-ql-profile-error`|
|[Section top](#minorfail-outcome-number-33)|Title|OWL&#32;QL&#32;Profile&#32;incompatible|
|[Section top](#minorfail-outcome-number-33)|Description|Class&#32;Expression&#32;not&#32;supported&#32;with&#32;rdfs:subClassOf|
|[Section top](#minorfail-outcome-number-33)|Pointer|<pre lang="Turtle"><code>coswot:Command&#32;rdfs:subClassOf&#32; &#91;&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:allValuesFrom&#32;coswot:Operation&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:onProperty&#32; &#91;&#32;owl:inverseOf&#32;coswot:represents&#32;]&#32;]&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-33)|Pointer|<pre lang="Turtle"><code>coswot:CommandKind&#32;rdfs:subClassOf&#32; &#91;&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:allValuesFrom&#32;coswot:OperationKind&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:onProperty&#32; &#91;&#32;owl:inverseOf&#32;coswot:represents&#32;]&#32;]&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-33)|Pointer|<pre lang="Turtle"><code>coswot:DeviceKind&#32;rdfs:subClassOf&#32; &#91;&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:allValuesFrom&#32;coswot:ServiceKind&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:onProperty&#32;coswot:offers&#32;]&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-33)|Pointer|<pre lang="Turtle"><code>coswot:Function&#32;rdfs:subClassOf&#32; &#91;&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:allValuesFrom&#32;coswot:Service&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:onProperty&#32; &#91;&#32;owl:inverseOf&#32;coswot:represents&#32;]&#32;]&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-33)|Pointer|<pre lang="Turtle"><code>coswot:FunctionKind&#32;rdfs:subClassOf&#32; &#91;&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:allValuesFrom&#32;coswot:ServiceKind&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:onProperty&#32; &#91;&#32;owl:inverseOf&#32;coswot:represents&#32;]&#32;]&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-33)|Pointer|<pre lang="Turtle"><code>coswot:Operation&#32;a&#32;owl:Class&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;Operation&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;A&#32;coswot:Operation&#32;is&#32;the&#32;means&#32;of&#32;a&#32;service&#32;to&#32;communicate&#32;...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32; &#60;https://w3id.org/coswot/core/services&lowbar;operations> &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:subClassOf&#32; &#91;&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:allValuesFrom&#32;coswot:Command&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:onProperty&#32;coswot:represents&#32;],  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;coswot:Procedure&#32;;  &#10; &#32; &#32; &#32; &#32;owl:disjointUnionOf&#32;(&#32;coswot:OperationOfInterest&#32;coswot:OperationKind&#32;)&#32;;  &#10; &#32; &#32; &#32; &#32;skos:example&#32; &#34;In&#32;the&#32;set&#32;of&#32;operations&#32;exposed&#32;by&#32;a&#32;smart&#32;light&#32;bulb&#32;on&#32;a&#32;...&#34;,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#34;In&#32;the&#32;set&#32;of&#32;operations&#32;exposed&#32;by&#32;a&#32;smart&#32;washing&#32;machine&#32;...&#34;,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#34;To&#32;turn&#32;on&#32;a&#32;light,&#32;send&#32;a&#32;CoAP&#32;PUT&#32;request&#32;with&#32;CBOR&#32;conten...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;skos:note&#32; &#34;An&#32;operation&#32;may&#32;be&#32;described&#32;in&#32;terms&#32;of&#32;its&#32;inputs&#32;and&#32;out...&#34;,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#34;Typically,&#32;a&#32;device&#32;connected&#32;to&#32;a&#32;given&#32;network&#32;offers&#32;one&#32;...&#34; &#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-33)|Pointer|<pre lang="Turtle"><code>coswot:OperationExecution&#32;a&#32;owl:Class&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;Operation&#32;Execution&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;Describes&#32;the&#32;execution&#32;of&#32;an&#32;operation&#32;in&#32;a&#32;network:&#32;theâ€“...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32; &#60;https://w3id.org/coswot/core/services&lowbar;operations> &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:subClassOf&#32; &#91;&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:allValuesFrom&#32;coswot:Operation&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:onProperty&#32;coswot:isExecutionOf&#32;],  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;coswot:ProcedureExecution&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-33)|Pointer|<pre lang="Turtle"><code>coswot:OperationKind&#32;a&#32;owl:Class&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;Operation&#32;Kind&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;An&#32;operation&#32;kind&#32;describes&#32;an&#32;archetype&#32;of&#32;operation.&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32; &#60;https://w3id.org/coswot/core/services&lowbar;operations> &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:subClassOf&#32; &#91;&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:allValuesFrom&#32;coswot:OperationKind&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:onProperty&#32;skos:broader&#32;],  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#91;&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:allValuesFrom&#32;coswot:OperationKind&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:onProperty&#32;skos:narrower&#32;],  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#91;&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:allValuesFrom&#32;owl:Nothing&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:onProperty&#32;coswot:hasKind&#32;],  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#91;&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:allValuesFrom&#32;coswot:CommandKind&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:onProperty&#32;coswot:represents&#32;],  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#91;&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:allValuesFrom&#32;coswot:ServiceKind&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:onProperty&#32;coswot:isOperationOf&#32;],  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;skos:Concept,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;coswot:Operation&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-33)|Pointer|<pre lang="Turtle"><code>coswot:OperationOfInterest&#32;a&#32;owl:Class&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;Operation&#32;Of&#32;Interest&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;An&#32;operation&#32;of&#32;interest&#32;is&#32;specific&#32;to&#32;a&#32;function&#32;of&#32;intere...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32; &#60;https://w3id.org/coswot/core/services&lowbar;operations> &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:subClassOf&#32; &#91;&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:allValuesFrom&#32;coswot:OperationKind&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:onProperty&#32;coswot:hasKind&#32;],  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#91;&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:onProperty&#32;coswot:hasKind&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:someValuesFrom&#32;coswot:OperationKind&#32;],  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#91;&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:onClass&#32;coswot:CommandOfInterest&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:onProperty&#32;coswot:represents&#32;],  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#91;&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:onClass&#32;coswot:CommandOfInterest&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:onProperty&#32;coswot:represents&#32;],  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#91;&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:onProperty&#32;coswot:isOperationOf&#32;],  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;coswot:Operation&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-33)|Pointer|<pre lang="Turtle"><code>coswot:ServiceKind&#32;a&#32;owl:Class&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;Service&#32;Kind&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;A&#32;coswot:Service&#32;is&#32;a&#32;digital&#32;representation&#32;of&#32;a&#32;function&#32;i...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32; &#60;https://w3id.org/coswot/core/services&lowbar;operations> &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:subClassOf&#32; &#91;&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:allValuesFrom&#32;coswot:ServiceKind&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:onProperty&#32;skos:broader&#32;],  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#91;&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:allValuesFrom&#32;coswot:ServiceKind&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:onProperty&#32;skos:narrower&#32;],  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#91;&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:allValuesFrom&#32;owl:Nothing&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:onProperty&#32;coswot:hasKind&#32;],  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#91;&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:allValuesFrom&#32;coswot:FunctionKind&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:onProperty&#32;coswot:represents&#32;],  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#91;&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:allValuesFrom&#32;coswot:DeviceKind&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:onProperty&#32;coswot:isOfferedBy&#32;],  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#91;&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:allValuesFrom&#32;coswot:OperationKind&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:onProperty&#32;coswot:hasOperation&#32;],  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;coswot:Service&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-33)|Pointer|<pre lang="Turtle"><code>coswot:ServiceOfInterest&#32;a&#32;owl:Class&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;Service&#32;Of&#32;Interest&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;A&#32;coswot:Service&#32;is&#32;a&#32;digital&#32;representation&#32;of&#32;a&#32;function&#32;i...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32; &#60;https://w3id.org/coswot/core/services&lowbar;operations> &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:subClassOf&#32; &#91;&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:allValuesFrom&#32;coswot:ServiceKind&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:onProperty&#32;coswot:hasKind&#32;],  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#91;&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:onProperty&#32;coswot:hasKind&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:someValuesFrom&#32;coswot:ServiceKind&#32;],  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#91;&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:onClass&#32;coswot:FunctionOfInterest&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:onProperty&#32;coswot:represents&#32;],  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;coswot:Service&#32;.</code></pre>|

***
### MinorFail Outcome number 34

[Jump to summary definition](#summary-MinorFail-34)	|	[Previous MinorFail outcome](#minorfail-outcome-number-33)	|	[Next MinorFail outcome](#minorfail-outcome-number-35)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-services-operations-ontology|
|----|----|
|Title|Standalone&#32;module&#32;core&#92;services&lowbar;operations&#92;ontology.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- https://gitlab.com/coswot/coswot-acimov/blob/HEAD/core/services_operations/ontology.ttl|

#### Criterion detail
|Identifier|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|
|----|----|
|Title|Profile&#32;compatibility&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;check&#32;whether&#32;the&#32;test&#32;subject&#32;is&#32;compatible&#32;with&#32;a&#32;profile&#32;or&#32;not,&#32;and&#32;if&#32;it&#32;is&#32;not,&#32;why.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-34)|Identifier|`owl-ql-profile-error`|
|[Section top](#minorfail-outcome-number-34)|Title|OWL&#32;QL&#32;Profile&#32;incompatible|
|[Section top](#minorfail-outcome-number-34)|Description|Property&#32;inclusions&#32;involving&#32;property&#32;chains&#32;not&#32;supported|
|[Section top](#minorfail-outcome-number-34)|Pointer|<pre lang="Turtle"><code>coswot:isExecutionOf&#32;owl:propertyChainAxiom&#32;(&#32;coswot:isExecutionOf&#32;coswot:hasKind&#32;)&#32;.</code></pre>|

***
### MinorFail Outcome number 35

[Jump to summary definition](#summary-MinorFail-35)	|	[Previous MinorFail outcome](#minorfail-outcome-number-34)	|	[Next MinorFail outcome](#minorfail-outcome-number-36)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-services-operations-ontology|
|----|----|
|Title|Standalone&#32;module&#32;core&#92;services&lowbar;operations&#92;ontology.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- https://gitlab.com/coswot/coswot-acimov/blob/HEAD/core/services_operations/ontology.ttl|

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
|[Section top](#minorfail-outcome-number-35)|Description|Statement&#32;not&#32;supported|
|[Section top](#minorfail-outcome-number-35)|Pointer|<pre lang="Turtle"><code>coswot:Service&#32;a&#32;owl:Class&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;Service&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;A&#32;coswot:Service&#32;is&#32;a&#32;digital&#32;representation&#32;of&#32;a&#32;function&#32;i...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32; &#60;https://w3id.org/coswot/core/services&lowbar;operations> &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:subClassOf&#32; &#91;&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:allValuesFrom&#32;coswot:Function&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:onProperty&#32;coswot:represents&#32;],  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;coswot:ProcedureCollection&#32;;  &#10; &#32; &#32; &#32; &#32;owl:disjointUnionOf&#32;(&#32;coswot:ServiceOfInterest&#32;coswot:ServiceKind&#32;)&#32;;  &#10; &#32; &#32; &#32; &#32;skos:example&#32; &#34;For&#32;example,&#32;a&#32;light&#32;switch&#32;can&#32;offer&#32;the&#32;service&#32;of&#32;remotel...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;skos:note&#32; &#34;Typically,&#32;a&#32;device&#32;connected&#32;to&#32;a&#32;given&#32;network&#32;offers&#32;one&#32;...&#34; &#32;.</code></pre>|

***
### MinorFail Outcome number 36

[Jump to summary definition](#summary-MinorFail-36)	|	[Previous MinorFail outcome](#minorfail-outcome-number-35)	|	[Next MinorFail outcome](#minorfail-outcome-number-37)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-services-operations-ontology|
|----|----|
|Title|Standalone&#32;module&#32;core&#92;services&lowbar;operations&#92;ontology.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- https://gitlab.com/coswot/coswot-acimov/blob/HEAD/core/services_operations/ontology.ttl|

#### Criterion detail
|Identifier|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|
|----|----|
|Title|Profile&#32;compatibility&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;check&#32;whether&#32;the&#32;test&#32;subject&#32;is&#32;compatible&#32;with&#32;a&#32;profile&#32;or&#32;not,&#32;and&#32;if&#32;it&#32;is&#32;not,&#32;why.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-36)|Identifier|`owl-ql-profile-error`|
|[Section top](#minorfail-outcome-number-36)|Title|OWL&#32;QL&#32;Profile&#32;incompatible|
|[Section top](#minorfail-outcome-number-36)|Description|Statement&#32;not&#32;supported&#32;in&#32;a&#32;Super&#32;Class&#32;Expression|
|[Section top](#minorfail-outcome-number-36)|Pointer|<pre lang="Turtle"><code>&#91;]&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32;owl:allValuesFrom&#32;coswot:ServiceKind&#32;;  &#10; &#32; &#32; &#32; &#32;owl:onProperty&#32;skos:broader&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-36)|Pointer|<pre lang="Turtle"><code>&#91;]&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32;owl:allValuesFrom&#32;coswot:ServiceKind&#32;;  &#10; &#32; &#32; &#32; &#32;owl:onProperty&#32;skos:narrower&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-36)|Pointer|<pre lang="Turtle"><code>&#91;]&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32;owl:allValuesFrom&#32;owl:Nothing&#32;;  &#10; &#32; &#32; &#32; &#32;owl:onProperty&#32;coswot:hasKind&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-36)|Pointer|<pre lang="Turtle"><code>&#91;]&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32;owl:allValuesFrom&#32;coswot:ServiceKind&#32;;  &#10; &#32; &#32; &#32; &#32;owl:onProperty&#32;coswot:hasKind&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-36)|Pointer|<pre lang="Turtle"><code>&#91;]&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32;owl:allValuesFrom&#32;coswot:OperationKind&#32;;  &#10; &#32; &#32; &#32; &#32;owl:onProperty&#32;skos:broader&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-36)|Pointer|<pre lang="Turtle"><code>&#91;]&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32;owl:allValuesFrom&#32;coswot:OperationKind&#32;;  &#10; &#32; &#32; &#32; &#32;owl:onProperty&#32;skos:narrower&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-36)|Pointer|<pre lang="Turtle"><code>&#91;]&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32;owl:allValuesFrom&#32;coswot:OperationKind&#32;;  &#10; &#32; &#32; &#32; &#32;owl:onProperty&#32;coswot:hasKind&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-36)|Pointer|<pre lang="Turtle"><code>&#91;]&#32;a&#32;owl:Class&#32;;  &#10; &#32; &#32;&#32; &#32;owl:unionOf&#32;(&#32;coswot:Service&#32;coswot:Operation&#32;)&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-36)|Pointer|<pre lang="Turtle"><code>&#91;]&#32;a&#32;owl:Class&#32;;  &#10; &#32; &#32;&#32; &#32;owl:unionOf&#32;(&#32;coswot:Function&#32;coswot:Command&#32;)&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-36)|Pointer|<pre lang="Turtle"><code>&#91;]&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32;owl:allValuesFrom&#32;coswot:Function&#32;;  &#10; &#32; &#32; &#32; &#32;owl:onProperty&#32;coswot:represents&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-36)|Pointer|<pre lang="Turtle"><code>&#91;]&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32;owl:allValuesFrom&#32;coswot:Service&#32;;  &#10; &#32; &#32; &#32; &#32;owl:onProperty&#32; &#91;&#32;owl:inverseOf&#32;coswot:represents&#32;]&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-36)|Pointer|<pre lang="Turtle"><code>&#91;]&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32;owl:allValuesFrom&#32;coswot:Command&#32;;  &#10; &#32; &#32; &#32; &#32;owl:onProperty&#32;coswot:represents&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-36)|Pointer|<pre lang="Turtle"><code>&#91;]&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32;owl:allValuesFrom&#32;coswot:Operation&#32;;  &#10; &#32; &#32; &#32; &#32;owl:onProperty&#32; &#91;&#32;owl:inverseOf&#32;coswot:represents&#32;]&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-36)|Pointer|<pre lang="Turtle"><code>&#91;]&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32;owl:allValuesFrom&#32;coswot:FunctionKind&#32;;  &#10; &#32; &#32; &#32; &#32;owl:onProperty&#32;coswot:represents&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-36)|Pointer|<pre lang="Turtle"><code>&#91;]&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32;owl:allValuesFrom&#32;coswot:ServiceKind&#32;;  &#10; &#32; &#32; &#32; &#32;owl:onProperty&#32; &#91;&#32;owl:inverseOf&#32;coswot:represents&#32;]&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-36)|Pointer|<pre lang="Turtle"><code>&#91;]&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32;owl:allValuesFrom&#32;coswot:CommandKind&#32;;  &#10; &#32; &#32; &#32; &#32;owl:onProperty&#32;coswot:represents&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-36)|Pointer|<pre lang="Turtle"><code>&#91;]&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32;owl:allValuesFrom&#32;coswot:OperationKind&#32;;  &#10; &#32; &#32; &#32; &#32;owl:onProperty&#32; &#91;&#32;owl:inverseOf&#32;coswot:represents&#32;]&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-36)|Pointer|<pre lang="Turtle"><code>&#91;]&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32;owl:onClass&#32;coswot:FunctionOfInterest&#32;;  &#10; &#32; &#32; &#32; &#32;owl:onProperty&#32;coswot:represents&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-36)|Pointer|<pre lang="Turtle"><code>&#91;]&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32;owl:onClass&#32;coswot:CommandOfInterest&#32;;  &#10; &#32; &#32; &#32; &#32;owl:onProperty&#32;coswot:represents&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-36)|Pointer|<pre lang="Turtle"><code>&#91;]&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32;owl:allValuesFrom&#32;coswot:ServiceKind&#32;;  &#10; &#32; &#32; &#32; &#32;owl:onProperty&#32;coswot:offers&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-36)|Pointer|<pre lang="Turtle"><code>&#91;]&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32;owl:allValuesFrom&#32;coswot:DeviceKind&#32;;  &#10; &#32; &#32; &#32; &#32;owl:onProperty&#32;coswot:isOfferedBy&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-36)|Pointer|<pre lang="Turtle"><code>&#91;]&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32;owl:allValuesFrom&#32;coswot:OperationKind&#32;;  &#10; &#32; &#32; &#32; &#32;owl:onProperty&#32;coswot:hasOperation&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-36)|Pointer|<pre lang="Turtle"><code>&#91;]&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32;owl:allValuesFrom&#32;coswot:ServiceKind&#32;;  &#10; &#32; &#32; &#32; &#32;owl:onProperty&#32;coswot:isOperationOf&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-36)|Pointer|<pre lang="Turtle"><code>&#91;]&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32;&#32; &#32;owl:onProperty&#32;coswot:isOperationOf&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-36)|Pointer|<pre lang="Turtle"><code>&#91;]&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32;owl:allValuesFrom&#32;coswot:Operation&#32;;  &#10; &#32; &#32; &#32; &#32;owl:onProperty&#32;coswot:isExecutionOf&#32;.</code></pre>|

***
### MinorFail Outcome number 37

[Jump to summary definition](#summary-MinorFail-37)	|	[Previous MinorFail outcome](#minorfail-outcome-number-36)	|	[Next MinorFail outcome](#minorfail-outcome-number-38)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-services-operations-ontology|
|----|----|
|Title|Standalone&#32;module&#32;core&#92;services&lowbar;operations&#92;ontology.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- https://gitlab.com/coswot/coswot-acimov/blob/HEAD/core/services_operations/ontology.ttl|

#### Criterion detail
|Identifier|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|
|----|----|
|Title|Profile&#32;compatibility&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;check&#32;whether&#32;the&#32;test&#32;subject&#32;is&#32;compatible&#32;with&#32;a&#32;profile&#32;or&#32;not,&#32;and&#32;if&#32;it&#32;is&#32;not,&#32;why.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-37)|Identifier|`owl-rl-profile-error`|
|[Section top](#minorfail-outcome-number-37)|Title|OWL&#32;RL&#32;Profile&#32;incompatible|
|[Section top](#minorfail-outcome-number-37)|Description|Class&#32;Expression&#32;not&#32;supported&#32;as&#32;object&#32;of&#32;rdfs:domain&#32;or&#32;rdfs:range|
|[Section top](#minorfail-outcome-number-37)|Pointer|<pre lang="Turtle"><code>coswot:represents&#32;a&#32;owl:ObjectProperty&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;represents&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;Links&#32;a&#32;service&#32;to&#32;some&#32;function&#32;or&#32;function&#32;of&#32;interest&#32;it&#32;...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:domain&#32; &#91;&#32;a&#32;owl:Class&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:unionOf&#32;(&#32;coswot:Service&#32;coswot:Operation&#32;)&#32;]&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32; &#60;https://w3id.org/coswot/core/services&lowbar;operations> &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:range&#32; &#91;&#32;a&#32;owl:Class&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:unionOf&#32;(&#32;coswot:Function&#32;coswot:Command&#32;)&#32;]&#32;.</code></pre>|

***
### MinorFail Outcome number 38

[Jump to summary definition](#summary-MinorFail-38)	|	[Previous MinorFail outcome](#minorfail-outcome-number-37)	|	[Next MinorFail outcome](#minorfail-outcome-number-39)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-services-operations-ontology|
|----|----|
|Title|Standalone&#32;module&#32;core&#92;services&lowbar;operations&#92;ontology.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- https://gitlab.com/coswot/coswot-acimov/blob/HEAD/core/services_operations/ontology.ttl|

#### Criterion detail
|Identifier|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|
|----|----|
|Title|Profile&#32;compatibility&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;check&#32;whether&#32;the&#32;test&#32;subject&#32;is&#32;compatible&#32;with&#32;a&#32;profile&#32;or&#32;not,&#32;and&#32;if&#32;it&#32;is&#32;not,&#32;why.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-38)|Identifier|`owl-rl-profile-error`|
|[Section top](#minorfail-outcome-number-38)|Title|OWL&#32;RL&#32;Profile&#32;incompatible|
|[Section top](#minorfail-outcome-number-38)|Description|Class&#32;Expression&#32;not&#32;supported&#32;with&#32;rdfs:subClassOf|
|[Section top](#minorfail-outcome-number-38)|Pointer|<pre lang="Turtle"><code>coswot:OperationOfInterest&#32;a&#32;owl:Class&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;Operation&#32;Of&#32;Interest&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;An&#32;operation&#32;of&#32;interest&#32;is&#32;specific&#32;to&#32;a&#32;function&#32;of&#32;intere...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32; &#60;https://w3id.org/coswot/core/services&lowbar;operations> &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:subClassOf&#32; &#91;&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:allValuesFrom&#32;coswot:OperationKind&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:onProperty&#32;coswot:hasKind&#32;],  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#91;&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:onProperty&#32;coswot:hasKind&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:someValuesFrom&#32;coswot:OperationKind&#32;],  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#91;&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:onClass&#32;coswot:CommandOfInterest&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:onProperty&#32;coswot:represents&#32;],  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#91;&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:onClass&#32;coswot:CommandOfInterest&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:onProperty&#32;coswot:represents&#32;],  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#91;&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:onProperty&#32;coswot:isOperationOf&#32;],  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;coswot:Operation&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-38)|Pointer|<pre lang="Turtle"><code>coswot:ServiceOfInterest&#32;a&#32;owl:Class&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;Service&#32;Of&#32;Interest&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;A&#32;coswot:Service&#32;is&#32;a&#32;digital&#32;representation&#32;of&#32;a&#32;function&#32;i...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32; &#60;https://w3id.org/coswot/core/services&lowbar;operations> &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:subClassOf&#32; &#91;&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:allValuesFrom&#32;coswot:ServiceKind&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:onProperty&#32;coswot:hasKind&#32;],  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#91;&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:onProperty&#32;coswot:hasKind&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:someValuesFrom&#32;coswot:ServiceKind&#32;],  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#91;&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:onClass&#32;coswot:FunctionOfInterest&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:onProperty&#32;coswot:represents&#32;],  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;coswot:Service&#32;.</code></pre>|

***
### MinorFail Outcome number 39

[Jump to summary definition](#summary-MinorFail-39)	|	[Previous MinorFail outcome](#minorfail-outcome-number-38)	|	[Next MinorFail outcome](#minorfail-outcome-number-40)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-services-operations-ontology|
|----|----|
|Title|Standalone&#32;module&#32;core&#92;services&lowbar;operations&#92;ontology.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- https://gitlab.com/coswot/coswot-acimov/blob/HEAD/core/services_operations/ontology.ttl|

#### Criterion detail
|Identifier|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|
|----|----|
|Title|Profile&#32;compatibility&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;check&#32;whether&#32;the&#32;test&#32;subject&#32;is&#32;compatible&#32;with&#32;a&#32;profile&#32;or&#32;not,&#32;and&#32;if&#32;it&#32;is&#32;not,&#32;why.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-39)|Identifier|`owl-rl-profile-error`|
|[Section top](#minorfail-outcome-number-39)|Title|OWL&#32;RL&#32;Profile&#32;incompatible|
|[Section top](#minorfail-outcome-number-39)|Description|Statement&#32;not&#32;supported|
|[Section top](#minorfail-outcome-number-39)|Pointer|<pre lang="Turtle"><code>coswot:Service&#32;a&#32;owl:Class&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;Service&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;A&#32;coswot:Service&#32;is&#32;a&#32;digital&#32;representation&#32;of&#32;a&#32;function&#32;i...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32; &#60;https://w3id.org/coswot/core/services&lowbar;operations> &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:subClassOf&#32; &#91;&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:allValuesFrom&#32;coswot:Function&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:onProperty&#32;coswot:represents&#32;],  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;coswot:ProcedureCollection&#32;;  &#10; &#32; &#32; &#32; &#32;owl:disjointUnionOf&#32;(&#32;coswot:ServiceOfInterest&#32;coswot:ServiceKind&#32;)&#32;;  &#10; &#32; &#32; &#32; &#32;skos:example&#32; &#34;For&#32;example,&#32;a&#32;light&#32;switch&#32;can&#32;offer&#32;the&#32;service&#32;of&#32;remotel...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;skos:note&#32; &#34;Typically,&#32;a&#32;device&#32;connected&#32;to&#32;a&#32;given&#32;network&#32;offers&#32;one&#32;...&#34; &#32;.</code></pre>|

***
### MinorFail Outcome number 40

[Jump to summary definition](#summary-MinorFail-40)	|	[Previous MinorFail outcome](#minorfail-outcome-number-39)	|	[Next MinorFail outcome](#minorfail-outcome-number-41)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-services-operations-ontology|
|----|----|
|Title|Standalone&#32;module&#32;core&#92;services&lowbar;operations&#92;ontology.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- https://gitlab.com/coswot/coswot-acimov/blob/HEAD/core/services_operations/ontology.ttl|

#### Criterion detail
|Identifier|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|
|----|----|
|Title|Profile&#32;compatibility&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;check&#32;whether&#32;the&#32;test&#32;subject&#32;is&#32;compatible&#32;with&#32;a&#32;profile&#32;or&#32;not,&#32;and&#32;if&#32;it&#32;is&#32;not,&#32;why.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-40)|Identifier|`owl-rl-profile-error`|
|[Section top](#minorfail-outcome-number-40)|Title|OWL&#32;RL&#32;Profile&#32;incompatible|
|[Section top](#minorfail-outcome-number-40)|Description|Statement&#32;not&#32;supported&#32;in&#32;a&#32;Super&#32;Class&#32;Expression|
|[Section top](#minorfail-outcome-number-40)|Pointer|<pre lang="Turtle"><code>&#91;]&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32;owl:onProperty&#32;coswot:hasKind&#32;;  &#10; &#32; &#32; &#32; &#32;owl:someValuesFrom&#32;coswot:ServiceKind&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-40)|Pointer|<pre lang="Turtle"><code>&#91;]&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32;owl:onProperty&#32;coswot:hasKind&#32;;  &#10; &#32; &#32; &#32; &#32;owl:someValuesFrom&#32;coswot:OperationKind&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-40)|Pointer|<pre lang="Turtle"><code>&#91;]&#32;a&#32;owl:Class&#32;;  &#10; &#32; &#32;&#32; &#32;owl:unionOf&#32;(&#32;coswot:Service&#32;coswot:Operation&#32;)&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-40)|Pointer|<pre lang="Turtle"><code>&#91;]&#32;a&#32;owl:Class&#32;;  &#10; &#32; &#32;&#32; &#32;owl:unionOf&#32;(&#32;coswot:Function&#32;coswot:Command&#32;)&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-40)|Pointer|<pre lang="Turtle"><code>&#91;]&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32;owl:onClass&#32;coswot:FunctionOfInterest&#32;;  &#10; &#32; &#32; &#32; &#32;owl:onProperty&#32;coswot:represents&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-40)|Pointer|<pre lang="Turtle"><code>&#91;]&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32;owl:onClass&#32;coswot:CommandOfInterest&#32;;  &#10; &#32; &#32; &#32; &#32;owl:onProperty&#32;coswot:represents&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-40)|Pointer|<pre lang="Turtle"><code>&#91;]&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32;&#32; &#32;owl:onProperty&#32;coswot:isOperationOf&#32;.</code></pre>|

***
### MinorFail Outcome number 41

[Jump to summary definition](#summary-MinorFail-41)	|	[Previous MinorFail outcome](#minorfail-outcome-number-40)	|	[Next MinorFail outcome](#minorfail-outcome-number-42)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-services-operations-ontology|
|----|----|
|Title|Standalone&#32;module&#32;core&#92;services&lowbar;operations&#92;ontology.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- https://gitlab.com/coswot/coswot-acimov/blob/HEAD/core/services_operations/ontology.ttl|

#### Criterion detail
|Identifier|[term-referencing](https://ns.inria.fr/olivaw#term-referencing)|
|----|----|
|Title|Term&#32;referencing&#32;test|
|Description|A&#32;test&#32;case&#32;from&#32;the&#32;Best&#32;Practices&#32;tests&#32;checking&#32;if&#32;each&#32;term&#32;of&#32;the&#32;test&#32;subject&#32;is&#32;referenced&#32;to&#32;a&#32;module&#32;through&#32;a&#32;rdfs:isDefinedBy&#32;property.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-41)|Identifier|`no-reference-module`|
|[Section top](#minorfail-outcome-number-41)|Title|Term&#32;not&#32;referenced&#32;to&#32;a&#32;module|
|[Section top](#minorfail-outcome-number-41)|Description|Subject&#32;terms&#32;not&#32;linked&#32;to&#32;a&#32;module&#32;by&#32;a&#32;rdfs:isDefinedBy&#32;property|
|[Section top](#minorfail-outcome-number-41)|Pointer|<pre lang="Turtle"><code>:Function&#32;rdfs:subClassOf&#32; &#91;&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:allValuesFrom&#32;:Service&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:onProperty&#32; &#91;&#32;owl:inverseOf&#32;:represents&#32;]&#32;]&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-41)|Pointer|<pre lang="Turtle"><code>:Command&#32;rdfs:subClassOf&#32; &#91;&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:allValuesFrom&#32;:Operation&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:onProperty&#32; &#91;&#32;owl:inverseOf&#32;:represents&#32;]&#32;]&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-41)|Pointer|<pre lang="Turtle"><code>:FunctionKind&#32;rdfs:subClassOf&#32; &#91;&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:allValuesFrom&#32;:ServiceKind&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:onProperty&#32; &#91;&#32;owl:inverseOf&#32;:represents&#32;]&#32;]&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-41)|Pointer|<pre lang="Turtle"><code>:CommandKind&#32;rdfs:subClassOf&#32; &#91;&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:allValuesFrom&#32;:OperationKind&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:onProperty&#32; &#91;&#32;owl:inverseOf&#32;:represents&#32;]&#32;]&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-41)|Pointer|<pre lang="Turtle"><code>:DeviceKind&#32;rdfs:subClassOf&#32; &#91;&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:allValuesFrom&#32;:ServiceKind&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:onProperty&#32;:offers&#32;]&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-41)|Pointer|<pre lang="Turtle"><code>:isExecutionOf&#32;owl:propertyChainAxiom&#32;(&#32;:isExecutionOf&#32;:hasKind&#32;)&#32;.</code></pre>|

***
### MinorFail Outcome number 42

[Jump to summary definition](#summary-MinorFail-42)	|	[Previous MinorFail outcome](#minorfail-outcome-number-41)	|	[Next MinorFail outcome](#minorfail-outcome-number-43)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-samples-ontology|
|----|----|
|Title|Standalone&#32;module&#32;core&#92;samples&#92;ontology.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- https://gitlab.com/coswot/coswot-acimov/blob/HEAD/core/samples/ontology.ttl|

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
|[Section top](#minorfail-outcome-number-42)|Pointer|<pre lang="Turtle"><code>coswot:isSamplePropertyOf&#32;a&#32;owl:FunctionalProperty,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:ObjectProperty&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;is&#32;sample&#32;property&#32;of&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;Direct&#32;relation&#32;from&#32;the&#32;Property&#32;of&#32;interest&#32;of&#32;a&#32;sample&#32;to...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:domain&#32;coswot:PropertyOfInterest&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32; &#60;https://w3id.org/coswot/core/samples> &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:range&#32;coswot:PropertyOfInterest&#32;.</code></pre>|

***
### MinorFail Outcome number 43

[Jump to summary definition](#summary-MinorFail-43)	|	[Previous MinorFail outcome](#minorfail-outcome-number-42)	|	[Next MinorFail outcome](#minorfail-outcome-number-44)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-samples-ontology|
|----|----|
|Title|Standalone&#32;module&#32;core&#92;samples&#92;ontology.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- https://gitlab.com/coswot/coswot-acimov/blob/HEAD/core/samples/ontology.ttl|

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
|[Section top](#minorfail-outcome-number-43)|Description|Property&#32;inclusions&#32;involving&#32;property&#32;chains&#32;not&#32;supported|
|[Section top](#minorfail-outcome-number-43)|Pointer|<pre lang="Turtle"><code>coswot:hasSample&#32;a&#32;owl:ObjectProperty&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;has&#32;sample&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;schema:domainIncludes&#32;coswot:FeatureOfInterest&#32;;  &#10; &#32; &#32; &#32; &#32;schema:rangeIncludes&#32;coswot:Sample&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;Relation&#32;between&#32;a&#32;FeatureOfInterest&#32;and&#32;the&#32;Sample&#32;used&#32;to&#32;...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32; &#60;https://w3id.org/coswot/core/samples> &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:subPropertyOf&#32;coswot:hasTransitiveSample&#32;;  &#10; &#32; &#32; &#32; &#32;owl:inverseOf&#32;coswot:isSampleOf&#32;;  &#10; &#32; &#32; &#32; &#32;owl:propertyChainAxiom&#32;(&#32;coswot:hasPropertyOfInterest&#32;coswot:hasSampleProperty&#32;coswot:isPropertyOfInterestOf&#32;),  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;(&#32;coswot:hasStateOfInterest&#32;coswot:hasSampleState&#32;coswot:isStateOfInterestOf&#32;)&#32;.</code></pre>|

***
### MinorFail Outcome number 44

[Jump to summary definition](#summary-MinorFail-44)	|	[Previous MinorFail outcome](#minorfail-outcome-number-43)	|	[Next MinorFail outcome](#minorfail-outcome-number-45)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-samples-ontology|
|----|----|
|Title|Standalone&#32;module&#32;core&#92;samples&#92;ontology.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- https://gitlab.com/coswot/coswot-acimov/blob/HEAD/core/samples/ontology.ttl|

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
|[Section top](#minorfail-outcome-number-44)|Description|Statement&#32;not&#32;supported|
|[Section top](#minorfail-outcome-number-44)|Pointer|<pre lang="Turtle"><code>coswot:isSamplePropertyOf&#32;a&#32;owl:FunctionalProperty,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:ObjectProperty&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;is&#32;sample&#32;property&#32;of&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;Direct&#32;relation&#32;from&#32;the&#32;Property&#32;of&#32;interest&#32;of&#32;a&#32;sample&#32;to...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:domain&#32;coswot:PropertyOfInterest&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32; &#60;https://w3id.org/coswot/core/samples> &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:range&#32;coswot:PropertyOfInterest&#32;.</code></pre>|

***
### MinorFail Outcome number 45

[Jump to summary definition](#summary-MinorFail-45)	|	[Previous MinorFail outcome](#minorfail-outcome-number-44)	|	[Next MinorFail outcome](#minorfail-outcome-number-46)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-property-values-ontology|
|----|----|
|Title|Standalone&#32;module&#32;core&#92;property&lowbar;values&#92;ontology.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- https://gitlab.com/coswot/coswot-acimov/blob/HEAD/core/property_values/ontology.ttl|

#### Criterion detail
|Identifier|[domain-and-range-referencing](https://ns.inria.fr/olivaw#domain-and-range-referencing)|
|----|----|
|Title|Domain&#32;and&#32;range&#32;referencing&#32;test|
|Description|A&#32;test&#32;case&#32;from&#32;the&#32;Best&#32;Practices&#32;tests&#32;checking&#32;if&#32;all&#32;the&#32;ranges&#32;and&#32;domains&#32;from&#32;the&#32;test&#32;subject&#32;point&#32;to&#32;terms&#32;that&#32;are&#32;defined&#32;in&#32;the&#32;vocabulary.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-45)|Identifier|`range-out-of-vocabulary`|
|[Section top](#minorfail-outcome-number-45)|Title|Range&#32;out&#32;of&#32;vocabulary|
|[Section top](#minorfail-outcome-number-45)|Description|Some&#32;properties&#32;have&#32;a&#32;range&#32;out&#32;of&#32;the&#32;ontology|
|[Section top](#minorfail-outcome-number-45)|Pointer|<pre lang="Turtle"><code>:isMeasuredIn&#32;a&#32;owl:ObjectProperty&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;is&#32;measured&#32;in&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;A&#32;relationship&#32;identifying&#32;the&#32;unit&#32;of&#32;measure&#32;used&#32;for&#32;a&#32;ce...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32; &#60;https://w3id.org/coswot/core/property&lowbar;values> &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:range&#32;skos:Concept,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;:UnitOfMeasure&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-45)|Pointer|http://www.w3.org/2004/02/skos/core#Concept|

***
### MinorFail Outcome number 46

[Jump to summary definition](#summary-MinorFail-46)	|	[Previous MinorFail outcome](#minorfail-outcome-number-45)	|	[Next MinorFail outcome](#minorfail-outcome-number-47)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-property-values-ontology|
|----|----|
|Title|Standalone&#32;module&#32;core&#92;property&lowbar;values&#92;ontology.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- https://gitlab.com/coswot/coswot-acimov/blob/HEAD/core/property_values/ontology.ttl|

#### Criterion detail
|Identifier|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|
|----|----|
|Title|Profile&#32;compatibility&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;check&#32;whether&#32;the&#32;test&#32;subject&#32;is&#32;compatible&#32;with&#32;a&#32;profile&#32;or&#32;not,&#32;and&#32;if&#32;it&#32;is&#32;not,&#32;why.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-46)|Identifier|`owl-el-profile-error`|
|[Section top](#minorfail-outcome-number-46)|Title|OWL&#32;EL&#32;Profile&#32;incompatible|
|[Section top](#minorfail-outcome-number-46)|Description|Class&#32;Expression&#32;not&#32;supported&#32;as&#32;object&#32;of&#32;rdfs:domain&#32;or&#32;rdfs:range|
|[Section top](#minorfail-outcome-number-46)|Pointer|<pre lang="Turtle"><code>coswot:hasPropertyValue&#32;a&#32;owl:ObjectProperty&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;has&#32;property&#32;value&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;Links&#32;a&#32;feature&#32;or&#32;a&#32;property&#32;of&#32;interest&#32;to&#32;a&#32;property&#32;valu...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:domain&#32; &#91;&#32;a&#32;owl:Class&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:unionOf&#32;(&#32;coswot:Feature&#32;coswot:PropertyOfInterest&#32;)&#32;]&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32; &#60;https://w3id.org/coswot/core/property&lowbar;values> &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:range&#32;coswot:PropertyValue&#32;;  &#10; &#32; &#32; &#32; &#32;owl:propertyChainAxiom&#32;(&#32;skos:broader&#32;coswot:hasPropertyValue&#32;)&#32;.</code></pre>|

***
### MinorFail Outcome number 47

[Jump to summary definition](#summary-MinorFail-47)	|	[Previous MinorFail outcome](#minorfail-outcome-number-46)	|	[Next MinorFail outcome](#minorfail-outcome-number-48)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-property-values-ontology|
|----|----|
|Title|Standalone&#32;module&#32;core&#92;property&lowbar;values&#92;ontology.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- https://gitlab.com/coswot/coswot-acimov/blob/HEAD/core/property_values/ontology.ttl|

#### Criterion detail
|Identifier|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|
|----|----|
|Title|Profile&#32;compatibility&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;check&#32;whether&#32;the&#32;test&#32;subject&#32;is&#32;compatible&#32;with&#32;a&#32;profile&#32;or&#32;not,&#32;and&#32;if&#32;it&#32;is&#32;not,&#32;why.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-47)|Identifier|`owl-el-profile-error`|
|[Section top](#minorfail-outcome-number-47)|Title|OWL&#32;EL&#32;Profile&#32;incompatible|
|[Section top](#minorfail-outcome-number-47)|Description|Class&#32;Expression&#32;not&#32;supported&#32;with&#32;rdfs:subClassOf|
|[Section top](#minorfail-outcome-number-47)|Pointer|<pre lang="Turtle"><code>coswot:PropertyValue&#32;a&#32;owl:Class&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;Property&#32;Value&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;Describes&#32;the&#32;value&#32;for&#32;a&#32;property.&#32;The&#32;property&#32;value&#32;is&#32;li...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32; &#60;https://w3id.org/coswot/core/property&lowbar;values> &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:subClassOf&#32; &#91;&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:onProperty&#32;coswot:hasValue&#32;],  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#91;&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:onProperty&#32;coswot:isMeasuredIn&#32;]&#32;.</code></pre>|

***
### MinorFail Outcome number 48

[Jump to summary definition](#summary-MinorFail-48)	|	[Previous MinorFail outcome](#minorfail-outcome-number-47)	|	[Next MinorFail outcome](#minorfail-outcome-number-49)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-property-values-ontology|
|----|----|
|Title|Standalone&#32;module&#32;core&#92;property&lowbar;values&#92;ontology.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- https://gitlab.com/coswot/coswot-acimov/blob/HEAD/core/property_values/ontology.ttl|

#### Criterion detail
|Identifier|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|
|----|----|
|Title|Profile&#32;compatibility&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;check&#32;whether&#32;the&#32;test&#32;subject&#32;is&#32;compatible&#32;with&#32;a&#32;profile&#32;or&#32;not,&#32;and&#32;if&#32;it&#32;is&#32;not,&#32;why.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-48)|Identifier|`owl-el-profile-error`|
|[Section top](#minorfail-outcome-number-48)|Title|OWL&#32;EL&#32;Profile&#32;incompatible|
|[Section top](#minorfail-outcome-number-48)|Description|Statement&#32;not&#32;supported&#32;in&#32;a&#32;Class&#32;Expression|
|[Section top](#minorfail-outcome-number-48)|Pointer|<pre lang="Turtle"><code>&#91;]&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32;&#32; &#32;owl:onProperty&#32;coswot:hasValue&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-48)|Pointer|<pre lang="Turtle"><code>&#91;]&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32;&#32; &#32;owl:onProperty&#32;coswot:isMeasuredIn&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-48)|Pointer|<pre lang="Turtle"><code>&#91;]&#32;a&#32;owl:Class&#32;;  &#10; &#32; &#32;&#32; &#32;owl:unionOf&#32;(&#32;coswot:Feature&#32;coswot:PropertyOfInterest&#32;)&#32;.</code></pre>|

***
### MinorFail Outcome number 49

[Jump to summary definition](#summary-MinorFail-49)	|	[Previous MinorFail outcome](#minorfail-outcome-number-48)	|	[Next MinorFail outcome](#minorfail-outcome-number-50)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-property-values-ontology|
|----|----|
|Title|Standalone&#32;module&#32;core&#92;property&lowbar;values&#92;ontology.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- https://gitlab.com/coswot/coswot-acimov/blob/HEAD/core/property_values/ontology.ttl|

#### Criterion detail
|Identifier|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|
|----|----|
|Title|Profile&#32;compatibility&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;check&#32;whether&#32;the&#32;test&#32;subject&#32;is&#32;compatible&#32;with&#32;a&#32;profile&#32;or&#32;not,&#32;and&#32;if&#32;it&#32;is&#32;not,&#32;why.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-49)|Identifier|`owl-ql-profile-error`|
|[Section top](#minorfail-outcome-number-49)|Title|OWL&#32;QL&#32;Profile&#32;incompatible|
|[Section top](#minorfail-outcome-number-49)|Description|Class&#32;Expression&#32;not&#32;supported&#32;as&#32;object&#32;of&#32;rdfs:domain&#32;or&#32;rdfs:range  &#10;Property&#32;inclusions&#32;involving&#32;property&#32;chains&#32;not&#32;supported|
|[Section top](#minorfail-outcome-number-49)|Pointer|<pre lang="Turtle"><code>coswot:hasPropertyValue&#32;a&#32;owl:ObjectProperty&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;has&#32;property&#32;value&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;Links&#32;a&#32;feature&#32;or&#32;a&#32;property&#32;of&#32;interest&#32;to&#32;a&#32;property&#32;valu...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:domain&#32; &#91;&#32;a&#32;owl:Class&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:unionOf&#32;(&#32;coswot:Feature&#32;coswot:PropertyOfInterest&#32;)&#32;]&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32; &#60;https://w3id.org/coswot/core/property&lowbar;values> &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:range&#32;coswot:PropertyValue&#32;;  &#10; &#32; &#32; &#32; &#32;owl:propertyChainAxiom&#32;(&#32;skos:broader&#32;coswot:hasPropertyValue&#32;)&#32;.</code></pre>|

***
### MinorFail Outcome number 50

[Jump to summary definition](#summary-MinorFail-50)	|	[Previous MinorFail outcome](#minorfail-outcome-number-49)	|	[Next MinorFail outcome](#minorfail-outcome-number-51)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-property-values-ontology|
|----|----|
|Title|Standalone&#32;module&#32;core&#92;property&lowbar;values&#92;ontology.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- https://gitlab.com/coswot/coswot-acimov/blob/HEAD/core/property_values/ontology.ttl|

#### Criterion detail
|Identifier|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|
|----|----|
|Title|Profile&#32;compatibility&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;check&#32;whether&#32;the&#32;test&#32;subject&#32;is&#32;compatible&#32;with&#32;a&#32;profile&#32;or&#32;not,&#32;and&#32;if&#32;it&#32;is&#32;not,&#32;why.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-50)|Identifier|`owl-ql-profile-error`|
|[Section top](#minorfail-outcome-number-50)|Title|OWL&#32;QL&#32;Profile&#32;incompatible|
|[Section top](#minorfail-outcome-number-50)|Description|Class&#32;Expression&#32;not&#32;supported&#32;with&#32;rdfs:subClassOf|
|[Section top](#minorfail-outcome-number-50)|Pointer|<pre lang="Turtle"><code>coswot:PropertyValue&#32;a&#32;owl:Class&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;Property&#32;Value&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;Describes&#32;the&#32;value&#32;for&#32;a&#32;property.&#32;The&#32;property&#32;value&#32;is&#32;li...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32; &#60;https://w3id.org/coswot/core/property&lowbar;values> &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:subClassOf&#32; &#91;&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:onProperty&#32;coswot:hasValue&#32;],  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#91;&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:onProperty&#32;coswot:isMeasuredIn&#32;]&#32;.</code></pre>|

***
### MinorFail Outcome number 51

[Jump to summary definition](#summary-MinorFail-51)	|	[Previous MinorFail outcome](#minorfail-outcome-number-50)	|	[Next MinorFail outcome](#minorfail-outcome-number-52)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-property-values-ontology|
|----|----|
|Title|Standalone&#32;module&#32;core&#92;property&lowbar;values&#92;ontology.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- https://gitlab.com/coswot/coswot-acimov/blob/HEAD/core/property_values/ontology.ttl|

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
|[Section top](#minorfail-outcome-number-51)|Description|Property&#32;inclusions&#32;involving&#32;property&#32;chains&#32;not&#32;supported|
|[Section top](#minorfail-outcome-number-51)|Pointer|<pre lang="Turtle"><code>coswot:isValueOfProperty&#32;a&#32;owl:ObjectProperty&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;is&#32;value&#32;of&#32;property&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;Links&#32;a&#32;property&#32;value&#32;to&#32;the&#32;property&#32;or&#32;property&#32;of&#32;intere...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:domain&#32;coswot:PropertyValue&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32; &#60;https://w3id.org/coswot/core/property&lowbar;values> &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:range&#32;coswot:Property&#32;;  &#10; &#32; &#32; &#32; &#32;owl:propertyChainAxiom&#32;(&#32;coswot:isValueOfProperty&#32;coswot:hasKind&#32;)&#32;.</code></pre>|

***
### MinorFail Outcome number 52

[Jump to summary definition](#summary-MinorFail-52)	|	[Previous MinorFail outcome](#minorfail-outcome-number-51)	|	[Next MinorFail outcome](#minorfail-outcome-number-53)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-property-values-ontology|
|----|----|
|Title|Standalone&#32;module&#32;core&#92;property&lowbar;values&#92;ontology.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- https://gitlab.com/coswot/coswot-acimov/blob/HEAD/core/property_values/ontology.ttl|

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
|[Section top](#minorfail-outcome-number-52)|Description|Statement&#32;not&#32;supported&#32;in&#32;a&#32;Super&#32;Class&#32;Expression|
|[Section top](#minorfail-outcome-number-52)|Pointer|<pre lang="Turtle"><code>&#91;]&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32;&#32; &#32;owl:onProperty&#32;coswot:hasValue&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-52)|Pointer|<pre lang="Turtle"><code>&#91;]&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32;&#32; &#32;owl:onProperty&#32;coswot:isMeasuredIn&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-52)|Pointer|<pre lang="Turtle"><code>&#91;]&#32;a&#32;owl:Class&#32;;  &#10; &#32; &#32;&#32; &#32;owl:unionOf&#32;(&#32;coswot:Feature&#32;coswot:PropertyOfInterest&#32;)&#32;.</code></pre>|

***
### MinorFail Outcome number 53

[Jump to summary definition](#summary-MinorFail-53)	|	[Previous MinorFail outcome](#minorfail-outcome-number-52)	|	[Next MinorFail outcome](#minorfail-outcome-number-54)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-property-values-ontology|
|----|----|
|Title|Standalone&#32;module&#32;core&#92;property&lowbar;values&#92;ontology.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- https://gitlab.com/coswot/coswot-acimov/blob/HEAD/core/property_values/ontology.ttl|

#### Criterion detail
|Identifier|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|
|----|----|
|Title|Profile&#32;compatibility&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;check&#32;whether&#32;the&#32;test&#32;subject&#32;is&#32;compatible&#32;with&#32;a&#32;profile&#32;or&#32;not,&#32;and&#32;if&#32;it&#32;is&#32;not,&#32;why.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-53)|Identifier|`owl-rl-profile-error`|
|[Section top](#minorfail-outcome-number-53)|Title|OWL&#32;RL&#32;Profile&#32;incompatible|
|[Section top](#minorfail-outcome-number-53)|Description|Class&#32;Expression&#32;not&#32;supported&#32;as&#32;object&#32;of&#32;rdfs:domain&#32;or&#32;rdfs:range|
|[Section top](#minorfail-outcome-number-53)|Pointer|<pre lang="Turtle"><code>coswot:hasPropertyValue&#32;a&#32;owl:ObjectProperty&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;has&#32;property&#32;value&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;Links&#32;a&#32;feature&#32;or&#32;a&#32;property&#32;of&#32;interest&#32;to&#32;a&#32;property&#32;valu...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:domain&#32; &#91;&#32;a&#32;owl:Class&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:unionOf&#32;(&#32;coswot:Feature&#32;coswot:PropertyOfInterest&#32;)&#32;]&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32; &#60;https://w3id.org/coswot/core/property&lowbar;values> &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:range&#32;coswot:PropertyValue&#32;;  &#10; &#32; &#32; &#32; &#32;owl:propertyChainAxiom&#32;(&#32;skos:broader&#32;coswot:hasPropertyValue&#32;)&#32;.</code></pre>|

***
### MinorFail Outcome number 54

[Jump to summary definition](#summary-MinorFail-54)	|	[Previous MinorFail outcome](#minorfail-outcome-number-53)	|	[Next MinorFail outcome](#minorfail-outcome-number-55)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-property-values-ontology|
|----|----|
|Title|Standalone&#32;module&#32;core&#92;property&lowbar;values&#92;ontology.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- https://gitlab.com/coswot/coswot-acimov/blob/HEAD/core/property_values/ontology.ttl|

#### Criterion detail
|Identifier|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|
|----|----|
|Title|Profile&#32;compatibility&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;check&#32;whether&#32;the&#32;test&#32;subject&#32;is&#32;compatible&#32;with&#32;a&#32;profile&#32;or&#32;not,&#32;and&#32;if&#32;it&#32;is&#32;not,&#32;why.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-54)|Identifier|`owl-rl-profile-error`|
|[Section top](#minorfail-outcome-number-54)|Title|OWL&#32;RL&#32;Profile&#32;incompatible|
|[Section top](#minorfail-outcome-number-54)|Description|Class&#32;Expression&#32;not&#32;supported&#32;with&#32;rdfs:subClassOf|
|[Section top](#minorfail-outcome-number-54)|Pointer|<pre lang="Turtle"><code>coswot:PropertyValue&#32;a&#32;owl:Class&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;Property&#32;Value&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;Describes&#32;the&#32;value&#32;for&#32;a&#32;property.&#32;The&#32;property&#32;value&#32;is&#32;li...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32; &#60;https://w3id.org/coswot/core/property&lowbar;values> &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:subClassOf&#32; &#91;&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:onProperty&#32;coswot:hasValue&#32;],  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#91;&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:onProperty&#32;coswot:isMeasuredIn&#32;]&#32;.</code></pre>|

***
### MinorFail Outcome number 55

[Jump to summary definition](#summary-MinorFail-55)	|	[Previous MinorFail outcome](#minorfail-outcome-number-54)	|	[Next MinorFail outcome](#minorfail-outcome-number-56)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-property-values-ontology|
|----|----|
|Title|Standalone&#32;module&#32;core&#92;property&lowbar;values&#92;ontology.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- https://gitlab.com/coswot/coswot-acimov/blob/HEAD/core/property_values/ontology.ttl|

#### Criterion detail
|Identifier|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|
|----|----|
|Title|Profile&#32;compatibility&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;check&#32;whether&#32;the&#32;test&#32;subject&#32;is&#32;compatible&#32;with&#32;a&#32;profile&#32;or&#32;not,&#32;and&#32;if&#32;it&#32;is&#32;not,&#32;why.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-55)|Identifier|`owl-rl-profile-error`|
|[Section top](#minorfail-outcome-number-55)|Title|OWL&#32;RL&#32;Profile&#32;incompatible|
|[Section top](#minorfail-outcome-number-55)|Description|Statement&#32;not&#32;supported&#32;in&#32;a&#32;Super&#32;Class&#32;Expression|
|[Section top](#minorfail-outcome-number-55)|Pointer|<pre lang="Turtle"><code>&#91;]&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32;&#32; &#32;owl:onProperty&#32;coswot:hasValue&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-55)|Pointer|<pre lang="Turtle"><code>&#91;]&#32;a&#32;owl:Class&#32;;  &#10; &#32; &#32;&#32; &#32;owl:unionOf&#32;(&#32;coswot:Feature&#32;coswot:PropertyOfInterest&#32;)&#32;.</code></pre>|

***
### MinorFail Outcome number 56

[Jump to summary definition](#summary-MinorFail-56)	|	[Previous MinorFail outcome](#minorfail-outcome-number-55)	|	[Next MinorFail outcome](#minorfail-outcome-number-57)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-properties-ontology-catalogs|
|----|----|
|Title|Standalone&#32;module&#32;core&#92;properties&#92;ontology.catalogs.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- https://gitlab.com/coswot/coswot-acimov/blob/HEAD/core/properties/ontology.catalogs.ttl|

#### Criterion detail
|Identifier|[domain-and-range-referencing](https://ns.inria.fr/olivaw#domain-and-range-referencing)|
|----|----|
|Title|Domain&#32;and&#32;range&#32;referencing&#32;test|
|Description|A&#32;test&#32;case&#32;from&#32;the&#32;Best&#32;Practices&#32;tests&#32;checking&#32;if&#32;all&#32;the&#32;ranges&#32;and&#32;domains&#32;from&#32;the&#32;test&#32;subject&#32;point&#32;to&#32;terms&#32;that&#32;are&#32;defined&#32;in&#32;the&#32;vocabulary.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-56)|Identifier|`domain-out-of-vocabulary`|
|[Section top](#minorfail-outcome-number-56)|Title|Domain&#32;out&#32;of&#32;vocabulary|
|[Section top](#minorfail-outcome-number-56)|Description|Some&#32;properties&#32;have&#32;a&#32;domain&#32;out&#32;of&#32;the&#32;ontology|
|[Section top](#minorfail-outcome-number-56)|Pointer|<pre lang="Turtle"><code>:isPropertyOf&#32;a&#32;owl:ObjectProperty&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;is&#32;property&#32;of&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;Links&#32;a&#32;property&#32;to&#32;the&#32;feature&#32;it&#32;is&#32;a&#32;property&#32;of.&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:domain&#32; &#91;&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:allValuesFrom&#32;:PropertyKind&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:onProperty&#32;skos:broader&#32;],  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#91;&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:allValuesFrom&#32;:PropertyKind&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:onProperty&#32;skos:narrower&#32;],  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;skos:Concept,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;:PropertyKind&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32; &#60;https://w3id.org/coswot/core/properties> &#32;;  &#10; &#32; &#32; &#32; &#32;owl:inverseOf&#32;:hasProperty&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-56)|Pointer|http://www.w3.org/2004/02/skos/core#Concept|

***
### MinorFail Outcome number 57

[Jump to summary definition](#summary-MinorFail-57)	|	[Previous MinorFail outcome](#minorfail-outcome-number-56)	|	[Next MinorFail outcome](#minorfail-outcome-number-58)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-properties-ontology-catalogs|
|----|----|
|Title|Standalone&#32;module&#32;core&#92;properties&#92;ontology.catalogs.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- https://gitlab.com/coswot/coswot-acimov/blob/HEAD/core/properties/ontology.catalogs.ttl|

#### Criterion detail
|Identifier|[domain-and-range-referencing](https://ns.inria.fr/olivaw#domain-and-range-referencing)|
|----|----|
|Title|Domain&#32;and&#32;range&#32;referencing&#32;test|
|Description|A&#32;test&#32;case&#32;from&#32;the&#32;Best&#32;Practices&#32;tests&#32;checking&#32;if&#32;all&#32;the&#32;ranges&#32;and&#32;domains&#32;from&#32;the&#32;test&#32;subject&#32;point&#32;to&#32;terms&#32;that&#32;are&#32;defined&#32;in&#32;the&#32;vocabulary.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-57)|Identifier|`range-out-of-vocabulary`|
|[Section top](#minorfail-outcome-number-57)|Title|Range&#32;out&#32;of&#32;vocabulary|
|[Section top](#minorfail-outcome-number-57)|Description|Some&#32;properties&#32;have&#32;a&#32;range&#32;out&#32;of&#32;the&#32;ontology|
|[Section top](#minorfail-outcome-number-57)|Pointer|<pre lang="Turtle"><code>:hasProperty&#32;a&#32;owl:ObjectProperty&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;has&#32;property&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;Links&#32;a&#32;feature&#32;to&#32;one&#32;of&#32;its&#32;properties.&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32; &#60;https://w3id.org/coswot/core/properties> &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:range&#32; &#91;&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:allValuesFrom&#32;:PropertyKind&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:onProperty&#32;skos:broader&#32;],  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#91;&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:allValuesFrom&#32;:PropertyKind&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:onProperty&#32;skos:narrower&#32;],  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;skos:Concept,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;:PropertyKind&#32;;  &#10; &#32; &#32; &#32; &#32;owl:inverseOf&#32;:isPropertyOf&#32;;  &#10; &#32; &#32; &#32; &#32;owl:propertyChainAxiom&#32;(&#32;skos:broader&#32;:hasProperty&#32;)&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-57)|Pointer|http://www.w3.org/2004/02/skos/core#Concept|

***
### MinorFail Outcome number 58

[Jump to summary definition](#summary-MinorFail-58)	|	[Previous MinorFail outcome](#minorfail-outcome-number-57)	|	[Next MinorFail outcome](#minorfail-outcome-number-59)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-properties-ontology-catalogs|
|----|----|
|Title|Standalone&#32;module&#32;core&#92;properties&#92;ontology.catalogs.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- https://gitlab.com/coswot/coswot-acimov/blob/HEAD/core/properties/ontology.catalogs.ttl|

#### Criterion detail
|Identifier|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|
|----|----|
|Title|Profile&#32;compatibility&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;check&#32;whether&#32;the&#32;test&#32;subject&#32;is&#32;compatible&#32;with&#32;a&#32;profile&#32;or&#32;not,&#32;and&#32;if&#32;it&#32;is&#32;not,&#32;why.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-58)|Identifier|`owl-el-profile-error`|
|[Section top](#minorfail-outcome-number-58)|Title|OWL&#32;EL&#32;Profile&#32;incompatible|
|[Section top](#minorfail-outcome-number-58)|Description|Class&#32;Expression&#32;not&#32;supported&#32;with&#32;rdfs:subClassOf|
|[Section top](#minorfail-outcome-number-58)|Pointer|<pre lang="Turtle"><code>coswot:PropertyKind&#32;a&#32;owl:Class&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;Property&#32;Kind&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;Identifiable&#32;qualities&#32;of&#32;features&#32;of&#32;interest&#32;that&#32;can&#32;be&#32;t...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32; &#60;https://w3id.org/coswot/core/properties> &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:subClassOf&#32; &#91;&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:allValuesFrom&#32;coswot:PropertyKind&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:onProperty&#32;skos:broader&#32;],  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#91;&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:allValuesFrom&#32;coswot:PropertyKind&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:onProperty&#32;skos:narrower&#32;],  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;skos:Concept&#32;;  &#10; &#32; &#32; &#32; &#32;skos:example&#32; &#34;Air&#32;temperature,&#32;pressure,&#32;luminance,&#32;etc.&#32;are&#32;all&#32;property&#32;...&#34;,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#34;Two&#32;examples&#32;using&#32;the&#32;QUDT&#32;Quantity&#32;Kind&#32;vocabulary,&#32;and&#32;th...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;skos:note&#32; &#34;Concepts&#32;from&#32;existing&#32;code&#32;lists,&#32;vocabularies,&#32;and&#32;taxonom...&#34; &#32;.</code></pre>|

***
### MinorFail Outcome number 59

[Jump to summary definition](#summary-MinorFail-59)	|	[Previous MinorFail outcome](#minorfail-outcome-number-58)	|	[Next MinorFail outcome](#minorfail-outcome-number-60)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-properties-ontology-catalogs|
|----|----|
|Title|Standalone&#32;module&#32;core&#92;properties&#92;ontology.catalogs.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- https://gitlab.com/coswot/coswot-acimov/blob/HEAD/core/properties/ontology.catalogs.ttl|

#### Criterion detail
|Identifier|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|
|----|----|
|Title|Profile&#32;compatibility&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;check&#32;whether&#32;the&#32;test&#32;subject&#32;is&#32;compatible&#32;with&#32;a&#32;profile&#32;or&#32;not,&#32;and&#32;if&#32;it&#32;is&#32;not,&#32;why.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-59)|Identifier|`owl-el-profile-error`|
|[Section top](#minorfail-outcome-number-59)|Title|OWL&#32;EL&#32;Profile&#32;incompatible|
|[Section top](#minorfail-outcome-number-59)|Description|Statement&#32;not&#32;supported&#32;in&#32;a&#32;Class&#32;Expression|
|[Section top](#minorfail-outcome-number-59)|Pointer|<pre lang="Turtle"><code>&#91;]&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32;owl:allValuesFrom&#32;coswot:PropertyKind&#32;;  &#10; &#32; &#32; &#32; &#32;owl:onProperty&#32;skos:broader&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-59)|Pointer|<pre lang="Turtle"><code>&#91;]&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32;owl:allValuesFrom&#32;coswot:PropertyKind&#32;;  &#10; &#32; &#32; &#32; &#32;owl:onProperty&#32;skos:narrower&#32;.</code></pre>|

***
### MinorFail Outcome number 60

[Jump to summary definition](#summary-MinorFail-60)	|	[Previous MinorFail outcome](#minorfail-outcome-number-59)	|	[Next MinorFail outcome](#minorfail-outcome-number-61)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-properties-ontology-catalogs|
|----|----|
|Title|Standalone&#32;module&#32;core&#92;properties&#92;ontology.catalogs.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- https://gitlab.com/coswot/coswot-acimov/blob/HEAD/core/properties/ontology.catalogs.ttl|

#### Criterion detail
|Identifier|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|
|----|----|
|Title|Profile&#32;compatibility&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;check&#32;whether&#32;the&#32;test&#32;subject&#32;is&#32;compatible&#32;with&#32;a&#32;profile&#32;or&#32;not,&#32;and&#32;if&#32;it&#32;is&#32;not,&#32;why.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-60)|Identifier|`owl-ql-profile-error`|
|[Section top](#minorfail-outcome-number-60)|Title|OWL&#32;QL&#32;Profile&#32;incompatible|
|[Section top](#minorfail-outcome-number-60)|Description|Class&#32;Expression&#32;not&#32;supported&#32;with&#32;rdfs:subClassOf|
|[Section top](#minorfail-outcome-number-60)|Pointer|<pre lang="Turtle"><code>coswot:PropertyKind&#32;a&#32;owl:Class&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;Property&#32;Kind&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;Identifiable&#32;qualities&#32;of&#32;features&#32;of&#32;interest&#32;that&#32;can&#32;be&#32;t...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32; &#60;https://w3id.org/coswot/core/properties> &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:subClassOf&#32; &#91;&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:allValuesFrom&#32;coswot:PropertyKind&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:onProperty&#32;skos:broader&#32;],  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#91;&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:allValuesFrom&#32;coswot:PropertyKind&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:onProperty&#32;skos:narrower&#32;],  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;skos:Concept&#32;;  &#10; &#32; &#32; &#32; &#32;skos:example&#32; &#34;Air&#32;temperature,&#32;pressure,&#32;luminance,&#32;etc.&#32;are&#32;all&#32;property&#32;...&#34;,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#34;Two&#32;examples&#32;using&#32;the&#32;QUDT&#32;Quantity&#32;Kind&#32;vocabulary,&#32;and&#32;th...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;skos:note&#32; &#34;Concepts&#32;from&#32;existing&#32;code&#32;lists,&#32;vocabularies,&#32;and&#32;taxonom...&#34; &#32;.</code></pre>|

***
### MinorFail Outcome number 61

[Jump to summary definition](#summary-MinorFail-61)	|	[Previous MinorFail outcome](#minorfail-outcome-number-60)	|	[Next MinorFail outcome](#minorfail-outcome-number-62)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-properties-ontology-catalogs|
|----|----|
|Title|Standalone&#32;module&#32;core&#92;properties&#92;ontology.catalogs.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- https://gitlab.com/coswot/coswot-acimov/blob/HEAD/core/properties/ontology.catalogs.ttl|

#### Criterion detail
|Identifier|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|
|----|----|
|Title|Profile&#32;compatibility&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;check&#32;whether&#32;the&#32;test&#32;subject&#32;is&#32;compatible&#32;with&#32;a&#32;profile&#32;or&#32;not,&#32;and&#32;if&#32;it&#32;is&#32;not,&#32;why.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-61)|Identifier|`owl-ql-profile-error`|
|[Section top](#minorfail-outcome-number-61)|Title|OWL&#32;QL&#32;Profile&#32;incompatible|
|[Section top](#minorfail-outcome-number-61)|Description|Property&#32;inclusions&#32;involving&#32;property&#32;chains&#32;not&#32;supported|
|[Section top](#minorfail-outcome-number-61)|Pointer|<pre lang="Turtle"><code>coswot:hasProperty&#32;a&#32;owl:ObjectProperty&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;has&#32;property&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;Links&#32;a&#32;feature&#32;to&#32;one&#32;of&#32;its&#32;properties.&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32; &#60;https://w3id.org/coswot/core/properties> &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:range&#32;coswot:PropertyKind&#32;;  &#10; &#32; &#32; &#32; &#32;owl:inverseOf&#32;coswot:isPropertyOf&#32;;  &#10; &#32; &#32; &#32; &#32;owl:propertyChainAxiom&#32;(&#32;skos:broader&#32;coswot:hasProperty&#32;)&#32;.</code></pre>|

***
### MinorFail Outcome number 62

[Jump to summary definition](#summary-MinorFail-62)	|	[Previous MinorFail outcome](#minorfail-outcome-number-61)	|	[Next MinorFail outcome](#minorfail-outcome-number-63)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-properties-ontology-catalogs|
|----|----|
|Title|Standalone&#32;module&#32;core&#92;properties&#92;ontology.catalogs.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- https://gitlab.com/coswot/coswot-acimov/blob/HEAD/core/properties/ontology.catalogs.ttl|

#### Criterion detail
|Identifier|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|
|----|----|
|Title|Profile&#32;compatibility&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;check&#32;whether&#32;the&#32;test&#32;subject&#32;is&#32;compatible&#32;with&#32;a&#32;profile&#32;or&#32;not,&#32;and&#32;if&#32;it&#32;is&#32;not,&#32;why.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-62)|Identifier|`owl-ql-profile-error`|
|[Section top](#minorfail-outcome-number-62)|Title|OWL&#32;QL&#32;Profile&#32;incompatible|
|[Section top](#minorfail-outcome-number-62)|Description|Statement&#32;not&#32;supported&#32;in&#32;a&#32;Super&#32;Class&#32;Expression|
|[Section top](#minorfail-outcome-number-62)|Pointer|<pre lang="Turtle"><code>&#91;]&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32;owl:allValuesFrom&#32;coswot:PropertyKind&#32;;  &#10; &#32; &#32; &#32; &#32;owl:onProperty&#32;skos:broader&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-62)|Pointer|<pre lang="Turtle"><code>&#91;]&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32;owl:allValuesFrom&#32;coswot:PropertyKind&#32;;  &#10; &#32; &#32; &#32; &#32;owl:onProperty&#32;skos:narrower&#32;.</code></pre>|

***
### MinorFail Outcome number 63

[Jump to summary definition](#summary-MinorFail-63)	|	[Previous MinorFail outcome](#minorfail-outcome-number-62)	|	[Next MinorFail outcome](#minorfail-outcome-number-64)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-properties-ontology|
|----|----|
|Title|Standalone&#32;module&#32;core&#92;properties&#92;ontology.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- https://gitlab.com/coswot/coswot-acimov/blob/HEAD/core/properties/ontology.ttl|

#### Criterion detail
|Identifier|[domain-and-range-referencing](https://ns.inria.fr/olivaw#domain-and-range-referencing)|
|----|----|
|Title|Domain&#32;and&#32;range&#32;referencing&#32;test|
|Description|A&#32;test&#32;case&#32;from&#32;the&#32;Best&#32;Practices&#32;tests&#32;checking&#32;if&#32;all&#32;the&#32;ranges&#32;and&#32;domains&#32;from&#32;the&#32;test&#32;subject&#32;point&#32;to&#32;terms&#32;that&#32;are&#32;defined&#32;in&#32;the&#32;vocabulary.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-63)|Identifier|`domain-out-of-vocabulary`|
|[Section top](#minorfail-outcome-number-63)|Title|Domain&#32;out&#32;of&#32;vocabulary|
|[Section top](#minorfail-outcome-number-63)|Description|Some&#32;properties&#32;have&#32;a&#32;domain&#32;out&#32;of&#32;the&#32;ontology|
|[Section top](#minorfail-outcome-number-63)|Pointer|<pre lang="Turtle"><code>:isPropertyOf&#32;a&#32;owl:ObjectProperty&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;is&#32;property&#32;of&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;Links&#32;a&#32;property&#32;kind&#32;to&#32;the&#32;feature&#32;it&#32;is&#32;a&#32;property&#32;of.&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:domain&#32; &#91;&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:allValuesFrom&#32;:PropertyKind&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:onProperty&#32;skos:broader&#32;],  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#91;&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:allValuesFrom&#32;:PropertyKind&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:onProperty&#32;skos:narrower&#32;],  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#91;&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;rdfs:subClassOf&#32;&lowbar;:nfd114b5647404a058c98ee679d5e59a8b4&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:allValuesFrom&#32;owl:Nothing&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:onProperty&#32;:hasKind&#32;],  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;&lowbar;:nfd114b5647404a058c98ee679d5e59a8b4,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;skos:Concept,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;:Property,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;:PropertyKind&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32; &#60;https://w3id.org/coswot/core/properties> &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:range&#32;:Feature&#32;;  &#10; &#32; &#32; &#32; &#32;owl:inverseOf&#32;:hasProperty&#32;.  &#10;&lowbar;:nfd114b5647404a058c98ee679d5e59a8b4&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32;owl:allValuesFrom&#32;:PropertyKind&#32;;  &#10; &#32; &#32; &#32; &#32;owl:onProperty&#32;:hasKind&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-63)|Pointer|http://www.w3.org/2004/02/skos/core#Concept|

***
### MinorFail Outcome number 64

[Jump to summary definition](#summary-MinorFail-64)	|	[Previous MinorFail outcome](#minorfail-outcome-number-63)	|	[Next MinorFail outcome](#minorfail-outcome-number-65)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-properties-ontology|
|----|----|
|Title|Standalone&#32;module&#32;core&#92;properties&#92;ontology.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- https://gitlab.com/coswot/coswot-acimov/blob/HEAD/core/properties/ontology.ttl|

#### Criterion detail
|Identifier|[domain-and-range-referencing](https://ns.inria.fr/olivaw#domain-and-range-referencing)|
|----|----|
|Title|Domain&#32;and&#32;range&#32;referencing&#32;test|
|Description|A&#32;test&#32;case&#32;from&#32;the&#32;Best&#32;Practices&#32;tests&#32;checking&#32;if&#32;all&#32;the&#32;ranges&#32;and&#32;domains&#32;from&#32;the&#32;test&#32;subject&#32;point&#32;to&#32;terms&#32;that&#32;are&#32;defined&#32;in&#32;the&#32;vocabulary.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-64)|Identifier|`range-out-of-vocabulary`|
|[Section top](#minorfail-outcome-number-64)|Title|Range&#32;out&#32;of&#32;vocabulary|
|[Section top](#minorfail-outcome-number-64)|Description|Some&#32;properties&#32;have&#32;a&#32;range&#32;out&#32;of&#32;the&#32;ontology|
|[Section top](#minorfail-outcome-number-64)|Pointer|<pre lang="Turtle"><code>:hasProperty&#32;a&#32;owl:ObjectProperty&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;has&#32;property&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;Links&#32;a&#32;feature&#32;to&#32;one&#32;of&#32;its&#32;property&#32;kinds.&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:domain&#32;:Feature&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32; &#60;https://w3id.org/coswot/core/properties> &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:range&#32; &#91;&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:allValuesFrom&#32;:PropertyKind&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:onProperty&#32;skos:broader&#32;],  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#91;&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:allValuesFrom&#32;:PropertyKind&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:onProperty&#32;skos:narrower&#32;],  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#91;&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;rdfs:subClassOf&#32;&lowbar;:nb5f67b80b28d4e5383397ccc89bcd4fdb4&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:allValuesFrom&#32;owl:Nothing&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:onProperty&#32;:hasKind&#32;],  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;&lowbar;:nb5f67b80b28d4e5383397ccc89bcd4fdb4,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;skos:Concept,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;:Property,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;:PropertyKind&#32;;  &#10; &#32; &#32; &#32; &#32;owl:inverseOf&#32;:isPropertyOf&#32;;  &#10; &#32; &#32; &#32; &#32;owl:propertyChainAxiom&#32;(&#32;skos:broader&#32;:hasProperty&#32;),  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;(&#32;:hasKind&#32;:hasProperty&#32;),  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;(&#32;:hasPropertyOfInterest&#32;:hasKind&#32;)&#32;.  &#10;&lowbar;:nb5f67b80b28d4e5383397ccc89bcd4fdb4&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32;owl:allValuesFrom&#32;:PropertyKind&#32;;  &#10; &#32; &#32; &#32; &#32;owl:onProperty&#32;:hasKind&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-64)|Pointer|http://www.w3.org/2004/02/skos/core#Concept|

***
### MinorFail Outcome number 65

[Jump to summary definition](#summary-MinorFail-65)	|	[Previous MinorFail outcome](#minorfail-outcome-number-64)	|	[Next MinorFail outcome](#minorfail-outcome-number-66)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-properties-ontology|
|----|----|
|Title|Standalone&#32;module&#32;core&#92;properties&#92;ontology.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- https://gitlab.com/coswot/coswot-acimov/blob/HEAD/core/properties/ontology.ttl|

#### Criterion detail
|Identifier|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|
|----|----|
|Title|Profile&#32;compatibility&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;check&#32;whether&#32;the&#32;test&#32;subject&#32;is&#32;compatible&#32;with&#32;a&#32;profile&#32;or&#32;not,&#32;and&#32;if&#32;it&#32;is&#32;not,&#32;why.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-65)|Identifier|`owl-el-profile-error`|
|[Section top](#minorfail-outcome-number-65)|Title|OWL&#32;EL&#32;Profile&#32;incompatible|
|[Section top](#minorfail-outcome-number-65)|Description|Class&#32;Expression&#32;not&#32;supported&#32;with&#32;rdfs:subClassOf|
|[Section top](#minorfail-outcome-number-65)|Pointer|<pre lang="Turtle"><code>coswot:PropertyKind&#32;a&#32;owl:Class&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;Property&#32;Kind&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;Identifiable&#32;qualities&#32;of&#32;features&#32;that&#32;can&#32;be&#32;observed&#32;or&#32;c...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32; &#60;https://w3id.org/coswot/core/properties> &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:subClassOf&#32; &#91;&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:allValuesFrom&#32;coswot:PropertyKind&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:onProperty&#32;skos:broader&#32;],  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#91;&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:allValuesFrom&#32;coswot:PropertyKind&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:onProperty&#32;skos:narrower&#32;],  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#91;&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:allValuesFrom&#32;owl:Nothing&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:onProperty&#32;coswot:hasKind&#32;],  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;skos:Concept,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;coswot:Property&#32;;  &#10; &#32; &#32; &#32; &#32;skos:example&#32; &#34;Air&#32;temperature,&#32;pressure,&#32;luminance,&#32;etc.&#32;are&#32;all&#32;property&#32;...&#34;,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#34;Two&#32;examples&#32;using&#32;the&#32;QUDT&#32;Quantity&#32;Kind&#32;vocabulary,&#32;and&#32;th...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;skos:note&#32; &#34;Concepts&#32;from&#32;existing&#32;code&#32;lists,&#32;vocabularies,&#32;and&#32;taxonom...&#34; &#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-65)|Pointer|<pre lang="Turtle"><code>coswot:PropertyOfInterest&#32;a&#32;owl:Class&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;Property&#32;of&#32;Interest&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;Identifiable&#32;qualities&#32;of&#32;features&#32;of&#32;interest&#32;that&#32;can&#32;be&#32;o...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32; &#60;https://w3id.org/coswot/core/properties> &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:subClassOf&#32; &#91;&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:allValuesFrom&#32;coswot:PropertyKind&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:onProperty&#32;coswot:hasKind&#32;],  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#91;&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:onProperty&#32;coswot:hasKind&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:someValuesFrom&#32;coswot:PropertyKind&#32;],  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#91;&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:onProperty&#32;coswot:isPropertyOfInterestOf&#32;],  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;coswot:Property&#32;;  &#10; &#32; &#32; &#32; &#32;skos:example&#32; &#34;The&#32;air&#32;temperature&#32;of&#32;the&#32;atmosphere&#32;sample&#32;at&#32;a&#32;certain&#32;lo...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;skos:note&#32; &#34;A&#32;property&#32;of&#32;interest&#32;is&#32;the&#32;property&#32;of&#32;(OP&#32;coswot:isPrope...&#34;,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#34;Per&#32;convention,&#32;the&#32;IRI&#32;of&#32;properties&#32;of&#32;interest&#32;should&#32;con...&#34;,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#34;Properties&#32;of&#32;interest&#32;need&#32;not&#32;always&#32;be&#32;explicited.&#32;It&#32;dep...&#34; &#32;.</code></pre>|

***
### MinorFail Outcome number 66

[Jump to summary definition](#summary-MinorFail-66)	|	[Previous MinorFail outcome](#minorfail-outcome-number-65)	|	[Next MinorFail outcome](#minorfail-outcome-number-67)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-properties-ontology|
|----|----|
|Title|Standalone&#32;module&#32;core&#92;properties&#92;ontology.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- https://gitlab.com/coswot/coswot-acimov/blob/HEAD/core/properties/ontology.ttl|

#### Criterion detail
|Identifier|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|
|----|----|
|Title|Profile&#32;compatibility&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;check&#32;whether&#32;the&#32;test&#32;subject&#32;is&#32;compatible&#32;with&#32;a&#32;profile&#32;or&#32;not,&#32;and&#32;if&#32;it&#32;is&#32;not,&#32;why.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-66)|Identifier|`owl-el-profile-error`|
|[Section top](#minorfail-outcome-number-66)|Title|OWL&#32;EL&#32;Profile&#32;incompatible|
|[Section top](#minorfail-outcome-number-66)|Description|Statement&#32;not&#32;supported|
|[Section top](#minorfail-outcome-number-66)|Pointer|<pre lang="Turtle"><code>coswot:Property&#32;a&#32;owl:Class&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;Property&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;Identifiable&#32;qualities&#32;of&#32;features&#32;that&#32;can&#32;be&#32;observed&#32;or&#32;c...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32; &#60;https://w3id.org/coswot/core/properties> &#32;;  &#10; &#32; &#32; &#32; &#32;owl:disjointUnionOf&#32;(&#32;coswot:PropertyOfInterest&#32;coswot:PropertyKind&#32;)&#32;.</code></pre>|

***
### MinorFail Outcome number 67

[Jump to summary definition](#summary-MinorFail-67)	|	[Previous MinorFail outcome](#minorfail-outcome-number-66)	|	[Next MinorFail outcome](#minorfail-outcome-number-68)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-properties-ontology|
|----|----|
|Title|Standalone&#32;module&#32;core&#92;properties&#92;ontology.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- https://gitlab.com/coswot/coswot-acimov/blob/HEAD/core/properties/ontology.ttl|

#### Criterion detail
|Identifier|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|
|----|----|
|Title|Profile&#32;compatibility&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;check&#32;whether&#32;the&#32;test&#32;subject&#32;is&#32;compatible&#32;with&#32;a&#32;profile&#32;or&#32;not,&#32;and&#32;if&#32;it&#32;is&#32;not,&#32;why.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-67)|Identifier|`owl-el-profile-error`|
|[Section top](#minorfail-outcome-number-67)|Title|OWL&#32;EL&#32;Profile&#32;incompatible|
|[Section top](#minorfail-outcome-number-67)|Description|Statement&#32;not&#32;supported&#32;in&#32;a&#32;Class&#32;Expression|
|[Section top](#minorfail-outcome-number-67)|Pointer|<pre lang="Turtle"><code>&#91;]&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32;owl:allValuesFrom&#32;coswot:PropertyKind&#32;;  &#10; &#32; &#32; &#32; &#32;owl:onProperty&#32;skos:broader&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-67)|Pointer|<pre lang="Turtle"><code>&#91;]&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32;owl:allValuesFrom&#32;coswot:PropertyKind&#32;;  &#10; &#32; &#32; &#32; &#32;owl:onProperty&#32;skos:narrower&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-67)|Pointer|<pre lang="Turtle"><code>&#91;]&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32;owl:allValuesFrom&#32;owl:Nothing&#32;;  &#10; &#32; &#32; &#32; &#32;owl:onProperty&#32;coswot:hasKind&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-67)|Pointer|<pre lang="Turtle"><code>&#91;]&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32;owl:allValuesFrom&#32;coswot:PropertyKind&#32;;  &#10; &#32; &#32; &#32; &#32;owl:onProperty&#32;coswot:hasKind&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-67)|Pointer|<pre lang="Turtle"><code>&#91;]&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32;&#32; &#32;owl:onProperty&#32;coswot:isPropertyOfInterestOf&#32;.</code></pre>|

***
### MinorFail Outcome number 68

[Jump to summary definition](#summary-MinorFail-68)	|	[Previous MinorFail outcome](#minorfail-outcome-number-67)	|	[Next MinorFail outcome](#minorfail-outcome-number-69)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-properties-ontology|
|----|----|
|Title|Standalone&#32;module&#32;core&#92;properties&#92;ontology.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- https://gitlab.com/coswot/coswot-acimov/blob/HEAD/core/properties/ontology.ttl|

#### Criterion detail
|Identifier|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|
|----|----|
|Title|Profile&#32;compatibility&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;check&#32;whether&#32;the&#32;test&#32;subject&#32;is&#32;compatible&#32;with&#32;a&#32;profile&#32;or&#32;not,&#32;and&#32;if&#32;it&#32;is&#32;not,&#32;why.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-68)|Identifier|`owl-ql-profile-error`|
|[Section top](#minorfail-outcome-number-68)|Title|OWL&#32;QL&#32;Profile&#32;incompatible|
|[Section top](#minorfail-outcome-number-68)|Description|Class&#32;Expression&#32;not&#32;supported&#32;with&#32;rdfs:subClassOf|
|[Section top](#minorfail-outcome-number-68)|Pointer|<pre lang="Turtle"><code>coswot:PropertyKind&#32;a&#32;owl:Class&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;Property&#32;Kind&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;Identifiable&#32;qualities&#32;of&#32;features&#32;that&#32;can&#32;be&#32;observed&#32;or&#32;c...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32; &#60;https://w3id.org/coswot/core/properties> &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:subClassOf&#32; &#91;&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:allValuesFrom&#32;coswot:PropertyKind&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:onProperty&#32;skos:broader&#32;],  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#91;&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:allValuesFrom&#32;coswot:PropertyKind&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:onProperty&#32;skos:narrower&#32;],  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#91;&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:allValuesFrom&#32;owl:Nothing&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:onProperty&#32;coswot:hasKind&#32;],  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;skos:Concept,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;coswot:Property&#32;;  &#10; &#32; &#32; &#32; &#32;skos:example&#32; &#34;Air&#32;temperature,&#32;pressure,&#32;luminance,&#32;etc.&#32;are&#32;all&#32;property&#32;...&#34;,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#34;Two&#32;examples&#32;using&#32;the&#32;QUDT&#32;Quantity&#32;Kind&#32;vocabulary,&#32;and&#32;th...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;skos:note&#32; &#34;Concepts&#32;from&#32;existing&#32;code&#32;lists,&#32;vocabularies,&#32;and&#32;taxonom...&#34; &#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-68)|Pointer|<pre lang="Turtle"><code>coswot:PropertyOfInterest&#32;a&#32;owl:Class&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;Property&#32;of&#32;Interest&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;Identifiable&#32;qualities&#32;of&#32;features&#32;of&#32;interest&#32;that&#32;can&#32;be&#32;o...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32; &#60;https://w3id.org/coswot/core/properties> &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:subClassOf&#32; &#91;&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:allValuesFrom&#32;coswot:PropertyKind&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:onProperty&#32;coswot:hasKind&#32;],  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#91;&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:onProperty&#32;coswot:hasKind&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:someValuesFrom&#32;coswot:PropertyKind&#32;],  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#91;&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:onProperty&#32;coswot:isPropertyOfInterestOf&#32;],  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;coswot:Property&#32;;  &#10; &#32; &#32; &#32; &#32;skos:example&#32; &#34;The&#32;air&#32;temperature&#32;of&#32;the&#32;atmosphere&#32;sample&#32;at&#32;a&#32;certain&#32;lo...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;skos:note&#32; &#34;A&#32;property&#32;of&#32;interest&#32;is&#32;the&#32;property&#32;of&#32;(OP&#32;coswot:isPrope...&#34;,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#34;Per&#32;convention,&#32;the&#32;IRI&#32;of&#32;properties&#32;of&#32;interest&#32;should&#32;con...&#34;,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#34;Properties&#32;of&#32;interest&#32;need&#32;not&#32;always&#32;be&#32;explicited.&#32;It&#32;dep...&#34; &#32;.</code></pre>|

***
### MinorFail Outcome number 69

[Jump to summary definition](#summary-MinorFail-69)	|	[Previous MinorFail outcome](#minorfail-outcome-number-68)	|	[Next MinorFail outcome](#minorfail-outcome-number-70)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-properties-ontology|
|----|----|
|Title|Standalone&#32;module&#32;core&#92;properties&#92;ontology.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- https://gitlab.com/coswot/coswot-acimov/blob/HEAD/core/properties/ontology.ttl|

#### Criterion detail
|Identifier|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|
|----|----|
|Title|Profile&#32;compatibility&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;check&#32;whether&#32;the&#32;test&#32;subject&#32;is&#32;compatible&#32;with&#32;a&#32;profile&#32;or&#32;not,&#32;and&#32;if&#32;it&#32;is&#32;not,&#32;why.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-69)|Identifier|`owl-ql-profile-error`|
|[Section top](#minorfail-outcome-number-69)|Title|OWL&#32;QL&#32;Profile&#32;incompatible|
|[Section top](#minorfail-outcome-number-69)|Description|Property&#32;inclusions&#32;involving&#32;property&#32;chains&#32;not&#32;supported|
|[Section top](#minorfail-outcome-number-69)|Pointer|<pre lang="Turtle"><code>coswot:hasProperty&#32;a&#32;owl:ObjectProperty&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;has&#32;property&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;Links&#32;a&#32;feature&#32;to&#32;one&#32;of&#32;its&#32;property&#32;kinds.&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:domain&#32;coswot:Feature&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32; &#60;https://w3id.org/coswot/core/properties> &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:range&#32;coswot:PropertyKind&#32;;  &#10; &#32; &#32; &#32; &#32;owl:inverseOf&#32;coswot:isPropertyOf&#32;;  &#10; &#32; &#32; &#32; &#32;owl:propertyChainAxiom&#32;(&#32;skos:broader&#32;coswot:hasProperty&#32;),  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;(&#32;coswot:hasKind&#32;coswot:hasProperty&#32;),  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;(&#32;coswot:hasPropertyOfInterest&#32;coswot:hasKind&#32;)&#32;.</code></pre>|

***
### MinorFail Outcome number 70

[Jump to summary definition](#summary-MinorFail-70)	|	[Previous MinorFail outcome](#minorfail-outcome-number-69)	|	[Next MinorFail outcome](#minorfail-outcome-number-71)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-properties-ontology|
|----|----|
|Title|Standalone&#32;module&#32;core&#92;properties&#92;ontology.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- https://gitlab.com/coswot/coswot-acimov/blob/HEAD/core/properties/ontology.ttl|

#### Criterion detail
|Identifier|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|
|----|----|
|Title|Profile&#32;compatibility&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;check&#32;whether&#32;the&#32;test&#32;subject&#32;is&#32;compatible&#32;with&#32;a&#32;profile&#32;or&#32;not,&#32;and&#32;if&#32;it&#32;is&#32;not,&#32;why.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-70)|Identifier|`owl-ql-profile-error`|
|[Section top](#minorfail-outcome-number-70)|Title|OWL&#32;QL&#32;Profile&#32;incompatible|
|[Section top](#minorfail-outcome-number-70)|Description|Statement&#32;not&#32;supported|
|[Section top](#minorfail-outcome-number-70)|Pointer|<pre lang="Turtle"><code>coswot:Property&#32;a&#32;owl:Class&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;Property&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;Identifiable&#32;qualities&#32;of&#32;features&#32;that&#32;can&#32;be&#32;observed&#32;or&#32;c...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32; &#60;https://w3id.org/coswot/core/properties> &#32;;  &#10; &#32; &#32; &#32; &#32;owl:disjointUnionOf&#32;(&#32;coswot:PropertyOfInterest&#32;coswot:PropertyKind&#32;)&#32;.</code></pre>|

***
### MinorFail Outcome number 71

[Jump to summary definition](#summary-MinorFail-71)	|	[Previous MinorFail outcome](#minorfail-outcome-number-70)	|	[Next MinorFail outcome](#minorfail-outcome-number-72)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-properties-ontology|
|----|----|
|Title|Standalone&#32;module&#32;core&#92;properties&#92;ontology.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- https://gitlab.com/coswot/coswot-acimov/blob/HEAD/core/properties/ontology.ttl|

#### Criterion detail
|Identifier|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|
|----|----|
|Title|Profile&#32;compatibility&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;check&#32;whether&#32;the&#32;test&#32;subject&#32;is&#32;compatible&#32;with&#32;a&#32;profile&#32;or&#32;not,&#32;and&#32;if&#32;it&#32;is&#32;not,&#32;why.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-71)|Identifier|`owl-ql-profile-error`|
|[Section top](#minorfail-outcome-number-71)|Title|OWL&#32;QL&#32;Profile&#32;incompatible|
|[Section top](#minorfail-outcome-number-71)|Description|Statement&#32;not&#32;supported&#32;in&#32;a&#32;Super&#32;Class&#32;Expression|
|[Section top](#minorfail-outcome-number-71)|Pointer|<pre lang="Turtle"><code>&#91;]&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32;owl:allValuesFrom&#32;coswot:PropertyKind&#32;;  &#10; &#32; &#32; &#32; &#32;owl:onProperty&#32;skos:broader&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-71)|Pointer|<pre lang="Turtle"><code>&#91;]&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32;owl:allValuesFrom&#32;coswot:PropertyKind&#32;;  &#10; &#32; &#32; &#32; &#32;owl:onProperty&#32;skos:narrower&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-71)|Pointer|<pre lang="Turtle"><code>&#91;]&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32;owl:allValuesFrom&#32;owl:Nothing&#32;;  &#10; &#32; &#32; &#32; &#32;owl:onProperty&#32;coswot:hasKind&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-71)|Pointer|<pre lang="Turtle"><code>&#91;]&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32;owl:allValuesFrom&#32;coswot:PropertyKind&#32;;  &#10; &#32; &#32; &#32; &#32;owl:onProperty&#32;coswot:hasKind&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-71)|Pointer|<pre lang="Turtle"><code>&#91;]&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32;&#32; &#32;owl:onProperty&#32;coswot:isPropertyOfInterestOf&#32;.</code></pre>|

***
### MinorFail Outcome number 72

[Jump to summary definition](#summary-MinorFail-72)	|	[Previous MinorFail outcome](#minorfail-outcome-number-71)	|	[Next MinorFail outcome](#minorfail-outcome-number-73)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-properties-ontology|
|----|----|
|Title|Standalone&#32;module&#32;core&#92;properties&#92;ontology.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- https://gitlab.com/coswot/coswot-acimov/blob/HEAD/core/properties/ontology.ttl|

#### Criterion detail
|Identifier|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|
|----|----|
|Title|Profile&#32;compatibility&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;check&#32;whether&#32;the&#32;test&#32;subject&#32;is&#32;compatible&#32;with&#32;a&#32;profile&#32;or&#32;not,&#32;and&#32;if&#32;it&#32;is&#32;not,&#32;why.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-72)|Identifier|`owl-rl-profile-error`|
|[Section top](#minorfail-outcome-number-72)|Title|OWL&#32;RL&#32;Profile&#32;incompatible|
|[Section top](#minorfail-outcome-number-72)|Description|Class&#32;Expression&#32;not&#32;supported&#32;with&#32;rdfs:subClassOf|
|[Section top](#minorfail-outcome-number-72)|Pointer|<pre lang="Turtle"><code>coswot:PropertyOfInterest&#32;a&#32;owl:Class&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;Property&#32;of&#32;Interest&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;Identifiable&#32;qualities&#32;of&#32;features&#32;of&#32;interest&#32;that&#32;can&#32;be&#32;o...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32; &#60;https://w3id.org/coswot/core/properties> &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:subClassOf&#32; &#91;&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:allValuesFrom&#32;coswot:PropertyKind&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:onProperty&#32;coswot:hasKind&#32;],  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#91;&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:onProperty&#32;coswot:hasKind&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:someValuesFrom&#32;coswot:PropertyKind&#32;],  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#91;&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:onProperty&#32;coswot:isPropertyOfInterestOf&#32;],  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;coswot:Property&#32;;  &#10; &#32; &#32; &#32; &#32;skos:example&#32; &#34;The&#32;air&#32;temperature&#32;of&#32;the&#32;atmosphere&#32;sample&#32;at&#32;a&#32;certain&#32;lo...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;skos:note&#32; &#34;A&#32;property&#32;of&#32;interest&#32;is&#32;the&#32;property&#32;of&#32;(OP&#32;coswot:isPrope...&#34;,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#34;Per&#32;convention,&#32;the&#32;IRI&#32;of&#32;properties&#32;of&#32;interest&#32;should&#32;con...&#34;,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#34;Properties&#32;of&#32;interest&#32;need&#32;not&#32;always&#32;be&#32;explicited.&#32;It&#32;dep...&#34; &#32;.</code></pre>|

***
### MinorFail Outcome number 73

[Jump to summary definition](#summary-MinorFail-73)	|	[Previous MinorFail outcome](#minorfail-outcome-number-72)	|	[Next MinorFail outcome](#minorfail-outcome-number-74)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-properties-ontology|
|----|----|
|Title|Standalone&#32;module&#32;core&#92;properties&#92;ontology.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- https://gitlab.com/coswot/coswot-acimov/blob/HEAD/core/properties/ontology.ttl|

#### Criterion detail
|Identifier|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|
|----|----|
|Title|Profile&#32;compatibility&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;check&#32;whether&#32;the&#32;test&#32;subject&#32;is&#32;compatible&#32;with&#32;a&#32;profile&#32;or&#32;not,&#32;and&#32;if&#32;it&#32;is&#32;not,&#32;why.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-73)|Identifier|`owl-rl-profile-error`|
|[Section top](#minorfail-outcome-number-73)|Title|OWL&#32;RL&#32;Profile&#32;incompatible|
|[Section top](#minorfail-outcome-number-73)|Description|Statement&#32;not&#32;supported|
|[Section top](#minorfail-outcome-number-73)|Pointer|<pre lang="Turtle"><code>coswot:Property&#32;a&#32;owl:Class&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;Property&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;Identifiable&#32;qualities&#32;of&#32;features&#32;that&#32;can&#32;be&#32;observed&#32;or&#32;c...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32; &#60;https://w3id.org/coswot/core/properties> &#32;;  &#10; &#32; &#32; &#32; &#32;owl:disjointUnionOf&#32;(&#32;coswot:PropertyOfInterest&#32;coswot:PropertyKind&#32;)&#32;.</code></pre>|

***
### MinorFail Outcome number 74

[Jump to summary definition](#summary-MinorFail-74)	|	[Previous MinorFail outcome](#minorfail-outcome-number-73)	|	[Next MinorFail outcome](#minorfail-outcome-number-75)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-properties-ontology|
|----|----|
|Title|Standalone&#32;module&#32;core&#92;properties&#92;ontology.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- https://gitlab.com/coswot/coswot-acimov/blob/HEAD/core/properties/ontology.ttl|

#### Criterion detail
|Identifier|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|
|----|----|
|Title|Profile&#32;compatibility&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;check&#32;whether&#32;the&#32;test&#32;subject&#32;is&#32;compatible&#32;with&#32;a&#32;profile&#32;or&#32;not,&#32;and&#32;if&#32;it&#32;is&#32;not,&#32;why.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-74)|Identifier|`owl-rl-profile-error`|
|[Section top](#minorfail-outcome-number-74)|Title|OWL&#32;RL&#32;Profile&#32;incompatible|
|[Section top](#minorfail-outcome-number-74)|Description|Statement&#32;not&#32;supported&#32;in&#32;a&#32;Super&#32;Class&#32;Expression|
|[Section top](#minorfail-outcome-number-74)|Pointer|<pre lang="Turtle"><code>&#91;]&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32;owl:onProperty&#32;coswot:hasKind&#32;;  &#10; &#32; &#32; &#32; &#32;owl:someValuesFrom&#32;coswot:PropertyKind&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-74)|Pointer|<pre lang="Turtle"><code>&#91;]&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32;&#32; &#32;owl:onProperty&#32;coswot:isPropertyOfInterestOf&#32;.</code></pre>|

***
### MinorFail Outcome number 75

[Jump to summary definition](#summary-MinorFail-75)	|	[Previous MinorFail outcome](#minorfail-outcome-number-74)	|	[Next MinorFail outcome](#minorfail-outcome-number-76)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-procedures-ontology|
|----|----|
|Title|Standalone&#32;module&#32;core&#92;procedures&#92;ontology.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- https://gitlab.com/coswot/coswot-acimov/blob/HEAD/core/procedures/ontology.ttl|

#### Criterion detail
|Identifier|[domain-and-range-referencing](https://ns.inria.fr/olivaw#domain-and-range-referencing)|
|----|----|
|Title|Domain&#32;and&#32;range&#32;referencing&#32;test|
|Description|A&#32;test&#32;case&#32;from&#32;the&#32;Best&#32;Practices&#32;tests&#32;checking&#32;if&#32;all&#32;the&#32;ranges&#32;and&#32;domains&#32;from&#32;the&#32;test&#32;subject&#32;point&#32;to&#32;terms&#32;that&#32;are&#32;defined&#32;in&#32;the&#32;vocabulary.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-75)|Identifier|`range-out-of-vocabulary`|
|[Section top](#minorfail-outcome-number-75)|Title|Range&#32;out&#32;of&#32;vocabulary|
|[Section top](#minorfail-outcome-number-75)|Description|Some&#32;properties&#32;have&#32;a&#32;range&#32;out&#32;of&#32;the&#32;ontology|
|[Section top](#minorfail-outcome-number-75)|Pointer|<pre lang="Turtle"><code>:hasPhenomenonTime&#32;a&#32;owl:ObjectProperty&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;has&#32;phenomenon&#32;time&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;Links&#32;a&#32;procedure&#32;execution&#32;to&#32;the&#32;time&#32;that&#32;the&#32;result&#32;appl...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:domain&#32; &#91;&#32;a&#32;owl:Class&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:unionOf&#32;(&#32;:Procedure&#32;:ProcedureExecution&#32;)&#32;],  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;:ProcedureExecution&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32; &#60;https://w3id.org/coswot/core/procedures> &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:range&#32;time:TemporalEntity&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-75)|Pointer|<pre lang="Turtle"><code>:TemporalEntity&#32;a&#32;owl:Class&#32;.</code></pre>|

***
### MinorFail Outcome number 76

[Jump to summary definition](#summary-MinorFail-76)	|	[Previous MinorFail outcome](#minorfail-outcome-number-75)	|	[Next MinorFail outcome](#minorfail-outcome-number-77)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-procedures-ontology|
|----|----|
|Title|Standalone&#32;module&#32;core&#92;procedures&#92;ontology.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- https://gitlab.com/coswot/coswot-acimov/blob/HEAD/core/procedures/ontology.ttl|

#### Criterion detail
|Identifier|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|
|----|----|
|Title|Profile&#32;compatibility&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;check&#32;whether&#32;the&#32;test&#32;subject&#32;is&#32;compatible&#32;with&#32;a&#32;profile&#32;or&#32;not,&#32;and&#32;if&#32;it&#32;is&#32;not,&#32;why.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-76)|Identifier|`owl-el-profile-error`|
|[Section top](#minorfail-outcome-number-76)|Title|OWL&#32;EL&#32;Profile&#32;incompatible|
|[Section top](#minorfail-outcome-number-76)|Description|Class&#32;Expression&#32;not&#32;supported&#32;as&#32;object&#32;of&#32;rdfs:domain&#32;or&#32;rdfs:range|
|[Section top](#minorfail-outcome-number-76)|Pointer|<pre lang="Turtle"><code>coswot:hasInput&#32;a&#32;owl:ObjectProperty&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;has&#32;input&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;Links&#32;a&#32;procedure&#32;(e.g.,&#32;a&#32;command)&#32;or&#32;procedure&#32;execution&#32;(...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:domain&#32; &#91;&#32;a&#32;owl:Class&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:unionOf&#32;(&#32;coswot:Procedure&#32;coswot:ProcedureExecution&#32;)&#32;]&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32; &#60;https://w3id.org/coswot/core/functions&lowbar;commands> &#32;;  &#10; &#32; &#32; &#32; &#32;skos:example&#32; &#34;Different&#32;complementary&#32;commands&#32;can&#32;be&#32;defined&#32;for&#32;controll...&#34; &#32;.</code></pre>|

***
### MinorFail Outcome number 77

[Jump to summary definition](#summary-MinorFail-77)	|	[Previous MinorFail outcome](#minorfail-outcome-number-76)	|	[Next MinorFail outcome](#minorfail-outcome-number-78)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-procedures-ontology|
|----|----|
|Title|Standalone&#32;module&#32;core&#92;procedures&#92;ontology.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- https://gitlab.com/coswot/coswot-acimov/blob/HEAD/core/procedures/ontology.ttl|

#### Criterion detail
|Identifier|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|
|----|----|
|Title|Profile&#32;compatibility&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;check&#32;whether&#32;the&#32;test&#32;subject&#32;is&#32;compatible&#32;with&#32;a&#32;profile&#32;or&#32;not,&#32;and&#32;if&#32;it&#32;is&#32;not,&#32;why.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-77)|Identifier|`owl-el-profile-error`|
|[Section top](#minorfail-outcome-number-77)|Title|OWL&#32;EL&#32;Profile&#32;incompatible|
|[Section top](#minorfail-outcome-number-77)|Description|Statement&#32;not&#32;supported&#32;in&#32;a&#32;Class&#32;Expression|
|[Section top](#minorfail-outcome-number-77)|Pointer|<pre lang="Turtle"><code>&#91;]&#32;a&#32;owl:Class&#32;;  &#10; &#32; &#32;&#32; &#32;owl:unionOf&#32;(&#32;coswot:Procedure&#32;coswot:ProcedureExecution&#32;)&#32;.</code></pre>|

***
### MinorFail Outcome number 78

[Jump to summary definition](#summary-MinorFail-78)	|	[Previous MinorFail outcome](#minorfail-outcome-number-77)	|	[Next MinorFail outcome](#minorfail-outcome-number-79)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-procedures-ontology|
|----|----|
|Title|Standalone&#32;module&#32;core&#92;procedures&#92;ontology.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- https://gitlab.com/coswot/coswot-acimov/blob/HEAD/core/procedures/ontology.ttl|

#### Criterion detail
|Identifier|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|
|----|----|
|Title|Profile&#32;compatibility&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;check&#32;whether&#32;the&#32;test&#32;subject&#32;is&#32;compatible&#32;with&#32;a&#32;profile&#32;or&#32;not,&#32;and&#32;if&#32;it&#32;is&#32;not,&#32;why.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-78)|Identifier|`owl-ql-profile-error`|
|[Section top](#minorfail-outcome-number-78)|Title|OWL&#32;QL&#32;Profile&#32;incompatible|
|[Section top](#minorfail-outcome-number-78)|Description|Class&#32;Expression&#32;not&#32;supported&#32;as&#32;object&#32;of&#32;rdfs:domain&#32;or&#32;rdfs:range|
|[Section top](#minorfail-outcome-number-78)|Pointer|<pre lang="Turtle"><code>coswot:hasInput&#32;a&#32;owl:ObjectProperty&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;has&#32;input&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;Links&#32;a&#32;procedure&#32;(e.g.,&#32;a&#32;command)&#32;or&#32;procedure&#32;execution&#32;(...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:domain&#32; &#91;&#32;a&#32;owl:Class&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:unionOf&#32;(&#32;coswot:Procedure&#32;coswot:ProcedureExecution&#32;)&#32;]&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32; &#60;https://w3id.org/coswot/core/functions&lowbar;commands> &#32;;  &#10; &#32; &#32; &#32; &#32;skos:example&#32; &#34;Different&#32;complementary&#32;commands&#32;can&#32;be&#32;defined&#32;for&#32;controll...&#34; &#32;.</code></pre>|

***
### MinorFail Outcome number 79

[Jump to summary definition](#summary-MinorFail-79)	|	[Previous MinorFail outcome](#minorfail-outcome-number-78)	|	[Next MinorFail outcome](#minorfail-outcome-number-80)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-procedures-ontology|
|----|----|
|Title|Standalone&#32;module&#32;core&#92;procedures&#92;ontology.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- https://gitlab.com/coswot/coswot-acimov/blob/HEAD/core/procedures/ontology.ttl|

#### Criterion detail
|Identifier|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|
|----|----|
|Title|Profile&#32;compatibility&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;check&#32;whether&#32;the&#32;test&#32;subject&#32;is&#32;compatible&#32;with&#32;a&#32;profile&#32;or&#32;not,&#32;and&#32;if&#32;it&#32;is&#32;not,&#32;why.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-79)|Identifier|`owl-ql-profile-error`|
|[Section top](#minorfail-outcome-number-79)|Title|OWL&#32;QL&#32;Profile&#32;incompatible|
|[Section top](#minorfail-outcome-number-79)|Description|Property&#32;inclusions&#32;involving&#32;property&#32;chains&#32;not&#32;supported|
|[Section top](#minorfail-outcome-number-79)|Pointer|<pre lang="Turtle"><code>coswot:isExecutionOf&#32;a&#32;owl:ObjectProperty&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;is&#32;execution&#32;of&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;Links&#32;a&#32;procedure&#32;execution&#32;to&#32;the&#32;procedure&#32;that&#32;was&#32;execut...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:domain&#32;coswot:ProcedureExecution&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32; &#60;https://w3id.org/coswot/core/procedures> &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:range&#32;coswot:Procedure&#32;;  &#10; &#32; &#32; &#32; &#32;owl:propertyChainAxiom&#32;(&#32;coswot:isExecutionOf&#32;skos:broader&#32;)&#32;.</code></pre>|

***
### MinorFail Outcome number 80

[Jump to summary definition](#summary-MinorFail-80)	|	[Previous MinorFail outcome](#minorfail-outcome-number-79)	|	[Next MinorFail outcome](#minorfail-outcome-number-81)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-procedures-ontology|
|----|----|
|Title|Standalone&#32;module&#32;core&#92;procedures&#92;ontology.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- https://gitlab.com/coswot/coswot-acimov/blob/HEAD/core/procedures/ontology.ttl|

#### Criterion detail
|Identifier|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|
|----|----|
|Title|Profile&#32;compatibility&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;check&#32;whether&#32;the&#32;test&#32;subject&#32;is&#32;compatible&#32;with&#32;a&#32;profile&#32;or&#32;not,&#32;and&#32;if&#32;it&#32;is&#32;not,&#32;why.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-80)|Identifier|`owl-ql-profile-error`|
|[Section top](#minorfail-outcome-number-80)|Title|OWL&#32;QL&#32;Profile&#32;incompatible|
|[Section top](#minorfail-outcome-number-80)|Description|Statement&#32;not&#32;supported&#32;in&#32;a&#32;Super&#32;Class&#32;Expression|
|[Section top](#minorfail-outcome-number-80)|Pointer|<pre lang="Turtle"><code>&#91;]&#32;a&#32;owl:Class&#32;;  &#10; &#32; &#32;&#32; &#32;owl:unionOf&#32;(&#32;coswot:Procedure&#32;coswot:ProcedureExecution&#32;)&#32;.</code></pre>|

***
### MinorFail Outcome number 81

[Jump to summary definition](#summary-MinorFail-81)	|	[Previous MinorFail outcome](#minorfail-outcome-number-80)	|	[Next MinorFail outcome](#minorfail-outcome-number-82)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-procedures-ontology|
|----|----|
|Title|Standalone&#32;module&#32;core&#92;procedures&#92;ontology.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- https://gitlab.com/coswot/coswot-acimov/blob/HEAD/core/procedures/ontology.ttl|

#### Criterion detail
|Identifier|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|
|----|----|
|Title|Profile&#32;compatibility&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;check&#32;whether&#32;the&#32;test&#32;subject&#32;is&#32;compatible&#32;with&#32;a&#32;profile&#32;or&#32;not,&#32;and&#32;if&#32;it&#32;is&#32;not,&#32;why.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-81)|Identifier|`owl-rl-profile-error`|
|[Section top](#minorfail-outcome-number-81)|Title|OWL&#32;RL&#32;Profile&#32;incompatible|
|[Section top](#minorfail-outcome-number-81)|Description|Class&#32;Expression&#32;not&#32;supported&#32;as&#32;object&#32;of&#32;rdfs:domain&#32;or&#32;rdfs:range|
|[Section top](#minorfail-outcome-number-81)|Pointer|<pre lang="Turtle"><code>coswot:hasInput&#32;a&#32;owl:ObjectProperty&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;has&#32;input&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;Links&#32;a&#32;procedure&#32;(e.g.,&#32;a&#32;command)&#32;or&#32;procedure&#32;execution&#32;(...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:domain&#32; &#91;&#32;a&#32;owl:Class&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:unionOf&#32;(&#32;coswot:Procedure&#32;coswot:ProcedureExecution&#32;)&#32;]&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32; &#60;https://w3id.org/coswot/core/functions&lowbar;commands> &#32;;  &#10; &#32; &#32; &#32; &#32;skos:example&#32; &#34;Different&#32;complementary&#32;commands&#32;can&#32;be&#32;defined&#32;for&#32;controll...&#34; &#32;.</code></pre>|

***
### MinorFail Outcome number 82

[Jump to summary definition](#summary-MinorFail-82)	|	[Previous MinorFail outcome](#minorfail-outcome-number-81)	|	[Next MinorFail outcome](#minorfail-outcome-number-83)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-procedures-ontology|
|----|----|
|Title|Standalone&#32;module&#32;core&#92;procedures&#92;ontology.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- https://gitlab.com/coswot/coswot-acimov/blob/HEAD/core/procedures/ontology.ttl|

#### Criterion detail
|Identifier|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|
|----|----|
|Title|Profile&#32;compatibility&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;check&#32;whether&#32;the&#32;test&#32;subject&#32;is&#32;compatible&#32;with&#32;a&#32;profile&#32;or&#32;not,&#32;and&#32;if&#32;it&#32;is&#32;not,&#32;why.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-82)|Identifier|`owl-rl-profile-error`|
|[Section top](#minorfail-outcome-number-82)|Title|OWL&#32;RL&#32;Profile&#32;incompatible|
|[Section top](#minorfail-outcome-number-82)|Description|Statement&#32;not&#32;supported&#32;in&#32;a&#32;Super&#32;Class&#32;Expression|
|[Section top](#minorfail-outcome-number-82)|Pointer|<pre lang="Turtle"><code>&#91;]&#32;a&#32;owl:Class&#32;;  &#10; &#32; &#32;&#32; &#32;owl:unionOf&#32;(&#32;coswot:Procedure&#32;coswot:ProcedureExecution&#32;)&#32;.</code></pre>|

***
### MinorFail Outcome number 83

[Jump to summary definition](#summary-MinorFail-83)	|	[Previous MinorFail outcome](#minorfail-outcome-number-82)	|	[Next MinorFail outcome](#minorfail-outcome-number-84)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-observations-ontology|
|----|----|
|Title|Standalone&#32;module&#32;core&#92;observations&#92;ontology.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- https://gitlab.com/coswot/coswot-acimov/blob/HEAD/core/observations/ontology.ttl|

#### Criterion detail
|Identifier|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|
|----|----|
|Title|Profile&#32;compatibility&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;check&#32;whether&#32;the&#32;test&#32;subject&#32;is&#32;compatible&#32;with&#32;a&#32;profile&#32;or&#32;not,&#32;and&#32;if&#32;it&#32;is&#32;not,&#32;why.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-83)|Identifier|`owl-el-profile-error`|
|[Section top](#minorfail-outcome-number-83)|Title|OWL&#32;EL&#32;Profile&#32;incompatible|
|[Section top](#minorfail-outcome-number-83)|Description|Class&#32;Expression&#32;not&#32;supported&#32;as&#32;object&#32;of&#32;rdfs:domain&#32;or&#32;rdfs:range|
|[Section top](#minorfail-outcome-number-83)|Pointer|<pre lang="Turtle"><code>coswot:observes&#32;a&#32;owl:ObjectProperty&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;observes&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;Links&#32;a&#32;sensor,&#32;sensing&#32;function,&#32;sensing&#32;command,&#32;or&#32;observ...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:domain&#32; &#91;&#32;a&#32;owl:Class&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:unionOf&#32;(&#32;coswot:Sensor&#32;coswot:SensingFunction&#32;coswot:SensingCommand&#32;coswot:Observation&#32;)&#32;]&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32; &#60;https://w3id.org/coswot/core/procedures> &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:subPropertyOf&#32;coswot:targets&#32;;  &#10; &#32; &#32; &#32; &#32;owl:inverseOf&#32;coswot:isObservedBy&#32;.</code></pre>|

***
### MinorFail Outcome number 84

[Jump to summary definition](#summary-MinorFail-84)	|	[Previous MinorFail outcome](#minorfail-outcome-number-83)	|	[Next MinorFail outcome](#minorfail-outcome-number-85)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-observations-ontology|
|----|----|
|Title|Standalone&#32;module&#32;core&#92;observations&#92;ontology.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- https://gitlab.com/coswot/coswot-acimov/blob/HEAD/core/observations/ontology.ttl|

#### Criterion detail
|Identifier|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|
|----|----|
|Title|Profile&#32;compatibility&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;check&#32;whether&#32;the&#32;test&#32;subject&#32;is&#32;compatible&#32;with&#32;a&#32;profile&#32;or&#32;not,&#32;and&#32;if&#32;it&#32;is&#32;not,&#32;why.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-84)|Identifier|`owl-el-profile-error`|
|[Section top](#minorfail-outcome-number-84)|Title|OWL&#32;EL&#32;Profile&#32;incompatible|
|[Section top](#minorfail-outcome-number-84)|Description|Class&#32;Expression&#32;not&#32;supported&#32;with&#32;rdfs:subClassOf|
|[Section top](#minorfail-outcome-number-84)|Pointer|<pre lang="Turtle"><code>coswot:Observation&#32;a&#32;owl:Class&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;Observation&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;A&#32;coswot:Observation&#32;is&#32;the&#32;act&#32;of&#32;carrying&#32;out&#32;a&#32;procedure&#32;...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32; &#60;https://w3id.org/coswot/core/observations> &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:subClassOf&#32; &#91;&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:allValuesFrom&#32;coswot:Sensor&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:onProperty&#32;coswot:madeBy&#32;],  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#91;&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:onProperty&#32;coswot:observes&#32;],  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;coswot:ProcedureExecution&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-84)|Pointer|<pre lang="Turtle"><code>coswot:SensingCommand&#32;a&#32;owl:Class&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;Sensing&#32;Command&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;An&#32;instance&#32;of&#32;sensing&#32;command&#32;is&#32;a&#32;command&#32;that&#32;observes&#32;so...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32; &#60;https://w3id.org/coswot/core/observations> &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:subClassOf&#32; &#91;&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:onProperty&#32;coswot:observes&#32;],  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;coswot:Command&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-84)|Pointer|<pre lang="Turtle"><code>coswot:SensorOfInterest&#32;a&#32;owl:Class&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;Sensor&#32;Of&#32;Interest&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;A&#32;specific,&#32;tangible&#32;device&#32;designed&#32;to&#32;observe&#32;one&#32;or&#32;more&#32;...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32; &#60;https://w3id.org/coswot/core/observations> &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:subClassOf&#32; &#91;&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:onProperty&#32;coswot:observes&#32;],  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;coswot:DeviceOfInterest,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;coswot:Sensor&#32;.</code></pre>|

***
### MinorFail Outcome number 85

[Jump to summary definition](#summary-MinorFail-85)	|	[Previous MinorFail outcome](#minorfail-outcome-number-84)	|	[Next MinorFail outcome](#minorfail-outcome-number-86)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-observations-ontology|
|----|----|
|Title|Standalone&#32;module&#32;core&#92;observations&#92;ontology.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- https://gitlab.com/coswot/coswot-acimov/blob/HEAD/core/observations/ontology.ttl|

#### Criterion detail
|Identifier|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|
|----|----|
|Title|Profile&#32;compatibility&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;check&#32;whether&#32;the&#32;test&#32;subject&#32;is&#32;compatible&#32;with&#32;a&#32;profile&#32;or&#32;not,&#32;and&#32;if&#32;it&#32;is&#32;not,&#32;why.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-85)|Identifier|`owl-el-profile-error`|
|[Section top](#minorfail-outcome-number-85)|Title|OWL&#32;EL&#32;Profile&#32;incompatible|
|[Section top](#minorfail-outcome-number-85)|Description|Statement&#32;not&#32;supported|
|[Section top](#minorfail-outcome-number-85)|Pointer|<pre lang="Turtle"><code>coswot:Sensor&#32;a&#32;owl:Class&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;Sensor&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;Sensors&#32;are&#32;devices&#32;designed&#32;to&#32;observe&#32;one&#32;or&#32;more&#32;properti...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32; &#60;https://w3id.org/coswot/core/observations> &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:subClassOf&#32; &#91;&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:onProperty&#32;coswot:observes&#32;],  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;coswot:Device&#32;;  &#10; &#32; &#32; &#32; &#32;owl:disjointUnionOf&#32;(&#32;coswot:SensorOfInterest&#32;coswot:SensorKind&#32;)&#32;.</code></pre>|

***
### MinorFail Outcome number 86

[Jump to summary definition](#summary-MinorFail-86)	|	[Previous MinorFail outcome](#minorfail-outcome-number-85)	|	[Next MinorFail outcome](#minorfail-outcome-number-87)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-observations-ontology|
|----|----|
|Title|Standalone&#32;module&#32;core&#92;observations&#92;ontology.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- https://gitlab.com/coswot/coswot-acimov/blob/HEAD/core/observations/ontology.ttl|

#### Criterion detail
|Identifier|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|
|----|----|
|Title|Profile&#32;compatibility&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;check&#32;whether&#32;the&#32;test&#32;subject&#32;is&#32;compatible&#32;with&#32;a&#32;profile&#32;or&#32;not,&#32;and&#32;if&#32;it&#32;is&#32;not,&#32;why.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-86)|Identifier|`owl-el-profile-error`|
|[Section top](#minorfail-outcome-number-86)|Title|OWL&#32;EL&#32;Profile&#32;incompatible|
|[Section top](#minorfail-outcome-number-86)|Description|Statement&#32;not&#32;supported&#32;in&#32;a&#32;Class&#32;Expression|
|[Section top](#minorfail-outcome-number-86)|Pointer|<pre lang="Turtle"><code>&#91;]&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32;&#32; &#32;owl:onProperty&#32;coswot:observes&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-86)|Pointer|<pre lang="Turtle"><code>&#91;]&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32;owl:allValuesFrom&#32;coswot:Sensor&#32;;  &#10; &#32; &#32; &#32; &#32;owl:onProperty&#32;coswot:madeBy&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-86)|Pointer|<pre lang="Turtle"><code>&#91;]&#32;a&#32;owl:Class&#32;;  &#10; &#32; &#32;&#32; &#32;owl:unionOf&#32;(&#32;coswot:Sensor&#32;coswot:SensingFunction&#32;coswot:SensingCommand&#32;coswot:Observation&#32;)&#32;.</code></pre>|

***
### MinorFail Outcome number 87

[Jump to summary definition](#summary-MinorFail-87)	|	[Previous MinorFail outcome](#minorfail-outcome-number-86)	|	[Next MinorFail outcome](#minorfail-outcome-number-88)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-observations-ontology|
|----|----|
|Title|Standalone&#32;module&#32;core&#92;observations&#92;ontology.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- https://gitlab.com/coswot/coswot-acimov/blob/HEAD/core/observations/ontology.ttl|

#### Criterion detail
|Identifier|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|
|----|----|
|Title|Profile&#32;compatibility&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;check&#32;whether&#32;the&#32;test&#32;subject&#32;is&#32;compatible&#32;with&#32;a&#32;profile&#32;or&#32;not,&#32;and&#32;if&#32;it&#32;is&#32;not,&#32;why.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-87)|Identifier|`owl-ql-profile-error`|
|[Section top](#minorfail-outcome-number-87)|Title|OWL&#32;QL&#32;Profile&#32;incompatible|
|[Section top](#minorfail-outcome-number-87)|Description|Class&#32;Expression&#32;not&#32;supported&#32;as&#32;object&#32;of&#32;rdfs:domain&#32;or&#32;rdfs:range|
|[Section top](#minorfail-outcome-number-87)|Pointer|<pre lang="Turtle"><code>coswot:observes&#32;a&#32;owl:ObjectProperty&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;observes&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;Links&#32;a&#32;sensor,&#32;sensing&#32;function,&#32;sensing&#32;command,&#32;or&#32;observ...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:domain&#32; &#91;&#32;a&#32;owl:Class&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:unionOf&#32;(&#32;coswot:Sensor&#32;coswot:SensingFunction&#32;coswot:SensingCommand&#32;coswot:Observation&#32;)&#32;]&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32; &#60;https://w3id.org/coswot/core/procedures> &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:subPropertyOf&#32;coswot:targets&#32;;  &#10; &#32; &#32; &#32; &#32;owl:inverseOf&#32;coswot:isObservedBy&#32;.</code></pre>|

***
### MinorFail Outcome number 88

[Jump to summary definition](#summary-MinorFail-88)	|	[Previous MinorFail outcome](#minorfail-outcome-number-87)	|	[Next MinorFail outcome](#minorfail-outcome-number-89)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-observations-ontology|
|----|----|
|Title|Standalone&#32;module&#32;core&#92;observations&#92;ontology.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- https://gitlab.com/coswot/coswot-acimov/blob/HEAD/core/observations/ontology.ttl|

#### Criterion detail
|Identifier|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|
|----|----|
|Title|Profile&#32;compatibility&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;check&#32;whether&#32;the&#32;test&#32;subject&#32;is&#32;compatible&#32;with&#32;a&#32;profile&#32;or&#32;not,&#32;and&#32;if&#32;it&#32;is&#32;not,&#32;why.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-88)|Identifier|`owl-ql-profile-error`|
|[Section top](#minorfail-outcome-number-88)|Title|OWL&#32;QL&#32;Profile&#32;incompatible|
|[Section top](#minorfail-outcome-number-88)|Description|Class&#32;Expression&#32;not&#32;supported&#32;with&#32;rdfs:subClassOf|
|[Section top](#minorfail-outcome-number-88)|Pointer|<pre lang="Turtle"><code>coswot:Observation&#32;a&#32;owl:Class&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;Observation&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;A&#32;coswot:Observation&#32;is&#32;the&#32;act&#32;of&#32;carrying&#32;out&#32;a&#32;procedure&#32;...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32; &#60;https://w3id.org/coswot/core/observations> &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:subClassOf&#32; &#91;&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:allValuesFrom&#32;coswot:Sensor&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:onProperty&#32;coswot:madeBy&#32;],  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#91;&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:onProperty&#32;coswot:observes&#32;],  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;coswot:ProcedureExecution&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-88)|Pointer|<pre lang="Turtle"><code>coswot:SensingCommand&#32;a&#32;owl:Class&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;Sensing&#32;Command&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;An&#32;instance&#32;of&#32;sensing&#32;command&#32;is&#32;a&#32;command&#32;that&#32;observes&#32;so...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32; &#60;https://w3id.org/coswot/core/observations> &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:subClassOf&#32; &#91;&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:onProperty&#32;coswot:observes&#32;],  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;coswot:Command&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-88)|Pointer|<pre lang="Turtle"><code>coswot:SensorOfInterest&#32;a&#32;owl:Class&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;Sensor&#32;Of&#32;Interest&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;A&#32;specific,&#32;tangible&#32;device&#32;designed&#32;to&#32;observe&#32;one&#32;or&#32;more&#32;...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32; &#60;https://w3id.org/coswot/core/observations> &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:subClassOf&#32; &#91;&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:onProperty&#32;coswot:observes&#32;],  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;coswot:DeviceOfInterest,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;coswot:Sensor&#32;.</code></pre>|

***
### MinorFail Outcome number 89

[Jump to summary definition](#summary-MinorFail-89)	|	[Previous MinorFail outcome](#minorfail-outcome-number-88)	|	[Next MinorFail outcome](#minorfail-outcome-number-90)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-observations-ontology|
|----|----|
|Title|Standalone&#32;module&#32;core&#92;observations&#92;ontology.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- https://gitlab.com/coswot/coswot-acimov/blob/HEAD/core/observations/ontology.ttl|

#### Criterion detail
|Identifier|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|
|----|----|
|Title|Profile&#32;compatibility&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;check&#32;whether&#32;the&#32;test&#32;subject&#32;is&#32;compatible&#32;with&#32;a&#32;profile&#32;or&#32;not,&#32;and&#32;if&#32;it&#32;is&#32;not,&#32;why.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-89)|Identifier|`owl-ql-profile-error`|
|[Section top](#minorfail-outcome-number-89)|Title|OWL&#32;QL&#32;Profile&#32;incompatible|
|[Section top](#minorfail-outcome-number-89)|Description|Statement&#32;not&#32;supported|
|[Section top](#minorfail-outcome-number-89)|Pointer|<pre lang="Turtle"><code>coswot:Sensor&#32;a&#32;owl:Class&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;Sensor&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;Sensors&#32;are&#32;devices&#32;designed&#32;to&#32;observe&#32;one&#32;or&#32;more&#32;properti...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32; &#60;https://w3id.org/coswot/core/observations> &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:subClassOf&#32; &#91;&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:onProperty&#32;coswot:observes&#32;],  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;coswot:Device&#32;;  &#10; &#32; &#32; &#32; &#32;owl:disjointUnionOf&#32;(&#32;coswot:SensorOfInterest&#32;coswot:SensorKind&#32;)&#32;.</code></pre>|

***
### MinorFail Outcome number 90

[Jump to summary definition](#summary-MinorFail-90)	|	[Previous MinorFail outcome](#minorfail-outcome-number-89)	|	[Next MinorFail outcome](#minorfail-outcome-number-91)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-observations-ontology|
|----|----|
|Title|Standalone&#32;module&#32;core&#92;observations&#92;ontology.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- https://gitlab.com/coswot/coswot-acimov/blob/HEAD/core/observations/ontology.ttl|

#### Criterion detail
|Identifier|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|
|----|----|
|Title|Profile&#32;compatibility&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;check&#32;whether&#32;the&#32;test&#32;subject&#32;is&#32;compatible&#32;with&#32;a&#32;profile&#32;or&#32;not,&#32;and&#32;if&#32;it&#32;is&#32;not,&#32;why.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-90)|Identifier|`owl-ql-profile-error`|
|[Section top](#minorfail-outcome-number-90)|Title|OWL&#32;QL&#32;Profile&#32;incompatible|
|[Section top](#minorfail-outcome-number-90)|Description|Statement&#32;not&#32;supported&#32;in&#32;a&#32;Super&#32;Class&#32;Expression|
|[Section top](#minorfail-outcome-number-90)|Pointer|<pre lang="Turtle"><code>&#91;]&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32;&#32; &#32;owl:onProperty&#32;coswot:observes&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-90)|Pointer|<pre lang="Turtle"><code>&#91;]&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32;owl:allValuesFrom&#32;coswot:Sensor&#32;;  &#10; &#32; &#32; &#32; &#32;owl:onProperty&#32;coswot:madeBy&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-90)|Pointer|<pre lang="Turtle"><code>&#91;]&#32;a&#32;owl:Class&#32;;  &#10; &#32; &#32;&#32; &#32;owl:unionOf&#32;(&#32;coswot:Sensor&#32;coswot:SensingFunction&#32;coswot:SensingCommand&#32;coswot:Observation&#32;)&#32;.</code></pre>|

***
### MinorFail Outcome number 91

[Jump to summary definition](#summary-MinorFail-91)	|	[Previous MinorFail outcome](#minorfail-outcome-number-90)	|	[Next MinorFail outcome](#minorfail-outcome-number-92)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-observations-ontology|
|----|----|
|Title|Standalone&#32;module&#32;core&#92;observations&#92;ontology.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- https://gitlab.com/coswot/coswot-acimov/blob/HEAD/core/observations/ontology.ttl|

#### Criterion detail
|Identifier|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|
|----|----|
|Title|Profile&#32;compatibility&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;check&#32;whether&#32;the&#32;test&#32;subject&#32;is&#32;compatible&#32;with&#32;a&#32;profile&#32;or&#32;not,&#32;and&#32;if&#32;it&#32;is&#32;not,&#32;why.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-91)|Identifier|`owl-rl-profile-error`|
|[Section top](#minorfail-outcome-number-91)|Title|OWL&#32;RL&#32;Profile&#32;incompatible|
|[Section top](#minorfail-outcome-number-91)|Description|Class&#32;Expression&#32;not&#32;supported&#32;as&#32;object&#32;of&#32;rdfs:domain&#32;or&#32;rdfs:range|
|[Section top](#minorfail-outcome-number-91)|Pointer|<pre lang="Turtle"><code>coswot:observes&#32;a&#32;owl:ObjectProperty&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;observes&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;Links&#32;a&#32;sensor,&#32;sensing&#32;function,&#32;sensing&#32;command,&#32;or&#32;observ...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:domain&#32; &#91;&#32;a&#32;owl:Class&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:unionOf&#32;(&#32;coswot:Sensor&#32;coswot:SensingFunction&#32;coswot:SensingCommand&#32;coswot:Observation&#32;)&#32;]&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32; &#60;https://w3id.org/coswot/core/procedures> &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:subPropertyOf&#32;coswot:targets&#32;;  &#10; &#32; &#32; &#32; &#32;owl:inverseOf&#32;coswot:isObservedBy&#32;.</code></pre>|

***
### MinorFail Outcome number 92

[Jump to summary definition](#summary-MinorFail-92)	|	[Previous MinorFail outcome](#minorfail-outcome-number-91)	|	[Next MinorFail outcome](#minorfail-outcome-number-93)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-observations-ontology|
|----|----|
|Title|Standalone&#32;module&#32;core&#92;observations&#92;ontology.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- https://gitlab.com/coswot/coswot-acimov/blob/HEAD/core/observations/ontology.ttl|

#### Criterion detail
|Identifier|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|
|----|----|
|Title|Profile&#32;compatibility&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;check&#32;whether&#32;the&#32;test&#32;subject&#32;is&#32;compatible&#32;with&#32;a&#32;profile&#32;or&#32;not,&#32;and&#32;if&#32;it&#32;is&#32;not,&#32;why.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-92)|Identifier|`owl-rl-profile-error`|
|[Section top](#minorfail-outcome-number-92)|Title|OWL&#32;RL&#32;Profile&#32;incompatible|
|[Section top](#minorfail-outcome-number-92)|Description|Class&#32;Expression&#32;not&#32;supported&#32;with&#32;rdfs:subClassOf|
|[Section top](#minorfail-outcome-number-92)|Pointer|<pre lang="Turtle"><code>coswot:Observation&#32;a&#32;owl:Class&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;Observation&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;A&#32;coswot:Observation&#32;is&#32;the&#32;act&#32;of&#32;carrying&#32;out&#32;a&#32;procedure&#32;...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32; &#60;https://w3id.org/coswot/core/observations> &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:subClassOf&#32; &#91;&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:allValuesFrom&#32;coswot:Sensor&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:onProperty&#32;coswot:madeBy&#32;],  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#91;&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:onProperty&#32;coswot:observes&#32;],  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;coswot:ProcedureExecution&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-92)|Pointer|<pre lang="Turtle"><code>coswot:SensingCommand&#32;a&#32;owl:Class&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;Sensing&#32;Command&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;An&#32;instance&#32;of&#32;sensing&#32;command&#32;is&#32;a&#32;command&#32;that&#32;observes&#32;so...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32; &#60;https://w3id.org/coswot/core/observations> &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:subClassOf&#32; &#91;&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:onProperty&#32;coswot:observes&#32;],  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;coswot:Command&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-92)|Pointer|<pre lang="Turtle"><code>coswot:SensingFunction&#32;a&#32;owl:Class&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;Sensing&#32;Function&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;An&#32;sensing&#32;function&#32;is&#32;a&#32;function&#32;that&#32;has&#32;at&#32;least&#32;one&#32;sens...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32; &#60;https://w3id.org/coswot/core/observations> &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:subClassOf&#32; &#91;&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:onProperty&#32;coswot:hasCommand&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:someValuesFrom&#32;coswot:SensingCommand&#32;],  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;coswot:Function&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-92)|Pointer|<pre lang="Turtle"><code>coswot:SensorOfInterest&#32;a&#32;owl:Class&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;Sensor&#32;Of&#32;Interest&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;A&#32;specific,&#32;tangible&#32;device&#32;designed&#32;to&#32;observe&#32;one&#32;or&#32;more&#32;...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32; &#60;https://w3id.org/coswot/core/observations> &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:subClassOf&#32; &#91;&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:onProperty&#32;coswot:observes&#32;],  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;coswot:DeviceOfInterest,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;coswot:Sensor&#32;.</code></pre>|

***
### MinorFail Outcome number 93

[Jump to summary definition](#summary-MinorFail-93)	|	[Previous MinorFail outcome](#minorfail-outcome-number-92)	|	[Next MinorFail outcome](#minorfail-outcome-number-94)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-observations-ontology|
|----|----|
|Title|Standalone&#32;module&#32;core&#92;observations&#92;ontology.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- https://gitlab.com/coswot/coswot-acimov/blob/HEAD/core/observations/ontology.ttl|

#### Criterion detail
|Identifier|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|
|----|----|
|Title|Profile&#32;compatibility&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;check&#32;whether&#32;the&#32;test&#32;subject&#32;is&#32;compatible&#32;with&#32;a&#32;profile&#32;or&#32;not,&#32;and&#32;if&#32;it&#32;is&#32;not,&#32;why.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-93)|Identifier|`owl-rl-profile-error`|
|[Section top](#minorfail-outcome-number-93)|Title|OWL&#32;RL&#32;Profile&#32;incompatible|
|[Section top](#minorfail-outcome-number-93)|Description|Statement&#32;not&#32;supported|
|[Section top](#minorfail-outcome-number-93)|Pointer|<pre lang="Turtle"><code>coswot:Sensor&#32;a&#32;owl:Class&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;Sensor&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;Sensors&#32;are&#32;devices&#32;designed&#32;to&#32;observe&#32;one&#32;or&#32;more&#32;properti...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32; &#60;https://w3id.org/coswot/core/observations> &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:subClassOf&#32; &#91;&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:onProperty&#32;coswot:observes&#32;],  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;coswot:Device&#32;;  &#10; &#32; &#32; &#32; &#32;owl:disjointUnionOf&#32;(&#32;coswot:SensorOfInterest&#32;coswot:SensorKind&#32;)&#32;.</code></pre>|

***
### MinorFail Outcome number 94

[Jump to summary definition](#summary-MinorFail-94)	|	[Previous MinorFail outcome](#minorfail-outcome-number-93)	|	[Next MinorFail outcome](#minorfail-outcome-number-95)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-observations-ontology|
|----|----|
|Title|Standalone&#32;module&#32;core&#92;observations&#92;ontology.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- https://gitlab.com/coswot/coswot-acimov/blob/HEAD/core/observations/ontology.ttl|

#### Criterion detail
|Identifier|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|
|----|----|
|Title|Profile&#32;compatibility&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;check&#32;whether&#32;the&#32;test&#32;subject&#32;is&#32;compatible&#32;with&#32;a&#32;profile&#32;or&#32;not,&#32;and&#32;if&#32;it&#32;is&#32;not,&#32;why.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-94)|Identifier|`owl-rl-profile-error`|
|[Section top](#minorfail-outcome-number-94)|Title|OWL&#32;RL&#32;Profile&#32;incompatible|
|[Section top](#minorfail-outcome-number-94)|Description|Statement&#32;not&#32;supported&#32;in&#32;a&#32;Super&#32;Class&#32;Expression|
|[Section top](#minorfail-outcome-number-94)|Pointer|<pre lang="Turtle"><code>&#91;]&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32;&#32; &#32;owl:onProperty&#32;coswot:observes&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-94)|Pointer|<pre lang="Turtle"><code>&#91;]&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32;owl:onProperty&#32;coswot:hasCommand&#32;;  &#10; &#32; &#32; &#32; &#32;owl:someValuesFrom&#32;coswot:SensingCommand&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-94)|Pointer|<pre lang="Turtle"><code>&#91;]&#32;a&#32;owl:Class&#32;;  &#10; &#32; &#32;&#32; &#32;owl:unionOf&#32;(&#32;coswot:Sensor&#32;coswot:SensingFunction&#32;coswot:SensingCommand&#32;coswot:Observation&#32;)&#32;.</code></pre>|

***
### MinorFail Outcome number 95

[Jump to summary definition](#summary-MinorFail-95)	|	[Previous MinorFail outcome](#minorfail-outcome-number-94)	|	[Next MinorFail outcome](#minorfail-outcome-number-96)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-functions-commands-ontology|
|----|----|
|Title|Standalone&#32;module&#32;core&#92;functions&lowbar;commands&#92;ontology.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- https://gitlab.com/coswot/coswot-acimov/blob/HEAD/core/functions_commands/ontology.ttl|

#### Criterion detail
|Identifier|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|
|----|----|
|Title|Profile&#32;compatibility&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;check&#32;whether&#32;the&#32;test&#32;subject&#32;is&#32;compatible&#32;with&#32;a&#32;profile&#32;or&#32;not,&#32;and&#32;if&#32;it&#32;is&#32;not,&#32;why.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-95)|Identifier|`owl-el-profile-error`|
|[Section top](#minorfail-outcome-number-95)|Title|OWL&#32;EL&#32;Profile&#32;incompatible|
|[Section top](#minorfail-outcome-number-95)|Description|Class&#32;Expression&#32;not&#32;supported&#32;with&#32;rdfs:subClassOf|
|[Section top](#minorfail-outcome-number-95)|Pointer|<pre lang="Turtle"><code>coswot:CommandExecution&#32;a&#32;owl:Class&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;Command&#32;Execution&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;Describes&#32;the&#32;execution&#32;of&#32;a&#32;command.&#32;Typically,&#32;its&#32;inputs&#32;...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32; &#60;https://w3id.org/coswot/core/functions&lowbar;commands> &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:subClassOf&#32; &#91;&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:allValuesFrom&#32;coswot:Command&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:onProperty&#32;coswot:isExecutionOf&#32;],  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;coswot:ProcedureExecution&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-95)|Pointer|<pre lang="Turtle"><code>coswot:CommandKind&#32;a&#32;owl:Class&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;Command&#32;Kind&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;The&#32;lowest-level&#32;directives&#32;a&#32;function&#32;exposes&#32;to&#32;some&#32;netwo...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32; &#60;https://w3id.org/coswot/core/functions&lowbar;commands> &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:subClassOf&#32; &#91;&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:allValuesFrom&#32;coswot:CommandKind&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:onProperty&#32;skos:broader&#32;],  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#91;&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:allValuesFrom&#32;coswot:CommandKind&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:onProperty&#32;skos:narrower&#32;],  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#91;&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:allValuesFrom&#32;owl:Nothing&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:onProperty&#32;coswot:hasKind&#32;],  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#91;&#32;owl:allValuesFrom&#32;coswot:FunctionKind&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:onProperty&#32;coswot:isCommandOf&#32;],  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;coswot:Command&#32;;  &#10; &#32; &#32; &#32; &#32;skos:example&#32; &#34;Observe&#32;property,&#32;control&#32;property,&#32;observe&#32;state,&#32;control&#32;s...&#34; &#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-95)|Pointer|<pre lang="Turtle"><code>coswot:CommandOfInterest&#32;a&#32;owl:Class&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;Command&#32;Of&#32;Interest&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;The&#32;lowest-level&#32;directives&#32;a&#32;device&#32;supports&#32;and&#32;exposes&#32;to...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32; &#60;https://w3id.org/coswot/core/functions&lowbar;commands> &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:subClassOf&#32; &#91;&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:allValuesFrom&#32;coswot:CommandKind&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:onProperty&#32;coswot:hasKind&#32;],  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#91;&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:onProperty&#32;coswot:hasKind&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:someValuesFrom&#32;coswot:CommandKind&#32;],  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#91;&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:onProperty&#32;coswot:isCommandOfInterestOf&#32;],  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;coswot:Command&#32;;  &#10; &#32; &#32; &#32; &#32;skos:example&#32; &#34;The&#32;corridor&#32;smart&#32;light&#32;switch&#32;supports&#32;a&#32;command&#32;of&#32;kind&#32;“...&#34;,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#34;The&#32;smart&#32;fridge&#32;supports&#32;a&#32;command&#32;of&#32;kind&#32;“observe&#32;tempera...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;skos:note&#32; &#34;Commands&#32;of&#32;interest&#32;need&#32;not&#32;always&#32;be&#32;explicited.&#32;It&#32;depen...&#34;,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#34;Like&#32;for&#32;commands,&#32;commands&#32;of&#32;interest&#32;may&#32;be&#32;described&#32;in&#32;...&#34; &#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-95)|Pointer|<pre lang="Turtle"><code>coswot:DeviceKind&#32;rdfs:subClassOf&#32; &#91;&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:allValuesFrom&#32;coswot:FunctionKind&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:onProperty&#32;coswot:hasFunction&#32;]&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-95)|Pointer|<pre lang="Turtle"><code>coswot:FunctionKind&#32;a&#32;owl:Class&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;Function&#32;Kind&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;Logical&#32;groups&#32;of&#32;commands&#32;that&#32;devices&#32;support&#32;to&#32;accomplis...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32; &#60;https://w3id.org/coswot/core/functions&lowbar;commands> &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:subClassOf&#32; &#91;&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:allValuesFrom&#32;coswot:FunctionKind&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:onProperty&#32;skos:broader&#32;],  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#91;&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:allValuesFrom&#32;coswot:FunctionKind&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:onProperty&#32;skos:narrower&#32;],  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#91;&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:allValuesFrom&#32;owl:Nothing&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:onProperty&#32;coswot:hasKind&#32;],  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#91;&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:allValuesFrom&#32;coswot:DeviceKind&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:onProperty&#32;coswot:isFunctionOf&#32;],  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#91;&#32;owl:allValuesFrom&#32;coswot:CommandKind&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:onProperty&#32;coswot:hasCommand&#32;],  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;coswot:Function&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-95)|Pointer|<pre lang="Turtle"><code>coswot:FunctionOfInterest&#32;a&#32;owl:Class&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;Function&#32;of&#32;Interest&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;Logical&#32;groups&#32;of&#32;commands&#32;that&#32;devices&#32;support&#32;to&#32;accomplis...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32; &#60;https://w3id.org/coswot/core/functions&lowbar;commands> &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:subClassOf&#32; &#91;&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:allValuesFrom&#32;coswot:FunctionKind&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:onProperty&#32;coswot:hasKind&#32;],  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#91;&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:onProperty&#32;coswot:hasKind&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:someValuesFrom&#32;coswot:FunctionKind&#32;],  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#91;&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:onProperty&#32;coswot:isFunctionOfInterestOf&#32;],  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;coswot:Function&#32;;  &#10; &#32; &#32; &#32; &#32;skos:note&#32; &#34;A&#32;function&#32;of&#32;interest&#32;is&#32;the&#32;function&#32;of&#32;(OP&#32;coswot:isFunct...&#34;,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#34;Functions&#32;of&#32;interest&#32;need&#32;not&#32;always&#32;be&#32;explicited.&#32;It&#32;depe...&#34; &#32;.</code></pre>|

***
### MinorFail Outcome number 96

[Jump to summary definition](#summary-MinorFail-96)	|	[Previous MinorFail outcome](#minorfail-outcome-number-95)	|	[Next MinorFail outcome](#minorfail-outcome-number-97)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-functions-commands-ontology|
|----|----|
|Title|Standalone&#32;module&#32;core&#92;functions&lowbar;commands&#92;ontology.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- https://gitlab.com/coswot/coswot-acimov/blob/HEAD/core/functions_commands/ontology.ttl|

#### Criterion detail
|Identifier|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|
|----|----|
|Title|Profile&#32;compatibility&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;check&#32;whether&#32;the&#32;test&#32;subject&#32;is&#32;compatible&#32;with&#32;a&#32;profile&#32;or&#32;not,&#32;and&#32;if&#32;it&#32;is&#32;not,&#32;why.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-96)|Identifier|`owl-el-profile-error`|
|[Section top](#minorfail-outcome-number-96)|Title|OWL&#32;EL&#32;Profile&#32;incompatible|
|[Section top](#minorfail-outcome-number-96)|Description|Statement&#32;not&#32;supported|
|[Section top](#minorfail-outcome-number-96)|Pointer|<pre lang="Turtle"><code>coswot:Function&#32;a&#32;owl:Class&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;Function&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;Logical&#32;groups&#32;of&#32;commands&#32;that&#32;devices&#32;support&#32;to&#32;accomplis...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32; &#60;https://w3id.org/coswot/core/functions&lowbar;commands> &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:subClassOf&#32;coswot:ProcedureCollection&#32;;  &#10; &#32; &#32; &#32; &#32;owl:disjointUnionOf&#32;(&#32;coswot:FunctionOfInterest&#32;coswot:FunctionKind&#32;)&#32;.</code></pre>|

***
### MinorFail Outcome number 97

[Jump to summary definition](#summary-MinorFail-97)	|	[Previous MinorFail outcome](#minorfail-outcome-number-96)	|	[Next MinorFail outcome](#minorfail-outcome-number-98)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-functions-commands-ontology|
|----|----|
|Title|Standalone&#32;module&#32;core&#92;functions&lowbar;commands&#92;ontology.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- https://gitlab.com/coswot/coswot-acimov/blob/HEAD/core/functions_commands/ontology.ttl|

#### Criterion detail
|Identifier|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|
|----|----|
|Title|Profile&#32;compatibility&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;check&#32;whether&#32;the&#32;test&#32;subject&#32;is&#32;compatible&#32;with&#32;a&#32;profile&#32;or&#32;not,&#32;and&#32;if&#32;it&#32;is&#32;not,&#32;why.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-97)|Identifier|`owl-el-profile-error`|
|[Section top](#minorfail-outcome-number-97)|Title|OWL&#32;EL&#32;Profile&#32;incompatible|
|[Section top](#minorfail-outcome-number-97)|Description|Statement&#32;not&#32;supported&#32;in&#32;a&#32;Class&#32;Expression|
|[Section top](#minorfail-outcome-number-97)|Pointer|<pre lang="Turtle"><code>&#91;]&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32;owl:allValuesFrom&#32;coswot:FunctionKind&#32;;  &#10; &#32; &#32; &#32; &#32;owl:onProperty&#32;skos:broader&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-97)|Pointer|<pre lang="Turtle"><code>&#91;]&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32;owl:allValuesFrom&#32;coswot:FunctionKind&#32;;  &#10; &#32; &#32; &#32; &#32;owl:onProperty&#32;skos:narrower&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-97)|Pointer|<pre lang="Turtle"><code>&#91;]&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32;owl:allValuesFrom&#32;owl:Nothing&#32;;  &#10; &#32; &#32; &#32; &#32;owl:onProperty&#32;coswot:hasKind&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-97)|Pointer|<pre lang="Turtle"><code>&#91;]&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32;owl:allValuesFrom&#32;coswot:FunctionKind&#32;;  &#10; &#32; &#32; &#32; &#32;owl:onProperty&#32;coswot:hasKind&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-97)|Pointer|<pre lang="Turtle"><code>&#91;]&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32;owl:allValuesFrom&#32;coswot:FunctionKind&#32;;  &#10; &#32; &#32; &#32; &#32;owl:onProperty&#32;coswot:hasFunction&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-97)|Pointer|<pre lang="Turtle"><code>&#91;]&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32;owl:allValuesFrom&#32;coswot:DeviceKind&#32;;  &#10; &#32; &#32; &#32; &#32;owl:onProperty&#32;coswot:isFunctionOf&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-97)|Pointer|<pre lang="Turtle"><code>&#91;]&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32;&#32; &#32;owl:onProperty&#32;coswot:isFunctionOfInterestOf&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-97)|Pointer|<pre lang="Turtle"><code>&#91;]&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32;owl:allValuesFrom&#32;coswot:CommandKind&#32;;  &#10; &#32; &#32; &#32; &#32;owl:onProperty&#32;skos:broader&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-97)|Pointer|<pre lang="Turtle"><code>&#91;]&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32;owl:allValuesFrom&#32;coswot:CommandKind&#32;;  &#10; &#32; &#32; &#32; &#32;owl:onProperty&#32;skos:narrower&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-97)|Pointer|<pre lang="Turtle"><code>&#91;]&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32;owl:allValuesFrom&#32;coswot:CommandKind&#32;;  &#10; &#32; &#32; &#32; &#32;owl:onProperty&#32;coswot:hasKind&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-97)|Pointer|<pre lang="Turtle"><code>&#91;]&#32;owl:allValuesFrom&#32;coswot:CommandKind&#32;;  &#10; &#32; &#32;&#32; &#32;owl:onProperty&#32;coswot:hasCommand&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-97)|Pointer|<pre lang="Turtle"><code>&#91;]&#32;owl:allValuesFrom&#32;coswot:FunctionKind&#32;;  &#10; &#32; &#32;&#32; &#32;owl:onProperty&#32;coswot:isCommandOf&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-97)|Pointer|<pre lang="Turtle"><code>&#91;]&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32;&#32; &#32;owl:onProperty&#32;coswot:isCommandOfInterestOf&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-97)|Pointer|<pre lang="Turtle"><code>&#91;]&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32;owl:allValuesFrom&#32;coswot:Command&#32;;  &#10; &#32; &#32; &#32; &#32;owl:onProperty&#32;coswot:isExecutionOf&#32;.</code></pre>|

***
### MinorFail Outcome number 98

[Jump to summary definition](#summary-MinorFail-98)	|	[Previous MinorFail outcome](#minorfail-outcome-number-97)	|	[Next MinorFail outcome](#minorfail-outcome-number-99)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-functions-commands-ontology|
|----|----|
|Title|Standalone&#32;module&#32;core&#92;functions&lowbar;commands&#92;ontology.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- https://gitlab.com/coswot/coswot-acimov/blob/HEAD/core/functions_commands/ontology.ttl|

#### Criterion detail
|Identifier|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|
|----|----|
|Title|Profile&#32;compatibility&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;check&#32;whether&#32;the&#32;test&#32;subject&#32;is&#32;compatible&#32;with&#32;a&#32;profile&#32;or&#32;not,&#32;and&#32;if&#32;it&#32;is&#32;not,&#32;why.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-98)|Identifier|`owl-ql-profile-error`|
|[Section top](#minorfail-outcome-number-98)|Title|OWL&#32;QL&#32;Profile&#32;incompatible|
|[Section top](#minorfail-outcome-number-98)|Description|Class&#32;Expression&#32;not&#32;supported&#32;with&#32;rdfs:subClassOf|
|[Section top](#minorfail-outcome-number-98)|Pointer|<pre lang="Turtle"><code>coswot:CommandExecution&#32;a&#32;owl:Class&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;Command&#32;Execution&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;Describes&#32;the&#32;execution&#32;of&#32;a&#32;command.&#32;Typically,&#32;its&#32;inputs&#32;...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32; &#60;https://w3id.org/coswot/core/functions&lowbar;commands> &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:subClassOf&#32; &#91;&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:allValuesFrom&#32;coswot:Command&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:onProperty&#32;coswot:isExecutionOf&#32;],  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;coswot:ProcedureExecution&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-98)|Pointer|<pre lang="Turtle"><code>coswot:CommandKind&#32;a&#32;owl:Class&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;Command&#32;Kind&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;The&#32;lowest-level&#32;directives&#32;a&#32;function&#32;exposes&#32;to&#32;some&#32;netwo...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32; &#60;https://w3id.org/coswot/core/functions&lowbar;commands> &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:subClassOf&#32; &#91;&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:allValuesFrom&#32;coswot:CommandKind&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:onProperty&#32;skos:broader&#32;],  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#91;&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:allValuesFrom&#32;coswot:CommandKind&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:onProperty&#32;skos:narrower&#32;],  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#91;&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:allValuesFrom&#32;owl:Nothing&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:onProperty&#32;coswot:hasKind&#32;],  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#91;&#32;owl:allValuesFrom&#32;coswot:FunctionKind&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:onProperty&#32;coswot:isCommandOf&#32;],  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;coswot:Command&#32;;  &#10; &#32; &#32; &#32; &#32;skos:example&#32; &#34;Observe&#32;property,&#32;control&#32;property,&#32;observe&#32;state,&#32;control&#32;s...&#34; &#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-98)|Pointer|<pre lang="Turtle"><code>coswot:CommandOfInterest&#32;a&#32;owl:Class&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;Command&#32;Of&#32;Interest&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;The&#32;lowest-level&#32;directives&#32;a&#32;device&#32;supports&#32;and&#32;exposes&#32;to...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32; &#60;https://w3id.org/coswot/core/functions&lowbar;commands> &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:subClassOf&#32; &#91;&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:allValuesFrom&#32;coswot:CommandKind&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:onProperty&#32;coswot:hasKind&#32;],  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#91;&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:onProperty&#32;coswot:hasKind&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:someValuesFrom&#32;coswot:CommandKind&#32;],  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#91;&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:onProperty&#32;coswot:isCommandOfInterestOf&#32;],  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;coswot:Command&#32;;  &#10; &#32; &#32; &#32; &#32;skos:example&#32; &#34;The&#32;corridor&#32;smart&#32;light&#32;switch&#32;supports&#32;a&#32;command&#32;of&#32;kind&#32;“...&#34;,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#34;The&#32;smart&#32;fridge&#32;supports&#32;a&#32;command&#32;of&#32;kind&#32;“observe&#32;tempera...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;skos:note&#32; &#34;Commands&#32;of&#32;interest&#32;need&#32;not&#32;always&#32;be&#32;explicited.&#32;It&#32;depen...&#34;,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#34;Like&#32;for&#32;commands,&#32;commands&#32;of&#32;interest&#32;may&#32;be&#32;described&#32;in&#32;...&#34; &#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-98)|Pointer|<pre lang="Turtle"><code>coswot:DeviceKind&#32;rdfs:subClassOf&#32; &#91;&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:allValuesFrom&#32;coswot:FunctionKind&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:onProperty&#32;coswot:hasFunction&#32;]&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-98)|Pointer|<pre lang="Turtle"><code>coswot:FunctionKind&#32;a&#32;owl:Class&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;Function&#32;Kind&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;Logical&#32;groups&#32;of&#32;commands&#32;that&#32;devices&#32;support&#32;to&#32;accomplis...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32; &#60;https://w3id.org/coswot/core/functions&lowbar;commands> &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:subClassOf&#32; &#91;&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:allValuesFrom&#32;coswot:FunctionKind&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:onProperty&#32;skos:broader&#32;],  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#91;&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:allValuesFrom&#32;coswot:FunctionKind&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:onProperty&#32;skos:narrower&#32;],  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#91;&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:allValuesFrom&#32;owl:Nothing&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:onProperty&#32;coswot:hasKind&#32;],  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#91;&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:allValuesFrom&#32;coswot:DeviceKind&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:onProperty&#32;coswot:isFunctionOf&#32;],  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#91;&#32;owl:allValuesFrom&#32;coswot:CommandKind&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:onProperty&#32;coswot:hasCommand&#32;],  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;coswot:Function&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-98)|Pointer|<pre lang="Turtle"><code>coswot:FunctionOfInterest&#32;a&#32;owl:Class&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;Function&#32;of&#32;Interest&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;Logical&#32;groups&#32;of&#32;commands&#32;that&#32;devices&#32;support&#32;to&#32;accomplis...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32; &#60;https://w3id.org/coswot/core/functions&lowbar;commands> &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:subClassOf&#32; &#91;&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:allValuesFrom&#32;coswot:FunctionKind&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:onProperty&#32;coswot:hasKind&#32;],  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#91;&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:onProperty&#32;coswot:hasKind&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:someValuesFrom&#32;coswot:FunctionKind&#32;],  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#91;&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:onProperty&#32;coswot:isFunctionOfInterestOf&#32;],  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;coswot:Function&#32;;  &#10; &#32; &#32; &#32; &#32;skos:note&#32; &#34;A&#32;function&#32;of&#32;interest&#32;is&#32;the&#32;function&#32;of&#32;(OP&#32;coswot:isFunct...&#34;,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#34;Functions&#32;of&#32;interest&#32;need&#32;not&#32;always&#32;be&#32;explicited.&#32;It&#32;depe...&#34; &#32;.</code></pre>|

***
### MinorFail Outcome number 99

[Jump to summary definition](#summary-MinorFail-99)	|	[Previous MinorFail outcome](#minorfail-outcome-number-98)	|	[Next MinorFail outcome](#minorfail-outcome-number-100)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-functions-commands-ontology|
|----|----|
|Title|Standalone&#32;module&#32;core&#92;functions&lowbar;commands&#92;ontology.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- https://gitlab.com/coswot/coswot-acimov/blob/HEAD/core/functions_commands/ontology.ttl|

#### Criterion detail
|Identifier|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|
|----|----|
|Title|Profile&#32;compatibility&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;check&#32;whether&#32;the&#32;test&#32;subject&#32;is&#32;compatible&#32;with&#32;a&#32;profile&#32;or&#32;not,&#32;and&#32;if&#32;it&#32;is&#32;not,&#32;why.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-99)|Identifier|`owl-ql-profile-error`|
|[Section top](#minorfail-outcome-number-99)|Title|OWL&#32;QL&#32;Profile&#32;incompatible|
|[Section top](#minorfail-outcome-number-99)|Description|Property&#32;inclusions&#32;involving&#32;property&#32;chains&#32;not&#32;supported|
|[Section top](#minorfail-outcome-number-99)|Pointer|<pre lang="Turtle"><code>coswot:hasCommand&#32;a&#32;owl:ObjectProperty&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;has&#32;command&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;Links&#32;a&#32;function&#32;and&#32;the&#32;command&#32;it&#32;supports.&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:domain&#32;coswot:Function&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32; &#60;https://w3id.org/coswot/core/functions&lowbar;commands> &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:range&#32;coswot:Command&#32;;  &#10; &#32; &#32; &#32; &#32;owl:inverseOf&#32;coswot:isCommandOf&#32;;  &#10; &#32; &#32; &#32; &#32;owl:propertyChainAxiom&#32;(&#32;coswot:hasKind&#32;coswot:hasMandatoryCommand&#32;),  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;(&#32;coswot:hasCommandOfInterest&#32;coswot:hasKind&#32;)&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-99)|Pointer|<pre lang="Turtle"><code>coswot:hasFunction&#32;a&#32;owl:ObjectProperty&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;has&#32;function&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;Links&#32;a&#32;device&#32;to&#32;one&#32;of&#32;its&#32;functions.&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:domain&#32;coswot:Device&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32; &#60;https://w3id.org/coswot/core/functions&lowbar;commands> &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:range&#32;coswot:Function&#32;;  &#10; &#32; &#32; &#32; &#32;owl:inverseOf&#32;coswot:isFunctionOf&#32;;  &#10; &#32; &#32; &#32; &#32;owl:propertyChainAxiom&#32;(&#32;skos:broader&#32;coswot:hasFunction&#32;),  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;(&#32;coswot:hasKind&#32;coswot:hasFunction&#32;),  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;(&#32;coswot:hasFunctionOfInterest&#32;coswot:hasKind&#32;)&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-99)|Pointer|<pre lang="Turtle"><code>coswot:hasMandatoryCommand&#32;a&#32;owl:ObjectProperty&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;has&#32;mandatory&#32;command&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;Links&#32;a&#32;function&#32;and&#32;one&#32;of&#32;its&#32;mandatory&#32;commands&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:domain&#32;coswot:FunctionKind&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32; &#60;https://w3id.org/coswot/core/functions&lowbar;commands> &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:range&#32;coswot:CommandKind&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:subPropertyOf&#32;coswot:hasCommand&#32;;  &#10; &#32; &#32; &#32; &#32;owl:propertyChainAxiom&#32;(&#32;skos:broader&#32;coswot:hasMandatoryCommand&#32;)&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-99)|Pointer|<pre lang="Turtle"><code>coswot:isExecutionOf&#32;owl:propertyChainAxiom&#32;(&#32;coswot:isExecutionOf&#32;coswot:hasKind&#32;)&#32;.</code></pre>|

***
### MinorFail Outcome number 100

[Jump to summary definition](#summary-MinorFail-100)	|	[Previous MinorFail outcome](#minorfail-outcome-number-99)	|	[Next MinorFail outcome](#minorfail-outcome-number-101)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-functions-commands-ontology|
|----|----|
|Title|Standalone&#32;module&#32;core&#92;functions&lowbar;commands&#92;ontology.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- https://gitlab.com/coswot/coswot-acimov/blob/HEAD/core/functions_commands/ontology.ttl|

#### Criterion detail
|Identifier|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|
|----|----|
|Title|Profile&#32;compatibility&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;check&#32;whether&#32;the&#32;test&#32;subject&#32;is&#32;compatible&#32;with&#32;a&#32;profile&#32;or&#32;not,&#32;and&#32;if&#32;it&#32;is&#32;not,&#32;why.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-100)|Identifier|`owl-ql-profile-error`|
|[Section top](#minorfail-outcome-number-100)|Title|OWL&#32;QL&#32;Profile&#32;incompatible|
|[Section top](#minorfail-outcome-number-100)|Description|Statement&#32;not&#32;supported|
|[Section top](#minorfail-outcome-number-100)|Pointer|<pre lang="Turtle"><code>coswot:Function&#32;a&#32;owl:Class&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;Function&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;Logical&#32;groups&#32;of&#32;commands&#32;that&#32;devices&#32;support&#32;to&#32;accomplis...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32; &#60;https://w3id.org/coswot/core/functions&lowbar;commands> &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:subClassOf&#32;coswot:ProcedureCollection&#32;;  &#10; &#32; &#32; &#32; &#32;owl:disjointUnionOf&#32;(&#32;coswot:FunctionOfInterest&#32;coswot:FunctionKind&#32;)&#32;.</code></pre>|

***
### MinorFail Outcome number 101

[Jump to summary definition](#summary-MinorFail-101)	|	[Previous MinorFail outcome](#minorfail-outcome-number-100)	|	[Next MinorFail outcome](#minorfail-outcome-number-102)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-functions-commands-ontology|
|----|----|
|Title|Standalone&#32;module&#32;core&#92;functions&lowbar;commands&#92;ontology.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- https://gitlab.com/coswot/coswot-acimov/blob/HEAD/core/functions_commands/ontology.ttl|

#### Criterion detail
|Identifier|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|
|----|----|
|Title|Profile&#32;compatibility&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;check&#32;whether&#32;the&#32;test&#32;subject&#32;is&#32;compatible&#32;with&#32;a&#32;profile&#32;or&#32;not,&#32;and&#32;if&#32;it&#32;is&#32;not,&#32;why.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-101)|Identifier|`owl-ql-profile-error`|
|[Section top](#minorfail-outcome-number-101)|Title|OWL&#32;QL&#32;Profile&#32;incompatible|
|[Section top](#minorfail-outcome-number-101)|Description|Statement&#32;not&#32;supported&#32;in&#32;a&#32;Super&#32;Class&#32;Expression|
|[Section top](#minorfail-outcome-number-101)|Pointer|<pre lang="Turtle"><code>&#91;]&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32;owl:allValuesFrom&#32;coswot:FunctionKind&#32;;  &#10; &#32; &#32; &#32; &#32;owl:onProperty&#32;skos:broader&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-101)|Pointer|<pre lang="Turtle"><code>&#91;]&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32;owl:allValuesFrom&#32;coswot:FunctionKind&#32;;  &#10; &#32; &#32; &#32; &#32;owl:onProperty&#32;skos:narrower&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-101)|Pointer|<pre lang="Turtle"><code>&#91;]&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32;owl:allValuesFrom&#32;owl:Nothing&#32;;  &#10; &#32; &#32; &#32; &#32;owl:onProperty&#32;coswot:hasKind&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-101)|Pointer|<pre lang="Turtle"><code>&#91;]&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32;owl:allValuesFrom&#32;coswot:FunctionKind&#32;;  &#10; &#32; &#32; &#32; &#32;owl:onProperty&#32;coswot:hasKind&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-101)|Pointer|<pre lang="Turtle"><code>&#91;]&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32;owl:allValuesFrom&#32;coswot:FunctionKind&#32;;  &#10; &#32; &#32; &#32; &#32;owl:onProperty&#32;coswot:hasFunction&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-101)|Pointer|<pre lang="Turtle"><code>&#91;]&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32;owl:allValuesFrom&#32;coswot:DeviceKind&#32;;  &#10; &#32; &#32; &#32; &#32;owl:onProperty&#32;coswot:isFunctionOf&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-101)|Pointer|<pre lang="Turtle"><code>&#91;]&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32;&#32; &#32;owl:onProperty&#32;coswot:isFunctionOfInterestOf&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-101)|Pointer|<pre lang="Turtle"><code>&#91;]&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32;owl:allValuesFrom&#32;coswot:CommandKind&#32;;  &#10; &#32; &#32; &#32; &#32;owl:onProperty&#32;skos:broader&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-101)|Pointer|<pre lang="Turtle"><code>&#91;]&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32;owl:allValuesFrom&#32;coswot:CommandKind&#32;;  &#10; &#32; &#32; &#32; &#32;owl:onProperty&#32;skos:narrower&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-101)|Pointer|<pre lang="Turtle"><code>&#91;]&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32;owl:allValuesFrom&#32;coswot:CommandKind&#32;;  &#10; &#32; &#32; &#32; &#32;owl:onProperty&#32;coswot:hasKind&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-101)|Pointer|<pre lang="Turtle"><code>&#91;]&#32;owl:allValuesFrom&#32;coswot:CommandKind&#32;;  &#10; &#32; &#32;&#32; &#32;owl:onProperty&#32;coswot:hasCommand&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-101)|Pointer|<pre lang="Turtle"><code>&#91;]&#32;owl:allValuesFrom&#32;coswot:FunctionKind&#32;;  &#10; &#32; &#32;&#32; &#32;owl:onProperty&#32;coswot:isCommandOf&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-101)|Pointer|<pre lang="Turtle"><code>&#91;]&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32;&#32; &#32;owl:onProperty&#32;coswot:isCommandOfInterestOf&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-101)|Pointer|<pre lang="Turtle"><code>&#91;]&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32;owl:allValuesFrom&#32;coswot:Command&#32;;  &#10; &#32; &#32; &#32; &#32;owl:onProperty&#32;coswot:isExecutionOf&#32;.</code></pre>|

***
### MinorFail Outcome number 102

[Jump to summary definition](#summary-MinorFail-102)	|	[Previous MinorFail outcome](#minorfail-outcome-number-101)	|	[Next MinorFail outcome](#minorfail-outcome-number-103)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-functions-commands-ontology|
|----|----|
|Title|Standalone&#32;module&#32;core&#92;functions&lowbar;commands&#92;ontology.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- https://gitlab.com/coswot/coswot-acimov/blob/HEAD/core/functions_commands/ontology.ttl|

#### Criterion detail
|Identifier|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|
|----|----|
|Title|Profile&#32;compatibility&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;check&#32;whether&#32;the&#32;test&#32;subject&#32;is&#32;compatible&#32;with&#32;a&#32;profile&#32;or&#32;not,&#32;and&#32;if&#32;it&#32;is&#32;not,&#32;why.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-102)|Identifier|`owl-rl-profile-error`|
|[Section top](#minorfail-outcome-number-102)|Title|OWL&#32;RL&#32;Profile&#32;incompatible|
|[Section top](#minorfail-outcome-number-102)|Description|Class&#32;Expression&#32;not&#32;supported&#32;with&#32;rdfs:subClassOf|
|[Section top](#minorfail-outcome-number-102)|Pointer|<pre lang="Turtle"><code>coswot:CommandOfInterest&#32;a&#32;owl:Class&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;Command&#32;Of&#32;Interest&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;The&#32;lowest-level&#32;directives&#32;a&#32;device&#32;supports&#32;and&#32;exposes&#32;to...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32; &#60;https://w3id.org/coswot/core/functions&lowbar;commands> &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:subClassOf&#32; &#91;&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:allValuesFrom&#32;coswot:CommandKind&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:onProperty&#32;coswot:hasKind&#32;],  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#91;&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:onProperty&#32;coswot:hasKind&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:someValuesFrom&#32;coswot:CommandKind&#32;],  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#91;&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:onProperty&#32;coswot:isCommandOfInterestOf&#32;],  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;coswot:Command&#32;;  &#10; &#32; &#32; &#32; &#32;skos:example&#32; &#34;The&#32;corridor&#32;smart&#32;light&#32;switch&#32;supports&#32;a&#32;command&#32;of&#32;kind&#32;“...&#34;,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#34;The&#32;smart&#32;fridge&#32;supports&#32;a&#32;command&#32;of&#32;kind&#32;“observe&#32;tempera...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;skos:note&#32; &#34;Commands&#32;of&#32;interest&#32;need&#32;not&#32;always&#32;be&#32;explicited.&#32;It&#32;depen...&#34;,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#34;Like&#32;for&#32;commands,&#32;commands&#32;of&#32;interest&#32;may&#32;be&#32;described&#32;in&#32;...&#34; &#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-102)|Pointer|<pre lang="Turtle"><code>coswot:FunctionOfInterest&#32;a&#32;owl:Class&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;Function&#32;of&#32;Interest&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;Logical&#32;groups&#32;of&#32;commands&#32;that&#32;devices&#32;support&#32;to&#32;accomplis...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32; &#60;https://w3id.org/coswot/core/functions&lowbar;commands> &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:subClassOf&#32; &#91;&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:allValuesFrom&#32;coswot:FunctionKind&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:onProperty&#32;coswot:hasKind&#32;],  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#91;&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:onProperty&#32;coswot:hasKind&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:someValuesFrom&#32;coswot:FunctionKind&#32;],  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#91;&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:onProperty&#32;coswot:isFunctionOfInterestOf&#32;],  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;coswot:Function&#32;;  &#10; &#32; &#32; &#32; &#32;skos:note&#32; &#34;A&#32;function&#32;of&#32;interest&#32;is&#32;the&#32;function&#32;of&#32;(OP&#32;coswot:isFunct...&#34;,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#34;Functions&#32;of&#32;interest&#32;need&#32;not&#32;always&#32;be&#32;explicited.&#32;It&#32;depe...&#34; &#32;.</code></pre>|

***
### MinorFail Outcome number 103

[Jump to summary definition](#summary-MinorFail-103)	|	[Previous MinorFail outcome](#minorfail-outcome-number-102)	|	[Next MinorFail outcome](#minorfail-outcome-number-104)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-functions-commands-ontology|
|----|----|
|Title|Standalone&#32;module&#32;core&#92;functions&lowbar;commands&#92;ontology.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- https://gitlab.com/coswot/coswot-acimov/blob/HEAD/core/functions_commands/ontology.ttl|

#### Criterion detail
|Identifier|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|
|----|----|
|Title|Profile&#32;compatibility&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;check&#32;whether&#32;the&#32;test&#32;subject&#32;is&#32;compatible&#32;with&#32;a&#32;profile&#32;or&#32;not,&#32;and&#32;if&#32;it&#32;is&#32;not,&#32;why.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-103)|Identifier|`owl-rl-profile-error`|
|[Section top](#minorfail-outcome-number-103)|Title|OWL&#32;RL&#32;Profile&#32;incompatible|
|[Section top](#minorfail-outcome-number-103)|Description|Statement&#32;not&#32;supported|
|[Section top](#minorfail-outcome-number-103)|Pointer|<pre lang="Turtle"><code>coswot:Function&#32;a&#32;owl:Class&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;Function&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;Logical&#32;groups&#32;of&#32;commands&#32;that&#32;devices&#32;support&#32;to&#32;accomplis...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32; &#60;https://w3id.org/coswot/core/functions&lowbar;commands> &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:subClassOf&#32;coswot:ProcedureCollection&#32;;  &#10; &#32; &#32; &#32; &#32;owl:disjointUnionOf&#32;(&#32;coswot:FunctionOfInterest&#32;coswot:FunctionKind&#32;)&#32;.</code></pre>|

***
### MinorFail Outcome number 104

[Jump to summary definition](#summary-MinorFail-104)	|	[Previous MinorFail outcome](#minorfail-outcome-number-103)	|	[Next MinorFail outcome](#minorfail-outcome-number-105)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-functions-commands-ontology|
|----|----|
|Title|Standalone&#32;module&#32;core&#92;functions&lowbar;commands&#92;ontology.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- https://gitlab.com/coswot/coswot-acimov/blob/HEAD/core/functions_commands/ontology.ttl|

#### Criterion detail
|Identifier|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|
|----|----|
|Title|Profile&#32;compatibility&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;check&#32;whether&#32;the&#32;test&#32;subject&#32;is&#32;compatible&#32;with&#32;a&#32;profile&#32;or&#32;not,&#32;and&#32;if&#32;it&#32;is&#32;not,&#32;why.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-104)|Identifier|`owl-rl-profile-error`|
|[Section top](#minorfail-outcome-number-104)|Title|OWL&#32;RL&#32;Profile&#32;incompatible|
|[Section top](#minorfail-outcome-number-104)|Description|Statement&#32;not&#32;supported&#32;in&#32;a&#32;Super&#32;Class&#32;Expression|
|[Section top](#minorfail-outcome-number-104)|Pointer|<pre lang="Turtle"><code>&#91;]&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32;owl:onProperty&#32;coswot:hasKind&#32;;  &#10; &#32; &#32; &#32; &#32;owl:someValuesFrom&#32;coswot:FunctionKind&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-104)|Pointer|<pre lang="Turtle"><code>&#91;]&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32;&#32; &#32;owl:onProperty&#32;coswot:isFunctionOfInterestOf&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-104)|Pointer|<pre lang="Turtle"><code>&#91;]&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32;owl:onProperty&#32;coswot:hasKind&#32;;  &#10; &#32; &#32; &#32; &#32;owl:someValuesFrom&#32;coswot:CommandKind&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-104)|Pointer|<pre lang="Turtle"><code>&#91;]&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32;&#32; &#32;owl:onProperty&#32;coswot:isCommandOfInterestOf&#32;.</code></pre>|

***
### MinorFail Outcome number 105

[Jump to summary definition](#summary-MinorFail-105)	|	[Previous MinorFail outcome](#minorfail-outcome-number-104)	|	[Next MinorFail outcome](#minorfail-outcome-number-106)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-functions-commands-ontology|
|----|----|
|Title|Standalone&#32;module&#32;core&#92;functions&lowbar;commands&#92;ontology.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- https://gitlab.com/coswot/coswot-acimov/blob/HEAD/core/functions_commands/ontology.ttl|

#### Criterion detail
|Identifier|[term-referencing](https://ns.inria.fr/olivaw#term-referencing)|
|----|----|
|Title|Term&#32;referencing&#32;test|
|Description|A&#32;test&#32;case&#32;from&#32;the&#32;Best&#32;Practices&#32;tests&#32;checking&#32;if&#32;each&#32;term&#32;of&#32;the&#32;test&#32;subject&#32;is&#32;referenced&#32;to&#32;a&#32;module&#32;through&#32;a&#32;rdfs:isDefinedBy&#32;property.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-105)|Identifier|`no-reference-module`|
|[Section top](#minorfail-outcome-number-105)|Title|Term&#32;not&#32;referenced&#32;to&#32;a&#32;module|
|[Section top](#minorfail-outcome-number-105)|Description|Subject&#32;terms&#32;not&#32;linked&#32;to&#32;a&#32;module&#32;by&#32;a&#32;rdfs:isDefinedBy&#32;property|
|[Section top](#minorfail-outcome-number-105)|Pointer|<pre lang="Turtle"><code>:DeviceKind&#32;rdfs:subClassOf&#32; &#91;&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:allValuesFrom&#32;:FunctionKind&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:onProperty&#32;:hasFunction&#32;]&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-105)|Pointer|<pre lang="Turtle"><code>:isExecutionOf&#32;owl:propertyChainAxiom&#32;(&#32;:isExecutionOf&#32;:hasKind&#32;)&#32;.</code></pre>|

***
### MinorFail Outcome number 106

[Jump to summary definition](#summary-MinorFail-106)	|	[Previous MinorFail outcome](#minorfail-outcome-number-105)	|	[Next MinorFail outcome](#minorfail-outcome-number-107)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-features-ontology-catalogs|
|----|----|
|Title|Standalone&#32;module&#32;core&#92;features&#92;ontology.catalogs.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- https://gitlab.com/coswot/coswot-acimov/blob/HEAD/core/features/ontology.catalogs.ttl|

#### Criterion detail
|Identifier|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|
|----|----|
|Title|Profile&#32;compatibility&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;check&#32;whether&#32;the&#32;test&#32;subject&#32;is&#32;compatible&#32;with&#32;a&#32;profile&#32;or&#32;not,&#32;and&#32;if&#32;it&#32;is&#32;not,&#32;why.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-106)|Identifier|`owl-el-profile-error`|
|[Section top](#minorfail-outcome-number-106)|Title|OWL&#32;EL&#32;Profile&#32;incompatible|
|[Section top](#minorfail-outcome-number-106)|Description|Class&#32;Expression&#32;not&#32;supported&#32;with&#32;rdfs:subClassOf|
|[Section top](#minorfail-outcome-number-106)|Pointer|<pre lang="Turtle"><code>coswot:FeatureKind&#32;a&#32;owl:Class&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;Feature&#32;kind&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;A&#32;Feature&#32;Kind&#32;represents&#32;an&#32;archetype&#32;of&#32;real&#32;world&#32;entitie...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32; &#60;https://w3id.org/coswot/core/features> &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:subClassOf&#32; &#91;&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:allValuesFrom&#32;coswot:FeatureKind&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:onProperty&#32;skos:broader&#32;],  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#91;&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:allValuesFrom&#32;coswot:FeatureKind&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:onProperty&#32;skos:narrower&#32;],  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#91;&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:allValuesFrom&#32;coswot:FeatureKind&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:onProperty&#32;coswot:consistsOf&#32;],  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;skos:Concept&#32;.</code></pre>|

***
### MinorFail Outcome number 107

[Jump to summary definition](#summary-MinorFail-107)	|	[Previous MinorFail outcome](#minorfail-outcome-number-106)	|	[Next MinorFail outcome](#minorfail-outcome-number-108)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-features-ontology-catalogs|
|----|----|
|Title|Standalone&#32;module&#32;core&#92;features&#92;ontology.catalogs.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- https://gitlab.com/coswot/coswot-acimov/blob/HEAD/core/features/ontology.catalogs.ttl|

#### Criterion detail
|Identifier|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|
|----|----|
|Title|Profile&#32;compatibility&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;check&#32;whether&#32;the&#32;test&#32;subject&#32;is&#32;compatible&#32;with&#32;a&#32;profile&#32;or&#32;not,&#32;and&#32;if&#32;it&#32;is&#32;not,&#32;why.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-107)|Identifier|`owl-el-profile-error`|
|[Section top](#minorfail-outcome-number-107)|Title|OWL&#32;EL&#32;Profile&#32;incompatible|
|[Section top](#minorfail-outcome-number-107)|Description|Statement&#32;not&#32;supported&#32;in&#32;a&#32;Class&#32;Expression|
|[Section top](#minorfail-outcome-number-107)|Pointer|<pre lang="Turtle"><code>&#91;]&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32;owl:allValuesFrom&#32;coswot:FeatureKind&#32;;  &#10; &#32; &#32; &#32; &#32;owl:onProperty&#32;skos:broader&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-107)|Pointer|<pre lang="Turtle"><code>&#91;]&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32;owl:allValuesFrom&#32;coswot:FeatureKind&#32;;  &#10; &#32; &#32; &#32; &#32;owl:onProperty&#32;skos:narrower&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-107)|Pointer|<pre lang="Turtle"><code>&#91;]&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32;owl:allValuesFrom&#32;coswot:FeatureKind&#32;;  &#10; &#32; &#32; &#32; &#32;owl:onProperty&#32;coswot:consistsOf&#32;.</code></pre>|

***
### MinorFail Outcome number 108

[Jump to summary definition](#summary-MinorFail-108)	|	[Previous MinorFail outcome](#minorfail-outcome-number-107)	|	[Next MinorFail outcome](#minorfail-outcome-number-109)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-features-ontology-catalogs|
|----|----|
|Title|Standalone&#32;module&#32;core&#92;features&#92;ontology.catalogs.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- https://gitlab.com/coswot/coswot-acimov/blob/HEAD/core/features/ontology.catalogs.ttl|

#### Criterion detail
|Identifier|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|
|----|----|
|Title|Profile&#32;compatibility&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;check&#32;whether&#32;the&#32;test&#32;subject&#32;is&#32;compatible&#32;with&#32;a&#32;profile&#32;or&#32;not,&#32;and&#32;if&#32;it&#32;is&#32;not,&#32;why.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-108)|Identifier|`owl-ql-profile-error`|
|[Section top](#minorfail-outcome-number-108)|Title|OWL&#32;QL&#32;Profile&#32;incompatible|
|[Section top](#minorfail-outcome-number-108)|Description|Class&#32;Expression&#32;not&#32;supported&#32;with&#32;rdfs:subClassOf|
|[Section top](#minorfail-outcome-number-108)|Pointer|<pre lang="Turtle"><code>coswot:FeatureKind&#32;a&#32;owl:Class&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;Feature&#32;kind&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;A&#32;Feature&#32;Kind&#32;represents&#32;an&#32;archetype&#32;of&#32;real&#32;world&#32;entitie...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32; &#60;https://w3id.org/coswot/core/features> &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:subClassOf&#32; &#91;&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:allValuesFrom&#32;coswot:FeatureKind&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:onProperty&#32;skos:broader&#32;],  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#91;&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:allValuesFrom&#32;coswot:FeatureKind&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:onProperty&#32;skos:narrower&#32;],  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#91;&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:allValuesFrom&#32;coswot:FeatureKind&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:onProperty&#32;coswot:consistsOf&#32;],  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;skos:Concept&#32;.</code></pre>|

***
### MinorFail Outcome number 109

[Jump to summary definition](#summary-MinorFail-109)	|	[Previous MinorFail outcome](#minorfail-outcome-number-108)	|	[Next MinorFail outcome](#minorfail-outcome-number-110)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-features-ontology-catalogs|
|----|----|
|Title|Standalone&#32;module&#32;core&#92;features&#92;ontology.catalogs.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- https://gitlab.com/coswot/coswot-acimov/blob/HEAD/core/features/ontology.catalogs.ttl|

#### Criterion detail
|Identifier|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|
|----|----|
|Title|Profile&#32;compatibility&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;check&#32;whether&#32;the&#32;test&#32;subject&#32;is&#32;compatible&#32;with&#32;a&#32;profile&#32;or&#32;not,&#32;and&#32;if&#32;it&#32;is&#32;not,&#32;why.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-109)|Identifier|`owl-ql-profile-error`|
|[Section top](#minorfail-outcome-number-109)|Title|OWL&#32;QL&#32;Profile&#32;incompatible|
|[Section top](#minorfail-outcome-number-109)|Description|Statement&#32;not&#32;supported&#32;in&#32;a&#32;Super&#32;Class&#32;Expression|
|[Section top](#minorfail-outcome-number-109)|Pointer|<pre lang="Turtle"><code>&#91;]&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32;owl:allValuesFrom&#32;coswot:FeatureKind&#32;;  &#10; &#32; &#32; &#32; &#32;owl:onProperty&#32;skos:broader&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-109)|Pointer|<pre lang="Turtle"><code>&#91;]&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32;owl:allValuesFrom&#32;coswot:FeatureKind&#32;;  &#10; &#32; &#32; &#32; &#32;owl:onProperty&#32;skos:narrower&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-109)|Pointer|<pre lang="Turtle"><code>&#91;]&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32;owl:allValuesFrom&#32;coswot:FeatureKind&#32;;  &#10; &#32; &#32; &#32; &#32;owl:onProperty&#32;coswot:consistsOf&#32;.</code></pre>|

***
### MinorFail Outcome number 110

[Jump to summary definition](#summary-MinorFail-110)	|	[Previous MinorFail outcome](#minorfail-outcome-number-109)	|	[Next MinorFail outcome](#minorfail-outcome-number-111)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-features-ontology|
|----|----|
|Title|Standalone&#32;module&#32;core&#92;features&#92;ontology.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- https://gitlab.com/coswot/coswot-acimov/blob/HEAD/core/features/ontology.ttl|

#### Criterion detail
|Identifier|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|
|----|----|
|Title|Profile&#32;compatibility&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;check&#32;whether&#32;the&#32;test&#32;subject&#32;is&#32;compatible&#32;with&#32;a&#32;profile&#32;or&#32;not,&#32;and&#32;if&#32;it&#32;is&#32;not,&#32;why.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-110)|Identifier|`owl-el-profile-error`|
|[Section top](#minorfail-outcome-number-110)|Title|OWL&#32;EL&#32;Profile&#32;incompatible|
|[Section top](#minorfail-outcome-number-110)|Description|Class&#32;Expression&#32;not&#32;supported&#32;with&#32;rdfs:subClassOf|
|[Section top](#minorfail-outcome-number-110)|Pointer|<pre lang="Turtle"><code>coswot:FeatureKind&#32;a&#32;owl:Class&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;Feature&#32;kind&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;A&#32;Feature&#32;Kind&#32;represents&#32;an&#32;archetype&#32;of&#32;real&#32;world&#32;entitie...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32; &#60;https://w3id.org/coswot/core/features> &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:subClassOf&#32; &#91;&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:allValuesFrom&#32;coswot:FeatureKind&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:onProperty&#32;skos:broader&#32;],  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#91;&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:allValuesFrom&#32;coswot:FeatureKind&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:onProperty&#32;skos:narrower&#32;],  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#91;&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:allValuesFrom&#32;owl:Nothing&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:onProperty&#32;coswot:hasKind&#32;],  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#91;&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:allValuesFrom&#32;coswot:FeatureKind&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:onProperty&#32;coswot:consistsOf&#32;],  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;skos:Concept,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;coswot:Feature&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-110)|Pointer|<pre lang="Turtle"><code>coswot:FeatureOfInterest&#32;a&#32;owl:Class&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;Feature&#32;of&#32;interest&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;A&#32;feature&#32;of&#32;interest&#32;represents&#32;one&#32;specific&#32;real&#32;world&#32;ent...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32; &#60;https://w3id.org/coswot/core/features> &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:subClassOf&#32; &#91;&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:allValuesFrom&#32;coswot:FeatureKind&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:onProperty&#32;coswot:hasKind&#32;],  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#91;&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:onProperty&#32;coswot:hasKind&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:someValuesFrom&#32;coswot:FeatureKind&#32;],  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#91;&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:allValuesFrom&#32;coswot:FeatureOfInterest&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:onProperty&#32;coswot:consistsOf&#32;],  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;coswot:Feature&#32;.</code></pre>|

***
### MinorFail Outcome number 111

[Jump to summary definition](#summary-MinorFail-111)	|	[Previous MinorFail outcome](#minorfail-outcome-number-110)	|	[Next MinorFail outcome](#minorfail-outcome-number-112)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-features-ontology|
|----|----|
|Title|Standalone&#32;module&#32;core&#92;features&#92;ontology.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- https://gitlab.com/coswot/coswot-acimov/blob/HEAD/core/features/ontology.ttl|

#### Criterion detail
|Identifier|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|
|----|----|
|Title|Profile&#32;compatibility&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;check&#32;whether&#32;the&#32;test&#32;subject&#32;is&#32;compatible&#32;with&#32;a&#32;profile&#32;or&#32;not,&#32;and&#32;if&#32;it&#32;is&#32;not,&#32;why.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-111)|Identifier|`owl-el-profile-error`|
|[Section top](#minorfail-outcome-number-111)|Title|OWL&#32;EL&#32;Profile&#32;incompatible|
|[Section top](#minorfail-outcome-number-111)|Description|Statement&#32;not&#32;supported|
|[Section top](#minorfail-outcome-number-111)|Pointer|<pre lang="Turtle"><code>coswot:Feature&#32;a&#32;owl:Class&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;Feature&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;Real&#32;world&#32;entities&#32;from&#32;which&#32;a&#32;property&#32;or&#32;a&#32;state&#32;may&#32;be&#32;...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32; &#60;https://w3id.org/coswot/core/features> &#32;;  &#10; &#32; &#32; &#32; &#32;owl:disjointUnionOf&#32;(&#32;coswot:FeatureOfInterest&#32;coswot:FeatureKind&#32;)&#32;.</code></pre>|

***
### MinorFail Outcome number 112

[Jump to summary definition](#summary-MinorFail-112)	|	[Previous MinorFail outcome](#minorfail-outcome-number-111)	|	[Next MinorFail outcome](#minorfail-outcome-number-113)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-features-ontology|
|----|----|
|Title|Standalone&#32;module&#32;core&#92;features&#92;ontology.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- https://gitlab.com/coswot/coswot-acimov/blob/HEAD/core/features/ontology.ttl|

#### Criterion detail
|Identifier|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|
|----|----|
|Title|Profile&#32;compatibility&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;check&#32;whether&#32;the&#32;test&#32;subject&#32;is&#32;compatible&#32;with&#32;a&#32;profile&#32;or&#32;not,&#32;and&#32;if&#32;it&#32;is&#32;not,&#32;why.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-112)|Identifier|`owl-el-profile-error`|
|[Section top](#minorfail-outcome-number-112)|Title|OWL&#32;EL&#32;Profile&#32;incompatible|
|[Section top](#minorfail-outcome-number-112)|Description|Statement&#32;not&#32;supported&#32;in&#32;a&#32;Class&#32;Expression|
|[Section top](#minorfail-outcome-number-112)|Pointer|<pre lang="Turtle"><code>&#91;]&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32;owl:allValuesFrom&#32;coswot:FeatureKind&#32;;  &#10; &#32; &#32; &#32; &#32;owl:onProperty&#32;skos:broader&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-112)|Pointer|<pre lang="Turtle"><code>&#91;]&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32;owl:allValuesFrom&#32;coswot:FeatureKind&#32;;  &#10; &#32; &#32; &#32; &#32;owl:onProperty&#32;skos:narrower&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-112)|Pointer|<pre lang="Turtle"><code>&#91;]&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32;owl:allValuesFrom&#32;owl:Nothing&#32;;  &#10; &#32; &#32; &#32; &#32;owl:onProperty&#32;coswot:hasKind&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-112)|Pointer|<pre lang="Turtle"><code>&#91;]&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32;owl:allValuesFrom&#32;coswot:FeatureKind&#32;;  &#10; &#32; &#32; &#32; &#32;owl:onProperty&#32;coswot:hasKind&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-112)|Pointer|<pre lang="Turtle"><code>&#91;]&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32;owl:allValuesFrom&#32;coswot:FeatureKind&#32;;  &#10; &#32; &#32; &#32; &#32;owl:onProperty&#32;coswot:consistsOf&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-112)|Pointer|<pre lang="Turtle"><code>&#91;]&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32;owl:allValuesFrom&#32;coswot:FeatureOfInterest&#32;;  &#10; &#32; &#32; &#32; &#32;owl:onProperty&#32;coswot:consistsOf&#32;.</code></pre>|

***
### MinorFail Outcome number 113

[Jump to summary definition](#summary-MinorFail-113)	|	[Previous MinorFail outcome](#minorfail-outcome-number-112)	|	[Next MinorFail outcome](#minorfail-outcome-number-114)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-features-ontology|
|----|----|
|Title|Standalone&#32;module&#32;core&#92;features&#92;ontology.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- https://gitlab.com/coswot/coswot-acimov/blob/HEAD/core/features/ontology.ttl|

#### Criterion detail
|Identifier|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|
|----|----|
|Title|Profile&#32;compatibility&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;check&#32;whether&#32;the&#32;test&#32;subject&#32;is&#32;compatible&#32;with&#32;a&#32;profile&#32;or&#32;not,&#32;and&#32;if&#32;it&#32;is&#32;not,&#32;why.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-113)|Identifier|`owl-ql-profile-error`|
|[Section top](#minorfail-outcome-number-113)|Title|OWL&#32;QL&#32;Profile&#32;incompatible|
|[Section top](#minorfail-outcome-number-113)|Description|Class&#32;Expression&#32;not&#32;supported&#32;with&#32;rdfs:subClassOf|
|[Section top](#minorfail-outcome-number-113)|Pointer|<pre lang="Turtle"><code>coswot:FeatureKind&#32;a&#32;owl:Class&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;Feature&#32;kind&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;A&#32;Feature&#32;Kind&#32;represents&#32;an&#32;archetype&#32;of&#32;real&#32;world&#32;entitie...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32; &#60;https://w3id.org/coswot/core/features> &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:subClassOf&#32; &#91;&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:allValuesFrom&#32;coswot:FeatureKind&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:onProperty&#32;skos:broader&#32;],  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#91;&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:allValuesFrom&#32;coswot:FeatureKind&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:onProperty&#32;skos:narrower&#32;],  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#91;&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:allValuesFrom&#32;owl:Nothing&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:onProperty&#32;coswot:hasKind&#32;],  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#91;&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:allValuesFrom&#32;coswot:FeatureKind&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:onProperty&#32;coswot:consistsOf&#32;],  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;skos:Concept,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;coswot:Feature&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-113)|Pointer|<pre lang="Turtle"><code>coswot:FeatureOfInterest&#32;a&#32;owl:Class&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;Feature&#32;of&#32;interest&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;A&#32;feature&#32;of&#32;interest&#32;represents&#32;one&#32;specific&#32;real&#32;world&#32;ent...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32; &#60;https://w3id.org/coswot/core/features> &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:subClassOf&#32; &#91;&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:allValuesFrom&#32;coswot:FeatureKind&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:onProperty&#32;coswot:hasKind&#32;],  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#91;&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:onProperty&#32;coswot:hasKind&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:someValuesFrom&#32;coswot:FeatureKind&#32;],  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#91;&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:allValuesFrom&#32;coswot:FeatureOfInterest&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:onProperty&#32;coswot:consistsOf&#32;],  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;coswot:Feature&#32;.</code></pre>|

***
### MinorFail Outcome number 114

[Jump to summary definition](#summary-MinorFail-114)	|	[Previous MinorFail outcome](#minorfail-outcome-number-113)	|	[Next MinorFail outcome](#minorfail-outcome-number-115)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-features-ontology|
|----|----|
|Title|Standalone&#32;module&#32;core&#92;features&#92;ontology.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- https://gitlab.com/coswot/coswot-acimov/blob/HEAD/core/features/ontology.ttl|

#### Criterion detail
|Identifier|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|
|----|----|
|Title|Profile&#32;compatibility&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;check&#32;whether&#32;the&#32;test&#32;subject&#32;is&#32;compatible&#32;with&#32;a&#32;profile&#32;or&#32;not,&#32;and&#32;if&#32;it&#32;is&#32;not,&#32;why.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-114)|Identifier|`owl-ql-profile-error`|
|[Section top](#minorfail-outcome-number-114)|Title|OWL&#32;QL&#32;Profile&#32;incompatible|
|[Section top](#minorfail-outcome-number-114)|Description|Property&#32;inclusions&#32;involving&#32;property&#32;chains&#32;not&#32;supported|
|[Section top](#minorfail-outcome-number-114)|Pointer|<pre lang="Turtle"><code>coswot:hasKind&#32;a&#32;owl:ObjectProperty&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;has&#32;feature&#32;kind&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;links&#32;something&#32;of&#32;interest&#32;interest&#32;to&#32;its&#32;kind&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32; &#60;https://w3id.org/coswot/core/features> &#32;;  &#10; &#32; &#32; &#32; &#32;owl:propertyChainAxiom&#32;(&#32;coswot:hasKind&#32;skos:broader&#32;)&#32;.</code></pre>|

***
### MinorFail Outcome number 115

[Jump to summary definition](#summary-MinorFail-115)	|	[Previous MinorFail outcome](#minorfail-outcome-number-114)	|	[Next MinorFail outcome](#minorfail-outcome-number-116)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-features-ontology|
|----|----|
|Title|Standalone&#32;module&#32;core&#92;features&#92;ontology.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- https://gitlab.com/coswot/coswot-acimov/blob/HEAD/core/features/ontology.ttl|

#### Criterion detail
|Identifier|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|
|----|----|
|Title|Profile&#32;compatibility&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;check&#32;whether&#32;the&#32;test&#32;subject&#32;is&#32;compatible&#32;with&#32;a&#32;profile&#32;or&#32;not,&#32;and&#32;if&#32;it&#32;is&#32;not,&#32;why.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-115)|Identifier|`owl-ql-profile-error`|
|[Section top](#minorfail-outcome-number-115)|Title|OWL&#32;QL&#32;Profile&#32;incompatible|
|[Section top](#minorfail-outcome-number-115)|Description|Statement&#32;not&#32;supported|
|[Section top](#minorfail-outcome-number-115)|Pointer|<pre lang="Turtle"><code>coswot:Feature&#32;a&#32;owl:Class&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;Feature&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;Real&#32;world&#32;entities&#32;from&#32;which&#32;a&#32;property&#32;or&#32;a&#32;state&#32;may&#32;be&#32;...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32; &#60;https://w3id.org/coswot/core/features> &#32;;  &#10; &#32; &#32; &#32; &#32;owl:disjointUnionOf&#32;(&#32;coswot:FeatureOfInterest&#32;coswot:FeatureKind&#32;)&#32;.</code></pre>|

***
### MinorFail Outcome number 116

[Jump to summary definition](#summary-MinorFail-116)	|	[Previous MinorFail outcome](#minorfail-outcome-number-115)	|	[Next MinorFail outcome](#minorfail-outcome-number-117)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-features-ontology|
|----|----|
|Title|Standalone&#32;module&#32;core&#92;features&#92;ontology.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- https://gitlab.com/coswot/coswot-acimov/blob/HEAD/core/features/ontology.ttl|

#### Criterion detail
|Identifier|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|
|----|----|
|Title|Profile&#32;compatibility&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;check&#32;whether&#32;the&#32;test&#32;subject&#32;is&#32;compatible&#32;with&#32;a&#32;profile&#32;or&#32;not,&#32;and&#32;if&#32;it&#32;is&#32;not,&#32;why.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-116)|Identifier|`owl-ql-profile-error`|
|[Section top](#minorfail-outcome-number-116)|Title|OWL&#32;QL&#32;Profile&#32;incompatible|
|[Section top](#minorfail-outcome-number-116)|Description|Statement&#32;not&#32;supported&#32;in&#32;a&#32;Super&#32;Class&#32;Expression|
|[Section top](#minorfail-outcome-number-116)|Pointer|<pre lang="Turtle"><code>&#91;]&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32;owl:allValuesFrom&#32;coswot:FeatureKind&#32;;  &#10; &#32; &#32; &#32; &#32;owl:onProperty&#32;skos:broader&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-116)|Pointer|<pre lang="Turtle"><code>&#91;]&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32;owl:allValuesFrom&#32;coswot:FeatureKind&#32;;  &#10; &#32; &#32; &#32; &#32;owl:onProperty&#32;skos:narrower&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-116)|Pointer|<pre lang="Turtle"><code>&#91;]&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32;owl:allValuesFrom&#32;owl:Nothing&#32;;  &#10; &#32; &#32; &#32; &#32;owl:onProperty&#32;coswot:hasKind&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-116)|Pointer|<pre lang="Turtle"><code>&#91;]&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32;owl:allValuesFrom&#32;coswot:FeatureKind&#32;;  &#10; &#32; &#32; &#32; &#32;owl:onProperty&#32;coswot:hasKind&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-116)|Pointer|<pre lang="Turtle"><code>&#91;]&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32;owl:allValuesFrom&#32;coswot:FeatureKind&#32;;  &#10; &#32; &#32; &#32; &#32;owl:onProperty&#32;coswot:consistsOf&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-116)|Pointer|<pre lang="Turtle"><code>&#91;]&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32;owl:allValuesFrom&#32;coswot:FeatureOfInterest&#32;;  &#10; &#32; &#32; &#32; &#32;owl:onProperty&#32;coswot:consistsOf&#32;.</code></pre>|

***
### MinorFail Outcome number 117

[Jump to summary definition](#summary-MinorFail-117)	|	[Previous MinorFail outcome](#minorfail-outcome-number-116)	|	[Next MinorFail outcome](#minorfail-outcome-number-118)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-features-ontology|
|----|----|
|Title|Standalone&#32;module&#32;core&#92;features&#92;ontology.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- https://gitlab.com/coswot/coswot-acimov/blob/HEAD/core/features/ontology.ttl|

#### Criterion detail
|Identifier|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|
|----|----|
|Title|Profile&#32;compatibility&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;check&#32;whether&#32;the&#32;test&#32;subject&#32;is&#32;compatible&#32;with&#32;a&#32;profile&#32;or&#32;not,&#32;and&#32;if&#32;it&#32;is&#32;not,&#32;why.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-117)|Identifier|`owl-rl-profile-error`|
|[Section top](#minorfail-outcome-number-117)|Title|OWL&#32;RL&#32;Profile&#32;incompatible|
|[Section top](#minorfail-outcome-number-117)|Description|Class&#32;Expression&#32;not&#32;supported&#32;with&#32;rdfs:subClassOf|
|[Section top](#minorfail-outcome-number-117)|Pointer|<pre lang="Turtle"><code>coswot:FeatureOfInterest&#32;a&#32;owl:Class&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;Feature&#32;of&#32;interest&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;A&#32;feature&#32;of&#32;interest&#32;represents&#32;one&#32;specific&#32;real&#32;world&#32;ent...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32; &#60;https://w3id.org/coswot/core/features> &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:subClassOf&#32; &#91;&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:allValuesFrom&#32;coswot:FeatureKind&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:onProperty&#32;coswot:hasKind&#32;],  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#91;&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:onProperty&#32;coswot:hasKind&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:someValuesFrom&#32;coswot:FeatureKind&#32;],  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#91;&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:allValuesFrom&#32;coswot:FeatureOfInterest&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:onProperty&#32;coswot:consistsOf&#32;],  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;coswot:Feature&#32;.</code></pre>|

***
### MinorFail Outcome number 118

[Jump to summary definition](#summary-MinorFail-118)	|	[Previous MinorFail outcome](#minorfail-outcome-number-117)	|	[Next MinorFail outcome](#minorfail-outcome-number-119)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-features-ontology|
|----|----|
|Title|Standalone&#32;module&#32;core&#92;features&#92;ontology.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- https://gitlab.com/coswot/coswot-acimov/blob/HEAD/core/features/ontology.ttl|

#### Criterion detail
|Identifier|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|
|----|----|
|Title|Profile&#32;compatibility&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;check&#32;whether&#32;the&#32;test&#32;subject&#32;is&#32;compatible&#32;with&#32;a&#32;profile&#32;or&#32;not,&#32;and&#32;if&#32;it&#32;is&#32;not,&#32;why.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-118)|Identifier|`owl-rl-profile-error`|
|[Section top](#minorfail-outcome-number-118)|Title|OWL&#32;RL&#32;Profile&#32;incompatible|
|[Section top](#minorfail-outcome-number-118)|Description|Statement&#32;not&#32;supported|
|[Section top](#minorfail-outcome-number-118)|Pointer|<pre lang="Turtle"><code>coswot:Feature&#32;a&#32;owl:Class&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;Feature&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;Real&#32;world&#32;entities&#32;from&#32;which&#32;a&#32;property&#32;or&#32;a&#32;state&#32;may&#32;be&#32;...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32; &#60;https://w3id.org/coswot/core/features> &#32;;  &#10; &#32; &#32; &#32; &#32;owl:disjointUnionOf&#32;(&#32;coswot:FeatureOfInterest&#32;coswot:FeatureKind&#32;)&#32;.</code></pre>|

***
### MinorFail Outcome number 119

[Jump to summary definition](#summary-MinorFail-119)	|	[Previous MinorFail outcome](#minorfail-outcome-number-118)	|	[Next MinorFail outcome](#minorfail-outcome-number-120)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-features-ontology|
|----|----|
|Title|Standalone&#32;module&#32;core&#92;features&#92;ontology.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- https://gitlab.com/coswot/coswot-acimov/blob/HEAD/core/features/ontology.ttl|

#### Criterion detail
|Identifier|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|
|----|----|
|Title|Profile&#32;compatibility&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;check&#32;whether&#32;the&#32;test&#32;subject&#32;is&#32;compatible&#32;with&#32;a&#32;profile&#32;or&#32;not,&#32;and&#32;if&#32;it&#32;is&#32;not,&#32;why.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-119)|Identifier|`owl-rl-profile-error`|
|[Section top](#minorfail-outcome-number-119)|Title|OWL&#32;RL&#32;Profile&#32;incompatible|
|[Section top](#minorfail-outcome-number-119)|Description|Statement&#32;not&#32;supported&#32;in&#32;a&#32;Super&#32;Class&#32;Expression|
|[Section top](#minorfail-outcome-number-119)|Pointer|<pre lang="Turtle"><code>&#91;]&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32;owl:onProperty&#32;coswot:hasKind&#32;;  &#10; &#32; &#32; &#32; &#32;owl:someValuesFrom&#32;coswot:FeatureKind&#32;.</code></pre>|

***
### MinorFail Outcome number 120

[Jump to summary definition](#summary-MinorFail-120)	|	[Previous MinorFail outcome](#minorfail-outcome-number-119)	|	[Next MinorFail outcome](#minorfail-outcome-number-121)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-devices-ontology|
|----|----|
|Title|Standalone&#32;module&#32;core&#92;devices&#92;ontology.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- https://gitlab.com/coswot/coswot-acimov/blob/HEAD/core/devices/ontology.ttl|

#### Criterion detail
|Identifier|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|
|----|----|
|Title|Profile&#32;compatibility&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;check&#32;whether&#32;the&#32;test&#32;subject&#32;is&#32;compatible&#32;with&#32;a&#32;profile&#32;or&#32;not,&#32;and&#32;if&#32;it&#32;is&#32;not,&#32;why.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-120)|Identifier|`owl-el-profile-error`|
|[Section top](#minorfail-outcome-number-120)|Title|OWL&#32;EL&#32;Profile&#32;incompatible|
|[Section top](#minorfail-outcome-number-120)|Description|Class&#32;Expression&#32;not&#32;supported&#32;as&#32;object&#32;of&#32;rdfs:domain&#32;or&#32;rdfs:range|
|[Section top](#minorfail-outcome-number-120)|Pointer|<pre lang="Turtle"><code>coswot:isTargetOf&#32;a&#32;owl:ObjectProperty&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;is&#32;target&#32;of&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;Links&#32;a&#32;feature,&#32;property,&#32;or&#32;state,&#32;to&#32;the&#32;device,&#32;function...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:domain&#32; &#91;&#32;a&#32;owl:Class&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:unionOf&#32;(&#32;coswot:Feature&#32;coswot:Property&#32;coswot:State&#32;)&#32;]&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32; &#60;https://w3id.org/coswot/core/devices> &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:range&#32; &#91;&#32;a&#32;owl:Class&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:unionOf&#32;(&#32;coswot:Device&#32;coswot:Function&#32;coswot:Command&#32;coswot:ProcedureExecution&#32;)&#32;]&#32;;  &#10; &#32; &#32; &#32; &#32;owl:inverseOf&#32;coswot:targets&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-120)|Pointer|<pre lang="Turtle"><code>coswot:targets&#32;a&#32;owl:ObjectProperty&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;targets&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;Links&#32;a&#32;device,&#32;function,&#32;command,&#32;or&#32;procedure&#32;execution,&#32;t...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:domain&#32; &#91;&#32;a&#32;owl:Class&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:unionOf&#32;(&#32;coswot:Device&#32;coswot:Function&#32;coswot:Command&#32;coswot:ProcedureExecution&#32;)&#32;]&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32; &#60;https://w3id.org/coswot/core/devices> &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:range&#32; &#91;&#32;a&#32;owl:Class&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:unionOf&#32;(&#32;coswot:Feature&#32;coswot:Property&#32;coswot:State&#32;)&#32;]&#32;.</code></pre>|

***
### MinorFail Outcome number 121

[Jump to summary definition](#summary-MinorFail-121)	|	[Previous MinorFail outcome](#minorfail-outcome-number-120)	|	[Next MinorFail outcome](#minorfail-outcome-number-122)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-devices-ontology|
|----|----|
|Title|Standalone&#32;module&#32;core&#92;devices&#92;ontology.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- https://gitlab.com/coswot/coswot-acimov/blob/HEAD/core/devices/ontology.ttl|

#### Criterion detail
|Identifier|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|
|----|----|
|Title|Profile&#32;compatibility&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;check&#32;whether&#32;the&#32;test&#32;subject&#32;is&#32;compatible&#32;with&#32;a&#32;profile&#32;or&#32;not,&#32;and&#32;if&#32;it&#32;is&#32;not,&#32;why.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-121)|Identifier|`owl-el-profile-error`|
|[Section top](#minorfail-outcome-number-121)|Title|OWL&#32;EL&#32;Profile&#32;incompatible|
|[Section top](#minorfail-outcome-number-121)|Description|Class&#32;Expression&#32;not&#32;supported&#32;with&#32;rdfs:subClassOf|
|[Section top](#minorfail-outcome-number-121)|Pointer|<pre lang="Turtle"><code>coswot:DeviceKind&#32;a&#32;owl:Class&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;Device&#32;Kind&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;Device&#32;kinds&#32;allow&#32;to&#32;describe&#32;kinds&#32;of&#32;devices,&#32;with&#32;common...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32; &#60;https://w3id.org/coswot/core/devices> &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:subClassOf&#32; &#91;&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:allValuesFrom&#32;coswot:FeatureKind&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:onProperty&#32;skos:broader&#32;],  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#91;&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:allValuesFrom&#32;coswot:FeatureKind&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:onProperty&#32;skos:narrower&#32;],  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#91;&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:allValuesFrom&#32;owl:Nothing&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:onProperty&#32;coswot:hasKind&#32;],  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;coswot:Device,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;coswot:FeatureKind&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-121)|Pointer|<pre lang="Turtle"><code>coswot:DeviceOfInterest&#32;a&#32;owl:Class&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;Device&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;A&#32;tangible&#32;object&#32;designed&#32;to&#32;accomplish&#32;a&#32;particular&#32;task.&#32;...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32; &#60;https://w3id.org/coswot/core/devices> &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:subClassOf&#32; &#91;&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:allValuesFrom&#32;coswot:DeviceKind&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:onProperty&#32;coswot:hasKind&#32;],  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#91;&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:onProperty&#32;coswot:hasKind&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:someValuesFrom&#32;coswot:DeviceKind&#32;],  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;coswot:Device,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;coswot:FeatureOfInterest&#32;;  &#10; &#32; &#32; &#32; &#32;skos:example&#32; &#34;Examples&#32;of&#32;devices&#32;are&#32;a&#32;light&#32;switch,&#32;a&#32;temperature&#32;sensor...&#34; &#32;.</code></pre>|

***
### MinorFail Outcome number 122

[Jump to summary definition](#summary-MinorFail-122)	|	[Previous MinorFail outcome](#minorfail-outcome-number-121)	|	[Next MinorFail outcome](#minorfail-outcome-number-123)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-devices-ontology|
|----|----|
|Title|Standalone&#32;module&#32;core&#92;devices&#92;ontology.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- https://gitlab.com/coswot/coswot-acimov/blob/HEAD/core/devices/ontology.ttl|

#### Criterion detail
|Identifier|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|
|----|----|
|Title|Profile&#32;compatibility&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;check&#32;whether&#32;the&#32;test&#32;subject&#32;is&#32;compatible&#32;with&#32;a&#32;profile&#32;or&#32;not,&#32;and&#32;if&#32;it&#32;is&#32;not,&#32;why.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-122)|Identifier|`owl-el-profile-error`|
|[Section top](#minorfail-outcome-number-122)|Title|OWL&#32;EL&#32;Profile&#32;incompatible|
|[Section top](#minorfail-outcome-number-122)|Description|Statement&#32;not&#32;supported|
|[Section top](#minorfail-outcome-number-122)|Pointer|<pre lang="Turtle"><code>coswot:Device&#32;a&#32;owl:Class&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;Device&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;A&#32;tangible&#32;object&#32;designed&#32;to&#32;accomplish&#32;a&#32;particular&#32;task.&#32;...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32; &#60;https://w3id.org/coswot/core/devices> &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:subClassOf&#32;coswot:System&#32;;  &#10; &#32; &#32; &#32; &#32;owl:disjointUnionOf&#32;(&#32;coswot:DeviceOfInterest&#32;coswot:DeviceKind&#32;)&#32;;  &#10; &#32; &#32; &#32; &#32;skos:example&#32; &#34;Examples&#32;of&#32;devices&#32;are&#32;a&#32;light&#32;switch,&#32;a&#32;temperature&#32;sensor...&#34; &#32;.</code></pre>|

***
### MinorFail Outcome number 123

[Jump to summary definition](#summary-MinorFail-123)	|	[Previous MinorFail outcome](#minorfail-outcome-number-122)	|	[Next MinorFail outcome](#minorfail-outcome-number-124)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-devices-ontology|
|----|----|
|Title|Standalone&#32;module&#32;core&#92;devices&#92;ontology.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- https://gitlab.com/coswot/coswot-acimov/blob/HEAD/core/devices/ontology.ttl|

#### Criterion detail
|Identifier|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|
|----|----|
|Title|Profile&#32;compatibility&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;check&#32;whether&#32;the&#32;test&#32;subject&#32;is&#32;compatible&#32;with&#32;a&#32;profile&#32;or&#32;not,&#32;and&#32;if&#32;it&#32;is&#32;not,&#32;why.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-123)|Identifier|`owl-el-profile-error`|
|[Section top](#minorfail-outcome-number-123)|Title|OWL&#32;EL&#32;Profile&#32;incompatible|
|[Section top](#minorfail-outcome-number-123)|Description|Statement&#32;not&#32;supported&#32;in&#32;a&#32;Class&#32;Expression|
|[Section top](#minorfail-outcome-number-123)|Pointer|<pre lang="Turtle"><code>&#91;]&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32;owl:allValuesFrom&#32;coswot:FeatureKind&#32;;  &#10; &#32; &#32; &#32; &#32;owl:onProperty&#32;skos:broader&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-123)|Pointer|<pre lang="Turtle"><code>&#91;]&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32;owl:allValuesFrom&#32;coswot:FeatureKind&#32;;  &#10; &#32; &#32; &#32; &#32;owl:onProperty&#32;skos:narrower&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-123)|Pointer|<pre lang="Turtle"><code>&#91;]&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32;owl:allValuesFrom&#32;owl:Nothing&#32;;  &#10; &#32; &#32; &#32; &#32;owl:onProperty&#32;coswot:hasKind&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-123)|Pointer|<pre lang="Turtle"><code>&#91;]&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32;owl:allValuesFrom&#32;coswot:DeviceKind&#32;;  &#10; &#32; &#32; &#32; &#32;owl:onProperty&#32;coswot:hasKind&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-123)|Pointer|<pre lang="Turtle"><code>&#91;]&#32;a&#32;owl:Class&#32;;  &#10; &#32; &#32;&#32; &#32;owl:unionOf&#32;(&#32;coswot:Device&#32;coswot:Function&#32;coswot:Command&#32;coswot:ProcedureExecution&#32;)&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-123)|Pointer|<pre lang="Turtle"><code>&#91;]&#32;a&#32;owl:Class&#32;;  &#10; &#32; &#32;&#32; &#32;owl:unionOf&#32;(&#32;coswot:Feature&#32;coswot:Property&#32;coswot:State&#32;)&#32;.</code></pre>|

***
### MinorFail Outcome number 124

[Jump to summary definition](#summary-MinorFail-124)	|	[Previous MinorFail outcome](#minorfail-outcome-number-123)	|	[Next MinorFail outcome](#minorfail-outcome-number-125)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-devices-ontology|
|----|----|
|Title|Standalone&#32;module&#32;core&#92;devices&#92;ontology.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- https://gitlab.com/coswot/coswot-acimov/blob/HEAD/core/devices/ontology.ttl|

#### Criterion detail
|Identifier|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|
|----|----|
|Title|Profile&#32;compatibility&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;check&#32;whether&#32;the&#32;test&#32;subject&#32;is&#32;compatible&#32;with&#32;a&#32;profile&#32;or&#32;not,&#32;and&#32;if&#32;it&#32;is&#32;not,&#32;why.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-124)|Identifier|`owl-ql-profile-error`|
|[Section top](#minorfail-outcome-number-124)|Title|OWL&#32;QL&#32;Profile&#32;incompatible|
|[Section top](#minorfail-outcome-number-124)|Description|Class&#32;Expression&#32;not&#32;supported&#32;as&#32;object&#32;of&#32;rdfs:domain&#32;or&#32;rdfs:range|
|[Section top](#minorfail-outcome-number-124)|Pointer|<pre lang="Turtle"><code>coswot:isTargetOf&#32;a&#32;owl:ObjectProperty&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;is&#32;target&#32;of&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;Links&#32;a&#32;feature,&#32;property,&#32;or&#32;state,&#32;to&#32;the&#32;device,&#32;function...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:domain&#32; &#91;&#32;a&#32;owl:Class&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:unionOf&#32;(&#32;coswot:Feature&#32;coswot:Property&#32;coswot:State&#32;)&#32;]&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32; &#60;https://w3id.org/coswot/core/devices> &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:range&#32; &#91;&#32;a&#32;owl:Class&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:unionOf&#32;(&#32;coswot:Device&#32;coswot:Function&#32;coswot:Command&#32;coswot:ProcedureExecution&#32;)&#32;]&#32;;  &#10; &#32; &#32; &#32; &#32;owl:inverseOf&#32;coswot:targets&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-124)|Pointer|<pre lang="Turtle"><code>coswot:targets&#32;a&#32;owl:ObjectProperty&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;targets&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;Links&#32;a&#32;device,&#32;function,&#32;command,&#32;or&#32;procedure&#32;execution,&#32;t...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:domain&#32; &#91;&#32;a&#32;owl:Class&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:unionOf&#32;(&#32;coswot:Device&#32;coswot:Function&#32;coswot:Command&#32;coswot:ProcedureExecution&#32;)&#32;]&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32; &#60;https://w3id.org/coswot/core/devices> &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:range&#32; &#91;&#32;a&#32;owl:Class&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:unionOf&#32;(&#32;coswot:Feature&#32;coswot:Property&#32;coswot:State&#32;)&#32;]&#32;.</code></pre>|

***
### MinorFail Outcome number 125

[Jump to summary definition](#summary-MinorFail-125)	|	[Previous MinorFail outcome](#minorfail-outcome-number-124)	|	[Next MinorFail outcome](#minorfail-outcome-number-126)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-devices-ontology|
|----|----|
|Title|Standalone&#32;module&#32;core&#92;devices&#92;ontology.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- https://gitlab.com/coswot/coswot-acimov/blob/HEAD/core/devices/ontology.ttl|

#### Criterion detail
|Identifier|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|
|----|----|
|Title|Profile&#32;compatibility&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;check&#32;whether&#32;the&#32;test&#32;subject&#32;is&#32;compatible&#32;with&#32;a&#32;profile&#32;or&#32;not,&#32;and&#32;if&#32;it&#32;is&#32;not,&#32;why.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-125)|Identifier|`owl-ql-profile-error`|
|[Section top](#minorfail-outcome-number-125)|Title|OWL&#32;QL&#32;Profile&#32;incompatible|
|[Section top](#minorfail-outcome-number-125)|Description|Class&#32;Expression&#32;not&#32;supported&#32;with&#32;rdfs:subClassOf|
|[Section top](#minorfail-outcome-number-125)|Pointer|<pre lang="Turtle"><code>coswot:DeviceKind&#32;a&#32;owl:Class&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;Device&#32;Kind&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;Device&#32;kinds&#32;allow&#32;to&#32;describe&#32;kinds&#32;of&#32;devices,&#32;with&#32;common...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32; &#60;https://w3id.org/coswot/core/devices> &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:subClassOf&#32; &#91;&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:allValuesFrom&#32;coswot:FeatureKind&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:onProperty&#32;skos:broader&#32;],  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#91;&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:allValuesFrom&#32;coswot:FeatureKind&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:onProperty&#32;skos:narrower&#32;],  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#91;&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:allValuesFrom&#32;owl:Nothing&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:onProperty&#32;coswot:hasKind&#32;],  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;coswot:Device,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;coswot:FeatureKind&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-125)|Pointer|<pre lang="Turtle"><code>coswot:DeviceOfInterest&#32;a&#32;owl:Class&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;Device&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;A&#32;tangible&#32;object&#32;designed&#32;to&#32;accomplish&#32;a&#32;particular&#32;task.&#32;...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32; &#60;https://w3id.org/coswot/core/devices> &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:subClassOf&#32; &#91;&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:allValuesFrom&#32;coswot:DeviceKind&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:onProperty&#32;coswot:hasKind&#32;],  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#91;&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:onProperty&#32;coswot:hasKind&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:someValuesFrom&#32;coswot:DeviceKind&#32;],  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;coswot:Device,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;coswot:FeatureOfInterest&#32;;  &#10; &#32; &#32; &#32; &#32;skos:example&#32; &#34;Examples&#32;of&#32;devices&#32;are&#32;a&#32;light&#32;switch,&#32;a&#32;temperature&#32;sensor...&#34; &#32;.</code></pre>|

***
### MinorFail Outcome number 126

[Jump to summary definition](#summary-MinorFail-126)	|	[Previous MinorFail outcome](#minorfail-outcome-number-125)	|	[Next MinorFail outcome](#minorfail-outcome-number-127)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-devices-ontology|
|----|----|
|Title|Standalone&#32;module&#32;core&#92;devices&#92;ontology.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- https://gitlab.com/coswot/coswot-acimov/blob/HEAD/core/devices/ontology.ttl|

#### Criterion detail
|Identifier|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|
|----|----|
|Title|Profile&#32;compatibility&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;check&#32;whether&#32;the&#32;test&#32;subject&#32;is&#32;compatible&#32;with&#32;a&#32;profile&#32;or&#32;not,&#32;and&#32;if&#32;it&#32;is&#32;not,&#32;why.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-126)|Identifier|`owl-ql-profile-error`|
|[Section top](#minorfail-outcome-number-126)|Title|OWL&#32;QL&#32;Profile&#32;incompatible|
|[Section top](#minorfail-outcome-number-126)|Description|Statement&#32;not&#32;supported|
|[Section top](#minorfail-outcome-number-126)|Pointer|<pre lang="Turtle"><code>coswot:Device&#32;a&#32;owl:Class&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;Device&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;A&#32;tangible&#32;object&#32;designed&#32;to&#32;accomplish&#32;a&#32;particular&#32;task.&#32;...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32; &#60;https://w3id.org/coswot/core/devices> &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:subClassOf&#32;coswot:System&#32;;  &#10; &#32; &#32; &#32; &#32;owl:disjointUnionOf&#32;(&#32;coswot:DeviceOfInterest&#32;coswot:DeviceKind&#32;)&#32;;  &#10; &#32; &#32; &#32; &#32;skos:example&#32; &#34;Examples&#32;of&#32;devices&#32;are&#32;a&#32;light&#32;switch,&#32;a&#32;temperature&#32;sensor...&#34; &#32;.</code></pre>|

***
### MinorFail Outcome number 127

[Jump to summary definition](#summary-MinorFail-127)	|	[Previous MinorFail outcome](#minorfail-outcome-number-126)	|	[Next MinorFail outcome](#minorfail-outcome-number-128)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-devices-ontology|
|----|----|
|Title|Standalone&#32;module&#32;core&#92;devices&#92;ontology.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- https://gitlab.com/coswot/coswot-acimov/blob/HEAD/core/devices/ontology.ttl|

#### Criterion detail
|Identifier|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|
|----|----|
|Title|Profile&#32;compatibility&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;check&#32;whether&#32;the&#32;test&#32;subject&#32;is&#32;compatible&#32;with&#32;a&#32;profile&#32;or&#32;not,&#32;and&#32;if&#32;it&#32;is&#32;not,&#32;why.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-127)|Identifier|`owl-ql-profile-error`|
|[Section top](#minorfail-outcome-number-127)|Title|OWL&#32;QL&#32;Profile&#32;incompatible|
|[Section top](#minorfail-outcome-number-127)|Description|Statement&#32;not&#32;supported&#32;in&#32;a&#32;Super&#32;Class&#32;Expression|
|[Section top](#minorfail-outcome-number-127)|Pointer|<pre lang="Turtle"><code>&#91;]&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32;owl:allValuesFrom&#32;coswot:FeatureKind&#32;;  &#10; &#32; &#32; &#32; &#32;owl:onProperty&#32;skos:broader&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-127)|Pointer|<pre lang="Turtle"><code>&#91;]&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32;owl:allValuesFrom&#32;coswot:FeatureKind&#32;;  &#10; &#32; &#32; &#32; &#32;owl:onProperty&#32;skos:narrower&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-127)|Pointer|<pre lang="Turtle"><code>&#91;]&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32;owl:allValuesFrom&#32;owl:Nothing&#32;;  &#10; &#32; &#32; &#32; &#32;owl:onProperty&#32;coswot:hasKind&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-127)|Pointer|<pre lang="Turtle"><code>&#91;]&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32;owl:allValuesFrom&#32;coswot:DeviceKind&#32;;  &#10; &#32; &#32; &#32; &#32;owl:onProperty&#32;coswot:hasKind&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-127)|Pointer|<pre lang="Turtle"><code>&#91;]&#32;a&#32;owl:Class&#32;;  &#10; &#32; &#32;&#32; &#32;owl:unionOf&#32;(&#32;coswot:Device&#32;coswot:Function&#32;coswot:Command&#32;coswot:ProcedureExecution&#32;)&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-127)|Pointer|<pre lang="Turtle"><code>&#91;]&#32;a&#32;owl:Class&#32;;  &#10; &#32; &#32;&#32; &#32;owl:unionOf&#32;(&#32;coswot:Feature&#32;coswot:Property&#32;coswot:State&#32;)&#32;.</code></pre>|

***
### MinorFail Outcome number 128

[Jump to summary definition](#summary-MinorFail-128)	|	[Previous MinorFail outcome](#minorfail-outcome-number-127)	|	[Next MinorFail outcome](#minorfail-outcome-number-129)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-devices-ontology|
|----|----|
|Title|Standalone&#32;module&#32;core&#92;devices&#92;ontology.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- https://gitlab.com/coswot/coswot-acimov/blob/HEAD/core/devices/ontology.ttl|

#### Criterion detail
|Identifier|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|
|----|----|
|Title|Profile&#32;compatibility&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;check&#32;whether&#32;the&#32;test&#32;subject&#32;is&#32;compatible&#32;with&#32;a&#32;profile&#32;or&#32;not,&#32;and&#32;if&#32;it&#32;is&#32;not,&#32;why.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-128)|Identifier|`owl-rl-profile-error`|
|[Section top](#minorfail-outcome-number-128)|Title|OWL&#32;RL&#32;Profile&#32;incompatible|
|[Section top](#minorfail-outcome-number-128)|Description|Class&#32;Expression&#32;not&#32;supported&#32;as&#32;object&#32;of&#32;rdfs:domain&#32;or&#32;rdfs:range|
|[Section top](#minorfail-outcome-number-128)|Pointer|<pre lang="Turtle"><code>coswot:isTargetOf&#32;a&#32;owl:ObjectProperty&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;is&#32;target&#32;of&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;Links&#32;a&#32;feature,&#32;property,&#32;or&#32;state,&#32;to&#32;the&#32;device,&#32;function...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:domain&#32; &#91;&#32;a&#32;owl:Class&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:unionOf&#32;(&#32;coswot:Feature&#32;coswot:Property&#32;coswot:State&#32;)&#32;]&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32; &#60;https://w3id.org/coswot/core/devices> &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:range&#32; &#91;&#32;a&#32;owl:Class&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:unionOf&#32;(&#32;coswot:Device&#32;coswot:Function&#32;coswot:Command&#32;coswot:ProcedureExecution&#32;)&#32;]&#32;;  &#10; &#32; &#32; &#32; &#32;owl:inverseOf&#32;coswot:targets&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-128)|Pointer|<pre lang="Turtle"><code>coswot:targets&#32;a&#32;owl:ObjectProperty&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;targets&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;Links&#32;a&#32;device,&#32;function,&#32;command,&#32;or&#32;procedure&#32;execution,&#32;t...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:domain&#32; &#91;&#32;a&#32;owl:Class&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:unionOf&#32;(&#32;coswot:Device&#32;coswot:Function&#32;coswot:Command&#32;coswot:ProcedureExecution&#32;)&#32;]&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32; &#60;https://w3id.org/coswot/core/devices> &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:range&#32; &#91;&#32;a&#32;owl:Class&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:unionOf&#32;(&#32;coswot:Feature&#32;coswot:Property&#32;coswot:State&#32;)&#32;]&#32;.</code></pre>|

***
### MinorFail Outcome number 129

[Jump to summary definition](#summary-MinorFail-129)	|	[Previous MinorFail outcome](#minorfail-outcome-number-128)	|	[Next MinorFail outcome](#minorfail-outcome-number-130)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-devices-ontology|
|----|----|
|Title|Standalone&#32;module&#32;core&#92;devices&#92;ontology.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- https://gitlab.com/coswot/coswot-acimov/blob/HEAD/core/devices/ontology.ttl|

#### Criterion detail
|Identifier|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|
|----|----|
|Title|Profile&#32;compatibility&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;check&#32;whether&#32;the&#32;test&#32;subject&#32;is&#32;compatible&#32;with&#32;a&#32;profile&#32;or&#32;not,&#32;and&#32;if&#32;it&#32;is&#32;not,&#32;why.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-129)|Identifier|`owl-rl-profile-error`|
|[Section top](#minorfail-outcome-number-129)|Title|OWL&#32;RL&#32;Profile&#32;incompatible|
|[Section top](#minorfail-outcome-number-129)|Description|Class&#32;Expression&#32;not&#32;supported&#32;with&#32;rdfs:subClassOf|
|[Section top](#minorfail-outcome-number-129)|Pointer|<pre lang="Turtle"><code>coswot:DeviceOfInterest&#32;a&#32;owl:Class&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;Device&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;A&#32;tangible&#32;object&#32;designed&#32;to&#32;accomplish&#32;a&#32;particular&#32;task.&#32;...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32; &#60;https://w3id.org/coswot/core/devices> &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:subClassOf&#32; &#91;&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:allValuesFrom&#32;coswot:DeviceKind&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:onProperty&#32;coswot:hasKind&#32;],  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#91;&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:onProperty&#32;coswot:hasKind&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:someValuesFrom&#32;coswot:DeviceKind&#32;],  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;coswot:Device,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;coswot:FeatureOfInterest&#32;;  &#10; &#32; &#32; &#32; &#32;skos:example&#32; &#34;Examples&#32;of&#32;devices&#32;are&#32;a&#32;light&#32;switch,&#32;a&#32;temperature&#32;sensor...&#34; &#32;.</code></pre>|

***
### MinorFail Outcome number 130

[Jump to summary definition](#summary-MinorFail-130)	|	[Previous MinorFail outcome](#minorfail-outcome-number-129)	|	[Next MinorFail outcome](#minorfail-outcome-number-131)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-devices-ontology|
|----|----|
|Title|Standalone&#32;module&#32;core&#92;devices&#92;ontology.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- https://gitlab.com/coswot/coswot-acimov/blob/HEAD/core/devices/ontology.ttl|

#### Criterion detail
|Identifier|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|
|----|----|
|Title|Profile&#32;compatibility&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;check&#32;whether&#32;the&#32;test&#32;subject&#32;is&#32;compatible&#32;with&#32;a&#32;profile&#32;or&#32;not,&#32;and&#32;if&#32;it&#32;is&#32;not,&#32;why.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-130)|Identifier|`owl-rl-profile-error`|
|[Section top](#minorfail-outcome-number-130)|Title|OWL&#32;RL&#32;Profile&#32;incompatible|
|[Section top](#minorfail-outcome-number-130)|Description|Statement&#32;not&#32;supported|
|[Section top](#minorfail-outcome-number-130)|Pointer|<pre lang="Turtle"><code>coswot:Device&#32;a&#32;owl:Class&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;Device&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;A&#32;tangible&#32;object&#32;designed&#32;to&#32;accomplish&#32;a&#32;particular&#32;task.&#32;...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32; &#60;https://w3id.org/coswot/core/devices> &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:subClassOf&#32;coswot:System&#32;;  &#10; &#32; &#32; &#32; &#32;owl:disjointUnionOf&#32;(&#32;coswot:DeviceOfInterest&#32;coswot:DeviceKind&#32;)&#32;;  &#10; &#32; &#32; &#32; &#32;skos:example&#32; &#34;Examples&#32;of&#32;devices&#32;are&#32;a&#32;light&#32;switch,&#32;a&#32;temperature&#32;sensor...&#34; &#32;.</code></pre>|

***
### MinorFail Outcome number 131

[Jump to summary definition](#summary-MinorFail-131)	|	[Previous MinorFail outcome](#minorfail-outcome-number-130)	|	[Next MinorFail outcome](#minorfail-outcome-number-132)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-devices-ontology|
|----|----|
|Title|Standalone&#32;module&#32;core&#92;devices&#92;ontology.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- https://gitlab.com/coswot/coswot-acimov/blob/HEAD/core/devices/ontology.ttl|

#### Criterion detail
|Identifier|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|
|----|----|
|Title|Profile&#32;compatibility&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;check&#32;whether&#32;the&#32;test&#32;subject&#32;is&#32;compatible&#32;with&#32;a&#32;profile&#32;or&#32;not,&#32;and&#32;if&#32;it&#32;is&#32;not,&#32;why.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-131)|Identifier|`owl-rl-profile-error`|
|[Section top](#minorfail-outcome-number-131)|Title|OWL&#32;RL&#32;Profile&#32;incompatible|
|[Section top](#minorfail-outcome-number-131)|Description|Statement&#32;not&#32;supported&#32;in&#32;a&#32;Super&#32;Class&#32;Expression|
|[Section top](#minorfail-outcome-number-131)|Pointer|<pre lang="Turtle"><code>&#91;]&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32;owl:onProperty&#32;coswot:hasKind&#32;;  &#10; &#32; &#32; &#32; &#32;owl:someValuesFrom&#32;coswot:DeviceKind&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-131)|Pointer|<pre lang="Turtle"><code>&#91;]&#32;a&#32;owl:Class&#32;;  &#10; &#32; &#32;&#32; &#32;owl:unionOf&#32;(&#32;coswot:Device&#32;coswot:Function&#32;coswot:Command&#32;coswot:ProcedureExecution&#32;)&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-131)|Pointer|<pre lang="Turtle"><code>&#91;]&#32;a&#32;owl:Class&#32;;  &#10; &#32; &#32;&#32; &#32;owl:unionOf&#32;(&#32;coswot:Feature&#32;coswot:Property&#32;coswot:State&#32;)&#32;.</code></pre>|

***
### MinorFail Outcome number 132

[Jump to summary definition](#summary-MinorFail-132)	|	[Previous MinorFail outcome](#minorfail-outcome-number-131)	|	[Next MinorFail outcome](#minorfail-outcome-number-133)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-coswot-sosa|
|----|----|
|Title|Standalone&#32;module&#32;core&#92;coswot-sosa.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- https://gitlab.com/coswot/coswot-acimov/blob/HEAD/core/coswot-sosa.ttl|

#### Criterion detail
|Identifier|[term-referencing](https://ns.inria.fr/olivaw#term-referencing)|
|----|----|
|Title|Term&#32;referencing&#32;test|
|Description|A&#32;test&#32;case&#32;from&#32;the&#32;Best&#32;Practices&#32;tests&#32;checking&#32;if&#32;each&#32;term&#32;of&#32;the&#32;test&#32;subject&#32;is&#32;referenced&#32;to&#32;a&#32;module&#32;through&#32;a&#32;rdfs:isDefinedBy&#32;property.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-132)|Identifier|`no-reference-module`|
|[Section top](#minorfail-outcome-number-132)|Title|Term&#32;not&#32;referenced&#32;to&#32;a&#32;module|
|[Section top](#minorfail-outcome-number-132)|Description|Subject&#32;terms&#32;not&#32;linked&#32;to&#32;a&#32;module&#32;by&#32;a&#32;rdfs:isDefinedBy&#32;property|
|[Section top](#minorfail-outcome-number-132)|Pointer|<pre lang="Turtle"><code>:hasResult&#32;rdfs:equivalentProperty&#32;sosa:hasResult&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-132)|Pointer|<pre lang="Turtle"><code>:SensorOfInterest&#32;rdfs:subClassOf&#32;sosa:Sensor&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-132)|Pointer|<pre lang="Turtle"><code>:Observation&#32;rdfs:subClassOf&#32;sosa:Observation&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-132)|Pointer|<pre lang="Turtle"><code>:CommunicationSystem&#32;rdfs:subClassOf&#32;sosa:System&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-132)|Pointer|<pre lang="Turtle"><code>:hasStartTime&#32;rdfs:subPropertyOf&#32;sosa:startTime&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-132)|Pointer|<pre lang="Turtle"><code>:hasResultTime&#32;rdfs:subPropertyOf&#32;sosa:resultTime&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-132)|Pointer|<pre lang="Turtle"><code>:hasPhenomenonTime&#32;rdfs:subPropertyOf&#32;sosa:phenomenonTime&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-132)|Pointer|<pre lang="Turtle"><code>:FeatureOfInterest&#32;owl:equivalentClass&#32;sosa:FeatureOfInterest&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-132)|Pointer|<pre lang="Turtle"><code>:PropertyOfInterest&#32;owl:equivalentClass&#32;sosa:PropertyOfInterest&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-132)|Pointer|<pre lang="Turtle"><code>:Sample&#32;owl:equivalentClass&#32;sosa:Sample&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-132)|Pointer|<pre lang="Turtle"><code>:PropertyKind&#32;owl:equivalentClass&#32;sosa:Property&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-132)|Pointer|<pre lang="Turtle"><code>:Procedure&#32;owl:equivalentClass&#32;sosa:Procedure&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-132)|Pointer|<pre lang="Turtle"><code>:ProcedureExecution&#32;owl:equivalentClass&#32;sosa:Execution&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-132)|Pointer|<pre lang="Turtle"><code>:ObservationCollection&#32;owl:equivalentClass&#32;sosa:ObservationCollection&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-132)|Pointer|<pre lang="Turtle"><code>:ActuatorOfInterest&#32;owl:equivalentClass&#32;sosa:Actuator&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-132)|Pointer|<pre lang="Turtle"><code>:SensorKind&#32;owl:equivalentClass&#32;sosa:SensorKind&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-132)|Pointer|<pre lang="Turtle"><code>:ActuatorKind&#32;owl:equivalentClass&#32;sosa:ActuatorKind&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-132)|Pointer|<pre lang="Turtle"><code>:Actuation&#32;owl:equivalentClass&#32;sosa:Actuation&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-132)|Pointer|<pre lang="Turtle"><code>:hasSample&#32;owl:equivalentProperty&#32;sosa:Sample&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-132)|Pointer|<pre lang="Turtle"><code>:isSampleOf&#32;owl:equivalentProperty&#32;sosa:isSampleOf&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-132)|Pointer|<pre lang="Turtle"><code>:hasMember&#32;owl:equivalentProperty&#32;sosa:hasMember&#32;.</code></pre>|

***
### MinorFail Outcome number 133

[Jump to summary definition](#summary-MinorFail-133)	|	[Previous MinorFail outcome](#minorfail-outcome-number-132)	|	[Next MinorFail outcome](#minorfail-outcome-number-134)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-communications-ontology|
|----|----|
|Title|Standalone&#32;module&#32;core&#92;communications&#92;ontology.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- https://gitlab.com/coswot/coswot-acimov/blob/HEAD/core/communications/ontology.ttl|

#### Criterion detail
|Identifier|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|
|----|----|
|Title|Profile&#32;compatibility&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;check&#32;whether&#32;the&#32;test&#32;subject&#32;is&#32;compatible&#32;with&#32;a&#32;profile&#32;or&#32;not,&#32;and&#32;if&#32;it&#32;is&#32;not,&#32;why.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-133)|Identifier|`owl-el-profile-error`|
|[Section top](#minorfail-outcome-number-133)|Title|OWL&#32;EL&#32;Profile&#32;incompatible|
|[Section top](#minorfail-outcome-number-133)|Description|Class&#32;Expression&#32;not&#32;supported&#32;with&#32;rdfs:subClassOf|
|[Section top](#minorfail-outcome-number-133)|Pointer|<pre lang="Turtle"><code>coswot:Communication&#32;a&#32;owl:Class&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;Communication.&#34;@en,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#34;Communication&#34;@fr&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;A&#32;communication&#32;occurs&#32;through&#32;a&#32;communicationMedium,&#32;convey...&#34;,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#34;une&#32;communication&#32;est&#32;produite&#32;à&#32;travers&#32;un&#32;média&#32;de&#32;communi...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32; &#60;https://w3id.org/coswot/core/communications> &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:subClassOf&#32; &#91;&#32;owl:onProperty&#32;coswot:conveys&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:someValuesFrom&#32;coswot:Message&#32;],  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#91;&#32;owl:onProperty&#32;coswot:hasMedium&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:someValuesFrom&#32;coswot:CommunicationMedium&#32;],  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#91;&#32;owl:onProperty&#32;coswot:hasCommunicator&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:someValuesFrom&#32;coswot:CommunicationSystem&#32;],  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#91;&#32;owl:onProperty&#32;coswot:hasCommunicator&#32;],  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#91;&#32;owl:onProperty&#32;coswot:hasAddressee&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:someValuesFrom&#32;coswot:CommunicationSystem&#32;],  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#91;&#32;owl:onProperty&#32;coswot:isAbout&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:someValuesFrom&#32;xsd:string&#32;],  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;coswot:ProcedureExecution&#32;.</code></pre>|

***
### MinorFail Outcome number 134

[Jump to summary definition](#summary-MinorFail-134)	|	[Previous MinorFail outcome](#minorfail-outcome-number-133)	|	[Next MinorFail outcome](#minorfail-outcome-number-135)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-communications-ontology|
|----|----|
|Title|Standalone&#32;module&#32;core&#92;communications&#92;ontology.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- https://gitlab.com/coswot/coswot-acimov/blob/HEAD/core/communications/ontology.ttl|

#### Criterion detail
|Identifier|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|
|----|----|
|Title|Profile&#32;compatibility&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;check&#32;whether&#32;the&#32;test&#32;subject&#32;is&#32;compatible&#32;with&#32;a&#32;profile&#32;or&#32;not,&#32;and&#32;if&#32;it&#32;is&#32;not,&#32;why.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-134)|Identifier|`owl-el-profile-error`|
|[Section top](#minorfail-outcome-number-134)|Title|OWL&#32;EL&#32;Profile&#32;incompatible|
|[Section top](#minorfail-outcome-number-134)|Description|Statement&#32;not&#32;supported&#32;in&#32;a&#32;Class&#32;Expression|
|[Section top](#minorfail-outcome-number-134)|Pointer|<pre lang="Turtle"><code>&#91;]&#32;owl:onProperty&#32;coswot:hasCommunicator&#32;.</code></pre>|

***
### MinorFail Outcome number 135

[Jump to summary definition](#summary-MinorFail-135)	|	[Previous MinorFail outcome](#minorfail-outcome-number-134)	|	[Next MinorFail outcome](#minorfail-outcome-number-136)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-communications-ontology|
|----|----|
|Title|Standalone&#32;module&#32;core&#92;communications&#92;ontology.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- https://gitlab.com/coswot/coswot-acimov/blob/HEAD/core/communications/ontology.ttl|

#### Criterion detail
|Identifier|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|
|----|----|
|Title|Profile&#32;compatibility&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;check&#32;whether&#32;the&#32;test&#32;subject&#32;is&#32;compatible&#32;with&#32;a&#32;profile&#32;or&#32;not,&#32;and&#32;if&#32;it&#32;is&#32;not,&#32;why.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-135)|Identifier|`owl-ql-profile-error`|
|[Section top](#minorfail-outcome-number-135)|Title|OWL&#32;QL&#32;Profile&#32;incompatible|
|[Section top](#minorfail-outcome-number-135)|Description|Class&#32;Expression&#32;not&#32;supported&#32;with&#32;rdfs:subClassOf|
|[Section top](#minorfail-outcome-number-135)|Pointer|<pre lang="Turtle"><code>coswot:Communication&#32;a&#32;owl:Class&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;Communication.&#34;@en,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#34;Communication&#34;@fr&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;A&#32;communication&#32;occurs&#32;through&#32;a&#32;communicationMedium,&#32;convey...&#34;,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#34;une&#32;communication&#32;est&#32;produite&#32;à&#32;travers&#32;un&#32;média&#32;de&#32;communi...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32; &#60;https://w3id.org/coswot/core/communications> &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:subClassOf&#32; &#91;&#32;owl:onProperty&#32;coswot:conveys&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:someValuesFrom&#32;coswot:Message&#32;],  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#91;&#32;owl:onProperty&#32;coswot:hasMedium&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:someValuesFrom&#32;coswot:CommunicationMedium&#32;],  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#91;&#32;owl:onProperty&#32;coswot:hasCommunicator&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:someValuesFrom&#32;coswot:CommunicationSystem&#32;],  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#91;&#32;owl:onProperty&#32;coswot:hasCommunicator&#32;],  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#91;&#32;owl:onProperty&#32;coswot:hasAddressee&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:someValuesFrom&#32;coswot:CommunicationSystem&#32;],  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#91;&#32;owl:onProperty&#32;coswot:isAbout&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:someValuesFrom&#32;xsd:string&#32;],  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;coswot:ProcedureExecution&#32;.</code></pre>|

***
### MinorFail Outcome number 136

[Jump to summary definition](#summary-MinorFail-136)	|	[Previous MinorFail outcome](#minorfail-outcome-number-135)	|	[Next MinorFail outcome](#minorfail-outcome-number-137)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-communications-ontology|
|----|----|
|Title|Standalone&#32;module&#32;core&#92;communications&#92;ontology.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- https://gitlab.com/coswot/coswot-acimov/blob/HEAD/core/communications/ontology.ttl|

#### Criterion detail
|Identifier|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|
|----|----|
|Title|Profile&#32;compatibility&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;check&#32;whether&#32;the&#32;test&#32;subject&#32;is&#32;compatible&#32;with&#32;a&#32;profile&#32;or&#32;not,&#32;and&#32;if&#32;it&#32;is&#32;not,&#32;why.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-136)|Identifier|`owl-ql-profile-error`|
|[Section top](#minorfail-outcome-number-136)|Title|OWL&#32;QL&#32;Profile&#32;incompatible|
|[Section top](#minorfail-outcome-number-136)|Description|Statement&#32;not&#32;supported&#32;in&#32;a&#32;Super&#32;Class&#32;Expression|
|[Section top](#minorfail-outcome-number-136)|Pointer|<pre lang="Turtle"><code>&#91;]&#32;owl:onProperty&#32;coswot:hasCommunicator&#32;.</code></pre>|

***
### MinorFail Outcome number 137

[Jump to summary definition](#summary-MinorFail-137)	|	[Previous MinorFail outcome](#minorfail-outcome-number-136)	|	[Next MinorFail outcome](#minorfail-outcome-number-138)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-communications-ontology|
|----|----|
|Title|Standalone&#32;module&#32;core&#92;communications&#92;ontology.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- https://gitlab.com/coswot/coswot-acimov/blob/HEAD/core/communications/ontology.ttl|

#### Criterion detail
|Identifier|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|
|----|----|
|Title|Profile&#32;compatibility&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;check&#32;whether&#32;the&#32;test&#32;subject&#32;is&#32;compatible&#32;with&#32;a&#32;profile&#32;or&#32;not,&#32;and&#32;if&#32;it&#32;is&#32;not,&#32;why.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-137)|Identifier|`owl-rl-profile-error`|
|[Section top](#minorfail-outcome-number-137)|Title|OWL&#32;RL&#32;Profile&#32;incompatible|
|[Section top](#minorfail-outcome-number-137)|Description|Class&#32;Expression&#32;not&#32;supported&#32;with&#32;rdfs:subClassOf|
|[Section top](#minorfail-outcome-number-137)|Pointer|<pre lang="Turtle"><code>coswot:Communication&#32;a&#32;owl:Class&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;Communication.&#34;@en,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#34;Communication&#34;@fr&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;A&#32;communication&#32;occurs&#32;through&#32;a&#32;communicationMedium,&#32;convey...&#34;,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#34;une&#32;communication&#32;est&#32;produite&#32;à&#32;travers&#32;un&#32;média&#32;de&#32;communi...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32; &#60;https://w3id.org/coswot/core/communications> &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:subClassOf&#32; &#91;&#32;owl:onProperty&#32;coswot:conveys&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:someValuesFrom&#32;coswot:Message&#32;],  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#91;&#32;owl:onProperty&#32;coswot:hasMedium&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:someValuesFrom&#32;coswot:CommunicationMedium&#32;],  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#91;&#32;owl:onProperty&#32;coswot:hasCommunicator&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:someValuesFrom&#32;coswot:CommunicationSystem&#32;],  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#91;&#32;owl:onProperty&#32;coswot:hasCommunicator&#32;],  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#91;&#32;owl:onProperty&#32;coswot:hasAddressee&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:someValuesFrom&#32;coswot:CommunicationSystem&#32;],  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#91;&#32;owl:onProperty&#32;coswot:isAbout&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:someValuesFrom&#32;xsd:string&#32;],  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;coswot:ProcedureExecution&#32;.</code></pre>|

***
### MinorFail Outcome number 138

[Jump to summary definition](#summary-MinorFail-138)	|	[Previous MinorFail outcome](#minorfail-outcome-number-137)	|	[Next MinorFail outcome](#minorfail-outcome-number-139)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-communications-ontology|
|----|----|
|Title|Standalone&#32;module&#32;core&#92;communications&#92;ontology.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- https://gitlab.com/coswot/coswot-acimov/blob/HEAD/core/communications/ontology.ttl|

#### Criterion detail
|Identifier|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|
|----|----|
|Title|Profile&#32;compatibility&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;check&#32;whether&#32;the&#32;test&#32;subject&#32;is&#32;compatible&#32;with&#32;a&#32;profile&#32;or&#32;not,&#32;and&#32;if&#32;it&#32;is&#32;not,&#32;why.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-138)|Identifier|`owl-rl-profile-error`|
|[Section top](#minorfail-outcome-number-138)|Title|OWL&#32;RL&#32;Profile&#32;incompatible|
|[Section top](#minorfail-outcome-number-138)|Description|Statement&#32;not&#32;supported&#32;in&#32;a&#32;Super&#32;Class&#32;Expression|
|[Section top](#minorfail-outcome-number-138)|Pointer|<pre lang="Turtle"><code>&#91;]&#32;owl:onProperty&#32;coswot:conveys&#32;;  &#10; &#32; &#32;&#32; &#32;owl:someValuesFrom&#32;coswot:Message&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-138)|Pointer|<pre lang="Turtle"><code>&#91;]&#32;owl:onProperty&#32;coswot:hasMedium&#32;;  &#10; &#32; &#32;&#32; &#32;owl:someValuesFrom&#32;coswot:CommunicationMedium&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-138)|Pointer|<pre lang="Turtle"><code>&#91;]&#32;owl:onProperty&#32;coswot:hasCommunicator&#32;;  &#10; &#32; &#32;&#32; &#32;owl:someValuesFrom&#32;coswot:CommunicationSystem&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-138)|Pointer|<pre lang="Turtle"><code>&#91;]&#32;owl:onProperty&#32;coswot:hasCommunicator&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-138)|Pointer|<pre lang="Turtle"><code>&#91;]&#32;owl:onProperty&#32;coswot:hasAddressee&#32;;  &#10; &#32; &#32;&#32; &#32;owl:someValuesFrom&#32;coswot:CommunicationSystem&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-138)|Pointer|<pre lang="Turtle"><code>&#91;]&#32;owl:onProperty&#32;coswot:isAbout&#32;;  &#10; &#32; &#32;&#32; &#32;owl:someValuesFrom&#32;xsd:string&#32;.</code></pre>|

***
### MinorFail Outcome number 139

[Jump to summary definition](#summary-MinorFail-139)	|	[Previous MinorFail outcome](#minorfail-outcome-number-138)	|	[Next MinorFail outcome](#minorfail-outcome-number-140)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-aggregations-ontology|
|----|----|
|Title|Standalone&#32;module&#32;core&#92;aggregations&#92;ontology.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- https://gitlab.com/coswot/coswot-acimov/blob/HEAD/core/aggregations/ontology.ttl|

#### Criterion detail
|Identifier|[domain-and-range-referencing](https://ns.inria.fr/olivaw#domain-and-range-referencing)|
|----|----|
|Title|Domain&#32;and&#32;range&#32;referencing&#32;test|
|Description|A&#32;test&#32;case&#32;from&#32;the&#32;Best&#32;Practices&#32;tests&#32;checking&#32;if&#32;all&#32;the&#32;ranges&#32;and&#32;domains&#32;from&#32;the&#32;test&#32;subject&#32;point&#32;to&#32;terms&#32;that&#32;are&#32;defined&#32;in&#32;the&#32;vocabulary.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-139)|Identifier|`range-out-of-vocabulary`|
|[Section top](#minorfail-outcome-number-139)|Title|Range&#32;out&#32;of&#32;vocabulary|
|[Section top](#minorfail-outcome-number-139)|Description|Some&#32;properties&#32;have&#32;a&#32;range&#32;out&#32;of&#32;the&#32;ontology|
|[Section top](#minorfail-outcome-number-139)|Pointer|<pre lang="Turtle"><code>:hasAggregationKind&#32;a&#32;owl:ObjectProperty&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;has&#32;aggregation&#32;kind&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;Links&#32;a&#32;property,&#32;state,&#32;or&#32;aggregation,&#32;to&#32;the&#32;kind&#32;of&#32;aggr...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:domain&#32; &#91;&#32;a&#32;owl:Class&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:unionOf&#32;(&#32;:Property&#32;:State&#32;:Aggregation&#32;)&#32;]&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32; &#60;https://w3id.org/coswot/core/aggregations> &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:range&#32; &#91;&#32;a&#32;owl:Class&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:unionOf&#32;(&#32;:Property&#32;:State&#32;:Aggregation&#32;:AggregationKind&#32;)&#32;],  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;skos:Concept,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;:AggregationKind&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-139)|Pointer|<pre lang="Turtle"><code>:hasAggregationTime&#32;a&#32;owl:ObjectProperty&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;has&#32;aggregation&#32;time&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;Links&#32;a&#32;property,&#32;state,&#32;aggregation,&#32;or&#32;aggregation&#32;kind,&#32;t...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:domain&#32; &#91;&#32;a&#32;owl:Class&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:unionOf&#32;(&#32;:Property&#32;:State&#32;:Aggregation&#32;:AggregationKind&#32;)&#32;]&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32; &#60;https://w3id.org/coswot/core/aggregations> &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:range&#32;time:TemporalInterval&#32;;  &#10; &#32; &#32; &#32; &#32;owl:propertyChainAxiom&#32;(&#32;:hasAggregationKind&#32;:hasAggregationTime&#32;)&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-139)|Pointer|<pre lang="Turtle"><code>http://www.w3.org/2006/time#TemporalInterval</code></pre>|
|[Section top](#minorfail-outcome-number-139)|Pointer|http://www.w3.org/2004/02/skos/core#Concept|

***
### MinorFail Outcome number 140

[Jump to summary definition](#summary-MinorFail-140)	|	[Previous MinorFail outcome](#minorfail-outcome-number-139)	|	[Next MinorFail outcome](#minorfail-outcome-number-141)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-aggregations-ontology|
|----|----|
|Title|Standalone&#32;module&#32;core&#92;aggregations&#92;ontology.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- https://gitlab.com/coswot/coswot-acimov/blob/HEAD/core/aggregations/ontology.ttl|

#### Criterion detail
|Identifier|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|
|----|----|
|Title|Profile&#32;compatibility&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;check&#32;whether&#32;the&#32;test&#32;subject&#32;is&#32;compatible&#32;with&#32;a&#32;profile&#32;or&#32;not,&#32;and&#32;if&#32;it&#32;is&#32;not,&#32;why.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-140)|Identifier|`owl-el-profile-error`|
|[Section top](#minorfail-outcome-number-140)|Title|OWL&#32;EL&#32;Profile&#32;incompatible|
|[Section top](#minorfail-outcome-number-140)|Description|Class&#32;Expression&#32;not&#32;supported&#32;as&#32;object&#32;of&#32;rdfs:domain&#32;or&#32;rdfs:range|
|[Section top](#minorfail-outcome-number-140)|Pointer|<pre lang="Turtle"><code>coswot:hasAggregationDuration&#32;a&#32;owl:DatatypeProperty&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;has&#32;aggregation&#32;duration&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;Links&#32;a&#32;property,&#32;state,&#32;aggregation,&#32;or&#32;aggregation&#32;kind,&#32;t...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:domain&#32; &#91;&#32;a&#32;owl:Class&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:unionOf&#32;(&#32;coswot:Property&#32;coswot:State&#32;coswot:Aggregation&#32;coswot:AggregationKind&#32;)&#32;]&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32; &#60;https://w3id.org/coswot/core/aggregations> &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:range&#32;xsd:duration&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-140)|Pointer|<pre lang="Turtle"><code>coswot:hasAggregationKind&#32;a&#32;owl:ObjectProperty&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;has&#32;aggregation&#32;kind&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;Links&#32;a&#32;property,&#32;state,&#32;or&#32;aggregation,&#32;to&#32;the&#32;kind&#32;of&#32;aggr...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:domain&#32; &#91;&#32;a&#32;owl:Class&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:unionOf&#32;(&#32;coswot:Property&#32;coswot:State&#32;coswot:Aggregation&#32;)&#32;]&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32; &#60;https://w3id.org/coswot/core/aggregations> &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:range&#32;coswot:AggregationKind&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-140)|Pointer|<pre lang="Turtle"><code>coswot:hasAggregationTime&#32;a&#32;owl:ObjectProperty&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;has&#32;aggregation&#32;time&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;Links&#32;a&#32;property,&#32;state,&#32;aggregation,&#32;or&#32;aggregation&#32;kind,&#32;t...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:domain&#32; &#91;&#32;a&#32;owl:Class&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:unionOf&#32;(&#32;coswot:Property&#32;coswot:State&#32;coswot:Aggregation&#32;coswot:AggregationKind&#32;)&#32;]&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32; &#60;https://w3id.org/coswot/core/aggregations> &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:range&#32;time:TemporalInterval&#32;;  &#10; &#32; &#32; &#32; &#32;owl:propertyChainAxiom&#32;(&#32;coswot:hasAggregationKind&#32;coswot:hasAggregationTime&#32;)&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-140)|Pointer|<pre lang="Turtle"><code>coswot:hasMember&#32;a&#32;owl:ObjectProperty&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;has&#32;member&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;Link&#32;to&#32;a&#32;member&#32;within&#32;a&#32;collection&#32;of&#32;(actuations&#32;or&#32;sampl...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:domain&#32;coswot:ObservationCollection&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32; &#60;https://w3id.org/coswot/core/aggregations> &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:range&#32; &#91;&#32;a&#32;owl:Class&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:unionOf&#32;(&#32;coswot:Observation&#32;coswot:ObservationCollection&#32;)&#32;]&#32;.</code></pre>|

***
### MinorFail Outcome number 141

[Jump to summary definition](#summary-MinorFail-141)	|	[Previous MinorFail outcome](#minorfail-outcome-number-140)	|	[Next MinorFail outcome](#minorfail-outcome-number-142)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-aggregations-ontology|
|----|----|
|Title|Standalone&#32;module&#32;core&#92;aggregations&#92;ontology.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- https://gitlab.com/coswot/coswot-acimov/blob/HEAD/core/aggregations/ontology.ttl|

#### Criterion detail
|Identifier|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|
|----|----|
|Title|Profile&#32;compatibility&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;check&#32;whether&#32;the&#32;test&#32;subject&#32;is&#32;compatible&#32;with&#32;a&#32;profile&#32;or&#32;not,&#32;and&#32;if&#32;it&#32;is&#32;not,&#32;why.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-141)|Identifier|`owl-el-profile-error`|
|[Section top](#minorfail-outcome-number-141)|Title|OWL&#32;EL&#32;Profile&#32;incompatible|
|[Section top](#minorfail-outcome-number-141)|Description|Statement&#32;not&#32;supported&#32;in&#32;a&#32;Class&#32;Expression|
|[Section top](#minorfail-outcome-number-141)|Pointer|<pre lang="Turtle"><code>&#91;]&#32;a&#32;owl:Class&#32;;  &#10; &#32; &#32;&#32; &#32;owl:unionOf&#32;(&#32;coswot:Observation&#32;coswot:ObservationCollection&#32;)&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-141)|Pointer|<pre lang="Turtle"><code>&#91;]&#32;a&#32;owl:Class&#32;;  &#10; &#32; &#32;&#32; &#32;owl:unionOf&#32;(&#32;coswot:Property&#32;coswot:State&#32;coswot:Aggregation&#32;)&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-141)|Pointer|<pre lang="Turtle"><code>&#91;]&#32;a&#32;owl:Class&#32;;  &#10; &#32; &#32;&#32; &#32;owl:unionOf&#32;(&#32;coswot:Property&#32;coswot:State&#32;coswot:Aggregation&#32;coswot:AggregationKind&#32;)&#32;.</code></pre>|

***
### MinorFail Outcome number 142

[Jump to summary definition](#summary-MinorFail-142)	|	[Previous MinorFail outcome](#minorfail-outcome-number-141)	|	[Next MinorFail outcome](#minorfail-outcome-number-143)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-aggregations-ontology|
|----|----|
|Title|Standalone&#32;module&#32;core&#92;aggregations&#92;ontology.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- https://gitlab.com/coswot/coswot-acimov/blob/HEAD/core/aggregations/ontology.ttl|

#### Criterion detail
|Identifier|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|
|----|----|
|Title|Profile&#32;compatibility&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;check&#32;whether&#32;the&#32;test&#32;subject&#32;is&#32;compatible&#32;with&#32;a&#32;profile&#32;or&#32;not,&#32;and&#32;if&#32;it&#32;is&#32;not,&#32;why.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-142)|Identifier|`owl-ql-profile-error`|
|[Section top](#minorfail-outcome-number-142)|Title|OWL&#32;QL&#32;Profile&#32;incompatible|
|[Section top](#minorfail-outcome-number-142)|Description|Class&#32;Expression&#32;not&#32;supported&#32;as&#32;object&#32;of&#32;rdfs:domain&#32;or&#32;rdfs:range|
|[Section top](#minorfail-outcome-number-142)|Pointer|<pre lang="Turtle"><code>coswot:hasAggregationDuration&#32;a&#32;owl:DatatypeProperty&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;has&#32;aggregation&#32;duration&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;Links&#32;a&#32;property,&#32;state,&#32;aggregation,&#32;or&#32;aggregation&#32;kind,&#32;t...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:domain&#32; &#91;&#32;a&#32;owl:Class&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:unionOf&#32;(&#32;coswot:Property&#32;coswot:State&#32;coswot:Aggregation&#32;coswot:AggregationKind&#32;)&#32;]&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32; &#60;https://w3id.org/coswot/core/aggregations> &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:range&#32;xsd:duration&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-142)|Pointer|<pre lang="Turtle"><code>coswot:hasAggregationKind&#32;a&#32;owl:ObjectProperty&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;has&#32;aggregation&#32;kind&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;Links&#32;a&#32;property,&#32;state,&#32;or&#32;aggregation,&#32;to&#32;the&#32;kind&#32;of&#32;aggr...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:domain&#32; &#91;&#32;a&#32;owl:Class&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:unionOf&#32;(&#32;coswot:Property&#32;coswot:State&#32;coswot:Aggregation&#32;)&#32;]&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32; &#60;https://w3id.org/coswot/core/aggregations> &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:range&#32;coswot:AggregationKind&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-142)|Pointer|<pre lang="Turtle"><code>coswot:hasMember&#32;a&#32;owl:ObjectProperty&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;has&#32;member&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;Link&#32;to&#32;a&#32;member&#32;within&#32;a&#32;collection&#32;of&#32;(actuations&#32;or&#32;sampl...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:domain&#32;coswot:ObservationCollection&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32; &#60;https://w3id.org/coswot/core/aggregations> &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:range&#32; &#91;&#32;a&#32;owl:Class&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:unionOf&#32;(&#32;coswot:Observation&#32;coswot:ObservationCollection&#32;)&#32;]&#32;.</code></pre>|

***
### MinorFail Outcome number 143

[Jump to summary definition](#summary-MinorFail-143)	|	[Previous MinorFail outcome](#minorfail-outcome-number-142)	|	[Next MinorFail outcome](#minorfail-outcome-number-144)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-aggregations-ontology|
|----|----|
|Title|Standalone&#32;module&#32;core&#92;aggregations&#92;ontology.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- https://gitlab.com/coswot/coswot-acimov/blob/HEAD/core/aggregations/ontology.ttl|

#### Criterion detail
|Identifier|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|
|----|----|
|Title|Profile&#32;compatibility&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;check&#32;whether&#32;the&#32;test&#32;subject&#32;is&#32;compatible&#32;with&#32;a&#32;profile&#32;or&#32;not,&#32;and&#32;if&#32;it&#32;is&#32;not,&#32;why.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-143)|Identifier|`owl-ql-profile-error`|
|[Section top](#minorfail-outcome-number-143)|Title|OWL&#32;QL&#32;Profile&#32;incompatible|
|[Section top](#minorfail-outcome-number-143)|Description|Class&#32;Expression&#32;not&#32;supported&#32;as&#32;object&#32;of&#32;rdfs:domain&#32;or&#32;rdfs:range  &#10;Property&#32;inclusions&#32;involving&#32;property&#32;chains&#32;not&#32;supported|
|[Section top](#minorfail-outcome-number-143)|Pointer|<pre lang="Turtle"><code>coswot:hasAggregationTime&#32;a&#32;owl:ObjectProperty&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;has&#32;aggregation&#32;time&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;Links&#32;a&#32;property,&#32;state,&#32;aggregation,&#32;or&#32;aggregation&#32;kind,&#32;t...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:domain&#32; &#91;&#32;a&#32;owl:Class&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:unionOf&#32;(&#32;coswot:Property&#32;coswot:State&#32;coswot:Aggregation&#32;coswot:AggregationKind&#32;)&#32;]&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32; &#60;https://w3id.org/coswot/core/aggregations> &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:range&#32;time:TemporalInterval&#32;;  &#10; &#32; &#32; &#32; &#32;owl:propertyChainAxiom&#32;(&#32;coswot:hasAggregationKind&#32;coswot:hasAggregationTime&#32;)&#32;.</code></pre>|

***
### MinorFail Outcome number 144

[Jump to summary definition](#summary-MinorFail-144)	|	[Previous MinorFail outcome](#minorfail-outcome-number-143)	|	[Next MinorFail outcome](#minorfail-outcome-number-145)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-aggregations-ontology|
|----|----|
|Title|Standalone&#32;module&#32;core&#92;aggregations&#92;ontology.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- https://gitlab.com/coswot/coswot-acimov/blob/HEAD/core/aggregations/ontology.ttl|

#### Criterion detail
|Identifier|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|
|----|----|
|Title|Profile&#32;compatibility&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;check&#32;whether&#32;the&#32;test&#32;subject&#32;is&#32;compatible&#32;with&#32;a&#32;profile&#32;or&#32;not,&#32;and&#32;if&#32;it&#32;is&#32;not,&#32;why.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-144)|Identifier|`owl-ql-profile-error`|
|[Section top](#minorfail-outcome-number-144)|Title|OWL&#32;QL&#32;Profile&#32;incompatible|
|[Section top](#minorfail-outcome-number-144)|Description|Statement&#32;not&#32;supported&#32;in&#32;a&#32;Super&#32;Class&#32;Expression|
|[Section top](#minorfail-outcome-number-144)|Pointer|<pre lang="Turtle"><code>&#91;]&#32;a&#32;owl:Class&#32;;  &#10; &#32; &#32;&#32; &#32;owl:unionOf&#32;(&#32;coswot:Observation&#32;coswot:ObservationCollection&#32;)&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-144)|Pointer|<pre lang="Turtle"><code>&#91;]&#32;a&#32;owl:Class&#32;;  &#10; &#32; &#32;&#32; &#32;owl:unionOf&#32;(&#32;coswot:Property&#32;coswot:State&#32;coswot:Aggregation&#32;)&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-144)|Pointer|<pre lang="Turtle"><code>&#91;]&#32;a&#32;owl:Class&#32;;  &#10; &#32; &#32;&#32; &#32;owl:unionOf&#32;(&#32;coswot:Property&#32;coswot:State&#32;coswot:Aggregation&#32;coswot:AggregationKind&#32;)&#32;.</code></pre>|

***
### MinorFail Outcome number 145

[Jump to summary definition](#summary-MinorFail-145)	|	[Previous MinorFail outcome](#minorfail-outcome-number-144)	|	[Next MinorFail outcome](#minorfail-outcome-number-146)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-aggregations-ontology|
|----|----|
|Title|Standalone&#32;module&#32;core&#92;aggregations&#92;ontology.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- https://gitlab.com/coswot/coswot-acimov/blob/HEAD/core/aggregations/ontology.ttl|

#### Criterion detail
|Identifier|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|
|----|----|
|Title|Profile&#32;compatibility&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;check&#32;whether&#32;the&#32;test&#32;subject&#32;is&#32;compatible&#32;with&#32;a&#32;profile&#32;or&#32;not,&#32;and&#32;if&#32;it&#32;is&#32;not,&#32;why.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-145)|Identifier|`owl-rl-profile-error`|
|[Section top](#minorfail-outcome-number-145)|Title|OWL&#32;RL&#32;Profile&#32;incompatible|
|[Section top](#minorfail-outcome-number-145)|Description|Class&#32;Expression&#32;not&#32;supported&#32;as&#32;object&#32;of&#32;rdfs:domain&#32;or&#32;rdfs:range|
|[Section top](#minorfail-outcome-number-145)|Pointer|<pre lang="Turtle"><code>coswot:hasAggregationDuration&#32;a&#32;owl:DatatypeProperty&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;has&#32;aggregation&#32;duration&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;Links&#32;a&#32;property,&#32;state,&#32;aggregation,&#32;or&#32;aggregation&#32;kind,&#32;t...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:domain&#32; &#91;&#32;a&#32;owl:Class&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:unionOf&#32;(&#32;coswot:Property&#32;coswot:State&#32;coswot:Aggregation&#32;coswot:AggregationKind&#32;)&#32;]&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32; &#60;https://w3id.org/coswot/core/aggregations> &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:range&#32;xsd:duration&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-145)|Pointer|<pre lang="Turtle"><code>coswot:hasAggregationKind&#32;a&#32;owl:ObjectProperty&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;has&#32;aggregation&#32;kind&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;Links&#32;a&#32;property,&#32;state,&#32;or&#32;aggregation,&#32;to&#32;the&#32;kind&#32;of&#32;aggr...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:domain&#32; &#91;&#32;a&#32;owl:Class&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:unionOf&#32;(&#32;coswot:Property&#32;coswot:State&#32;coswot:Aggregation&#32;)&#32;]&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32; &#60;https://w3id.org/coswot/core/aggregations> &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:range&#32;coswot:AggregationKind&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-145)|Pointer|<pre lang="Turtle"><code>coswot:hasAggregationTime&#32;a&#32;owl:ObjectProperty&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;has&#32;aggregation&#32;time&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;Links&#32;a&#32;property,&#32;state,&#32;aggregation,&#32;or&#32;aggregation&#32;kind,&#32;t...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:domain&#32; &#91;&#32;a&#32;owl:Class&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:unionOf&#32;(&#32;coswot:Property&#32;coswot:State&#32;coswot:Aggregation&#32;coswot:AggregationKind&#32;)&#32;]&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32; &#60;https://w3id.org/coswot/core/aggregations> &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:range&#32;time:TemporalInterval&#32;;  &#10; &#32; &#32; &#32; &#32;owl:propertyChainAxiom&#32;(&#32;coswot:hasAggregationKind&#32;coswot:hasAggregationTime&#32;)&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-145)|Pointer|<pre lang="Turtle"><code>coswot:hasMember&#32;a&#32;owl:ObjectProperty&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;has&#32;member&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;Link&#32;to&#32;a&#32;member&#32;within&#32;a&#32;collection&#32;of&#32;(actuations&#32;or&#32;sampl...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:domain&#32;coswot:ObservationCollection&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32; &#60;https://w3id.org/coswot/core/aggregations> &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:range&#32; &#91;&#32;a&#32;owl:Class&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:unionOf&#32;(&#32;coswot:Observation&#32;coswot:ObservationCollection&#32;)&#32;]&#32;.</code></pre>|

***
### MinorFail Outcome number 146

[Jump to summary definition](#summary-MinorFail-146)	|	[Previous MinorFail outcome](#minorfail-outcome-number-145)	|	[Next MinorFail outcome](#minorfail-outcome-number-147)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-aggregations-ontology|
|----|----|
|Title|Standalone&#32;module&#32;core&#92;aggregations&#92;ontology.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- https://gitlab.com/coswot/coswot-acimov/blob/HEAD/core/aggregations/ontology.ttl|

#### Criterion detail
|Identifier|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|
|----|----|
|Title|Profile&#32;compatibility&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;check&#32;whether&#32;the&#32;test&#32;subject&#32;is&#32;compatible&#32;with&#32;a&#32;profile&#32;or&#32;not,&#32;and&#32;if&#32;it&#32;is&#32;not,&#32;why.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-146)|Identifier|`owl-rl-profile-error`|
|[Section top](#minorfail-outcome-number-146)|Title|OWL&#32;RL&#32;Profile&#32;incompatible|
|[Section top](#minorfail-outcome-number-146)|Description|Class&#32;Expression&#32;not&#32;supported&#32;with&#32;rdfs:subClassOf|
|[Section top](#minorfail-outcome-number-146)|Pointer|<pre lang="Turtle"><code>coswot:Aggregation&#32;a&#32;owl:Class&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;Aggregation&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;Observation&#32;that&#32;takes&#32;as&#32;input&#32;a&#32;collection&#32;of&#32;observations...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32; &#60;https://w3id.org/coswot/core/aggregations> &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:subClassOf&#32; &#91;&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:onProperty&#32;coswot:hasInput&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:someValuesFrom&#32;coswot:ObservationCollection&#32;],  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#91;&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:onProperty&#32;coswot:hasAggregationKind&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:someValuesFrom&#32;coswot:AggregationKind&#32;],  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;coswot:Observation&#32;.</code></pre>|

***
### MinorFail Outcome number 147

[Jump to summary definition](#summary-MinorFail-147)	|	[Previous MinorFail outcome](#minorfail-outcome-number-146)	|	[Next MinorFail outcome](#minorfail-outcome-number-148)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-aggregations-ontology|
|----|----|
|Title|Standalone&#32;module&#32;core&#92;aggregations&#92;ontology.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- https://gitlab.com/coswot/coswot-acimov/blob/HEAD/core/aggregations/ontology.ttl|

#### Criterion detail
|Identifier|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|
|----|----|
|Title|Profile&#32;compatibility&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;check&#32;whether&#32;the&#32;test&#32;subject&#32;is&#32;compatible&#32;with&#32;a&#32;profile&#32;or&#32;not,&#32;and&#32;if&#32;it&#32;is&#32;not,&#32;why.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-147)|Identifier|`owl-rl-profile-error`|
|[Section top](#minorfail-outcome-number-147)|Title|OWL&#32;RL&#32;Profile&#32;incompatible|
|[Section top](#minorfail-outcome-number-147)|Description|Statement&#32;not&#32;supported&#32;in&#32;a&#32;Super&#32;Class&#32;Expression|
|[Section top](#minorfail-outcome-number-147)|Pointer|<pre lang="Turtle"><code>&#91;]&#32;a&#32;owl:Class&#32;;  &#10; &#32; &#32;&#32; &#32;owl:unionOf&#32;(&#32;coswot:Observation&#32;coswot:ObservationCollection&#32;)&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-147)|Pointer|<pre lang="Turtle"><code>&#91;]&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32;owl:onProperty&#32;coswot:hasInput&#32;;  &#10; &#32; &#32; &#32; &#32;owl:someValuesFrom&#32;coswot:ObservationCollection&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-147)|Pointer|<pre lang="Turtle"><code>&#91;]&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32;owl:onProperty&#32;coswot:hasAggregationKind&#32;;  &#10; &#32; &#32; &#32; &#32;owl:someValuesFrom&#32;coswot:AggregationKind&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-147)|Pointer|<pre lang="Turtle"><code>&#91;]&#32;a&#32;owl:Class&#32;;  &#10; &#32; &#32;&#32; &#32;owl:unionOf&#32;(&#32;coswot:Property&#32;coswot:State&#32;coswot:Aggregation&#32;)&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-147)|Pointer|<pre lang="Turtle"><code>&#91;]&#32;a&#32;owl:Class&#32;;  &#10; &#32; &#32;&#32; &#32;owl:unionOf&#32;(&#32;coswot:Property&#32;coswot:State&#32;coswot:Aggregation&#32;coswot:AggregationKind&#32;)&#32;.</code></pre>|

***
### MinorFail Outcome number 148

[Jump to summary definition](#summary-MinorFail-148)	|	[Previous MinorFail outcome](#minorfail-outcome-number-147)	|	[Next MinorFail outcome](#minorfail-outcome-number-149)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-actuations-ontology|
|----|----|
|Title|Standalone&#32;module&#32;core&#92;actuations&#92;ontology.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- https://gitlab.com/coswot/coswot-acimov/blob/HEAD/core/actuations/ontology.ttl|

#### Criterion detail
|Identifier|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|
|----|----|
|Title|Profile&#32;compatibility&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;check&#32;whether&#32;the&#32;test&#32;subject&#32;is&#32;compatible&#32;with&#32;a&#32;profile&#32;or&#32;not,&#32;and&#32;if&#32;it&#32;is&#32;not,&#32;why.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-148)|Identifier|`owl-el-profile-error`|
|[Section top](#minorfail-outcome-number-148)|Title|OWL&#32;EL&#32;Profile&#32;incompatible|
|[Section top](#minorfail-outcome-number-148)|Description|Class&#32;Expression&#32;not&#32;supported&#32;as&#32;object&#32;of&#32;rdfs:domain&#32;or&#32;rdfs:range|
|[Section top](#minorfail-outcome-number-148)|Pointer|<pre lang="Turtle"><code>coswot:controls&#32;a&#32;owl:ObjectProperty&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;controls&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;Links&#32;an&#32;actuator,&#32;actuating&#32;function,&#32;actuating&#32;command,&#32;or...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:domain&#32; &#91;&#32;a&#32;owl:Class&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:unionOf&#32;(&#32;coswot:Actuator&#32;coswot:ActuatingFunction&#32;coswot:ActuatingCommand&#32;coswot:Actuation&#32;)&#32;]&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32; &#60;https://w3id.org/coswot/core/actuations> &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:subPropertyOf&#32;coswot:targets&#32;;  &#10; &#32; &#32; &#32; &#32;owl:inverseOf&#32;coswot:isControlledBy&#32;.</code></pre>|

***
### MinorFail Outcome number 149

[Jump to summary definition](#summary-MinorFail-149)	|	[Previous MinorFail outcome](#minorfail-outcome-number-148)	|	[Next MinorFail outcome](#minorfail-outcome-number-150)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-actuations-ontology|
|----|----|
|Title|Standalone&#32;module&#32;core&#92;actuations&#92;ontology.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- https://gitlab.com/coswot/coswot-acimov/blob/HEAD/core/actuations/ontology.ttl|

#### Criterion detail
|Identifier|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|
|----|----|
|Title|Profile&#32;compatibility&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;check&#32;whether&#32;the&#32;test&#32;subject&#32;is&#32;compatible&#32;with&#32;a&#32;profile&#32;or&#32;not,&#32;and&#32;if&#32;it&#32;is&#32;not,&#32;why.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-149)|Identifier|`owl-el-profile-error`|
|[Section top](#minorfail-outcome-number-149)|Title|OWL&#32;EL&#32;Profile&#32;incompatible|
|[Section top](#minorfail-outcome-number-149)|Description|Class&#32;Expression&#32;not&#32;supported&#32;with&#32;rdfs:subClassOf|
|[Section top](#minorfail-outcome-number-149)|Pointer|<pre lang="Turtle"><code>coswot:ActuatingCommand&#32;a&#32;owl:Class&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;Actuating&#32;Command&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;An&#32;instance&#32;of&#32;actuating&#32;command&#32;is&#32;a&#32;command&#32;that&#32;controls&#32;...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32; &#60;https://w3id.org/coswot/core/actuations> &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:subClassOf&#32; &#91;&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:onProperty&#32;coswot:controls&#32;],  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;coswot:Command&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-149)|Pointer|<pre lang="Turtle"><code>coswot:Actuation&#32;a&#32;owl:Class&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;Actuation&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;A&#32;coswot:Actuation&#32;is&#32;the&#32;act&#32;of&#32;carrying&#32;out&#32;a&#32;procedure&#32;to...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32; &#60;https://w3id.org/coswot/core/actuations> &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:subClassOf&#32; &#91;&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:allValuesFrom&#32;coswot:Actuator&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:onProperty&#32;coswot:madeBy&#32;],  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#91;&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:onProperty&#32;coswot:controls&#32;],  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;coswot:ProcedureExecution&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-149)|Pointer|<pre lang="Turtle"><code>coswot:ActuatorOfInterest&#32;a&#32;owl:Class&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;Actuator&#32;Of&#32;Interest&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;A&#32;specific,&#32;tangible&#32;device&#32;designed&#32;to&#32;control&#32;one&#32;or&#32;more&#32;...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32; &#60;https://w3id.org/coswot/core/actuations> &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:subClassOf&#32; &#91;&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:onProperty&#32;coswot:controls&#32;],  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;coswot:Actuator,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;coswot:DeviceOfInterest&#32;.</code></pre>|

***
### MinorFail Outcome number 150

[Jump to summary definition](#summary-MinorFail-150)	|	[Previous MinorFail outcome](#minorfail-outcome-number-149)	|	[Next MinorFail outcome](#minorfail-outcome-number-151)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-actuations-ontology|
|----|----|
|Title|Standalone&#32;module&#32;core&#92;actuations&#92;ontology.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- https://gitlab.com/coswot/coswot-acimov/blob/HEAD/core/actuations/ontology.ttl|

#### Criterion detail
|Identifier|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|
|----|----|
|Title|Profile&#32;compatibility&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;check&#32;whether&#32;the&#32;test&#32;subject&#32;is&#32;compatible&#32;with&#32;a&#32;profile&#32;or&#32;not,&#32;and&#32;if&#32;it&#32;is&#32;not,&#32;why.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-150)|Identifier|`owl-el-profile-error`|
|[Section top](#minorfail-outcome-number-150)|Title|OWL&#32;EL&#32;Profile&#32;incompatible|
|[Section top](#minorfail-outcome-number-150)|Description|Statement&#32;not&#32;supported|
|[Section top](#minorfail-outcome-number-150)|Pointer|<pre lang="Turtle"><code>coswot:Actuator&#32;a&#32;owl:Class&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;Actuator&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;Actuators&#32;are&#32;devices&#32;designed&#32;to&#32;control&#32;one&#32;or&#32;more&#32;proper...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32; &#60;https://w3id.org/coswot/core/actuations> &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:subClassOf&#32; &#91;&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:onProperty&#32;coswot:controls&#32;],  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;coswot:Device&#32;;  &#10; &#32; &#32; &#32; &#32;owl:disjointUnionOf&#32;(&#32;coswot:ActuatorOfInterest&#32;coswot:ActuatorKind&#32;)&#32;.</code></pre>|

***
### MinorFail Outcome number 151

[Jump to summary definition](#summary-MinorFail-151)	|	[Previous MinorFail outcome](#minorfail-outcome-number-150)	|	[Next MinorFail outcome](#minorfail-outcome-number-152)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-actuations-ontology|
|----|----|
|Title|Standalone&#32;module&#32;core&#92;actuations&#92;ontology.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- https://gitlab.com/coswot/coswot-acimov/blob/HEAD/core/actuations/ontology.ttl|

#### Criterion detail
|Identifier|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|
|----|----|
|Title|Profile&#32;compatibility&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;check&#32;whether&#32;the&#32;test&#32;subject&#32;is&#32;compatible&#32;with&#32;a&#32;profile&#32;or&#32;not,&#32;and&#32;if&#32;it&#32;is&#32;not,&#32;why.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-151)|Identifier|`owl-el-profile-error`|
|[Section top](#minorfail-outcome-number-151)|Title|OWL&#32;EL&#32;Profile&#32;incompatible|
|[Section top](#minorfail-outcome-number-151)|Description|Statement&#32;not&#32;supported&#32;in&#32;a&#32;Class&#32;Expression|
|[Section top](#minorfail-outcome-number-151)|Pointer|<pre lang="Turtle"><code>&#91;]&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32;&#32; &#32;owl:onProperty&#32;coswot:controls&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-151)|Pointer|<pre lang="Turtle"><code>&#91;]&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32;owl:allValuesFrom&#32;coswot:Actuator&#32;;  &#10; &#32; &#32; &#32; &#32;owl:onProperty&#32;coswot:madeBy&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-151)|Pointer|<pre lang="Turtle"><code>&#91;]&#32;a&#32;owl:Class&#32;;  &#10; &#32; &#32;&#32; &#32;owl:unionOf&#32;(&#32;coswot:Actuator&#32;coswot:ActuatingFunction&#32;coswot:ActuatingCommand&#32;coswot:Actuation&#32;)&#32;.</code></pre>|

***
### MinorFail Outcome number 152

[Jump to summary definition](#summary-MinorFail-152)	|	[Previous MinorFail outcome](#minorfail-outcome-number-151)	|	[Next MinorFail outcome](#minorfail-outcome-number-153)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-actuations-ontology|
|----|----|
|Title|Standalone&#32;module&#32;core&#92;actuations&#92;ontology.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- https://gitlab.com/coswot/coswot-acimov/blob/HEAD/core/actuations/ontology.ttl|

#### Criterion detail
|Identifier|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|
|----|----|
|Title|Profile&#32;compatibility&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;check&#32;whether&#32;the&#32;test&#32;subject&#32;is&#32;compatible&#32;with&#32;a&#32;profile&#32;or&#32;not,&#32;and&#32;if&#32;it&#32;is&#32;not,&#32;why.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-152)|Identifier|`owl-ql-profile-error`|
|[Section top](#minorfail-outcome-number-152)|Title|OWL&#32;QL&#32;Profile&#32;incompatible|
|[Section top](#minorfail-outcome-number-152)|Description|Class&#32;Expression&#32;not&#32;supported&#32;as&#32;object&#32;of&#32;rdfs:domain&#32;or&#32;rdfs:range|
|[Section top](#minorfail-outcome-number-152)|Pointer|<pre lang="Turtle"><code>coswot:controls&#32;a&#32;owl:ObjectProperty&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;controls&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;Links&#32;an&#32;actuator,&#32;actuating&#32;function,&#32;actuating&#32;command,&#32;or...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:domain&#32; &#91;&#32;a&#32;owl:Class&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:unionOf&#32;(&#32;coswot:Actuator&#32;coswot:ActuatingFunction&#32;coswot:ActuatingCommand&#32;coswot:Actuation&#32;)&#32;]&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32; &#60;https://w3id.org/coswot/core/actuations> &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:subPropertyOf&#32;coswot:targets&#32;;  &#10; &#32; &#32; &#32; &#32;owl:inverseOf&#32;coswot:isControlledBy&#32;.</code></pre>|

***
### MinorFail Outcome number 153

[Jump to summary definition](#summary-MinorFail-153)	|	[Previous MinorFail outcome](#minorfail-outcome-number-152)	|	[Next MinorFail outcome](#minorfail-outcome-number-154)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-actuations-ontology|
|----|----|
|Title|Standalone&#32;module&#32;core&#92;actuations&#92;ontology.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- https://gitlab.com/coswot/coswot-acimov/blob/HEAD/core/actuations/ontology.ttl|

#### Criterion detail
|Identifier|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|
|----|----|
|Title|Profile&#32;compatibility&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;check&#32;whether&#32;the&#32;test&#32;subject&#32;is&#32;compatible&#32;with&#32;a&#32;profile&#32;or&#32;not,&#32;and&#32;if&#32;it&#32;is&#32;not,&#32;why.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-153)|Identifier|`owl-ql-profile-error`|
|[Section top](#minorfail-outcome-number-153)|Title|OWL&#32;QL&#32;Profile&#32;incompatible|
|[Section top](#minorfail-outcome-number-153)|Description|Class&#32;Expression&#32;not&#32;supported&#32;with&#32;rdfs:subClassOf|
|[Section top](#minorfail-outcome-number-153)|Pointer|<pre lang="Turtle"><code>coswot:ActuatingCommand&#32;a&#32;owl:Class&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;Actuating&#32;Command&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;An&#32;instance&#32;of&#32;actuating&#32;command&#32;is&#32;a&#32;command&#32;that&#32;controls&#32;...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32; &#60;https://w3id.org/coswot/core/actuations> &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:subClassOf&#32; &#91;&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:onProperty&#32;coswot:controls&#32;],  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;coswot:Command&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-153)|Pointer|<pre lang="Turtle"><code>coswot:Actuation&#32;a&#32;owl:Class&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;Actuation&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;A&#32;coswot:Actuation&#32;is&#32;the&#32;act&#32;of&#32;carrying&#32;out&#32;a&#32;procedure&#32;to...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32; &#60;https://w3id.org/coswot/core/actuations> &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:subClassOf&#32; &#91;&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:allValuesFrom&#32;coswot:Actuator&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:onProperty&#32;coswot:madeBy&#32;],  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#91;&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:onProperty&#32;coswot:controls&#32;],  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;coswot:ProcedureExecution&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-153)|Pointer|<pre lang="Turtle"><code>coswot:ActuatorOfInterest&#32;a&#32;owl:Class&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;Actuator&#32;Of&#32;Interest&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;A&#32;specific,&#32;tangible&#32;device&#32;designed&#32;to&#32;control&#32;one&#32;or&#32;more&#32;...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32; &#60;https://w3id.org/coswot/core/actuations> &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:subClassOf&#32; &#91;&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:onProperty&#32;coswot:controls&#32;],  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;coswot:Actuator,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;coswot:DeviceOfInterest&#32;.</code></pre>|

***
### MinorFail Outcome number 154

[Jump to summary definition](#summary-MinorFail-154)	|	[Previous MinorFail outcome](#minorfail-outcome-number-153)	|	[Next MinorFail outcome](#minorfail-outcome-number-155)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-actuations-ontology|
|----|----|
|Title|Standalone&#32;module&#32;core&#92;actuations&#92;ontology.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- https://gitlab.com/coswot/coswot-acimov/blob/HEAD/core/actuations/ontology.ttl|

#### Criterion detail
|Identifier|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|
|----|----|
|Title|Profile&#32;compatibility&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;check&#32;whether&#32;the&#32;test&#32;subject&#32;is&#32;compatible&#32;with&#32;a&#32;profile&#32;or&#32;not,&#32;and&#32;if&#32;it&#32;is&#32;not,&#32;why.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-154)|Identifier|`owl-ql-profile-error`|
|[Section top](#minorfail-outcome-number-154)|Title|OWL&#32;QL&#32;Profile&#32;incompatible|
|[Section top](#minorfail-outcome-number-154)|Description|Statement&#32;not&#32;supported|
|[Section top](#minorfail-outcome-number-154)|Pointer|<pre lang="Turtle"><code>coswot:Actuator&#32;a&#32;owl:Class&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;Actuator&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;Actuators&#32;are&#32;devices&#32;designed&#32;to&#32;control&#32;one&#32;or&#32;more&#32;proper...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32; &#60;https://w3id.org/coswot/core/actuations> &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:subClassOf&#32; &#91;&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:onProperty&#32;coswot:controls&#32;],  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;coswot:Device&#32;;  &#10; &#32; &#32; &#32; &#32;owl:disjointUnionOf&#32;(&#32;coswot:ActuatorOfInterest&#32;coswot:ActuatorKind&#32;)&#32;.</code></pre>|

***
### MinorFail Outcome number 155

[Jump to summary definition](#summary-MinorFail-155)	|	[Previous MinorFail outcome](#minorfail-outcome-number-154)	|	[Next MinorFail outcome](#minorfail-outcome-number-156)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-actuations-ontology|
|----|----|
|Title|Standalone&#32;module&#32;core&#92;actuations&#92;ontology.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- https://gitlab.com/coswot/coswot-acimov/blob/HEAD/core/actuations/ontology.ttl|

#### Criterion detail
|Identifier|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|
|----|----|
|Title|Profile&#32;compatibility&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;check&#32;whether&#32;the&#32;test&#32;subject&#32;is&#32;compatible&#32;with&#32;a&#32;profile&#32;or&#32;not,&#32;and&#32;if&#32;it&#32;is&#32;not,&#32;why.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-155)|Identifier|`owl-ql-profile-error`|
|[Section top](#minorfail-outcome-number-155)|Title|OWL&#32;QL&#32;Profile&#32;incompatible|
|[Section top](#minorfail-outcome-number-155)|Description|Statement&#32;not&#32;supported&#32;in&#32;a&#32;Super&#32;Class&#32;Expression|
|[Section top](#minorfail-outcome-number-155)|Pointer|<pre lang="Turtle"><code>&#91;]&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32;&#32; &#32;owl:onProperty&#32;coswot:controls&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-155)|Pointer|<pre lang="Turtle"><code>&#91;]&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32;owl:allValuesFrom&#32;coswot:Actuator&#32;;  &#10; &#32; &#32; &#32; &#32;owl:onProperty&#32;coswot:madeBy&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-155)|Pointer|<pre lang="Turtle"><code>&#91;]&#32;a&#32;owl:Class&#32;;  &#10; &#32; &#32;&#32; &#32;owl:unionOf&#32;(&#32;coswot:Actuator&#32;coswot:ActuatingFunction&#32;coswot:ActuatingCommand&#32;coswot:Actuation&#32;)&#32;.</code></pre>|

***
### MinorFail Outcome number 156

[Jump to summary definition](#summary-MinorFail-156)	|	[Previous MinorFail outcome](#minorfail-outcome-number-155)	|	[Next MinorFail outcome](#minorfail-outcome-number-157)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-actuations-ontology|
|----|----|
|Title|Standalone&#32;module&#32;core&#92;actuations&#92;ontology.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- https://gitlab.com/coswot/coswot-acimov/blob/HEAD/core/actuations/ontology.ttl|

#### Criterion detail
|Identifier|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|
|----|----|
|Title|Profile&#32;compatibility&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;check&#32;whether&#32;the&#32;test&#32;subject&#32;is&#32;compatible&#32;with&#32;a&#32;profile&#32;or&#32;not,&#32;and&#32;if&#32;it&#32;is&#32;not,&#32;why.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-156)|Identifier|`owl-rl-profile-error`|
|[Section top](#minorfail-outcome-number-156)|Title|OWL&#32;RL&#32;Profile&#32;incompatible|
|[Section top](#minorfail-outcome-number-156)|Description|Class&#32;Expression&#32;not&#32;supported&#32;as&#32;object&#32;of&#32;rdfs:domain&#32;or&#32;rdfs:range|
|[Section top](#minorfail-outcome-number-156)|Pointer|<pre lang="Turtle"><code>coswot:controls&#32;a&#32;owl:ObjectProperty&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;controls&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;Links&#32;an&#32;actuator,&#32;actuating&#32;function,&#32;actuating&#32;command,&#32;or...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:domain&#32; &#91;&#32;a&#32;owl:Class&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:unionOf&#32;(&#32;coswot:Actuator&#32;coswot:ActuatingFunction&#32;coswot:ActuatingCommand&#32;coswot:Actuation&#32;)&#32;]&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32; &#60;https://w3id.org/coswot/core/actuations> &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:subPropertyOf&#32;coswot:targets&#32;;  &#10; &#32; &#32; &#32; &#32;owl:inverseOf&#32;coswot:isControlledBy&#32;.</code></pre>|

***
### MinorFail Outcome number 157

[Jump to summary definition](#summary-MinorFail-157)	|	[Previous MinorFail outcome](#minorfail-outcome-number-156)	|	[Next MinorFail outcome](#minorfail-outcome-number-158)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-actuations-ontology|
|----|----|
|Title|Standalone&#32;module&#32;core&#92;actuations&#92;ontology.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- https://gitlab.com/coswot/coswot-acimov/blob/HEAD/core/actuations/ontology.ttl|

#### Criterion detail
|Identifier|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|
|----|----|
|Title|Profile&#32;compatibility&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;check&#32;whether&#32;the&#32;test&#32;subject&#32;is&#32;compatible&#32;with&#32;a&#32;profile&#32;or&#32;not,&#32;and&#32;if&#32;it&#32;is&#32;not,&#32;why.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-157)|Identifier|`owl-rl-profile-error`|
|[Section top](#minorfail-outcome-number-157)|Title|OWL&#32;RL&#32;Profile&#32;incompatible|
|[Section top](#minorfail-outcome-number-157)|Description|Class&#32;Expression&#32;not&#32;supported&#32;with&#32;rdfs:subClassOf|
|[Section top](#minorfail-outcome-number-157)|Pointer|<pre lang="Turtle"><code>coswot:ActuatingCommand&#32;a&#32;owl:Class&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;Actuating&#32;Command&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;An&#32;instance&#32;of&#32;actuating&#32;command&#32;is&#32;a&#32;command&#32;that&#32;controls&#32;...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32; &#60;https://w3id.org/coswot/core/actuations> &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:subClassOf&#32; &#91;&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:onProperty&#32;coswot:controls&#32;],  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;coswot:Command&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-157)|Pointer|<pre lang="Turtle"><code>coswot:ActuatingFunction&#32;a&#32;owl:Class&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;Actuating&#32;Function&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;An&#32;actuating&#32;function&#32;is&#32;a&#32;function&#32;that&#32;has&#32;at&#32;least&#32;one&#32;ac...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32; &#60;https://w3id.org/coswot/core/actuations> &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:subClassOf&#32; &#91;&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:onProperty&#32;coswot:hasCommand&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:someValuesFrom&#32;coswot:ActuatingCommand&#32;],  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;coswot:Function&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-157)|Pointer|<pre lang="Turtle"><code>coswot:Actuation&#32;a&#32;owl:Class&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;Actuation&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;A&#32;coswot:Actuation&#32;is&#32;the&#32;act&#32;of&#32;carrying&#32;out&#32;a&#32;procedure&#32;to...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32; &#60;https://w3id.org/coswot/core/actuations> &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:subClassOf&#32; &#91;&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:allValuesFrom&#32;coswot:Actuator&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:onProperty&#32;coswot:madeBy&#32;],  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#91;&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:onProperty&#32;coswot:controls&#32;],  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;coswot:ProcedureExecution&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-157)|Pointer|<pre lang="Turtle"><code>coswot:ActuatorOfInterest&#32;a&#32;owl:Class&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;Actuator&#32;Of&#32;Interest&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;A&#32;specific,&#32;tangible&#32;device&#32;designed&#32;to&#32;control&#32;one&#32;or&#32;more&#32;...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32; &#60;https://w3id.org/coswot/core/actuations> &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:subClassOf&#32; &#91;&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:onProperty&#32;coswot:controls&#32;],  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;coswot:Actuator,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;coswot:DeviceOfInterest&#32;.</code></pre>|

***
### MinorFail Outcome number 158

[Jump to summary definition](#summary-MinorFail-158)	|	[Previous MinorFail outcome](#minorfail-outcome-number-157)	|	[Next MinorFail outcome](#minorfail-outcome-number-159)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-actuations-ontology|
|----|----|
|Title|Standalone&#32;module&#32;core&#92;actuations&#92;ontology.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- https://gitlab.com/coswot/coswot-acimov/blob/HEAD/core/actuations/ontology.ttl|

#### Criterion detail
|Identifier|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|
|----|----|
|Title|Profile&#32;compatibility&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;check&#32;whether&#32;the&#32;test&#32;subject&#32;is&#32;compatible&#32;with&#32;a&#32;profile&#32;or&#32;not,&#32;and&#32;if&#32;it&#32;is&#32;not,&#32;why.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-158)|Identifier|`owl-rl-profile-error`|
|[Section top](#minorfail-outcome-number-158)|Title|OWL&#32;RL&#32;Profile&#32;incompatible|
|[Section top](#minorfail-outcome-number-158)|Description|Statement&#32;not&#32;supported|
|[Section top](#minorfail-outcome-number-158)|Pointer|<pre lang="Turtle"><code>coswot:Actuator&#32;a&#32;owl:Class&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;Actuator&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;Actuators&#32;are&#32;devices&#32;designed&#32;to&#32;control&#32;one&#32;or&#32;more&#32;proper...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32; &#60;https://w3id.org/coswot/core/actuations> &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:subClassOf&#32; &#91;&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:onProperty&#32;coswot:controls&#32;],  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;coswot:Device&#32;;  &#10; &#32; &#32; &#32; &#32;owl:disjointUnionOf&#32;(&#32;coswot:ActuatorOfInterest&#32;coswot:ActuatorKind&#32;)&#32;.</code></pre>|

***
### MinorFail Outcome number 159

[Jump to summary definition](#summary-MinorFail-159)	|	[Previous MinorFail outcome](#minorfail-outcome-number-158)	|	[Next MinorFail outcome](#minorfail-outcome-number-160)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-actuations-ontology|
|----|----|
|Title|Standalone&#32;module&#32;core&#92;actuations&#92;ontology.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- https://gitlab.com/coswot/coswot-acimov/blob/HEAD/core/actuations/ontology.ttl|

#### Criterion detail
|Identifier|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|
|----|----|
|Title|Profile&#32;compatibility&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;check&#32;whether&#32;the&#32;test&#32;subject&#32;is&#32;compatible&#32;with&#32;a&#32;profile&#32;or&#32;not,&#32;and&#32;if&#32;it&#32;is&#32;not,&#32;why.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-159)|Identifier|`owl-rl-profile-error`|
|[Section top](#minorfail-outcome-number-159)|Title|OWL&#32;RL&#32;Profile&#32;incompatible|
|[Section top](#minorfail-outcome-number-159)|Description|Statement&#32;not&#32;supported&#32;in&#32;a&#32;Super&#32;Class&#32;Expression|
|[Section top](#minorfail-outcome-number-159)|Pointer|<pre lang="Turtle"><code>&#91;]&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32;&#32; &#32;owl:onProperty&#32;coswot:controls&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-159)|Pointer|<pre lang="Turtle"><code>&#91;]&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32;owl:onProperty&#32;coswot:hasCommand&#32;;  &#10; &#32; &#32; &#32; &#32;owl:someValuesFrom&#32;coswot:ActuatingCommand&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-159)|Pointer|<pre lang="Turtle"><code>&#91;]&#32;a&#32;owl:Class&#32;;  &#10; &#32; &#32;&#32; &#32;owl:unionOf&#32;(&#32;coswot:Actuator&#32;coswot:ActuatingFunction&#32;coswot:ActuatingCommand&#32;coswot:Actuation&#32;)&#32;.</code></pre>|

***
### MinorFail Outcome number 160

[Jump to summary definition](#summary-MinorFail-160)	|	[Previous MinorFail outcome](#minorfail-outcome-number-159)	|	Next MinorFail outcome

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-actuations-ontology|
|----|----|
|Title|Standalone&#32;module&#32;core&#92;actuations&#92;ontology.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- https://gitlab.com/coswot/coswot-acimov/blob/HEAD/core/actuations/ontology.ttl|

#### Criterion detail
|Identifier|[terms-differenciation](https://ns.inria.fr/olivaw#terms-differenciation)|
|----|----|
|Title|Terms&#32;differenciation&#32;test|
|Description|A&#32;test&#32;case&#32;from&#32;the&#32;Best&#32;Practices&#32;tests&#32;checking&#32;if&#32;all&#32;the&#32;terms&#32;are&#32;different&#32;enough&#32;from&#32;each&#32;other&#32;according&#32;to&#32;the&#32;Levenshtein&#32;distance&#32;metric.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-160)|Identifier|`too-close-terms`|
|[Section top](#minorfail-outcome-number-160)|Title|Too&#32;close&#32;terms|
|[Section top](#minorfail-outcome-number-160)|Description|Some&#32;terms&#32;are&#32;too&#32;similar|
|[Section top](#minorfail-outcome-number-160)|Pointer|<pre lang="Turtle"><code>:Actuator&#32;a&#32;owl:Class&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;Actuator&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;Actuators&#32;are&#32;devices&#32;designed&#32;to&#32;control&#32;one&#32;or&#32;more&#32;proper...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32; &#60;https://w3id.org/coswot/core/actuations> &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:subClassOf&#32; &#91;&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:onProperty&#32;:controls&#32;],  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;:Device&#32;;  &#10; &#32; &#32; &#32; &#32;owl:disjointUnionOf&#32;(&#32;:ActuatorOfInterest&#32;:ActuatorKind&#32;)&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-160)|Pointer|<pre lang="Turtle"><code>:Actuation&#32;a&#32;owl:Class&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;Actuation&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;A&#32;coswot:Actuation&#32;is&#32;the&#32;act&#32;of&#32;carrying&#32;out&#32;a&#32;procedure&#32;to...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32; &#60;https://w3id.org/coswot/core/actuations> &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:subClassOf&#32; &#91;&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:allValuesFrom&#32;:Actuator&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:onProperty&#32;:madeBy&#32;],  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#91;&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:onProperty&#32;:controls&#32;],  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;:ProcedureExecution&#32;.</code></pre>|

***

</details>

***


# NotTested Outcomes

[Jump to statistic summary](#statistic-summary)	|	[Previous section](#minorfail-outcomes)	|	[Next section](#pass-outcomes)

Here is the chapter related to the NotTested outcome

:grey_question:10 NotTested outcomes

<details>
<summary>Fold/Unfold the 10 summary and details</summary>

## NotTested Outcomes Summary

:grey_question:10 NotTested outcomes

|*Jump*|*Number*|*Status*|*Subject*|*Criterion*|*Title*|*Link*|
|------|--------|--------|---------|-----------|-------|------|
|[Chapter top](#nottested-outcomes)|<div id="summary-NotTested-1">1/10</div>|:grey_question:NotTested|`module-coswot-saref`|[domain-and-range-referencing](https://ns.inria.fr/olivaw#domain-and-range-referencing)|The test could not be run|[Jump](#nottested-outcome-number-1)|
|[Chapter top](#nottested-outcomes)|<div id="summary-NotTested-2">2/10</div>|:grey_question:NotTested|`module-coswot-saref`|[domain-and-range-referencing](https://ns.inria.fr/olivaw#domain-and-range-referencing)|The test could not be run|[Jump](#nottested-outcome-number-2)|
|[Chapter top](#nottested-outcomes)|<div id="summary-NotTested-3">3/10</div>|:grey_question:NotTested|`module-coswot-saref`|[labeled-terms](https://ns.inria.fr/olivaw#labeled-terms)|The test could not be run|[Jump](#nottested-outcome-number-3)|
|[Chapter top](#nottested-outcomes)|<div id="summary-NotTested-4">4/10</div>|:grey_question:NotTested|`module-coswot-saref`|[labeled-terms](https://ns.inria.fr/olivaw#labeled-terms)|The test could not be run|[Jump](#nottested-outcome-number-4)|
|[Chapter top](#nottested-outcomes)|<div id="summary-NotTested-5">5/10</div>|:grey_question:NotTested|`module-coswot-saref`|[owl-rl-constraint](https://ns.inria.fr/olivaw#owl-rl-constraint)|The test could not be run|[Jump](#nottested-outcome-number-5)|
|[Chapter top](#nottested-outcomes)|<div id="summary-NotTested-6">6/10</div>|:grey_question:NotTested|`module-coswot-saref`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|The test could not be run|[Jump](#nottested-outcome-number-6)|
|[Chapter top](#nottested-outcomes)|<div id="summary-NotTested-7">7/10</div>|:grey_question:NotTested|`module-coswot-saref`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|The test could not be run|[Jump](#nottested-outcome-number-7)|
|[Chapter top](#nottested-outcomes)|<div id="summary-NotTested-8">8/10</div>|:grey_question:NotTested|`module-coswot-saref`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|The test could not be run|[Jump](#nottested-outcome-number-8)|
|[Chapter top](#nottested-outcomes)|<div id="summary-NotTested-9">9/10</div>|:grey_question:NotTested|`module-coswot-saref`|[term-referencing](https://ns.inria.fr/olivaw#term-referencing)|The test could not be run|[Jump](#nottested-outcome-number-9)|
|[Chapter top](#nottested-outcomes)|<div id="summary-NotTested-10">10/10</div>|:grey_question:NotTested|`module-coswot-saref`|[terms-differenciation](https://ns.inria.fr/olivaw#terms-differenciation)|The test could not be run|[Jump](#nottested-outcome-number-10)|

***

## NotTested Outcomes Details

This subchapter gives more details to the :grey_question:NotTested outcomes

### NotTested Outcome number 1

[Jump to summary definition](#summary-NotTested-1)	|	Previous NotTested outcome	|	[Next NotTested outcome](#nottested-outcome-number-2)

:grey_question:NotTested outcome
#### Subject detail
|Name|module-coswot-saref|
|----|----|
|Title|Standalone&#32;module&#32;core&#92;coswot-saref.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- https://gitlab.com/coswot/coswot-acimov/blob/HEAD/core/coswot-saref.ttl|

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
|Name|module-coswot-saref|
|----|----|
|Title|Standalone&#32;module&#32;core&#92;coswot-saref.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- https://gitlab.com/coswot/coswot-acimov/blob/HEAD/core/coswot-saref.ttl|

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
|Name|module-coswot-saref|
|----|----|
|Title|Standalone&#32;module&#32;core&#92;coswot-saref.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- https://gitlab.com/coswot/coswot-acimov/blob/HEAD/core/coswot-saref.ttl|

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
|Name|module-coswot-saref|
|----|----|
|Title|Standalone&#32;module&#32;core&#92;coswot-saref.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- https://gitlab.com/coswot/coswot-acimov/blob/HEAD/core/coswot-saref.ttl|

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
|Name|module-coswot-saref|
|----|----|
|Title|Standalone&#32;module&#32;core&#92;coswot-saref.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- https://gitlab.com/coswot/coswot-acimov/blob/HEAD/core/coswot-saref.ttl|

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
|Name|module-coswot-saref|
|----|----|
|Title|Standalone&#32;module&#32;core&#92;coswot-saref.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- https://gitlab.com/coswot/coswot-acimov/blob/HEAD/core/coswot-saref.ttl|

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
|Name|module-coswot-saref|
|----|----|
|Title|Standalone&#32;module&#32;core&#92;coswot-saref.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- https://gitlab.com/coswot/coswot-acimov/blob/HEAD/core/coswot-saref.ttl|

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
|Name|module-coswot-saref|
|----|----|
|Title|Standalone&#32;module&#32;core&#92;coswot-saref.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- https://gitlab.com/coswot/coswot-acimov/blob/HEAD/core/coswot-saref.ttl|

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
|Name|module-coswot-saref|
|----|----|
|Title|Standalone&#32;module&#32;core&#92;coswot-saref.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- https://gitlab.com/coswot/coswot-acimov/blob/HEAD/core/coswot-saref.ttl|

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

[Jump to summary definition](#summary-NotTested-10)	|	[Previous NotTested outcome](#nottested-outcome-number-9)	|	Next NotTested outcome

:grey_question:NotTested outcome
#### Subject detail
|Name|module-coswot-saref|
|----|----|
|Title|Standalone&#32;module&#32;core&#92;coswot-saref.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- https://gitlab.com/coswot/coswot-acimov/blob/HEAD/core/coswot-saref.ttl|

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

</details>

***


# Pass Outcomes

[Jump to statistic summary](#statistic-summary)	|	[Previous section](#nottested-outcomes)	|	Next section

Here is the chapter related to the Pass outcome

:white_check_mark:211 Pass outcomes

<details>
<summary>Fold/Unfold the 211 summary and details</summary>

## Pass Outcomes Summary

:white_check_mark:211 Pass outcomes

|*Jump*|*Number*|*Status*|*Subject*|*Criterion*|*Title*|*Link*|
|------|--------|--------|---------|-----------|-------|------|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-1">1/211</div>|:white_check_mark:Pass|`module-systems-ontology`|[domain-and-range-referencing](https://ns.inria.fr/olivaw#domain-and-range-referencing)|Domains properly defined|[Jump](#pass-outcome-number-1)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-2">2/211</div>|:white_check_mark:Pass|`module-systems-ontology`|[domain-and-range-referencing](https://ns.inria.fr/olivaw#domain-and-range-referencing)|Ranges properly defined|[Jump](#pass-outcome-number-2)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-3">3/211</div>|:white_check_mark:Pass|`module-systems-ontology`|[labeled-terms](https://ns.inria.fr/olivaw#labeled-terms)|All terms labeled|[Jump](#pass-outcome-number-3)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-4">4/211</div>|:white_check_mark:Pass|`module-systems-ontology`|[owl-rl-constraint](https://ns.inria.fr/olivaw#owl-rl-constraint)|OWL RL consistent|[Jump](#pass-outcome-number-4)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-5">5/211</div>|:white_check_mark:Pass|`module-systems-ontology`|[proper-extension-predicate](https://ns.inria.fr/olivaw#proper-extension-predicate)|No class subproperty|[Jump](#pass-outcome-number-5)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-6">6/211</div>|:white_check_mark:Pass|`module-systems-ontology`|[proper-extension-predicate](https://ns.inria.fr/olivaw#proper-extension-predicate)|No property subclass|[Jump](#pass-outcome-number-6)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-7">7/211</div>|:white_check_mark:Pass|`module-systems-ontology`|[proper-extension-predicate](https://ns.inria.fr/olivaw#proper-extension-predicate)|No subclass of property|[Jump](#pass-outcome-number-7)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-8">8/211</div>|:white_check_mark:Pass|`module-systems-ontology`|[proper-extension-predicate](https://ns.inria.fr/olivaw#proper-extension-predicate)|No subproperty of class|[Jump](#pass-outcome-number-8)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-9">9/211</div>|:white_check_mark:Pass|`module-systems-ontology`|[term-referencing](https://ns.inria.fr/olivaw#term-referencing)|Any term is referenced|[Jump](#pass-outcome-number-9)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-10">10/211</div>|:white_check_mark:Pass|`module-systems-ontology`|[terms-differenciation](https://ns.inria.fr/olivaw#terms-differenciation)|Terms differenciated enough|[Jump](#pass-outcome-number-10)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-11">11/211</div>|:white_check_mark:Pass|`module-states-ontology-catalog`|[labeled-terms](https://ns.inria.fr/olivaw#labeled-terms)|All terms labeled|[Jump](#pass-outcome-number-11)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-12">12/211</div>|:white_check_mark:Pass|`module-states-ontology-catalog`|[owl-rl-constraint](https://ns.inria.fr/olivaw#owl-rl-constraint)|OWL RL consistent|[Jump](#pass-outcome-number-12)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-13">13/211</div>|:white_check_mark:Pass|`module-states-ontology-catalog`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL RL Profile compatible|[Jump](#pass-outcome-number-13)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-14">14/211</div>|:white_check_mark:Pass|`module-states-ontology-catalog`|[proper-extension-predicate](https://ns.inria.fr/olivaw#proper-extension-predicate)|No class subproperty|[Jump](#pass-outcome-number-14)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-15">15/211</div>|:white_check_mark:Pass|`module-states-ontology-catalog`|[proper-extension-predicate](https://ns.inria.fr/olivaw#proper-extension-predicate)|No property subclass|[Jump](#pass-outcome-number-15)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-16">16/211</div>|:white_check_mark:Pass|`module-states-ontology-catalog`|[proper-extension-predicate](https://ns.inria.fr/olivaw#proper-extension-predicate)|No subclass of property|[Jump](#pass-outcome-number-16)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-17">17/211</div>|:white_check_mark:Pass|`module-states-ontology-catalog`|[proper-extension-predicate](https://ns.inria.fr/olivaw#proper-extension-predicate)|No subproperty of class|[Jump](#pass-outcome-number-17)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-18">18/211</div>|:white_check_mark:Pass|`module-states-ontology-catalog`|[term-referencing](https://ns.inria.fr/olivaw#term-referencing)|Any term is referenced|[Jump](#pass-outcome-number-18)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-19">19/211</div>|:white_check_mark:Pass|`module-states-ontology-catalog`|[terms-differenciation](https://ns.inria.fr/olivaw#terms-differenciation)|Terms differenciated enough|[Jump](#pass-outcome-number-19)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-20">20/211</div>|:white_check_mark:Pass|`module-states-ontology`|[labeled-terms](https://ns.inria.fr/olivaw#labeled-terms)|All terms labeled|[Jump](#pass-outcome-number-20)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-21">21/211</div>|:white_check_mark:Pass|`module-states-ontology`|[owl-rl-constraint](https://ns.inria.fr/olivaw#owl-rl-constraint)|OWL RL consistent|[Jump](#pass-outcome-number-21)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-22">22/211</div>|:white_check_mark:Pass|`module-states-ontology`|[proper-extension-predicate](https://ns.inria.fr/olivaw#proper-extension-predicate)|No class subproperty|[Jump](#pass-outcome-number-22)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-23">23/211</div>|:white_check_mark:Pass|`module-states-ontology`|[proper-extension-predicate](https://ns.inria.fr/olivaw#proper-extension-predicate)|No property subclass|[Jump](#pass-outcome-number-23)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-24">24/211</div>|:white_check_mark:Pass|`module-states-ontology`|[proper-extension-predicate](https://ns.inria.fr/olivaw#proper-extension-predicate)|No subclass of property|[Jump](#pass-outcome-number-24)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-25">25/211</div>|:white_check_mark:Pass|`module-states-ontology`|[proper-extension-predicate](https://ns.inria.fr/olivaw#proper-extension-predicate)|No subproperty of class|[Jump](#pass-outcome-number-25)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-26">26/211</div>|:white_check_mark:Pass|`module-states-ontology`|[term-referencing](https://ns.inria.fr/olivaw#term-referencing)|Any term is referenced|[Jump](#pass-outcome-number-26)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-27">27/211</div>|:white_check_mark:Pass|`module-states-ontology`|[terms-differenciation](https://ns.inria.fr/olivaw#terms-differenciation)|Terms differenciated enough|[Jump](#pass-outcome-number-27)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-28">28/211</div>|:white_check_mark:Pass|`module-services-operations-ontology`|[domain-and-range-referencing](https://ns.inria.fr/olivaw#domain-and-range-referencing)|Domains properly defined|[Jump](#pass-outcome-number-28)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-29">29/211</div>|:white_check_mark:Pass|`module-services-operations-ontology`|[domain-and-range-referencing](https://ns.inria.fr/olivaw#domain-and-range-referencing)|Ranges properly defined|[Jump](#pass-outcome-number-29)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-30">30/211</div>|:white_check_mark:Pass|`module-services-operations-ontology`|[labeled-terms](https://ns.inria.fr/olivaw#labeled-terms)|All terms labeled|[Jump](#pass-outcome-number-30)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-31">31/211</div>|:white_check_mark:Pass|`module-services-operations-ontology`|[owl-rl-constraint](https://ns.inria.fr/olivaw#owl-rl-constraint)|OWL RL consistent|[Jump](#pass-outcome-number-31)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-32">32/211</div>|:white_check_mark:Pass|`module-services-operations-ontology`|[proper-extension-predicate](https://ns.inria.fr/olivaw#proper-extension-predicate)|No class subproperty|[Jump](#pass-outcome-number-32)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-33">33/211</div>|:white_check_mark:Pass|`module-services-operations-ontology`|[proper-extension-predicate](https://ns.inria.fr/olivaw#proper-extension-predicate)|No property subclass|[Jump](#pass-outcome-number-33)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-34">34/211</div>|:white_check_mark:Pass|`module-services-operations-ontology`|[proper-extension-predicate](https://ns.inria.fr/olivaw#proper-extension-predicate)|No subclass of property|[Jump](#pass-outcome-number-34)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-35">35/211</div>|:white_check_mark:Pass|`module-services-operations-ontology`|[proper-extension-predicate](https://ns.inria.fr/olivaw#proper-extension-predicate)|No subproperty of class|[Jump](#pass-outcome-number-35)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-36">36/211</div>|:white_check_mark:Pass|`module-services-operations-ontology`|[terms-differenciation](https://ns.inria.fr/olivaw#terms-differenciation)|Terms differenciated enough|[Jump](#pass-outcome-number-36)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-37">37/211</div>|:white_check_mark:Pass|`module-samples-ontology`|[domain-and-range-referencing](https://ns.inria.fr/olivaw#domain-and-range-referencing)|Domains properly defined|[Jump](#pass-outcome-number-37)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-38">38/211</div>|:white_check_mark:Pass|`module-samples-ontology`|[domain-and-range-referencing](https://ns.inria.fr/olivaw#domain-and-range-referencing)|Ranges properly defined|[Jump](#pass-outcome-number-38)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-39">39/211</div>|:white_check_mark:Pass|`module-samples-ontology`|[labeled-terms](https://ns.inria.fr/olivaw#labeled-terms)|All terms labeled|[Jump](#pass-outcome-number-39)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-40">40/211</div>|:white_check_mark:Pass|`module-samples-ontology`|[owl-rl-constraint](https://ns.inria.fr/olivaw#owl-rl-constraint)|OWL RL consistent|[Jump](#pass-outcome-number-40)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-41">41/211</div>|:white_check_mark:Pass|`module-samples-ontology`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL RL Profile compatible|[Jump](#pass-outcome-number-41)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-42">42/211</div>|:white_check_mark:Pass|`module-samples-ontology`|[proper-extension-predicate](https://ns.inria.fr/olivaw#proper-extension-predicate)|No class subproperty|[Jump](#pass-outcome-number-42)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-43">43/211</div>|:white_check_mark:Pass|`module-samples-ontology`|[proper-extension-predicate](https://ns.inria.fr/olivaw#proper-extension-predicate)|No property subclass|[Jump](#pass-outcome-number-43)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-44">44/211</div>|:white_check_mark:Pass|`module-samples-ontology`|[proper-extension-predicate](https://ns.inria.fr/olivaw#proper-extension-predicate)|No subclass of property|[Jump](#pass-outcome-number-44)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-45">45/211</div>|:white_check_mark:Pass|`module-samples-ontology`|[proper-extension-predicate](https://ns.inria.fr/olivaw#proper-extension-predicate)|No subproperty of class|[Jump](#pass-outcome-number-45)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-46">46/211</div>|:white_check_mark:Pass|`module-samples-ontology`|[term-referencing](https://ns.inria.fr/olivaw#term-referencing)|Any term is referenced|[Jump](#pass-outcome-number-46)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-47">47/211</div>|:white_check_mark:Pass|`module-samples-ontology`|[terms-differenciation](https://ns.inria.fr/olivaw#terms-differenciation)|Terms differenciated enough|[Jump](#pass-outcome-number-47)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-48">48/211</div>|:white_check_mark:Pass|`module-property-values-ontology`|[domain-and-range-referencing](https://ns.inria.fr/olivaw#domain-and-range-referencing)|Domains properly defined|[Jump](#pass-outcome-number-48)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-49">49/211</div>|:white_check_mark:Pass|`module-property-values-ontology`|[labeled-terms](https://ns.inria.fr/olivaw#labeled-terms)|All terms labeled|[Jump](#pass-outcome-number-49)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-50">50/211</div>|:white_check_mark:Pass|`module-property-values-ontology`|[owl-rl-constraint](https://ns.inria.fr/olivaw#owl-rl-constraint)|OWL RL consistent|[Jump](#pass-outcome-number-50)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-51">51/211</div>|:white_check_mark:Pass|`module-property-values-ontology`|[proper-extension-predicate](https://ns.inria.fr/olivaw#proper-extension-predicate)|No class subproperty|[Jump](#pass-outcome-number-51)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-52">52/211</div>|:white_check_mark:Pass|`module-property-values-ontology`|[proper-extension-predicate](https://ns.inria.fr/olivaw#proper-extension-predicate)|No property subclass|[Jump](#pass-outcome-number-52)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-53">53/211</div>|:white_check_mark:Pass|`module-property-values-ontology`|[proper-extension-predicate](https://ns.inria.fr/olivaw#proper-extension-predicate)|No subclass of property|[Jump](#pass-outcome-number-53)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-54">54/211</div>|:white_check_mark:Pass|`module-property-values-ontology`|[proper-extension-predicate](https://ns.inria.fr/olivaw#proper-extension-predicate)|No subproperty of class|[Jump](#pass-outcome-number-54)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-55">55/211</div>|:white_check_mark:Pass|`module-property-values-ontology`|[term-referencing](https://ns.inria.fr/olivaw#term-referencing)|Any term is referenced|[Jump](#pass-outcome-number-55)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-56">56/211</div>|:white_check_mark:Pass|`module-property-values-ontology`|[terms-differenciation](https://ns.inria.fr/olivaw#terms-differenciation)|Terms differenciated enough|[Jump](#pass-outcome-number-56)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-57">57/211</div>|:white_check_mark:Pass|`module-properties-ontology-catalogs`|[labeled-terms](https://ns.inria.fr/olivaw#labeled-terms)|All terms labeled|[Jump](#pass-outcome-number-57)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-58">58/211</div>|:white_check_mark:Pass|`module-properties-ontology-catalogs`|[owl-rl-constraint](https://ns.inria.fr/olivaw#owl-rl-constraint)|OWL RL consistent|[Jump](#pass-outcome-number-58)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-59">59/211</div>|:white_check_mark:Pass|`module-properties-ontology-catalogs`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL RL Profile compatible|[Jump](#pass-outcome-number-59)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-60">60/211</div>|:white_check_mark:Pass|`module-properties-ontology-catalogs`|[proper-extension-predicate](https://ns.inria.fr/olivaw#proper-extension-predicate)|No class subproperty|[Jump](#pass-outcome-number-60)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-61">61/211</div>|:white_check_mark:Pass|`module-properties-ontology-catalogs`|[proper-extension-predicate](https://ns.inria.fr/olivaw#proper-extension-predicate)|No property subclass|[Jump](#pass-outcome-number-61)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-62">62/211</div>|:white_check_mark:Pass|`module-properties-ontology-catalogs`|[proper-extension-predicate](https://ns.inria.fr/olivaw#proper-extension-predicate)|No subclass of property|[Jump](#pass-outcome-number-62)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-63">63/211</div>|:white_check_mark:Pass|`module-properties-ontology-catalogs`|[proper-extension-predicate](https://ns.inria.fr/olivaw#proper-extension-predicate)|No subproperty of class|[Jump](#pass-outcome-number-63)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-64">64/211</div>|:white_check_mark:Pass|`module-properties-ontology-catalogs`|[term-referencing](https://ns.inria.fr/olivaw#term-referencing)|Any term is referenced|[Jump](#pass-outcome-number-64)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-65">65/211</div>|:white_check_mark:Pass|`module-properties-ontology-catalogs`|[terms-differenciation](https://ns.inria.fr/olivaw#terms-differenciation)|Terms differenciated enough|[Jump](#pass-outcome-number-65)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-66">66/211</div>|:white_check_mark:Pass|`module-properties-ontology`|[labeled-terms](https://ns.inria.fr/olivaw#labeled-terms)|All terms labeled|[Jump](#pass-outcome-number-66)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-67">67/211</div>|:white_check_mark:Pass|`module-properties-ontology`|[owl-rl-constraint](https://ns.inria.fr/olivaw#owl-rl-constraint)|OWL RL consistent|[Jump](#pass-outcome-number-67)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-68">68/211</div>|:white_check_mark:Pass|`module-properties-ontology`|[proper-extension-predicate](https://ns.inria.fr/olivaw#proper-extension-predicate)|No class subproperty|[Jump](#pass-outcome-number-68)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-69">69/211</div>|:white_check_mark:Pass|`module-properties-ontology`|[proper-extension-predicate](https://ns.inria.fr/olivaw#proper-extension-predicate)|No property subclass|[Jump](#pass-outcome-number-69)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-70">70/211</div>|:white_check_mark:Pass|`module-properties-ontology`|[proper-extension-predicate](https://ns.inria.fr/olivaw#proper-extension-predicate)|No subclass of property|[Jump](#pass-outcome-number-70)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-71">71/211</div>|:white_check_mark:Pass|`module-properties-ontology`|[proper-extension-predicate](https://ns.inria.fr/olivaw#proper-extension-predicate)|No subproperty of class|[Jump](#pass-outcome-number-71)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-72">72/211</div>|:white_check_mark:Pass|`module-properties-ontology`|[term-referencing](https://ns.inria.fr/olivaw#term-referencing)|Any term is referenced|[Jump](#pass-outcome-number-72)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-73">73/211</div>|:white_check_mark:Pass|`module-properties-ontology`|[terms-differenciation](https://ns.inria.fr/olivaw#terms-differenciation)|Terms differenciated enough|[Jump](#pass-outcome-number-73)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-74">74/211</div>|:white_check_mark:Pass|`module-procedures-ontology`|[domain-and-range-referencing](https://ns.inria.fr/olivaw#domain-and-range-referencing)|Domains properly defined|[Jump](#pass-outcome-number-74)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-75">75/211</div>|:white_check_mark:Pass|`module-procedures-ontology`|[labeled-terms](https://ns.inria.fr/olivaw#labeled-terms)|All terms labeled|[Jump](#pass-outcome-number-75)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-76">76/211</div>|:white_check_mark:Pass|`module-procedures-ontology`|[owl-rl-constraint](https://ns.inria.fr/olivaw#owl-rl-constraint)|OWL RL consistent|[Jump](#pass-outcome-number-76)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-77">77/211</div>|:white_check_mark:Pass|`module-procedures-ontology`|[proper-extension-predicate](https://ns.inria.fr/olivaw#proper-extension-predicate)|No class subproperty|[Jump](#pass-outcome-number-77)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-78">78/211</div>|:white_check_mark:Pass|`module-procedures-ontology`|[proper-extension-predicate](https://ns.inria.fr/olivaw#proper-extension-predicate)|No property subclass|[Jump](#pass-outcome-number-78)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-79">79/211</div>|:white_check_mark:Pass|`module-procedures-ontology`|[proper-extension-predicate](https://ns.inria.fr/olivaw#proper-extension-predicate)|No subclass of property|[Jump](#pass-outcome-number-79)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-80">80/211</div>|:white_check_mark:Pass|`module-procedures-ontology`|[proper-extension-predicate](https://ns.inria.fr/olivaw#proper-extension-predicate)|No subproperty of class|[Jump](#pass-outcome-number-80)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-81">81/211</div>|:white_check_mark:Pass|`module-procedures-ontology`|[term-referencing](https://ns.inria.fr/olivaw#term-referencing)|Any term is referenced|[Jump](#pass-outcome-number-81)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-82">82/211</div>|:white_check_mark:Pass|`module-procedures-ontology`|[terms-differenciation](https://ns.inria.fr/olivaw#terms-differenciation)|Terms differenciated enough|[Jump](#pass-outcome-number-82)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-83">83/211</div>|:white_check_mark:Pass|`module-ontology`|[domain-and-range-referencing](https://ns.inria.fr/olivaw#domain-and-range-referencing)|Domains properly defined|[Jump](#pass-outcome-number-83)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-84">84/211</div>|:white_check_mark:Pass|`module-ontology`|[domain-and-range-referencing](https://ns.inria.fr/olivaw#domain-and-range-referencing)|Ranges properly defined|[Jump](#pass-outcome-number-84)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-85">85/211</div>|:white_check_mark:Pass|`module-ontology`|[labeled-terms](https://ns.inria.fr/olivaw#labeled-terms)|All terms labeled|[Jump](#pass-outcome-number-85)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-86">86/211</div>|:white_check_mark:Pass|`module-ontology`|[owl-rl-constraint](https://ns.inria.fr/olivaw#owl-rl-constraint)|OWL RL consistent|[Jump](#pass-outcome-number-86)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-87">87/211</div>|:white_check_mark:Pass|`module-ontology`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL EL Profile compatible|[Jump](#pass-outcome-number-87)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-88">88/211</div>|:white_check_mark:Pass|`module-ontology`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL QL Profile compatible|[Jump](#pass-outcome-number-88)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-89">89/211</div>|:white_check_mark:Pass|`module-ontology`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL RL Profile compatible|[Jump](#pass-outcome-number-89)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-90">90/211</div>|:white_check_mark:Pass|`module-ontology`|[proper-extension-predicate](https://ns.inria.fr/olivaw#proper-extension-predicate)|No class subproperty|[Jump](#pass-outcome-number-90)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-91">91/211</div>|:white_check_mark:Pass|`module-ontology`|[proper-extension-predicate](https://ns.inria.fr/olivaw#proper-extension-predicate)|No property subclass|[Jump](#pass-outcome-number-91)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-92">92/211</div>|:white_check_mark:Pass|`module-ontology`|[proper-extension-predicate](https://ns.inria.fr/olivaw#proper-extension-predicate)|No subclass of property|[Jump](#pass-outcome-number-92)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-93">93/211</div>|:white_check_mark:Pass|`module-ontology`|[proper-extension-predicate](https://ns.inria.fr/olivaw#proper-extension-predicate)|No subproperty of class|[Jump](#pass-outcome-number-93)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-94">94/211</div>|:white_check_mark:Pass|`module-ontology`|[term-referencing](https://ns.inria.fr/olivaw#term-referencing)|Any term is referenced|[Jump](#pass-outcome-number-94)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-95">95/211</div>|:white_check_mark:Pass|`module-ontology`|[terms-differenciation](https://ns.inria.fr/olivaw#terms-differenciation)|Terms differenciated enough|[Jump](#pass-outcome-number-95)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-96">96/211</div>|:white_check_mark:Pass|`module-observations-ontology`|[domain-and-range-referencing](https://ns.inria.fr/olivaw#domain-and-range-referencing)|Domains properly defined|[Jump](#pass-outcome-number-96)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-97">97/211</div>|:white_check_mark:Pass|`module-observations-ontology`|[domain-and-range-referencing](https://ns.inria.fr/olivaw#domain-and-range-referencing)|Ranges properly defined|[Jump](#pass-outcome-number-97)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-98">98/211</div>|:white_check_mark:Pass|`module-observations-ontology`|[labeled-terms](https://ns.inria.fr/olivaw#labeled-terms)|All terms labeled|[Jump](#pass-outcome-number-98)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-99">99/211</div>|:white_check_mark:Pass|`module-observations-ontology`|[owl-rl-constraint](https://ns.inria.fr/olivaw#owl-rl-constraint)|OWL RL consistent|[Jump](#pass-outcome-number-99)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-100">100/211</div>|:white_check_mark:Pass|`module-observations-ontology`|[proper-extension-predicate](https://ns.inria.fr/olivaw#proper-extension-predicate)|No class subproperty|[Jump](#pass-outcome-number-100)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-101">101/211</div>|:white_check_mark:Pass|`module-observations-ontology`|[proper-extension-predicate](https://ns.inria.fr/olivaw#proper-extension-predicate)|No property subclass|[Jump](#pass-outcome-number-101)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-102">102/211</div>|:white_check_mark:Pass|`module-observations-ontology`|[proper-extension-predicate](https://ns.inria.fr/olivaw#proper-extension-predicate)|No subclass of property|[Jump](#pass-outcome-number-102)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-103">103/211</div>|:white_check_mark:Pass|`module-observations-ontology`|[proper-extension-predicate](https://ns.inria.fr/olivaw#proper-extension-predicate)|No subproperty of class|[Jump](#pass-outcome-number-103)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-104">104/211</div>|:white_check_mark:Pass|`module-observations-ontology`|[term-referencing](https://ns.inria.fr/olivaw#term-referencing)|Any term is referenced|[Jump](#pass-outcome-number-104)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-105">105/211</div>|:white_check_mark:Pass|`module-observations-ontology`|[terms-differenciation](https://ns.inria.fr/olivaw#terms-differenciation)|Terms differenciated enough|[Jump](#pass-outcome-number-105)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-106">106/211</div>|:white_check_mark:Pass|`module-functions-commands-ontology`|[domain-and-range-referencing](https://ns.inria.fr/olivaw#domain-and-range-referencing)|Domains properly defined|[Jump](#pass-outcome-number-106)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-107">107/211</div>|:white_check_mark:Pass|`module-functions-commands-ontology`|[domain-and-range-referencing](https://ns.inria.fr/olivaw#domain-and-range-referencing)|Ranges properly defined|[Jump](#pass-outcome-number-107)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-108">108/211</div>|:white_check_mark:Pass|`module-functions-commands-ontology`|[labeled-terms](https://ns.inria.fr/olivaw#labeled-terms)|All terms labeled|[Jump](#pass-outcome-number-108)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-109">109/211</div>|:white_check_mark:Pass|`module-functions-commands-ontology`|[owl-rl-constraint](https://ns.inria.fr/olivaw#owl-rl-constraint)|OWL RL consistent|[Jump](#pass-outcome-number-109)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-110">110/211</div>|:white_check_mark:Pass|`module-functions-commands-ontology`|[proper-extension-predicate](https://ns.inria.fr/olivaw#proper-extension-predicate)|No class subproperty|[Jump](#pass-outcome-number-110)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-111">111/211</div>|:white_check_mark:Pass|`module-functions-commands-ontology`|[proper-extension-predicate](https://ns.inria.fr/olivaw#proper-extension-predicate)|No property subclass|[Jump](#pass-outcome-number-111)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-112">112/211</div>|:white_check_mark:Pass|`module-functions-commands-ontology`|[proper-extension-predicate](https://ns.inria.fr/olivaw#proper-extension-predicate)|No subclass of property|[Jump](#pass-outcome-number-112)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-113">113/211</div>|:white_check_mark:Pass|`module-functions-commands-ontology`|[proper-extension-predicate](https://ns.inria.fr/olivaw#proper-extension-predicate)|No subproperty of class|[Jump](#pass-outcome-number-113)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-114">114/211</div>|:white_check_mark:Pass|`module-functions-commands-ontology`|[terms-differenciation](https://ns.inria.fr/olivaw#terms-differenciation)|Terms differenciated enough|[Jump](#pass-outcome-number-114)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-115">115/211</div>|:white_check_mark:Pass|`module-features-ontology-catalogs`|[domain-and-range-referencing](https://ns.inria.fr/olivaw#domain-and-range-referencing)|Domains properly defined|[Jump](#pass-outcome-number-115)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-116">116/211</div>|:white_check_mark:Pass|`module-features-ontology-catalogs`|[domain-and-range-referencing](https://ns.inria.fr/olivaw#domain-and-range-referencing)|Ranges properly defined|[Jump](#pass-outcome-number-116)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-117">117/211</div>|:white_check_mark:Pass|`module-features-ontology-catalogs`|[labeled-terms](https://ns.inria.fr/olivaw#labeled-terms)|All terms labeled|[Jump](#pass-outcome-number-117)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-118">118/211</div>|:white_check_mark:Pass|`module-features-ontology-catalogs`|[owl-rl-constraint](https://ns.inria.fr/olivaw#owl-rl-constraint)|OWL RL consistent|[Jump](#pass-outcome-number-118)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-119">119/211</div>|:white_check_mark:Pass|`module-features-ontology-catalogs`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL RL Profile compatible|[Jump](#pass-outcome-number-119)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-120">120/211</div>|:white_check_mark:Pass|`module-features-ontology-catalogs`|[proper-extension-predicate](https://ns.inria.fr/olivaw#proper-extension-predicate)|No class subproperty|[Jump](#pass-outcome-number-120)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-121">121/211</div>|:white_check_mark:Pass|`module-features-ontology-catalogs`|[proper-extension-predicate](https://ns.inria.fr/olivaw#proper-extension-predicate)|No property subclass|[Jump](#pass-outcome-number-121)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-122">122/211</div>|:white_check_mark:Pass|`module-features-ontology-catalogs`|[proper-extension-predicate](https://ns.inria.fr/olivaw#proper-extension-predicate)|No subclass of property|[Jump](#pass-outcome-number-122)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-123">123/211</div>|:white_check_mark:Pass|`module-features-ontology-catalogs`|[proper-extension-predicate](https://ns.inria.fr/olivaw#proper-extension-predicate)|No subproperty of class|[Jump](#pass-outcome-number-123)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-124">124/211</div>|:white_check_mark:Pass|`module-features-ontology-catalogs`|[term-referencing](https://ns.inria.fr/olivaw#term-referencing)|Any term is referenced|[Jump](#pass-outcome-number-124)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-125">125/211</div>|:white_check_mark:Pass|`module-features-ontology-catalogs`|[terms-differenciation](https://ns.inria.fr/olivaw#terms-differenciation)|Terms differenciated enough|[Jump](#pass-outcome-number-125)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-126">126/211</div>|:white_check_mark:Pass|`module-features-ontology`|[domain-and-range-referencing](https://ns.inria.fr/olivaw#domain-and-range-referencing)|Domains properly defined|[Jump](#pass-outcome-number-126)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-127">127/211</div>|:white_check_mark:Pass|`module-features-ontology`|[domain-and-range-referencing](https://ns.inria.fr/olivaw#domain-and-range-referencing)|Ranges properly defined|[Jump](#pass-outcome-number-127)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-128">128/211</div>|:white_check_mark:Pass|`module-features-ontology`|[labeled-terms](https://ns.inria.fr/olivaw#labeled-terms)|All terms labeled|[Jump](#pass-outcome-number-128)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-129">129/211</div>|:white_check_mark:Pass|`module-features-ontology`|[owl-rl-constraint](https://ns.inria.fr/olivaw#owl-rl-constraint)|OWL RL consistent|[Jump](#pass-outcome-number-129)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-130">130/211</div>|:white_check_mark:Pass|`module-features-ontology`|[proper-extension-predicate](https://ns.inria.fr/olivaw#proper-extension-predicate)|No class subproperty|[Jump](#pass-outcome-number-130)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-131">131/211</div>|:white_check_mark:Pass|`module-features-ontology`|[proper-extension-predicate](https://ns.inria.fr/olivaw#proper-extension-predicate)|No property subclass|[Jump](#pass-outcome-number-131)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-132">132/211</div>|:white_check_mark:Pass|`module-features-ontology`|[proper-extension-predicate](https://ns.inria.fr/olivaw#proper-extension-predicate)|No subclass of property|[Jump](#pass-outcome-number-132)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-133">133/211</div>|:white_check_mark:Pass|`module-features-ontology`|[proper-extension-predicate](https://ns.inria.fr/olivaw#proper-extension-predicate)|No subproperty of class|[Jump](#pass-outcome-number-133)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-134">134/211</div>|:white_check_mark:Pass|`module-features-ontology`|[term-referencing](https://ns.inria.fr/olivaw#term-referencing)|Any term is referenced|[Jump](#pass-outcome-number-134)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-135">135/211</div>|:white_check_mark:Pass|`module-features-ontology`|[terms-differenciation](https://ns.inria.fr/olivaw#terms-differenciation)|Terms differenciated enough|[Jump](#pass-outcome-number-135)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-136">136/211</div>|:white_check_mark:Pass|`module-devices-ontology`|[domain-and-range-referencing](https://ns.inria.fr/olivaw#domain-and-range-referencing)|Domains properly defined|[Jump](#pass-outcome-number-136)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-137">137/211</div>|:white_check_mark:Pass|`module-devices-ontology`|[domain-and-range-referencing](https://ns.inria.fr/olivaw#domain-and-range-referencing)|Ranges properly defined|[Jump](#pass-outcome-number-137)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-138">138/211</div>|:white_check_mark:Pass|`module-devices-ontology`|[labeled-terms](https://ns.inria.fr/olivaw#labeled-terms)|All terms labeled|[Jump](#pass-outcome-number-138)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-139">139/211</div>|:white_check_mark:Pass|`module-devices-ontology`|[owl-rl-constraint](https://ns.inria.fr/olivaw#owl-rl-constraint)|OWL RL consistent|[Jump](#pass-outcome-number-139)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-140">140/211</div>|:white_check_mark:Pass|`module-devices-ontology`|[proper-extension-predicate](https://ns.inria.fr/olivaw#proper-extension-predicate)|No class subproperty|[Jump](#pass-outcome-number-140)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-141">141/211</div>|:white_check_mark:Pass|`module-devices-ontology`|[proper-extension-predicate](https://ns.inria.fr/olivaw#proper-extension-predicate)|No property subclass|[Jump](#pass-outcome-number-141)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-142">142/211</div>|:white_check_mark:Pass|`module-devices-ontology`|[proper-extension-predicate](https://ns.inria.fr/olivaw#proper-extension-predicate)|No subclass of property|[Jump](#pass-outcome-number-142)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-143">143/211</div>|:white_check_mark:Pass|`module-devices-ontology`|[proper-extension-predicate](https://ns.inria.fr/olivaw#proper-extension-predicate)|No subproperty of class|[Jump](#pass-outcome-number-143)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-144">144/211</div>|:white_check_mark:Pass|`module-devices-ontology`|[term-referencing](https://ns.inria.fr/olivaw#term-referencing)|Any term is referenced|[Jump](#pass-outcome-number-144)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-145">145/211</div>|:white_check_mark:Pass|`module-devices-ontology`|[terms-differenciation](https://ns.inria.fr/olivaw#terms-differenciation)|Terms differenciated enough|[Jump](#pass-outcome-number-145)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-146">146/211</div>|:white_check_mark:Pass|`module-coswot-sosa`|[domain-and-range-referencing](https://ns.inria.fr/olivaw#domain-and-range-referencing)|Domains properly defined|[Jump](#pass-outcome-number-146)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-147">147/211</div>|:white_check_mark:Pass|`module-coswot-sosa`|[domain-and-range-referencing](https://ns.inria.fr/olivaw#domain-and-range-referencing)|Ranges properly defined|[Jump](#pass-outcome-number-147)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-148">148/211</div>|:white_check_mark:Pass|`module-coswot-sosa`|[labeled-terms](https://ns.inria.fr/olivaw#labeled-terms)|All terms labeled|[Jump](#pass-outcome-number-148)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-149">149/211</div>|:white_check_mark:Pass|`module-coswot-sosa`|[owl-rl-constraint](https://ns.inria.fr/olivaw#owl-rl-constraint)|OWL RL consistent|[Jump](#pass-outcome-number-149)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-150">150/211</div>|:white_check_mark:Pass|`module-coswot-sosa`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL EL Profile compatible|[Jump](#pass-outcome-number-150)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-151">151/211</div>|:white_check_mark:Pass|`module-coswot-sosa`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL QL Profile compatible|[Jump](#pass-outcome-number-151)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-152">152/211</div>|:white_check_mark:Pass|`module-coswot-sosa`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL RL Profile compatible|[Jump](#pass-outcome-number-152)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-153">153/211</div>|:white_check_mark:Pass|`module-coswot-sosa`|[proper-extension-predicate](https://ns.inria.fr/olivaw#proper-extension-predicate)|No class subproperty|[Jump](#pass-outcome-number-153)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-154">154/211</div>|:white_check_mark:Pass|`module-coswot-sosa`|[proper-extension-predicate](https://ns.inria.fr/olivaw#proper-extension-predicate)|No property subclass|[Jump](#pass-outcome-number-154)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-155">155/211</div>|:white_check_mark:Pass|`module-coswot-sosa`|[proper-extension-predicate](https://ns.inria.fr/olivaw#proper-extension-predicate)|No subclass of property|[Jump](#pass-outcome-number-155)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-156">156/211</div>|:white_check_mark:Pass|`module-coswot-sosa`|[proper-extension-predicate](https://ns.inria.fr/olivaw#proper-extension-predicate)|No subproperty of class|[Jump](#pass-outcome-number-156)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-157">157/211</div>|:white_check_mark:Pass|`module-coswot-sosa`|[terms-differenciation](https://ns.inria.fr/olivaw#terms-differenciation)|Terms differenciated enough|[Jump](#pass-outcome-number-157)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-158">158/211</div>|:white_check_mark:Pass|`module-communications-ontology`|[domain-and-range-referencing](https://ns.inria.fr/olivaw#domain-and-range-referencing)|Domains properly defined|[Jump](#pass-outcome-number-158)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-159">159/211</div>|:white_check_mark:Pass|`module-communications-ontology`|[domain-and-range-referencing](https://ns.inria.fr/olivaw#domain-and-range-referencing)|Ranges properly defined|[Jump](#pass-outcome-number-159)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-160">160/211</div>|:white_check_mark:Pass|`module-communications-ontology`|[labeled-terms](https://ns.inria.fr/olivaw#labeled-terms)|All terms labeled|[Jump](#pass-outcome-number-160)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-161">161/211</div>|:white_check_mark:Pass|`module-communications-ontology`|[owl-rl-constraint](https://ns.inria.fr/olivaw#owl-rl-constraint)|OWL RL consistent|[Jump](#pass-outcome-number-161)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-162">162/211</div>|:white_check_mark:Pass|`module-communications-ontology`|[proper-extension-predicate](https://ns.inria.fr/olivaw#proper-extension-predicate)|No class subproperty|[Jump](#pass-outcome-number-162)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-163">163/211</div>|:white_check_mark:Pass|`module-communications-ontology`|[proper-extension-predicate](https://ns.inria.fr/olivaw#proper-extension-predicate)|No property subclass|[Jump](#pass-outcome-number-163)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-164">164/211</div>|:white_check_mark:Pass|`module-communications-ontology`|[proper-extension-predicate](https://ns.inria.fr/olivaw#proper-extension-predicate)|No subclass of property|[Jump](#pass-outcome-number-164)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-165">165/211</div>|:white_check_mark:Pass|`module-communications-ontology`|[proper-extension-predicate](https://ns.inria.fr/olivaw#proper-extension-predicate)|No subproperty of class|[Jump](#pass-outcome-number-165)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-166">166/211</div>|:white_check_mark:Pass|`module-communications-ontology`|[term-referencing](https://ns.inria.fr/olivaw#term-referencing)|Any term is referenced|[Jump](#pass-outcome-number-166)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-167">167/211</div>|:white_check_mark:Pass|`module-communications-ontology`|[terms-differenciation](https://ns.inria.fr/olivaw#terms-differenciation)|Terms differenciated enough|[Jump](#pass-outcome-number-167)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-168">168/211</div>|:white_check_mark:Pass|`module-aggregations-ontology`|[domain-and-range-referencing](https://ns.inria.fr/olivaw#domain-and-range-referencing)|Domains properly defined|[Jump](#pass-outcome-number-168)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-169">169/211</div>|:white_check_mark:Pass|`module-aggregations-ontology`|[labeled-terms](https://ns.inria.fr/olivaw#labeled-terms)|All terms labeled|[Jump](#pass-outcome-number-169)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-170">170/211</div>|:white_check_mark:Pass|`module-aggregations-ontology`|[owl-rl-constraint](https://ns.inria.fr/olivaw#owl-rl-constraint)|OWL RL consistent|[Jump](#pass-outcome-number-170)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-171">171/211</div>|:white_check_mark:Pass|`module-aggregations-ontology`|[proper-extension-predicate](https://ns.inria.fr/olivaw#proper-extension-predicate)|No class subproperty|[Jump](#pass-outcome-number-171)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-172">172/211</div>|:white_check_mark:Pass|`module-aggregations-ontology`|[proper-extension-predicate](https://ns.inria.fr/olivaw#proper-extension-predicate)|No property subclass|[Jump](#pass-outcome-number-172)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-173">173/211</div>|:white_check_mark:Pass|`module-aggregations-ontology`|[proper-extension-predicate](https://ns.inria.fr/olivaw#proper-extension-predicate)|No subclass of property|[Jump](#pass-outcome-number-173)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-174">174/211</div>|:white_check_mark:Pass|`module-aggregations-ontology`|[proper-extension-predicate](https://ns.inria.fr/olivaw#proper-extension-predicate)|No subproperty of class|[Jump](#pass-outcome-number-174)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-175">175/211</div>|:white_check_mark:Pass|`module-aggregations-ontology`|[term-referencing](https://ns.inria.fr/olivaw#term-referencing)|Any term is referenced|[Jump](#pass-outcome-number-175)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-176">176/211</div>|:white_check_mark:Pass|`module-aggregations-ontology`|[terms-differenciation](https://ns.inria.fr/olivaw#terms-differenciation)|Terms differenciated enough|[Jump](#pass-outcome-number-176)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-177">177/211</div>|:white_check_mark:Pass|`module-aggregations-aggregation-kind-thesaurus`|[domain-and-range-referencing](https://ns.inria.fr/olivaw#domain-and-range-referencing)|Domains properly defined|[Jump](#pass-outcome-number-177)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-178">178/211</div>|:white_check_mark:Pass|`module-aggregations-aggregation-kind-thesaurus`|[domain-and-range-referencing](https://ns.inria.fr/olivaw#domain-and-range-referencing)|Ranges properly defined|[Jump](#pass-outcome-number-178)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-179">179/211</div>|:white_check_mark:Pass|`module-aggregations-aggregation-kind-thesaurus`|[labeled-terms](https://ns.inria.fr/olivaw#labeled-terms)|All terms labeled|[Jump](#pass-outcome-number-179)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-180">180/211</div>|:white_check_mark:Pass|`module-aggregations-aggregation-kind-thesaurus`|[owl-rl-constraint](https://ns.inria.fr/olivaw#owl-rl-constraint)|OWL RL consistent|[Jump](#pass-outcome-number-180)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-181">181/211</div>|:white_check_mark:Pass|`module-aggregations-aggregation-kind-thesaurus`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL EL Profile compatible|[Jump](#pass-outcome-number-181)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-182">182/211</div>|:white_check_mark:Pass|`module-aggregations-aggregation-kind-thesaurus`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL QL Profile compatible|[Jump](#pass-outcome-number-182)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-183">183/211</div>|:white_check_mark:Pass|`module-aggregations-aggregation-kind-thesaurus`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL RL Profile compatible|[Jump](#pass-outcome-number-183)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-184">184/211</div>|:white_check_mark:Pass|`module-aggregations-aggregation-kind-thesaurus`|[proper-extension-predicate](https://ns.inria.fr/olivaw#proper-extension-predicate)|No class subproperty|[Jump](#pass-outcome-number-184)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-185">185/211</div>|:white_check_mark:Pass|`module-aggregations-aggregation-kind-thesaurus`|[proper-extension-predicate](https://ns.inria.fr/olivaw#proper-extension-predicate)|No property subclass|[Jump](#pass-outcome-number-185)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-186">186/211</div>|:white_check_mark:Pass|`module-aggregations-aggregation-kind-thesaurus`|[proper-extension-predicate](https://ns.inria.fr/olivaw#proper-extension-predicate)|No subclass of property|[Jump](#pass-outcome-number-186)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-187">187/211</div>|:white_check_mark:Pass|`module-aggregations-aggregation-kind-thesaurus`|[proper-extension-predicate](https://ns.inria.fr/olivaw#proper-extension-predicate)|No subproperty of class|[Jump](#pass-outcome-number-187)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-188">188/211</div>|:white_check_mark:Pass|`module-aggregations-aggregation-kind-thesaurus`|[term-referencing](https://ns.inria.fr/olivaw#term-referencing)|Any term is referenced|[Jump](#pass-outcome-number-188)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-189">189/211</div>|:white_check_mark:Pass|`module-aggregations-aggregation-kind-thesaurus`|[terms-differenciation](https://ns.inria.fr/olivaw#terms-differenciation)|Terms differenciated enough|[Jump](#pass-outcome-number-189)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-190">190/211</div>|:white_check_mark:Pass|`module-affordances-ontology`|[domain-and-range-referencing](https://ns.inria.fr/olivaw#domain-and-range-referencing)|Domains properly defined|[Jump](#pass-outcome-number-190)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-191">191/211</div>|:white_check_mark:Pass|`module-affordances-ontology`|[domain-and-range-referencing](https://ns.inria.fr/olivaw#domain-and-range-referencing)|Ranges properly defined|[Jump](#pass-outcome-number-191)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-192">192/211</div>|:white_check_mark:Pass|`module-affordances-ontology`|[labeled-terms](https://ns.inria.fr/olivaw#labeled-terms)|All terms labeled|[Jump](#pass-outcome-number-192)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-193">193/211</div>|:white_check_mark:Pass|`module-affordances-ontology`|[owl-rl-constraint](https://ns.inria.fr/olivaw#owl-rl-constraint)|OWL RL consistent|[Jump](#pass-outcome-number-193)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-194">194/211</div>|:white_check_mark:Pass|`module-affordances-ontology`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL EL Profile compatible|[Jump](#pass-outcome-number-194)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-195">195/211</div>|:white_check_mark:Pass|`module-affordances-ontology`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL QL Profile compatible|[Jump](#pass-outcome-number-195)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-196">196/211</div>|:white_check_mark:Pass|`module-affordances-ontology`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL RL Profile compatible|[Jump](#pass-outcome-number-196)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-197">197/211</div>|:white_check_mark:Pass|`module-affordances-ontology`|[proper-extension-predicate](https://ns.inria.fr/olivaw#proper-extension-predicate)|No class subproperty|[Jump](#pass-outcome-number-197)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-198">198/211</div>|:white_check_mark:Pass|`module-affordances-ontology`|[proper-extension-predicate](https://ns.inria.fr/olivaw#proper-extension-predicate)|No property subclass|[Jump](#pass-outcome-number-198)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-199">199/211</div>|:white_check_mark:Pass|`module-affordances-ontology`|[proper-extension-predicate](https://ns.inria.fr/olivaw#proper-extension-predicate)|No subclass of property|[Jump](#pass-outcome-number-199)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-200">200/211</div>|:white_check_mark:Pass|`module-affordances-ontology`|[proper-extension-predicate](https://ns.inria.fr/olivaw#proper-extension-predicate)|No subproperty of class|[Jump](#pass-outcome-number-200)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-201">201/211</div>|:white_check_mark:Pass|`module-affordances-ontology`|[term-referencing](https://ns.inria.fr/olivaw#term-referencing)|Any term is referenced|[Jump](#pass-outcome-number-201)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-202">202/211</div>|:white_check_mark:Pass|`module-affordances-ontology`|[terms-differenciation](https://ns.inria.fr/olivaw#terms-differenciation)|Terms differenciated enough|[Jump](#pass-outcome-number-202)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-203">203/211</div>|:white_check_mark:Pass|`module-actuations-ontology`|[domain-and-range-referencing](https://ns.inria.fr/olivaw#domain-and-range-referencing)|Domains properly defined|[Jump](#pass-outcome-number-203)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-204">204/211</div>|:white_check_mark:Pass|`module-actuations-ontology`|[domain-and-range-referencing](https://ns.inria.fr/olivaw#domain-and-range-referencing)|Ranges properly defined|[Jump](#pass-outcome-number-204)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-205">205/211</div>|:white_check_mark:Pass|`module-actuations-ontology`|[labeled-terms](https://ns.inria.fr/olivaw#labeled-terms)|All terms labeled|[Jump](#pass-outcome-number-205)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-206">206/211</div>|:white_check_mark:Pass|`module-actuations-ontology`|[owl-rl-constraint](https://ns.inria.fr/olivaw#owl-rl-constraint)|OWL RL consistent|[Jump](#pass-outcome-number-206)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-207">207/211</div>|:white_check_mark:Pass|`module-actuations-ontology`|[proper-extension-predicate](https://ns.inria.fr/olivaw#proper-extension-predicate)|No class subproperty|[Jump](#pass-outcome-number-207)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-208">208/211</div>|:white_check_mark:Pass|`module-actuations-ontology`|[proper-extension-predicate](https://ns.inria.fr/olivaw#proper-extension-predicate)|No property subclass|[Jump](#pass-outcome-number-208)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-209">209/211</div>|:white_check_mark:Pass|`module-actuations-ontology`|[proper-extension-predicate](https://ns.inria.fr/olivaw#proper-extension-predicate)|No subclass of property|[Jump](#pass-outcome-number-209)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-210">210/211</div>|:white_check_mark:Pass|`module-actuations-ontology`|[proper-extension-predicate](https://ns.inria.fr/olivaw#proper-extension-predicate)|No subproperty of class|[Jump](#pass-outcome-number-210)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-211">211/211</div>|:white_check_mark:Pass|`module-actuations-ontology`|[term-referencing](https://ns.inria.fr/olivaw#term-referencing)|Any term is referenced|[Jump](#pass-outcome-number-211)|

***

## Pass Outcomes Details

This subchapter gives more details to the :white_check_mark:Pass outcomes

### Pass Outcome number 1

[Jump to summary definition](#summary-Pass-1)	|	Previous Pass outcome	|	[Next Pass outcome](#pass-outcome-number-2)

:white_check_mark:Pass outcome
#### Subject detail
|Name|module-systems-ontology|
|----|----|
|Title|Standalone&#32;module&#32;core&#92;systems&#92;ontology.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- https://gitlab.com/coswot/coswot-acimov/blob/HEAD/core/systems/ontology.ttl|

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
|Name|module-systems-ontology|
|----|----|
|Title|Standalone&#32;module&#32;core&#92;systems&#92;ontology.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- https://gitlab.com/coswot/coswot-acimov/blob/HEAD/core/systems/ontology.ttl|

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
|Name|module-systems-ontology|
|----|----|
|Title|Standalone&#32;module&#32;core&#92;systems&#92;ontology.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- https://gitlab.com/coswot/coswot-acimov/blob/HEAD/core/systems/ontology.ttl|

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
|Name|module-systems-ontology|
|----|----|
|Title|Standalone&#32;module&#32;core&#92;systems&#92;ontology.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- https://gitlab.com/coswot/coswot-acimov/blob/HEAD/core/systems/ontology.ttl|

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
|Name|module-systems-ontology|
|----|----|
|Title|Standalone&#32;module&#32;core&#92;systems&#92;ontology.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- https://gitlab.com/coswot/coswot-acimov/blob/HEAD/core/systems/ontology.ttl|

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
|Name|module-systems-ontology|
|----|----|
|Title|Standalone&#32;module&#32;core&#92;systems&#92;ontology.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- https://gitlab.com/coswot/coswot-acimov/blob/HEAD/core/systems/ontology.ttl|

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
|Name|module-systems-ontology|
|----|----|
|Title|Standalone&#32;module&#32;core&#92;systems&#92;ontology.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- https://gitlab.com/coswot/coswot-acimov/blob/HEAD/core/systems/ontology.ttl|

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
|Name|module-systems-ontology|
|----|----|
|Title|Standalone&#32;module&#32;core&#92;systems&#92;ontology.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- https://gitlab.com/coswot/coswot-acimov/blob/HEAD/core/systems/ontology.ttl|

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

[Jump to summary definition](#summary-Pass-9)	|	[Previous Pass outcome](#pass-outcome-number-8)	|	[Next Pass outcome](#pass-outcome-number-10)

:white_check_mark:Pass outcome
#### Subject detail
|Name|module-systems-ontology|
|----|----|
|Title|Standalone&#32;module&#32;core&#92;systems&#92;ontology.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- https://gitlab.com/coswot/coswot-acimov/blob/HEAD/core/systems/ontology.ttl|

#### Criterion detail
|Identifier|[term-referencing](https://ns.inria.fr/olivaw#term-referencing)|
|----|----|
|Title|Term&#32;referencing&#32;test|
|Description|A&#32;test&#32;case&#32;from&#32;the&#32;Best&#32;Practices&#32;tests&#32;checking&#32;if&#32;each&#32;term&#32;of&#32;the&#32;test&#32;subject&#32;is&#32;referenced&#32;to&#32;a&#32;module&#32;through&#32;a&#32;rdfs:isDefinedBy&#32;property.|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-9)|Identifier|`no-reference-module`|
|[Section top](#pass-outcome-number-9)|Title|Any&#32;term&#32;is&#32;referenced|
|[Section top](#pass-outcome-number-9)|Description|Each&#32;term&#32;of&#32;the&#32;test&#32;subject&#32;is&#32;linked&#32;to&#32;a&#32;module&#32;by&#32;a&#32;rdfs:isDefinedBy&#32;property|

***
### Pass Outcome number 10

[Jump to summary definition](#summary-Pass-10)	|	[Previous Pass outcome](#pass-outcome-number-9)	|	[Next Pass outcome](#pass-outcome-number-11)

:white_check_mark:Pass outcome
#### Subject detail
|Name|module-systems-ontology|
|----|----|
|Title|Standalone&#32;module&#32;core&#92;systems&#92;ontology.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- https://gitlab.com/coswot/coswot-acimov/blob/HEAD/core/systems/ontology.ttl|

#### Criterion detail
|Identifier|[terms-differenciation](https://ns.inria.fr/olivaw#terms-differenciation)|
|----|----|
|Title|Terms&#32;differenciation&#32;test|
|Description|A&#32;test&#32;case&#32;from&#32;the&#32;Best&#32;Practices&#32;tests&#32;checking&#32;if&#32;all&#32;the&#32;terms&#32;are&#32;different&#32;enough&#32;from&#32;each&#32;other&#32;according&#32;to&#32;the&#32;Levenshtein&#32;distance&#32;metric.|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-10)|Identifier|`too-close-terms`|
|[Section top](#pass-outcome-number-10)|Title|Terms&#32;differenciated&#32;enough|
|[Section top](#pass-outcome-number-10)|Description|All&#32;the&#32;terms&#32;have&#32;have&#32;a&#32;satisfying&#32;Levenshtein&#32;distance&#32;from&#32;each&#32;other&#32;term.|

***
### Pass Outcome number 11

[Jump to summary definition](#summary-Pass-11)	|	[Previous Pass outcome](#pass-outcome-number-10)	|	[Next Pass outcome](#pass-outcome-number-12)

:white_check_mark:Pass outcome
#### Subject detail
|Name|module-states-ontology-catalog|
|----|----|
|Title|Standalone&#32;module&#32;core&#92;states&#92;ontology.catalog.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- https://gitlab.com/coswot/coswot-acimov/blob/HEAD/core/states/ontology.catalog.ttl|

#### Criterion detail
|Identifier|[labeled-terms](https://ns.inria.fr/olivaw#labeled-terms)|
|----|----|
|Title|Term&#32;labeling&#32;test|
|Description|A&#32;test&#32;case&#32;from&#32;the&#32;Best&#32;Practices&#32;tests&#32;checking&#32;if&#32;all&#32;the&#32;terms&#32;of&#32;the&#32;subject&#32;have&#32;a&#32;rdfs:label&#32;property&#32;pointing&#32;to&#32;a&#32;literal&#32;in&#32;English|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-11)|Identifier|`not-labeled-term`|
|[Section top](#pass-outcome-number-11)|Title|All&#32;terms&#32;labeled|
|[Section top](#pass-outcome-number-11)|Description|All&#32;the&#32;terms&#32;defined&#32;in&#32;the&#32;subject&#32;have&#32;a&#32;rdfs:label&#32;in&#32;English|

***
### Pass Outcome number 12

[Jump to summary definition](#summary-Pass-12)	|	[Previous Pass outcome](#pass-outcome-number-11)	|	[Next Pass outcome](#pass-outcome-number-13)

:white_check_mark:Pass outcome
#### Subject detail
|Name|module-states-ontology-catalog|
|----|----|
|Title|Standalone&#32;module&#32;core&#92;states&#92;ontology.catalog.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- https://gitlab.com/coswot/coswot-acimov/blob/HEAD/core/states/ontology.catalog.ttl|

#### Criterion detail
|Identifier|[owl-rl-constraint](https://ns.inria.fr/olivaw#owl-rl-constraint)|
|----|----|
|Title|OWL&#32;RL&#32;Constraint&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;check&#32;wether&#32;the&#32;test&#32;subject&#32;is&#32;syntaxically&#32;correct&#32;or&#32;not.|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-12)|Identifier|`owl-rl-constraint-violation`|
|[Section top](#pass-outcome-number-12)|Title|OWL&#32;RL&#32;consistent|
|[Section top](#pass-outcome-number-12)|Description|The&#32;provided&#32;graph&#32;is&#32;consistent&#32;for&#32;any&#32;OWL&#32;RL&#32;constraint|

***
### Pass Outcome number 13

[Jump to summary definition](#summary-Pass-13)	|	[Previous Pass outcome](#pass-outcome-number-12)	|	[Next Pass outcome](#pass-outcome-number-14)

:white_check_mark:Pass outcome
#### Subject detail
|Name|module-states-ontology-catalog|
|----|----|
|Title|Standalone&#32;module&#32;core&#92;states&#92;ontology.catalog.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- https://gitlab.com/coswot/coswot-acimov/blob/HEAD/core/states/ontology.catalog.ttl|

#### Criterion detail
|Identifier|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|
|----|----|
|Title|Profile&#32;compatibility&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;check&#32;whether&#32;the&#32;test&#32;subject&#32;is&#32;compatible&#32;with&#32;a&#32;profile&#32;or&#32;not,&#32;and&#32;if&#32;it&#32;is&#32;not,&#32;why.|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-13)|Identifier|`owl-rl-profile-error`|
|[Section top](#pass-outcome-number-13)|Title|OWL&#32;RL&#32;Profile&#32;compatible|
|[Section top](#pass-outcome-number-13)|Description|The&#32;subject&#32;is&#32;included&#32;in&#32;the&#32;OWL&#32;RL&#32;sublanguage|

***
### Pass Outcome number 14

[Jump to summary definition](#summary-Pass-14)	|	[Previous Pass outcome](#pass-outcome-number-13)	|	[Next Pass outcome](#pass-outcome-number-15)

:white_check_mark:Pass outcome
#### Subject detail
|Name|module-states-ontology-catalog|
|----|----|
|Title|Standalone&#32;module&#32;core&#92;states&#92;ontology.catalog.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- https://gitlab.com/coswot/coswot-acimov/blob/HEAD/core/states/ontology.catalog.ttl|

#### Criterion detail
|Identifier|[proper-extension-predicate](https://ns.inria.fr/olivaw#proper-extension-predicate)|
|----|----|
|Title|Predicate&#32;extension&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;test&#32;the&#32;proper&#32;use&#32;of&#32;predicates&#32;rdfs:subClassOf&#32;and&#32;rdfs:subPropertyOf&#32;on&#32;the&#32;ontology&#32;terms|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-14)|Identifier|`class-subpropertyof`|
|[Section top](#pass-outcome-number-14)|Title|No&#32;class&#32;subproperty|
|[Section top](#pass-outcome-number-14)|Description|No&#32;ontology&#32;class&#32;is&#32;a&#32;subproperty|

***
### Pass Outcome number 15

[Jump to summary definition](#summary-Pass-15)	|	[Previous Pass outcome](#pass-outcome-number-14)	|	[Next Pass outcome](#pass-outcome-number-16)

:white_check_mark:Pass outcome
#### Subject detail
|Name|module-states-ontology-catalog|
|----|----|
|Title|Standalone&#32;module&#32;core&#92;states&#92;ontology.catalog.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- https://gitlab.com/coswot/coswot-acimov/blob/HEAD/core/states/ontology.catalog.ttl|

#### Criterion detail
|Identifier|[proper-extension-predicate](https://ns.inria.fr/olivaw#proper-extension-predicate)|
|----|----|
|Title|Predicate&#32;extension&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;test&#32;the&#32;proper&#32;use&#32;of&#32;predicates&#32;rdfs:subClassOf&#32;and&#32;rdfs:subPropertyOf&#32;on&#32;the&#32;ontology&#32;terms|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-15)|Identifier|`property-subclassof`|
|[Section top](#pass-outcome-number-15)|Title|No&#32;property&#32;subclass|
|[Section top](#pass-outcome-number-15)|Description|No&#32;ontology&#32;property&#32;is&#32;a&#32;subclass|

***
### Pass Outcome number 16

[Jump to summary definition](#summary-Pass-16)	|	[Previous Pass outcome](#pass-outcome-number-15)	|	[Next Pass outcome](#pass-outcome-number-17)

:white_check_mark:Pass outcome
#### Subject detail
|Name|module-states-ontology-catalog|
|----|----|
|Title|Standalone&#32;module&#32;core&#92;states&#92;ontology.catalog.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- https://gitlab.com/coswot/coswot-acimov/blob/HEAD/core/states/ontology.catalog.ttl|

#### Criterion detail
|Identifier|[proper-extension-predicate](https://ns.inria.fr/olivaw#proper-extension-predicate)|
|----|----|
|Title|Predicate&#32;extension&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;test&#32;the&#32;proper&#32;use&#32;of&#32;predicates&#32;rdfs:subClassOf&#32;and&#32;rdfs:subPropertyOf&#32;on&#32;the&#32;ontology&#32;terms|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-16)|Identifier|`subclassof-property`|
|[Section top](#pass-outcome-number-16)|Title|No&#32;subclass&#32;of&#32;property|
|[Section top](#pass-outcome-number-16)|Description|No&#32;ontology&#32;term&#32;is&#32;a&#32;subclass&#32;of&#32;a&#32;property|

***
### Pass Outcome number 17

[Jump to summary definition](#summary-Pass-17)	|	[Previous Pass outcome](#pass-outcome-number-16)	|	[Next Pass outcome](#pass-outcome-number-18)

:white_check_mark:Pass outcome
#### Subject detail
|Name|module-states-ontology-catalog|
|----|----|
|Title|Standalone&#32;module&#32;core&#92;states&#92;ontology.catalog.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- https://gitlab.com/coswot/coswot-acimov/blob/HEAD/core/states/ontology.catalog.ttl|

#### Criterion detail
|Identifier|[proper-extension-predicate](https://ns.inria.fr/olivaw#proper-extension-predicate)|
|----|----|
|Title|Predicate&#32;extension&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;test&#32;the&#32;proper&#32;use&#32;of&#32;predicates&#32;rdfs:subClassOf&#32;and&#32;rdfs:subPropertyOf&#32;on&#32;the&#32;ontology&#32;terms|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-17)|Identifier|`subpropertyof-class`|
|[Section top](#pass-outcome-number-17)|Title|No&#32;subproperty&#32;of&#32;class|
|[Section top](#pass-outcome-number-17)|Description|No&#32;ontology&#32;term&#32;is&#32;a&#32;subproperty&#32;of&#32;a&#32;class|

***
### Pass Outcome number 18

[Jump to summary definition](#summary-Pass-18)	|	[Previous Pass outcome](#pass-outcome-number-17)	|	[Next Pass outcome](#pass-outcome-number-19)

:white_check_mark:Pass outcome
#### Subject detail
|Name|module-states-ontology-catalog|
|----|----|
|Title|Standalone&#32;module&#32;core&#92;states&#92;ontology.catalog.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- https://gitlab.com/coswot/coswot-acimov/blob/HEAD/core/states/ontology.catalog.ttl|

#### Criterion detail
|Identifier|[term-referencing](https://ns.inria.fr/olivaw#term-referencing)|
|----|----|
|Title|Term&#32;referencing&#32;test|
|Description|A&#32;test&#32;case&#32;from&#32;the&#32;Best&#32;Practices&#32;tests&#32;checking&#32;if&#32;each&#32;term&#32;of&#32;the&#32;test&#32;subject&#32;is&#32;referenced&#32;to&#32;a&#32;module&#32;through&#32;a&#32;rdfs:isDefinedBy&#32;property.|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-18)|Identifier|`no-reference-module`|
|[Section top](#pass-outcome-number-18)|Title|Any&#32;term&#32;is&#32;referenced|
|[Section top](#pass-outcome-number-18)|Description|Each&#32;term&#32;of&#32;the&#32;test&#32;subject&#32;is&#32;linked&#32;to&#32;a&#32;module&#32;by&#32;a&#32;rdfs:isDefinedBy&#32;property|

***
### Pass Outcome number 19

[Jump to summary definition](#summary-Pass-19)	|	[Previous Pass outcome](#pass-outcome-number-18)	|	[Next Pass outcome](#pass-outcome-number-20)

:white_check_mark:Pass outcome
#### Subject detail
|Name|module-states-ontology-catalog|
|----|----|
|Title|Standalone&#32;module&#32;core&#92;states&#92;ontology.catalog.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- https://gitlab.com/coswot/coswot-acimov/blob/HEAD/core/states/ontology.catalog.ttl|

#### Criterion detail
|Identifier|[terms-differenciation](https://ns.inria.fr/olivaw#terms-differenciation)|
|----|----|
|Title|Terms&#32;differenciation&#32;test|
|Description|A&#32;test&#32;case&#32;from&#32;the&#32;Best&#32;Practices&#32;tests&#32;checking&#32;if&#32;all&#32;the&#32;terms&#32;are&#32;different&#32;enough&#32;from&#32;each&#32;other&#32;according&#32;to&#32;the&#32;Levenshtein&#32;distance&#32;metric.|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-19)|Identifier|`too-close-terms`|
|[Section top](#pass-outcome-number-19)|Title|Terms&#32;differenciated&#32;enough|
|[Section top](#pass-outcome-number-19)|Description|All&#32;the&#32;terms&#32;have&#32;have&#32;a&#32;satisfying&#32;Levenshtein&#32;distance&#32;from&#32;each&#32;other&#32;term.|

***
### Pass Outcome number 20

[Jump to summary definition](#summary-Pass-20)	|	[Previous Pass outcome](#pass-outcome-number-19)	|	[Next Pass outcome](#pass-outcome-number-21)

:white_check_mark:Pass outcome
#### Subject detail
|Name|module-states-ontology|
|----|----|
|Title|Standalone&#32;module&#32;core&#92;states&#92;ontology.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- https://gitlab.com/coswot/coswot-acimov/blob/HEAD/core/states/ontology.ttl|

#### Criterion detail
|Identifier|[labeled-terms](https://ns.inria.fr/olivaw#labeled-terms)|
|----|----|
|Title|Term&#32;labeling&#32;test|
|Description|A&#32;test&#32;case&#32;from&#32;the&#32;Best&#32;Practices&#32;tests&#32;checking&#32;if&#32;all&#32;the&#32;terms&#32;of&#32;the&#32;subject&#32;have&#32;a&#32;rdfs:label&#32;property&#32;pointing&#32;to&#32;a&#32;literal&#32;in&#32;English|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-20)|Identifier|`not-labeled-term`|
|[Section top](#pass-outcome-number-20)|Title|All&#32;terms&#32;labeled|
|[Section top](#pass-outcome-number-20)|Description|All&#32;the&#32;terms&#32;defined&#32;in&#32;the&#32;subject&#32;have&#32;a&#32;rdfs:label&#32;in&#32;English|

***
### Pass Outcome number 21

[Jump to summary definition](#summary-Pass-21)	|	[Previous Pass outcome](#pass-outcome-number-20)	|	[Next Pass outcome](#pass-outcome-number-22)

:white_check_mark:Pass outcome
#### Subject detail
|Name|module-states-ontology|
|----|----|
|Title|Standalone&#32;module&#32;core&#92;states&#92;ontology.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- https://gitlab.com/coswot/coswot-acimov/blob/HEAD/core/states/ontology.ttl|

#### Criterion detail
|Identifier|[owl-rl-constraint](https://ns.inria.fr/olivaw#owl-rl-constraint)|
|----|----|
|Title|OWL&#32;RL&#32;Constraint&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;check&#32;wether&#32;the&#32;test&#32;subject&#32;is&#32;syntaxically&#32;correct&#32;or&#32;not.|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-21)|Identifier|`owl-rl-constraint-violation`|
|[Section top](#pass-outcome-number-21)|Title|OWL&#32;RL&#32;consistent|
|[Section top](#pass-outcome-number-21)|Description|The&#32;provided&#32;graph&#32;is&#32;consistent&#32;for&#32;any&#32;OWL&#32;RL&#32;constraint|

***
### Pass Outcome number 22

[Jump to summary definition](#summary-Pass-22)	|	[Previous Pass outcome](#pass-outcome-number-21)	|	[Next Pass outcome](#pass-outcome-number-23)

:white_check_mark:Pass outcome
#### Subject detail
|Name|module-states-ontology|
|----|----|
|Title|Standalone&#32;module&#32;core&#92;states&#92;ontology.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- https://gitlab.com/coswot/coswot-acimov/blob/HEAD/core/states/ontology.ttl|

#### Criterion detail
|Identifier|[proper-extension-predicate](https://ns.inria.fr/olivaw#proper-extension-predicate)|
|----|----|
|Title|Predicate&#32;extension&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;test&#32;the&#32;proper&#32;use&#32;of&#32;predicates&#32;rdfs:subClassOf&#32;and&#32;rdfs:subPropertyOf&#32;on&#32;the&#32;ontology&#32;terms|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-22)|Identifier|`class-subpropertyof`|
|[Section top](#pass-outcome-number-22)|Title|No&#32;class&#32;subproperty|
|[Section top](#pass-outcome-number-22)|Description|No&#32;ontology&#32;class&#32;is&#32;a&#32;subproperty|

***
### Pass Outcome number 23

[Jump to summary definition](#summary-Pass-23)	|	[Previous Pass outcome](#pass-outcome-number-22)	|	[Next Pass outcome](#pass-outcome-number-24)

:white_check_mark:Pass outcome
#### Subject detail
|Name|module-states-ontology|
|----|----|
|Title|Standalone&#32;module&#32;core&#92;states&#92;ontology.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- https://gitlab.com/coswot/coswot-acimov/blob/HEAD/core/states/ontology.ttl|

#### Criterion detail
|Identifier|[proper-extension-predicate](https://ns.inria.fr/olivaw#proper-extension-predicate)|
|----|----|
|Title|Predicate&#32;extension&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;test&#32;the&#32;proper&#32;use&#32;of&#32;predicates&#32;rdfs:subClassOf&#32;and&#32;rdfs:subPropertyOf&#32;on&#32;the&#32;ontology&#32;terms|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-23)|Identifier|`property-subclassof`|
|[Section top](#pass-outcome-number-23)|Title|No&#32;property&#32;subclass|
|[Section top](#pass-outcome-number-23)|Description|No&#32;ontology&#32;property&#32;is&#32;a&#32;subclass|

***
### Pass Outcome number 24

[Jump to summary definition](#summary-Pass-24)	|	[Previous Pass outcome](#pass-outcome-number-23)	|	[Next Pass outcome](#pass-outcome-number-25)

:white_check_mark:Pass outcome
#### Subject detail
|Name|module-states-ontology|
|----|----|
|Title|Standalone&#32;module&#32;core&#92;states&#92;ontology.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- https://gitlab.com/coswot/coswot-acimov/blob/HEAD/core/states/ontology.ttl|

#### Criterion detail
|Identifier|[proper-extension-predicate](https://ns.inria.fr/olivaw#proper-extension-predicate)|
|----|----|
|Title|Predicate&#32;extension&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;test&#32;the&#32;proper&#32;use&#32;of&#32;predicates&#32;rdfs:subClassOf&#32;and&#32;rdfs:subPropertyOf&#32;on&#32;the&#32;ontology&#32;terms|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-24)|Identifier|`subclassof-property`|
|[Section top](#pass-outcome-number-24)|Title|No&#32;subclass&#32;of&#32;property|
|[Section top](#pass-outcome-number-24)|Description|No&#32;ontology&#32;term&#32;is&#32;a&#32;subclass&#32;of&#32;a&#32;property|

***
### Pass Outcome number 25

[Jump to summary definition](#summary-Pass-25)	|	[Previous Pass outcome](#pass-outcome-number-24)	|	[Next Pass outcome](#pass-outcome-number-26)

:white_check_mark:Pass outcome
#### Subject detail
|Name|module-states-ontology|
|----|----|
|Title|Standalone&#32;module&#32;core&#92;states&#92;ontology.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- https://gitlab.com/coswot/coswot-acimov/blob/HEAD/core/states/ontology.ttl|

#### Criterion detail
|Identifier|[proper-extension-predicate](https://ns.inria.fr/olivaw#proper-extension-predicate)|
|----|----|
|Title|Predicate&#32;extension&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;test&#32;the&#32;proper&#32;use&#32;of&#32;predicates&#32;rdfs:subClassOf&#32;and&#32;rdfs:subPropertyOf&#32;on&#32;the&#32;ontology&#32;terms|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-25)|Identifier|`subpropertyof-class`|
|[Section top](#pass-outcome-number-25)|Title|No&#32;subproperty&#32;of&#32;class|
|[Section top](#pass-outcome-number-25)|Description|No&#32;ontology&#32;term&#32;is&#32;a&#32;subproperty&#32;of&#32;a&#32;class|

***
### Pass Outcome number 26

[Jump to summary definition](#summary-Pass-26)	|	[Previous Pass outcome](#pass-outcome-number-25)	|	[Next Pass outcome](#pass-outcome-number-27)

:white_check_mark:Pass outcome
#### Subject detail
|Name|module-states-ontology|
|----|----|
|Title|Standalone&#32;module&#32;core&#92;states&#92;ontology.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- https://gitlab.com/coswot/coswot-acimov/blob/HEAD/core/states/ontology.ttl|

#### Criterion detail
|Identifier|[term-referencing](https://ns.inria.fr/olivaw#term-referencing)|
|----|----|
|Title|Term&#32;referencing&#32;test|
|Description|A&#32;test&#32;case&#32;from&#32;the&#32;Best&#32;Practices&#32;tests&#32;checking&#32;if&#32;each&#32;term&#32;of&#32;the&#32;test&#32;subject&#32;is&#32;referenced&#32;to&#32;a&#32;module&#32;through&#32;a&#32;rdfs:isDefinedBy&#32;property.|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-26)|Identifier|`no-reference-module`|
|[Section top](#pass-outcome-number-26)|Title|Any&#32;term&#32;is&#32;referenced|
|[Section top](#pass-outcome-number-26)|Description|Each&#32;term&#32;of&#32;the&#32;test&#32;subject&#32;is&#32;linked&#32;to&#32;a&#32;module&#32;by&#32;a&#32;rdfs:isDefinedBy&#32;property|

***
### Pass Outcome number 27

[Jump to summary definition](#summary-Pass-27)	|	[Previous Pass outcome](#pass-outcome-number-26)	|	[Next Pass outcome](#pass-outcome-number-28)

:white_check_mark:Pass outcome
#### Subject detail
|Name|module-states-ontology|
|----|----|
|Title|Standalone&#32;module&#32;core&#92;states&#92;ontology.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- https://gitlab.com/coswot/coswot-acimov/blob/HEAD/core/states/ontology.ttl|

#### Criterion detail
|Identifier|[terms-differenciation](https://ns.inria.fr/olivaw#terms-differenciation)|
|----|----|
|Title|Terms&#32;differenciation&#32;test|
|Description|A&#32;test&#32;case&#32;from&#32;the&#32;Best&#32;Practices&#32;tests&#32;checking&#32;if&#32;all&#32;the&#32;terms&#32;are&#32;different&#32;enough&#32;from&#32;each&#32;other&#32;according&#32;to&#32;the&#32;Levenshtein&#32;distance&#32;metric.|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-27)|Identifier|`too-close-terms`|
|[Section top](#pass-outcome-number-27)|Title|Terms&#32;differenciated&#32;enough|
|[Section top](#pass-outcome-number-27)|Description|All&#32;the&#32;terms&#32;have&#32;have&#32;a&#32;satisfying&#32;Levenshtein&#32;distance&#32;from&#32;each&#32;other&#32;term.|

***
### Pass Outcome number 28

[Jump to summary definition](#summary-Pass-28)	|	[Previous Pass outcome](#pass-outcome-number-27)	|	[Next Pass outcome](#pass-outcome-number-29)

:white_check_mark:Pass outcome
#### Subject detail
|Name|module-services-operations-ontology|
|----|----|
|Title|Standalone&#32;module&#32;core&#92;services&lowbar;operations&#92;ontology.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- https://gitlab.com/coswot/coswot-acimov/blob/HEAD/core/services_operations/ontology.ttl|

#### Criterion detail
|Identifier|[domain-and-range-referencing](https://ns.inria.fr/olivaw#domain-and-range-referencing)|
|----|----|
|Title|Domain&#32;and&#32;range&#32;referencing&#32;test|
|Description|A&#32;test&#32;case&#32;from&#32;the&#32;Best&#32;Practices&#32;tests&#32;checking&#32;if&#32;all&#32;the&#32;ranges&#32;and&#32;domains&#32;from&#32;the&#32;test&#32;subject&#32;point&#32;to&#32;terms&#32;that&#32;are&#32;defined&#32;in&#32;the&#32;vocabulary.|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-28)|Identifier|`domain-out-of-vocabulary`|
|[Section top](#pass-outcome-number-28)|Title|Domains&#32;properly&#32;defined|
|[Section top](#pass-outcome-number-28)|Description|Each&#32;rdfs:domain&#32;is&#32;defined&#32;within&#32;the&#32;fragment|

***
### Pass Outcome number 29

[Jump to summary definition](#summary-Pass-29)	|	[Previous Pass outcome](#pass-outcome-number-28)	|	[Next Pass outcome](#pass-outcome-number-30)

:white_check_mark:Pass outcome
#### Subject detail
|Name|module-services-operations-ontology|
|----|----|
|Title|Standalone&#32;module&#32;core&#92;services&lowbar;operations&#92;ontology.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- https://gitlab.com/coswot/coswot-acimov/blob/HEAD/core/services_operations/ontology.ttl|

#### Criterion detail
|Identifier|[domain-and-range-referencing](https://ns.inria.fr/olivaw#domain-and-range-referencing)|
|----|----|
|Title|Domain&#32;and&#32;range&#32;referencing&#32;test|
|Description|A&#32;test&#32;case&#32;from&#32;the&#32;Best&#32;Practices&#32;tests&#32;checking&#32;if&#32;all&#32;the&#32;ranges&#32;and&#32;domains&#32;from&#32;the&#32;test&#32;subject&#32;point&#32;to&#32;terms&#32;that&#32;are&#32;defined&#32;in&#32;the&#32;vocabulary.|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-29)|Identifier|`range-out-of-vocabulary`|
|[Section top](#pass-outcome-number-29)|Title|Ranges&#32;properly&#32;defined|
|[Section top](#pass-outcome-number-29)|Description|Each&#32;rdfs:range&#32;is&#32;defined&#32;within&#32;the&#32;fragment|

***
### Pass Outcome number 30

[Jump to summary definition](#summary-Pass-30)	|	[Previous Pass outcome](#pass-outcome-number-29)	|	[Next Pass outcome](#pass-outcome-number-31)

:white_check_mark:Pass outcome
#### Subject detail
|Name|module-services-operations-ontology|
|----|----|
|Title|Standalone&#32;module&#32;core&#92;services&lowbar;operations&#92;ontology.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- https://gitlab.com/coswot/coswot-acimov/blob/HEAD/core/services_operations/ontology.ttl|

#### Criterion detail
|Identifier|[labeled-terms](https://ns.inria.fr/olivaw#labeled-terms)|
|----|----|
|Title|Term&#32;labeling&#32;test|
|Description|A&#32;test&#32;case&#32;from&#32;the&#32;Best&#32;Practices&#32;tests&#32;checking&#32;if&#32;all&#32;the&#32;terms&#32;of&#32;the&#32;subject&#32;have&#32;a&#32;rdfs:label&#32;property&#32;pointing&#32;to&#32;a&#32;literal&#32;in&#32;English|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-30)|Identifier|`not-labeled-term`|
|[Section top](#pass-outcome-number-30)|Title|All&#32;terms&#32;labeled|
|[Section top](#pass-outcome-number-30)|Description|All&#32;the&#32;terms&#32;defined&#32;in&#32;the&#32;subject&#32;have&#32;a&#32;rdfs:label&#32;in&#32;English|

***
### Pass Outcome number 31

[Jump to summary definition](#summary-Pass-31)	|	[Previous Pass outcome](#pass-outcome-number-30)	|	[Next Pass outcome](#pass-outcome-number-32)

:white_check_mark:Pass outcome
#### Subject detail
|Name|module-services-operations-ontology|
|----|----|
|Title|Standalone&#32;module&#32;core&#92;services&lowbar;operations&#92;ontology.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- https://gitlab.com/coswot/coswot-acimov/blob/HEAD/core/services_operations/ontology.ttl|

#### Criterion detail
|Identifier|[owl-rl-constraint](https://ns.inria.fr/olivaw#owl-rl-constraint)|
|----|----|
|Title|OWL&#32;RL&#32;Constraint&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;check&#32;wether&#32;the&#32;test&#32;subject&#32;is&#32;syntaxically&#32;correct&#32;or&#32;not.|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-31)|Identifier|`owl-rl-constraint-violation`|
|[Section top](#pass-outcome-number-31)|Title|OWL&#32;RL&#32;consistent|
|[Section top](#pass-outcome-number-31)|Description|The&#32;provided&#32;graph&#32;is&#32;consistent&#32;for&#32;any&#32;OWL&#32;RL&#32;constraint|

***
### Pass Outcome number 32

[Jump to summary definition](#summary-Pass-32)	|	[Previous Pass outcome](#pass-outcome-number-31)	|	[Next Pass outcome](#pass-outcome-number-33)

:white_check_mark:Pass outcome
#### Subject detail
|Name|module-services-operations-ontology|
|----|----|
|Title|Standalone&#32;module&#32;core&#92;services&lowbar;operations&#92;ontology.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- https://gitlab.com/coswot/coswot-acimov/blob/HEAD/core/services_operations/ontology.ttl|

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
|Name|module-services-operations-ontology|
|----|----|
|Title|Standalone&#32;module&#32;core&#92;services&lowbar;operations&#92;ontology.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- https://gitlab.com/coswot/coswot-acimov/blob/HEAD/core/services_operations/ontology.ttl|

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
|Name|module-services-operations-ontology|
|----|----|
|Title|Standalone&#32;module&#32;core&#92;services&lowbar;operations&#92;ontology.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- https://gitlab.com/coswot/coswot-acimov/blob/HEAD/core/services_operations/ontology.ttl|

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
|Name|module-services-operations-ontology|
|----|----|
|Title|Standalone&#32;module&#32;core&#92;services&lowbar;operations&#92;ontology.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- https://gitlab.com/coswot/coswot-acimov/blob/HEAD/core/services_operations/ontology.ttl|

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
|Name|module-services-operations-ontology|
|----|----|
|Title|Standalone&#32;module&#32;core&#92;services&lowbar;operations&#92;ontology.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- https://gitlab.com/coswot/coswot-acimov/blob/HEAD/core/services_operations/ontology.ttl|

#### Criterion detail
|Identifier|[terms-differenciation](https://ns.inria.fr/olivaw#terms-differenciation)|
|----|----|
|Title|Terms&#32;differenciation&#32;test|
|Description|A&#32;test&#32;case&#32;from&#32;the&#32;Best&#32;Practices&#32;tests&#32;checking&#32;if&#32;all&#32;the&#32;terms&#32;are&#32;different&#32;enough&#32;from&#32;each&#32;other&#32;according&#32;to&#32;the&#32;Levenshtein&#32;distance&#32;metric.|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-36)|Identifier|`too-close-terms`|
|[Section top](#pass-outcome-number-36)|Title|Terms&#32;differenciated&#32;enough|
|[Section top](#pass-outcome-number-36)|Description|All&#32;the&#32;terms&#32;have&#32;have&#32;a&#32;satisfying&#32;Levenshtein&#32;distance&#32;from&#32;each&#32;other&#32;term.|

***
### Pass Outcome number 37

[Jump to summary definition](#summary-Pass-37)	|	[Previous Pass outcome](#pass-outcome-number-36)	|	[Next Pass outcome](#pass-outcome-number-38)

:white_check_mark:Pass outcome
#### Subject detail
|Name|module-samples-ontology|
|----|----|
|Title|Standalone&#32;module&#32;core&#92;samples&#92;ontology.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- https://gitlab.com/coswot/coswot-acimov/blob/HEAD/core/samples/ontology.ttl|

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
|Name|module-samples-ontology|
|----|----|
|Title|Standalone&#32;module&#32;core&#92;samples&#92;ontology.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- https://gitlab.com/coswot/coswot-acimov/blob/HEAD/core/samples/ontology.ttl|

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
|Name|module-samples-ontology|
|----|----|
|Title|Standalone&#32;module&#32;core&#92;samples&#92;ontology.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- https://gitlab.com/coswot/coswot-acimov/blob/HEAD/core/samples/ontology.ttl|

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
|Name|module-samples-ontology|
|----|----|
|Title|Standalone&#32;module&#32;core&#92;samples&#92;ontology.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- https://gitlab.com/coswot/coswot-acimov/blob/HEAD/core/samples/ontology.ttl|

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
|Name|module-samples-ontology|
|----|----|
|Title|Standalone&#32;module&#32;core&#92;samples&#92;ontology.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- https://gitlab.com/coswot/coswot-acimov/blob/HEAD/core/samples/ontology.ttl|

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
|Name|module-samples-ontology|
|----|----|
|Title|Standalone&#32;module&#32;core&#92;samples&#92;ontology.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- https://gitlab.com/coswot/coswot-acimov/blob/HEAD/core/samples/ontology.ttl|

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
|Name|module-samples-ontology|
|----|----|
|Title|Standalone&#32;module&#32;core&#92;samples&#92;ontology.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- https://gitlab.com/coswot/coswot-acimov/blob/HEAD/core/samples/ontology.ttl|

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
|Name|module-samples-ontology|
|----|----|
|Title|Standalone&#32;module&#32;core&#92;samples&#92;ontology.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- https://gitlab.com/coswot/coswot-acimov/blob/HEAD/core/samples/ontology.ttl|

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
|Name|module-samples-ontology|
|----|----|
|Title|Standalone&#32;module&#32;core&#92;samples&#92;ontology.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- https://gitlab.com/coswot/coswot-acimov/blob/HEAD/core/samples/ontology.ttl|

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
|Name|module-samples-ontology|
|----|----|
|Title|Standalone&#32;module&#32;core&#92;samples&#92;ontology.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- https://gitlab.com/coswot/coswot-acimov/blob/HEAD/core/samples/ontology.ttl|

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
|Name|module-samples-ontology|
|----|----|
|Title|Standalone&#32;module&#32;core&#92;samples&#92;ontology.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- https://gitlab.com/coswot/coswot-acimov/blob/HEAD/core/samples/ontology.ttl|

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
|Name|module-property-values-ontology|
|----|----|
|Title|Standalone&#32;module&#32;core&#92;property&lowbar;values&#92;ontology.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- https://gitlab.com/coswot/coswot-acimov/blob/HEAD/core/property_values/ontology.ttl|

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
|Name|module-property-values-ontology|
|----|----|
|Title|Standalone&#32;module&#32;core&#92;property&lowbar;values&#92;ontology.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- https://gitlab.com/coswot/coswot-acimov/blob/HEAD/core/property_values/ontology.ttl|

#### Criterion detail
|Identifier|[labeled-terms](https://ns.inria.fr/olivaw#labeled-terms)|
|----|----|
|Title|Term&#32;labeling&#32;test|
|Description|A&#32;test&#32;case&#32;from&#32;the&#32;Best&#32;Practices&#32;tests&#32;checking&#32;if&#32;all&#32;the&#32;terms&#32;of&#32;the&#32;subject&#32;have&#32;a&#32;rdfs:label&#32;property&#32;pointing&#32;to&#32;a&#32;literal&#32;in&#32;English|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-49)|Identifier|`not-labeled-term`|
|[Section top](#pass-outcome-number-49)|Title|All&#32;terms&#32;labeled|
|[Section top](#pass-outcome-number-49)|Description|All&#32;the&#32;terms&#32;defined&#32;in&#32;the&#32;subject&#32;have&#32;a&#32;rdfs:label&#32;in&#32;English|

***
### Pass Outcome number 50

[Jump to summary definition](#summary-Pass-50)	|	[Previous Pass outcome](#pass-outcome-number-49)	|	[Next Pass outcome](#pass-outcome-number-51)

:white_check_mark:Pass outcome
#### Subject detail
|Name|module-property-values-ontology|
|----|----|
|Title|Standalone&#32;module&#32;core&#92;property&lowbar;values&#92;ontology.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- https://gitlab.com/coswot/coswot-acimov/blob/HEAD/core/property_values/ontology.ttl|

#### Criterion detail
|Identifier|[owl-rl-constraint](https://ns.inria.fr/olivaw#owl-rl-constraint)|
|----|----|
|Title|OWL&#32;RL&#32;Constraint&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;check&#32;wether&#32;the&#32;test&#32;subject&#32;is&#32;syntaxically&#32;correct&#32;or&#32;not.|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-50)|Identifier|`owl-rl-constraint-violation`|
|[Section top](#pass-outcome-number-50)|Title|OWL&#32;RL&#32;consistent|
|[Section top](#pass-outcome-number-50)|Description|The&#32;provided&#32;graph&#32;is&#32;consistent&#32;for&#32;any&#32;OWL&#32;RL&#32;constraint|

***
### Pass Outcome number 51

[Jump to summary definition](#summary-Pass-51)	|	[Previous Pass outcome](#pass-outcome-number-50)	|	[Next Pass outcome](#pass-outcome-number-52)

:white_check_mark:Pass outcome
#### Subject detail
|Name|module-property-values-ontology|
|----|----|
|Title|Standalone&#32;module&#32;core&#92;property&lowbar;values&#92;ontology.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- https://gitlab.com/coswot/coswot-acimov/blob/HEAD/core/property_values/ontology.ttl|

#### Criterion detail
|Identifier|[proper-extension-predicate](https://ns.inria.fr/olivaw#proper-extension-predicate)|
|----|----|
|Title|Predicate&#32;extension&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;test&#32;the&#32;proper&#32;use&#32;of&#32;predicates&#32;rdfs:subClassOf&#32;and&#32;rdfs:subPropertyOf&#32;on&#32;the&#32;ontology&#32;terms|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-51)|Identifier|`class-subpropertyof`|
|[Section top](#pass-outcome-number-51)|Title|No&#32;class&#32;subproperty|
|[Section top](#pass-outcome-number-51)|Description|No&#32;ontology&#32;class&#32;is&#32;a&#32;subproperty|

***
### Pass Outcome number 52

[Jump to summary definition](#summary-Pass-52)	|	[Previous Pass outcome](#pass-outcome-number-51)	|	[Next Pass outcome](#pass-outcome-number-53)

:white_check_mark:Pass outcome
#### Subject detail
|Name|module-property-values-ontology|
|----|----|
|Title|Standalone&#32;module&#32;core&#92;property&lowbar;values&#92;ontology.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- https://gitlab.com/coswot/coswot-acimov/blob/HEAD/core/property_values/ontology.ttl|

#### Criterion detail
|Identifier|[proper-extension-predicate](https://ns.inria.fr/olivaw#proper-extension-predicate)|
|----|----|
|Title|Predicate&#32;extension&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;test&#32;the&#32;proper&#32;use&#32;of&#32;predicates&#32;rdfs:subClassOf&#32;and&#32;rdfs:subPropertyOf&#32;on&#32;the&#32;ontology&#32;terms|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-52)|Identifier|`property-subclassof`|
|[Section top](#pass-outcome-number-52)|Title|No&#32;property&#32;subclass|
|[Section top](#pass-outcome-number-52)|Description|No&#32;ontology&#32;property&#32;is&#32;a&#32;subclass|

***
### Pass Outcome number 53

[Jump to summary definition](#summary-Pass-53)	|	[Previous Pass outcome](#pass-outcome-number-52)	|	[Next Pass outcome](#pass-outcome-number-54)

:white_check_mark:Pass outcome
#### Subject detail
|Name|module-property-values-ontology|
|----|----|
|Title|Standalone&#32;module&#32;core&#92;property&lowbar;values&#92;ontology.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- https://gitlab.com/coswot/coswot-acimov/blob/HEAD/core/property_values/ontology.ttl|

#### Criterion detail
|Identifier|[proper-extension-predicate](https://ns.inria.fr/olivaw#proper-extension-predicate)|
|----|----|
|Title|Predicate&#32;extension&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;test&#32;the&#32;proper&#32;use&#32;of&#32;predicates&#32;rdfs:subClassOf&#32;and&#32;rdfs:subPropertyOf&#32;on&#32;the&#32;ontology&#32;terms|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-53)|Identifier|`subclassof-property`|
|[Section top](#pass-outcome-number-53)|Title|No&#32;subclass&#32;of&#32;property|
|[Section top](#pass-outcome-number-53)|Description|No&#32;ontology&#32;term&#32;is&#32;a&#32;subclass&#32;of&#32;a&#32;property|

***
### Pass Outcome number 54

[Jump to summary definition](#summary-Pass-54)	|	[Previous Pass outcome](#pass-outcome-number-53)	|	[Next Pass outcome](#pass-outcome-number-55)

:white_check_mark:Pass outcome
#### Subject detail
|Name|module-property-values-ontology|
|----|----|
|Title|Standalone&#32;module&#32;core&#92;property&lowbar;values&#92;ontology.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- https://gitlab.com/coswot/coswot-acimov/blob/HEAD/core/property_values/ontology.ttl|

#### Criterion detail
|Identifier|[proper-extension-predicate](https://ns.inria.fr/olivaw#proper-extension-predicate)|
|----|----|
|Title|Predicate&#32;extension&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;test&#32;the&#32;proper&#32;use&#32;of&#32;predicates&#32;rdfs:subClassOf&#32;and&#32;rdfs:subPropertyOf&#32;on&#32;the&#32;ontology&#32;terms|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-54)|Identifier|`subpropertyof-class`|
|[Section top](#pass-outcome-number-54)|Title|No&#32;subproperty&#32;of&#32;class|
|[Section top](#pass-outcome-number-54)|Description|No&#32;ontology&#32;term&#32;is&#32;a&#32;subproperty&#32;of&#32;a&#32;class|

***
### Pass Outcome number 55

[Jump to summary definition](#summary-Pass-55)	|	[Previous Pass outcome](#pass-outcome-number-54)	|	[Next Pass outcome](#pass-outcome-number-56)

:white_check_mark:Pass outcome
#### Subject detail
|Name|module-property-values-ontology|
|----|----|
|Title|Standalone&#32;module&#32;core&#92;property&lowbar;values&#92;ontology.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- https://gitlab.com/coswot/coswot-acimov/blob/HEAD/core/property_values/ontology.ttl|

#### Criterion detail
|Identifier|[term-referencing](https://ns.inria.fr/olivaw#term-referencing)|
|----|----|
|Title|Term&#32;referencing&#32;test|
|Description|A&#32;test&#32;case&#32;from&#32;the&#32;Best&#32;Practices&#32;tests&#32;checking&#32;if&#32;each&#32;term&#32;of&#32;the&#32;test&#32;subject&#32;is&#32;referenced&#32;to&#32;a&#32;module&#32;through&#32;a&#32;rdfs:isDefinedBy&#32;property.|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-55)|Identifier|`no-reference-module`|
|[Section top](#pass-outcome-number-55)|Title|Any&#32;term&#32;is&#32;referenced|
|[Section top](#pass-outcome-number-55)|Description|Each&#32;term&#32;of&#32;the&#32;test&#32;subject&#32;is&#32;linked&#32;to&#32;a&#32;module&#32;by&#32;a&#32;rdfs:isDefinedBy&#32;property|

***
### Pass Outcome number 56

[Jump to summary definition](#summary-Pass-56)	|	[Previous Pass outcome](#pass-outcome-number-55)	|	[Next Pass outcome](#pass-outcome-number-57)

:white_check_mark:Pass outcome
#### Subject detail
|Name|module-property-values-ontology|
|----|----|
|Title|Standalone&#32;module&#32;core&#92;property&lowbar;values&#92;ontology.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- https://gitlab.com/coswot/coswot-acimov/blob/HEAD/core/property_values/ontology.ttl|

#### Criterion detail
|Identifier|[terms-differenciation](https://ns.inria.fr/olivaw#terms-differenciation)|
|----|----|
|Title|Terms&#32;differenciation&#32;test|
|Description|A&#32;test&#32;case&#32;from&#32;the&#32;Best&#32;Practices&#32;tests&#32;checking&#32;if&#32;all&#32;the&#32;terms&#32;are&#32;different&#32;enough&#32;from&#32;each&#32;other&#32;according&#32;to&#32;the&#32;Levenshtein&#32;distance&#32;metric.|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-56)|Identifier|`too-close-terms`|
|[Section top](#pass-outcome-number-56)|Title|Terms&#32;differenciated&#32;enough|
|[Section top](#pass-outcome-number-56)|Description|All&#32;the&#32;terms&#32;have&#32;have&#32;a&#32;satisfying&#32;Levenshtein&#32;distance&#32;from&#32;each&#32;other&#32;term.|

***
### Pass Outcome number 57

[Jump to summary definition](#summary-Pass-57)	|	[Previous Pass outcome](#pass-outcome-number-56)	|	[Next Pass outcome](#pass-outcome-number-58)

:white_check_mark:Pass outcome
#### Subject detail
|Name|module-properties-ontology-catalogs|
|----|----|
|Title|Standalone&#32;module&#32;core&#92;properties&#92;ontology.catalogs.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- https://gitlab.com/coswot/coswot-acimov/blob/HEAD/core/properties/ontology.catalogs.ttl|

#### Criterion detail
|Identifier|[labeled-terms](https://ns.inria.fr/olivaw#labeled-terms)|
|----|----|
|Title|Term&#32;labeling&#32;test|
|Description|A&#32;test&#32;case&#32;from&#32;the&#32;Best&#32;Practices&#32;tests&#32;checking&#32;if&#32;all&#32;the&#32;terms&#32;of&#32;the&#32;subject&#32;have&#32;a&#32;rdfs:label&#32;property&#32;pointing&#32;to&#32;a&#32;literal&#32;in&#32;English|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-57)|Identifier|`not-labeled-term`|
|[Section top](#pass-outcome-number-57)|Title|All&#32;terms&#32;labeled|
|[Section top](#pass-outcome-number-57)|Description|All&#32;the&#32;terms&#32;defined&#32;in&#32;the&#32;subject&#32;have&#32;a&#32;rdfs:label&#32;in&#32;English|

***
### Pass Outcome number 58

[Jump to summary definition](#summary-Pass-58)	|	[Previous Pass outcome](#pass-outcome-number-57)	|	[Next Pass outcome](#pass-outcome-number-59)

:white_check_mark:Pass outcome
#### Subject detail
|Name|module-properties-ontology-catalogs|
|----|----|
|Title|Standalone&#32;module&#32;core&#92;properties&#92;ontology.catalogs.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- https://gitlab.com/coswot/coswot-acimov/blob/HEAD/core/properties/ontology.catalogs.ttl|

#### Criterion detail
|Identifier|[owl-rl-constraint](https://ns.inria.fr/olivaw#owl-rl-constraint)|
|----|----|
|Title|OWL&#32;RL&#32;Constraint&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;check&#32;wether&#32;the&#32;test&#32;subject&#32;is&#32;syntaxically&#32;correct&#32;or&#32;not.|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-58)|Identifier|`owl-rl-constraint-violation`|
|[Section top](#pass-outcome-number-58)|Title|OWL&#32;RL&#32;consistent|
|[Section top](#pass-outcome-number-58)|Description|The&#32;provided&#32;graph&#32;is&#32;consistent&#32;for&#32;any&#32;OWL&#32;RL&#32;constraint|

***
### Pass Outcome number 59

[Jump to summary definition](#summary-Pass-59)	|	[Previous Pass outcome](#pass-outcome-number-58)	|	[Next Pass outcome](#pass-outcome-number-60)

:white_check_mark:Pass outcome
#### Subject detail
|Name|module-properties-ontology-catalogs|
|----|----|
|Title|Standalone&#32;module&#32;core&#92;properties&#92;ontology.catalogs.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- https://gitlab.com/coswot/coswot-acimov/blob/HEAD/core/properties/ontology.catalogs.ttl|

#### Criterion detail
|Identifier|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|
|----|----|
|Title|Profile&#32;compatibility&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;check&#32;whether&#32;the&#32;test&#32;subject&#32;is&#32;compatible&#32;with&#32;a&#32;profile&#32;or&#32;not,&#32;and&#32;if&#32;it&#32;is&#32;not,&#32;why.|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-59)|Identifier|`owl-rl-profile-error`|
|[Section top](#pass-outcome-number-59)|Title|OWL&#32;RL&#32;Profile&#32;compatible|
|[Section top](#pass-outcome-number-59)|Description|The&#32;subject&#32;is&#32;included&#32;in&#32;the&#32;OWL&#32;RL&#32;sublanguage|

***
### Pass Outcome number 60

[Jump to summary definition](#summary-Pass-60)	|	[Previous Pass outcome](#pass-outcome-number-59)	|	[Next Pass outcome](#pass-outcome-number-61)

:white_check_mark:Pass outcome
#### Subject detail
|Name|module-properties-ontology-catalogs|
|----|----|
|Title|Standalone&#32;module&#32;core&#92;properties&#92;ontology.catalogs.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- https://gitlab.com/coswot/coswot-acimov/blob/HEAD/core/properties/ontology.catalogs.ttl|

#### Criterion detail
|Identifier|[proper-extension-predicate](https://ns.inria.fr/olivaw#proper-extension-predicate)|
|----|----|
|Title|Predicate&#32;extension&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;test&#32;the&#32;proper&#32;use&#32;of&#32;predicates&#32;rdfs:subClassOf&#32;and&#32;rdfs:subPropertyOf&#32;on&#32;the&#32;ontology&#32;terms|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-60)|Identifier|`class-subpropertyof`|
|[Section top](#pass-outcome-number-60)|Title|No&#32;class&#32;subproperty|
|[Section top](#pass-outcome-number-60)|Description|No&#32;ontology&#32;class&#32;is&#32;a&#32;subproperty|

***
### Pass Outcome number 61

[Jump to summary definition](#summary-Pass-61)	|	[Previous Pass outcome](#pass-outcome-number-60)	|	[Next Pass outcome](#pass-outcome-number-62)

:white_check_mark:Pass outcome
#### Subject detail
|Name|module-properties-ontology-catalogs|
|----|----|
|Title|Standalone&#32;module&#32;core&#92;properties&#92;ontology.catalogs.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- https://gitlab.com/coswot/coswot-acimov/blob/HEAD/core/properties/ontology.catalogs.ttl|

#### Criterion detail
|Identifier|[proper-extension-predicate](https://ns.inria.fr/olivaw#proper-extension-predicate)|
|----|----|
|Title|Predicate&#32;extension&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;test&#32;the&#32;proper&#32;use&#32;of&#32;predicates&#32;rdfs:subClassOf&#32;and&#32;rdfs:subPropertyOf&#32;on&#32;the&#32;ontology&#32;terms|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-61)|Identifier|`property-subclassof`|
|[Section top](#pass-outcome-number-61)|Title|No&#32;property&#32;subclass|
|[Section top](#pass-outcome-number-61)|Description|No&#32;ontology&#32;property&#32;is&#32;a&#32;subclass|

***
### Pass Outcome number 62

[Jump to summary definition](#summary-Pass-62)	|	[Previous Pass outcome](#pass-outcome-number-61)	|	[Next Pass outcome](#pass-outcome-number-63)

:white_check_mark:Pass outcome
#### Subject detail
|Name|module-properties-ontology-catalogs|
|----|----|
|Title|Standalone&#32;module&#32;core&#92;properties&#92;ontology.catalogs.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- https://gitlab.com/coswot/coswot-acimov/blob/HEAD/core/properties/ontology.catalogs.ttl|

#### Criterion detail
|Identifier|[proper-extension-predicate](https://ns.inria.fr/olivaw#proper-extension-predicate)|
|----|----|
|Title|Predicate&#32;extension&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;test&#32;the&#32;proper&#32;use&#32;of&#32;predicates&#32;rdfs:subClassOf&#32;and&#32;rdfs:subPropertyOf&#32;on&#32;the&#32;ontology&#32;terms|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-62)|Identifier|`subclassof-property`|
|[Section top](#pass-outcome-number-62)|Title|No&#32;subclass&#32;of&#32;property|
|[Section top](#pass-outcome-number-62)|Description|No&#32;ontology&#32;term&#32;is&#32;a&#32;subclass&#32;of&#32;a&#32;property|

***
### Pass Outcome number 63

[Jump to summary definition](#summary-Pass-63)	|	[Previous Pass outcome](#pass-outcome-number-62)	|	[Next Pass outcome](#pass-outcome-number-64)

:white_check_mark:Pass outcome
#### Subject detail
|Name|module-properties-ontology-catalogs|
|----|----|
|Title|Standalone&#32;module&#32;core&#92;properties&#92;ontology.catalogs.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- https://gitlab.com/coswot/coswot-acimov/blob/HEAD/core/properties/ontology.catalogs.ttl|

#### Criterion detail
|Identifier|[proper-extension-predicate](https://ns.inria.fr/olivaw#proper-extension-predicate)|
|----|----|
|Title|Predicate&#32;extension&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;test&#32;the&#32;proper&#32;use&#32;of&#32;predicates&#32;rdfs:subClassOf&#32;and&#32;rdfs:subPropertyOf&#32;on&#32;the&#32;ontology&#32;terms|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-63)|Identifier|`subpropertyof-class`|
|[Section top](#pass-outcome-number-63)|Title|No&#32;subproperty&#32;of&#32;class|
|[Section top](#pass-outcome-number-63)|Description|No&#32;ontology&#32;term&#32;is&#32;a&#32;subproperty&#32;of&#32;a&#32;class|

***
### Pass Outcome number 64

[Jump to summary definition](#summary-Pass-64)	|	[Previous Pass outcome](#pass-outcome-number-63)	|	[Next Pass outcome](#pass-outcome-number-65)

:white_check_mark:Pass outcome
#### Subject detail
|Name|module-properties-ontology-catalogs|
|----|----|
|Title|Standalone&#32;module&#32;core&#92;properties&#92;ontology.catalogs.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- https://gitlab.com/coswot/coswot-acimov/blob/HEAD/core/properties/ontology.catalogs.ttl|

#### Criterion detail
|Identifier|[term-referencing](https://ns.inria.fr/olivaw#term-referencing)|
|----|----|
|Title|Term&#32;referencing&#32;test|
|Description|A&#32;test&#32;case&#32;from&#32;the&#32;Best&#32;Practices&#32;tests&#32;checking&#32;if&#32;each&#32;term&#32;of&#32;the&#32;test&#32;subject&#32;is&#32;referenced&#32;to&#32;a&#32;module&#32;through&#32;a&#32;rdfs:isDefinedBy&#32;property.|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-64)|Identifier|`no-reference-module`|
|[Section top](#pass-outcome-number-64)|Title|Any&#32;term&#32;is&#32;referenced|
|[Section top](#pass-outcome-number-64)|Description|Each&#32;term&#32;of&#32;the&#32;test&#32;subject&#32;is&#32;linked&#32;to&#32;a&#32;module&#32;by&#32;a&#32;rdfs:isDefinedBy&#32;property|

***
### Pass Outcome number 65

[Jump to summary definition](#summary-Pass-65)	|	[Previous Pass outcome](#pass-outcome-number-64)	|	[Next Pass outcome](#pass-outcome-number-66)

:white_check_mark:Pass outcome
#### Subject detail
|Name|module-properties-ontology-catalogs|
|----|----|
|Title|Standalone&#32;module&#32;core&#92;properties&#92;ontology.catalogs.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- https://gitlab.com/coswot/coswot-acimov/blob/HEAD/core/properties/ontology.catalogs.ttl|

#### Criterion detail
|Identifier|[terms-differenciation](https://ns.inria.fr/olivaw#terms-differenciation)|
|----|----|
|Title|Terms&#32;differenciation&#32;test|
|Description|A&#32;test&#32;case&#32;from&#32;the&#32;Best&#32;Practices&#32;tests&#32;checking&#32;if&#32;all&#32;the&#32;terms&#32;are&#32;different&#32;enough&#32;from&#32;each&#32;other&#32;according&#32;to&#32;the&#32;Levenshtein&#32;distance&#32;metric.|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-65)|Identifier|`too-close-terms`|
|[Section top](#pass-outcome-number-65)|Title|Terms&#32;differenciated&#32;enough|
|[Section top](#pass-outcome-number-65)|Description|All&#32;the&#32;terms&#32;have&#32;have&#32;a&#32;satisfying&#32;Levenshtein&#32;distance&#32;from&#32;each&#32;other&#32;term.|

***
### Pass Outcome number 66

[Jump to summary definition](#summary-Pass-66)	|	[Previous Pass outcome](#pass-outcome-number-65)	|	[Next Pass outcome](#pass-outcome-number-67)

:white_check_mark:Pass outcome
#### Subject detail
|Name|module-properties-ontology|
|----|----|
|Title|Standalone&#32;module&#32;core&#92;properties&#92;ontology.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- https://gitlab.com/coswot/coswot-acimov/blob/HEAD/core/properties/ontology.ttl|

#### Criterion detail
|Identifier|[labeled-terms](https://ns.inria.fr/olivaw#labeled-terms)|
|----|----|
|Title|Term&#32;labeling&#32;test|
|Description|A&#32;test&#32;case&#32;from&#32;the&#32;Best&#32;Practices&#32;tests&#32;checking&#32;if&#32;all&#32;the&#32;terms&#32;of&#32;the&#32;subject&#32;have&#32;a&#32;rdfs:label&#32;property&#32;pointing&#32;to&#32;a&#32;literal&#32;in&#32;English|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-66)|Identifier|`not-labeled-term`|
|[Section top](#pass-outcome-number-66)|Title|All&#32;terms&#32;labeled|
|[Section top](#pass-outcome-number-66)|Description|All&#32;the&#32;terms&#32;defined&#32;in&#32;the&#32;subject&#32;have&#32;a&#32;rdfs:label&#32;in&#32;English|

***
### Pass Outcome number 67

[Jump to summary definition](#summary-Pass-67)	|	[Previous Pass outcome](#pass-outcome-number-66)	|	[Next Pass outcome](#pass-outcome-number-68)

:white_check_mark:Pass outcome
#### Subject detail
|Name|module-properties-ontology|
|----|----|
|Title|Standalone&#32;module&#32;core&#92;properties&#92;ontology.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- https://gitlab.com/coswot/coswot-acimov/blob/HEAD/core/properties/ontology.ttl|

#### Criterion detail
|Identifier|[owl-rl-constraint](https://ns.inria.fr/olivaw#owl-rl-constraint)|
|----|----|
|Title|OWL&#32;RL&#32;Constraint&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;check&#32;wether&#32;the&#32;test&#32;subject&#32;is&#32;syntaxically&#32;correct&#32;or&#32;not.|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-67)|Identifier|`owl-rl-constraint-violation`|
|[Section top](#pass-outcome-number-67)|Title|OWL&#32;RL&#32;consistent|
|[Section top](#pass-outcome-number-67)|Description|The&#32;provided&#32;graph&#32;is&#32;consistent&#32;for&#32;any&#32;OWL&#32;RL&#32;constraint|

***
### Pass Outcome number 68

[Jump to summary definition](#summary-Pass-68)	|	[Previous Pass outcome](#pass-outcome-number-67)	|	[Next Pass outcome](#pass-outcome-number-69)

:white_check_mark:Pass outcome
#### Subject detail
|Name|module-properties-ontology|
|----|----|
|Title|Standalone&#32;module&#32;core&#92;properties&#92;ontology.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- https://gitlab.com/coswot/coswot-acimov/blob/HEAD/core/properties/ontology.ttl|

#### Criterion detail
|Identifier|[proper-extension-predicate](https://ns.inria.fr/olivaw#proper-extension-predicate)|
|----|----|
|Title|Predicate&#32;extension&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;test&#32;the&#32;proper&#32;use&#32;of&#32;predicates&#32;rdfs:subClassOf&#32;and&#32;rdfs:subPropertyOf&#32;on&#32;the&#32;ontology&#32;terms|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-68)|Identifier|`class-subpropertyof`|
|[Section top](#pass-outcome-number-68)|Title|No&#32;class&#32;subproperty|
|[Section top](#pass-outcome-number-68)|Description|No&#32;ontology&#32;class&#32;is&#32;a&#32;subproperty|

***
### Pass Outcome number 69

[Jump to summary definition](#summary-Pass-69)	|	[Previous Pass outcome](#pass-outcome-number-68)	|	[Next Pass outcome](#pass-outcome-number-70)

:white_check_mark:Pass outcome
#### Subject detail
|Name|module-properties-ontology|
|----|----|
|Title|Standalone&#32;module&#32;core&#92;properties&#92;ontology.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- https://gitlab.com/coswot/coswot-acimov/blob/HEAD/core/properties/ontology.ttl|

#### Criterion detail
|Identifier|[proper-extension-predicate](https://ns.inria.fr/olivaw#proper-extension-predicate)|
|----|----|
|Title|Predicate&#32;extension&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;test&#32;the&#32;proper&#32;use&#32;of&#32;predicates&#32;rdfs:subClassOf&#32;and&#32;rdfs:subPropertyOf&#32;on&#32;the&#32;ontology&#32;terms|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-69)|Identifier|`property-subclassof`|
|[Section top](#pass-outcome-number-69)|Title|No&#32;property&#32;subclass|
|[Section top](#pass-outcome-number-69)|Description|No&#32;ontology&#32;property&#32;is&#32;a&#32;subclass|

***
### Pass Outcome number 70

[Jump to summary definition](#summary-Pass-70)	|	[Previous Pass outcome](#pass-outcome-number-69)	|	[Next Pass outcome](#pass-outcome-number-71)

:white_check_mark:Pass outcome
#### Subject detail
|Name|module-properties-ontology|
|----|----|
|Title|Standalone&#32;module&#32;core&#92;properties&#92;ontology.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- https://gitlab.com/coswot/coswot-acimov/blob/HEAD/core/properties/ontology.ttl|

#### Criterion detail
|Identifier|[proper-extension-predicate](https://ns.inria.fr/olivaw#proper-extension-predicate)|
|----|----|
|Title|Predicate&#32;extension&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;test&#32;the&#32;proper&#32;use&#32;of&#32;predicates&#32;rdfs:subClassOf&#32;and&#32;rdfs:subPropertyOf&#32;on&#32;the&#32;ontology&#32;terms|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-70)|Identifier|`subclassof-property`|
|[Section top](#pass-outcome-number-70)|Title|No&#32;subclass&#32;of&#32;property|
|[Section top](#pass-outcome-number-70)|Description|No&#32;ontology&#32;term&#32;is&#32;a&#32;subclass&#32;of&#32;a&#32;property|

***
### Pass Outcome number 71

[Jump to summary definition](#summary-Pass-71)	|	[Previous Pass outcome](#pass-outcome-number-70)	|	[Next Pass outcome](#pass-outcome-number-72)

:white_check_mark:Pass outcome
#### Subject detail
|Name|module-properties-ontology|
|----|----|
|Title|Standalone&#32;module&#32;core&#92;properties&#92;ontology.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- https://gitlab.com/coswot/coswot-acimov/blob/HEAD/core/properties/ontology.ttl|

#### Criterion detail
|Identifier|[proper-extension-predicate](https://ns.inria.fr/olivaw#proper-extension-predicate)|
|----|----|
|Title|Predicate&#32;extension&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;test&#32;the&#32;proper&#32;use&#32;of&#32;predicates&#32;rdfs:subClassOf&#32;and&#32;rdfs:subPropertyOf&#32;on&#32;the&#32;ontology&#32;terms|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-71)|Identifier|`subpropertyof-class`|
|[Section top](#pass-outcome-number-71)|Title|No&#32;subproperty&#32;of&#32;class|
|[Section top](#pass-outcome-number-71)|Description|No&#32;ontology&#32;term&#32;is&#32;a&#32;subproperty&#32;of&#32;a&#32;class|

***
### Pass Outcome number 72

[Jump to summary definition](#summary-Pass-72)	|	[Previous Pass outcome](#pass-outcome-number-71)	|	[Next Pass outcome](#pass-outcome-number-73)

:white_check_mark:Pass outcome
#### Subject detail
|Name|module-properties-ontology|
|----|----|
|Title|Standalone&#32;module&#32;core&#92;properties&#92;ontology.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- https://gitlab.com/coswot/coswot-acimov/blob/HEAD/core/properties/ontology.ttl|

#### Criterion detail
|Identifier|[term-referencing](https://ns.inria.fr/olivaw#term-referencing)|
|----|----|
|Title|Term&#32;referencing&#32;test|
|Description|A&#32;test&#32;case&#32;from&#32;the&#32;Best&#32;Practices&#32;tests&#32;checking&#32;if&#32;each&#32;term&#32;of&#32;the&#32;test&#32;subject&#32;is&#32;referenced&#32;to&#32;a&#32;module&#32;through&#32;a&#32;rdfs:isDefinedBy&#32;property.|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-72)|Identifier|`no-reference-module`|
|[Section top](#pass-outcome-number-72)|Title|Any&#32;term&#32;is&#32;referenced|
|[Section top](#pass-outcome-number-72)|Description|Each&#32;term&#32;of&#32;the&#32;test&#32;subject&#32;is&#32;linked&#32;to&#32;a&#32;module&#32;by&#32;a&#32;rdfs:isDefinedBy&#32;property|

***
### Pass Outcome number 73

[Jump to summary definition](#summary-Pass-73)	|	[Previous Pass outcome](#pass-outcome-number-72)	|	[Next Pass outcome](#pass-outcome-number-74)

:white_check_mark:Pass outcome
#### Subject detail
|Name|module-properties-ontology|
|----|----|
|Title|Standalone&#32;module&#32;core&#92;properties&#92;ontology.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- https://gitlab.com/coswot/coswot-acimov/blob/HEAD/core/properties/ontology.ttl|

#### Criterion detail
|Identifier|[terms-differenciation](https://ns.inria.fr/olivaw#terms-differenciation)|
|----|----|
|Title|Terms&#32;differenciation&#32;test|
|Description|A&#32;test&#32;case&#32;from&#32;the&#32;Best&#32;Practices&#32;tests&#32;checking&#32;if&#32;all&#32;the&#32;terms&#32;are&#32;different&#32;enough&#32;from&#32;each&#32;other&#32;according&#32;to&#32;the&#32;Levenshtein&#32;distance&#32;metric.|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-73)|Identifier|`too-close-terms`|
|[Section top](#pass-outcome-number-73)|Title|Terms&#32;differenciated&#32;enough|
|[Section top](#pass-outcome-number-73)|Description|All&#32;the&#32;terms&#32;have&#32;have&#32;a&#32;satisfying&#32;Levenshtein&#32;distance&#32;from&#32;each&#32;other&#32;term.|

***
### Pass Outcome number 74

[Jump to summary definition](#summary-Pass-74)	|	[Previous Pass outcome](#pass-outcome-number-73)	|	[Next Pass outcome](#pass-outcome-number-75)

:white_check_mark:Pass outcome
#### Subject detail
|Name|module-procedures-ontology|
|----|----|
|Title|Standalone&#32;module&#32;core&#92;procedures&#92;ontology.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- https://gitlab.com/coswot/coswot-acimov/blob/HEAD/core/procedures/ontology.ttl|

#### Criterion detail
|Identifier|[domain-and-range-referencing](https://ns.inria.fr/olivaw#domain-and-range-referencing)|
|----|----|
|Title|Domain&#32;and&#32;range&#32;referencing&#32;test|
|Description|A&#32;test&#32;case&#32;from&#32;the&#32;Best&#32;Practices&#32;tests&#32;checking&#32;if&#32;all&#32;the&#32;ranges&#32;and&#32;domains&#32;from&#32;the&#32;test&#32;subject&#32;point&#32;to&#32;terms&#32;that&#32;are&#32;defined&#32;in&#32;the&#32;vocabulary.|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-74)|Identifier|`domain-out-of-vocabulary`|
|[Section top](#pass-outcome-number-74)|Title|Domains&#32;properly&#32;defined|
|[Section top](#pass-outcome-number-74)|Description|Each&#32;rdfs:domain&#32;is&#32;defined&#32;within&#32;the&#32;fragment|

***
### Pass Outcome number 75

[Jump to summary definition](#summary-Pass-75)	|	[Previous Pass outcome](#pass-outcome-number-74)	|	[Next Pass outcome](#pass-outcome-number-76)

:white_check_mark:Pass outcome
#### Subject detail
|Name|module-procedures-ontology|
|----|----|
|Title|Standalone&#32;module&#32;core&#92;procedures&#92;ontology.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- https://gitlab.com/coswot/coswot-acimov/blob/HEAD/core/procedures/ontology.ttl|

#### Criterion detail
|Identifier|[labeled-terms](https://ns.inria.fr/olivaw#labeled-terms)|
|----|----|
|Title|Term&#32;labeling&#32;test|
|Description|A&#32;test&#32;case&#32;from&#32;the&#32;Best&#32;Practices&#32;tests&#32;checking&#32;if&#32;all&#32;the&#32;terms&#32;of&#32;the&#32;subject&#32;have&#32;a&#32;rdfs:label&#32;property&#32;pointing&#32;to&#32;a&#32;literal&#32;in&#32;English|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-75)|Identifier|`not-labeled-term`|
|[Section top](#pass-outcome-number-75)|Title|All&#32;terms&#32;labeled|
|[Section top](#pass-outcome-number-75)|Description|All&#32;the&#32;terms&#32;defined&#32;in&#32;the&#32;subject&#32;have&#32;a&#32;rdfs:label&#32;in&#32;English|

***
### Pass Outcome number 76

[Jump to summary definition](#summary-Pass-76)	|	[Previous Pass outcome](#pass-outcome-number-75)	|	[Next Pass outcome](#pass-outcome-number-77)

:white_check_mark:Pass outcome
#### Subject detail
|Name|module-procedures-ontology|
|----|----|
|Title|Standalone&#32;module&#32;core&#92;procedures&#92;ontology.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- https://gitlab.com/coswot/coswot-acimov/blob/HEAD/core/procedures/ontology.ttl|

#### Criterion detail
|Identifier|[owl-rl-constraint](https://ns.inria.fr/olivaw#owl-rl-constraint)|
|----|----|
|Title|OWL&#32;RL&#32;Constraint&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;check&#32;wether&#32;the&#32;test&#32;subject&#32;is&#32;syntaxically&#32;correct&#32;or&#32;not.|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-76)|Identifier|`owl-rl-constraint-violation`|
|[Section top](#pass-outcome-number-76)|Title|OWL&#32;RL&#32;consistent|
|[Section top](#pass-outcome-number-76)|Description|The&#32;provided&#32;graph&#32;is&#32;consistent&#32;for&#32;any&#32;OWL&#32;RL&#32;constraint|

***
### Pass Outcome number 77

[Jump to summary definition](#summary-Pass-77)	|	[Previous Pass outcome](#pass-outcome-number-76)	|	[Next Pass outcome](#pass-outcome-number-78)

:white_check_mark:Pass outcome
#### Subject detail
|Name|module-procedures-ontology|
|----|----|
|Title|Standalone&#32;module&#32;core&#92;procedures&#92;ontology.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- https://gitlab.com/coswot/coswot-acimov/blob/HEAD/core/procedures/ontology.ttl|

#### Criterion detail
|Identifier|[proper-extension-predicate](https://ns.inria.fr/olivaw#proper-extension-predicate)|
|----|----|
|Title|Predicate&#32;extension&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;test&#32;the&#32;proper&#32;use&#32;of&#32;predicates&#32;rdfs:subClassOf&#32;and&#32;rdfs:subPropertyOf&#32;on&#32;the&#32;ontology&#32;terms|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-77)|Identifier|`class-subpropertyof`|
|[Section top](#pass-outcome-number-77)|Title|No&#32;class&#32;subproperty|
|[Section top](#pass-outcome-number-77)|Description|No&#32;ontology&#32;class&#32;is&#32;a&#32;subproperty|

***
### Pass Outcome number 78

[Jump to summary definition](#summary-Pass-78)	|	[Previous Pass outcome](#pass-outcome-number-77)	|	[Next Pass outcome](#pass-outcome-number-79)

:white_check_mark:Pass outcome
#### Subject detail
|Name|module-procedures-ontology|
|----|----|
|Title|Standalone&#32;module&#32;core&#92;procedures&#92;ontology.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- https://gitlab.com/coswot/coswot-acimov/blob/HEAD/core/procedures/ontology.ttl|

#### Criterion detail
|Identifier|[proper-extension-predicate](https://ns.inria.fr/olivaw#proper-extension-predicate)|
|----|----|
|Title|Predicate&#32;extension&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;test&#32;the&#32;proper&#32;use&#32;of&#32;predicates&#32;rdfs:subClassOf&#32;and&#32;rdfs:subPropertyOf&#32;on&#32;the&#32;ontology&#32;terms|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-78)|Identifier|`property-subclassof`|
|[Section top](#pass-outcome-number-78)|Title|No&#32;property&#32;subclass|
|[Section top](#pass-outcome-number-78)|Description|No&#32;ontology&#32;property&#32;is&#32;a&#32;subclass|

***
### Pass Outcome number 79

[Jump to summary definition](#summary-Pass-79)	|	[Previous Pass outcome](#pass-outcome-number-78)	|	[Next Pass outcome](#pass-outcome-number-80)

:white_check_mark:Pass outcome
#### Subject detail
|Name|module-procedures-ontology|
|----|----|
|Title|Standalone&#32;module&#32;core&#92;procedures&#92;ontology.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- https://gitlab.com/coswot/coswot-acimov/blob/HEAD/core/procedures/ontology.ttl|

#### Criterion detail
|Identifier|[proper-extension-predicate](https://ns.inria.fr/olivaw#proper-extension-predicate)|
|----|----|
|Title|Predicate&#32;extension&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;test&#32;the&#32;proper&#32;use&#32;of&#32;predicates&#32;rdfs:subClassOf&#32;and&#32;rdfs:subPropertyOf&#32;on&#32;the&#32;ontology&#32;terms|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-79)|Identifier|`subclassof-property`|
|[Section top](#pass-outcome-number-79)|Title|No&#32;subclass&#32;of&#32;property|
|[Section top](#pass-outcome-number-79)|Description|No&#32;ontology&#32;term&#32;is&#32;a&#32;subclass&#32;of&#32;a&#32;property|

***
### Pass Outcome number 80

[Jump to summary definition](#summary-Pass-80)	|	[Previous Pass outcome](#pass-outcome-number-79)	|	[Next Pass outcome](#pass-outcome-number-81)

:white_check_mark:Pass outcome
#### Subject detail
|Name|module-procedures-ontology|
|----|----|
|Title|Standalone&#32;module&#32;core&#92;procedures&#92;ontology.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- https://gitlab.com/coswot/coswot-acimov/blob/HEAD/core/procedures/ontology.ttl|

#### Criterion detail
|Identifier|[proper-extension-predicate](https://ns.inria.fr/olivaw#proper-extension-predicate)|
|----|----|
|Title|Predicate&#32;extension&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;test&#32;the&#32;proper&#32;use&#32;of&#32;predicates&#32;rdfs:subClassOf&#32;and&#32;rdfs:subPropertyOf&#32;on&#32;the&#32;ontology&#32;terms|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-80)|Identifier|`subpropertyof-class`|
|[Section top](#pass-outcome-number-80)|Title|No&#32;subproperty&#32;of&#32;class|
|[Section top](#pass-outcome-number-80)|Description|No&#32;ontology&#32;term&#32;is&#32;a&#32;subproperty&#32;of&#32;a&#32;class|

***
### Pass Outcome number 81

[Jump to summary definition](#summary-Pass-81)	|	[Previous Pass outcome](#pass-outcome-number-80)	|	[Next Pass outcome](#pass-outcome-number-82)

:white_check_mark:Pass outcome
#### Subject detail
|Name|module-procedures-ontology|
|----|----|
|Title|Standalone&#32;module&#32;core&#92;procedures&#92;ontology.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- https://gitlab.com/coswot/coswot-acimov/blob/HEAD/core/procedures/ontology.ttl|

#### Criterion detail
|Identifier|[term-referencing](https://ns.inria.fr/olivaw#term-referencing)|
|----|----|
|Title|Term&#32;referencing&#32;test|
|Description|A&#32;test&#32;case&#32;from&#32;the&#32;Best&#32;Practices&#32;tests&#32;checking&#32;if&#32;each&#32;term&#32;of&#32;the&#32;test&#32;subject&#32;is&#32;referenced&#32;to&#32;a&#32;module&#32;through&#32;a&#32;rdfs:isDefinedBy&#32;property.|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-81)|Identifier|`no-reference-module`|
|[Section top](#pass-outcome-number-81)|Title|Any&#32;term&#32;is&#32;referenced|
|[Section top](#pass-outcome-number-81)|Description|Each&#32;term&#32;of&#32;the&#32;test&#32;subject&#32;is&#32;linked&#32;to&#32;a&#32;module&#32;by&#32;a&#32;rdfs:isDefinedBy&#32;property|

***
### Pass Outcome number 82

[Jump to summary definition](#summary-Pass-82)	|	[Previous Pass outcome](#pass-outcome-number-81)	|	[Next Pass outcome](#pass-outcome-number-83)

:white_check_mark:Pass outcome
#### Subject detail
|Name|module-procedures-ontology|
|----|----|
|Title|Standalone&#32;module&#32;core&#92;procedures&#92;ontology.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- https://gitlab.com/coswot/coswot-acimov/blob/HEAD/core/procedures/ontology.ttl|

#### Criterion detail
|Identifier|[terms-differenciation](https://ns.inria.fr/olivaw#terms-differenciation)|
|----|----|
|Title|Terms&#32;differenciation&#32;test|
|Description|A&#32;test&#32;case&#32;from&#32;the&#32;Best&#32;Practices&#32;tests&#32;checking&#32;if&#32;all&#32;the&#32;terms&#32;are&#32;different&#32;enough&#32;from&#32;each&#32;other&#32;according&#32;to&#32;the&#32;Levenshtein&#32;distance&#32;metric.|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-82)|Identifier|`too-close-terms`|
|[Section top](#pass-outcome-number-82)|Title|Terms&#32;differenciated&#32;enough|
|[Section top](#pass-outcome-number-82)|Description|All&#32;the&#32;terms&#32;have&#32;have&#32;a&#32;satisfying&#32;Levenshtein&#32;distance&#32;from&#32;each&#32;other&#32;term.|

***
### Pass Outcome number 83

[Jump to summary definition](#summary-Pass-83)	|	[Previous Pass outcome](#pass-outcome-number-82)	|	[Next Pass outcome](#pass-outcome-number-84)

:white_check_mark:Pass outcome
#### Subject detail
|Name|module-ontology|
|----|----|
|Title|Standalone&#32;module&#32;core&#92;ontology.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- https://gitlab.com/coswot/coswot-acimov/blob/HEAD/core/ontology.ttl|

#### Criterion detail
|Identifier|[domain-and-range-referencing](https://ns.inria.fr/olivaw#domain-and-range-referencing)|
|----|----|
|Title|Domain&#32;and&#32;range&#32;referencing&#32;test|
|Description|A&#32;test&#32;case&#32;from&#32;the&#32;Best&#32;Practices&#32;tests&#32;checking&#32;if&#32;all&#32;the&#32;ranges&#32;and&#32;domains&#32;from&#32;the&#32;test&#32;subject&#32;point&#32;to&#32;terms&#32;that&#32;are&#32;defined&#32;in&#32;the&#32;vocabulary.|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-83)|Identifier|`domain-out-of-vocabulary`|
|[Section top](#pass-outcome-number-83)|Title|Domains&#32;properly&#32;defined|
|[Section top](#pass-outcome-number-83)|Description|Each&#32;rdfs:domain&#32;is&#32;defined&#32;within&#32;the&#32;fragment|

***
### Pass Outcome number 84

[Jump to summary definition](#summary-Pass-84)	|	[Previous Pass outcome](#pass-outcome-number-83)	|	[Next Pass outcome](#pass-outcome-number-85)

:white_check_mark:Pass outcome
#### Subject detail
|Name|module-ontology|
|----|----|
|Title|Standalone&#32;module&#32;core&#92;ontology.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- https://gitlab.com/coswot/coswot-acimov/blob/HEAD/core/ontology.ttl|

#### Criterion detail
|Identifier|[domain-and-range-referencing](https://ns.inria.fr/olivaw#domain-and-range-referencing)|
|----|----|
|Title|Domain&#32;and&#32;range&#32;referencing&#32;test|
|Description|A&#32;test&#32;case&#32;from&#32;the&#32;Best&#32;Practices&#32;tests&#32;checking&#32;if&#32;all&#32;the&#32;ranges&#32;and&#32;domains&#32;from&#32;the&#32;test&#32;subject&#32;point&#32;to&#32;terms&#32;that&#32;are&#32;defined&#32;in&#32;the&#32;vocabulary.|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-84)|Identifier|`range-out-of-vocabulary`|
|[Section top](#pass-outcome-number-84)|Title|Ranges&#32;properly&#32;defined|
|[Section top](#pass-outcome-number-84)|Description|Each&#32;rdfs:range&#32;is&#32;defined&#32;within&#32;the&#32;fragment|

***
### Pass Outcome number 85

[Jump to summary definition](#summary-Pass-85)	|	[Previous Pass outcome](#pass-outcome-number-84)	|	[Next Pass outcome](#pass-outcome-number-86)

:white_check_mark:Pass outcome
#### Subject detail
|Name|module-ontology|
|----|----|
|Title|Standalone&#32;module&#32;core&#92;ontology.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- https://gitlab.com/coswot/coswot-acimov/blob/HEAD/core/ontology.ttl|

#### Criterion detail
|Identifier|[labeled-terms](https://ns.inria.fr/olivaw#labeled-terms)|
|----|----|
|Title|Term&#32;labeling&#32;test|
|Description|A&#32;test&#32;case&#32;from&#32;the&#32;Best&#32;Practices&#32;tests&#32;checking&#32;if&#32;all&#32;the&#32;terms&#32;of&#32;the&#32;subject&#32;have&#32;a&#32;rdfs:label&#32;property&#32;pointing&#32;to&#32;a&#32;literal&#32;in&#32;English|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-85)|Identifier|`not-labeled-term`|
|[Section top](#pass-outcome-number-85)|Title|All&#32;terms&#32;labeled|
|[Section top](#pass-outcome-number-85)|Description|All&#32;the&#32;terms&#32;defined&#32;in&#32;the&#32;subject&#32;have&#32;a&#32;rdfs:label&#32;in&#32;English|

***
### Pass Outcome number 86

[Jump to summary definition](#summary-Pass-86)	|	[Previous Pass outcome](#pass-outcome-number-85)	|	[Next Pass outcome](#pass-outcome-number-87)

:white_check_mark:Pass outcome
#### Subject detail
|Name|module-ontology|
|----|----|
|Title|Standalone&#32;module&#32;core&#92;ontology.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- https://gitlab.com/coswot/coswot-acimov/blob/HEAD/core/ontology.ttl|

#### Criterion detail
|Identifier|[owl-rl-constraint](https://ns.inria.fr/olivaw#owl-rl-constraint)|
|----|----|
|Title|OWL&#32;RL&#32;Constraint&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;check&#32;wether&#32;the&#32;test&#32;subject&#32;is&#32;syntaxically&#32;correct&#32;or&#32;not.|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-86)|Identifier|`owl-rl-constraint-violation`|
|[Section top](#pass-outcome-number-86)|Title|OWL&#32;RL&#32;consistent|
|[Section top](#pass-outcome-number-86)|Description|The&#32;provided&#32;graph&#32;is&#32;consistent&#32;for&#32;any&#32;OWL&#32;RL&#32;constraint|

***
### Pass Outcome number 87

[Jump to summary definition](#summary-Pass-87)	|	[Previous Pass outcome](#pass-outcome-number-86)	|	[Next Pass outcome](#pass-outcome-number-88)

:white_check_mark:Pass outcome
#### Subject detail
|Name|module-ontology|
|----|----|
|Title|Standalone&#32;module&#32;core&#92;ontology.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- https://gitlab.com/coswot/coswot-acimov/blob/HEAD/core/ontology.ttl|

#### Criterion detail
|Identifier|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|
|----|----|
|Title|Profile&#32;compatibility&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;check&#32;whether&#32;the&#32;test&#32;subject&#32;is&#32;compatible&#32;with&#32;a&#32;profile&#32;or&#32;not,&#32;and&#32;if&#32;it&#32;is&#32;not,&#32;why.|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-87)|Identifier|`owl-el-profile-error`|
|[Section top](#pass-outcome-number-87)|Title|OWL&#32;EL&#32;Profile&#32;compatible|
|[Section top](#pass-outcome-number-87)|Description|The&#32;subject&#32;is&#32;included&#32;in&#32;the&#32;OWL&#32;EL&#32;sublanguage|

***
### Pass Outcome number 88

[Jump to summary definition](#summary-Pass-88)	|	[Previous Pass outcome](#pass-outcome-number-87)	|	[Next Pass outcome](#pass-outcome-number-89)

:white_check_mark:Pass outcome
#### Subject detail
|Name|module-ontology|
|----|----|
|Title|Standalone&#32;module&#32;core&#92;ontology.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- https://gitlab.com/coswot/coswot-acimov/blob/HEAD/core/ontology.ttl|

#### Criterion detail
|Identifier|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|
|----|----|
|Title|Profile&#32;compatibility&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;check&#32;whether&#32;the&#32;test&#32;subject&#32;is&#32;compatible&#32;with&#32;a&#32;profile&#32;or&#32;not,&#32;and&#32;if&#32;it&#32;is&#32;not,&#32;why.|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-88)|Identifier|`owl-ql-profile-error`|
|[Section top](#pass-outcome-number-88)|Title|OWL&#32;QL&#32;Profile&#32;compatible|
|[Section top](#pass-outcome-number-88)|Description|The&#32;subject&#32;is&#32;included&#32;in&#32;the&#32;OWL&#32;QL&#32;sublanguage|

***
### Pass Outcome number 89

[Jump to summary definition](#summary-Pass-89)	|	[Previous Pass outcome](#pass-outcome-number-88)	|	[Next Pass outcome](#pass-outcome-number-90)

:white_check_mark:Pass outcome
#### Subject detail
|Name|module-ontology|
|----|----|
|Title|Standalone&#32;module&#32;core&#92;ontology.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- https://gitlab.com/coswot/coswot-acimov/blob/HEAD/core/ontology.ttl|

#### Criterion detail
|Identifier|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|
|----|----|
|Title|Profile&#32;compatibility&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;check&#32;whether&#32;the&#32;test&#32;subject&#32;is&#32;compatible&#32;with&#32;a&#32;profile&#32;or&#32;not,&#32;and&#32;if&#32;it&#32;is&#32;not,&#32;why.|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-89)|Identifier|`owl-rl-profile-error`|
|[Section top](#pass-outcome-number-89)|Title|OWL&#32;RL&#32;Profile&#32;compatible|
|[Section top](#pass-outcome-number-89)|Description|The&#32;subject&#32;is&#32;included&#32;in&#32;the&#32;OWL&#32;RL&#32;sublanguage|

***
### Pass Outcome number 90

[Jump to summary definition](#summary-Pass-90)	|	[Previous Pass outcome](#pass-outcome-number-89)	|	[Next Pass outcome](#pass-outcome-number-91)

:white_check_mark:Pass outcome
#### Subject detail
|Name|module-ontology|
|----|----|
|Title|Standalone&#32;module&#32;core&#92;ontology.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- https://gitlab.com/coswot/coswot-acimov/blob/HEAD/core/ontology.ttl|

#### Criterion detail
|Identifier|[proper-extension-predicate](https://ns.inria.fr/olivaw#proper-extension-predicate)|
|----|----|
|Title|Predicate&#32;extension&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;test&#32;the&#32;proper&#32;use&#32;of&#32;predicates&#32;rdfs:subClassOf&#32;and&#32;rdfs:subPropertyOf&#32;on&#32;the&#32;ontology&#32;terms|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-90)|Identifier|`class-subpropertyof`|
|[Section top](#pass-outcome-number-90)|Title|No&#32;class&#32;subproperty|
|[Section top](#pass-outcome-number-90)|Description|No&#32;ontology&#32;class&#32;is&#32;a&#32;subproperty|

***
### Pass Outcome number 91

[Jump to summary definition](#summary-Pass-91)	|	[Previous Pass outcome](#pass-outcome-number-90)	|	[Next Pass outcome](#pass-outcome-number-92)

:white_check_mark:Pass outcome
#### Subject detail
|Name|module-ontology|
|----|----|
|Title|Standalone&#32;module&#32;core&#92;ontology.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- https://gitlab.com/coswot/coswot-acimov/blob/HEAD/core/ontology.ttl|

#### Criterion detail
|Identifier|[proper-extension-predicate](https://ns.inria.fr/olivaw#proper-extension-predicate)|
|----|----|
|Title|Predicate&#32;extension&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;test&#32;the&#32;proper&#32;use&#32;of&#32;predicates&#32;rdfs:subClassOf&#32;and&#32;rdfs:subPropertyOf&#32;on&#32;the&#32;ontology&#32;terms|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-91)|Identifier|`property-subclassof`|
|[Section top](#pass-outcome-number-91)|Title|No&#32;property&#32;subclass|
|[Section top](#pass-outcome-number-91)|Description|No&#32;ontology&#32;property&#32;is&#32;a&#32;subclass|

***
### Pass Outcome number 92

[Jump to summary definition](#summary-Pass-92)	|	[Previous Pass outcome](#pass-outcome-number-91)	|	[Next Pass outcome](#pass-outcome-number-93)

:white_check_mark:Pass outcome
#### Subject detail
|Name|module-ontology|
|----|----|
|Title|Standalone&#32;module&#32;core&#92;ontology.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- https://gitlab.com/coswot/coswot-acimov/blob/HEAD/core/ontology.ttl|

#### Criterion detail
|Identifier|[proper-extension-predicate](https://ns.inria.fr/olivaw#proper-extension-predicate)|
|----|----|
|Title|Predicate&#32;extension&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;test&#32;the&#32;proper&#32;use&#32;of&#32;predicates&#32;rdfs:subClassOf&#32;and&#32;rdfs:subPropertyOf&#32;on&#32;the&#32;ontology&#32;terms|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-92)|Identifier|`subclassof-property`|
|[Section top](#pass-outcome-number-92)|Title|No&#32;subclass&#32;of&#32;property|
|[Section top](#pass-outcome-number-92)|Description|No&#32;ontology&#32;term&#32;is&#32;a&#32;subclass&#32;of&#32;a&#32;property|

***
### Pass Outcome number 93

[Jump to summary definition](#summary-Pass-93)	|	[Previous Pass outcome](#pass-outcome-number-92)	|	[Next Pass outcome](#pass-outcome-number-94)

:white_check_mark:Pass outcome
#### Subject detail
|Name|module-ontology|
|----|----|
|Title|Standalone&#32;module&#32;core&#92;ontology.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- https://gitlab.com/coswot/coswot-acimov/blob/HEAD/core/ontology.ttl|

#### Criterion detail
|Identifier|[proper-extension-predicate](https://ns.inria.fr/olivaw#proper-extension-predicate)|
|----|----|
|Title|Predicate&#32;extension&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;test&#32;the&#32;proper&#32;use&#32;of&#32;predicates&#32;rdfs:subClassOf&#32;and&#32;rdfs:subPropertyOf&#32;on&#32;the&#32;ontology&#32;terms|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-93)|Identifier|`subpropertyof-class`|
|[Section top](#pass-outcome-number-93)|Title|No&#32;subproperty&#32;of&#32;class|
|[Section top](#pass-outcome-number-93)|Description|No&#32;ontology&#32;term&#32;is&#32;a&#32;subproperty&#32;of&#32;a&#32;class|

***
### Pass Outcome number 94

[Jump to summary definition](#summary-Pass-94)	|	[Previous Pass outcome](#pass-outcome-number-93)	|	[Next Pass outcome](#pass-outcome-number-95)

:white_check_mark:Pass outcome
#### Subject detail
|Name|module-ontology|
|----|----|
|Title|Standalone&#32;module&#32;core&#92;ontology.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- https://gitlab.com/coswot/coswot-acimov/blob/HEAD/core/ontology.ttl|

#### Criterion detail
|Identifier|[term-referencing](https://ns.inria.fr/olivaw#term-referencing)|
|----|----|
|Title|Term&#32;referencing&#32;test|
|Description|A&#32;test&#32;case&#32;from&#32;the&#32;Best&#32;Practices&#32;tests&#32;checking&#32;if&#32;each&#32;term&#32;of&#32;the&#32;test&#32;subject&#32;is&#32;referenced&#32;to&#32;a&#32;module&#32;through&#32;a&#32;rdfs:isDefinedBy&#32;property.|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-94)|Identifier|`no-reference-module`|
|[Section top](#pass-outcome-number-94)|Title|Any&#32;term&#32;is&#32;referenced|
|[Section top](#pass-outcome-number-94)|Description|Each&#32;term&#32;of&#32;the&#32;test&#32;subject&#32;is&#32;linked&#32;to&#32;a&#32;module&#32;by&#32;a&#32;rdfs:isDefinedBy&#32;property|

***
### Pass Outcome number 95

[Jump to summary definition](#summary-Pass-95)	|	[Previous Pass outcome](#pass-outcome-number-94)	|	[Next Pass outcome](#pass-outcome-number-96)

:white_check_mark:Pass outcome
#### Subject detail
|Name|module-ontology|
|----|----|
|Title|Standalone&#32;module&#32;core&#92;ontology.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- https://gitlab.com/coswot/coswot-acimov/blob/HEAD/core/ontology.ttl|

#### Criterion detail
|Identifier|[terms-differenciation](https://ns.inria.fr/olivaw#terms-differenciation)|
|----|----|
|Title|Terms&#32;differenciation&#32;test|
|Description|A&#32;test&#32;case&#32;from&#32;the&#32;Best&#32;Practices&#32;tests&#32;checking&#32;if&#32;all&#32;the&#32;terms&#32;are&#32;different&#32;enough&#32;from&#32;each&#32;other&#32;according&#32;to&#32;the&#32;Levenshtein&#32;distance&#32;metric.|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-95)|Identifier|`too-close-terms`|
|[Section top](#pass-outcome-number-95)|Title|Terms&#32;differenciated&#32;enough|
|[Section top](#pass-outcome-number-95)|Description|All&#32;the&#32;terms&#32;have&#32;have&#32;a&#32;satisfying&#32;Levenshtein&#32;distance&#32;from&#32;each&#32;other&#32;term.|

***
### Pass Outcome number 96

[Jump to summary definition](#summary-Pass-96)	|	[Previous Pass outcome](#pass-outcome-number-95)	|	[Next Pass outcome](#pass-outcome-number-97)

:white_check_mark:Pass outcome
#### Subject detail
|Name|module-observations-ontology|
|----|----|
|Title|Standalone&#32;module&#32;core&#92;observations&#92;ontology.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- https://gitlab.com/coswot/coswot-acimov/blob/HEAD/core/observations/ontology.ttl|

#### Criterion detail
|Identifier|[domain-and-range-referencing](https://ns.inria.fr/olivaw#domain-and-range-referencing)|
|----|----|
|Title|Domain&#32;and&#32;range&#32;referencing&#32;test|
|Description|A&#32;test&#32;case&#32;from&#32;the&#32;Best&#32;Practices&#32;tests&#32;checking&#32;if&#32;all&#32;the&#32;ranges&#32;and&#32;domains&#32;from&#32;the&#32;test&#32;subject&#32;point&#32;to&#32;terms&#32;that&#32;are&#32;defined&#32;in&#32;the&#32;vocabulary.|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-96)|Identifier|`domain-out-of-vocabulary`|
|[Section top](#pass-outcome-number-96)|Title|Domains&#32;properly&#32;defined|
|[Section top](#pass-outcome-number-96)|Description|Each&#32;rdfs:domain&#32;is&#32;defined&#32;within&#32;the&#32;fragment|

***
### Pass Outcome number 97

[Jump to summary definition](#summary-Pass-97)	|	[Previous Pass outcome](#pass-outcome-number-96)	|	[Next Pass outcome](#pass-outcome-number-98)

:white_check_mark:Pass outcome
#### Subject detail
|Name|module-observations-ontology|
|----|----|
|Title|Standalone&#32;module&#32;core&#92;observations&#92;ontology.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- https://gitlab.com/coswot/coswot-acimov/blob/HEAD/core/observations/ontology.ttl|

#### Criterion detail
|Identifier|[domain-and-range-referencing](https://ns.inria.fr/olivaw#domain-and-range-referencing)|
|----|----|
|Title|Domain&#32;and&#32;range&#32;referencing&#32;test|
|Description|A&#32;test&#32;case&#32;from&#32;the&#32;Best&#32;Practices&#32;tests&#32;checking&#32;if&#32;all&#32;the&#32;ranges&#32;and&#32;domains&#32;from&#32;the&#32;test&#32;subject&#32;point&#32;to&#32;terms&#32;that&#32;are&#32;defined&#32;in&#32;the&#32;vocabulary.|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-97)|Identifier|`range-out-of-vocabulary`|
|[Section top](#pass-outcome-number-97)|Title|Ranges&#32;properly&#32;defined|
|[Section top](#pass-outcome-number-97)|Description|Each&#32;rdfs:range&#32;is&#32;defined&#32;within&#32;the&#32;fragment|

***
### Pass Outcome number 98

[Jump to summary definition](#summary-Pass-98)	|	[Previous Pass outcome](#pass-outcome-number-97)	|	[Next Pass outcome](#pass-outcome-number-99)

:white_check_mark:Pass outcome
#### Subject detail
|Name|module-observations-ontology|
|----|----|
|Title|Standalone&#32;module&#32;core&#92;observations&#92;ontology.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- https://gitlab.com/coswot/coswot-acimov/blob/HEAD/core/observations/ontology.ttl|

#### Criterion detail
|Identifier|[labeled-terms](https://ns.inria.fr/olivaw#labeled-terms)|
|----|----|
|Title|Term&#32;labeling&#32;test|
|Description|A&#32;test&#32;case&#32;from&#32;the&#32;Best&#32;Practices&#32;tests&#32;checking&#32;if&#32;all&#32;the&#32;terms&#32;of&#32;the&#32;subject&#32;have&#32;a&#32;rdfs:label&#32;property&#32;pointing&#32;to&#32;a&#32;literal&#32;in&#32;English|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-98)|Identifier|`not-labeled-term`|
|[Section top](#pass-outcome-number-98)|Title|All&#32;terms&#32;labeled|
|[Section top](#pass-outcome-number-98)|Description|All&#32;the&#32;terms&#32;defined&#32;in&#32;the&#32;subject&#32;have&#32;a&#32;rdfs:label&#32;in&#32;English|

***
### Pass Outcome number 99

[Jump to summary definition](#summary-Pass-99)	|	[Previous Pass outcome](#pass-outcome-number-98)	|	[Next Pass outcome](#pass-outcome-number-100)

:white_check_mark:Pass outcome
#### Subject detail
|Name|module-observations-ontology|
|----|----|
|Title|Standalone&#32;module&#32;core&#92;observations&#92;ontology.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- https://gitlab.com/coswot/coswot-acimov/blob/HEAD/core/observations/ontology.ttl|

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
|Name|module-observations-ontology|
|----|----|
|Title|Standalone&#32;module&#32;core&#92;observations&#92;ontology.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- https://gitlab.com/coswot/coswot-acimov/blob/HEAD/core/observations/ontology.ttl|

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
|Name|module-observations-ontology|
|----|----|
|Title|Standalone&#32;module&#32;core&#92;observations&#92;ontology.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- https://gitlab.com/coswot/coswot-acimov/blob/HEAD/core/observations/ontology.ttl|

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
|Name|module-observations-ontology|
|----|----|
|Title|Standalone&#32;module&#32;core&#92;observations&#92;ontology.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- https://gitlab.com/coswot/coswot-acimov/blob/HEAD/core/observations/ontology.ttl|

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
|Name|module-observations-ontology|
|----|----|
|Title|Standalone&#32;module&#32;core&#92;observations&#92;ontology.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- https://gitlab.com/coswot/coswot-acimov/blob/HEAD/core/observations/ontology.ttl|

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
|Name|module-observations-ontology|
|----|----|
|Title|Standalone&#32;module&#32;core&#92;observations&#92;ontology.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- https://gitlab.com/coswot/coswot-acimov/blob/HEAD/core/observations/ontology.ttl|

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
|Name|module-observations-ontology|
|----|----|
|Title|Standalone&#32;module&#32;core&#92;observations&#92;ontology.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- https://gitlab.com/coswot/coswot-acimov/blob/HEAD/core/observations/ontology.ttl|

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
|Name|module-functions-commands-ontology|
|----|----|
|Title|Standalone&#32;module&#32;core&#92;functions&lowbar;commands&#92;ontology.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- https://gitlab.com/coswot/coswot-acimov/blob/HEAD/core/functions_commands/ontology.ttl|

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
|Name|module-functions-commands-ontology|
|----|----|
|Title|Standalone&#32;module&#32;core&#92;functions&lowbar;commands&#92;ontology.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- https://gitlab.com/coswot/coswot-acimov/blob/HEAD/core/functions_commands/ontology.ttl|

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
|Name|module-functions-commands-ontology|
|----|----|
|Title|Standalone&#32;module&#32;core&#92;functions&lowbar;commands&#92;ontology.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- https://gitlab.com/coswot/coswot-acimov/blob/HEAD/core/functions_commands/ontology.ttl|

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
|Name|module-functions-commands-ontology|
|----|----|
|Title|Standalone&#32;module&#32;core&#92;functions&lowbar;commands&#92;ontology.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- https://gitlab.com/coswot/coswot-acimov/blob/HEAD/core/functions_commands/ontology.ttl|

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
|Name|module-functions-commands-ontology|
|----|----|
|Title|Standalone&#32;module&#32;core&#92;functions&lowbar;commands&#92;ontology.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- https://gitlab.com/coswot/coswot-acimov/blob/HEAD/core/functions_commands/ontology.ttl|

#### Criterion detail
|Identifier|[proper-extension-predicate](https://ns.inria.fr/olivaw#proper-extension-predicate)|
|----|----|
|Title|Predicate&#32;extension&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;test&#32;the&#32;proper&#32;use&#32;of&#32;predicates&#32;rdfs:subClassOf&#32;and&#32;rdfs:subPropertyOf&#32;on&#32;the&#32;ontology&#32;terms|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-110)|Identifier|`class-subpropertyof`|
|[Section top](#pass-outcome-number-110)|Title|No&#32;class&#32;subproperty|
|[Section top](#pass-outcome-number-110)|Description|No&#32;ontology&#32;class&#32;is&#32;a&#32;subproperty|

***
### Pass Outcome number 111

[Jump to summary definition](#summary-Pass-111)	|	[Previous Pass outcome](#pass-outcome-number-110)	|	[Next Pass outcome](#pass-outcome-number-112)

:white_check_mark:Pass outcome
#### Subject detail
|Name|module-functions-commands-ontology|
|----|----|
|Title|Standalone&#32;module&#32;core&#92;functions&lowbar;commands&#92;ontology.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- https://gitlab.com/coswot/coswot-acimov/blob/HEAD/core/functions_commands/ontology.ttl|

#### Criterion detail
|Identifier|[proper-extension-predicate](https://ns.inria.fr/olivaw#proper-extension-predicate)|
|----|----|
|Title|Predicate&#32;extension&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;test&#32;the&#32;proper&#32;use&#32;of&#32;predicates&#32;rdfs:subClassOf&#32;and&#32;rdfs:subPropertyOf&#32;on&#32;the&#32;ontology&#32;terms|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-111)|Identifier|`property-subclassof`|
|[Section top](#pass-outcome-number-111)|Title|No&#32;property&#32;subclass|
|[Section top](#pass-outcome-number-111)|Description|No&#32;ontology&#32;property&#32;is&#32;a&#32;subclass|

***
### Pass Outcome number 112

[Jump to summary definition](#summary-Pass-112)	|	[Previous Pass outcome](#pass-outcome-number-111)	|	[Next Pass outcome](#pass-outcome-number-113)

:white_check_mark:Pass outcome
#### Subject detail
|Name|module-functions-commands-ontology|
|----|----|
|Title|Standalone&#32;module&#32;core&#92;functions&lowbar;commands&#92;ontology.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- https://gitlab.com/coswot/coswot-acimov/blob/HEAD/core/functions_commands/ontology.ttl|

#### Criterion detail
|Identifier|[proper-extension-predicate](https://ns.inria.fr/olivaw#proper-extension-predicate)|
|----|----|
|Title|Predicate&#32;extension&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;test&#32;the&#32;proper&#32;use&#32;of&#32;predicates&#32;rdfs:subClassOf&#32;and&#32;rdfs:subPropertyOf&#32;on&#32;the&#32;ontology&#32;terms|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-112)|Identifier|`subclassof-property`|
|[Section top](#pass-outcome-number-112)|Title|No&#32;subclass&#32;of&#32;property|
|[Section top](#pass-outcome-number-112)|Description|No&#32;ontology&#32;term&#32;is&#32;a&#32;subclass&#32;of&#32;a&#32;property|

***
### Pass Outcome number 113

[Jump to summary definition](#summary-Pass-113)	|	[Previous Pass outcome](#pass-outcome-number-112)	|	[Next Pass outcome](#pass-outcome-number-114)

:white_check_mark:Pass outcome
#### Subject detail
|Name|module-functions-commands-ontology|
|----|----|
|Title|Standalone&#32;module&#32;core&#92;functions&lowbar;commands&#92;ontology.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- https://gitlab.com/coswot/coswot-acimov/blob/HEAD/core/functions_commands/ontology.ttl|

#### Criterion detail
|Identifier|[proper-extension-predicate](https://ns.inria.fr/olivaw#proper-extension-predicate)|
|----|----|
|Title|Predicate&#32;extension&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;test&#32;the&#32;proper&#32;use&#32;of&#32;predicates&#32;rdfs:subClassOf&#32;and&#32;rdfs:subPropertyOf&#32;on&#32;the&#32;ontology&#32;terms|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-113)|Identifier|`subpropertyof-class`|
|[Section top](#pass-outcome-number-113)|Title|No&#32;subproperty&#32;of&#32;class|
|[Section top](#pass-outcome-number-113)|Description|No&#32;ontology&#32;term&#32;is&#32;a&#32;subproperty&#32;of&#32;a&#32;class|

***
### Pass Outcome number 114

[Jump to summary definition](#summary-Pass-114)	|	[Previous Pass outcome](#pass-outcome-number-113)	|	[Next Pass outcome](#pass-outcome-number-115)

:white_check_mark:Pass outcome
#### Subject detail
|Name|module-functions-commands-ontology|
|----|----|
|Title|Standalone&#32;module&#32;core&#92;functions&lowbar;commands&#92;ontology.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- https://gitlab.com/coswot/coswot-acimov/blob/HEAD/core/functions_commands/ontology.ttl|

#### Criterion detail
|Identifier|[terms-differenciation](https://ns.inria.fr/olivaw#terms-differenciation)|
|----|----|
|Title|Terms&#32;differenciation&#32;test|
|Description|A&#32;test&#32;case&#32;from&#32;the&#32;Best&#32;Practices&#32;tests&#32;checking&#32;if&#32;all&#32;the&#32;terms&#32;are&#32;different&#32;enough&#32;from&#32;each&#32;other&#32;according&#32;to&#32;the&#32;Levenshtein&#32;distance&#32;metric.|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-114)|Identifier|`too-close-terms`|
|[Section top](#pass-outcome-number-114)|Title|Terms&#32;differenciated&#32;enough|
|[Section top](#pass-outcome-number-114)|Description|All&#32;the&#32;terms&#32;have&#32;have&#32;a&#32;satisfying&#32;Levenshtein&#32;distance&#32;from&#32;each&#32;other&#32;term.|

***
### Pass Outcome number 115

[Jump to summary definition](#summary-Pass-115)	|	[Previous Pass outcome](#pass-outcome-number-114)	|	[Next Pass outcome](#pass-outcome-number-116)

:white_check_mark:Pass outcome
#### Subject detail
|Name|module-features-ontology-catalogs|
|----|----|
|Title|Standalone&#32;module&#32;core&#92;features&#92;ontology.catalogs.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- https://gitlab.com/coswot/coswot-acimov/blob/HEAD/core/features/ontology.catalogs.ttl|

#### Criterion detail
|Identifier|[domain-and-range-referencing](https://ns.inria.fr/olivaw#domain-and-range-referencing)|
|----|----|
|Title|Domain&#32;and&#32;range&#32;referencing&#32;test|
|Description|A&#32;test&#32;case&#32;from&#32;the&#32;Best&#32;Practices&#32;tests&#32;checking&#32;if&#32;all&#32;the&#32;ranges&#32;and&#32;domains&#32;from&#32;the&#32;test&#32;subject&#32;point&#32;to&#32;terms&#32;that&#32;are&#32;defined&#32;in&#32;the&#32;vocabulary.|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-115)|Identifier|`domain-out-of-vocabulary`|
|[Section top](#pass-outcome-number-115)|Title|Domains&#32;properly&#32;defined|
|[Section top](#pass-outcome-number-115)|Description|Each&#32;rdfs:domain&#32;is&#32;defined&#32;within&#32;the&#32;fragment|

***
### Pass Outcome number 116

[Jump to summary definition](#summary-Pass-116)	|	[Previous Pass outcome](#pass-outcome-number-115)	|	[Next Pass outcome](#pass-outcome-number-117)

:white_check_mark:Pass outcome
#### Subject detail
|Name|module-features-ontology-catalogs|
|----|----|
|Title|Standalone&#32;module&#32;core&#92;features&#92;ontology.catalogs.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- https://gitlab.com/coswot/coswot-acimov/blob/HEAD/core/features/ontology.catalogs.ttl|

#### Criterion detail
|Identifier|[domain-and-range-referencing](https://ns.inria.fr/olivaw#domain-and-range-referencing)|
|----|----|
|Title|Domain&#32;and&#32;range&#32;referencing&#32;test|
|Description|A&#32;test&#32;case&#32;from&#32;the&#32;Best&#32;Practices&#32;tests&#32;checking&#32;if&#32;all&#32;the&#32;ranges&#32;and&#32;domains&#32;from&#32;the&#32;test&#32;subject&#32;point&#32;to&#32;terms&#32;that&#32;are&#32;defined&#32;in&#32;the&#32;vocabulary.|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-116)|Identifier|`range-out-of-vocabulary`|
|[Section top](#pass-outcome-number-116)|Title|Ranges&#32;properly&#32;defined|
|[Section top](#pass-outcome-number-116)|Description|Each&#32;rdfs:range&#32;is&#32;defined&#32;within&#32;the&#32;fragment|

***
### Pass Outcome number 117

[Jump to summary definition](#summary-Pass-117)	|	[Previous Pass outcome](#pass-outcome-number-116)	|	[Next Pass outcome](#pass-outcome-number-118)

:white_check_mark:Pass outcome
#### Subject detail
|Name|module-features-ontology-catalogs|
|----|----|
|Title|Standalone&#32;module&#32;core&#92;features&#92;ontology.catalogs.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- https://gitlab.com/coswot/coswot-acimov/blob/HEAD/core/features/ontology.catalogs.ttl|

#### Criterion detail
|Identifier|[labeled-terms](https://ns.inria.fr/olivaw#labeled-terms)|
|----|----|
|Title|Term&#32;labeling&#32;test|
|Description|A&#32;test&#32;case&#32;from&#32;the&#32;Best&#32;Practices&#32;tests&#32;checking&#32;if&#32;all&#32;the&#32;terms&#32;of&#32;the&#32;subject&#32;have&#32;a&#32;rdfs:label&#32;property&#32;pointing&#32;to&#32;a&#32;literal&#32;in&#32;English|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-117)|Identifier|`not-labeled-term`|
|[Section top](#pass-outcome-number-117)|Title|All&#32;terms&#32;labeled|
|[Section top](#pass-outcome-number-117)|Description|All&#32;the&#32;terms&#32;defined&#32;in&#32;the&#32;subject&#32;have&#32;a&#32;rdfs:label&#32;in&#32;English|

***
### Pass Outcome number 118

[Jump to summary definition](#summary-Pass-118)	|	[Previous Pass outcome](#pass-outcome-number-117)	|	[Next Pass outcome](#pass-outcome-number-119)

:white_check_mark:Pass outcome
#### Subject detail
|Name|module-features-ontology-catalogs|
|----|----|
|Title|Standalone&#32;module&#32;core&#92;features&#92;ontology.catalogs.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- https://gitlab.com/coswot/coswot-acimov/blob/HEAD/core/features/ontology.catalogs.ttl|

#### Criterion detail
|Identifier|[owl-rl-constraint](https://ns.inria.fr/olivaw#owl-rl-constraint)|
|----|----|
|Title|OWL&#32;RL&#32;Constraint&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;check&#32;wether&#32;the&#32;test&#32;subject&#32;is&#32;syntaxically&#32;correct&#32;or&#32;not.|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-118)|Identifier|`owl-rl-constraint-violation`|
|[Section top](#pass-outcome-number-118)|Title|OWL&#32;RL&#32;consistent|
|[Section top](#pass-outcome-number-118)|Description|The&#32;provided&#32;graph&#32;is&#32;consistent&#32;for&#32;any&#32;OWL&#32;RL&#32;constraint|

***
### Pass Outcome number 119

[Jump to summary definition](#summary-Pass-119)	|	[Previous Pass outcome](#pass-outcome-number-118)	|	[Next Pass outcome](#pass-outcome-number-120)

:white_check_mark:Pass outcome
#### Subject detail
|Name|module-features-ontology-catalogs|
|----|----|
|Title|Standalone&#32;module&#32;core&#92;features&#92;ontology.catalogs.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- https://gitlab.com/coswot/coswot-acimov/blob/HEAD/core/features/ontology.catalogs.ttl|

#### Criterion detail
|Identifier|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|
|----|----|
|Title|Profile&#32;compatibility&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;check&#32;whether&#32;the&#32;test&#32;subject&#32;is&#32;compatible&#32;with&#32;a&#32;profile&#32;or&#32;not,&#32;and&#32;if&#32;it&#32;is&#32;not,&#32;why.|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-119)|Identifier|`owl-rl-profile-error`|
|[Section top](#pass-outcome-number-119)|Title|OWL&#32;RL&#32;Profile&#32;compatible|
|[Section top](#pass-outcome-number-119)|Description|The&#32;subject&#32;is&#32;included&#32;in&#32;the&#32;OWL&#32;RL&#32;sublanguage|

***
### Pass Outcome number 120

[Jump to summary definition](#summary-Pass-120)	|	[Previous Pass outcome](#pass-outcome-number-119)	|	[Next Pass outcome](#pass-outcome-number-121)

:white_check_mark:Pass outcome
#### Subject detail
|Name|module-features-ontology-catalogs|
|----|----|
|Title|Standalone&#32;module&#32;core&#92;features&#92;ontology.catalogs.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- https://gitlab.com/coswot/coswot-acimov/blob/HEAD/core/features/ontology.catalogs.ttl|

#### Criterion detail
|Identifier|[proper-extension-predicate](https://ns.inria.fr/olivaw#proper-extension-predicate)|
|----|----|
|Title|Predicate&#32;extension&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;test&#32;the&#32;proper&#32;use&#32;of&#32;predicates&#32;rdfs:subClassOf&#32;and&#32;rdfs:subPropertyOf&#32;on&#32;the&#32;ontology&#32;terms|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-120)|Identifier|`class-subpropertyof`|
|[Section top](#pass-outcome-number-120)|Title|No&#32;class&#32;subproperty|
|[Section top](#pass-outcome-number-120)|Description|No&#32;ontology&#32;class&#32;is&#32;a&#32;subproperty|

***
### Pass Outcome number 121

[Jump to summary definition](#summary-Pass-121)	|	[Previous Pass outcome](#pass-outcome-number-120)	|	[Next Pass outcome](#pass-outcome-number-122)

:white_check_mark:Pass outcome
#### Subject detail
|Name|module-features-ontology-catalogs|
|----|----|
|Title|Standalone&#32;module&#32;core&#92;features&#92;ontology.catalogs.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- https://gitlab.com/coswot/coswot-acimov/blob/HEAD/core/features/ontology.catalogs.ttl|

#### Criterion detail
|Identifier|[proper-extension-predicate](https://ns.inria.fr/olivaw#proper-extension-predicate)|
|----|----|
|Title|Predicate&#32;extension&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;test&#32;the&#32;proper&#32;use&#32;of&#32;predicates&#32;rdfs:subClassOf&#32;and&#32;rdfs:subPropertyOf&#32;on&#32;the&#32;ontology&#32;terms|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-121)|Identifier|`property-subclassof`|
|[Section top](#pass-outcome-number-121)|Title|No&#32;property&#32;subclass|
|[Section top](#pass-outcome-number-121)|Description|No&#32;ontology&#32;property&#32;is&#32;a&#32;subclass|

***
### Pass Outcome number 122

[Jump to summary definition](#summary-Pass-122)	|	[Previous Pass outcome](#pass-outcome-number-121)	|	[Next Pass outcome](#pass-outcome-number-123)

:white_check_mark:Pass outcome
#### Subject detail
|Name|module-features-ontology-catalogs|
|----|----|
|Title|Standalone&#32;module&#32;core&#92;features&#92;ontology.catalogs.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- https://gitlab.com/coswot/coswot-acimov/blob/HEAD/core/features/ontology.catalogs.ttl|

#### Criterion detail
|Identifier|[proper-extension-predicate](https://ns.inria.fr/olivaw#proper-extension-predicate)|
|----|----|
|Title|Predicate&#32;extension&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;test&#32;the&#32;proper&#32;use&#32;of&#32;predicates&#32;rdfs:subClassOf&#32;and&#32;rdfs:subPropertyOf&#32;on&#32;the&#32;ontology&#32;terms|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-122)|Identifier|`subclassof-property`|
|[Section top](#pass-outcome-number-122)|Title|No&#32;subclass&#32;of&#32;property|
|[Section top](#pass-outcome-number-122)|Description|No&#32;ontology&#32;term&#32;is&#32;a&#32;subclass&#32;of&#32;a&#32;property|

***
### Pass Outcome number 123

[Jump to summary definition](#summary-Pass-123)	|	[Previous Pass outcome](#pass-outcome-number-122)	|	[Next Pass outcome](#pass-outcome-number-124)

:white_check_mark:Pass outcome
#### Subject detail
|Name|module-features-ontology-catalogs|
|----|----|
|Title|Standalone&#32;module&#32;core&#92;features&#92;ontology.catalogs.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- https://gitlab.com/coswot/coswot-acimov/blob/HEAD/core/features/ontology.catalogs.ttl|

#### Criterion detail
|Identifier|[proper-extension-predicate](https://ns.inria.fr/olivaw#proper-extension-predicate)|
|----|----|
|Title|Predicate&#32;extension&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;test&#32;the&#32;proper&#32;use&#32;of&#32;predicates&#32;rdfs:subClassOf&#32;and&#32;rdfs:subPropertyOf&#32;on&#32;the&#32;ontology&#32;terms|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-123)|Identifier|`subpropertyof-class`|
|[Section top](#pass-outcome-number-123)|Title|No&#32;subproperty&#32;of&#32;class|
|[Section top](#pass-outcome-number-123)|Description|No&#32;ontology&#32;term&#32;is&#32;a&#32;subproperty&#32;of&#32;a&#32;class|

***
### Pass Outcome number 124

[Jump to summary definition](#summary-Pass-124)	|	[Previous Pass outcome](#pass-outcome-number-123)	|	[Next Pass outcome](#pass-outcome-number-125)

:white_check_mark:Pass outcome
#### Subject detail
|Name|module-features-ontology-catalogs|
|----|----|
|Title|Standalone&#32;module&#32;core&#92;features&#92;ontology.catalogs.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- https://gitlab.com/coswot/coswot-acimov/blob/HEAD/core/features/ontology.catalogs.ttl|

#### Criterion detail
|Identifier|[term-referencing](https://ns.inria.fr/olivaw#term-referencing)|
|----|----|
|Title|Term&#32;referencing&#32;test|
|Description|A&#32;test&#32;case&#32;from&#32;the&#32;Best&#32;Practices&#32;tests&#32;checking&#32;if&#32;each&#32;term&#32;of&#32;the&#32;test&#32;subject&#32;is&#32;referenced&#32;to&#32;a&#32;module&#32;through&#32;a&#32;rdfs:isDefinedBy&#32;property.|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-124)|Identifier|`no-reference-module`|
|[Section top](#pass-outcome-number-124)|Title|Any&#32;term&#32;is&#32;referenced|
|[Section top](#pass-outcome-number-124)|Description|Each&#32;term&#32;of&#32;the&#32;test&#32;subject&#32;is&#32;linked&#32;to&#32;a&#32;module&#32;by&#32;a&#32;rdfs:isDefinedBy&#32;property|

***
### Pass Outcome number 125

[Jump to summary definition](#summary-Pass-125)	|	[Previous Pass outcome](#pass-outcome-number-124)	|	[Next Pass outcome](#pass-outcome-number-126)

:white_check_mark:Pass outcome
#### Subject detail
|Name|module-features-ontology-catalogs|
|----|----|
|Title|Standalone&#32;module&#32;core&#92;features&#92;ontology.catalogs.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- https://gitlab.com/coswot/coswot-acimov/blob/HEAD/core/features/ontology.catalogs.ttl|

#### Criterion detail
|Identifier|[terms-differenciation](https://ns.inria.fr/olivaw#terms-differenciation)|
|----|----|
|Title|Terms&#32;differenciation&#32;test|
|Description|A&#32;test&#32;case&#32;from&#32;the&#32;Best&#32;Practices&#32;tests&#32;checking&#32;if&#32;all&#32;the&#32;terms&#32;are&#32;different&#32;enough&#32;from&#32;each&#32;other&#32;according&#32;to&#32;the&#32;Levenshtein&#32;distance&#32;metric.|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-125)|Identifier|`too-close-terms`|
|[Section top](#pass-outcome-number-125)|Title|Terms&#32;differenciated&#32;enough|
|[Section top](#pass-outcome-number-125)|Description|All&#32;the&#32;terms&#32;have&#32;have&#32;a&#32;satisfying&#32;Levenshtein&#32;distance&#32;from&#32;each&#32;other&#32;term.|

***
### Pass Outcome number 126

[Jump to summary definition](#summary-Pass-126)	|	[Previous Pass outcome](#pass-outcome-number-125)	|	[Next Pass outcome](#pass-outcome-number-127)

:white_check_mark:Pass outcome
#### Subject detail
|Name|module-features-ontology|
|----|----|
|Title|Standalone&#32;module&#32;core&#92;features&#92;ontology.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- https://gitlab.com/coswot/coswot-acimov/blob/HEAD/core/features/ontology.ttl|

#### Criterion detail
|Identifier|[domain-and-range-referencing](https://ns.inria.fr/olivaw#domain-and-range-referencing)|
|----|----|
|Title|Domain&#32;and&#32;range&#32;referencing&#32;test|
|Description|A&#32;test&#32;case&#32;from&#32;the&#32;Best&#32;Practices&#32;tests&#32;checking&#32;if&#32;all&#32;the&#32;ranges&#32;and&#32;domains&#32;from&#32;the&#32;test&#32;subject&#32;point&#32;to&#32;terms&#32;that&#32;are&#32;defined&#32;in&#32;the&#32;vocabulary.|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-126)|Identifier|`domain-out-of-vocabulary`|
|[Section top](#pass-outcome-number-126)|Title|Domains&#32;properly&#32;defined|
|[Section top](#pass-outcome-number-126)|Description|Each&#32;rdfs:domain&#32;is&#32;defined&#32;within&#32;the&#32;fragment|

***
### Pass Outcome number 127

[Jump to summary definition](#summary-Pass-127)	|	[Previous Pass outcome](#pass-outcome-number-126)	|	[Next Pass outcome](#pass-outcome-number-128)

:white_check_mark:Pass outcome
#### Subject detail
|Name|module-features-ontology|
|----|----|
|Title|Standalone&#32;module&#32;core&#92;features&#92;ontology.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- https://gitlab.com/coswot/coswot-acimov/blob/HEAD/core/features/ontology.ttl|

#### Criterion detail
|Identifier|[domain-and-range-referencing](https://ns.inria.fr/olivaw#domain-and-range-referencing)|
|----|----|
|Title|Domain&#32;and&#32;range&#32;referencing&#32;test|
|Description|A&#32;test&#32;case&#32;from&#32;the&#32;Best&#32;Practices&#32;tests&#32;checking&#32;if&#32;all&#32;the&#32;ranges&#32;and&#32;domains&#32;from&#32;the&#32;test&#32;subject&#32;point&#32;to&#32;terms&#32;that&#32;are&#32;defined&#32;in&#32;the&#32;vocabulary.|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-127)|Identifier|`range-out-of-vocabulary`|
|[Section top](#pass-outcome-number-127)|Title|Ranges&#32;properly&#32;defined|
|[Section top](#pass-outcome-number-127)|Description|Each&#32;rdfs:range&#32;is&#32;defined&#32;within&#32;the&#32;fragment|

***
### Pass Outcome number 128

[Jump to summary definition](#summary-Pass-128)	|	[Previous Pass outcome](#pass-outcome-number-127)	|	[Next Pass outcome](#pass-outcome-number-129)

:white_check_mark:Pass outcome
#### Subject detail
|Name|module-features-ontology|
|----|----|
|Title|Standalone&#32;module&#32;core&#92;features&#92;ontology.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- https://gitlab.com/coswot/coswot-acimov/blob/HEAD/core/features/ontology.ttl|

#### Criterion detail
|Identifier|[labeled-terms](https://ns.inria.fr/olivaw#labeled-terms)|
|----|----|
|Title|Term&#32;labeling&#32;test|
|Description|A&#32;test&#32;case&#32;from&#32;the&#32;Best&#32;Practices&#32;tests&#32;checking&#32;if&#32;all&#32;the&#32;terms&#32;of&#32;the&#32;subject&#32;have&#32;a&#32;rdfs:label&#32;property&#32;pointing&#32;to&#32;a&#32;literal&#32;in&#32;English|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-128)|Identifier|`not-labeled-term`|
|[Section top](#pass-outcome-number-128)|Title|All&#32;terms&#32;labeled|
|[Section top](#pass-outcome-number-128)|Description|All&#32;the&#32;terms&#32;defined&#32;in&#32;the&#32;subject&#32;have&#32;a&#32;rdfs:label&#32;in&#32;English|

***
### Pass Outcome number 129

[Jump to summary definition](#summary-Pass-129)	|	[Previous Pass outcome](#pass-outcome-number-128)	|	[Next Pass outcome](#pass-outcome-number-130)

:white_check_mark:Pass outcome
#### Subject detail
|Name|module-features-ontology|
|----|----|
|Title|Standalone&#32;module&#32;core&#92;features&#92;ontology.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- https://gitlab.com/coswot/coswot-acimov/blob/HEAD/core/features/ontology.ttl|

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
|Name|module-features-ontology|
|----|----|
|Title|Standalone&#32;module&#32;core&#92;features&#92;ontology.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- https://gitlab.com/coswot/coswot-acimov/blob/HEAD/core/features/ontology.ttl|

#### Criterion detail
|Identifier|[proper-extension-predicate](https://ns.inria.fr/olivaw#proper-extension-predicate)|
|----|----|
|Title|Predicate&#32;extension&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;test&#32;the&#32;proper&#32;use&#32;of&#32;predicates&#32;rdfs:subClassOf&#32;and&#32;rdfs:subPropertyOf&#32;on&#32;the&#32;ontology&#32;terms|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-130)|Identifier|`class-subpropertyof`|
|[Section top](#pass-outcome-number-130)|Title|No&#32;class&#32;subproperty|
|[Section top](#pass-outcome-number-130)|Description|No&#32;ontology&#32;class&#32;is&#32;a&#32;subproperty|

***
### Pass Outcome number 131

[Jump to summary definition](#summary-Pass-131)	|	[Previous Pass outcome](#pass-outcome-number-130)	|	[Next Pass outcome](#pass-outcome-number-132)

:white_check_mark:Pass outcome
#### Subject detail
|Name|module-features-ontology|
|----|----|
|Title|Standalone&#32;module&#32;core&#92;features&#92;ontology.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- https://gitlab.com/coswot/coswot-acimov/blob/HEAD/core/features/ontology.ttl|

#### Criterion detail
|Identifier|[proper-extension-predicate](https://ns.inria.fr/olivaw#proper-extension-predicate)|
|----|----|
|Title|Predicate&#32;extension&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;test&#32;the&#32;proper&#32;use&#32;of&#32;predicates&#32;rdfs:subClassOf&#32;and&#32;rdfs:subPropertyOf&#32;on&#32;the&#32;ontology&#32;terms|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-131)|Identifier|`property-subclassof`|
|[Section top](#pass-outcome-number-131)|Title|No&#32;property&#32;subclass|
|[Section top](#pass-outcome-number-131)|Description|No&#32;ontology&#32;property&#32;is&#32;a&#32;subclass|

***
### Pass Outcome number 132

[Jump to summary definition](#summary-Pass-132)	|	[Previous Pass outcome](#pass-outcome-number-131)	|	[Next Pass outcome](#pass-outcome-number-133)

:white_check_mark:Pass outcome
#### Subject detail
|Name|module-features-ontology|
|----|----|
|Title|Standalone&#32;module&#32;core&#92;features&#92;ontology.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- https://gitlab.com/coswot/coswot-acimov/blob/HEAD/core/features/ontology.ttl|

#### Criterion detail
|Identifier|[proper-extension-predicate](https://ns.inria.fr/olivaw#proper-extension-predicate)|
|----|----|
|Title|Predicate&#32;extension&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;test&#32;the&#32;proper&#32;use&#32;of&#32;predicates&#32;rdfs:subClassOf&#32;and&#32;rdfs:subPropertyOf&#32;on&#32;the&#32;ontology&#32;terms|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-132)|Identifier|`subclassof-property`|
|[Section top](#pass-outcome-number-132)|Title|No&#32;subclass&#32;of&#32;property|
|[Section top](#pass-outcome-number-132)|Description|No&#32;ontology&#32;term&#32;is&#32;a&#32;subclass&#32;of&#32;a&#32;property|

***
### Pass Outcome number 133

[Jump to summary definition](#summary-Pass-133)	|	[Previous Pass outcome](#pass-outcome-number-132)	|	[Next Pass outcome](#pass-outcome-number-134)

:white_check_mark:Pass outcome
#### Subject detail
|Name|module-features-ontology|
|----|----|
|Title|Standalone&#32;module&#32;core&#92;features&#92;ontology.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- https://gitlab.com/coswot/coswot-acimov/blob/HEAD/core/features/ontology.ttl|

#### Criterion detail
|Identifier|[proper-extension-predicate](https://ns.inria.fr/olivaw#proper-extension-predicate)|
|----|----|
|Title|Predicate&#32;extension&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;test&#32;the&#32;proper&#32;use&#32;of&#32;predicates&#32;rdfs:subClassOf&#32;and&#32;rdfs:subPropertyOf&#32;on&#32;the&#32;ontology&#32;terms|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-133)|Identifier|`subpropertyof-class`|
|[Section top](#pass-outcome-number-133)|Title|No&#32;subproperty&#32;of&#32;class|
|[Section top](#pass-outcome-number-133)|Description|No&#32;ontology&#32;term&#32;is&#32;a&#32;subproperty&#32;of&#32;a&#32;class|

***
### Pass Outcome number 134

[Jump to summary definition](#summary-Pass-134)	|	[Previous Pass outcome](#pass-outcome-number-133)	|	[Next Pass outcome](#pass-outcome-number-135)

:white_check_mark:Pass outcome
#### Subject detail
|Name|module-features-ontology|
|----|----|
|Title|Standalone&#32;module&#32;core&#92;features&#92;ontology.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- https://gitlab.com/coswot/coswot-acimov/blob/HEAD/core/features/ontology.ttl|

#### Criterion detail
|Identifier|[term-referencing](https://ns.inria.fr/olivaw#term-referencing)|
|----|----|
|Title|Term&#32;referencing&#32;test|
|Description|A&#32;test&#32;case&#32;from&#32;the&#32;Best&#32;Practices&#32;tests&#32;checking&#32;if&#32;each&#32;term&#32;of&#32;the&#32;test&#32;subject&#32;is&#32;referenced&#32;to&#32;a&#32;module&#32;through&#32;a&#32;rdfs:isDefinedBy&#32;property.|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-134)|Identifier|`no-reference-module`|
|[Section top](#pass-outcome-number-134)|Title|Any&#32;term&#32;is&#32;referenced|
|[Section top](#pass-outcome-number-134)|Description|Each&#32;term&#32;of&#32;the&#32;test&#32;subject&#32;is&#32;linked&#32;to&#32;a&#32;module&#32;by&#32;a&#32;rdfs:isDefinedBy&#32;property|

***
### Pass Outcome number 135

[Jump to summary definition](#summary-Pass-135)	|	[Previous Pass outcome](#pass-outcome-number-134)	|	[Next Pass outcome](#pass-outcome-number-136)

:white_check_mark:Pass outcome
#### Subject detail
|Name|module-features-ontology|
|----|----|
|Title|Standalone&#32;module&#32;core&#92;features&#92;ontology.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- https://gitlab.com/coswot/coswot-acimov/blob/HEAD/core/features/ontology.ttl|

#### Criterion detail
|Identifier|[terms-differenciation](https://ns.inria.fr/olivaw#terms-differenciation)|
|----|----|
|Title|Terms&#32;differenciation&#32;test|
|Description|A&#32;test&#32;case&#32;from&#32;the&#32;Best&#32;Practices&#32;tests&#32;checking&#32;if&#32;all&#32;the&#32;terms&#32;are&#32;different&#32;enough&#32;from&#32;each&#32;other&#32;according&#32;to&#32;the&#32;Levenshtein&#32;distance&#32;metric.|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-135)|Identifier|`too-close-terms`|
|[Section top](#pass-outcome-number-135)|Title|Terms&#32;differenciated&#32;enough|
|[Section top](#pass-outcome-number-135)|Description|All&#32;the&#32;terms&#32;have&#32;have&#32;a&#32;satisfying&#32;Levenshtein&#32;distance&#32;from&#32;each&#32;other&#32;term.|

***
### Pass Outcome number 136

[Jump to summary definition](#summary-Pass-136)	|	[Previous Pass outcome](#pass-outcome-number-135)	|	[Next Pass outcome](#pass-outcome-number-137)

:white_check_mark:Pass outcome
#### Subject detail
|Name|module-devices-ontology|
|----|----|
|Title|Standalone&#32;module&#32;core&#92;devices&#92;ontology.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- https://gitlab.com/coswot/coswot-acimov/blob/HEAD/core/devices/ontology.ttl|

#### Criterion detail
|Identifier|[domain-and-range-referencing](https://ns.inria.fr/olivaw#domain-and-range-referencing)|
|----|----|
|Title|Domain&#32;and&#32;range&#32;referencing&#32;test|
|Description|A&#32;test&#32;case&#32;from&#32;the&#32;Best&#32;Practices&#32;tests&#32;checking&#32;if&#32;all&#32;the&#32;ranges&#32;and&#32;domains&#32;from&#32;the&#32;test&#32;subject&#32;point&#32;to&#32;terms&#32;that&#32;are&#32;defined&#32;in&#32;the&#32;vocabulary.|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-136)|Identifier|`domain-out-of-vocabulary`|
|[Section top](#pass-outcome-number-136)|Title|Domains&#32;properly&#32;defined|
|[Section top](#pass-outcome-number-136)|Description|Each&#32;rdfs:domain&#32;is&#32;defined&#32;within&#32;the&#32;fragment|

***
### Pass Outcome number 137

[Jump to summary definition](#summary-Pass-137)	|	[Previous Pass outcome](#pass-outcome-number-136)	|	[Next Pass outcome](#pass-outcome-number-138)

:white_check_mark:Pass outcome
#### Subject detail
|Name|module-devices-ontology|
|----|----|
|Title|Standalone&#32;module&#32;core&#92;devices&#92;ontology.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- https://gitlab.com/coswot/coswot-acimov/blob/HEAD/core/devices/ontology.ttl|

#### Criterion detail
|Identifier|[domain-and-range-referencing](https://ns.inria.fr/olivaw#domain-and-range-referencing)|
|----|----|
|Title|Domain&#32;and&#32;range&#32;referencing&#32;test|
|Description|A&#32;test&#32;case&#32;from&#32;the&#32;Best&#32;Practices&#32;tests&#32;checking&#32;if&#32;all&#32;the&#32;ranges&#32;and&#32;domains&#32;from&#32;the&#32;test&#32;subject&#32;point&#32;to&#32;terms&#32;that&#32;are&#32;defined&#32;in&#32;the&#32;vocabulary.|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-137)|Identifier|`range-out-of-vocabulary`|
|[Section top](#pass-outcome-number-137)|Title|Ranges&#32;properly&#32;defined|
|[Section top](#pass-outcome-number-137)|Description|Each&#32;rdfs:range&#32;is&#32;defined&#32;within&#32;the&#32;fragment|

***
### Pass Outcome number 138

[Jump to summary definition](#summary-Pass-138)	|	[Previous Pass outcome](#pass-outcome-number-137)	|	[Next Pass outcome](#pass-outcome-number-139)

:white_check_mark:Pass outcome
#### Subject detail
|Name|module-devices-ontology|
|----|----|
|Title|Standalone&#32;module&#32;core&#92;devices&#92;ontology.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- https://gitlab.com/coswot/coswot-acimov/blob/HEAD/core/devices/ontology.ttl|

#### Criterion detail
|Identifier|[labeled-terms](https://ns.inria.fr/olivaw#labeled-terms)|
|----|----|
|Title|Term&#32;labeling&#32;test|
|Description|A&#32;test&#32;case&#32;from&#32;the&#32;Best&#32;Practices&#32;tests&#32;checking&#32;if&#32;all&#32;the&#32;terms&#32;of&#32;the&#32;subject&#32;have&#32;a&#32;rdfs:label&#32;property&#32;pointing&#32;to&#32;a&#32;literal&#32;in&#32;English|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-138)|Identifier|`not-labeled-term`|
|[Section top](#pass-outcome-number-138)|Title|All&#32;terms&#32;labeled|
|[Section top](#pass-outcome-number-138)|Description|All&#32;the&#32;terms&#32;defined&#32;in&#32;the&#32;subject&#32;have&#32;a&#32;rdfs:label&#32;in&#32;English|

***
### Pass Outcome number 139

[Jump to summary definition](#summary-Pass-139)	|	[Previous Pass outcome](#pass-outcome-number-138)	|	[Next Pass outcome](#pass-outcome-number-140)

:white_check_mark:Pass outcome
#### Subject detail
|Name|module-devices-ontology|
|----|----|
|Title|Standalone&#32;module&#32;core&#92;devices&#92;ontology.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- https://gitlab.com/coswot/coswot-acimov/blob/HEAD/core/devices/ontology.ttl|

#### Criterion detail
|Identifier|[owl-rl-constraint](https://ns.inria.fr/olivaw#owl-rl-constraint)|
|----|----|
|Title|OWL&#32;RL&#32;Constraint&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;check&#32;wether&#32;the&#32;test&#32;subject&#32;is&#32;syntaxically&#32;correct&#32;or&#32;not.|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-139)|Identifier|`owl-rl-constraint-violation`|
|[Section top](#pass-outcome-number-139)|Title|OWL&#32;RL&#32;consistent|
|[Section top](#pass-outcome-number-139)|Description|The&#32;provided&#32;graph&#32;is&#32;consistent&#32;for&#32;any&#32;OWL&#32;RL&#32;constraint|

***
### Pass Outcome number 140

[Jump to summary definition](#summary-Pass-140)	|	[Previous Pass outcome](#pass-outcome-number-139)	|	[Next Pass outcome](#pass-outcome-number-141)

:white_check_mark:Pass outcome
#### Subject detail
|Name|module-devices-ontology|
|----|----|
|Title|Standalone&#32;module&#32;core&#92;devices&#92;ontology.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- https://gitlab.com/coswot/coswot-acimov/blob/HEAD/core/devices/ontology.ttl|

#### Criterion detail
|Identifier|[proper-extension-predicate](https://ns.inria.fr/olivaw#proper-extension-predicate)|
|----|----|
|Title|Predicate&#32;extension&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;test&#32;the&#32;proper&#32;use&#32;of&#32;predicates&#32;rdfs:subClassOf&#32;and&#32;rdfs:subPropertyOf&#32;on&#32;the&#32;ontology&#32;terms|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-140)|Identifier|`class-subpropertyof`|
|[Section top](#pass-outcome-number-140)|Title|No&#32;class&#32;subproperty|
|[Section top](#pass-outcome-number-140)|Description|No&#32;ontology&#32;class&#32;is&#32;a&#32;subproperty|

***
### Pass Outcome number 141

[Jump to summary definition](#summary-Pass-141)	|	[Previous Pass outcome](#pass-outcome-number-140)	|	[Next Pass outcome](#pass-outcome-number-142)

:white_check_mark:Pass outcome
#### Subject detail
|Name|module-devices-ontology|
|----|----|
|Title|Standalone&#32;module&#32;core&#92;devices&#92;ontology.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- https://gitlab.com/coswot/coswot-acimov/blob/HEAD/core/devices/ontology.ttl|

#### Criterion detail
|Identifier|[proper-extension-predicate](https://ns.inria.fr/olivaw#proper-extension-predicate)|
|----|----|
|Title|Predicate&#32;extension&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;test&#32;the&#32;proper&#32;use&#32;of&#32;predicates&#32;rdfs:subClassOf&#32;and&#32;rdfs:subPropertyOf&#32;on&#32;the&#32;ontology&#32;terms|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-141)|Identifier|`property-subclassof`|
|[Section top](#pass-outcome-number-141)|Title|No&#32;property&#32;subclass|
|[Section top](#pass-outcome-number-141)|Description|No&#32;ontology&#32;property&#32;is&#32;a&#32;subclass|

***
### Pass Outcome number 142

[Jump to summary definition](#summary-Pass-142)	|	[Previous Pass outcome](#pass-outcome-number-141)	|	[Next Pass outcome](#pass-outcome-number-143)

:white_check_mark:Pass outcome
#### Subject detail
|Name|module-devices-ontology|
|----|----|
|Title|Standalone&#32;module&#32;core&#92;devices&#92;ontology.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- https://gitlab.com/coswot/coswot-acimov/blob/HEAD/core/devices/ontology.ttl|

#### Criterion detail
|Identifier|[proper-extension-predicate](https://ns.inria.fr/olivaw#proper-extension-predicate)|
|----|----|
|Title|Predicate&#32;extension&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;test&#32;the&#32;proper&#32;use&#32;of&#32;predicates&#32;rdfs:subClassOf&#32;and&#32;rdfs:subPropertyOf&#32;on&#32;the&#32;ontology&#32;terms|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-142)|Identifier|`subclassof-property`|
|[Section top](#pass-outcome-number-142)|Title|No&#32;subclass&#32;of&#32;property|
|[Section top](#pass-outcome-number-142)|Description|No&#32;ontology&#32;term&#32;is&#32;a&#32;subclass&#32;of&#32;a&#32;property|

***
### Pass Outcome number 143

[Jump to summary definition](#summary-Pass-143)	|	[Previous Pass outcome](#pass-outcome-number-142)	|	[Next Pass outcome](#pass-outcome-number-144)

:white_check_mark:Pass outcome
#### Subject detail
|Name|module-devices-ontology|
|----|----|
|Title|Standalone&#32;module&#32;core&#92;devices&#92;ontology.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- https://gitlab.com/coswot/coswot-acimov/blob/HEAD/core/devices/ontology.ttl|

#### Criterion detail
|Identifier|[proper-extension-predicate](https://ns.inria.fr/olivaw#proper-extension-predicate)|
|----|----|
|Title|Predicate&#32;extension&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;test&#32;the&#32;proper&#32;use&#32;of&#32;predicates&#32;rdfs:subClassOf&#32;and&#32;rdfs:subPropertyOf&#32;on&#32;the&#32;ontology&#32;terms|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-143)|Identifier|`subpropertyof-class`|
|[Section top](#pass-outcome-number-143)|Title|No&#32;subproperty&#32;of&#32;class|
|[Section top](#pass-outcome-number-143)|Description|No&#32;ontology&#32;term&#32;is&#32;a&#32;subproperty&#32;of&#32;a&#32;class|

***
### Pass Outcome number 144

[Jump to summary definition](#summary-Pass-144)	|	[Previous Pass outcome](#pass-outcome-number-143)	|	[Next Pass outcome](#pass-outcome-number-145)

:white_check_mark:Pass outcome
#### Subject detail
|Name|module-devices-ontology|
|----|----|
|Title|Standalone&#32;module&#32;core&#92;devices&#92;ontology.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- https://gitlab.com/coswot/coswot-acimov/blob/HEAD/core/devices/ontology.ttl|

#### Criterion detail
|Identifier|[term-referencing](https://ns.inria.fr/olivaw#term-referencing)|
|----|----|
|Title|Term&#32;referencing&#32;test|
|Description|A&#32;test&#32;case&#32;from&#32;the&#32;Best&#32;Practices&#32;tests&#32;checking&#32;if&#32;each&#32;term&#32;of&#32;the&#32;test&#32;subject&#32;is&#32;referenced&#32;to&#32;a&#32;module&#32;through&#32;a&#32;rdfs:isDefinedBy&#32;property.|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-144)|Identifier|`no-reference-module`|
|[Section top](#pass-outcome-number-144)|Title|Any&#32;term&#32;is&#32;referenced|
|[Section top](#pass-outcome-number-144)|Description|Each&#32;term&#32;of&#32;the&#32;test&#32;subject&#32;is&#32;linked&#32;to&#32;a&#32;module&#32;by&#32;a&#32;rdfs:isDefinedBy&#32;property|

***
### Pass Outcome number 145

[Jump to summary definition](#summary-Pass-145)	|	[Previous Pass outcome](#pass-outcome-number-144)	|	[Next Pass outcome](#pass-outcome-number-146)

:white_check_mark:Pass outcome
#### Subject detail
|Name|module-devices-ontology|
|----|----|
|Title|Standalone&#32;module&#32;core&#92;devices&#92;ontology.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- https://gitlab.com/coswot/coswot-acimov/blob/HEAD/core/devices/ontology.ttl|

#### Criterion detail
|Identifier|[terms-differenciation](https://ns.inria.fr/olivaw#terms-differenciation)|
|----|----|
|Title|Terms&#32;differenciation&#32;test|
|Description|A&#32;test&#32;case&#32;from&#32;the&#32;Best&#32;Practices&#32;tests&#32;checking&#32;if&#32;all&#32;the&#32;terms&#32;are&#32;different&#32;enough&#32;from&#32;each&#32;other&#32;according&#32;to&#32;the&#32;Levenshtein&#32;distance&#32;metric.|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-145)|Identifier|`too-close-terms`|
|[Section top](#pass-outcome-number-145)|Title|Terms&#32;differenciated&#32;enough|
|[Section top](#pass-outcome-number-145)|Description|All&#32;the&#32;terms&#32;have&#32;have&#32;a&#32;satisfying&#32;Levenshtein&#32;distance&#32;from&#32;each&#32;other&#32;term.|

***
### Pass Outcome number 146

[Jump to summary definition](#summary-Pass-146)	|	[Previous Pass outcome](#pass-outcome-number-145)	|	[Next Pass outcome](#pass-outcome-number-147)

:white_check_mark:Pass outcome
#### Subject detail
|Name|module-coswot-sosa|
|----|----|
|Title|Standalone&#32;module&#32;core&#92;coswot-sosa.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- https://gitlab.com/coswot/coswot-acimov/blob/HEAD/core/coswot-sosa.ttl|

#### Criterion detail
|Identifier|[domain-and-range-referencing](https://ns.inria.fr/olivaw#domain-and-range-referencing)|
|----|----|
|Title|Domain&#32;and&#32;range&#32;referencing&#32;test|
|Description|A&#32;test&#32;case&#32;from&#32;the&#32;Best&#32;Practices&#32;tests&#32;checking&#32;if&#32;all&#32;the&#32;ranges&#32;and&#32;domains&#32;from&#32;the&#32;test&#32;subject&#32;point&#32;to&#32;terms&#32;that&#32;are&#32;defined&#32;in&#32;the&#32;vocabulary.|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-146)|Identifier|`domain-out-of-vocabulary`|
|[Section top](#pass-outcome-number-146)|Title|Domains&#32;properly&#32;defined|
|[Section top](#pass-outcome-number-146)|Description|Each&#32;rdfs:domain&#32;is&#32;defined&#32;within&#32;the&#32;fragment|

***
### Pass Outcome number 147

[Jump to summary definition](#summary-Pass-147)	|	[Previous Pass outcome](#pass-outcome-number-146)	|	[Next Pass outcome](#pass-outcome-number-148)

:white_check_mark:Pass outcome
#### Subject detail
|Name|module-coswot-sosa|
|----|----|
|Title|Standalone&#32;module&#32;core&#92;coswot-sosa.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- https://gitlab.com/coswot/coswot-acimov/blob/HEAD/core/coswot-sosa.ttl|

#### Criterion detail
|Identifier|[domain-and-range-referencing](https://ns.inria.fr/olivaw#domain-and-range-referencing)|
|----|----|
|Title|Domain&#32;and&#32;range&#32;referencing&#32;test|
|Description|A&#32;test&#32;case&#32;from&#32;the&#32;Best&#32;Practices&#32;tests&#32;checking&#32;if&#32;all&#32;the&#32;ranges&#32;and&#32;domains&#32;from&#32;the&#32;test&#32;subject&#32;point&#32;to&#32;terms&#32;that&#32;are&#32;defined&#32;in&#32;the&#32;vocabulary.|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-147)|Identifier|`range-out-of-vocabulary`|
|[Section top](#pass-outcome-number-147)|Title|Ranges&#32;properly&#32;defined|
|[Section top](#pass-outcome-number-147)|Description|Each&#32;rdfs:range&#32;is&#32;defined&#32;within&#32;the&#32;fragment|

***
### Pass Outcome number 148

[Jump to summary definition](#summary-Pass-148)	|	[Previous Pass outcome](#pass-outcome-number-147)	|	[Next Pass outcome](#pass-outcome-number-149)

:white_check_mark:Pass outcome
#### Subject detail
|Name|module-coswot-sosa|
|----|----|
|Title|Standalone&#32;module&#32;core&#92;coswot-sosa.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- https://gitlab.com/coswot/coswot-acimov/blob/HEAD/core/coswot-sosa.ttl|

#### Criterion detail
|Identifier|[labeled-terms](https://ns.inria.fr/olivaw#labeled-terms)|
|----|----|
|Title|Term&#32;labeling&#32;test|
|Description|A&#32;test&#32;case&#32;from&#32;the&#32;Best&#32;Practices&#32;tests&#32;checking&#32;if&#32;all&#32;the&#32;terms&#32;of&#32;the&#32;subject&#32;have&#32;a&#32;rdfs:label&#32;property&#32;pointing&#32;to&#32;a&#32;literal&#32;in&#32;English|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-148)|Identifier|`not-labeled-term`|
|[Section top](#pass-outcome-number-148)|Title|All&#32;terms&#32;labeled|
|[Section top](#pass-outcome-number-148)|Description|All&#32;the&#32;terms&#32;defined&#32;in&#32;the&#32;subject&#32;have&#32;a&#32;rdfs:label&#32;in&#32;English|

***
### Pass Outcome number 149

[Jump to summary definition](#summary-Pass-149)	|	[Previous Pass outcome](#pass-outcome-number-148)	|	[Next Pass outcome](#pass-outcome-number-150)

:white_check_mark:Pass outcome
#### Subject detail
|Name|module-coswot-sosa|
|----|----|
|Title|Standalone&#32;module&#32;core&#92;coswot-sosa.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- https://gitlab.com/coswot/coswot-acimov/blob/HEAD/core/coswot-sosa.ttl|

#### Criterion detail
|Identifier|[owl-rl-constraint](https://ns.inria.fr/olivaw#owl-rl-constraint)|
|----|----|
|Title|OWL&#32;RL&#32;Constraint&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;check&#32;wether&#32;the&#32;test&#32;subject&#32;is&#32;syntaxically&#32;correct&#32;or&#32;not.|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-149)|Identifier|`owl-rl-constraint-violation`|
|[Section top](#pass-outcome-number-149)|Title|OWL&#32;RL&#32;consistent|
|[Section top](#pass-outcome-number-149)|Description|The&#32;provided&#32;graph&#32;is&#32;consistent&#32;for&#32;any&#32;OWL&#32;RL&#32;constraint|

***
### Pass Outcome number 150

[Jump to summary definition](#summary-Pass-150)	|	[Previous Pass outcome](#pass-outcome-number-149)	|	[Next Pass outcome](#pass-outcome-number-151)

:white_check_mark:Pass outcome
#### Subject detail
|Name|module-coswot-sosa|
|----|----|
|Title|Standalone&#32;module&#32;core&#92;coswot-sosa.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- https://gitlab.com/coswot/coswot-acimov/blob/HEAD/core/coswot-sosa.ttl|

#### Criterion detail
|Identifier|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|
|----|----|
|Title|Profile&#32;compatibility&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;check&#32;whether&#32;the&#32;test&#32;subject&#32;is&#32;compatible&#32;with&#32;a&#32;profile&#32;or&#32;not,&#32;and&#32;if&#32;it&#32;is&#32;not,&#32;why.|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-150)|Identifier|`owl-el-profile-error`|
|[Section top](#pass-outcome-number-150)|Title|OWL&#32;EL&#32;Profile&#32;compatible|
|[Section top](#pass-outcome-number-150)|Description|The&#32;subject&#32;is&#32;included&#32;in&#32;the&#32;OWL&#32;EL&#32;sublanguage|

***
### Pass Outcome number 151

[Jump to summary definition](#summary-Pass-151)	|	[Previous Pass outcome](#pass-outcome-number-150)	|	[Next Pass outcome](#pass-outcome-number-152)

:white_check_mark:Pass outcome
#### Subject detail
|Name|module-coswot-sosa|
|----|----|
|Title|Standalone&#32;module&#32;core&#92;coswot-sosa.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- https://gitlab.com/coswot/coswot-acimov/blob/HEAD/core/coswot-sosa.ttl|

#### Criterion detail
|Identifier|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|
|----|----|
|Title|Profile&#32;compatibility&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;check&#32;whether&#32;the&#32;test&#32;subject&#32;is&#32;compatible&#32;with&#32;a&#32;profile&#32;or&#32;not,&#32;and&#32;if&#32;it&#32;is&#32;not,&#32;why.|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-151)|Identifier|`owl-ql-profile-error`|
|[Section top](#pass-outcome-number-151)|Title|OWL&#32;QL&#32;Profile&#32;compatible|
|[Section top](#pass-outcome-number-151)|Description|The&#32;subject&#32;is&#32;included&#32;in&#32;the&#32;OWL&#32;QL&#32;sublanguage|

***
### Pass Outcome number 152

[Jump to summary definition](#summary-Pass-152)	|	[Previous Pass outcome](#pass-outcome-number-151)	|	[Next Pass outcome](#pass-outcome-number-153)

:white_check_mark:Pass outcome
#### Subject detail
|Name|module-coswot-sosa|
|----|----|
|Title|Standalone&#32;module&#32;core&#92;coswot-sosa.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- https://gitlab.com/coswot/coswot-acimov/blob/HEAD/core/coswot-sosa.ttl|

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
|Name|module-coswot-sosa|
|----|----|
|Title|Standalone&#32;module&#32;core&#92;coswot-sosa.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- https://gitlab.com/coswot/coswot-acimov/blob/HEAD/core/coswot-sosa.ttl|

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
|Name|module-coswot-sosa|
|----|----|
|Title|Standalone&#32;module&#32;core&#92;coswot-sosa.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- https://gitlab.com/coswot/coswot-acimov/blob/HEAD/core/coswot-sosa.ttl|

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
|Name|module-coswot-sosa|
|----|----|
|Title|Standalone&#32;module&#32;core&#92;coswot-sosa.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- https://gitlab.com/coswot/coswot-acimov/blob/HEAD/core/coswot-sosa.ttl|

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
|Name|module-coswot-sosa|
|----|----|
|Title|Standalone&#32;module&#32;core&#92;coswot-sosa.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- https://gitlab.com/coswot/coswot-acimov/blob/HEAD/core/coswot-sosa.ttl|

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
|Name|module-coswot-sosa|
|----|----|
|Title|Standalone&#32;module&#32;core&#92;coswot-sosa.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- https://gitlab.com/coswot/coswot-acimov/blob/HEAD/core/coswot-sosa.ttl|

#### Criterion detail
|Identifier|[terms-differenciation](https://ns.inria.fr/olivaw#terms-differenciation)|
|----|----|
|Title|Terms&#32;differenciation&#32;test|
|Description|A&#32;test&#32;case&#32;from&#32;the&#32;Best&#32;Practices&#32;tests&#32;checking&#32;if&#32;all&#32;the&#32;terms&#32;are&#32;different&#32;enough&#32;from&#32;each&#32;other&#32;according&#32;to&#32;the&#32;Levenshtein&#32;distance&#32;metric.|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-157)|Identifier|`too-close-terms`|
|[Section top](#pass-outcome-number-157)|Title|Terms&#32;differenciated&#32;enough|
|[Section top](#pass-outcome-number-157)|Description|All&#32;the&#32;terms&#32;have&#32;have&#32;a&#32;satisfying&#32;Levenshtein&#32;distance&#32;from&#32;each&#32;other&#32;term.|

***
### Pass Outcome number 158

[Jump to summary definition](#summary-Pass-158)	|	[Previous Pass outcome](#pass-outcome-number-157)	|	[Next Pass outcome](#pass-outcome-number-159)

:white_check_mark:Pass outcome
#### Subject detail
|Name|module-communications-ontology|
|----|----|
|Title|Standalone&#32;module&#32;core&#92;communications&#92;ontology.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- https://gitlab.com/coswot/coswot-acimov/blob/HEAD/core/communications/ontology.ttl|

#### Criterion detail
|Identifier|[domain-and-range-referencing](https://ns.inria.fr/olivaw#domain-and-range-referencing)|
|----|----|
|Title|Domain&#32;and&#32;range&#32;referencing&#32;test|
|Description|A&#32;test&#32;case&#32;from&#32;the&#32;Best&#32;Practices&#32;tests&#32;checking&#32;if&#32;all&#32;the&#32;ranges&#32;and&#32;domains&#32;from&#32;the&#32;test&#32;subject&#32;point&#32;to&#32;terms&#32;that&#32;are&#32;defined&#32;in&#32;the&#32;vocabulary.|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-158)|Identifier|`domain-out-of-vocabulary`|
|[Section top](#pass-outcome-number-158)|Title|Domains&#32;properly&#32;defined|
|[Section top](#pass-outcome-number-158)|Description|Each&#32;rdfs:domain&#32;is&#32;defined&#32;within&#32;the&#32;fragment|

***
### Pass Outcome number 159

[Jump to summary definition](#summary-Pass-159)	|	[Previous Pass outcome](#pass-outcome-number-158)	|	[Next Pass outcome](#pass-outcome-number-160)

:white_check_mark:Pass outcome
#### Subject detail
|Name|module-communications-ontology|
|----|----|
|Title|Standalone&#32;module&#32;core&#92;communications&#92;ontology.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- https://gitlab.com/coswot/coswot-acimov/blob/HEAD/core/communications/ontology.ttl|

#### Criterion detail
|Identifier|[domain-and-range-referencing](https://ns.inria.fr/olivaw#domain-and-range-referencing)|
|----|----|
|Title|Domain&#32;and&#32;range&#32;referencing&#32;test|
|Description|A&#32;test&#32;case&#32;from&#32;the&#32;Best&#32;Practices&#32;tests&#32;checking&#32;if&#32;all&#32;the&#32;ranges&#32;and&#32;domains&#32;from&#32;the&#32;test&#32;subject&#32;point&#32;to&#32;terms&#32;that&#32;are&#32;defined&#32;in&#32;the&#32;vocabulary.|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-159)|Identifier|`range-out-of-vocabulary`|
|[Section top](#pass-outcome-number-159)|Title|Ranges&#32;properly&#32;defined|
|[Section top](#pass-outcome-number-159)|Description|Each&#32;rdfs:range&#32;is&#32;defined&#32;within&#32;the&#32;fragment|

***
### Pass Outcome number 160

[Jump to summary definition](#summary-Pass-160)	|	[Previous Pass outcome](#pass-outcome-number-159)	|	[Next Pass outcome](#pass-outcome-number-161)

:white_check_mark:Pass outcome
#### Subject detail
|Name|module-communications-ontology|
|----|----|
|Title|Standalone&#32;module&#32;core&#92;communications&#92;ontology.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- https://gitlab.com/coswot/coswot-acimov/blob/HEAD/core/communications/ontology.ttl|

#### Criterion detail
|Identifier|[labeled-terms](https://ns.inria.fr/olivaw#labeled-terms)|
|----|----|
|Title|Term&#32;labeling&#32;test|
|Description|A&#32;test&#32;case&#32;from&#32;the&#32;Best&#32;Practices&#32;tests&#32;checking&#32;if&#32;all&#32;the&#32;terms&#32;of&#32;the&#32;subject&#32;have&#32;a&#32;rdfs:label&#32;property&#32;pointing&#32;to&#32;a&#32;literal&#32;in&#32;English|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-160)|Identifier|`not-labeled-term`|
|[Section top](#pass-outcome-number-160)|Title|All&#32;terms&#32;labeled|
|[Section top](#pass-outcome-number-160)|Description|All&#32;the&#32;terms&#32;defined&#32;in&#32;the&#32;subject&#32;have&#32;a&#32;rdfs:label&#32;in&#32;English|

***
### Pass Outcome number 161

[Jump to summary definition](#summary-Pass-161)	|	[Previous Pass outcome](#pass-outcome-number-160)	|	[Next Pass outcome](#pass-outcome-number-162)

:white_check_mark:Pass outcome
#### Subject detail
|Name|module-communications-ontology|
|----|----|
|Title|Standalone&#32;module&#32;core&#92;communications&#92;ontology.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- https://gitlab.com/coswot/coswot-acimov/blob/HEAD/core/communications/ontology.ttl|

#### Criterion detail
|Identifier|[owl-rl-constraint](https://ns.inria.fr/olivaw#owl-rl-constraint)|
|----|----|
|Title|OWL&#32;RL&#32;Constraint&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;check&#32;wether&#32;the&#32;test&#32;subject&#32;is&#32;syntaxically&#32;correct&#32;or&#32;not.|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-161)|Identifier|`owl-rl-constraint-violation`|
|[Section top](#pass-outcome-number-161)|Title|OWL&#32;RL&#32;consistent|
|[Section top](#pass-outcome-number-161)|Description|The&#32;provided&#32;graph&#32;is&#32;consistent&#32;for&#32;any&#32;OWL&#32;RL&#32;constraint|

***
### Pass Outcome number 162

[Jump to summary definition](#summary-Pass-162)	|	[Previous Pass outcome](#pass-outcome-number-161)	|	[Next Pass outcome](#pass-outcome-number-163)

:white_check_mark:Pass outcome
#### Subject detail
|Name|module-communications-ontology|
|----|----|
|Title|Standalone&#32;module&#32;core&#92;communications&#92;ontology.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- https://gitlab.com/coswot/coswot-acimov/blob/HEAD/core/communications/ontology.ttl|

#### Criterion detail
|Identifier|[proper-extension-predicate](https://ns.inria.fr/olivaw#proper-extension-predicate)|
|----|----|
|Title|Predicate&#32;extension&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;test&#32;the&#32;proper&#32;use&#32;of&#32;predicates&#32;rdfs:subClassOf&#32;and&#32;rdfs:subPropertyOf&#32;on&#32;the&#32;ontology&#32;terms|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-162)|Identifier|`class-subpropertyof`|
|[Section top](#pass-outcome-number-162)|Title|No&#32;class&#32;subproperty|
|[Section top](#pass-outcome-number-162)|Description|No&#32;ontology&#32;class&#32;is&#32;a&#32;subproperty|

***
### Pass Outcome number 163

[Jump to summary definition](#summary-Pass-163)	|	[Previous Pass outcome](#pass-outcome-number-162)	|	[Next Pass outcome](#pass-outcome-number-164)

:white_check_mark:Pass outcome
#### Subject detail
|Name|module-communications-ontology|
|----|----|
|Title|Standalone&#32;module&#32;core&#92;communications&#92;ontology.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- https://gitlab.com/coswot/coswot-acimov/blob/HEAD/core/communications/ontology.ttl|

#### Criterion detail
|Identifier|[proper-extension-predicate](https://ns.inria.fr/olivaw#proper-extension-predicate)|
|----|----|
|Title|Predicate&#32;extension&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;test&#32;the&#32;proper&#32;use&#32;of&#32;predicates&#32;rdfs:subClassOf&#32;and&#32;rdfs:subPropertyOf&#32;on&#32;the&#32;ontology&#32;terms|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-163)|Identifier|`property-subclassof`|
|[Section top](#pass-outcome-number-163)|Title|No&#32;property&#32;subclass|
|[Section top](#pass-outcome-number-163)|Description|No&#32;ontology&#32;property&#32;is&#32;a&#32;subclass|

***
### Pass Outcome number 164

[Jump to summary definition](#summary-Pass-164)	|	[Previous Pass outcome](#pass-outcome-number-163)	|	[Next Pass outcome](#pass-outcome-number-165)

:white_check_mark:Pass outcome
#### Subject detail
|Name|module-communications-ontology|
|----|----|
|Title|Standalone&#32;module&#32;core&#92;communications&#92;ontology.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- https://gitlab.com/coswot/coswot-acimov/blob/HEAD/core/communications/ontology.ttl|

#### Criterion detail
|Identifier|[proper-extension-predicate](https://ns.inria.fr/olivaw#proper-extension-predicate)|
|----|----|
|Title|Predicate&#32;extension&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;test&#32;the&#32;proper&#32;use&#32;of&#32;predicates&#32;rdfs:subClassOf&#32;and&#32;rdfs:subPropertyOf&#32;on&#32;the&#32;ontology&#32;terms|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-164)|Identifier|`subclassof-property`|
|[Section top](#pass-outcome-number-164)|Title|No&#32;subclass&#32;of&#32;property|
|[Section top](#pass-outcome-number-164)|Description|No&#32;ontology&#32;term&#32;is&#32;a&#32;subclass&#32;of&#32;a&#32;property|

***
### Pass Outcome number 165

[Jump to summary definition](#summary-Pass-165)	|	[Previous Pass outcome](#pass-outcome-number-164)	|	[Next Pass outcome](#pass-outcome-number-166)

:white_check_mark:Pass outcome
#### Subject detail
|Name|module-communications-ontology|
|----|----|
|Title|Standalone&#32;module&#32;core&#92;communications&#92;ontology.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- https://gitlab.com/coswot/coswot-acimov/blob/HEAD/core/communications/ontology.ttl|

#### Criterion detail
|Identifier|[proper-extension-predicate](https://ns.inria.fr/olivaw#proper-extension-predicate)|
|----|----|
|Title|Predicate&#32;extension&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;test&#32;the&#32;proper&#32;use&#32;of&#32;predicates&#32;rdfs:subClassOf&#32;and&#32;rdfs:subPropertyOf&#32;on&#32;the&#32;ontology&#32;terms|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-165)|Identifier|`subpropertyof-class`|
|[Section top](#pass-outcome-number-165)|Title|No&#32;subproperty&#32;of&#32;class|
|[Section top](#pass-outcome-number-165)|Description|No&#32;ontology&#32;term&#32;is&#32;a&#32;subproperty&#32;of&#32;a&#32;class|

***
### Pass Outcome number 166

[Jump to summary definition](#summary-Pass-166)	|	[Previous Pass outcome](#pass-outcome-number-165)	|	[Next Pass outcome](#pass-outcome-number-167)

:white_check_mark:Pass outcome
#### Subject detail
|Name|module-communications-ontology|
|----|----|
|Title|Standalone&#32;module&#32;core&#92;communications&#92;ontology.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- https://gitlab.com/coswot/coswot-acimov/blob/HEAD/core/communications/ontology.ttl|

#### Criterion detail
|Identifier|[term-referencing](https://ns.inria.fr/olivaw#term-referencing)|
|----|----|
|Title|Term&#32;referencing&#32;test|
|Description|A&#32;test&#32;case&#32;from&#32;the&#32;Best&#32;Practices&#32;tests&#32;checking&#32;if&#32;each&#32;term&#32;of&#32;the&#32;test&#32;subject&#32;is&#32;referenced&#32;to&#32;a&#32;module&#32;through&#32;a&#32;rdfs:isDefinedBy&#32;property.|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-166)|Identifier|`no-reference-module`|
|[Section top](#pass-outcome-number-166)|Title|Any&#32;term&#32;is&#32;referenced|
|[Section top](#pass-outcome-number-166)|Description|Each&#32;term&#32;of&#32;the&#32;test&#32;subject&#32;is&#32;linked&#32;to&#32;a&#32;module&#32;by&#32;a&#32;rdfs:isDefinedBy&#32;property|

***
### Pass Outcome number 167

[Jump to summary definition](#summary-Pass-167)	|	[Previous Pass outcome](#pass-outcome-number-166)	|	[Next Pass outcome](#pass-outcome-number-168)

:white_check_mark:Pass outcome
#### Subject detail
|Name|module-communications-ontology|
|----|----|
|Title|Standalone&#32;module&#32;core&#92;communications&#92;ontology.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- https://gitlab.com/coswot/coswot-acimov/blob/HEAD/core/communications/ontology.ttl|

#### Criterion detail
|Identifier|[terms-differenciation](https://ns.inria.fr/olivaw#terms-differenciation)|
|----|----|
|Title|Terms&#32;differenciation&#32;test|
|Description|A&#32;test&#32;case&#32;from&#32;the&#32;Best&#32;Practices&#32;tests&#32;checking&#32;if&#32;all&#32;the&#32;terms&#32;are&#32;different&#32;enough&#32;from&#32;each&#32;other&#32;according&#32;to&#32;the&#32;Levenshtein&#32;distance&#32;metric.|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-167)|Identifier|`too-close-terms`|
|[Section top](#pass-outcome-number-167)|Title|Terms&#32;differenciated&#32;enough|
|[Section top](#pass-outcome-number-167)|Description|All&#32;the&#32;terms&#32;have&#32;have&#32;a&#32;satisfying&#32;Levenshtein&#32;distance&#32;from&#32;each&#32;other&#32;term.|

***
### Pass Outcome number 168

[Jump to summary definition](#summary-Pass-168)	|	[Previous Pass outcome](#pass-outcome-number-167)	|	[Next Pass outcome](#pass-outcome-number-169)

:white_check_mark:Pass outcome
#### Subject detail
|Name|module-aggregations-ontology|
|----|----|
|Title|Standalone&#32;module&#32;core&#92;aggregations&#92;ontology.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- https://gitlab.com/coswot/coswot-acimov/blob/HEAD/core/aggregations/ontology.ttl|

#### Criterion detail
|Identifier|[domain-and-range-referencing](https://ns.inria.fr/olivaw#domain-and-range-referencing)|
|----|----|
|Title|Domain&#32;and&#32;range&#32;referencing&#32;test|
|Description|A&#32;test&#32;case&#32;from&#32;the&#32;Best&#32;Practices&#32;tests&#32;checking&#32;if&#32;all&#32;the&#32;ranges&#32;and&#32;domains&#32;from&#32;the&#32;test&#32;subject&#32;point&#32;to&#32;terms&#32;that&#32;are&#32;defined&#32;in&#32;the&#32;vocabulary.|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-168)|Identifier|`domain-out-of-vocabulary`|
|[Section top](#pass-outcome-number-168)|Title|Domains&#32;properly&#32;defined|
|[Section top](#pass-outcome-number-168)|Description|Each&#32;rdfs:domain&#32;is&#32;defined&#32;within&#32;the&#32;fragment|

***
### Pass Outcome number 169

[Jump to summary definition](#summary-Pass-169)	|	[Previous Pass outcome](#pass-outcome-number-168)	|	[Next Pass outcome](#pass-outcome-number-170)

:white_check_mark:Pass outcome
#### Subject detail
|Name|module-aggregations-ontology|
|----|----|
|Title|Standalone&#32;module&#32;core&#92;aggregations&#92;ontology.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- https://gitlab.com/coswot/coswot-acimov/blob/HEAD/core/aggregations/ontology.ttl|

#### Criterion detail
|Identifier|[labeled-terms](https://ns.inria.fr/olivaw#labeled-terms)|
|----|----|
|Title|Term&#32;labeling&#32;test|
|Description|A&#32;test&#32;case&#32;from&#32;the&#32;Best&#32;Practices&#32;tests&#32;checking&#32;if&#32;all&#32;the&#32;terms&#32;of&#32;the&#32;subject&#32;have&#32;a&#32;rdfs:label&#32;property&#32;pointing&#32;to&#32;a&#32;literal&#32;in&#32;English|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-169)|Identifier|`not-labeled-term`|
|[Section top](#pass-outcome-number-169)|Title|All&#32;terms&#32;labeled|
|[Section top](#pass-outcome-number-169)|Description|All&#32;the&#32;terms&#32;defined&#32;in&#32;the&#32;subject&#32;have&#32;a&#32;rdfs:label&#32;in&#32;English|

***
### Pass Outcome number 170

[Jump to summary definition](#summary-Pass-170)	|	[Previous Pass outcome](#pass-outcome-number-169)	|	[Next Pass outcome](#pass-outcome-number-171)

:white_check_mark:Pass outcome
#### Subject detail
|Name|module-aggregations-ontology|
|----|----|
|Title|Standalone&#32;module&#32;core&#92;aggregations&#92;ontology.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- https://gitlab.com/coswot/coswot-acimov/blob/HEAD/core/aggregations/ontology.ttl|

#### Criterion detail
|Identifier|[owl-rl-constraint](https://ns.inria.fr/olivaw#owl-rl-constraint)|
|----|----|
|Title|OWL&#32;RL&#32;Constraint&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;check&#32;wether&#32;the&#32;test&#32;subject&#32;is&#32;syntaxically&#32;correct&#32;or&#32;not.|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-170)|Identifier|`owl-rl-constraint-violation`|
|[Section top](#pass-outcome-number-170)|Title|OWL&#32;RL&#32;consistent|
|[Section top](#pass-outcome-number-170)|Description|The&#32;provided&#32;graph&#32;is&#32;consistent&#32;for&#32;any&#32;OWL&#32;RL&#32;constraint|

***
### Pass Outcome number 171

[Jump to summary definition](#summary-Pass-171)	|	[Previous Pass outcome](#pass-outcome-number-170)	|	[Next Pass outcome](#pass-outcome-number-172)

:white_check_mark:Pass outcome
#### Subject detail
|Name|module-aggregations-ontology|
|----|----|
|Title|Standalone&#32;module&#32;core&#92;aggregations&#92;ontology.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- https://gitlab.com/coswot/coswot-acimov/blob/HEAD/core/aggregations/ontology.ttl|

#### Criterion detail
|Identifier|[proper-extension-predicate](https://ns.inria.fr/olivaw#proper-extension-predicate)|
|----|----|
|Title|Predicate&#32;extension&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;test&#32;the&#32;proper&#32;use&#32;of&#32;predicates&#32;rdfs:subClassOf&#32;and&#32;rdfs:subPropertyOf&#32;on&#32;the&#32;ontology&#32;terms|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-171)|Identifier|`class-subpropertyof`|
|[Section top](#pass-outcome-number-171)|Title|No&#32;class&#32;subproperty|
|[Section top](#pass-outcome-number-171)|Description|No&#32;ontology&#32;class&#32;is&#32;a&#32;subproperty|

***
### Pass Outcome number 172

[Jump to summary definition](#summary-Pass-172)	|	[Previous Pass outcome](#pass-outcome-number-171)	|	[Next Pass outcome](#pass-outcome-number-173)

:white_check_mark:Pass outcome
#### Subject detail
|Name|module-aggregations-ontology|
|----|----|
|Title|Standalone&#32;module&#32;core&#92;aggregations&#92;ontology.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- https://gitlab.com/coswot/coswot-acimov/blob/HEAD/core/aggregations/ontology.ttl|

#### Criterion detail
|Identifier|[proper-extension-predicate](https://ns.inria.fr/olivaw#proper-extension-predicate)|
|----|----|
|Title|Predicate&#32;extension&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;test&#32;the&#32;proper&#32;use&#32;of&#32;predicates&#32;rdfs:subClassOf&#32;and&#32;rdfs:subPropertyOf&#32;on&#32;the&#32;ontology&#32;terms|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-172)|Identifier|`property-subclassof`|
|[Section top](#pass-outcome-number-172)|Title|No&#32;property&#32;subclass|
|[Section top](#pass-outcome-number-172)|Description|No&#32;ontology&#32;property&#32;is&#32;a&#32;subclass|

***
### Pass Outcome number 173

[Jump to summary definition](#summary-Pass-173)	|	[Previous Pass outcome](#pass-outcome-number-172)	|	[Next Pass outcome](#pass-outcome-number-174)

:white_check_mark:Pass outcome
#### Subject detail
|Name|module-aggregations-ontology|
|----|----|
|Title|Standalone&#32;module&#32;core&#92;aggregations&#92;ontology.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- https://gitlab.com/coswot/coswot-acimov/blob/HEAD/core/aggregations/ontology.ttl|

#### Criterion detail
|Identifier|[proper-extension-predicate](https://ns.inria.fr/olivaw#proper-extension-predicate)|
|----|----|
|Title|Predicate&#32;extension&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;test&#32;the&#32;proper&#32;use&#32;of&#32;predicates&#32;rdfs:subClassOf&#32;and&#32;rdfs:subPropertyOf&#32;on&#32;the&#32;ontology&#32;terms|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-173)|Identifier|`subclassof-property`|
|[Section top](#pass-outcome-number-173)|Title|No&#32;subclass&#32;of&#32;property|
|[Section top](#pass-outcome-number-173)|Description|No&#32;ontology&#32;term&#32;is&#32;a&#32;subclass&#32;of&#32;a&#32;property|

***
### Pass Outcome number 174

[Jump to summary definition](#summary-Pass-174)	|	[Previous Pass outcome](#pass-outcome-number-173)	|	[Next Pass outcome](#pass-outcome-number-175)

:white_check_mark:Pass outcome
#### Subject detail
|Name|module-aggregations-ontology|
|----|----|
|Title|Standalone&#32;module&#32;core&#92;aggregations&#92;ontology.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- https://gitlab.com/coswot/coswot-acimov/blob/HEAD/core/aggregations/ontology.ttl|

#### Criterion detail
|Identifier|[proper-extension-predicate](https://ns.inria.fr/olivaw#proper-extension-predicate)|
|----|----|
|Title|Predicate&#32;extension&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;test&#32;the&#32;proper&#32;use&#32;of&#32;predicates&#32;rdfs:subClassOf&#32;and&#32;rdfs:subPropertyOf&#32;on&#32;the&#32;ontology&#32;terms|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-174)|Identifier|`subpropertyof-class`|
|[Section top](#pass-outcome-number-174)|Title|No&#32;subproperty&#32;of&#32;class|
|[Section top](#pass-outcome-number-174)|Description|No&#32;ontology&#32;term&#32;is&#32;a&#32;subproperty&#32;of&#32;a&#32;class|

***
### Pass Outcome number 175

[Jump to summary definition](#summary-Pass-175)	|	[Previous Pass outcome](#pass-outcome-number-174)	|	[Next Pass outcome](#pass-outcome-number-176)

:white_check_mark:Pass outcome
#### Subject detail
|Name|module-aggregations-ontology|
|----|----|
|Title|Standalone&#32;module&#32;core&#92;aggregations&#92;ontology.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- https://gitlab.com/coswot/coswot-acimov/blob/HEAD/core/aggregations/ontology.ttl|

#### Criterion detail
|Identifier|[term-referencing](https://ns.inria.fr/olivaw#term-referencing)|
|----|----|
|Title|Term&#32;referencing&#32;test|
|Description|A&#32;test&#32;case&#32;from&#32;the&#32;Best&#32;Practices&#32;tests&#32;checking&#32;if&#32;each&#32;term&#32;of&#32;the&#32;test&#32;subject&#32;is&#32;referenced&#32;to&#32;a&#32;module&#32;through&#32;a&#32;rdfs:isDefinedBy&#32;property.|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-175)|Identifier|`no-reference-module`|
|[Section top](#pass-outcome-number-175)|Title|Any&#32;term&#32;is&#32;referenced|
|[Section top](#pass-outcome-number-175)|Description|Each&#32;term&#32;of&#32;the&#32;test&#32;subject&#32;is&#32;linked&#32;to&#32;a&#32;module&#32;by&#32;a&#32;rdfs:isDefinedBy&#32;property|

***
### Pass Outcome number 176

[Jump to summary definition](#summary-Pass-176)	|	[Previous Pass outcome](#pass-outcome-number-175)	|	[Next Pass outcome](#pass-outcome-number-177)

:white_check_mark:Pass outcome
#### Subject detail
|Name|module-aggregations-ontology|
|----|----|
|Title|Standalone&#32;module&#32;core&#92;aggregations&#92;ontology.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- https://gitlab.com/coswot/coswot-acimov/blob/HEAD/core/aggregations/ontology.ttl|

#### Criterion detail
|Identifier|[terms-differenciation](https://ns.inria.fr/olivaw#terms-differenciation)|
|----|----|
|Title|Terms&#32;differenciation&#32;test|
|Description|A&#32;test&#32;case&#32;from&#32;the&#32;Best&#32;Practices&#32;tests&#32;checking&#32;if&#32;all&#32;the&#32;terms&#32;are&#32;different&#32;enough&#32;from&#32;each&#32;other&#32;according&#32;to&#32;the&#32;Levenshtein&#32;distance&#32;metric.|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-176)|Identifier|`too-close-terms`|
|[Section top](#pass-outcome-number-176)|Title|Terms&#32;differenciated&#32;enough|
|[Section top](#pass-outcome-number-176)|Description|All&#32;the&#32;terms&#32;have&#32;have&#32;a&#32;satisfying&#32;Levenshtein&#32;distance&#32;from&#32;each&#32;other&#32;term.|

***
### Pass Outcome number 177

[Jump to summary definition](#summary-Pass-177)	|	[Previous Pass outcome](#pass-outcome-number-176)	|	[Next Pass outcome](#pass-outcome-number-178)

:white_check_mark:Pass outcome
#### Subject detail
|Name|module-aggregations-aggregation-kind-thesaurus|
|----|----|
|Title|Standalone&#32;module&#32;core&#92;aggregations&#92;aggregation&lowbar;kind&lowbar;thesaurus.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- https://gitlab.com/coswot/coswot-acimov/blob/HEAD/core/aggregations/aggregation_kind_thesaurus.ttl|

#### Criterion detail
|Identifier|[domain-and-range-referencing](https://ns.inria.fr/olivaw#domain-and-range-referencing)|
|----|----|
|Title|Domain&#32;and&#32;range&#32;referencing&#32;test|
|Description|A&#32;test&#32;case&#32;from&#32;the&#32;Best&#32;Practices&#32;tests&#32;checking&#32;if&#32;all&#32;the&#32;ranges&#32;and&#32;domains&#32;from&#32;the&#32;test&#32;subject&#32;point&#32;to&#32;terms&#32;that&#32;are&#32;defined&#32;in&#32;the&#32;vocabulary.|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-177)|Identifier|`domain-out-of-vocabulary`|
|[Section top](#pass-outcome-number-177)|Title|Domains&#32;properly&#32;defined|
|[Section top](#pass-outcome-number-177)|Description|Each&#32;rdfs:domain&#32;is&#32;defined&#32;within&#32;the&#32;fragment|

***
### Pass Outcome number 178

[Jump to summary definition](#summary-Pass-178)	|	[Previous Pass outcome](#pass-outcome-number-177)	|	[Next Pass outcome](#pass-outcome-number-179)

:white_check_mark:Pass outcome
#### Subject detail
|Name|module-aggregations-aggregation-kind-thesaurus|
|----|----|
|Title|Standalone&#32;module&#32;core&#92;aggregations&#92;aggregation&lowbar;kind&lowbar;thesaurus.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- https://gitlab.com/coswot/coswot-acimov/blob/HEAD/core/aggregations/aggregation_kind_thesaurus.ttl|

#### Criterion detail
|Identifier|[domain-and-range-referencing](https://ns.inria.fr/olivaw#domain-and-range-referencing)|
|----|----|
|Title|Domain&#32;and&#32;range&#32;referencing&#32;test|
|Description|A&#32;test&#32;case&#32;from&#32;the&#32;Best&#32;Practices&#32;tests&#32;checking&#32;if&#32;all&#32;the&#32;ranges&#32;and&#32;domains&#32;from&#32;the&#32;test&#32;subject&#32;point&#32;to&#32;terms&#32;that&#32;are&#32;defined&#32;in&#32;the&#32;vocabulary.|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-178)|Identifier|`range-out-of-vocabulary`|
|[Section top](#pass-outcome-number-178)|Title|Ranges&#32;properly&#32;defined|
|[Section top](#pass-outcome-number-178)|Description|Each&#32;rdfs:range&#32;is&#32;defined&#32;within&#32;the&#32;fragment|

***
### Pass Outcome number 179

[Jump to summary definition](#summary-Pass-179)	|	[Previous Pass outcome](#pass-outcome-number-178)	|	[Next Pass outcome](#pass-outcome-number-180)

:white_check_mark:Pass outcome
#### Subject detail
|Name|module-aggregations-aggregation-kind-thesaurus|
|----|----|
|Title|Standalone&#32;module&#32;core&#92;aggregations&#92;aggregation&lowbar;kind&lowbar;thesaurus.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- https://gitlab.com/coswot/coswot-acimov/blob/HEAD/core/aggregations/aggregation_kind_thesaurus.ttl|

#### Criterion detail
|Identifier|[labeled-terms](https://ns.inria.fr/olivaw#labeled-terms)|
|----|----|
|Title|Term&#32;labeling&#32;test|
|Description|A&#32;test&#32;case&#32;from&#32;the&#32;Best&#32;Practices&#32;tests&#32;checking&#32;if&#32;all&#32;the&#32;terms&#32;of&#32;the&#32;subject&#32;have&#32;a&#32;rdfs:label&#32;property&#32;pointing&#32;to&#32;a&#32;literal&#32;in&#32;English|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-179)|Identifier|`not-labeled-term`|
|[Section top](#pass-outcome-number-179)|Title|All&#32;terms&#32;labeled|
|[Section top](#pass-outcome-number-179)|Description|All&#32;the&#32;terms&#32;defined&#32;in&#32;the&#32;subject&#32;have&#32;a&#32;rdfs:label&#32;in&#32;English|

***
### Pass Outcome number 180

[Jump to summary definition](#summary-Pass-180)	|	[Previous Pass outcome](#pass-outcome-number-179)	|	[Next Pass outcome](#pass-outcome-number-181)

:white_check_mark:Pass outcome
#### Subject detail
|Name|module-aggregations-aggregation-kind-thesaurus|
|----|----|
|Title|Standalone&#32;module&#32;core&#92;aggregations&#92;aggregation&lowbar;kind&lowbar;thesaurus.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- https://gitlab.com/coswot/coswot-acimov/blob/HEAD/core/aggregations/aggregation_kind_thesaurus.ttl|

#### Criterion detail
|Identifier|[owl-rl-constraint](https://ns.inria.fr/olivaw#owl-rl-constraint)|
|----|----|
|Title|OWL&#32;RL&#32;Constraint&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;check&#32;wether&#32;the&#32;test&#32;subject&#32;is&#32;syntaxically&#32;correct&#32;or&#32;not.|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-180)|Identifier|`owl-rl-constraint-violation`|
|[Section top](#pass-outcome-number-180)|Title|OWL&#32;RL&#32;consistent|
|[Section top](#pass-outcome-number-180)|Description|The&#32;provided&#32;graph&#32;is&#32;consistent&#32;for&#32;any&#32;OWL&#32;RL&#32;constraint|

***
### Pass Outcome number 181

[Jump to summary definition](#summary-Pass-181)	|	[Previous Pass outcome](#pass-outcome-number-180)	|	[Next Pass outcome](#pass-outcome-number-182)

:white_check_mark:Pass outcome
#### Subject detail
|Name|module-aggregations-aggregation-kind-thesaurus|
|----|----|
|Title|Standalone&#32;module&#32;core&#92;aggregations&#92;aggregation&lowbar;kind&lowbar;thesaurus.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- https://gitlab.com/coswot/coswot-acimov/blob/HEAD/core/aggregations/aggregation_kind_thesaurus.ttl|

#### Criterion detail
|Identifier|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|
|----|----|
|Title|Profile&#32;compatibility&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;check&#32;whether&#32;the&#32;test&#32;subject&#32;is&#32;compatible&#32;with&#32;a&#32;profile&#32;or&#32;not,&#32;and&#32;if&#32;it&#32;is&#32;not,&#32;why.|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-181)|Identifier|`owl-el-profile-error`|
|[Section top](#pass-outcome-number-181)|Title|OWL&#32;EL&#32;Profile&#32;compatible|
|[Section top](#pass-outcome-number-181)|Description|The&#32;subject&#32;is&#32;included&#32;in&#32;the&#32;OWL&#32;EL&#32;sublanguage|

***
### Pass Outcome number 182

[Jump to summary definition](#summary-Pass-182)	|	[Previous Pass outcome](#pass-outcome-number-181)	|	[Next Pass outcome](#pass-outcome-number-183)

:white_check_mark:Pass outcome
#### Subject detail
|Name|module-aggregations-aggregation-kind-thesaurus|
|----|----|
|Title|Standalone&#32;module&#32;core&#92;aggregations&#92;aggregation&lowbar;kind&lowbar;thesaurus.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- https://gitlab.com/coswot/coswot-acimov/blob/HEAD/core/aggregations/aggregation_kind_thesaurus.ttl|

#### Criterion detail
|Identifier|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|
|----|----|
|Title|Profile&#32;compatibility&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;check&#32;whether&#32;the&#32;test&#32;subject&#32;is&#32;compatible&#32;with&#32;a&#32;profile&#32;or&#32;not,&#32;and&#32;if&#32;it&#32;is&#32;not,&#32;why.|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-182)|Identifier|`owl-ql-profile-error`|
|[Section top](#pass-outcome-number-182)|Title|OWL&#32;QL&#32;Profile&#32;compatible|
|[Section top](#pass-outcome-number-182)|Description|The&#32;subject&#32;is&#32;included&#32;in&#32;the&#32;OWL&#32;QL&#32;sublanguage|

***
### Pass Outcome number 183

[Jump to summary definition](#summary-Pass-183)	|	[Previous Pass outcome](#pass-outcome-number-182)	|	[Next Pass outcome](#pass-outcome-number-184)

:white_check_mark:Pass outcome
#### Subject detail
|Name|module-aggregations-aggregation-kind-thesaurus|
|----|----|
|Title|Standalone&#32;module&#32;core&#92;aggregations&#92;aggregation&lowbar;kind&lowbar;thesaurus.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- https://gitlab.com/coswot/coswot-acimov/blob/HEAD/core/aggregations/aggregation_kind_thesaurus.ttl|

#### Criterion detail
|Identifier|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|
|----|----|
|Title|Profile&#32;compatibility&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;check&#32;whether&#32;the&#32;test&#32;subject&#32;is&#32;compatible&#32;with&#32;a&#32;profile&#32;or&#32;not,&#32;and&#32;if&#32;it&#32;is&#32;not,&#32;why.|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-183)|Identifier|`owl-rl-profile-error`|
|[Section top](#pass-outcome-number-183)|Title|OWL&#32;RL&#32;Profile&#32;compatible|
|[Section top](#pass-outcome-number-183)|Description|The&#32;subject&#32;is&#32;included&#32;in&#32;the&#32;OWL&#32;RL&#32;sublanguage|

***
### Pass Outcome number 184

[Jump to summary definition](#summary-Pass-184)	|	[Previous Pass outcome](#pass-outcome-number-183)	|	[Next Pass outcome](#pass-outcome-number-185)

:white_check_mark:Pass outcome
#### Subject detail
|Name|module-aggregations-aggregation-kind-thesaurus|
|----|----|
|Title|Standalone&#32;module&#32;core&#92;aggregations&#92;aggregation&lowbar;kind&lowbar;thesaurus.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- https://gitlab.com/coswot/coswot-acimov/blob/HEAD/core/aggregations/aggregation_kind_thesaurus.ttl|

#### Criterion detail
|Identifier|[proper-extension-predicate](https://ns.inria.fr/olivaw#proper-extension-predicate)|
|----|----|
|Title|Predicate&#32;extension&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;test&#32;the&#32;proper&#32;use&#32;of&#32;predicates&#32;rdfs:subClassOf&#32;and&#32;rdfs:subPropertyOf&#32;on&#32;the&#32;ontology&#32;terms|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-184)|Identifier|`class-subpropertyof`|
|[Section top](#pass-outcome-number-184)|Title|No&#32;class&#32;subproperty|
|[Section top](#pass-outcome-number-184)|Description|No&#32;ontology&#32;class&#32;is&#32;a&#32;subproperty|

***
### Pass Outcome number 185

[Jump to summary definition](#summary-Pass-185)	|	[Previous Pass outcome](#pass-outcome-number-184)	|	[Next Pass outcome](#pass-outcome-number-186)

:white_check_mark:Pass outcome
#### Subject detail
|Name|module-aggregations-aggregation-kind-thesaurus|
|----|----|
|Title|Standalone&#32;module&#32;core&#92;aggregations&#92;aggregation&lowbar;kind&lowbar;thesaurus.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- https://gitlab.com/coswot/coswot-acimov/blob/HEAD/core/aggregations/aggregation_kind_thesaurus.ttl|

#### Criterion detail
|Identifier|[proper-extension-predicate](https://ns.inria.fr/olivaw#proper-extension-predicate)|
|----|----|
|Title|Predicate&#32;extension&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;test&#32;the&#32;proper&#32;use&#32;of&#32;predicates&#32;rdfs:subClassOf&#32;and&#32;rdfs:subPropertyOf&#32;on&#32;the&#32;ontology&#32;terms|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-185)|Identifier|`property-subclassof`|
|[Section top](#pass-outcome-number-185)|Title|No&#32;property&#32;subclass|
|[Section top](#pass-outcome-number-185)|Description|No&#32;ontology&#32;property&#32;is&#32;a&#32;subclass|

***
### Pass Outcome number 186

[Jump to summary definition](#summary-Pass-186)	|	[Previous Pass outcome](#pass-outcome-number-185)	|	[Next Pass outcome](#pass-outcome-number-187)

:white_check_mark:Pass outcome
#### Subject detail
|Name|module-aggregations-aggregation-kind-thesaurus|
|----|----|
|Title|Standalone&#32;module&#32;core&#92;aggregations&#92;aggregation&lowbar;kind&lowbar;thesaurus.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- https://gitlab.com/coswot/coswot-acimov/blob/HEAD/core/aggregations/aggregation_kind_thesaurus.ttl|

#### Criterion detail
|Identifier|[proper-extension-predicate](https://ns.inria.fr/olivaw#proper-extension-predicate)|
|----|----|
|Title|Predicate&#32;extension&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;test&#32;the&#32;proper&#32;use&#32;of&#32;predicates&#32;rdfs:subClassOf&#32;and&#32;rdfs:subPropertyOf&#32;on&#32;the&#32;ontology&#32;terms|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-186)|Identifier|`subclassof-property`|
|[Section top](#pass-outcome-number-186)|Title|No&#32;subclass&#32;of&#32;property|
|[Section top](#pass-outcome-number-186)|Description|No&#32;ontology&#32;term&#32;is&#32;a&#32;subclass&#32;of&#32;a&#32;property|

***
### Pass Outcome number 187

[Jump to summary definition](#summary-Pass-187)	|	[Previous Pass outcome](#pass-outcome-number-186)	|	[Next Pass outcome](#pass-outcome-number-188)

:white_check_mark:Pass outcome
#### Subject detail
|Name|module-aggregations-aggregation-kind-thesaurus|
|----|----|
|Title|Standalone&#32;module&#32;core&#92;aggregations&#92;aggregation&lowbar;kind&lowbar;thesaurus.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- https://gitlab.com/coswot/coswot-acimov/blob/HEAD/core/aggregations/aggregation_kind_thesaurus.ttl|

#### Criterion detail
|Identifier|[proper-extension-predicate](https://ns.inria.fr/olivaw#proper-extension-predicate)|
|----|----|
|Title|Predicate&#32;extension&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;test&#32;the&#32;proper&#32;use&#32;of&#32;predicates&#32;rdfs:subClassOf&#32;and&#32;rdfs:subPropertyOf&#32;on&#32;the&#32;ontology&#32;terms|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-187)|Identifier|`subpropertyof-class`|
|[Section top](#pass-outcome-number-187)|Title|No&#32;subproperty&#32;of&#32;class|
|[Section top](#pass-outcome-number-187)|Description|No&#32;ontology&#32;term&#32;is&#32;a&#32;subproperty&#32;of&#32;a&#32;class|

***
### Pass Outcome number 188

[Jump to summary definition](#summary-Pass-188)	|	[Previous Pass outcome](#pass-outcome-number-187)	|	[Next Pass outcome](#pass-outcome-number-189)

:white_check_mark:Pass outcome
#### Subject detail
|Name|module-aggregations-aggregation-kind-thesaurus|
|----|----|
|Title|Standalone&#32;module&#32;core&#92;aggregations&#92;aggregation&lowbar;kind&lowbar;thesaurus.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- https://gitlab.com/coswot/coswot-acimov/blob/HEAD/core/aggregations/aggregation_kind_thesaurus.ttl|

#### Criterion detail
|Identifier|[term-referencing](https://ns.inria.fr/olivaw#term-referencing)|
|----|----|
|Title|Term&#32;referencing&#32;test|
|Description|A&#32;test&#32;case&#32;from&#32;the&#32;Best&#32;Practices&#32;tests&#32;checking&#32;if&#32;each&#32;term&#32;of&#32;the&#32;test&#32;subject&#32;is&#32;referenced&#32;to&#32;a&#32;module&#32;through&#32;a&#32;rdfs:isDefinedBy&#32;property.|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-188)|Identifier|`no-reference-module`|
|[Section top](#pass-outcome-number-188)|Title|Any&#32;term&#32;is&#32;referenced|
|[Section top](#pass-outcome-number-188)|Description|Each&#32;term&#32;of&#32;the&#32;test&#32;subject&#32;is&#32;linked&#32;to&#32;a&#32;module&#32;by&#32;a&#32;rdfs:isDefinedBy&#32;property|

***
### Pass Outcome number 189

[Jump to summary definition](#summary-Pass-189)	|	[Previous Pass outcome](#pass-outcome-number-188)	|	[Next Pass outcome](#pass-outcome-number-190)

:white_check_mark:Pass outcome
#### Subject detail
|Name|module-aggregations-aggregation-kind-thesaurus|
|----|----|
|Title|Standalone&#32;module&#32;core&#92;aggregations&#92;aggregation&lowbar;kind&lowbar;thesaurus.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- https://gitlab.com/coswot/coswot-acimov/blob/HEAD/core/aggregations/aggregation_kind_thesaurus.ttl|

#### Criterion detail
|Identifier|[terms-differenciation](https://ns.inria.fr/olivaw#terms-differenciation)|
|----|----|
|Title|Terms&#32;differenciation&#32;test|
|Description|A&#32;test&#32;case&#32;from&#32;the&#32;Best&#32;Practices&#32;tests&#32;checking&#32;if&#32;all&#32;the&#32;terms&#32;are&#32;different&#32;enough&#32;from&#32;each&#32;other&#32;according&#32;to&#32;the&#32;Levenshtein&#32;distance&#32;metric.|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-189)|Identifier|`too-close-terms`|
|[Section top](#pass-outcome-number-189)|Title|Terms&#32;differenciated&#32;enough|
|[Section top](#pass-outcome-number-189)|Description|All&#32;the&#32;terms&#32;have&#32;have&#32;a&#32;satisfying&#32;Levenshtein&#32;distance&#32;from&#32;each&#32;other&#32;term.|

***
### Pass Outcome number 190

[Jump to summary definition](#summary-Pass-190)	|	[Previous Pass outcome](#pass-outcome-number-189)	|	[Next Pass outcome](#pass-outcome-number-191)

:white_check_mark:Pass outcome
#### Subject detail
|Name|module-affordances-ontology|
|----|----|
|Title|Standalone&#32;module&#32;core&#92;affordances&#92;ontology.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- https://gitlab.com/coswot/coswot-acimov/blob/HEAD/core/affordances/ontology.ttl|

#### Criterion detail
|Identifier|[domain-and-range-referencing](https://ns.inria.fr/olivaw#domain-and-range-referencing)|
|----|----|
|Title|Domain&#32;and&#32;range&#32;referencing&#32;test|
|Description|A&#32;test&#32;case&#32;from&#32;the&#32;Best&#32;Practices&#32;tests&#32;checking&#32;if&#32;all&#32;the&#32;ranges&#32;and&#32;domains&#32;from&#32;the&#32;test&#32;subject&#32;point&#32;to&#32;terms&#32;that&#32;are&#32;defined&#32;in&#32;the&#32;vocabulary.|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-190)|Identifier|`domain-out-of-vocabulary`|
|[Section top](#pass-outcome-number-190)|Title|Domains&#32;properly&#32;defined|
|[Section top](#pass-outcome-number-190)|Description|Each&#32;rdfs:domain&#32;is&#32;defined&#32;within&#32;the&#32;fragment|

***
### Pass Outcome number 191

[Jump to summary definition](#summary-Pass-191)	|	[Previous Pass outcome](#pass-outcome-number-190)	|	[Next Pass outcome](#pass-outcome-number-192)

:white_check_mark:Pass outcome
#### Subject detail
|Name|module-affordances-ontology|
|----|----|
|Title|Standalone&#32;module&#32;core&#92;affordances&#92;ontology.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- https://gitlab.com/coswot/coswot-acimov/blob/HEAD/core/affordances/ontology.ttl|

#### Criterion detail
|Identifier|[domain-and-range-referencing](https://ns.inria.fr/olivaw#domain-and-range-referencing)|
|----|----|
|Title|Domain&#32;and&#32;range&#32;referencing&#32;test|
|Description|A&#32;test&#32;case&#32;from&#32;the&#32;Best&#32;Practices&#32;tests&#32;checking&#32;if&#32;all&#32;the&#32;ranges&#32;and&#32;domains&#32;from&#32;the&#32;test&#32;subject&#32;point&#32;to&#32;terms&#32;that&#32;are&#32;defined&#32;in&#32;the&#32;vocabulary.|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-191)|Identifier|`range-out-of-vocabulary`|
|[Section top](#pass-outcome-number-191)|Title|Ranges&#32;properly&#32;defined|
|[Section top](#pass-outcome-number-191)|Description|Each&#32;rdfs:range&#32;is&#32;defined&#32;within&#32;the&#32;fragment|

***
### Pass Outcome number 192

[Jump to summary definition](#summary-Pass-192)	|	[Previous Pass outcome](#pass-outcome-number-191)	|	[Next Pass outcome](#pass-outcome-number-193)

:white_check_mark:Pass outcome
#### Subject detail
|Name|module-affordances-ontology|
|----|----|
|Title|Standalone&#32;module&#32;core&#92;affordances&#92;ontology.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- https://gitlab.com/coswot/coswot-acimov/blob/HEAD/core/affordances/ontology.ttl|

#### Criterion detail
|Identifier|[labeled-terms](https://ns.inria.fr/olivaw#labeled-terms)|
|----|----|
|Title|Term&#32;labeling&#32;test|
|Description|A&#32;test&#32;case&#32;from&#32;the&#32;Best&#32;Practices&#32;tests&#32;checking&#32;if&#32;all&#32;the&#32;terms&#32;of&#32;the&#32;subject&#32;have&#32;a&#32;rdfs:label&#32;property&#32;pointing&#32;to&#32;a&#32;literal&#32;in&#32;English|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-192)|Identifier|`not-labeled-term`|
|[Section top](#pass-outcome-number-192)|Title|All&#32;terms&#32;labeled|
|[Section top](#pass-outcome-number-192)|Description|All&#32;the&#32;terms&#32;defined&#32;in&#32;the&#32;subject&#32;have&#32;a&#32;rdfs:label&#32;in&#32;English|

***
### Pass Outcome number 193

[Jump to summary definition](#summary-Pass-193)	|	[Previous Pass outcome](#pass-outcome-number-192)	|	[Next Pass outcome](#pass-outcome-number-194)

:white_check_mark:Pass outcome
#### Subject detail
|Name|module-affordances-ontology|
|----|----|
|Title|Standalone&#32;module&#32;core&#92;affordances&#92;ontology.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- https://gitlab.com/coswot/coswot-acimov/blob/HEAD/core/affordances/ontology.ttl|

#### Criterion detail
|Identifier|[owl-rl-constraint](https://ns.inria.fr/olivaw#owl-rl-constraint)|
|----|----|
|Title|OWL&#32;RL&#32;Constraint&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;check&#32;wether&#32;the&#32;test&#32;subject&#32;is&#32;syntaxically&#32;correct&#32;or&#32;not.|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-193)|Identifier|`owl-rl-constraint-violation`|
|[Section top](#pass-outcome-number-193)|Title|OWL&#32;RL&#32;consistent|
|[Section top](#pass-outcome-number-193)|Description|The&#32;provided&#32;graph&#32;is&#32;consistent&#32;for&#32;any&#32;OWL&#32;RL&#32;constraint|

***
### Pass Outcome number 194

[Jump to summary definition](#summary-Pass-194)	|	[Previous Pass outcome](#pass-outcome-number-193)	|	[Next Pass outcome](#pass-outcome-number-195)

:white_check_mark:Pass outcome
#### Subject detail
|Name|module-affordances-ontology|
|----|----|
|Title|Standalone&#32;module&#32;core&#92;affordances&#92;ontology.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- https://gitlab.com/coswot/coswot-acimov/blob/HEAD/core/affordances/ontology.ttl|

#### Criterion detail
|Identifier|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|
|----|----|
|Title|Profile&#32;compatibility&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;check&#32;whether&#32;the&#32;test&#32;subject&#32;is&#32;compatible&#32;with&#32;a&#32;profile&#32;or&#32;not,&#32;and&#32;if&#32;it&#32;is&#32;not,&#32;why.|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-194)|Identifier|`owl-el-profile-error`|
|[Section top](#pass-outcome-number-194)|Title|OWL&#32;EL&#32;Profile&#32;compatible|
|[Section top](#pass-outcome-number-194)|Description|The&#32;subject&#32;is&#32;included&#32;in&#32;the&#32;OWL&#32;EL&#32;sublanguage|

***
### Pass Outcome number 195

[Jump to summary definition](#summary-Pass-195)	|	[Previous Pass outcome](#pass-outcome-number-194)	|	[Next Pass outcome](#pass-outcome-number-196)

:white_check_mark:Pass outcome
#### Subject detail
|Name|module-affordances-ontology|
|----|----|
|Title|Standalone&#32;module&#32;core&#92;affordances&#92;ontology.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- https://gitlab.com/coswot/coswot-acimov/blob/HEAD/core/affordances/ontology.ttl|

#### Criterion detail
|Identifier|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|
|----|----|
|Title|Profile&#32;compatibility&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;check&#32;whether&#32;the&#32;test&#32;subject&#32;is&#32;compatible&#32;with&#32;a&#32;profile&#32;or&#32;not,&#32;and&#32;if&#32;it&#32;is&#32;not,&#32;why.|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-195)|Identifier|`owl-ql-profile-error`|
|[Section top](#pass-outcome-number-195)|Title|OWL&#32;QL&#32;Profile&#32;compatible|
|[Section top](#pass-outcome-number-195)|Description|The&#32;subject&#32;is&#32;included&#32;in&#32;the&#32;OWL&#32;QL&#32;sublanguage|

***
### Pass Outcome number 196

[Jump to summary definition](#summary-Pass-196)	|	[Previous Pass outcome](#pass-outcome-number-195)	|	[Next Pass outcome](#pass-outcome-number-197)

:white_check_mark:Pass outcome
#### Subject detail
|Name|module-affordances-ontology|
|----|----|
|Title|Standalone&#32;module&#32;core&#92;affordances&#92;ontology.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- https://gitlab.com/coswot/coswot-acimov/blob/HEAD/core/affordances/ontology.ttl|

#### Criterion detail
|Identifier|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|
|----|----|
|Title|Profile&#32;compatibility&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;check&#32;whether&#32;the&#32;test&#32;subject&#32;is&#32;compatible&#32;with&#32;a&#32;profile&#32;or&#32;not,&#32;and&#32;if&#32;it&#32;is&#32;not,&#32;why.|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-196)|Identifier|`owl-rl-profile-error`|
|[Section top](#pass-outcome-number-196)|Title|OWL&#32;RL&#32;Profile&#32;compatible|
|[Section top](#pass-outcome-number-196)|Description|The&#32;subject&#32;is&#32;included&#32;in&#32;the&#32;OWL&#32;RL&#32;sublanguage|

***
### Pass Outcome number 197

[Jump to summary definition](#summary-Pass-197)	|	[Previous Pass outcome](#pass-outcome-number-196)	|	[Next Pass outcome](#pass-outcome-number-198)

:white_check_mark:Pass outcome
#### Subject detail
|Name|module-affordances-ontology|
|----|----|
|Title|Standalone&#32;module&#32;core&#92;affordances&#92;ontology.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- https://gitlab.com/coswot/coswot-acimov/blob/HEAD/core/affordances/ontology.ttl|

#### Criterion detail
|Identifier|[proper-extension-predicate](https://ns.inria.fr/olivaw#proper-extension-predicate)|
|----|----|
|Title|Predicate&#32;extension&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;test&#32;the&#32;proper&#32;use&#32;of&#32;predicates&#32;rdfs:subClassOf&#32;and&#32;rdfs:subPropertyOf&#32;on&#32;the&#32;ontology&#32;terms|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-197)|Identifier|`class-subpropertyof`|
|[Section top](#pass-outcome-number-197)|Title|No&#32;class&#32;subproperty|
|[Section top](#pass-outcome-number-197)|Description|No&#32;ontology&#32;class&#32;is&#32;a&#32;subproperty|

***
### Pass Outcome number 198

[Jump to summary definition](#summary-Pass-198)	|	[Previous Pass outcome](#pass-outcome-number-197)	|	[Next Pass outcome](#pass-outcome-number-199)

:white_check_mark:Pass outcome
#### Subject detail
|Name|module-affordances-ontology|
|----|----|
|Title|Standalone&#32;module&#32;core&#92;affordances&#92;ontology.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- https://gitlab.com/coswot/coswot-acimov/blob/HEAD/core/affordances/ontology.ttl|

#### Criterion detail
|Identifier|[proper-extension-predicate](https://ns.inria.fr/olivaw#proper-extension-predicate)|
|----|----|
|Title|Predicate&#32;extension&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;test&#32;the&#32;proper&#32;use&#32;of&#32;predicates&#32;rdfs:subClassOf&#32;and&#32;rdfs:subPropertyOf&#32;on&#32;the&#32;ontology&#32;terms|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-198)|Identifier|`property-subclassof`|
|[Section top](#pass-outcome-number-198)|Title|No&#32;property&#32;subclass|
|[Section top](#pass-outcome-number-198)|Description|No&#32;ontology&#32;property&#32;is&#32;a&#32;subclass|

***
### Pass Outcome number 199

[Jump to summary definition](#summary-Pass-199)	|	[Previous Pass outcome](#pass-outcome-number-198)	|	[Next Pass outcome](#pass-outcome-number-200)

:white_check_mark:Pass outcome
#### Subject detail
|Name|module-affordances-ontology|
|----|----|
|Title|Standalone&#32;module&#32;core&#92;affordances&#92;ontology.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- https://gitlab.com/coswot/coswot-acimov/blob/HEAD/core/affordances/ontology.ttl|

#### Criterion detail
|Identifier|[proper-extension-predicate](https://ns.inria.fr/olivaw#proper-extension-predicate)|
|----|----|
|Title|Predicate&#32;extension&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;test&#32;the&#32;proper&#32;use&#32;of&#32;predicates&#32;rdfs:subClassOf&#32;and&#32;rdfs:subPropertyOf&#32;on&#32;the&#32;ontology&#32;terms|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-199)|Identifier|`subclassof-property`|
|[Section top](#pass-outcome-number-199)|Title|No&#32;subclass&#32;of&#32;property|
|[Section top](#pass-outcome-number-199)|Description|No&#32;ontology&#32;term&#32;is&#32;a&#32;subclass&#32;of&#32;a&#32;property|

***
### Pass Outcome number 200

[Jump to summary definition](#summary-Pass-200)	|	[Previous Pass outcome](#pass-outcome-number-199)	|	[Next Pass outcome](#pass-outcome-number-201)

:white_check_mark:Pass outcome
#### Subject detail
|Name|module-affordances-ontology|
|----|----|
|Title|Standalone&#32;module&#32;core&#92;affordances&#92;ontology.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- https://gitlab.com/coswot/coswot-acimov/blob/HEAD/core/affordances/ontology.ttl|

#### Criterion detail
|Identifier|[proper-extension-predicate](https://ns.inria.fr/olivaw#proper-extension-predicate)|
|----|----|
|Title|Predicate&#32;extension&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;test&#32;the&#32;proper&#32;use&#32;of&#32;predicates&#32;rdfs:subClassOf&#32;and&#32;rdfs:subPropertyOf&#32;on&#32;the&#32;ontology&#32;terms|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-200)|Identifier|`subpropertyof-class`|
|[Section top](#pass-outcome-number-200)|Title|No&#32;subproperty&#32;of&#32;class|
|[Section top](#pass-outcome-number-200)|Description|No&#32;ontology&#32;term&#32;is&#32;a&#32;subproperty&#32;of&#32;a&#32;class|

***
### Pass Outcome number 201

[Jump to summary definition](#summary-Pass-201)	|	[Previous Pass outcome](#pass-outcome-number-200)	|	[Next Pass outcome](#pass-outcome-number-202)

:white_check_mark:Pass outcome
#### Subject detail
|Name|module-affordances-ontology|
|----|----|
|Title|Standalone&#32;module&#32;core&#92;affordances&#92;ontology.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- https://gitlab.com/coswot/coswot-acimov/blob/HEAD/core/affordances/ontology.ttl|

#### Criterion detail
|Identifier|[term-referencing](https://ns.inria.fr/olivaw#term-referencing)|
|----|----|
|Title|Term&#32;referencing&#32;test|
|Description|A&#32;test&#32;case&#32;from&#32;the&#32;Best&#32;Practices&#32;tests&#32;checking&#32;if&#32;each&#32;term&#32;of&#32;the&#32;test&#32;subject&#32;is&#32;referenced&#32;to&#32;a&#32;module&#32;through&#32;a&#32;rdfs:isDefinedBy&#32;property.|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-201)|Identifier|`no-reference-module`|
|[Section top](#pass-outcome-number-201)|Title|Any&#32;term&#32;is&#32;referenced|
|[Section top](#pass-outcome-number-201)|Description|Each&#32;term&#32;of&#32;the&#32;test&#32;subject&#32;is&#32;linked&#32;to&#32;a&#32;module&#32;by&#32;a&#32;rdfs:isDefinedBy&#32;property|

***
### Pass Outcome number 202

[Jump to summary definition](#summary-Pass-202)	|	[Previous Pass outcome](#pass-outcome-number-201)	|	[Next Pass outcome](#pass-outcome-number-203)

:white_check_mark:Pass outcome
#### Subject detail
|Name|module-affordances-ontology|
|----|----|
|Title|Standalone&#32;module&#32;core&#92;affordances&#92;ontology.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- https://gitlab.com/coswot/coswot-acimov/blob/HEAD/core/affordances/ontology.ttl|

#### Criterion detail
|Identifier|[terms-differenciation](https://ns.inria.fr/olivaw#terms-differenciation)|
|----|----|
|Title|Terms&#32;differenciation&#32;test|
|Description|A&#32;test&#32;case&#32;from&#32;the&#32;Best&#32;Practices&#32;tests&#32;checking&#32;if&#32;all&#32;the&#32;terms&#32;are&#32;different&#32;enough&#32;from&#32;each&#32;other&#32;according&#32;to&#32;the&#32;Levenshtein&#32;distance&#32;metric.|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-202)|Identifier|`too-close-terms`|
|[Section top](#pass-outcome-number-202)|Title|Terms&#32;differenciated&#32;enough|
|[Section top](#pass-outcome-number-202)|Description|All&#32;the&#32;terms&#32;have&#32;have&#32;a&#32;satisfying&#32;Levenshtein&#32;distance&#32;from&#32;each&#32;other&#32;term.|

***
### Pass Outcome number 203

[Jump to summary definition](#summary-Pass-203)	|	[Previous Pass outcome](#pass-outcome-number-202)	|	[Next Pass outcome](#pass-outcome-number-204)

:white_check_mark:Pass outcome
#### Subject detail
|Name|module-actuations-ontology|
|----|----|
|Title|Standalone&#32;module&#32;core&#92;actuations&#92;ontology.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- https://gitlab.com/coswot/coswot-acimov/blob/HEAD/core/actuations/ontology.ttl|

#### Criterion detail
|Identifier|[domain-and-range-referencing](https://ns.inria.fr/olivaw#domain-and-range-referencing)|
|----|----|
|Title|Domain&#32;and&#32;range&#32;referencing&#32;test|
|Description|A&#32;test&#32;case&#32;from&#32;the&#32;Best&#32;Practices&#32;tests&#32;checking&#32;if&#32;all&#32;the&#32;ranges&#32;and&#32;domains&#32;from&#32;the&#32;test&#32;subject&#32;point&#32;to&#32;terms&#32;that&#32;are&#32;defined&#32;in&#32;the&#32;vocabulary.|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-203)|Identifier|`domain-out-of-vocabulary`|
|[Section top](#pass-outcome-number-203)|Title|Domains&#32;properly&#32;defined|
|[Section top](#pass-outcome-number-203)|Description|Each&#32;rdfs:domain&#32;is&#32;defined&#32;within&#32;the&#32;fragment|

***
### Pass Outcome number 204

[Jump to summary definition](#summary-Pass-204)	|	[Previous Pass outcome](#pass-outcome-number-203)	|	[Next Pass outcome](#pass-outcome-number-205)

:white_check_mark:Pass outcome
#### Subject detail
|Name|module-actuations-ontology|
|----|----|
|Title|Standalone&#32;module&#32;core&#92;actuations&#92;ontology.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- https://gitlab.com/coswot/coswot-acimov/blob/HEAD/core/actuations/ontology.ttl|

#### Criterion detail
|Identifier|[domain-and-range-referencing](https://ns.inria.fr/olivaw#domain-and-range-referencing)|
|----|----|
|Title|Domain&#32;and&#32;range&#32;referencing&#32;test|
|Description|A&#32;test&#32;case&#32;from&#32;the&#32;Best&#32;Practices&#32;tests&#32;checking&#32;if&#32;all&#32;the&#32;ranges&#32;and&#32;domains&#32;from&#32;the&#32;test&#32;subject&#32;point&#32;to&#32;terms&#32;that&#32;are&#32;defined&#32;in&#32;the&#32;vocabulary.|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-204)|Identifier|`range-out-of-vocabulary`|
|[Section top](#pass-outcome-number-204)|Title|Ranges&#32;properly&#32;defined|
|[Section top](#pass-outcome-number-204)|Description|Each&#32;rdfs:range&#32;is&#32;defined&#32;within&#32;the&#32;fragment|

***
### Pass Outcome number 205

[Jump to summary definition](#summary-Pass-205)	|	[Previous Pass outcome](#pass-outcome-number-204)	|	[Next Pass outcome](#pass-outcome-number-206)

:white_check_mark:Pass outcome
#### Subject detail
|Name|module-actuations-ontology|
|----|----|
|Title|Standalone&#32;module&#32;core&#92;actuations&#92;ontology.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- https://gitlab.com/coswot/coswot-acimov/blob/HEAD/core/actuations/ontology.ttl|

#### Criterion detail
|Identifier|[labeled-terms](https://ns.inria.fr/olivaw#labeled-terms)|
|----|----|
|Title|Term&#32;labeling&#32;test|
|Description|A&#32;test&#32;case&#32;from&#32;the&#32;Best&#32;Practices&#32;tests&#32;checking&#32;if&#32;all&#32;the&#32;terms&#32;of&#32;the&#32;subject&#32;have&#32;a&#32;rdfs:label&#32;property&#32;pointing&#32;to&#32;a&#32;literal&#32;in&#32;English|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-205)|Identifier|`not-labeled-term`|
|[Section top](#pass-outcome-number-205)|Title|All&#32;terms&#32;labeled|
|[Section top](#pass-outcome-number-205)|Description|All&#32;the&#32;terms&#32;defined&#32;in&#32;the&#32;subject&#32;have&#32;a&#32;rdfs:label&#32;in&#32;English|

***
### Pass Outcome number 206

[Jump to summary definition](#summary-Pass-206)	|	[Previous Pass outcome](#pass-outcome-number-205)	|	[Next Pass outcome](#pass-outcome-number-207)

:white_check_mark:Pass outcome
#### Subject detail
|Name|module-actuations-ontology|
|----|----|
|Title|Standalone&#32;module&#32;core&#92;actuations&#92;ontology.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- https://gitlab.com/coswot/coswot-acimov/blob/HEAD/core/actuations/ontology.ttl|

#### Criterion detail
|Identifier|[owl-rl-constraint](https://ns.inria.fr/olivaw#owl-rl-constraint)|
|----|----|
|Title|OWL&#32;RL&#32;Constraint&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;check&#32;wether&#32;the&#32;test&#32;subject&#32;is&#32;syntaxically&#32;correct&#32;or&#32;not.|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-206)|Identifier|`owl-rl-constraint-violation`|
|[Section top](#pass-outcome-number-206)|Title|OWL&#32;RL&#32;consistent|
|[Section top](#pass-outcome-number-206)|Description|The&#32;provided&#32;graph&#32;is&#32;consistent&#32;for&#32;any&#32;OWL&#32;RL&#32;constraint|

***
### Pass Outcome number 207

[Jump to summary definition](#summary-Pass-207)	|	[Previous Pass outcome](#pass-outcome-number-206)	|	[Next Pass outcome](#pass-outcome-number-208)

:white_check_mark:Pass outcome
#### Subject detail
|Name|module-actuations-ontology|
|----|----|
|Title|Standalone&#32;module&#32;core&#92;actuations&#92;ontology.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- https://gitlab.com/coswot/coswot-acimov/blob/HEAD/core/actuations/ontology.ttl|

#### Criterion detail
|Identifier|[proper-extension-predicate](https://ns.inria.fr/olivaw#proper-extension-predicate)|
|----|----|
|Title|Predicate&#32;extension&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;test&#32;the&#32;proper&#32;use&#32;of&#32;predicates&#32;rdfs:subClassOf&#32;and&#32;rdfs:subPropertyOf&#32;on&#32;the&#32;ontology&#32;terms|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-207)|Identifier|`class-subpropertyof`|
|[Section top](#pass-outcome-number-207)|Title|No&#32;class&#32;subproperty|
|[Section top](#pass-outcome-number-207)|Description|No&#32;ontology&#32;class&#32;is&#32;a&#32;subproperty|

***
### Pass Outcome number 208

[Jump to summary definition](#summary-Pass-208)	|	[Previous Pass outcome](#pass-outcome-number-207)	|	[Next Pass outcome](#pass-outcome-number-209)

:white_check_mark:Pass outcome
#### Subject detail
|Name|module-actuations-ontology|
|----|----|
|Title|Standalone&#32;module&#32;core&#92;actuations&#92;ontology.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- https://gitlab.com/coswot/coswot-acimov/blob/HEAD/core/actuations/ontology.ttl|

#### Criterion detail
|Identifier|[proper-extension-predicate](https://ns.inria.fr/olivaw#proper-extension-predicate)|
|----|----|
|Title|Predicate&#32;extension&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;test&#32;the&#32;proper&#32;use&#32;of&#32;predicates&#32;rdfs:subClassOf&#32;and&#32;rdfs:subPropertyOf&#32;on&#32;the&#32;ontology&#32;terms|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-208)|Identifier|`property-subclassof`|
|[Section top](#pass-outcome-number-208)|Title|No&#32;property&#32;subclass|
|[Section top](#pass-outcome-number-208)|Description|No&#32;ontology&#32;property&#32;is&#32;a&#32;subclass|

***
### Pass Outcome number 209

[Jump to summary definition](#summary-Pass-209)	|	[Previous Pass outcome](#pass-outcome-number-208)	|	[Next Pass outcome](#pass-outcome-number-210)

:white_check_mark:Pass outcome
#### Subject detail
|Name|module-actuations-ontology|
|----|----|
|Title|Standalone&#32;module&#32;core&#92;actuations&#92;ontology.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- https://gitlab.com/coswot/coswot-acimov/blob/HEAD/core/actuations/ontology.ttl|

#### Criterion detail
|Identifier|[proper-extension-predicate](https://ns.inria.fr/olivaw#proper-extension-predicate)|
|----|----|
|Title|Predicate&#32;extension&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;test&#32;the&#32;proper&#32;use&#32;of&#32;predicates&#32;rdfs:subClassOf&#32;and&#32;rdfs:subPropertyOf&#32;on&#32;the&#32;ontology&#32;terms|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-209)|Identifier|`subclassof-property`|
|[Section top](#pass-outcome-number-209)|Title|No&#32;subclass&#32;of&#32;property|
|[Section top](#pass-outcome-number-209)|Description|No&#32;ontology&#32;term&#32;is&#32;a&#32;subclass&#32;of&#32;a&#32;property|

***
### Pass Outcome number 210

[Jump to summary definition](#summary-Pass-210)	|	[Previous Pass outcome](#pass-outcome-number-209)	|	[Next Pass outcome](#pass-outcome-number-211)

:white_check_mark:Pass outcome
#### Subject detail
|Name|module-actuations-ontology|
|----|----|
|Title|Standalone&#32;module&#32;core&#92;actuations&#92;ontology.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- https://gitlab.com/coswot/coswot-acimov/blob/HEAD/core/actuations/ontology.ttl|

#### Criterion detail
|Identifier|[proper-extension-predicate](https://ns.inria.fr/olivaw#proper-extension-predicate)|
|----|----|
|Title|Predicate&#32;extension&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;test&#32;the&#32;proper&#32;use&#32;of&#32;predicates&#32;rdfs:subClassOf&#32;and&#32;rdfs:subPropertyOf&#32;on&#32;the&#32;ontology&#32;terms|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-210)|Identifier|`subpropertyof-class`|
|[Section top](#pass-outcome-number-210)|Title|No&#32;subproperty&#32;of&#32;class|
|[Section top](#pass-outcome-number-210)|Description|No&#32;ontology&#32;term&#32;is&#32;a&#32;subproperty&#32;of&#32;a&#32;class|

***
### Pass Outcome number 211

[Jump to summary definition](#summary-Pass-211)	|	[Previous Pass outcome](#pass-outcome-number-210)	|	Next Pass outcome

:white_check_mark:Pass outcome
#### Subject detail
|Name|module-actuations-ontology|
|----|----|
|Title|Standalone&#32;module&#32;core&#92;actuations&#92;ontology.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- https://gitlab.com/coswot/coswot-acimov/blob/HEAD/core/actuations/ontology.ttl|

#### Criterion detail
|Identifier|[term-referencing](https://ns.inria.fr/olivaw#term-referencing)|
|----|----|
|Title|Term&#32;referencing&#32;test|
|Description|A&#32;test&#32;case&#32;from&#32;the&#32;Best&#32;Practices&#32;tests&#32;checking&#32;if&#32;each&#32;term&#32;of&#32;the&#32;test&#32;subject&#32;is&#32;referenced&#32;to&#32;a&#32;module&#32;through&#32;a&#32;rdfs:isDefinedBy&#32;property.|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-211)|Identifier|`no-reference-module`|
|[Section top](#pass-outcome-number-211)|Title|Any&#32;term&#32;is&#32;referenced|
|[Section top](#pass-outcome-number-211)|Description|Each&#32;term&#32;of&#32;the&#32;test&#32;subject&#32;is&#32;linked&#32;to&#32;a&#32;module&#32;by&#32;a&#32;rdfs:isDefinedBy&#32;property|

***

</details>

***
