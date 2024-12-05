# Test Report Markdown Export

This file is an export of the RDF test report made out of [EARL vocabulary](https://www.w3.org/TR/EARL10/)

This test is powered by Corese, check the [website](https://project.inria.fr/corese/) and the [repository](https://github.com/Wimmics/corese)

The original test report is available in turtle syntax [here](./model-test-manual-NicoRobertIn-2024-12-05T15-00-47.ttl).

# Test Activity

Here is some information about the testing activity that led to this report

|Title|Model&#32;tests&#32;of&#32;[coswot/coswot-acimov](https://gitlab.com/coswot/coswot-acimov)&#32;on&#32;branch&#32;HEAD|
|--|--|
|Description|[NicoRobertIn](https://gitlab.com/NicoRobertIn)&#32;launch&#32;manual&#32;run&#32;of&#32;model&#32;tests&#32;against&#32;[coswot/coswot-acimov](https://gitlab.com/coswot/coswot-acimov)&#32;on&#32;branch&#32;HEAD|
|Tester|[NicoRobertIn](https://gitlab.com/NicoRobertIn)|
|Ontology|[coswot/coswot-acimov](https://gitlab.com/coswot/coswot-acimov)|
|Ontology version|Local state `59ebb02c5380cf2f3920327824a7f596b3c9ab3d`|
|Ontology version date|2024-12-05 15:00:26|
|Ontology previous version|[daf15cf7a12a78e0b00c5ae2de74709ae5b6e87f](https://gitlab.com/coswot/coswot-acimov/tree/daf15cf7a12a78e0b00c5ae2de74709ae5b6e87f)|
|Ontology branch|[HEAD](https://gitlab.com/coswot/coswot-acimov/tree/HEAD)|
|Olivaw suite|[olivaw model test suite](https://github.com/Wimmics/olivaw/blob/v0.0.6/olivaw/test/model/suite.py)|
|Olivaw version|[v0.0.6](https://pypi.org/project/olivaw/0.0.6)|
|Generated turtle|[Turtle report](./model-test-manual-NicoRobertIn-2024-12-05T15-00-47.ttl)|
|Generated Markdown|[Markdown report](./model-test-manual-NicoRobertIn-2024-12-05T15-00-47.md)|

# Statistic summary

Here is a short overview for this test report

168 Outcomes

:boom:1 MajorFail, :exclamation:167 MinorFail, :warning:0 CannotTell, :grey_question:0 NotTested, :white_check_mark:0 Pass

<div  style="border-radius: 12px; height: 25px; overflow: hidden"><img src="../assets/red.png" width="1%" height="25px"/><img src="../assets/orange.png" width="99%" height="25px"/><img src="../assets/grey.png" width="0%" height="25px"/><img src="../assets/white.png" width="0%" height="25px"/><img src="../assets/green.png" width="0%" height="25px"/></div>

<br/>

The different status types are an extension of the [EARL](https://www.w3.org/TR/EARL10-Schema/) vocabulary where the nextended terms can be found in the [olivaw ontology](https://ns.inria.fr/olivaw#), each outcome type means:
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
|[Chapter top](#majorfail-outcomes)|<div id="summary-MajorFail-1">1/1</div>|:boom:MajorFail|`module-src-coswot-saref`|[syntax](https://ns.inria.fr/olivaw#syntax)|Test subject has syntax errors|[Jump](#majorfail-outcome-number-1)|

***

## MajorFail Outcomes Details

This subchapter gives more details to the :boom:MajorFail outcomes

### MajorFail Outcome number 1

[Jump to summary definition](#summary-MajorFail-1)	|	Previous MajorFail outcome	|	Next MajorFail outcome

:boom:MajorFail outcome
#### Subject detail
|Name|module-src-coswot-saref|
|----|----|
|Title|Standalone&#32;module&#32;src/coswot-saref.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Module coswot-saref](https://gitlab.com/coswot/coswot-acimov/blob/HEAD/src/coswot-saref.ttl)|

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

[Jump to statistic summary](#statistic-summary)	|	[Previous section](#majorfail-outcomes)	|	Next section

Here is the chapter related to the MinorFail outcome

:exclamation:167 MinorFail outcomes

<details>
<summary>Fold/Unfold the 167 summary and details</summary>

## MinorFail Outcomes Summary

:exclamation:167 MinorFail outcomes

|*Jump*|*Number*|*Status*|*Subject*|*Criterion*|*Title*|*Link*|
|------|--------|--------|---------|-----------|-------|------|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-1">1/167</div>|:exclamation:MinorFail|`module-src-systems-ontology`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL EL Profile incompatible|[Jump](#minorfail-outcome-number-1)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-2">2/167</div>|:exclamation:MinorFail|`module-src-systems-ontology`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL QL Profile incompatible|[Jump](#minorfail-outcome-number-2)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-3">3/167</div>|:exclamation:MinorFail|`module-src-systems-ontology`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL RL Profile incompatible|[Jump](#minorfail-outcome-number-3)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-4">4/167</div>|:exclamation:MinorFail|`module-src-systems-ontology`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL RL Profile incompatible|[Jump](#minorfail-outcome-number-4)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-5">5/167</div>|:exclamation:MinorFail|`module-src-states-ontology-catalog`|[domain-and-range-referencing](https://ns.inria.fr/olivaw#domain-and-range-referencing)|Domain out of vocabulary|[Jump](#minorfail-outcome-number-5)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-6">6/167</div>|:exclamation:MinorFail|`module-src-states-ontology-catalog`|[domain-and-range-referencing](https://ns.inria.fr/olivaw#domain-and-range-referencing)|Range out of vocabulary|[Jump](#minorfail-outcome-number-6)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-7">7/167</div>|:exclamation:MinorFail|`module-src-states-ontology-catalog`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL EL Profile incompatible|[Jump](#minorfail-outcome-number-7)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-8">8/167</div>|:exclamation:MinorFail|`module-src-states-ontology-catalog`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL EL Profile incompatible|[Jump](#minorfail-outcome-number-8)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-9">9/167</div>|:exclamation:MinorFail|`module-src-states-ontology-catalog`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL QL Profile incompatible|[Jump](#minorfail-outcome-number-9)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-10">10/167</div>|:exclamation:MinorFail|`module-src-states-ontology-catalog`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL QL Profile incompatible|[Jump](#minorfail-outcome-number-10)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-11">11/167</div>|:exclamation:MinorFail|`module-src-states-ontology-catalog`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL QL Profile incompatible|[Jump](#minorfail-outcome-number-11)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-12">12/167</div>|:exclamation:MinorFail|`module-src-states-ontology`|[domain-and-range-referencing](https://ns.inria.fr/olivaw#domain-and-range-referencing)|Domain out of vocabulary|[Jump](#minorfail-outcome-number-12)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-13">13/167</div>|:exclamation:MinorFail|`module-src-states-ontology`|[domain-and-range-referencing](https://ns.inria.fr/olivaw#domain-and-range-referencing)|Range out of vocabulary|[Jump](#minorfail-outcome-number-13)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-14">14/167</div>|:exclamation:MinorFail|`module-src-states-ontology`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL EL Profile incompatible|[Jump](#minorfail-outcome-number-14)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-15">15/167</div>|:exclamation:MinorFail|`module-src-states-ontology`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL EL Profile incompatible|[Jump](#minorfail-outcome-number-15)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-16">16/167</div>|:exclamation:MinorFail|`module-src-states-ontology`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL EL Profile incompatible|[Jump](#minorfail-outcome-number-16)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-17">17/167</div>|:exclamation:MinorFail|`module-src-states-ontology`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL EL Profile incompatible|[Jump](#minorfail-outcome-number-17)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-18">18/167</div>|:exclamation:MinorFail|`module-src-states-ontology`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL QL Profile incompatible|[Jump](#minorfail-outcome-number-18)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-19">19/167</div>|:exclamation:MinorFail|`module-src-states-ontology`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL QL Profile incompatible|[Jump](#minorfail-outcome-number-19)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-20">20/167</div>|:exclamation:MinorFail|`module-src-states-ontology`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL QL Profile incompatible|[Jump](#minorfail-outcome-number-20)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-21">21/167</div>|:exclamation:MinorFail|`module-src-states-ontology`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL QL Profile incompatible|[Jump](#minorfail-outcome-number-21)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-22">22/167</div>|:exclamation:MinorFail|`module-src-states-ontology`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL QL Profile incompatible|[Jump](#minorfail-outcome-number-22)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-23">23/167</div>|:exclamation:MinorFail|`module-src-states-ontology`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL QL Profile incompatible|[Jump](#minorfail-outcome-number-23)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-24">24/167</div>|:exclamation:MinorFail|`module-src-states-ontology`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL RL Profile incompatible|[Jump](#minorfail-outcome-number-24)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-25">25/167</div>|:exclamation:MinorFail|`module-src-states-ontology`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL RL Profile incompatible|[Jump](#minorfail-outcome-number-25)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-26">26/167</div>|:exclamation:MinorFail|`module-src-states-ontology`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL RL Profile incompatible|[Jump](#minorfail-outcome-number-26)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-27">27/167</div>|:exclamation:MinorFail|`module-src-states-ontology`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL RL Profile incompatible|[Jump](#minorfail-outcome-number-27)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-28">28/167</div>|:exclamation:MinorFail|`module-src-services-operations-ontology`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL EL Profile incompatible|[Jump](#minorfail-outcome-number-28)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-29">29/167</div>|:exclamation:MinorFail|`module-src-services-operations-ontology`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL EL Profile incompatible|[Jump](#minorfail-outcome-number-29)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-30">30/167</div>|:exclamation:MinorFail|`module-src-services-operations-ontology`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL EL Profile incompatible|[Jump](#minorfail-outcome-number-30)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-31">31/167</div>|:exclamation:MinorFail|`module-src-services-operations-ontology`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL EL Profile incompatible|[Jump](#minorfail-outcome-number-31)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-32">32/167</div>|:exclamation:MinorFail|`module-src-services-operations-ontology`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL QL Profile incompatible|[Jump](#minorfail-outcome-number-32)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-33">33/167</div>|:exclamation:MinorFail|`module-src-services-operations-ontology`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL QL Profile incompatible|[Jump](#minorfail-outcome-number-33)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-34">34/167</div>|:exclamation:MinorFail|`module-src-services-operations-ontology`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL QL Profile incompatible|[Jump](#minorfail-outcome-number-34)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-35">35/167</div>|:exclamation:MinorFail|`module-src-services-operations-ontology`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL QL Profile incompatible|[Jump](#minorfail-outcome-number-35)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-36">36/167</div>|:exclamation:MinorFail|`module-src-services-operations-ontology`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL QL Profile incompatible|[Jump](#minorfail-outcome-number-36)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-37">37/167</div>|:exclamation:MinorFail|`module-src-services-operations-ontology`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL RL Profile incompatible|[Jump](#minorfail-outcome-number-37)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-38">38/167</div>|:exclamation:MinorFail|`module-src-services-operations-ontology`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL RL Profile incompatible|[Jump](#minorfail-outcome-number-38)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-39">39/167</div>|:exclamation:MinorFail|`module-src-services-operations-ontology`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL RL Profile incompatible|[Jump](#minorfail-outcome-number-39)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-40">40/167</div>|:exclamation:MinorFail|`module-src-services-operations-ontology`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL RL Profile incompatible|[Jump](#minorfail-outcome-number-40)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-41">41/167</div>|:exclamation:MinorFail|`module-src-services-operations-ontology`|[term-referencing](https://ns.inria.fr/olivaw#term-referencing)|Term not referenced to a module|[Jump](#minorfail-outcome-number-41)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-42">42/167</div>|:exclamation:MinorFail|`module-src-samples-ontology`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL EL Profile incompatible|[Jump](#minorfail-outcome-number-42)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-43">43/167</div>|:exclamation:MinorFail|`module-src-samples-ontology`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL QL Profile incompatible|[Jump](#minorfail-outcome-number-43)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-44">44/167</div>|:exclamation:MinorFail|`module-src-samples-ontology`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL QL Profile incompatible|[Jump](#minorfail-outcome-number-44)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-45">45/167</div>|:exclamation:MinorFail|`module-src-property-values-ontology`|[domain-and-range-referencing](https://ns.inria.fr/olivaw#domain-and-range-referencing)|Range out of vocabulary|[Jump](#minorfail-outcome-number-45)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-46">46/167</div>|:exclamation:MinorFail|`module-src-property-values-ontology`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL EL Profile incompatible|[Jump](#minorfail-outcome-number-46)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-47">47/167</div>|:exclamation:MinorFail|`module-src-property-values-ontology`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL EL Profile incompatible|[Jump](#minorfail-outcome-number-47)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-48">48/167</div>|:exclamation:MinorFail|`module-src-property-values-ontology`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL EL Profile incompatible|[Jump](#minorfail-outcome-number-48)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-49">49/167</div>|:exclamation:MinorFail|`module-src-property-values-ontology`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL QL Profile incompatible|[Jump](#minorfail-outcome-number-49)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-50">50/167</div>|:exclamation:MinorFail|`module-src-property-values-ontology`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL QL Profile incompatible|[Jump](#minorfail-outcome-number-50)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-51">51/167</div>|:exclamation:MinorFail|`module-src-property-values-ontology`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL QL Profile incompatible|[Jump](#minorfail-outcome-number-51)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-52">52/167</div>|:exclamation:MinorFail|`module-src-property-values-ontology`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL QL Profile incompatible|[Jump](#minorfail-outcome-number-52)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-53">53/167</div>|:exclamation:MinorFail|`module-src-property-values-ontology`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL RL Profile incompatible|[Jump](#minorfail-outcome-number-53)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-54">54/167</div>|:exclamation:MinorFail|`module-src-property-values-ontology`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL RL Profile incompatible|[Jump](#minorfail-outcome-number-54)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-55">55/167</div>|:exclamation:MinorFail|`module-src-property-values-ontology`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL RL Profile incompatible|[Jump](#minorfail-outcome-number-55)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-56">56/167</div>|:exclamation:MinorFail|`module-src-properties-ontology-catalogs`|[domain-and-range-referencing](https://ns.inria.fr/olivaw#domain-and-range-referencing)|Domain out of vocabulary|[Jump](#minorfail-outcome-number-56)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-57">57/167</div>|:exclamation:MinorFail|`module-src-properties-ontology-catalogs`|[domain-and-range-referencing](https://ns.inria.fr/olivaw#domain-and-range-referencing)|Range out of vocabulary|[Jump](#minorfail-outcome-number-57)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-58">58/167</div>|:exclamation:MinorFail|`module-src-properties-ontology-catalogs`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL EL Profile incompatible|[Jump](#minorfail-outcome-number-58)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-59">59/167</div>|:exclamation:MinorFail|`module-src-properties-ontology-catalogs`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL EL Profile incompatible|[Jump](#minorfail-outcome-number-59)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-60">60/167</div>|:exclamation:MinorFail|`module-src-properties-ontology-catalogs`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL QL Profile incompatible|[Jump](#minorfail-outcome-number-60)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-61">61/167</div>|:exclamation:MinorFail|`module-src-properties-ontology-catalogs`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL QL Profile incompatible|[Jump](#minorfail-outcome-number-61)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-62">62/167</div>|:exclamation:MinorFail|`module-src-properties-ontology-catalogs`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL QL Profile incompatible|[Jump](#minorfail-outcome-number-62)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-63">63/167</div>|:exclamation:MinorFail|`module-src-properties-ontology`|[domain-and-range-referencing](https://ns.inria.fr/olivaw#domain-and-range-referencing)|Domain out of vocabulary|[Jump](#minorfail-outcome-number-63)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-64">64/167</div>|:exclamation:MinorFail|`module-src-properties-ontology`|[domain-and-range-referencing](https://ns.inria.fr/olivaw#domain-and-range-referencing)|Range out of vocabulary|[Jump](#minorfail-outcome-number-64)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-65">65/167</div>|:exclamation:MinorFail|`module-src-properties-ontology`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL EL Profile incompatible|[Jump](#minorfail-outcome-number-65)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-66">66/167</div>|:exclamation:MinorFail|`module-src-properties-ontology`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL EL Profile incompatible|[Jump](#minorfail-outcome-number-66)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-67">67/167</div>|:exclamation:MinorFail|`module-src-properties-ontology`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL EL Profile incompatible|[Jump](#minorfail-outcome-number-67)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-68">68/167</div>|:exclamation:MinorFail|`module-src-properties-ontology`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL QL Profile incompatible|[Jump](#minorfail-outcome-number-68)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-69">69/167</div>|:exclamation:MinorFail|`module-src-properties-ontology`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL QL Profile incompatible|[Jump](#minorfail-outcome-number-69)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-70">70/167</div>|:exclamation:MinorFail|`module-src-properties-ontology`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL QL Profile incompatible|[Jump](#minorfail-outcome-number-70)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-71">71/167</div>|:exclamation:MinorFail|`module-src-properties-ontology`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL QL Profile incompatible|[Jump](#minorfail-outcome-number-71)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-72">72/167</div>|:exclamation:MinorFail|`module-src-properties-ontology`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL RL Profile incompatible|[Jump](#minorfail-outcome-number-72)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-73">73/167</div>|:exclamation:MinorFail|`module-src-properties-ontology`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL RL Profile incompatible|[Jump](#minorfail-outcome-number-73)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-74">74/167</div>|:exclamation:MinorFail|`module-src-properties-ontology`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL RL Profile incompatible|[Jump](#minorfail-outcome-number-74)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-75">75/167</div>|:exclamation:MinorFail|`module-src-procedures-ontology`|[domain-and-range-referencing](https://ns.inria.fr/olivaw#domain-and-range-referencing)|Range out of vocabulary|[Jump](#minorfail-outcome-number-75)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-76">76/167</div>|:exclamation:MinorFail|`module-src-procedures-ontology`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL EL Profile incompatible|[Jump](#minorfail-outcome-number-76)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-77">77/167</div>|:exclamation:MinorFail|`module-src-procedures-ontology`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL EL Profile incompatible|[Jump](#minorfail-outcome-number-77)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-78">78/167</div>|:exclamation:MinorFail|`module-src-procedures-ontology`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL QL Profile incompatible|[Jump](#minorfail-outcome-number-78)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-79">79/167</div>|:exclamation:MinorFail|`module-src-procedures-ontology`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL QL Profile incompatible|[Jump](#minorfail-outcome-number-79)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-80">80/167</div>|:exclamation:MinorFail|`module-src-procedures-ontology`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL QL Profile incompatible|[Jump](#minorfail-outcome-number-80)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-81">81/167</div>|:exclamation:MinorFail|`module-src-procedures-ontology`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL RL Profile incompatible|[Jump](#minorfail-outcome-number-81)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-82">82/167</div>|:exclamation:MinorFail|`module-src-procedures-ontology`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL RL Profile incompatible|[Jump](#minorfail-outcome-number-82)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-83">83/167</div>|:exclamation:MinorFail|`module-src-observations-ontology`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL EL Profile incompatible|[Jump](#minorfail-outcome-number-83)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-84">84/167</div>|:exclamation:MinorFail|`module-src-observations-ontology`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL EL Profile incompatible|[Jump](#minorfail-outcome-number-84)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-85">85/167</div>|:exclamation:MinorFail|`module-src-observations-ontology`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL EL Profile incompatible|[Jump](#minorfail-outcome-number-85)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-86">86/167</div>|:exclamation:MinorFail|`module-src-observations-ontology`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL EL Profile incompatible|[Jump](#minorfail-outcome-number-86)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-87">87/167</div>|:exclamation:MinorFail|`module-src-observations-ontology`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL QL Profile incompatible|[Jump](#minorfail-outcome-number-87)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-88">88/167</div>|:exclamation:MinorFail|`module-src-observations-ontology`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL QL Profile incompatible|[Jump](#minorfail-outcome-number-88)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-89">89/167</div>|:exclamation:MinorFail|`module-src-observations-ontology`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL QL Profile incompatible|[Jump](#minorfail-outcome-number-89)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-90">90/167</div>|:exclamation:MinorFail|`module-src-observations-ontology`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL QL Profile incompatible|[Jump](#minorfail-outcome-number-90)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-91">91/167</div>|:exclamation:MinorFail|`module-src-observations-ontology`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL RL Profile incompatible|[Jump](#minorfail-outcome-number-91)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-92">92/167</div>|:exclamation:MinorFail|`module-src-observations-ontology`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL RL Profile incompatible|[Jump](#minorfail-outcome-number-92)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-93">93/167</div>|:exclamation:MinorFail|`module-src-observations-ontology`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL RL Profile incompatible|[Jump](#minorfail-outcome-number-93)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-94">94/167</div>|:exclamation:MinorFail|`module-src-observations-ontology`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL RL Profile incompatible|[Jump](#minorfail-outcome-number-94)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-95">95/167</div>|:exclamation:MinorFail|`module-src-functions-commands-ontology`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL EL Profile incompatible|[Jump](#minorfail-outcome-number-95)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-96">96/167</div>|:exclamation:MinorFail|`module-src-functions-commands-ontology`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL EL Profile incompatible|[Jump](#minorfail-outcome-number-96)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-97">97/167</div>|:exclamation:MinorFail|`module-src-functions-commands-ontology`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL EL Profile incompatible|[Jump](#minorfail-outcome-number-97)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-98">98/167</div>|:exclamation:MinorFail|`module-src-functions-commands-ontology`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL QL Profile incompatible|[Jump](#minorfail-outcome-number-98)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-99">99/167</div>|:exclamation:MinorFail|`module-src-functions-commands-ontology`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL QL Profile incompatible|[Jump](#minorfail-outcome-number-99)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-100">100/167</div>|:exclamation:MinorFail|`module-src-functions-commands-ontology`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL QL Profile incompatible|[Jump](#minorfail-outcome-number-100)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-101">101/167</div>|:exclamation:MinorFail|`module-src-functions-commands-ontology`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL QL Profile incompatible|[Jump](#minorfail-outcome-number-101)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-102">102/167</div>|:exclamation:MinorFail|`module-src-functions-commands-ontology`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL RL Profile incompatible|[Jump](#minorfail-outcome-number-102)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-103">103/167</div>|:exclamation:MinorFail|`module-src-functions-commands-ontology`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL RL Profile incompatible|[Jump](#minorfail-outcome-number-103)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-104">104/167</div>|:exclamation:MinorFail|`module-src-functions-commands-ontology`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL RL Profile incompatible|[Jump](#minorfail-outcome-number-104)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-105">105/167</div>|:exclamation:MinorFail|`module-src-functions-commands-ontology`|[term-referencing](https://ns.inria.fr/olivaw#term-referencing)|Term not referenced to a module|[Jump](#minorfail-outcome-number-105)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-106">106/167</div>|:exclamation:MinorFail|`module-src-features-ontology-catalogs`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL EL Profile incompatible|[Jump](#minorfail-outcome-number-106)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-107">107/167</div>|:exclamation:MinorFail|`module-src-features-ontology-catalogs`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL EL Profile incompatible|[Jump](#minorfail-outcome-number-107)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-108">108/167</div>|:exclamation:MinorFail|`module-src-features-ontology-catalogs`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL QL Profile incompatible|[Jump](#minorfail-outcome-number-108)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-109">109/167</div>|:exclamation:MinorFail|`module-src-features-ontology-catalogs`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL QL Profile incompatible|[Jump](#minorfail-outcome-number-109)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-110">110/167</div>|:exclamation:MinorFail|`module-src-features-ontology`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL EL Profile incompatible|[Jump](#minorfail-outcome-number-110)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-111">111/167</div>|:exclamation:MinorFail|`module-src-features-ontology`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL EL Profile incompatible|[Jump](#minorfail-outcome-number-111)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-112">112/167</div>|:exclamation:MinorFail|`module-src-features-ontology`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL EL Profile incompatible|[Jump](#minorfail-outcome-number-112)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-113">113/167</div>|:exclamation:MinorFail|`module-src-features-ontology`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL QL Profile incompatible|[Jump](#minorfail-outcome-number-113)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-114">114/167</div>|:exclamation:MinorFail|`module-src-features-ontology`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL QL Profile incompatible|[Jump](#minorfail-outcome-number-114)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-115">115/167</div>|:exclamation:MinorFail|`module-src-features-ontology`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL QL Profile incompatible|[Jump](#minorfail-outcome-number-115)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-116">116/167</div>|:exclamation:MinorFail|`module-src-features-ontology`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL QL Profile incompatible|[Jump](#minorfail-outcome-number-116)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-117">117/167</div>|:exclamation:MinorFail|`module-src-features-ontology`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL RL Profile incompatible|[Jump](#minorfail-outcome-number-117)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-118">118/167</div>|:exclamation:MinorFail|`module-src-features-ontology`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL RL Profile incompatible|[Jump](#minorfail-outcome-number-118)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-119">119/167</div>|:exclamation:MinorFail|`module-src-features-ontology`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL RL Profile incompatible|[Jump](#minorfail-outcome-number-119)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-120">120/167</div>|:exclamation:MinorFail|`module-src-devices-ontology`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL EL Profile incompatible|[Jump](#minorfail-outcome-number-120)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-121">121/167</div>|:exclamation:MinorFail|`module-src-devices-ontology`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL EL Profile incompatible|[Jump](#minorfail-outcome-number-121)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-122">122/167</div>|:exclamation:MinorFail|`module-src-devices-ontology`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL EL Profile incompatible|[Jump](#minorfail-outcome-number-122)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-123">123/167</div>|:exclamation:MinorFail|`module-src-devices-ontology`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL EL Profile incompatible|[Jump](#minorfail-outcome-number-123)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-124">124/167</div>|:exclamation:MinorFail|`module-src-devices-ontology`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL QL Profile incompatible|[Jump](#minorfail-outcome-number-124)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-125">125/167</div>|:exclamation:MinorFail|`module-src-devices-ontology`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL QL Profile incompatible|[Jump](#minorfail-outcome-number-125)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-126">126/167</div>|:exclamation:MinorFail|`module-src-devices-ontology`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL QL Profile incompatible|[Jump](#minorfail-outcome-number-126)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-127">127/167</div>|:exclamation:MinorFail|`module-src-devices-ontology`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL QL Profile incompatible|[Jump](#minorfail-outcome-number-127)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-128">128/167</div>|:exclamation:MinorFail|`module-src-devices-ontology`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL RL Profile incompatible|[Jump](#minorfail-outcome-number-128)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-129">129/167</div>|:exclamation:MinorFail|`module-src-devices-ontology`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL RL Profile incompatible|[Jump](#minorfail-outcome-number-129)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-130">130/167</div>|:exclamation:MinorFail|`module-src-devices-ontology`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL RL Profile incompatible|[Jump](#minorfail-outcome-number-130)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-131">131/167</div>|:exclamation:MinorFail|`module-src-devices-ontology`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL RL Profile incompatible|[Jump](#minorfail-outcome-number-131)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-132">132/167</div>|:exclamation:MinorFail|`module-src-coswot-sosa`|[term-referencing](https://ns.inria.fr/olivaw#term-referencing)|Term not referenced to a module|[Jump](#minorfail-outcome-number-132)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-133">133/167</div>|:exclamation:MinorFail|`module-src-communications-ontology`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL EL Profile incompatible|[Jump](#minorfail-outcome-number-133)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-134">134/167</div>|:exclamation:MinorFail|`module-src-communications-ontology`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL EL Profile incompatible|[Jump](#minorfail-outcome-number-134)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-135">135/167</div>|:exclamation:MinorFail|`module-src-communications-ontology`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL QL Profile incompatible|[Jump](#minorfail-outcome-number-135)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-136">136/167</div>|:exclamation:MinorFail|`module-src-communications-ontology`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL QL Profile incompatible|[Jump](#minorfail-outcome-number-136)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-137">137/167</div>|:exclamation:MinorFail|`module-src-communications-ontology`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL RL Profile incompatible|[Jump](#minorfail-outcome-number-137)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-138">138/167</div>|:exclamation:MinorFail|`module-src-communications-ontology`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL RL Profile incompatible|[Jump](#minorfail-outcome-number-138)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-139">139/167</div>|:exclamation:MinorFail|`module-src-aggregations-ontology`|[domain-and-range-referencing](https://ns.inria.fr/olivaw#domain-and-range-referencing)|Range out of vocabulary|[Jump](#minorfail-outcome-number-139)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-140">140/167</div>|:exclamation:MinorFail|`module-src-aggregations-ontology`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL EL Profile incompatible|[Jump](#minorfail-outcome-number-140)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-141">141/167</div>|:exclamation:MinorFail|`module-src-aggregations-ontology`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL EL Profile incompatible|[Jump](#minorfail-outcome-number-141)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-142">142/167</div>|:exclamation:MinorFail|`module-src-aggregations-ontology`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL QL Profile incompatible|[Jump](#minorfail-outcome-number-142)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-143">143/167</div>|:exclamation:MinorFail|`module-src-aggregations-ontology`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL QL Profile incompatible|[Jump](#minorfail-outcome-number-143)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-144">144/167</div>|:exclamation:MinorFail|`module-src-aggregations-ontology`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL QL Profile incompatible|[Jump](#minorfail-outcome-number-144)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-145">145/167</div>|:exclamation:MinorFail|`module-src-aggregations-ontology`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL RL Profile incompatible|[Jump](#minorfail-outcome-number-145)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-146">146/167</div>|:exclamation:MinorFail|`module-src-aggregations-ontology`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL RL Profile incompatible|[Jump](#minorfail-outcome-number-146)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-147">147/167</div>|:exclamation:MinorFail|`module-src-aggregations-ontology`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL RL Profile incompatible|[Jump](#minorfail-outcome-number-147)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-148">148/167</div>|:exclamation:MinorFail|`module-src-actuations-ontology`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL EL Profile incompatible|[Jump](#minorfail-outcome-number-148)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-149">149/167</div>|:exclamation:MinorFail|`module-src-actuations-ontology`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL EL Profile incompatible|[Jump](#minorfail-outcome-number-149)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-150">150/167</div>|:exclamation:MinorFail|`module-src-actuations-ontology`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL EL Profile incompatible|[Jump](#minorfail-outcome-number-150)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-151">151/167</div>|:exclamation:MinorFail|`module-src-actuations-ontology`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL EL Profile incompatible|[Jump](#minorfail-outcome-number-151)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-152">152/167</div>|:exclamation:MinorFail|`module-src-actuations-ontology`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL QL Profile incompatible|[Jump](#minorfail-outcome-number-152)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-153">153/167</div>|:exclamation:MinorFail|`module-src-actuations-ontology`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL QL Profile incompatible|[Jump](#minorfail-outcome-number-153)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-154">154/167</div>|:exclamation:MinorFail|`module-src-actuations-ontology`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL QL Profile incompatible|[Jump](#minorfail-outcome-number-154)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-155">155/167</div>|:exclamation:MinorFail|`module-src-actuations-ontology`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL QL Profile incompatible|[Jump](#minorfail-outcome-number-155)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-156">156/167</div>|:exclamation:MinorFail|`module-src-actuations-ontology`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL RL Profile incompatible|[Jump](#minorfail-outcome-number-156)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-157">157/167</div>|:exclamation:MinorFail|`module-src-actuations-ontology`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL RL Profile incompatible|[Jump](#minorfail-outcome-number-157)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-158">158/167</div>|:exclamation:MinorFail|`module-src-actuations-ontology`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL RL Profile incompatible|[Jump](#minorfail-outcome-number-158)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-159">159/167</div>|:exclamation:MinorFail|`module-src-actuations-ontology`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL RL Profile incompatible|[Jump](#minorfail-outcome-number-159)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-160">160/167</div>|:exclamation:MinorFail|`module-src-actuations-ontology`|[terms-differenciation](https://ns.inria.fr/olivaw#terms-differenciation)|Too close terms|[Jump](#minorfail-outcome-number-160)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-161">161/167</div>|:exclamation:MinorFail|`modelet-building-automation-samples`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL EL Profile incompatible|[Jump](#minorfail-outcome-number-161)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-162">162/167</div>|:exclamation:MinorFail|`modelet-building-automation-samples`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL QL Profile incompatible|[Jump](#minorfail-outcome-number-162)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-163">163/167</div>|:exclamation:MinorFail|`modelet-building-automation-features`|[domain-and-range-referencing](https://ns.inria.fr/olivaw#domain-and-range-referencing)|Domain out of vocabulary|[Jump](#minorfail-outcome-number-163)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-164">164/167</div>|:exclamation:MinorFail|`modelet-building-automation-features`|[domain-and-range-referencing](https://ns.inria.fr/olivaw#domain-and-range-referencing)|Range out of vocabulary|[Jump](#minorfail-outcome-number-164)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-165">165/167</div>|:exclamation:MinorFail|`modelet-building-automation-features`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL EL Profile incompatible|[Jump](#minorfail-outcome-number-165)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-166">166/167</div>|:exclamation:MinorFail|`modelet-building-automation-features`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL QL Profile incompatible|[Jump](#minorfail-outcome-number-166)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-167">167/167</div>|:exclamation:MinorFail|`modelet-building-automation-features`|[terms-differenciation](https://ns.inria.fr/olivaw#terms-differenciation)|Too close terms|[Jump](#minorfail-outcome-number-167)|

***

## MinorFail Outcomes Details

This subchapter gives more details to the :exclamation:MinorFail outcomes

### MinorFail Outcome number 1

[Jump to summary definition](#summary-MinorFail-1)	|	Previous MinorFail outcome	|	[Next MinorFail outcome](#minorfail-outcome-number-2)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-src-systems-ontology|
|----|----|
|Title|Standalone&#32;module&#32;src/systems/ontology.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Module systems/ontology](https://gitlab.com/coswot/coswot-acimov/blob/HEAD/src/systems/ontology.ttl)|

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
|Name|module-src-systems-ontology|
|----|----|
|Title|Standalone&#32;module&#32;src/systems/ontology.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Module systems/ontology](https://gitlab.com/coswot/coswot-acimov/blob/HEAD/src/systems/ontology.ttl)|

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
|Name|module-src-systems-ontology|
|----|----|
|Title|Standalone&#32;module&#32;src/systems/ontology.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Module systems/ontology](https://gitlab.com/coswot/coswot-acimov/blob/HEAD/src/systems/ontology.ttl)|

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
|Name|module-src-systems-ontology|
|----|----|
|Title|Standalone&#32;module&#32;src/systems/ontology.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Module systems/ontology](https://gitlab.com/coswot/coswot-acimov/blob/HEAD/src/systems/ontology.ttl)|

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
|Name|module-src-states-ontology-catalog|
|----|----|
|Title|Standalone&#32;module&#32;src/states/ontology.catalog.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Module states/ontology.catalog](https://gitlab.com/coswot/coswot-acimov/blob/HEAD/src/states/ontology.catalog.ttl)|

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
|[Section top](#minorfail-outcome-number-5)|Pointer|<pre lang="Turtle"><code>:isStateOf&#32;a&#32;owl:ObjectProperty&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;is&#32;state&#32;of&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;Links&#32;a&#32;state&#32;to&#32;the&#32;feature&#32;kind&#32;or&#32;feature&#32;of&#32;interest&#32;it&#32;...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:domain&#32; &#91;&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:allValuesFrom&#32;:StateKind&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:onProperty&#32;skos:broader&#32;],  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#91;&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:allValuesFrom&#32;:StateKind&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:onProperty&#32;skos:narrower&#32;],  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;skos:Concept,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;:StateKind&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32; &#60;https://w3id.org/coswot/core/states> &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:subPropertyOf&#32;:isStateOf&#32;;  &#10; &#32; &#32; &#32; &#32;owl:equivalentProperty&#32;:isStateOf&#32;;  &#10; &#32; &#32; &#32; &#32;owl:inverseOf&#32;:hasState&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-5)|Pointer|http://www.w3.org/2004/02/skos/core#Concept|

***
### MinorFail Outcome number 6

[Jump to summary definition](#summary-MinorFail-6)	|	[Previous MinorFail outcome](#minorfail-outcome-number-5)	|	[Next MinorFail outcome](#minorfail-outcome-number-7)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-src-states-ontology-catalog|
|----|----|
|Title|Standalone&#32;module&#32;src/states/ontology.catalog.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Module states/ontology.catalog](https://gitlab.com/coswot/coswot-acimov/blob/HEAD/src/states/ontology.catalog.ttl)|

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
|[Section top](#minorfail-outcome-number-6)|Pointer|<pre lang="Turtle"><code>:hasState&#32;a&#32;owl:ObjectProperty&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;has&#32;state&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;Links&#32;a&#32;feature&#32;kind&#32;or&#32;a&#32;feature&#32;of&#32;interest&#32;to&#32;one&#32;of&#32;its&#32;...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32; &#60;https://w3id.org/coswot/core/states> &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:range&#32; &#91;&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:allValuesFrom&#32;:StateKind&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:onProperty&#32;skos:broader&#32;],  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#91;&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:allValuesFrom&#32;:StateKind&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:onProperty&#32;skos:narrower&#32;],  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;skos:Concept,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;:StateKind&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:subPropertyOf&#32;:hasState&#32;;  &#10; &#32; &#32; &#32; &#32;owl:equivalentProperty&#32;:hasState&#32;;  &#10; &#32; &#32; &#32; &#32;owl:inverseOf&#32;:isStateOf&#32;;  &#10; &#32; &#32; &#32; &#32;owl:propertyChainAxiom&#32;(&#32;skos:broader&#32;:hasState&#32;)&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-6)|Pointer|http://www.w3.org/2004/02/skos/core#Concept|

***
### MinorFail Outcome number 7

[Jump to summary definition](#summary-MinorFail-7)	|	[Previous MinorFail outcome](#minorfail-outcome-number-6)	|	[Next MinorFail outcome](#minorfail-outcome-number-8)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-src-states-ontology-catalog|
|----|----|
|Title|Standalone&#32;module&#32;src/states/ontology.catalog.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Module states/ontology.catalog](https://gitlab.com/coswot/coswot-acimov/blob/HEAD/src/states/ontology.catalog.ttl)|

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
|Name|module-src-states-ontology-catalog|
|----|----|
|Title|Standalone&#32;module&#32;src/states/ontology.catalog.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Module states/ontology.catalog](https://gitlab.com/coswot/coswot-acimov/blob/HEAD/src/states/ontology.catalog.ttl)|

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
|Name|module-src-states-ontology-catalog|
|----|----|
|Title|Standalone&#32;module&#32;src/states/ontology.catalog.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Module states/ontology.catalog](https://gitlab.com/coswot/coswot-acimov/blob/HEAD/src/states/ontology.catalog.ttl)|

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
|Name|module-src-states-ontology-catalog|
|----|----|
|Title|Standalone&#32;module&#32;src/states/ontology.catalog.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Module states/ontology.catalog](https://gitlab.com/coswot/coswot-acimov/blob/HEAD/src/states/ontology.catalog.ttl)|

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
|Name|module-src-states-ontology-catalog|
|----|----|
|Title|Standalone&#32;module&#32;src/states/ontology.catalog.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Module states/ontology.catalog](https://gitlab.com/coswot/coswot-acimov/blob/HEAD/src/states/ontology.catalog.ttl)|

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
|Name|module-src-states-ontology|
|----|----|
|Title|Standalone&#32;module&#32;src/states/ontology.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Module states/ontology](https://gitlab.com/coswot/coswot-acimov/blob/HEAD/src/states/ontology.ttl)|

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
|[Section top](#minorfail-outcome-number-12)|Pointer|<pre lang="Turtle"><code>:isStateOf&#32;a&#32;owl:ObjectProperty&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;is&#32;state&#32;of&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;Links&#32;a&#32;state&#32;to&#32;the&#32;feature&#32;kind&#32;or&#32;feature&#32;of&#32;interest&#32;it&#32;...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:domain&#32; &#91;&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:allValuesFrom&#32;:StateKind&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:onProperty&#32;skos:broader&#32;],  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#91;&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:allValuesFrom&#32;:StateKind&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:onProperty&#32;skos:narrower&#32;],  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#91;&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;rdfs:subClassOf&#32;&lowbar;:n6eecde05abfe457d83c7d5435d216501b4&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:allValuesFrom&#32;owl:Nothing&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:onProperty&#32;:hasKind&#32;],  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;&lowbar;:n6eecde05abfe457d83c7d5435d216501b4,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;skos:Concept,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;:State,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;:StateKind&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32; &#60;https://w3id.org/coswot/core/states> &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:range&#32;&lowbar;:n6eecde05abfe457d83c7d5435d216501b5&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:subPropertyOf&#32;:isStateOf&#32;;  &#10; &#32; &#32; &#32; &#32;owl:equivalentProperty&#32;:isStateOf&#32;;  &#10; &#32; &#32; &#32; &#32;owl:inverseOf&#32;:hasState&#32;.  &#10;&lowbar;:n6eecde05abfe457d83c7d5435d216501b6&#32;rdf:first&#32;:StateOfInterest&#32;;  &#10; &#32; &#32; &#32; &#32;rdf:rest&#32;()&#32;.  &#10;&lowbar;:n6eecde05abfe457d83c7d5435d216501b7&#32;rdf:first&#32;:Feature&#32;;  &#10; &#32; &#32; &#32; &#32;rdf:rest&#32;&lowbar;:n6eecde05abfe457d83c7d5435d216501b6&#32;.  &#10;&lowbar;:n6eecde05abfe457d83c7d5435d216501b4&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32;owl:allValuesFrom&#32;:StateKind&#32;;  &#10; &#32; &#32; &#32; &#32;owl:onProperty&#32;:hasKind&#32;.  &#10;&lowbar;:n6eecde05abfe457d83c7d5435d216501b5&#32;a&#32;owl:Class&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:subClassOf&#32;&lowbar;:n6eecde05abfe457d83c7d5435d216501b5&#32;;  &#10; &#32; &#32; &#32; &#32;owl:equivalentClass&#32;&lowbar;:n6eecde05abfe457d83c7d5435d216501b5&#32;;  &#10; &#32; &#32; &#32; &#32;owl:unionOf&#32;&lowbar;:n6eecde05abfe457d83c7d5435d216501b7&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-12)|Pointer|http://www.w3.org/2004/02/skos/core#Concept|

***
### MinorFail Outcome number 13

[Jump to summary definition](#summary-MinorFail-13)	|	[Previous MinorFail outcome](#minorfail-outcome-number-12)	|	[Next MinorFail outcome](#minorfail-outcome-number-14)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-src-states-ontology|
|----|----|
|Title|Standalone&#32;module&#32;src/states/ontology.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Module states/ontology](https://gitlab.com/coswot/coswot-acimov/blob/HEAD/src/states/ontology.ttl)|

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
|[Section top](#minorfail-outcome-number-13)|Pointer|<pre lang="Turtle"><code>:hasKind&#32;a&#32;owl:ObjectProperty&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;has&#32;state&#32;kind&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;links&#32;a&#32;state&#32;of&#32;interest&#32;to&#32;its&#32;kind,&#32;a&#32;state&#32;kind&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:domain&#32;&lowbar;:ndbbe622b5e314178acf5189f36fa59f6b1,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#91;&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:onProperty&#32;:hasKind&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:someValuesFrom&#32;:StateKind&#32;],  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;&lowbar;:ndbbe622b5e314178acf5189f36fa59f6b3,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#91;&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:onProperty&#32;:isStateOfInterestOf&#32;],  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;:State,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;:StateOfInterest&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32; &#60;https://w3id.org/coswot/core/states> &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:range&#32;&lowbar;:ndbbe622b5e314178acf5189f36fa59f6b1,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#91;&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:allValuesFrom&#32;:StateKind&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:onProperty&#32;skos:broader&#32;],  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#91;&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:allValuesFrom&#32;:StateKind&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:onProperty&#32;skos:narrower&#32;],  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#91;&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;rdfs:subClassOf&#32;&lowbar;:ndbbe622b5e314178acf5189f36fa59f6b1&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:allValuesFrom&#32;owl:Nothing&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:onProperty&#32;:hasKind&#32;],  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;skos:Concept,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;:State,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;:StateKind&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:subPropertyOf&#32;:hasKind&#32;;  &#10; &#32; &#32; &#32; &#32;owl:equivalentProperty&#32;:hasKind&#32;;  &#10; &#32; &#32; &#32; &#32;owl:propertyChainAxiom&#32;(&#32;:hasKind&#32;skos:broader&#32;)&#32;.  &#10;&lowbar;:ndbbe622b5e314178acf5189f36fa59f6b10&#32;rdf:first&#32;:StateOfInterest&#32;;  &#10; &#32; &#32; &#32; &#32;rdf:rest&#32;()&#32;.  &#10;&lowbar;:ndbbe622b5e314178acf5189f36fa59f6b11&#32;rdf:first&#32;:Feature&#32;;  &#10; &#32; &#32; &#32; &#32;rdf:rest&#32;&lowbar;:ndbbe622b5e314178acf5189f36fa59f6b10&#32;.  &#10;&lowbar;:ndbbe622b5e314178acf5189f36fa59f6b1&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32;owl:allValuesFrom&#32;:StateKind&#32;;  &#10; &#32; &#32; &#32; &#32;owl:onProperty&#32;:hasKind&#32;.  &#10;&lowbar;:ndbbe622b5e314178acf5189f36fa59f6b3&#32;a&#32;owl:Class&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:subClassOf&#32;&lowbar;:ndbbe622b5e314178acf5189f36fa59f6b3&#32;;  &#10; &#32; &#32; &#32; &#32;owl:equivalentClass&#32;&lowbar;:ndbbe622b5e314178acf5189f36fa59f6b3&#32;;  &#10; &#32; &#32; &#32; &#32;owl:unionOf&#32;&lowbar;:ndbbe622b5e314178acf5189f36fa59f6b11&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-13)|Pointer|<pre lang="Turtle"><code>:hasState&#32;a&#32;owl:ObjectProperty&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;has&#32;state&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;Links&#32;a&#32;feature&#32;kind&#32;or&#32;a&#32;feature&#32;of&#32;interest&#32;to&#32;one&#32;of&#32;its&#32;...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:domain&#32;&lowbar;:na3f5bdfd06e744ba9a077a42b9668efcb1&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32; &#60;https://w3id.org/coswot/core/states> &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:range&#32; &#91;&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:allValuesFrom&#32;:StateKind&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:onProperty&#32;skos:broader&#32;],  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#91;&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:allValuesFrom&#32;:StateKind&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:onProperty&#32;skos:narrower&#32;],  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#91;&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;rdfs:subClassOf&#32;&lowbar;:na3f5bdfd06e744ba9a077a42b9668efcb5&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:allValuesFrom&#32;owl:Nothing&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:onProperty&#32;:hasKind&#32;],  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;&lowbar;:na3f5bdfd06e744ba9a077a42b9668efcb5,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;skos:Concept,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;:State,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;:StateKind&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:subPropertyOf&#32;:hasState&#32;;  &#10; &#32; &#32; &#32; &#32;owl:equivalentProperty&#32;:hasState&#32;;  &#10; &#32; &#32; &#32; &#32;owl:inverseOf&#32;:isStateOf&#32;;  &#10; &#32; &#32; &#32; &#32;owl:propertyChainAxiom&#32;(&#32;:hasStateOfInterest&#32;:hasKind&#32;),  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;(&#32;skos:broader&#32;:hasState&#32;),  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;(&#32;:hasKind&#32;:hasState&#32;)&#32;.  &#10;&lowbar;:na3f5bdfd06e744ba9a077a42b9668efcb12&#32;rdf:first&#32;:StateOfInterest&#32;;  &#10; &#32; &#32; &#32; &#32;rdf:rest&#32;()&#32;.  &#10;&lowbar;:na3f5bdfd06e744ba9a077a42b9668efcb13&#32;rdf:first&#32;:Feature&#32;;  &#10; &#32; &#32; &#32; &#32;rdf:rest&#32;&lowbar;:na3f5bdfd06e744ba9a077a42b9668efcb12&#32;.  &#10;&lowbar;:na3f5bdfd06e744ba9a077a42b9668efcb5&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32;owl:allValuesFrom&#32;:StateKind&#32;;  &#10; &#32; &#32; &#32; &#32;owl:onProperty&#32;:hasKind&#32;.  &#10;&lowbar;:na3f5bdfd06e744ba9a077a42b9668efcb1&#32;a&#32;owl:Class&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:subClassOf&#32;&lowbar;:na3f5bdfd06e744ba9a077a42b9668efcb1&#32;;  &#10; &#32; &#32; &#32; &#32;owl:equivalentClass&#32;&lowbar;:na3f5bdfd06e744ba9a077a42b9668efcb1&#32;;  &#10; &#32; &#32; &#32; &#32;owl:unionOf&#32;&lowbar;:na3f5bdfd06e744ba9a077a42b9668efcb13&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-13)|Pointer|http://www.w3.org/2004/02/skos/core#Concept|

***
### MinorFail Outcome number 14

[Jump to summary definition](#summary-MinorFail-14)	|	[Previous MinorFail outcome](#minorfail-outcome-number-13)	|	[Next MinorFail outcome](#minorfail-outcome-number-15)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-src-states-ontology|
|----|----|
|Title|Standalone&#32;module&#32;src/states/ontology.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Module states/ontology](https://gitlab.com/coswot/coswot-acimov/blob/HEAD/src/states/ontology.ttl)|

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
|Name|module-src-states-ontology|
|----|----|
|Title|Standalone&#32;module&#32;src/states/ontology.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Module states/ontology](https://gitlab.com/coswot/coswot-acimov/blob/HEAD/src/states/ontology.ttl)|

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
|Name|module-src-states-ontology|
|----|----|
|Title|Standalone&#32;module&#32;src/states/ontology.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Module states/ontology](https://gitlab.com/coswot/coswot-acimov/blob/HEAD/src/states/ontology.ttl)|

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
|Name|module-src-states-ontology|
|----|----|
|Title|Standalone&#32;module&#32;src/states/ontology.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Module states/ontology](https://gitlab.com/coswot/coswot-acimov/blob/HEAD/src/states/ontology.ttl)|

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
|Name|module-src-states-ontology|
|----|----|
|Title|Standalone&#32;module&#32;src/states/ontology.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Module states/ontology](https://gitlab.com/coswot/coswot-acimov/blob/HEAD/src/states/ontology.ttl)|

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
|Name|module-src-states-ontology|
|----|----|
|Title|Standalone&#32;module&#32;src/states/ontology.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Module states/ontology](https://gitlab.com/coswot/coswot-acimov/blob/HEAD/src/states/ontology.ttl)|

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
|Name|module-src-states-ontology|
|----|----|
|Title|Standalone&#32;module&#32;src/states/ontology.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Module states/ontology](https://gitlab.com/coswot/coswot-acimov/blob/HEAD/src/states/ontology.ttl)|

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
|Name|module-src-states-ontology|
|----|----|
|Title|Standalone&#32;module&#32;src/states/ontology.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Module states/ontology](https://gitlab.com/coswot/coswot-acimov/blob/HEAD/src/states/ontology.ttl)|

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
|Name|module-src-states-ontology|
|----|----|
|Title|Standalone&#32;module&#32;src/states/ontology.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Module states/ontology](https://gitlab.com/coswot/coswot-acimov/blob/HEAD/src/states/ontology.ttl)|

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
|Name|module-src-states-ontology|
|----|----|
|Title|Standalone&#32;module&#32;src/states/ontology.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Module states/ontology](https://gitlab.com/coswot/coswot-acimov/blob/HEAD/src/states/ontology.ttl)|

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
|Name|module-src-states-ontology|
|----|----|
|Title|Standalone&#32;module&#32;src/states/ontology.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Module states/ontology](https://gitlab.com/coswot/coswot-acimov/blob/HEAD/src/states/ontology.ttl)|

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
|Name|module-src-states-ontology|
|----|----|
|Title|Standalone&#32;module&#32;src/states/ontology.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Module states/ontology](https://gitlab.com/coswot/coswot-acimov/blob/HEAD/src/states/ontology.ttl)|

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
|Name|module-src-states-ontology|
|----|----|
|Title|Standalone&#32;module&#32;src/states/ontology.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Module states/ontology](https://gitlab.com/coswot/coswot-acimov/blob/HEAD/src/states/ontology.ttl)|

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
|Name|module-src-states-ontology|
|----|----|
|Title|Standalone&#32;module&#32;src/states/ontology.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Module states/ontology](https://gitlab.com/coswot/coswot-acimov/blob/HEAD/src/states/ontology.ttl)|

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
|Name|module-src-services-operations-ontology|
|----|----|
|Title|Standalone&#32;module&#32;src/services&lowbar;operations/ontology.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Module services&lowbar;operations/ontology](https://gitlab.com/coswot/coswot-acimov/blob/HEAD/src/services_operations/ontology.ttl)|

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
|Name|module-src-services-operations-ontology|
|----|----|
|Title|Standalone&#32;module&#32;src/services&lowbar;operations/ontology.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Module services&lowbar;operations/ontology](https://gitlab.com/coswot/coswot-acimov/blob/HEAD/src/services_operations/ontology.ttl)|

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
|Name|module-src-services-operations-ontology|
|----|----|
|Title|Standalone&#32;module&#32;src/services&lowbar;operations/ontology.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Module services&lowbar;operations/ontology](https://gitlab.com/coswot/coswot-acimov/blob/HEAD/src/services_operations/ontology.ttl)|

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
|Name|module-src-services-operations-ontology|
|----|----|
|Title|Standalone&#32;module&#32;src/services&lowbar;operations/ontology.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Module services&lowbar;operations/ontology](https://gitlab.com/coswot/coswot-acimov/blob/HEAD/src/services_operations/ontology.ttl)|

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
|Name|module-src-services-operations-ontology|
|----|----|
|Title|Standalone&#32;module&#32;src/services&lowbar;operations/ontology.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Module services&lowbar;operations/ontology](https://gitlab.com/coswot/coswot-acimov/blob/HEAD/src/services_operations/ontology.ttl)|

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
|Name|module-src-services-operations-ontology|
|----|----|
|Title|Standalone&#32;module&#32;src/services&lowbar;operations/ontology.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Module services&lowbar;operations/ontology](https://gitlab.com/coswot/coswot-acimov/blob/HEAD/src/services_operations/ontology.ttl)|

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
|Name|module-src-services-operations-ontology|
|----|----|
|Title|Standalone&#32;module&#32;src/services&lowbar;operations/ontology.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Module services&lowbar;operations/ontology](https://gitlab.com/coswot/coswot-acimov/blob/HEAD/src/services_operations/ontology.ttl)|

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
|Name|module-src-services-operations-ontology|
|----|----|
|Title|Standalone&#32;module&#32;src/services&lowbar;operations/ontology.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Module services&lowbar;operations/ontology](https://gitlab.com/coswot/coswot-acimov/blob/HEAD/src/services_operations/ontology.ttl)|

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
|Name|module-src-services-operations-ontology|
|----|----|
|Title|Standalone&#32;module&#32;src/services&lowbar;operations/ontology.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Module services&lowbar;operations/ontology](https://gitlab.com/coswot/coswot-acimov/blob/HEAD/src/services_operations/ontology.ttl)|

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
|Name|module-src-services-operations-ontology|
|----|----|
|Title|Standalone&#32;module&#32;src/services&lowbar;operations/ontology.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Module services&lowbar;operations/ontology](https://gitlab.com/coswot/coswot-acimov/blob/HEAD/src/services_operations/ontology.ttl)|

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
|Name|module-src-services-operations-ontology|
|----|----|
|Title|Standalone&#32;module&#32;src/services&lowbar;operations/ontology.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Module services&lowbar;operations/ontology](https://gitlab.com/coswot/coswot-acimov/blob/HEAD/src/services_operations/ontology.ttl)|

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
|Name|module-src-services-operations-ontology|
|----|----|
|Title|Standalone&#32;module&#32;src/services&lowbar;operations/ontology.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Module services&lowbar;operations/ontology](https://gitlab.com/coswot/coswot-acimov/blob/HEAD/src/services_operations/ontology.ttl)|

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
|Name|module-src-services-operations-ontology|
|----|----|
|Title|Standalone&#32;module&#32;src/services&lowbar;operations/ontology.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Module services&lowbar;operations/ontology](https://gitlab.com/coswot/coswot-acimov/blob/HEAD/src/services_operations/ontology.ttl)|

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
|Name|module-src-services-operations-ontology|
|----|----|
|Title|Standalone&#32;module&#32;src/services&lowbar;operations/ontology.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Module services&lowbar;operations/ontology](https://gitlab.com/coswot/coswot-acimov/blob/HEAD/src/services_operations/ontology.ttl)|

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
|Name|module-src-samples-ontology|
|----|----|
|Title|Standalone&#32;module&#32;src/samples/ontology.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Module samples/ontology](https://gitlab.com/coswot/coswot-acimov/blob/HEAD/src/samples/ontology.ttl)|

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
|Name|module-src-samples-ontology|
|----|----|
|Title|Standalone&#32;module&#32;src/samples/ontology.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Module samples/ontology](https://gitlab.com/coswot/coswot-acimov/blob/HEAD/src/samples/ontology.ttl)|

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
|Name|module-src-samples-ontology|
|----|----|
|Title|Standalone&#32;module&#32;src/samples/ontology.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Module samples/ontology](https://gitlab.com/coswot/coswot-acimov/blob/HEAD/src/samples/ontology.ttl)|

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
|Name|module-src-property-values-ontology|
|----|----|
|Title|Standalone&#32;module&#32;src/property&lowbar;values/ontology.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Module property&lowbar;values/ontology](https://gitlab.com/coswot/coswot-acimov/blob/HEAD/src/property_values/ontology.ttl)|

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
|[Section top](#minorfail-outcome-number-45)|Pointer|<pre lang="Turtle"><code>:isMeasuredIn&#32;a&#32;owl:ObjectProperty&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;is&#32;measured&#32;in&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;A&#32;relationship&#32;identifying&#32;the&#32;unit&#32;of&#32;measure&#32;used&#32;for&#32;a&#32;ce...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32; &#60;https://w3id.org/coswot/core/property&lowbar;values> &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:range&#32;skos:Concept,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;:UnitOfMeasure&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:subPropertyOf&#32;:isMeasuredIn&#32;;  &#10; &#32; &#32; &#32; &#32;owl:equivalentProperty&#32;:isMeasuredIn&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-45)|Pointer|http://www.w3.org/2004/02/skos/core#Concept|

***
### MinorFail Outcome number 46

[Jump to summary definition](#summary-MinorFail-46)	|	[Previous MinorFail outcome](#minorfail-outcome-number-45)	|	[Next MinorFail outcome](#minorfail-outcome-number-47)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-src-property-values-ontology|
|----|----|
|Title|Standalone&#32;module&#32;src/property&lowbar;values/ontology.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Module property&lowbar;values/ontology](https://gitlab.com/coswot/coswot-acimov/blob/HEAD/src/property_values/ontology.ttl)|

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
|Name|module-src-property-values-ontology|
|----|----|
|Title|Standalone&#32;module&#32;src/property&lowbar;values/ontology.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Module property&lowbar;values/ontology](https://gitlab.com/coswot/coswot-acimov/blob/HEAD/src/property_values/ontology.ttl)|

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
|Name|module-src-property-values-ontology|
|----|----|
|Title|Standalone&#32;module&#32;src/property&lowbar;values/ontology.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Module property&lowbar;values/ontology](https://gitlab.com/coswot/coswot-acimov/blob/HEAD/src/property_values/ontology.ttl)|

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
|Name|module-src-property-values-ontology|
|----|----|
|Title|Standalone&#32;module&#32;src/property&lowbar;values/ontology.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Module property&lowbar;values/ontology](https://gitlab.com/coswot/coswot-acimov/blob/HEAD/src/property_values/ontology.ttl)|

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
|Name|module-src-property-values-ontology|
|----|----|
|Title|Standalone&#32;module&#32;src/property&lowbar;values/ontology.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Module property&lowbar;values/ontology](https://gitlab.com/coswot/coswot-acimov/blob/HEAD/src/property_values/ontology.ttl)|

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
|Name|module-src-property-values-ontology|
|----|----|
|Title|Standalone&#32;module&#32;src/property&lowbar;values/ontology.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Module property&lowbar;values/ontology](https://gitlab.com/coswot/coswot-acimov/blob/HEAD/src/property_values/ontology.ttl)|

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
|Name|module-src-property-values-ontology|
|----|----|
|Title|Standalone&#32;module&#32;src/property&lowbar;values/ontology.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Module property&lowbar;values/ontology](https://gitlab.com/coswot/coswot-acimov/blob/HEAD/src/property_values/ontology.ttl)|

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
|Name|module-src-property-values-ontology|
|----|----|
|Title|Standalone&#32;module&#32;src/property&lowbar;values/ontology.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Module property&lowbar;values/ontology](https://gitlab.com/coswot/coswot-acimov/blob/HEAD/src/property_values/ontology.ttl)|

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
|Name|module-src-property-values-ontology|
|----|----|
|Title|Standalone&#32;module&#32;src/property&lowbar;values/ontology.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Module property&lowbar;values/ontology](https://gitlab.com/coswot/coswot-acimov/blob/HEAD/src/property_values/ontology.ttl)|

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
|Name|module-src-property-values-ontology|
|----|----|
|Title|Standalone&#32;module&#32;src/property&lowbar;values/ontology.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Module property&lowbar;values/ontology](https://gitlab.com/coswot/coswot-acimov/blob/HEAD/src/property_values/ontology.ttl)|

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
|Name|module-src-properties-ontology-catalogs|
|----|----|
|Title|Standalone&#32;module&#32;src/properties/ontology.catalogs.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Module properties/ontology.catalogs](https://gitlab.com/coswot/coswot-acimov/blob/HEAD/src/properties/ontology.catalogs.ttl)|

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
|[Section top](#minorfail-outcome-number-56)|Pointer|<pre lang="Turtle"><code>:isPropertyOf&#32;a&#32;owl:ObjectProperty&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;is&#32;property&#32;of&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;Links&#32;a&#32;property&#32;to&#32;the&#32;feature&#32;it&#32;is&#32;a&#32;property&#32;of.&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:domain&#32; &#91;&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:allValuesFrom&#32;:PropertyKind&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:onProperty&#32;skos:broader&#32;],  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#91;&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:allValuesFrom&#32;:PropertyKind&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:onProperty&#32;skos:narrower&#32;],  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;skos:Concept,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;:PropertyKind&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32; &#60;https://w3id.org/coswot/core/properties> &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:subPropertyOf&#32;:isPropertyOf&#32;;  &#10; &#32; &#32; &#32; &#32;owl:equivalentProperty&#32;:isPropertyOf&#32;;  &#10; &#32; &#32; &#32; &#32;owl:inverseOf&#32;:hasProperty&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-56)|Pointer|http://www.w3.org/2004/02/skos/core#Concept|

***
### MinorFail Outcome number 57

[Jump to summary definition](#summary-MinorFail-57)	|	[Previous MinorFail outcome](#minorfail-outcome-number-56)	|	[Next MinorFail outcome](#minorfail-outcome-number-58)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-src-properties-ontology-catalogs|
|----|----|
|Title|Standalone&#32;module&#32;src/properties/ontology.catalogs.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Module properties/ontology.catalogs](https://gitlab.com/coswot/coswot-acimov/blob/HEAD/src/properties/ontology.catalogs.ttl)|

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
|[Section top](#minorfail-outcome-number-57)|Pointer|<pre lang="Turtle"><code>:hasProperty&#32;a&#32;owl:ObjectProperty&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;has&#32;property&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;Links&#32;a&#32;feature&#32;to&#32;one&#32;of&#32;its&#32;properties.&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32; &#60;https://w3id.org/coswot/core/properties> &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:range&#32; &#91;&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:allValuesFrom&#32;:PropertyKind&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:onProperty&#32;skos:broader&#32;],  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#91;&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:allValuesFrom&#32;:PropertyKind&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:onProperty&#32;skos:narrower&#32;],  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;skos:Concept,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;:PropertyKind&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:subPropertyOf&#32;:hasProperty&#32;;  &#10; &#32; &#32; &#32; &#32;owl:equivalentProperty&#32;:hasProperty&#32;;  &#10; &#32; &#32; &#32; &#32;owl:inverseOf&#32;:isPropertyOf&#32;;  &#10; &#32; &#32; &#32; &#32;owl:propertyChainAxiom&#32;(&#32;skos:broader&#32;:hasProperty&#32;)&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-57)|Pointer|http://www.w3.org/2004/02/skos/core#Concept|

***
### MinorFail Outcome number 58

[Jump to summary definition](#summary-MinorFail-58)	|	[Previous MinorFail outcome](#minorfail-outcome-number-57)	|	[Next MinorFail outcome](#minorfail-outcome-number-59)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-src-properties-ontology-catalogs|
|----|----|
|Title|Standalone&#32;module&#32;src/properties/ontology.catalogs.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Module properties/ontology.catalogs](https://gitlab.com/coswot/coswot-acimov/blob/HEAD/src/properties/ontology.catalogs.ttl)|

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
|Name|module-src-properties-ontology-catalogs|
|----|----|
|Title|Standalone&#32;module&#32;src/properties/ontology.catalogs.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Module properties/ontology.catalogs](https://gitlab.com/coswot/coswot-acimov/blob/HEAD/src/properties/ontology.catalogs.ttl)|

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
|Name|module-src-properties-ontology-catalogs|
|----|----|
|Title|Standalone&#32;module&#32;src/properties/ontology.catalogs.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Module properties/ontology.catalogs](https://gitlab.com/coswot/coswot-acimov/blob/HEAD/src/properties/ontology.catalogs.ttl)|

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
|Name|module-src-properties-ontology-catalogs|
|----|----|
|Title|Standalone&#32;module&#32;src/properties/ontology.catalogs.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Module properties/ontology.catalogs](https://gitlab.com/coswot/coswot-acimov/blob/HEAD/src/properties/ontology.catalogs.ttl)|

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
|Name|module-src-properties-ontology-catalogs|
|----|----|
|Title|Standalone&#32;module&#32;src/properties/ontology.catalogs.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Module properties/ontology.catalogs](https://gitlab.com/coswot/coswot-acimov/blob/HEAD/src/properties/ontology.catalogs.ttl)|

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
|Name|module-src-properties-ontology|
|----|----|
|Title|Standalone&#32;module&#32;src/properties/ontology.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Module properties/ontology](https://gitlab.com/coswot/coswot-acimov/blob/HEAD/src/properties/ontology.ttl)|

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
|[Section top](#minorfail-outcome-number-63)|Pointer|<pre lang="Turtle"><code>:isPropertyOf&#32;a&#32;owl:ObjectProperty&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;is&#32;property&#32;of&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;Links&#32;a&#32;property&#32;kind&#32;to&#32;the&#32;feature&#32;it&#32;is&#32;a&#32;property&#32;of.&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:domain&#32; &#91;&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:allValuesFrom&#32;:PropertyKind&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:onProperty&#32;skos:broader&#32;],  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#91;&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:allValuesFrom&#32;:PropertyKind&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:onProperty&#32;skos:narrower&#32;],  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#91;&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;rdfs:subClassOf&#32;&lowbar;:ne7e29e626c2845c1acc3cf9be21d395cb4&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:allValuesFrom&#32;owl:Nothing&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:onProperty&#32;:hasKind&#32;],  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;&lowbar;:ne7e29e626c2845c1acc3cf9be21d395cb4,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;skos:Concept,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;:Property,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;:PropertyKind&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32; &#60;https://w3id.org/coswot/core/properties> &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:range&#32;:Feature&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:subPropertyOf&#32;:isPropertyOf&#32;;  &#10; &#32; &#32; &#32; &#32;owl:equivalentProperty&#32;:isPropertyOf&#32;;  &#10; &#32; &#32; &#32; &#32;owl:inverseOf&#32;:hasProperty&#32;.  &#10;&lowbar;:ne7e29e626c2845c1acc3cf9be21d395cb4&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32;owl:allValuesFrom&#32;:PropertyKind&#32;;  &#10; &#32; &#32; &#32; &#32;owl:onProperty&#32;:hasKind&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-63)|Pointer|http://www.w3.org/2004/02/skos/core#Concept|

***
### MinorFail Outcome number 64

[Jump to summary definition](#summary-MinorFail-64)	|	[Previous MinorFail outcome](#minorfail-outcome-number-63)	|	[Next MinorFail outcome](#minorfail-outcome-number-65)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-src-properties-ontology|
|----|----|
|Title|Standalone&#32;module&#32;src/properties/ontology.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Module properties/ontology](https://gitlab.com/coswot/coswot-acimov/blob/HEAD/src/properties/ontology.ttl)|

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
|[Section top](#minorfail-outcome-number-64)|Pointer|<pre lang="Turtle"><code>:hasProperty&#32;a&#32;owl:ObjectProperty&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;has&#32;property&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;Links&#32;a&#32;feature&#32;to&#32;one&#32;of&#32;its&#32;property&#32;kinds.&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:domain&#32;:Feature&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32; &#60;https://w3id.org/coswot/core/properties> &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:range&#32; &#91;&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:allValuesFrom&#32;:PropertyKind&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:onProperty&#32;skos:broader&#32;],  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#91;&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:allValuesFrom&#32;:PropertyKind&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:onProperty&#32;skos:narrower&#32;],  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#91;&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;rdfs:subClassOf&#32;&lowbar;:n7886c127a7c1493ba32279c3ac1ec125b4&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:allValuesFrom&#32;owl:Nothing&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:onProperty&#32;:hasKind&#32;],  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;&lowbar;:n7886c127a7c1493ba32279c3ac1ec125b4,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;skos:Concept,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;:Property,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;:PropertyKind&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:subPropertyOf&#32;:hasProperty&#32;;  &#10; &#32; &#32; &#32; &#32;owl:equivalentProperty&#32;:hasProperty&#32;;  &#10; &#32; &#32; &#32; &#32;owl:inverseOf&#32;:isPropertyOf&#32;;  &#10; &#32; &#32; &#32; &#32;owl:propertyChainAxiom&#32;(&#32;skos:broader&#32;:hasProperty&#32;),  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;(&#32;:hasKind&#32;:hasProperty&#32;),  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;(&#32;:hasPropertyOfInterest&#32;:hasKind&#32;)&#32;.  &#10;&lowbar;:n7886c127a7c1493ba32279c3ac1ec125b4&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32;owl:allValuesFrom&#32;:PropertyKind&#32;;  &#10; &#32; &#32; &#32; &#32;owl:onProperty&#32;:hasKind&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-64)|Pointer|http://www.w3.org/2004/02/skos/core#Concept|

***
### MinorFail Outcome number 65

[Jump to summary definition](#summary-MinorFail-65)	|	[Previous MinorFail outcome](#minorfail-outcome-number-64)	|	[Next MinorFail outcome](#minorfail-outcome-number-66)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-src-properties-ontology|
|----|----|
|Title|Standalone&#32;module&#32;src/properties/ontology.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Module properties/ontology](https://gitlab.com/coswot/coswot-acimov/blob/HEAD/src/properties/ontology.ttl)|

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
|Name|module-src-properties-ontology|
|----|----|
|Title|Standalone&#32;module&#32;src/properties/ontology.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Module properties/ontology](https://gitlab.com/coswot/coswot-acimov/blob/HEAD/src/properties/ontology.ttl)|

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
|Name|module-src-properties-ontology|
|----|----|
|Title|Standalone&#32;module&#32;src/properties/ontology.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Module properties/ontology](https://gitlab.com/coswot/coswot-acimov/blob/HEAD/src/properties/ontology.ttl)|

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
|Name|module-src-properties-ontology|
|----|----|
|Title|Standalone&#32;module&#32;src/properties/ontology.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Module properties/ontology](https://gitlab.com/coswot/coswot-acimov/blob/HEAD/src/properties/ontology.ttl)|

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
|Name|module-src-properties-ontology|
|----|----|
|Title|Standalone&#32;module&#32;src/properties/ontology.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Module properties/ontology](https://gitlab.com/coswot/coswot-acimov/blob/HEAD/src/properties/ontology.ttl)|

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
|Name|module-src-properties-ontology|
|----|----|
|Title|Standalone&#32;module&#32;src/properties/ontology.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Module properties/ontology](https://gitlab.com/coswot/coswot-acimov/blob/HEAD/src/properties/ontology.ttl)|

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
|Name|module-src-properties-ontology|
|----|----|
|Title|Standalone&#32;module&#32;src/properties/ontology.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Module properties/ontology](https://gitlab.com/coswot/coswot-acimov/blob/HEAD/src/properties/ontology.ttl)|

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
|Name|module-src-properties-ontology|
|----|----|
|Title|Standalone&#32;module&#32;src/properties/ontology.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Module properties/ontology](https://gitlab.com/coswot/coswot-acimov/blob/HEAD/src/properties/ontology.ttl)|

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
|Name|module-src-properties-ontology|
|----|----|
|Title|Standalone&#32;module&#32;src/properties/ontology.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Module properties/ontology](https://gitlab.com/coswot/coswot-acimov/blob/HEAD/src/properties/ontology.ttl)|

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
|Name|module-src-properties-ontology|
|----|----|
|Title|Standalone&#32;module&#32;src/properties/ontology.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Module properties/ontology](https://gitlab.com/coswot/coswot-acimov/blob/HEAD/src/properties/ontology.ttl)|

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
|Name|module-src-procedures-ontology|
|----|----|
|Title|Standalone&#32;module&#32;src/procedures/ontology.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Module procedures/ontology](https://gitlab.com/coswot/coswot-acimov/blob/HEAD/src/procedures/ontology.ttl)|

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
|[Section top](#minorfail-outcome-number-75)|Pointer|<pre lang="Turtle"><code>:hasPhenomenonTime&#32;a&#32;owl:ObjectProperty&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;has&#32;phenomenon&#32;time&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;Links&#32;a&#32;procedure&#32;execution&#32;to&#32;the&#32;time&#32;that&#32;the&#32;result&#32;appl...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:domain&#32;&lowbar;:nb7ed8ad796b841e582f17edb730c3911b1,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;:ProcedureExecution&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32; &#60;https://w3id.org/coswot/core/procedures> &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:range&#32;time:TemporalEntity&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:subPropertyOf&#32;:hasPhenomenonTime&#32;;  &#10; &#32; &#32; &#32; &#32;owl:equivalentProperty&#32;:hasPhenomenonTime&#32;.  &#10;&lowbar;:nb7ed8ad796b841e582f17edb730c3911b2&#32;rdf:first&#32;:Procedure&#32;;  &#10; &#32; &#32; &#32; &#32;rdf:rest&#32;(&#32;:ProcedureExecution&#32;)&#32;.  &#10;&lowbar;:nb7ed8ad796b841e582f17edb730c3911b1&#32;a&#32;owl:Class&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:subClassOf&#32;&lowbar;:nb7ed8ad796b841e582f17edb730c3911b1&#32;;  &#10; &#32; &#32; &#32; &#32;owl:equivalentClass&#32;&lowbar;:nb7ed8ad796b841e582f17edb730c3911b1&#32;;  &#10; &#32; &#32; &#32; &#32;owl:unionOf&#32;&lowbar;:nb7ed8ad796b841e582f17edb730c3911b2&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-75)|Pointer|<pre lang="Turtle"><code>:TemporalEntity&#32;a&#32;owl:Class&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:subClassOf&#32;:TemporalEntity&#32;;  &#10; &#32; &#32; &#32; &#32;owl:equivalentClass&#32;:TemporalEntity&#32;.</code></pre>|

***
### MinorFail Outcome number 76

[Jump to summary definition](#summary-MinorFail-76)	|	[Previous MinorFail outcome](#minorfail-outcome-number-75)	|	[Next MinorFail outcome](#minorfail-outcome-number-77)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-src-procedures-ontology|
|----|----|
|Title|Standalone&#32;module&#32;src/procedures/ontology.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Module procedures/ontology](https://gitlab.com/coswot/coswot-acimov/blob/HEAD/src/procedures/ontology.ttl)|

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
|Name|module-src-procedures-ontology|
|----|----|
|Title|Standalone&#32;module&#32;src/procedures/ontology.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Module procedures/ontology](https://gitlab.com/coswot/coswot-acimov/blob/HEAD/src/procedures/ontology.ttl)|

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
|Name|module-src-procedures-ontology|
|----|----|
|Title|Standalone&#32;module&#32;src/procedures/ontology.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Module procedures/ontology](https://gitlab.com/coswot/coswot-acimov/blob/HEAD/src/procedures/ontology.ttl)|

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
|Name|module-src-procedures-ontology|
|----|----|
|Title|Standalone&#32;module&#32;src/procedures/ontology.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Module procedures/ontology](https://gitlab.com/coswot/coswot-acimov/blob/HEAD/src/procedures/ontology.ttl)|

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
|Name|module-src-procedures-ontology|
|----|----|
|Title|Standalone&#32;module&#32;src/procedures/ontology.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Module procedures/ontology](https://gitlab.com/coswot/coswot-acimov/blob/HEAD/src/procedures/ontology.ttl)|

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
|Name|module-src-procedures-ontology|
|----|----|
|Title|Standalone&#32;module&#32;src/procedures/ontology.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Module procedures/ontology](https://gitlab.com/coswot/coswot-acimov/blob/HEAD/src/procedures/ontology.ttl)|

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
|Name|module-src-procedures-ontology|
|----|----|
|Title|Standalone&#32;module&#32;src/procedures/ontology.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Module procedures/ontology](https://gitlab.com/coswot/coswot-acimov/blob/HEAD/src/procedures/ontology.ttl)|

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
|Name|module-src-observations-ontology|
|----|----|
|Title|Standalone&#32;module&#32;src/observations/ontology.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Module observations/ontology](https://gitlab.com/coswot/coswot-acimov/blob/HEAD/src/observations/ontology.ttl)|

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
|Name|module-src-observations-ontology|
|----|----|
|Title|Standalone&#32;module&#32;src/observations/ontology.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Module observations/ontology](https://gitlab.com/coswot/coswot-acimov/blob/HEAD/src/observations/ontology.ttl)|

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
|Name|module-src-observations-ontology|
|----|----|
|Title|Standalone&#32;module&#32;src/observations/ontology.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Module observations/ontology](https://gitlab.com/coswot/coswot-acimov/blob/HEAD/src/observations/ontology.ttl)|

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
|Name|module-src-observations-ontology|
|----|----|
|Title|Standalone&#32;module&#32;src/observations/ontology.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Module observations/ontology](https://gitlab.com/coswot/coswot-acimov/blob/HEAD/src/observations/ontology.ttl)|

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
|Name|module-src-observations-ontology|
|----|----|
|Title|Standalone&#32;module&#32;src/observations/ontology.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Module observations/ontology](https://gitlab.com/coswot/coswot-acimov/blob/HEAD/src/observations/ontology.ttl)|

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
|Name|module-src-observations-ontology|
|----|----|
|Title|Standalone&#32;module&#32;src/observations/ontology.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Module observations/ontology](https://gitlab.com/coswot/coswot-acimov/blob/HEAD/src/observations/ontology.ttl)|

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
|Name|module-src-observations-ontology|
|----|----|
|Title|Standalone&#32;module&#32;src/observations/ontology.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Module observations/ontology](https://gitlab.com/coswot/coswot-acimov/blob/HEAD/src/observations/ontology.ttl)|

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
|Name|module-src-observations-ontology|
|----|----|
|Title|Standalone&#32;module&#32;src/observations/ontology.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Module observations/ontology](https://gitlab.com/coswot/coswot-acimov/blob/HEAD/src/observations/ontology.ttl)|

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
|Name|module-src-observations-ontology|
|----|----|
|Title|Standalone&#32;module&#32;src/observations/ontology.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Module observations/ontology](https://gitlab.com/coswot/coswot-acimov/blob/HEAD/src/observations/ontology.ttl)|

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
|Name|module-src-observations-ontology|
|----|----|
|Title|Standalone&#32;module&#32;src/observations/ontology.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Module observations/ontology](https://gitlab.com/coswot/coswot-acimov/blob/HEAD/src/observations/ontology.ttl)|

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
|Name|module-src-observations-ontology|
|----|----|
|Title|Standalone&#32;module&#32;src/observations/ontology.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Module observations/ontology](https://gitlab.com/coswot/coswot-acimov/blob/HEAD/src/observations/ontology.ttl)|

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
|Name|module-src-observations-ontology|
|----|----|
|Title|Standalone&#32;module&#32;src/observations/ontology.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Module observations/ontology](https://gitlab.com/coswot/coswot-acimov/blob/HEAD/src/observations/ontology.ttl)|

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
|Name|module-src-functions-commands-ontology|
|----|----|
|Title|Standalone&#32;module&#32;src/functions&lowbar;commands/ontology.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Module functions&lowbar;commands/ontology](https://gitlab.com/coswot/coswot-acimov/blob/HEAD/src/functions_commands/ontology.ttl)|

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
|Name|module-src-functions-commands-ontology|
|----|----|
|Title|Standalone&#32;module&#32;src/functions&lowbar;commands/ontology.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Module functions&lowbar;commands/ontology](https://gitlab.com/coswot/coswot-acimov/blob/HEAD/src/functions_commands/ontology.ttl)|

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
|Name|module-src-functions-commands-ontology|
|----|----|
|Title|Standalone&#32;module&#32;src/functions&lowbar;commands/ontology.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Module functions&lowbar;commands/ontology](https://gitlab.com/coswot/coswot-acimov/blob/HEAD/src/functions_commands/ontology.ttl)|

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
|Name|module-src-functions-commands-ontology|
|----|----|
|Title|Standalone&#32;module&#32;src/functions&lowbar;commands/ontology.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Module functions&lowbar;commands/ontology](https://gitlab.com/coswot/coswot-acimov/blob/HEAD/src/functions_commands/ontology.ttl)|

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
|Name|module-src-functions-commands-ontology|
|----|----|
|Title|Standalone&#32;module&#32;src/functions&lowbar;commands/ontology.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Module functions&lowbar;commands/ontology](https://gitlab.com/coswot/coswot-acimov/blob/HEAD/src/functions_commands/ontology.ttl)|

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
|Name|module-src-functions-commands-ontology|
|----|----|
|Title|Standalone&#32;module&#32;src/functions&lowbar;commands/ontology.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Module functions&lowbar;commands/ontology](https://gitlab.com/coswot/coswot-acimov/blob/HEAD/src/functions_commands/ontology.ttl)|

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
|Name|module-src-functions-commands-ontology|
|----|----|
|Title|Standalone&#32;module&#32;src/functions&lowbar;commands/ontology.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Module functions&lowbar;commands/ontology](https://gitlab.com/coswot/coswot-acimov/blob/HEAD/src/functions_commands/ontology.ttl)|

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
|Name|module-src-functions-commands-ontology|
|----|----|
|Title|Standalone&#32;module&#32;src/functions&lowbar;commands/ontology.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Module functions&lowbar;commands/ontology](https://gitlab.com/coswot/coswot-acimov/blob/HEAD/src/functions_commands/ontology.ttl)|

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
|Name|module-src-functions-commands-ontology|
|----|----|
|Title|Standalone&#32;module&#32;src/functions&lowbar;commands/ontology.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Module functions&lowbar;commands/ontology](https://gitlab.com/coswot/coswot-acimov/blob/HEAD/src/functions_commands/ontology.ttl)|

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
|Name|module-src-functions-commands-ontology|
|----|----|
|Title|Standalone&#32;module&#32;src/functions&lowbar;commands/ontology.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Module functions&lowbar;commands/ontology](https://gitlab.com/coswot/coswot-acimov/blob/HEAD/src/functions_commands/ontology.ttl)|

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
|Name|module-src-functions-commands-ontology|
|----|----|
|Title|Standalone&#32;module&#32;src/functions&lowbar;commands/ontology.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Module functions&lowbar;commands/ontology](https://gitlab.com/coswot/coswot-acimov/blob/HEAD/src/functions_commands/ontology.ttl)|

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
|Name|module-src-features-ontology-catalogs|
|----|----|
|Title|Standalone&#32;module&#32;src/features/ontology.catalogs.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Module features/ontology.catalogs](https://gitlab.com/coswot/coswot-acimov/blob/HEAD/src/features/ontology.catalogs.ttl)|

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
|Name|module-src-features-ontology-catalogs|
|----|----|
|Title|Standalone&#32;module&#32;src/features/ontology.catalogs.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Module features/ontology.catalogs](https://gitlab.com/coswot/coswot-acimov/blob/HEAD/src/features/ontology.catalogs.ttl)|

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
|Name|module-src-features-ontology-catalogs|
|----|----|
|Title|Standalone&#32;module&#32;src/features/ontology.catalogs.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Module features/ontology.catalogs](https://gitlab.com/coswot/coswot-acimov/blob/HEAD/src/features/ontology.catalogs.ttl)|

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
|Name|module-src-features-ontology-catalogs|
|----|----|
|Title|Standalone&#32;module&#32;src/features/ontology.catalogs.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Module features/ontology.catalogs](https://gitlab.com/coswot/coswot-acimov/blob/HEAD/src/features/ontology.catalogs.ttl)|

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
|Name|module-src-features-ontology|
|----|----|
|Title|Standalone&#32;module&#32;src/features/ontology.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Module features/ontology](https://gitlab.com/coswot/coswot-acimov/blob/HEAD/src/features/ontology.ttl)|

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
|Name|module-src-features-ontology|
|----|----|
|Title|Standalone&#32;module&#32;src/features/ontology.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Module features/ontology](https://gitlab.com/coswot/coswot-acimov/blob/HEAD/src/features/ontology.ttl)|

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
|Name|module-src-features-ontology|
|----|----|
|Title|Standalone&#32;module&#32;src/features/ontology.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Module features/ontology](https://gitlab.com/coswot/coswot-acimov/blob/HEAD/src/features/ontology.ttl)|

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
|Name|module-src-features-ontology|
|----|----|
|Title|Standalone&#32;module&#32;src/features/ontology.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Module features/ontology](https://gitlab.com/coswot/coswot-acimov/blob/HEAD/src/features/ontology.ttl)|

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
|Name|module-src-features-ontology|
|----|----|
|Title|Standalone&#32;module&#32;src/features/ontology.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Module features/ontology](https://gitlab.com/coswot/coswot-acimov/blob/HEAD/src/features/ontology.ttl)|

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
|Name|module-src-features-ontology|
|----|----|
|Title|Standalone&#32;module&#32;src/features/ontology.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Module features/ontology](https://gitlab.com/coswot/coswot-acimov/blob/HEAD/src/features/ontology.ttl)|

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
|Name|module-src-features-ontology|
|----|----|
|Title|Standalone&#32;module&#32;src/features/ontology.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Module features/ontology](https://gitlab.com/coswot/coswot-acimov/blob/HEAD/src/features/ontology.ttl)|

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
|Name|module-src-features-ontology|
|----|----|
|Title|Standalone&#32;module&#32;src/features/ontology.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Module features/ontology](https://gitlab.com/coswot/coswot-acimov/blob/HEAD/src/features/ontology.ttl)|

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
|Name|module-src-features-ontology|
|----|----|
|Title|Standalone&#32;module&#32;src/features/ontology.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Module features/ontology](https://gitlab.com/coswot/coswot-acimov/blob/HEAD/src/features/ontology.ttl)|

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
|Name|module-src-features-ontology|
|----|----|
|Title|Standalone&#32;module&#32;src/features/ontology.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Module features/ontology](https://gitlab.com/coswot/coswot-acimov/blob/HEAD/src/features/ontology.ttl)|

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
|Name|module-src-devices-ontology|
|----|----|
|Title|Standalone&#32;module&#32;src/devices/ontology.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Module devices/ontology](https://gitlab.com/coswot/coswot-acimov/blob/HEAD/src/devices/ontology.ttl)|

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
|Name|module-src-devices-ontology|
|----|----|
|Title|Standalone&#32;module&#32;src/devices/ontology.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Module devices/ontology](https://gitlab.com/coswot/coswot-acimov/blob/HEAD/src/devices/ontology.ttl)|

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
|Name|module-src-devices-ontology|
|----|----|
|Title|Standalone&#32;module&#32;src/devices/ontology.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Module devices/ontology](https://gitlab.com/coswot/coswot-acimov/blob/HEAD/src/devices/ontology.ttl)|

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
|Name|module-src-devices-ontology|
|----|----|
|Title|Standalone&#32;module&#32;src/devices/ontology.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Module devices/ontology](https://gitlab.com/coswot/coswot-acimov/blob/HEAD/src/devices/ontology.ttl)|

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
|Name|module-src-devices-ontology|
|----|----|
|Title|Standalone&#32;module&#32;src/devices/ontology.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Module devices/ontology](https://gitlab.com/coswot/coswot-acimov/blob/HEAD/src/devices/ontology.ttl)|

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
|Name|module-src-devices-ontology|
|----|----|
|Title|Standalone&#32;module&#32;src/devices/ontology.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Module devices/ontology](https://gitlab.com/coswot/coswot-acimov/blob/HEAD/src/devices/ontology.ttl)|

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
|Name|module-src-devices-ontology|
|----|----|
|Title|Standalone&#32;module&#32;src/devices/ontology.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Module devices/ontology](https://gitlab.com/coswot/coswot-acimov/blob/HEAD/src/devices/ontology.ttl)|

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
|Name|module-src-devices-ontology|
|----|----|
|Title|Standalone&#32;module&#32;src/devices/ontology.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Module devices/ontology](https://gitlab.com/coswot/coswot-acimov/blob/HEAD/src/devices/ontology.ttl)|

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
|Name|module-src-devices-ontology|
|----|----|
|Title|Standalone&#32;module&#32;src/devices/ontology.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Module devices/ontology](https://gitlab.com/coswot/coswot-acimov/blob/HEAD/src/devices/ontology.ttl)|

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
|Name|module-src-devices-ontology|
|----|----|
|Title|Standalone&#32;module&#32;src/devices/ontology.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Module devices/ontology](https://gitlab.com/coswot/coswot-acimov/blob/HEAD/src/devices/ontology.ttl)|

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
|Name|module-src-devices-ontology|
|----|----|
|Title|Standalone&#32;module&#32;src/devices/ontology.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Module devices/ontology](https://gitlab.com/coswot/coswot-acimov/blob/HEAD/src/devices/ontology.ttl)|

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
|Name|module-src-devices-ontology|
|----|----|
|Title|Standalone&#32;module&#32;src/devices/ontology.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Module devices/ontology](https://gitlab.com/coswot/coswot-acimov/blob/HEAD/src/devices/ontology.ttl)|

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
|Name|module-src-coswot-sosa|
|----|----|
|Title|Standalone&#32;module&#32;src/coswot-sosa.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Module coswot-sosa](https://gitlab.com/coswot/coswot-acimov/blob/HEAD/src/coswot-sosa.ttl)|

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
|Name|module-src-communications-ontology|
|----|----|
|Title|Standalone&#32;module&#32;src/communications/ontology.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Module communications/ontology](https://gitlab.com/coswot/coswot-acimov/blob/HEAD/src/communications/ontology.ttl)|

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
|Name|module-src-communications-ontology|
|----|----|
|Title|Standalone&#32;module&#32;src/communications/ontology.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Module communications/ontology](https://gitlab.com/coswot/coswot-acimov/blob/HEAD/src/communications/ontology.ttl)|

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
|Name|module-src-communications-ontology|
|----|----|
|Title|Standalone&#32;module&#32;src/communications/ontology.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Module communications/ontology](https://gitlab.com/coswot/coswot-acimov/blob/HEAD/src/communications/ontology.ttl)|

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
|Name|module-src-communications-ontology|
|----|----|
|Title|Standalone&#32;module&#32;src/communications/ontology.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Module communications/ontology](https://gitlab.com/coswot/coswot-acimov/blob/HEAD/src/communications/ontology.ttl)|

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
|Name|module-src-communications-ontology|
|----|----|
|Title|Standalone&#32;module&#32;src/communications/ontology.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Module communications/ontology](https://gitlab.com/coswot/coswot-acimov/blob/HEAD/src/communications/ontology.ttl)|

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
|Name|module-src-communications-ontology|
|----|----|
|Title|Standalone&#32;module&#32;src/communications/ontology.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Module communications/ontology](https://gitlab.com/coswot/coswot-acimov/blob/HEAD/src/communications/ontology.ttl)|

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
|Name|module-src-aggregations-ontology|
|----|----|
|Title|Standalone&#32;module&#32;src/aggregations/ontology.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Module aggregations/ontology](https://gitlab.com/coswot/coswot-acimov/blob/HEAD/src/aggregations/ontology.ttl)|

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
|[Section top](#minorfail-outcome-number-139)|Pointer|<pre lang="Turtle"><code>:hasAggregationKind&#32;a&#32;owl:ObjectProperty&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;has&#32;aggregation&#32;kind&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;Links&#32;a&#32;property,&#32;state,&#32;or&#32;aggregation,&#32;to&#32;the&#32;kind&#32;of&#32;aggr...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:domain&#32;&lowbar;:n922291ca256249aa8d59a2aeee69a3f6b1&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32; &#60;https://w3id.org/coswot/core/aggregations> &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:range&#32;&lowbar;:n922291ca256249aa8d59a2aeee69a3f6b2,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;skos:Concept,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;:AggregationKind&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:subPropertyOf&#32;:hasAggregationKind&#32;;  &#10; &#32; &#32; &#32; &#32;owl:equivalentProperty&#32;:hasAggregationKind&#32;.  &#10;&lowbar;:n922291ca256249aa8d59a2aeee69a3f6b3&#32;rdf:first&#32;:Aggregation&#32;;  &#10; &#32; &#32; &#32; &#32;rdf:rest&#32;(&#32;:AggregationKind&#32;)&#32;.  &#10;&lowbar;:n922291ca256249aa8d59a2aeee69a3f6b5&#32;rdf:first&#32;:State&#32;;  &#10; &#32; &#32; &#32; &#32;rdf:rest&#32;&lowbar;:n922291ca256249aa8d59a2aeee69a3f6b3&#32;.  &#10;&lowbar;:n922291ca256249aa8d59a2aeee69a3f6b6&#32;rdf:first&#32;:Property&#32;;  &#10; &#32; &#32; &#32; &#32;rdf:rest&#32;&lowbar;:n922291ca256249aa8d59a2aeee69a3f6b5&#32;.  &#10;&lowbar;:n922291ca256249aa8d59a2aeee69a3f6b7&#32;rdf:first&#32;:Aggregation&#32;;  &#10; &#32; &#32; &#32; &#32;rdf:rest&#32;()&#32;.  &#10;&lowbar;:n922291ca256249aa8d59a2aeee69a3f6b8&#32;rdf:first&#32;:State&#32;;  &#10; &#32; &#32; &#32; &#32;rdf:rest&#32;&lowbar;:n922291ca256249aa8d59a2aeee69a3f6b7&#32;.  &#10;&lowbar;:n922291ca256249aa8d59a2aeee69a3f6b9&#32;rdf:first&#32;:Property&#32;;  &#10; &#32; &#32; &#32; &#32;rdf:rest&#32;&lowbar;:n922291ca256249aa8d59a2aeee69a3f6b8&#32;.  &#10;&lowbar;:n922291ca256249aa8d59a2aeee69a3f6b1&#32;a&#32;owl:Class&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:subClassOf&#32;&lowbar;:n922291ca256249aa8d59a2aeee69a3f6b1&#32;;  &#10; &#32; &#32; &#32; &#32;owl:equivalentClass&#32;&lowbar;:n922291ca256249aa8d59a2aeee69a3f6b1&#32;;  &#10; &#32; &#32; &#32; &#32;owl:unionOf&#32;&lowbar;:n922291ca256249aa8d59a2aeee69a3f6b9&#32;.  &#10;&lowbar;:n922291ca256249aa8d59a2aeee69a3f6b2&#32;a&#32;owl:Class&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:subClassOf&#32;&lowbar;:n922291ca256249aa8d59a2aeee69a3f6b2&#32;;  &#10; &#32; &#32; &#32; &#32;owl:equivalentClass&#32;&lowbar;:n922291ca256249aa8d59a2aeee69a3f6b2&#32;;  &#10; &#32; &#32; &#32; &#32;owl:unionOf&#32;&lowbar;:n922291ca256249aa8d59a2aeee69a3f6b6&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-139)|Pointer|<pre lang="Turtle"><code>:hasAggregationTime&#32;a&#32;owl:ObjectProperty&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;has&#32;aggregation&#32;time&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;Links&#32;a&#32;property,&#32;state,&#32;aggregation,&#32;or&#32;aggregation&#32;kind,&#32;t...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:domain&#32;&lowbar;:n5ffcbc67409848cb972d46e71aa2d488b1&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32; &#60;https://w3id.org/coswot/core/aggregations> &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:range&#32;time:TemporalInterval&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:subPropertyOf&#32;:hasAggregationTime&#32;;  &#10; &#32; &#32; &#32; &#32;owl:equivalentProperty&#32;:hasAggregationTime&#32;;  &#10; &#32; &#32; &#32; &#32;owl:propertyChainAxiom&#32;(&#32;:hasAggregationKind&#32;:hasAggregationTime&#32;)&#32;.  &#10;&lowbar;:n5ffcbc67409848cb972d46e71aa2d488b4&#32;rdf:first&#32;:Property&#32;;  &#10; &#32; &#32; &#32; &#32;rdf:rest&#32;(&#32;:State&#32;:Aggregation&#32;:AggregationKind&#32;)&#32;.  &#10;&lowbar;:n5ffcbc67409848cb972d46e71aa2d488b1&#32;a&#32;owl:Class&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:subClassOf&#32;&lowbar;:n5ffcbc67409848cb972d46e71aa2d488b1&#32;;  &#10; &#32; &#32; &#32; &#32;owl:equivalentClass&#32;&lowbar;:n5ffcbc67409848cb972d46e71aa2d488b1&#32;;  &#10; &#32; &#32; &#32; &#32;owl:unionOf&#32;&lowbar;:n5ffcbc67409848cb972d46e71aa2d488b4&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-139)|Pointer|<pre lang="Turtle"><code></code></pre>|
|[Section top](#minorfail-outcome-number-139)|Pointer|http://www.w3.org/2004/02/skos/core#Concept|

***
### MinorFail Outcome number 140

[Jump to summary definition](#summary-MinorFail-140)	|	[Previous MinorFail outcome](#minorfail-outcome-number-139)	|	[Next MinorFail outcome](#minorfail-outcome-number-141)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-src-aggregations-ontology|
|----|----|
|Title|Standalone&#32;module&#32;src/aggregations/ontology.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Module aggregations/ontology](https://gitlab.com/coswot/coswot-acimov/blob/HEAD/src/aggregations/ontology.ttl)|

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
|Name|module-src-aggregations-ontology|
|----|----|
|Title|Standalone&#32;module&#32;src/aggregations/ontology.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Module aggregations/ontology](https://gitlab.com/coswot/coswot-acimov/blob/HEAD/src/aggregations/ontology.ttl)|

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
|Name|module-src-aggregations-ontology|
|----|----|
|Title|Standalone&#32;module&#32;src/aggregations/ontology.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Module aggregations/ontology](https://gitlab.com/coswot/coswot-acimov/blob/HEAD/src/aggregations/ontology.ttl)|

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
|Name|module-src-aggregations-ontology|
|----|----|
|Title|Standalone&#32;module&#32;src/aggregations/ontology.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Module aggregations/ontology](https://gitlab.com/coswot/coswot-acimov/blob/HEAD/src/aggregations/ontology.ttl)|

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
|Name|module-src-aggregations-ontology|
|----|----|
|Title|Standalone&#32;module&#32;src/aggregations/ontology.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Module aggregations/ontology](https://gitlab.com/coswot/coswot-acimov/blob/HEAD/src/aggregations/ontology.ttl)|

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
|Name|module-src-aggregations-ontology|
|----|----|
|Title|Standalone&#32;module&#32;src/aggregations/ontology.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Module aggregations/ontology](https://gitlab.com/coswot/coswot-acimov/blob/HEAD/src/aggregations/ontology.ttl)|

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
|Name|module-src-aggregations-ontology|
|----|----|
|Title|Standalone&#32;module&#32;src/aggregations/ontology.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Module aggregations/ontology](https://gitlab.com/coswot/coswot-acimov/blob/HEAD/src/aggregations/ontology.ttl)|

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
|Name|module-src-aggregations-ontology|
|----|----|
|Title|Standalone&#32;module&#32;src/aggregations/ontology.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Module aggregations/ontology](https://gitlab.com/coswot/coswot-acimov/blob/HEAD/src/aggregations/ontology.ttl)|

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
|Name|module-src-actuations-ontology|
|----|----|
|Title|Standalone&#32;module&#32;src/actuations/ontology.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Module actuations/ontology](https://gitlab.com/coswot/coswot-acimov/blob/HEAD/src/actuations/ontology.ttl)|

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
|Name|module-src-actuations-ontology|
|----|----|
|Title|Standalone&#32;module&#32;src/actuations/ontology.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Module actuations/ontology](https://gitlab.com/coswot/coswot-acimov/blob/HEAD/src/actuations/ontology.ttl)|

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
|Name|module-src-actuations-ontology|
|----|----|
|Title|Standalone&#32;module&#32;src/actuations/ontology.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Module actuations/ontology](https://gitlab.com/coswot/coswot-acimov/blob/HEAD/src/actuations/ontology.ttl)|

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
|Name|module-src-actuations-ontology|
|----|----|
|Title|Standalone&#32;module&#32;src/actuations/ontology.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Module actuations/ontology](https://gitlab.com/coswot/coswot-acimov/blob/HEAD/src/actuations/ontology.ttl)|

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
|Name|module-src-actuations-ontology|
|----|----|
|Title|Standalone&#32;module&#32;src/actuations/ontology.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Module actuations/ontology](https://gitlab.com/coswot/coswot-acimov/blob/HEAD/src/actuations/ontology.ttl)|

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
|Name|module-src-actuations-ontology|
|----|----|
|Title|Standalone&#32;module&#32;src/actuations/ontology.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Module actuations/ontology](https://gitlab.com/coswot/coswot-acimov/blob/HEAD/src/actuations/ontology.ttl)|

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
|Name|module-src-actuations-ontology|
|----|----|
|Title|Standalone&#32;module&#32;src/actuations/ontology.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Module actuations/ontology](https://gitlab.com/coswot/coswot-acimov/blob/HEAD/src/actuations/ontology.ttl)|

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
|Name|module-src-actuations-ontology|
|----|----|
|Title|Standalone&#32;module&#32;src/actuations/ontology.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Module actuations/ontology](https://gitlab.com/coswot/coswot-acimov/blob/HEAD/src/actuations/ontology.ttl)|

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
|Name|module-src-actuations-ontology|
|----|----|
|Title|Standalone&#32;module&#32;src/actuations/ontology.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Module actuations/ontology](https://gitlab.com/coswot/coswot-acimov/blob/HEAD/src/actuations/ontology.ttl)|

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
|Name|module-src-actuations-ontology|
|----|----|
|Title|Standalone&#32;module&#32;src/actuations/ontology.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Module actuations/ontology](https://gitlab.com/coswot/coswot-acimov/blob/HEAD/src/actuations/ontology.ttl)|

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
|Name|module-src-actuations-ontology|
|----|----|
|Title|Standalone&#32;module&#32;src/actuations/ontology.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Module actuations/ontology](https://gitlab.com/coswot/coswot-acimov/blob/HEAD/src/actuations/ontology.ttl)|

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
|Name|module-src-actuations-ontology|
|----|----|
|Title|Standalone&#32;module&#32;src/actuations/ontology.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Module actuations/ontology](https://gitlab.com/coswot/coswot-acimov/blob/HEAD/src/actuations/ontology.ttl)|

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

[Jump to summary definition](#summary-MinorFail-160)	|	[Previous MinorFail outcome](#minorfail-outcome-number-159)	|	[Next MinorFail outcome](#minorfail-outcome-number-161)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-src-actuations-ontology|
|----|----|
|Title|Standalone&#32;module&#32;src/actuations/ontology.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Module actuations/ontology](https://gitlab.com/coswot/coswot-acimov/blob/HEAD/src/actuations/ontology.ttl)|

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
### MinorFail Outcome number 161

[Jump to summary definition](#summary-MinorFail-161)	|	[Previous MinorFail outcome](#minorfail-outcome-number-160)	|	[Next MinorFail outcome](#minorfail-outcome-number-162)

:exclamation:MinorFail outcome
#### Subject detail
|Name|modelet-building-automation-samples|
|----|----|
|Title|Standalone&#32;modelet&#32;domains/building-automation/samples/onto.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Modelet building-automation/samples](https://gitlab.com/coswot/coswot-acimov/blob/HEAD/domains/building-automation/samples/onto.ttl)|

#### Criterion detail
|Identifier|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|
|----|----|
|Title|Profile&#32;compatibility&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;check&#32;whether&#32;the&#32;test&#32;subject&#32;is&#32;compatible&#32;with&#32;a&#32;profile&#32;or&#32;not,&#32;and&#32;if&#32;it&#32;is&#32;not,&#32;why.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-161)|Identifier|`owl-el-profile-error`|
|[Section top](#minorfail-outcome-number-161)|Title|OWL&#32;EL&#32;Profile&#32;incompatible|
|[Section top](#minorfail-outcome-number-161)|Description|Anonymous&#32;individuals&#32;are&#32;not&#32;supported|
|[Section top](#minorfail-outcome-number-161)|Pointer|<pre lang="Turtle"><code>&#91;]&#32;a&#32;coswot:PropertyValue&#32;;  &#10; &#32; &#32; &#32; &#32;coswot:isMeasuredIn&#32; &#60;https://qudt.org/vocab/unit/M3> &#32;;  &#10; &#32; &#32; &#32; &#32;coswot:isValueOfProperty&#32;coswot:Volume&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-161)|Pointer|<pre lang="Turtle"><code>coswot:AirSample1M3&#32;a&#32;coswot:FeatureKind&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;Air&#32;Sample&#32;1&#32;m3&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;Type&#32;d'un&#32;échantillon&#32;d'air&#32;de&#32;1m3.&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32; &#60;https://w3id.org/coswot/building&lowbar;automation/samples> &#32;;  &#10; &#32; &#32; &#32; &#32;skos:inScheme&#32; &#60;https://w3id.org/coswot/building&lowbar;automation/samples> &#32;;  &#10; &#32; &#32; &#32; &#32;coswot:hasValue&#32; &#91;&#32;a&#32;coswot:PropertyValue&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;coswot:isMeasuredIn&#32; &#60;https://qudt.org/vocab/unit/M3> &#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;coswot:isValueOfProperty&#32;coswot:Volume&#32;]&#32;.</code></pre>|

***
### MinorFail Outcome number 162

[Jump to summary definition](#summary-MinorFail-162)	|	[Previous MinorFail outcome](#minorfail-outcome-number-161)	|	[Next MinorFail outcome](#minorfail-outcome-number-163)

:exclamation:MinorFail outcome
#### Subject detail
|Name|modelet-building-automation-samples|
|----|----|
|Title|Standalone&#32;modelet&#32;domains/building-automation/samples/onto.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Modelet building-automation/samples](https://gitlab.com/coswot/coswot-acimov/blob/HEAD/domains/building-automation/samples/onto.ttl)|

#### Criterion detail
|Identifier|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|
|----|----|
|Title|Profile&#32;compatibility&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;check&#32;whether&#32;the&#32;test&#32;subject&#32;is&#32;compatible&#32;with&#32;a&#32;profile&#32;or&#32;not,&#32;and&#32;if&#32;it&#32;is&#32;not,&#32;why.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-162)|Identifier|`owl-ql-profile-error`|
|[Section top](#minorfail-outcome-number-162)|Title|OWL&#32;QL&#32;Profile&#32;incompatible|
|[Section top](#minorfail-outcome-number-162)|Description|Anonymous&#32;individuals&#32;are&#32;not&#32;supported|
|[Section top](#minorfail-outcome-number-162)|Pointer|<pre lang="Turtle"><code>&#91;]&#32;a&#32;coswot:PropertyValue&#32;;  &#10; &#32; &#32; &#32; &#32;coswot:isMeasuredIn&#32; &#60;https://qudt.org/vocab/unit/M3> &#32;;  &#10; &#32; &#32; &#32; &#32;coswot:isValueOfProperty&#32;coswot:Volume&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-162)|Pointer|<pre lang="Turtle"><code>coswot:AirSample1M3&#32;a&#32;coswot:FeatureKind&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;Air&#32;Sample&#32;1&#32;m3&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;Type&#32;d'un&#32;échantillon&#32;d'air&#32;de&#32;1m3.&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32; &#60;https://w3id.org/coswot/building&lowbar;automation/samples> &#32;;  &#10; &#32; &#32; &#32; &#32;skos:inScheme&#32; &#60;https://w3id.org/coswot/building&lowbar;automation/samples> &#32;;  &#10; &#32; &#32; &#32; &#32;coswot:hasValue&#32; &#91;&#32;a&#32;coswot:PropertyValue&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;coswot:isMeasuredIn&#32; &#60;https://qudt.org/vocab/unit/M3> &#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;coswot:isValueOfProperty&#32;coswot:Volume&#32;]&#32;.</code></pre>|

***
### MinorFail Outcome number 163

[Jump to summary definition](#summary-MinorFail-163)	|	[Previous MinorFail outcome](#minorfail-outcome-number-162)	|	[Next MinorFail outcome](#minorfail-outcome-number-164)

:exclamation:MinorFail outcome
#### Subject detail
|Name|modelet-building-automation-features|
|----|----|
|Title|Standalone&#32;modelet&#32;domains/building-automation/features/onto.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Modelet building-automation/features](https://gitlab.com/coswot/coswot-acimov/blob/HEAD/domains/building-automation/features/onto.ttl)|

#### Criterion detail
|Identifier|[domain-and-range-referencing](https://ns.inria.fr/olivaw#domain-and-range-referencing)|
|----|----|
|Title|Domain&#32;and&#32;range&#32;referencing&#32;test|
|Description|A&#32;test&#32;case&#32;from&#32;the&#32;Best&#32;Practices&#32;tests&#32;checking&#32;if&#32;all&#32;the&#32;ranges&#32;and&#32;domains&#32;from&#32;the&#32;test&#32;subject&#32;point&#32;to&#32;terms&#32;that&#32;are&#32;defined&#32;in&#32;the&#32;vocabulary.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-163)|Identifier|`domain-out-of-vocabulary`|
|[Section top](#minorfail-outcome-number-163)|Title|Domain&#32;out&#32;of&#32;vocabulary|
|[Section top](#minorfail-outcome-number-163)|Description|Some&#32;properties&#32;have&#32;a&#32;domain&#32;out&#32;of&#32;the&#32;ontology|
|[Section top](#minorfail-outcome-number-163)|Pointer|<pre lang="Turtle"><code>:containsZone&#32;a&#32;owl:ObjectProperty,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:TransitiveProperty&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;contains&#32;zone&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;Relationship&#32;to&#32;the&#32;subzones&#32;of&#32;a&#32;major&#32;zone.&#32;A&#32;space&#32;zone&#32;c...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:domain&#32; &#60;https://w3id.org/bot#Zone>,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;:System,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;:Zone&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32; &#60;https://w3id.org/coswot/building&lowbar;automation/features> &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:range&#32; &#60;https://w3id.org/bot#Zone>,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;:System,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;:Zone&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:subClassOf&#32; &#60;https://w3id.org/bot#containsZone>,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;:containsZone&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:subPropertyOf&#32;:containsZone,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;:hasSubSystem&#32;;  &#10; &#32; &#32; &#32; &#32;owl:equivalentClass&#32; &#60;https://w3id.org/bot#containsZone> &#32;;  &#10; &#32; &#32; &#32; &#32;owl:equivalentProperty&#32;:containsZone&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-163)|Pointer|<pre lang="Turtle"><code>:Zone&#32;rdfs:subClassOf&#32;:Zone,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;coswot:System,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;coswot:Zone&#32;;  &#10; &#32; &#32; &#32; &#32;owl:equivalentClass&#32;coswot:Zone&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-163)|Pointer|<pre lang="Turtle"><code>:hasBuilding&#32;a&#32;owl:ObjectProperty&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;has&#32;building&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;Relation&#32;to&#32;buildings&#32;contained&#32;in&#32;a&#32;zone.&#32;The&#32;typical&#32;domai...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:domain&#32; &#60;https://w3id.org/bot#Zone>,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;:System,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;:Zone&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32; &#60;https://w3id.org/coswot/building&lowbar;automation/features> &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:range&#32; &#60;https://w3id.org/bot#Building>,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#60;https://w3id.org/bot#Zone>,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;:Building,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;:System,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;:Zone&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:subClassOf&#32; &#60;https://w3id.org/bot#hasBuilding>,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;:hasBuilding&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:subPropertyOf&#32;:containsZone,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;:hasBuilding,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;:hasSubSystem&#32;;  &#10; &#32; &#32; &#32; &#32;owl:equivalentClass&#32; &#60;https://w3id.org/bot#hasBuilding> &#32;;  &#10; &#32; &#32; &#32; &#32;owl:equivalentProperty&#32;:hasBuilding&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-163)|Pointer|<pre lang="Turtle"><code>:hasStorey&#32;a&#32;owl:ObjectProperty&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;has&#32;storey&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;Relation&#32;to&#32;storeys&#32;contained&#32;in&#32;a&#32;zone.&#32;The&#32;typical&#32;domains...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:domain&#32; &#60;https://w3id.org/bot#Zone>,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;:System,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;:Zone&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32; &#60;https://w3id.org/coswot/building&lowbar;automation/features> &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:range&#32; &#60;https://w3id.org/bot#Storey>,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#60;https://w3id.org/bot#Zone>,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;:Storey,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;:System,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;:Zone&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:subClassOf&#32; &#60;https://w3id.org/bot#hasStorey>,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;:hasStorey&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:subPropertyOf&#32;:containsZone,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;:hasStorey,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;:hasSubSystem&#32;;  &#10; &#32; &#32; &#32; &#32;owl:equivalentClass&#32; &#60;https://w3id.org/bot#hasStorey> &#32;;  &#10; &#32; &#32; &#32; &#32;owl:equivalentProperty&#32;:hasStorey&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-163)|Pointer|<pre lang="Turtle"><code>:hasSpace&#32;a&#32;owl:ObjectProperty&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;has&#32;space&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;Relation&#32;to&#32;spaces&#32;contained&#32;in&#32;a&#32;zone.&#32;The&#32;typical&#32;domains&#32;...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:domain&#32; &#60;https://w3id.org/bot#Zone>,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;:System,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;:Zone&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32; &#60;https://w3id.org/coswot/building&lowbar;automation/features> &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:range&#32; &#60;https://w3id.org/bot#Space>,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#60;https://w3id.org/bot#Zone>,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;:Space,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;:System,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;:Zone&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:subClassOf&#32; &#60;https://w3id.org/bot#hasSpace>,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;:hasSpace&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:subPropertyOf&#32;:containsZone,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;:hasSpace,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;:hasSubSystem&#32;;  &#10; &#32; &#32; &#32; &#32;owl:equivalentClass&#32; &#60;https://w3id.org/bot#hasSpace> &#32;;  &#10; &#32; &#32; &#32; &#32;owl:equivalentProperty&#32;:hasSpace&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-163)|Pointer|<pre lang="Turtle"><code>:canWalkTo&#32;a&#32;owl:ObjectProperty,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:SymmetricProperty&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;can&#32;walk&#32;to&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;Links&#32;a&#32;zone&#32;to&#32;another&#32;zone&#32;one&#32;can&#32;walk&#32;to.&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:domain&#32; &#60;https://w3id.org/bot#Zone>,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;:System,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;:Zone&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32; &#60;https://w3id.org/coswot/building&lowbar;automation/features> &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:range&#32; &#60;https://w3id.org/bot#Zone>,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;:System,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;:Zone&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:subPropertyOf&#32;:canWalkTo,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;:connectedTo&#32;;  &#10; &#32; &#32; &#32; &#32;owl:equivalentProperty&#32;:canWalkTo&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-163)|Pointer|<pre lang="Turtle"><code>:adjacentZone&#32;a&#32;owl:ObjectProperty,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:SymmetricProperty&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;adjacent&#32;zone&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;Relationship&#32;between&#32;two&#32;zones&#32;that&#32;share&#32;a&#32;common&#32;interface...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:domain&#32; &#60;https://w3id.org/bot#Zone>,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;:System,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;:Zone&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32; &#60;https://w3id.org/coswot/building&lowbar;automation/features> &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:range&#32; &#60;https://w3id.org/bot#Zone>,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;:System,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;:Zone&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:subPropertyOf&#32;:adjacentZone,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;:connectedTo&#32;;  &#10; &#32; &#32; &#32; &#32;owl:equivalentProperty&#32;:adjacentZone&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-163)|Pointer|<pre lang="Turtle"><code>:adjacentElement&#32;a&#32;owl:ObjectProperty&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;adjacent&#32;element&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;Relation&#32;between&#32;a&#32;zone&#32;and&#32;its&#32;adjacent&#32;building&#32;elements,&#32;...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:domain&#32; &#60;https://w3id.org/bot#Zone>,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;:System,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;:Zone&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32; &#60;https://w3id.org/coswot/building&lowbar;automation/features> &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:range&#32; &#60;https://w3id.org/bot#Element>,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;:BuildingElement,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;:System&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:subPropertyOf&#32;:adjacentElement,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;:connectedTo&#32;;  &#10; &#32; &#32; &#32; &#32;owl:equivalentProperty&#32;:adjacentElement&#32;.</code></pre>|

***
### MinorFail Outcome number 164

[Jump to summary definition](#summary-MinorFail-164)	|	[Previous MinorFail outcome](#minorfail-outcome-number-163)	|	[Next MinorFail outcome](#minorfail-outcome-number-165)

:exclamation:MinorFail outcome
#### Subject detail
|Name|modelet-building-automation-features|
|----|----|
|Title|Standalone&#32;modelet&#32;domains/building-automation/features/onto.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Modelet building-automation/features](https://gitlab.com/coswot/coswot-acimov/blob/HEAD/domains/building-automation/features/onto.ttl)|

#### Criterion detail
|Identifier|[domain-and-range-referencing](https://ns.inria.fr/olivaw#domain-and-range-referencing)|
|----|----|
|Title|Domain&#32;and&#32;range&#32;referencing&#32;test|
|Description|A&#32;test&#32;case&#32;from&#32;the&#32;Best&#32;Practices&#32;tests&#32;checking&#32;if&#32;all&#32;the&#32;ranges&#32;and&#32;domains&#32;from&#32;the&#32;test&#32;subject&#32;point&#32;to&#32;terms&#32;that&#32;are&#32;defined&#32;in&#32;the&#32;vocabulary.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-164)|Identifier|`range-out-of-vocabulary`|
|[Section top](#minorfail-outcome-number-164)|Title|Range&#32;out&#32;of&#32;vocabulary|
|[Section top](#minorfail-outcome-number-164)|Description|Some&#32;properties&#32;have&#32;a&#32;range&#32;out&#32;of&#32;the&#32;ontology|
|[Section top](#minorfail-outcome-number-164)|Pointer|<pre lang="Turtle"><code>:containsZone&#32;a&#32;owl:ObjectProperty,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:TransitiveProperty&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;contains&#32;zone&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;Relationship&#32;to&#32;the&#32;subzones&#32;of&#32;a&#32;major&#32;zone.&#32;A&#32;space&#32;zone&#32;c...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:domain&#32; &#60;https://w3id.org/bot#Zone>,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;:System,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;:Zone&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32; &#60;https://w3id.org/coswot/building&lowbar;automation/features> &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:range&#32; &#60;https://w3id.org/bot#Zone>,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;:System,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;:Zone&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:subClassOf&#32; &#60;https://w3id.org/bot#containsZone>,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;:containsZone&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:subPropertyOf&#32;:containsZone,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;:hasSubSystem&#32;;  &#10; &#32; &#32; &#32; &#32;owl:equivalentClass&#32; &#60;https://w3id.org/bot#containsZone> &#32;;  &#10; &#32; &#32; &#32; &#32;owl:equivalentProperty&#32;:containsZone&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-164)|Pointer|<pre lang="Turtle"><code>:Zone&#32;rdfs:subClassOf&#32;:Zone,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;coswot:System,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;coswot:Zone&#32;;  &#10; &#32; &#32; &#32; &#32;owl:equivalentClass&#32;coswot:Zone&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-164)|Pointer|<pre lang="Turtle"><code>:hasBuilding&#32;a&#32;owl:ObjectProperty&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;has&#32;building&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;Relation&#32;to&#32;buildings&#32;contained&#32;in&#32;a&#32;zone.&#32;The&#32;typical&#32;domai...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:domain&#32; &#60;https://w3id.org/bot#Zone>,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;:System,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;:Zone&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32; &#60;https://w3id.org/coswot/building&lowbar;automation/features> &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:range&#32; &#60;https://w3id.org/bot#Building>,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#60;https://w3id.org/bot#Zone>,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;:Building,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;:System,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;:Zone&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:subClassOf&#32; &#60;https://w3id.org/bot#hasBuilding>,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;:hasBuilding&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:subPropertyOf&#32;:containsZone,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;:hasBuilding,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;:hasSubSystem&#32;;  &#10; &#32; &#32; &#32; &#32;owl:equivalentClass&#32; &#60;https://w3id.org/bot#hasBuilding> &#32;;  &#10; &#32; &#32; &#32; &#32;owl:equivalentProperty&#32;:hasBuilding&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-164)|Pointer|<pre lang="Turtle"><code>:Building&#32;rdfs:subClassOf&#32;:Building,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;:Zone,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;coswot:Building,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;coswot:System,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;coswot:Zone&#32;;  &#10; &#32; &#32; &#32; &#32;owl:equivalentClass&#32;coswot:Building&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-164)|Pointer|<pre lang="Turtle"><code>:hasStorey&#32;a&#32;owl:ObjectProperty&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;has&#32;storey&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;Relation&#32;to&#32;storeys&#32;contained&#32;in&#32;a&#32;zone.&#32;The&#32;typical&#32;domains...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:domain&#32; &#60;https://w3id.org/bot#Zone>,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;:System,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;:Zone&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32; &#60;https://w3id.org/coswot/building&lowbar;automation/features> &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:range&#32; &#60;https://w3id.org/bot#Storey>,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#60;https://w3id.org/bot#Zone>,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;:Storey,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;:System,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;:Zone&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:subClassOf&#32; &#60;https://w3id.org/bot#hasStorey>,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;:hasStorey&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:subPropertyOf&#32;:containsZone,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;:hasStorey,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;:hasSubSystem&#32;;  &#10; &#32; &#32; &#32; &#32;owl:equivalentClass&#32; &#60;https://w3id.org/bot#hasStorey> &#32;;  &#10; &#32; &#32; &#32; &#32;owl:equivalentProperty&#32;:hasStorey&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-164)|Pointer|<pre lang="Turtle"><code>:Storey&#32;rdfs:subClassOf&#32;:Storey,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;:Zone,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;coswot:Storey,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;coswot:System,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;coswot:Zone&#32;;  &#10; &#32; &#32; &#32; &#32;owl:equivalentClass&#32;coswot:Storey&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-164)|Pointer|<pre lang="Turtle"><code>:hasSpace&#32;a&#32;owl:ObjectProperty&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;has&#32;space&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;Relation&#32;to&#32;spaces&#32;contained&#32;in&#32;a&#32;zone.&#32;The&#32;typical&#32;domains&#32;...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:domain&#32; &#60;https://w3id.org/bot#Zone>,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;:System,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;:Zone&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32; &#60;https://w3id.org/coswot/building&lowbar;automation/features> &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:range&#32; &#60;https://w3id.org/bot#Space>,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#60;https://w3id.org/bot#Zone>,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;:Space,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;:System,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;:Zone&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:subClassOf&#32; &#60;https://w3id.org/bot#hasSpace>,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;:hasSpace&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:subPropertyOf&#32;:containsZone,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;:hasSpace,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;:hasSubSystem&#32;;  &#10; &#32; &#32; &#32; &#32;owl:equivalentClass&#32; &#60;https://w3id.org/bot#hasSpace> &#32;;  &#10; &#32; &#32; &#32; &#32;owl:equivalentProperty&#32;:hasSpace&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-164)|Pointer|<pre lang="Turtle"><code>:Space&#32;rdfs:subClassOf&#32;:Space,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;:Zone,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;coswot:Space,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;coswot:System,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;coswot:Zone&#32;;  &#10; &#32; &#32; &#32; &#32;owl:equivalentClass&#32;coswot:Space&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-164)|Pointer|<pre lang="Turtle"><code>:canWalkTo&#32;a&#32;owl:ObjectProperty,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:SymmetricProperty&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;can&#32;walk&#32;to&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;Links&#32;a&#32;zone&#32;to&#32;another&#32;zone&#32;one&#32;can&#32;walk&#32;to.&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:domain&#32; &#60;https://w3id.org/bot#Zone>,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;:System,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;:Zone&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32; &#60;https://w3id.org/coswot/building&lowbar;automation/features> &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:range&#32; &#60;https://w3id.org/bot#Zone>,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;:System,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;:Zone&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:subPropertyOf&#32;:canWalkTo,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;:connectedTo&#32;;  &#10; &#32; &#32; &#32; &#32;owl:equivalentProperty&#32;:canWalkTo&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-164)|Pointer|<pre lang="Turtle"><code>:adjacentZone&#32;a&#32;owl:ObjectProperty,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:SymmetricProperty&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;adjacent&#32;zone&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;Relationship&#32;between&#32;two&#32;zones&#32;that&#32;share&#32;a&#32;common&#32;interface...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:domain&#32; &#60;https://w3id.org/bot#Zone>,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;:System,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;:Zone&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32; &#60;https://w3id.org/coswot/building&lowbar;automation/features> &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:range&#32; &#60;https://w3id.org/bot#Zone>,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;:System,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;:Zone&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:subPropertyOf&#32;:adjacentZone,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;:connectedTo&#32;;  &#10; &#32; &#32; &#32; &#32;owl:equivalentProperty&#32;:adjacentZone&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-164)|Pointer|<pre lang="Turtle"><code>:adjacentElement&#32;a&#32;owl:ObjectProperty&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;adjacent&#32;element&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;Relation&#32;between&#32;a&#32;zone&#32;and&#32;its&#32;adjacent&#32;building&#32;elements,&#32;...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:domain&#32; &#60;https://w3id.org/bot#Zone>,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;:System,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;:Zone&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32; &#60;https://w3id.org/coswot/building&lowbar;automation/features> &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:range&#32; &#60;https://w3id.org/bot#Element>,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;:BuildingElement,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;:System&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:subPropertyOf&#32;:adjacentElement,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;:connectedTo&#32;;  &#10; &#32; &#32; &#32; &#32;owl:equivalentProperty&#32;:adjacentElement&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-164)|Pointer|<pre lang="Turtle"><code>:Element&#32;rdfs:subClassOf&#32;:Element,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;coswot:BuildingElement,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;coswot:System&#32;;  &#10; &#32; &#32; &#32; &#32;owl:equivalentClass&#32;coswot:BuildingElement&#32;.</code></pre>|

***
### MinorFail Outcome number 165

[Jump to summary definition](#summary-MinorFail-165)	|	[Previous MinorFail outcome](#minorfail-outcome-number-164)	|	[Next MinorFail outcome](#minorfail-outcome-number-166)

:exclamation:MinorFail outcome
#### Subject detail
|Name|modelet-building-automation-features|
|----|----|
|Title|Standalone&#32;modelet&#32;domains/building-automation/features/onto.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Modelet building-automation/features](https://gitlab.com/coswot/coswot-acimov/blob/HEAD/domains/building-automation/features/onto.ttl)|

#### Criterion detail
|Identifier|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|
|----|----|
|Title|Profile&#32;compatibility&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;check&#32;whether&#32;the&#32;test&#32;subject&#32;is&#32;compatible&#32;with&#32;a&#32;profile&#32;or&#32;not,&#32;and&#32;if&#32;it&#32;is&#32;not,&#32;why.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-165)|Identifier|`owl-el-profile-error`|
|[Section top](#minorfail-outcome-number-165)|Title|OWL&#32;EL&#32;Profile&#32;incompatible|
|[Section top](#minorfail-outcome-number-165)|Description|Statement&#32;not&#32;supported|
|[Section top](#minorfail-outcome-number-165)|Pointer|<pre lang="Turtle"><code>coswot:canWalkTo&#32;a&#32;owl:ObjectProperty,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:SymmetricProperty&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;can&#32;walk&#32;to&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;Links&#32;a&#32;zone&#32;to&#32;another&#32;zone&#32;one&#32;can&#32;walk&#32;to.&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:domain&#32;coswot:Zone&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32; &#60;https://w3id.org/coswot/building&lowbar;automation/features> &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:range&#32;coswot:Zone&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:subPropertyOf&#32;coswot:connectedTo&#32;.</code></pre>|

***
### MinorFail Outcome number 166

[Jump to summary definition](#summary-MinorFail-166)	|	[Previous MinorFail outcome](#minorfail-outcome-number-165)	|	[Next MinorFail outcome](#minorfail-outcome-number-167)

:exclamation:MinorFail outcome
#### Subject detail
|Name|modelet-building-automation-features|
|----|----|
|Title|Standalone&#32;modelet&#32;domains/building-automation/features/onto.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Modelet building-automation/features](https://gitlab.com/coswot/coswot-acimov/blob/HEAD/domains/building-automation/features/onto.ttl)|

#### Criterion detail
|Identifier|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|
|----|----|
|Title|Profile&#32;compatibility&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;check&#32;whether&#32;the&#32;test&#32;subject&#32;is&#32;compatible&#32;with&#32;a&#32;profile&#32;or&#32;not,&#32;and&#32;if&#32;it&#32;is&#32;not,&#32;why.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-166)|Identifier|`owl-ql-profile-error`|
|[Section top](#minorfail-outcome-number-166)|Title|OWL&#32;QL&#32;Profile&#32;incompatible|
|[Section top](#minorfail-outcome-number-166)|Description|Statement&#32;not&#32;supported|
|[Section top](#minorfail-outcome-number-166)|Pointer|<pre lang="Turtle"><code>coswot:containsZone&#32;a&#32;owl:ObjectProperty,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:TransitiveProperty&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;contains&#32;zone&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;Relationship&#32;to&#32;the&#32;subzones&#32;of&#32;a&#32;major&#32;zone.&#32;A&#32;space&#32;zone&#32;c...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:domain&#32;coswot:Zone&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32; &#60;https://w3id.org/coswot/building&lowbar;automation/features> &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:range&#32;coswot:Zone&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:subPropertyOf&#32;coswot:hasSubSystem&#32;;  &#10; &#32; &#32; &#32; &#32;owl:equivalentClass&#32; &#60;https://w3id.org/bot#containsZone> &#32;.</code></pre>|

***
### MinorFail Outcome number 167

[Jump to summary definition](#summary-MinorFail-167)	|	[Previous MinorFail outcome](#minorfail-outcome-number-166)	|	Next MinorFail outcome

:exclamation:MinorFail outcome
#### Subject detail
|Name|modelet-building-automation-features|
|----|----|
|Title|Standalone&#32;modelet&#32;domains/building-automation/features/onto.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Modelet building-automation/features](https://gitlab.com/coswot/coswot-acimov/blob/HEAD/domains/building-automation/features/onto.ttl)|

#### Criterion detail
|Identifier|[terms-differenciation](https://ns.inria.fr/olivaw#terms-differenciation)|
|----|----|
|Title|Terms&#32;differenciation&#32;test|
|Description|A&#32;test&#32;case&#32;from&#32;the&#32;Best&#32;Practices&#32;tests&#32;checking&#32;if&#32;all&#32;the&#32;terms&#32;are&#32;different&#32;enough&#32;from&#32;each&#32;other&#32;according&#32;to&#32;the&#32;Levenshtein&#32;distance&#32;metric.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-167)|Identifier|`too-close-terms`|
|[Section top](#minorfail-outcome-number-167)|Title|Too&#32;close&#32;terms|
|[Section top](#minorfail-outcome-number-167)|Description|Some&#32;terms&#32;are&#32;too&#32;similar|
|[Section top](#minorfail-outcome-number-167)|Pointer|<pre lang="Turtle"><code>:Room&#32;a&#32;owl:Class&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;Room&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;A&#32;part&#32;of&#32;the&#32;physical&#32;world&#32;or&#32;a&#32;virtual&#32;world&#32;whose&#32;3D&#32;spa...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32; &#60;https://w3id.org/coswot/building&lowbar;automation/features> &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:subClassOf&#32;:Space&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-167)|Pointer|<pre lang="Turtle"><code>:Door&#32;a&#32;owl:Class&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;Door&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;Definition&#32;from&#32;ISO&#32;6707-1:1989:&#32;Construction&#32;for&#32;closing&#32;an...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32; &#60;https://w3id.org/coswot/building&lowbar;automation/features> &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:subClassOf&#32;:BuildingElement&#32;.</code></pre>|

***

</details>

***
