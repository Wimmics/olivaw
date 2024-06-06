# Test Report Markdown Export

This file is an export of the RDF test report made out of [EARL vocabulary](https://www.w3.org/TR/EARL10/)

This test is powered by Corese, check the [website](https://project.inria.fr/corese/) and the [repository](https://github.com/Wimmics/corese)

The original test report is available in turtle syntax [here](./model-test-manual-NicoRobertIn-2024-06-06T11-25-56.ttl).

# Test Context

Here is some context about under which context this test was made

|Assertor|[NicoRobertIn](https://gitlab.com/NicoRobertIn)|
|----|-----|
|Title|NicoRobertIn using manual script|
|Description|Test triggered by [@NicoRobertIn](https://gitlab.com/NicoRobertIn) by manual trigger|
|Script|[model test suite](https://github.com/Wimmics/olivaw/blob/main/olivaw/test/model/suite.py)
|Date|2024-06-06 11:25:39|

***


# Statistic summary

Here is a short overview for this test report

168 Outcomes

:boom:1 MajorFail, :exclamation:167 MinorFail, :warning:0 CannotTell, :grey_question:0 NotTested, :white_check_mark:0 Pass

<div  style="border-radius: 12px; height: 25px; overflow: hidden"><img src="../assets/red.png" width="1%" height="25px"/><img src="../assets/orange.png" width="99%" height="25px"/><img src="../assets/grey.png" width="0%" height="25px"/><img src="../assets/white.png" width="0%" height="25px"/><img src="../assets/green.png" width="0%" height="25px"/></div>

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
|[Chapter top](#majorfail-outcomes)|<div id="summary-MajorFail-1">1/1</div>|:boom:MajorFail|`module-src-coswot-saref`|[syntax](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#syntax)|Test subject has syntax errors|[Jump](#majorfail-outcome-number-1)|

***

## MajorFail Outcomes Details

This subchapter gives more details to the :boom:MajorFail outcomes

### MajorFail Outcome number 1

[Jump to summary definition](#summary-MajorFail-1)	|	Previous MajorFail outcome	|	Next MajorFail outcome

:boom:MajorFail outcome
#### Subject detail
|Name|module-src-coswot-saref|
|----|----|
|Title|Standalone module src/coswot-saref.ttl from branch main|
|Composition|- [Module coswot-saref](https://gitlab.com/coswot/coswot-acimov/blob/main/src/coswot-saref.ttl)|

#### Criterion detail
|Identifier|[syntax](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#syntax)|
|----|----|
|Title|Syntax test|
|Description|A test meant to check wether the test subject is syntaxically correct or not.|

#### Outcome Detail
|Jump|Type|:boom:MajorFail|
|----|----|----|
|[Section top](#majorfail-outcome-number-1)|Identifier|`syntax-error`|
|[Section top](#majorfail-outcome-number-1)|Title|Test subject has syntax errors|
|[Section top](#majorfail-outcome-number-1)|Description|The subject has turtle syntax errors that makes it unprocessable by an engine|
|[Section top](#majorfail-outcome-number-1)|Pointer|<pre lang="Turtle"><code>Encountered &#34;.&#34; at line 113, column 36.</code></pre>|

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
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-1">1/167</div>|:exclamation:MinorFail|`module-src-systems-ontology`|[profile-compatibility](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#profile-compatibility)|OWL RL Profile incompatible|[Jump](#minorfail-outcome-number-1)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-2">2/167</div>|:exclamation:MinorFail|`module-src-systems-ontology`|[profile-compatibility](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#profile-compatibility)|OWL RL Profile incompatible|[Jump](#minorfail-outcome-number-2)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-3">3/167</div>|:exclamation:MinorFail|`module-src-systems-ontology`|[profile-compatibility](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#profile-compatibility)|OWL QL Profile incompatible|[Jump](#minorfail-outcome-number-3)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-4">4/167</div>|:exclamation:MinorFail|`module-src-systems-ontology`|[profile-compatibility](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#profile-compatibility)|OWL EL Profile incompatible|[Jump](#minorfail-outcome-number-4)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-5">5/167</div>|:exclamation:MinorFail|`module-src-states-ontology-catalog`|[domain-and-range-referencing](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#domain-and-range-referencing)|Domain out of vocabulary|[Jump](#minorfail-outcome-number-5)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-6">6/167</div>|:exclamation:MinorFail|`module-src-states-ontology-catalog`|[domain-and-range-referencing](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#domain-and-range-referencing)|Range out of vocabulary|[Jump](#minorfail-outcome-number-6)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-7">7/167</div>|:exclamation:MinorFail|`module-src-states-ontology-catalog`|[profile-compatibility](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#profile-compatibility)|OWL QL Profile incompatible|[Jump](#minorfail-outcome-number-7)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-8">8/167</div>|:exclamation:MinorFail|`module-src-states-ontology-catalog`|[profile-compatibility](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#profile-compatibility)|OWL QL Profile incompatible|[Jump](#minorfail-outcome-number-8)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-9">9/167</div>|:exclamation:MinorFail|`module-src-states-ontology-catalog`|[profile-compatibility](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#profile-compatibility)|OWL QL Profile incompatible|[Jump](#minorfail-outcome-number-9)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-10">10/167</div>|:exclamation:MinorFail|`module-src-states-ontology-catalog`|[profile-compatibility](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#profile-compatibility)|OWL EL Profile incompatible|[Jump](#minorfail-outcome-number-10)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-11">11/167</div>|:exclamation:MinorFail|`module-src-states-ontology-catalog`|[profile-compatibility](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#profile-compatibility)|OWL EL Profile incompatible|[Jump](#minorfail-outcome-number-11)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-12">12/167</div>|:exclamation:MinorFail|`module-src-states-ontology`|[domain-and-range-referencing](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#domain-and-range-referencing)|Domain out of vocabulary|[Jump](#minorfail-outcome-number-12)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-13">13/167</div>|:exclamation:MinorFail|`module-src-states-ontology`|[domain-and-range-referencing](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#domain-and-range-referencing)|Range out of vocabulary|[Jump](#minorfail-outcome-number-13)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-14">14/167</div>|:exclamation:MinorFail|`module-src-states-ontology`|[profile-compatibility](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#profile-compatibility)|OWL RL Profile incompatible|[Jump](#minorfail-outcome-number-14)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-15">15/167</div>|:exclamation:MinorFail|`module-src-states-ontology`|[profile-compatibility](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#profile-compatibility)|OWL RL Profile incompatible|[Jump](#minorfail-outcome-number-15)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-16">16/167</div>|:exclamation:MinorFail|`module-src-states-ontology`|[profile-compatibility](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#profile-compatibility)|OWL RL Profile incompatible|[Jump](#minorfail-outcome-number-16)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-17">17/167</div>|:exclamation:MinorFail|`module-src-states-ontology`|[profile-compatibility](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#profile-compatibility)|OWL RL Profile incompatible|[Jump](#minorfail-outcome-number-17)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-18">18/167</div>|:exclamation:MinorFail|`module-src-states-ontology`|[profile-compatibility](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#profile-compatibility)|OWL QL Profile incompatible|[Jump](#minorfail-outcome-number-18)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-19">19/167</div>|:exclamation:MinorFail|`module-src-states-ontology`|[profile-compatibility](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#profile-compatibility)|OWL QL Profile incompatible|[Jump](#minorfail-outcome-number-19)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-20">20/167</div>|:exclamation:MinorFail|`module-src-states-ontology`|[profile-compatibility](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#profile-compatibility)|OWL QL Profile incompatible|[Jump](#minorfail-outcome-number-20)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-21">21/167</div>|:exclamation:MinorFail|`module-src-states-ontology`|[profile-compatibility](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#profile-compatibility)|OWL QL Profile incompatible|[Jump](#minorfail-outcome-number-21)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-22">22/167</div>|:exclamation:MinorFail|`module-src-states-ontology`|[profile-compatibility](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#profile-compatibility)|OWL QL Profile incompatible|[Jump](#minorfail-outcome-number-22)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-23">23/167</div>|:exclamation:MinorFail|`module-src-states-ontology`|[profile-compatibility](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#profile-compatibility)|OWL QL Profile incompatible|[Jump](#minorfail-outcome-number-23)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-24">24/167</div>|:exclamation:MinorFail|`module-src-states-ontology`|[profile-compatibility](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#profile-compatibility)|OWL EL Profile incompatible|[Jump](#minorfail-outcome-number-24)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-25">25/167</div>|:exclamation:MinorFail|`module-src-states-ontology`|[profile-compatibility](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#profile-compatibility)|OWL EL Profile incompatible|[Jump](#minorfail-outcome-number-25)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-26">26/167</div>|:exclamation:MinorFail|`module-src-states-ontology`|[profile-compatibility](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#profile-compatibility)|OWL EL Profile incompatible|[Jump](#minorfail-outcome-number-26)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-27">27/167</div>|:exclamation:MinorFail|`module-src-states-ontology`|[profile-compatibility](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#profile-compatibility)|OWL EL Profile incompatible|[Jump](#minorfail-outcome-number-27)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-28">28/167</div>|:exclamation:MinorFail|`module-src-services-operations-ontology`|[profile-compatibility](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#profile-compatibility)|OWL RL Profile incompatible|[Jump](#minorfail-outcome-number-28)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-29">29/167</div>|:exclamation:MinorFail|`module-src-services-operations-ontology`|[profile-compatibility](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#profile-compatibility)|OWL RL Profile incompatible|[Jump](#minorfail-outcome-number-29)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-30">30/167</div>|:exclamation:MinorFail|`module-src-services-operations-ontology`|[profile-compatibility](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#profile-compatibility)|OWL RL Profile incompatible|[Jump](#minorfail-outcome-number-30)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-31">31/167</div>|:exclamation:MinorFail|`module-src-services-operations-ontology`|[profile-compatibility](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#profile-compatibility)|OWL RL Profile incompatible|[Jump](#minorfail-outcome-number-31)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-32">32/167</div>|:exclamation:MinorFail|`module-src-services-operations-ontology`|[profile-compatibility](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#profile-compatibility)|OWL QL Profile incompatible|[Jump](#minorfail-outcome-number-32)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-33">33/167</div>|:exclamation:MinorFail|`module-src-services-operations-ontology`|[profile-compatibility](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#profile-compatibility)|OWL QL Profile incompatible|[Jump](#minorfail-outcome-number-33)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-34">34/167</div>|:exclamation:MinorFail|`module-src-services-operations-ontology`|[profile-compatibility](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#profile-compatibility)|OWL QL Profile incompatible|[Jump](#minorfail-outcome-number-34)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-35">35/167</div>|:exclamation:MinorFail|`module-src-services-operations-ontology`|[profile-compatibility](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#profile-compatibility)|OWL QL Profile incompatible|[Jump](#minorfail-outcome-number-35)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-36">36/167</div>|:exclamation:MinorFail|`module-src-services-operations-ontology`|[profile-compatibility](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#profile-compatibility)|OWL QL Profile incompatible|[Jump](#minorfail-outcome-number-36)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-37">37/167</div>|:exclamation:MinorFail|`module-src-services-operations-ontology`|[profile-compatibility](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#profile-compatibility)|OWL EL Profile incompatible|[Jump](#minorfail-outcome-number-37)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-38">38/167</div>|:exclamation:MinorFail|`module-src-services-operations-ontology`|[profile-compatibility](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#profile-compatibility)|OWL EL Profile incompatible|[Jump](#minorfail-outcome-number-38)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-39">39/167</div>|:exclamation:MinorFail|`module-src-services-operations-ontology`|[profile-compatibility](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#profile-compatibility)|OWL EL Profile incompatible|[Jump](#minorfail-outcome-number-39)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-40">40/167</div>|:exclamation:MinorFail|`module-src-services-operations-ontology`|[profile-compatibility](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#profile-compatibility)|OWL EL Profile incompatible|[Jump](#minorfail-outcome-number-40)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-41">41/167</div>|:exclamation:MinorFail|`module-src-services-operations-ontology`|[term-referencing](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#term-referencing)|Term not referenced to a module|[Jump](#minorfail-outcome-number-41)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-42">42/167</div>|:exclamation:MinorFail|`module-src-samples-ontology`|[profile-compatibility](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#profile-compatibility)|OWL QL Profile incompatible|[Jump](#minorfail-outcome-number-42)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-43">43/167</div>|:exclamation:MinorFail|`module-src-samples-ontology`|[profile-compatibility](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#profile-compatibility)|OWL QL Profile incompatible|[Jump](#minorfail-outcome-number-43)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-44">44/167</div>|:exclamation:MinorFail|`module-src-samples-ontology`|[profile-compatibility](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#profile-compatibility)|OWL EL Profile incompatible|[Jump](#minorfail-outcome-number-44)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-45">45/167</div>|:exclamation:MinorFail|`module-src-property-values-ontology`|[domain-and-range-referencing](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#domain-and-range-referencing)|Range out of vocabulary|[Jump](#minorfail-outcome-number-45)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-46">46/167</div>|:exclamation:MinorFail|`module-src-property-values-ontology`|[profile-compatibility](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#profile-compatibility)|OWL RL Profile incompatible|[Jump](#minorfail-outcome-number-46)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-47">47/167</div>|:exclamation:MinorFail|`module-src-property-values-ontology`|[profile-compatibility](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#profile-compatibility)|OWL RL Profile incompatible|[Jump](#minorfail-outcome-number-47)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-48">48/167</div>|:exclamation:MinorFail|`module-src-property-values-ontology`|[profile-compatibility](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#profile-compatibility)|OWL RL Profile incompatible|[Jump](#minorfail-outcome-number-48)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-49">49/167</div>|:exclamation:MinorFail|`module-src-property-values-ontology`|[profile-compatibility](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#profile-compatibility)|OWL QL Profile incompatible|[Jump](#minorfail-outcome-number-49)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-50">50/167</div>|:exclamation:MinorFail|`module-src-property-values-ontology`|[profile-compatibility](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#profile-compatibility)|OWL QL Profile incompatible|[Jump](#minorfail-outcome-number-50)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-51">51/167</div>|:exclamation:MinorFail|`module-src-property-values-ontology`|[profile-compatibility](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#profile-compatibility)|OWL QL Profile incompatible|[Jump](#minorfail-outcome-number-51)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-52">52/167</div>|:exclamation:MinorFail|`module-src-property-values-ontology`|[profile-compatibility](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#profile-compatibility)|OWL QL Profile incompatible|[Jump](#minorfail-outcome-number-52)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-53">53/167</div>|:exclamation:MinorFail|`module-src-property-values-ontology`|[profile-compatibility](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#profile-compatibility)|OWL EL Profile incompatible|[Jump](#minorfail-outcome-number-53)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-54">54/167</div>|:exclamation:MinorFail|`module-src-property-values-ontology`|[profile-compatibility](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#profile-compatibility)|OWL EL Profile incompatible|[Jump](#minorfail-outcome-number-54)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-55">55/167</div>|:exclamation:MinorFail|`module-src-property-values-ontology`|[profile-compatibility](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#profile-compatibility)|OWL EL Profile incompatible|[Jump](#minorfail-outcome-number-55)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-56">56/167</div>|:exclamation:MinorFail|`module-src-properties-ontology-catalogs`|[domain-and-range-referencing](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#domain-and-range-referencing)|Domain out of vocabulary|[Jump](#minorfail-outcome-number-56)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-57">57/167</div>|:exclamation:MinorFail|`module-src-properties-ontology-catalogs`|[domain-and-range-referencing](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#domain-and-range-referencing)|Range out of vocabulary|[Jump](#minorfail-outcome-number-57)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-58">58/167</div>|:exclamation:MinorFail|`module-src-properties-ontology-catalogs`|[profile-compatibility](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#profile-compatibility)|OWL QL Profile incompatible|[Jump](#minorfail-outcome-number-58)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-59">59/167</div>|:exclamation:MinorFail|`module-src-properties-ontology-catalogs`|[profile-compatibility](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#profile-compatibility)|OWL QL Profile incompatible|[Jump](#minorfail-outcome-number-59)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-60">60/167</div>|:exclamation:MinorFail|`module-src-properties-ontology-catalogs`|[profile-compatibility](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#profile-compatibility)|OWL QL Profile incompatible|[Jump](#minorfail-outcome-number-60)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-61">61/167</div>|:exclamation:MinorFail|`module-src-properties-ontology-catalogs`|[profile-compatibility](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#profile-compatibility)|OWL EL Profile incompatible|[Jump](#minorfail-outcome-number-61)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-62">62/167</div>|:exclamation:MinorFail|`module-src-properties-ontology-catalogs`|[profile-compatibility](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#profile-compatibility)|OWL EL Profile incompatible|[Jump](#minorfail-outcome-number-62)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-63">63/167</div>|:exclamation:MinorFail|`module-src-properties-ontology`|[domain-and-range-referencing](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#domain-and-range-referencing)|Domain out of vocabulary|[Jump](#minorfail-outcome-number-63)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-64">64/167</div>|:exclamation:MinorFail|`module-src-properties-ontology`|[domain-and-range-referencing](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#domain-and-range-referencing)|Range out of vocabulary|[Jump](#minorfail-outcome-number-64)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-65">65/167</div>|:exclamation:MinorFail|`module-src-properties-ontology`|[profile-compatibility](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#profile-compatibility)|OWL RL Profile incompatible|[Jump](#minorfail-outcome-number-65)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-66">66/167</div>|:exclamation:MinorFail|`module-src-properties-ontology`|[profile-compatibility](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#profile-compatibility)|OWL RL Profile incompatible|[Jump](#minorfail-outcome-number-66)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-67">67/167</div>|:exclamation:MinorFail|`module-src-properties-ontology`|[profile-compatibility](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#profile-compatibility)|OWL RL Profile incompatible|[Jump](#minorfail-outcome-number-67)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-68">68/167</div>|:exclamation:MinorFail|`module-src-properties-ontology`|[profile-compatibility](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#profile-compatibility)|OWL QL Profile incompatible|[Jump](#minorfail-outcome-number-68)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-69">69/167</div>|:exclamation:MinorFail|`module-src-properties-ontology`|[profile-compatibility](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#profile-compatibility)|OWL QL Profile incompatible|[Jump](#minorfail-outcome-number-69)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-70">70/167</div>|:exclamation:MinorFail|`module-src-properties-ontology`|[profile-compatibility](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#profile-compatibility)|OWL QL Profile incompatible|[Jump](#minorfail-outcome-number-70)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-71">71/167</div>|:exclamation:MinorFail|`module-src-properties-ontology`|[profile-compatibility](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#profile-compatibility)|OWL QL Profile incompatible|[Jump](#minorfail-outcome-number-71)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-72">72/167</div>|:exclamation:MinorFail|`module-src-properties-ontology`|[profile-compatibility](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#profile-compatibility)|OWL EL Profile incompatible|[Jump](#minorfail-outcome-number-72)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-73">73/167</div>|:exclamation:MinorFail|`module-src-properties-ontology`|[profile-compatibility](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#profile-compatibility)|OWL EL Profile incompatible|[Jump](#minorfail-outcome-number-73)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-74">74/167</div>|:exclamation:MinorFail|`module-src-properties-ontology`|[profile-compatibility](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#profile-compatibility)|OWL EL Profile incompatible|[Jump](#minorfail-outcome-number-74)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-75">75/167</div>|:exclamation:MinorFail|`module-src-procedures-ontology`|[domain-and-range-referencing](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#domain-and-range-referencing)|Range out of vocabulary|[Jump](#minorfail-outcome-number-75)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-76">76/167</div>|:exclamation:MinorFail|`module-src-procedures-ontology`|[profile-compatibility](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#profile-compatibility)|OWL RL Profile incompatible|[Jump](#minorfail-outcome-number-76)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-77">77/167</div>|:exclamation:MinorFail|`module-src-procedures-ontology`|[profile-compatibility](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#profile-compatibility)|OWL RL Profile incompatible|[Jump](#minorfail-outcome-number-77)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-78">78/167</div>|:exclamation:MinorFail|`module-src-procedures-ontology`|[profile-compatibility](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#profile-compatibility)|OWL QL Profile incompatible|[Jump](#minorfail-outcome-number-78)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-79">79/167</div>|:exclamation:MinorFail|`module-src-procedures-ontology`|[profile-compatibility](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#profile-compatibility)|OWL QL Profile incompatible|[Jump](#minorfail-outcome-number-79)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-80">80/167</div>|:exclamation:MinorFail|`module-src-procedures-ontology`|[profile-compatibility](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#profile-compatibility)|OWL QL Profile incompatible|[Jump](#minorfail-outcome-number-80)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-81">81/167</div>|:exclamation:MinorFail|`module-src-procedures-ontology`|[profile-compatibility](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#profile-compatibility)|OWL EL Profile incompatible|[Jump](#minorfail-outcome-number-81)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-82">82/167</div>|:exclamation:MinorFail|`module-src-procedures-ontology`|[profile-compatibility](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#profile-compatibility)|OWL EL Profile incompatible|[Jump](#minorfail-outcome-number-82)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-83">83/167</div>|:exclamation:MinorFail|`module-src-observations-ontology`|[profile-compatibility](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#profile-compatibility)|OWL RL Profile incompatible|[Jump](#minorfail-outcome-number-83)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-84">84/167</div>|:exclamation:MinorFail|`module-src-observations-ontology`|[profile-compatibility](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#profile-compatibility)|OWL RL Profile incompatible|[Jump](#minorfail-outcome-number-84)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-85">85/167</div>|:exclamation:MinorFail|`module-src-observations-ontology`|[profile-compatibility](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#profile-compatibility)|OWL RL Profile incompatible|[Jump](#minorfail-outcome-number-85)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-86">86/167</div>|:exclamation:MinorFail|`module-src-observations-ontology`|[profile-compatibility](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#profile-compatibility)|OWL RL Profile incompatible|[Jump](#minorfail-outcome-number-86)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-87">87/167</div>|:exclamation:MinorFail|`module-src-observations-ontology`|[profile-compatibility](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#profile-compatibility)|OWL QL Profile incompatible|[Jump](#minorfail-outcome-number-87)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-88">88/167</div>|:exclamation:MinorFail|`module-src-observations-ontology`|[profile-compatibility](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#profile-compatibility)|OWL QL Profile incompatible|[Jump](#minorfail-outcome-number-88)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-89">89/167</div>|:exclamation:MinorFail|`module-src-observations-ontology`|[profile-compatibility](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#profile-compatibility)|OWL QL Profile incompatible|[Jump](#minorfail-outcome-number-89)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-90">90/167</div>|:exclamation:MinorFail|`module-src-observations-ontology`|[profile-compatibility](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#profile-compatibility)|OWL QL Profile incompatible|[Jump](#minorfail-outcome-number-90)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-91">91/167</div>|:exclamation:MinorFail|`module-src-observations-ontology`|[profile-compatibility](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#profile-compatibility)|OWL EL Profile incompatible|[Jump](#minorfail-outcome-number-91)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-92">92/167</div>|:exclamation:MinorFail|`module-src-observations-ontology`|[profile-compatibility](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#profile-compatibility)|OWL EL Profile incompatible|[Jump](#minorfail-outcome-number-92)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-93">93/167</div>|:exclamation:MinorFail|`module-src-observations-ontology`|[profile-compatibility](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#profile-compatibility)|OWL EL Profile incompatible|[Jump](#minorfail-outcome-number-93)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-94">94/167</div>|:exclamation:MinorFail|`module-src-observations-ontology`|[profile-compatibility](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#profile-compatibility)|OWL EL Profile incompatible|[Jump](#minorfail-outcome-number-94)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-95">95/167</div>|:exclamation:MinorFail|`module-src-functions-commands-ontology`|[profile-compatibility](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#profile-compatibility)|OWL RL Profile incompatible|[Jump](#minorfail-outcome-number-95)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-96">96/167</div>|:exclamation:MinorFail|`module-src-functions-commands-ontology`|[profile-compatibility](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#profile-compatibility)|OWL RL Profile incompatible|[Jump](#minorfail-outcome-number-96)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-97">97/167</div>|:exclamation:MinorFail|`module-src-functions-commands-ontology`|[profile-compatibility](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#profile-compatibility)|OWL RL Profile incompatible|[Jump](#minorfail-outcome-number-97)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-98">98/167</div>|:exclamation:MinorFail|`module-src-functions-commands-ontology`|[profile-compatibility](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#profile-compatibility)|OWL QL Profile incompatible|[Jump](#minorfail-outcome-number-98)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-99">99/167</div>|:exclamation:MinorFail|`module-src-functions-commands-ontology`|[profile-compatibility](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#profile-compatibility)|OWL QL Profile incompatible|[Jump](#minorfail-outcome-number-99)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-100">100/167</div>|:exclamation:MinorFail|`module-src-functions-commands-ontology`|[profile-compatibility](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#profile-compatibility)|OWL QL Profile incompatible|[Jump](#minorfail-outcome-number-100)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-101">101/167</div>|:exclamation:MinorFail|`module-src-functions-commands-ontology`|[profile-compatibility](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#profile-compatibility)|OWL QL Profile incompatible|[Jump](#minorfail-outcome-number-101)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-102">102/167</div>|:exclamation:MinorFail|`module-src-functions-commands-ontology`|[profile-compatibility](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#profile-compatibility)|OWL EL Profile incompatible|[Jump](#minorfail-outcome-number-102)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-103">103/167</div>|:exclamation:MinorFail|`module-src-functions-commands-ontology`|[profile-compatibility](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#profile-compatibility)|OWL EL Profile incompatible|[Jump](#minorfail-outcome-number-103)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-104">104/167</div>|:exclamation:MinorFail|`module-src-functions-commands-ontology`|[profile-compatibility](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#profile-compatibility)|OWL EL Profile incompatible|[Jump](#minorfail-outcome-number-104)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-105">105/167</div>|:exclamation:MinorFail|`module-src-functions-commands-ontology`|[term-referencing](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#term-referencing)|Term not referenced to a module|[Jump](#minorfail-outcome-number-105)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-106">106/167</div>|:exclamation:MinorFail|`module-src-features-ontology-catalogs`|[profile-compatibility](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#profile-compatibility)|OWL QL Profile incompatible|[Jump](#minorfail-outcome-number-106)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-107">107/167</div>|:exclamation:MinorFail|`module-src-features-ontology-catalogs`|[profile-compatibility](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#profile-compatibility)|OWL QL Profile incompatible|[Jump](#minorfail-outcome-number-107)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-108">108/167</div>|:exclamation:MinorFail|`module-src-features-ontology-catalogs`|[profile-compatibility](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#profile-compatibility)|OWL EL Profile incompatible|[Jump](#minorfail-outcome-number-108)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-109">109/167</div>|:exclamation:MinorFail|`module-src-features-ontology-catalogs`|[profile-compatibility](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#profile-compatibility)|OWL EL Profile incompatible|[Jump](#minorfail-outcome-number-109)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-110">110/167</div>|:exclamation:MinorFail|`module-src-features-ontology`|[profile-compatibility](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#profile-compatibility)|OWL RL Profile incompatible|[Jump](#minorfail-outcome-number-110)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-111">111/167</div>|:exclamation:MinorFail|`module-src-features-ontology`|[profile-compatibility](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#profile-compatibility)|OWL RL Profile incompatible|[Jump](#minorfail-outcome-number-111)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-112">112/167</div>|:exclamation:MinorFail|`module-src-features-ontology`|[profile-compatibility](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#profile-compatibility)|OWL RL Profile incompatible|[Jump](#minorfail-outcome-number-112)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-113">113/167</div>|:exclamation:MinorFail|`module-src-features-ontology`|[profile-compatibility](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#profile-compatibility)|OWL QL Profile incompatible|[Jump](#minorfail-outcome-number-113)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-114">114/167</div>|:exclamation:MinorFail|`module-src-features-ontology`|[profile-compatibility](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#profile-compatibility)|OWL QL Profile incompatible|[Jump](#minorfail-outcome-number-114)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-115">115/167</div>|:exclamation:MinorFail|`module-src-features-ontology`|[profile-compatibility](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#profile-compatibility)|OWL QL Profile incompatible|[Jump](#minorfail-outcome-number-115)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-116">116/167</div>|:exclamation:MinorFail|`module-src-features-ontology`|[profile-compatibility](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#profile-compatibility)|OWL QL Profile incompatible|[Jump](#minorfail-outcome-number-116)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-117">117/167</div>|:exclamation:MinorFail|`module-src-features-ontology`|[profile-compatibility](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#profile-compatibility)|OWL EL Profile incompatible|[Jump](#minorfail-outcome-number-117)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-118">118/167</div>|:exclamation:MinorFail|`module-src-features-ontology`|[profile-compatibility](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#profile-compatibility)|OWL EL Profile incompatible|[Jump](#minorfail-outcome-number-118)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-119">119/167</div>|:exclamation:MinorFail|`module-src-features-ontology`|[profile-compatibility](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#profile-compatibility)|OWL EL Profile incompatible|[Jump](#minorfail-outcome-number-119)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-120">120/167</div>|:exclamation:MinorFail|`module-src-devices-ontology`|[profile-compatibility](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#profile-compatibility)|OWL RL Profile incompatible|[Jump](#minorfail-outcome-number-120)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-121">121/167</div>|:exclamation:MinorFail|`module-src-devices-ontology`|[profile-compatibility](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#profile-compatibility)|OWL RL Profile incompatible|[Jump](#minorfail-outcome-number-121)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-122">122/167</div>|:exclamation:MinorFail|`module-src-devices-ontology`|[profile-compatibility](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#profile-compatibility)|OWL RL Profile incompatible|[Jump](#minorfail-outcome-number-122)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-123">123/167</div>|:exclamation:MinorFail|`module-src-devices-ontology`|[profile-compatibility](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#profile-compatibility)|OWL RL Profile incompatible|[Jump](#minorfail-outcome-number-123)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-124">124/167</div>|:exclamation:MinorFail|`module-src-devices-ontology`|[profile-compatibility](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#profile-compatibility)|OWL QL Profile incompatible|[Jump](#minorfail-outcome-number-124)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-125">125/167</div>|:exclamation:MinorFail|`module-src-devices-ontology`|[profile-compatibility](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#profile-compatibility)|OWL QL Profile incompatible|[Jump](#minorfail-outcome-number-125)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-126">126/167</div>|:exclamation:MinorFail|`module-src-devices-ontology`|[profile-compatibility](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#profile-compatibility)|OWL QL Profile incompatible|[Jump](#minorfail-outcome-number-126)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-127">127/167</div>|:exclamation:MinorFail|`module-src-devices-ontology`|[profile-compatibility](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#profile-compatibility)|OWL QL Profile incompatible|[Jump](#minorfail-outcome-number-127)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-128">128/167</div>|:exclamation:MinorFail|`module-src-devices-ontology`|[profile-compatibility](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#profile-compatibility)|OWL EL Profile incompatible|[Jump](#minorfail-outcome-number-128)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-129">129/167</div>|:exclamation:MinorFail|`module-src-devices-ontology`|[profile-compatibility](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#profile-compatibility)|OWL EL Profile incompatible|[Jump](#minorfail-outcome-number-129)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-130">130/167</div>|:exclamation:MinorFail|`module-src-devices-ontology`|[profile-compatibility](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#profile-compatibility)|OWL EL Profile incompatible|[Jump](#minorfail-outcome-number-130)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-131">131/167</div>|:exclamation:MinorFail|`module-src-devices-ontology`|[profile-compatibility](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#profile-compatibility)|OWL EL Profile incompatible|[Jump](#minorfail-outcome-number-131)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-132">132/167</div>|:exclamation:MinorFail|`module-src-coswot-sosa`|[term-referencing](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#term-referencing)|Term not referenced to a module|[Jump](#minorfail-outcome-number-132)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-133">133/167</div>|:exclamation:MinorFail|`module-src-communications-ontology`|[profile-compatibility](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#profile-compatibility)|OWL RL Profile incompatible|[Jump](#minorfail-outcome-number-133)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-134">134/167</div>|:exclamation:MinorFail|`module-src-communications-ontology`|[profile-compatibility](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#profile-compatibility)|OWL RL Profile incompatible|[Jump](#minorfail-outcome-number-134)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-135">135/167</div>|:exclamation:MinorFail|`module-src-communications-ontology`|[profile-compatibility](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#profile-compatibility)|OWL QL Profile incompatible|[Jump](#minorfail-outcome-number-135)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-136">136/167</div>|:exclamation:MinorFail|`module-src-communications-ontology`|[profile-compatibility](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#profile-compatibility)|OWL QL Profile incompatible|[Jump](#minorfail-outcome-number-136)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-137">137/167</div>|:exclamation:MinorFail|`module-src-communications-ontology`|[profile-compatibility](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#profile-compatibility)|OWL EL Profile incompatible|[Jump](#minorfail-outcome-number-137)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-138">138/167</div>|:exclamation:MinorFail|`module-src-communications-ontology`|[profile-compatibility](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#profile-compatibility)|OWL EL Profile incompatible|[Jump](#minorfail-outcome-number-138)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-139">139/167</div>|:exclamation:MinorFail|`module-src-aggregations-ontology`|[domain-and-range-referencing](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#domain-and-range-referencing)|Range out of vocabulary|[Jump](#minorfail-outcome-number-139)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-140">140/167</div>|:exclamation:MinorFail|`module-src-aggregations-ontology`|[profile-compatibility](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#profile-compatibility)|OWL RL Profile incompatible|[Jump](#minorfail-outcome-number-140)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-141">141/167</div>|:exclamation:MinorFail|`module-src-aggregations-ontology`|[profile-compatibility](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#profile-compatibility)|OWL RL Profile incompatible|[Jump](#minorfail-outcome-number-141)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-142">142/167</div>|:exclamation:MinorFail|`module-src-aggregations-ontology`|[profile-compatibility](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#profile-compatibility)|OWL RL Profile incompatible|[Jump](#minorfail-outcome-number-142)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-143">143/167</div>|:exclamation:MinorFail|`module-src-aggregations-ontology`|[profile-compatibility](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#profile-compatibility)|OWL QL Profile incompatible|[Jump](#minorfail-outcome-number-143)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-144">144/167</div>|:exclamation:MinorFail|`module-src-aggregations-ontology`|[profile-compatibility](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#profile-compatibility)|OWL QL Profile incompatible|[Jump](#minorfail-outcome-number-144)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-145">145/167</div>|:exclamation:MinorFail|`module-src-aggregations-ontology`|[profile-compatibility](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#profile-compatibility)|OWL QL Profile incompatible|[Jump](#minorfail-outcome-number-145)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-146">146/167</div>|:exclamation:MinorFail|`module-src-aggregations-ontology`|[profile-compatibility](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#profile-compatibility)|OWL EL Profile incompatible|[Jump](#minorfail-outcome-number-146)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-147">147/167</div>|:exclamation:MinorFail|`module-src-aggregations-ontology`|[profile-compatibility](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#profile-compatibility)|OWL EL Profile incompatible|[Jump](#minorfail-outcome-number-147)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-148">148/167</div>|:exclamation:MinorFail|`module-src-actuations-ontology`|[profile-compatibility](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#profile-compatibility)|OWL RL Profile incompatible|[Jump](#minorfail-outcome-number-148)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-149">149/167</div>|:exclamation:MinorFail|`module-src-actuations-ontology`|[profile-compatibility](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#profile-compatibility)|OWL RL Profile incompatible|[Jump](#minorfail-outcome-number-149)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-150">150/167</div>|:exclamation:MinorFail|`module-src-actuations-ontology`|[profile-compatibility](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#profile-compatibility)|OWL RL Profile incompatible|[Jump](#minorfail-outcome-number-150)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-151">151/167</div>|:exclamation:MinorFail|`module-src-actuations-ontology`|[profile-compatibility](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#profile-compatibility)|OWL RL Profile incompatible|[Jump](#minorfail-outcome-number-151)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-152">152/167</div>|:exclamation:MinorFail|`module-src-actuations-ontology`|[profile-compatibility](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#profile-compatibility)|OWL QL Profile incompatible|[Jump](#minorfail-outcome-number-152)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-153">153/167</div>|:exclamation:MinorFail|`module-src-actuations-ontology`|[profile-compatibility](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#profile-compatibility)|OWL QL Profile incompatible|[Jump](#minorfail-outcome-number-153)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-154">154/167</div>|:exclamation:MinorFail|`module-src-actuations-ontology`|[profile-compatibility](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#profile-compatibility)|OWL QL Profile incompatible|[Jump](#minorfail-outcome-number-154)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-155">155/167</div>|:exclamation:MinorFail|`module-src-actuations-ontology`|[profile-compatibility](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#profile-compatibility)|OWL QL Profile incompatible|[Jump](#minorfail-outcome-number-155)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-156">156/167</div>|:exclamation:MinorFail|`module-src-actuations-ontology`|[profile-compatibility](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#profile-compatibility)|OWL EL Profile incompatible|[Jump](#minorfail-outcome-number-156)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-157">157/167</div>|:exclamation:MinorFail|`module-src-actuations-ontology`|[profile-compatibility](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#profile-compatibility)|OWL EL Profile incompatible|[Jump](#minorfail-outcome-number-157)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-158">158/167</div>|:exclamation:MinorFail|`module-src-actuations-ontology`|[profile-compatibility](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#profile-compatibility)|OWL EL Profile incompatible|[Jump](#minorfail-outcome-number-158)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-159">159/167</div>|:exclamation:MinorFail|`module-src-actuations-ontology`|[profile-compatibility](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#profile-compatibility)|OWL EL Profile incompatible|[Jump](#minorfail-outcome-number-159)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-160">160/167</div>|:exclamation:MinorFail|`module-src-actuations-ontology`|[terms-differenciation](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#terms-differenciation)|Too close terms|[Jump](#minorfail-outcome-number-160)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-161">161/167</div>|:exclamation:MinorFail|`modelet-building-automation-samples`|[profile-compatibility](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#profile-compatibility)|OWL QL Profile incompatible|[Jump](#minorfail-outcome-number-161)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-162">162/167</div>|:exclamation:MinorFail|`modelet-building-automation-samples`|[profile-compatibility](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#profile-compatibility)|OWL EL Profile incompatible|[Jump](#minorfail-outcome-number-162)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-163">163/167</div>|:exclamation:MinorFail|`modelet-building-automation-features`|[domain-and-range-referencing](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#domain-and-range-referencing)|Domain out of vocabulary|[Jump](#minorfail-outcome-number-163)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-164">164/167</div>|:exclamation:MinorFail|`modelet-building-automation-features`|[domain-and-range-referencing](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#domain-and-range-referencing)|Range out of vocabulary|[Jump](#minorfail-outcome-number-164)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-165">165/167</div>|:exclamation:MinorFail|`modelet-building-automation-features`|[profile-compatibility](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#profile-compatibility)|OWL QL Profile incompatible|[Jump](#minorfail-outcome-number-165)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-166">166/167</div>|:exclamation:MinorFail|`modelet-building-automation-features`|[profile-compatibility](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#profile-compatibility)|OWL EL Profile incompatible|[Jump](#minorfail-outcome-number-166)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-167">167/167</div>|:exclamation:MinorFail|`modelet-building-automation-features`|[terms-differenciation](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#terms-differenciation)|Too close terms|[Jump](#minorfail-outcome-number-167)|

***

## MinorFail Outcomes Details

This subchapter gives more details to the :exclamation:MinorFail outcomes

### MinorFail Outcome number 1

[Jump to summary definition](#summary-MinorFail-1)	|	Previous MinorFail outcome	|	[Next MinorFail outcome](#minorfail-outcome-number-2)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-src-systems-ontology|
|----|----|
|Title|Standalone module src/systems/ontology.ttl from branch main|
|Composition|- [Module systems/ontology](https://gitlab.com/coswot/coswot-acimov/blob/main/src/systems/ontology.ttl)|

#### Criterion detail
|Identifier|[profile-compatibility](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#profile-compatibility)|
|----|----|
|Title|Profile compatibility test|
|Description|A test meant to check whether the test subject is compatible with a profile or not, and if it is not, why.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-1)|Identifier|`owl-rl-profile-error`|
|[Section top](#minorfail-outcome-number-1)|Title|OWL RL Profile incompatible|
|[Section top](#minorfail-outcome-number-1)|Description|Class Expression not supported with rdfs:subClassOf|
|[Section top](#minorfail-outcome-number-1)|Pointer|<pre lang="Turtle"><code>coswot:Connection a owl:Class ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;Connection&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:comment &#34;The class of connections between systems. This class qualifi...&#34; ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy &#60;https://w3id.org/coswot/core/systems> ;  &#10;&#32;&#32;&#32;&#32;rdfs:subClassOf &#91; owl:onProperty coswot:connectsSystem ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:someValuesFrom coswot:System ],  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;coswot:Feature ;  &#10;&#32;&#32;&#32;&#32;owl:disjointWith coswot:System .</code></pre>|

***
### MinorFail Outcome number 2

[Jump to summary definition](#summary-MinorFail-2)	|	[Previous MinorFail outcome](#minorfail-outcome-number-1)	|	[Next MinorFail outcome](#minorfail-outcome-number-3)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-src-systems-ontology|
|----|----|
|Title|Standalone module src/systems/ontology.ttl from branch main|
|Composition|- [Module systems/ontology](https://gitlab.com/coswot/coswot-acimov/blob/main/src/systems/ontology.ttl)|

#### Criterion detail
|Identifier|[profile-compatibility](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#profile-compatibility)|
|----|----|
|Title|Profile compatibility test|
|Description|A test meant to check whether the test subject is compatible with a profile or not, and if it is not, why.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-2)|Identifier|`owl-rl-profile-error`|
|[Section top](#minorfail-outcome-number-2)|Title|OWL RL Profile incompatible|
|[Section top](#minorfail-outcome-number-2)|Description|Statement not supported in a Super Class Expression|
|[Section top](#minorfail-outcome-number-2)|Pointer|<pre lang="Turtle"><code>&#91;] owl:onProperty coswot:connectsSystem ;  &#10;&#32;&#32;&#32;&#32;owl:someValuesFrom coswot:System .</code></pre>|

***
### MinorFail Outcome number 3

[Jump to summary definition](#summary-MinorFail-3)	|	[Previous MinorFail outcome](#minorfail-outcome-number-2)	|	[Next MinorFail outcome](#minorfail-outcome-number-4)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-src-systems-ontology|
|----|----|
|Title|Standalone module src/systems/ontology.ttl from branch main|
|Composition|- [Module systems/ontology](https://gitlab.com/coswot/coswot-acimov/blob/main/src/systems/ontology.ttl)|

#### Criterion detail
|Identifier|[profile-compatibility](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#profile-compatibility)|
|----|----|
|Title|Profile compatibility test|
|Description|A test meant to check whether the test subject is compatible with a profile or not, and if it is not, why.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-3)|Identifier|`owl-ql-profile-error`|
|[Section top](#minorfail-outcome-number-3)|Title|OWL QL Profile incompatible|
|[Section top](#minorfail-outcome-number-3)|Description|Statement not supported|
|[Section top](#minorfail-outcome-number-3)|Pointer|<pre lang="Turtle"><code>coswot:subSystemOf a owl:ObjectProperty,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:TransitiveProperty ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;sub system of&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:comment &#34;Links a system to its super system. Properties of subsystems...&#34; ;  &#10;&#32;&#32;&#32;&#32;rdfs:domain coswot:System ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy &#60;https://w3id.org/coswot/core/systems> ;  &#10;&#32;&#32;&#32;&#32;rdfs:range coswot:System ;  &#10;&#32;&#32;&#32;&#32;owl:inverseOf coswot:hasSubSystem .</code></pre>|

***
### MinorFail Outcome number 4

[Jump to summary definition](#summary-MinorFail-4)	|	[Previous MinorFail outcome](#minorfail-outcome-number-3)	|	[Next MinorFail outcome](#minorfail-outcome-number-5)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-src-systems-ontology|
|----|----|
|Title|Standalone module src/systems/ontology.ttl from branch main|
|Composition|- [Module systems/ontology](https://gitlab.com/coswot/coswot-acimov/blob/main/src/systems/ontology.ttl)|

#### Criterion detail
|Identifier|[profile-compatibility](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#profile-compatibility)|
|----|----|
|Title|Profile compatibility test|
|Description|A test meant to check whether the test subject is compatible with a profile or not, and if it is not, why.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-4)|Identifier|`owl-el-profile-error`|
|[Section top](#minorfail-outcome-number-4)|Title|OWL EL Profile incompatible|
|[Section top](#minorfail-outcome-number-4)|Description|Statement not supported|
|[Section top](#minorfail-outcome-number-4)|Pointer|<pre lang="Turtle"><code>coswot:connectedTo a owl:ObjectProperty,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:SymmetricProperty ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;connected to&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:comment &#34;Links a system to a system it is connected to. Connected sys...&#34; ;  &#10;&#32;&#32;&#32;&#32;rdfs:domain coswot:System ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy &#60;https://w3id.org/coswot/core/systems> ;  &#10;&#32;&#32;&#32;&#32;rdfs:range coswot:System .</code></pre>|

***
### MinorFail Outcome number 5

[Jump to summary definition](#summary-MinorFail-5)	|	[Previous MinorFail outcome](#minorfail-outcome-number-4)	|	[Next MinorFail outcome](#minorfail-outcome-number-6)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-src-states-ontology-catalog|
|----|----|
|Title|Standalone module src/states/ontology.catalog.ttl from branch main|
|Composition|- [Module states/ontology.catalog](https://gitlab.com/coswot/coswot-acimov/blob/main/src/states/ontology.catalog.ttl)|

#### Criterion detail
|Identifier|[domain-and-range-referencing](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#domain-and-range-referencing)|
|----|----|
|Title|Domain and range referencing test|
|Description|A test case from the Best Practices tests checking if all the ranges and domains from the test subject point to terms that are defined in the vocabulary.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-5)|Identifier|`domain-out-of-vocabulary`|
|[Section top](#minorfail-outcome-number-5)|Title|Domain out of vocabulary|
|[Section top](#minorfail-outcome-number-5)|Description|Some properties have a domain out of the ontology|
|[Section top](#minorfail-outcome-number-5)|Pointer|<pre lang="Turtle"><code>:isStateOf a owl:ObjectProperty ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;is state of&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:comment &#34;Links a state to the feature kind or feature of interest it ...&#34; ;  &#10;&#32;&#32;&#32;&#32;rdfs:domain &#91; a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:allValuesFrom :StateKind ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:onProperty skos:broader ],  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#91; a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:allValuesFrom :StateKind ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:onProperty skos:narrower ],  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:Thing,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;skos:Concept,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;:StateKind ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy &#60;https://w3id.org/coswot/core/states> ;  &#10;&#32;&#32;&#32;&#32;rdfs:subPropertyOf :isStateOf ;  &#10;&#32;&#32;&#32;&#32;owl:equivalentProperty :isStateOf ;  &#10;&#32;&#32;&#32;&#32;owl:inverseOf :hasState .</code></pre>|
|[Section top](#minorfail-outcome-number-5)|Pointer|http://www.w3.org/2004/02/skos/core#Concept|

***
### MinorFail Outcome number 6

[Jump to summary definition](#summary-MinorFail-6)	|	[Previous MinorFail outcome](#minorfail-outcome-number-5)	|	[Next MinorFail outcome](#minorfail-outcome-number-7)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-src-states-ontology-catalog|
|----|----|
|Title|Standalone module src/states/ontology.catalog.ttl from branch main|
|Composition|- [Module states/ontology.catalog](https://gitlab.com/coswot/coswot-acimov/blob/main/src/states/ontology.catalog.ttl)|

#### Criterion detail
|Identifier|[domain-and-range-referencing](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#domain-and-range-referencing)|
|----|----|
|Title|Domain and range referencing test|
|Description|A test case from the Best Practices tests checking if all the ranges and domains from the test subject point to terms that are defined in the vocabulary.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-6)|Identifier|`range-out-of-vocabulary`|
|[Section top](#minorfail-outcome-number-6)|Title|Range out of vocabulary|
|[Section top](#minorfail-outcome-number-6)|Description|Some properties have a range out of the ontology|
|[Section top](#minorfail-outcome-number-6)|Pointer|<pre lang="Turtle"><code>:hasState a owl:ObjectProperty ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;has state&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:comment &#34;Links a feature kind or a feature of interest to one of its ...&#34; ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy &#60;https://w3id.org/coswot/core/states> ;  &#10;&#32;&#32;&#32;&#32;rdfs:range &#91; a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:allValuesFrom :StateKind ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:onProperty skos:broader ],  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#91; a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:allValuesFrom :StateKind ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:onProperty skos:narrower ],  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:Thing,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;skos:Concept,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;:StateKind ;  &#10;&#32;&#32;&#32;&#32;rdfs:subPropertyOf :hasState ;  &#10;&#32;&#32;&#32;&#32;owl:equivalentProperty :hasState ;  &#10;&#32;&#32;&#32;&#32;owl:inverseOf :isStateOf ;  &#10;&#32;&#32;&#32;&#32;owl:propertyChainAxiom ( skos:broader :hasState ) .</code></pre>|
|[Section top](#minorfail-outcome-number-6)|Pointer|http://www.w3.org/2004/02/skos/core#Concept|

***
### MinorFail Outcome number 7

[Jump to summary definition](#summary-MinorFail-7)	|	[Previous MinorFail outcome](#minorfail-outcome-number-6)	|	[Next MinorFail outcome](#minorfail-outcome-number-8)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-src-states-ontology-catalog|
|----|----|
|Title|Standalone module src/states/ontology.catalog.ttl from branch main|
|Composition|- [Module states/ontology.catalog](https://gitlab.com/coswot/coswot-acimov/blob/main/src/states/ontology.catalog.ttl)|

#### Criterion detail
|Identifier|[profile-compatibility](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#profile-compatibility)|
|----|----|
|Title|Profile compatibility test|
|Description|A test meant to check whether the test subject is compatible with a profile or not, and if it is not, why.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-7)|Identifier|`owl-ql-profile-error`|
|[Section top](#minorfail-outcome-number-7)|Title|OWL QL Profile incompatible|
|[Section top](#minorfail-outcome-number-7)|Description|Class Expression not supported with rdfs:subClassOf|
|[Section top](#minorfail-outcome-number-7)|Pointer|<pre lang="Turtle"><code>coswot:StateKind a owl:Class ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;State Kind&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:comment &#34;Identifiable conditions that features are or may be in, and ...&#34; ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy &#60;https://w3id.org/coswot/core/states> ;  &#10;&#32;&#32;&#32;&#32;rdfs:subClassOf &#91; a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:allValuesFrom coswot:StateKind ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:onProperty skos:broader ],  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#91; a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:allValuesFrom coswot:StateKind ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:onProperty skos:narrower ],  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;skos:Concept ;  &#10;&#32;&#32;&#32;&#32;skos:note &#34;Concepts from existing code lists, vocabularies, and taxonom...&#34; .</code></pre>|

***
### MinorFail Outcome number 8

[Jump to summary definition](#summary-MinorFail-8)	|	[Previous MinorFail outcome](#minorfail-outcome-number-7)	|	[Next MinorFail outcome](#minorfail-outcome-number-9)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-src-states-ontology-catalog|
|----|----|
|Title|Standalone module src/states/ontology.catalog.ttl from branch main|
|Composition|- [Module states/ontology.catalog](https://gitlab.com/coswot/coswot-acimov/blob/main/src/states/ontology.catalog.ttl)|

#### Criterion detail
|Identifier|[profile-compatibility](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#profile-compatibility)|
|----|----|
|Title|Profile compatibility test|
|Description|A test meant to check whether the test subject is compatible with a profile or not, and if it is not, why.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-8)|Identifier|`owl-ql-profile-error`|
|[Section top](#minorfail-outcome-number-8)|Title|OWL QL Profile incompatible|
|[Section top](#minorfail-outcome-number-8)|Description|Statement not supported in a Super Class Expression|
|[Section top](#minorfail-outcome-number-8)|Pointer|<pre lang="Turtle"><code>&#91;] a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;owl:allValuesFrom coswot:StateKind ;  &#10;&#32;&#32;&#32;&#32;owl:onProperty skos:broader .</code></pre>|
|[Section top](#minorfail-outcome-number-8)|Pointer|<pre lang="Turtle"><code>&#91;] a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;owl:allValuesFrom coswot:StateKind ;  &#10;&#32;&#32;&#32;&#32;owl:onProperty skos:narrower .</code></pre>|

***
### MinorFail Outcome number 9

[Jump to summary definition](#summary-MinorFail-9)	|	[Previous MinorFail outcome](#minorfail-outcome-number-8)	|	[Next MinorFail outcome](#minorfail-outcome-number-10)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-src-states-ontology-catalog|
|----|----|
|Title|Standalone module src/states/ontology.catalog.ttl from branch main|
|Composition|- [Module states/ontology.catalog](https://gitlab.com/coswot/coswot-acimov/blob/main/src/states/ontology.catalog.ttl)|

#### Criterion detail
|Identifier|[profile-compatibility](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#profile-compatibility)|
|----|----|
|Title|Profile compatibility test|
|Description|A test meant to check whether the test subject is compatible with a profile or not, and if it is not, why.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-9)|Identifier|`owl-ql-profile-error`|
|[Section top](#minorfail-outcome-number-9)|Title|OWL QL Profile incompatible|
|[Section top](#minorfail-outcome-number-9)|Description|Property inclusions involving property chains not supported|
|[Section top](#minorfail-outcome-number-9)|Pointer|<pre lang="Turtle"><code>coswot:hasState a owl:ObjectProperty ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;has state&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:comment &#34;Links a feature kind or a feature of interest to one of its ...&#34; ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy &#60;https://w3id.org/coswot/core/states> ;  &#10;&#32;&#32;&#32;&#32;rdfs:range coswot:StateKind ;  &#10;&#32;&#32;&#32;&#32;owl:inverseOf coswot:isStateOf ;  &#10;&#32;&#32;&#32;&#32;owl:propertyChainAxiom ( skos:broader coswot:hasState ) .</code></pre>|

***
### MinorFail Outcome number 10

[Jump to summary definition](#summary-MinorFail-10)	|	[Previous MinorFail outcome](#minorfail-outcome-number-9)	|	[Next MinorFail outcome](#minorfail-outcome-number-11)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-src-states-ontology-catalog|
|----|----|
|Title|Standalone module src/states/ontology.catalog.ttl from branch main|
|Composition|- [Module states/ontology.catalog](https://gitlab.com/coswot/coswot-acimov/blob/main/src/states/ontology.catalog.ttl)|

#### Criterion detail
|Identifier|[profile-compatibility](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#profile-compatibility)|
|----|----|
|Title|Profile compatibility test|
|Description|A test meant to check whether the test subject is compatible with a profile or not, and if it is not, why.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-10)|Identifier|`owl-el-profile-error`|
|[Section top](#minorfail-outcome-number-10)|Title|OWL EL Profile incompatible|
|[Section top](#minorfail-outcome-number-10)|Description|Statement not supported in a Class Expression|
|[Section top](#minorfail-outcome-number-10)|Pointer|<pre lang="Turtle"><code>&#91;] a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;owl:allValuesFrom coswot:StateKind ;  &#10;&#32;&#32;&#32;&#32;owl:onProperty skos:broader .</code></pre>|
|[Section top](#minorfail-outcome-number-10)|Pointer|<pre lang="Turtle"><code>&#91;] a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;owl:allValuesFrom coswot:StateKind ;  &#10;&#32;&#32;&#32;&#32;owl:onProperty skos:narrower .</code></pre>|

***
### MinorFail Outcome number 11

[Jump to summary definition](#summary-MinorFail-11)	|	[Previous MinorFail outcome](#minorfail-outcome-number-10)	|	[Next MinorFail outcome](#minorfail-outcome-number-12)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-src-states-ontology-catalog|
|----|----|
|Title|Standalone module src/states/ontology.catalog.ttl from branch main|
|Composition|- [Module states/ontology.catalog](https://gitlab.com/coswot/coswot-acimov/blob/main/src/states/ontology.catalog.ttl)|

#### Criterion detail
|Identifier|[profile-compatibility](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#profile-compatibility)|
|----|----|
|Title|Profile compatibility test|
|Description|A test meant to check whether the test subject is compatible with a profile or not, and if it is not, why.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-11)|Identifier|`owl-el-profile-error`|
|[Section top](#minorfail-outcome-number-11)|Title|OWL EL Profile incompatible|
|[Section top](#minorfail-outcome-number-11)|Description|Class Expression not supported with rdfs:subClassOf|
|[Section top](#minorfail-outcome-number-11)|Pointer|<pre lang="Turtle"><code>coswot:StateKind a owl:Class ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;State Kind&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:comment &#34;Identifiable conditions that features are or may be in, and ...&#34; ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy &#60;https://w3id.org/coswot/core/states> ;  &#10;&#32;&#32;&#32;&#32;rdfs:subClassOf &#91; a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:allValuesFrom coswot:StateKind ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:onProperty skos:broader ],  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#91; a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:allValuesFrom coswot:StateKind ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:onProperty skos:narrower ],  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;skos:Concept ;  &#10;&#32;&#32;&#32;&#32;skos:note &#34;Concepts from existing code lists, vocabularies, and taxonom...&#34; .</code></pre>|

***
### MinorFail Outcome number 12

[Jump to summary definition](#summary-MinorFail-12)	|	[Previous MinorFail outcome](#minorfail-outcome-number-11)	|	[Next MinorFail outcome](#minorfail-outcome-number-13)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-src-states-ontology|
|----|----|
|Title|Standalone module src/states/ontology.ttl from branch main|
|Composition|- [Module states/ontology](https://gitlab.com/coswot/coswot-acimov/blob/main/src/states/ontology.ttl)|

#### Criterion detail
|Identifier|[domain-and-range-referencing](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#domain-and-range-referencing)|
|----|----|
|Title|Domain and range referencing test|
|Description|A test case from the Best Practices tests checking if all the ranges and domains from the test subject point to terms that are defined in the vocabulary.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-12)|Identifier|`domain-out-of-vocabulary`|
|[Section top](#minorfail-outcome-number-12)|Title|Domain out of vocabulary|
|[Section top](#minorfail-outcome-number-12)|Description|Some properties have a domain out of the ontology|
|[Section top](#minorfail-outcome-number-12)|Pointer|<pre lang="Turtle"><code>:isStateOf a owl:ObjectProperty ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;is state of&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:comment &#34;Links a state to the feature kind or feature of interest it ...&#34; ;  &#10;&#32;&#32;&#32;&#32;rdfs:domain &#91; a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:allValuesFrom :StateKind ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:onProperty skos:broader ],  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#91; a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:allValuesFrom :StateKind ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:onProperty skos:narrower ],  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#91; a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;rdfs:subClassOf &lowbar;:n3ed13fbcf32645cc9e3a9615455662dcb4 ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:allValuesFrom owl:Nothing ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:onProperty :hasKind ],  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&lowbar;:n3ed13fbcf32645cc9e3a9615455662dcb4,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:Thing,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;skos:Concept,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;:State,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;:StateKind ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy &#60;https://w3id.org/coswot/core/states> ;  &#10;&#32;&#32;&#32;&#32;rdfs:range &lowbar;:n3ed13fbcf32645cc9e3a9615455662dcb5,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:Thing ;  &#10;&#32;&#32;&#32;&#32;rdfs:subPropertyOf :isStateOf ;  &#10;&#32;&#32;&#32;&#32;owl:equivalentProperty :isStateOf ;  &#10;&#32;&#32;&#32;&#32;owl:inverseOf :hasState .  &#10;&lowbar;:n3ed13fbcf32645cc9e3a9615455662dcb6 rdf:first :StateOfInterest ;  &#10;&#32;&#32;&#32;&#32;rdf:rest () .  &#10;&lowbar;:n3ed13fbcf32645cc9e3a9615455662dcb7 rdf:first :Feature ;  &#10;&#32;&#32;&#32;&#32;rdf:rest &lowbar;:n3ed13fbcf32645cc9e3a9615455662dcb6 .  &#10;&lowbar;:n3ed13fbcf32645cc9e3a9615455662dcb4 a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;owl:allValuesFrom :StateKind ;  &#10;&#32;&#32;&#32;&#32;owl:onProperty :hasKind .  &#10;&lowbar;:n3ed13fbcf32645cc9e3a9615455662dcb5 a owl:Class ;  &#10;&#32;&#32;&#32;&#32;rdfs:subClassOf &lowbar;:n3ed13fbcf32645cc9e3a9615455662dcb5,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:Thing ;  &#10;&#32;&#32;&#32;&#32;owl:equivalentClass &lowbar;:n3ed13fbcf32645cc9e3a9615455662dcb5 ;  &#10;&#32;&#32;&#32;&#32;owl:unionOf &lowbar;:n3ed13fbcf32645cc9e3a9615455662dcb7 .</code></pre>|
|[Section top](#minorfail-outcome-number-12)|Pointer|http://www.w3.org/2004/02/skos/core#Concept|

***
### MinorFail Outcome number 13

[Jump to summary definition](#summary-MinorFail-13)	|	[Previous MinorFail outcome](#minorfail-outcome-number-12)	|	[Next MinorFail outcome](#minorfail-outcome-number-14)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-src-states-ontology|
|----|----|
|Title|Standalone module src/states/ontology.ttl from branch main|
|Composition|- [Module states/ontology](https://gitlab.com/coswot/coswot-acimov/blob/main/src/states/ontology.ttl)|

#### Criterion detail
|Identifier|[domain-and-range-referencing](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#domain-and-range-referencing)|
|----|----|
|Title|Domain and range referencing test|
|Description|A test case from the Best Practices tests checking if all the ranges and domains from the test subject point to terms that are defined in the vocabulary.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-13)|Identifier|`range-out-of-vocabulary`|
|[Section top](#minorfail-outcome-number-13)|Title|Range out of vocabulary|
|[Section top](#minorfail-outcome-number-13)|Description|Some properties have a range out of the ontology|
|[Section top](#minorfail-outcome-number-13)|Pointer|<pre lang="Turtle"><code>:hasKind a owl:ObjectProperty ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;has state kind&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:comment &#34;links a state of interest to its kind, a state kind&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:domain &lowbar;:nc741b307f2c14b4c911639abb5d59542b1,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#91; a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:onProperty :hasKind ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:someValuesFrom :StateKind ],  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&lowbar;:nc741b307f2c14b4c911639abb5d59542b3,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#91; a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:onProperty :isStateOfInterestOf ],  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:Thing,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;:State,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;:StateOfInterest ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy &#60;https://w3id.org/coswot/core/states> ;  &#10;&#32;&#32;&#32;&#32;rdfs:range &lowbar;:nc741b307f2c14b4c911639abb5d59542b1,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#91; a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:allValuesFrom :StateKind ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:onProperty skos:broader ],  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#91; a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:allValuesFrom :StateKind ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:onProperty skos:narrower ],  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#91; a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;rdfs:subClassOf &lowbar;:nc741b307f2c14b4c911639abb5d59542b1 ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:allValuesFrom owl:Nothing ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:onProperty :hasKind ],  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:Thing,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;skos:Concept,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;:State,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;:StateKind ;  &#10;&#32;&#32;&#32;&#32;rdfs:subPropertyOf :hasKind ;  &#10;&#32;&#32;&#32;&#32;owl:equivalentProperty :hasKind ;  &#10;&#32;&#32;&#32;&#32;owl:propertyChainAxiom ( :hasKind skos:broader ) .  &#10;&lowbar;:nc741b307f2c14b4c911639abb5d59542b10 rdf:first :StateOfInterest ;  &#10;&#32;&#32;&#32;&#32;rdf:rest () .  &#10;&lowbar;:nc741b307f2c14b4c911639abb5d59542b11 rdf:first :Feature ;  &#10;&#32;&#32;&#32;&#32;rdf:rest &lowbar;:nc741b307f2c14b4c911639abb5d59542b10 .  &#10;&lowbar;:nc741b307f2c14b4c911639abb5d59542b1 a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;owl:allValuesFrom :StateKind ;  &#10;&#32;&#32;&#32;&#32;owl:onProperty :hasKind .  &#10;&lowbar;:nc741b307f2c14b4c911639abb5d59542b3 a owl:Class ;  &#10;&#32;&#32;&#32;&#32;rdfs:subClassOf &lowbar;:nc741b307f2c14b4c911639abb5d59542b3,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:Thing ;  &#10;&#32;&#32;&#32;&#32;owl:equivalentClass &lowbar;:nc741b307f2c14b4c911639abb5d59542b3 ;  &#10;&#32;&#32;&#32;&#32;owl:unionOf &lowbar;:nc741b307f2c14b4c911639abb5d59542b11 .</code></pre>|
|[Section top](#minorfail-outcome-number-13)|Pointer|<pre lang="Turtle"><code>:hasState a owl:ObjectProperty ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;has state&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:comment &#34;Links a feature kind or a feature of interest to one of its ...&#34; ;  &#10;&#32;&#32;&#32;&#32;rdfs:domain &lowbar;:n39291f9a67a947479f57119059074373b1,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:Thing ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy &#60;https://w3id.org/coswot/core/states> ;  &#10;&#32;&#32;&#32;&#32;rdfs:range &#91; a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:allValuesFrom :StateKind ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:onProperty skos:broader ],  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#91; a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:allValuesFrom :StateKind ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:onProperty skos:narrower ],  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#91; a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;rdfs:subClassOf &lowbar;:n39291f9a67a947479f57119059074373b5 ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:allValuesFrom owl:Nothing ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:onProperty :hasKind ],  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&lowbar;:n39291f9a67a947479f57119059074373b5,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:Thing,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;skos:Concept,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;:State,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;:StateKind ;  &#10;&#32;&#32;&#32;&#32;rdfs:subPropertyOf :hasState ;  &#10;&#32;&#32;&#32;&#32;owl:equivalentProperty :hasState ;  &#10;&#32;&#32;&#32;&#32;owl:inverseOf :isStateOf ;  &#10;&#32;&#32;&#32;&#32;owl:propertyChainAxiom ( :hasStateOfInterest :hasKind ),  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;( skos:broader :hasState ),  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;( :hasKind :hasState ) .  &#10;&lowbar;:n39291f9a67a947479f57119059074373b12 rdf:first :StateOfInterest ;  &#10;&#32;&#32;&#32;&#32;rdf:rest () .  &#10;&lowbar;:n39291f9a67a947479f57119059074373b13 rdf:first :Feature ;  &#10;&#32;&#32;&#32;&#32;rdf:rest &lowbar;:n39291f9a67a947479f57119059074373b12 .  &#10;&lowbar;:n39291f9a67a947479f57119059074373b5 a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;owl:allValuesFrom :StateKind ;  &#10;&#32;&#32;&#32;&#32;owl:onProperty :hasKind .  &#10;&lowbar;:n39291f9a67a947479f57119059074373b1 a owl:Class ;  &#10;&#32;&#32;&#32;&#32;rdfs:subClassOf &lowbar;:n39291f9a67a947479f57119059074373b1,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:Thing ;  &#10;&#32;&#32;&#32;&#32;owl:equivalentClass &lowbar;:n39291f9a67a947479f57119059074373b1 ;  &#10;&#32;&#32;&#32;&#32;owl:unionOf &lowbar;:n39291f9a67a947479f57119059074373b13 .</code></pre>|
|[Section top](#minorfail-outcome-number-13)|Pointer|http://www.w3.org/2004/02/skos/core#Concept|

***
### MinorFail Outcome number 14

[Jump to summary definition](#summary-MinorFail-14)	|	[Previous MinorFail outcome](#minorfail-outcome-number-13)	|	[Next MinorFail outcome](#minorfail-outcome-number-15)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-src-states-ontology|
|----|----|
|Title|Standalone module src/states/ontology.ttl from branch main|
|Composition|- [Module states/ontology](https://gitlab.com/coswot/coswot-acimov/blob/main/src/states/ontology.ttl)|

#### Criterion detail
|Identifier|[profile-compatibility](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#profile-compatibility)|
|----|----|
|Title|Profile compatibility test|
|Description|A test meant to check whether the test subject is compatible with a profile or not, and if it is not, why.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-14)|Identifier|`owl-rl-profile-error`|
|[Section top](#minorfail-outcome-number-14)|Title|OWL RL Profile incompatible|
|[Section top](#minorfail-outcome-number-14)|Description|Class Expression not supported with rdfs:subClassOf|
|[Section top](#minorfail-outcome-number-14)|Pointer|<pre lang="Turtle"><code>coswot:StateOfInterest a owl:Class ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;State of Interest&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:comment &#34;Identifiable conditions that features of interest are or may...&#34; ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy &#60;https://w3id.org/coswot/core/states> ;  &#10;&#32;&#32;&#32;&#32;rdfs:subClassOf &#91; a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:allValuesFrom coswot:StateKind ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:onProperty coswot:hasKind ],  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#91; a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:onProperty coswot:hasKind ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:someValuesFrom coswot:StateKind ],  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#91; a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:onProperty coswot:isStateOfInterestOf ],  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;coswot:State ;  &#10;&#32;&#32;&#32;&#32;skos:note &#34;A state of interest is the state of (OP coswot:isStateOfInte...&#34;,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#34;Per convention, the IRI of states of interest should consist...&#34;,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#34;States of interest need not always be explicited. It depends...&#34; .</code></pre>|

***
### MinorFail Outcome number 15

[Jump to summary definition](#summary-MinorFail-15)	|	[Previous MinorFail outcome](#minorfail-outcome-number-14)	|	[Next MinorFail outcome](#minorfail-outcome-number-16)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-src-states-ontology|
|----|----|
|Title|Standalone module src/states/ontology.ttl from branch main|
|Composition|- [Module states/ontology](https://gitlab.com/coswot/coswot-acimov/blob/main/src/states/ontology.ttl)|

#### Criterion detail
|Identifier|[profile-compatibility](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#profile-compatibility)|
|----|----|
|Title|Profile compatibility test|
|Description|A test meant to check whether the test subject is compatible with a profile or not, and if it is not, why.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-15)|Identifier|`owl-rl-profile-error`|
|[Section top](#minorfail-outcome-number-15)|Title|OWL RL Profile incompatible|
|[Section top](#minorfail-outcome-number-15)|Description|Statement not supported|
|[Section top](#minorfail-outcome-number-15)|Pointer|<pre lang="Turtle"><code>coswot:State a owl:Class ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;State&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:comment &#34;Identifiable conditions that features are or may be in, and ...&#34; ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy &#60;https://w3id.org/coswot/core/states> ;  &#10;&#32;&#32;&#32;&#32;owl:disjointUnionOf ( coswot:StateOfInterest coswot:StateKind ) .</code></pre>|

***
### MinorFail Outcome number 16

[Jump to summary definition](#summary-MinorFail-16)	|	[Previous MinorFail outcome](#minorfail-outcome-number-15)	|	[Next MinorFail outcome](#minorfail-outcome-number-17)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-src-states-ontology|
|----|----|
|Title|Standalone module src/states/ontology.ttl from branch main|
|Composition|- [Module states/ontology](https://gitlab.com/coswot/coswot-acimov/blob/main/src/states/ontology.ttl)|

#### Criterion detail
|Identifier|[profile-compatibility](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#profile-compatibility)|
|----|----|
|Title|Profile compatibility test|
|Description|A test meant to check whether the test subject is compatible with a profile or not, and if it is not, why.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-16)|Identifier|`owl-rl-profile-error`|
|[Section top](#minorfail-outcome-number-16)|Title|OWL RL Profile incompatible|
|[Section top](#minorfail-outcome-number-16)|Description|Statement not supported in a Super Class Expression|
|[Section top](#minorfail-outcome-number-16)|Pointer|<pre lang="Turtle"><code>&#91;] a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;owl:onProperty coswot:hasKind ;  &#10;&#32;&#32;&#32;&#32;owl:someValuesFrom coswot:StateKind .</code></pre>|
|[Section top](#minorfail-outcome-number-16)|Pointer|<pre lang="Turtle"><code>&#91;] a owl:Class ;  &#10;&#32;&#32;&#32;&#32;owl:unionOf ( coswot:Feature coswot:StateOfInterest ) .</code></pre>|
|[Section top](#minorfail-outcome-number-16)|Pointer|<pre lang="Turtle"><code>&#91;] a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;owl:onProperty coswot:isStateOfInterestOf .</code></pre>|

***
### MinorFail Outcome number 17

[Jump to summary definition](#summary-MinorFail-17)	|	[Previous MinorFail outcome](#minorfail-outcome-number-16)	|	[Next MinorFail outcome](#minorfail-outcome-number-18)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-src-states-ontology|
|----|----|
|Title|Standalone module src/states/ontology.ttl from branch main|
|Composition|- [Module states/ontology](https://gitlab.com/coswot/coswot-acimov/blob/main/src/states/ontology.ttl)|

#### Criterion detail
|Identifier|[profile-compatibility](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#profile-compatibility)|
|----|----|
|Title|Profile compatibility test|
|Description|A test meant to check whether the test subject is compatible with a profile or not, and if it is not, why.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-17)|Identifier|`owl-rl-profile-error`|
|[Section top](#minorfail-outcome-number-17)|Title|OWL RL Profile incompatible|
|[Section top](#minorfail-outcome-number-17)|Description|Class Expression not supported as object of rdfs:domain or rdfs:range|
|[Section top](#minorfail-outcome-number-17)|Pointer|<pre lang="Turtle"><code>coswot:hasState a owl:ObjectProperty ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;has state&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:comment &#34;Links a feature kind or a feature of interest to one of its ...&#34; ;  &#10;&#32;&#32;&#32;&#32;rdfs:domain &#91; a owl:Class ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:unionOf ( coswot:Feature coswot:StateOfInterest ) ] ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy &#60;https://w3id.org/coswot/core/states> ;  &#10;&#32;&#32;&#32;&#32;rdfs:range coswot:StateKind ;  &#10;&#32;&#32;&#32;&#32;owl:inverseOf coswot:isStateOf ;  &#10;&#32;&#32;&#32;&#32;owl:propertyChainAxiom ( skos:broader coswot:hasState ),  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;( coswot:hasKind coswot:hasState ),  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;( coswot:hasStateOfInterest coswot:hasKind ) .</code></pre>|
|[Section top](#minorfail-outcome-number-17)|Pointer|<pre lang="Turtle"><code>coswot:isStateOf a owl:ObjectProperty ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;is state of&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:comment &#34;Links a state to the feature kind or feature of interest it ...&#34; ;  &#10;&#32;&#32;&#32;&#32;rdfs:domain coswot:StateKind ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy &#60;https://w3id.org/coswot/core/states> ;  &#10;&#32;&#32;&#32;&#32;rdfs:range &#91; a owl:Class ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:unionOf ( coswot:Feature coswot:StateOfInterest ) ] ;  &#10;&#32;&#32;&#32;&#32;owl:inverseOf coswot:hasState .</code></pre>|

***
### MinorFail Outcome number 18

[Jump to summary definition](#summary-MinorFail-18)	|	[Previous MinorFail outcome](#minorfail-outcome-number-17)	|	[Next MinorFail outcome](#minorfail-outcome-number-19)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-src-states-ontology|
|----|----|
|Title|Standalone module src/states/ontology.ttl from branch main|
|Composition|- [Module states/ontology](https://gitlab.com/coswot/coswot-acimov/blob/main/src/states/ontology.ttl)|

#### Criterion detail
|Identifier|[profile-compatibility](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#profile-compatibility)|
|----|----|
|Title|Profile compatibility test|
|Description|A test meant to check whether the test subject is compatible with a profile or not, and if it is not, why.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-18)|Identifier|`owl-ql-profile-error`|
|[Section top](#minorfail-outcome-number-18)|Title|OWL QL Profile incompatible|
|[Section top](#minorfail-outcome-number-18)|Description|Statement not supported in a Super Class Expression|
|[Section top](#minorfail-outcome-number-18)|Pointer|<pre lang="Turtle"><code>&#91;] a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;owl:allValuesFrom coswot:StateKind ;  &#10;&#32;&#32;&#32;&#32;owl:onProperty skos:broader .</code></pre>|
|[Section top](#minorfail-outcome-number-18)|Pointer|<pre lang="Turtle"><code>&#91;] a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;owl:allValuesFrom coswot:StateKind ;  &#10;&#32;&#32;&#32;&#32;owl:onProperty skos:narrower .</code></pre>|
|[Section top](#minorfail-outcome-number-18)|Pointer|<pre lang="Turtle"><code>&#91;] a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;owl:allValuesFrom owl:Nothing ;  &#10;&#32;&#32;&#32;&#32;owl:onProperty coswot:hasKind .</code></pre>|
|[Section top](#minorfail-outcome-number-18)|Pointer|<pre lang="Turtle"><code>&#91;] a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;owl:allValuesFrom coswot:StateKind ;  &#10;&#32;&#32;&#32;&#32;owl:onProperty coswot:hasKind .</code></pre>|
|[Section top](#minorfail-outcome-number-18)|Pointer|<pre lang="Turtle"><code>&#91;] a owl:Class ;  &#10;&#32;&#32;&#32;&#32;owl:unionOf ( coswot:Feature coswot:StateOfInterest ) .</code></pre>|
|[Section top](#minorfail-outcome-number-18)|Pointer|<pre lang="Turtle"><code>&#91;] a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;owl:onProperty coswot:isStateOfInterestOf .</code></pre>|

***
### MinorFail Outcome number 19

[Jump to summary definition](#summary-MinorFail-19)	|	[Previous MinorFail outcome](#minorfail-outcome-number-18)	|	[Next MinorFail outcome](#minorfail-outcome-number-20)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-src-states-ontology|
|----|----|
|Title|Standalone module src/states/ontology.ttl from branch main|
|Composition|- [Module states/ontology](https://gitlab.com/coswot/coswot-acimov/blob/main/src/states/ontology.ttl)|

#### Criterion detail
|Identifier|[profile-compatibility](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#profile-compatibility)|
|----|----|
|Title|Profile compatibility test|
|Description|A test meant to check whether the test subject is compatible with a profile or not, and if it is not, why.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-19)|Identifier|`owl-ql-profile-error`|
|[Section top](#minorfail-outcome-number-19)|Title|OWL QL Profile incompatible|
|[Section top](#minorfail-outcome-number-19)|Description|Class Expression not supported with rdfs:subClassOf|
|[Section top](#minorfail-outcome-number-19)|Pointer|<pre lang="Turtle"><code>coswot:StateKind a owl:Class ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;State Kind&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:comment &#34;Identifiable conditions that features are or may be in, and ...&#34; ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy &#60;https://w3id.org/coswot/core/states> ;  &#10;&#32;&#32;&#32;&#32;rdfs:subClassOf &#91; a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:allValuesFrom coswot:StateKind ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:onProperty skos:broader ],  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#91; a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:allValuesFrom coswot:StateKind ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:onProperty skos:narrower ],  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#91; a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:allValuesFrom owl:Nothing ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:onProperty coswot:hasKind ],  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#91; a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:allValuesFrom coswot:StateKind ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:onProperty skos:broader ],  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#91; a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:allValuesFrom coswot:StateKind ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:onProperty skos:narrower ],  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;skos:Concept,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;coswot:State ;  &#10;&#32;&#32;&#32;&#32;skos:note &#34;Concepts from existing code lists, vocabularies, and taxonom...&#34; .</code></pre>|
|[Section top](#minorfail-outcome-number-19)|Pointer|<pre lang="Turtle"><code>coswot:StateOfInterest a owl:Class ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;State of Interest&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:comment &#34;Identifiable conditions that features of interest are or may...&#34; ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy &#60;https://w3id.org/coswot/core/states> ;  &#10;&#32;&#32;&#32;&#32;rdfs:subClassOf &#91; a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:allValuesFrom coswot:StateKind ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:onProperty coswot:hasKind ],  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#91; a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:onProperty coswot:hasKind ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:someValuesFrom coswot:StateKind ],  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#91; a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:onProperty coswot:isStateOfInterestOf ],  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;coswot:State ;  &#10;&#32;&#32;&#32;&#32;skos:note &#34;A state of interest is the state of (OP coswot:isStateOfInte...&#34;,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#34;Per convention, the IRI of states of interest should consist...&#34;,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#34;States of interest need not always be explicited. It depends...&#34; .</code></pre>|

***
### MinorFail Outcome number 20

[Jump to summary definition](#summary-MinorFail-20)	|	[Previous MinorFail outcome](#minorfail-outcome-number-19)	|	[Next MinorFail outcome](#minorfail-outcome-number-21)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-src-states-ontology|
|----|----|
|Title|Standalone module src/states/ontology.ttl from branch main|
|Composition|- [Module states/ontology](https://gitlab.com/coswot/coswot-acimov/blob/main/src/states/ontology.ttl)|

#### Criterion detail
|Identifier|[profile-compatibility](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#profile-compatibility)|
|----|----|
|Title|Profile compatibility test|
|Description|A test meant to check whether the test subject is compatible with a profile or not, and if it is not, why.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-20)|Identifier|`owl-ql-profile-error`|
|[Section top](#minorfail-outcome-number-20)|Title|OWL QL Profile incompatible|
|[Section top](#minorfail-outcome-number-20)|Description|Property inclusions involving property chains not supported|
|[Section top](#minorfail-outcome-number-20)|Pointer|<pre lang="Turtle"><code>coswot:hasKind a owl:ObjectProperty ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;has state kind&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:comment &#34;links a state of interest to its kind, a state kind&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:domain coswot:StateOfInterest ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy &#60;https://w3id.org/coswot/core/states> ;  &#10;&#32;&#32;&#32;&#32;rdfs:range coswot:StateKind ;  &#10;&#32;&#32;&#32;&#32;owl:propertyChainAxiom ( coswot:hasKind skos:broader ) .</code></pre>|

***
### MinorFail Outcome number 21

[Jump to summary definition](#summary-MinorFail-21)	|	[Previous MinorFail outcome](#minorfail-outcome-number-20)	|	[Next MinorFail outcome](#minorfail-outcome-number-22)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-src-states-ontology|
|----|----|
|Title|Standalone module src/states/ontology.ttl from branch main|
|Composition|- [Module states/ontology](https://gitlab.com/coswot/coswot-acimov/blob/main/src/states/ontology.ttl)|

#### Criterion detail
|Identifier|[profile-compatibility](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#profile-compatibility)|
|----|----|
|Title|Profile compatibility test|
|Description|A test meant to check whether the test subject is compatible with a profile or not, and if it is not, why.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-21)|Identifier|`owl-ql-profile-error`|
|[Section top](#minorfail-outcome-number-21)|Title|OWL QL Profile incompatible|
|[Section top](#minorfail-outcome-number-21)|Description|Class Expression not supported as object of rdfs:domain or rdfs:range|
|[Section top](#minorfail-outcome-number-21)|Pointer|<pre lang="Turtle"><code>coswot:isStateOf a owl:ObjectProperty ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;is state of&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:comment &#34;Links a state to the feature kind or feature of interest it ...&#34; ;  &#10;&#32;&#32;&#32;&#32;rdfs:domain coswot:StateKind ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy &#60;https://w3id.org/coswot/core/states> ;  &#10;&#32;&#32;&#32;&#32;rdfs:range &#91; a owl:Class ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:unionOf ( coswot:Feature coswot:StateOfInterest ) ] ;  &#10;&#32;&#32;&#32;&#32;owl:inverseOf coswot:hasState .</code></pre>|

***
### MinorFail Outcome number 22

[Jump to summary definition](#summary-MinorFail-22)	|	[Previous MinorFail outcome](#minorfail-outcome-number-21)	|	[Next MinorFail outcome](#minorfail-outcome-number-23)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-src-states-ontology|
|----|----|
|Title|Standalone module src/states/ontology.ttl from branch main|
|Composition|- [Module states/ontology](https://gitlab.com/coswot/coswot-acimov/blob/main/src/states/ontology.ttl)|

#### Criterion detail
|Identifier|[profile-compatibility](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#profile-compatibility)|
|----|----|
|Title|Profile compatibility test|
|Description|A test meant to check whether the test subject is compatible with a profile or not, and if it is not, why.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-22)|Identifier|`owl-ql-profile-error`|
|[Section top](#minorfail-outcome-number-22)|Title|OWL QL Profile incompatible|
|[Section top](#minorfail-outcome-number-22)|Description|Class Expression not supported as object of rdfs:domain or rdfs:range  &#10;Property inclusions involving property chains not supported|
|[Section top](#minorfail-outcome-number-22)|Pointer|<pre lang="Turtle"><code>coswot:hasState a owl:ObjectProperty ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;has state&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:comment &#34;Links a feature kind or a feature of interest to one of its ...&#34; ;  &#10;&#32;&#32;&#32;&#32;rdfs:domain &#91; a owl:Class ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:unionOf ( coswot:Feature coswot:StateOfInterest ) ] ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy &#60;https://w3id.org/coswot/core/states> ;  &#10;&#32;&#32;&#32;&#32;rdfs:range coswot:StateKind ;  &#10;&#32;&#32;&#32;&#32;owl:inverseOf coswot:isStateOf ;  &#10;&#32;&#32;&#32;&#32;owl:propertyChainAxiom ( skos:broader coswot:hasState ),  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;( coswot:hasKind coswot:hasState ),  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;( coswot:hasStateOfInterest coswot:hasKind ) .</code></pre>|

***
### MinorFail Outcome number 23

[Jump to summary definition](#summary-MinorFail-23)	|	[Previous MinorFail outcome](#minorfail-outcome-number-22)	|	[Next MinorFail outcome](#minorfail-outcome-number-24)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-src-states-ontology|
|----|----|
|Title|Standalone module src/states/ontology.ttl from branch main|
|Composition|- [Module states/ontology](https://gitlab.com/coswot/coswot-acimov/blob/main/src/states/ontology.ttl)|

#### Criterion detail
|Identifier|[profile-compatibility](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#profile-compatibility)|
|----|----|
|Title|Profile compatibility test|
|Description|A test meant to check whether the test subject is compatible with a profile or not, and if it is not, why.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-23)|Identifier|`owl-ql-profile-error`|
|[Section top](#minorfail-outcome-number-23)|Title|OWL QL Profile incompatible|
|[Section top](#minorfail-outcome-number-23)|Description|Statement not supported|
|[Section top](#minorfail-outcome-number-23)|Pointer|<pre lang="Turtle"><code>coswot:State a owl:Class ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;State&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:comment &#34;Identifiable conditions that features are or may be in, and ...&#34; ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy &#60;https://w3id.org/coswot/core/states> ;  &#10;&#32;&#32;&#32;&#32;owl:disjointUnionOf ( coswot:StateOfInterest coswot:StateKind ) .</code></pre>|

***
### MinorFail Outcome number 24

[Jump to summary definition](#summary-MinorFail-24)	|	[Previous MinorFail outcome](#minorfail-outcome-number-23)	|	[Next MinorFail outcome](#minorfail-outcome-number-25)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-src-states-ontology|
|----|----|
|Title|Standalone module src/states/ontology.ttl from branch main|
|Composition|- [Module states/ontology](https://gitlab.com/coswot/coswot-acimov/blob/main/src/states/ontology.ttl)|

#### Criterion detail
|Identifier|[profile-compatibility](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#profile-compatibility)|
|----|----|
|Title|Profile compatibility test|
|Description|A test meant to check whether the test subject is compatible with a profile or not, and if it is not, why.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-24)|Identifier|`owl-el-profile-error`|
|[Section top](#minorfail-outcome-number-24)|Title|OWL EL Profile incompatible|
|[Section top](#minorfail-outcome-number-24)|Description|Statement not supported in a Class Expression|
|[Section top](#minorfail-outcome-number-24)|Pointer|<pre lang="Turtle"><code>&#91;] a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;owl:allValuesFrom coswot:StateKind ;  &#10;&#32;&#32;&#32;&#32;owl:onProperty skos:broader .</code></pre>|
|[Section top](#minorfail-outcome-number-24)|Pointer|<pre lang="Turtle"><code>&#91;] a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;owl:allValuesFrom coswot:StateKind ;  &#10;&#32;&#32;&#32;&#32;owl:onProperty skos:narrower .</code></pre>|
|[Section top](#minorfail-outcome-number-24)|Pointer|<pre lang="Turtle"><code>&#91;] a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;owl:allValuesFrom owl:Nothing ;  &#10;&#32;&#32;&#32;&#32;owl:onProperty coswot:hasKind .</code></pre>|
|[Section top](#minorfail-outcome-number-24)|Pointer|<pre lang="Turtle"><code>&#91;] a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;owl:allValuesFrom coswot:StateKind ;  &#10;&#32;&#32;&#32;&#32;owl:onProperty coswot:hasKind .</code></pre>|
|[Section top](#minorfail-outcome-number-24)|Pointer|<pre lang="Turtle"><code>&#91;] a owl:Class ;  &#10;&#32;&#32;&#32;&#32;owl:unionOf ( coswot:Feature coswot:StateOfInterest ) .</code></pre>|
|[Section top](#minorfail-outcome-number-24)|Pointer|<pre lang="Turtle"><code>&#91;] a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;owl:onProperty coswot:isStateOfInterestOf .</code></pre>|

***
### MinorFail Outcome number 25

[Jump to summary definition](#summary-MinorFail-25)	|	[Previous MinorFail outcome](#minorfail-outcome-number-24)	|	[Next MinorFail outcome](#minorfail-outcome-number-26)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-src-states-ontology|
|----|----|
|Title|Standalone module src/states/ontology.ttl from branch main|
|Composition|- [Module states/ontology](https://gitlab.com/coswot/coswot-acimov/blob/main/src/states/ontology.ttl)|

#### Criterion detail
|Identifier|[profile-compatibility](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#profile-compatibility)|
|----|----|
|Title|Profile compatibility test|
|Description|A test meant to check whether the test subject is compatible with a profile or not, and if it is not, why.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-25)|Identifier|`owl-el-profile-error`|
|[Section top](#minorfail-outcome-number-25)|Title|OWL EL Profile incompatible|
|[Section top](#minorfail-outcome-number-25)|Description|Statement not supported|
|[Section top](#minorfail-outcome-number-25)|Pointer|<pre lang="Turtle"><code>coswot:State a owl:Class ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;State&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:comment &#34;Identifiable conditions that features are or may be in, and ...&#34; ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy &#60;https://w3id.org/coswot/core/states> ;  &#10;&#32;&#32;&#32;&#32;owl:disjointUnionOf ( coswot:StateOfInterest coswot:StateKind ) .</code></pre>|

***
### MinorFail Outcome number 26

[Jump to summary definition](#summary-MinorFail-26)	|	[Previous MinorFail outcome](#minorfail-outcome-number-25)	|	[Next MinorFail outcome](#minorfail-outcome-number-27)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-src-states-ontology|
|----|----|
|Title|Standalone module src/states/ontology.ttl from branch main|
|Composition|- [Module states/ontology](https://gitlab.com/coswot/coswot-acimov/blob/main/src/states/ontology.ttl)|

#### Criterion detail
|Identifier|[profile-compatibility](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#profile-compatibility)|
|----|----|
|Title|Profile compatibility test|
|Description|A test meant to check whether the test subject is compatible with a profile or not, and if it is not, why.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-26)|Identifier|`owl-el-profile-error`|
|[Section top](#minorfail-outcome-number-26)|Title|OWL EL Profile incompatible|
|[Section top](#minorfail-outcome-number-26)|Description|Class Expression not supported as object of rdfs:domain or rdfs:range|
|[Section top](#minorfail-outcome-number-26)|Pointer|<pre lang="Turtle"><code>coswot:hasState a owl:ObjectProperty ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;has state&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:comment &#34;Links a feature kind or a feature of interest to one of its ...&#34; ;  &#10;&#32;&#32;&#32;&#32;rdfs:domain &#91; a owl:Class ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:unionOf ( coswot:Feature coswot:StateOfInterest ) ] ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy &#60;https://w3id.org/coswot/core/states> ;  &#10;&#32;&#32;&#32;&#32;rdfs:range coswot:StateKind ;  &#10;&#32;&#32;&#32;&#32;owl:inverseOf coswot:isStateOf ;  &#10;&#32;&#32;&#32;&#32;owl:propertyChainAxiom ( skos:broader coswot:hasState ),  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;( coswot:hasKind coswot:hasState ),  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;( coswot:hasStateOfInterest coswot:hasKind ) .</code></pre>|
|[Section top](#minorfail-outcome-number-26)|Pointer|<pre lang="Turtle"><code>coswot:isStateOf a owl:ObjectProperty ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;is state of&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:comment &#34;Links a state to the feature kind or feature of interest it ...&#34; ;  &#10;&#32;&#32;&#32;&#32;rdfs:domain coswot:StateKind ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy &#60;https://w3id.org/coswot/core/states> ;  &#10;&#32;&#32;&#32;&#32;rdfs:range &#91; a owl:Class ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:unionOf ( coswot:Feature coswot:StateOfInterest ) ] ;  &#10;&#32;&#32;&#32;&#32;owl:inverseOf coswot:hasState .</code></pre>|

***
### MinorFail Outcome number 27

[Jump to summary definition](#summary-MinorFail-27)	|	[Previous MinorFail outcome](#minorfail-outcome-number-26)	|	[Next MinorFail outcome](#minorfail-outcome-number-28)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-src-states-ontology|
|----|----|
|Title|Standalone module src/states/ontology.ttl from branch main|
|Composition|- [Module states/ontology](https://gitlab.com/coswot/coswot-acimov/blob/main/src/states/ontology.ttl)|

#### Criterion detail
|Identifier|[profile-compatibility](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#profile-compatibility)|
|----|----|
|Title|Profile compatibility test|
|Description|A test meant to check whether the test subject is compatible with a profile or not, and if it is not, why.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-27)|Identifier|`owl-el-profile-error`|
|[Section top](#minorfail-outcome-number-27)|Title|OWL EL Profile incompatible|
|[Section top](#minorfail-outcome-number-27)|Description|Class Expression not supported with rdfs:subClassOf|
|[Section top](#minorfail-outcome-number-27)|Pointer|<pre lang="Turtle"><code>coswot:StateKind a owl:Class ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;State Kind&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:comment &#34;Identifiable conditions that features are or may be in, and ...&#34; ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy &#60;https://w3id.org/coswot/core/states> ;  &#10;&#32;&#32;&#32;&#32;rdfs:subClassOf &#91; a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:allValuesFrom coswot:StateKind ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:onProperty skos:broader ],  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#91; a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:allValuesFrom coswot:StateKind ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:onProperty skos:narrower ],  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#91; a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:allValuesFrom owl:Nothing ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:onProperty coswot:hasKind ],  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#91; a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:allValuesFrom coswot:StateKind ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:onProperty skos:broader ],  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#91; a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:allValuesFrom coswot:StateKind ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:onProperty skos:narrower ],  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;skos:Concept,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;coswot:State ;  &#10;&#32;&#32;&#32;&#32;skos:note &#34;Concepts from existing code lists, vocabularies, and taxonom...&#34; .</code></pre>|
|[Section top](#minorfail-outcome-number-27)|Pointer|<pre lang="Turtle"><code>coswot:StateOfInterest a owl:Class ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;State of Interest&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:comment &#34;Identifiable conditions that features of interest are or may...&#34; ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy &#60;https://w3id.org/coswot/core/states> ;  &#10;&#32;&#32;&#32;&#32;rdfs:subClassOf &#91; a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:allValuesFrom coswot:StateKind ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:onProperty coswot:hasKind ],  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#91; a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:onProperty coswot:hasKind ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:someValuesFrom coswot:StateKind ],  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#91; a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:onProperty coswot:isStateOfInterestOf ],  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;coswot:State ;  &#10;&#32;&#32;&#32;&#32;skos:note &#34;A state of interest is the state of (OP coswot:isStateOfInte...&#34;,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#34;Per convention, the IRI of states of interest should consist...&#34;,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#34;States of interest need not always be explicited. It depends...&#34; .</code></pre>|

***
### MinorFail Outcome number 28

[Jump to summary definition](#summary-MinorFail-28)	|	[Previous MinorFail outcome](#minorfail-outcome-number-27)	|	[Next MinorFail outcome](#minorfail-outcome-number-29)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-src-services-operations-ontology|
|----|----|
|Title|Standalone module src/services&lowbar;operations/ontology.ttl from branch main|
|Composition|- [Module services&lowbar;operations/ontology](https://gitlab.com/coswot/coswot-acimov/blob/main/src/services_operations/ontology.ttl)|

#### Criterion detail
|Identifier|[profile-compatibility](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#profile-compatibility)|
|----|----|
|Title|Profile compatibility test|
|Description|A test meant to check whether the test subject is compatible with a profile or not, and if it is not, why.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-28)|Identifier|`owl-rl-profile-error`|
|[Section top](#minorfail-outcome-number-28)|Title|OWL RL Profile incompatible|
|[Section top](#minorfail-outcome-number-28)|Description|Class Expression not supported with rdfs:subClassOf|
|[Section top](#minorfail-outcome-number-28)|Pointer|<pre lang="Turtle"><code>coswot:OperationOfInterest a owl:Class ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;Operation Of Interest&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:comment &#34;An operation of interest is specific to a function of intere...&#34; ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy &#60;https://w3id.org/coswot/core/services&lowbar;operations> ;  &#10;&#32;&#32;&#32;&#32;rdfs:subClassOf &#91; a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:allValuesFrom coswot:OperationKind ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:onProperty coswot:hasKind ],  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#91; a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:onProperty coswot:hasKind ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:someValuesFrom coswot:OperationKind ],  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#91; a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:onClass coswot:CommandOfInterest ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:onProperty coswot:represents ],  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#91; a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:onClass coswot:CommandOfInterest ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:onProperty coswot:represents ],  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#91; a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:onProperty coswot:isOperationOf ],  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;coswot:Operation .</code></pre>|
|[Section top](#minorfail-outcome-number-28)|Pointer|<pre lang="Turtle"><code>coswot:ServiceOfInterest a owl:Class ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;Service Of Interest&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:comment &#34;A coswot:Service is a digital representation of a function i...&#34; ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy &#60;https://w3id.org/coswot/core/services&lowbar;operations> ;  &#10;&#32;&#32;&#32;&#32;rdfs:subClassOf &#91; a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:allValuesFrom coswot:ServiceKind ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:onProperty coswot:hasKind ],  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#91; a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:onProperty coswot:hasKind ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:someValuesFrom coswot:ServiceKind ],  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#91; a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:onClass coswot:FunctionOfInterest ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:onProperty coswot:represents ],  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;coswot:Service .</code></pre>|

***
### MinorFail Outcome number 29

[Jump to summary definition](#summary-MinorFail-29)	|	[Previous MinorFail outcome](#minorfail-outcome-number-28)	|	[Next MinorFail outcome](#minorfail-outcome-number-30)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-src-services-operations-ontology|
|----|----|
|Title|Standalone module src/services&lowbar;operations/ontology.ttl from branch main|
|Composition|- [Module services&lowbar;operations/ontology](https://gitlab.com/coswot/coswot-acimov/blob/main/src/services_operations/ontology.ttl)|

#### Criterion detail
|Identifier|[profile-compatibility](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#profile-compatibility)|
|----|----|
|Title|Profile compatibility test|
|Description|A test meant to check whether the test subject is compatible with a profile or not, and if it is not, why.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-29)|Identifier|`owl-rl-profile-error`|
|[Section top](#minorfail-outcome-number-29)|Title|OWL RL Profile incompatible|
|[Section top](#minorfail-outcome-number-29)|Description|Statement not supported|
|[Section top](#minorfail-outcome-number-29)|Pointer|<pre lang="Turtle"><code>coswot:Service a owl:Class ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;Service&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:comment &#34;A coswot:Service is a digital representation of a function i...&#34; ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy &#60;https://w3id.org/coswot/core/services&lowbar;operations> ;  &#10;&#32;&#32;&#32;&#32;rdfs:subClassOf &#91; a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:allValuesFrom coswot:Function ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:onProperty coswot:represents ],  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;coswot:ProcedureCollection ;  &#10;&#32;&#32;&#32;&#32;owl:disjointUnionOf ( coswot:ServiceOfInterest coswot:ServiceKind ) ;  &#10;&#32;&#32;&#32;&#32;skos:example &#34;For example, a light switch can offer the service of remotel...&#34; ;  &#10;&#32;&#32;&#32;&#32;skos:note &#34;Typically, a device connected to a given network offers one ...&#34; .</code></pre>|

***
### MinorFail Outcome number 30

[Jump to summary definition](#summary-MinorFail-30)	|	[Previous MinorFail outcome](#minorfail-outcome-number-29)	|	[Next MinorFail outcome](#minorfail-outcome-number-31)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-src-services-operations-ontology|
|----|----|
|Title|Standalone module src/services&lowbar;operations/ontology.ttl from branch main|
|Composition|- [Module services&lowbar;operations/ontology](https://gitlab.com/coswot/coswot-acimov/blob/main/src/services_operations/ontology.ttl)|

#### Criterion detail
|Identifier|[profile-compatibility](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#profile-compatibility)|
|----|----|
|Title|Profile compatibility test|
|Description|A test meant to check whether the test subject is compatible with a profile or not, and if it is not, why.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-30)|Identifier|`owl-rl-profile-error`|
|[Section top](#minorfail-outcome-number-30)|Title|OWL RL Profile incompatible|
|[Section top](#minorfail-outcome-number-30)|Description|Statement not supported in a Super Class Expression|
|[Section top](#minorfail-outcome-number-30)|Pointer|<pre lang="Turtle"><code>&#91;] a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;owl:onProperty coswot:hasKind ;  &#10;&#32;&#32;&#32;&#32;owl:someValuesFrom coswot:ServiceKind .</code></pre>|
|[Section top](#minorfail-outcome-number-30)|Pointer|<pre lang="Turtle"><code>&#91;] a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;owl:onProperty coswot:hasKind ;  &#10;&#32;&#32;&#32;&#32;owl:someValuesFrom coswot:OperationKind .</code></pre>|
|[Section top](#minorfail-outcome-number-30)|Pointer|<pre lang="Turtle"><code>&#91;] a owl:Class ;  &#10;&#32;&#32;&#32;&#32;owl:unionOf ( coswot:Service coswot:Operation ) .</code></pre>|
|[Section top](#minorfail-outcome-number-30)|Pointer|<pre lang="Turtle"><code>&#91;] a owl:Class ;  &#10;&#32;&#32;&#32;&#32;owl:unionOf ( coswot:Function coswot:Command ) .</code></pre>|
|[Section top](#minorfail-outcome-number-30)|Pointer|<pre lang="Turtle"><code>&#91;] a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;owl:onClass coswot:FunctionOfInterest ;  &#10;&#32;&#32;&#32;&#32;owl:onProperty coswot:represents .</code></pre>|
|[Section top](#minorfail-outcome-number-30)|Pointer|<pre lang="Turtle"><code>&#91;] a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;owl:onClass coswot:CommandOfInterest ;  &#10;&#32;&#32;&#32;&#32;owl:onProperty coswot:represents .</code></pre>|
|[Section top](#minorfail-outcome-number-30)|Pointer|<pre lang="Turtle"><code>&#91;] a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;owl:onProperty coswot:isOperationOf .</code></pre>|

***
### MinorFail Outcome number 31

[Jump to summary definition](#summary-MinorFail-31)	|	[Previous MinorFail outcome](#minorfail-outcome-number-30)	|	[Next MinorFail outcome](#minorfail-outcome-number-32)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-src-services-operations-ontology|
|----|----|
|Title|Standalone module src/services&lowbar;operations/ontology.ttl from branch main|
|Composition|- [Module services&lowbar;operations/ontology](https://gitlab.com/coswot/coswot-acimov/blob/main/src/services_operations/ontology.ttl)|

#### Criterion detail
|Identifier|[profile-compatibility](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#profile-compatibility)|
|----|----|
|Title|Profile compatibility test|
|Description|A test meant to check whether the test subject is compatible with a profile or not, and if it is not, why.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-31)|Identifier|`owl-rl-profile-error`|
|[Section top](#minorfail-outcome-number-31)|Title|OWL RL Profile incompatible|
|[Section top](#minorfail-outcome-number-31)|Description|Class Expression not supported as object of rdfs:domain or rdfs:range|
|[Section top](#minorfail-outcome-number-31)|Pointer|<pre lang="Turtle"><code>coswot:represents a owl:ObjectProperty ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;represents&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:comment &#34;Links a service to some function or function of interest it ...&#34; ;  &#10;&#32;&#32;&#32;&#32;rdfs:domain &#91; a owl:Class ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:unionOf ( coswot:Service coswot:Operation ) ] ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy &#60;https://w3id.org/coswot/core/services&lowbar;operations> ;  &#10;&#32;&#32;&#32;&#32;rdfs:range &#91; a owl:Class ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:unionOf ( coswot:Function coswot:Command ) ] .</code></pre>|

***
### MinorFail Outcome number 32

[Jump to summary definition](#summary-MinorFail-32)	|	[Previous MinorFail outcome](#minorfail-outcome-number-31)	|	[Next MinorFail outcome](#minorfail-outcome-number-33)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-src-services-operations-ontology|
|----|----|
|Title|Standalone module src/services&lowbar;operations/ontology.ttl from branch main|
|Composition|- [Module services&lowbar;operations/ontology](https://gitlab.com/coswot/coswot-acimov/blob/main/src/services_operations/ontology.ttl)|

#### Criterion detail
|Identifier|[profile-compatibility](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#profile-compatibility)|
|----|----|
|Title|Profile compatibility test|
|Description|A test meant to check whether the test subject is compatible with a profile or not, and if it is not, why.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-32)|Identifier|`owl-ql-profile-error`|
|[Section top](#minorfail-outcome-number-32)|Title|OWL QL Profile incompatible|
|[Section top](#minorfail-outcome-number-32)|Description|Statement not supported in a Super Class Expression|
|[Section top](#minorfail-outcome-number-32)|Pointer|<pre lang="Turtle"><code>&#91;] a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;owl:allValuesFrom coswot:ServiceKind ;  &#10;&#32;&#32;&#32;&#32;owl:onProperty skos:broader .</code></pre>|
|[Section top](#minorfail-outcome-number-32)|Pointer|<pre lang="Turtle"><code>&#91;] a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;owl:allValuesFrom coswot:ServiceKind ;  &#10;&#32;&#32;&#32;&#32;owl:onProperty skos:narrower .</code></pre>|
|[Section top](#minorfail-outcome-number-32)|Pointer|<pre lang="Turtle"><code>&#91;] a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;owl:allValuesFrom owl:Nothing ;  &#10;&#32;&#32;&#32;&#32;owl:onProperty coswot:hasKind .</code></pre>|
|[Section top](#minorfail-outcome-number-32)|Pointer|<pre lang="Turtle"><code>&#91;] a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;owl:allValuesFrom coswot:ServiceKind ;  &#10;&#32;&#32;&#32;&#32;owl:onProperty coswot:hasKind .</code></pre>|
|[Section top](#minorfail-outcome-number-32)|Pointer|<pre lang="Turtle"><code>&#91;] a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;owl:allValuesFrom coswot:OperationKind ;  &#10;&#32;&#32;&#32;&#32;owl:onProperty skos:broader .</code></pre>|
|[Section top](#minorfail-outcome-number-32)|Pointer|<pre lang="Turtle"><code>&#91;] a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;owl:allValuesFrom coswot:OperationKind ;  &#10;&#32;&#32;&#32;&#32;owl:onProperty skos:narrower .</code></pre>|
|[Section top](#minorfail-outcome-number-32)|Pointer|<pre lang="Turtle"><code>&#91;] a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;owl:allValuesFrom coswot:OperationKind ;  &#10;&#32;&#32;&#32;&#32;owl:onProperty coswot:hasKind .</code></pre>|
|[Section top](#minorfail-outcome-number-32)|Pointer|<pre lang="Turtle"><code>&#91;] a owl:Class ;  &#10;&#32;&#32;&#32;&#32;owl:unionOf ( coswot:Service coswot:Operation ) .</code></pre>|
|[Section top](#minorfail-outcome-number-32)|Pointer|<pre lang="Turtle"><code>&#91;] a owl:Class ;  &#10;&#32;&#32;&#32;&#32;owl:unionOf ( coswot:Function coswot:Command ) .</code></pre>|
|[Section top](#minorfail-outcome-number-32)|Pointer|<pre lang="Turtle"><code>&#91;] a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;owl:allValuesFrom coswot:Function ;  &#10;&#32;&#32;&#32;&#32;owl:onProperty coswot:represents .</code></pre>|
|[Section top](#minorfail-outcome-number-32)|Pointer|<pre lang="Turtle"><code>&#91;] a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;owl:allValuesFrom coswot:Service ;  &#10;&#32;&#32;&#32;&#32;owl:onProperty &#91; owl:inverseOf coswot:represents ] .</code></pre>|
|[Section top](#minorfail-outcome-number-32)|Pointer|<pre lang="Turtle"><code>&#91;] a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;owl:allValuesFrom coswot:Command ;  &#10;&#32;&#32;&#32;&#32;owl:onProperty coswot:represents .</code></pre>|
|[Section top](#minorfail-outcome-number-32)|Pointer|<pre lang="Turtle"><code>&#91;] a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;owl:allValuesFrom coswot:Operation ;  &#10;&#32;&#32;&#32;&#32;owl:onProperty &#91; owl:inverseOf coswot:represents ] .</code></pre>|
|[Section top](#minorfail-outcome-number-32)|Pointer|<pre lang="Turtle"><code>&#91;] a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;owl:allValuesFrom coswot:FunctionKind ;  &#10;&#32;&#32;&#32;&#32;owl:onProperty coswot:represents .</code></pre>|
|[Section top](#minorfail-outcome-number-32)|Pointer|<pre lang="Turtle"><code>&#91;] a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;owl:allValuesFrom coswot:ServiceKind ;  &#10;&#32;&#32;&#32;&#32;owl:onProperty &#91; owl:inverseOf coswot:represents ] .</code></pre>|
|[Section top](#minorfail-outcome-number-32)|Pointer|<pre lang="Turtle"><code>&#91;] a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;owl:allValuesFrom coswot:CommandKind ;  &#10;&#32;&#32;&#32;&#32;owl:onProperty coswot:represents .</code></pre>|
|[Section top](#minorfail-outcome-number-32)|Pointer|<pre lang="Turtle"><code>&#91;] a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;owl:allValuesFrom coswot:OperationKind ;  &#10;&#32;&#32;&#32;&#32;owl:onProperty &#91; owl:inverseOf coswot:represents ] .</code></pre>|
|[Section top](#minorfail-outcome-number-32)|Pointer|<pre lang="Turtle"><code>&#91;] a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;owl:onClass coswot:FunctionOfInterest ;  &#10;&#32;&#32;&#32;&#32;owl:onProperty coswot:represents .</code></pre>|
|[Section top](#minorfail-outcome-number-32)|Pointer|<pre lang="Turtle"><code>&#91;] a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;owl:onClass coswot:CommandOfInterest ;  &#10;&#32;&#32;&#32;&#32;owl:onProperty coswot:represents .</code></pre>|
|[Section top](#minorfail-outcome-number-32)|Pointer|<pre lang="Turtle"><code>&#91;] a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;owl:allValuesFrom coswot:ServiceKind ;  &#10;&#32;&#32;&#32;&#32;owl:onProperty coswot:offers .</code></pre>|
|[Section top](#minorfail-outcome-number-32)|Pointer|<pre lang="Turtle"><code>&#91;] a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;owl:allValuesFrom coswot:DeviceKind ;  &#10;&#32;&#32;&#32;&#32;owl:onProperty coswot:isOfferedBy .</code></pre>|
|[Section top](#minorfail-outcome-number-32)|Pointer|<pre lang="Turtle"><code>&#91;] a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;owl:allValuesFrom coswot:OperationKind ;  &#10;&#32;&#32;&#32;&#32;owl:onProperty coswot:hasOperation .</code></pre>|
|[Section top](#minorfail-outcome-number-32)|Pointer|<pre lang="Turtle"><code>&#91;] a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;owl:allValuesFrom coswot:ServiceKind ;  &#10;&#32;&#32;&#32;&#32;owl:onProperty coswot:isOperationOf .</code></pre>|
|[Section top](#minorfail-outcome-number-32)|Pointer|<pre lang="Turtle"><code>&#91;] a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;owl:onProperty coswot:isOperationOf .</code></pre>|
|[Section top](#minorfail-outcome-number-32)|Pointer|<pre lang="Turtle"><code>&#91;] a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;owl:allValuesFrom coswot:Operation ;  &#10;&#32;&#32;&#32;&#32;owl:onProperty coswot:isExecutionOf .</code></pre>|

***
### MinorFail Outcome number 33

[Jump to summary definition](#summary-MinorFail-33)	|	[Previous MinorFail outcome](#minorfail-outcome-number-32)	|	[Next MinorFail outcome](#minorfail-outcome-number-34)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-src-services-operations-ontology|
|----|----|
|Title|Standalone module src/services&lowbar;operations/ontology.ttl from branch main|
|Composition|- [Module services&lowbar;operations/ontology](https://gitlab.com/coswot/coswot-acimov/blob/main/src/services_operations/ontology.ttl)|

#### Criterion detail
|Identifier|[profile-compatibility](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#profile-compatibility)|
|----|----|
|Title|Profile compatibility test|
|Description|A test meant to check whether the test subject is compatible with a profile or not, and if it is not, why.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-33)|Identifier|`owl-ql-profile-error`|
|[Section top](#minorfail-outcome-number-33)|Title|OWL QL Profile incompatible|
|[Section top](#minorfail-outcome-number-33)|Description|Class Expression not supported with rdfs:subClassOf|
|[Section top](#minorfail-outcome-number-33)|Pointer|<pre lang="Turtle"><code>coswot:Command rdfs:subClassOf &#91; a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:allValuesFrom coswot:Operation ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:onProperty &#91; owl:inverseOf coswot:represents ] ] .</code></pre>|
|[Section top](#minorfail-outcome-number-33)|Pointer|<pre lang="Turtle"><code>coswot:CommandKind rdfs:subClassOf &#91; a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:allValuesFrom coswot:OperationKind ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:onProperty &#91; owl:inverseOf coswot:represents ] ] .</code></pre>|
|[Section top](#minorfail-outcome-number-33)|Pointer|<pre lang="Turtle"><code>coswot:DeviceKind rdfs:subClassOf &#91; a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:allValuesFrom coswot:ServiceKind ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:onProperty coswot:offers ] .</code></pre>|
|[Section top](#minorfail-outcome-number-33)|Pointer|<pre lang="Turtle"><code>coswot:Function rdfs:subClassOf &#91; a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:allValuesFrom coswot:Service ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:onProperty &#91; owl:inverseOf coswot:represents ] ] .</code></pre>|
|[Section top](#minorfail-outcome-number-33)|Pointer|<pre lang="Turtle"><code>coswot:FunctionKind rdfs:subClassOf &#91; a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:allValuesFrom coswot:ServiceKind ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:onProperty &#91; owl:inverseOf coswot:represents ] ] .</code></pre>|
|[Section top](#minorfail-outcome-number-33)|Pointer|<pre lang="Turtle"><code>coswot:Operation a owl:Class ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;Operation&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:comment &#34;A coswot:Operation is the means of a service to communicate ...&#34; ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy &#60;https://w3id.org/coswot/core/services&lowbar;operations> ;  &#10;&#32;&#32;&#32;&#32;rdfs:subClassOf &#91; a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:allValuesFrom coswot:Command ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:onProperty coswot:represents ],  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;coswot:Procedure ;  &#10;&#32;&#32;&#32;&#32;owl:disjointUnionOf ( coswot:OperationOfInterest coswot:OperationKind ) ;  &#10;&#32;&#32;&#32;&#32;skos:example &#34;In the set of operations exposed by a smart light bulb on a ...&#34;,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#34;In the set of operations exposed by a smart washing machine ...&#34;,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#34;To turn on a light, send a CoAP PUT request with CBOR conten...&#34; ;  &#10;&#32;&#32;&#32;&#32;skos:note &#34;An operation may be described in terms of its inputs and out...&#34;,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#34;Typically, a device connected to a given network offers one ...&#34; .</code></pre>|
|[Section top](#minorfail-outcome-number-33)|Pointer|<pre lang="Turtle"><code>coswot:OperationExecution a owl:Class ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;Operation Execution&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:comment &#34;Describes the execution of an operation in a network: theâ€“...&#34; ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy &#60;https://w3id.org/coswot/core/services&lowbar;operations> ;  &#10;&#32;&#32;&#32;&#32;rdfs:subClassOf &#91; a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:allValuesFrom coswot:Operation ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:onProperty coswot:isExecutionOf ],  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;coswot:ProcedureExecution .</code></pre>|
|[Section top](#minorfail-outcome-number-33)|Pointer|<pre lang="Turtle"><code>coswot:OperationKind a owl:Class ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;Operation Kind&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:comment &#34;An operation kind describes an archetype of operation.&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy &#60;https://w3id.org/coswot/core/services&lowbar;operations> ;  &#10;&#32;&#32;&#32;&#32;rdfs:subClassOf &#91; a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:allValuesFrom coswot:OperationKind ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:onProperty skos:broader ],  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#91; a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:allValuesFrom coswot:OperationKind ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:onProperty skos:narrower ],  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#91; a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:allValuesFrom owl:Nothing ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:onProperty coswot:hasKind ],  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#91; a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:allValuesFrom coswot:CommandKind ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:onProperty coswot:represents ],  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#91; a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:allValuesFrom coswot:ServiceKind ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:onProperty coswot:isOperationOf ],  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;skos:Concept,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;coswot:Operation .</code></pre>|
|[Section top](#minorfail-outcome-number-33)|Pointer|<pre lang="Turtle"><code>coswot:OperationOfInterest a owl:Class ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;Operation Of Interest&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:comment &#34;An operation of interest is specific to a function of intere...&#34; ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy &#60;https://w3id.org/coswot/core/services&lowbar;operations> ;  &#10;&#32;&#32;&#32;&#32;rdfs:subClassOf &#91; a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:allValuesFrom coswot:OperationKind ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:onProperty coswot:hasKind ],  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#91; a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:onProperty coswot:hasKind ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:someValuesFrom coswot:OperationKind ],  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#91; a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:onClass coswot:CommandOfInterest ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:onProperty coswot:represents ],  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#91; a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:onClass coswot:CommandOfInterest ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:onProperty coswot:represents ],  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#91; a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:onProperty coswot:isOperationOf ],  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;coswot:Operation .</code></pre>|
|[Section top](#minorfail-outcome-number-33)|Pointer|<pre lang="Turtle"><code>coswot:ServiceKind a owl:Class ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;Service Kind&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:comment &#34;A coswot:Service is a digital representation of a function i...&#34; ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy &#60;https://w3id.org/coswot/core/services&lowbar;operations> ;  &#10;&#32;&#32;&#32;&#32;rdfs:subClassOf &#91; a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:allValuesFrom coswot:ServiceKind ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:onProperty skos:broader ],  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#91; a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:allValuesFrom coswot:ServiceKind ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:onProperty skos:narrower ],  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#91; a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:allValuesFrom owl:Nothing ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:onProperty coswot:hasKind ],  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#91; a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:allValuesFrom coswot:FunctionKind ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:onProperty coswot:represents ],  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#91; a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:allValuesFrom coswot:DeviceKind ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:onProperty coswot:isOfferedBy ],  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#91; a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:allValuesFrom coswot:OperationKind ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:onProperty coswot:hasOperation ],  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;coswot:Service .</code></pre>|
|[Section top](#minorfail-outcome-number-33)|Pointer|<pre lang="Turtle"><code>coswot:ServiceOfInterest a owl:Class ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;Service Of Interest&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:comment &#34;A coswot:Service is a digital representation of a function i...&#34; ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy &#60;https://w3id.org/coswot/core/services&lowbar;operations> ;  &#10;&#32;&#32;&#32;&#32;rdfs:subClassOf &#91; a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:allValuesFrom coswot:ServiceKind ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:onProperty coswot:hasKind ],  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#91; a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:onProperty coswot:hasKind ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:someValuesFrom coswot:ServiceKind ],  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#91; a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:onClass coswot:FunctionOfInterest ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:onProperty coswot:represents ],  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;coswot:Service .</code></pre>|

***
### MinorFail Outcome number 34

[Jump to summary definition](#summary-MinorFail-34)	|	[Previous MinorFail outcome](#minorfail-outcome-number-33)	|	[Next MinorFail outcome](#minorfail-outcome-number-35)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-src-services-operations-ontology|
|----|----|
|Title|Standalone module src/services&lowbar;operations/ontology.ttl from branch main|
|Composition|- [Module services&lowbar;operations/ontology](https://gitlab.com/coswot/coswot-acimov/blob/main/src/services_operations/ontology.ttl)|

#### Criterion detail
|Identifier|[profile-compatibility](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#profile-compatibility)|
|----|----|
|Title|Profile compatibility test|
|Description|A test meant to check whether the test subject is compatible with a profile or not, and if it is not, why.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-34)|Identifier|`owl-ql-profile-error`|
|[Section top](#minorfail-outcome-number-34)|Title|OWL QL Profile incompatible|
|[Section top](#minorfail-outcome-number-34)|Description|Class Expression not supported as object of rdfs:domain or rdfs:range|
|[Section top](#minorfail-outcome-number-34)|Pointer|<pre lang="Turtle"><code>coswot:represents a owl:ObjectProperty ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;represents&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:comment &#34;Links a service to some function or function of interest it ...&#34; ;  &#10;&#32;&#32;&#32;&#32;rdfs:domain &#91; a owl:Class ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:unionOf ( coswot:Service coswot:Operation ) ] ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy &#60;https://w3id.org/coswot/core/services&lowbar;operations> ;  &#10;&#32;&#32;&#32;&#32;rdfs:range &#91; a owl:Class ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:unionOf ( coswot:Function coswot:Command ) ] .</code></pre>|

***
### MinorFail Outcome number 35

[Jump to summary definition](#summary-MinorFail-35)	|	[Previous MinorFail outcome](#minorfail-outcome-number-34)	|	[Next MinorFail outcome](#minorfail-outcome-number-36)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-src-services-operations-ontology|
|----|----|
|Title|Standalone module src/services&lowbar;operations/ontology.ttl from branch main|
|Composition|- [Module services&lowbar;operations/ontology](https://gitlab.com/coswot/coswot-acimov/blob/main/src/services_operations/ontology.ttl)|

#### Criterion detail
|Identifier|[profile-compatibility](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#profile-compatibility)|
|----|----|
|Title|Profile compatibility test|
|Description|A test meant to check whether the test subject is compatible with a profile or not, and if it is not, why.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-35)|Identifier|`owl-ql-profile-error`|
|[Section top](#minorfail-outcome-number-35)|Title|OWL QL Profile incompatible|
|[Section top](#minorfail-outcome-number-35)|Description|Property inclusions involving property chains not supported|
|[Section top](#minorfail-outcome-number-35)|Pointer|<pre lang="Turtle"><code>coswot:isExecutionOf owl:propertyChainAxiom ( coswot:isExecutionOf coswot:hasKind ) .</code></pre>|

***
### MinorFail Outcome number 36

[Jump to summary definition](#summary-MinorFail-36)	|	[Previous MinorFail outcome](#minorfail-outcome-number-35)	|	[Next MinorFail outcome](#minorfail-outcome-number-37)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-src-services-operations-ontology|
|----|----|
|Title|Standalone module src/services&lowbar;operations/ontology.ttl from branch main|
|Composition|- [Module services&lowbar;operations/ontology](https://gitlab.com/coswot/coswot-acimov/blob/main/src/services_operations/ontology.ttl)|

#### Criterion detail
|Identifier|[profile-compatibility](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#profile-compatibility)|
|----|----|
|Title|Profile compatibility test|
|Description|A test meant to check whether the test subject is compatible with a profile or not, and if it is not, why.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-36)|Identifier|`owl-ql-profile-error`|
|[Section top](#minorfail-outcome-number-36)|Title|OWL QL Profile incompatible|
|[Section top](#minorfail-outcome-number-36)|Description|Statement not supported|
|[Section top](#minorfail-outcome-number-36)|Pointer|<pre lang="Turtle"><code>coswot:Service a owl:Class ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;Service&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:comment &#34;A coswot:Service is a digital representation of a function i...&#34; ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy &#60;https://w3id.org/coswot/core/services&lowbar;operations> ;  &#10;&#32;&#32;&#32;&#32;rdfs:subClassOf &#91; a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:allValuesFrom coswot:Function ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:onProperty coswot:represents ],  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;coswot:ProcedureCollection ;  &#10;&#32;&#32;&#32;&#32;owl:disjointUnionOf ( coswot:ServiceOfInterest coswot:ServiceKind ) ;  &#10;&#32;&#32;&#32;&#32;skos:example &#34;For example, a light switch can offer the service of remotel...&#34; ;  &#10;&#32;&#32;&#32;&#32;skos:note &#34;Typically, a device connected to a given network offers one ...&#34; .</code></pre>|

***
### MinorFail Outcome number 37

[Jump to summary definition](#summary-MinorFail-37)	|	[Previous MinorFail outcome](#minorfail-outcome-number-36)	|	[Next MinorFail outcome](#minorfail-outcome-number-38)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-src-services-operations-ontology|
|----|----|
|Title|Standalone module src/services&lowbar;operations/ontology.ttl from branch main|
|Composition|- [Module services&lowbar;operations/ontology](https://gitlab.com/coswot/coswot-acimov/blob/main/src/services_operations/ontology.ttl)|

#### Criterion detail
|Identifier|[profile-compatibility](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#profile-compatibility)|
|----|----|
|Title|Profile compatibility test|
|Description|A test meant to check whether the test subject is compatible with a profile or not, and if it is not, why.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-37)|Identifier|`owl-el-profile-error`|
|[Section top](#minorfail-outcome-number-37)|Title|OWL EL Profile incompatible|
|[Section top](#minorfail-outcome-number-37)|Description|Statement not supported in a Class Expression|
|[Section top](#minorfail-outcome-number-37)|Pointer|<pre lang="Turtle"><code>&#91;] a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;owl:allValuesFrom coswot:ServiceKind ;  &#10;&#32;&#32;&#32;&#32;owl:onProperty skos:broader .</code></pre>|
|[Section top](#minorfail-outcome-number-37)|Pointer|<pre lang="Turtle"><code>&#91;] a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;owl:allValuesFrom coswot:ServiceKind ;  &#10;&#32;&#32;&#32;&#32;owl:onProperty skos:narrower .</code></pre>|
|[Section top](#minorfail-outcome-number-37)|Pointer|<pre lang="Turtle"><code>&#91;] a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;owl:allValuesFrom owl:Nothing ;  &#10;&#32;&#32;&#32;&#32;owl:onProperty coswot:hasKind .</code></pre>|
|[Section top](#minorfail-outcome-number-37)|Pointer|<pre lang="Turtle"><code>&#91;] a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;owl:allValuesFrom coswot:ServiceKind ;  &#10;&#32;&#32;&#32;&#32;owl:onProperty coswot:hasKind .</code></pre>|
|[Section top](#minorfail-outcome-number-37)|Pointer|<pre lang="Turtle"><code>&#91;] a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;owl:allValuesFrom coswot:OperationKind ;  &#10;&#32;&#32;&#32;&#32;owl:onProperty skos:broader .</code></pre>|
|[Section top](#minorfail-outcome-number-37)|Pointer|<pre lang="Turtle"><code>&#91;] a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;owl:allValuesFrom coswot:OperationKind ;  &#10;&#32;&#32;&#32;&#32;owl:onProperty skos:narrower .</code></pre>|
|[Section top](#minorfail-outcome-number-37)|Pointer|<pre lang="Turtle"><code>&#91;] a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;owl:allValuesFrom coswot:OperationKind ;  &#10;&#32;&#32;&#32;&#32;owl:onProperty coswot:hasKind .</code></pre>|
|[Section top](#minorfail-outcome-number-37)|Pointer|<pre lang="Turtle"><code>&#91;] a owl:Class ;  &#10;&#32;&#32;&#32;&#32;owl:unionOf ( coswot:Service coswot:Operation ) .</code></pre>|
|[Section top](#minorfail-outcome-number-37)|Pointer|<pre lang="Turtle"><code>&#91;] a owl:Class ;  &#10;&#32;&#32;&#32;&#32;owl:unionOf ( coswot:Function coswot:Command ) .</code></pre>|
|[Section top](#minorfail-outcome-number-37)|Pointer|<pre lang="Turtle"><code>&#91;] a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;owl:allValuesFrom coswot:Function ;  &#10;&#32;&#32;&#32;&#32;owl:onProperty coswot:represents .</code></pre>|
|[Section top](#minorfail-outcome-number-37)|Pointer|<pre lang="Turtle"><code>&#91;] a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;owl:allValuesFrom coswot:Service ;  &#10;&#32;&#32;&#32;&#32;owl:onProperty &#91; owl:inverseOf coswot:represents ] .</code></pre>|
|[Section top](#minorfail-outcome-number-37)|Pointer|<pre lang="Turtle"><code>&#91;] a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;owl:allValuesFrom coswot:Command ;  &#10;&#32;&#32;&#32;&#32;owl:onProperty coswot:represents .</code></pre>|
|[Section top](#minorfail-outcome-number-37)|Pointer|<pre lang="Turtle"><code>&#91;] a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;owl:allValuesFrom coswot:Operation ;  &#10;&#32;&#32;&#32;&#32;owl:onProperty &#91; owl:inverseOf coswot:represents ] .</code></pre>|
|[Section top](#minorfail-outcome-number-37)|Pointer|<pre lang="Turtle"><code>&#91;] a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;owl:allValuesFrom coswot:FunctionKind ;  &#10;&#32;&#32;&#32;&#32;owl:onProperty coswot:represents .</code></pre>|
|[Section top](#minorfail-outcome-number-37)|Pointer|<pre lang="Turtle"><code>&#91;] a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;owl:allValuesFrom coswot:ServiceKind ;  &#10;&#32;&#32;&#32;&#32;owl:onProperty &#91; owl:inverseOf coswot:represents ] .</code></pre>|
|[Section top](#minorfail-outcome-number-37)|Pointer|<pre lang="Turtle"><code>&#91;] a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;owl:allValuesFrom coswot:CommandKind ;  &#10;&#32;&#32;&#32;&#32;owl:onProperty coswot:represents .</code></pre>|
|[Section top](#minorfail-outcome-number-37)|Pointer|<pre lang="Turtle"><code>&#91;] a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;owl:allValuesFrom coswot:OperationKind ;  &#10;&#32;&#32;&#32;&#32;owl:onProperty &#91; owl:inverseOf coswot:represents ] .</code></pre>|
|[Section top](#minorfail-outcome-number-37)|Pointer|<pre lang="Turtle"><code>&#91;] a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;owl:onClass coswot:FunctionOfInterest ;  &#10;&#32;&#32;&#32;&#32;owl:onProperty coswot:represents .</code></pre>|
|[Section top](#minorfail-outcome-number-37)|Pointer|<pre lang="Turtle"><code>&#91;] a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;owl:onClass coswot:CommandOfInterest ;  &#10;&#32;&#32;&#32;&#32;owl:onProperty coswot:represents .</code></pre>|
|[Section top](#minorfail-outcome-number-37)|Pointer|<pre lang="Turtle"><code>&#91;] a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;owl:allValuesFrom coswot:ServiceKind ;  &#10;&#32;&#32;&#32;&#32;owl:onProperty coswot:offers .</code></pre>|
|[Section top](#minorfail-outcome-number-37)|Pointer|<pre lang="Turtle"><code>&#91;] a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;owl:allValuesFrom coswot:DeviceKind ;  &#10;&#32;&#32;&#32;&#32;owl:onProperty coswot:isOfferedBy .</code></pre>|
|[Section top](#minorfail-outcome-number-37)|Pointer|<pre lang="Turtle"><code>&#91;] a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;owl:allValuesFrom coswot:OperationKind ;  &#10;&#32;&#32;&#32;&#32;owl:onProperty coswot:hasOperation .</code></pre>|
|[Section top](#minorfail-outcome-number-37)|Pointer|<pre lang="Turtle"><code>&#91;] a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;owl:allValuesFrom coswot:ServiceKind ;  &#10;&#32;&#32;&#32;&#32;owl:onProperty coswot:isOperationOf .</code></pre>|
|[Section top](#minorfail-outcome-number-37)|Pointer|<pre lang="Turtle"><code>&#91;] a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;owl:onProperty coswot:isOperationOf .</code></pre>|
|[Section top](#minorfail-outcome-number-37)|Pointer|<pre lang="Turtle"><code>&#91;] a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;owl:allValuesFrom coswot:Operation ;  &#10;&#32;&#32;&#32;&#32;owl:onProperty coswot:isExecutionOf .</code></pre>|

***
### MinorFail Outcome number 38

[Jump to summary definition](#summary-MinorFail-38)	|	[Previous MinorFail outcome](#minorfail-outcome-number-37)	|	[Next MinorFail outcome](#minorfail-outcome-number-39)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-src-services-operations-ontology|
|----|----|
|Title|Standalone module src/services&lowbar;operations/ontology.ttl from branch main|
|Composition|- [Module services&lowbar;operations/ontology](https://gitlab.com/coswot/coswot-acimov/blob/main/src/services_operations/ontology.ttl)|

#### Criterion detail
|Identifier|[profile-compatibility](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#profile-compatibility)|
|----|----|
|Title|Profile compatibility test|
|Description|A test meant to check whether the test subject is compatible with a profile or not, and if it is not, why.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-38)|Identifier|`owl-el-profile-error`|
|[Section top](#minorfail-outcome-number-38)|Title|OWL EL Profile incompatible|
|[Section top](#minorfail-outcome-number-38)|Description|Statement not supported|
|[Section top](#minorfail-outcome-number-38)|Pointer|<pre lang="Turtle"><code>coswot:Service a owl:Class ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;Service&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:comment &#34;A coswot:Service is a digital representation of a function i...&#34; ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy &#60;https://w3id.org/coswot/core/services&lowbar;operations> ;  &#10;&#32;&#32;&#32;&#32;rdfs:subClassOf &#91; a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:allValuesFrom coswot:Function ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:onProperty coswot:represents ],  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;coswot:ProcedureCollection ;  &#10;&#32;&#32;&#32;&#32;owl:disjointUnionOf ( coswot:ServiceOfInterest coswot:ServiceKind ) ;  &#10;&#32;&#32;&#32;&#32;skos:example &#34;For example, a light switch can offer the service of remotel...&#34; ;  &#10;&#32;&#32;&#32;&#32;skos:note &#34;Typically, a device connected to a given network offers one ...&#34; .</code></pre>|

***
### MinorFail Outcome number 39

[Jump to summary definition](#summary-MinorFail-39)	|	[Previous MinorFail outcome](#minorfail-outcome-number-38)	|	[Next MinorFail outcome](#minorfail-outcome-number-40)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-src-services-operations-ontology|
|----|----|
|Title|Standalone module src/services&lowbar;operations/ontology.ttl from branch main|
|Composition|- [Module services&lowbar;operations/ontology](https://gitlab.com/coswot/coswot-acimov/blob/main/src/services_operations/ontology.ttl)|

#### Criterion detail
|Identifier|[profile-compatibility](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#profile-compatibility)|
|----|----|
|Title|Profile compatibility test|
|Description|A test meant to check whether the test subject is compatible with a profile or not, and if it is not, why.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-39)|Identifier|`owl-el-profile-error`|
|[Section top](#minorfail-outcome-number-39)|Title|OWL EL Profile incompatible|
|[Section top](#minorfail-outcome-number-39)|Description|Class Expression not supported as object of rdfs:domain or rdfs:range|
|[Section top](#minorfail-outcome-number-39)|Pointer|<pre lang="Turtle"><code>coswot:represents a owl:ObjectProperty ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;represents&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:comment &#34;Links a service to some function or function of interest it ...&#34; ;  &#10;&#32;&#32;&#32;&#32;rdfs:domain &#91; a owl:Class ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:unionOf ( coswot:Service coswot:Operation ) ] ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy &#60;https://w3id.org/coswot/core/services&lowbar;operations> ;  &#10;&#32;&#32;&#32;&#32;rdfs:range &#91; a owl:Class ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:unionOf ( coswot:Function coswot:Command ) ] .</code></pre>|

***
### MinorFail Outcome number 40

[Jump to summary definition](#summary-MinorFail-40)	|	[Previous MinorFail outcome](#minorfail-outcome-number-39)	|	[Next MinorFail outcome](#minorfail-outcome-number-41)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-src-services-operations-ontology|
|----|----|
|Title|Standalone module src/services&lowbar;operations/ontology.ttl from branch main|
|Composition|- [Module services&lowbar;operations/ontology](https://gitlab.com/coswot/coswot-acimov/blob/main/src/services_operations/ontology.ttl)|

#### Criterion detail
|Identifier|[profile-compatibility](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#profile-compatibility)|
|----|----|
|Title|Profile compatibility test|
|Description|A test meant to check whether the test subject is compatible with a profile or not, and if it is not, why.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-40)|Identifier|`owl-el-profile-error`|
|[Section top](#minorfail-outcome-number-40)|Title|OWL EL Profile incompatible|
|[Section top](#minorfail-outcome-number-40)|Description|Class Expression not supported with rdfs:subClassOf|
|[Section top](#minorfail-outcome-number-40)|Pointer|<pre lang="Turtle"><code>coswot:Command rdfs:subClassOf &#91; a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:allValuesFrom coswot:Operation ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:onProperty &#91; owl:inverseOf coswot:represents ] ] .</code></pre>|
|[Section top](#minorfail-outcome-number-40)|Pointer|<pre lang="Turtle"><code>coswot:CommandKind rdfs:subClassOf &#91; a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:allValuesFrom coswot:OperationKind ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:onProperty &#91; owl:inverseOf coswot:represents ] ] .</code></pre>|
|[Section top](#minorfail-outcome-number-40)|Pointer|<pre lang="Turtle"><code>coswot:DeviceKind rdfs:subClassOf &#91; a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:allValuesFrom coswot:ServiceKind ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:onProperty coswot:offers ] .</code></pre>|
|[Section top](#minorfail-outcome-number-40)|Pointer|<pre lang="Turtle"><code>coswot:Function rdfs:subClassOf &#91; a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:allValuesFrom coswot:Service ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:onProperty &#91; owl:inverseOf coswot:represents ] ] .</code></pre>|
|[Section top](#minorfail-outcome-number-40)|Pointer|<pre lang="Turtle"><code>coswot:FunctionKind rdfs:subClassOf &#91; a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:allValuesFrom coswot:ServiceKind ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:onProperty &#91; owl:inverseOf coswot:represents ] ] .</code></pre>|
|[Section top](#minorfail-outcome-number-40)|Pointer|<pre lang="Turtle"><code>coswot:Operation a owl:Class ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;Operation&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:comment &#34;A coswot:Operation is the means of a service to communicate ...&#34; ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy &#60;https://w3id.org/coswot/core/services&lowbar;operations> ;  &#10;&#32;&#32;&#32;&#32;rdfs:subClassOf &#91; a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:allValuesFrom coswot:Command ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:onProperty coswot:represents ],  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;coswot:Procedure ;  &#10;&#32;&#32;&#32;&#32;owl:disjointUnionOf ( coswot:OperationOfInterest coswot:OperationKind ) ;  &#10;&#32;&#32;&#32;&#32;skos:example &#34;In the set of operations exposed by a smart light bulb on a ...&#34;,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#34;In the set of operations exposed by a smart washing machine ...&#34;,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#34;To turn on a light, send a CoAP PUT request with CBOR conten...&#34; ;  &#10;&#32;&#32;&#32;&#32;skos:note &#34;An operation may be described in terms of its inputs and out...&#34;,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#34;Typically, a device connected to a given network offers one ...&#34; .</code></pre>|
|[Section top](#minorfail-outcome-number-40)|Pointer|<pre lang="Turtle"><code>coswot:OperationExecution a owl:Class ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;Operation Execution&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:comment &#34;Describes the execution of an operation in a network: theâ€“...&#34; ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy &#60;https://w3id.org/coswot/core/services&lowbar;operations> ;  &#10;&#32;&#32;&#32;&#32;rdfs:subClassOf &#91; a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:allValuesFrom coswot:Operation ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:onProperty coswot:isExecutionOf ],  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;coswot:ProcedureExecution .</code></pre>|
|[Section top](#minorfail-outcome-number-40)|Pointer|<pre lang="Turtle"><code>coswot:OperationKind a owl:Class ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;Operation Kind&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:comment &#34;An operation kind describes an archetype of operation.&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy &#60;https://w3id.org/coswot/core/services&lowbar;operations> ;  &#10;&#32;&#32;&#32;&#32;rdfs:subClassOf &#91; a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:allValuesFrom coswot:OperationKind ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:onProperty skos:broader ],  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#91; a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:allValuesFrom coswot:OperationKind ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:onProperty skos:narrower ],  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#91; a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:allValuesFrom owl:Nothing ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:onProperty coswot:hasKind ],  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#91; a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:allValuesFrom coswot:CommandKind ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:onProperty coswot:represents ],  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#91; a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:allValuesFrom coswot:ServiceKind ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:onProperty coswot:isOperationOf ],  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;skos:Concept,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;coswot:Operation .</code></pre>|
|[Section top](#minorfail-outcome-number-40)|Pointer|<pre lang="Turtle"><code>coswot:OperationOfInterest a owl:Class ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;Operation Of Interest&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:comment &#34;An operation of interest is specific to a function of intere...&#34; ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy &#60;https://w3id.org/coswot/core/services&lowbar;operations> ;  &#10;&#32;&#32;&#32;&#32;rdfs:subClassOf &#91; a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:allValuesFrom coswot:OperationKind ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:onProperty coswot:hasKind ],  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#91; a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:onProperty coswot:hasKind ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:someValuesFrom coswot:OperationKind ],  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#91; a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:onClass coswot:CommandOfInterest ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:onProperty coswot:represents ],  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#91; a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:onClass coswot:CommandOfInterest ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:onProperty coswot:represents ],  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#91; a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:onProperty coswot:isOperationOf ],  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;coswot:Operation .</code></pre>|
|[Section top](#minorfail-outcome-number-40)|Pointer|<pre lang="Turtle"><code>coswot:ServiceKind a owl:Class ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;Service Kind&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:comment &#34;A coswot:Service is a digital representation of a function i...&#34; ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy &#60;https://w3id.org/coswot/core/services&lowbar;operations> ;  &#10;&#32;&#32;&#32;&#32;rdfs:subClassOf &#91; a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:allValuesFrom coswot:ServiceKind ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:onProperty skos:broader ],  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#91; a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:allValuesFrom coswot:ServiceKind ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:onProperty skos:narrower ],  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#91; a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:allValuesFrom owl:Nothing ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:onProperty coswot:hasKind ],  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#91; a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:allValuesFrom coswot:FunctionKind ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:onProperty coswot:represents ],  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#91; a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:allValuesFrom coswot:DeviceKind ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:onProperty coswot:isOfferedBy ],  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#91; a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:allValuesFrom coswot:OperationKind ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:onProperty coswot:hasOperation ],  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;coswot:Service .</code></pre>|
|[Section top](#minorfail-outcome-number-40)|Pointer|<pre lang="Turtle"><code>coswot:ServiceOfInterest a owl:Class ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;Service Of Interest&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:comment &#34;A coswot:Service is a digital representation of a function i...&#34; ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy &#60;https://w3id.org/coswot/core/services&lowbar;operations> ;  &#10;&#32;&#32;&#32;&#32;rdfs:subClassOf &#91; a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:allValuesFrom coswot:ServiceKind ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:onProperty coswot:hasKind ],  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#91; a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:onProperty coswot:hasKind ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:someValuesFrom coswot:ServiceKind ],  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#91; a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:onClass coswot:FunctionOfInterest ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:onProperty coswot:represents ],  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;coswot:Service .</code></pre>|

***
### MinorFail Outcome number 41

[Jump to summary definition](#summary-MinorFail-41)	|	[Previous MinorFail outcome](#minorfail-outcome-number-40)	|	[Next MinorFail outcome](#minorfail-outcome-number-42)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-src-services-operations-ontology|
|----|----|
|Title|Standalone module src/services&lowbar;operations/ontology.ttl from branch main|
|Composition|- [Module services&lowbar;operations/ontology](https://gitlab.com/coswot/coswot-acimov/blob/main/src/services_operations/ontology.ttl)|

#### Criterion detail
|Identifier|[term-referencing](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#term-referencing)|
|----|----|
|Title|Term referencing test|
|Description|A test case from the Best Practices tests checking if each term of the test subject is referenced to a module through a rdfs:isDefinedBy property.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-41)|Identifier|`no-reference-module`|
|[Section top](#minorfail-outcome-number-41)|Title|Term not referenced to a module|
|[Section top](#minorfail-outcome-number-41)|Description|Subject terms not linked to a module by a rdfs:isDefinedBy property|
|[Section top](#minorfail-outcome-number-41)|Pointer|<pre lang="Turtle"><code>:Function rdfs:subClassOf &#91; a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:allValuesFrom :Service ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:onProperty &#91; owl:inverseOf :represents ] ] .</code></pre>|
|[Section top](#minorfail-outcome-number-41)|Pointer|<pre lang="Turtle"><code>:Command rdfs:subClassOf &#91; a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:allValuesFrom :Operation ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:onProperty &#91; owl:inverseOf :represents ] ] .</code></pre>|
|[Section top](#minorfail-outcome-number-41)|Pointer|<pre lang="Turtle"><code>:FunctionKind rdfs:subClassOf &#91; a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:allValuesFrom :ServiceKind ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:onProperty &#91; owl:inverseOf :represents ] ] .</code></pre>|
|[Section top](#minorfail-outcome-number-41)|Pointer|<pre lang="Turtle"><code>:CommandKind rdfs:subClassOf &#91; a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:allValuesFrom :OperationKind ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:onProperty &#91; owl:inverseOf :represents ] ] .</code></pre>|
|[Section top](#minorfail-outcome-number-41)|Pointer|<pre lang="Turtle"><code>:DeviceKind rdfs:subClassOf &#91; a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:allValuesFrom :ServiceKind ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:onProperty :offers ] .</code></pre>|
|[Section top](#minorfail-outcome-number-41)|Pointer|<pre lang="Turtle"><code>:isExecutionOf owl:propertyChainAxiom ( :isExecutionOf :hasKind ) .</code></pre>|

***
### MinorFail Outcome number 42

[Jump to summary definition](#summary-MinorFail-42)	|	[Previous MinorFail outcome](#minorfail-outcome-number-41)	|	[Next MinorFail outcome](#minorfail-outcome-number-43)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-src-samples-ontology|
|----|----|
|Title|Standalone module src/samples/ontology.ttl from branch main|
|Composition|- [Module samples/ontology](https://gitlab.com/coswot/coswot-acimov/blob/main/src/samples/ontology.ttl)|

#### Criterion detail
|Identifier|[profile-compatibility](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#profile-compatibility)|
|----|----|
|Title|Profile compatibility test|
|Description|A test meant to check whether the test subject is compatible with a profile or not, and if it is not, why.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-42)|Identifier|`owl-ql-profile-error`|
|[Section top](#minorfail-outcome-number-42)|Title|OWL QL Profile incompatible|
|[Section top](#minorfail-outcome-number-42)|Description|Property inclusions involving property chains not supported|
|[Section top](#minorfail-outcome-number-42)|Pointer|<pre lang="Turtle"><code>coswot:hasSample a owl:ObjectProperty ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;has sample&#34;@en ;  &#10;&#32;&#32;&#32;&#32;schema:domainIncludes coswot:FeatureOfInterest ;  &#10;&#32;&#32;&#32;&#32;schema:rangeIncludes coswot:Sample ;  &#10;&#32;&#32;&#32;&#32;rdfs:comment &#34;Relation between a FeatureOfInterest and the Sample used to ...&#34; ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy &#60;https://w3id.org/coswot/core/samples> ;  &#10;&#32;&#32;&#32;&#32;rdfs:subPropertyOf coswot:hasTransitiveSample ;  &#10;&#32;&#32;&#32;&#32;owl:inverseOf coswot:isSampleOf ;  &#10;&#32;&#32;&#32;&#32;owl:propertyChainAxiom ( coswot:hasPropertyOfInterest coswot:hasSampleProperty coswot:isPropertyOfInterestOf ),  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;( coswot:hasStateOfInterest coswot:hasSampleState coswot:isStateOfInterestOf ) .</code></pre>|

***
### MinorFail Outcome number 43

[Jump to summary definition](#summary-MinorFail-43)	|	[Previous MinorFail outcome](#minorfail-outcome-number-42)	|	[Next MinorFail outcome](#minorfail-outcome-number-44)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-src-samples-ontology|
|----|----|
|Title|Standalone module src/samples/ontology.ttl from branch main|
|Composition|- [Module samples/ontology](https://gitlab.com/coswot/coswot-acimov/blob/main/src/samples/ontology.ttl)|

#### Criterion detail
|Identifier|[profile-compatibility](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#profile-compatibility)|
|----|----|
|Title|Profile compatibility test|
|Description|A test meant to check whether the test subject is compatible with a profile or not, and if it is not, why.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-43)|Identifier|`owl-ql-profile-error`|
|[Section top](#minorfail-outcome-number-43)|Title|OWL QL Profile incompatible|
|[Section top](#minorfail-outcome-number-43)|Description|Statement not supported|
|[Section top](#minorfail-outcome-number-43)|Pointer|<pre lang="Turtle"><code>coswot:isSamplePropertyOf a owl:FunctionalProperty,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:ObjectProperty ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;is sample property of&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:comment &#34;Direct relation from the Property of interest of a sample to...&#34; ;  &#10;&#32;&#32;&#32;&#32;rdfs:domain coswot:PropertyOfInterest ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy &#60;https://w3id.org/coswot/core/samples> ;  &#10;&#32;&#32;&#32;&#32;rdfs:range coswot:PropertyOfInterest .</code></pre>|

***
### MinorFail Outcome number 44

[Jump to summary definition](#summary-MinorFail-44)	|	[Previous MinorFail outcome](#minorfail-outcome-number-43)	|	[Next MinorFail outcome](#minorfail-outcome-number-45)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-src-samples-ontology|
|----|----|
|Title|Standalone module src/samples/ontology.ttl from branch main|
|Composition|- [Module samples/ontology](https://gitlab.com/coswot/coswot-acimov/blob/main/src/samples/ontology.ttl)|

#### Criterion detail
|Identifier|[profile-compatibility](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#profile-compatibility)|
|----|----|
|Title|Profile compatibility test|
|Description|A test meant to check whether the test subject is compatible with a profile or not, and if it is not, why.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-44)|Identifier|`owl-el-profile-error`|
|[Section top](#minorfail-outcome-number-44)|Title|OWL EL Profile incompatible|
|[Section top](#minorfail-outcome-number-44)|Description|Statement not supported|
|[Section top](#minorfail-outcome-number-44)|Pointer|<pre lang="Turtle"><code>coswot:isSamplePropertyOf a owl:FunctionalProperty,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:ObjectProperty ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;is sample property of&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:comment &#34;Direct relation from the Property of interest of a sample to...&#34; ;  &#10;&#32;&#32;&#32;&#32;rdfs:domain coswot:PropertyOfInterest ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy &#60;https://w3id.org/coswot/core/samples> ;  &#10;&#32;&#32;&#32;&#32;rdfs:range coswot:PropertyOfInterest .</code></pre>|

***
### MinorFail Outcome number 45

[Jump to summary definition](#summary-MinorFail-45)	|	[Previous MinorFail outcome](#minorfail-outcome-number-44)	|	[Next MinorFail outcome](#minorfail-outcome-number-46)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-src-property-values-ontology|
|----|----|
|Title|Standalone module src/property&lowbar;values/ontology.ttl from branch main|
|Composition|- [Module property&lowbar;values/ontology](https://gitlab.com/coswot/coswot-acimov/blob/main/src/property_values/ontology.ttl)|

#### Criterion detail
|Identifier|[domain-and-range-referencing](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#domain-and-range-referencing)|
|----|----|
|Title|Domain and range referencing test|
|Description|A test case from the Best Practices tests checking if all the ranges and domains from the test subject point to terms that are defined in the vocabulary.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-45)|Identifier|`range-out-of-vocabulary`|
|[Section top](#minorfail-outcome-number-45)|Title|Range out of vocabulary|
|[Section top](#minorfail-outcome-number-45)|Description|Some properties have a range out of the ontology|
|[Section top](#minorfail-outcome-number-45)|Pointer|<pre lang="Turtle"><code>:isMeasuredIn a owl:ObjectProperty ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;is measured in&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:comment &#34;A relationship identifying the unit of measure used for a ce...&#34; ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy &#60;https://w3id.org/coswot/core/property&lowbar;values> ;  &#10;&#32;&#32;&#32;&#32;rdfs:range owl:Thing,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;skos:Concept,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;:UnitOfMeasure ;  &#10;&#32;&#32;&#32;&#32;rdfs:subPropertyOf :isMeasuredIn ;  &#10;&#32;&#32;&#32;&#32;owl:equivalentProperty :isMeasuredIn .</code></pre>|
|[Section top](#minorfail-outcome-number-45)|Pointer|http://www.w3.org/2004/02/skos/core#Concept|

***
### MinorFail Outcome number 46

[Jump to summary definition](#summary-MinorFail-46)	|	[Previous MinorFail outcome](#minorfail-outcome-number-45)	|	[Next MinorFail outcome](#minorfail-outcome-number-47)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-src-property-values-ontology|
|----|----|
|Title|Standalone module src/property&lowbar;values/ontology.ttl from branch main|
|Composition|- [Module property&lowbar;values/ontology](https://gitlab.com/coswot/coswot-acimov/blob/main/src/property_values/ontology.ttl)|

#### Criterion detail
|Identifier|[profile-compatibility](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#profile-compatibility)|
|----|----|
|Title|Profile compatibility test|
|Description|A test meant to check whether the test subject is compatible with a profile or not, and if it is not, why.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-46)|Identifier|`owl-rl-profile-error`|
|[Section top](#minorfail-outcome-number-46)|Title|OWL RL Profile incompatible|
|[Section top](#minorfail-outcome-number-46)|Description|Class Expression not supported with rdfs:subClassOf|
|[Section top](#minorfail-outcome-number-46)|Pointer|<pre lang="Turtle"><code>coswot:PropertyValue a owl:Class ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;Property Value&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:comment &#34;Describes the value for a property. The property value is li...&#34; ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy &#60;https://w3id.org/coswot/core/property&lowbar;values> ;  &#10;&#32;&#32;&#32;&#32;rdfs:subClassOf &#91; a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:onProperty coswot:hasValue ],  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#91; a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:onProperty coswot:isMeasuredIn ] .</code></pre>|

***
### MinorFail Outcome number 47

[Jump to summary definition](#summary-MinorFail-47)	|	[Previous MinorFail outcome](#minorfail-outcome-number-46)	|	[Next MinorFail outcome](#minorfail-outcome-number-48)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-src-property-values-ontology|
|----|----|
|Title|Standalone module src/property&lowbar;values/ontology.ttl from branch main|
|Composition|- [Module property&lowbar;values/ontology](https://gitlab.com/coswot/coswot-acimov/blob/main/src/property_values/ontology.ttl)|

#### Criterion detail
|Identifier|[profile-compatibility](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#profile-compatibility)|
|----|----|
|Title|Profile compatibility test|
|Description|A test meant to check whether the test subject is compatible with a profile or not, and if it is not, why.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-47)|Identifier|`owl-rl-profile-error`|
|[Section top](#minorfail-outcome-number-47)|Title|OWL RL Profile incompatible|
|[Section top](#minorfail-outcome-number-47)|Description|Statement not supported in a Super Class Expression|
|[Section top](#minorfail-outcome-number-47)|Pointer|<pre lang="Turtle"><code>&#91;] a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;owl:onProperty coswot:hasValue .</code></pre>|
|[Section top](#minorfail-outcome-number-47)|Pointer|<pre lang="Turtle"><code>&#91;] a owl:Class ;  &#10;&#32;&#32;&#32;&#32;owl:unionOf ( coswot:Feature coswot:PropertyOfInterest ) .</code></pre>|

***
### MinorFail Outcome number 48

[Jump to summary definition](#summary-MinorFail-48)	|	[Previous MinorFail outcome](#minorfail-outcome-number-47)	|	[Next MinorFail outcome](#minorfail-outcome-number-49)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-src-property-values-ontology|
|----|----|
|Title|Standalone module src/property&lowbar;values/ontology.ttl from branch main|
|Composition|- [Module property&lowbar;values/ontology](https://gitlab.com/coswot/coswot-acimov/blob/main/src/property_values/ontology.ttl)|

#### Criterion detail
|Identifier|[profile-compatibility](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#profile-compatibility)|
|----|----|
|Title|Profile compatibility test|
|Description|A test meant to check whether the test subject is compatible with a profile or not, and if it is not, why.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-48)|Identifier|`owl-rl-profile-error`|
|[Section top](#minorfail-outcome-number-48)|Title|OWL RL Profile incompatible|
|[Section top](#minorfail-outcome-number-48)|Description|Class Expression not supported as object of rdfs:domain or rdfs:range|
|[Section top](#minorfail-outcome-number-48)|Pointer|<pre lang="Turtle"><code>coswot:hasPropertyValue a owl:ObjectProperty ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;has property value&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:comment &#34;Links a feature or a property of interest to a property valu...&#34; ;  &#10;&#32;&#32;&#32;&#32;rdfs:domain &#91; a owl:Class ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:unionOf ( coswot:Feature coswot:PropertyOfInterest ) ] ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy &#60;https://w3id.org/coswot/core/property&lowbar;values> ;  &#10;&#32;&#32;&#32;&#32;rdfs:range coswot:PropertyValue ;  &#10;&#32;&#32;&#32;&#32;owl:propertyChainAxiom ( skos:broader coswot:hasPropertyValue ) .</code></pre>|

***
### MinorFail Outcome number 49

[Jump to summary definition](#summary-MinorFail-49)	|	[Previous MinorFail outcome](#minorfail-outcome-number-48)	|	[Next MinorFail outcome](#minorfail-outcome-number-50)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-src-property-values-ontology|
|----|----|
|Title|Standalone module src/property&lowbar;values/ontology.ttl from branch main|
|Composition|- [Module property&lowbar;values/ontology](https://gitlab.com/coswot/coswot-acimov/blob/main/src/property_values/ontology.ttl)|

#### Criterion detail
|Identifier|[profile-compatibility](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#profile-compatibility)|
|----|----|
|Title|Profile compatibility test|
|Description|A test meant to check whether the test subject is compatible with a profile or not, and if it is not, why.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-49)|Identifier|`owl-ql-profile-error`|
|[Section top](#minorfail-outcome-number-49)|Title|OWL QL Profile incompatible|
|[Section top](#minorfail-outcome-number-49)|Description|Class Expression not supported with rdfs:subClassOf|
|[Section top](#minorfail-outcome-number-49)|Pointer|<pre lang="Turtle"><code>coswot:PropertyValue a owl:Class ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;Property Value&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:comment &#34;Describes the value for a property. The property value is li...&#34; ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy &#60;https://w3id.org/coswot/core/property&lowbar;values> ;  &#10;&#32;&#32;&#32;&#32;rdfs:subClassOf &#91; a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:onProperty coswot:hasValue ],  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#91; a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:onProperty coswot:isMeasuredIn ] .</code></pre>|

***
### MinorFail Outcome number 50

[Jump to summary definition](#summary-MinorFail-50)	|	[Previous MinorFail outcome](#minorfail-outcome-number-49)	|	[Next MinorFail outcome](#minorfail-outcome-number-51)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-src-property-values-ontology|
|----|----|
|Title|Standalone module src/property&lowbar;values/ontology.ttl from branch main|
|Composition|- [Module property&lowbar;values/ontology](https://gitlab.com/coswot/coswot-acimov/blob/main/src/property_values/ontology.ttl)|

#### Criterion detail
|Identifier|[profile-compatibility](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#profile-compatibility)|
|----|----|
|Title|Profile compatibility test|
|Description|A test meant to check whether the test subject is compatible with a profile or not, and if it is not, why.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-50)|Identifier|`owl-ql-profile-error`|
|[Section top](#minorfail-outcome-number-50)|Title|OWL QL Profile incompatible|
|[Section top](#minorfail-outcome-number-50)|Description|Statement not supported in a Super Class Expression|
|[Section top](#minorfail-outcome-number-50)|Pointer|<pre lang="Turtle"><code>&#91;] a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;owl:onProperty coswot:hasValue .</code></pre>|
|[Section top](#minorfail-outcome-number-50)|Pointer|<pre lang="Turtle"><code>&#91;] a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;owl:onProperty coswot:isMeasuredIn .</code></pre>|
|[Section top](#minorfail-outcome-number-50)|Pointer|<pre lang="Turtle"><code>&#91;] a owl:Class ;  &#10;&#32;&#32;&#32;&#32;owl:unionOf ( coswot:Feature coswot:PropertyOfInterest ) .</code></pre>|

***
### MinorFail Outcome number 51

[Jump to summary definition](#summary-MinorFail-51)	|	[Previous MinorFail outcome](#minorfail-outcome-number-50)	|	[Next MinorFail outcome](#minorfail-outcome-number-52)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-src-property-values-ontology|
|----|----|
|Title|Standalone module src/property&lowbar;values/ontology.ttl from branch main|
|Composition|- [Module property&lowbar;values/ontology](https://gitlab.com/coswot/coswot-acimov/blob/main/src/property_values/ontology.ttl)|

#### Criterion detail
|Identifier|[profile-compatibility](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#profile-compatibility)|
|----|----|
|Title|Profile compatibility test|
|Description|A test meant to check whether the test subject is compatible with a profile or not, and if it is not, why.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-51)|Identifier|`owl-ql-profile-error`|
|[Section top](#minorfail-outcome-number-51)|Title|OWL QL Profile incompatible|
|[Section top](#minorfail-outcome-number-51)|Description|Property inclusions involving property chains not supported|
|[Section top](#minorfail-outcome-number-51)|Pointer|<pre lang="Turtle"><code>coswot:isValueOfProperty a owl:ObjectProperty ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;is value of property&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:comment &#34;Links a property value to the property or property of intere...&#34; ;  &#10;&#32;&#32;&#32;&#32;rdfs:domain coswot:PropertyValue ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy &#60;https://w3id.org/coswot/core/property&lowbar;values> ;  &#10;&#32;&#32;&#32;&#32;rdfs:range coswot:Property ;  &#10;&#32;&#32;&#32;&#32;owl:propertyChainAxiom ( coswot:isValueOfProperty coswot:hasKind ) .</code></pre>|

***
### MinorFail Outcome number 52

[Jump to summary definition](#summary-MinorFail-52)	|	[Previous MinorFail outcome](#minorfail-outcome-number-51)	|	[Next MinorFail outcome](#minorfail-outcome-number-53)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-src-property-values-ontology|
|----|----|
|Title|Standalone module src/property&lowbar;values/ontology.ttl from branch main|
|Composition|- [Module property&lowbar;values/ontology](https://gitlab.com/coswot/coswot-acimov/blob/main/src/property_values/ontology.ttl)|

#### Criterion detail
|Identifier|[profile-compatibility](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#profile-compatibility)|
|----|----|
|Title|Profile compatibility test|
|Description|A test meant to check whether the test subject is compatible with a profile or not, and if it is not, why.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-52)|Identifier|`owl-ql-profile-error`|
|[Section top](#minorfail-outcome-number-52)|Title|OWL QL Profile incompatible|
|[Section top](#minorfail-outcome-number-52)|Description|Class Expression not supported as object of rdfs:domain or rdfs:range  &#10;Property inclusions involving property chains not supported|
|[Section top](#minorfail-outcome-number-52)|Pointer|<pre lang="Turtle"><code>coswot:hasPropertyValue a owl:ObjectProperty ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;has property value&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:comment &#34;Links a feature or a property of interest to a property valu...&#34; ;  &#10;&#32;&#32;&#32;&#32;rdfs:domain &#91; a owl:Class ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:unionOf ( coswot:Feature coswot:PropertyOfInterest ) ] ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy &#60;https://w3id.org/coswot/core/property&lowbar;values> ;  &#10;&#32;&#32;&#32;&#32;rdfs:range coswot:PropertyValue ;  &#10;&#32;&#32;&#32;&#32;owl:propertyChainAxiom ( skos:broader coswot:hasPropertyValue ) .</code></pre>|

***
### MinorFail Outcome number 53

[Jump to summary definition](#summary-MinorFail-53)	|	[Previous MinorFail outcome](#minorfail-outcome-number-52)	|	[Next MinorFail outcome](#minorfail-outcome-number-54)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-src-property-values-ontology|
|----|----|
|Title|Standalone module src/property&lowbar;values/ontology.ttl from branch main|
|Composition|- [Module property&lowbar;values/ontology](https://gitlab.com/coswot/coswot-acimov/blob/main/src/property_values/ontology.ttl)|

#### Criterion detail
|Identifier|[profile-compatibility](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#profile-compatibility)|
|----|----|
|Title|Profile compatibility test|
|Description|A test meant to check whether the test subject is compatible with a profile or not, and if it is not, why.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-53)|Identifier|`owl-el-profile-error`|
|[Section top](#minorfail-outcome-number-53)|Title|OWL EL Profile incompatible|
|[Section top](#minorfail-outcome-number-53)|Description|Statement not supported in a Class Expression|
|[Section top](#minorfail-outcome-number-53)|Pointer|<pre lang="Turtle"><code>&#91;] a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;owl:onProperty coswot:hasValue .</code></pre>|
|[Section top](#minorfail-outcome-number-53)|Pointer|<pre lang="Turtle"><code>&#91;] a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;owl:onProperty coswot:isMeasuredIn .</code></pre>|
|[Section top](#minorfail-outcome-number-53)|Pointer|<pre lang="Turtle"><code>&#91;] a owl:Class ;  &#10;&#32;&#32;&#32;&#32;owl:unionOf ( coswot:Feature coswot:PropertyOfInterest ) .</code></pre>|

***
### MinorFail Outcome number 54

[Jump to summary definition](#summary-MinorFail-54)	|	[Previous MinorFail outcome](#minorfail-outcome-number-53)	|	[Next MinorFail outcome](#minorfail-outcome-number-55)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-src-property-values-ontology|
|----|----|
|Title|Standalone module src/property&lowbar;values/ontology.ttl from branch main|
|Composition|- [Module property&lowbar;values/ontology](https://gitlab.com/coswot/coswot-acimov/blob/main/src/property_values/ontology.ttl)|

#### Criterion detail
|Identifier|[profile-compatibility](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#profile-compatibility)|
|----|----|
|Title|Profile compatibility test|
|Description|A test meant to check whether the test subject is compatible with a profile or not, and if it is not, why.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-54)|Identifier|`owl-el-profile-error`|
|[Section top](#minorfail-outcome-number-54)|Title|OWL EL Profile incompatible|
|[Section top](#minorfail-outcome-number-54)|Description|Class Expression not supported as object of rdfs:domain or rdfs:range|
|[Section top](#minorfail-outcome-number-54)|Pointer|<pre lang="Turtle"><code>coswot:hasPropertyValue a owl:ObjectProperty ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;has property value&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:comment &#34;Links a feature or a property of interest to a property valu...&#34; ;  &#10;&#32;&#32;&#32;&#32;rdfs:domain &#91; a owl:Class ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:unionOf ( coswot:Feature coswot:PropertyOfInterest ) ] ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy &#60;https://w3id.org/coswot/core/property&lowbar;values> ;  &#10;&#32;&#32;&#32;&#32;rdfs:range coswot:PropertyValue ;  &#10;&#32;&#32;&#32;&#32;owl:propertyChainAxiom ( skos:broader coswot:hasPropertyValue ) .</code></pre>|

***
### MinorFail Outcome number 55

[Jump to summary definition](#summary-MinorFail-55)	|	[Previous MinorFail outcome](#minorfail-outcome-number-54)	|	[Next MinorFail outcome](#minorfail-outcome-number-56)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-src-property-values-ontology|
|----|----|
|Title|Standalone module src/property&lowbar;values/ontology.ttl from branch main|
|Composition|- [Module property&lowbar;values/ontology](https://gitlab.com/coswot/coswot-acimov/blob/main/src/property_values/ontology.ttl)|

#### Criterion detail
|Identifier|[profile-compatibility](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#profile-compatibility)|
|----|----|
|Title|Profile compatibility test|
|Description|A test meant to check whether the test subject is compatible with a profile or not, and if it is not, why.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-55)|Identifier|`owl-el-profile-error`|
|[Section top](#minorfail-outcome-number-55)|Title|OWL EL Profile incompatible|
|[Section top](#minorfail-outcome-number-55)|Description|Class Expression not supported with rdfs:subClassOf|
|[Section top](#minorfail-outcome-number-55)|Pointer|<pre lang="Turtle"><code>coswot:PropertyValue a owl:Class ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;Property Value&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:comment &#34;Describes the value for a property. The property value is li...&#34; ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy &#60;https://w3id.org/coswot/core/property&lowbar;values> ;  &#10;&#32;&#32;&#32;&#32;rdfs:subClassOf &#91; a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:onProperty coswot:hasValue ],  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#91; a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:onProperty coswot:isMeasuredIn ] .</code></pre>|

***
### MinorFail Outcome number 56

[Jump to summary definition](#summary-MinorFail-56)	|	[Previous MinorFail outcome](#minorfail-outcome-number-55)	|	[Next MinorFail outcome](#minorfail-outcome-number-57)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-src-properties-ontology-catalogs|
|----|----|
|Title|Standalone module src/properties/ontology.catalogs.ttl from branch main|
|Composition|- [Module properties/ontology.catalogs](https://gitlab.com/coswot/coswot-acimov/blob/main/src/properties/ontology.catalogs.ttl)|

#### Criterion detail
|Identifier|[domain-and-range-referencing](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#domain-and-range-referencing)|
|----|----|
|Title|Domain and range referencing test|
|Description|A test case from the Best Practices tests checking if all the ranges and domains from the test subject point to terms that are defined in the vocabulary.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-56)|Identifier|`domain-out-of-vocabulary`|
|[Section top](#minorfail-outcome-number-56)|Title|Domain out of vocabulary|
|[Section top](#minorfail-outcome-number-56)|Description|Some properties have a domain out of the ontology|
|[Section top](#minorfail-outcome-number-56)|Pointer|<pre lang="Turtle"><code>:isPropertyOf a owl:ObjectProperty ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;is property of&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:comment &#34;Links a property to the feature it is a property of.&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:domain &#91; a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:allValuesFrom :PropertyKind ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:onProperty skos:broader ],  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#91; a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:allValuesFrom :PropertyKind ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:onProperty skos:narrower ],  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:Thing,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;skos:Concept,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;:PropertyKind ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy &#60;https://w3id.org/coswot/core/properties> ;  &#10;&#32;&#32;&#32;&#32;rdfs:subPropertyOf :isPropertyOf ;  &#10;&#32;&#32;&#32;&#32;owl:equivalentProperty :isPropertyOf ;  &#10;&#32;&#32;&#32;&#32;owl:inverseOf :hasProperty .</code></pre>|
|[Section top](#minorfail-outcome-number-56)|Pointer|http://www.w3.org/2004/02/skos/core#Concept|

***
### MinorFail Outcome number 57

[Jump to summary definition](#summary-MinorFail-57)	|	[Previous MinorFail outcome](#minorfail-outcome-number-56)	|	[Next MinorFail outcome](#minorfail-outcome-number-58)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-src-properties-ontology-catalogs|
|----|----|
|Title|Standalone module src/properties/ontology.catalogs.ttl from branch main|
|Composition|- [Module properties/ontology.catalogs](https://gitlab.com/coswot/coswot-acimov/blob/main/src/properties/ontology.catalogs.ttl)|

#### Criterion detail
|Identifier|[domain-and-range-referencing](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#domain-and-range-referencing)|
|----|----|
|Title|Domain and range referencing test|
|Description|A test case from the Best Practices tests checking if all the ranges and domains from the test subject point to terms that are defined in the vocabulary.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-57)|Identifier|`range-out-of-vocabulary`|
|[Section top](#minorfail-outcome-number-57)|Title|Range out of vocabulary|
|[Section top](#minorfail-outcome-number-57)|Description|Some properties have a range out of the ontology|
|[Section top](#minorfail-outcome-number-57)|Pointer|<pre lang="Turtle"><code>:hasProperty a owl:ObjectProperty ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;has property&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:comment &#34;Links a feature to one of its properties.&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy &#60;https://w3id.org/coswot/core/properties> ;  &#10;&#32;&#32;&#32;&#32;rdfs:range &#91; a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:allValuesFrom :PropertyKind ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:onProperty skos:broader ],  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#91; a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:allValuesFrom :PropertyKind ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:onProperty skos:narrower ],  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:Thing,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;skos:Concept,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;:PropertyKind ;  &#10;&#32;&#32;&#32;&#32;rdfs:subPropertyOf :hasProperty ;  &#10;&#32;&#32;&#32;&#32;owl:equivalentProperty :hasProperty ;  &#10;&#32;&#32;&#32;&#32;owl:inverseOf :isPropertyOf ;  &#10;&#32;&#32;&#32;&#32;owl:propertyChainAxiom ( skos:broader :hasProperty ) .</code></pre>|
|[Section top](#minorfail-outcome-number-57)|Pointer|http://www.w3.org/2004/02/skos/core#Concept|

***
### MinorFail Outcome number 58

[Jump to summary definition](#summary-MinorFail-58)	|	[Previous MinorFail outcome](#minorfail-outcome-number-57)	|	[Next MinorFail outcome](#minorfail-outcome-number-59)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-src-properties-ontology-catalogs|
|----|----|
|Title|Standalone module src/properties/ontology.catalogs.ttl from branch main|
|Composition|- [Module properties/ontology.catalogs](https://gitlab.com/coswot/coswot-acimov/blob/main/src/properties/ontology.catalogs.ttl)|

#### Criterion detail
|Identifier|[profile-compatibility](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#profile-compatibility)|
|----|----|
|Title|Profile compatibility test|
|Description|A test meant to check whether the test subject is compatible with a profile or not, and if it is not, why.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-58)|Identifier|`owl-ql-profile-error`|
|[Section top](#minorfail-outcome-number-58)|Title|OWL QL Profile incompatible|
|[Section top](#minorfail-outcome-number-58)|Description|Class Expression not supported with rdfs:subClassOf|
|[Section top](#minorfail-outcome-number-58)|Pointer|<pre lang="Turtle"><code>coswot:PropertyKind a owl:Class ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;Property Kind&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:comment &#34;Identifiable qualities of features of interest that can be t...&#34; ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy &#60;https://w3id.org/coswot/core/properties> ;  &#10;&#32;&#32;&#32;&#32;rdfs:subClassOf &#91; a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:allValuesFrom coswot:PropertyKind ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:onProperty skos:broader ],  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#91; a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:allValuesFrom coswot:PropertyKind ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:onProperty skos:narrower ],  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;skos:Concept ;  &#10;&#32;&#32;&#32;&#32;skos:example &#34;Air temperature, pressure, luminance, etc. are all property ...&#34;,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#34;Two examples using the QUDT Quantity Kind vocabulary, and th...&#34; ;  &#10;&#32;&#32;&#32;&#32;skos:note &#34;Concepts from existing code lists, vocabularies, and taxonom...&#34; .</code></pre>|

***
### MinorFail Outcome number 59

[Jump to summary definition](#summary-MinorFail-59)	|	[Previous MinorFail outcome](#minorfail-outcome-number-58)	|	[Next MinorFail outcome](#minorfail-outcome-number-60)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-src-properties-ontology-catalogs|
|----|----|
|Title|Standalone module src/properties/ontology.catalogs.ttl from branch main|
|Composition|- [Module properties/ontology.catalogs](https://gitlab.com/coswot/coswot-acimov/blob/main/src/properties/ontology.catalogs.ttl)|

#### Criterion detail
|Identifier|[profile-compatibility](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#profile-compatibility)|
|----|----|
|Title|Profile compatibility test|
|Description|A test meant to check whether the test subject is compatible with a profile or not, and if it is not, why.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-59)|Identifier|`owl-ql-profile-error`|
|[Section top](#minorfail-outcome-number-59)|Title|OWL QL Profile incompatible|
|[Section top](#minorfail-outcome-number-59)|Description|Statement not supported in a Super Class Expression|
|[Section top](#minorfail-outcome-number-59)|Pointer|<pre lang="Turtle"><code>&#91;] a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;owl:allValuesFrom coswot:PropertyKind ;  &#10;&#32;&#32;&#32;&#32;owl:onProperty skos:broader .</code></pre>|
|[Section top](#minorfail-outcome-number-59)|Pointer|<pre lang="Turtle"><code>&#91;] a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;owl:allValuesFrom coswot:PropertyKind ;  &#10;&#32;&#32;&#32;&#32;owl:onProperty skos:narrower .</code></pre>|

***
### MinorFail Outcome number 60

[Jump to summary definition](#summary-MinorFail-60)	|	[Previous MinorFail outcome](#minorfail-outcome-number-59)	|	[Next MinorFail outcome](#minorfail-outcome-number-61)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-src-properties-ontology-catalogs|
|----|----|
|Title|Standalone module src/properties/ontology.catalogs.ttl from branch main|
|Composition|- [Module properties/ontology.catalogs](https://gitlab.com/coswot/coswot-acimov/blob/main/src/properties/ontology.catalogs.ttl)|

#### Criterion detail
|Identifier|[profile-compatibility](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#profile-compatibility)|
|----|----|
|Title|Profile compatibility test|
|Description|A test meant to check whether the test subject is compatible with a profile or not, and if it is not, why.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-60)|Identifier|`owl-ql-profile-error`|
|[Section top](#minorfail-outcome-number-60)|Title|OWL QL Profile incompatible|
|[Section top](#minorfail-outcome-number-60)|Description|Property inclusions involving property chains not supported|
|[Section top](#minorfail-outcome-number-60)|Pointer|<pre lang="Turtle"><code>coswot:hasProperty a owl:ObjectProperty ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;has property&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:comment &#34;Links a feature to one of its properties.&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy &#60;https://w3id.org/coswot/core/properties> ;  &#10;&#32;&#32;&#32;&#32;rdfs:range coswot:PropertyKind ;  &#10;&#32;&#32;&#32;&#32;owl:inverseOf coswot:isPropertyOf ;  &#10;&#32;&#32;&#32;&#32;owl:propertyChainAxiom ( skos:broader coswot:hasProperty ) .</code></pre>|

***
### MinorFail Outcome number 61

[Jump to summary definition](#summary-MinorFail-61)	|	[Previous MinorFail outcome](#minorfail-outcome-number-60)	|	[Next MinorFail outcome](#minorfail-outcome-number-62)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-src-properties-ontology-catalogs|
|----|----|
|Title|Standalone module src/properties/ontology.catalogs.ttl from branch main|
|Composition|- [Module properties/ontology.catalogs](https://gitlab.com/coswot/coswot-acimov/blob/main/src/properties/ontology.catalogs.ttl)|

#### Criterion detail
|Identifier|[profile-compatibility](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#profile-compatibility)|
|----|----|
|Title|Profile compatibility test|
|Description|A test meant to check whether the test subject is compatible with a profile or not, and if it is not, why.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-61)|Identifier|`owl-el-profile-error`|
|[Section top](#minorfail-outcome-number-61)|Title|OWL EL Profile incompatible|
|[Section top](#minorfail-outcome-number-61)|Description|Statement not supported in a Class Expression|
|[Section top](#minorfail-outcome-number-61)|Pointer|<pre lang="Turtle"><code>&#91;] a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;owl:allValuesFrom coswot:PropertyKind ;  &#10;&#32;&#32;&#32;&#32;owl:onProperty skos:broader .</code></pre>|
|[Section top](#minorfail-outcome-number-61)|Pointer|<pre lang="Turtle"><code>&#91;] a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;owl:allValuesFrom coswot:PropertyKind ;  &#10;&#32;&#32;&#32;&#32;owl:onProperty skos:narrower .</code></pre>|

***
### MinorFail Outcome number 62

[Jump to summary definition](#summary-MinorFail-62)	|	[Previous MinorFail outcome](#minorfail-outcome-number-61)	|	[Next MinorFail outcome](#minorfail-outcome-number-63)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-src-properties-ontology-catalogs|
|----|----|
|Title|Standalone module src/properties/ontology.catalogs.ttl from branch main|
|Composition|- [Module properties/ontology.catalogs](https://gitlab.com/coswot/coswot-acimov/blob/main/src/properties/ontology.catalogs.ttl)|

#### Criterion detail
|Identifier|[profile-compatibility](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#profile-compatibility)|
|----|----|
|Title|Profile compatibility test|
|Description|A test meant to check whether the test subject is compatible with a profile or not, and if it is not, why.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-62)|Identifier|`owl-el-profile-error`|
|[Section top](#minorfail-outcome-number-62)|Title|OWL EL Profile incompatible|
|[Section top](#minorfail-outcome-number-62)|Description|Class Expression not supported with rdfs:subClassOf|
|[Section top](#minorfail-outcome-number-62)|Pointer|<pre lang="Turtle"><code>coswot:PropertyKind a owl:Class ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;Property Kind&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:comment &#34;Identifiable qualities of features of interest that can be t...&#34; ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy &#60;https://w3id.org/coswot/core/properties> ;  &#10;&#32;&#32;&#32;&#32;rdfs:subClassOf &#91; a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:allValuesFrom coswot:PropertyKind ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:onProperty skos:broader ],  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#91; a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:allValuesFrom coswot:PropertyKind ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:onProperty skos:narrower ],  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;skos:Concept ;  &#10;&#32;&#32;&#32;&#32;skos:example &#34;Air temperature, pressure, luminance, etc. are all property ...&#34;,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#34;Two examples using the QUDT Quantity Kind vocabulary, and th...&#34; ;  &#10;&#32;&#32;&#32;&#32;skos:note &#34;Concepts from existing code lists, vocabularies, and taxonom...&#34; .</code></pre>|

***
### MinorFail Outcome number 63

[Jump to summary definition](#summary-MinorFail-63)	|	[Previous MinorFail outcome](#minorfail-outcome-number-62)	|	[Next MinorFail outcome](#minorfail-outcome-number-64)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-src-properties-ontology|
|----|----|
|Title|Standalone module src/properties/ontology.ttl from branch main|
|Composition|- [Module properties/ontology](https://gitlab.com/coswot/coswot-acimov/blob/main/src/properties/ontology.ttl)|

#### Criterion detail
|Identifier|[domain-and-range-referencing](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#domain-and-range-referencing)|
|----|----|
|Title|Domain and range referencing test|
|Description|A test case from the Best Practices tests checking if all the ranges and domains from the test subject point to terms that are defined in the vocabulary.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-63)|Identifier|`domain-out-of-vocabulary`|
|[Section top](#minorfail-outcome-number-63)|Title|Domain out of vocabulary|
|[Section top](#minorfail-outcome-number-63)|Description|Some properties have a domain out of the ontology|
|[Section top](#minorfail-outcome-number-63)|Pointer|<pre lang="Turtle"><code>:isPropertyOf a owl:ObjectProperty ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;is property of&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:comment &#34;Links a property kind to the feature it is a property of.&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:domain &#91; a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:allValuesFrom :PropertyKind ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:onProperty skos:broader ],  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#91; a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:allValuesFrom :PropertyKind ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:onProperty skos:narrower ],  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#91; a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;rdfs:subClassOf &lowbar;:n073e6fe2a8b3457397218b41e359babeb4 ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:allValuesFrom owl:Nothing ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:onProperty :hasKind ],  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&lowbar;:n073e6fe2a8b3457397218b41e359babeb4,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:Thing,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;skos:Concept,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;:Property,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;:PropertyKind ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy &#60;https://w3id.org/coswot/core/properties> ;  &#10;&#32;&#32;&#32;&#32;rdfs:range :Feature ;  &#10;&#32;&#32;&#32;&#32;rdfs:subPropertyOf :isPropertyOf ;  &#10;&#32;&#32;&#32;&#32;owl:equivalentProperty :isPropertyOf ;  &#10;&#32;&#32;&#32;&#32;owl:inverseOf :hasProperty .  &#10;&lowbar;:n073e6fe2a8b3457397218b41e359babeb4 a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;owl:allValuesFrom :PropertyKind ;  &#10;&#32;&#32;&#32;&#32;owl:onProperty :hasKind .</code></pre>|
|[Section top](#minorfail-outcome-number-63)|Pointer|http://www.w3.org/2004/02/skos/core#Concept|

***
### MinorFail Outcome number 64

[Jump to summary definition](#summary-MinorFail-64)	|	[Previous MinorFail outcome](#minorfail-outcome-number-63)	|	[Next MinorFail outcome](#minorfail-outcome-number-65)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-src-properties-ontology|
|----|----|
|Title|Standalone module src/properties/ontology.ttl from branch main|
|Composition|- [Module properties/ontology](https://gitlab.com/coswot/coswot-acimov/blob/main/src/properties/ontology.ttl)|

#### Criterion detail
|Identifier|[domain-and-range-referencing](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#domain-and-range-referencing)|
|----|----|
|Title|Domain and range referencing test|
|Description|A test case from the Best Practices tests checking if all the ranges and domains from the test subject point to terms that are defined in the vocabulary.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-64)|Identifier|`range-out-of-vocabulary`|
|[Section top](#minorfail-outcome-number-64)|Title|Range out of vocabulary|
|[Section top](#minorfail-outcome-number-64)|Description|Some properties have a range out of the ontology|
|[Section top](#minorfail-outcome-number-64)|Pointer|<pre lang="Turtle"><code>:hasProperty a owl:ObjectProperty ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;has property&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:comment &#34;Links a feature to one of its property kinds.&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:domain :Feature ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy &#60;https://w3id.org/coswot/core/properties> ;  &#10;&#32;&#32;&#32;&#32;rdfs:range &#91; a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:allValuesFrom :PropertyKind ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:onProperty skos:broader ],  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#91; a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:allValuesFrom :PropertyKind ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:onProperty skos:narrower ],  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#91; a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;rdfs:subClassOf &lowbar;:n5e5b0a9f57d84b85b42427ddcc3082e2b4 ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:allValuesFrom owl:Nothing ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:onProperty :hasKind ],  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&lowbar;:n5e5b0a9f57d84b85b42427ddcc3082e2b4,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:Thing,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;skos:Concept,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;:Property,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;:PropertyKind ;  &#10;&#32;&#32;&#32;&#32;rdfs:subPropertyOf :hasProperty ;  &#10;&#32;&#32;&#32;&#32;owl:equivalentProperty :hasProperty ;  &#10;&#32;&#32;&#32;&#32;owl:inverseOf :isPropertyOf ;  &#10;&#32;&#32;&#32;&#32;owl:propertyChainAxiom ( skos:broader :hasProperty ),  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;( :hasKind :hasProperty ),  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;( :hasPropertyOfInterest :hasKind ) .  &#10;&lowbar;:n5e5b0a9f57d84b85b42427ddcc3082e2b4 a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;owl:allValuesFrom :PropertyKind ;  &#10;&#32;&#32;&#32;&#32;owl:onProperty :hasKind .</code></pre>|
|[Section top](#minorfail-outcome-number-64)|Pointer|http://www.w3.org/2004/02/skos/core#Concept|

***
### MinorFail Outcome number 65

[Jump to summary definition](#summary-MinorFail-65)	|	[Previous MinorFail outcome](#minorfail-outcome-number-64)	|	[Next MinorFail outcome](#minorfail-outcome-number-66)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-src-properties-ontology|
|----|----|
|Title|Standalone module src/properties/ontology.ttl from branch main|
|Composition|- [Module properties/ontology](https://gitlab.com/coswot/coswot-acimov/blob/main/src/properties/ontology.ttl)|

#### Criterion detail
|Identifier|[profile-compatibility](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#profile-compatibility)|
|----|----|
|Title|Profile compatibility test|
|Description|A test meant to check whether the test subject is compatible with a profile or not, and if it is not, why.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-65)|Identifier|`owl-rl-profile-error`|
|[Section top](#minorfail-outcome-number-65)|Title|OWL RL Profile incompatible|
|[Section top](#minorfail-outcome-number-65)|Description|Class Expression not supported with rdfs:subClassOf|
|[Section top](#minorfail-outcome-number-65)|Pointer|<pre lang="Turtle"><code>coswot:PropertyOfInterest a owl:Class ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;Property of Interest&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:comment &#34;Identifiable qualities of features of interest that can be o...&#34; ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy &#60;https://w3id.org/coswot/core/properties> ;  &#10;&#32;&#32;&#32;&#32;rdfs:subClassOf &#91; a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:allValuesFrom coswot:PropertyKind ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:onProperty coswot:hasKind ],  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#91; a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:onProperty coswot:hasKind ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:someValuesFrom coswot:PropertyKind ],  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#91; a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:onProperty coswot:isPropertyOfInterestOf ],  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;coswot:Property ;  &#10;&#32;&#32;&#32;&#32;skos:example &#34;The air temperature of the atmosphere sample at a certain lo...&#34; ;  &#10;&#32;&#32;&#32;&#32;skos:note &#34;A property of interest is the property of (OP coswot:isPrope...&#34;,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#34;Per convention, the IRI of properties of interest should con...&#34;,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#34;Properties of interest need not always be explicited. It dep...&#34; .</code></pre>|

***
### MinorFail Outcome number 66

[Jump to summary definition](#summary-MinorFail-66)	|	[Previous MinorFail outcome](#minorfail-outcome-number-65)	|	[Next MinorFail outcome](#minorfail-outcome-number-67)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-src-properties-ontology|
|----|----|
|Title|Standalone module src/properties/ontology.ttl from branch main|
|Composition|- [Module properties/ontology](https://gitlab.com/coswot/coswot-acimov/blob/main/src/properties/ontology.ttl)|

#### Criterion detail
|Identifier|[profile-compatibility](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#profile-compatibility)|
|----|----|
|Title|Profile compatibility test|
|Description|A test meant to check whether the test subject is compatible with a profile or not, and if it is not, why.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-66)|Identifier|`owl-rl-profile-error`|
|[Section top](#minorfail-outcome-number-66)|Title|OWL RL Profile incompatible|
|[Section top](#minorfail-outcome-number-66)|Description|Statement not supported|
|[Section top](#minorfail-outcome-number-66)|Pointer|<pre lang="Turtle"><code>coswot:Property a owl:Class ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;Property&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:comment &#34;Identifiable qualities of features that can be observed or c...&#34; ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy &#60;https://w3id.org/coswot/core/properties> ;  &#10;&#32;&#32;&#32;&#32;owl:disjointUnionOf ( coswot:PropertyOfInterest coswot:PropertyKind ) .</code></pre>|

***
### MinorFail Outcome number 67

[Jump to summary definition](#summary-MinorFail-67)	|	[Previous MinorFail outcome](#minorfail-outcome-number-66)	|	[Next MinorFail outcome](#minorfail-outcome-number-68)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-src-properties-ontology|
|----|----|
|Title|Standalone module src/properties/ontology.ttl from branch main|
|Composition|- [Module properties/ontology](https://gitlab.com/coswot/coswot-acimov/blob/main/src/properties/ontology.ttl)|

#### Criterion detail
|Identifier|[profile-compatibility](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#profile-compatibility)|
|----|----|
|Title|Profile compatibility test|
|Description|A test meant to check whether the test subject is compatible with a profile or not, and if it is not, why.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-67)|Identifier|`owl-rl-profile-error`|
|[Section top](#minorfail-outcome-number-67)|Title|OWL RL Profile incompatible|
|[Section top](#minorfail-outcome-number-67)|Description|Statement not supported in a Super Class Expression|
|[Section top](#minorfail-outcome-number-67)|Pointer|<pre lang="Turtle"><code>&#91;] a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;owl:onProperty coswot:hasKind ;  &#10;&#32;&#32;&#32;&#32;owl:someValuesFrom coswot:PropertyKind .</code></pre>|
|[Section top](#minorfail-outcome-number-67)|Pointer|<pre lang="Turtle"><code>&#91;] a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;owl:onProperty coswot:isPropertyOfInterestOf .</code></pre>|

***
### MinorFail Outcome number 68

[Jump to summary definition](#summary-MinorFail-68)	|	[Previous MinorFail outcome](#minorfail-outcome-number-67)	|	[Next MinorFail outcome](#minorfail-outcome-number-69)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-src-properties-ontology|
|----|----|
|Title|Standalone module src/properties/ontology.ttl from branch main|
|Composition|- [Module properties/ontology](https://gitlab.com/coswot/coswot-acimov/blob/main/src/properties/ontology.ttl)|

#### Criterion detail
|Identifier|[profile-compatibility](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#profile-compatibility)|
|----|----|
|Title|Profile compatibility test|
|Description|A test meant to check whether the test subject is compatible with a profile or not, and if it is not, why.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-68)|Identifier|`owl-ql-profile-error`|
|[Section top](#minorfail-outcome-number-68)|Title|OWL QL Profile incompatible|
|[Section top](#minorfail-outcome-number-68)|Description|Class Expression not supported with rdfs:subClassOf|
|[Section top](#minorfail-outcome-number-68)|Pointer|<pre lang="Turtle"><code>coswot:PropertyKind a owl:Class ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;Property Kind&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:comment &#34;Identifiable qualities of features that can be observed or c...&#34; ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy &#60;https://w3id.org/coswot/core/properties> ;  &#10;&#32;&#32;&#32;&#32;rdfs:subClassOf &#91; a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:allValuesFrom coswot:PropertyKind ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:onProperty skos:broader ],  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#91; a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:allValuesFrom coswot:PropertyKind ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:onProperty skos:narrower ],  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#91; a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:allValuesFrom owl:Nothing ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:onProperty coswot:hasKind ],  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;skos:Concept,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;coswot:Property ;  &#10;&#32;&#32;&#32;&#32;skos:example &#34;Air temperature, pressure, luminance, etc. are all property ...&#34;,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#34;Two examples using the QUDT Quantity Kind vocabulary, and th...&#34; ;  &#10;&#32;&#32;&#32;&#32;skos:note &#34;Concepts from existing code lists, vocabularies, and taxonom...&#34; .</code></pre>|
|[Section top](#minorfail-outcome-number-68)|Pointer|<pre lang="Turtle"><code>coswot:PropertyOfInterest a owl:Class ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;Property of Interest&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:comment &#34;Identifiable qualities of features of interest that can be o...&#34; ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy &#60;https://w3id.org/coswot/core/properties> ;  &#10;&#32;&#32;&#32;&#32;rdfs:subClassOf &#91; a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:allValuesFrom coswot:PropertyKind ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:onProperty coswot:hasKind ],  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#91; a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:onProperty coswot:hasKind ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:someValuesFrom coswot:PropertyKind ],  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#91; a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:onProperty coswot:isPropertyOfInterestOf ],  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;coswot:Property ;  &#10;&#32;&#32;&#32;&#32;skos:example &#34;The air temperature of the atmosphere sample at a certain lo...&#34; ;  &#10;&#32;&#32;&#32;&#32;skos:note &#34;A property of interest is the property of (OP coswot:isPrope...&#34;,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#34;Per convention, the IRI of properties of interest should con...&#34;,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#34;Properties of interest need not always be explicited. It dep...&#34; .</code></pre>|

***
### MinorFail Outcome number 69

[Jump to summary definition](#summary-MinorFail-69)	|	[Previous MinorFail outcome](#minorfail-outcome-number-68)	|	[Next MinorFail outcome](#minorfail-outcome-number-70)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-src-properties-ontology|
|----|----|
|Title|Standalone module src/properties/ontology.ttl from branch main|
|Composition|- [Module properties/ontology](https://gitlab.com/coswot/coswot-acimov/blob/main/src/properties/ontology.ttl)|

#### Criterion detail
|Identifier|[profile-compatibility](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#profile-compatibility)|
|----|----|
|Title|Profile compatibility test|
|Description|A test meant to check whether the test subject is compatible with a profile or not, and if it is not, why.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-69)|Identifier|`owl-ql-profile-error`|
|[Section top](#minorfail-outcome-number-69)|Title|OWL QL Profile incompatible|
|[Section top](#minorfail-outcome-number-69)|Description|Statement not supported|
|[Section top](#minorfail-outcome-number-69)|Pointer|<pre lang="Turtle"><code>coswot:Property a owl:Class ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;Property&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:comment &#34;Identifiable qualities of features that can be observed or c...&#34; ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy &#60;https://w3id.org/coswot/core/properties> ;  &#10;&#32;&#32;&#32;&#32;owl:disjointUnionOf ( coswot:PropertyOfInterest coswot:PropertyKind ) .</code></pre>|

***
### MinorFail Outcome number 70

[Jump to summary definition](#summary-MinorFail-70)	|	[Previous MinorFail outcome](#minorfail-outcome-number-69)	|	[Next MinorFail outcome](#minorfail-outcome-number-71)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-src-properties-ontology|
|----|----|
|Title|Standalone module src/properties/ontology.ttl from branch main|
|Composition|- [Module properties/ontology](https://gitlab.com/coswot/coswot-acimov/blob/main/src/properties/ontology.ttl)|

#### Criterion detail
|Identifier|[profile-compatibility](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#profile-compatibility)|
|----|----|
|Title|Profile compatibility test|
|Description|A test meant to check whether the test subject is compatible with a profile or not, and if it is not, why.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-70)|Identifier|`owl-ql-profile-error`|
|[Section top](#minorfail-outcome-number-70)|Title|OWL QL Profile incompatible|
|[Section top](#minorfail-outcome-number-70)|Description|Statement not supported in a Super Class Expression|
|[Section top](#minorfail-outcome-number-70)|Pointer|<pre lang="Turtle"><code>&#91;] a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;owl:allValuesFrom coswot:PropertyKind ;  &#10;&#32;&#32;&#32;&#32;owl:onProperty skos:broader .</code></pre>|
|[Section top](#minorfail-outcome-number-70)|Pointer|<pre lang="Turtle"><code>&#91;] a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;owl:allValuesFrom coswot:PropertyKind ;  &#10;&#32;&#32;&#32;&#32;owl:onProperty skos:narrower .</code></pre>|
|[Section top](#minorfail-outcome-number-70)|Pointer|<pre lang="Turtle"><code>&#91;] a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;owl:allValuesFrom owl:Nothing ;  &#10;&#32;&#32;&#32;&#32;owl:onProperty coswot:hasKind .</code></pre>|
|[Section top](#minorfail-outcome-number-70)|Pointer|<pre lang="Turtle"><code>&#91;] a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;owl:allValuesFrom coswot:PropertyKind ;  &#10;&#32;&#32;&#32;&#32;owl:onProperty coswot:hasKind .</code></pre>|
|[Section top](#minorfail-outcome-number-70)|Pointer|<pre lang="Turtle"><code>&#91;] a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;owl:onProperty coswot:isPropertyOfInterestOf .</code></pre>|

***
### MinorFail Outcome number 71

[Jump to summary definition](#summary-MinorFail-71)	|	[Previous MinorFail outcome](#minorfail-outcome-number-70)	|	[Next MinorFail outcome](#minorfail-outcome-number-72)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-src-properties-ontology|
|----|----|
|Title|Standalone module src/properties/ontology.ttl from branch main|
|Composition|- [Module properties/ontology](https://gitlab.com/coswot/coswot-acimov/blob/main/src/properties/ontology.ttl)|

#### Criterion detail
|Identifier|[profile-compatibility](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#profile-compatibility)|
|----|----|
|Title|Profile compatibility test|
|Description|A test meant to check whether the test subject is compatible with a profile or not, and if it is not, why.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-71)|Identifier|`owl-ql-profile-error`|
|[Section top](#minorfail-outcome-number-71)|Title|OWL QL Profile incompatible|
|[Section top](#minorfail-outcome-number-71)|Description|Property inclusions involving property chains not supported|
|[Section top](#minorfail-outcome-number-71)|Pointer|<pre lang="Turtle"><code>coswot:hasProperty a owl:ObjectProperty ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;has property&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:comment &#34;Links a feature to one of its property kinds.&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:domain coswot:Feature ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy &#60;https://w3id.org/coswot/core/properties> ;  &#10;&#32;&#32;&#32;&#32;rdfs:range coswot:PropertyKind ;  &#10;&#32;&#32;&#32;&#32;owl:inverseOf coswot:isPropertyOf ;  &#10;&#32;&#32;&#32;&#32;owl:propertyChainAxiom ( skos:broader coswot:hasProperty ),  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;( coswot:hasKind coswot:hasProperty ),  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;( coswot:hasPropertyOfInterest coswot:hasKind ) .</code></pre>|

***
### MinorFail Outcome number 72

[Jump to summary definition](#summary-MinorFail-72)	|	[Previous MinorFail outcome](#minorfail-outcome-number-71)	|	[Next MinorFail outcome](#minorfail-outcome-number-73)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-src-properties-ontology|
|----|----|
|Title|Standalone module src/properties/ontology.ttl from branch main|
|Composition|- [Module properties/ontology](https://gitlab.com/coswot/coswot-acimov/blob/main/src/properties/ontology.ttl)|

#### Criterion detail
|Identifier|[profile-compatibility](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#profile-compatibility)|
|----|----|
|Title|Profile compatibility test|
|Description|A test meant to check whether the test subject is compatible with a profile or not, and if it is not, why.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-72)|Identifier|`owl-el-profile-error`|
|[Section top](#minorfail-outcome-number-72)|Title|OWL EL Profile incompatible|
|[Section top](#minorfail-outcome-number-72)|Description|Statement not supported in a Class Expression|
|[Section top](#minorfail-outcome-number-72)|Pointer|<pre lang="Turtle"><code>&#91;] a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;owl:allValuesFrom coswot:PropertyKind ;  &#10;&#32;&#32;&#32;&#32;owl:onProperty skos:broader .</code></pre>|
|[Section top](#minorfail-outcome-number-72)|Pointer|<pre lang="Turtle"><code>&#91;] a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;owl:allValuesFrom coswot:PropertyKind ;  &#10;&#32;&#32;&#32;&#32;owl:onProperty skos:narrower .</code></pre>|
|[Section top](#minorfail-outcome-number-72)|Pointer|<pre lang="Turtle"><code>&#91;] a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;owl:allValuesFrom owl:Nothing ;  &#10;&#32;&#32;&#32;&#32;owl:onProperty coswot:hasKind .</code></pre>|
|[Section top](#minorfail-outcome-number-72)|Pointer|<pre lang="Turtle"><code>&#91;] a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;owl:allValuesFrom coswot:PropertyKind ;  &#10;&#32;&#32;&#32;&#32;owl:onProperty coswot:hasKind .</code></pre>|
|[Section top](#minorfail-outcome-number-72)|Pointer|<pre lang="Turtle"><code>&#91;] a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;owl:onProperty coswot:isPropertyOfInterestOf .</code></pre>|

***
### MinorFail Outcome number 73

[Jump to summary definition](#summary-MinorFail-73)	|	[Previous MinorFail outcome](#minorfail-outcome-number-72)	|	[Next MinorFail outcome](#minorfail-outcome-number-74)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-src-properties-ontology|
|----|----|
|Title|Standalone module src/properties/ontology.ttl from branch main|
|Composition|- [Module properties/ontology](https://gitlab.com/coswot/coswot-acimov/blob/main/src/properties/ontology.ttl)|

#### Criterion detail
|Identifier|[profile-compatibility](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#profile-compatibility)|
|----|----|
|Title|Profile compatibility test|
|Description|A test meant to check whether the test subject is compatible with a profile or not, and if it is not, why.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-73)|Identifier|`owl-el-profile-error`|
|[Section top](#minorfail-outcome-number-73)|Title|OWL EL Profile incompatible|
|[Section top](#minorfail-outcome-number-73)|Description|Statement not supported|
|[Section top](#minorfail-outcome-number-73)|Pointer|<pre lang="Turtle"><code>coswot:Property a owl:Class ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;Property&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:comment &#34;Identifiable qualities of features that can be observed or c...&#34; ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy &#60;https://w3id.org/coswot/core/properties> ;  &#10;&#32;&#32;&#32;&#32;owl:disjointUnionOf ( coswot:PropertyOfInterest coswot:PropertyKind ) .</code></pre>|

***
### MinorFail Outcome number 74

[Jump to summary definition](#summary-MinorFail-74)	|	[Previous MinorFail outcome](#minorfail-outcome-number-73)	|	[Next MinorFail outcome](#minorfail-outcome-number-75)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-src-properties-ontology|
|----|----|
|Title|Standalone module src/properties/ontology.ttl from branch main|
|Composition|- [Module properties/ontology](https://gitlab.com/coswot/coswot-acimov/blob/main/src/properties/ontology.ttl)|

#### Criterion detail
|Identifier|[profile-compatibility](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#profile-compatibility)|
|----|----|
|Title|Profile compatibility test|
|Description|A test meant to check whether the test subject is compatible with a profile or not, and if it is not, why.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-74)|Identifier|`owl-el-profile-error`|
|[Section top](#minorfail-outcome-number-74)|Title|OWL EL Profile incompatible|
|[Section top](#minorfail-outcome-number-74)|Description|Class Expression not supported with rdfs:subClassOf|
|[Section top](#minorfail-outcome-number-74)|Pointer|<pre lang="Turtle"><code>coswot:PropertyKind a owl:Class ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;Property Kind&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:comment &#34;Identifiable qualities of features that can be observed or c...&#34; ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy &#60;https://w3id.org/coswot/core/properties> ;  &#10;&#32;&#32;&#32;&#32;rdfs:subClassOf &#91; a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:allValuesFrom coswot:PropertyKind ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:onProperty skos:broader ],  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#91; a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:allValuesFrom coswot:PropertyKind ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:onProperty skos:narrower ],  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#91; a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:allValuesFrom owl:Nothing ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:onProperty coswot:hasKind ],  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;skos:Concept,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;coswot:Property ;  &#10;&#32;&#32;&#32;&#32;skos:example &#34;Air temperature, pressure, luminance, etc. are all property ...&#34;,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#34;Two examples using the QUDT Quantity Kind vocabulary, and th...&#34; ;  &#10;&#32;&#32;&#32;&#32;skos:note &#34;Concepts from existing code lists, vocabularies, and taxonom...&#34; .</code></pre>|
|[Section top](#minorfail-outcome-number-74)|Pointer|<pre lang="Turtle"><code>coswot:PropertyOfInterest a owl:Class ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;Property of Interest&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:comment &#34;Identifiable qualities of features of interest that can be o...&#34; ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy &#60;https://w3id.org/coswot/core/properties> ;  &#10;&#32;&#32;&#32;&#32;rdfs:subClassOf &#91; a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:allValuesFrom coswot:PropertyKind ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:onProperty coswot:hasKind ],  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#91; a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:onProperty coswot:hasKind ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:someValuesFrom coswot:PropertyKind ],  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#91; a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:onProperty coswot:isPropertyOfInterestOf ],  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;coswot:Property ;  &#10;&#32;&#32;&#32;&#32;skos:example &#34;The air temperature of the atmosphere sample at a certain lo...&#34; ;  &#10;&#32;&#32;&#32;&#32;skos:note &#34;A property of interest is the property of (OP coswot:isPrope...&#34;,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#34;Per convention, the IRI of properties of interest should con...&#34;,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#34;Properties of interest need not always be explicited. It dep...&#34; .</code></pre>|

***
### MinorFail Outcome number 75

[Jump to summary definition](#summary-MinorFail-75)	|	[Previous MinorFail outcome](#minorfail-outcome-number-74)	|	[Next MinorFail outcome](#minorfail-outcome-number-76)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-src-procedures-ontology|
|----|----|
|Title|Standalone module src/procedures/ontology.ttl from branch main|
|Composition|- [Module procedures/ontology](https://gitlab.com/coswot/coswot-acimov/blob/main/src/procedures/ontology.ttl)|

#### Criterion detail
|Identifier|[domain-and-range-referencing](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#domain-and-range-referencing)|
|----|----|
|Title|Domain and range referencing test|
|Description|A test case from the Best Practices tests checking if all the ranges and domains from the test subject point to terms that are defined in the vocabulary.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-75)|Identifier|`range-out-of-vocabulary`|
|[Section top](#minorfail-outcome-number-75)|Title|Range out of vocabulary|
|[Section top](#minorfail-outcome-number-75)|Description|Some properties have a range out of the ontology|
|[Section top](#minorfail-outcome-number-75)|Pointer|<pre lang="Turtle"><code>:hasPhenomenonTime a owl:ObjectProperty ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;has phenomenon time&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:comment &#34;Links a procedure execution to the time that the result appl...&#34; ;  &#10;&#32;&#32;&#32;&#32;rdfs:domain &lowbar;:na702b4d3138043f68bff2c5df7766e77b1,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:Thing,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;:ProcedureExecution ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy &#60;https://w3id.org/coswot/core/procedures> ;  &#10;&#32;&#32;&#32;&#32;rdfs:range owl:Thing,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;time:TemporalEntity ;  &#10;&#32;&#32;&#32;&#32;rdfs:subPropertyOf :hasPhenomenonTime ;  &#10;&#32;&#32;&#32;&#32;owl:equivalentProperty :hasPhenomenonTime .  &#10;&lowbar;:na702b4d3138043f68bff2c5df7766e77b2 rdf:first :Procedure ;  &#10;&#32;&#32;&#32;&#32;rdf:rest ( :ProcedureExecution ) .  &#10;&lowbar;:na702b4d3138043f68bff2c5df7766e77b1 a owl:Class ;  &#10;&#32;&#32;&#32;&#32;rdfs:subClassOf &lowbar;:na702b4d3138043f68bff2c5df7766e77b1,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:Thing ;  &#10;&#32;&#32;&#32;&#32;owl:equivalentClass &lowbar;:na702b4d3138043f68bff2c5df7766e77b1 ;  &#10;&#32;&#32;&#32;&#32;owl:unionOf &lowbar;:na702b4d3138043f68bff2c5df7766e77b2 .</code></pre>|
|[Section top](#minorfail-outcome-number-75)|Pointer|<pre lang="Turtle"><code>:TemporalEntity a owl:Class ;  &#10;&#32;&#32;&#32;&#32;rdfs:subClassOf owl:Thing,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;:TemporalEntity ;  &#10;&#32;&#32;&#32;&#32;owl:equivalentClass :TemporalEntity .</code></pre>|

***
### MinorFail Outcome number 76

[Jump to summary definition](#summary-MinorFail-76)	|	[Previous MinorFail outcome](#minorfail-outcome-number-75)	|	[Next MinorFail outcome](#minorfail-outcome-number-77)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-src-procedures-ontology|
|----|----|
|Title|Standalone module src/procedures/ontology.ttl from branch main|
|Composition|- [Module procedures/ontology](https://gitlab.com/coswot/coswot-acimov/blob/main/src/procedures/ontology.ttl)|

#### Criterion detail
|Identifier|[profile-compatibility](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#profile-compatibility)|
|----|----|
|Title|Profile compatibility test|
|Description|A test meant to check whether the test subject is compatible with a profile or not, and if it is not, why.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-76)|Identifier|`owl-rl-profile-error`|
|[Section top](#minorfail-outcome-number-76)|Title|OWL RL Profile incompatible|
|[Section top](#minorfail-outcome-number-76)|Description|Class Expression not supported as object of rdfs:domain or rdfs:range|
|[Section top](#minorfail-outcome-number-76)|Pointer|<pre lang="Turtle"><code>coswot:hasInput a owl:ObjectProperty ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;has input&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:comment &#34;Links a procedure (e.g., a command) or procedure execution (...&#34; ;  &#10;&#32;&#32;&#32;&#32;rdfs:domain &#91; a owl:Class ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:unionOf ( coswot:Procedure coswot:ProcedureExecution ) ] ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy &#60;https://w3id.org/coswot/core/functions&lowbar;commands> ;  &#10;&#32;&#32;&#32;&#32;skos:example &#34;Different complementary commands can be defined for controll...&#34; .</code></pre>|

***
### MinorFail Outcome number 77

[Jump to summary definition](#summary-MinorFail-77)	|	[Previous MinorFail outcome](#minorfail-outcome-number-76)	|	[Next MinorFail outcome](#minorfail-outcome-number-78)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-src-procedures-ontology|
|----|----|
|Title|Standalone module src/procedures/ontology.ttl from branch main|
|Composition|- [Module procedures/ontology](https://gitlab.com/coswot/coswot-acimov/blob/main/src/procedures/ontology.ttl)|

#### Criterion detail
|Identifier|[profile-compatibility](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#profile-compatibility)|
|----|----|
|Title|Profile compatibility test|
|Description|A test meant to check whether the test subject is compatible with a profile or not, and if it is not, why.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-77)|Identifier|`owl-rl-profile-error`|
|[Section top](#minorfail-outcome-number-77)|Title|OWL RL Profile incompatible|
|[Section top](#minorfail-outcome-number-77)|Description|Statement not supported in a Super Class Expression|
|[Section top](#minorfail-outcome-number-77)|Pointer|<pre lang="Turtle"><code>&#91;] a owl:Class ;  &#10;&#32;&#32;&#32;&#32;owl:unionOf ( coswot:Procedure coswot:ProcedureExecution ) .</code></pre>|

***
### MinorFail Outcome number 78

[Jump to summary definition](#summary-MinorFail-78)	|	[Previous MinorFail outcome](#minorfail-outcome-number-77)	|	[Next MinorFail outcome](#minorfail-outcome-number-79)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-src-procedures-ontology|
|----|----|
|Title|Standalone module src/procedures/ontology.ttl from branch main|
|Composition|- [Module procedures/ontology](https://gitlab.com/coswot/coswot-acimov/blob/main/src/procedures/ontology.ttl)|

#### Criterion detail
|Identifier|[profile-compatibility](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#profile-compatibility)|
|----|----|
|Title|Profile compatibility test|
|Description|A test meant to check whether the test subject is compatible with a profile or not, and if it is not, why.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-78)|Identifier|`owl-ql-profile-error`|
|[Section top](#minorfail-outcome-number-78)|Title|OWL QL Profile incompatible|
|[Section top](#minorfail-outcome-number-78)|Description|Class Expression not supported as object of rdfs:domain or rdfs:range|
|[Section top](#minorfail-outcome-number-78)|Pointer|<pre lang="Turtle"><code>coswot:hasInput a owl:ObjectProperty ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;has input&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:comment &#34;Links a procedure (e.g., a command) or procedure execution (...&#34; ;  &#10;&#32;&#32;&#32;&#32;rdfs:domain &#91; a owl:Class ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:unionOf ( coswot:Procedure coswot:ProcedureExecution ) ] ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy &#60;https://w3id.org/coswot/core/functions&lowbar;commands> ;  &#10;&#32;&#32;&#32;&#32;skos:example &#34;Different complementary commands can be defined for controll...&#34; .</code></pre>|

***
### MinorFail Outcome number 79

[Jump to summary definition](#summary-MinorFail-79)	|	[Previous MinorFail outcome](#minorfail-outcome-number-78)	|	[Next MinorFail outcome](#minorfail-outcome-number-80)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-src-procedures-ontology|
|----|----|
|Title|Standalone module src/procedures/ontology.ttl from branch main|
|Composition|- [Module procedures/ontology](https://gitlab.com/coswot/coswot-acimov/blob/main/src/procedures/ontology.ttl)|

#### Criterion detail
|Identifier|[profile-compatibility](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#profile-compatibility)|
|----|----|
|Title|Profile compatibility test|
|Description|A test meant to check whether the test subject is compatible with a profile or not, and if it is not, why.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-79)|Identifier|`owl-ql-profile-error`|
|[Section top](#minorfail-outcome-number-79)|Title|OWL QL Profile incompatible|
|[Section top](#minorfail-outcome-number-79)|Description|Statement not supported in a Super Class Expression|
|[Section top](#minorfail-outcome-number-79)|Pointer|<pre lang="Turtle"><code>&#91;] a owl:Class ;  &#10;&#32;&#32;&#32;&#32;owl:unionOf ( coswot:Procedure coswot:ProcedureExecution ) .</code></pre>|

***
### MinorFail Outcome number 80

[Jump to summary definition](#summary-MinorFail-80)	|	[Previous MinorFail outcome](#minorfail-outcome-number-79)	|	[Next MinorFail outcome](#minorfail-outcome-number-81)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-src-procedures-ontology|
|----|----|
|Title|Standalone module src/procedures/ontology.ttl from branch main|
|Composition|- [Module procedures/ontology](https://gitlab.com/coswot/coswot-acimov/blob/main/src/procedures/ontology.ttl)|

#### Criterion detail
|Identifier|[profile-compatibility](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#profile-compatibility)|
|----|----|
|Title|Profile compatibility test|
|Description|A test meant to check whether the test subject is compatible with a profile or not, and if it is not, why.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-80)|Identifier|`owl-ql-profile-error`|
|[Section top](#minorfail-outcome-number-80)|Title|OWL QL Profile incompatible|
|[Section top](#minorfail-outcome-number-80)|Description|Property inclusions involving property chains not supported|
|[Section top](#minorfail-outcome-number-80)|Pointer|<pre lang="Turtle"><code>coswot:isExecutionOf a owl:ObjectProperty ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;is execution of&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:comment &#34;Links a procedure execution to the procedure that was execut...&#34; ;  &#10;&#32;&#32;&#32;&#32;rdfs:domain coswot:ProcedureExecution ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy &#60;https://w3id.org/coswot/core/procedures> ;  &#10;&#32;&#32;&#32;&#32;rdfs:range coswot:Procedure ;  &#10;&#32;&#32;&#32;&#32;owl:propertyChainAxiom ( coswot:isExecutionOf skos:broader ) .</code></pre>|

***
### MinorFail Outcome number 81

[Jump to summary definition](#summary-MinorFail-81)	|	[Previous MinorFail outcome](#minorfail-outcome-number-80)	|	[Next MinorFail outcome](#minorfail-outcome-number-82)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-src-procedures-ontology|
|----|----|
|Title|Standalone module src/procedures/ontology.ttl from branch main|
|Composition|- [Module procedures/ontology](https://gitlab.com/coswot/coswot-acimov/blob/main/src/procedures/ontology.ttl)|

#### Criterion detail
|Identifier|[profile-compatibility](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#profile-compatibility)|
|----|----|
|Title|Profile compatibility test|
|Description|A test meant to check whether the test subject is compatible with a profile or not, and if it is not, why.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-81)|Identifier|`owl-el-profile-error`|
|[Section top](#minorfail-outcome-number-81)|Title|OWL EL Profile incompatible|
|[Section top](#minorfail-outcome-number-81)|Description|Statement not supported in a Class Expression|
|[Section top](#minorfail-outcome-number-81)|Pointer|<pre lang="Turtle"><code>&#91;] a owl:Class ;  &#10;&#32;&#32;&#32;&#32;owl:unionOf ( coswot:Procedure coswot:ProcedureExecution ) .</code></pre>|

***
### MinorFail Outcome number 82

[Jump to summary definition](#summary-MinorFail-82)	|	[Previous MinorFail outcome](#minorfail-outcome-number-81)	|	[Next MinorFail outcome](#minorfail-outcome-number-83)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-src-procedures-ontology|
|----|----|
|Title|Standalone module src/procedures/ontology.ttl from branch main|
|Composition|- [Module procedures/ontology](https://gitlab.com/coswot/coswot-acimov/blob/main/src/procedures/ontology.ttl)|

#### Criterion detail
|Identifier|[profile-compatibility](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#profile-compatibility)|
|----|----|
|Title|Profile compatibility test|
|Description|A test meant to check whether the test subject is compatible with a profile or not, and if it is not, why.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-82)|Identifier|`owl-el-profile-error`|
|[Section top](#minorfail-outcome-number-82)|Title|OWL EL Profile incompatible|
|[Section top](#minorfail-outcome-number-82)|Description|Class Expression not supported as object of rdfs:domain or rdfs:range|
|[Section top](#minorfail-outcome-number-82)|Pointer|<pre lang="Turtle"><code>coswot:hasInput a owl:ObjectProperty ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;has input&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:comment &#34;Links a procedure (e.g., a command) or procedure execution (...&#34; ;  &#10;&#32;&#32;&#32;&#32;rdfs:domain &#91; a owl:Class ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:unionOf ( coswot:Procedure coswot:ProcedureExecution ) ] ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy &#60;https://w3id.org/coswot/core/functions&lowbar;commands> ;  &#10;&#32;&#32;&#32;&#32;skos:example &#34;Different complementary commands can be defined for controll...&#34; .</code></pre>|

***
### MinorFail Outcome number 83

[Jump to summary definition](#summary-MinorFail-83)	|	[Previous MinorFail outcome](#minorfail-outcome-number-82)	|	[Next MinorFail outcome](#minorfail-outcome-number-84)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-src-observations-ontology|
|----|----|
|Title|Standalone module src/observations/ontology.ttl from branch main|
|Composition|- [Module observations/ontology](https://gitlab.com/coswot/coswot-acimov/blob/main/src/observations/ontology.ttl)|

#### Criterion detail
|Identifier|[profile-compatibility](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#profile-compatibility)|
|----|----|
|Title|Profile compatibility test|
|Description|A test meant to check whether the test subject is compatible with a profile or not, and if it is not, why.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-83)|Identifier|`owl-rl-profile-error`|
|[Section top](#minorfail-outcome-number-83)|Title|OWL RL Profile incompatible|
|[Section top](#minorfail-outcome-number-83)|Description|Class Expression not supported with rdfs:subClassOf|
|[Section top](#minorfail-outcome-number-83)|Pointer|<pre lang="Turtle"><code>coswot:Observation a owl:Class ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;Observation&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:comment &#34;A coswot:Observation is the act of carrying out a procedure ...&#34; ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy &#60;https://w3id.org/coswot/core/observations> ;  &#10;&#32;&#32;&#32;&#32;rdfs:subClassOf &#91; a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:allValuesFrom coswot:Sensor ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:onProperty coswot:madeBy ],  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#91; a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:onProperty coswot:observes ],  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;coswot:ProcedureExecution .</code></pre>|
|[Section top](#minorfail-outcome-number-83)|Pointer|<pre lang="Turtle"><code>coswot:SensingCommand a owl:Class ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;Sensing Command&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:comment &#34;An instance of sensing command is a command that observes so...&#34; ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy &#60;https://w3id.org/coswot/core/observations> ;  &#10;&#32;&#32;&#32;&#32;rdfs:subClassOf &#91; a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:onProperty coswot:observes ],  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;coswot:Command .</code></pre>|
|[Section top](#minorfail-outcome-number-83)|Pointer|<pre lang="Turtle"><code>coswot:SensingFunction a owl:Class ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;Sensing Function&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:comment &#34;An sensing function is a function that has at least one sens...&#34; ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy &#60;https://w3id.org/coswot/core/observations> ;  &#10;&#32;&#32;&#32;&#32;rdfs:subClassOf &#91; a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:onProperty coswot:hasCommand ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:someValuesFrom coswot:SensingCommand ],  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;coswot:Function .</code></pre>|
|[Section top](#minorfail-outcome-number-83)|Pointer|<pre lang="Turtle"><code>coswot:SensorOfInterest a owl:Class ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;Sensor Of Interest&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:comment &#34;A specific, tangible device designed to observe one or more ...&#34; ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy &#60;https://w3id.org/coswot/core/observations> ;  &#10;&#32;&#32;&#32;&#32;rdfs:subClassOf &#91; a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:onProperty coswot:observes ],  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;coswot:DeviceOfInterest,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;coswot:Sensor .</code></pre>|

***
### MinorFail Outcome number 84

[Jump to summary definition](#summary-MinorFail-84)	|	[Previous MinorFail outcome](#minorfail-outcome-number-83)	|	[Next MinorFail outcome](#minorfail-outcome-number-85)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-src-observations-ontology|
|----|----|
|Title|Standalone module src/observations/ontology.ttl from branch main|
|Composition|- [Module observations/ontology](https://gitlab.com/coswot/coswot-acimov/blob/main/src/observations/ontology.ttl)|

#### Criterion detail
|Identifier|[profile-compatibility](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#profile-compatibility)|
|----|----|
|Title|Profile compatibility test|
|Description|A test meant to check whether the test subject is compatible with a profile or not, and if it is not, why.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-84)|Identifier|`owl-rl-profile-error`|
|[Section top](#minorfail-outcome-number-84)|Title|OWL RL Profile incompatible|
|[Section top](#minorfail-outcome-number-84)|Description|Statement not supported|
|[Section top](#minorfail-outcome-number-84)|Pointer|<pre lang="Turtle"><code>coswot:Sensor a owl:Class ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;Sensor&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:comment &#34;Sensors are devices designed to observe one or more properti...&#34; ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy &#60;https://w3id.org/coswot/core/observations> ;  &#10;&#32;&#32;&#32;&#32;rdfs:subClassOf &#91; a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:onProperty coswot:observes ],  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;coswot:Device ;  &#10;&#32;&#32;&#32;&#32;owl:disjointUnionOf ( coswot:SensorOfInterest coswot:SensorKind ) .</code></pre>|

***
### MinorFail Outcome number 85

[Jump to summary definition](#summary-MinorFail-85)	|	[Previous MinorFail outcome](#minorfail-outcome-number-84)	|	[Next MinorFail outcome](#minorfail-outcome-number-86)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-src-observations-ontology|
|----|----|
|Title|Standalone module src/observations/ontology.ttl from branch main|
|Composition|- [Module observations/ontology](https://gitlab.com/coswot/coswot-acimov/blob/main/src/observations/ontology.ttl)|

#### Criterion detail
|Identifier|[profile-compatibility](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#profile-compatibility)|
|----|----|
|Title|Profile compatibility test|
|Description|A test meant to check whether the test subject is compatible with a profile or not, and if it is not, why.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-85)|Identifier|`owl-rl-profile-error`|
|[Section top](#minorfail-outcome-number-85)|Title|OWL RL Profile incompatible|
|[Section top](#minorfail-outcome-number-85)|Description|Statement not supported in a Super Class Expression|
|[Section top](#minorfail-outcome-number-85)|Pointer|<pre lang="Turtle"><code>&#91;] a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;owl:onProperty coswot:observes .</code></pre>|
|[Section top](#minorfail-outcome-number-85)|Pointer|<pre lang="Turtle"><code>&#91;] a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;owl:onProperty coswot:hasCommand ;  &#10;&#32;&#32;&#32;&#32;owl:someValuesFrom coswot:SensingCommand .</code></pre>|
|[Section top](#minorfail-outcome-number-85)|Pointer|<pre lang="Turtle"><code>&#91;] a owl:Class ;  &#10;&#32;&#32;&#32;&#32;owl:unionOf ( coswot:Sensor coswot:SensingFunction coswot:SensingCommand coswot:Observation ) .</code></pre>|

***
### MinorFail Outcome number 86

[Jump to summary definition](#summary-MinorFail-86)	|	[Previous MinorFail outcome](#minorfail-outcome-number-85)	|	[Next MinorFail outcome](#minorfail-outcome-number-87)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-src-observations-ontology|
|----|----|
|Title|Standalone module src/observations/ontology.ttl from branch main|
|Composition|- [Module observations/ontology](https://gitlab.com/coswot/coswot-acimov/blob/main/src/observations/ontology.ttl)|

#### Criterion detail
|Identifier|[profile-compatibility](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#profile-compatibility)|
|----|----|
|Title|Profile compatibility test|
|Description|A test meant to check whether the test subject is compatible with a profile or not, and if it is not, why.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-86)|Identifier|`owl-rl-profile-error`|
|[Section top](#minorfail-outcome-number-86)|Title|OWL RL Profile incompatible|
|[Section top](#minorfail-outcome-number-86)|Description|Class Expression not supported as object of rdfs:domain or rdfs:range|
|[Section top](#minorfail-outcome-number-86)|Pointer|<pre lang="Turtle"><code>coswot:observes a owl:ObjectProperty ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;observes&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:comment &#34;Links a sensor, sensing function, sensing command, or observ...&#34; ;  &#10;&#32;&#32;&#32;&#32;rdfs:domain &#91; a owl:Class ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:unionOf ( coswot:Sensor coswot:SensingFunction coswot:SensingCommand coswot:Observation ) ] ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy &#60;https://w3id.org/coswot/core/procedures> ;  &#10;&#32;&#32;&#32;&#32;rdfs:subPropertyOf coswot:targets ;  &#10;&#32;&#32;&#32;&#32;owl:inverseOf coswot:isObservedBy .</code></pre>|

***
### MinorFail Outcome number 87

[Jump to summary definition](#summary-MinorFail-87)	|	[Previous MinorFail outcome](#minorfail-outcome-number-86)	|	[Next MinorFail outcome](#minorfail-outcome-number-88)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-src-observations-ontology|
|----|----|
|Title|Standalone module src/observations/ontology.ttl from branch main|
|Composition|- [Module observations/ontology](https://gitlab.com/coswot/coswot-acimov/blob/main/src/observations/ontology.ttl)|

#### Criterion detail
|Identifier|[profile-compatibility](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#profile-compatibility)|
|----|----|
|Title|Profile compatibility test|
|Description|A test meant to check whether the test subject is compatible with a profile or not, and if it is not, why.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-87)|Identifier|`owl-ql-profile-error`|
|[Section top](#minorfail-outcome-number-87)|Title|OWL QL Profile incompatible|
|[Section top](#minorfail-outcome-number-87)|Description|Class Expression not supported with rdfs:subClassOf|
|[Section top](#minorfail-outcome-number-87)|Pointer|<pre lang="Turtle"><code>coswot:Observation a owl:Class ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;Observation&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:comment &#34;A coswot:Observation is the act of carrying out a procedure ...&#34; ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy &#60;https://w3id.org/coswot/core/observations> ;  &#10;&#32;&#32;&#32;&#32;rdfs:subClassOf &#91; a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:allValuesFrom coswot:Sensor ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:onProperty coswot:madeBy ],  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#91; a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:onProperty coswot:observes ],  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;coswot:ProcedureExecution .</code></pre>|
|[Section top](#minorfail-outcome-number-87)|Pointer|<pre lang="Turtle"><code>coswot:SensingCommand a owl:Class ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;Sensing Command&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:comment &#34;An instance of sensing command is a command that observes so...&#34; ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy &#60;https://w3id.org/coswot/core/observations> ;  &#10;&#32;&#32;&#32;&#32;rdfs:subClassOf &#91; a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:onProperty coswot:observes ],  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;coswot:Command .</code></pre>|
|[Section top](#minorfail-outcome-number-87)|Pointer|<pre lang="Turtle"><code>coswot:SensorOfInterest a owl:Class ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;Sensor Of Interest&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:comment &#34;A specific, tangible device designed to observe one or more ...&#34; ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy &#60;https://w3id.org/coswot/core/observations> ;  &#10;&#32;&#32;&#32;&#32;rdfs:subClassOf &#91; a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:onProperty coswot:observes ],  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;coswot:DeviceOfInterest,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;coswot:Sensor .</code></pre>|

***
### MinorFail Outcome number 88

[Jump to summary definition](#summary-MinorFail-88)	|	[Previous MinorFail outcome](#minorfail-outcome-number-87)	|	[Next MinorFail outcome](#minorfail-outcome-number-89)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-src-observations-ontology|
|----|----|
|Title|Standalone module src/observations/ontology.ttl from branch main|
|Composition|- [Module observations/ontology](https://gitlab.com/coswot/coswot-acimov/blob/main/src/observations/ontology.ttl)|

#### Criterion detail
|Identifier|[profile-compatibility](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#profile-compatibility)|
|----|----|
|Title|Profile compatibility test|
|Description|A test meant to check whether the test subject is compatible with a profile or not, and if it is not, why.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-88)|Identifier|`owl-ql-profile-error`|
|[Section top](#minorfail-outcome-number-88)|Title|OWL QL Profile incompatible|
|[Section top](#minorfail-outcome-number-88)|Description|Statement not supported|
|[Section top](#minorfail-outcome-number-88)|Pointer|<pre lang="Turtle"><code>coswot:Sensor a owl:Class ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;Sensor&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:comment &#34;Sensors are devices designed to observe one or more properti...&#34; ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy &#60;https://w3id.org/coswot/core/observations> ;  &#10;&#32;&#32;&#32;&#32;rdfs:subClassOf &#91; a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:onProperty coswot:observes ],  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;coswot:Device ;  &#10;&#32;&#32;&#32;&#32;owl:disjointUnionOf ( coswot:SensorOfInterest coswot:SensorKind ) .</code></pre>|

***
### MinorFail Outcome number 89

[Jump to summary definition](#summary-MinorFail-89)	|	[Previous MinorFail outcome](#minorfail-outcome-number-88)	|	[Next MinorFail outcome](#minorfail-outcome-number-90)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-src-observations-ontology|
|----|----|
|Title|Standalone module src/observations/ontology.ttl from branch main|
|Composition|- [Module observations/ontology](https://gitlab.com/coswot/coswot-acimov/blob/main/src/observations/ontology.ttl)|

#### Criterion detail
|Identifier|[profile-compatibility](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#profile-compatibility)|
|----|----|
|Title|Profile compatibility test|
|Description|A test meant to check whether the test subject is compatible with a profile or not, and if it is not, why.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-89)|Identifier|`owl-ql-profile-error`|
|[Section top](#minorfail-outcome-number-89)|Title|OWL QL Profile incompatible|
|[Section top](#minorfail-outcome-number-89)|Description|Statement not supported in a Super Class Expression|
|[Section top](#minorfail-outcome-number-89)|Pointer|<pre lang="Turtle"><code>&#91;] a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;owl:onProperty coswot:observes .</code></pre>|
|[Section top](#minorfail-outcome-number-89)|Pointer|<pre lang="Turtle"><code>&#91;] a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;owl:allValuesFrom coswot:Sensor ;  &#10;&#32;&#32;&#32;&#32;owl:onProperty coswot:madeBy .</code></pre>|
|[Section top](#minorfail-outcome-number-89)|Pointer|<pre lang="Turtle"><code>&#91;] a owl:Class ;  &#10;&#32;&#32;&#32;&#32;owl:unionOf ( coswot:Sensor coswot:SensingFunction coswot:SensingCommand coswot:Observation ) .</code></pre>|

***
### MinorFail Outcome number 90

[Jump to summary definition](#summary-MinorFail-90)	|	[Previous MinorFail outcome](#minorfail-outcome-number-89)	|	[Next MinorFail outcome](#minorfail-outcome-number-91)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-src-observations-ontology|
|----|----|
|Title|Standalone module src/observations/ontology.ttl from branch main|
|Composition|- [Module observations/ontology](https://gitlab.com/coswot/coswot-acimov/blob/main/src/observations/ontology.ttl)|

#### Criterion detail
|Identifier|[profile-compatibility](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#profile-compatibility)|
|----|----|
|Title|Profile compatibility test|
|Description|A test meant to check whether the test subject is compatible with a profile or not, and if it is not, why.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-90)|Identifier|`owl-ql-profile-error`|
|[Section top](#minorfail-outcome-number-90)|Title|OWL QL Profile incompatible|
|[Section top](#minorfail-outcome-number-90)|Description|Class Expression not supported as object of rdfs:domain or rdfs:range|
|[Section top](#minorfail-outcome-number-90)|Pointer|<pre lang="Turtle"><code>coswot:observes a owl:ObjectProperty ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;observes&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:comment &#34;Links a sensor, sensing function, sensing command, or observ...&#34; ;  &#10;&#32;&#32;&#32;&#32;rdfs:domain &#91; a owl:Class ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:unionOf ( coswot:Sensor coswot:SensingFunction coswot:SensingCommand coswot:Observation ) ] ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy &#60;https://w3id.org/coswot/core/procedures> ;  &#10;&#32;&#32;&#32;&#32;rdfs:subPropertyOf coswot:targets ;  &#10;&#32;&#32;&#32;&#32;owl:inverseOf coswot:isObservedBy .</code></pre>|

***
### MinorFail Outcome number 91

[Jump to summary definition](#summary-MinorFail-91)	|	[Previous MinorFail outcome](#minorfail-outcome-number-90)	|	[Next MinorFail outcome](#minorfail-outcome-number-92)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-src-observations-ontology|
|----|----|
|Title|Standalone module src/observations/ontology.ttl from branch main|
|Composition|- [Module observations/ontology](https://gitlab.com/coswot/coswot-acimov/blob/main/src/observations/ontology.ttl)|

#### Criterion detail
|Identifier|[profile-compatibility](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#profile-compatibility)|
|----|----|
|Title|Profile compatibility test|
|Description|A test meant to check whether the test subject is compatible with a profile or not, and if it is not, why.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-91)|Identifier|`owl-el-profile-error`|
|[Section top](#minorfail-outcome-number-91)|Title|OWL EL Profile incompatible|
|[Section top](#minorfail-outcome-number-91)|Description|Statement not supported in a Class Expression|
|[Section top](#minorfail-outcome-number-91)|Pointer|<pre lang="Turtle"><code>&#91;] a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;owl:onProperty coswot:observes .</code></pre>|
|[Section top](#minorfail-outcome-number-91)|Pointer|<pre lang="Turtle"><code>&#91;] a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;owl:allValuesFrom coswot:Sensor ;  &#10;&#32;&#32;&#32;&#32;owl:onProperty coswot:madeBy .</code></pre>|
|[Section top](#minorfail-outcome-number-91)|Pointer|<pre lang="Turtle"><code>&#91;] a owl:Class ;  &#10;&#32;&#32;&#32;&#32;owl:unionOf ( coswot:Sensor coswot:SensingFunction coswot:SensingCommand coswot:Observation ) .</code></pre>|

***
### MinorFail Outcome number 92

[Jump to summary definition](#summary-MinorFail-92)	|	[Previous MinorFail outcome](#minorfail-outcome-number-91)	|	[Next MinorFail outcome](#minorfail-outcome-number-93)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-src-observations-ontology|
|----|----|
|Title|Standalone module src/observations/ontology.ttl from branch main|
|Composition|- [Module observations/ontology](https://gitlab.com/coswot/coswot-acimov/blob/main/src/observations/ontology.ttl)|

#### Criterion detail
|Identifier|[profile-compatibility](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#profile-compatibility)|
|----|----|
|Title|Profile compatibility test|
|Description|A test meant to check whether the test subject is compatible with a profile or not, and if it is not, why.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-92)|Identifier|`owl-el-profile-error`|
|[Section top](#minorfail-outcome-number-92)|Title|OWL EL Profile incompatible|
|[Section top](#minorfail-outcome-number-92)|Description|Statement not supported|
|[Section top](#minorfail-outcome-number-92)|Pointer|<pre lang="Turtle"><code>coswot:Sensor a owl:Class ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;Sensor&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:comment &#34;Sensors are devices designed to observe one or more properti...&#34; ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy &#60;https://w3id.org/coswot/core/observations> ;  &#10;&#32;&#32;&#32;&#32;rdfs:subClassOf &#91; a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:onProperty coswot:observes ],  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;coswot:Device ;  &#10;&#32;&#32;&#32;&#32;owl:disjointUnionOf ( coswot:SensorOfInterest coswot:SensorKind ) .</code></pre>|

***
### MinorFail Outcome number 93

[Jump to summary definition](#summary-MinorFail-93)	|	[Previous MinorFail outcome](#minorfail-outcome-number-92)	|	[Next MinorFail outcome](#minorfail-outcome-number-94)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-src-observations-ontology|
|----|----|
|Title|Standalone module src/observations/ontology.ttl from branch main|
|Composition|- [Module observations/ontology](https://gitlab.com/coswot/coswot-acimov/blob/main/src/observations/ontology.ttl)|

#### Criterion detail
|Identifier|[profile-compatibility](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#profile-compatibility)|
|----|----|
|Title|Profile compatibility test|
|Description|A test meant to check whether the test subject is compatible with a profile or not, and if it is not, why.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-93)|Identifier|`owl-el-profile-error`|
|[Section top](#minorfail-outcome-number-93)|Title|OWL EL Profile incompatible|
|[Section top](#minorfail-outcome-number-93)|Description|Class Expression not supported as object of rdfs:domain or rdfs:range|
|[Section top](#minorfail-outcome-number-93)|Pointer|<pre lang="Turtle"><code>coswot:observes a owl:ObjectProperty ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;observes&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:comment &#34;Links a sensor, sensing function, sensing command, or observ...&#34; ;  &#10;&#32;&#32;&#32;&#32;rdfs:domain &#91; a owl:Class ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:unionOf ( coswot:Sensor coswot:SensingFunction coswot:SensingCommand coswot:Observation ) ] ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy &#60;https://w3id.org/coswot/core/procedures> ;  &#10;&#32;&#32;&#32;&#32;rdfs:subPropertyOf coswot:targets ;  &#10;&#32;&#32;&#32;&#32;owl:inverseOf coswot:isObservedBy .</code></pre>|

***
### MinorFail Outcome number 94

[Jump to summary definition](#summary-MinorFail-94)	|	[Previous MinorFail outcome](#minorfail-outcome-number-93)	|	[Next MinorFail outcome](#minorfail-outcome-number-95)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-src-observations-ontology|
|----|----|
|Title|Standalone module src/observations/ontology.ttl from branch main|
|Composition|- [Module observations/ontology](https://gitlab.com/coswot/coswot-acimov/blob/main/src/observations/ontology.ttl)|

#### Criterion detail
|Identifier|[profile-compatibility](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#profile-compatibility)|
|----|----|
|Title|Profile compatibility test|
|Description|A test meant to check whether the test subject is compatible with a profile or not, and if it is not, why.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-94)|Identifier|`owl-el-profile-error`|
|[Section top](#minorfail-outcome-number-94)|Title|OWL EL Profile incompatible|
|[Section top](#minorfail-outcome-number-94)|Description|Class Expression not supported with rdfs:subClassOf|
|[Section top](#minorfail-outcome-number-94)|Pointer|<pre lang="Turtle"><code>coswot:Observation a owl:Class ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;Observation&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:comment &#34;A coswot:Observation is the act of carrying out a procedure ...&#34; ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy &#60;https://w3id.org/coswot/core/observations> ;  &#10;&#32;&#32;&#32;&#32;rdfs:subClassOf &#91; a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:allValuesFrom coswot:Sensor ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:onProperty coswot:madeBy ],  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#91; a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:onProperty coswot:observes ],  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;coswot:ProcedureExecution .</code></pre>|
|[Section top](#minorfail-outcome-number-94)|Pointer|<pre lang="Turtle"><code>coswot:SensingCommand a owl:Class ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;Sensing Command&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:comment &#34;An instance of sensing command is a command that observes so...&#34; ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy &#60;https://w3id.org/coswot/core/observations> ;  &#10;&#32;&#32;&#32;&#32;rdfs:subClassOf &#91; a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:onProperty coswot:observes ],  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;coswot:Command .</code></pre>|
|[Section top](#minorfail-outcome-number-94)|Pointer|<pre lang="Turtle"><code>coswot:SensorOfInterest a owl:Class ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;Sensor Of Interest&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:comment &#34;A specific, tangible device designed to observe one or more ...&#34; ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy &#60;https://w3id.org/coswot/core/observations> ;  &#10;&#32;&#32;&#32;&#32;rdfs:subClassOf &#91; a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:onProperty coswot:observes ],  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;coswot:DeviceOfInterest,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;coswot:Sensor .</code></pre>|

***
### MinorFail Outcome number 95

[Jump to summary definition](#summary-MinorFail-95)	|	[Previous MinorFail outcome](#minorfail-outcome-number-94)	|	[Next MinorFail outcome](#minorfail-outcome-number-96)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-src-functions-commands-ontology|
|----|----|
|Title|Standalone module src/functions&lowbar;commands/ontology.ttl from branch main|
|Composition|- [Module functions&lowbar;commands/ontology](https://gitlab.com/coswot/coswot-acimov/blob/main/src/functions_commands/ontology.ttl)|

#### Criterion detail
|Identifier|[profile-compatibility](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#profile-compatibility)|
|----|----|
|Title|Profile compatibility test|
|Description|A test meant to check whether the test subject is compatible with a profile or not, and if it is not, why.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-95)|Identifier|`owl-rl-profile-error`|
|[Section top](#minorfail-outcome-number-95)|Title|OWL RL Profile incompatible|
|[Section top](#minorfail-outcome-number-95)|Description|Class Expression not supported with rdfs:subClassOf|
|[Section top](#minorfail-outcome-number-95)|Pointer|<pre lang="Turtle"><code>coswot:CommandOfInterest a owl:Class ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;Command Of Interest&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:comment &#34;The lowest-level directives a device supports and exposes to...&#34; ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy &#60;https://w3id.org/coswot/core/functions&lowbar;commands> ;  &#10;&#32;&#32;&#32;&#32;rdfs:subClassOf &#91; a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:allValuesFrom coswot:CommandKind ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:onProperty coswot:hasKind ],  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#91; a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:onProperty coswot:hasKind ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:someValuesFrom coswot:CommandKind ],  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#91; a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:onProperty coswot:isCommandOfInterestOf ],  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;coswot:Command ;  &#10;&#32;&#32;&#32;&#32;skos:example &#34;The corridor smart light switch supports a command of kind “...&#34;,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#34;The smart fridge supports a command of kind “observe tempera...&#34; ;  &#10;&#32;&#32;&#32;&#32;skos:note &#34;Commands of interest need not always be explicited. It depen...&#34;,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#34;Like for commands, commands of interest may be described in ...&#34; .</code></pre>|
|[Section top](#minorfail-outcome-number-95)|Pointer|<pre lang="Turtle"><code>coswot:FunctionOfInterest a owl:Class ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;Function of Interest&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:comment &#34;Logical groups of commands that devices support to accomplis...&#34; ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy &#60;https://w3id.org/coswot/core/functions&lowbar;commands> ;  &#10;&#32;&#32;&#32;&#32;rdfs:subClassOf &#91; a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:allValuesFrom coswot:FunctionKind ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:onProperty coswot:hasKind ],  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#91; a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:onProperty coswot:hasKind ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:someValuesFrom coswot:FunctionKind ],  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#91; a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:onProperty coswot:isFunctionOfInterestOf ],  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;coswot:Function ;  &#10;&#32;&#32;&#32;&#32;skos:note &#34;A function of interest is the function of (OP coswot:isFunct...&#34;,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#34;Functions of interest need not always be explicited. It depe...&#34; .</code></pre>|

***
### MinorFail Outcome number 96

[Jump to summary definition](#summary-MinorFail-96)	|	[Previous MinorFail outcome](#minorfail-outcome-number-95)	|	[Next MinorFail outcome](#minorfail-outcome-number-97)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-src-functions-commands-ontology|
|----|----|
|Title|Standalone module src/functions&lowbar;commands/ontology.ttl from branch main|
|Composition|- [Module functions&lowbar;commands/ontology](https://gitlab.com/coswot/coswot-acimov/blob/main/src/functions_commands/ontology.ttl)|

#### Criterion detail
|Identifier|[profile-compatibility](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#profile-compatibility)|
|----|----|
|Title|Profile compatibility test|
|Description|A test meant to check whether the test subject is compatible with a profile or not, and if it is not, why.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-96)|Identifier|`owl-rl-profile-error`|
|[Section top](#minorfail-outcome-number-96)|Title|OWL RL Profile incompatible|
|[Section top](#minorfail-outcome-number-96)|Description|Statement not supported|
|[Section top](#minorfail-outcome-number-96)|Pointer|<pre lang="Turtle"><code>coswot:Function a owl:Class ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;Function&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:comment &#34;Logical groups of commands that devices support to accomplis...&#34; ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy &#60;https://w3id.org/coswot/core/functions&lowbar;commands> ;  &#10;&#32;&#32;&#32;&#32;rdfs:subClassOf coswot:ProcedureCollection ;  &#10;&#32;&#32;&#32;&#32;owl:disjointUnionOf ( coswot:FunctionOfInterest coswot:FunctionKind ) .</code></pre>|

***
### MinorFail Outcome number 97

[Jump to summary definition](#summary-MinorFail-97)	|	[Previous MinorFail outcome](#minorfail-outcome-number-96)	|	[Next MinorFail outcome](#minorfail-outcome-number-98)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-src-functions-commands-ontology|
|----|----|
|Title|Standalone module src/functions&lowbar;commands/ontology.ttl from branch main|
|Composition|- [Module functions&lowbar;commands/ontology](https://gitlab.com/coswot/coswot-acimov/blob/main/src/functions_commands/ontology.ttl)|

#### Criterion detail
|Identifier|[profile-compatibility](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#profile-compatibility)|
|----|----|
|Title|Profile compatibility test|
|Description|A test meant to check whether the test subject is compatible with a profile or not, and if it is not, why.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-97)|Identifier|`owl-rl-profile-error`|
|[Section top](#minorfail-outcome-number-97)|Title|OWL RL Profile incompatible|
|[Section top](#minorfail-outcome-number-97)|Description|Statement not supported in a Super Class Expression|
|[Section top](#minorfail-outcome-number-97)|Pointer|<pre lang="Turtle"><code>&#91;] a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;owl:onProperty coswot:hasKind ;  &#10;&#32;&#32;&#32;&#32;owl:someValuesFrom coswot:FunctionKind .</code></pre>|
|[Section top](#minorfail-outcome-number-97)|Pointer|<pre lang="Turtle"><code>&#91;] a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;owl:onProperty coswot:isFunctionOfInterestOf .</code></pre>|
|[Section top](#minorfail-outcome-number-97)|Pointer|<pre lang="Turtle"><code>&#91;] a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;owl:onProperty coswot:hasKind ;  &#10;&#32;&#32;&#32;&#32;owl:someValuesFrom coswot:CommandKind .</code></pre>|
|[Section top](#minorfail-outcome-number-97)|Pointer|<pre lang="Turtle"><code>&#91;] a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;owl:onProperty coswot:isCommandOfInterestOf .</code></pre>|

***
### MinorFail Outcome number 98

[Jump to summary definition](#summary-MinorFail-98)	|	[Previous MinorFail outcome](#minorfail-outcome-number-97)	|	[Next MinorFail outcome](#minorfail-outcome-number-99)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-src-functions-commands-ontology|
|----|----|
|Title|Standalone module src/functions&lowbar;commands/ontology.ttl from branch main|
|Composition|- [Module functions&lowbar;commands/ontology](https://gitlab.com/coswot/coswot-acimov/blob/main/src/functions_commands/ontology.ttl)|

#### Criterion detail
|Identifier|[profile-compatibility](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#profile-compatibility)|
|----|----|
|Title|Profile compatibility test|
|Description|A test meant to check whether the test subject is compatible with a profile or not, and if it is not, why.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-98)|Identifier|`owl-ql-profile-error`|
|[Section top](#minorfail-outcome-number-98)|Title|OWL QL Profile incompatible|
|[Section top](#minorfail-outcome-number-98)|Description|Class Expression not supported with rdfs:subClassOf|
|[Section top](#minorfail-outcome-number-98)|Pointer|<pre lang="Turtle"><code>coswot:CommandExecution a owl:Class ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;Command Execution&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:comment &#34;Describes the execution of a command. Typically, its inputs ...&#34; ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy &#60;https://w3id.org/coswot/core/functions&lowbar;commands> ;  &#10;&#32;&#32;&#32;&#32;rdfs:subClassOf &#91; a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:allValuesFrom coswot:Command ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:onProperty coswot:isExecutionOf ],  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;coswot:ProcedureExecution .</code></pre>|
|[Section top](#minorfail-outcome-number-98)|Pointer|<pre lang="Turtle"><code>coswot:CommandKind a owl:Class ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;Command Kind&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:comment &#34;The lowest-level directives a function exposes to some netwo...&#34; ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy &#60;https://w3id.org/coswot/core/functions&lowbar;commands> ;  &#10;&#32;&#32;&#32;&#32;rdfs:subClassOf &#91; a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:allValuesFrom coswot:CommandKind ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:onProperty skos:broader ],  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#91; a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:allValuesFrom coswot:CommandKind ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:onProperty skos:narrower ],  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#91; a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:allValuesFrom owl:Nothing ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:onProperty coswot:hasKind ],  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#91; owl:allValuesFrom coswot:FunctionKind ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:onProperty coswot:isCommandOf ],  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;coswot:Command ;  &#10;&#32;&#32;&#32;&#32;skos:example &#34;Observe property, control property, observe state, control s...&#34; .</code></pre>|
|[Section top](#minorfail-outcome-number-98)|Pointer|<pre lang="Turtle"><code>coswot:CommandOfInterest a owl:Class ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;Command Of Interest&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:comment &#34;The lowest-level directives a device supports and exposes to...&#34; ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy &#60;https://w3id.org/coswot/core/functions&lowbar;commands> ;  &#10;&#32;&#32;&#32;&#32;rdfs:subClassOf &#91; a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:allValuesFrom coswot:CommandKind ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:onProperty coswot:hasKind ],  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#91; a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:onProperty coswot:hasKind ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:someValuesFrom coswot:CommandKind ],  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#91; a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:onProperty coswot:isCommandOfInterestOf ],  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;coswot:Command ;  &#10;&#32;&#32;&#32;&#32;skos:example &#34;The corridor smart light switch supports a command of kind “...&#34;,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#34;The smart fridge supports a command of kind “observe tempera...&#34; ;  &#10;&#32;&#32;&#32;&#32;skos:note &#34;Commands of interest need not always be explicited. It depen...&#34;,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#34;Like for commands, commands of interest may be described in ...&#34; .</code></pre>|
|[Section top](#minorfail-outcome-number-98)|Pointer|<pre lang="Turtle"><code>coswot:DeviceKind rdfs:subClassOf &#91; a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:allValuesFrom coswot:FunctionKind ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:onProperty coswot:hasFunction ] .</code></pre>|
|[Section top](#minorfail-outcome-number-98)|Pointer|<pre lang="Turtle"><code>coswot:FunctionKind a owl:Class ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;Function Kind&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:comment &#34;Logical groups of commands that devices support to accomplis...&#34; ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy &#60;https://w3id.org/coswot/core/functions&lowbar;commands> ;  &#10;&#32;&#32;&#32;&#32;rdfs:subClassOf &#91; a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:allValuesFrom coswot:FunctionKind ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:onProperty skos:broader ],  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#91; a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:allValuesFrom coswot:FunctionKind ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:onProperty skos:narrower ],  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#91; a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:allValuesFrom owl:Nothing ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:onProperty coswot:hasKind ],  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#91; a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:allValuesFrom coswot:DeviceKind ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:onProperty coswot:isFunctionOf ],  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#91; owl:allValuesFrom coswot:CommandKind ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:onProperty coswot:hasCommand ],  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;coswot:Function .</code></pre>|
|[Section top](#minorfail-outcome-number-98)|Pointer|<pre lang="Turtle"><code>coswot:FunctionOfInterest a owl:Class ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;Function of Interest&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:comment &#34;Logical groups of commands that devices support to accomplis...&#34; ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy &#60;https://w3id.org/coswot/core/functions&lowbar;commands> ;  &#10;&#32;&#32;&#32;&#32;rdfs:subClassOf &#91; a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:allValuesFrom coswot:FunctionKind ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:onProperty coswot:hasKind ],  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#91; a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:onProperty coswot:hasKind ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:someValuesFrom coswot:FunctionKind ],  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#91; a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:onProperty coswot:isFunctionOfInterestOf ],  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;coswot:Function ;  &#10;&#32;&#32;&#32;&#32;skos:note &#34;A function of interest is the function of (OP coswot:isFunct...&#34;,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#34;Functions of interest need not always be explicited. It depe...&#34; .</code></pre>|

***
### MinorFail Outcome number 99

[Jump to summary definition](#summary-MinorFail-99)	|	[Previous MinorFail outcome](#minorfail-outcome-number-98)	|	[Next MinorFail outcome](#minorfail-outcome-number-100)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-src-functions-commands-ontology|
|----|----|
|Title|Standalone module src/functions&lowbar;commands/ontology.ttl from branch main|
|Composition|- [Module functions&lowbar;commands/ontology](https://gitlab.com/coswot/coswot-acimov/blob/main/src/functions_commands/ontology.ttl)|

#### Criterion detail
|Identifier|[profile-compatibility](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#profile-compatibility)|
|----|----|
|Title|Profile compatibility test|
|Description|A test meant to check whether the test subject is compatible with a profile or not, and if it is not, why.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-99)|Identifier|`owl-ql-profile-error`|
|[Section top](#minorfail-outcome-number-99)|Title|OWL QL Profile incompatible|
|[Section top](#minorfail-outcome-number-99)|Description|Statement not supported|
|[Section top](#minorfail-outcome-number-99)|Pointer|<pre lang="Turtle"><code>coswot:Function a owl:Class ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;Function&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:comment &#34;Logical groups of commands that devices support to accomplis...&#34; ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy &#60;https://w3id.org/coswot/core/functions&lowbar;commands> ;  &#10;&#32;&#32;&#32;&#32;rdfs:subClassOf coswot:ProcedureCollection ;  &#10;&#32;&#32;&#32;&#32;owl:disjointUnionOf ( coswot:FunctionOfInterest coswot:FunctionKind ) .</code></pre>|

***
### MinorFail Outcome number 100

[Jump to summary definition](#summary-MinorFail-100)	|	[Previous MinorFail outcome](#minorfail-outcome-number-99)	|	[Next MinorFail outcome](#minorfail-outcome-number-101)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-src-functions-commands-ontology|
|----|----|
|Title|Standalone module src/functions&lowbar;commands/ontology.ttl from branch main|
|Composition|- [Module functions&lowbar;commands/ontology](https://gitlab.com/coswot/coswot-acimov/blob/main/src/functions_commands/ontology.ttl)|

#### Criterion detail
|Identifier|[profile-compatibility](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#profile-compatibility)|
|----|----|
|Title|Profile compatibility test|
|Description|A test meant to check whether the test subject is compatible with a profile or not, and if it is not, why.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-100)|Identifier|`owl-ql-profile-error`|
|[Section top](#minorfail-outcome-number-100)|Title|OWL QL Profile incompatible|
|[Section top](#minorfail-outcome-number-100)|Description|Statement not supported in a Super Class Expression|
|[Section top](#minorfail-outcome-number-100)|Pointer|<pre lang="Turtle"><code>&#91;] a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;owl:allValuesFrom coswot:FunctionKind ;  &#10;&#32;&#32;&#32;&#32;owl:onProperty skos:broader .</code></pre>|
|[Section top](#minorfail-outcome-number-100)|Pointer|<pre lang="Turtle"><code>&#91;] a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;owl:allValuesFrom coswot:FunctionKind ;  &#10;&#32;&#32;&#32;&#32;owl:onProperty skos:narrower .</code></pre>|
|[Section top](#minorfail-outcome-number-100)|Pointer|<pre lang="Turtle"><code>&#91;] a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;owl:allValuesFrom owl:Nothing ;  &#10;&#32;&#32;&#32;&#32;owl:onProperty coswot:hasKind .</code></pre>|
|[Section top](#minorfail-outcome-number-100)|Pointer|<pre lang="Turtle"><code>&#91;] a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;owl:allValuesFrom coswot:FunctionKind ;  &#10;&#32;&#32;&#32;&#32;owl:onProperty coswot:hasKind .</code></pre>|
|[Section top](#minorfail-outcome-number-100)|Pointer|<pre lang="Turtle"><code>&#91;] a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;owl:allValuesFrom coswot:FunctionKind ;  &#10;&#32;&#32;&#32;&#32;owl:onProperty coswot:hasFunction .</code></pre>|
|[Section top](#minorfail-outcome-number-100)|Pointer|<pre lang="Turtle"><code>&#91;] a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;owl:allValuesFrom coswot:DeviceKind ;  &#10;&#32;&#32;&#32;&#32;owl:onProperty coswot:isFunctionOf .</code></pre>|
|[Section top](#minorfail-outcome-number-100)|Pointer|<pre lang="Turtle"><code>&#91;] a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;owl:onProperty coswot:isFunctionOfInterestOf .</code></pre>|
|[Section top](#minorfail-outcome-number-100)|Pointer|<pre lang="Turtle"><code>&#91;] a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;owl:allValuesFrom coswot:CommandKind ;  &#10;&#32;&#32;&#32;&#32;owl:onProperty skos:broader .</code></pre>|
|[Section top](#minorfail-outcome-number-100)|Pointer|<pre lang="Turtle"><code>&#91;] a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;owl:allValuesFrom coswot:CommandKind ;  &#10;&#32;&#32;&#32;&#32;owl:onProperty skos:narrower .</code></pre>|
|[Section top](#minorfail-outcome-number-100)|Pointer|<pre lang="Turtle"><code>&#91;] a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;owl:allValuesFrom coswot:CommandKind ;  &#10;&#32;&#32;&#32;&#32;owl:onProperty coswot:hasKind .</code></pre>|
|[Section top](#minorfail-outcome-number-100)|Pointer|<pre lang="Turtle"><code>&#91;] owl:allValuesFrom coswot:CommandKind ;  &#10;&#32;&#32;&#32;&#32;owl:onProperty coswot:hasCommand .</code></pre>|
|[Section top](#minorfail-outcome-number-100)|Pointer|<pre lang="Turtle"><code>&#91;] owl:allValuesFrom coswot:FunctionKind ;  &#10;&#32;&#32;&#32;&#32;owl:onProperty coswot:isCommandOf .</code></pre>|
|[Section top](#minorfail-outcome-number-100)|Pointer|<pre lang="Turtle"><code>&#91;] a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;owl:onProperty coswot:isCommandOfInterestOf .</code></pre>|
|[Section top](#minorfail-outcome-number-100)|Pointer|<pre lang="Turtle"><code>&#91;] a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;owl:allValuesFrom coswot:Command ;  &#10;&#32;&#32;&#32;&#32;owl:onProperty coswot:isExecutionOf .</code></pre>|

***
### MinorFail Outcome number 101

[Jump to summary definition](#summary-MinorFail-101)	|	[Previous MinorFail outcome](#minorfail-outcome-number-100)	|	[Next MinorFail outcome](#minorfail-outcome-number-102)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-src-functions-commands-ontology|
|----|----|
|Title|Standalone module src/functions&lowbar;commands/ontology.ttl from branch main|
|Composition|- [Module functions&lowbar;commands/ontology](https://gitlab.com/coswot/coswot-acimov/blob/main/src/functions_commands/ontology.ttl)|

#### Criterion detail
|Identifier|[profile-compatibility](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#profile-compatibility)|
|----|----|
|Title|Profile compatibility test|
|Description|A test meant to check whether the test subject is compatible with a profile or not, and if it is not, why.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-101)|Identifier|`owl-ql-profile-error`|
|[Section top](#minorfail-outcome-number-101)|Title|OWL QL Profile incompatible|
|[Section top](#minorfail-outcome-number-101)|Description|Property inclusions involving property chains not supported|
|[Section top](#minorfail-outcome-number-101)|Pointer|<pre lang="Turtle"><code>coswot:hasCommand a owl:ObjectProperty ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;has command&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:comment &#34;Links a function and the command it supports.&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:domain coswot:Function ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy &#60;https://w3id.org/coswot/core/functions&lowbar;commands> ;  &#10;&#32;&#32;&#32;&#32;rdfs:range coswot:Command ;  &#10;&#32;&#32;&#32;&#32;owl:inverseOf coswot:isCommandOf ;  &#10;&#32;&#32;&#32;&#32;owl:propertyChainAxiom ( coswot:hasKind coswot:hasMandatoryCommand ),  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;( coswot:hasCommandOfInterest coswot:hasKind ) .</code></pre>|
|[Section top](#minorfail-outcome-number-101)|Pointer|<pre lang="Turtle"><code>coswot:hasFunction a owl:ObjectProperty ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;has function&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:comment &#34;Links a device to one of its functions.&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:domain coswot:Device ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy &#60;https://w3id.org/coswot/core/functions&lowbar;commands> ;  &#10;&#32;&#32;&#32;&#32;rdfs:range coswot:Function ;  &#10;&#32;&#32;&#32;&#32;owl:inverseOf coswot:isFunctionOf ;  &#10;&#32;&#32;&#32;&#32;owl:propertyChainAxiom ( skos:broader coswot:hasFunction ),  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;( coswot:hasKind coswot:hasFunction ),  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;( coswot:hasFunctionOfInterest coswot:hasKind ) .</code></pre>|
|[Section top](#minorfail-outcome-number-101)|Pointer|<pre lang="Turtle"><code>coswot:hasMandatoryCommand a owl:ObjectProperty ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;has mandatory command&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:comment &#34;Links a function and one of its mandatory commands&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:domain coswot:FunctionKind ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy &#60;https://w3id.org/coswot/core/functions&lowbar;commands> ;  &#10;&#32;&#32;&#32;&#32;rdfs:range coswot:CommandKind ;  &#10;&#32;&#32;&#32;&#32;rdfs:subPropertyOf coswot:hasCommand ;  &#10;&#32;&#32;&#32;&#32;owl:propertyChainAxiom ( skos:broader coswot:hasMandatoryCommand ) .</code></pre>|
|[Section top](#minorfail-outcome-number-101)|Pointer|<pre lang="Turtle"><code>coswot:isExecutionOf owl:propertyChainAxiom ( coswot:isExecutionOf coswot:hasKind ) .</code></pre>|

***
### MinorFail Outcome number 102

[Jump to summary definition](#summary-MinorFail-102)	|	[Previous MinorFail outcome](#minorfail-outcome-number-101)	|	[Next MinorFail outcome](#minorfail-outcome-number-103)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-src-functions-commands-ontology|
|----|----|
|Title|Standalone module src/functions&lowbar;commands/ontology.ttl from branch main|
|Composition|- [Module functions&lowbar;commands/ontology](https://gitlab.com/coswot/coswot-acimov/blob/main/src/functions_commands/ontology.ttl)|

#### Criterion detail
|Identifier|[profile-compatibility](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#profile-compatibility)|
|----|----|
|Title|Profile compatibility test|
|Description|A test meant to check whether the test subject is compatible with a profile or not, and if it is not, why.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-102)|Identifier|`owl-el-profile-error`|
|[Section top](#minorfail-outcome-number-102)|Title|OWL EL Profile incompatible|
|[Section top](#minorfail-outcome-number-102)|Description|Statement not supported in a Class Expression|
|[Section top](#minorfail-outcome-number-102)|Pointer|<pre lang="Turtle"><code>&#91;] a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;owl:allValuesFrom coswot:FunctionKind ;  &#10;&#32;&#32;&#32;&#32;owl:onProperty skos:broader .</code></pre>|
|[Section top](#minorfail-outcome-number-102)|Pointer|<pre lang="Turtle"><code>&#91;] a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;owl:allValuesFrom coswot:FunctionKind ;  &#10;&#32;&#32;&#32;&#32;owl:onProperty skos:narrower .</code></pre>|
|[Section top](#minorfail-outcome-number-102)|Pointer|<pre lang="Turtle"><code>&#91;] a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;owl:allValuesFrom owl:Nothing ;  &#10;&#32;&#32;&#32;&#32;owl:onProperty coswot:hasKind .</code></pre>|
|[Section top](#minorfail-outcome-number-102)|Pointer|<pre lang="Turtle"><code>&#91;] a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;owl:allValuesFrom coswot:FunctionKind ;  &#10;&#32;&#32;&#32;&#32;owl:onProperty coswot:hasKind .</code></pre>|
|[Section top](#minorfail-outcome-number-102)|Pointer|<pre lang="Turtle"><code>&#91;] a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;owl:allValuesFrom coswot:FunctionKind ;  &#10;&#32;&#32;&#32;&#32;owl:onProperty coswot:hasFunction .</code></pre>|
|[Section top](#minorfail-outcome-number-102)|Pointer|<pre lang="Turtle"><code>&#91;] a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;owl:allValuesFrom coswot:DeviceKind ;  &#10;&#32;&#32;&#32;&#32;owl:onProperty coswot:isFunctionOf .</code></pre>|
|[Section top](#minorfail-outcome-number-102)|Pointer|<pre lang="Turtle"><code>&#91;] a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;owl:onProperty coswot:isFunctionOfInterestOf .</code></pre>|
|[Section top](#minorfail-outcome-number-102)|Pointer|<pre lang="Turtle"><code>&#91;] a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;owl:allValuesFrom coswot:CommandKind ;  &#10;&#32;&#32;&#32;&#32;owl:onProperty skos:broader .</code></pre>|
|[Section top](#minorfail-outcome-number-102)|Pointer|<pre lang="Turtle"><code>&#91;] a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;owl:allValuesFrom coswot:CommandKind ;  &#10;&#32;&#32;&#32;&#32;owl:onProperty skos:narrower .</code></pre>|
|[Section top](#minorfail-outcome-number-102)|Pointer|<pre lang="Turtle"><code>&#91;] a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;owl:allValuesFrom coswot:CommandKind ;  &#10;&#32;&#32;&#32;&#32;owl:onProperty coswot:hasKind .</code></pre>|
|[Section top](#minorfail-outcome-number-102)|Pointer|<pre lang="Turtle"><code>&#91;] owl:allValuesFrom coswot:CommandKind ;  &#10;&#32;&#32;&#32;&#32;owl:onProperty coswot:hasCommand .</code></pre>|
|[Section top](#minorfail-outcome-number-102)|Pointer|<pre lang="Turtle"><code>&#91;] owl:allValuesFrom coswot:FunctionKind ;  &#10;&#32;&#32;&#32;&#32;owl:onProperty coswot:isCommandOf .</code></pre>|
|[Section top](#minorfail-outcome-number-102)|Pointer|<pre lang="Turtle"><code>&#91;] a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;owl:onProperty coswot:isCommandOfInterestOf .</code></pre>|
|[Section top](#minorfail-outcome-number-102)|Pointer|<pre lang="Turtle"><code>&#91;] a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;owl:allValuesFrom coswot:Command ;  &#10;&#32;&#32;&#32;&#32;owl:onProperty coswot:isExecutionOf .</code></pre>|

***
### MinorFail Outcome number 103

[Jump to summary definition](#summary-MinorFail-103)	|	[Previous MinorFail outcome](#minorfail-outcome-number-102)	|	[Next MinorFail outcome](#minorfail-outcome-number-104)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-src-functions-commands-ontology|
|----|----|
|Title|Standalone module src/functions&lowbar;commands/ontology.ttl from branch main|
|Composition|- [Module functions&lowbar;commands/ontology](https://gitlab.com/coswot/coswot-acimov/blob/main/src/functions_commands/ontology.ttl)|

#### Criterion detail
|Identifier|[profile-compatibility](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#profile-compatibility)|
|----|----|
|Title|Profile compatibility test|
|Description|A test meant to check whether the test subject is compatible with a profile or not, and if it is not, why.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-103)|Identifier|`owl-el-profile-error`|
|[Section top](#minorfail-outcome-number-103)|Title|OWL EL Profile incompatible|
|[Section top](#minorfail-outcome-number-103)|Description|Statement not supported|
|[Section top](#minorfail-outcome-number-103)|Pointer|<pre lang="Turtle"><code>coswot:Function a owl:Class ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;Function&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:comment &#34;Logical groups of commands that devices support to accomplis...&#34; ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy &#60;https://w3id.org/coswot/core/functions&lowbar;commands> ;  &#10;&#32;&#32;&#32;&#32;rdfs:subClassOf coswot:ProcedureCollection ;  &#10;&#32;&#32;&#32;&#32;owl:disjointUnionOf ( coswot:FunctionOfInterest coswot:FunctionKind ) .</code></pre>|

***
### MinorFail Outcome number 104

[Jump to summary definition](#summary-MinorFail-104)	|	[Previous MinorFail outcome](#minorfail-outcome-number-103)	|	[Next MinorFail outcome](#minorfail-outcome-number-105)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-src-functions-commands-ontology|
|----|----|
|Title|Standalone module src/functions&lowbar;commands/ontology.ttl from branch main|
|Composition|- [Module functions&lowbar;commands/ontology](https://gitlab.com/coswot/coswot-acimov/blob/main/src/functions_commands/ontology.ttl)|

#### Criterion detail
|Identifier|[profile-compatibility](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#profile-compatibility)|
|----|----|
|Title|Profile compatibility test|
|Description|A test meant to check whether the test subject is compatible with a profile or not, and if it is not, why.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-104)|Identifier|`owl-el-profile-error`|
|[Section top](#minorfail-outcome-number-104)|Title|OWL EL Profile incompatible|
|[Section top](#minorfail-outcome-number-104)|Description|Class Expression not supported with rdfs:subClassOf|
|[Section top](#minorfail-outcome-number-104)|Pointer|<pre lang="Turtle"><code>coswot:CommandExecution a owl:Class ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;Command Execution&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:comment &#34;Describes the execution of a command. Typically, its inputs ...&#34; ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy &#60;https://w3id.org/coswot/core/functions&lowbar;commands> ;  &#10;&#32;&#32;&#32;&#32;rdfs:subClassOf &#91; a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:allValuesFrom coswot:Command ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:onProperty coswot:isExecutionOf ],  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;coswot:ProcedureExecution .</code></pre>|
|[Section top](#minorfail-outcome-number-104)|Pointer|<pre lang="Turtle"><code>coswot:CommandKind a owl:Class ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;Command Kind&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:comment &#34;The lowest-level directives a function exposes to some netwo...&#34; ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy &#60;https://w3id.org/coswot/core/functions&lowbar;commands> ;  &#10;&#32;&#32;&#32;&#32;rdfs:subClassOf &#91; a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:allValuesFrom coswot:CommandKind ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:onProperty skos:broader ],  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#91; a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:allValuesFrom coswot:CommandKind ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:onProperty skos:narrower ],  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#91; a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:allValuesFrom owl:Nothing ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:onProperty coswot:hasKind ],  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#91; owl:allValuesFrom coswot:FunctionKind ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:onProperty coswot:isCommandOf ],  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;coswot:Command ;  &#10;&#32;&#32;&#32;&#32;skos:example &#34;Observe property, control property, observe state, control s...&#34; .</code></pre>|
|[Section top](#minorfail-outcome-number-104)|Pointer|<pre lang="Turtle"><code>coswot:CommandOfInterest a owl:Class ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;Command Of Interest&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:comment &#34;The lowest-level directives a device supports and exposes to...&#34; ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy &#60;https://w3id.org/coswot/core/functions&lowbar;commands> ;  &#10;&#32;&#32;&#32;&#32;rdfs:subClassOf &#91; a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:allValuesFrom coswot:CommandKind ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:onProperty coswot:hasKind ],  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#91; a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:onProperty coswot:hasKind ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:someValuesFrom coswot:CommandKind ],  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#91; a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:onProperty coswot:isCommandOfInterestOf ],  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;coswot:Command ;  &#10;&#32;&#32;&#32;&#32;skos:example &#34;The corridor smart light switch supports a command of kind “...&#34;,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#34;The smart fridge supports a command of kind “observe tempera...&#34; ;  &#10;&#32;&#32;&#32;&#32;skos:note &#34;Commands of interest need not always be explicited. It depen...&#34;,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#34;Like for commands, commands of interest may be described in ...&#34; .</code></pre>|
|[Section top](#minorfail-outcome-number-104)|Pointer|<pre lang="Turtle"><code>coswot:DeviceKind rdfs:subClassOf &#91; a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:allValuesFrom coswot:FunctionKind ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:onProperty coswot:hasFunction ] .</code></pre>|
|[Section top](#minorfail-outcome-number-104)|Pointer|<pre lang="Turtle"><code>coswot:FunctionKind a owl:Class ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;Function Kind&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:comment &#34;Logical groups of commands that devices support to accomplis...&#34; ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy &#60;https://w3id.org/coswot/core/functions&lowbar;commands> ;  &#10;&#32;&#32;&#32;&#32;rdfs:subClassOf &#91; a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:allValuesFrom coswot:FunctionKind ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:onProperty skos:broader ],  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#91; a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:allValuesFrom coswot:FunctionKind ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:onProperty skos:narrower ],  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#91; a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:allValuesFrom owl:Nothing ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:onProperty coswot:hasKind ],  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#91; a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:allValuesFrom coswot:DeviceKind ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:onProperty coswot:isFunctionOf ],  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#91; owl:allValuesFrom coswot:CommandKind ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:onProperty coswot:hasCommand ],  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;coswot:Function .</code></pre>|
|[Section top](#minorfail-outcome-number-104)|Pointer|<pre lang="Turtle"><code>coswot:FunctionOfInterest a owl:Class ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;Function of Interest&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:comment &#34;Logical groups of commands that devices support to accomplis...&#34; ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy &#60;https://w3id.org/coswot/core/functions&lowbar;commands> ;  &#10;&#32;&#32;&#32;&#32;rdfs:subClassOf &#91; a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:allValuesFrom coswot:FunctionKind ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:onProperty coswot:hasKind ],  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#91; a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:onProperty coswot:hasKind ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:someValuesFrom coswot:FunctionKind ],  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#91; a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:onProperty coswot:isFunctionOfInterestOf ],  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;coswot:Function ;  &#10;&#32;&#32;&#32;&#32;skos:note &#34;A function of interest is the function of (OP coswot:isFunct...&#34;,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#34;Functions of interest need not always be explicited. It depe...&#34; .</code></pre>|

***
### MinorFail Outcome number 105

[Jump to summary definition](#summary-MinorFail-105)	|	[Previous MinorFail outcome](#minorfail-outcome-number-104)	|	[Next MinorFail outcome](#minorfail-outcome-number-106)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-src-functions-commands-ontology|
|----|----|
|Title|Standalone module src/functions&lowbar;commands/ontology.ttl from branch main|
|Composition|- [Module functions&lowbar;commands/ontology](https://gitlab.com/coswot/coswot-acimov/blob/main/src/functions_commands/ontology.ttl)|

#### Criterion detail
|Identifier|[term-referencing](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#term-referencing)|
|----|----|
|Title|Term referencing test|
|Description|A test case from the Best Practices tests checking if each term of the test subject is referenced to a module through a rdfs:isDefinedBy property.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-105)|Identifier|`no-reference-module`|
|[Section top](#minorfail-outcome-number-105)|Title|Term not referenced to a module|
|[Section top](#minorfail-outcome-number-105)|Description|Subject terms not linked to a module by a rdfs:isDefinedBy property|
|[Section top](#minorfail-outcome-number-105)|Pointer|<pre lang="Turtle"><code>:DeviceKind rdfs:subClassOf &#91; a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:allValuesFrom :FunctionKind ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:onProperty :hasFunction ] .</code></pre>|
|[Section top](#minorfail-outcome-number-105)|Pointer|<pre lang="Turtle"><code>:isExecutionOf owl:propertyChainAxiom ( :isExecutionOf :hasKind ) .</code></pre>|

***
### MinorFail Outcome number 106

[Jump to summary definition](#summary-MinorFail-106)	|	[Previous MinorFail outcome](#minorfail-outcome-number-105)	|	[Next MinorFail outcome](#minorfail-outcome-number-107)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-src-features-ontology-catalogs|
|----|----|
|Title|Standalone module src/features/ontology.catalogs.ttl from branch main|
|Composition|- [Module features/ontology.catalogs](https://gitlab.com/coswot/coswot-acimov/blob/main/src/features/ontology.catalogs.ttl)|

#### Criterion detail
|Identifier|[profile-compatibility](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#profile-compatibility)|
|----|----|
|Title|Profile compatibility test|
|Description|A test meant to check whether the test subject is compatible with a profile or not, and if it is not, why.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-106)|Identifier|`owl-ql-profile-error`|
|[Section top](#minorfail-outcome-number-106)|Title|OWL QL Profile incompatible|
|[Section top](#minorfail-outcome-number-106)|Description|Class Expression not supported with rdfs:subClassOf|
|[Section top](#minorfail-outcome-number-106)|Pointer|<pre lang="Turtle"><code>coswot:FeatureKind a owl:Class ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;Feature kind&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:comment &#34;A Feature Kind represents an archetype of real world entitie...&#34; ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy &#60;https://w3id.org/coswot/core/features> ;  &#10;&#32;&#32;&#32;&#32;rdfs:subClassOf &#91; a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:allValuesFrom coswot:FeatureKind ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:onProperty skos:broader ],  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#91; a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:allValuesFrom coswot:FeatureKind ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:onProperty skos:narrower ],  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#91; a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:allValuesFrom coswot:FeatureKind ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:onProperty coswot:consistsOf ],  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;skos:Concept .</code></pre>|

***
### MinorFail Outcome number 107

[Jump to summary definition](#summary-MinorFail-107)	|	[Previous MinorFail outcome](#minorfail-outcome-number-106)	|	[Next MinorFail outcome](#minorfail-outcome-number-108)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-src-features-ontology-catalogs|
|----|----|
|Title|Standalone module src/features/ontology.catalogs.ttl from branch main|
|Composition|- [Module features/ontology.catalogs](https://gitlab.com/coswot/coswot-acimov/blob/main/src/features/ontology.catalogs.ttl)|

#### Criterion detail
|Identifier|[profile-compatibility](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#profile-compatibility)|
|----|----|
|Title|Profile compatibility test|
|Description|A test meant to check whether the test subject is compatible with a profile or not, and if it is not, why.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-107)|Identifier|`owl-ql-profile-error`|
|[Section top](#minorfail-outcome-number-107)|Title|OWL QL Profile incompatible|
|[Section top](#minorfail-outcome-number-107)|Description|Statement not supported in a Super Class Expression|
|[Section top](#minorfail-outcome-number-107)|Pointer|<pre lang="Turtle"><code>&#91;] a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;owl:allValuesFrom coswot:FeatureKind ;  &#10;&#32;&#32;&#32;&#32;owl:onProperty skos:broader .</code></pre>|
|[Section top](#minorfail-outcome-number-107)|Pointer|<pre lang="Turtle"><code>&#91;] a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;owl:allValuesFrom coswot:FeatureKind ;  &#10;&#32;&#32;&#32;&#32;owl:onProperty skos:narrower .</code></pre>|
|[Section top](#minorfail-outcome-number-107)|Pointer|<pre lang="Turtle"><code>&#91;] a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;owl:allValuesFrom coswot:FeatureKind ;  &#10;&#32;&#32;&#32;&#32;owl:onProperty coswot:consistsOf .</code></pre>|

***
### MinorFail Outcome number 108

[Jump to summary definition](#summary-MinorFail-108)	|	[Previous MinorFail outcome](#minorfail-outcome-number-107)	|	[Next MinorFail outcome](#minorfail-outcome-number-109)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-src-features-ontology-catalogs|
|----|----|
|Title|Standalone module src/features/ontology.catalogs.ttl from branch main|
|Composition|- [Module features/ontology.catalogs](https://gitlab.com/coswot/coswot-acimov/blob/main/src/features/ontology.catalogs.ttl)|

#### Criterion detail
|Identifier|[profile-compatibility](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#profile-compatibility)|
|----|----|
|Title|Profile compatibility test|
|Description|A test meant to check whether the test subject is compatible with a profile or not, and if it is not, why.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-108)|Identifier|`owl-el-profile-error`|
|[Section top](#minorfail-outcome-number-108)|Title|OWL EL Profile incompatible|
|[Section top](#minorfail-outcome-number-108)|Description|Statement not supported in a Class Expression|
|[Section top](#minorfail-outcome-number-108)|Pointer|<pre lang="Turtle"><code>&#91;] a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;owl:allValuesFrom coswot:FeatureKind ;  &#10;&#32;&#32;&#32;&#32;owl:onProperty skos:broader .</code></pre>|
|[Section top](#minorfail-outcome-number-108)|Pointer|<pre lang="Turtle"><code>&#91;] a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;owl:allValuesFrom coswot:FeatureKind ;  &#10;&#32;&#32;&#32;&#32;owl:onProperty skos:narrower .</code></pre>|
|[Section top](#minorfail-outcome-number-108)|Pointer|<pre lang="Turtle"><code>&#91;] a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;owl:allValuesFrom coswot:FeatureKind ;  &#10;&#32;&#32;&#32;&#32;owl:onProperty coswot:consistsOf .</code></pre>|

***
### MinorFail Outcome number 109

[Jump to summary definition](#summary-MinorFail-109)	|	[Previous MinorFail outcome](#minorfail-outcome-number-108)	|	[Next MinorFail outcome](#minorfail-outcome-number-110)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-src-features-ontology-catalogs|
|----|----|
|Title|Standalone module src/features/ontology.catalogs.ttl from branch main|
|Composition|- [Module features/ontology.catalogs](https://gitlab.com/coswot/coswot-acimov/blob/main/src/features/ontology.catalogs.ttl)|

#### Criterion detail
|Identifier|[profile-compatibility](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#profile-compatibility)|
|----|----|
|Title|Profile compatibility test|
|Description|A test meant to check whether the test subject is compatible with a profile or not, and if it is not, why.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-109)|Identifier|`owl-el-profile-error`|
|[Section top](#minorfail-outcome-number-109)|Title|OWL EL Profile incompatible|
|[Section top](#minorfail-outcome-number-109)|Description|Class Expression not supported with rdfs:subClassOf|
|[Section top](#minorfail-outcome-number-109)|Pointer|<pre lang="Turtle"><code>coswot:FeatureKind a owl:Class ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;Feature kind&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:comment &#34;A Feature Kind represents an archetype of real world entitie...&#34; ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy &#60;https://w3id.org/coswot/core/features> ;  &#10;&#32;&#32;&#32;&#32;rdfs:subClassOf &#91; a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:allValuesFrom coswot:FeatureKind ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:onProperty skos:broader ],  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#91; a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:allValuesFrom coswot:FeatureKind ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:onProperty skos:narrower ],  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#91; a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:allValuesFrom coswot:FeatureKind ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:onProperty coswot:consistsOf ],  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;skos:Concept .</code></pre>|

***
### MinorFail Outcome number 110

[Jump to summary definition](#summary-MinorFail-110)	|	[Previous MinorFail outcome](#minorfail-outcome-number-109)	|	[Next MinorFail outcome](#minorfail-outcome-number-111)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-src-features-ontology|
|----|----|
|Title|Standalone module src/features/ontology.ttl from branch main|
|Composition|- [Module features/ontology](https://gitlab.com/coswot/coswot-acimov/blob/main/src/features/ontology.ttl)|

#### Criterion detail
|Identifier|[profile-compatibility](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#profile-compatibility)|
|----|----|
|Title|Profile compatibility test|
|Description|A test meant to check whether the test subject is compatible with a profile or not, and if it is not, why.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-110)|Identifier|`owl-rl-profile-error`|
|[Section top](#minorfail-outcome-number-110)|Title|OWL RL Profile incompatible|
|[Section top](#minorfail-outcome-number-110)|Description|Class Expression not supported with rdfs:subClassOf|
|[Section top](#minorfail-outcome-number-110)|Pointer|<pre lang="Turtle"><code>coswot:FeatureOfInterest a owl:Class ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;Feature of interest&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:comment &#34;A feature of interest represents one specific real world ent...&#34; ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy &#60;https://w3id.org/coswot/core/features> ;  &#10;&#32;&#32;&#32;&#32;rdfs:subClassOf &#91; a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:allValuesFrom coswot:FeatureKind ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:onProperty coswot:hasKind ],  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#91; a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:onProperty coswot:hasKind ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:someValuesFrom coswot:FeatureKind ],  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#91; a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:allValuesFrom coswot:FeatureOfInterest ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:onProperty coswot:consistsOf ],  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;coswot:Feature .</code></pre>|

***
### MinorFail Outcome number 111

[Jump to summary definition](#summary-MinorFail-111)	|	[Previous MinorFail outcome](#minorfail-outcome-number-110)	|	[Next MinorFail outcome](#minorfail-outcome-number-112)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-src-features-ontology|
|----|----|
|Title|Standalone module src/features/ontology.ttl from branch main|
|Composition|- [Module features/ontology](https://gitlab.com/coswot/coswot-acimov/blob/main/src/features/ontology.ttl)|

#### Criterion detail
|Identifier|[profile-compatibility](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#profile-compatibility)|
|----|----|
|Title|Profile compatibility test|
|Description|A test meant to check whether the test subject is compatible with a profile or not, and if it is not, why.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-111)|Identifier|`owl-rl-profile-error`|
|[Section top](#minorfail-outcome-number-111)|Title|OWL RL Profile incompatible|
|[Section top](#minorfail-outcome-number-111)|Description|Statement not supported|
|[Section top](#minorfail-outcome-number-111)|Pointer|<pre lang="Turtle"><code>coswot:Feature a owl:Class ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;Feature&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:comment &#34;Real world entities from which a property or a state may be ...&#34; ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy &#60;https://w3id.org/coswot/core/features> ;  &#10;&#32;&#32;&#32;&#32;owl:disjointUnionOf ( coswot:FeatureOfInterest coswot:FeatureKind ) .</code></pre>|

***
### MinorFail Outcome number 112

[Jump to summary definition](#summary-MinorFail-112)	|	[Previous MinorFail outcome](#minorfail-outcome-number-111)	|	[Next MinorFail outcome](#minorfail-outcome-number-113)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-src-features-ontology|
|----|----|
|Title|Standalone module src/features/ontology.ttl from branch main|
|Composition|- [Module features/ontology](https://gitlab.com/coswot/coswot-acimov/blob/main/src/features/ontology.ttl)|

#### Criterion detail
|Identifier|[profile-compatibility](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#profile-compatibility)|
|----|----|
|Title|Profile compatibility test|
|Description|A test meant to check whether the test subject is compatible with a profile or not, and if it is not, why.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-112)|Identifier|`owl-rl-profile-error`|
|[Section top](#minorfail-outcome-number-112)|Title|OWL RL Profile incompatible|
|[Section top](#minorfail-outcome-number-112)|Description|Statement not supported in a Super Class Expression|
|[Section top](#minorfail-outcome-number-112)|Pointer|<pre lang="Turtle"><code>&#91;] a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;owl:onProperty coswot:hasKind ;  &#10;&#32;&#32;&#32;&#32;owl:someValuesFrom coswot:FeatureKind .</code></pre>|

***
### MinorFail Outcome number 113

[Jump to summary definition](#summary-MinorFail-113)	|	[Previous MinorFail outcome](#minorfail-outcome-number-112)	|	[Next MinorFail outcome](#minorfail-outcome-number-114)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-src-features-ontology|
|----|----|
|Title|Standalone module src/features/ontology.ttl from branch main|
|Composition|- [Module features/ontology](https://gitlab.com/coswot/coswot-acimov/blob/main/src/features/ontology.ttl)|

#### Criterion detail
|Identifier|[profile-compatibility](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#profile-compatibility)|
|----|----|
|Title|Profile compatibility test|
|Description|A test meant to check whether the test subject is compatible with a profile or not, and if it is not, why.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-113)|Identifier|`owl-ql-profile-error`|
|[Section top](#minorfail-outcome-number-113)|Title|OWL QL Profile incompatible|
|[Section top](#minorfail-outcome-number-113)|Description|Class Expression not supported with rdfs:subClassOf|
|[Section top](#minorfail-outcome-number-113)|Pointer|<pre lang="Turtle"><code>coswot:FeatureKind a owl:Class ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;Feature kind&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:comment &#34;A Feature Kind represents an archetype of real world entitie...&#34; ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy &#60;https://w3id.org/coswot/core/features> ;  &#10;&#32;&#32;&#32;&#32;rdfs:subClassOf &#91; a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:allValuesFrom coswot:FeatureKind ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:onProperty skos:broader ],  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#91; a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:allValuesFrom coswot:FeatureKind ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:onProperty skos:narrower ],  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#91; a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:allValuesFrom owl:Nothing ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:onProperty coswot:hasKind ],  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#91; a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:allValuesFrom coswot:FeatureKind ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:onProperty coswot:consistsOf ],  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;skos:Concept,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;coswot:Feature .</code></pre>|
|[Section top](#minorfail-outcome-number-113)|Pointer|<pre lang="Turtle"><code>coswot:FeatureOfInterest a owl:Class ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;Feature of interest&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:comment &#34;A feature of interest represents one specific real world ent...&#34; ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy &#60;https://w3id.org/coswot/core/features> ;  &#10;&#32;&#32;&#32;&#32;rdfs:subClassOf &#91; a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:allValuesFrom coswot:FeatureKind ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:onProperty coswot:hasKind ],  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#91; a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:onProperty coswot:hasKind ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:someValuesFrom coswot:FeatureKind ],  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#91; a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:allValuesFrom coswot:FeatureOfInterest ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:onProperty coswot:consistsOf ],  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;coswot:Feature .</code></pre>|

***
### MinorFail Outcome number 114

[Jump to summary definition](#summary-MinorFail-114)	|	[Previous MinorFail outcome](#minorfail-outcome-number-113)	|	[Next MinorFail outcome](#minorfail-outcome-number-115)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-src-features-ontology|
|----|----|
|Title|Standalone module src/features/ontology.ttl from branch main|
|Composition|- [Module features/ontology](https://gitlab.com/coswot/coswot-acimov/blob/main/src/features/ontology.ttl)|

#### Criterion detail
|Identifier|[profile-compatibility](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#profile-compatibility)|
|----|----|
|Title|Profile compatibility test|
|Description|A test meant to check whether the test subject is compatible with a profile or not, and if it is not, why.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-114)|Identifier|`owl-ql-profile-error`|
|[Section top](#minorfail-outcome-number-114)|Title|OWL QL Profile incompatible|
|[Section top](#minorfail-outcome-number-114)|Description|Statement not supported|
|[Section top](#minorfail-outcome-number-114)|Pointer|<pre lang="Turtle"><code>coswot:Feature a owl:Class ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;Feature&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:comment &#34;Real world entities from which a property or a state may be ...&#34; ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy &#60;https://w3id.org/coswot/core/features> ;  &#10;&#32;&#32;&#32;&#32;owl:disjointUnionOf ( coswot:FeatureOfInterest coswot:FeatureKind ) .</code></pre>|

***
### MinorFail Outcome number 115

[Jump to summary definition](#summary-MinorFail-115)	|	[Previous MinorFail outcome](#minorfail-outcome-number-114)	|	[Next MinorFail outcome](#minorfail-outcome-number-116)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-src-features-ontology|
|----|----|
|Title|Standalone module src/features/ontology.ttl from branch main|
|Composition|- [Module features/ontology](https://gitlab.com/coswot/coswot-acimov/blob/main/src/features/ontology.ttl)|

#### Criterion detail
|Identifier|[profile-compatibility](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#profile-compatibility)|
|----|----|
|Title|Profile compatibility test|
|Description|A test meant to check whether the test subject is compatible with a profile or not, and if it is not, why.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-115)|Identifier|`owl-ql-profile-error`|
|[Section top](#minorfail-outcome-number-115)|Title|OWL QL Profile incompatible|
|[Section top](#minorfail-outcome-number-115)|Description|Statement not supported in a Super Class Expression|
|[Section top](#minorfail-outcome-number-115)|Pointer|<pre lang="Turtle"><code>&#91;] a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;owl:allValuesFrom coswot:FeatureKind ;  &#10;&#32;&#32;&#32;&#32;owl:onProperty skos:broader .</code></pre>|
|[Section top](#minorfail-outcome-number-115)|Pointer|<pre lang="Turtle"><code>&#91;] a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;owl:allValuesFrom coswot:FeatureKind ;  &#10;&#32;&#32;&#32;&#32;owl:onProperty skos:narrower .</code></pre>|
|[Section top](#minorfail-outcome-number-115)|Pointer|<pre lang="Turtle"><code>&#91;] a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;owl:allValuesFrom owl:Nothing ;  &#10;&#32;&#32;&#32;&#32;owl:onProperty coswot:hasKind .</code></pre>|
|[Section top](#minorfail-outcome-number-115)|Pointer|<pre lang="Turtle"><code>&#91;] a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;owl:allValuesFrom coswot:FeatureKind ;  &#10;&#32;&#32;&#32;&#32;owl:onProperty coswot:hasKind .</code></pre>|
|[Section top](#minorfail-outcome-number-115)|Pointer|<pre lang="Turtle"><code>&#91;] a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;owl:allValuesFrom coswot:FeatureKind ;  &#10;&#32;&#32;&#32;&#32;owl:onProperty coswot:consistsOf .</code></pre>|
|[Section top](#minorfail-outcome-number-115)|Pointer|<pre lang="Turtle"><code>&#91;] a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;owl:allValuesFrom coswot:FeatureOfInterest ;  &#10;&#32;&#32;&#32;&#32;owl:onProperty coswot:consistsOf .</code></pre>|

***
### MinorFail Outcome number 116

[Jump to summary definition](#summary-MinorFail-116)	|	[Previous MinorFail outcome](#minorfail-outcome-number-115)	|	[Next MinorFail outcome](#minorfail-outcome-number-117)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-src-features-ontology|
|----|----|
|Title|Standalone module src/features/ontology.ttl from branch main|
|Composition|- [Module features/ontology](https://gitlab.com/coswot/coswot-acimov/blob/main/src/features/ontology.ttl)|

#### Criterion detail
|Identifier|[profile-compatibility](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#profile-compatibility)|
|----|----|
|Title|Profile compatibility test|
|Description|A test meant to check whether the test subject is compatible with a profile or not, and if it is not, why.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-116)|Identifier|`owl-ql-profile-error`|
|[Section top](#minorfail-outcome-number-116)|Title|OWL QL Profile incompatible|
|[Section top](#minorfail-outcome-number-116)|Description|Property inclusions involving property chains not supported|
|[Section top](#minorfail-outcome-number-116)|Pointer|<pre lang="Turtle"><code>coswot:hasKind a owl:ObjectProperty ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;has feature kind&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:comment &#34;links something of interest interest to its kind&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy &#60;https://w3id.org/coswot/core/features> ;  &#10;&#32;&#32;&#32;&#32;owl:propertyChainAxiom ( coswot:hasKind skos:broader ) .</code></pre>|

***
### MinorFail Outcome number 117

[Jump to summary definition](#summary-MinorFail-117)	|	[Previous MinorFail outcome](#minorfail-outcome-number-116)	|	[Next MinorFail outcome](#minorfail-outcome-number-118)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-src-features-ontology|
|----|----|
|Title|Standalone module src/features/ontology.ttl from branch main|
|Composition|- [Module features/ontology](https://gitlab.com/coswot/coswot-acimov/blob/main/src/features/ontology.ttl)|

#### Criterion detail
|Identifier|[profile-compatibility](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#profile-compatibility)|
|----|----|
|Title|Profile compatibility test|
|Description|A test meant to check whether the test subject is compatible with a profile or not, and if it is not, why.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-117)|Identifier|`owl-el-profile-error`|
|[Section top](#minorfail-outcome-number-117)|Title|OWL EL Profile incompatible|
|[Section top](#minorfail-outcome-number-117)|Description|Statement not supported in a Class Expression|
|[Section top](#minorfail-outcome-number-117)|Pointer|<pre lang="Turtle"><code>&#91;] a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;owl:allValuesFrom coswot:FeatureKind ;  &#10;&#32;&#32;&#32;&#32;owl:onProperty skos:broader .</code></pre>|
|[Section top](#minorfail-outcome-number-117)|Pointer|<pre lang="Turtle"><code>&#91;] a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;owl:allValuesFrom coswot:FeatureKind ;  &#10;&#32;&#32;&#32;&#32;owl:onProperty skos:narrower .</code></pre>|
|[Section top](#minorfail-outcome-number-117)|Pointer|<pre lang="Turtle"><code>&#91;] a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;owl:allValuesFrom owl:Nothing ;  &#10;&#32;&#32;&#32;&#32;owl:onProperty coswot:hasKind .</code></pre>|
|[Section top](#minorfail-outcome-number-117)|Pointer|<pre lang="Turtle"><code>&#91;] a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;owl:allValuesFrom coswot:FeatureKind ;  &#10;&#32;&#32;&#32;&#32;owl:onProperty coswot:hasKind .</code></pre>|
|[Section top](#minorfail-outcome-number-117)|Pointer|<pre lang="Turtle"><code>&#91;] a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;owl:allValuesFrom coswot:FeatureKind ;  &#10;&#32;&#32;&#32;&#32;owl:onProperty coswot:consistsOf .</code></pre>|
|[Section top](#minorfail-outcome-number-117)|Pointer|<pre lang="Turtle"><code>&#91;] a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;owl:allValuesFrom coswot:FeatureOfInterest ;  &#10;&#32;&#32;&#32;&#32;owl:onProperty coswot:consistsOf .</code></pre>|

***
### MinorFail Outcome number 118

[Jump to summary definition](#summary-MinorFail-118)	|	[Previous MinorFail outcome](#minorfail-outcome-number-117)	|	[Next MinorFail outcome](#minorfail-outcome-number-119)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-src-features-ontology|
|----|----|
|Title|Standalone module src/features/ontology.ttl from branch main|
|Composition|- [Module features/ontology](https://gitlab.com/coswot/coswot-acimov/blob/main/src/features/ontology.ttl)|

#### Criterion detail
|Identifier|[profile-compatibility](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#profile-compatibility)|
|----|----|
|Title|Profile compatibility test|
|Description|A test meant to check whether the test subject is compatible with a profile or not, and if it is not, why.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-118)|Identifier|`owl-el-profile-error`|
|[Section top](#minorfail-outcome-number-118)|Title|OWL EL Profile incompatible|
|[Section top](#minorfail-outcome-number-118)|Description|Statement not supported|
|[Section top](#minorfail-outcome-number-118)|Pointer|<pre lang="Turtle"><code>coswot:Feature a owl:Class ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;Feature&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:comment &#34;Real world entities from which a property or a state may be ...&#34; ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy &#60;https://w3id.org/coswot/core/features> ;  &#10;&#32;&#32;&#32;&#32;owl:disjointUnionOf ( coswot:FeatureOfInterest coswot:FeatureKind ) .</code></pre>|

***
### MinorFail Outcome number 119

[Jump to summary definition](#summary-MinorFail-119)	|	[Previous MinorFail outcome](#minorfail-outcome-number-118)	|	[Next MinorFail outcome](#minorfail-outcome-number-120)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-src-features-ontology|
|----|----|
|Title|Standalone module src/features/ontology.ttl from branch main|
|Composition|- [Module features/ontology](https://gitlab.com/coswot/coswot-acimov/blob/main/src/features/ontology.ttl)|

#### Criterion detail
|Identifier|[profile-compatibility](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#profile-compatibility)|
|----|----|
|Title|Profile compatibility test|
|Description|A test meant to check whether the test subject is compatible with a profile or not, and if it is not, why.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-119)|Identifier|`owl-el-profile-error`|
|[Section top](#minorfail-outcome-number-119)|Title|OWL EL Profile incompatible|
|[Section top](#minorfail-outcome-number-119)|Description|Class Expression not supported with rdfs:subClassOf|
|[Section top](#minorfail-outcome-number-119)|Pointer|<pre lang="Turtle"><code>coswot:FeatureKind a owl:Class ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;Feature kind&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:comment &#34;A Feature Kind represents an archetype of real world entitie...&#34; ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy &#60;https://w3id.org/coswot/core/features> ;  &#10;&#32;&#32;&#32;&#32;rdfs:subClassOf &#91; a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:allValuesFrom coswot:FeatureKind ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:onProperty skos:broader ],  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#91; a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:allValuesFrom coswot:FeatureKind ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:onProperty skos:narrower ],  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#91; a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:allValuesFrom owl:Nothing ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:onProperty coswot:hasKind ],  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#91; a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:allValuesFrom coswot:FeatureKind ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:onProperty coswot:consistsOf ],  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;skos:Concept,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;coswot:Feature .</code></pre>|
|[Section top](#minorfail-outcome-number-119)|Pointer|<pre lang="Turtle"><code>coswot:FeatureOfInterest a owl:Class ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;Feature of interest&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:comment &#34;A feature of interest represents one specific real world ent...&#34; ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy &#60;https://w3id.org/coswot/core/features> ;  &#10;&#32;&#32;&#32;&#32;rdfs:subClassOf &#91; a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:allValuesFrom coswot:FeatureKind ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:onProperty coswot:hasKind ],  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#91; a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:onProperty coswot:hasKind ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:someValuesFrom coswot:FeatureKind ],  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#91; a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:allValuesFrom coswot:FeatureOfInterest ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:onProperty coswot:consistsOf ],  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;coswot:Feature .</code></pre>|

***
### MinorFail Outcome number 120

[Jump to summary definition](#summary-MinorFail-120)	|	[Previous MinorFail outcome](#minorfail-outcome-number-119)	|	[Next MinorFail outcome](#minorfail-outcome-number-121)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-src-devices-ontology|
|----|----|
|Title|Standalone module src/devices/ontology.ttl from branch main|
|Composition|- [Module devices/ontology](https://gitlab.com/coswot/coswot-acimov/blob/main/src/devices/ontology.ttl)|

#### Criterion detail
|Identifier|[profile-compatibility](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#profile-compatibility)|
|----|----|
|Title|Profile compatibility test|
|Description|A test meant to check whether the test subject is compatible with a profile or not, and if it is not, why.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-120)|Identifier|`owl-rl-profile-error`|
|[Section top](#minorfail-outcome-number-120)|Title|OWL RL Profile incompatible|
|[Section top](#minorfail-outcome-number-120)|Description|Class Expression not supported with rdfs:subClassOf|
|[Section top](#minorfail-outcome-number-120)|Pointer|<pre lang="Turtle"><code>coswot:DeviceOfInterest a owl:Class ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;Device&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:comment &#34;A tangible object designed to accomplish a particular task. ...&#34; ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy &#60;https://w3id.org/coswot/core/devices> ;  &#10;&#32;&#32;&#32;&#32;rdfs:subClassOf &#91; a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:allValuesFrom coswot:DeviceKind ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:onProperty coswot:hasKind ],  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#91; a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:onProperty coswot:hasKind ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:someValuesFrom coswot:DeviceKind ],  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;coswot:Device,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;coswot:FeatureOfInterest ;  &#10;&#32;&#32;&#32;&#32;skos:example &#34;Examples of devices are a light switch, a temperature sensor...&#34; .</code></pre>|

***
### MinorFail Outcome number 121

[Jump to summary definition](#summary-MinorFail-121)	|	[Previous MinorFail outcome](#minorfail-outcome-number-120)	|	[Next MinorFail outcome](#minorfail-outcome-number-122)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-src-devices-ontology|
|----|----|
|Title|Standalone module src/devices/ontology.ttl from branch main|
|Composition|- [Module devices/ontology](https://gitlab.com/coswot/coswot-acimov/blob/main/src/devices/ontology.ttl)|

#### Criterion detail
|Identifier|[profile-compatibility](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#profile-compatibility)|
|----|----|
|Title|Profile compatibility test|
|Description|A test meant to check whether the test subject is compatible with a profile or not, and if it is not, why.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-121)|Identifier|`owl-rl-profile-error`|
|[Section top](#minorfail-outcome-number-121)|Title|OWL RL Profile incompatible|
|[Section top](#minorfail-outcome-number-121)|Description|Statement not supported|
|[Section top](#minorfail-outcome-number-121)|Pointer|<pre lang="Turtle"><code>coswot:Device a owl:Class ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;Device&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:comment &#34;A tangible object designed to accomplish a particular task. ...&#34; ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy &#60;https://w3id.org/coswot/core/devices> ;  &#10;&#32;&#32;&#32;&#32;rdfs:subClassOf coswot:System ;  &#10;&#32;&#32;&#32;&#32;owl:disjointUnionOf ( coswot:DeviceOfInterest coswot:DeviceKind ) ;  &#10;&#32;&#32;&#32;&#32;skos:example &#34;Examples of devices are a light switch, a temperature sensor...&#34; .</code></pre>|

***
### MinorFail Outcome number 122

[Jump to summary definition](#summary-MinorFail-122)	|	[Previous MinorFail outcome](#minorfail-outcome-number-121)	|	[Next MinorFail outcome](#minorfail-outcome-number-123)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-src-devices-ontology|
|----|----|
|Title|Standalone module src/devices/ontology.ttl from branch main|
|Composition|- [Module devices/ontology](https://gitlab.com/coswot/coswot-acimov/blob/main/src/devices/ontology.ttl)|

#### Criterion detail
|Identifier|[profile-compatibility](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#profile-compatibility)|
|----|----|
|Title|Profile compatibility test|
|Description|A test meant to check whether the test subject is compatible with a profile or not, and if it is not, why.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-122)|Identifier|`owl-rl-profile-error`|
|[Section top](#minorfail-outcome-number-122)|Title|OWL RL Profile incompatible|
|[Section top](#minorfail-outcome-number-122)|Description|Statement not supported in a Super Class Expression|
|[Section top](#minorfail-outcome-number-122)|Pointer|<pre lang="Turtle"><code>&#91;] a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;owl:onProperty coswot:hasKind ;  &#10;&#32;&#32;&#32;&#32;owl:someValuesFrom coswot:DeviceKind .</code></pre>|
|[Section top](#minorfail-outcome-number-122)|Pointer|<pre lang="Turtle"><code>&#91;] a owl:Class ;  &#10;&#32;&#32;&#32;&#32;owl:unionOf ( coswot:Device coswot:Function coswot:Command coswot:ProcedureExecution ) .</code></pre>|
|[Section top](#minorfail-outcome-number-122)|Pointer|<pre lang="Turtle"><code>&#91;] a owl:Class ;  &#10;&#32;&#32;&#32;&#32;owl:unionOf ( coswot:Feature coswot:Property coswot:State ) .</code></pre>|

***
### MinorFail Outcome number 123

[Jump to summary definition](#summary-MinorFail-123)	|	[Previous MinorFail outcome](#minorfail-outcome-number-122)	|	[Next MinorFail outcome](#minorfail-outcome-number-124)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-src-devices-ontology|
|----|----|
|Title|Standalone module src/devices/ontology.ttl from branch main|
|Composition|- [Module devices/ontology](https://gitlab.com/coswot/coswot-acimov/blob/main/src/devices/ontology.ttl)|

#### Criterion detail
|Identifier|[profile-compatibility](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#profile-compatibility)|
|----|----|
|Title|Profile compatibility test|
|Description|A test meant to check whether the test subject is compatible with a profile or not, and if it is not, why.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-123)|Identifier|`owl-rl-profile-error`|
|[Section top](#minorfail-outcome-number-123)|Title|OWL RL Profile incompatible|
|[Section top](#minorfail-outcome-number-123)|Description|Class Expression not supported as object of rdfs:domain or rdfs:range|
|[Section top](#minorfail-outcome-number-123)|Pointer|<pre lang="Turtle"><code>coswot:isTargetOf a owl:ObjectProperty ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;is target of&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:comment &#34;Links a feature, property, or state, to the device, function...&#34; ;  &#10;&#32;&#32;&#32;&#32;rdfs:domain &#91; a owl:Class ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:unionOf ( coswot:Feature coswot:Property coswot:State ) ] ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy &#60;https://w3id.org/coswot/core/devices> ;  &#10;&#32;&#32;&#32;&#32;rdfs:range &#91; a owl:Class ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:unionOf ( coswot:Device coswot:Function coswot:Command coswot:ProcedureExecution ) ] ;  &#10;&#32;&#32;&#32;&#32;owl:inverseOf coswot:targets .</code></pre>|
|[Section top](#minorfail-outcome-number-123)|Pointer|<pre lang="Turtle"><code>coswot:targets a owl:ObjectProperty ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;targets&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:comment &#34;Links a device, function, command, or procedure execution, t...&#34; ;  &#10;&#32;&#32;&#32;&#32;rdfs:domain &#91; a owl:Class ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:unionOf ( coswot:Device coswot:Function coswot:Command coswot:ProcedureExecution ) ] ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy &#60;https://w3id.org/coswot/core/devices> ;  &#10;&#32;&#32;&#32;&#32;rdfs:range &#91; a owl:Class ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:unionOf ( coswot:Feature coswot:Property coswot:State ) ] .</code></pre>|

***
### MinorFail Outcome number 124

[Jump to summary definition](#summary-MinorFail-124)	|	[Previous MinorFail outcome](#minorfail-outcome-number-123)	|	[Next MinorFail outcome](#minorfail-outcome-number-125)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-src-devices-ontology|
|----|----|
|Title|Standalone module src/devices/ontology.ttl from branch main|
|Composition|- [Module devices/ontology](https://gitlab.com/coswot/coswot-acimov/blob/main/src/devices/ontology.ttl)|

#### Criterion detail
|Identifier|[profile-compatibility](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#profile-compatibility)|
|----|----|
|Title|Profile compatibility test|
|Description|A test meant to check whether the test subject is compatible with a profile or not, and if it is not, why.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-124)|Identifier|`owl-ql-profile-error`|
|[Section top](#minorfail-outcome-number-124)|Title|OWL QL Profile incompatible|
|[Section top](#minorfail-outcome-number-124)|Description|Class Expression not supported with rdfs:subClassOf|
|[Section top](#minorfail-outcome-number-124)|Pointer|<pre lang="Turtle"><code>coswot:DeviceKind a owl:Class ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;Device Kind&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:comment &#34;Device kinds allow to describe kinds of devices, with common...&#34; ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy &#60;https://w3id.org/coswot/core/devices> ;  &#10;&#32;&#32;&#32;&#32;rdfs:subClassOf &#91; a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:allValuesFrom coswot:FeatureKind ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:onProperty skos:broader ],  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#91; a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:allValuesFrom coswot:FeatureKind ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:onProperty skos:narrower ],  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#91; a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:allValuesFrom owl:Nothing ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:onProperty coswot:hasKind ],  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;coswot:Device,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;coswot:FeatureKind .</code></pre>|
|[Section top](#minorfail-outcome-number-124)|Pointer|<pre lang="Turtle"><code>coswot:DeviceOfInterest a owl:Class ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;Device&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:comment &#34;A tangible object designed to accomplish a particular task. ...&#34; ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy &#60;https://w3id.org/coswot/core/devices> ;  &#10;&#32;&#32;&#32;&#32;rdfs:subClassOf &#91; a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:allValuesFrom coswot:DeviceKind ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:onProperty coswot:hasKind ],  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#91; a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:onProperty coswot:hasKind ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:someValuesFrom coswot:DeviceKind ],  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;coswot:Device,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;coswot:FeatureOfInterest ;  &#10;&#32;&#32;&#32;&#32;skos:example &#34;Examples of devices are a light switch, a temperature sensor...&#34; .</code></pre>|

***
### MinorFail Outcome number 125

[Jump to summary definition](#summary-MinorFail-125)	|	[Previous MinorFail outcome](#minorfail-outcome-number-124)	|	[Next MinorFail outcome](#minorfail-outcome-number-126)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-src-devices-ontology|
|----|----|
|Title|Standalone module src/devices/ontology.ttl from branch main|
|Composition|- [Module devices/ontology](https://gitlab.com/coswot/coswot-acimov/blob/main/src/devices/ontology.ttl)|

#### Criterion detail
|Identifier|[profile-compatibility](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#profile-compatibility)|
|----|----|
|Title|Profile compatibility test|
|Description|A test meant to check whether the test subject is compatible with a profile or not, and if it is not, why.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-125)|Identifier|`owl-ql-profile-error`|
|[Section top](#minorfail-outcome-number-125)|Title|OWL QL Profile incompatible|
|[Section top](#minorfail-outcome-number-125)|Description|Statement not supported|
|[Section top](#minorfail-outcome-number-125)|Pointer|<pre lang="Turtle"><code>coswot:Device a owl:Class ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;Device&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:comment &#34;A tangible object designed to accomplish a particular task. ...&#34; ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy &#60;https://w3id.org/coswot/core/devices> ;  &#10;&#32;&#32;&#32;&#32;rdfs:subClassOf coswot:System ;  &#10;&#32;&#32;&#32;&#32;owl:disjointUnionOf ( coswot:DeviceOfInterest coswot:DeviceKind ) ;  &#10;&#32;&#32;&#32;&#32;skos:example &#34;Examples of devices are a light switch, a temperature sensor...&#34; .</code></pre>|

***
### MinorFail Outcome number 126

[Jump to summary definition](#summary-MinorFail-126)	|	[Previous MinorFail outcome](#minorfail-outcome-number-125)	|	[Next MinorFail outcome](#minorfail-outcome-number-127)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-src-devices-ontology|
|----|----|
|Title|Standalone module src/devices/ontology.ttl from branch main|
|Composition|- [Module devices/ontology](https://gitlab.com/coswot/coswot-acimov/blob/main/src/devices/ontology.ttl)|

#### Criterion detail
|Identifier|[profile-compatibility](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#profile-compatibility)|
|----|----|
|Title|Profile compatibility test|
|Description|A test meant to check whether the test subject is compatible with a profile or not, and if it is not, why.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-126)|Identifier|`owl-ql-profile-error`|
|[Section top](#minorfail-outcome-number-126)|Title|OWL QL Profile incompatible|
|[Section top](#minorfail-outcome-number-126)|Description|Statement not supported in a Super Class Expression|
|[Section top](#minorfail-outcome-number-126)|Pointer|<pre lang="Turtle"><code>&#91;] a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;owl:allValuesFrom coswot:FeatureKind ;  &#10;&#32;&#32;&#32;&#32;owl:onProperty skos:broader .</code></pre>|
|[Section top](#minorfail-outcome-number-126)|Pointer|<pre lang="Turtle"><code>&#91;] a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;owl:allValuesFrom coswot:FeatureKind ;  &#10;&#32;&#32;&#32;&#32;owl:onProperty skos:narrower .</code></pre>|
|[Section top](#minorfail-outcome-number-126)|Pointer|<pre lang="Turtle"><code>&#91;] a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;owl:allValuesFrom owl:Nothing ;  &#10;&#32;&#32;&#32;&#32;owl:onProperty coswot:hasKind .</code></pre>|
|[Section top](#minorfail-outcome-number-126)|Pointer|<pre lang="Turtle"><code>&#91;] a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;owl:allValuesFrom coswot:DeviceKind ;  &#10;&#32;&#32;&#32;&#32;owl:onProperty coswot:hasKind .</code></pre>|
|[Section top](#minorfail-outcome-number-126)|Pointer|<pre lang="Turtle"><code>&#91;] a owl:Class ;  &#10;&#32;&#32;&#32;&#32;owl:unionOf ( coswot:Device coswot:Function coswot:Command coswot:ProcedureExecution ) .</code></pre>|
|[Section top](#minorfail-outcome-number-126)|Pointer|<pre lang="Turtle"><code>&#91;] a owl:Class ;  &#10;&#32;&#32;&#32;&#32;owl:unionOf ( coswot:Feature coswot:Property coswot:State ) .</code></pre>|

***
### MinorFail Outcome number 127

[Jump to summary definition](#summary-MinorFail-127)	|	[Previous MinorFail outcome](#minorfail-outcome-number-126)	|	[Next MinorFail outcome](#minorfail-outcome-number-128)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-src-devices-ontology|
|----|----|
|Title|Standalone module src/devices/ontology.ttl from branch main|
|Composition|- [Module devices/ontology](https://gitlab.com/coswot/coswot-acimov/blob/main/src/devices/ontology.ttl)|

#### Criterion detail
|Identifier|[profile-compatibility](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#profile-compatibility)|
|----|----|
|Title|Profile compatibility test|
|Description|A test meant to check whether the test subject is compatible with a profile or not, and if it is not, why.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-127)|Identifier|`owl-ql-profile-error`|
|[Section top](#minorfail-outcome-number-127)|Title|OWL QL Profile incompatible|
|[Section top](#minorfail-outcome-number-127)|Description|Class Expression not supported as object of rdfs:domain or rdfs:range|
|[Section top](#minorfail-outcome-number-127)|Pointer|<pre lang="Turtle"><code>coswot:isTargetOf a owl:ObjectProperty ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;is target of&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:comment &#34;Links a feature, property, or state, to the device, function...&#34; ;  &#10;&#32;&#32;&#32;&#32;rdfs:domain &#91; a owl:Class ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:unionOf ( coswot:Feature coswot:Property coswot:State ) ] ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy &#60;https://w3id.org/coswot/core/devices> ;  &#10;&#32;&#32;&#32;&#32;rdfs:range &#91; a owl:Class ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:unionOf ( coswot:Device coswot:Function coswot:Command coswot:ProcedureExecution ) ] ;  &#10;&#32;&#32;&#32;&#32;owl:inverseOf coswot:targets .</code></pre>|
|[Section top](#minorfail-outcome-number-127)|Pointer|<pre lang="Turtle"><code>coswot:targets a owl:ObjectProperty ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;targets&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:comment &#34;Links a device, function, command, or procedure execution, t...&#34; ;  &#10;&#32;&#32;&#32;&#32;rdfs:domain &#91; a owl:Class ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:unionOf ( coswot:Device coswot:Function coswot:Command coswot:ProcedureExecution ) ] ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy &#60;https://w3id.org/coswot/core/devices> ;  &#10;&#32;&#32;&#32;&#32;rdfs:range &#91; a owl:Class ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:unionOf ( coswot:Feature coswot:Property coswot:State ) ] .</code></pre>|

***
### MinorFail Outcome number 128

[Jump to summary definition](#summary-MinorFail-128)	|	[Previous MinorFail outcome](#minorfail-outcome-number-127)	|	[Next MinorFail outcome](#minorfail-outcome-number-129)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-src-devices-ontology|
|----|----|
|Title|Standalone module src/devices/ontology.ttl from branch main|
|Composition|- [Module devices/ontology](https://gitlab.com/coswot/coswot-acimov/blob/main/src/devices/ontology.ttl)|

#### Criterion detail
|Identifier|[profile-compatibility](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#profile-compatibility)|
|----|----|
|Title|Profile compatibility test|
|Description|A test meant to check whether the test subject is compatible with a profile or not, and if it is not, why.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-128)|Identifier|`owl-el-profile-error`|
|[Section top](#minorfail-outcome-number-128)|Title|OWL EL Profile incompatible|
|[Section top](#minorfail-outcome-number-128)|Description|Statement not supported in a Class Expression|
|[Section top](#minorfail-outcome-number-128)|Pointer|<pre lang="Turtle"><code>&#91;] a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;owl:allValuesFrom coswot:FeatureKind ;  &#10;&#32;&#32;&#32;&#32;owl:onProperty skos:broader .</code></pre>|
|[Section top](#minorfail-outcome-number-128)|Pointer|<pre lang="Turtle"><code>&#91;] a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;owl:allValuesFrom coswot:FeatureKind ;  &#10;&#32;&#32;&#32;&#32;owl:onProperty skos:narrower .</code></pre>|
|[Section top](#minorfail-outcome-number-128)|Pointer|<pre lang="Turtle"><code>&#91;] a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;owl:allValuesFrom owl:Nothing ;  &#10;&#32;&#32;&#32;&#32;owl:onProperty coswot:hasKind .</code></pre>|
|[Section top](#minorfail-outcome-number-128)|Pointer|<pre lang="Turtle"><code>&#91;] a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;owl:allValuesFrom coswot:DeviceKind ;  &#10;&#32;&#32;&#32;&#32;owl:onProperty coswot:hasKind .</code></pre>|
|[Section top](#minorfail-outcome-number-128)|Pointer|<pre lang="Turtle"><code>&#91;] a owl:Class ;  &#10;&#32;&#32;&#32;&#32;owl:unionOf ( coswot:Device coswot:Function coswot:Command coswot:ProcedureExecution ) .</code></pre>|
|[Section top](#minorfail-outcome-number-128)|Pointer|<pre lang="Turtle"><code>&#91;] a owl:Class ;  &#10;&#32;&#32;&#32;&#32;owl:unionOf ( coswot:Feature coswot:Property coswot:State ) .</code></pre>|

***
### MinorFail Outcome number 129

[Jump to summary definition](#summary-MinorFail-129)	|	[Previous MinorFail outcome](#minorfail-outcome-number-128)	|	[Next MinorFail outcome](#minorfail-outcome-number-130)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-src-devices-ontology|
|----|----|
|Title|Standalone module src/devices/ontology.ttl from branch main|
|Composition|- [Module devices/ontology](https://gitlab.com/coswot/coswot-acimov/blob/main/src/devices/ontology.ttl)|

#### Criterion detail
|Identifier|[profile-compatibility](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#profile-compatibility)|
|----|----|
|Title|Profile compatibility test|
|Description|A test meant to check whether the test subject is compatible with a profile or not, and if it is not, why.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-129)|Identifier|`owl-el-profile-error`|
|[Section top](#minorfail-outcome-number-129)|Title|OWL EL Profile incompatible|
|[Section top](#minorfail-outcome-number-129)|Description|Statement not supported|
|[Section top](#minorfail-outcome-number-129)|Pointer|<pre lang="Turtle"><code>coswot:Device a owl:Class ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;Device&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:comment &#34;A tangible object designed to accomplish a particular task. ...&#34; ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy &#60;https://w3id.org/coswot/core/devices> ;  &#10;&#32;&#32;&#32;&#32;rdfs:subClassOf coswot:System ;  &#10;&#32;&#32;&#32;&#32;owl:disjointUnionOf ( coswot:DeviceOfInterest coswot:DeviceKind ) ;  &#10;&#32;&#32;&#32;&#32;skos:example &#34;Examples of devices are a light switch, a temperature sensor...&#34; .</code></pre>|

***
### MinorFail Outcome number 130

[Jump to summary definition](#summary-MinorFail-130)	|	[Previous MinorFail outcome](#minorfail-outcome-number-129)	|	[Next MinorFail outcome](#minorfail-outcome-number-131)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-src-devices-ontology|
|----|----|
|Title|Standalone module src/devices/ontology.ttl from branch main|
|Composition|- [Module devices/ontology](https://gitlab.com/coswot/coswot-acimov/blob/main/src/devices/ontology.ttl)|

#### Criterion detail
|Identifier|[profile-compatibility](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#profile-compatibility)|
|----|----|
|Title|Profile compatibility test|
|Description|A test meant to check whether the test subject is compatible with a profile or not, and if it is not, why.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-130)|Identifier|`owl-el-profile-error`|
|[Section top](#minorfail-outcome-number-130)|Title|OWL EL Profile incompatible|
|[Section top](#minorfail-outcome-number-130)|Description|Class Expression not supported as object of rdfs:domain or rdfs:range|
|[Section top](#minorfail-outcome-number-130)|Pointer|<pre lang="Turtle"><code>coswot:isTargetOf a owl:ObjectProperty ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;is target of&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:comment &#34;Links a feature, property, or state, to the device, function...&#34; ;  &#10;&#32;&#32;&#32;&#32;rdfs:domain &#91; a owl:Class ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:unionOf ( coswot:Feature coswot:Property coswot:State ) ] ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy &#60;https://w3id.org/coswot/core/devices> ;  &#10;&#32;&#32;&#32;&#32;rdfs:range &#91; a owl:Class ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:unionOf ( coswot:Device coswot:Function coswot:Command coswot:ProcedureExecution ) ] ;  &#10;&#32;&#32;&#32;&#32;owl:inverseOf coswot:targets .</code></pre>|
|[Section top](#minorfail-outcome-number-130)|Pointer|<pre lang="Turtle"><code>coswot:targets a owl:ObjectProperty ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;targets&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:comment &#34;Links a device, function, command, or procedure execution, t...&#34; ;  &#10;&#32;&#32;&#32;&#32;rdfs:domain &#91; a owl:Class ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:unionOf ( coswot:Device coswot:Function coswot:Command coswot:ProcedureExecution ) ] ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy &#60;https://w3id.org/coswot/core/devices> ;  &#10;&#32;&#32;&#32;&#32;rdfs:range &#91; a owl:Class ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:unionOf ( coswot:Feature coswot:Property coswot:State ) ] .</code></pre>|

***
### MinorFail Outcome number 131

[Jump to summary definition](#summary-MinorFail-131)	|	[Previous MinorFail outcome](#minorfail-outcome-number-130)	|	[Next MinorFail outcome](#minorfail-outcome-number-132)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-src-devices-ontology|
|----|----|
|Title|Standalone module src/devices/ontology.ttl from branch main|
|Composition|- [Module devices/ontology](https://gitlab.com/coswot/coswot-acimov/blob/main/src/devices/ontology.ttl)|

#### Criterion detail
|Identifier|[profile-compatibility](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#profile-compatibility)|
|----|----|
|Title|Profile compatibility test|
|Description|A test meant to check whether the test subject is compatible with a profile or not, and if it is not, why.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-131)|Identifier|`owl-el-profile-error`|
|[Section top](#minorfail-outcome-number-131)|Title|OWL EL Profile incompatible|
|[Section top](#minorfail-outcome-number-131)|Description|Class Expression not supported with rdfs:subClassOf|
|[Section top](#minorfail-outcome-number-131)|Pointer|<pre lang="Turtle"><code>coswot:DeviceKind a owl:Class ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;Device Kind&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:comment &#34;Device kinds allow to describe kinds of devices, with common...&#34; ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy &#60;https://w3id.org/coswot/core/devices> ;  &#10;&#32;&#32;&#32;&#32;rdfs:subClassOf &#91; a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:allValuesFrom coswot:FeatureKind ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:onProperty skos:broader ],  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#91; a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:allValuesFrom coswot:FeatureKind ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:onProperty skos:narrower ],  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#91; a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:allValuesFrom owl:Nothing ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:onProperty coswot:hasKind ],  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;coswot:Device,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;coswot:FeatureKind .</code></pre>|
|[Section top](#minorfail-outcome-number-131)|Pointer|<pre lang="Turtle"><code>coswot:DeviceOfInterest a owl:Class ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;Device&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:comment &#34;A tangible object designed to accomplish a particular task. ...&#34; ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy &#60;https://w3id.org/coswot/core/devices> ;  &#10;&#32;&#32;&#32;&#32;rdfs:subClassOf &#91; a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:allValuesFrom coswot:DeviceKind ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:onProperty coswot:hasKind ],  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#91; a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:onProperty coswot:hasKind ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:someValuesFrom coswot:DeviceKind ],  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;coswot:Device,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;coswot:FeatureOfInterest ;  &#10;&#32;&#32;&#32;&#32;skos:example &#34;Examples of devices are a light switch, a temperature sensor...&#34; .</code></pre>|

***
### MinorFail Outcome number 132

[Jump to summary definition](#summary-MinorFail-132)	|	[Previous MinorFail outcome](#minorfail-outcome-number-131)	|	[Next MinorFail outcome](#minorfail-outcome-number-133)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-src-coswot-sosa|
|----|----|
|Title|Standalone module src/coswot-sosa.ttl from branch main|
|Composition|- [Module coswot-sosa](https://gitlab.com/coswot/coswot-acimov/blob/main/src/coswot-sosa.ttl)|

#### Criterion detail
|Identifier|[term-referencing](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#term-referencing)|
|----|----|
|Title|Term referencing test|
|Description|A test case from the Best Practices tests checking if each term of the test subject is referenced to a module through a rdfs:isDefinedBy property.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-132)|Identifier|`no-reference-module`|
|[Section top](#minorfail-outcome-number-132)|Title|Term not referenced to a module|
|[Section top](#minorfail-outcome-number-132)|Description|Subject terms not linked to a module by a rdfs:isDefinedBy property|
|[Section top](#minorfail-outcome-number-132)|Pointer|<pre lang="Turtle"><code>:hasResult rdfs:equivalentProperty sosa:hasResult .</code></pre>|
|[Section top](#minorfail-outcome-number-132)|Pointer|<pre lang="Turtle"><code>:SensorOfInterest rdfs:subClassOf sosa:Sensor .</code></pre>|
|[Section top](#minorfail-outcome-number-132)|Pointer|<pre lang="Turtle"><code>:Observation rdfs:subClassOf sosa:Observation .</code></pre>|
|[Section top](#minorfail-outcome-number-132)|Pointer|<pre lang="Turtle"><code>:CommunicationSystem rdfs:subClassOf sosa:System .</code></pre>|
|[Section top](#minorfail-outcome-number-132)|Pointer|<pre lang="Turtle"><code>:hasStartTime rdfs:subPropertyOf sosa:startTime .</code></pre>|
|[Section top](#minorfail-outcome-number-132)|Pointer|<pre lang="Turtle"><code>:hasResultTime rdfs:subPropertyOf sosa:resultTime .</code></pre>|
|[Section top](#minorfail-outcome-number-132)|Pointer|<pre lang="Turtle"><code>:hasPhenomenonTime rdfs:subPropertyOf sosa:phenomenonTime .</code></pre>|
|[Section top](#minorfail-outcome-number-132)|Pointer|<pre lang="Turtle"><code>:FeatureOfInterest owl:equivalentClass sosa:FeatureOfInterest .</code></pre>|
|[Section top](#minorfail-outcome-number-132)|Pointer|<pre lang="Turtle"><code>:PropertyOfInterest owl:equivalentClass sosa:PropertyOfInterest .</code></pre>|
|[Section top](#minorfail-outcome-number-132)|Pointer|<pre lang="Turtle"><code>:Sample owl:equivalentClass sosa:Sample .</code></pre>|
|[Section top](#minorfail-outcome-number-132)|Pointer|<pre lang="Turtle"><code>:PropertyKind owl:equivalentClass sosa:Property .</code></pre>|
|[Section top](#minorfail-outcome-number-132)|Pointer|<pre lang="Turtle"><code>:Procedure owl:equivalentClass sosa:Procedure .</code></pre>|
|[Section top](#minorfail-outcome-number-132)|Pointer|<pre lang="Turtle"><code>:ProcedureExecution owl:equivalentClass sosa:Execution .</code></pre>|
|[Section top](#minorfail-outcome-number-132)|Pointer|<pre lang="Turtle"><code>:ObservationCollection owl:equivalentClass sosa:ObservationCollection .</code></pre>|
|[Section top](#minorfail-outcome-number-132)|Pointer|<pre lang="Turtle"><code>:ActuatorOfInterest owl:equivalentClass sosa:Actuator .</code></pre>|
|[Section top](#minorfail-outcome-number-132)|Pointer|<pre lang="Turtle"><code>:SensorKind owl:equivalentClass sosa:SensorKind .</code></pre>|
|[Section top](#minorfail-outcome-number-132)|Pointer|<pre lang="Turtle"><code>:ActuatorKind owl:equivalentClass sosa:ActuatorKind .</code></pre>|
|[Section top](#minorfail-outcome-number-132)|Pointer|<pre lang="Turtle"><code>:Actuation owl:equivalentClass sosa:Actuation .</code></pre>|
|[Section top](#minorfail-outcome-number-132)|Pointer|<pre lang="Turtle"><code>:hasSample owl:equivalentProperty sosa:Sample .</code></pre>|
|[Section top](#minorfail-outcome-number-132)|Pointer|<pre lang="Turtle"><code>:isSampleOf owl:equivalentProperty sosa:isSampleOf .</code></pre>|
|[Section top](#minorfail-outcome-number-132)|Pointer|<pre lang="Turtle"><code>:hasMember owl:equivalentProperty sosa:hasMember .</code></pre>|

***
### MinorFail Outcome number 133

[Jump to summary definition](#summary-MinorFail-133)	|	[Previous MinorFail outcome](#minorfail-outcome-number-132)	|	[Next MinorFail outcome](#minorfail-outcome-number-134)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-src-communications-ontology|
|----|----|
|Title|Standalone module src/communications/ontology.ttl from branch main|
|Composition|- [Module communications/ontology](https://gitlab.com/coswot/coswot-acimov/blob/main/src/communications/ontology.ttl)|

#### Criterion detail
|Identifier|[profile-compatibility](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#profile-compatibility)|
|----|----|
|Title|Profile compatibility test|
|Description|A test meant to check whether the test subject is compatible with a profile or not, and if it is not, why.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-133)|Identifier|`owl-rl-profile-error`|
|[Section top](#minorfail-outcome-number-133)|Title|OWL RL Profile incompatible|
|[Section top](#minorfail-outcome-number-133)|Description|Class Expression not supported with rdfs:subClassOf|
|[Section top](#minorfail-outcome-number-133)|Pointer|<pre lang="Turtle"><code>coswot:Communication a owl:Class ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;Communication.&#34;@en,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#34;Communication&#34;@fr ;  &#10;&#32;&#32;&#32;&#32;rdfs:comment &#34;A communication occurs through a communicationMedium, convey...&#34;,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#34;une communication est produite à travers un média de communi...&#34; ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy &#60;https://w3id.org/coswot/core/communications> ;  &#10;&#32;&#32;&#32;&#32;rdfs:subClassOf &#91; owl:onProperty coswot:conveys ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:someValuesFrom coswot:Message ],  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#91; owl:onProperty coswot:hasMedium ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:someValuesFrom coswot:CommunicationMedium ],  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#91; owl:onProperty coswot:hasCommunicator ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:someValuesFrom coswot:CommunicationSystem ],  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#91; owl:onProperty coswot:hasCommunicator ],  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#91; owl:onProperty coswot:hasAddressee ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:someValuesFrom coswot:CommunicationSystem ],  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#91; owl:onProperty coswot:isAbout ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:someValuesFrom xsd:string ],  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;coswot:ProcedureExecution .</code></pre>|

***
### MinorFail Outcome number 134

[Jump to summary definition](#summary-MinorFail-134)	|	[Previous MinorFail outcome](#minorfail-outcome-number-133)	|	[Next MinorFail outcome](#minorfail-outcome-number-135)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-src-communications-ontology|
|----|----|
|Title|Standalone module src/communications/ontology.ttl from branch main|
|Composition|- [Module communications/ontology](https://gitlab.com/coswot/coswot-acimov/blob/main/src/communications/ontology.ttl)|

#### Criterion detail
|Identifier|[profile-compatibility](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#profile-compatibility)|
|----|----|
|Title|Profile compatibility test|
|Description|A test meant to check whether the test subject is compatible with a profile or not, and if it is not, why.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-134)|Identifier|`owl-rl-profile-error`|
|[Section top](#minorfail-outcome-number-134)|Title|OWL RL Profile incompatible|
|[Section top](#minorfail-outcome-number-134)|Description|Statement not supported in a Super Class Expression|
|[Section top](#minorfail-outcome-number-134)|Pointer|<pre lang="Turtle"><code>&#91;] owl:onProperty coswot:conveys ;  &#10;&#32;&#32;&#32;&#32;owl:someValuesFrom coswot:Message .</code></pre>|
|[Section top](#minorfail-outcome-number-134)|Pointer|<pre lang="Turtle"><code>&#91;] owl:onProperty coswot:hasMedium ;  &#10;&#32;&#32;&#32;&#32;owl:someValuesFrom coswot:CommunicationMedium .</code></pre>|
|[Section top](#minorfail-outcome-number-134)|Pointer|<pre lang="Turtle"><code>&#91;] owl:onProperty coswot:hasCommunicator ;  &#10;&#32;&#32;&#32;&#32;owl:someValuesFrom coswot:CommunicationSystem .</code></pre>|
|[Section top](#minorfail-outcome-number-134)|Pointer|<pre lang="Turtle"><code>&#91;] owl:onProperty coswot:hasCommunicator .</code></pre>|
|[Section top](#minorfail-outcome-number-134)|Pointer|<pre lang="Turtle"><code>&#91;] owl:onProperty coswot:hasAddressee ;  &#10;&#32;&#32;&#32;&#32;owl:someValuesFrom coswot:CommunicationSystem .</code></pre>|
|[Section top](#minorfail-outcome-number-134)|Pointer|<pre lang="Turtle"><code>&#91;] owl:onProperty coswot:isAbout ;  &#10;&#32;&#32;&#32;&#32;owl:someValuesFrom xsd:string .</code></pre>|

***
### MinorFail Outcome number 135

[Jump to summary definition](#summary-MinorFail-135)	|	[Previous MinorFail outcome](#minorfail-outcome-number-134)	|	[Next MinorFail outcome](#minorfail-outcome-number-136)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-src-communications-ontology|
|----|----|
|Title|Standalone module src/communications/ontology.ttl from branch main|
|Composition|- [Module communications/ontology](https://gitlab.com/coswot/coswot-acimov/blob/main/src/communications/ontology.ttl)|

#### Criterion detail
|Identifier|[profile-compatibility](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#profile-compatibility)|
|----|----|
|Title|Profile compatibility test|
|Description|A test meant to check whether the test subject is compatible with a profile or not, and if it is not, why.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-135)|Identifier|`owl-ql-profile-error`|
|[Section top](#minorfail-outcome-number-135)|Title|OWL QL Profile incompatible|
|[Section top](#minorfail-outcome-number-135)|Description|Class Expression not supported with rdfs:subClassOf|
|[Section top](#minorfail-outcome-number-135)|Pointer|<pre lang="Turtle"><code>coswot:Communication a owl:Class ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;Communication.&#34;@en,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#34;Communication&#34;@fr ;  &#10;&#32;&#32;&#32;&#32;rdfs:comment &#34;A communication occurs through a communicationMedium, convey...&#34;,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#34;une communication est produite à travers un média de communi...&#34; ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy &#60;https://w3id.org/coswot/core/communications> ;  &#10;&#32;&#32;&#32;&#32;rdfs:subClassOf &#91; owl:onProperty coswot:conveys ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:someValuesFrom coswot:Message ],  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#91; owl:onProperty coswot:hasMedium ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:someValuesFrom coswot:CommunicationMedium ],  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#91; owl:onProperty coswot:hasCommunicator ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:someValuesFrom coswot:CommunicationSystem ],  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#91; owl:onProperty coswot:hasCommunicator ],  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#91; owl:onProperty coswot:hasAddressee ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:someValuesFrom coswot:CommunicationSystem ],  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#91; owl:onProperty coswot:isAbout ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:someValuesFrom xsd:string ],  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;coswot:ProcedureExecution .</code></pre>|

***
### MinorFail Outcome number 136

[Jump to summary definition](#summary-MinorFail-136)	|	[Previous MinorFail outcome](#minorfail-outcome-number-135)	|	[Next MinorFail outcome](#minorfail-outcome-number-137)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-src-communications-ontology|
|----|----|
|Title|Standalone module src/communications/ontology.ttl from branch main|
|Composition|- [Module communications/ontology](https://gitlab.com/coswot/coswot-acimov/blob/main/src/communications/ontology.ttl)|

#### Criterion detail
|Identifier|[profile-compatibility](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#profile-compatibility)|
|----|----|
|Title|Profile compatibility test|
|Description|A test meant to check whether the test subject is compatible with a profile or not, and if it is not, why.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-136)|Identifier|`owl-ql-profile-error`|
|[Section top](#minorfail-outcome-number-136)|Title|OWL QL Profile incompatible|
|[Section top](#minorfail-outcome-number-136)|Description|Statement not supported in a Super Class Expression|
|[Section top](#minorfail-outcome-number-136)|Pointer|<pre lang="Turtle"><code>&#91;] owl:onProperty coswot:hasCommunicator .</code></pre>|

***
### MinorFail Outcome number 137

[Jump to summary definition](#summary-MinorFail-137)	|	[Previous MinorFail outcome](#minorfail-outcome-number-136)	|	[Next MinorFail outcome](#minorfail-outcome-number-138)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-src-communications-ontology|
|----|----|
|Title|Standalone module src/communications/ontology.ttl from branch main|
|Composition|- [Module communications/ontology](https://gitlab.com/coswot/coswot-acimov/blob/main/src/communications/ontology.ttl)|

#### Criterion detail
|Identifier|[profile-compatibility](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#profile-compatibility)|
|----|----|
|Title|Profile compatibility test|
|Description|A test meant to check whether the test subject is compatible with a profile or not, and if it is not, why.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-137)|Identifier|`owl-el-profile-error`|
|[Section top](#minorfail-outcome-number-137)|Title|OWL EL Profile incompatible|
|[Section top](#minorfail-outcome-number-137)|Description|Statement not supported in a Class Expression|
|[Section top](#minorfail-outcome-number-137)|Pointer|<pre lang="Turtle"><code>&#91;] owl:onProperty coswot:hasCommunicator .</code></pre>|

***
### MinorFail Outcome number 138

[Jump to summary definition](#summary-MinorFail-138)	|	[Previous MinorFail outcome](#minorfail-outcome-number-137)	|	[Next MinorFail outcome](#minorfail-outcome-number-139)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-src-communications-ontology|
|----|----|
|Title|Standalone module src/communications/ontology.ttl from branch main|
|Composition|- [Module communications/ontology](https://gitlab.com/coswot/coswot-acimov/blob/main/src/communications/ontology.ttl)|

#### Criterion detail
|Identifier|[profile-compatibility](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#profile-compatibility)|
|----|----|
|Title|Profile compatibility test|
|Description|A test meant to check whether the test subject is compatible with a profile or not, and if it is not, why.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-138)|Identifier|`owl-el-profile-error`|
|[Section top](#minorfail-outcome-number-138)|Title|OWL EL Profile incompatible|
|[Section top](#minorfail-outcome-number-138)|Description|Class Expression not supported with rdfs:subClassOf|
|[Section top](#minorfail-outcome-number-138)|Pointer|<pre lang="Turtle"><code>coswot:Communication a owl:Class ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;Communication.&#34;@en,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#34;Communication&#34;@fr ;  &#10;&#32;&#32;&#32;&#32;rdfs:comment &#34;A communication occurs through a communicationMedium, convey...&#34;,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#34;une communication est produite à travers un média de communi...&#34; ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy &#60;https://w3id.org/coswot/core/communications> ;  &#10;&#32;&#32;&#32;&#32;rdfs:subClassOf &#91; owl:onProperty coswot:conveys ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:someValuesFrom coswot:Message ],  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#91; owl:onProperty coswot:hasMedium ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:someValuesFrom coswot:CommunicationMedium ],  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#91; owl:onProperty coswot:hasCommunicator ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:someValuesFrom coswot:CommunicationSystem ],  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#91; owl:onProperty coswot:hasCommunicator ],  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#91; owl:onProperty coswot:hasAddressee ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:someValuesFrom coswot:CommunicationSystem ],  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#91; owl:onProperty coswot:isAbout ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:someValuesFrom xsd:string ],  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;coswot:ProcedureExecution .</code></pre>|

***
### MinorFail Outcome number 139

[Jump to summary definition](#summary-MinorFail-139)	|	[Previous MinorFail outcome](#minorfail-outcome-number-138)	|	[Next MinorFail outcome](#minorfail-outcome-number-140)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-src-aggregations-ontology|
|----|----|
|Title|Standalone module src/aggregations/ontology.ttl from branch main|
|Composition|- [Module aggregations/ontology](https://gitlab.com/coswot/coswot-acimov/blob/main/src/aggregations/ontology.ttl)|

#### Criterion detail
|Identifier|[domain-and-range-referencing](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#domain-and-range-referencing)|
|----|----|
|Title|Domain and range referencing test|
|Description|A test case from the Best Practices tests checking if all the ranges and domains from the test subject point to terms that are defined in the vocabulary.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-139)|Identifier|`range-out-of-vocabulary`|
|[Section top](#minorfail-outcome-number-139)|Title|Range out of vocabulary|
|[Section top](#minorfail-outcome-number-139)|Description|Some properties have a range out of the ontology|
|[Section top](#minorfail-outcome-number-139)|Pointer|<pre lang="Turtle"><code>:hasAggregationKind a owl:ObjectProperty ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;has aggregation kind&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:comment &#34;Links a property, state, or aggregation, to the kind of aggr...&#34; ;  &#10;&#32;&#32;&#32;&#32;rdfs:domain &lowbar;:n8a38cdbee9c3419994802ea775046383b1,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:Thing ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy &#60;https://w3id.org/coswot/core/aggregations> ;  &#10;&#32;&#32;&#32;&#32;rdfs:range &lowbar;:n8a38cdbee9c3419994802ea775046383b2,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:Thing,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;skos:Concept,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;:AggregationKind ;  &#10;&#32;&#32;&#32;&#32;rdfs:subPropertyOf :hasAggregationKind ;  &#10;&#32;&#32;&#32;&#32;owl:equivalentProperty :hasAggregationKind .  &#10;&lowbar;:n8a38cdbee9c3419994802ea775046383b3 rdf:first :Aggregation ;  &#10;&#32;&#32;&#32;&#32;rdf:rest ( :AggregationKind ) .  &#10;&lowbar;:n8a38cdbee9c3419994802ea775046383b5 rdf:first :State ;  &#10;&#32;&#32;&#32;&#32;rdf:rest &lowbar;:n8a38cdbee9c3419994802ea775046383b3 .  &#10;&lowbar;:n8a38cdbee9c3419994802ea775046383b6 rdf:first :Property ;  &#10;&#32;&#32;&#32;&#32;rdf:rest &lowbar;:n8a38cdbee9c3419994802ea775046383b5 .  &#10;&lowbar;:n8a38cdbee9c3419994802ea775046383b7 rdf:first :Aggregation ;  &#10;&#32;&#32;&#32;&#32;rdf:rest () .  &#10;&lowbar;:n8a38cdbee9c3419994802ea775046383b8 rdf:first :State ;  &#10;&#32;&#32;&#32;&#32;rdf:rest &lowbar;:n8a38cdbee9c3419994802ea775046383b7 .  &#10;&lowbar;:n8a38cdbee9c3419994802ea775046383b9 rdf:first :Property ;  &#10;&#32;&#32;&#32;&#32;rdf:rest &lowbar;:n8a38cdbee9c3419994802ea775046383b8 .  &#10;&lowbar;:n8a38cdbee9c3419994802ea775046383b1 a owl:Class ;  &#10;&#32;&#32;&#32;&#32;rdfs:subClassOf &lowbar;:n8a38cdbee9c3419994802ea775046383b1,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:Thing ;  &#10;&#32;&#32;&#32;&#32;owl:equivalentClass &lowbar;:n8a38cdbee9c3419994802ea775046383b1 ;  &#10;&#32;&#32;&#32;&#32;owl:unionOf &lowbar;:n8a38cdbee9c3419994802ea775046383b9 .  &#10;&lowbar;:n8a38cdbee9c3419994802ea775046383b2 a owl:Class ;  &#10;&#32;&#32;&#32;&#32;rdfs:subClassOf &lowbar;:n8a38cdbee9c3419994802ea775046383b2,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:Thing ;  &#10;&#32;&#32;&#32;&#32;owl:equivalentClass &lowbar;:n8a38cdbee9c3419994802ea775046383b2 ;  &#10;&#32;&#32;&#32;&#32;owl:unionOf &lowbar;:n8a38cdbee9c3419994802ea775046383b6 .</code></pre>|
|[Section top](#minorfail-outcome-number-139)|Pointer|<pre lang="Turtle"><code>:hasAggregationTime a owl:ObjectProperty ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;has aggregation time&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:comment &#34;Links a property, state, aggregation, or aggregation kind, t...&#34; ;  &#10;&#32;&#32;&#32;&#32;rdfs:domain &lowbar;:nb171652e698346cda9778749a89598efb1,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:Thing ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy &#60;https://w3id.org/coswot/core/aggregations> ;  &#10;&#32;&#32;&#32;&#32;rdfs:range time:TemporalInterval ;  &#10;&#32;&#32;&#32;&#32;rdfs:subPropertyOf :hasAggregationTime ;  &#10;&#32;&#32;&#32;&#32;owl:equivalentProperty :hasAggregationTime ;  &#10;&#32;&#32;&#32;&#32;owl:propertyChainAxiom ( :hasAggregationKind :hasAggregationTime ) .  &#10;&lowbar;:nb171652e698346cda9778749a89598efb4 rdf:first :Property ;  &#10;&#32;&#32;&#32;&#32;rdf:rest ( :State :Aggregation :AggregationKind ) .  &#10;&lowbar;:nb171652e698346cda9778749a89598efb1 a owl:Class ;  &#10;&#32;&#32;&#32;&#32;rdfs:subClassOf &lowbar;:nb171652e698346cda9778749a89598efb1,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:Thing ;  &#10;&#32;&#32;&#32;&#32;owl:equivalentClass &lowbar;:nb171652e698346cda9778749a89598efb1 ;  &#10;&#32;&#32;&#32;&#32;owl:unionOf &lowbar;:nb171652e698346cda9778749a89598efb4 .</code></pre>|
|[Section top](#minorfail-outcome-number-139)|Pointer|<pre lang="Turtle"><code></code></pre>|
|[Section top](#minorfail-outcome-number-139)|Pointer|http://www.w3.org/2004/02/skos/core#Concept|

***
### MinorFail Outcome number 140

[Jump to summary definition](#summary-MinorFail-140)	|	[Previous MinorFail outcome](#minorfail-outcome-number-139)	|	[Next MinorFail outcome](#minorfail-outcome-number-141)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-src-aggregations-ontology|
|----|----|
|Title|Standalone module src/aggregations/ontology.ttl from branch main|
|Composition|- [Module aggregations/ontology](https://gitlab.com/coswot/coswot-acimov/blob/main/src/aggregations/ontology.ttl)|

#### Criterion detail
|Identifier|[profile-compatibility](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#profile-compatibility)|
|----|----|
|Title|Profile compatibility test|
|Description|A test meant to check whether the test subject is compatible with a profile or not, and if it is not, why.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-140)|Identifier|`owl-rl-profile-error`|
|[Section top](#minorfail-outcome-number-140)|Title|OWL RL Profile incompatible|
|[Section top](#minorfail-outcome-number-140)|Description|Class Expression not supported with rdfs:subClassOf|
|[Section top](#minorfail-outcome-number-140)|Pointer|<pre lang="Turtle"><code>coswot:Aggregation a owl:Class ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;Aggregation&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:comment &#34;Observation that takes as input a collection of observations...&#34; ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy &#60;https://w3id.org/coswot/core/aggregations> ;  &#10;&#32;&#32;&#32;&#32;rdfs:subClassOf &#91; a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:onProperty coswot:hasInput ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:someValuesFrom coswot:ObservationCollection ],  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#91; a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:onProperty coswot:hasAggregationKind ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:someValuesFrom coswot:AggregationKind ],  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;coswot:Observation .</code></pre>|

***
### MinorFail Outcome number 141

[Jump to summary definition](#summary-MinorFail-141)	|	[Previous MinorFail outcome](#minorfail-outcome-number-140)	|	[Next MinorFail outcome](#minorfail-outcome-number-142)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-src-aggregations-ontology|
|----|----|
|Title|Standalone module src/aggregations/ontology.ttl from branch main|
|Composition|- [Module aggregations/ontology](https://gitlab.com/coswot/coswot-acimov/blob/main/src/aggregations/ontology.ttl)|

#### Criterion detail
|Identifier|[profile-compatibility](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#profile-compatibility)|
|----|----|
|Title|Profile compatibility test|
|Description|A test meant to check whether the test subject is compatible with a profile or not, and if it is not, why.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-141)|Identifier|`owl-rl-profile-error`|
|[Section top](#minorfail-outcome-number-141)|Title|OWL RL Profile incompatible|
|[Section top](#minorfail-outcome-number-141)|Description|Statement not supported in a Super Class Expression|
|[Section top](#minorfail-outcome-number-141)|Pointer|<pre lang="Turtle"><code>&#91;] a owl:Class ;  &#10;&#32;&#32;&#32;&#32;owl:unionOf ( coswot:Observation coswot:ObservationCollection ) .</code></pre>|
|[Section top](#minorfail-outcome-number-141)|Pointer|<pre lang="Turtle"><code>&#91;] a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;owl:onProperty coswot:hasInput ;  &#10;&#32;&#32;&#32;&#32;owl:someValuesFrom coswot:ObservationCollection .</code></pre>|
|[Section top](#minorfail-outcome-number-141)|Pointer|<pre lang="Turtle"><code>&#91;] a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;owl:onProperty coswot:hasAggregationKind ;  &#10;&#32;&#32;&#32;&#32;owl:someValuesFrom coswot:AggregationKind .</code></pre>|
|[Section top](#minorfail-outcome-number-141)|Pointer|<pre lang="Turtle"><code>&#91;] a owl:Class ;  &#10;&#32;&#32;&#32;&#32;owl:unionOf ( coswot:Property coswot:State coswot:Aggregation ) .</code></pre>|
|[Section top](#minorfail-outcome-number-141)|Pointer|<pre lang="Turtle"><code>&#91;] a owl:Class ;  &#10;&#32;&#32;&#32;&#32;owl:unionOf ( coswot:Property coswot:State coswot:Aggregation coswot:AggregationKind ) .</code></pre>|

***
### MinorFail Outcome number 142

[Jump to summary definition](#summary-MinorFail-142)	|	[Previous MinorFail outcome](#minorfail-outcome-number-141)	|	[Next MinorFail outcome](#minorfail-outcome-number-143)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-src-aggregations-ontology|
|----|----|
|Title|Standalone module src/aggregations/ontology.ttl from branch main|
|Composition|- [Module aggregations/ontology](https://gitlab.com/coswot/coswot-acimov/blob/main/src/aggregations/ontology.ttl)|

#### Criterion detail
|Identifier|[profile-compatibility](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#profile-compatibility)|
|----|----|
|Title|Profile compatibility test|
|Description|A test meant to check whether the test subject is compatible with a profile or not, and if it is not, why.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-142)|Identifier|`owl-rl-profile-error`|
|[Section top](#minorfail-outcome-number-142)|Title|OWL RL Profile incompatible|
|[Section top](#minorfail-outcome-number-142)|Description|Class Expression not supported as object of rdfs:domain or rdfs:range|
|[Section top](#minorfail-outcome-number-142)|Pointer|<pre lang="Turtle"><code>coswot:hasAggregationDuration a owl:DatatypeProperty ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;has aggregation duration&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:comment &#34;Links a property, state, aggregation, or aggregation kind, t...&#34; ;  &#10;&#32;&#32;&#32;&#32;rdfs:domain &#91; a owl:Class ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:unionOf ( coswot:Property coswot:State coswot:Aggregation coswot:AggregationKind ) ] ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy &#60;https://w3id.org/coswot/core/aggregations> ;  &#10;&#32;&#32;&#32;&#32;rdfs:range xsd:duration .</code></pre>|
|[Section top](#minorfail-outcome-number-142)|Pointer|<pre lang="Turtle"><code>coswot:hasAggregationKind a owl:ObjectProperty ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;has aggregation kind&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:comment &#34;Links a property, state, or aggregation, to the kind of aggr...&#34; ;  &#10;&#32;&#32;&#32;&#32;rdfs:domain &#91; a owl:Class ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:unionOf ( coswot:Property coswot:State coswot:Aggregation ) ] ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy &#60;https://w3id.org/coswot/core/aggregations> ;  &#10;&#32;&#32;&#32;&#32;rdfs:range coswot:AggregationKind .</code></pre>|
|[Section top](#minorfail-outcome-number-142)|Pointer|<pre lang="Turtle"><code>coswot:hasAggregationTime a owl:ObjectProperty ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;has aggregation time&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:comment &#34;Links a property, state, aggregation, or aggregation kind, t...&#34; ;  &#10;&#32;&#32;&#32;&#32;rdfs:domain &#91; a owl:Class ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:unionOf ( coswot:Property coswot:State coswot:Aggregation coswot:AggregationKind ) ] ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy &#60;https://w3id.org/coswot/core/aggregations> ;  &#10;&#32;&#32;&#32;&#32;rdfs:range time:TemporalInterval ;  &#10;&#32;&#32;&#32;&#32;owl:propertyChainAxiom ( coswot:hasAggregationKind coswot:hasAggregationTime ) .</code></pre>|
|[Section top](#minorfail-outcome-number-142)|Pointer|<pre lang="Turtle"><code>coswot:hasMember a owl:ObjectProperty ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;has member&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:comment &#34;Link to a member within a collection of (actuations or sampl...&#34; ;  &#10;&#32;&#32;&#32;&#32;rdfs:domain coswot:ObservationCollection ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy &#60;https://w3id.org/coswot/core/aggregations> ;  &#10;&#32;&#32;&#32;&#32;rdfs:range &#91; a owl:Class ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:unionOf ( coswot:Observation coswot:ObservationCollection ) ] .</code></pre>|

***
### MinorFail Outcome number 143

[Jump to summary definition](#summary-MinorFail-143)	|	[Previous MinorFail outcome](#minorfail-outcome-number-142)	|	[Next MinorFail outcome](#minorfail-outcome-number-144)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-src-aggregations-ontology|
|----|----|
|Title|Standalone module src/aggregations/ontology.ttl from branch main|
|Composition|- [Module aggregations/ontology](https://gitlab.com/coswot/coswot-acimov/blob/main/src/aggregations/ontology.ttl)|

#### Criterion detail
|Identifier|[profile-compatibility](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#profile-compatibility)|
|----|----|
|Title|Profile compatibility test|
|Description|A test meant to check whether the test subject is compatible with a profile or not, and if it is not, why.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-143)|Identifier|`owl-ql-profile-error`|
|[Section top](#minorfail-outcome-number-143)|Title|OWL QL Profile incompatible|
|[Section top](#minorfail-outcome-number-143)|Description|Class Expression not supported as object of rdfs:domain or rdfs:range|
|[Section top](#minorfail-outcome-number-143)|Pointer|<pre lang="Turtle"><code>coswot:hasAggregationDuration a owl:DatatypeProperty ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;has aggregation duration&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:comment &#34;Links a property, state, aggregation, or aggregation kind, t...&#34; ;  &#10;&#32;&#32;&#32;&#32;rdfs:domain &#91; a owl:Class ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:unionOf ( coswot:Property coswot:State coswot:Aggregation coswot:AggregationKind ) ] ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy &#60;https://w3id.org/coswot/core/aggregations> ;  &#10;&#32;&#32;&#32;&#32;rdfs:range xsd:duration .</code></pre>|
|[Section top](#minorfail-outcome-number-143)|Pointer|<pre lang="Turtle"><code>coswot:hasAggregationKind a owl:ObjectProperty ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;has aggregation kind&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:comment &#34;Links a property, state, or aggregation, to the kind of aggr...&#34; ;  &#10;&#32;&#32;&#32;&#32;rdfs:domain &#91; a owl:Class ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:unionOf ( coswot:Property coswot:State coswot:Aggregation ) ] ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy &#60;https://w3id.org/coswot/core/aggregations> ;  &#10;&#32;&#32;&#32;&#32;rdfs:range coswot:AggregationKind .</code></pre>|
|[Section top](#minorfail-outcome-number-143)|Pointer|<pre lang="Turtle"><code>coswot:hasMember a owl:ObjectProperty ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;has member&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:comment &#34;Link to a member within a collection of (actuations or sampl...&#34; ;  &#10;&#32;&#32;&#32;&#32;rdfs:domain coswot:ObservationCollection ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy &#60;https://w3id.org/coswot/core/aggregations> ;  &#10;&#32;&#32;&#32;&#32;rdfs:range &#91; a owl:Class ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:unionOf ( coswot:Observation coswot:ObservationCollection ) ] .</code></pre>|

***
### MinorFail Outcome number 144

[Jump to summary definition](#summary-MinorFail-144)	|	[Previous MinorFail outcome](#minorfail-outcome-number-143)	|	[Next MinorFail outcome](#minorfail-outcome-number-145)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-src-aggregations-ontology|
|----|----|
|Title|Standalone module src/aggregations/ontology.ttl from branch main|
|Composition|- [Module aggregations/ontology](https://gitlab.com/coswot/coswot-acimov/blob/main/src/aggregations/ontology.ttl)|

#### Criterion detail
|Identifier|[profile-compatibility](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#profile-compatibility)|
|----|----|
|Title|Profile compatibility test|
|Description|A test meant to check whether the test subject is compatible with a profile or not, and if it is not, why.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-144)|Identifier|`owl-ql-profile-error`|
|[Section top](#minorfail-outcome-number-144)|Title|OWL QL Profile incompatible|
|[Section top](#minorfail-outcome-number-144)|Description|Statement not supported in a Super Class Expression|
|[Section top](#minorfail-outcome-number-144)|Pointer|<pre lang="Turtle"><code>&#91;] a owl:Class ;  &#10;&#32;&#32;&#32;&#32;owl:unionOf ( coswot:Observation coswot:ObservationCollection ) .</code></pre>|
|[Section top](#minorfail-outcome-number-144)|Pointer|<pre lang="Turtle"><code>&#91;] a owl:Class ;  &#10;&#32;&#32;&#32;&#32;owl:unionOf ( coswot:Property coswot:State coswot:Aggregation ) .</code></pre>|
|[Section top](#minorfail-outcome-number-144)|Pointer|<pre lang="Turtle"><code>&#91;] a owl:Class ;  &#10;&#32;&#32;&#32;&#32;owl:unionOf ( coswot:Property coswot:State coswot:Aggregation coswot:AggregationKind ) .</code></pre>|

***
### MinorFail Outcome number 145

[Jump to summary definition](#summary-MinorFail-145)	|	[Previous MinorFail outcome](#minorfail-outcome-number-144)	|	[Next MinorFail outcome](#minorfail-outcome-number-146)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-src-aggregations-ontology|
|----|----|
|Title|Standalone module src/aggregations/ontology.ttl from branch main|
|Composition|- [Module aggregations/ontology](https://gitlab.com/coswot/coswot-acimov/blob/main/src/aggregations/ontology.ttl)|

#### Criterion detail
|Identifier|[profile-compatibility](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#profile-compatibility)|
|----|----|
|Title|Profile compatibility test|
|Description|A test meant to check whether the test subject is compatible with a profile or not, and if it is not, why.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-145)|Identifier|`owl-ql-profile-error`|
|[Section top](#minorfail-outcome-number-145)|Title|OWL QL Profile incompatible|
|[Section top](#minorfail-outcome-number-145)|Description|Class Expression not supported as object of rdfs:domain or rdfs:range  &#10;Property inclusions involving property chains not supported|
|[Section top](#minorfail-outcome-number-145)|Pointer|<pre lang="Turtle"><code>coswot:hasAggregationTime a owl:ObjectProperty ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;has aggregation time&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:comment &#34;Links a property, state, aggregation, or aggregation kind, t...&#34; ;  &#10;&#32;&#32;&#32;&#32;rdfs:domain &#91; a owl:Class ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:unionOf ( coswot:Property coswot:State coswot:Aggregation coswot:AggregationKind ) ] ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy &#60;https://w3id.org/coswot/core/aggregations> ;  &#10;&#32;&#32;&#32;&#32;rdfs:range time:TemporalInterval ;  &#10;&#32;&#32;&#32;&#32;owl:propertyChainAxiom ( coswot:hasAggregationKind coswot:hasAggregationTime ) .</code></pre>|

***
### MinorFail Outcome number 146

[Jump to summary definition](#summary-MinorFail-146)	|	[Previous MinorFail outcome](#minorfail-outcome-number-145)	|	[Next MinorFail outcome](#minorfail-outcome-number-147)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-src-aggregations-ontology|
|----|----|
|Title|Standalone module src/aggregations/ontology.ttl from branch main|
|Composition|- [Module aggregations/ontology](https://gitlab.com/coswot/coswot-acimov/blob/main/src/aggregations/ontology.ttl)|

#### Criterion detail
|Identifier|[profile-compatibility](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#profile-compatibility)|
|----|----|
|Title|Profile compatibility test|
|Description|A test meant to check whether the test subject is compatible with a profile or not, and if it is not, why.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-146)|Identifier|`owl-el-profile-error`|
|[Section top](#minorfail-outcome-number-146)|Title|OWL EL Profile incompatible|
|[Section top](#minorfail-outcome-number-146)|Description|Statement not supported in a Class Expression|
|[Section top](#minorfail-outcome-number-146)|Pointer|<pre lang="Turtle"><code>&#91;] a owl:Class ;  &#10;&#32;&#32;&#32;&#32;owl:unionOf ( coswot:Observation coswot:ObservationCollection ) .</code></pre>|
|[Section top](#minorfail-outcome-number-146)|Pointer|<pre lang="Turtle"><code>&#91;] a owl:Class ;  &#10;&#32;&#32;&#32;&#32;owl:unionOf ( coswot:Property coswot:State coswot:Aggregation ) .</code></pre>|
|[Section top](#minorfail-outcome-number-146)|Pointer|<pre lang="Turtle"><code>&#91;] a owl:Class ;  &#10;&#32;&#32;&#32;&#32;owl:unionOf ( coswot:Property coswot:State coswot:Aggregation coswot:AggregationKind ) .</code></pre>|

***
### MinorFail Outcome number 147

[Jump to summary definition](#summary-MinorFail-147)	|	[Previous MinorFail outcome](#minorfail-outcome-number-146)	|	[Next MinorFail outcome](#minorfail-outcome-number-148)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-src-aggregations-ontology|
|----|----|
|Title|Standalone module src/aggregations/ontology.ttl from branch main|
|Composition|- [Module aggregations/ontology](https://gitlab.com/coswot/coswot-acimov/blob/main/src/aggregations/ontology.ttl)|

#### Criterion detail
|Identifier|[profile-compatibility](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#profile-compatibility)|
|----|----|
|Title|Profile compatibility test|
|Description|A test meant to check whether the test subject is compatible with a profile or not, and if it is not, why.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-147)|Identifier|`owl-el-profile-error`|
|[Section top](#minorfail-outcome-number-147)|Title|OWL EL Profile incompatible|
|[Section top](#minorfail-outcome-number-147)|Description|Class Expression not supported as object of rdfs:domain or rdfs:range|
|[Section top](#minorfail-outcome-number-147)|Pointer|<pre lang="Turtle"><code>coswot:hasAggregationDuration a owl:DatatypeProperty ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;has aggregation duration&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:comment &#34;Links a property, state, aggregation, or aggregation kind, t...&#34; ;  &#10;&#32;&#32;&#32;&#32;rdfs:domain &#91; a owl:Class ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:unionOf ( coswot:Property coswot:State coswot:Aggregation coswot:AggregationKind ) ] ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy &#60;https://w3id.org/coswot/core/aggregations> ;  &#10;&#32;&#32;&#32;&#32;rdfs:range xsd:duration .</code></pre>|
|[Section top](#minorfail-outcome-number-147)|Pointer|<pre lang="Turtle"><code>coswot:hasAggregationKind a owl:ObjectProperty ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;has aggregation kind&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:comment &#34;Links a property, state, or aggregation, to the kind of aggr...&#34; ;  &#10;&#32;&#32;&#32;&#32;rdfs:domain &#91; a owl:Class ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:unionOf ( coswot:Property coswot:State coswot:Aggregation ) ] ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy &#60;https://w3id.org/coswot/core/aggregations> ;  &#10;&#32;&#32;&#32;&#32;rdfs:range coswot:AggregationKind .</code></pre>|
|[Section top](#minorfail-outcome-number-147)|Pointer|<pre lang="Turtle"><code>coswot:hasAggregationTime a owl:ObjectProperty ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;has aggregation time&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:comment &#34;Links a property, state, aggregation, or aggregation kind, t...&#34; ;  &#10;&#32;&#32;&#32;&#32;rdfs:domain &#91; a owl:Class ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:unionOf ( coswot:Property coswot:State coswot:Aggregation coswot:AggregationKind ) ] ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy &#60;https://w3id.org/coswot/core/aggregations> ;  &#10;&#32;&#32;&#32;&#32;rdfs:range time:TemporalInterval ;  &#10;&#32;&#32;&#32;&#32;owl:propertyChainAxiom ( coswot:hasAggregationKind coswot:hasAggregationTime ) .</code></pre>|
|[Section top](#minorfail-outcome-number-147)|Pointer|<pre lang="Turtle"><code>coswot:hasMember a owl:ObjectProperty ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;has member&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:comment &#34;Link to a member within a collection of (actuations or sampl...&#34; ;  &#10;&#32;&#32;&#32;&#32;rdfs:domain coswot:ObservationCollection ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy &#60;https://w3id.org/coswot/core/aggregations> ;  &#10;&#32;&#32;&#32;&#32;rdfs:range &#91; a owl:Class ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:unionOf ( coswot:Observation coswot:ObservationCollection ) ] .</code></pre>|

***
### MinorFail Outcome number 148

[Jump to summary definition](#summary-MinorFail-148)	|	[Previous MinorFail outcome](#minorfail-outcome-number-147)	|	[Next MinorFail outcome](#minorfail-outcome-number-149)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-src-actuations-ontology|
|----|----|
|Title|Standalone module src/actuations/ontology.ttl from branch main|
|Composition|- [Module actuations/ontology](https://gitlab.com/coswot/coswot-acimov/blob/main/src/actuations/ontology.ttl)|

#### Criterion detail
|Identifier|[profile-compatibility](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#profile-compatibility)|
|----|----|
|Title|Profile compatibility test|
|Description|A test meant to check whether the test subject is compatible with a profile or not, and if it is not, why.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-148)|Identifier|`owl-rl-profile-error`|
|[Section top](#minorfail-outcome-number-148)|Title|OWL RL Profile incompatible|
|[Section top](#minorfail-outcome-number-148)|Description|Class Expression not supported with rdfs:subClassOf|
|[Section top](#minorfail-outcome-number-148)|Pointer|<pre lang="Turtle"><code>coswot:ActuatingCommand a owl:Class ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;Actuating Command&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:comment &#34;An instance of actuating command is a command that controls ...&#34; ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy &#60;https://w3id.org/coswot/core/actuations> ;  &#10;&#32;&#32;&#32;&#32;rdfs:subClassOf &#91; a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:onProperty coswot:controls ],  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;coswot:Command .</code></pre>|
|[Section top](#minorfail-outcome-number-148)|Pointer|<pre lang="Turtle"><code>coswot:ActuatingFunction a owl:Class ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;Actuating Function&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:comment &#34;An actuating function is a function that has at least one ac...&#34; ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy &#60;https://w3id.org/coswot/core/actuations> ;  &#10;&#32;&#32;&#32;&#32;rdfs:subClassOf &#91; a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:onProperty coswot:hasCommand ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:someValuesFrom coswot:ActuatingCommand ],  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;coswot:Function .</code></pre>|
|[Section top](#minorfail-outcome-number-148)|Pointer|<pre lang="Turtle"><code>coswot:Actuation a owl:Class ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;Actuation&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:comment &#34;A coswot:Actuation is the act of carrying out a procedure to...&#34; ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy &#60;https://w3id.org/coswot/core/actuations> ;  &#10;&#32;&#32;&#32;&#32;rdfs:subClassOf &#91; a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:allValuesFrom coswot:Actuator ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:onProperty coswot:madeBy ],  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#91; a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:onProperty coswot:controls ],  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;coswot:ProcedureExecution .</code></pre>|
|[Section top](#minorfail-outcome-number-148)|Pointer|<pre lang="Turtle"><code>coswot:ActuatorOfInterest a owl:Class ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;Actuator Of Interest&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:comment &#34;A specific, tangible device designed to control one or more ...&#34; ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy &#60;https://w3id.org/coswot/core/actuations> ;  &#10;&#32;&#32;&#32;&#32;rdfs:subClassOf &#91; a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:onProperty coswot:controls ],  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;coswot:Actuator,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;coswot:DeviceOfInterest .</code></pre>|

***
### MinorFail Outcome number 149

[Jump to summary definition](#summary-MinorFail-149)	|	[Previous MinorFail outcome](#minorfail-outcome-number-148)	|	[Next MinorFail outcome](#minorfail-outcome-number-150)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-src-actuations-ontology|
|----|----|
|Title|Standalone module src/actuations/ontology.ttl from branch main|
|Composition|- [Module actuations/ontology](https://gitlab.com/coswot/coswot-acimov/blob/main/src/actuations/ontology.ttl)|

#### Criterion detail
|Identifier|[profile-compatibility](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#profile-compatibility)|
|----|----|
|Title|Profile compatibility test|
|Description|A test meant to check whether the test subject is compatible with a profile or not, and if it is not, why.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-149)|Identifier|`owl-rl-profile-error`|
|[Section top](#minorfail-outcome-number-149)|Title|OWL RL Profile incompatible|
|[Section top](#minorfail-outcome-number-149)|Description|Statement not supported|
|[Section top](#minorfail-outcome-number-149)|Pointer|<pre lang="Turtle"><code>coswot:Actuator a owl:Class ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;Actuator&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:comment &#34;Actuators are devices designed to control one or more proper...&#34; ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy &#60;https://w3id.org/coswot/core/actuations> ;  &#10;&#32;&#32;&#32;&#32;rdfs:subClassOf &#91; a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:onProperty coswot:controls ],  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;coswot:Device ;  &#10;&#32;&#32;&#32;&#32;owl:disjointUnionOf ( coswot:ActuatorOfInterest coswot:ActuatorKind ) .</code></pre>|

***
### MinorFail Outcome number 150

[Jump to summary definition](#summary-MinorFail-150)	|	[Previous MinorFail outcome](#minorfail-outcome-number-149)	|	[Next MinorFail outcome](#minorfail-outcome-number-151)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-src-actuations-ontology|
|----|----|
|Title|Standalone module src/actuations/ontology.ttl from branch main|
|Composition|- [Module actuations/ontology](https://gitlab.com/coswot/coswot-acimov/blob/main/src/actuations/ontology.ttl)|

#### Criterion detail
|Identifier|[profile-compatibility](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#profile-compatibility)|
|----|----|
|Title|Profile compatibility test|
|Description|A test meant to check whether the test subject is compatible with a profile or not, and if it is not, why.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-150)|Identifier|`owl-rl-profile-error`|
|[Section top](#minorfail-outcome-number-150)|Title|OWL RL Profile incompatible|
|[Section top](#minorfail-outcome-number-150)|Description|Statement not supported in a Super Class Expression|
|[Section top](#minorfail-outcome-number-150)|Pointer|<pre lang="Turtle"><code>&#91;] a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;owl:onProperty coswot:controls .</code></pre>|
|[Section top](#minorfail-outcome-number-150)|Pointer|<pre lang="Turtle"><code>&#91;] a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;owl:onProperty coswot:hasCommand ;  &#10;&#32;&#32;&#32;&#32;owl:someValuesFrom coswot:ActuatingCommand .</code></pre>|
|[Section top](#minorfail-outcome-number-150)|Pointer|<pre lang="Turtle"><code>&#91;] a owl:Class ;  &#10;&#32;&#32;&#32;&#32;owl:unionOf ( coswot:Actuator coswot:ActuatingFunction coswot:ActuatingCommand coswot:Actuation ) .</code></pre>|

***
### MinorFail Outcome number 151

[Jump to summary definition](#summary-MinorFail-151)	|	[Previous MinorFail outcome](#minorfail-outcome-number-150)	|	[Next MinorFail outcome](#minorfail-outcome-number-152)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-src-actuations-ontology|
|----|----|
|Title|Standalone module src/actuations/ontology.ttl from branch main|
|Composition|- [Module actuations/ontology](https://gitlab.com/coswot/coswot-acimov/blob/main/src/actuations/ontology.ttl)|

#### Criterion detail
|Identifier|[profile-compatibility](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#profile-compatibility)|
|----|----|
|Title|Profile compatibility test|
|Description|A test meant to check whether the test subject is compatible with a profile or not, and if it is not, why.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-151)|Identifier|`owl-rl-profile-error`|
|[Section top](#minorfail-outcome-number-151)|Title|OWL RL Profile incompatible|
|[Section top](#minorfail-outcome-number-151)|Description|Class Expression not supported as object of rdfs:domain or rdfs:range|
|[Section top](#minorfail-outcome-number-151)|Pointer|<pre lang="Turtle"><code>coswot:controls a owl:ObjectProperty ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;controls&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:comment &#34;Links an actuator, actuating function, actuating command, or...&#34; ;  &#10;&#32;&#32;&#32;&#32;rdfs:domain &#91; a owl:Class ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:unionOf ( coswot:Actuator coswot:ActuatingFunction coswot:ActuatingCommand coswot:Actuation ) ] ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy &#60;https://w3id.org/coswot/core/actuations> ;  &#10;&#32;&#32;&#32;&#32;rdfs:subPropertyOf coswot:targets ;  &#10;&#32;&#32;&#32;&#32;owl:inverseOf coswot:isControlledBy .</code></pre>|

***
### MinorFail Outcome number 152

[Jump to summary definition](#summary-MinorFail-152)	|	[Previous MinorFail outcome](#minorfail-outcome-number-151)	|	[Next MinorFail outcome](#minorfail-outcome-number-153)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-src-actuations-ontology|
|----|----|
|Title|Standalone module src/actuations/ontology.ttl from branch main|
|Composition|- [Module actuations/ontology](https://gitlab.com/coswot/coswot-acimov/blob/main/src/actuations/ontology.ttl)|

#### Criterion detail
|Identifier|[profile-compatibility](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#profile-compatibility)|
|----|----|
|Title|Profile compatibility test|
|Description|A test meant to check whether the test subject is compatible with a profile or not, and if it is not, why.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-152)|Identifier|`owl-ql-profile-error`|
|[Section top](#minorfail-outcome-number-152)|Title|OWL QL Profile incompatible|
|[Section top](#minorfail-outcome-number-152)|Description|Class Expression not supported with rdfs:subClassOf|
|[Section top](#minorfail-outcome-number-152)|Pointer|<pre lang="Turtle"><code>coswot:ActuatingCommand a owl:Class ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;Actuating Command&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:comment &#34;An instance of actuating command is a command that controls ...&#34; ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy &#60;https://w3id.org/coswot/core/actuations> ;  &#10;&#32;&#32;&#32;&#32;rdfs:subClassOf &#91; a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:onProperty coswot:controls ],  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;coswot:Command .</code></pre>|
|[Section top](#minorfail-outcome-number-152)|Pointer|<pre lang="Turtle"><code>coswot:Actuation a owl:Class ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;Actuation&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:comment &#34;A coswot:Actuation is the act of carrying out a procedure to...&#34; ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy &#60;https://w3id.org/coswot/core/actuations> ;  &#10;&#32;&#32;&#32;&#32;rdfs:subClassOf &#91; a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:allValuesFrom coswot:Actuator ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:onProperty coswot:madeBy ],  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#91; a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:onProperty coswot:controls ],  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;coswot:ProcedureExecution .</code></pre>|
|[Section top](#minorfail-outcome-number-152)|Pointer|<pre lang="Turtle"><code>coswot:ActuatorOfInterest a owl:Class ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;Actuator Of Interest&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:comment &#34;A specific, tangible device designed to control one or more ...&#34; ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy &#60;https://w3id.org/coswot/core/actuations> ;  &#10;&#32;&#32;&#32;&#32;rdfs:subClassOf &#91; a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:onProperty coswot:controls ],  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;coswot:Actuator,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;coswot:DeviceOfInterest .</code></pre>|

***
### MinorFail Outcome number 153

[Jump to summary definition](#summary-MinorFail-153)	|	[Previous MinorFail outcome](#minorfail-outcome-number-152)	|	[Next MinorFail outcome](#minorfail-outcome-number-154)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-src-actuations-ontology|
|----|----|
|Title|Standalone module src/actuations/ontology.ttl from branch main|
|Composition|- [Module actuations/ontology](https://gitlab.com/coswot/coswot-acimov/blob/main/src/actuations/ontology.ttl)|

#### Criterion detail
|Identifier|[profile-compatibility](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#profile-compatibility)|
|----|----|
|Title|Profile compatibility test|
|Description|A test meant to check whether the test subject is compatible with a profile or not, and if it is not, why.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-153)|Identifier|`owl-ql-profile-error`|
|[Section top](#minorfail-outcome-number-153)|Title|OWL QL Profile incompatible|
|[Section top](#minorfail-outcome-number-153)|Description|Statement not supported|
|[Section top](#minorfail-outcome-number-153)|Pointer|<pre lang="Turtle"><code>coswot:Actuator a owl:Class ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;Actuator&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:comment &#34;Actuators are devices designed to control one or more proper...&#34; ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy &#60;https://w3id.org/coswot/core/actuations> ;  &#10;&#32;&#32;&#32;&#32;rdfs:subClassOf &#91; a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:onProperty coswot:controls ],  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;coswot:Device ;  &#10;&#32;&#32;&#32;&#32;owl:disjointUnionOf ( coswot:ActuatorOfInterest coswot:ActuatorKind ) .</code></pre>|

***
### MinorFail Outcome number 154

[Jump to summary definition](#summary-MinorFail-154)	|	[Previous MinorFail outcome](#minorfail-outcome-number-153)	|	[Next MinorFail outcome](#minorfail-outcome-number-155)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-src-actuations-ontology|
|----|----|
|Title|Standalone module src/actuations/ontology.ttl from branch main|
|Composition|- [Module actuations/ontology](https://gitlab.com/coswot/coswot-acimov/blob/main/src/actuations/ontology.ttl)|

#### Criterion detail
|Identifier|[profile-compatibility](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#profile-compatibility)|
|----|----|
|Title|Profile compatibility test|
|Description|A test meant to check whether the test subject is compatible with a profile or not, and if it is not, why.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-154)|Identifier|`owl-ql-profile-error`|
|[Section top](#minorfail-outcome-number-154)|Title|OWL QL Profile incompatible|
|[Section top](#minorfail-outcome-number-154)|Description|Statement not supported in a Super Class Expression|
|[Section top](#minorfail-outcome-number-154)|Pointer|<pre lang="Turtle"><code>&#91;] a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;owl:onProperty coswot:controls .</code></pre>|
|[Section top](#minorfail-outcome-number-154)|Pointer|<pre lang="Turtle"><code>&#91;] a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;owl:allValuesFrom coswot:Actuator ;  &#10;&#32;&#32;&#32;&#32;owl:onProperty coswot:madeBy .</code></pre>|
|[Section top](#minorfail-outcome-number-154)|Pointer|<pre lang="Turtle"><code>&#91;] a owl:Class ;  &#10;&#32;&#32;&#32;&#32;owl:unionOf ( coswot:Actuator coswot:ActuatingFunction coswot:ActuatingCommand coswot:Actuation ) .</code></pre>|

***
### MinorFail Outcome number 155

[Jump to summary definition](#summary-MinorFail-155)	|	[Previous MinorFail outcome](#minorfail-outcome-number-154)	|	[Next MinorFail outcome](#minorfail-outcome-number-156)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-src-actuations-ontology|
|----|----|
|Title|Standalone module src/actuations/ontology.ttl from branch main|
|Composition|- [Module actuations/ontology](https://gitlab.com/coswot/coswot-acimov/blob/main/src/actuations/ontology.ttl)|

#### Criterion detail
|Identifier|[profile-compatibility](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#profile-compatibility)|
|----|----|
|Title|Profile compatibility test|
|Description|A test meant to check whether the test subject is compatible with a profile or not, and if it is not, why.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-155)|Identifier|`owl-ql-profile-error`|
|[Section top](#minorfail-outcome-number-155)|Title|OWL QL Profile incompatible|
|[Section top](#minorfail-outcome-number-155)|Description|Class Expression not supported as object of rdfs:domain or rdfs:range|
|[Section top](#minorfail-outcome-number-155)|Pointer|<pre lang="Turtle"><code>coswot:controls a owl:ObjectProperty ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;controls&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:comment &#34;Links an actuator, actuating function, actuating command, or...&#34; ;  &#10;&#32;&#32;&#32;&#32;rdfs:domain &#91; a owl:Class ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:unionOf ( coswot:Actuator coswot:ActuatingFunction coswot:ActuatingCommand coswot:Actuation ) ] ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy &#60;https://w3id.org/coswot/core/actuations> ;  &#10;&#32;&#32;&#32;&#32;rdfs:subPropertyOf coswot:targets ;  &#10;&#32;&#32;&#32;&#32;owl:inverseOf coswot:isControlledBy .</code></pre>|

***
### MinorFail Outcome number 156

[Jump to summary definition](#summary-MinorFail-156)	|	[Previous MinorFail outcome](#minorfail-outcome-number-155)	|	[Next MinorFail outcome](#minorfail-outcome-number-157)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-src-actuations-ontology|
|----|----|
|Title|Standalone module src/actuations/ontology.ttl from branch main|
|Composition|- [Module actuations/ontology](https://gitlab.com/coswot/coswot-acimov/blob/main/src/actuations/ontology.ttl)|

#### Criterion detail
|Identifier|[profile-compatibility](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#profile-compatibility)|
|----|----|
|Title|Profile compatibility test|
|Description|A test meant to check whether the test subject is compatible with a profile or not, and if it is not, why.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-156)|Identifier|`owl-el-profile-error`|
|[Section top](#minorfail-outcome-number-156)|Title|OWL EL Profile incompatible|
|[Section top](#minorfail-outcome-number-156)|Description|Statement not supported in a Class Expression|
|[Section top](#minorfail-outcome-number-156)|Pointer|<pre lang="Turtle"><code>&#91;] a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;owl:onProperty coswot:controls .</code></pre>|
|[Section top](#minorfail-outcome-number-156)|Pointer|<pre lang="Turtle"><code>&#91;] a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;owl:allValuesFrom coswot:Actuator ;  &#10;&#32;&#32;&#32;&#32;owl:onProperty coswot:madeBy .</code></pre>|
|[Section top](#minorfail-outcome-number-156)|Pointer|<pre lang="Turtle"><code>&#91;] a owl:Class ;  &#10;&#32;&#32;&#32;&#32;owl:unionOf ( coswot:Actuator coswot:ActuatingFunction coswot:ActuatingCommand coswot:Actuation ) .</code></pre>|

***
### MinorFail Outcome number 157

[Jump to summary definition](#summary-MinorFail-157)	|	[Previous MinorFail outcome](#minorfail-outcome-number-156)	|	[Next MinorFail outcome](#minorfail-outcome-number-158)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-src-actuations-ontology|
|----|----|
|Title|Standalone module src/actuations/ontology.ttl from branch main|
|Composition|- [Module actuations/ontology](https://gitlab.com/coswot/coswot-acimov/blob/main/src/actuations/ontology.ttl)|

#### Criterion detail
|Identifier|[profile-compatibility](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#profile-compatibility)|
|----|----|
|Title|Profile compatibility test|
|Description|A test meant to check whether the test subject is compatible with a profile or not, and if it is not, why.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-157)|Identifier|`owl-el-profile-error`|
|[Section top](#minorfail-outcome-number-157)|Title|OWL EL Profile incompatible|
|[Section top](#minorfail-outcome-number-157)|Description|Statement not supported|
|[Section top](#minorfail-outcome-number-157)|Pointer|<pre lang="Turtle"><code>coswot:Actuator a owl:Class ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;Actuator&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:comment &#34;Actuators are devices designed to control one or more proper...&#34; ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy &#60;https://w3id.org/coswot/core/actuations> ;  &#10;&#32;&#32;&#32;&#32;rdfs:subClassOf &#91; a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:onProperty coswot:controls ],  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;coswot:Device ;  &#10;&#32;&#32;&#32;&#32;owl:disjointUnionOf ( coswot:ActuatorOfInterest coswot:ActuatorKind ) .</code></pre>|

***
### MinorFail Outcome number 158

[Jump to summary definition](#summary-MinorFail-158)	|	[Previous MinorFail outcome](#minorfail-outcome-number-157)	|	[Next MinorFail outcome](#minorfail-outcome-number-159)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-src-actuations-ontology|
|----|----|
|Title|Standalone module src/actuations/ontology.ttl from branch main|
|Composition|- [Module actuations/ontology](https://gitlab.com/coswot/coswot-acimov/blob/main/src/actuations/ontology.ttl)|

#### Criterion detail
|Identifier|[profile-compatibility](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#profile-compatibility)|
|----|----|
|Title|Profile compatibility test|
|Description|A test meant to check whether the test subject is compatible with a profile or not, and if it is not, why.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-158)|Identifier|`owl-el-profile-error`|
|[Section top](#minorfail-outcome-number-158)|Title|OWL EL Profile incompatible|
|[Section top](#minorfail-outcome-number-158)|Description|Class Expression not supported as object of rdfs:domain or rdfs:range|
|[Section top](#minorfail-outcome-number-158)|Pointer|<pre lang="Turtle"><code>coswot:controls a owl:ObjectProperty ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;controls&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:comment &#34;Links an actuator, actuating function, actuating command, or...&#34; ;  &#10;&#32;&#32;&#32;&#32;rdfs:domain &#91; a owl:Class ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:unionOf ( coswot:Actuator coswot:ActuatingFunction coswot:ActuatingCommand coswot:Actuation ) ] ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy &#60;https://w3id.org/coswot/core/actuations> ;  &#10;&#32;&#32;&#32;&#32;rdfs:subPropertyOf coswot:targets ;  &#10;&#32;&#32;&#32;&#32;owl:inverseOf coswot:isControlledBy .</code></pre>|

***
### MinorFail Outcome number 159

[Jump to summary definition](#summary-MinorFail-159)	|	[Previous MinorFail outcome](#minorfail-outcome-number-158)	|	[Next MinorFail outcome](#minorfail-outcome-number-160)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-src-actuations-ontology|
|----|----|
|Title|Standalone module src/actuations/ontology.ttl from branch main|
|Composition|- [Module actuations/ontology](https://gitlab.com/coswot/coswot-acimov/blob/main/src/actuations/ontology.ttl)|

#### Criterion detail
|Identifier|[profile-compatibility](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#profile-compatibility)|
|----|----|
|Title|Profile compatibility test|
|Description|A test meant to check whether the test subject is compatible with a profile or not, and if it is not, why.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-159)|Identifier|`owl-el-profile-error`|
|[Section top](#minorfail-outcome-number-159)|Title|OWL EL Profile incompatible|
|[Section top](#minorfail-outcome-number-159)|Description|Class Expression not supported with rdfs:subClassOf|
|[Section top](#minorfail-outcome-number-159)|Pointer|<pre lang="Turtle"><code>coswot:ActuatingCommand a owl:Class ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;Actuating Command&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:comment &#34;An instance of actuating command is a command that controls ...&#34; ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy &#60;https://w3id.org/coswot/core/actuations> ;  &#10;&#32;&#32;&#32;&#32;rdfs:subClassOf &#91; a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:onProperty coswot:controls ],  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;coswot:Command .</code></pre>|
|[Section top](#minorfail-outcome-number-159)|Pointer|<pre lang="Turtle"><code>coswot:Actuation a owl:Class ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;Actuation&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:comment &#34;A coswot:Actuation is the act of carrying out a procedure to...&#34; ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy &#60;https://w3id.org/coswot/core/actuations> ;  &#10;&#32;&#32;&#32;&#32;rdfs:subClassOf &#91; a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:allValuesFrom coswot:Actuator ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:onProperty coswot:madeBy ],  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#91; a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:onProperty coswot:controls ],  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;coswot:ProcedureExecution .</code></pre>|
|[Section top](#minorfail-outcome-number-159)|Pointer|<pre lang="Turtle"><code>coswot:ActuatorOfInterest a owl:Class ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;Actuator Of Interest&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:comment &#34;A specific, tangible device designed to control one or more ...&#34; ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy &#60;https://w3id.org/coswot/core/actuations> ;  &#10;&#32;&#32;&#32;&#32;rdfs:subClassOf &#91; a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:onProperty coswot:controls ],  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;coswot:Actuator,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;coswot:DeviceOfInterest .</code></pre>|

***
### MinorFail Outcome number 160

[Jump to summary definition](#summary-MinorFail-160)	|	[Previous MinorFail outcome](#minorfail-outcome-number-159)	|	[Next MinorFail outcome](#minorfail-outcome-number-161)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-src-actuations-ontology|
|----|----|
|Title|Standalone module src/actuations/ontology.ttl from branch main|
|Composition|- [Module actuations/ontology](https://gitlab.com/coswot/coswot-acimov/blob/main/src/actuations/ontology.ttl)|

#### Criterion detail
|Identifier|[terms-differenciation](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#terms-differenciation)|
|----|----|
|Title|Terms differenciation test|
|Description|A test case from the Best Practices tests checking if all the terms are different enough from each other according to the Levenshtein distance metric.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-160)|Identifier|`too-close-terms`|
|[Section top](#minorfail-outcome-number-160)|Title|Too close terms|
|[Section top](#minorfail-outcome-number-160)|Description|Some terms are too similar|
|[Section top](#minorfail-outcome-number-160)|Pointer|<pre lang="Turtle"><code>:Actuator a owl:Class ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;Actuator&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:comment &#34;Actuators are devices designed to control one or more proper...&#34; ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy &#60;https://w3id.org/coswot/core/actuations> ;  &#10;&#32;&#32;&#32;&#32;rdfs:subClassOf &#91; a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:onProperty :controls ],  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;:Device ;  &#10;&#32;&#32;&#32;&#32;owl:disjointUnionOf ( :ActuatorOfInterest :ActuatorKind ) .</code></pre>|
|[Section top](#minorfail-outcome-number-160)|Pointer|<pre lang="Turtle"><code>:Actuation a owl:Class ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;Actuation&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:comment &#34;A coswot:Actuation is the act of carrying out a procedure to...&#34; ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy &#60;https://w3id.org/coswot/core/actuations> ;  &#10;&#32;&#32;&#32;&#32;rdfs:subClassOf &#91; a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:allValuesFrom :Actuator ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:onProperty :madeBy ],  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#91; a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:onProperty :controls ],  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;:ProcedureExecution .</code></pre>|

***
### MinorFail Outcome number 161

[Jump to summary definition](#summary-MinorFail-161)	|	[Previous MinorFail outcome](#minorfail-outcome-number-160)	|	[Next MinorFail outcome](#minorfail-outcome-number-162)

:exclamation:MinorFail outcome
#### Subject detail
|Name|modelet-building-automation-samples|
|----|----|
|Title|Standalone modelet domains/building-automation/samples/onto.ttl from branch main|
|Composition|- [Modelet building-automation/samples](https://gitlab.com/coswot/coswot-acimov/blob/main/domains/building-automation/samples/onto.ttl)|

#### Criterion detail
|Identifier|[profile-compatibility](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#profile-compatibility)|
|----|----|
|Title|Profile compatibility test|
|Description|A test meant to check whether the test subject is compatible with a profile or not, and if it is not, why.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-161)|Identifier|`owl-ql-profile-error`|
|[Section top](#minorfail-outcome-number-161)|Title|OWL QL Profile incompatible|
|[Section top](#minorfail-outcome-number-161)|Description|Anonymous individuals are not supported|
|[Section top](#minorfail-outcome-number-161)|Pointer|<pre lang="Turtle"><code>&#91;] a coswot:PropertyValue ;  &#10;&#32;&#32;&#32;&#32;coswot:isMeasuredIn &#60;https://qudt.org/vocab/unit/M3> ;  &#10;&#32;&#32;&#32;&#32;coswot:isValueOfProperty coswot:Volume .</code></pre>|
|[Section top](#minorfail-outcome-number-161)|Pointer|<pre lang="Turtle"><code>coswot:AirSample1M3 a coswot:FeatureKind ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;Air Sample 1 m3&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:comment &#34;Type d'un échantillon d'air de 1m3.&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy &#60;https://w3id.org/coswot/building&lowbar;automation/samples> ;  &#10;&#32;&#32;&#32;&#32;skos:inScheme &#60;https://w3id.org/coswot/building&lowbar;automation/samples> ;  &#10;&#32;&#32;&#32;&#32;coswot:hasValue &#91; a coswot:PropertyValue ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;coswot:isMeasuredIn &#60;https://qudt.org/vocab/unit/M3> ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;coswot:isValueOfProperty coswot:Volume ] .</code></pre>|

***
### MinorFail Outcome number 162

[Jump to summary definition](#summary-MinorFail-162)	|	[Previous MinorFail outcome](#minorfail-outcome-number-161)	|	[Next MinorFail outcome](#minorfail-outcome-number-163)

:exclamation:MinorFail outcome
#### Subject detail
|Name|modelet-building-automation-samples|
|----|----|
|Title|Standalone modelet domains/building-automation/samples/onto.ttl from branch main|
|Composition|- [Modelet building-automation/samples](https://gitlab.com/coswot/coswot-acimov/blob/main/domains/building-automation/samples/onto.ttl)|

#### Criterion detail
|Identifier|[profile-compatibility](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#profile-compatibility)|
|----|----|
|Title|Profile compatibility test|
|Description|A test meant to check whether the test subject is compatible with a profile or not, and if it is not, why.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-162)|Identifier|`owl-el-profile-error`|
|[Section top](#minorfail-outcome-number-162)|Title|OWL EL Profile incompatible|
|[Section top](#minorfail-outcome-number-162)|Description|Anonymous individuals are not supported|
|[Section top](#minorfail-outcome-number-162)|Pointer|<pre lang="Turtle"><code>&#91;] a coswot:PropertyValue ;  &#10;&#32;&#32;&#32;&#32;coswot:isMeasuredIn &#60;https://qudt.org/vocab/unit/M3> ;  &#10;&#32;&#32;&#32;&#32;coswot:isValueOfProperty coswot:Volume .</code></pre>|
|[Section top](#minorfail-outcome-number-162)|Pointer|<pre lang="Turtle"><code>coswot:AirSample1M3 a coswot:FeatureKind ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;Air Sample 1 m3&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:comment &#34;Type d'un échantillon d'air de 1m3.&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy &#60;https://w3id.org/coswot/building&lowbar;automation/samples> ;  &#10;&#32;&#32;&#32;&#32;skos:inScheme &#60;https://w3id.org/coswot/building&lowbar;automation/samples> ;  &#10;&#32;&#32;&#32;&#32;coswot:hasValue &#91; a coswot:PropertyValue ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;coswot:isMeasuredIn &#60;https://qudt.org/vocab/unit/M3> ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;coswot:isValueOfProperty coswot:Volume ] .</code></pre>|

***
### MinorFail Outcome number 163

[Jump to summary definition](#summary-MinorFail-163)	|	[Previous MinorFail outcome](#minorfail-outcome-number-162)	|	[Next MinorFail outcome](#minorfail-outcome-number-164)

:exclamation:MinorFail outcome
#### Subject detail
|Name|modelet-building-automation-features|
|----|----|
|Title|Standalone modelet domains/building-automation/features/onto.ttl from branch main|
|Composition|- [Modelet building-automation/features](https://gitlab.com/coswot/coswot-acimov/blob/main/domains/building-automation/features/onto.ttl)|

#### Criterion detail
|Identifier|[domain-and-range-referencing](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#domain-and-range-referencing)|
|----|----|
|Title|Domain and range referencing test|
|Description|A test case from the Best Practices tests checking if all the ranges and domains from the test subject point to terms that are defined in the vocabulary.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-163)|Identifier|`domain-out-of-vocabulary`|
|[Section top](#minorfail-outcome-number-163)|Title|Domain out of vocabulary|
|[Section top](#minorfail-outcome-number-163)|Description|Some properties have a domain out of the ontology|
|[Section top](#minorfail-outcome-number-163)|Pointer|<pre lang="Turtle"><code>:containsZone a owl:ObjectProperty,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:TransitiveProperty ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;contains zone&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:comment &#34;Relationship to the subzones of a major zone. A space zone c...&#34; ;  &#10;&#32;&#32;&#32;&#32;rdfs:domain owl:Thing,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#60;https://w3id.org/bot#Zone>,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;:System,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;:Zone ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy &#60;https://w3id.org/coswot/building&lowbar;automation/features> ;  &#10;&#32;&#32;&#32;&#32;rdfs:range owl:Thing,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#60;https://w3id.org/bot#Zone>,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;:System,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;:Zone ;  &#10;&#32;&#32;&#32;&#32;rdfs:subClassOf &#60;https://w3id.org/bot#containsZone>,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;:containsZone ;  &#10;&#32;&#32;&#32;&#32;rdfs:subPropertyOf :containsZone,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;:hasSubSystem ;  &#10;&#32;&#32;&#32;&#32;owl:equivalentClass &#60;https://w3id.org/bot#containsZone> ;  &#10;&#32;&#32;&#32;&#32;owl:equivalentProperty :containsZone .</code></pre>|
|[Section top](#minorfail-outcome-number-163)|Pointer|<pre lang="Turtle"><code>:Zone rdfs:subClassOf owl:Thing,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;:Zone,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;coswot:System,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;coswot:Zone ;  &#10;&#32;&#32;&#32;&#32;owl:equivalentClass coswot:Zone .</code></pre>|
|[Section top](#minorfail-outcome-number-163)|Pointer|<pre lang="Turtle"><code>:hasBuilding a owl:ObjectProperty ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;has building&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:comment &#34;Relation to buildings contained in a zone. The typical domai...&#34; ;  &#10;&#32;&#32;&#32;&#32;rdfs:domain owl:Thing,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#60;https://w3id.org/bot#Zone>,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;:System,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;:Zone ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy &#60;https://w3id.org/coswot/building&lowbar;automation/features> ;  &#10;&#32;&#32;&#32;&#32;rdfs:range owl:Thing,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#60;https://w3id.org/bot#Building>,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#60;https://w3id.org/bot#Zone>,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;:Building,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;:System,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;:Zone ;  &#10;&#32;&#32;&#32;&#32;rdfs:subClassOf &#60;https://w3id.org/bot#hasBuilding>,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;:hasBuilding ;  &#10;&#32;&#32;&#32;&#32;rdfs:subPropertyOf :containsZone,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;:hasBuilding,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;:hasSubSystem ;  &#10;&#32;&#32;&#32;&#32;owl:equivalentClass &#60;https://w3id.org/bot#hasBuilding> ;  &#10;&#32;&#32;&#32;&#32;owl:equivalentProperty :hasBuilding .</code></pre>|
|[Section top](#minorfail-outcome-number-163)|Pointer|<pre lang="Turtle"><code>:hasStorey a owl:ObjectProperty ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;has storey&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:comment &#34;Relation to storeys contained in a zone. The typical domains...&#34; ;  &#10;&#32;&#32;&#32;&#32;rdfs:domain owl:Thing,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#60;https://w3id.org/bot#Zone>,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;:System,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;:Zone ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy &#60;https://w3id.org/coswot/building&lowbar;automation/features> ;  &#10;&#32;&#32;&#32;&#32;rdfs:range owl:Thing,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#60;https://w3id.org/bot#Storey>,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#60;https://w3id.org/bot#Zone>,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;:Storey,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;:System,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;:Zone ;  &#10;&#32;&#32;&#32;&#32;rdfs:subClassOf &#60;https://w3id.org/bot#hasStorey>,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;:hasStorey ;  &#10;&#32;&#32;&#32;&#32;rdfs:subPropertyOf :containsZone,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;:hasStorey,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;:hasSubSystem ;  &#10;&#32;&#32;&#32;&#32;owl:equivalentClass &#60;https://w3id.org/bot#hasStorey> ;  &#10;&#32;&#32;&#32;&#32;owl:equivalentProperty :hasStorey .</code></pre>|
|[Section top](#minorfail-outcome-number-163)|Pointer|<pre lang="Turtle"><code>:hasSpace a owl:ObjectProperty ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;has space&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:comment &#34;Relation to spaces contained in a zone. The typical domains ...&#34; ;  &#10;&#32;&#32;&#32;&#32;rdfs:domain owl:Thing,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#60;https://w3id.org/bot#Zone>,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;:System,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;:Zone ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy &#60;https://w3id.org/coswot/building&lowbar;automation/features> ;  &#10;&#32;&#32;&#32;&#32;rdfs:range owl:Thing,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#60;https://w3id.org/bot#Space>,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#60;https://w3id.org/bot#Zone>,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;:Space,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;:System,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;:Zone ;  &#10;&#32;&#32;&#32;&#32;rdfs:subClassOf &#60;https://w3id.org/bot#hasSpace>,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;:hasSpace ;  &#10;&#32;&#32;&#32;&#32;rdfs:subPropertyOf :containsZone,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;:hasSpace,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;:hasSubSystem ;  &#10;&#32;&#32;&#32;&#32;owl:equivalentClass &#60;https://w3id.org/bot#hasSpace> ;  &#10;&#32;&#32;&#32;&#32;owl:equivalentProperty :hasSpace .</code></pre>|
|[Section top](#minorfail-outcome-number-163)|Pointer|<pre lang="Turtle"><code>:canWalkTo a owl:ObjectProperty,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:SymmetricProperty ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;can walk to&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:comment &#34;Links a zone to another zone one can walk to.&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:domain owl:Thing,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#60;https://w3id.org/bot#Zone>,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;:System,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;:Zone ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy &#60;https://w3id.org/coswot/building&lowbar;automation/features> ;  &#10;&#32;&#32;&#32;&#32;rdfs:range owl:Thing,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#60;https://w3id.org/bot#Zone>,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;:System,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;:Zone ;  &#10;&#32;&#32;&#32;&#32;rdfs:subPropertyOf :canWalkTo,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;:connectedTo ;  &#10;&#32;&#32;&#32;&#32;owl:equivalentProperty :canWalkTo .</code></pre>|
|[Section top](#minorfail-outcome-number-163)|Pointer|<pre lang="Turtle"><code>:adjacentZone a owl:ObjectProperty,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:SymmetricProperty ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;adjacent zone&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:comment &#34;Relationship between two zones that share a common interface...&#34; ;  &#10;&#32;&#32;&#32;&#32;rdfs:domain owl:Thing,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#60;https://w3id.org/bot#Zone>,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;:System,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;:Zone ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy &#60;https://w3id.org/coswot/building&lowbar;automation/features> ;  &#10;&#32;&#32;&#32;&#32;rdfs:range owl:Thing,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#60;https://w3id.org/bot#Zone>,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;:System,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;:Zone ;  &#10;&#32;&#32;&#32;&#32;rdfs:subPropertyOf :adjacentZone,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;:connectedTo ;  &#10;&#32;&#32;&#32;&#32;owl:equivalentProperty :adjacentZone .</code></pre>|
|[Section top](#minorfail-outcome-number-163)|Pointer|<pre lang="Turtle"><code>:adjacentElement a owl:ObjectProperty ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;adjacent element&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:comment &#34;Relation between a zone and its adjacent building elements, ...&#34; ;  &#10;&#32;&#32;&#32;&#32;rdfs:domain owl:Thing,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#60;https://w3id.org/bot#Zone>,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;:System,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;:Zone ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy &#60;https://w3id.org/coswot/building&lowbar;automation/features> ;  &#10;&#32;&#32;&#32;&#32;rdfs:range owl:Thing,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#60;https://w3id.org/bot#Element>,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;:BuildingElement,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;:System ;  &#10;&#32;&#32;&#32;&#32;rdfs:subPropertyOf :adjacentElement,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;:connectedTo ;  &#10;&#32;&#32;&#32;&#32;owl:equivalentProperty :adjacentElement .</code></pre>|

***
### MinorFail Outcome number 164

[Jump to summary definition](#summary-MinorFail-164)	|	[Previous MinorFail outcome](#minorfail-outcome-number-163)	|	[Next MinorFail outcome](#minorfail-outcome-number-165)

:exclamation:MinorFail outcome
#### Subject detail
|Name|modelet-building-automation-features|
|----|----|
|Title|Standalone modelet domains/building-automation/features/onto.ttl from branch main|
|Composition|- [Modelet building-automation/features](https://gitlab.com/coswot/coswot-acimov/blob/main/domains/building-automation/features/onto.ttl)|

#### Criterion detail
|Identifier|[domain-and-range-referencing](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#domain-and-range-referencing)|
|----|----|
|Title|Domain and range referencing test|
|Description|A test case from the Best Practices tests checking if all the ranges and domains from the test subject point to terms that are defined in the vocabulary.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-164)|Identifier|`range-out-of-vocabulary`|
|[Section top](#minorfail-outcome-number-164)|Title|Range out of vocabulary|
|[Section top](#minorfail-outcome-number-164)|Description|Some properties have a range out of the ontology|
|[Section top](#minorfail-outcome-number-164)|Pointer|<pre lang="Turtle"><code>:containsZone a owl:ObjectProperty,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:TransitiveProperty ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;contains zone&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:comment &#34;Relationship to the subzones of a major zone. A space zone c...&#34; ;  &#10;&#32;&#32;&#32;&#32;rdfs:domain owl:Thing,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#60;https://w3id.org/bot#Zone>,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;:System,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;:Zone ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy &#60;https://w3id.org/coswot/building&lowbar;automation/features> ;  &#10;&#32;&#32;&#32;&#32;rdfs:range owl:Thing,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#60;https://w3id.org/bot#Zone>,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;:System,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;:Zone ;  &#10;&#32;&#32;&#32;&#32;rdfs:subClassOf &#60;https://w3id.org/bot#containsZone>,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;:containsZone ;  &#10;&#32;&#32;&#32;&#32;rdfs:subPropertyOf :containsZone,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;:hasSubSystem ;  &#10;&#32;&#32;&#32;&#32;owl:equivalentClass &#60;https://w3id.org/bot#containsZone> ;  &#10;&#32;&#32;&#32;&#32;owl:equivalentProperty :containsZone .</code></pre>|
|[Section top](#minorfail-outcome-number-164)|Pointer|<pre lang="Turtle"><code>:Zone rdfs:subClassOf owl:Thing,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;:Zone,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;coswot:System,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;coswot:Zone ;  &#10;&#32;&#32;&#32;&#32;owl:equivalentClass coswot:Zone .</code></pre>|
|[Section top](#minorfail-outcome-number-164)|Pointer|<pre lang="Turtle"><code>:hasBuilding a owl:ObjectProperty ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;has building&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:comment &#34;Relation to buildings contained in a zone. The typical domai...&#34; ;  &#10;&#32;&#32;&#32;&#32;rdfs:domain owl:Thing,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#60;https://w3id.org/bot#Zone>,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;:System,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;:Zone ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy &#60;https://w3id.org/coswot/building&lowbar;automation/features> ;  &#10;&#32;&#32;&#32;&#32;rdfs:range owl:Thing,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#60;https://w3id.org/bot#Building>,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#60;https://w3id.org/bot#Zone>,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;:Building,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;:System,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;:Zone ;  &#10;&#32;&#32;&#32;&#32;rdfs:subClassOf &#60;https://w3id.org/bot#hasBuilding>,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;:hasBuilding ;  &#10;&#32;&#32;&#32;&#32;rdfs:subPropertyOf :containsZone,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;:hasBuilding,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;:hasSubSystem ;  &#10;&#32;&#32;&#32;&#32;owl:equivalentClass &#60;https://w3id.org/bot#hasBuilding> ;  &#10;&#32;&#32;&#32;&#32;owl:equivalentProperty :hasBuilding .</code></pre>|
|[Section top](#minorfail-outcome-number-164)|Pointer|<pre lang="Turtle"><code>:Building rdfs:subClassOf owl:Thing,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;:Building,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;:Zone,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;coswot:Building,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;coswot:System,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;coswot:Zone ;  &#10;&#32;&#32;&#32;&#32;owl:equivalentClass coswot:Building .</code></pre>|
|[Section top](#minorfail-outcome-number-164)|Pointer|<pre lang="Turtle"><code>:hasStorey a owl:ObjectProperty ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;has storey&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:comment &#34;Relation to storeys contained in a zone. The typical domains...&#34; ;  &#10;&#32;&#32;&#32;&#32;rdfs:domain owl:Thing,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#60;https://w3id.org/bot#Zone>,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;:System,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;:Zone ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy &#60;https://w3id.org/coswot/building&lowbar;automation/features> ;  &#10;&#32;&#32;&#32;&#32;rdfs:range owl:Thing,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#60;https://w3id.org/bot#Storey>,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#60;https://w3id.org/bot#Zone>,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;:Storey,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;:System,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;:Zone ;  &#10;&#32;&#32;&#32;&#32;rdfs:subClassOf &#60;https://w3id.org/bot#hasStorey>,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;:hasStorey ;  &#10;&#32;&#32;&#32;&#32;rdfs:subPropertyOf :containsZone,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;:hasStorey,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;:hasSubSystem ;  &#10;&#32;&#32;&#32;&#32;owl:equivalentClass &#60;https://w3id.org/bot#hasStorey> ;  &#10;&#32;&#32;&#32;&#32;owl:equivalentProperty :hasStorey .</code></pre>|
|[Section top](#minorfail-outcome-number-164)|Pointer|<pre lang="Turtle"><code>:Storey rdfs:subClassOf owl:Thing,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;:Storey,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;:Zone,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;coswot:Storey,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;coswot:System,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;coswot:Zone ;  &#10;&#32;&#32;&#32;&#32;owl:equivalentClass coswot:Storey .</code></pre>|
|[Section top](#minorfail-outcome-number-164)|Pointer|<pre lang="Turtle"><code>:hasSpace a owl:ObjectProperty ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;has space&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:comment &#34;Relation to spaces contained in a zone. The typical domains ...&#34; ;  &#10;&#32;&#32;&#32;&#32;rdfs:domain owl:Thing,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#60;https://w3id.org/bot#Zone>,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;:System,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;:Zone ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy &#60;https://w3id.org/coswot/building&lowbar;automation/features> ;  &#10;&#32;&#32;&#32;&#32;rdfs:range owl:Thing,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#60;https://w3id.org/bot#Space>,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#60;https://w3id.org/bot#Zone>,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;:Space,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;:System,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;:Zone ;  &#10;&#32;&#32;&#32;&#32;rdfs:subClassOf &#60;https://w3id.org/bot#hasSpace>,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;:hasSpace ;  &#10;&#32;&#32;&#32;&#32;rdfs:subPropertyOf :containsZone,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;:hasSpace,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;:hasSubSystem ;  &#10;&#32;&#32;&#32;&#32;owl:equivalentClass &#60;https://w3id.org/bot#hasSpace> ;  &#10;&#32;&#32;&#32;&#32;owl:equivalentProperty :hasSpace .</code></pre>|
|[Section top](#minorfail-outcome-number-164)|Pointer|<pre lang="Turtle"><code>:Space rdfs:subClassOf owl:Thing,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;:Space,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;:Zone,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;coswot:Space,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;coswot:System,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;coswot:Zone ;  &#10;&#32;&#32;&#32;&#32;owl:equivalentClass coswot:Space .</code></pre>|
|[Section top](#minorfail-outcome-number-164)|Pointer|<pre lang="Turtle"><code>:canWalkTo a owl:ObjectProperty,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:SymmetricProperty ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;can walk to&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:comment &#34;Links a zone to another zone one can walk to.&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:domain owl:Thing,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#60;https://w3id.org/bot#Zone>,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;:System,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;:Zone ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy &#60;https://w3id.org/coswot/building&lowbar;automation/features> ;  &#10;&#32;&#32;&#32;&#32;rdfs:range owl:Thing,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#60;https://w3id.org/bot#Zone>,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;:System,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;:Zone ;  &#10;&#32;&#32;&#32;&#32;rdfs:subPropertyOf :canWalkTo,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;:connectedTo ;  &#10;&#32;&#32;&#32;&#32;owl:equivalentProperty :canWalkTo .</code></pre>|
|[Section top](#minorfail-outcome-number-164)|Pointer|<pre lang="Turtle"><code>:adjacentZone a owl:ObjectProperty,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:SymmetricProperty ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;adjacent zone&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:comment &#34;Relationship between two zones that share a common interface...&#34; ;  &#10;&#32;&#32;&#32;&#32;rdfs:domain owl:Thing,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#60;https://w3id.org/bot#Zone>,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;:System,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;:Zone ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy &#60;https://w3id.org/coswot/building&lowbar;automation/features> ;  &#10;&#32;&#32;&#32;&#32;rdfs:range owl:Thing,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#60;https://w3id.org/bot#Zone>,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;:System,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;:Zone ;  &#10;&#32;&#32;&#32;&#32;rdfs:subPropertyOf :adjacentZone,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;:connectedTo ;  &#10;&#32;&#32;&#32;&#32;owl:equivalentProperty :adjacentZone .</code></pre>|
|[Section top](#minorfail-outcome-number-164)|Pointer|<pre lang="Turtle"><code>:adjacentElement a owl:ObjectProperty ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;adjacent element&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:comment &#34;Relation between a zone and its adjacent building elements, ...&#34; ;  &#10;&#32;&#32;&#32;&#32;rdfs:domain owl:Thing,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#60;https://w3id.org/bot#Zone>,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;:System,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;:Zone ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy &#60;https://w3id.org/coswot/building&lowbar;automation/features> ;  &#10;&#32;&#32;&#32;&#32;rdfs:range owl:Thing,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#60;https://w3id.org/bot#Element>,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;:BuildingElement,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;:System ;  &#10;&#32;&#32;&#32;&#32;rdfs:subPropertyOf :adjacentElement,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;:connectedTo ;  &#10;&#32;&#32;&#32;&#32;owl:equivalentProperty :adjacentElement .</code></pre>|
|[Section top](#minorfail-outcome-number-164)|Pointer|<pre lang="Turtle"><code>:Element rdfs:subClassOf owl:Thing,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;:Element,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;coswot:BuildingElement,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;coswot:System ;  &#10;&#32;&#32;&#32;&#32;owl:equivalentClass coswot:BuildingElement .</code></pre>|

***
### MinorFail Outcome number 165

[Jump to summary definition](#summary-MinorFail-165)	|	[Previous MinorFail outcome](#minorfail-outcome-number-164)	|	[Next MinorFail outcome](#minorfail-outcome-number-166)

:exclamation:MinorFail outcome
#### Subject detail
|Name|modelet-building-automation-features|
|----|----|
|Title|Standalone modelet domains/building-automation/features/onto.ttl from branch main|
|Composition|- [Modelet building-automation/features](https://gitlab.com/coswot/coswot-acimov/blob/main/domains/building-automation/features/onto.ttl)|

#### Criterion detail
|Identifier|[profile-compatibility](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#profile-compatibility)|
|----|----|
|Title|Profile compatibility test|
|Description|A test meant to check whether the test subject is compatible with a profile or not, and if it is not, why.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-165)|Identifier|`owl-ql-profile-error`|
|[Section top](#minorfail-outcome-number-165)|Title|OWL QL Profile incompatible|
|[Section top](#minorfail-outcome-number-165)|Description|Statement not supported|
|[Section top](#minorfail-outcome-number-165)|Pointer|<pre lang="Turtle"><code>coswot:containsZone a owl:ObjectProperty,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:TransitiveProperty ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;contains zone&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:comment &#34;Relationship to the subzones of a major zone. A space zone c...&#34; ;  &#10;&#32;&#32;&#32;&#32;rdfs:domain coswot:Zone ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy &#60;https://w3id.org/coswot/building&lowbar;automation/features> ;  &#10;&#32;&#32;&#32;&#32;rdfs:range coswot:Zone ;  &#10;&#32;&#32;&#32;&#32;rdfs:subPropertyOf coswot:hasSubSystem ;  &#10;&#32;&#32;&#32;&#32;owl:equivalentClass &#60;https://w3id.org/bot#containsZone> .</code></pre>|

***
### MinorFail Outcome number 166

[Jump to summary definition](#summary-MinorFail-166)	|	[Previous MinorFail outcome](#minorfail-outcome-number-165)	|	[Next MinorFail outcome](#minorfail-outcome-number-167)

:exclamation:MinorFail outcome
#### Subject detail
|Name|modelet-building-automation-features|
|----|----|
|Title|Standalone modelet domains/building-automation/features/onto.ttl from branch main|
|Composition|- [Modelet building-automation/features](https://gitlab.com/coswot/coswot-acimov/blob/main/domains/building-automation/features/onto.ttl)|

#### Criterion detail
|Identifier|[profile-compatibility](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#profile-compatibility)|
|----|----|
|Title|Profile compatibility test|
|Description|A test meant to check whether the test subject is compatible with a profile or not, and if it is not, why.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-166)|Identifier|`owl-el-profile-error`|
|[Section top](#minorfail-outcome-number-166)|Title|OWL EL Profile incompatible|
|[Section top](#minorfail-outcome-number-166)|Description|Statement not supported|
|[Section top](#minorfail-outcome-number-166)|Pointer|<pre lang="Turtle"><code>coswot:canWalkTo a owl:ObjectProperty,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:SymmetricProperty ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;can walk to&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:comment &#34;Links a zone to another zone one can walk to.&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:domain coswot:Zone ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy &#60;https://w3id.org/coswot/building&lowbar;automation/features> ;  &#10;&#32;&#32;&#32;&#32;rdfs:range coswot:Zone ;  &#10;&#32;&#32;&#32;&#32;rdfs:subPropertyOf coswot:connectedTo .</code></pre>|

***
### MinorFail Outcome number 167

[Jump to summary definition](#summary-MinorFail-167)	|	[Previous MinorFail outcome](#minorfail-outcome-number-166)	|	Next MinorFail outcome

:exclamation:MinorFail outcome
#### Subject detail
|Name|modelet-building-automation-features|
|----|----|
|Title|Standalone modelet domains/building-automation/features/onto.ttl from branch main|
|Composition|- [Modelet building-automation/features](https://gitlab.com/coswot/coswot-acimov/blob/main/domains/building-automation/features/onto.ttl)|

#### Criterion detail
|Identifier|[terms-differenciation](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#terms-differenciation)|
|----|----|
|Title|Terms differenciation test|
|Description|A test case from the Best Practices tests checking if all the terms are different enough from each other according to the Levenshtein distance metric.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-167)|Identifier|`too-close-terms`|
|[Section top](#minorfail-outcome-number-167)|Title|Too close terms|
|[Section top](#minorfail-outcome-number-167)|Description|Some terms are too similar|
|[Section top](#minorfail-outcome-number-167)|Pointer|<pre lang="Turtle"><code>:Room a owl:Class ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;Room&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:comment &#34;A part of the physical world or a virtual world whose 3D spa...&#34; ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy &#60;https://w3id.org/coswot/building&lowbar;automation/features> ;  &#10;&#32;&#32;&#32;&#32;rdfs:subClassOf :Space .</code></pre>|
|[Section top](#minorfail-outcome-number-167)|Pointer|<pre lang="Turtle"><code>:Door a owl:Class ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;Door&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:comment &#34;Definition from ISO 6707-1:1989: Construction for closing an...&#34; ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy &#60;https://w3id.org/coswot/building&lowbar;automation/features> ;  &#10;&#32;&#32;&#32;&#32;rdfs:subClassOf :BuildingElement .</code></pre>|

***

</details>

***
