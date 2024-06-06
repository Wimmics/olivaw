# Test Report Markdown Export

This file is an export of the RDF test report made out of [EARL vocabulary](https://www.w3.org/TR/EARL10/)

This test is powered by Corese, check the [website](https://project.inria.fr/corese/) and the [repository](https://github.com/Wimmics/corese)

The original test report is available in turtle syntax [here](./model-test-manual-NicoRobertIn-2024-06-06T11-59-10.ttl).

# Test Context

Here is some context about under which context this test was made

|Assertor|[NicoRobertIn](https://github.com/NicoRobertIn)|
|----|-----|
|Title|NicoRobertIn using manual script|
|Description|Test triggered by [@NicoRobertIn](https://github.com/NicoRobertIn) by manual trigger|
|Script|[model test suite](https://github.com/Wimmics/olivaw/blob/main/olivaw/test/model/suite.py)
|Date|2024-06-06 11:58:42|

***


# Statistic summary

Here is a short overview for this test report

161 Outcomes

:boom:0 MajorFail, :exclamation:161 MinorFail, :warning:0 CannotTell, :grey_question:0 NotTested, :white_check_mark:0 Pass

<div  style="border-radius: 12px; height: 25px; overflow: hidden"><img src="../assets/red.png" width="0%" height="25px"/><img src="../assets/orange.png" width="100%" height="25px"/><img src="../assets/grey.png" width="0%" height="25px"/><img src="../assets/white.png" width="0%" height="25px"/><img src="../assets/green.png" width="0%" height="25px"/></div>

<br/>

The different status types are an extension of the [EARL](https://www.w3.org/TR/EARL10-Schema/) vocabulary where the nextended terms can be found in the [olivaw-earl dataset](https://github.com/Wimmics/olivaw/blob/main/olivaw/test/olivaw-earl.ttl), each outcome type means:
* :boom: MajorFail: This is an error that is critical and consider as blocking for production
* :exclamation: MinorFail: This is an error that should be fixed, but it is cannot be considered as critical error
* :warning: CannotTell: It is unclear if the subject passed or failed the test. This happens when an automated test requires human judgement to make a definite decision.
* :grey_question: NotTested:  The test has not been carried out. Here this is because a previous test that was mandatory to be passed did not end up as Pass.
* :white_check_mark: Pass: The subject passed the test.

***


# MinorFail Outcomes

[Jump to statistic summary](#statistic-summary)	|	Previous section	|	Next section

Here is the chapter related to the MinorFail outcome

:exclamation:161 MinorFail outcomes

<details>
<summary>Fold/Unfold the 161 summary and details</summary>

## MinorFail Outcomes Summary

:exclamation:161 MinorFail outcomes

|*Jump*|*Number*|*Status*|*Subject*|*Criterion*|*Title*|*Link*|
|------|--------|--------|---------|-----------|-------|------|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-1">1/161</div>|:exclamation:MinorFail|`module-src-vocabularies-quantity-kinds`|[labeled-terms](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#labeled-terms)|Terms not labeled|[Jump](#minorfail-outcome-number-1)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-2">2/161</div>|:exclamation:MinorFail|`module-src-vocabularies-quantity-kinds`|[profile-compatibility](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#profile-compatibility)|OWL QL Profile incompatible|[Jump](#minorfail-outcome-number-2)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-3">3/161</div>|:exclamation:MinorFail|`module-src-vocabularies-quantity-kinds`|[profile-compatibility](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#profile-compatibility)|OWL QL Profile incompatible|[Jump](#minorfail-outcome-number-3)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-4">4/161</div>|:exclamation:MinorFail|`module-src-vocabularies-quantity-kinds`|[profile-compatibility](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#profile-compatibility)|OWL QL Profile incompatible|[Jump](#minorfail-outcome-number-4)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-5">5/161</div>|:exclamation:MinorFail|`module-src-vocabularies-quantity-kinds`|[terms-differenciation](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#terms-differenciation)|Too close terms|[Jump](#minorfail-outcome-number-5)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-6">6/161</div>|:exclamation:MinorFail|`module-src-vocabularies-permitting-stages`|[domain-and-range-referencing](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#domain-and-range-referencing)|Range out of vocabulary|[Jump](#minorfail-outcome-number-6)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-7">7/161</div>|:exclamation:MinorFail|`module-src-vocabularies-permitting-stages`|[labeled-terms](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#labeled-terms)|Terms not labeled|[Jump](#minorfail-outcome-number-7)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-8">8/161</div>|:exclamation:MinorFail|`module-src-vocabularies-permitting-stages`|[profile-compatibility](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#profile-compatibility)|OWL QL Profile incompatible|[Jump](#minorfail-outcome-number-8)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-9">9/161</div>|:exclamation:MinorFail|`module-src-vocabularies-permitting-stages`|[profile-compatibility](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#profile-compatibility)|OWL QL Profile incompatible|[Jump](#minorfail-outcome-number-9)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-10">10/161</div>|:exclamation:MinorFail|`module-src-vocabularies-permitting-stages`|[profile-compatibility](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#profile-compatibility)|OWL QL Profile incompatible|[Jump](#minorfail-outcome-number-10)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-11">11/161</div>|:exclamation:MinorFail|`module-src-vocabularies-disciplines`|[domain-and-range-referencing](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#domain-and-range-referencing)|Range out of vocabulary|[Jump](#minorfail-outcome-number-11)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-12">12/161</div>|:exclamation:MinorFail|`module-src-vocabularies-disciplines`|[labeled-terms](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#labeled-terms)|Terms not labeled|[Jump](#minorfail-outcome-number-12)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-13">13/161</div>|:exclamation:MinorFail|`module-src-vocabularies-disciplines`|[profile-compatibility](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#profile-compatibility)|OWL QL Profile incompatible|[Jump](#minorfail-outcome-number-13)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-14">14/161</div>|:exclamation:MinorFail|`module-src-vocabularies-disciplines`|[profile-compatibility](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#profile-compatibility)|OWL QL Profile incompatible|[Jump](#minorfail-outcome-number-14)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-15">15/161</div>|:exclamation:MinorFail|`module-src-vocabularies-disciplines`|[profile-compatibility](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#profile-compatibility)|OWL QL Profile incompatible|[Jump](#minorfail-outcome-number-15)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-16">16/161</div>|:exclamation:MinorFail|`module-src-vocabularies-check-method-operators`|[labeled-terms](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#labeled-terms)|Terms not labeled|[Jump](#minorfail-outcome-number-16)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-17">17/161</div>|:exclamation:MinorFail|`module-src-vocabularies-check-method-operators`|[profile-compatibility](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#profile-compatibility)|OWL QL Profile incompatible|[Jump](#minorfail-outcome-number-17)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-18">18/161</div>|:exclamation:MinorFail|`module-src-vocabularies-check-method-operators`|[profile-compatibility](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#profile-compatibility)|OWL QL Profile incompatible|[Jump](#minorfail-outcome-number-18)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-19">19/161</div>|:exclamation:MinorFail|`module-src-vocabularies-check-method-operators`|[profile-compatibility](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#profile-compatibility)|OWL QL Profile incompatible|[Jump](#minorfail-outcome-number-19)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-20">20/161</div>|:exclamation:MinorFail|`module-src-vocabularies-check-method-operators`|[profile-compatibility](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#profile-compatibility)|OWL EL Profile incompatible|[Jump](#minorfail-outcome-number-20)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-21">21/161</div>|:exclamation:MinorFail|`module-src-vocabularies-check-method-comparators`|[labeled-terms](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#labeled-terms)|Terms not labeled|[Jump](#minorfail-outcome-number-21)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-22">22/161</div>|:exclamation:MinorFail|`module-src-vocabularies-check-method-comparators`|[profile-compatibility](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#profile-compatibility)|OWL QL Profile incompatible|[Jump](#minorfail-outcome-number-22)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-23">23/161</div>|:exclamation:MinorFail|`module-src-vocabularies-check-method-comparators`|[profile-compatibility](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#profile-compatibility)|OWL QL Profile incompatible|[Jump](#minorfail-outcome-number-23)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-24">24/161</div>|:exclamation:MinorFail|`module-src-vocabularies-check-method-comparators`|[profile-compatibility](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#profile-compatibility)|OWL QL Profile incompatible|[Jump](#minorfail-outcome-number-24)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-25">25/161</div>|:exclamation:MinorFail|`module-src-vocabularies-check-method-comparators`|[profile-compatibility](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#profile-compatibility)|OWL EL Profile incompatible|[Jump](#minorfail-outcome-number-25)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-26">26/161</div>|:exclamation:MinorFail|`module-src-vocabularies-check-method-comparators`|[terms-differenciation](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#terms-differenciation)|Too close terms|[Jump](#minorfail-outcome-number-26)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-27">27/161</div>|:exclamation:MinorFail|`module-src-vocabularies-building-usage`|[domain-and-range-referencing](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#domain-and-range-referencing)|Range out of vocabulary|[Jump](#minorfail-outcome-number-27)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-28">28/161</div>|:exclamation:MinorFail|`module-src-vocabularies-building-usage`|[labeled-terms](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#labeled-terms)|Terms not labeled|[Jump](#minorfail-outcome-number-28)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-29">29/161</div>|:exclamation:MinorFail|`module-src-vocabularies-building-usage`|[profile-compatibility](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#profile-compatibility)|OWL QL Profile incompatible|[Jump](#minorfail-outcome-number-29)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-30">30/161</div>|:exclamation:MinorFail|`module-src-vocabularies-building-usage`|[profile-compatibility](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#profile-compatibility)|OWL QL Profile incompatible|[Jump](#minorfail-outcome-number-30)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-31">31/161</div>|:exclamation:MinorFail|`module-src-vocabularies-building-usage`|[profile-compatibility](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#profile-compatibility)|OWL QL Profile incompatible|[Jump](#minorfail-outcome-number-31)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-32">32/161</div>|:exclamation:MinorFail|`module-src-vocabularies-building-usage`|[profile-compatibility](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#profile-compatibility)|OWL EL Profile incompatible|[Jump](#minorfail-outcome-number-32)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-33">33/161</div>|:exclamation:MinorFail|`module-src-vocabularies-building-structure`|[domain-and-range-referencing](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#domain-and-range-referencing)|Range out of vocabulary|[Jump](#minorfail-outcome-number-33)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-34">34/161</div>|:exclamation:MinorFail|`module-src-vocabularies-building-structure`|[labeled-terms](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#labeled-terms)|Terms not labeled|[Jump](#minorfail-outcome-number-34)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-35">35/161</div>|:exclamation:MinorFail|`module-src-vocabularies-building-structure`|[profile-compatibility](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#profile-compatibility)|OWL QL Profile incompatible|[Jump](#minorfail-outcome-number-35)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-36">36/161</div>|:exclamation:MinorFail|`module-src-vocabularies-building-structure`|[profile-compatibility](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#profile-compatibility)|OWL QL Profile incompatible|[Jump](#minorfail-outcome-number-36)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-37">37/161</div>|:exclamation:MinorFail|`module-src-vocabularies-building-structure`|[profile-compatibility](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#profile-compatibility)|OWL QL Profile incompatible|[Jump](#minorfail-outcome-number-37)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-38">38/161</div>|:exclamation:MinorFail|`module-src-vocabularies-building-structure`|[profile-compatibility](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#profile-compatibility)|OWL EL Profile incompatible|[Jump](#minorfail-outcome-number-38)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-39">39/161</div>|:exclamation:MinorFail|`module-src-vocabularies-administrative-areas`|[domain-and-range-referencing](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#domain-and-range-referencing)|Range out of vocabulary|[Jump](#minorfail-outcome-number-39)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-40">40/161</div>|:exclamation:MinorFail|`module-src-vocabularies-administrative-areas`|[labeled-terms](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#labeled-terms)|Terms not labeled|[Jump](#minorfail-outcome-number-40)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-41">41/161</div>|:exclamation:MinorFail|`module-src-vocabularies-administrative-areas`|[profile-compatibility](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#profile-compatibility)|OWL QL Profile incompatible|[Jump](#minorfail-outcome-number-41)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-42">42/161</div>|:exclamation:MinorFail|`module-src-vocabularies-administrative-areas`|[profile-compatibility](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#profile-compatibility)|OWL QL Profile incompatible|[Jump](#minorfail-outcome-number-42)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-43">43/161</div>|:exclamation:MinorFail|`module-src-vocabularies-administrative-areas`|[profile-compatibility](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#profile-compatibility)|OWL QL Profile incompatible|[Jump](#minorfail-outcome-number-43)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-44">44/161</div>|:exclamation:MinorFail|`module-src-table`|[profile-compatibility](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#profile-compatibility)|OWL RL Profile incompatible|[Jump](#minorfail-outcome-number-44)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-45">45/161</div>|:exclamation:MinorFail|`module-src-table`|[profile-compatibility](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#profile-compatibility)|OWL RL Profile incompatible|[Jump](#minorfail-outcome-number-45)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-46">46/161</div>|:exclamation:MinorFail|`module-src-table`|[profile-compatibility](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#profile-compatibility)|OWL QL Profile incompatible|[Jump](#minorfail-outcome-number-46)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-47">47/161</div>|:exclamation:MinorFail|`module-src-table`|[profile-compatibility](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#profile-compatibility)|OWL QL Profile incompatible|[Jump](#minorfail-outcome-number-47)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-48">48/161</div>|:exclamation:MinorFail|`module-src-table`|[profile-compatibility](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#profile-compatibility)|OWL EL Profile incompatible|[Jump](#minorfail-outcome-number-48)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-49">49/161</div>|:exclamation:MinorFail|`module-src-table`|[profile-compatibility](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#profile-compatibility)|OWL EL Profile incompatible|[Jump](#minorfail-outcome-number-49)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-50">50/161</div>|:exclamation:MinorFail|`module-src-statement`|[profile-compatibility](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#profile-compatibility)|OWL RL Profile incompatible|[Jump](#minorfail-outcome-number-50)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-51">51/161</div>|:exclamation:MinorFail|`module-src-statement`|[profile-compatibility](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#profile-compatibility)|OWL RL Profile incompatible|[Jump](#minorfail-outcome-number-51)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-52">52/161</div>|:exclamation:MinorFail|`module-src-statement`|[profile-compatibility](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#profile-compatibility)|OWL QL Profile incompatible|[Jump](#minorfail-outcome-number-52)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-53">53/161</div>|:exclamation:MinorFail|`module-src-statement`|[profile-compatibility](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#profile-compatibility)|OWL QL Profile incompatible|[Jump](#minorfail-outcome-number-53)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-54">54/161</div>|:exclamation:MinorFail|`module-src-statement`|[profile-compatibility](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#profile-compatibility)|OWL QL Profile incompatible|[Jump](#minorfail-outcome-number-54)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-55">55/161</div>|:exclamation:MinorFail|`module-src-statement`|[profile-compatibility](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#profile-compatibility)|OWL EL Profile incompatible|[Jump](#minorfail-outcome-number-55)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-56">56/161</div>|:exclamation:MinorFail|`module-src-statement`|[profile-compatibility](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#profile-compatibility)|OWL EL Profile incompatible|[Jump](#minorfail-outcome-number-56)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-57">57/161</div>|:exclamation:MinorFail|`module-src-statement`|[profile-compatibility](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#profile-compatibility)|OWL EL Profile incompatible|[Jump](#minorfail-outcome-number-57)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-58">58/161</div>|:exclamation:MinorFail|`module-src-statement`|[terms-differenciation](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#terms-differenciation)|Too close terms|[Jump](#minorfail-outcome-number-58)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-59">59/161</div>|:exclamation:MinorFail|`module-src-model`|[profile-compatibility](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#profile-compatibility)|OWL RL Profile incompatible|[Jump](#minorfail-outcome-number-59)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-60">60/161</div>|:exclamation:MinorFail|`module-src-model`|[profile-compatibility](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#profile-compatibility)|OWL RL Profile incompatible|[Jump](#minorfail-outcome-number-60)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-61">61/161</div>|:exclamation:MinorFail|`module-src-model`|[profile-compatibility](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#profile-compatibility)|OWL QL Profile incompatible|[Jump](#minorfail-outcome-number-61)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-62">62/161</div>|:exclamation:MinorFail|`module-src-model`|[profile-compatibility](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#profile-compatibility)|OWL QL Profile incompatible|[Jump](#minorfail-outcome-number-62)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-63">63/161</div>|:exclamation:MinorFail|`module-src-model`|[profile-compatibility](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#profile-compatibility)|OWL EL Profile incompatible|[Jump](#minorfail-outcome-number-63)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-64">64/161</div>|:exclamation:MinorFail|`module-src-model`|[profile-compatibility](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#profile-compatibility)|OWL EL Profile incompatible|[Jump](#minorfail-outcome-number-64)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-65">65/161</div>|:exclamation:MinorFail|`module-src-model`|[term-referencing](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#term-referencing)|Term not referenced to a module|[Jump](#minorfail-outcome-number-65)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-66">66/161</div>|:exclamation:MinorFail|`module-src-legal-verifier`|[profile-compatibility](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#profile-compatibility)|OWL QL Profile incompatible|[Jump](#minorfail-outcome-number-66)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-67">67/161</div>|:exclamation:MinorFail|`module-src-legal-verifier`|[profile-compatibility](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#profile-compatibility)|OWL QL Profile incompatible|[Jump](#minorfail-outcome-number-67)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-68">68/161</div>|:exclamation:MinorFail|`module-src-legal-verifier`|[profile-compatibility](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#profile-compatibility)|OWL EL Profile incompatible|[Jump](#minorfail-outcome-number-68)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-69">69/161</div>|:exclamation:MinorFail|`module-src-legal-verifier`|[profile-compatibility](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#profile-compatibility)|OWL EL Profile incompatible|[Jump](#minorfail-outcome-number-69)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-70">70/161</div>|:exclamation:MinorFail|`module-src-feature-of-interest`|[domain-and-range-referencing](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#domain-and-range-referencing)|Domain out of vocabulary|[Jump](#minorfail-outcome-number-70)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-71">71/161</div>|:exclamation:MinorFail|`module-src-feature-of-interest`|[domain-and-range-referencing](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#domain-and-range-referencing)|Range out of vocabulary|[Jump](#minorfail-outcome-number-71)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-72">72/161</div>|:exclamation:MinorFail|`module-src-evidence`|[domain-and-range-referencing](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#domain-and-range-referencing)|Range out of vocabulary|[Jump](#minorfail-outcome-number-72)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-73">73/161</div>|:exclamation:MinorFail|`module-src-evidence`|[labeled-terms](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#labeled-terms)|Terms not labeled|[Jump](#minorfail-outcome-number-73)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-74">74/161</div>|:exclamation:MinorFail|`module-src-document`|[profile-compatibility](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#profile-compatibility)|OWL RL Profile incompatible|[Jump](#minorfail-outcome-number-74)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-75">75/161</div>|:exclamation:MinorFail|`module-src-document`|[profile-compatibility](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#profile-compatibility)|OWL RL Profile incompatible|[Jump](#minorfail-outcome-number-75)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-76">76/161</div>|:exclamation:MinorFail|`module-src-document`|[profile-compatibility](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#profile-compatibility)|OWL QL Profile incompatible|[Jump](#minorfail-outcome-number-76)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-77">77/161</div>|:exclamation:MinorFail|`module-src-document`|[profile-compatibility](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#profile-compatibility)|OWL QL Profile incompatible|[Jump](#minorfail-outcome-number-77)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-78">78/161</div>|:exclamation:MinorFail|`module-src-document`|[profile-compatibility](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#profile-compatibility)|OWL QL Profile incompatible|[Jump](#minorfail-outcome-number-78)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-79">79/161</div>|:exclamation:MinorFail|`module-src-document`|[profile-compatibility](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#profile-compatibility)|OWL EL Profile incompatible|[Jump](#minorfail-outcome-number-79)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-80">80/161</div>|:exclamation:MinorFail|`module-src-document`|[profile-compatibility](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#profile-compatibility)|OWL EL Profile incompatible|[Jump](#minorfail-outcome-number-80)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-81">81/161</div>|:exclamation:MinorFail|`module-src-document`|[profile-compatibility](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#profile-compatibility)|OWL EL Profile incompatible|[Jump](#minorfail-outcome-number-81)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-82">82/161</div>|:exclamation:MinorFail|`module-src-compliance-verification-report`|[profile-compatibility](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#profile-compatibility)|OWL RL Profile incompatible|[Jump](#minorfail-outcome-number-82)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-83">83/161</div>|:exclamation:MinorFail|`module-src-compliance-verification-report`|[profile-compatibility](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#profile-compatibility)|OWL RL Profile incompatible|[Jump](#minorfail-outcome-number-83)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-84">84/161</div>|:exclamation:MinorFail|`module-src-compliance-verification-report`|[profile-compatibility](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#profile-compatibility)|OWL QL Profile incompatible|[Jump](#minorfail-outcome-number-84)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-85">85/161</div>|:exclamation:MinorFail|`module-src-compliance-verification-report`|[profile-compatibility](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#profile-compatibility)|OWL QL Profile incompatible|[Jump](#minorfail-outcome-number-85)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-86">86/161</div>|:exclamation:MinorFail|`module-src-compliance-verification-report`|[profile-compatibility](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#profile-compatibility)|OWL QL Profile incompatible|[Jump](#minorfail-outcome-number-86)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-87">87/161</div>|:exclamation:MinorFail|`module-src-compliance-verification-report`|[profile-compatibility](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#profile-compatibility)|OWL EL Profile incompatible|[Jump](#minorfail-outcome-number-87)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-88">88/161</div>|:exclamation:MinorFail|`module-src-compliance-verification-report`|[profile-compatibility](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#profile-compatibility)|OWL EL Profile incompatible|[Jump](#minorfail-outcome-number-88)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-89">89/161</div>|:exclamation:MinorFail|`module-src-compliance-verification-report`|[profile-compatibility](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#profile-compatibility)|OWL EL Profile incompatible|[Jump](#minorfail-outcome-number-89)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-90">90/161</div>|:exclamation:MinorFail|`module-src-compliance-verification-report`|[terms-differenciation](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#terms-differenciation)|Too close terms|[Jump](#minorfail-outcome-number-90)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-91">91/161</div>|:exclamation:MinorFail|`module-src-checking-act`|[domain-and-range-referencing](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#domain-and-range-referencing)|Domain out of vocabulary|[Jump](#minorfail-outcome-number-91)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-92">92/161</div>|:exclamation:MinorFail|`module-src-checking-act`|[profile-compatibility](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#profile-compatibility)|OWL RL Profile incompatible|[Jump](#minorfail-outcome-number-92)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-93">93/161</div>|:exclamation:MinorFail|`module-src-checking-act`|[profile-compatibility](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#profile-compatibility)|OWL RL Profile incompatible|[Jump](#minorfail-outcome-number-93)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-94">94/161</div>|:exclamation:MinorFail|`module-src-check-method`|[domain-and-range-referencing](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#domain-and-range-referencing)|Domain out of vocabulary|[Jump](#minorfail-outcome-number-94)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-95">95/161</div>|:exclamation:MinorFail|`module-src-check-method`|[domain-and-range-referencing](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#domain-and-range-referencing)|Range out of vocabulary|[Jump](#minorfail-outcome-number-95)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-96">96/161</div>|:exclamation:MinorFail|`module-src-check-method`|[profile-compatibility](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#profile-compatibility)|OWL RL Profile incompatible|[Jump](#minorfail-outcome-number-96)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-97">97/161</div>|:exclamation:MinorFail|`module-src-check-method`|[profile-compatibility](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#profile-compatibility)|OWL RL Profile incompatible|[Jump](#minorfail-outcome-number-97)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-98">98/161</div>|:exclamation:MinorFail|`module-src-check-method`|[profile-compatibility](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#profile-compatibility)|OWL RL Profile incompatible|[Jump](#minorfail-outcome-number-98)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-99">99/161</div>|:exclamation:MinorFail|`module-src-check-method`|[profile-compatibility](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#profile-compatibility)|OWL RL Profile incompatible|[Jump](#minorfail-outcome-number-99)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-100">100/161</div>|:exclamation:MinorFail|`module-src-check-method`|[profile-compatibility](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#profile-compatibility)|OWL RL Profile incompatible|[Jump](#minorfail-outcome-number-100)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-101">101/161</div>|:exclamation:MinorFail|`module-src-check-method`|[profile-compatibility](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#profile-compatibility)|OWL QL Profile incompatible|[Jump](#minorfail-outcome-number-101)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-102">102/161</div>|:exclamation:MinorFail|`module-src-check-method`|[profile-compatibility](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#profile-compatibility)|OWL QL Profile incompatible|[Jump](#minorfail-outcome-number-102)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-103">103/161</div>|:exclamation:MinorFail|`module-src-check-method`|[profile-compatibility](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#profile-compatibility)|OWL QL Profile incompatible|[Jump](#minorfail-outcome-number-103)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-104">104/161</div>|:exclamation:MinorFail|`module-src-check-method`|[profile-compatibility](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#profile-compatibility)|OWL QL Profile incompatible|[Jump](#minorfail-outcome-number-104)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-105">105/161</div>|:exclamation:MinorFail|`module-src-check-method`|[profile-compatibility](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#profile-compatibility)|OWL QL Profile incompatible|[Jump](#minorfail-outcome-number-105)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-106">106/161</div>|:exclamation:MinorFail|`module-src-check-method`|[profile-compatibility](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#profile-compatibility)|OWL EL Profile incompatible|[Jump](#minorfail-outcome-number-106)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-107">107/161</div>|:exclamation:MinorFail|`module-src-check-method`|[profile-compatibility](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#profile-compatibility)|OWL EL Profile incompatible|[Jump](#minorfail-outcome-number-107)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-108">108/161</div>|:exclamation:MinorFail|`module-src-check-method`|[profile-compatibility](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#profile-compatibility)|OWL EL Profile incompatible|[Jump](#minorfail-outcome-number-108)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-109">109/161</div>|:exclamation:MinorFail|`module-src-check-method`|[profile-compatibility](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#profile-compatibility)|OWL EL Profile incompatible|[Jump](#minorfail-outcome-number-109)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-110">110/161</div>|:exclamation:MinorFail|`module-src-check-method`|[term-referencing](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#term-referencing)|Term not referenced to a module|[Jump](#minorfail-outcome-number-110)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-111">111/161</div>|:exclamation:MinorFail|`module-src-aec3po`|[profile-compatibility](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#profile-compatibility)|OWL RL Profile incompatible|[Jump](#minorfail-outcome-number-111)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-112">112/161</div>|:exclamation:MinorFail|`module-src-aec3po`|[profile-compatibility](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#profile-compatibility)|OWL RL Profile incompatible|[Jump](#minorfail-outcome-number-112)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-113">113/161</div>|:exclamation:MinorFail|`module-src-aec3po`|[profile-compatibility](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#profile-compatibility)|OWL QL Profile incompatible|[Jump](#minorfail-outcome-number-113)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-114">114/161</div>|:exclamation:MinorFail|`module-src-aec3po`|[profile-compatibility](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#profile-compatibility)|OWL QL Profile incompatible|[Jump](#minorfail-outcome-number-114)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-115">115/161</div>|:exclamation:MinorFail|`module-src-aec3po`|[profile-compatibility](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#profile-compatibility)|OWL EL Profile incompatible|[Jump](#minorfail-outcome-number-115)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-116">116/161</div>|:exclamation:MinorFail|`module-src-aec3po`|[profile-compatibility](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#profile-compatibility)|OWL EL Profile incompatible|[Jump](#minorfail-outcome-number-116)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-117">117/161</div>|:exclamation:MinorFail|`module-src-aec3po`|[term-referencing](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#term-referencing)|Term not referenced to a module|[Jump](#minorfail-outcome-number-117)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-118">118/161</div>|:exclamation:MinorFail|`all-modules`|[domain-and-range-referencing](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#domain-and-range-referencing)|Domain out of vocabulary|[Jump](#minorfail-outcome-number-118)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-119">119/161</div>|:exclamation:MinorFail|`all-modules`|[domain-and-range-referencing](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#domain-and-range-referencing)|Range out of vocabulary|[Jump](#minorfail-outcome-number-119)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-120">120/161</div>|:exclamation:MinorFail|`all-modules`|[labeled-terms](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#labeled-terms)|Terms not labeled|[Jump](#minorfail-outcome-number-120)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-121">121/161</div>|:exclamation:MinorFail|`all-modules`|[profile-compatibility](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#profile-compatibility)|OWL RL Profile incompatible|[Jump](#minorfail-outcome-number-121)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-122">122/161</div>|:exclamation:MinorFail|`all-modules`|[profile-compatibility](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#profile-compatibility)|OWL RL Profile incompatible|[Jump](#minorfail-outcome-number-122)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-123">123/161</div>|:exclamation:MinorFail|`all-modules`|[profile-compatibility](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#profile-compatibility)|OWL RL Profile incompatible|[Jump](#minorfail-outcome-number-123)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-124">124/161</div>|:exclamation:MinorFail|`all-modules`|[profile-compatibility](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#profile-compatibility)|OWL RL Profile incompatible|[Jump](#minorfail-outcome-number-124)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-125">125/161</div>|:exclamation:MinorFail|`all-modules`|[profile-compatibility](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#profile-compatibility)|OWL RL Profile incompatible|[Jump](#minorfail-outcome-number-125)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-126">126/161</div>|:exclamation:MinorFail|`all-modules`|[profile-compatibility](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#profile-compatibility)|OWL RL Profile incompatible|[Jump](#minorfail-outcome-number-126)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-127">127/161</div>|:exclamation:MinorFail|`all-modules`|[profile-compatibility](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#profile-compatibility)|OWL QL Profile incompatible|[Jump](#minorfail-outcome-number-127)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-128">128/161</div>|:exclamation:MinorFail|`all-modules`|[profile-compatibility](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#profile-compatibility)|OWL QL Profile incompatible|[Jump](#minorfail-outcome-number-128)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-129">129/161</div>|:exclamation:MinorFail|`all-modules`|[profile-compatibility](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#profile-compatibility)|OWL QL Profile incompatible|[Jump](#minorfail-outcome-number-129)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-130">130/161</div>|:exclamation:MinorFail|`all-modules`|[profile-compatibility](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#profile-compatibility)|OWL QL Profile incompatible|[Jump](#minorfail-outcome-number-130)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-131">131/161</div>|:exclamation:MinorFail|`all-modules`|[profile-compatibility](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#profile-compatibility)|OWL QL Profile incompatible|[Jump](#minorfail-outcome-number-131)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-132">132/161</div>|:exclamation:MinorFail|`all-modules`|[profile-compatibility](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#profile-compatibility)|OWL QL Profile incompatible|[Jump](#minorfail-outcome-number-132)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-133">133/161</div>|:exclamation:MinorFail|`all-modules`|[profile-compatibility](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#profile-compatibility)|OWL EL Profile incompatible|[Jump](#minorfail-outcome-number-133)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-134">134/161</div>|:exclamation:MinorFail|`all-modules`|[profile-compatibility](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#profile-compatibility)|OWL EL Profile incompatible|[Jump](#minorfail-outcome-number-134)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-135">135/161</div>|:exclamation:MinorFail|`all-modules`|[profile-compatibility](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#profile-compatibility)|OWL EL Profile incompatible|[Jump](#minorfail-outcome-number-135)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-136">136/161</div>|:exclamation:MinorFail|`all-modules`|[profile-compatibility](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#profile-compatibility)|OWL EL Profile incompatible|[Jump](#minorfail-outcome-number-136)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-137">137/161</div>|:exclamation:MinorFail|`all-modules`|[profile-compatibility](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#profile-compatibility)|OWL EL Profile incompatible|[Jump](#minorfail-outcome-number-137)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-138">138/161</div>|:exclamation:MinorFail|`all-modules`|[term-referencing](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#term-referencing)|Term not referenced to a module|[Jump](#minorfail-outcome-number-138)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-139">139/161</div>|:exclamation:MinorFail|`all-modules`|[terms-differenciation](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#terms-differenciation)|Too close terms|[Jump](#minorfail-outcome-number-139)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-140">140/161</div>|:exclamation:MinorFail|`all-fragments`|[domain-and-range-referencing](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#domain-and-range-referencing)|Domain out of vocabulary|[Jump](#minorfail-outcome-number-140)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-141">141/161</div>|:exclamation:MinorFail|`all-fragments`|[domain-and-range-referencing](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#domain-and-range-referencing)|Range out of vocabulary|[Jump](#minorfail-outcome-number-141)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-142">142/161</div>|:exclamation:MinorFail|`all-fragments`|[labeled-terms](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#labeled-terms)|Terms not labeled|[Jump](#minorfail-outcome-number-142)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-143">143/161</div>|:exclamation:MinorFail|`all-fragments`|[profile-compatibility](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#profile-compatibility)|OWL RL Profile incompatible|[Jump](#minorfail-outcome-number-143)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-144">144/161</div>|:exclamation:MinorFail|`all-fragments`|[profile-compatibility](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#profile-compatibility)|OWL RL Profile incompatible|[Jump](#minorfail-outcome-number-144)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-145">145/161</div>|:exclamation:MinorFail|`all-fragments`|[profile-compatibility](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#profile-compatibility)|OWL RL Profile incompatible|[Jump](#minorfail-outcome-number-145)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-146">146/161</div>|:exclamation:MinorFail|`all-fragments`|[profile-compatibility](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#profile-compatibility)|OWL RL Profile incompatible|[Jump](#minorfail-outcome-number-146)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-147">147/161</div>|:exclamation:MinorFail|`all-fragments`|[profile-compatibility](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#profile-compatibility)|OWL RL Profile incompatible|[Jump](#minorfail-outcome-number-147)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-148">148/161</div>|:exclamation:MinorFail|`all-fragments`|[profile-compatibility](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#profile-compatibility)|OWL RL Profile incompatible|[Jump](#minorfail-outcome-number-148)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-149">149/161</div>|:exclamation:MinorFail|`all-fragments`|[profile-compatibility](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#profile-compatibility)|OWL QL Profile incompatible|[Jump](#minorfail-outcome-number-149)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-150">150/161</div>|:exclamation:MinorFail|`all-fragments`|[profile-compatibility](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#profile-compatibility)|OWL QL Profile incompatible|[Jump](#minorfail-outcome-number-150)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-151">151/161</div>|:exclamation:MinorFail|`all-fragments`|[profile-compatibility](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#profile-compatibility)|OWL QL Profile incompatible|[Jump](#minorfail-outcome-number-151)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-152">152/161</div>|:exclamation:MinorFail|`all-fragments`|[profile-compatibility](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#profile-compatibility)|OWL QL Profile incompatible|[Jump](#minorfail-outcome-number-152)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-153">153/161</div>|:exclamation:MinorFail|`all-fragments`|[profile-compatibility](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#profile-compatibility)|OWL QL Profile incompatible|[Jump](#minorfail-outcome-number-153)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-154">154/161</div>|:exclamation:MinorFail|`all-fragments`|[profile-compatibility](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#profile-compatibility)|OWL QL Profile incompatible|[Jump](#minorfail-outcome-number-154)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-155">155/161</div>|:exclamation:MinorFail|`all-fragments`|[profile-compatibility](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#profile-compatibility)|OWL EL Profile incompatible|[Jump](#minorfail-outcome-number-155)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-156">156/161</div>|:exclamation:MinorFail|`all-fragments`|[profile-compatibility](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#profile-compatibility)|OWL EL Profile incompatible|[Jump](#minorfail-outcome-number-156)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-157">157/161</div>|:exclamation:MinorFail|`all-fragments`|[profile-compatibility](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#profile-compatibility)|OWL EL Profile incompatible|[Jump](#minorfail-outcome-number-157)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-158">158/161</div>|:exclamation:MinorFail|`all-fragments`|[profile-compatibility](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#profile-compatibility)|OWL EL Profile incompatible|[Jump](#minorfail-outcome-number-158)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-159">159/161</div>|:exclamation:MinorFail|`all-fragments`|[profile-compatibility](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#profile-compatibility)|OWL EL Profile incompatible|[Jump](#minorfail-outcome-number-159)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-160">160/161</div>|:exclamation:MinorFail|`all-fragments`|[term-referencing](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#term-referencing)|Term not referenced to a module|[Jump](#minorfail-outcome-number-160)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-161">161/161</div>|:exclamation:MinorFail|`all-fragments`|[terms-differenciation](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#terms-differenciation)|Too close terms|[Jump](#minorfail-outcome-number-161)|

***

## MinorFail Outcomes Details

This subchapter gives more details to the :exclamation:MinorFail outcomes

### MinorFail Outcome number 1

[Jump to summary definition](#summary-MinorFail-1)	|	Previous MinorFail outcome	|	[Next MinorFail outcome](#minorfail-outcome-number-2)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-src-vocabularies-quantity-kinds|
|----|----|
|Title|Standalone module src/vocabularies/quantity&lowbar;kinds.ttl from branch main|
|Composition|- [Module vocabularies/quantity&lowbar;kinds](https://github.com/Accord-Project/aec3po/blob/main/src/vocabularies/quantity_kinds.ttl)|

#### Criterion detail
|Identifier|[labeled-terms](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#labeled-terms)|
|----|----|
|Title|Term labeling test|
|Description|A test case from the Best Practices tests checking if all the terms of the subject have a rdfs:label property pointing to a literal in English|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-1)|Identifier|`not-labeled-term`|
|[Section top](#minorfail-outcome-number-1)|Title|Terms not labeled|
|[Section top](#minorfail-outcome-number-1)|Description|The following terms have no rdfs:label to define it in natural language|
|[Section top](#minorfail-outcome-number-1)|Pointer|<pre lang="Turtle"><code>:QuantityKind a owl:Class ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy &#60;http://qudt.org/2.1/schema/qudt> .</code></pre>|
|[Section top](#minorfail-outcome-number-1)|Pointer|<pre lang="Turtle"><code>:ModularRoomHeight a owl:NamedIndividual,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;skos:Concept,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;:QuantityKind ;  &#10;&#32;&#32;&#32;&#32;qudt:applicableUnit &#60;http://qudt.org/vocab/unit/CentiM>,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#60;http://qudt.org/vocab/unit/IN>,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#60;http://qudt.org/vocab/unit/M>,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#60;http://qudt.org/vocab/unit/MilliIN>,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#60;http://qudt.org/vocab/unit/MilliM> ;  &#10;&#32;&#32;&#32;&#32;qudt:hasDimensionVector &#60;http://qudt.org/vocab/dimensionvector/A0E0L1I0M0H0T0D0> ;  &#10;&#32;&#32;&#32;&#32;qudt:normativeReference &#34;https://www.iso.org/obp/ui/#iso:std:iso:6707:-1:ed-6:v1:en:t...&#34; ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy :quantity&lowbar;kinds ;  &#10;&#32;&#32;&#32;&#32;skos:broader &#60;http://qudt.org/vocab/quantitykind/Length> ;  &#10;&#32;&#32;&#32;&#32;skos:definition &#34;vertical distance within one storey between the modular plan...&#34; ;  &#10;&#32;&#32;&#32;&#32;skos:prefLabel &#34;modular room height&#34;@en .</code></pre>|
|[Section top](#minorfail-outcome-number-1)|Pointer|<pre lang="Turtle"><code>:WidthOfAngledCorridor a owl:NamedIndividual,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;skos:Concept,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;:QuantityKind ;  &#10;&#32;&#32;&#32;&#32;qudt:applicableUnit &#60;http://qudt.org/vocab/unit/CentiM>,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#60;http://qudt.org/vocab/unit/IN>,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#60;http://qudt.org/vocab/unit/M>,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#60;http://qudt.org/vocab/unit/MilliIN>,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#60;http://qudt.org/vocab/unit/MilliM> ;  &#10;&#32;&#32;&#32;&#32;qudt:hasDimensionVector &#60;http://qudt.org/vocab/dimensionvector/A0E0L1I0M0H0T0D0> ;  &#10;&#32;&#32;&#32;&#32;qudt:normativeReference &#34;https://www.iso.org/obp/ui/#iso:std:iso:7176:-5:ed-2:v1:en:t...&#34; ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy :quantity&lowbar;kinds ;  &#10;&#32;&#32;&#32;&#32;skos:broader &#60;http://qudt.org/vocab/quantitykind/Length> ;  &#10;&#32;&#32;&#32;&#32;skos:definition &#34;width of a corridor with a right angled turn in which the wh...&#34; ;  &#10;&#32;&#32;&#32;&#32;skos:prefLabel &#34;width of angled corridor&#34;@en .</code></pre>|
|[Section top](#minorfail-outcome-number-1)|Pointer|<pre lang="Turtle"><code>:CompressiveForce a owl:NamedIndividual,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;skos:Concept,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;:QuantityKind ;  &#10;&#32;&#32;&#32;&#32;qudt:hasDimensionVector &#60;http://qudt.org/vocab/dimensionvector/A0E0L1I0M1H0T-2D0> ;  &#10;&#32;&#32;&#32;&#32;qudt:symbol &#34;C&#34; ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy :quantity&lowbar;kinds ;  &#10;&#32;&#32;&#32;&#32;skos:broader &#60;http://qudt.org/vocab/quantitykind/Force> ;  &#10;&#32;&#32;&#32;&#32;skos:definition &#34;Force tending to reduce the size of a body.&#34; ;  &#10;&#32;&#32;&#32;&#32;skos:prefLabel &#34;compressive force&#34;@en .</code></pre>|
|[Section top](#minorfail-outcome-number-1)|Pointer|<pre lang="Turtle"><code>:PartialSafetyFactor a owl:NamedIndividual,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;skos:Concept,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;:QuantityKind ;  &#10;&#32;&#32;&#32;&#32;qudt:applicableUnit &#60;http://qudt.org/vocab/unit/UNITLESS> ;  &#10;&#32;&#32;&#32;&#32;qudt:hasDimensionVector &#60;http://qudt.org/vocab/dimensionvector/A0E0L0I0M0H0T0D0> ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy :quantity&lowbar;kinds ;  &#10;&#32;&#32;&#32;&#32;skos:definition &#34;Also written γM, the partial safety factor for resistance.&#34;@en ;  &#10;&#32;&#32;&#32;&#32;skos:prefLabel &#34;Partial Safety Factor&#34;@en .</code></pre>|
|[Section top](#minorfail-outcome-number-1)|Pointer|<pre lang="Turtle"><code>:PartialSafetyFactor0 a owl:NamedIndividual,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;skos:Concept,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;:QuantityKind ;  &#10;&#32;&#32;&#32;&#32;qudt:applicableUnit &#60;http://qudt.org/vocab/unit/UNITLESS> ;  &#10;&#32;&#32;&#32;&#32;qudt:hasDimensionVector &#60;http://qudt.org/vocab/dimensionvector/A0E0L0I0M0H0T0D0> ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy :quantity&lowbar;kinds ;  &#10;&#32;&#32;&#32;&#32;skos:broader :PartialSafetyFactor ;  &#10;&#32;&#32;&#32;&#32;skos:definition &#34;Also written γM0, the partial safety factor for resistance r...&#34; ;  &#10;&#32;&#32;&#32;&#32;skos:prefLabel &#34;Partial Safety Factor&#34;@en .</code></pre>|
|[Section top](#minorfail-outcome-number-1)|Pointer|<pre lang="Turtle"><code>:AxialCompressionStress a owl:NamedIndividual,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;skos:Concept,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;:QuantityKind ;  &#10;&#32;&#32;&#32;&#32;qudt:hasDimensionVector &#60;http://qudt.org/vocab/dimensionvector/A0E0L1I0M-1H0T-2D0> ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy :quantity&lowbar;kinds ;  &#10;&#32;&#32;&#32;&#32;skos:definition &#34;also known as fc0k&#34; ;  &#10;&#32;&#32;&#32;&#32;skos:prefLabel &#34;axial compression stress&#34;@en .</code></pre>|
|[Section top](#minorfail-outcome-number-1)|Pointer|<pre lang="Turtle"><code>:ModificationFactorKmod a owl:NamedIndividual,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;skos:Concept,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;:QuantityKind ;  &#10;&#32;&#32;&#32;&#32;qudt:applicableUnit &#60;http://qudt.org/vocab/unit/UNITLESS> ;  &#10;&#32;&#32;&#32;&#32;qudt:hasDimensionVector &#60;http://qudt.org/vocab/dimensionvector/A0E0L0I0M0H0T0D0> ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy :quantity&lowbar;kinds ;  &#10;&#32;&#32;&#32;&#32;skos:definition &#34;Modification Factor to take into account the duration of loa...&#34; ;  &#10;&#32;&#32;&#32;&#32;skos:prefLabel &#34;Modification Factor Kmod&#34;@en .</code></pre>|

***
### MinorFail Outcome number 2

[Jump to summary definition](#summary-MinorFail-2)	|	[Previous MinorFail outcome](#minorfail-outcome-number-1)	|	[Next MinorFail outcome](#minorfail-outcome-number-3)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-src-vocabularies-quantity-kinds|
|----|----|
|Title|Standalone module src/vocabularies/quantity&lowbar;kinds.ttl from branch main|
|Composition|- [Module vocabularies/quantity&lowbar;kinds](https://github.com/Accord-Project/aec3po/blob/main/src/vocabularies/quantity_kinds.ttl)|

#### Criterion detail
|Identifier|[profile-compatibility](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#profile-compatibility)|
|----|----|
|Title|Profile compatibility test|
|Description|A test meant to check whether the test subject is compatible with a profile or not, and if it is not, why.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-2)|Identifier|`owl-ql-profile-error`|
|[Section top](#minorfail-outcome-number-2)|Title|OWL QL Profile incompatible|
|[Section top](#minorfail-outcome-number-2)|Description|Statement not supported in a Sub Class Expression|
|[Section top](#minorfail-outcome-number-2)|Pointer|<pre lang="Turtle"><code>&#91;] owl:intersectionOf ( skos:Concept &#91; a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:hasValue aec3po:QuantityKindNomenclature ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:onProperty skos:inScheme ] ) .</code></pre>|

***
### MinorFail Outcome number 3

[Jump to summary definition](#summary-MinorFail-3)	|	[Previous MinorFail outcome](#minorfail-outcome-number-2)	|	[Next MinorFail outcome](#minorfail-outcome-number-4)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-src-vocabularies-quantity-kinds|
|----|----|
|Title|Standalone module src/vocabularies/quantity&lowbar;kinds.ttl from branch main|
|Composition|- [Module vocabularies/quantity&lowbar;kinds](https://github.com/Accord-Project/aec3po/blob/main/src/vocabularies/quantity_kinds.ttl)|

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
|[Section top](#minorfail-outcome-number-3)|Pointer|<pre lang="Turtle"><code>&#91;] a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;owl:hasValue aec3po:QuantityKindNomenclature ;  &#10;&#32;&#32;&#32;&#32;owl:onProperty skos:inScheme .</code></pre>|

***
### MinorFail Outcome number 4

[Jump to summary definition](#summary-MinorFail-4)	|	[Previous MinorFail outcome](#minorfail-outcome-number-3)	|	[Next MinorFail outcome](#minorfail-outcome-number-5)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-src-vocabularies-quantity-kinds|
|----|----|
|Title|Standalone module src/vocabularies/quantity&lowbar;kinds.ttl from branch main|
|Composition|- [Module vocabularies/quantity&lowbar;kinds](https://github.com/Accord-Project/aec3po/blob/main/src/vocabularies/quantity_kinds.ttl)|

#### Criterion detail
|Identifier|[profile-compatibility](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#profile-compatibility)|
|----|----|
|Title|Profile compatibility test|
|Description|A test meant to check whether the test subject is compatible with a profile or not, and if it is not, why.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-4)|Identifier|`owl-ql-profile-error`|
|[Section top](#minorfail-outcome-number-4)|Title|OWL QL Profile incompatible|
|[Section top](#minorfail-outcome-number-4)|Description|Class Expression not supported with owl:equivalentClass|
|[Section top](#minorfail-outcome-number-4)|Pointer|<pre lang="Turtle"><code>aec3po:QuantityKind a owl:Class ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;Quantity Kind&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:comment &#34;A Quantity Kind is any observable property that can be quant...&#34; ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy aec3po:quantity&lowbar;kinds ;  &#10;&#32;&#32;&#32;&#32;rdfs:subClassOf qudt:QuantityKind,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#60;http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#Region>,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;skos:Concept ;  &#10;&#32;&#32;&#32;&#32;owl:equivalentClass &#91; owl:intersectionOf ( skos:Concept &#91; a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:hasValue aec3po:QuantityKindNomenclature ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:onProperty skos:inScheme ] ) ] ;  &#10;&#32;&#32;&#32;&#32;skos:example &#34;Length, Area, U-Value.&#34;@en ;  &#10;&#32;&#32;&#32;&#32;skos:note &#34;Maxime Lefrançois argues that both qudt:QuantityKind and qud...&#34; .</code></pre>|

***
### MinorFail Outcome number 5

[Jump to summary definition](#summary-MinorFail-5)	|	[Previous MinorFail outcome](#minorfail-outcome-number-4)	|	[Next MinorFail outcome](#minorfail-outcome-number-6)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-src-vocabularies-quantity-kinds|
|----|----|
|Title|Standalone module src/vocabularies/quantity&lowbar;kinds.ttl from branch main|
|Composition|- [Module vocabularies/quantity&lowbar;kinds](https://github.com/Accord-Project/aec3po/blob/main/src/vocabularies/quantity_kinds.ttl)|

#### Criterion detail
|Identifier|[terms-differenciation](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#terms-differenciation)|
|----|----|
|Title|Terms differenciation test|
|Description|A test case from the Best Practices tests checking if all the terms are different enough from each other according to the Levenshtein distance metric.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-5)|Identifier|`too-close-terms`|
|[Section top](#minorfail-outcome-number-5)|Title|Too close terms|
|[Section top](#minorfail-outcome-number-5)|Description|Some terms are too similar|
|[Section top](#minorfail-outcome-number-5)|Pointer|<pre lang="Turtle"><code>:PartialSafetyFactor0 a owl:NamedIndividual,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;skos:Concept,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;:QuantityKind ;  &#10;&#32;&#32;&#32;&#32;qudt:applicableUnit &#60;http://qudt.org/vocab/unit/UNITLESS> ;  &#10;&#32;&#32;&#32;&#32;qudt:hasDimensionVector &#60;http://qudt.org/vocab/dimensionvector/A0E0L0I0M0H0T0D0> ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy :quantity&lowbar;kinds ;  &#10;&#32;&#32;&#32;&#32;skos:broader :PartialSafetyFactor ;  &#10;&#32;&#32;&#32;&#32;skos:definition &#34;Also written γM0, the partial safety factor for resistance r...&#34; ;  &#10;&#32;&#32;&#32;&#32;skos:prefLabel &#34;Partial Safety Factor&#34;@en .</code></pre>|
|[Section top](#minorfail-outcome-number-5)|Pointer|<pre lang="Turtle"><code>:PartialSafetyFactor a owl:NamedIndividual,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;skos:Concept,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;:QuantityKind ;  &#10;&#32;&#32;&#32;&#32;qudt:applicableUnit &#60;http://qudt.org/vocab/unit/UNITLESS> ;  &#10;&#32;&#32;&#32;&#32;qudt:hasDimensionVector &#60;http://qudt.org/vocab/dimensionvector/A0E0L0I0M0H0T0D0> ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy :quantity&lowbar;kinds ;  &#10;&#32;&#32;&#32;&#32;skos:definition &#34;Also written γM, the partial safety factor for resistance.&#34;@en ;  &#10;&#32;&#32;&#32;&#32;skos:prefLabel &#34;Partial Safety Factor&#34;@en .</code></pre>|
|[Section top](#minorfail-outcome-number-5)|Pointer|<pre lang="Turtle"><code>:PartialSafetyFactor1 a owl:NamedIndividual,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;skos:Concept,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;:QuantityKind ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;Partial Safety Factor&#34;@en ;  &#10;&#32;&#32;&#32;&#32;qudt:applicableUnit &#60;http://qudt.org/vocab/unit/UNITLESS> ;  &#10;&#32;&#32;&#32;&#32;qudt:hasDimensionVector &#60;http://qudt.org/vocab/dimensionvector/A0E0L0I0M0H0T0D0> ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy :quantity&lowbar;kinds ;  &#10;&#32;&#32;&#32;&#32;skos:broader :PartialSafetyFactor ;  &#10;&#32;&#32;&#32;&#32;skos:definition &#34;Also written γM1, the partial safety factor for resistance r...&#34; .</code></pre>|
|[Section top](#minorfail-outcome-number-5)|Pointer|<pre lang="Turtle"><code>:QuantityKind a owl:Class ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;Quantity Kind&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:comment &#34;A Quantity Kind is any observable property that can be quant...&#34; ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy :quantity&lowbar;kinds ;  &#10;&#32;&#32;&#32;&#32;rdfs:subClassOf qudt:QuantityKind,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#60;http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#Region>,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;skos:Concept ;  &#10;&#32;&#32;&#32;&#32;owl:equivalentClass &#91; owl:intersectionOf ( skos:Concept &#91; a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:hasValue :QuantityKindNomenclature ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:onProperty skos:inScheme ] ) ] ;  &#10;&#32;&#32;&#32;&#32;skos:example &#34;Length, Area, U-Value.&#34;@en ;  &#10;&#32;&#32;&#32;&#32;skos:note &#34;Maxime Lefrançois argues that both qudt:QuantityKind and qud...&#34; .</code></pre>|

***
### MinorFail Outcome number 6

[Jump to summary definition](#summary-MinorFail-6)	|	[Previous MinorFail outcome](#minorfail-outcome-number-5)	|	[Next MinorFail outcome](#minorfail-outcome-number-7)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-src-vocabularies-permitting-stages|
|----|----|
|Title|Standalone module src/vocabularies/permitting&lowbar;stages.ttl from branch main|
|Composition|- [Module vocabularies/permitting&lowbar;stages](https://github.com/Accord-Project/aec3po/blob/main/src/vocabularies/permitting_stages.ttl)|

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
|[Section top](#minorfail-outcome-number-6)|Pointer|<pre lang="Turtle"><code>:hasPermittingStage a owl:ObjectProperty ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;has permitting stage&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:comment &#34;Links an entity to the permitting stage this entity pertains&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy :permitting&lowbar;stage ;  &#10;&#32;&#32;&#32;&#32;rdfs:range &lowbar;:n67a48578241c4c65aa56ea5b6d0cb266b1,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&lowbar;:n67a48578241c4c65aa56ea5b6d0cb266b2,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:Thing,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;skos:Concept,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;:PermittingStage ;  &#10;&#32;&#32;&#32;&#32;rdfs:subPropertyOf &#60;https://w3id.org/digitalconstruction/0.5/Lifecycle#hasStage>,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;:hasPermittingStage ;  &#10;&#32;&#32;&#32;&#32;owl:equivalentProperty &#60;https://w3id.org/digitalconstruction/0.5/Lifecycle#hasStage>,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;:hasPermittingStage .  &#10;&lowbar;:n67a48578241c4c65aa56ea5b6d0cb266b3 rdf:first skos:Concept ;  &#10;&#32;&#32;&#32;&#32;rdf:rest ( &lowbar;:n67a48578241c4c65aa56ea5b6d0cb266b1 ) .  &#10;&lowbar;:n67a48578241c4c65aa56ea5b6d0cb266b2 rdfs:subClassOf &lowbar;:n67a48578241c4c65aa56ea5b6d0cb266b1,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&lowbar;:n67a48578241c4c65aa56ea5b6d0cb266b2,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:Thing,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;skos:Concept,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;:PermittingStage ;  &#10;&#32;&#32;&#32;&#32;owl:equivalentClass :PermittingStage ;  &#10;&#32;&#32;&#32;&#32;owl:intersectionOf &lowbar;:n67a48578241c4c65aa56ea5b6d0cb266b3 .  &#10;&lowbar;:n67a48578241c4c65aa56ea5b6d0cb266b1 a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;owl:hasValue :PermittingStageNomenclature ;  &#10;&#32;&#32;&#32;&#32;owl:onProperty skos:inScheme .</code></pre>|
|[Section top](#minorfail-outcome-number-6)|Pointer|http://www.w3.org/2004/02/skos/core#Concept|

***
### MinorFail Outcome number 7

[Jump to summary definition](#summary-MinorFail-7)	|	[Previous MinorFail outcome](#minorfail-outcome-number-6)	|	[Next MinorFail outcome](#minorfail-outcome-number-8)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-src-vocabularies-permitting-stages|
|----|----|
|Title|Standalone module src/vocabularies/permitting&lowbar;stages.ttl from branch main|
|Composition|- [Module vocabularies/permitting&lowbar;stages](https://github.com/Accord-Project/aec3po/blob/main/src/vocabularies/permitting_stages.ttl)|

#### Criterion detail
|Identifier|[labeled-terms](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#labeled-terms)|
|----|----|
|Title|Term labeling test|
|Description|A test case from the Best Practices tests checking if all the terms of the subject have a rdfs:label property pointing to a literal in English|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-7)|Identifier|`not-labeled-term`|
|[Section top](#minorfail-outcome-number-7)|Title|Terms not labeled|
|[Section top](#minorfail-outcome-number-7)|Description|The following terms have no rdfs:label to define it in natural language|
|[Section top](#minorfail-outcome-number-7)|Pointer|<pre lang="Turtle"><code>:UK&lowbar;Building&lowbar;Control&lowbar;Submission a owl:NamedIndividual,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;skos:Concept,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;:PermittingStage ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy :permitting&lowbar;stage ;  &#10;&#32;&#32;&#32;&#32;skos:definition &#34;The UK Building Control Submission permitting stage.&#34;@en ;  &#10;&#32;&#32;&#32;&#32;skos:inScheme :PermittingStageNomenclature ;  &#10;&#32;&#32;&#32;&#32;skos:prefLabel &#34;building control submission&#34;@en ;  &#10;&#32;&#32;&#32;&#32;skos:topConceptOf :PermittingStageNomenclature ;  &#10;&#32;&#32;&#32;&#32;:forAdministrativeArea :England .</code></pre>|
|[Section top](#minorfail-outcome-number-7)|Pointer|<pre lang="Turtle"><code>:UK&lowbar;Planning&lowbar;Permission a owl:NamedIndividual,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;skos:Concept,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;:PermittingStage ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy :permitting&lowbar;stage ;  &#10;&#32;&#32;&#32;&#32;skos:definition &#34;The UK Planning Permission permitting stage.&#34;@en ;  &#10;&#32;&#32;&#32;&#32;skos:inScheme :PermittingStageNomenclature ;  &#10;&#32;&#32;&#32;&#32;skos:prefLabel &#34;planning permission&#34;@en ;  &#10;&#32;&#32;&#32;&#32;skos:topConceptOf :PermittingStageNomenclature ;  &#10;&#32;&#32;&#32;&#32;:forAdministrativeArea :England .</code></pre>|

***
### MinorFail Outcome number 8

[Jump to summary definition](#summary-MinorFail-8)	|	[Previous MinorFail outcome](#minorfail-outcome-number-7)	|	[Next MinorFail outcome](#minorfail-outcome-number-9)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-src-vocabularies-permitting-stages|
|----|----|
|Title|Standalone module src/vocabularies/permitting&lowbar;stages.ttl from branch main|
|Composition|- [Module vocabularies/permitting&lowbar;stages](https://github.com/Accord-Project/aec3po/blob/main/src/vocabularies/permitting_stages.ttl)|

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
|[Section top](#minorfail-outcome-number-8)|Description|Statement not supported in a Sub Class Expression|
|[Section top](#minorfail-outcome-number-8)|Pointer|<pre lang="Turtle"><code>&#91;] owl:intersectionOf ( skos:Concept &#91; a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:hasValue aec3po:PermittingStageNomenclature ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:onProperty skos:inScheme ] ) .</code></pre>|

***
### MinorFail Outcome number 9

[Jump to summary definition](#summary-MinorFail-9)	|	[Previous MinorFail outcome](#minorfail-outcome-number-8)	|	[Next MinorFail outcome](#minorfail-outcome-number-10)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-src-vocabularies-permitting-stages|
|----|----|
|Title|Standalone module src/vocabularies/permitting&lowbar;stages.ttl from branch main|
|Composition|- [Module vocabularies/permitting&lowbar;stages](https://github.com/Accord-Project/aec3po/blob/main/src/vocabularies/permitting_stages.ttl)|

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
|[Section top](#minorfail-outcome-number-9)|Description|Statement not supported|
|[Section top](#minorfail-outcome-number-9)|Pointer|<pre lang="Turtle"><code>&#91;] a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;owl:hasValue aec3po:PermittingStageNomenclature ;  &#10;&#32;&#32;&#32;&#32;owl:onProperty skos:inScheme .</code></pre>|

***
### MinorFail Outcome number 10

[Jump to summary definition](#summary-MinorFail-10)	|	[Previous MinorFail outcome](#minorfail-outcome-number-9)	|	[Next MinorFail outcome](#minorfail-outcome-number-11)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-src-vocabularies-permitting-stages|
|----|----|
|Title|Standalone module src/vocabularies/permitting&lowbar;stages.ttl from branch main|
|Composition|- [Module vocabularies/permitting&lowbar;stages](https://github.com/Accord-Project/aec3po/blob/main/src/vocabularies/permitting_stages.ttl)|

#### Criterion detail
|Identifier|[profile-compatibility](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#profile-compatibility)|
|----|----|
|Title|Profile compatibility test|
|Description|A test meant to check whether the test subject is compatible with a profile or not, and if it is not, why.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-10)|Identifier|`owl-ql-profile-error`|
|[Section top](#minorfail-outcome-number-10)|Title|OWL QL Profile incompatible|
|[Section top](#minorfail-outcome-number-10)|Description|Class Expression not supported with owl:equivalentClass|
|[Section top](#minorfail-outcome-number-10)|Pointer|<pre lang="Turtle"><code>aec3po:PermittingStage a owl:Class ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;Permitting Stage&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:comment &#34;The class of permitting stages.&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy aec3po:permitting&lowbar;stage ;  &#10;&#32;&#32;&#32;&#32;rdfs:subClassOf skos:Concept ;  &#10;&#32;&#32;&#32;&#32;owl:equivalentClass &#91; owl:intersectionOf ( skos:Concept &#91; a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:hasValue aec3po:PermittingStageNomenclature ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:onProperty skos:inScheme ] ) ] .</code></pre>|

***
### MinorFail Outcome number 11

[Jump to summary definition](#summary-MinorFail-11)	|	[Previous MinorFail outcome](#minorfail-outcome-number-10)	|	[Next MinorFail outcome](#minorfail-outcome-number-12)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-src-vocabularies-disciplines|
|----|----|
|Title|Standalone module src/vocabularies/disciplines.ttl from branch main|
|Composition|- [Module vocabularies/disciplines](https://github.com/Accord-Project/aec3po/blob/main/src/vocabularies/disciplines.ttl)|

#### Criterion detail
|Identifier|[domain-and-range-referencing](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#domain-and-range-referencing)|
|----|----|
|Title|Domain and range referencing test|
|Description|A test case from the Best Practices tests checking if all the ranges and domains from the test subject point to terms that are defined in the vocabulary.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-11)|Identifier|`range-out-of-vocabulary`|
|[Section top](#minorfail-outcome-number-11)|Title|Range out of vocabulary|
|[Section top](#minorfail-outcome-number-11)|Description|Some properties have a range out of the ontology|
|[Section top](#minorfail-outcome-number-11)|Pointer|<pre lang="Turtle"><code>:hasDiscipline a owl:ObjectProperty ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;has discipline&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:comment &#34;Links an entity (procedure, statement, verifier, ...) to the...&#34; ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy :discipline ;  &#10;&#32;&#32;&#32;&#32;rdfs:range &lowbar;:n5bba27d18b7d478a986f700957424495b1,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&lowbar;:n5bba27d18b7d478a986f700957424495b2,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:Thing,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;skos:Concept,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;:Discipline ;  &#10;&#32;&#32;&#32;&#32;rdfs:subPropertyOf :hasDiscipline ;  &#10;&#32;&#32;&#32;&#32;owl:equivalentProperty :hasDiscipline .  &#10;&lowbar;:n5bba27d18b7d478a986f700957424495b3 rdf:first skos:Concept ;  &#10;&#32;&#32;&#32;&#32;rdf:rest ( &lowbar;:n5bba27d18b7d478a986f700957424495b1 ) .  &#10;&lowbar;:n5bba27d18b7d478a986f700957424495b2 rdfs:subClassOf &lowbar;:n5bba27d18b7d478a986f700957424495b1,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&lowbar;:n5bba27d18b7d478a986f700957424495b2,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:Thing,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;skos:Concept,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;:Discipline ;  &#10;&#32;&#32;&#32;&#32;owl:equivalentClass :Discipline ;  &#10;&#32;&#32;&#32;&#32;owl:intersectionOf &lowbar;:n5bba27d18b7d478a986f700957424495b3 .  &#10;&lowbar;:n5bba27d18b7d478a986f700957424495b1 a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;owl:hasValue :DisciplineNomenclature ;  &#10;&#32;&#32;&#32;&#32;owl:onProperty skos:inScheme .</code></pre>|
|[Section top](#minorfail-outcome-number-11)|Pointer|http://www.w3.org/2004/02/skos/core#Concept|

***
### MinorFail Outcome number 12

[Jump to summary definition](#summary-MinorFail-12)	|	[Previous MinorFail outcome](#minorfail-outcome-number-11)	|	[Next MinorFail outcome](#minorfail-outcome-number-13)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-src-vocabularies-disciplines|
|----|----|
|Title|Standalone module src/vocabularies/disciplines.ttl from branch main|
|Composition|- [Module vocabularies/disciplines](https://github.com/Accord-Project/aec3po/blob/main/src/vocabularies/disciplines.ttl)|

#### Criterion detail
|Identifier|[labeled-terms](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#labeled-terms)|
|----|----|
|Title|Term labeling test|
|Description|A test case from the Best Practices tests checking if all the terms of the subject have a rdfs:label property pointing to a literal in English|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-12)|Identifier|`not-labeled-term`|
|[Section top](#minorfail-outcome-number-12)|Title|Terms not labeled|
|[Section top](#minorfail-outcome-number-12)|Description|The following terms have no rdfs:label to define it in natural language|
|[Section top](#minorfail-outcome-number-12)|Pointer|<pre lang="Turtle"><code>:Discipline-architecture a owl:NamedIndividual,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;skos:Concept,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;:Discipline ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy :discipline ;  &#10;&#32;&#32;&#32;&#32;skos:definition &#34;The Architecture discipline.&#34;@en ;  &#10;&#32;&#32;&#32;&#32;skos:inScheme :DisciplineNomenclature ;  &#10;&#32;&#32;&#32;&#32;skos:prefLabel &#34;architecture&#34;@en ;  &#10;&#32;&#32;&#32;&#32;skos:topConceptOf :DisciplineNomenclature .</code></pre>|
|[Section top](#minorfail-outcome-number-12)|Pointer|<pre lang="Turtle"><code>:Discipline-buildingServices a owl:NamedIndividual,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;skos:Concept,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;:Discipline ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy :discipline ;  &#10;&#32;&#32;&#32;&#32;skos:definition &#34;The Building Services discipline.&#34;@en ;  &#10;&#32;&#32;&#32;&#32;skos:inScheme :DisciplineNomenclature ;  &#10;&#32;&#32;&#32;&#32;skos:prefLabel &#34;building services&#34;@en ;  &#10;&#32;&#32;&#32;&#32;skos:topConceptOf :DisciplineNomenclature .</code></pre>|
|[Section top](#minorfail-outcome-number-12)|Pointer|<pre lang="Turtle"><code>:Discipline-construction a owl:NamedIndividual,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;skos:Concept,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;:Discipline ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy :discipline ;  &#10;&#32;&#32;&#32;&#32;skos:definition &#34;The Construction discipline.&#34;@en ;  &#10;&#32;&#32;&#32;&#32;skos:inScheme :DisciplineNomenclature ;  &#10;&#32;&#32;&#32;&#32;skos:prefLabel &#34;construction&#34;@en ;  &#10;&#32;&#32;&#32;&#32;skos:topConceptOf :DisciplineNomenclature .</code></pre>|
|[Section top](#minorfail-outcome-number-12)|Pointer|<pre lang="Turtle"><code>:Discipline-planning a owl:NamedIndividual,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;skos:Concept,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;:Discipline ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy :discipline ;  &#10;&#32;&#32;&#32;&#32;skos:definition &#34;The Planning discipline.&#34;@en ;  &#10;&#32;&#32;&#32;&#32;skos:inScheme :DisciplineNomenclature ;  &#10;&#32;&#32;&#32;&#32;skos:prefLabel &#34;planning&#34;@en ;  &#10;&#32;&#32;&#32;&#32;skos:topConceptOf :DisciplineNomenclature .</code></pre>|
|[Section top](#minorfail-outcome-number-12)|Pointer|<pre lang="Turtle"><code>:Discipline-structuralEngineering a owl:NamedIndividual,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;skos:Concept,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;:Discipline ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy :discipline ;  &#10;&#32;&#32;&#32;&#32;skos:definition &#34;The Structural Engineering discipline.&#34;@en ;  &#10;&#32;&#32;&#32;&#32;skos:inScheme :DisciplineNomenclature ;  &#10;&#32;&#32;&#32;&#32;skos:prefLabel &#34;structural engineering&#34;@en ;  &#10;&#32;&#32;&#32;&#32;skos:topConceptOf :DisciplineNomenclature .</code></pre>|

***
### MinorFail Outcome number 13

[Jump to summary definition](#summary-MinorFail-13)	|	[Previous MinorFail outcome](#minorfail-outcome-number-12)	|	[Next MinorFail outcome](#minorfail-outcome-number-14)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-src-vocabularies-disciplines|
|----|----|
|Title|Standalone module src/vocabularies/disciplines.ttl from branch main|
|Composition|- [Module vocabularies/disciplines](https://github.com/Accord-Project/aec3po/blob/main/src/vocabularies/disciplines.ttl)|

#### Criterion detail
|Identifier|[profile-compatibility](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#profile-compatibility)|
|----|----|
|Title|Profile compatibility test|
|Description|A test meant to check whether the test subject is compatible with a profile or not, and if it is not, why.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-13)|Identifier|`owl-ql-profile-error`|
|[Section top](#minorfail-outcome-number-13)|Title|OWL QL Profile incompatible|
|[Section top](#minorfail-outcome-number-13)|Description|Statement not supported in a Sub Class Expression|
|[Section top](#minorfail-outcome-number-13)|Pointer|<pre lang="Turtle"><code>&#91;] owl:intersectionOf ( skos:Concept &#91; a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:hasValue aec3po:DisciplineNomenclature ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:onProperty skos:inScheme ] ) .</code></pre>|

***
### MinorFail Outcome number 14

[Jump to summary definition](#summary-MinorFail-14)	|	[Previous MinorFail outcome](#minorfail-outcome-number-13)	|	[Next MinorFail outcome](#minorfail-outcome-number-15)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-src-vocabularies-disciplines|
|----|----|
|Title|Standalone module src/vocabularies/disciplines.ttl from branch main|
|Composition|- [Module vocabularies/disciplines](https://github.com/Accord-Project/aec3po/blob/main/src/vocabularies/disciplines.ttl)|

#### Criterion detail
|Identifier|[profile-compatibility](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#profile-compatibility)|
|----|----|
|Title|Profile compatibility test|
|Description|A test meant to check whether the test subject is compatible with a profile or not, and if it is not, why.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-14)|Identifier|`owl-ql-profile-error`|
|[Section top](#minorfail-outcome-number-14)|Title|OWL QL Profile incompatible|
|[Section top](#minorfail-outcome-number-14)|Description|Statement not supported|
|[Section top](#minorfail-outcome-number-14)|Pointer|<pre lang="Turtle"><code>&#91;] a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;owl:hasValue aec3po:DisciplineNomenclature ;  &#10;&#32;&#32;&#32;&#32;owl:onProperty skos:inScheme .</code></pre>|

***
### MinorFail Outcome number 15

[Jump to summary definition](#summary-MinorFail-15)	|	[Previous MinorFail outcome](#minorfail-outcome-number-14)	|	[Next MinorFail outcome](#minorfail-outcome-number-16)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-src-vocabularies-disciplines|
|----|----|
|Title|Standalone module src/vocabularies/disciplines.ttl from branch main|
|Composition|- [Module vocabularies/disciplines](https://github.com/Accord-Project/aec3po/blob/main/src/vocabularies/disciplines.ttl)|

#### Criterion detail
|Identifier|[profile-compatibility](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#profile-compatibility)|
|----|----|
|Title|Profile compatibility test|
|Description|A test meant to check whether the test subject is compatible with a profile or not, and if it is not, why.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-15)|Identifier|`owl-ql-profile-error`|
|[Section top](#minorfail-outcome-number-15)|Title|OWL QL Profile incompatible|
|[Section top](#minorfail-outcome-number-15)|Description|Class Expression not supported with owl:equivalentClass|
|[Section top](#minorfail-outcome-number-15)|Pointer|<pre lang="Turtle"><code>aec3po:Discipline a owl:Class ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;Discipline&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:comment &#34;The AEC discipline to which something pertains.&#34; ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy aec3po:discipline ;  &#10;&#32;&#32;&#32;&#32;rdfs:subClassOf skos:Concept ;  &#10;&#32;&#32;&#32;&#32;owl:equivalentClass &#91; owl:intersectionOf ( skos:Concept &#91; a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:hasValue aec3po:DisciplineNomenclature ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:onProperty skos:inScheme ] ) ] .</code></pre>|

***
### MinorFail Outcome number 16

[Jump to summary definition](#summary-MinorFail-16)	|	[Previous MinorFail outcome](#minorfail-outcome-number-15)	|	[Next MinorFail outcome](#minorfail-outcome-number-17)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-src-vocabularies-check-method-operators|
|----|----|
|Title|Standalone module src/vocabularies/check&lowbar;method&lowbar;operators.ttl from branch main|
|Composition|- [Module vocabularies/check&lowbar;method&lowbar;operators](https://github.com/Accord-Project/aec3po/blob/main/src/vocabularies/check_method_operators.ttl)|

#### Criterion detail
|Identifier|[labeled-terms](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#labeled-terms)|
|----|----|
|Title|Term labeling test|
|Description|A test case from the Best Practices tests checking if all the terms of the subject have a rdfs:label property pointing to a literal in English|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-16)|Identifier|`not-labeled-term`|
|[Section top](#minorfail-outcome-number-16)|Title|Terms not labeled|
|[Section top](#minorfail-outcome-number-16)|Description|The following terms have no rdfs:label to define it in natural language|
|[Section top](#minorfail-outcome-number-16)|Pointer|<pre lang="Turtle"><code>:CheckMethodOperator-exists a owl:NamedIndividual,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;skos:Concept,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;:CheckMethodOperator ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy :check&lowbar;method&lowbar;operators ;  &#10;&#32;&#32;&#32;&#32;skos:definition &#34;exists operator.&#34;@en ;  &#10;&#32;&#32;&#32;&#32;skos:inScheme :CheckMethodOperatorNomenclature ;  &#10;&#32;&#32;&#32;&#32;skos:prefLabel &#34;exists&#34;@en ;  &#10;&#32;&#32;&#32;&#32;skos:topConceptOf :CheckMethodOperatorNomenclature .</code></pre>|
|[Section top](#minorfail-outcome-number-16)|Pointer|<pre lang="Turtle"><code>:CheckMethodOperator-notExists a owl:NamedIndividual,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;skos:Concept,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;:CheckMethodOperator ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy :check&lowbar;method&lowbar;operators ;  &#10;&#32;&#32;&#32;&#32;skos:definition &#34;not exists operator.&#34;@en ;  &#10;&#32;&#32;&#32;&#32;skos:inScheme :CheckMethodOperatorNomenclature ;  &#10;&#32;&#32;&#32;&#32;skos:prefLabel &#34;not exists&#34;@en ;  &#10;&#32;&#32;&#32;&#32;skos:topConceptOf :CheckMethodOperatorNomenclature .</code></pre>|
|[Section top](#minorfail-outcome-number-16)|Pointer|<pre lang="Turtle"><code>:CheckMethodOperator-forall a owl:NamedIndividual,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;skos:Concept,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;:CheckMethodOperator ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy :check&lowbar;method&lowbar;operators ;  &#10;&#32;&#32;&#32;&#32;skos:definition &#34;forall operator.&#34;@en ;  &#10;&#32;&#32;&#32;&#32;skos:inScheme :CheckMethodOperatorNomenclature ;  &#10;&#32;&#32;&#32;&#32;skos:prefLabel &#34;forall&#34;@en ;  &#10;&#32;&#32;&#32;&#32;skos:topConceptOf :CheckMethodOperatorNomenclature .</code></pre>|
|[Section top](#minorfail-outcome-number-16)|Pointer|<pre lang="Turtle"><code>:CheckMethodOperator-addition a owl:NamedIndividual,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;skos:Concept,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;:CheckMethodOperator ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy :check&lowbar;method&lowbar;operators ;  &#10;&#32;&#32;&#32;&#32;skos:definition &#34;addition operator.&#34;@en ;  &#10;&#32;&#32;&#32;&#32;skos:inScheme :CheckMethodOperatorNomenclature ;  &#10;&#32;&#32;&#32;&#32;skos:prefLabel &#34;addition&#34;@en ;  &#10;&#32;&#32;&#32;&#32;skos:topConceptOf :CheckMethodOperatorNomenclature .</code></pre>|
|[Section top](#minorfail-outcome-number-16)|Pointer|<pre lang="Turtle"><code>:CheckMethodOperator-multiplication a owl:NamedIndividual,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;skos:Concept,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;:CheckMethodOperator ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy :check&lowbar;method&lowbar;operators ;  &#10;&#32;&#32;&#32;&#32;skos:definition &#34;multiplication Operator.&#34;@en ;  &#10;&#32;&#32;&#32;&#32;skos:inScheme :CheckMethodOperatorNomenclature ;  &#10;&#32;&#32;&#32;&#32;skos:prefLabel &#34;multiplication&#34;@en ;  &#10;&#32;&#32;&#32;&#32;skos:topConceptOf :CheckMethodOperatorNomenclature .</code></pre>|
|[Section top](#minorfail-outcome-number-16)|Pointer|<pre lang="Turtle"><code>:CheckMethodOperator-subtraction a owl:NamedIndividual,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;skos:Concept,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;:CheckMethodOperator ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy :check&lowbar;method&lowbar;operators ;  &#10;&#32;&#32;&#32;&#32;skos:definition &#34;subtraction operator.&#34;@en ;  &#10;&#32;&#32;&#32;&#32;skos:inScheme :CheckMethodOperatorNomenclature ;  &#10;&#32;&#32;&#32;&#32;skos:prefLabel &#34;subtraction&#34;@en ;  &#10;&#32;&#32;&#32;&#32;skos:topConceptOf :CheckMethodOperatorNomenclature .</code></pre>|
|[Section top](#minorfail-outcome-number-16)|Pointer|<pre lang="Turtle"><code>:CheckMethodOperator-division a owl:NamedIndividual,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;skos:Concept,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;:CheckMethodOperator ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy :check&lowbar;method&lowbar;operators ;  &#10;&#32;&#32;&#32;&#32;skos:definition &#34;division Operator.&#34;@en ;  &#10;&#32;&#32;&#32;&#32;skos:inScheme :CheckMethodOperatorNomenclature ;  &#10;&#32;&#32;&#32;&#32;skos:prefLabel &#34;division&#34;@en ;  &#10;&#32;&#32;&#32;&#32;skos:topConceptOf :CheckMethodOperatorNomenclature .</code></pre>|

***
### MinorFail Outcome number 17

[Jump to summary definition](#summary-MinorFail-17)	|	[Previous MinorFail outcome](#minorfail-outcome-number-16)	|	[Next MinorFail outcome](#minorfail-outcome-number-18)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-src-vocabularies-check-method-operators|
|----|----|
|Title|Standalone module src/vocabularies/check&lowbar;method&lowbar;operators.ttl from branch main|
|Composition|- [Module vocabularies/check&lowbar;method&lowbar;operators](https://github.com/Accord-Project/aec3po/blob/main/src/vocabularies/check_method_operators.ttl)|

#### Criterion detail
|Identifier|[profile-compatibility](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#profile-compatibility)|
|----|----|
|Title|Profile compatibility test|
|Description|A test meant to check whether the test subject is compatible with a profile or not, and if it is not, why.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-17)|Identifier|`owl-ql-profile-error`|
|[Section top](#minorfail-outcome-number-17)|Title|OWL QL Profile incompatible|
|[Section top](#minorfail-outcome-number-17)|Description|Statement not supported in a Sub Class Expression|
|[Section top](#minorfail-outcome-number-17)|Pointer|<pre lang="Turtle"><code>&#91;] owl:intersectionOf ( skos:Concept &#91; a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:hasValue aec3po:CheckMethodOperatorNomenclature ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:onProperty skos:inScheme ] ) .</code></pre>|

***
### MinorFail Outcome number 18

[Jump to summary definition](#summary-MinorFail-18)	|	[Previous MinorFail outcome](#minorfail-outcome-number-17)	|	[Next MinorFail outcome](#minorfail-outcome-number-19)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-src-vocabularies-check-method-operators|
|----|----|
|Title|Standalone module src/vocabularies/check&lowbar;method&lowbar;operators.ttl from branch main|
|Composition|- [Module vocabularies/check&lowbar;method&lowbar;operators](https://github.com/Accord-Project/aec3po/blob/main/src/vocabularies/check_method_operators.ttl)|

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
|[Section top](#minorfail-outcome-number-18)|Description|Statement not supported|
|[Section top](#minorfail-outcome-number-18)|Pointer|<pre lang="Turtle"><code>&#91;] a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;owl:hasValue aec3po:CheckMethodOperatorNomenclature ;  &#10;&#32;&#32;&#32;&#32;owl:onProperty skos:inScheme .</code></pre>|

***
### MinorFail Outcome number 19

[Jump to summary definition](#summary-MinorFail-19)	|	[Previous MinorFail outcome](#minorfail-outcome-number-18)	|	[Next MinorFail outcome](#minorfail-outcome-number-20)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-src-vocabularies-check-method-operators|
|----|----|
|Title|Standalone module src/vocabularies/check&lowbar;method&lowbar;operators.ttl from branch main|
|Composition|- [Module vocabularies/check&lowbar;method&lowbar;operators](https://github.com/Accord-Project/aec3po/blob/main/src/vocabularies/check_method_operators.ttl)|

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
|[Section top](#minorfail-outcome-number-19)|Description|Class Expression not supported with owl:equivalentClass|
|[Section top](#minorfail-outcome-number-19)|Pointer|<pre lang="Turtle"><code>aec3po:CheckMethodOperator a owl:Class ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;check method operator&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:comment &#34;Formally defined as the set of skos:Concept in concept schem...&#34; ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy aec3po:check&lowbar;method&lowbar;operators ;  &#10;&#32;&#32;&#32;&#32;rdfs:subClassOf skos:Concept,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;aec3po:CheckMethod ;  &#10;&#32;&#32;&#32;&#32;owl:equivalentClass &#91; owl:intersectionOf ( skos:Concept &#91; a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:hasValue aec3po:CheckMethodOperatorNomenclature ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:onProperty skos:inScheme ] ) ] .</code></pre>|

***
### MinorFail Outcome number 20

[Jump to summary definition](#summary-MinorFail-20)	|	[Previous MinorFail outcome](#minorfail-outcome-number-19)	|	[Next MinorFail outcome](#minorfail-outcome-number-21)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-src-vocabularies-check-method-operators|
|----|----|
|Title|Standalone module src/vocabularies/check&lowbar;method&lowbar;operators.ttl from branch main|
|Composition|- [Module vocabularies/check&lowbar;method&lowbar;operators](https://github.com/Accord-Project/aec3po/blob/main/src/vocabularies/check_method_operators.ttl)|

#### Criterion detail
|Identifier|[profile-compatibility](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#profile-compatibility)|
|----|----|
|Title|Profile compatibility test|
|Description|A test meant to check whether the test subject is compatible with a profile or not, and if it is not, why.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-20)|Identifier|`owl-el-profile-error`|
|[Section top](#minorfail-outcome-number-20)|Title|OWL EL Profile incompatible|
|[Section top](#minorfail-outcome-number-20)|Description|Statement not supported|
|[Section top](#minorfail-outcome-number-20)|Pointer|<pre lang="Turtle"><code>aec3po:hasOperator a owl:FunctionalProperty,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:ObjectProperty ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;has operator&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:comment &#34;The operator of a feature of interest or a property of that ...&#34; ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy aec3po:check&lowbar;method&lowbar;Operators ;  &#10;&#32;&#32;&#32;&#32;rdfs:range aec3po:CheckMethod ;  &#10;&#32;&#32;&#32;&#32;rdfs:subPropertyOf aec3po:hasDesign .</code></pre>|

***
### MinorFail Outcome number 21

[Jump to summary definition](#summary-MinorFail-21)	|	[Previous MinorFail outcome](#minorfail-outcome-number-20)	|	[Next MinorFail outcome](#minorfail-outcome-number-22)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-src-vocabularies-check-method-comparators|
|----|----|
|Title|Standalone module src/vocabularies/check&lowbar;method&lowbar;comparators.ttl from branch main|
|Composition|- [Module vocabularies/check&lowbar;method&lowbar;comparators](https://github.com/Accord-Project/aec3po/blob/main/src/vocabularies/check_method_comparators.ttl)|

#### Criterion detail
|Identifier|[labeled-terms](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#labeled-terms)|
|----|----|
|Title|Term labeling test|
|Description|A test case from the Best Practices tests checking if all the terms of the subject have a rdfs:label property pointing to a literal in English|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-21)|Identifier|`not-labeled-term`|
|[Section top](#minorfail-outcome-number-21)|Title|Terms not labeled|
|[Section top](#minorfail-outcome-number-21)|Description|The following terms have no rdfs:label to define it in natural language|
|[Section top](#minorfail-outcome-number-21)|Pointer|<pre lang="Turtle"><code>:CheckMethodcomparator-logicalAND a owl:NamedIndividual,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;skos:Concept,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;:CheckMethodComparator ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy :check&lowbar;method&lowbar;comparators ;  &#10;&#32;&#32;&#32;&#32;skos:definition &#34;logical AND comparator.&#34;@en ;  &#10;&#32;&#32;&#32;&#32;skos:inScheme :CheckMethodComparatorNomenclature ;  &#10;&#32;&#32;&#32;&#32;skos:prefLabel &#34;logicalAND&#34;@en ;  &#10;&#32;&#32;&#32;&#32;skos:topConceptOf :CheckMethodComparatorNomenclature .</code></pre>|
|[Section top](#minorfail-outcome-number-21)|Pointer|<pre lang="Turtle"><code>:CheckMethodcomparator-eq a owl:NamedIndividual,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;skos:Concept,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;:CheckMethodcomparator ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy :check&lowbar;method&lowbar;comparators ;  &#10;&#32;&#32;&#32;&#32;skos:definition &#34;equal-to comparator.&#34;@en ;  &#10;&#32;&#32;&#32;&#32;skos:inScheme :CheckMethodComparatorNomenclature ;  &#10;&#32;&#32;&#32;&#32;skos:prefLabel &#34;equal-to&#34;@en ;  &#10;&#32;&#32;&#32;&#32;skos:topConceptOf :CheckMethodComparatorNomenclature .</code></pre>|
|[Section top](#minorfail-outcome-number-21)|Pointer|<pre lang="Turtle"><code>:CheckMethodComparator-neq a owl:NamedIndividual,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;skos:Concept,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;:CheckMethodComparator ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy :check&lowbar;method&lowbar;comparators ;  &#10;&#32;&#32;&#32;&#32;skos:definition &#34;not equal-to comparator.&#34;@en ;  &#10;&#32;&#32;&#32;&#32;skos:inScheme :CheckMethodComparatorNomenclature ;  &#10;&#32;&#32;&#32;&#32;skos:prefLabel &#34;not equal-to&#34;@en ;  &#10;&#32;&#32;&#32;&#32;skos:topConceptOf :CheckMethodComparatorNomenclature .</code></pre>|
|[Section top](#minorfail-outcome-number-21)|Pointer|<pre lang="Turtle"><code>:CheckMethodComparator-lt a owl:NamedIndividual,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;skos:Concept,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;:CheckMethodComparator ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy :check&lowbar;method&lowbar;comparators ;  &#10;&#32;&#32;&#32;&#32;skos:definition &#34;less-than comparator.&#34;@en ;  &#10;&#32;&#32;&#32;&#32;skos:inScheme :CheckMethodComparatorNomenclature ;  &#10;&#32;&#32;&#32;&#32;skos:prefLabel &#34;less than&#34;@en ;  &#10;&#32;&#32;&#32;&#32;skos:topConceptOf :CheckMethodComparatorNomenclature .</code></pre>|
|[Section top](#minorfail-outcome-number-21)|Pointer|<pre lang="Turtle"><code>:CheckMethodComparator-le a owl:NamedIndividual,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;skos:Concept,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;:CheckMethodComparator ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy :check&lowbar;method&lowbar;comparators ;  &#10;&#32;&#32;&#32;&#32;skos:definition &#34;less-equal comparator.&#34;@en ;  &#10;&#32;&#32;&#32;&#32;skos:inScheme :CheckMethodComparatorNomenclature ;  &#10;&#32;&#32;&#32;&#32;skos:prefLabel &#34;less equal&#34;@en ;  &#10;&#32;&#32;&#32;&#32;skos:topConceptOf :CheckMethodComparatorNomenclature .</code></pre>|
|[Section top](#minorfail-outcome-number-21)|Pointer|<pre lang="Turtle"><code>:CheckMethodComparator-gt a owl:NamedIndividual,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;skos:Concept,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;:CheckMethodComparator ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy :check&lowbar;method&lowbar;comparators ;  &#10;&#32;&#32;&#32;&#32;skos:definition &#34;greater-than comparator.&#34;@en ;  &#10;&#32;&#32;&#32;&#32;skos:inScheme :CheckMethodComparatorNomenclature ;  &#10;&#32;&#32;&#32;&#32;skos:prefLabel &#34;greater than&#34;@en ;  &#10;&#32;&#32;&#32;&#32;skos:topConceptOf :CheckMethodComparatorNomenclature .</code></pre>|
|[Section top](#minorfail-outcome-number-21)|Pointer|<pre lang="Turtle"><code>:CheckMethodComparator-ge a owl:NamedIndividual,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;skos:Concept,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;:CheckMethodComparator ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy :check&lowbar;method&lowbar;comparators ;  &#10;&#32;&#32;&#32;&#32;skos:definition &#34;greater-equal comparator.&#34;@en ;  &#10;&#32;&#32;&#32;&#32;skos:inScheme :CheckMethodComparatorNomenclature ;  &#10;&#32;&#32;&#32;&#32;skos:prefLabel &#34;greater equal&#34;@en ;  &#10;&#32;&#32;&#32;&#32;skos:topConceptOf :CheckMethodComparatorNomenclature .</code></pre>|
|[Section top](#minorfail-outcome-number-21)|Pointer|<pre lang="Turtle"><code>:CheckMethodComparator-logicalOR a owl:NamedIndividual,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;skos:Concept,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;:CheckMethodComparator ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy :check&lowbar;method&lowbar;comparators ;  &#10;&#32;&#32;&#32;&#32;skos:definition &#34;logical OR comparator.&#34;@en ;  &#10;&#32;&#32;&#32;&#32;skos:inScheme :CheckMethodComparatorNomenclature ;  &#10;&#32;&#32;&#32;&#32;skos:prefLabel &#34;logicalOR&#34;@en ;  &#10;&#32;&#32;&#32;&#32;skos:topConceptOf :CheckMethodComparatorNomenclature .</code></pre>|

***
### MinorFail Outcome number 22

[Jump to summary definition](#summary-MinorFail-22)	|	[Previous MinorFail outcome](#minorfail-outcome-number-21)	|	[Next MinorFail outcome](#minorfail-outcome-number-23)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-src-vocabularies-check-method-comparators|
|----|----|
|Title|Standalone module src/vocabularies/check&lowbar;method&lowbar;comparators.ttl from branch main|
|Composition|- [Module vocabularies/check&lowbar;method&lowbar;comparators](https://github.com/Accord-Project/aec3po/blob/main/src/vocabularies/check_method_comparators.ttl)|

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
|[Section top](#minorfail-outcome-number-22)|Description|Statement not supported in a Sub Class Expression|
|[Section top](#minorfail-outcome-number-22)|Pointer|<pre lang="Turtle"><code>&#91;] owl:intersectionOf ( skos:Concept &#91; a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:hasValue aec3po:CheckMethodComparatorNomenclature ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:onProperty skos:inScheme ] ) .</code></pre>|

***
### MinorFail Outcome number 23

[Jump to summary definition](#summary-MinorFail-23)	|	[Previous MinorFail outcome](#minorfail-outcome-number-22)	|	[Next MinorFail outcome](#minorfail-outcome-number-24)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-src-vocabularies-check-method-comparators|
|----|----|
|Title|Standalone module src/vocabularies/check&lowbar;method&lowbar;comparators.ttl from branch main|
|Composition|- [Module vocabularies/check&lowbar;method&lowbar;comparators](https://github.com/Accord-Project/aec3po/blob/main/src/vocabularies/check_method_comparators.ttl)|

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
|[Section top](#minorfail-outcome-number-23)|Pointer|<pre lang="Turtle"><code>&#91;] a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;owl:hasValue aec3po:CheckMethodComparatorNomenclature ;  &#10;&#32;&#32;&#32;&#32;owl:onProperty skos:inScheme .</code></pre>|

***
### MinorFail Outcome number 24

[Jump to summary definition](#summary-MinorFail-24)	|	[Previous MinorFail outcome](#minorfail-outcome-number-23)	|	[Next MinorFail outcome](#minorfail-outcome-number-25)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-src-vocabularies-check-method-comparators|
|----|----|
|Title|Standalone module src/vocabularies/check&lowbar;method&lowbar;comparators.ttl from branch main|
|Composition|- [Module vocabularies/check&lowbar;method&lowbar;comparators](https://github.com/Accord-Project/aec3po/blob/main/src/vocabularies/check_method_comparators.ttl)|

#### Criterion detail
|Identifier|[profile-compatibility](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#profile-compatibility)|
|----|----|
|Title|Profile compatibility test|
|Description|A test meant to check whether the test subject is compatible with a profile or not, and if it is not, why.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-24)|Identifier|`owl-ql-profile-error`|
|[Section top](#minorfail-outcome-number-24)|Title|OWL QL Profile incompatible|
|[Section top](#minorfail-outcome-number-24)|Description|Class Expression not supported with owl:equivalentClass|
|[Section top](#minorfail-outcome-number-24)|Pointer|<pre lang="Turtle"><code>aec3po:CheckMethodComparator a owl:Class ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;check method comparator&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:comment &#34;Formally defined as the set of skos:Concept in concept schem...&#34; ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy aec3po:check&lowbar;method&lowbar;comparators ;  &#10;&#32;&#32;&#32;&#32;rdfs:subClassOf skos:Concept,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;aec3po:CheckMethod ;  &#10;&#32;&#32;&#32;&#32;owl:equivalentClass &#91; owl:intersectionOf ( skos:Concept &#91; a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:hasValue aec3po:CheckMethodComparatorNomenclature ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:onProperty skos:inScheme ] ) ] .</code></pre>|

***
### MinorFail Outcome number 25

[Jump to summary definition](#summary-MinorFail-25)	|	[Previous MinorFail outcome](#minorfail-outcome-number-24)	|	[Next MinorFail outcome](#minorfail-outcome-number-26)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-src-vocabularies-check-method-comparators|
|----|----|
|Title|Standalone module src/vocabularies/check&lowbar;method&lowbar;comparators.ttl from branch main|
|Composition|- [Module vocabularies/check&lowbar;method&lowbar;comparators](https://github.com/Accord-Project/aec3po/blob/main/src/vocabularies/check_method_comparators.ttl)|

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
|[Section top](#minorfail-outcome-number-25)|Pointer|<pre lang="Turtle"><code>aec3po:hasComparator a owl:FunctionalProperty,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:ObjectProperty ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;has comparator&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:comment &#34;The comparator of a feature of interest or a property of tha...&#34; ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy aec3po:check&lowbar;method&lowbar;comparators ;  &#10;&#32;&#32;&#32;&#32;rdfs:range aec3po:CheckMethod ;  &#10;&#32;&#32;&#32;&#32;rdfs:subPropertyOf aec3po:hasDesign .</code></pre>|

***
### MinorFail Outcome number 26

[Jump to summary definition](#summary-MinorFail-26)	|	[Previous MinorFail outcome](#minorfail-outcome-number-25)	|	[Next MinorFail outcome](#minorfail-outcome-number-27)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-src-vocabularies-check-method-comparators|
|----|----|
|Title|Standalone module src/vocabularies/check&lowbar;method&lowbar;comparators.ttl from branch main|
|Composition|- [Module vocabularies/check&lowbar;method&lowbar;comparators](https://github.com/Accord-Project/aec3po/blob/main/src/vocabularies/check_method_comparators.ttl)|

#### Criterion detail
|Identifier|[terms-differenciation](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#terms-differenciation)|
|----|----|
|Title|Terms differenciation test|
|Description|A test case from the Best Practices tests checking if all the terms are different enough from each other according to the Levenshtein distance metric.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-26)|Identifier|`too-close-terms`|
|[Section top](#minorfail-outcome-number-26)|Title|Too close terms|
|[Section top](#minorfail-outcome-number-26)|Description|Some terms are too similar|
|[Section top](#minorfail-outcome-number-26)|Pointer|<pre lang="Turtle"><code>:CheckMethodComparator-gt a owl:NamedIndividual,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;skos:Concept,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;:CheckMethodComparator ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy :check&lowbar;method&lowbar;comparators ;  &#10;&#32;&#32;&#32;&#32;skos:definition &#34;greater-than comparator.&#34;@en ;  &#10;&#32;&#32;&#32;&#32;skos:inScheme :CheckMethodComparatorNomenclature ;  &#10;&#32;&#32;&#32;&#32;skos:prefLabel &#34;greater than&#34;@en ;  &#10;&#32;&#32;&#32;&#32;skos:topConceptOf :CheckMethodComparatorNomenclature .</code></pre>|
|[Section top](#minorfail-outcome-number-26)|Pointer|<pre lang="Turtle"><code>:CheckMethodComparator-ge a owl:NamedIndividual,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;skos:Concept,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;:CheckMethodComparator ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy :check&lowbar;method&lowbar;comparators ;  &#10;&#32;&#32;&#32;&#32;skos:definition &#34;greater-equal comparator.&#34;@en ;  &#10;&#32;&#32;&#32;&#32;skos:inScheme :CheckMethodComparatorNomenclature ;  &#10;&#32;&#32;&#32;&#32;skos:prefLabel &#34;greater equal&#34;@en ;  &#10;&#32;&#32;&#32;&#32;skos:topConceptOf :CheckMethodComparatorNomenclature .</code></pre>|
|[Section top](#minorfail-outcome-number-26)|Pointer|<pre lang="Turtle"><code>:CheckMethodComparator-le a owl:NamedIndividual,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;skos:Concept,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;:CheckMethodComparator ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy :check&lowbar;method&lowbar;comparators ;  &#10;&#32;&#32;&#32;&#32;skos:definition &#34;less-equal comparator.&#34;@en ;  &#10;&#32;&#32;&#32;&#32;skos:inScheme :CheckMethodComparatorNomenclature ;  &#10;&#32;&#32;&#32;&#32;skos:prefLabel &#34;less equal&#34;@en ;  &#10;&#32;&#32;&#32;&#32;skos:topConceptOf :CheckMethodComparatorNomenclature .</code></pre>|
|[Section top](#minorfail-outcome-number-26)|Pointer|<pre lang="Turtle"><code>:CheckMethodComparator-lt a owl:NamedIndividual,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;skos:Concept,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;:CheckMethodComparator ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy :check&lowbar;method&lowbar;comparators ;  &#10;&#32;&#32;&#32;&#32;skos:definition &#34;less-than comparator.&#34;@en ;  &#10;&#32;&#32;&#32;&#32;skos:inScheme :CheckMethodComparatorNomenclature ;  &#10;&#32;&#32;&#32;&#32;skos:prefLabel &#34;less than&#34;@en ;  &#10;&#32;&#32;&#32;&#32;skos:topConceptOf :CheckMethodComparatorNomenclature .</code></pre>|
|[Section top](#minorfail-outcome-number-26)|Pointer|<pre lang="Turtle"><code>:CheckMethodComparator-neq a owl:NamedIndividual,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;skos:Concept,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;:CheckMethodComparator ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy :check&lowbar;method&lowbar;comparators ;  &#10;&#32;&#32;&#32;&#32;skos:definition &#34;not equal-to comparator.&#34;@en ;  &#10;&#32;&#32;&#32;&#32;skos:inScheme :CheckMethodComparatorNomenclature ;  &#10;&#32;&#32;&#32;&#32;skos:prefLabel &#34;not equal-to&#34;@en ;  &#10;&#32;&#32;&#32;&#32;skos:topConceptOf :CheckMethodComparatorNomenclature .</code></pre>|
|[Section top](#minorfail-outcome-number-26)|Pointer|<pre lang="Turtle"><code>:CheckMethodcomparator-eq a owl:NamedIndividual,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;skos:Concept,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;:CheckMethodcomparator ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy :check&lowbar;method&lowbar;comparators ;  &#10;&#32;&#32;&#32;&#32;skos:definition &#34;equal-to comparator.&#34;@en ;  &#10;&#32;&#32;&#32;&#32;skos:inScheme :CheckMethodComparatorNomenclature ;  &#10;&#32;&#32;&#32;&#32;skos:prefLabel &#34;equal-to&#34;@en ;  &#10;&#32;&#32;&#32;&#32;skos:topConceptOf :CheckMethodComparatorNomenclature .</code></pre>|

***
### MinorFail Outcome number 27

[Jump to summary definition](#summary-MinorFail-27)	|	[Previous MinorFail outcome](#minorfail-outcome-number-26)	|	[Next MinorFail outcome](#minorfail-outcome-number-28)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-src-vocabularies-building-usage|
|----|----|
|Title|Standalone module src/vocabularies/building&lowbar;usage.ttl from branch main|
|Composition|- [Module vocabularies/building&lowbar;usage](https://github.com/Accord-Project/aec3po/blob/main/src/vocabularies/building_usage.ttl)|

#### Criterion detail
|Identifier|[domain-and-range-referencing](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#domain-and-range-referencing)|
|----|----|
|Title|Domain and range referencing test|
|Description|A test case from the Best Practices tests checking if all the ranges and domains from the test subject point to terms that are defined in the vocabulary.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-27)|Identifier|`range-out-of-vocabulary`|
|[Section top](#minorfail-outcome-number-27)|Title|Range out of vocabulary|
|[Section top](#minorfail-outcome-number-27)|Description|Some properties have a range out of the ontology|
|[Section top](#minorfail-outcome-number-27)|Pointer|<pre lang="Turtle"><code>:forBuildingUsage a owl:ObjectProperty ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;for building usage&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:comment &#34;The building usage for which a specific check, verifier, or ...&#34; ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy :building&lowbar;usage ;  &#10;&#32;&#32;&#32;&#32;rdfs:range &lowbar;:ne2501429a7ee4f478be56c63cc57d5deb1,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&lowbar;:ne2501429a7ee4f478be56c63cc57d5deb2,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:Thing,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;skos:Concept,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;:BuildingUsage,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;:Design ;  &#10;&#32;&#32;&#32;&#32;rdfs:subPropertyOf :forBuildingUsage,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;:forDesign ;  &#10;&#32;&#32;&#32;&#32;owl:equivalentProperty :forBuildingUsage .  &#10;&lowbar;:ne2501429a7ee4f478be56c63cc57d5deb3 rdf:first &lowbar;:ne2501429a7ee4f478be56c63cc57d5deb1 ;  &#10;&#32;&#32;&#32;&#32;rdf:rest () .  &#10;&lowbar;:ne2501429a7ee4f478be56c63cc57d5deb4 rdf:first skos:Concept ;  &#10;&#32;&#32;&#32;&#32;rdf:rest &lowbar;:ne2501429a7ee4f478be56c63cc57d5deb3 .  &#10;&lowbar;:ne2501429a7ee4f478be56c63cc57d5deb2 rdfs:subClassOf &lowbar;:ne2501429a7ee4f478be56c63cc57d5deb1,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&lowbar;:ne2501429a7ee4f478be56c63cc57d5deb2,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:Thing,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;skos:Concept,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;:BuildingUsage,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;:Design ;  &#10;&#32;&#32;&#32;&#32;owl:equivalentClass :BuildingUsage ;  &#10;&#32;&#32;&#32;&#32;owl:intersectionOf &lowbar;:ne2501429a7ee4f478be56c63cc57d5deb4 .  &#10;&lowbar;:ne2501429a7ee4f478be56c63cc57d5deb1 a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;owl:hasValue :BuildingUsageNomenclature ;  &#10;&#32;&#32;&#32;&#32;owl:onProperty skos:inScheme .</code></pre>|
|[Section top](#minorfail-outcome-number-27)|Pointer|<pre lang="Turtle"><code>:hasBuildingUsage a owl:FunctionalProperty,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:ObjectProperty ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;has building usage&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:comment &#34;The building usage design of a feature of interest or a prop...&#34; ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy :building&lowbar;usage ;  &#10;&#32;&#32;&#32;&#32;rdfs:range &lowbar;:n461d3569440743ee8c2902c172183aa9b1,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&lowbar;:n461d3569440743ee8c2902c172183aa9b2,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:Thing,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;skos:Concept,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;:BuildingUsage,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;:Design ;  &#10;&#32;&#32;&#32;&#32;rdfs:subPropertyOf :hasBuildingUsage,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;:hasDesign ;  &#10;&#32;&#32;&#32;&#32;owl:equivalentProperty :hasBuildingUsage .  &#10;&lowbar;:n461d3569440743ee8c2902c172183aa9b3 rdf:first &lowbar;:n461d3569440743ee8c2902c172183aa9b1 ;  &#10;&#32;&#32;&#32;&#32;rdf:rest () .  &#10;&lowbar;:n461d3569440743ee8c2902c172183aa9b4 rdf:first skos:Concept ;  &#10;&#32;&#32;&#32;&#32;rdf:rest &lowbar;:n461d3569440743ee8c2902c172183aa9b3 .  &#10;&lowbar;:n461d3569440743ee8c2902c172183aa9b2 rdfs:subClassOf &lowbar;:n461d3569440743ee8c2902c172183aa9b1,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&lowbar;:n461d3569440743ee8c2902c172183aa9b2,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:Thing,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;skos:Concept,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;:BuildingUsage,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;:Design ;  &#10;&#32;&#32;&#32;&#32;owl:equivalentClass :BuildingUsage ;  &#10;&#32;&#32;&#32;&#32;owl:intersectionOf &lowbar;:n461d3569440743ee8c2902c172183aa9b4 .  &#10;&lowbar;:n461d3569440743ee8c2902c172183aa9b1 a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;owl:hasValue :BuildingUsageNomenclature ;  &#10;&#32;&#32;&#32;&#32;owl:onProperty skos:inScheme .</code></pre>|
|[Section top](#minorfail-outcome-number-27)|Pointer|http://www.w3.org/2004/02/skos/core#Concept|

***
### MinorFail Outcome number 28

[Jump to summary definition](#summary-MinorFail-28)	|	[Previous MinorFail outcome](#minorfail-outcome-number-27)	|	[Next MinorFail outcome](#minorfail-outcome-number-29)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-src-vocabularies-building-usage|
|----|----|
|Title|Standalone module src/vocabularies/building&lowbar;usage.ttl from branch main|
|Composition|- [Module vocabularies/building&lowbar;usage](https://github.com/Accord-Project/aec3po/blob/main/src/vocabularies/building_usage.ttl)|

#### Criterion detail
|Identifier|[labeled-terms](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#labeled-terms)|
|----|----|
|Title|Term labeling test|
|Description|A test case from the Best Practices tests checking if all the terms of the subject have a rdfs:label property pointing to a literal in English|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-28)|Identifier|`not-labeled-term`|
|[Section top](#minorfail-outcome-number-28)|Title|Terms not labeled|
|[Section top](#minorfail-outcome-number-28)|Description|The following terms have no rdfs:label to define it in natural language|
|[Section top](#minorfail-outcome-number-28)|Pointer|<pre lang="Turtle"><code>:BuildingUsage-commercial a owl:NamedIndividual,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;skos:Concept,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;:BuildingUsage ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy :building&lowbar;usage ;  &#10;&#32;&#32;&#32;&#32;skos:definition &#34;Building has commercial usage.&#34;@en ;  &#10;&#32;&#32;&#32;&#32;skos:inScheme :BuildingUsageNomenclature ;  &#10;&#32;&#32;&#32;&#32;skos:prefLabel &#34;commercial&#34;@en ;  &#10;&#32;&#32;&#32;&#32;skos:topConceptOf :BuildingUsageNomenclature .</code></pre>|
|[Section top](#minorfail-outcome-number-28)|Pointer|<pre lang="Turtle"><code>:BuildingUsage-residential a owl:NamedIndividual,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;skos:Concept,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;:BuildingUsage ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy :building&lowbar;usage ;  &#10;&#32;&#32;&#32;&#32;skos:definition &#34;Building has residential usage.&#34;@en ;  &#10;&#32;&#32;&#32;&#32;skos:inScheme :BuildingUsageNomenclature ;  &#10;&#32;&#32;&#32;&#32;skos:prefLabel &#34;residential&#34;@en ;  &#10;&#32;&#32;&#32;&#32;skos:topConceptOf :BuildingUsageNomenclature .</code></pre>|
|[Section top](#minorfail-outcome-number-28)|Pointer|<pre lang="Turtle"><code>:BuildingUsage-cultural a owl:NamedIndividual,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;skos:Concept,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;:BuildingUsage ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy :building&lowbar;usage ;  &#10;&#32;&#32;&#32;&#32;skos:definition &#34;Building has cultural usage.&#34;@en ;  &#10;&#32;&#32;&#32;&#32;skos:inScheme :BuildingUsageNomenclature ;  &#10;&#32;&#32;&#32;&#32;skos:prefLabel &#34;cultural&#34;@en ;  &#10;&#32;&#32;&#32;&#32;skos:topConceptOf :BuildingUsageNomenclature .</code></pre>|

***
### MinorFail Outcome number 29

[Jump to summary definition](#summary-MinorFail-29)	|	[Previous MinorFail outcome](#minorfail-outcome-number-28)	|	[Next MinorFail outcome](#minorfail-outcome-number-30)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-src-vocabularies-building-usage|
|----|----|
|Title|Standalone module src/vocabularies/building&lowbar;usage.ttl from branch main|
|Composition|- [Module vocabularies/building&lowbar;usage](https://github.com/Accord-Project/aec3po/blob/main/src/vocabularies/building_usage.ttl)|

#### Criterion detail
|Identifier|[profile-compatibility](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#profile-compatibility)|
|----|----|
|Title|Profile compatibility test|
|Description|A test meant to check whether the test subject is compatible with a profile or not, and if it is not, why.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-29)|Identifier|`owl-ql-profile-error`|
|[Section top](#minorfail-outcome-number-29)|Title|OWL QL Profile incompatible|
|[Section top](#minorfail-outcome-number-29)|Description|Statement not supported in a Sub Class Expression|
|[Section top](#minorfail-outcome-number-29)|Pointer|<pre lang="Turtle"><code>&#91;] owl:intersectionOf ( skos:Concept &#91; a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:hasValue aec3po:BuildingUsageNomenclature ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:onProperty skos:inScheme ] ) .</code></pre>|

***
### MinorFail Outcome number 30

[Jump to summary definition](#summary-MinorFail-30)	|	[Previous MinorFail outcome](#minorfail-outcome-number-29)	|	[Next MinorFail outcome](#minorfail-outcome-number-31)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-src-vocabularies-building-usage|
|----|----|
|Title|Standalone module src/vocabularies/building&lowbar;usage.ttl from branch main|
|Composition|- [Module vocabularies/building&lowbar;usage](https://github.com/Accord-Project/aec3po/blob/main/src/vocabularies/building_usage.ttl)|

#### Criterion detail
|Identifier|[profile-compatibility](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#profile-compatibility)|
|----|----|
|Title|Profile compatibility test|
|Description|A test meant to check whether the test subject is compatible with a profile or not, and if it is not, why.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-30)|Identifier|`owl-ql-profile-error`|
|[Section top](#minorfail-outcome-number-30)|Title|OWL QL Profile incompatible|
|[Section top](#minorfail-outcome-number-30)|Description|Statement not supported|
|[Section top](#minorfail-outcome-number-30)|Pointer|<pre lang="Turtle"><code>&#91;] a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;owl:hasValue aec3po:BuildingUsageNomenclature ;  &#10;&#32;&#32;&#32;&#32;owl:onProperty skos:inScheme .</code></pre>|

***
### MinorFail Outcome number 31

[Jump to summary definition](#summary-MinorFail-31)	|	[Previous MinorFail outcome](#minorfail-outcome-number-30)	|	[Next MinorFail outcome](#minorfail-outcome-number-32)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-src-vocabularies-building-usage|
|----|----|
|Title|Standalone module src/vocabularies/building&lowbar;usage.ttl from branch main|
|Composition|- [Module vocabularies/building&lowbar;usage](https://github.com/Accord-Project/aec3po/blob/main/src/vocabularies/building_usage.ttl)|

#### Criterion detail
|Identifier|[profile-compatibility](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#profile-compatibility)|
|----|----|
|Title|Profile compatibility test|
|Description|A test meant to check whether the test subject is compatible with a profile or not, and if it is not, why.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-31)|Identifier|`owl-ql-profile-error`|
|[Section top](#minorfail-outcome-number-31)|Title|OWL QL Profile incompatible|
|[Section top](#minorfail-outcome-number-31)|Description|Class Expression not supported with owl:equivalentClass|
|[Section top](#minorfail-outcome-number-31)|Pointer|<pre lang="Turtle"><code>aec3po:BuildingUsage a owl:Class ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;building usage&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:comment &#34;Formally defined as the set of skos:Concept in concept schem...&#34; ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy aec3po:building&lowbar;usage ;  &#10;&#32;&#32;&#32;&#32;rdfs:subClassOf skos:Concept,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;aec3po:Design ;  &#10;&#32;&#32;&#32;&#32;owl:equivalentClass &#91; owl:intersectionOf ( skos:Concept &#91; a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:hasValue aec3po:BuildingUsageNomenclature ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:onProperty skos:inScheme ] ) ] .</code></pre>|

***
### MinorFail Outcome number 32

[Jump to summary definition](#summary-MinorFail-32)	|	[Previous MinorFail outcome](#minorfail-outcome-number-31)	|	[Next MinorFail outcome](#minorfail-outcome-number-33)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-src-vocabularies-building-usage|
|----|----|
|Title|Standalone module src/vocabularies/building&lowbar;usage.ttl from branch main|
|Composition|- [Module vocabularies/building&lowbar;usage](https://github.com/Accord-Project/aec3po/blob/main/src/vocabularies/building_usage.ttl)|

#### Criterion detail
|Identifier|[profile-compatibility](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#profile-compatibility)|
|----|----|
|Title|Profile compatibility test|
|Description|A test meant to check whether the test subject is compatible with a profile or not, and if it is not, why.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-32)|Identifier|`owl-el-profile-error`|
|[Section top](#minorfail-outcome-number-32)|Title|OWL EL Profile incompatible|
|[Section top](#minorfail-outcome-number-32)|Description|Statement not supported|
|[Section top](#minorfail-outcome-number-32)|Pointer|<pre lang="Turtle"><code>aec3po:hasBuildingUsage a owl:FunctionalProperty,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:ObjectProperty ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;has building usage&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:comment &#34;The building usage design of a feature of interest or a prop...&#34; ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy aec3po:building&lowbar;usage ;  &#10;&#32;&#32;&#32;&#32;rdfs:range aec3po:BuildingUsage ;  &#10;&#32;&#32;&#32;&#32;rdfs:subPropertyOf aec3po:hasDesign .</code></pre>|

***
### MinorFail Outcome number 33

[Jump to summary definition](#summary-MinorFail-33)	|	[Previous MinorFail outcome](#minorfail-outcome-number-32)	|	[Next MinorFail outcome](#minorfail-outcome-number-34)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-src-vocabularies-building-structure|
|----|----|
|Title|Standalone module src/vocabularies/building&lowbar;structure.ttl from branch main|
|Composition|- [Module vocabularies/building&lowbar;structure](https://github.com/Accord-Project/aec3po/blob/main/src/vocabularies/building_structure.ttl)|

#### Criterion detail
|Identifier|[domain-and-range-referencing](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#domain-and-range-referencing)|
|----|----|
|Title|Domain and range referencing test|
|Description|A test case from the Best Practices tests checking if all the ranges and domains from the test subject point to terms that are defined in the vocabulary.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-33)|Identifier|`range-out-of-vocabulary`|
|[Section top](#minorfail-outcome-number-33)|Title|Range out of vocabulary|
|[Section top](#minorfail-outcome-number-33)|Description|Some properties have a range out of the ontology|
|[Section top](#minorfail-outcome-number-33)|Pointer|<pre lang="Turtle"><code>:forBuildingStructure a owl:ObjectProperty ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;for building structure&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:comment &#34;The building structure for which a specific check, verifier,...&#34; ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy :building&lowbar;structure ;  &#10;&#32;&#32;&#32;&#32;rdfs:range &lowbar;:nf868a69ea1b14dfba09ee70240a5e0dfb1,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&lowbar;:nf868a69ea1b14dfba09ee70240a5e0dfb2,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:Thing,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;skos:Concept,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;:BuildingStructure,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;:Design ;  &#10;&#32;&#32;&#32;&#32;rdfs:subPropertyOf :forBuildingStructure,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;:forDesign ;  &#10;&#32;&#32;&#32;&#32;owl:equivalentProperty :forBuildingStructure .  &#10;&lowbar;:nf868a69ea1b14dfba09ee70240a5e0dfb3 rdf:first skos:Concept ;  &#10;&#32;&#32;&#32;&#32;rdf:rest ( &lowbar;:nf868a69ea1b14dfba09ee70240a5e0dfb1 ) .  &#10;&lowbar;:nf868a69ea1b14dfba09ee70240a5e0dfb2 rdfs:subClassOf &lowbar;:nf868a69ea1b14dfba09ee70240a5e0dfb1,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&lowbar;:nf868a69ea1b14dfba09ee70240a5e0dfb2,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:Thing,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;skos:Concept,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;:BuildingStructure,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;:Design ;  &#10;&#32;&#32;&#32;&#32;owl:equivalentClass :BuildingStructure ;  &#10;&#32;&#32;&#32;&#32;owl:intersectionOf &lowbar;:nf868a69ea1b14dfba09ee70240a5e0dfb3 .  &#10;&lowbar;:nf868a69ea1b14dfba09ee70240a5e0dfb1 a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;owl:hasValue :BuildingStructureNomenclature ;  &#10;&#32;&#32;&#32;&#32;owl:onProperty skos:inScheme .</code></pre>|
|[Section top](#minorfail-outcome-number-33)|Pointer|<pre lang="Turtle"><code>:hasBuildingStructure a owl:FunctionalProperty,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:ObjectProperty ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;has building structure&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:comment &#34;The building structure design of a feature of interest or a ...&#34; ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy :building&lowbar;structure ;  &#10;&#32;&#32;&#32;&#32;rdfs:range &lowbar;:ne78fc3515aa244dfbaed67cbb6136092b1,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&lowbar;:ne78fc3515aa244dfbaed67cbb6136092b2,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:Thing,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;skos:Concept,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;:BuildingStructure,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;:Design ;  &#10;&#32;&#32;&#32;&#32;rdfs:subPropertyOf :hasBuildingStructure,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;:hasDesign ;  &#10;&#32;&#32;&#32;&#32;owl:equivalentProperty :hasBuildingStructure .  &#10;&lowbar;:ne78fc3515aa244dfbaed67cbb6136092b3 rdf:first skos:Concept ;  &#10;&#32;&#32;&#32;&#32;rdf:rest ( &lowbar;:ne78fc3515aa244dfbaed67cbb6136092b1 ) .  &#10;&lowbar;:ne78fc3515aa244dfbaed67cbb6136092b2 rdfs:subClassOf &lowbar;:ne78fc3515aa244dfbaed67cbb6136092b1,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&lowbar;:ne78fc3515aa244dfbaed67cbb6136092b2,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:Thing,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;skos:Concept,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;:BuildingStructure,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;:Design ;  &#10;&#32;&#32;&#32;&#32;owl:equivalentClass :BuildingStructure ;  &#10;&#32;&#32;&#32;&#32;owl:intersectionOf &lowbar;:ne78fc3515aa244dfbaed67cbb6136092b3 .  &#10;&lowbar;:ne78fc3515aa244dfbaed67cbb6136092b1 a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;owl:hasValue :BuildingStructureNomenclature ;  &#10;&#32;&#32;&#32;&#32;owl:onProperty skos:inScheme .</code></pre>|
|[Section top](#minorfail-outcome-number-33)|Pointer|http://www.w3.org/2004/02/skos/core#Concept|

***
### MinorFail Outcome number 34

[Jump to summary definition](#summary-MinorFail-34)	|	[Previous MinorFail outcome](#minorfail-outcome-number-33)	|	[Next MinorFail outcome](#minorfail-outcome-number-35)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-src-vocabularies-building-structure|
|----|----|
|Title|Standalone module src/vocabularies/building&lowbar;structure.ttl from branch main|
|Composition|- [Module vocabularies/building&lowbar;structure](https://github.com/Accord-Project/aec3po/blob/main/src/vocabularies/building_structure.ttl)|

#### Criterion detail
|Identifier|[labeled-terms](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#labeled-terms)|
|----|----|
|Title|Term labeling test|
|Description|A test case from the Best Practices tests checking if all the terms of the subject have a rdfs:label property pointing to a literal in English|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-34)|Identifier|`not-labeled-term`|
|[Section top](#minorfail-outcome-number-34)|Title|Terms not labeled|
|[Section top](#minorfail-outcome-number-34)|Description|The following terms have no rdfs:label to define it in natural language|
|[Section top](#minorfail-outcome-number-34)|Pointer|<pre lang="Turtle"><code>:BuildingStructure-steel a owl:NamedIndividual,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;skos:Concept,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;:BuildingStructure ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy :building&lowbar;structure ;  &#10;&#32;&#32;&#32;&#32;skos:definition &#34;Building has steel structure.&#34;@en ;  &#10;&#32;&#32;&#32;&#32;skos:inScheme :BuildingStructureNomenclature ;  &#10;&#32;&#32;&#32;&#32;skos:prefLabel &#34;steel&#34;@en ;  &#10;&#32;&#32;&#32;&#32;skos:topConceptOf :BuildingStructureNomenclature .</code></pre>|
|[Section top](#minorfail-outcome-number-34)|Pointer|<pre lang="Turtle"><code>:BuildingStructure-timber a owl:NamedIndividual,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;skos:Concept,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;:BuildingStructure ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy :building&lowbar;structure ;  &#10;&#32;&#32;&#32;&#32;skos:definition &#34;Building has timber structure.&#34;@en ;  &#10;&#32;&#32;&#32;&#32;skos:inScheme :BuildingStructureNomenclature ;  &#10;&#32;&#32;&#32;&#32;skos:prefLabel &#34;timber&#34;@en ;  &#10;&#32;&#32;&#32;&#32;skos:topConceptOf :BuildingStructureNomenclature .</code></pre>|

***
### MinorFail Outcome number 35

[Jump to summary definition](#summary-MinorFail-35)	|	[Previous MinorFail outcome](#minorfail-outcome-number-34)	|	[Next MinorFail outcome](#minorfail-outcome-number-36)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-src-vocabularies-building-structure|
|----|----|
|Title|Standalone module src/vocabularies/building&lowbar;structure.ttl from branch main|
|Composition|- [Module vocabularies/building&lowbar;structure](https://github.com/Accord-Project/aec3po/blob/main/src/vocabularies/building_structure.ttl)|

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
|[Section top](#minorfail-outcome-number-35)|Description|Statement not supported in a Sub Class Expression|
|[Section top](#minorfail-outcome-number-35)|Pointer|<pre lang="Turtle"><code>&#91;] owl:intersectionOf ( skos:Concept &#91; a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:hasValue aec3po:BuildingStructureNomenclature ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:onProperty skos:inScheme ] ) .</code></pre>|

***
### MinorFail Outcome number 36

[Jump to summary definition](#summary-MinorFail-36)	|	[Previous MinorFail outcome](#minorfail-outcome-number-35)	|	[Next MinorFail outcome](#minorfail-outcome-number-37)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-src-vocabularies-building-structure|
|----|----|
|Title|Standalone module src/vocabularies/building&lowbar;structure.ttl from branch main|
|Composition|- [Module vocabularies/building&lowbar;structure](https://github.com/Accord-Project/aec3po/blob/main/src/vocabularies/building_structure.ttl)|

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
|[Section top](#minorfail-outcome-number-36)|Pointer|<pre lang="Turtle"><code>&#91;] a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;owl:hasValue aec3po:BuildingStructureNomenclature ;  &#10;&#32;&#32;&#32;&#32;owl:onProperty skos:inScheme .</code></pre>|

***
### MinorFail Outcome number 37

[Jump to summary definition](#summary-MinorFail-37)	|	[Previous MinorFail outcome](#minorfail-outcome-number-36)	|	[Next MinorFail outcome](#minorfail-outcome-number-38)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-src-vocabularies-building-structure|
|----|----|
|Title|Standalone module src/vocabularies/building&lowbar;structure.ttl from branch main|
|Composition|- [Module vocabularies/building&lowbar;structure](https://github.com/Accord-Project/aec3po/blob/main/src/vocabularies/building_structure.ttl)|

#### Criterion detail
|Identifier|[profile-compatibility](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#profile-compatibility)|
|----|----|
|Title|Profile compatibility test|
|Description|A test meant to check whether the test subject is compatible with a profile or not, and if it is not, why.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-37)|Identifier|`owl-ql-profile-error`|
|[Section top](#minorfail-outcome-number-37)|Title|OWL QL Profile incompatible|
|[Section top](#minorfail-outcome-number-37)|Description|Class Expression not supported with owl:equivalentClass|
|[Section top](#minorfail-outcome-number-37)|Pointer|<pre lang="Turtle"><code>aec3po:BuildingStructure a owl:Class ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;building structure&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:comment &#34;Formally defined as the set of skos:Concept in concept schem...&#34; ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy aec3po:building&lowbar;structure ;  &#10;&#32;&#32;&#32;&#32;rdfs:subClassOf skos:Concept,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;aec3po:Design ;  &#10;&#32;&#32;&#32;&#32;owl:equivalentClass &#91; owl:intersectionOf ( skos:Concept &#91; a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:hasValue aec3po:BuildingStructureNomenclature ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:onProperty skos:inScheme ] ) ] .</code></pre>|

***
### MinorFail Outcome number 38

[Jump to summary definition](#summary-MinorFail-38)	|	[Previous MinorFail outcome](#minorfail-outcome-number-37)	|	[Next MinorFail outcome](#minorfail-outcome-number-39)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-src-vocabularies-building-structure|
|----|----|
|Title|Standalone module src/vocabularies/building&lowbar;structure.ttl from branch main|
|Composition|- [Module vocabularies/building&lowbar;structure](https://github.com/Accord-Project/aec3po/blob/main/src/vocabularies/building_structure.ttl)|

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
|[Section top](#minorfail-outcome-number-38)|Pointer|<pre lang="Turtle"><code>aec3po:hasBuildingStructure a owl:FunctionalProperty,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:ObjectProperty ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;has building structure&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:comment &#34;The building structure design of a feature of interest or a ...&#34; ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy aec3po:building&lowbar;structure ;  &#10;&#32;&#32;&#32;&#32;rdfs:range aec3po:BuildingStructure ;  &#10;&#32;&#32;&#32;&#32;rdfs:subPropertyOf aec3po:hasDesign .</code></pre>|

***
### MinorFail Outcome number 39

[Jump to summary definition](#summary-MinorFail-39)	|	[Previous MinorFail outcome](#minorfail-outcome-number-38)	|	[Next MinorFail outcome](#minorfail-outcome-number-40)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-src-vocabularies-administrative-areas|
|----|----|
|Title|Standalone module src/vocabularies/administrative&lowbar;areas.ttl from branch main|
|Composition|- [Module vocabularies/administrative&lowbar;areas](https://github.com/Accord-Project/aec3po/blob/main/src/vocabularies/administrative_areas.ttl)|

#### Criterion detail
|Identifier|[domain-and-range-referencing](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#domain-and-range-referencing)|
|----|----|
|Title|Domain and range referencing test|
|Description|A test case from the Best Practices tests checking if all the ranges and domains from the test subject point to terms that are defined in the vocabulary.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-39)|Identifier|`range-out-of-vocabulary`|
|[Section top](#minorfail-outcome-number-39)|Title|Range out of vocabulary|
|[Section top](#minorfail-outcome-number-39)|Description|Some properties have a range out of the ontology|
|[Section top](#minorfail-outcome-number-39)|Pointer|<pre lang="Turtle"><code>:forAdministrativeArea a owl:ObjectProperty ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;for administrative area&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:comment &#34;&#34;&#34;The administrative area for which something applies.&#92;r  &#10;A se...&#34;&#34;&#34; ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy :administrative&lowbar;areas ;  &#10;&#32;&#32;&#32;&#32;rdfs:range &lowbar;:nbac63eb1dd0f401b8888a62b58ec80c8b1,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&lowbar;:nbac63eb1dd0f401b8888a62b58ec80c8b2,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#60;http://data.europa.eu/eli/ontology#AdministrativeArea>,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:Thing,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;skos:Concept,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;:AdministrativeArea ;  &#10;&#32;&#32;&#32;&#32;rdfs:subPropertyOf :forAdministrativeArea ;  &#10;&#32;&#32;&#32;&#32;owl:equivalentProperty :forAdministrativeArea .  &#10;&lowbar;:nbac63eb1dd0f401b8888a62b58ec80c8b3 rdf:first skos:Concept ;  &#10;&#32;&#32;&#32;&#32;rdf:rest ( &lowbar;:nbac63eb1dd0f401b8888a62b58ec80c8b1 ) .  &#10;&lowbar;:nbac63eb1dd0f401b8888a62b58ec80c8b2 rdfs:subClassOf &lowbar;:nbac63eb1dd0f401b8888a62b58ec80c8b1,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&lowbar;:nbac63eb1dd0f401b8888a62b58ec80c8b2,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#60;http://data.europa.eu/eli/ontology#AdministrativeArea>,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:Thing,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;skos:Concept,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;:AdministrativeArea ;  &#10;&#32;&#32;&#32;&#32;owl:equivalentClass &#60;http://data.europa.eu/eli/ontology#AdministrativeArea>,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;:AdministrativeArea ;  &#10;&#32;&#32;&#32;&#32;owl:intersectionOf &lowbar;:nbac63eb1dd0f401b8888a62b58ec80c8b3 .  &#10;&lowbar;:nbac63eb1dd0f401b8888a62b58ec80c8b1 a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;owl:hasValue :AdministrativeAreaNomenclature ;  &#10;&#32;&#32;&#32;&#32;owl:onProperty skos:inScheme .</code></pre>|
|[Section top](#minorfail-outcome-number-39)|Pointer|<pre lang="Turtle"><code>:forAdministrativeArea a owl:ObjectProperty ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;for administrative area&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:comment &#34;&#34;&#34;The administrative area for which something applies.&#92;r  &#10;A se...&#34;&#34;&#34; ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy :administrative&lowbar;areas ;  &#10;&#32;&#32;&#32;&#32;rdfs:range &lowbar;:n345d9b395f224850a9b17d60fdab80e3b1,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&lowbar;:n345d9b395f224850a9b17d60fdab80e3b2,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#60;http://data.europa.eu/eli/ontology#AdministrativeArea>,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:Thing,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;skos:Concept,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;:AdministrativeArea ;  &#10;&#32;&#32;&#32;&#32;rdfs:subPropertyOf :forAdministrativeArea ;  &#10;&#32;&#32;&#32;&#32;owl:equivalentProperty :forAdministrativeArea .  &#10;&lowbar;:n345d9b395f224850a9b17d60fdab80e3b3 rdf:first skos:Concept ;  &#10;&#32;&#32;&#32;&#32;rdf:rest ( &lowbar;:n345d9b395f224850a9b17d60fdab80e3b1 ) .  &#10;&lowbar;:n345d9b395f224850a9b17d60fdab80e3b2 rdfs:subClassOf &lowbar;:n345d9b395f224850a9b17d60fdab80e3b1,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&lowbar;:n345d9b395f224850a9b17d60fdab80e3b2,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#60;http://data.europa.eu/eli/ontology#AdministrativeArea>,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:Thing,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;skos:Concept,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;:AdministrativeArea ;  &#10;&#32;&#32;&#32;&#32;owl:equivalentClass &#60;http://data.europa.eu/eli/ontology#AdministrativeArea>,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;:AdministrativeArea ;  &#10;&#32;&#32;&#32;&#32;owl:intersectionOf &lowbar;:n345d9b395f224850a9b17d60fdab80e3b3 .  &#10;&lowbar;:n345d9b395f224850a9b17d60fdab80e3b1 a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;owl:hasValue :AdministrativeAreaNomenclature ;  &#10;&#32;&#32;&#32;&#32;owl:onProperty skos:inScheme .</code></pre>|
|[Section top](#minorfail-outcome-number-39)|Pointer|<pre lang="Turtle"><code>:AdministrativeArea rdfs:subClassOf &lowbar;:n8cda2f52911942cc99fb3c4b884566d3b1,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&lowbar;:n8cda2f52911942cc99fb3c4b884566d3b2,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;:AdministrativeArea,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:Thing,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;skos:Concept,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;aec3po:AdministrativeArea ;  &#10;&#32;&#32;&#32;&#32;owl:equivalentClass &lowbar;:n8cda2f52911942cc99fb3c4b884566d3b2,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;aec3po:AdministrativeArea ;  &#10;&#32;&#32;&#32;&#32;owl:sameAs :AdministrativeArea .  &#10;&lowbar;:n8cda2f52911942cc99fb3c4b884566d3b3 rdf:first skos:Concept ;  &#10;&#32;&#32;&#32;&#32;rdf:rest ( &lowbar;:n8cda2f52911942cc99fb3c4b884566d3b1 ) .  &#10;&lowbar;:n8cda2f52911942cc99fb3c4b884566d3b1 a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;owl:hasValue aec3po:AdministrativeAreaNomenclature ;  &#10;&#32;&#32;&#32;&#32;owl:onProperty skos:inScheme .  &#10;&lowbar;:n8cda2f52911942cc99fb3c4b884566d3b2 rdfs:subClassOf &lowbar;:n8cda2f52911942cc99fb3c4b884566d3b1,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&lowbar;:n8cda2f52911942cc99fb3c4b884566d3b2,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;:AdministrativeArea,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:Thing,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;skos:Concept,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;aec3po:AdministrativeArea ;  &#10;&#32;&#32;&#32;&#32;owl:equivalentClass :AdministrativeArea,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;aec3po:AdministrativeArea ;  &#10;&#32;&#32;&#32;&#32;owl:intersectionOf &lowbar;:n8cda2f52911942cc99fb3c4b884566d3b3 .</code></pre>|
|[Section top](#minorfail-outcome-number-39)|Pointer|http://www.w3.org/2004/02/skos/core#Concept|

***
### MinorFail Outcome number 40

[Jump to summary definition](#summary-MinorFail-40)	|	[Previous MinorFail outcome](#minorfail-outcome-number-39)	|	[Next MinorFail outcome](#minorfail-outcome-number-41)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-src-vocabularies-administrative-areas|
|----|----|
|Title|Standalone module src/vocabularies/administrative&lowbar;areas.ttl from branch main|
|Composition|- [Module vocabularies/administrative&lowbar;areas](https://github.com/Accord-Project/aec3po/blob/main/src/vocabularies/administrative_areas.ttl)|

#### Criterion detail
|Identifier|[labeled-terms](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#labeled-terms)|
|----|----|
|Title|Term labeling test|
|Description|A test case from the Best Practices tests checking if all the terms of the subject have a rdfs:label property pointing to a literal in English|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-40)|Identifier|`not-labeled-term`|
|[Section top](#minorfail-outcome-number-40)|Title|Terms not labeled|
|[Section top](#minorfail-outcome-number-40)|Description|The following terms have no rdfs:label to define it in natural language|
|[Section top](#minorfail-outcome-number-40)|Pointer|<pre lang="Turtle"><code>:England a owl:NamedIndividual,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;skos:Concept,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;:AdministrativeArea ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy :administrative&lowbar;areas ;  &#10;&#32;&#32;&#32;&#32;skos:definition &#34;England&#34;@en ;  &#10;&#32;&#32;&#32;&#32;skos:inScheme :AdministrativeAreaNomenclature ;  &#10;&#32;&#32;&#32;&#32;skos:prefLabel &#34;England&#34;@en ;  &#10;&#32;&#32;&#32;&#32;skos:topConceptOf :AdministrativeAreaNomenclature .</code></pre>|
|[Section top](#minorfail-outcome-number-40)|Pointer|<pre lang="Turtle"><code>:Estonia a owl:NamedIndividual,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;skos:Concept,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;:AdministrativeArea ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy :administrative&lowbar;areas ;  &#10;&#32;&#32;&#32;&#32;skos:definition &#34;Estonia&#34;@en ;  &#10;&#32;&#32;&#32;&#32;skos:inScheme :AdministrativeAreaNomenclature ;  &#10;&#32;&#32;&#32;&#32;skos:prefLabel &#34;Estonia&#34;@en ;  &#10;&#32;&#32;&#32;&#32;skos:topConceptOf :AdministrativeAreaNomenclature .</code></pre>|
|[Section top](#minorfail-outcome-number-40)|Pointer|<pre lang="Turtle"><code>:Finland a owl:NamedIndividual,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;skos:Concept,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;:AdministrativeArea ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy :administrative&lowbar;areas ;  &#10;&#32;&#32;&#32;&#32;skos:definition &#34;Finland&#34;@en ;  &#10;&#32;&#32;&#32;&#32;skos:inScheme :AdministrativeAreaNomenclature ;  &#10;&#32;&#32;&#32;&#32;skos:prefLabel &#34;Finland&#34;@en ;  &#10;&#32;&#32;&#32;&#32;skos:topConceptOf :AdministrativeAreaNomenclature .</code></pre>|
|[Section top](#minorfail-outcome-number-40)|Pointer|<pre lang="Turtle"><code>:France a owl:NamedIndividual,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;skos:Concept,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;:AdministrativeArea ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy :administrative&lowbar;areas ;  &#10;&#32;&#32;&#32;&#32;skos:definition &#34;France&#34;@en ;  &#10;&#32;&#32;&#32;&#32;skos:inScheme :AdministrativeAreaNomenclature ;  &#10;&#32;&#32;&#32;&#32;skos:prefLabel &#34;France&#34;@en ;  &#10;&#32;&#32;&#32;&#32;skos:topConceptOf :AdministrativeAreaNomenclature .</code></pre>|
|[Section top](#minorfail-outcome-number-40)|Pointer|<pre lang="Turtle"><code>:Germany a owl:NamedIndividual,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;skos:Concept,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;:AdministrativeArea ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy :administrative&lowbar;areas ;  &#10;&#32;&#32;&#32;&#32;skos:definition &#34;Germany&#34;@en ;  &#10;&#32;&#32;&#32;&#32;skos:inScheme :AdministrativeAreaNomenclature ;  &#10;&#32;&#32;&#32;&#32;skos:prefLabel &#34;Germany&#34;@en ;  &#10;&#32;&#32;&#32;&#32;skos:topConceptOf :AdministrativeAreaNomenclature .</code></pre>|
|[Section top](#minorfail-outcome-number-40)|Pointer|<pre lang="Turtle"><code>:Italy a owl:NamedIndividual,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;skos:Concept,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;:AdministrativeArea ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy :administrative&lowbar;areas ;  &#10;&#32;&#32;&#32;&#32;skos:definition &#34;Italy&#34;@en ;  &#10;&#32;&#32;&#32;&#32;skos:inScheme :AdministrativeAreaNomenclature ;  &#10;&#32;&#32;&#32;&#32;skos:prefLabel &#34;Italy&#34;@en ;  &#10;&#32;&#32;&#32;&#32;skos:topConceptOf :AdministrativeAreaNomenclature .</code></pre>|
|[Section top](#minorfail-outcome-number-40)|Pointer|<pre lang="Turtle"><code>:Spain a owl:NamedIndividual,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;skos:Concept,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;:AdministrativeArea ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy :administrative&lowbar;areas ;  &#10;&#32;&#32;&#32;&#32;skos:definition &#34;Spain&#34;@en ;  &#10;&#32;&#32;&#32;&#32;skos:inScheme :AdministrativeAreaNomenclature ;  &#10;&#32;&#32;&#32;&#32;skos:prefLabel &#34;Spain&#34;@en ;  &#10;&#32;&#32;&#32;&#32;skos:topConceptOf :AdministrativeAreaNomenclature .</code></pre>|

***
### MinorFail Outcome number 41

[Jump to summary definition](#summary-MinorFail-41)	|	[Previous MinorFail outcome](#minorfail-outcome-number-40)	|	[Next MinorFail outcome](#minorfail-outcome-number-42)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-src-vocabularies-administrative-areas|
|----|----|
|Title|Standalone module src/vocabularies/administrative&lowbar;areas.ttl from branch main|
|Composition|- [Module vocabularies/administrative&lowbar;areas](https://github.com/Accord-Project/aec3po/blob/main/src/vocabularies/administrative_areas.ttl)|

#### Criterion detail
|Identifier|[profile-compatibility](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#profile-compatibility)|
|----|----|
|Title|Profile compatibility test|
|Description|A test meant to check whether the test subject is compatible with a profile or not, and if it is not, why.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-41)|Identifier|`owl-ql-profile-error`|
|[Section top](#minorfail-outcome-number-41)|Title|OWL QL Profile incompatible|
|[Section top](#minorfail-outcome-number-41)|Description|Statement not supported in a Sub Class Expression|
|[Section top](#minorfail-outcome-number-41)|Pointer|<pre lang="Turtle"><code>&#91;] owl:intersectionOf ( skos:Concept &#91; a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:hasValue aec3po:AdministrativeAreaNomenclature ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:onProperty skos:inScheme ] ) .</code></pre>|

***
### MinorFail Outcome number 42

[Jump to summary definition](#summary-MinorFail-42)	|	[Previous MinorFail outcome](#minorfail-outcome-number-41)	|	[Next MinorFail outcome](#minorfail-outcome-number-43)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-src-vocabularies-administrative-areas|
|----|----|
|Title|Standalone module src/vocabularies/administrative&lowbar;areas.ttl from branch main|
|Composition|- [Module vocabularies/administrative&lowbar;areas](https://github.com/Accord-Project/aec3po/blob/main/src/vocabularies/administrative_areas.ttl)|

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
|[Section top](#minorfail-outcome-number-42)|Description|Statement not supported|
|[Section top](#minorfail-outcome-number-42)|Pointer|<pre lang="Turtle"><code>&#91;] a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;owl:hasValue aec3po:AdministrativeAreaNomenclature ;  &#10;&#32;&#32;&#32;&#32;owl:onProperty skos:inScheme .</code></pre>|

***
### MinorFail Outcome number 43

[Jump to summary definition](#summary-MinorFail-43)	|	[Previous MinorFail outcome](#minorfail-outcome-number-42)	|	[Next MinorFail outcome](#minorfail-outcome-number-44)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-src-vocabularies-administrative-areas|
|----|----|
|Title|Standalone module src/vocabularies/administrative&lowbar;areas.ttl from branch main|
|Composition|- [Module vocabularies/administrative&lowbar;areas](https://github.com/Accord-Project/aec3po/blob/main/src/vocabularies/administrative_areas.ttl)|

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
|[Section top](#minorfail-outcome-number-43)|Description|Class Expression not supported with owl:equivalentClass|
|[Section top](#minorfail-outcome-number-43)|Pointer|<pre lang="Turtle"><code>aec3po:AdministrativeArea a owl:Class ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;Administrative Area&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:comment &#34;Formally defined as the set of skos:Concept either in concep...&#34; ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy aec3po:administrative&lowbar;areas ;  &#10;&#32;&#32;&#32;&#32;rdfs:seeAlso &#60;https://op.europa.eu/en/web/eu-vocabularies/concept-scheme/-/resource?uri=http://publications.europa.eu/resource/authority/atu> ;  &#10;&#32;&#32;&#32;&#32;rdfs:subClassOf skos:Concept ;  &#10;&#32;&#32;&#32;&#32;owl:equivalentClass &#91; owl:intersectionOf ( skos:Concept &#91; a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:hasValue aec3po:AdministrativeAreaNomenclature ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:onProperty skos:inScheme ] ) ],  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#60;http://data.europa.eu/eli/ontology#AdministrativeArea> .</code></pre>|

***
### MinorFail Outcome number 44

[Jump to summary definition](#summary-MinorFail-44)	|	[Previous MinorFail outcome](#minorfail-outcome-number-43)	|	[Next MinorFail outcome](#minorfail-outcome-number-45)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-src-table|
|----|----|
|Title|Standalone module src/table.ttl from branch main|
|Composition|- [Module table](https://github.com/Accord-Project/aec3po/blob/main/src/table.ttl)|

#### Criterion detail
|Identifier|[profile-compatibility](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#profile-compatibility)|
|----|----|
|Title|Profile compatibility test|
|Description|A test meant to check whether the test subject is compatible with a profile or not, and if it is not, why.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-44)|Identifier|`owl-rl-profile-error`|
|[Section top](#minorfail-outcome-number-44)|Title|OWL RL Profile incompatible|
|[Section top](#minorfail-outcome-number-44)|Description|Class Expression not supported as object of rdfs:domain or rdfs:range|
|[Section top](#minorfail-outcome-number-44)|Pointer|<pre lang="Turtle"><code>aec3po:caption a owl:DatatypeProperty ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;caption&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:comment &#34;The caption of a table, image, etc. &#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:domain &#91; a owl:Class ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:unionOf ( aec3po:Table aec3po:Image ) ] ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy aec3po:table .</code></pre>|
|[Section top](#minorfail-outcome-number-44)|Pointer|<pre lang="Turtle"><code>aec3po:contains a owl:ObjectProperty ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;Contains&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:comment &#34;A container contains a table and its caption. A table contai...&#34; ;  &#10;&#32;&#32;&#32;&#32;rdfs:domain &#91; a owl:Class ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:unionOf ( aec3po:Table aec3po:Image aec3po:Row aec3po:Column ) ] ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy aec3po:table .</code></pre>|
|[Section top](#minorfail-outcome-number-44)|Pointer|<pre lang="Turtle"><code>aec3po:isContainedIn a owl:ObjectProperty ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;is contained by&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:comment &#34;A table contains row, columns and other elements.&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy aec3po:table ;  &#10;&#32;&#32;&#32;&#32;rdfs:range &#91; a owl:Class ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:unionOf ( aec3po:Table aec3po:Image aec3po:Row aec3po:Column aec3po:Cell ) ] .</code></pre>|

***
### MinorFail Outcome number 45

[Jump to summary definition](#summary-MinorFail-45)	|	[Previous MinorFail outcome](#minorfail-outcome-number-44)	|	[Next MinorFail outcome](#minorfail-outcome-number-46)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-src-table|
|----|----|
|Title|Standalone module src/table.ttl from branch main|
|Composition|- [Module table](https://github.com/Accord-Project/aec3po/blob/main/src/table.ttl)|

#### Criterion detail
|Identifier|[profile-compatibility](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#profile-compatibility)|
|----|----|
|Title|Profile compatibility test|
|Description|A test meant to check whether the test subject is compatible with a profile or not, and if it is not, why.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-45)|Identifier|`owl-rl-profile-error`|
|[Section top](#minorfail-outcome-number-45)|Title|OWL RL Profile incompatible|
|[Section top](#minorfail-outcome-number-45)|Description|Statement not supported in a Super Class Expression|
|[Section top](#minorfail-outcome-number-45)|Pointer|<pre lang="Turtle"><code>&#91;] a owl:Class ;  &#10;&#32;&#32;&#32;&#32;owl:unionOf ( aec3po:Table aec3po:Image aec3po:Row aec3po:Column ) .</code></pre>|
|[Section top](#minorfail-outcome-number-45)|Pointer|<pre lang="Turtle"><code>&#91;] a owl:Class ;  &#10;&#32;&#32;&#32;&#32;owl:unionOf ( aec3po:Table aec3po:Image aec3po:Row aec3po:Column aec3po:Cell ) .</code></pre>|
|[Section top](#minorfail-outcome-number-45)|Pointer|<pre lang="Turtle"><code>&#91;] a owl:Class ;  &#10;&#32;&#32;&#32;&#32;owl:unionOf ( aec3po:Table aec3po:Image ) .</code></pre>|

***
### MinorFail Outcome number 46

[Jump to summary definition](#summary-MinorFail-46)	|	[Previous MinorFail outcome](#minorfail-outcome-number-45)	|	[Next MinorFail outcome](#minorfail-outcome-number-47)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-src-table|
|----|----|
|Title|Standalone module src/table.ttl from branch main|
|Composition|- [Module table](https://github.com/Accord-Project/aec3po/blob/main/src/table.ttl)|

#### Criterion detail
|Identifier|[profile-compatibility](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#profile-compatibility)|
|----|----|
|Title|Profile compatibility test|
|Description|A test meant to check whether the test subject is compatible with a profile or not, and if it is not, why.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-46)|Identifier|`owl-ql-profile-error`|
|[Section top](#minorfail-outcome-number-46)|Title|OWL QL Profile incompatible|
|[Section top](#minorfail-outcome-number-46)|Description|Class Expression not supported as object of rdfs:domain or rdfs:range|
|[Section top](#minorfail-outcome-number-46)|Pointer|<pre lang="Turtle"><code>aec3po:caption a owl:DatatypeProperty ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;caption&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:comment &#34;The caption of a table, image, etc. &#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:domain &#91; a owl:Class ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:unionOf ( aec3po:Table aec3po:Image ) ] ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy aec3po:table .</code></pre>|
|[Section top](#minorfail-outcome-number-46)|Pointer|<pre lang="Turtle"><code>aec3po:contains a owl:ObjectProperty ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;Contains&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:comment &#34;A container contains a table and its caption. A table contai...&#34; ;  &#10;&#32;&#32;&#32;&#32;rdfs:domain &#91; a owl:Class ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:unionOf ( aec3po:Table aec3po:Image aec3po:Row aec3po:Column ) ] ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy aec3po:table .</code></pre>|
|[Section top](#minorfail-outcome-number-46)|Pointer|<pre lang="Turtle"><code>aec3po:isContainedIn a owl:ObjectProperty ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;is contained by&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:comment &#34;A table contains row, columns and other elements.&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy aec3po:table ;  &#10;&#32;&#32;&#32;&#32;rdfs:range &#91; a owl:Class ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:unionOf ( aec3po:Table aec3po:Image aec3po:Row aec3po:Column aec3po:Cell ) ] .</code></pre>|

***
### MinorFail Outcome number 47

[Jump to summary definition](#summary-MinorFail-47)	|	[Previous MinorFail outcome](#minorfail-outcome-number-46)	|	[Next MinorFail outcome](#minorfail-outcome-number-48)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-src-table|
|----|----|
|Title|Standalone module src/table.ttl from branch main|
|Composition|- [Module table](https://github.com/Accord-Project/aec3po/blob/main/src/table.ttl)|

#### Criterion detail
|Identifier|[profile-compatibility](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#profile-compatibility)|
|----|----|
|Title|Profile compatibility test|
|Description|A test meant to check whether the test subject is compatible with a profile or not, and if it is not, why.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-47)|Identifier|`owl-ql-profile-error`|
|[Section top](#minorfail-outcome-number-47)|Title|OWL QL Profile incompatible|
|[Section top](#minorfail-outcome-number-47)|Description|Statement not supported in a Super Class Expression|
|[Section top](#minorfail-outcome-number-47)|Pointer|<pre lang="Turtle"><code>&#91;] a owl:Class ;  &#10;&#32;&#32;&#32;&#32;owl:unionOf ( aec3po:Table aec3po:Image aec3po:Row aec3po:Column ) .</code></pre>|
|[Section top](#minorfail-outcome-number-47)|Pointer|<pre lang="Turtle"><code>&#91;] a owl:Class ;  &#10;&#32;&#32;&#32;&#32;owl:unionOf ( aec3po:Table aec3po:Image aec3po:Row aec3po:Column aec3po:Cell ) .</code></pre>|
|[Section top](#minorfail-outcome-number-47)|Pointer|<pre lang="Turtle"><code>&#91;] a owl:Class ;  &#10;&#32;&#32;&#32;&#32;owl:unionOf ( aec3po:Table aec3po:Image ) .</code></pre>|

***
### MinorFail Outcome number 48

[Jump to summary definition](#summary-MinorFail-48)	|	[Previous MinorFail outcome](#minorfail-outcome-number-47)	|	[Next MinorFail outcome](#minorfail-outcome-number-49)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-src-table|
|----|----|
|Title|Standalone module src/table.ttl from branch main|
|Composition|- [Module table](https://github.com/Accord-Project/aec3po/blob/main/src/table.ttl)|

#### Criterion detail
|Identifier|[profile-compatibility](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#profile-compatibility)|
|----|----|
|Title|Profile compatibility test|
|Description|A test meant to check whether the test subject is compatible with a profile or not, and if it is not, why.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-48)|Identifier|`owl-el-profile-error`|
|[Section top](#minorfail-outcome-number-48)|Title|OWL EL Profile incompatible|
|[Section top](#minorfail-outcome-number-48)|Description|Statement not supported in a Class Expression|
|[Section top](#minorfail-outcome-number-48)|Pointer|<pre lang="Turtle"><code>&#91;] a owl:Class ;  &#10;&#32;&#32;&#32;&#32;owl:unionOf ( aec3po:Table aec3po:Image aec3po:Row aec3po:Column ) .</code></pre>|
|[Section top](#minorfail-outcome-number-48)|Pointer|<pre lang="Turtle"><code>&#91;] a owl:Class ;  &#10;&#32;&#32;&#32;&#32;owl:unionOf ( aec3po:Table aec3po:Image aec3po:Row aec3po:Column aec3po:Cell ) .</code></pre>|
|[Section top](#minorfail-outcome-number-48)|Pointer|<pre lang="Turtle"><code>&#91;] a owl:Class ;  &#10;&#32;&#32;&#32;&#32;owl:unionOf ( aec3po:Table aec3po:Image ) .</code></pre>|

***
### MinorFail Outcome number 49

[Jump to summary definition](#summary-MinorFail-49)	|	[Previous MinorFail outcome](#minorfail-outcome-number-48)	|	[Next MinorFail outcome](#minorfail-outcome-number-50)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-src-table|
|----|----|
|Title|Standalone module src/table.ttl from branch main|
|Composition|- [Module table](https://github.com/Accord-Project/aec3po/blob/main/src/table.ttl)|

#### Criterion detail
|Identifier|[profile-compatibility](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#profile-compatibility)|
|----|----|
|Title|Profile compatibility test|
|Description|A test meant to check whether the test subject is compatible with a profile or not, and if it is not, why.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-49)|Identifier|`owl-el-profile-error`|
|[Section top](#minorfail-outcome-number-49)|Title|OWL EL Profile incompatible|
|[Section top](#minorfail-outcome-number-49)|Description|Class Expression not supported as object of rdfs:domain or rdfs:range|
|[Section top](#minorfail-outcome-number-49)|Pointer|<pre lang="Turtle"><code>aec3po:caption a owl:DatatypeProperty ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;caption&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:comment &#34;The caption of a table, image, etc. &#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:domain &#91; a owl:Class ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:unionOf ( aec3po:Table aec3po:Image ) ] ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy aec3po:table .</code></pre>|
|[Section top](#minorfail-outcome-number-49)|Pointer|<pre lang="Turtle"><code>aec3po:contains a owl:ObjectProperty ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;Contains&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:comment &#34;A container contains a table and its caption. A table contai...&#34; ;  &#10;&#32;&#32;&#32;&#32;rdfs:domain &#91; a owl:Class ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:unionOf ( aec3po:Table aec3po:Image aec3po:Row aec3po:Column ) ] ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy aec3po:table .</code></pre>|
|[Section top](#minorfail-outcome-number-49)|Pointer|<pre lang="Turtle"><code>aec3po:isContainedIn a owl:ObjectProperty ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;is contained by&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:comment &#34;A table contains row, columns and other elements.&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy aec3po:table ;  &#10;&#32;&#32;&#32;&#32;rdfs:range &#91; a owl:Class ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:unionOf ( aec3po:Table aec3po:Image aec3po:Row aec3po:Column aec3po:Cell ) ] .</code></pre>|

***
### MinorFail Outcome number 50

[Jump to summary definition](#summary-MinorFail-50)	|	[Previous MinorFail outcome](#minorfail-outcome-number-49)	|	[Next MinorFail outcome](#minorfail-outcome-number-51)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-src-statement|
|----|----|
|Title|Standalone module src/statement.ttl from branch main|
|Composition|- [Module statement](https://github.com/Accord-Project/aec3po/blob/main/src/statement.ttl)|

#### Criterion detail
|Identifier|[profile-compatibility](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#profile-compatibility)|
|----|----|
|Title|Profile compatibility test|
|Description|A test meant to check whether the test subject is compatible with a profile or not, and if it is not, why.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-50)|Identifier|`owl-rl-profile-error`|
|[Section top](#minorfail-outcome-number-50)|Title|OWL RL Profile incompatible|
|[Section top](#minorfail-outcome-number-50)|Description|Class Expression not supported with rdfs:subClassOf|
|[Section top](#minorfail-outcome-number-50)|Pointer|<pre lang="Turtle"><code>aec3po:AndCheckStatement a owl:Class ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;And Check Statement&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:comment &#34;Check verified if and only if all of its sub-checks are veri...&#34; ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy aec3po:statement ;  &#10;&#32;&#32;&#32;&#32;rdfs:subClassOf &#91; a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:onProperty aec3po:hasSubdivision ],  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;aec3po:ChecklistStatement .</code></pre>|
|[Section top](#minorfail-outcome-number-50)|Pointer|<pre lang="Turtle"><code>aec3po:NotCheckStatement a owl:Class ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;Not Check Statement&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:comment &#34;Check verified if and only if the sub-check is not verified.&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy aec3po:statement ;  &#10;&#32;&#32;&#32;&#32;rdfs:subClassOf &#91; a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:onProperty aec3po:hasSubdivision ] .</code></pre>|
|[Section top](#minorfail-outcome-number-50)|Pointer|<pre lang="Turtle"><code>aec3po:OrCheckStatement a owl:Class ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;Or Check Statement&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:comment &#34;Check verified if and only if at least one of its sub-checks...&#34; ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy aec3po:statement ;  &#10;&#32;&#32;&#32;&#32;rdfs:subClassOf &#91; a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:onProperty aec3po:hasSubdivision ],  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;aec3po:ChecklistStatement .</code></pre>|

***
### MinorFail Outcome number 51

[Jump to summary definition](#summary-MinorFail-51)	|	[Previous MinorFail outcome](#minorfail-outcome-number-50)	|	[Next MinorFail outcome](#minorfail-outcome-number-52)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-src-statement|
|----|----|
|Title|Standalone module src/statement.ttl from branch main|
|Composition|- [Module statement](https://github.com/Accord-Project/aec3po/blob/main/src/statement.ttl)|

#### Criterion detail
|Identifier|[profile-compatibility](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#profile-compatibility)|
|----|----|
|Title|Profile compatibility test|
|Description|A test meant to check whether the test subject is compatible with a profile or not, and if it is not, why.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-51)|Identifier|`owl-rl-profile-error`|
|[Section top](#minorfail-outcome-number-51)|Title|OWL RL Profile incompatible|
|[Section top](#minorfail-outcome-number-51)|Description|Statement not supported in a Super Class Expression|
|[Section top](#minorfail-outcome-number-51)|Pointer|<pre lang="Turtle"><code>&#91;] a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;owl:onProperty aec3po:hasSubdivision .</code></pre>|

***
### MinorFail Outcome number 52

[Jump to summary definition](#summary-MinorFail-52)	|	[Previous MinorFail outcome](#minorfail-outcome-number-51)	|	[Next MinorFail outcome](#minorfail-outcome-number-53)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-src-statement|
|----|----|
|Title|Standalone module src/statement.ttl from branch main|
|Composition|- [Module statement](https://github.com/Accord-Project/aec3po/blob/main/src/statement.ttl)|

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
|[Section top](#minorfail-outcome-number-52)|Description|Statement not supported  &#10;Statement not supported in a Super Class Expression|
|[Section top](#minorfail-outcome-number-52)|Pointer|<pre lang="Turtle"><code>&#91;] a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;owl:onProperty aec3po:hasSubdivision .</code></pre>|

***
### MinorFail Outcome number 53

[Jump to summary definition](#summary-MinorFail-53)	|	[Previous MinorFail outcome](#minorfail-outcome-number-52)	|	[Next MinorFail outcome](#minorfail-outcome-number-54)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-src-statement|
|----|----|
|Title|Standalone module src/statement.ttl from branch main|
|Composition|- [Module statement](https://github.com/Accord-Project/aec3po/blob/main/src/statement.ttl)|

#### Criterion detail
|Identifier|[profile-compatibility](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#profile-compatibility)|
|----|----|
|Title|Profile compatibility test|
|Description|A test meant to check whether the test subject is compatible with a profile or not, and if it is not, why.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-53)|Identifier|`owl-ql-profile-error`|
|[Section top](#minorfail-outcome-number-53)|Title|OWL QL Profile incompatible|
|[Section top](#minorfail-outcome-number-53)|Description|Class Expression not supported with rdfs:subClassOf|
|[Section top](#minorfail-outcome-number-53)|Pointer|<pre lang="Turtle"><code>aec3po:AndCheckStatement a owl:Class ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;And Check Statement&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:comment &#34;Check verified if and only if all of its sub-checks are veri...&#34; ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy aec3po:statement ;  &#10;&#32;&#32;&#32;&#32;rdfs:subClassOf &#91; a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:onProperty aec3po:hasSubdivision ],  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;aec3po:ChecklistStatement .</code></pre>|
|[Section top](#minorfail-outcome-number-53)|Pointer|<pre lang="Turtle"><code>aec3po:NotCheckStatement a owl:Class ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;Not Check Statement&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:comment &#34;Check verified if and only if the sub-check is not verified.&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy aec3po:statement ;  &#10;&#32;&#32;&#32;&#32;rdfs:subClassOf &#91; a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:onProperty aec3po:hasSubdivision ] .</code></pre>|
|[Section top](#minorfail-outcome-number-53)|Pointer|<pre lang="Turtle"><code>aec3po:OrCheckStatement a owl:Class ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;Or Check Statement&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:comment &#34;Check verified if and only if at least one of its sub-checks...&#34; ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy aec3po:statement ;  &#10;&#32;&#32;&#32;&#32;rdfs:subClassOf &#91; a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:onProperty aec3po:hasSubdivision ],  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;aec3po:ChecklistStatement .</code></pre>|

***
### MinorFail Outcome number 54

[Jump to summary definition](#summary-MinorFail-54)	|	[Previous MinorFail outcome](#minorfail-outcome-number-53)	|	[Next MinorFail outcome](#minorfail-outcome-number-55)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-src-statement|
|----|----|
|Title|Standalone module src/statement.ttl from branch main|
|Composition|- [Module statement](https://github.com/Accord-Project/aec3po/blob/main/src/statement.ttl)|

#### Criterion detail
|Identifier|[profile-compatibility](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#profile-compatibility)|
|----|----|
|Title|Profile compatibility test|
|Description|A test meant to check whether the test subject is compatible with a profile or not, and if it is not, why.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-54)|Identifier|`owl-ql-profile-error`|
|[Section top](#minorfail-outcome-number-54)|Title|OWL QL Profile incompatible|
|[Section top](#minorfail-outcome-number-54)|Description|Statement not supported in a Super Class Expression|
|[Section top](#minorfail-outcome-number-54)|Pointer|<pre lang="Turtle"><code>&#91;] a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;owl:onProperty aec3po:hasSubdivision .</code></pre>|

***
### MinorFail Outcome number 55

[Jump to summary definition](#summary-MinorFail-55)	|	[Previous MinorFail outcome](#minorfail-outcome-number-54)	|	[Next MinorFail outcome](#minorfail-outcome-number-56)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-src-statement|
|----|----|
|Title|Standalone module src/statement.ttl from branch main|
|Composition|- [Module statement](https://github.com/Accord-Project/aec3po/blob/main/src/statement.ttl)|

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
|[Section top](#minorfail-outcome-number-55)|Description|Statement not supported in a Class Expression|
|[Section top](#minorfail-outcome-number-55)|Pointer|<pre lang="Turtle"><code>&#91;] a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;owl:onProperty aec3po:hasSubdivision .</code></pre>|

***
### MinorFail Outcome number 56

[Jump to summary definition](#summary-MinorFail-56)	|	[Previous MinorFail outcome](#minorfail-outcome-number-55)	|	[Next MinorFail outcome](#minorfail-outcome-number-57)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-src-statement|
|----|----|
|Title|Standalone module src/statement.ttl from branch main|
|Composition|- [Module statement](https://github.com/Accord-Project/aec3po/blob/main/src/statement.ttl)|

#### Criterion detail
|Identifier|[profile-compatibility](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#profile-compatibility)|
|----|----|
|Title|Profile compatibility test|
|Description|A test meant to check whether the test subject is compatible with a profile or not, and if it is not, why.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-56)|Identifier|`owl-el-profile-error`|
|[Section top](#minorfail-outcome-number-56)|Title|OWL EL Profile incompatible|
|[Section top](#minorfail-outcome-number-56)|Description|Statement not supported  &#10;Statement not supported in a Class Expression|
|[Section top](#minorfail-outcome-number-56)|Pointer|<pre lang="Turtle"><code>&#91;] a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;owl:onProperty aec3po:hasSubdivision .</code></pre>|

***
### MinorFail Outcome number 57

[Jump to summary definition](#summary-MinorFail-57)	|	[Previous MinorFail outcome](#minorfail-outcome-number-56)	|	[Next MinorFail outcome](#minorfail-outcome-number-58)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-src-statement|
|----|----|
|Title|Standalone module src/statement.ttl from branch main|
|Composition|- [Module statement](https://github.com/Accord-Project/aec3po/blob/main/src/statement.ttl)|

#### Criterion detail
|Identifier|[profile-compatibility](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#profile-compatibility)|
|----|----|
|Title|Profile compatibility test|
|Description|A test meant to check whether the test subject is compatible with a profile or not, and if it is not, why.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-57)|Identifier|`owl-el-profile-error`|
|[Section top](#minorfail-outcome-number-57)|Title|OWL EL Profile incompatible|
|[Section top](#minorfail-outcome-number-57)|Description|Class Expression not supported with rdfs:subClassOf|
|[Section top](#minorfail-outcome-number-57)|Pointer|<pre lang="Turtle"><code>aec3po:AndCheckStatement a owl:Class ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;And Check Statement&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:comment &#34;Check verified if and only if all of its sub-checks are veri...&#34; ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy aec3po:statement ;  &#10;&#32;&#32;&#32;&#32;rdfs:subClassOf &#91; a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:onProperty aec3po:hasSubdivision ],  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;aec3po:ChecklistStatement .</code></pre>|
|[Section top](#minorfail-outcome-number-57)|Pointer|<pre lang="Turtle"><code>aec3po:NotCheckStatement a owl:Class ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;Not Check Statement&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:comment &#34;Check verified if and only if the sub-check is not verified.&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy aec3po:statement ;  &#10;&#32;&#32;&#32;&#32;rdfs:subClassOf &#91; a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:onProperty aec3po:hasSubdivision ] .</code></pre>|
|[Section top](#minorfail-outcome-number-57)|Pointer|<pre lang="Turtle"><code>aec3po:OrCheckStatement a owl:Class ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;Or Check Statement&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:comment &#34;Check verified if and only if at least one of its sub-checks...&#34; ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy aec3po:statement ;  &#10;&#32;&#32;&#32;&#32;rdfs:subClassOf &#91; a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:onProperty aec3po:hasSubdivision ],  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;aec3po:ChecklistStatement .</code></pre>|

***
### MinorFail Outcome number 58

[Jump to summary definition](#summary-MinorFail-58)	|	[Previous MinorFail outcome](#minorfail-outcome-number-57)	|	[Next MinorFail outcome](#minorfail-outcome-number-59)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-src-statement|
|----|----|
|Title|Standalone module src/statement.ttl from branch main|
|Composition|- [Module statement](https://github.com/Accord-Project/aec3po/blob/main/src/statement.ttl)|

#### Criterion detail
|Identifier|[terms-differenciation](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#terms-differenciation)|
|----|----|
|Title|Terms differenciation test|
|Description|A test case from the Best Practices tests checking if all the terms are different enough from each other according to the Levenshtein distance metric.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-58)|Identifier|`too-close-terms`|
|[Section top](#minorfail-outcome-number-58)|Title|Too close terms|
|[Section top](#minorfail-outcome-number-58)|Description|Some terms are too similar|
|[Section top](#minorfail-outcome-number-58)|Pointer|<pre lang="Turtle"><code>:OrCheckStatement a owl:Class ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;Or Check Statement&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:comment &#34;Check verified if and only if at least one of its sub-checks...&#34; ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy :statement ;  &#10;&#32;&#32;&#32;&#32;rdfs:subClassOf &#91; a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:onProperty :hasSubdivision ],  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;:ChecklistStatement .</code></pre>|
|[Section top](#minorfail-outcome-number-58)|Pointer|<pre lang="Turtle"><code>:CheckStatement a owl:Class ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;Check Statement&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:comment &#34;refers to a type of statement that is used to specify condit...&#34; ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy :statement ;  &#10;&#32;&#32;&#32;&#32;rdfs:subClassOf :Statement .</code></pre>|

***
### MinorFail Outcome number 59

[Jump to summary definition](#summary-MinorFail-59)	|	[Previous MinorFail outcome](#minorfail-outcome-number-58)	|	[Next MinorFail outcome](#minorfail-outcome-number-60)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-src-model|
|----|----|
|Title|Standalone module src/model.ttl from branch main|
|Composition|- [Module model](https://github.com/Accord-Project/aec3po/blob/main/src/model.ttl)|

#### Criterion detail
|Identifier|[profile-compatibility](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#profile-compatibility)|
|----|----|
|Title|Profile compatibility test|
|Description|A test meant to check whether the test subject is compatible with a profile or not, and if it is not, why.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-59)|Identifier|`owl-rl-profile-error`|
|[Section top](#minorfail-outcome-number-59)|Title|OWL RL Profile incompatible|
|[Section top](#minorfail-outcome-number-59)|Description|Class Expression not supported as object of rdfs:domain or rdfs:range|
|[Section top](#minorfail-outcome-number-59)|Pointer|<pre lang="Turtle"><code>aec3po:locationCoverage a owl:ObjectProperty ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;location coverage&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:comment &#34;The spatialCoverage indicates the place(s) or the administra...&#34; ;  &#10;&#32;&#32;&#32;&#32;rdfs:domain &#60;https://schema.org/Model> ;  &#10;&#32;&#32;&#32;&#32;rdfs:range &#91; a owl:Class ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:unionOf ( &#60;https://schema.org/Place> aec3po:AdministrativeArea ) ] ;  &#10;&#32;&#32;&#32;&#32;owl:equivalentProperty &#60;https://schema.org/spatialCoverage> .</code></pre>|

***
### MinorFail Outcome number 60

[Jump to summary definition](#summary-MinorFail-60)	|	[Previous MinorFail outcome](#minorfail-outcome-number-59)	|	[Next MinorFail outcome](#minorfail-outcome-number-61)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-src-model|
|----|----|
|Title|Standalone module src/model.ttl from branch main|
|Composition|- [Module model](https://github.com/Accord-Project/aec3po/blob/main/src/model.ttl)|

#### Criterion detail
|Identifier|[profile-compatibility](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#profile-compatibility)|
|----|----|
|Title|Profile compatibility test|
|Description|A test meant to check whether the test subject is compatible with a profile or not, and if it is not, why.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-60)|Identifier|`owl-rl-profile-error`|
|[Section top](#minorfail-outcome-number-60)|Title|OWL RL Profile incompatible|
|[Section top](#minorfail-outcome-number-60)|Description|Statement not supported in a Super Class Expression|
|[Section top](#minorfail-outcome-number-60)|Pointer|<pre lang="Turtle"><code>&#91;] a owl:Class ;  &#10;&#32;&#32;&#32;&#32;owl:unionOf ( &#60;https://schema.org/Place> aec3po:AdministrativeArea ) .</code></pre>|

***
### MinorFail Outcome number 61

[Jump to summary definition](#summary-MinorFail-61)	|	[Previous MinorFail outcome](#minorfail-outcome-number-60)	|	[Next MinorFail outcome](#minorfail-outcome-number-62)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-src-model|
|----|----|
|Title|Standalone module src/model.ttl from branch main|
|Composition|- [Module model](https://github.com/Accord-Project/aec3po/blob/main/src/model.ttl)|

#### Criterion detail
|Identifier|[profile-compatibility](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#profile-compatibility)|
|----|----|
|Title|Profile compatibility test|
|Description|A test meant to check whether the test subject is compatible with a profile or not, and if it is not, why.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-61)|Identifier|`owl-ql-profile-error`|
|[Section top](#minorfail-outcome-number-61)|Title|OWL QL Profile incompatible|
|[Section top](#minorfail-outcome-number-61)|Description|Class Expression not supported as object of rdfs:domain or rdfs:range|
|[Section top](#minorfail-outcome-number-61)|Pointer|<pre lang="Turtle"><code>aec3po:locationCoverage a owl:ObjectProperty ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;location coverage&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:comment &#34;The spatialCoverage indicates the place(s) or the administra...&#34; ;  &#10;&#32;&#32;&#32;&#32;rdfs:domain &#60;https://schema.org/Model> ;  &#10;&#32;&#32;&#32;&#32;rdfs:range &#91; a owl:Class ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:unionOf ( &#60;https://schema.org/Place> aec3po:AdministrativeArea ) ] ;  &#10;&#32;&#32;&#32;&#32;owl:equivalentProperty &#60;https://schema.org/spatialCoverage> .</code></pre>|

***
### MinorFail Outcome number 62

[Jump to summary definition](#summary-MinorFail-62)	|	[Previous MinorFail outcome](#minorfail-outcome-number-61)	|	[Next MinorFail outcome](#minorfail-outcome-number-63)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-src-model|
|----|----|
|Title|Standalone module src/model.ttl from branch main|
|Composition|- [Module model](https://github.com/Accord-Project/aec3po/blob/main/src/model.ttl)|

#### Criterion detail
|Identifier|[profile-compatibility](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#profile-compatibility)|
|----|----|
|Title|Profile compatibility test|
|Description|A test meant to check whether the test subject is compatible with a profile or not, and if it is not, why.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-62)|Identifier|`owl-ql-profile-error`|
|[Section top](#minorfail-outcome-number-62)|Title|OWL QL Profile incompatible|
|[Section top](#minorfail-outcome-number-62)|Description|Statement not supported in a Super Class Expression|
|[Section top](#minorfail-outcome-number-62)|Pointer|<pre lang="Turtle"><code>&#91;] a owl:Class ;  &#10;&#32;&#32;&#32;&#32;owl:unionOf ( &#60;https://schema.org/Place> aec3po:AdministrativeArea ) .</code></pre>|

***
### MinorFail Outcome number 63

[Jump to summary definition](#summary-MinorFail-63)	|	[Previous MinorFail outcome](#minorfail-outcome-number-62)	|	[Next MinorFail outcome](#minorfail-outcome-number-64)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-src-model|
|----|----|
|Title|Standalone module src/model.ttl from branch main|
|Composition|- [Module model](https://github.com/Accord-Project/aec3po/blob/main/src/model.ttl)|

#### Criterion detail
|Identifier|[profile-compatibility](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#profile-compatibility)|
|----|----|
|Title|Profile compatibility test|
|Description|A test meant to check whether the test subject is compatible with a profile or not, and if it is not, why.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-63)|Identifier|`owl-el-profile-error`|
|[Section top](#minorfail-outcome-number-63)|Title|OWL EL Profile incompatible|
|[Section top](#minorfail-outcome-number-63)|Description|Statement not supported in a Class Expression|
|[Section top](#minorfail-outcome-number-63)|Pointer|<pre lang="Turtle"><code>&#91;] a owl:Class ;  &#10;&#32;&#32;&#32;&#32;owl:unionOf ( &#60;https://schema.org/Place> aec3po:AdministrativeArea ) .</code></pre>|

***
### MinorFail Outcome number 64

[Jump to summary definition](#summary-MinorFail-64)	|	[Previous MinorFail outcome](#minorfail-outcome-number-63)	|	[Next MinorFail outcome](#minorfail-outcome-number-65)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-src-model|
|----|----|
|Title|Standalone module src/model.ttl from branch main|
|Composition|- [Module model](https://github.com/Accord-Project/aec3po/blob/main/src/model.ttl)|

#### Criterion detail
|Identifier|[profile-compatibility](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#profile-compatibility)|
|----|----|
|Title|Profile compatibility test|
|Description|A test meant to check whether the test subject is compatible with a profile or not, and if it is not, why.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-64)|Identifier|`owl-el-profile-error`|
|[Section top](#minorfail-outcome-number-64)|Title|OWL EL Profile incompatible|
|[Section top](#minorfail-outcome-number-64)|Description|Class Expression not supported as object of rdfs:domain or rdfs:range|
|[Section top](#minorfail-outcome-number-64)|Pointer|<pre lang="Turtle"><code>aec3po:locationCoverage a owl:ObjectProperty ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;location coverage&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:comment &#34;The spatialCoverage indicates the place(s) or the administra...&#34; ;  &#10;&#32;&#32;&#32;&#32;rdfs:domain &#60;https://schema.org/Model> ;  &#10;&#32;&#32;&#32;&#32;rdfs:range &#91; a owl:Class ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:unionOf ( &#60;https://schema.org/Place> aec3po:AdministrativeArea ) ] ;  &#10;&#32;&#32;&#32;&#32;owl:equivalentProperty &#60;https://schema.org/spatialCoverage> .</code></pre>|

***
### MinorFail Outcome number 65

[Jump to summary definition](#summary-MinorFail-65)	|	[Previous MinorFail outcome](#minorfail-outcome-number-64)	|	[Next MinorFail outcome](#minorfail-outcome-number-66)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-src-model|
|----|----|
|Title|Standalone module src/model.ttl from branch main|
|Composition|- [Module model](https://github.com/Accord-Project/aec3po/blob/main/src/model.ttl)|

#### Criterion detail
|Identifier|[term-referencing](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#term-referencing)|
|----|----|
|Title|Term referencing test|
|Description|A test case from the Best Practices tests checking if each term of the test subject is referenced to a module through a rdfs:isDefinedBy property.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-65)|Identifier|`no-reference-module`|
|[Section top](#minorfail-outcome-number-65)|Title|Term not referenced to a module|
|[Section top](#minorfail-outcome-number-65)|Description|Subject terms not linked to a module by a rdfs:isDefinedBy property|
|[Section top](#minorfail-outcome-number-65)|Pointer|<pre lang="Turtle"><code>:name a owl:DatatypeProperty ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;name&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:comment &#34;The name or the identifier of the BIM model.&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:domain &#60;https://schema.org/Model> ;  &#10;&#32;&#32;&#32;&#32;rdfs:range xsd:string ;  &#10;&#32;&#32;&#32;&#32;owl:equivalentProperty &#60;https://schema.org/about> ;  &#10;&#32;&#32;&#32;&#32;owl:inverseOf &#60;https://schema.org/subjectOf> .</code></pre>|
|[Section top](#minorfail-outcome-number-65)|Pointer|<pre lang="Turtle"><code>:description a owl:DatatypeProperty ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;description&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:comment &#34;A textual description providing additional details about the...&#34; ;  &#10;&#32;&#32;&#32;&#32;rdfs:domain &#60;https://schema.org/Model> ;  &#10;&#32;&#32;&#32;&#32;rdfs:range xsd:string ;  &#10;&#32;&#32;&#32;&#32;owl:equivalentProperty &#60;https://schema.org/abstract> .</code></pre>|
|[Section top](#minorfail-outcome-number-65)|Pointer|<pre lang="Turtle"><code>:location a owl:ObjectProperty ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;location&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:comment &#34;The physical or geographic location of the building or struc...&#34; ;  &#10;&#32;&#32;&#32;&#32;rdfs:domain &#60;https://schema.org/Model> ;  &#10;&#32;&#32;&#32;&#32;rdfs:range &#60;https://schema.org/Place> ;  &#10;&#32;&#32;&#32;&#32;owl:equivalentProperty &#60;https://schema.org/spatial> .</code></pre>|
|[Section top](#minorfail-outcome-number-65)|Pointer|<pre lang="Turtle"><code>:locationCoverage a owl:ObjectProperty ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;location coverage&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:comment &#34;The spatialCoverage indicates the place(s) or the administra...&#34; ;  &#10;&#32;&#32;&#32;&#32;rdfs:domain &#60;https://schema.org/Model> ;  &#10;&#32;&#32;&#32;&#32;rdfs:range &#91; a owl:Class ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:unionOf ( &#60;https://schema.org/Place> :AdministrativeArea ) ] ;  &#10;&#32;&#32;&#32;&#32;owl:equivalentProperty &#60;https://schema.org/spatialCoverage> .</code></pre>|
|[Section top](#minorfail-outcome-number-65)|Pointer|<pre lang="Turtle"><code>:material a owl:DatatypeProperty ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;material&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:comment &#34;The materials used for different parts of the building, such...&#34; ;  &#10;&#32;&#32;&#32;&#32;rdfs:domain &#60;https://schema.org/Model> ;  &#10;&#32;&#32;&#32;&#32;rdfs:range xsd:string ;  &#10;&#32;&#32;&#32;&#32;owl:equivalentProperty &#60;https://schema.org/material> .</code></pre>|
|[Section top](#minorfail-outcome-number-65)|Pointer|<pre lang="Turtle"><code>:hasBuildingPhase a owl:ObjectProperty ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;has building phase&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:comment &#34;describes the relationship between a construction-related en...&#34; ;  &#10;&#32;&#32;&#32;&#32;rdfs:domain :Model ;  &#10;&#32;&#32;&#32;&#32;rdfs:range :Phase .</code></pre>|
|[Section top](#minorfail-outcome-number-65)|Pointer|<pre lang="Turtle"><code>:hasElementPhase a owl:ObjectProperty ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;has element phase&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:comment &#34;is used to establish a relationship between a construction e...&#34; ;  &#10;&#32;&#32;&#32;&#32;rdfs:domain :Model ;  &#10;&#32;&#32;&#32;&#32;rdfs:range :Phase .</code></pre>|
|[Section top](#minorfail-outcome-number-65)|Pointer|<pre lang="Turtle"><code>:hasDimension a owl:ObjectProperty ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;has dimension&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:comment &#34;is used to represent the physical dimensions or measurements...&#34; ;  &#10;&#32;&#32;&#32;&#32;rdfs:domain :Model ;  &#10;&#32;&#32;&#32;&#32;rdfs:range :Dimension .</code></pre>|
|[Section top](#minorfail-outcome-number-65)|Pointer|<pre lang="Turtle"><code>:hasClassification a owl:ObjectProperty ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;has dimension&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:comment &#34;is used to link building components, elements, or other enti...&#34; ;  &#10;&#32;&#32;&#32;&#32;rdfs:domain :Model ;  &#10;&#32;&#32;&#32;&#32;rdfs:range :Classification .</code></pre>|

***
### MinorFail Outcome number 66

[Jump to summary definition](#summary-MinorFail-66)	|	[Previous MinorFail outcome](#minorfail-outcome-number-65)	|	[Next MinorFail outcome](#minorfail-outcome-number-67)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-src-legal-verifier|
|----|----|
|Title|Standalone module src/legal&lowbar;verifier.ttl from branch main|
|Composition|- [Module legal&lowbar;verifier](https://github.com/Accord-Project/aec3po/blob/main/src/legal_verifier.ttl)|

#### Criterion detail
|Identifier|[profile-compatibility](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#profile-compatibility)|
|----|----|
|Title|Profile compatibility test|
|Description|A test meant to check whether the test subject is compatible with a profile or not, and if it is not, why.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-66)|Identifier|`owl-ql-profile-error`|
|[Section top](#minorfail-outcome-number-66)|Title|OWL QL Profile incompatible|
|[Section top](#minorfail-outcome-number-66)|Description|Class Expression not supported with rdfs:subClassOf|
|[Section top](#minorfail-outcome-number-66)|Pointer|<pre lang="Turtle"><code>aec3po:LegalVerifier a owl:Class ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;Legal Verifier&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:comment &#34;An entity that has the legal capacity to verify compliance w...&#34; ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy aec3po:legal&lowbar;verifier ;  &#10;&#32;&#32;&#32;&#32;rdfs:subClassOf &#91; owl:allValuesFrom aec3po:Document ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:onProperty aec3po:forDocument ],  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;foaf:Agent .</code></pre>|

***
### MinorFail Outcome number 67

[Jump to summary definition](#summary-MinorFail-67)	|	[Previous MinorFail outcome](#minorfail-outcome-number-66)	|	[Next MinorFail outcome](#minorfail-outcome-number-68)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-src-legal-verifier|
|----|----|
|Title|Standalone module src/legal&lowbar;verifier.ttl from branch main|
|Composition|- [Module legal&lowbar;verifier](https://github.com/Accord-Project/aec3po/blob/main/src/legal_verifier.ttl)|

#### Criterion detail
|Identifier|[profile-compatibility](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#profile-compatibility)|
|----|----|
|Title|Profile compatibility test|
|Description|A test meant to check whether the test subject is compatible with a profile or not, and if it is not, why.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-67)|Identifier|`owl-ql-profile-error`|
|[Section top](#minorfail-outcome-number-67)|Title|OWL QL Profile incompatible|
|[Section top](#minorfail-outcome-number-67)|Description|Statement not supported in a Super Class Expression|
|[Section top](#minorfail-outcome-number-67)|Pointer|<pre lang="Turtle"><code>&#91;] owl:allValuesFrom aec3po:Document ;  &#10;&#32;&#32;&#32;&#32;owl:onProperty aec3po:forDocument .</code></pre>|

***
### MinorFail Outcome number 68

[Jump to summary definition](#summary-MinorFail-68)	|	[Previous MinorFail outcome](#minorfail-outcome-number-67)	|	[Next MinorFail outcome](#minorfail-outcome-number-69)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-src-legal-verifier|
|----|----|
|Title|Standalone module src/legal&lowbar;verifier.ttl from branch main|
|Composition|- [Module legal&lowbar;verifier](https://github.com/Accord-Project/aec3po/blob/main/src/legal_verifier.ttl)|

#### Criterion detail
|Identifier|[profile-compatibility](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#profile-compatibility)|
|----|----|
|Title|Profile compatibility test|
|Description|A test meant to check whether the test subject is compatible with a profile or not, and if it is not, why.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-68)|Identifier|`owl-el-profile-error`|
|[Section top](#minorfail-outcome-number-68)|Title|OWL EL Profile incompatible|
|[Section top](#minorfail-outcome-number-68)|Description|Statement not supported in a Class Expression|
|[Section top](#minorfail-outcome-number-68)|Pointer|<pre lang="Turtle"><code>&#91;] owl:allValuesFrom aec3po:Document ;  &#10;&#32;&#32;&#32;&#32;owl:onProperty aec3po:forDocument .</code></pre>|

***
### MinorFail Outcome number 69

[Jump to summary definition](#summary-MinorFail-69)	|	[Previous MinorFail outcome](#minorfail-outcome-number-68)	|	[Next MinorFail outcome](#minorfail-outcome-number-70)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-src-legal-verifier|
|----|----|
|Title|Standalone module src/legal&lowbar;verifier.ttl from branch main|
|Composition|- [Module legal&lowbar;verifier](https://github.com/Accord-Project/aec3po/blob/main/src/legal_verifier.ttl)|

#### Criterion detail
|Identifier|[profile-compatibility](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#profile-compatibility)|
|----|----|
|Title|Profile compatibility test|
|Description|A test meant to check whether the test subject is compatible with a profile or not, and if it is not, why.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-69)|Identifier|`owl-el-profile-error`|
|[Section top](#minorfail-outcome-number-69)|Title|OWL EL Profile incompatible|
|[Section top](#minorfail-outcome-number-69)|Description|Class Expression not supported with rdfs:subClassOf|
|[Section top](#minorfail-outcome-number-69)|Pointer|<pre lang="Turtle"><code>aec3po:LegalVerifier a owl:Class ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;Legal Verifier&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:comment &#34;An entity that has the legal capacity to verify compliance w...&#34; ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy aec3po:legal&lowbar;verifier ;  &#10;&#32;&#32;&#32;&#32;rdfs:subClassOf &#91; owl:allValuesFrom aec3po:Document ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:onProperty aec3po:forDocument ],  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;foaf:Agent .</code></pre>|

***
### MinorFail Outcome number 70

[Jump to summary definition](#summary-MinorFail-70)	|	[Previous MinorFail outcome](#minorfail-outcome-number-69)	|	[Next MinorFail outcome](#minorfail-outcome-number-71)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-src-feature-of-interest|
|----|----|
|Title|Standalone module src/feature&lowbar;of&lowbar;interest.ttl from branch main|
|Composition|- [Module feature&lowbar;of&lowbar;interest](https://github.com/Accord-Project/aec3po/blob/main/src/feature_of_interest.ttl)|

#### Criterion detail
|Identifier|[domain-and-range-referencing](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#domain-and-range-referencing)|
|----|----|
|Title|Domain and range referencing test|
|Description|A test case from the Best Practices tests checking if all the ranges and domains from the test subject point to terms that are defined in the vocabulary.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-70)|Identifier|`domain-out-of-vocabulary`|
|[Section top](#minorfail-outcome-number-70)|Title|Domain out of vocabulary|
|[Section top](#minorfail-outcome-number-70)|Description|Some properties have a domain out of the ontology|
|[Section top](#minorfail-outcome-number-70)|Pointer|<pre lang="Turtle"><code>:hasProperty a owl:ObjectProperty ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;has Property&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:comment &#34;Links a feature of interest to one of its aspect that is int...&#34; ;  &#10;&#32;&#32;&#32;&#32;rdfs:domain &#60;http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#Object>,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:Thing,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#60;https://saref.etsi.org/core/FeatureOfInterest>,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;:FeatureOfInterest ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy :feature&lowbar;of&lowbar;interest ;  &#10;&#32;&#32;&#32;&#32;rdfs:range &#60;http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#Quality>,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:Thing,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;:Property ;  &#10;&#32;&#32;&#32;&#32;rdfs:subPropertyOf :hasProperty ;  &#10;&#32;&#32;&#32;&#32;owl:equivalentProperty :hasProperty ;  &#10;&#32;&#32;&#32;&#32;owl:sameAs :hasProperty ;  &#10;&#32;&#32;&#32;&#32;skos:example &#34;Links a space to the area property of that space, a wall to ...&#34; .</code></pre>|
|[Section top](#minorfail-outcome-number-70)|Pointer|<pre lang="Turtle"><code></code></pre>|
|[Section top](#minorfail-outcome-number-70)|Pointer|<pre lang="Turtle"><code>:hasQuantityKind a owl:ObjectProperty ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;has quantity kind&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:comment &#34;Links a property to its quantity kind&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:domain &#60;http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#Quality>,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:Thing,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;:Property ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy :feature&lowbar;of&lowbar;interest ;  &#10;&#32;&#32;&#32;&#32;rdfs:range owl:Thing,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;:QuantityKind ;  &#10;&#32;&#32;&#32;&#32;rdfs:subPropertyOf :hasQuantityKind ;  &#10;&#32;&#32;&#32;&#32;owl:equivalentProperty :hasQuantityKind ;  &#10;&#32;&#32;&#32;&#32;owl:sameAs :hasQuantityKind ;  &#10;&#32;&#32;&#32;&#32;skos:example &#34;A space area property to the property kind &#92;&#34;area&#92;&#34;.&#34;@en .</code></pre>|

***
### MinorFail Outcome number 71

[Jump to summary definition](#summary-MinorFail-71)	|	[Previous MinorFail outcome](#minorfail-outcome-number-70)	|	[Next MinorFail outcome](#minorfail-outcome-number-72)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-src-feature-of-interest|
|----|----|
|Title|Standalone module src/feature&lowbar;of&lowbar;interest.ttl from branch main|
|Composition|- [Module feature&lowbar;of&lowbar;interest](https://github.com/Accord-Project/aec3po/blob/main/src/feature_of_interest.ttl)|

#### Criterion detail
|Identifier|[domain-and-range-referencing](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#domain-and-range-referencing)|
|----|----|
|Title|Domain and range referencing test|
|Description|A test case from the Best Practices tests checking if all the ranges and domains from the test subject point to terms that are defined in the vocabulary.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-71)|Identifier|`range-out-of-vocabulary`|
|[Section top](#minorfail-outcome-number-71)|Title|Range out of vocabulary|
|[Section top](#minorfail-outcome-number-71)|Description|Some properties have a range out of the ontology|
|[Section top](#minorfail-outcome-number-71)|Pointer|<pre lang="Turtle"><code>:hasProperty a owl:ObjectProperty ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;has Property&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:comment &#34;Links a feature of interest to one of its aspect that is int...&#34; ;  &#10;&#32;&#32;&#32;&#32;rdfs:domain &#60;http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#Object>,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:Thing,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#60;https://saref.etsi.org/core/FeatureOfInterest>,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;:FeatureOfInterest ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy :feature&lowbar;of&lowbar;interest ;  &#10;&#32;&#32;&#32;&#32;rdfs:range &#60;http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#Quality>,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:Thing,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;:Property ;  &#10;&#32;&#32;&#32;&#32;rdfs:subPropertyOf :hasProperty ;  &#10;&#32;&#32;&#32;&#32;owl:equivalentProperty :hasProperty ;  &#10;&#32;&#32;&#32;&#32;owl:sameAs :hasProperty ;  &#10;&#32;&#32;&#32;&#32;skos:example &#34;Links a space to the area property of that space, a wall to ...&#34; .</code></pre>|
|[Section top](#minorfail-outcome-number-71)|Pointer|<pre lang="Turtle"><code></code></pre>|

***
### MinorFail Outcome number 72

[Jump to summary definition](#summary-MinorFail-72)	|	[Previous MinorFail outcome](#minorfail-outcome-number-71)	|	[Next MinorFail outcome](#minorfail-outcome-number-73)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-src-evidence|
|----|----|
|Title|Standalone module src/evidence.ttl from branch main|
|Composition|- [Module evidence](https://github.com/Accord-Project/aec3po/blob/main/src/evidence.ttl)|

#### Criterion detail
|Identifier|[domain-and-range-referencing](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#domain-and-range-referencing)|
|----|----|
|Title|Domain and range referencing test|
|Description|A test case from the Best Practices tests checking if all the ranges and domains from the test subject point to terms that are defined in the vocabulary.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-72)|Identifier|`range-out-of-vocabulary`|
|[Section top](#minorfail-outcome-number-72)|Title|Range out of vocabulary|
|[Section top](#minorfail-outcome-number-72)|Description|Some properties have a range out of the ontology|
|[Section top](#minorfail-outcome-number-72)|Pointer|<pre lang="Turtle"><code>:hasFormat a owl:ObjectProperty ;  &#10;&#32;&#32;&#32;&#32;rdfs:comment &#34;Defines the format of an evidence, which is of type dct:form...&#34; ;  &#10;&#32;&#32;&#32;&#32;rdfs:domain :Statement ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy :evidence ;  &#10;&#32;&#32;&#32;&#32;rdfs:range dc:format ;  &#10;&#32;&#32;&#32;&#32;rdfs:subPropertyOf :hasFormat ;  &#10;&#32;&#32;&#32;&#32;owl:equivalentProperty :hasFormat ;  &#10;&#32;&#32;&#32;&#32;owl:sameAs :hasFormat ;  &#10;&#32;&#32;&#32;&#32;skos:example &#34;an image, a drawing or a model can be an evidence.&#34;@en .</code></pre>|
|[Section top](#minorfail-outcome-number-72)|Pointer|http://purl.org/dc/elements/1.1/format|

***
### MinorFail Outcome number 73

[Jump to summary definition](#summary-MinorFail-73)	|	[Previous MinorFail outcome](#minorfail-outcome-number-72)	|	[Next MinorFail outcome](#minorfail-outcome-number-74)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-src-evidence|
|----|----|
|Title|Standalone module src/evidence.ttl from branch main|
|Composition|- [Module evidence](https://github.com/Accord-Project/aec3po/blob/main/src/evidence.ttl)|

#### Criterion detail
|Identifier|[labeled-terms](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#labeled-terms)|
|----|----|
|Title|Term labeling test|
|Description|A test case from the Best Practices tests checking if all the terms of the subject have a rdfs:label property pointing to a literal in English|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-73)|Identifier|`not-labeled-term`|
|[Section top](#minorfail-outcome-number-73)|Title|Terms not labeled|
|[Section top](#minorfail-outcome-number-73)|Description|The following terms have no rdfs:label to define it in natural language|
|[Section top](#minorfail-outcome-number-73)|Pointer|<pre lang="Turtle"><code>:hasEvidence a owl:ObjectProperty ;  &#10;&#32;&#32;&#32;&#32;rdfs:comment &#34;Links a statement to a piece of evidence for that statement ...&#34; ;  &#10;&#32;&#32;&#32;&#32;rdfs:domain :Statement ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy :statement ;  &#10;&#32;&#32;&#32;&#32;skos:note &#34;Unstable. Need evidence of how this property is intended to ...&#34; .</code></pre>|
|[Section top](#minorfail-outcome-number-73)|Pointer|<pre lang="Turtle"><code>:hasFormat a owl:ObjectProperty ;  &#10;&#32;&#32;&#32;&#32;rdfs:comment &#34;Defines the format of an evidence, which is of type dct:form...&#34; ;  &#10;&#32;&#32;&#32;&#32;rdfs:domain :Statement ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy :evidence ;  &#10;&#32;&#32;&#32;&#32;rdfs:range dc:format ;  &#10;&#32;&#32;&#32;&#32;skos:example &#34;an image, a drawing or a model can be an evidence.&#34;@en .</code></pre>|

***
### MinorFail Outcome number 74

[Jump to summary definition](#summary-MinorFail-74)	|	[Previous MinorFail outcome](#minorfail-outcome-number-73)	|	[Next MinorFail outcome](#minorfail-outcome-number-75)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-src-document|
|----|----|
|Title|Standalone module src/document.ttl from branch main|
|Composition|- [Module document](https://github.com/Accord-Project/aec3po/blob/main/src/document.ttl)|

#### Criterion detail
|Identifier|[profile-compatibility](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#profile-compatibility)|
|----|----|
|Title|Profile compatibility test|
|Description|A test meant to check whether the test subject is compatible with a profile or not, and if it is not, why.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-74)|Identifier|`owl-rl-profile-error`|
|[Section top](#minorfail-outcome-number-74)|Title|OWL RL Profile incompatible|
|[Section top](#minorfail-outcome-number-74)|Description|Class Expression not supported as object of rdfs:domain or rdfs:range|
|[Section top](#minorfail-outcome-number-74)|Pointer|<pre lang="Turtle"><code>aec3po:hasFirstSubdivision a owl:FunctionalProperty,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:ObjectProperty ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;has first subdivision&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:comment &#34;Links a document part to the first of its subdivision&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:domain &#91; owl:unionOf ( aec3po:Document aec3po:DocumentSubdivision ) ] ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy aec3po:document ;  &#10;&#32;&#32;&#32;&#32;rdfs:range aec3po:DocumentSubdivision ;  &#10;&#32;&#32;&#32;&#32;rdfs:subPropertyOf aec3po:hasSubdivision .</code></pre>|
|[Section top](#minorfail-outcome-number-74)|Pointer|<pre lang="Turtle"><code>aec3po:hasSubdivision a owl:ObjectProperty ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;has subdivision&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:comment &#34;links a document part to some of its subdivision&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:domain &#91; owl:unionOf ( aec3po:Document aec3po:DocumentSubdivision ) ] ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy aec3po:document ;  &#10;&#32;&#32;&#32;&#32;rdfs:range aec3po:DocumentSubdivision ;  &#10;&#32;&#32;&#32;&#32;rdfs:subPropertyOf dc:hasPart .</code></pre>|

***
### MinorFail Outcome number 75

[Jump to summary definition](#summary-MinorFail-75)	|	[Previous MinorFail outcome](#minorfail-outcome-number-74)	|	[Next MinorFail outcome](#minorfail-outcome-number-76)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-src-document|
|----|----|
|Title|Standalone module src/document.ttl from branch main|
|Composition|- [Module document](https://github.com/Accord-Project/aec3po/blob/main/src/document.ttl)|

#### Criterion detail
|Identifier|[profile-compatibility](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#profile-compatibility)|
|----|----|
|Title|Profile compatibility test|
|Description|A test meant to check whether the test subject is compatible with a profile or not, and if it is not, why.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-75)|Identifier|`owl-rl-profile-error`|
|[Section top](#minorfail-outcome-number-75)|Title|OWL RL Profile incompatible|
|[Section top](#minorfail-outcome-number-75)|Description|Statement not supported in a Super Class Expression|
|[Section top](#minorfail-outcome-number-75)|Pointer|<pre lang="Turtle"><code>&#91;] owl:unionOf ( aec3po:Document aec3po:DocumentSubdivision ) .</code></pre>|

***
### MinorFail Outcome number 76

[Jump to summary definition](#summary-MinorFail-76)	|	[Previous MinorFail outcome](#minorfail-outcome-number-75)	|	[Next MinorFail outcome](#minorfail-outcome-number-77)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-src-document|
|----|----|
|Title|Standalone module src/document.ttl from branch main|
|Composition|- [Module document](https://github.com/Accord-Project/aec3po/blob/main/src/document.ttl)|

#### Criterion detail
|Identifier|[profile-compatibility](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#profile-compatibility)|
|----|----|
|Title|Profile compatibility test|
|Description|A test meant to check whether the test subject is compatible with a profile or not, and if it is not, why.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-76)|Identifier|`owl-ql-profile-error`|
|[Section top](#minorfail-outcome-number-76)|Title|OWL QL Profile incompatible|
|[Section top](#minorfail-outcome-number-76)|Description|Class Expression not supported as object of rdfs:domain or rdfs:range|
|[Section top](#minorfail-outcome-number-76)|Pointer|<pre lang="Turtle"><code>aec3po:hasFirstSubdivision a owl:FunctionalProperty,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:ObjectProperty ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;has first subdivision&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:comment &#34;Links a document part to the first of its subdivision&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:domain &#91; owl:unionOf ( aec3po:Document aec3po:DocumentSubdivision ) ] ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy aec3po:document ;  &#10;&#32;&#32;&#32;&#32;rdfs:range aec3po:DocumentSubdivision ;  &#10;&#32;&#32;&#32;&#32;rdfs:subPropertyOf aec3po:hasSubdivision .</code></pre>|
|[Section top](#minorfail-outcome-number-76)|Pointer|<pre lang="Turtle"><code>aec3po:hasSubdivision a owl:ObjectProperty ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;has subdivision&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:comment &#34;links a document part to some of its subdivision&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:domain &#91; owl:unionOf ( aec3po:Document aec3po:DocumentSubdivision ) ] ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy aec3po:document ;  &#10;&#32;&#32;&#32;&#32;rdfs:range aec3po:DocumentSubdivision ;  &#10;&#32;&#32;&#32;&#32;rdfs:subPropertyOf dc:hasPart .</code></pre>|

***
### MinorFail Outcome number 77

[Jump to summary definition](#summary-MinorFail-77)	|	[Previous MinorFail outcome](#minorfail-outcome-number-76)	|	[Next MinorFail outcome](#minorfail-outcome-number-78)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-src-document|
|----|----|
|Title|Standalone module src/document.ttl from branch main|
|Composition|- [Module document](https://github.com/Accord-Project/aec3po/blob/main/src/document.ttl)|

#### Criterion detail
|Identifier|[profile-compatibility](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#profile-compatibility)|
|----|----|
|Title|Profile compatibility test|
|Description|A test meant to check whether the test subject is compatible with a profile or not, and if it is not, why.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-77)|Identifier|`owl-ql-profile-error`|
|[Section top](#minorfail-outcome-number-77)|Title|OWL QL Profile incompatible|
|[Section top](#minorfail-outcome-number-77)|Description|Class Expression not supported with rdfs:subClassOf|
|[Section top](#minorfail-outcome-number-77)|Pointer|<pre lang="Turtle"><code>aec3po:DocumentSubdivision a owl:Class ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;Document Subdivision&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:comment &#34;Any subdivision of a document, including sections, paragraph...&#34; ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy aec3po:document ;  &#10;&#32;&#32;&#32;&#32;rdfs:subClassOf &#91; a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:allValuesFrom aec3po:DocumentSubdivision ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:onProperty aec3po:hasSubdivision ] ;  &#10;&#32;&#32;&#32;&#32;skos:example &#34;Paragraph, section, definition...&#34;@en .</code></pre>|

***
### MinorFail Outcome number 78

[Jump to summary definition](#summary-MinorFail-78)	|	[Previous MinorFail outcome](#minorfail-outcome-number-77)	|	[Next MinorFail outcome](#minorfail-outcome-number-79)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-src-document|
|----|----|
|Title|Standalone module src/document.ttl from branch main|
|Composition|- [Module document](https://github.com/Accord-Project/aec3po/blob/main/src/document.ttl)|

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
|[Section top](#minorfail-outcome-number-78)|Description|Statement not supported in a Super Class Expression|
|[Section top](#minorfail-outcome-number-78)|Pointer|<pre lang="Turtle"><code>&#91;] a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;owl:allValuesFrom aec3po:DocumentSubdivision ;  &#10;&#32;&#32;&#32;&#32;owl:onProperty aec3po:hasSubdivision .</code></pre>|
|[Section top](#minorfail-outcome-number-78)|Pointer|<pre lang="Turtle"><code>&#91;] owl:unionOf ( aec3po:Document aec3po:DocumentSubdivision ) .</code></pre>|

***
### MinorFail Outcome number 79

[Jump to summary definition](#summary-MinorFail-79)	|	[Previous MinorFail outcome](#minorfail-outcome-number-78)	|	[Next MinorFail outcome](#minorfail-outcome-number-80)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-src-document|
|----|----|
|Title|Standalone module src/document.ttl from branch main|
|Composition|- [Module document](https://github.com/Accord-Project/aec3po/blob/main/src/document.ttl)|

#### Criterion detail
|Identifier|[profile-compatibility](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#profile-compatibility)|
|----|----|
|Title|Profile compatibility test|
|Description|A test meant to check whether the test subject is compatible with a profile or not, and if it is not, why.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-79)|Identifier|`owl-el-profile-error`|
|[Section top](#minorfail-outcome-number-79)|Title|OWL EL Profile incompatible|
|[Section top](#minorfail-outcome-number-79)|Description|Statement not supported in a Class Expression|
|[Section top](#minorfail-outcome-number-79)|Pointer|<pre lang="Turtle"><code>&#91;] a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;owl:allValuesFrom aec3po:DocumentSubdivision ;  &#10;&#32;&#32;&#32;&#32;owl:onProperty aec3po:hasSubdivision .</code></pre>|
|[Section top](#minorfail-outcome-number-79)|Pointer|<pre lang="Turtle"><code>&#91;] owl:unionOf ( aec3po:Document aec3po:DocumentSubdivision ) .</code></pre>|

***
### MinorFail Outcome number 80

[Jump to summary definition](#summary-MinorFail-80)	|	[Previous MinorFail outcome](#minorfail-outcome-number-79)	|	[Next MinorFail outcome](#minorfail-outcome-number-81)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-src-document|
|----|----|
|Title|Standalone module src/document.ttl from branch main|
|Composition|- [Module document](https://github.com/Accord-Project/aec3po/blob/main/src/document.ttl)|

#### Criterion detail
|Identifier|[profile-compatibility](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#profile-compatibility)|
|----|----|
|Title|Profile compatibility test|
|Description|A test meant to check whether the test subject is compatible with a profile or not, and if it is not, why.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-80)|Identifier|`owl-el-profile-error`|
|[Section top](#minorfail-outcome-number-80)|Title|OWL EL Profile incompatible|
|[Section top](#minorfail-outcome-number-80)|Description|Class Expression not supported with rdfs:subClassOf|
|[Section top](#minorfail-outcome-number-80)|Pointer|<pre lang="Turtle"><code>aec3po:DocumentSubdivision a owl:Class ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;Document Subdivision&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:comment &#34;Any subdivision of a document, including sections, paragraph...&#34; ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy aec3po:document ;  &#10;&#32;&#32;&#32;&#32;rdfs:subClassOf &#91; a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:allValuesFrom aec3po:DocumentSubdivision ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:onProperty aec3po:hasSubdivision ] ;  &#10;&#32;&#32;&#32;&#32;skos:example &#34;Paragraph, section, definition...&#34;@en .</code></pre>|

***
### MinorFail Outcome number 81

[Jump to summary definition](#summary-MinorFail-81)	|	[Previous MinorFail outcome](#minorfail-outcome-number-80)	|	[Next MinorFail outcome](#minorfail-outcome-number-82)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-src-document|
|----|----|
|Title|Standalone module src/document.ttl from branch main|
|Composition|- [Module document](https://github.com/Accord-Project/aec3po/blob/main/src/document.ttl)|

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
|[Section top](#minorfail-outcome-number-81)|Description|Class Expression not supported as object of rdfs:domain or rdfs:range|
|[Section top](#minorfail-outcome-number-81)|Pointer|<pre lang="Turtle"><code>aec3po:hasFirstSubdivision a owl:FunctionalProperty,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:ObjectProperty ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;has first subdivision&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:comment &#34;Links a document part to the first of its subdivision&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:domain &#91; owl:unionOf ( aec3po:Document aec3po:DocumentSubdivision ) ] ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy aec3po:document ;  &#10;&#32;&#32;&#32;&#32;rdfs:range aec3po:DocumentSubdivision ;  &#10;&#32;&#32;&#32;&#32;rdfs:subPropertyOf aec3po:hasSubdivision .</code></pre>|
|[Section top](#minorfail-outcome-number-81)|Pointer|<pre lang="Turtle"><code>aec3po:hasSubdivision a owl:ObjectProperty ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;has subdivision&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:comment &#34;links a document part to some of its subdivision&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:domain &#91; owl:unionOf ( aec3po:Document aec3po:DocumentSubdivision ) ] ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy aec3po:document ;  &#10;&#32;&#32;&#32;&#32;rdfs:range aec3po:DocumentSubdivision ;  &#10;&#32;&#32;&#32;&#32;rdfs:subPropertyOf dc:hasPart .</code></pre>|

***
### MinorFail Outcome number 82

[Jump to summary definition](#summary-MinorFail-82)	|	[Previous MinorFail outcome](#minorfail-outcome-number-81)	|	[Next MinorFail outcome](#minorfail-outcome-number-83)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-src-compliance-verification-report|
|----|----|
|Title|Standalone module src/compliance&lowbar;verification&lowbar;report.ttl from branch main|
|Composition|- [Module compliance&lowbar;verification&lowbar;report](https://github.com/Accord-Project/aec3po/blob/main/src/compliance_verification_report.ttl)|

#### Criterion detail
|Identifier|[profile-compatibility](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#profile-compatibility)|
|----|----|
|Title|Profile compatibility test|
|Description|A test meant to check whether the test subject is compatible with a profile or not, and if it is not, why.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-82)|Identifier|`owl-rl-profile-error`|
|[Section top](#minorfail-outcome-number-82)|Title|OWL RL Profile incompatible|
|[Section top](#minorfail-outcome-number-82)|Description|Class Expression not supported with rdfs:subClassOf|
|[Section top](#minorfail-outcome-number-82)|Pointer|<pre lang="Turtle"><code>aec3po:ComplianceVerificationReport a owl:Class ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;Compliance Verification Report&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:comment &#34;Result of a checking act. May be compliant or not.&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy aec3po:compliance&lowbar;verification&lowbar;report ;  &#10;&#32;&#32;&#32;&#32;rdfs:subClassOf &#91; a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:onProperty aec3po:conforms ] .</code></pre>|
|[Section top](#minorfail-outcome-number-82)|Pointer|<pre lang="Turtle"><code>aec3po:VerificationResult a owl:Class ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;Verification Result&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:comment &#34;Individual verification result of a Compliance Verification ...&#34; ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy aec3po:compliance&lowbar;verification&lowbar;report ;  &#10;&#32;&#32;&#32;&#32;rdfs:subClassOf &#91; a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:onProperty aec3po:verificationFocus ],  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#91; a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:onProperty aec3po:hasSeverity ] .</code></pre>|

***
### MinorFail Outcome number 83

[Jump to summary definition](#summary-MinorFail-83)	|	[Previous MinorFail outcome](#minorfail-outcome-number-82)	|	[Next MinorFail outcome](#minorfail-outcome-number-84)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-src-compliance-verification-report|
|----|----|
|Title|Standalone module src/compliance&lowbar;verification&lowbar;report.ttl from branch main|
|Composition|- [Module compliance&lowbar;verification&lowbar;report](https://github.com/Accord-Project/aec3po/blob/main/src/compliance_verification_report.ttl)|

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
|[Section top](#minorfail-outcome-number-83)|Description|Statement not supported in a Super Class Expression|
|[Section top](#minorfail-outcome-number-83)|Pointer|<pre lang="Turtle"><code>&#91;] a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;owl:onProperty aec3po:conforms .</code></pre>|
|[Section top](#minorfail-outcome-number-83)|Pointer|<pre lang="Turtle"><code>&#91;] a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;owl:onProperty aec3po:verificationFocus .</code></pre>|
|[Section top](#minorfail-outcome-number-83)|Pointer|<pre lang="Turtle"><code>&#91;] a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;owl:onProperty aec3po:hasSeverity .</code></pre>|

***
### MinorFail Outcome number 84

[Jump to summary definition](#summary-MinorFail-84)	|	[Previous MinorFail outcome](#minorfail-outcome-number-83)	|	[Next MinorFail outcome](#minorfail-outcome-number-85)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-src-compliance-verification-report|
|----|----|
|Title|Standalone module src/compliance&lowbar;verification&lowbar;report.ttl from branch main|
|Composition|- [Module compliance&lowbar;verification&lowbar;report](https://github.com/Accord-Project/aec3po/blob/main/src/compliance_verification_report.ttl)|

#### Criterion detail
|Identifier|[profile-compatibility](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#profile-compatibility)|
|----|----|
|Title|Profile compatibility test|
|Description|A test meant to check whether the test subject is compatible with a profile or not, and if it is not, why.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-84)|Identifier|`owl-ql-profile-error`|
|[Section top](#minorfail-outcome-number-84)|Title|OWL QL Profile incompatible|
|[Section top](#minorfail-outcome-number-84)|Description|Class Expression not supported with rdfs:subClassOf|
|[Section top](#minorfail-outcome-number-84)|Pointer|<pre lang="Turtle"><code>aec3po:ComplianceVerificationReport a owl:Class ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;Compliance Verification Report&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:comment &#34;Result of a checking act. May be compliant or not.&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy aec3po:compliance&lowbar;verification&lowbar;report ;  &#10;&#32;&#32;&#32;&#32;rdfs:subClassOf &#91; a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:onProperty aec3po:conforms ] .</code></pre>|
|[Section top](#minorfail-outcome-number-84)|Pointer|<pre lang="Turtle"><code>aec3po:VerificationResult a owl:Class ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;Verification Result&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:comment &#34;Individual verification result of a Compliance Verification ...&#34; ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy aec3po:compliance&lowbar;verification&lowbar;report ;  &#10;&#32;&#32;&#32;&#32;rdfs:subClassOf &#91; a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:onProperty aec3po:verificationFocus ],  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#91; a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:onProperty aec3po:hasSeverity ] .</code></pre>|

***
### MinorFail Outcome number 85

[Jump to summary definition](#summary-MinorFail-85)	|	[Previous MinorFail outcome](#minorfail-outcome-number-84)	|	[Next MinorFail outcome](#minorfail-outcome-number-86)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-src-compliance-verification-report|
|----|----|
|Title|Standalone module src/compliance&lowbar;verification&lowbar;report.ttl from branch main|
|Composition|- [Module compliance&lowbar;verification&lowbar;report](https://github.com/Accord-Project/aec3po/blob/main/src/compliance_verification_report.ttl)|

#### Criterion detail
|Identifier|[profile-compatibility](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#profile-compatibility)|
|----|----|
|Title|Profile compatibility test|
|Description|A test meant to check whether the test subject is compatible with a profile or not, and if it is not, why.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-85)|Identifier|`owl-ql-profile-error`|
|[Section top](#minorfail-outcome-number-85)|Title|OWL QL Profile incompatible|
|[Section top](#minorfail-outcome-number-85)|Description|Restriction on datatypes|
|[Section top](#minorfail-outcome-number-85)|Pointer|<pre lang="Turtle"><code>aec3po:conforms a owl:DatatypeProperty ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;conforms&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:comment &#34;True if the Checking act confirms the check was validated, a...&#34; ;  &#10;&#32;&#32;&#32;&#32;rdfs:domain aec3po:ComplianceVerificationReport ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy aec3po:compliance&lowbar;verification&lowbar;report ;  &#10;&#32;&#32;&#32;&#32;rdfs:range xsd:boolean .</code></pre>|

***
### MinorFail Outcome number 86

[Jump to summary definition](#summary-MinorFail-86)	|	[Previous MinorFail outcome](#minorfail-outcome-number-85)	|	[Next MinorFail outcome](#minorfail-outcome-number-87)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-src-compliance-verification-report|
|----|----|
|Title|Standalone module src/compliance&lowbar;verification&lowbar;report.ttl from branch main|
|Composition|- [Module compliance&lowbar;verification&lowbar;report](https://github.com/Accord-Project/aec3po/blob/main/src/compliance_verification_report.ttl)|

#### Criterion detail
|Identifier|[profile-compatibility](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#profile-compatibility)|
|----|----|
|Title|Profile compatibility test|
|Description|A test meant to check whether the test subject is compatible with a profile or not, and if it is not, why.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-86)|Identifier|`owl-ql-profile-error`|
|[Section top](#minorfail-outcome-number-86)|Title|OWL QL Profile incompatible|
|[Section top](#minorfail-outcome-number-86)|Description|Statement not supported in a Super Class Expression|
|[Section top](#minorfail-outcome-number-86)|Pointer|<pre lang="Turtle"><code>&#91;] a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;owl:onProperty aec3po:conforms .</code></pre>|
|[Section top](#minorfail-outcome-number-86)|Pointer|<pre lang="Turtle"><code>&#91;] a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;owl:onProperty aec3po:verificationFocus .</code></pre>|
|[Section top](#minorfail-outcome-number-86)|Pointer|<pre lang="Turtle"><code>&#91;] a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;owl:onProperty aec3po:hasSeverity .</code></pre>|

***
### MinorFail Outcome number 87

[Jump to summary definition](#summary-MinorFail-87)	|	[Previous MinorFail outcome](#minorfail-outcome-number-86)	|	[Next MinorFail outcome](#minorfail-outcome-number-88)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-src-compliance-verification-report|
|----|----|
|Title|Standalone module src/compliance&lowbar;verification&lowbar;report.ttl from branch main|
|Composition|- [Module compliance&lowbar;verification&lowbar;report](https://github.com/Accord-Project/aec3po/blob/main/src/compliance_verification_report.ttl)|

#### Criterion detail
|Identifier|[profile-compatibility](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#profile-compatibility)|
|----|----|
|Title|Profile compatibility test|
|Description|A test meant to check whether the test subject is compatible with a profile or not, and if it is not, why.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-87)|Identifier|`owl-el-profile-error`|
|[Section top](#minorfail-outcome-number-87)|Title|OWL EL Profile incompatible|
|[Section top](#minorfail-outcome-number-87)|Description|Statement not supported in a Class Expression|
|[Section top](#minorfail-outcome-number-87)|Pointer|<pre lang="Turtle"><code>&#91;] a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;owl:onProperty aec3po:conforms .</code></pre>|
|[Section top](#minorfail-outcome-number-87)|Pointer|<pre lang="Turtle"><code>&#91;] a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;owl:onProperty aec3po:verificationFocus .</code></pre>|
|[Section top](#minorfail-outcome-number-87)|Pointer|<pre lang="Turtle"><code>&#91;] a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;owl:onProperty aec3po:hasSeverity .</code></pre>|

***
### MinorFail Outcome number 88

[Jump to summary definition](#summary-MinorFail-88)	|	[Previous MinorFail outcome](#minorfail-outcome-number-87)	|	[Next MinorFail outcome](#minorfail-outcome-number-89)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-src-compliance-verification-report|
|----|----|
|Title|Standalone module src/compliance&lowbar;verification&lowbar;report.ttl from branch main|
|Composition|- [Module compliance&lowbar;verification&lowbar;report](https://github.com/Accord-Project/aec3po/blob/main/src/compliance_verification_report.ttl)|

#### Criterion detail
|Identifier|[profile-compatibility](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#profile-compatibility)|
|----|----|
|Title|Profile compatibility test|
|Description|A test meant to check whether the test subject is compatible with a profile or not, and if it is not, why.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-88)|Identifier|`owl-el-profile-error`|
|[Section top](#minorfail-outcome-number-88)|Title|OWL EL Profile incompatible|
|[Section top](#minorfail-outcome-number-88)|Description|Class Expression not supported with rdfs:subClassOf|
|[Section top](#minorfail-outcome-number-88)|Pointer|<pre lang="Turtle"><code>aec3po:ComplianceVerificationReport a owl:Class ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;Compliance Verification Report&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:comment &#34;Result of a checking act. May be compliant or not.&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy aec3po:compliance&lowbar;verification&lowbar;report ;  &#10;&#32;&#32;&#32;&#32;rdfs:subClassOf &#91; a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:onProperty aec3po:conforms ] .</code></pre>|
|[Section top](#minorfail-outcome-number-88)|Pointer|<pre lang="Turtle"><code>aec3po:VerificationResult a owl:Class ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;Verification Result&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:comment &#34;Individual verification result of a Compliance Verification ...&#34; ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy aec3po:compliance&lowbar;verification&lowbar;report ;  &#10;&#32;&#32;&#32;&#32;rdfs:subClassOf &#91; a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:onProperty aec3po:verificationFocus ],  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#91; a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:onProperty aec3po:hasSeverity ] .</code></pre>|

***
### MinorFail Outcome number 89

[Jump to summary definition](#summary-MinorFail-89)	|	[Previous MinorFail outcome](#minorfail-outcome-number-88)	|	[Next MinorFail outcome](#minorfail-outcome-number-90)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-src-compliance-verification-report|
|----|----|
|Title|Standalone module src/compliance&lowbar;verification&lowbar;report.ttl from branch main|
|Composition|- [Module compliance&lowbar;verification&lowbar;report](https://github.com/Accord-Project/aec3po/blob/main/src/compliance_verification_report.ttl)|

#### Criterion detail
|Identifier|[profile-compatibility](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#profile-compatibility)|
|----|----|
|Title|Profile compatibility test|
|Description|A test meant to check whether the test subject is compatible with a profile or not, and if it is not, why.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-89)|Identifier|`owl-el-profile-error`|
|[Section top](#minorfail-outcome-number-89)|Title|OWL EL Profile incompatible|
|[Section top](#minorfail-outcome-number-89)|Description|Restriction on datatypes|
|[Section top](#minorfail-outcome-number-89)|Pointer|<pre lang="Turtle"><code>aec3po:conforms a owl:DatatypeProperty ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;conforms&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:comment &#34;True if the Checking act confirms the check was validated, a...&#34; ;  &#10;&#32;&#32;&#32;&#32;rdfs:domain aec3po:ComplianceVerificationReport ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy aec3po:compliance&lowbar;verification&lowbar;report ;  &#10;&#32;&#32;&#32;&#32;rdfs:range xsd:boolean .</code></pre>|

***
### MinorFail Outcome number 90

[Jump to summary definition](#summary-MinorFail-90)	|	[Previous MinorFail outcome](#minorfail-outcome-number-89)	|	[Next MinorFail outcome](#minorfail-outcome-number-91)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-src-compliance-verification-report|
|----|----|
|Title|Standalone module src/compliance&lowbar;verification&lowbar;report.ttl from branch main|
|Composition|- [Module compliance&lowbar;verification&lowbar;report](https://github.com/Accord-Project/aec3po/blob/main/src/compliance_verification_report.ttl)|

#### Criterion detail
|Identifier|[terms-differenciation](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#terms-differenciation)|
|----|----|
|Title|Terms differenciation test|
|Description|A test case from the Best Practices tests checking if all the terms are different enough from each other according to the Levenshtein distance metric.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-90)|Identifier|`too-close-terms`|
|[Section top](#minorfail-outcome-number-90)|Title|Too close terms|
|[Section top](#minorfail-outcome-number-90)|Description|Some terms are too similar|
|[Section top](#minorfail-outcome-number-90)|Pointer|<pre lang="Turtle"><code>:severity a owl:ObjectProperty ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;severity&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:comment &#34;Each verification result has exactly one value for the prope...&#34; ;  &#10;&#32;&#32;&#32;&#32;rdfs:domain :VerificationResult ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy :compliance&lowbar;verification&lowbar;report ;  &#10;&#32;&#32;&#32;&#32;rdfs:range :Severity .</code></pre>|
|[Section top](#minorfail-outcome-number-90)|Pointer|<pre lang="Turtle"><code>:Severity a owl:Class ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;Severity&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:comment &#34;The class of validation result severity levels, including vi...&#34; ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy :compliance&lowbar;verification&lowbar;report .</code></pre>|

***
### MinorFail Outcome number 91

[Jump to summary definition](#summary-MinorFail-91)	|	[Previous MinorFail outcome](#minorfail-outcome-number-90)	|	[Next MinorFail outcome](#minorfail-outcome-number-92)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-src-checking-act|
|----|----|
|Title|Standalone module src/checking&lowbar;act.ttl from branch main|
|Composition|- [Module checking&lowbar;act](https://github.com/Accord-Project/aec3po/blob/main/src/checking_act.ttl)|

#### Criterion detail
|Identifier|[domain-and-range-referencing](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#domain-and-range-referencing)|
|----|----|
|Title|Domain and range referencing test|
|Description|A test case from the Best Practices tests checking if all the ranges and domains from the test subject point to terms that are defined in the vocabulary.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-91)|Identifier|`domain-out-of-vocabulary`|
|[Section top](#minorfail-outcome-number-91)|Title|Domain out of vocabulary|
|[Section top](#minorfail-outcome-number-91)|Description|Some properties have a domain out of the ontology|
|[Section top](#minorfail-outcome-number-91)|Pointer|<pre lang="Turtle"><code>:usedMethod a owl:ObjectProperty ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;used method&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:comment &#34;Links a checking act to the method it used (a aec3po:CheckMe...&#34; ;  &#10;&#32;&#32;&#32;&#32;rdfs:domain &#91; a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:onProperty :usedMethod ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:someValuesFrom :CheckMethod ],  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#91; a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:onProperty :madeBy ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:someValuesFrom :ProcessVerifier ],  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#91; a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:onProperty :checked ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:someValuesFrom owl:Thing ],  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#91; a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:onProperty :hasReport ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:someValuesFrom :ComplianceVerificationReport ],  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#60;http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#Event>,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:Thing,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;:CheckingAct ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy :checking&lowbar;act ;  &#10;&#32;&#32;&#32;&#32;rdfs:range :CheckMethod ;  &#10;&#32;&#32;&#32;&#32;rdfs:subPropertyOf :usedMethod ;  &#10;&#32;&#32;&#32;&#32;owl:equivalentProperty :usedMethod .</code></pre>|
|[Section top](#minorfail-outcome-number-91)|Pointer|<pre lang="Turtle"><code></code></pre>|
|[Section top](#minorfail-outcome-number-91)|Pointer|<pre lang="Turtle"><code>:madeBy a owl:ObjectProperty ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;made by&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:comment &#34;Links a checking act to the process verifier that made it (a...&#34; ;  &#10;&#32;&#32;&#32;&#32;rdfs:domain &#91; a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:onProperty :usedMethod ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:someValuesFrom :CheckMethod ],  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#91; a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:onProperty :madeBy ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:someValuesFrom :ProcessVerifier ],  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#91; a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:onProperty :checked ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:someValuesFrom owl:Thing ],  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#91; a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:onProperty :hasReport ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:someValuesFrom :ComplianceVerificationReport ],  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#60;http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#Event>,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:Thing,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;:CheckingAct ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy :checking&lowbar;act ;  &#10;&#32;&#32;&#32;&#32;rdfs:range :ProcessVerifier ;  &#10;&#32;&#32;&#32;&#32;rdfs:subPropertyOf :madeBy ;  &#10;&#32;&#32;&#32;&#32;owl:equivalentProperty :madeBy .</code></pre>|
|[Section top](#minorfail-outcome-number-91)|Pointer|<pre lang="Turtle"><code>:checked a owl:ObjectProperty ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;checked&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:comment &#34;Links a checking act to some entity (ex. statement, feature ...&#34; ;  &#10;&#32;&#32;&#32;&#32;rdfs:domain &#91; a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:onProperty :usedMethod ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:someValuesFrom :CheckMethod ],  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#91; a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:onProperty :madeBy ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:someValuesFrom :ProcessVerifier ],  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#91; a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:onProperty :checked ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:someValuesFrom owl:Thing ],  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#91; a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:onProperty :hasReport ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:someValuesFrom :ComplianceVerificationReport ],  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#60;http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#Event>,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:Thing,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;:CheckingAct ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy :checking&lowbar;act ;  &#10;&#32;&#32;&#32;&#32;rdfs:subPropertyOf :checked ;  &#10;&#32;&#32;&#32;&#32;owl:equivalentProperty :checked .</code></pre>|
|[Section top](#minorfail-outcome-number-91)|Pointer|<pre lang="Turtle"><code>:hasReport a owl:ObjectProperty ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;has report&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:comment &#34;Links a checking act to the resulting compliance verificatio...&#34; ;  &#10;&#32;&#32;&#32;&#32;rdfs:domain &#91; a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:onProperty :usedMethod ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:someValuesFrom :CheckMethod ],  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#91; a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:onProperty :madeBy ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:someValuesFrom :ProcessVerifier ],  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#91; a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:onProperty :checked ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:someValuesFrom owl:Thing ],  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#91; a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:onProperty :hasReport ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:someValuesFrom :ComplianceVerificationReport ],  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#60;http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#Event>,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:Thing,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;:CheckingAct ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy :checking&lowbar;act ;  &#10;&#32;&#32;&#32;&#32;rdfs:range :ComplianceVerificationReport ;  &#10;&#32;&#32;&#32;&#32;rdfs:subPropertyOf :hasReport ;  &#10;&#32;&#32;&#32;&#32;owl:equivalentProperty :hasReport .</code></pre>|

***
### MinorFail Outcome number 92

[Jump to summary definition](#summary-MinorFail-92)	|	[Previous MinorFail outcome](#minorfail-outcome-number-91)	|	[Next MinorFail outcome](#minorfail-outcome-number-93)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-src-checking-act|
|----|----|
|Title|Standalone module src/checking&lowbar;act.ttl from branch main|
|Composition|- [Module checking&lowbar;act](https://github.com/Accord-Project/aec3po/blob/main/src/checking_act.ttl)|

#### Criterion detail
|Identifier|[profile-compatibility](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#profile-compatibility)|
|----|----|
|Title|Profile compatibility test|
|Description|A test meant to check whether the test subject is compatible with a profile or not, and if it is not, why.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-92)|Identifier|`owl-rl-profile-error`|
|[Section top](#minorfail-outcome-number-92)|Title|OWL RL Profile incompatible|
|[Section top](#minorfail-outcome-number-92)|Description|Class Expression not supported with rdfs:subClassOf|
|[Section top](#minorfail-outcome-number-92)|Pointer|<pre lang="Turtle"><code>aec3po:CheckingAct a owl:Class ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;Checking Act&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:comment &#34;Act of checking some entities for something and generating a...&#34; ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy aec3po:checking&lowbar;act ;  &#10;&#32;&#32;&#32;&#32;rdfs:subClassOf &#91; a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:onProperty aec3po:usedMethod ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:someValuesFrom aec3po:CheckMethod ],  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#91; a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:onProperty aec3po:madeBy ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:someValuesFrom aec3po:ProcessVerifier ],  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#91; a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:onProperty aec3po:checked ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:someValuesFrom owl:Thing ],  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#91; a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:onProperty aec3po:hasReport ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:someValuesFrom aec3po:ComplianceVerificationReport ],  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#60;http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#Event> .</code></pre>|

***
### MinorFail Outcome number 93

[Jump to summary definition](#summary-MinorFail-93)	|	[Previous MinorFail outcome](#minorfail-outcome-number-92)	|	[Next MinorFail outcome](#minorfail-outcome-number-94)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-src-checking-act|
|----|----|
|Title|Standalone module src/checking&lowbar;act.ttl from branch main|
|Composition|- [Module checking&lowbar;act](https://github.com/Accord-Project/aec3po/blob/main/src/checking_act.ttl)|

#### Criterion detail
|Identifier|[profile-compatibility](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#profile-compatibility)|
|----|----|
|Title|Profile compatibility test|
|Description|A test meant to check whether the test subject is compatible with a profile or not, and if it is not, why.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-93)|Identifier|`owl-rl-profile-error`|
|[Section top](#minorfail-outcome-number-93)|Title|OWL RL Profile incompatible|
|[Section top](#minorfail-outcome-number-93)|Description|Statement not supported in a Super Class Expression|
|[Section top](#minorfail-outcome-number-93)|Pointer|<pre lang="Turtle"><code>&#91;] a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;owl:onProperty aec3po:usedMethod ;  &#10;&#32;&#32;&#32;&#32;owl:someValuesFrom aec3po:CheckMethod .</code></pre>|
|[Section top](#minorfail-outcome-number-93)|Pointer|<pre lang="Turtle"><code>&#91;] a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;owl:onProperty aec3po:madeBy ;  &#10;&#32;&#32;&#32;&#32;owl:someValuesFrom aec3po:ProcessVerifier .</code></pre>|
|[Section top](#minorfail-outcome-number-93)|Pointer|<pre lang="Turtle"><code>&#91;] a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;owl:onProperty aec3po:checked ;  &#10;&#32;&#32;&#32;&#32;owl:someValuesFrom owl:Thing .</code></pre>|
|[Section top](#minorfail-outcome-number-93)|Pointer|<pre lang="Turtle"><code>&#91;] a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;owl:onProperty aec3po:hasReport ;  &#10;&#32;&#32;&#32;&#32;owl:someValuesFrom aec3po:ComplianceVerificationReport .</code></pre>|

***
### MinorFail Outcome number 94

[Jump to summary definition](#summary-MinorFail-94)	|	[Previous MinorFail outcome](#minorfail-outcome-number-93)	|	[Next MinorFail outcome](#minorfail-outcome-number-95)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-src-check-method|
|----|----|
|Title|Standalone module src/check&lowbar;method.ttl from branch main|
|Composition|- [Module check&lowbar;method](https://github.com/Accord-Project/aec3po/blob/main/src/check_method.ttl)|

#### Criterion detail
|Identifier|[domain-and-range-referencing](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#domain-and-range-referencing)|
|----|----|
|Title|Domain and range referencing test|
|Description|A test case from the Best Practices tests checking if all the ranges and domains from the test subject point to terms that are defined in the vocabulary.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-94)|Identifier|`domain-out-of-vocabulary`|
|[Section top](#minorfail-outcome-number-94)|Title|Domain out of vocabulary|
|[Section top](#minorfail-outcome-number-94)|Description|Some properties have a domain out of the ontology|
|[Section top](#minorfail-outcome-number-94)|Pointer|<pre lang="Turtle"><code>:operationalizes a owl:ObjectProperty ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;operationalizes&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:comment &#34;Links a check method to a check statement in a document that...&#34; ;  &#10;&#32;&#32;&#32;&#32;rdfs:domain &lowbar;:ne936ad0d81da4f9f9785d7ac9cf30a47b1,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#60;http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#Method>,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:Thing,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;:CheckMethod ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy :check&lowbar;method ;  &#10;&#32;&#32;&#32;&#32;rdfs:range :CheckStatement ;  &#10;&#32;&#32;&#32;&#32;rdfs:subPropertyOf :operationalizes ;  &#10;&#32;&#32;&#32;&#32;owl:equivalentProperty :operationalizes ;  &#10;&#32;&#32;&#32;&#32;owl:inverseOf :isOperationalizedBy .  &#10;&lowbar;:ne936ad0d81da4f9f9785d7ac9cf30a47b2 rdf:first :CheckMethod ;  &#10;&#32;&#32;&#32;&#32;rdf:rest () .  &#10;&lowbar;:ne936ad0d81da4f9f9785d7ac9cf30a47b3 rdf:first :Property ;  &#10;&#32;&#32;&#32;&#32;rdf:rest &lowbar;:ne936ad0d81da4f9f9785d7ac9cf30a47b2 .  &#10;&lowbar;:ne936ad0d81da4f9f9785d7ac9cf30a47b4 rdf:first :FeatureOfInterest ;  &#10;&#32;&#32;&#32;&#32;rdf:rest &lowbar;:ne936ad0d81da4f9f9785d7ac9cf30a47b3 .  &#10;&lowbar;:ne936ad0d81da4f9f9785d7ac9cf30a47b1 a owl:Class ;  &#10;&#32;&#32;&#32;&#32;rdfs:subClassOf &lowbar;:ne936ad0d81da4f9f9785d7ac9cf30a47b1,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:Thing ;  &#10;&#32;&#32;&#32;&#32;owl:equivalentClass &lowbar;:ne936ad0d81da4f9f9785d7ac9cf30a47b1 ;  &#10;&#32;&#32;&#32;&#32;owl:unionOf &lowbar;:ne936ad0d81da4f9f9785d7ac9cf30a47b4 .</code></pre>|
|[Section top](#minorfail-outcome-number-94)|Pointer|<pre lang="Turtle"><code></code></pre>|
|[Section top](#minorfail-outcome-number-94)|Pointer|<pre lang="Turtle"><code>:hasComparator a owl:ObjectProperty ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;has comparator&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:comment &#34;Links a numerical check method to the check method comparato...&#34; ;  &#10;&#32;&#32;&#32;&#32;rdfs:domain &lowbar;:n0666e2930dbd4d35855555d299f23685b1,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#60;http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#Method>,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:Thing,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;:CheckMethod,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;:NumericalCheckMethod ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy :check&lowbar;method ;  &#10;&#32;&#32;&#32;&#32;rdfs:range :CheckMethodComparator ;  &#10;&#32;&#32;&#32;&#32;rdfs:subPropertyOf :hasComparator ;  &#10;&#32;&#32;&#32;&#32;owl:equivalentProperty :hasComparator .  &#10;&lowbar;:n0666e2930dbd4d35855555d299f23685b2 rdf:first :CheckMethod ;  &#10;&#32;&#32;&#32;&#32;rdf:rest () .  &#10;&lowbar;:n0666e2930dbd4d35855555d299f23685b3 rdf:first :Property ;  &#10;&#32;&#32;&#32;&#32;rdf:rest &lowbar;:n0666e2930dbd4d35855555d299f23685b2 .  &#10;&lowbar;:n0666e2930dbd4d35855555d299f23685b4 rdf:first :FeatureOfInterest ;  &#10;&#32;&#32;&#32;&#32;rdf:rest &lowbar;:n0666e2930dbd4d35855555d299f23685b3 .  &#10;&lowbar;:n0666e2930dbd4d35855555d299f23685b1 a owl:Class ;  &#10;&#32;&#32;&#32;&#32;rdfs:subClassOf &lowbar;:n0666e2930dbd4d35855555d299f23685b1,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:Thing ;  &#10;&#32;&#32;&#32;&#32;owl:equivalentClass &lowbar;:n0666e2930dbd4d35855555d299f23685b1 ;  &#10;&#32;&#32;&#32;&#32;owl:unionOf &lowbar;:n0666e2930dbd4d35855555d299f23685b4 .</code></pre>|
|[Section top](#minorfail-outcome-number-94)|Pointer|<pre lang="Turtle"><code>:hasNestedValue a owl:ObjectProperty ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;hasNestedValue&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:comment &#34;TBD&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:domain &lowbar;:n78e9daa4b6404e65ad022afdc0e3ccc8b1,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#60;http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#Method>,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:Thing,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;:CheckMethod ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy :check&lowbar;method ;  &#10;&#32;&#32;&#32;&#32;rdfs:subPropertyOf :hasNestedValue ;  &#10;&#32;&#32;&#32;&#32;owl:equivalentProperty :hasNestedValue .  &#10;&lowbar;:n78e9daa4b6404e65ad022afdc0e3ccc8b2 rdf:first :CheckMethod ;  &#10;&#32;&#32;&#32;&#32;rdf:rest () .  &#10;&lowbar;:n78e9daa4b6404e65ad022afdc0e3ccc8b3 rdf:first :Property ;  &#10;&#32;&#32;&#32;&#32;rdf:rest &lowbar;:n78e9daa4b6404e65ad022afdc0e3ccc8b2 .  &#10;&lowbar;:n78e9daa4b6404e65ad022afdc0e3ccc8b4 rdf:first :FeatureOfInterest ;  &#10;&#32;&#32;&#32;&#32;rdf:rest &lowbar;:n78e9daa4b6404e65ad022afdc0e3ccc8b3 .  &#10;&lowbar;:n78e9daa4b6404e65ad022afdc0e3ccc8b1 a owl:Class ;  &#10;&#32;&#32;&#32;&#32;rdfs:subClassOf &lowbar;:n78e9daa4b6404e65ad022afdc0e3ccc8b1,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:Thing ;  &#10;&#32;&#32;&#32;&#32;owl:equivalentClass &lowbar;:n78e9daa4b6404e65ad022afdc0e3ccc8b1 ;  &#10;&#32;&#32;&#32;&#32;owl:unionOf &lowbar;:n78e9daa4b6404e65ad022afdc0e3ccc8b4 .</code></pre>|
|[Section top](#minorfail-outcome-number-94)|Pointer|<pre lang="Turtle"><code>:hasOperator a owl:ObjectProperty ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;has operator&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:comment &#34;Links a boolean check method to the check method operator it...&#34; ;  &#10;&#32;&#32;&#32;&#32;rdfs:domain &lowbar;:n6d35c1359a71427688108831b3a5ccadb1,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#60;http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#Method>,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:Thing,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;:BooleanCheckMethod,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;:CheckMethod ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy :check&lowbar;method ;  &#10;&#32;&#32;&#32;&#32;rdfs:range :CheckMethodOperator ;  &#10;&#32;&#32;&#32;&#32;rdfs:subPropertyOf :hasOperator ;  &#10;&#32;&#32;&#32;&#32;owl:equivalentProperty :hasOperator .  &#10;&lowbar;:n6d35c1359a71427688108831b3a5ccadb2 rdf:first :CheckMethod ;  &#10;&#32;&#32;&#32;&#32;rdf:rest () .  &#10;&lowbar;:n6d35c1359a71427688108831b3a5ccadb3 rdf:first :Property ;  &#10;&#32;&#32;&#32;&#32;rdf:rest &lowbar;:n6d35c1359a71427688108831b3a5ccadb2 .  &#10;&lowbar;:n6d35c1359a71427688108831b3a5ccadb4 rdf:first :FeatureOfInterest ;  &#10;&#32;&#32;&#32;&#32;rdf:rest &lowbar;:n6d35c1359a71427688108831b3a5ccadb3 .  &#10;&lowbar;:n6d35c1359a71427688108831b3a5ccadb1 a owl:Class ;  &#10;&#32;&#32;&#32;&#32;rdfs:subClassOf &lowbar;:n6d35c1359a71427688108831b3a5ccadb1,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:Thing ;  &#10;&#32;&#32;&#32;&#32;owl:equivalentClass &lowbar;:n6d35c1359a71427688108831b3a5ccadb1 ;  &#10;&#32;&#32;&#32;&#32;owl:unionOf &lowbar;:n6d35c1359a71427688108831b3a5ccadb4 .</code></pre>|

***
### MinorFail Outcome number 95

[Jump to summary definition](#summary-MinorFail-95)	|	[Previous MinorFail outcome](#minorfail-outcome-number-94)	|	[Next MinorFail outcome](#minorfail-outcome-number-96)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-src-check-method|
|----|----|
|Title|Standalone module src/check&lowbar;method.ttl from branch main|
|Composition|- [Module check&lowbar;method](https://github.com/Accord-Project/aec3po/blob/main/src/check_method.ttl)|

#### Criterion detail
|Identifier|[domain-and-range-referencing](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#domain-and-range-referencing)|
|----|----|
|Title|Domain and range referencing test|
|Description|A test case from the Best Practices tests checking if all the ranges and domains from the test subject point to terms that are defined in the vocabulary.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-95)|Identifier|`range-out-of-vocabulary`|
|[Section top](#minorfail-outcome-number-95)|Title|Range out of vocabulary|
|[Section top](#minorfail-outcome-number-95)|Description|Some properties have a range out of the ontology|
|[Section top](#minorfail-outcome-number-95)|Pointer|<pre lang="Turtle"><code>:isOperationalizedBy a owl:ObjectProperty ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;is operationalized by&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:comment &#34;Links a check statement in a document to a check method that...&#34; ;  &#10;&#32;&#32;&#32;&#32;rdfs:domain :CheckStatement ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy :check&lowbar;method ;  &#10;&#32;&#32;&#32;&#32;rdfs:range &lowbar;:nb7ce27fed707433d90bd6f8e75f36ee6b1,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#60;http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#Method>,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:Thing,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;:CheckMethod ;  &#10;&#32;&#32;&#32;&#32;rdfs:subPropertyOf :isOperationalizedBy ;  &#10;&#32;&#32;&#32;&#32;owl:equivalentProperty :isOperationalizedBy ;  &#10;&#32;&#32;&#32;&#32;owl:inverseOf :operationalizes .  &#10;&lowbar;:nb7ce27fed707433d90bd6f8e75f36ee6b2 rdf:first :CheckMethod ;  &#10;&#32;&#32;&#32;&#32;rdf:rest () .  &#10;&lowbar;:nb7ce27fed707433d90bd6f8e75f36ee6b3 rdf:first :Property ;  &#10;&#32;&#32;&#32;&#32;rdf:rest &lowbar;:nb7ce27fed707433d90bd6f8e75f36ee6b2 .  &#10;&lowbar;:nb7ce27fed707433d90bd6f8e75f36ee6b4 rdf:first :FeatureOfInterest ;  &#10;&#32;&#32;&#32;&#32;rdf:rest &lowbar;:nb7ce27fed707433d90bd6f8e75f36ee6b3 .  &#10;&lowbar;:nb7ce27fed707433d90bd6f8e75f36ee6b1 a owl:Class ;  &#10;&#32;&#32;&#32;&#32;rdfs:subClassOf &lowbar;:nb7ce27fed707433d90bd6f8e75f36ee6b1,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:Thing ;  &#10;&#32;&#32;&#32;&#32;owl:equivalentClass &lowbar;:nb7ce27fed707433d90bd6f8e75f36ee6b1 ;  &#10;&#32;&#32;&#32;&#32;owl:unionOf &lowbar;:nb7ce27fed707433d90bd6f8e75f36ee6b4 .</code></pre>|
|[Section top](#minorfail-outcome-number-95)|Pointer|<pre lang="Turtle"><code></code></pre>|
|[Section top](#minorfail-outcome-number-95)|Pointer|<pre lang="Turtle"><code>:hasUnit a owl:FunctionalProperty,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:ObjectProperty ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;hasUnit&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:comment &#34;the hasUnit property is used to link a specific property or ...&#34; ;  &#10;&#32;&#32;&#32;&#32;rdfs:domain &lowbar;:n9a543e7fc552458ca1c9c33ec325260ab1,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:Thing ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy :check&lowbar;method ;  &#10;&#32;&#32;&#32;&#32;rdfs:range qudt:Unit ;  &#10;&#32;&#32;&#32;&#32;rdfs:subPropertyOf :hasUnit ;  &#10;&#32;&#32;&#32;&#32;owl:eqivalentProperty qudt:hasValue ;  &#10;&#32;&#32;&#32;&#32;owl:equivalentProperty :hasUnit .  &#10;&lowbar;:n9a543e7fc552458ca1c9c33ec325260ab2 rdf:first :CheckMethod ;  &#10;&#32;&#32;&#32;&#32;rdf:rest () .  &#10;&lowbar;:n9a543e7fc552458ca1c9c33ec325260ab3 rdf:first :Property ;  &#10;&#32;&#32;&#32;&#32;rdf:rest &lowbar;:n9a543e7fc552458ca1c9c33ec325260ab2 .  &#10;&lowbar;:n9a543e7fc552458ca1c9c33ec325260ab4 rdf:first :FeatureOfInterest ;  &#10;&#32;&#32;&#32;&#32;rdf:rest &lowbar;:n9a543e7fc552458ca1c9c33ec325260ab3 .  &#10;&lowbar;:n9a543e7fc552458ca1c9c33ec325260ab1 a owl:Class ;  &#10;&#32;&#32;&#32;&#32;rdfs:subClassOf &lowbar;:n9a543e7fc552458ca1c9c33ec325260ab1,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:Thing ;  &#10;&#32;&#32;&#32;&#32;owl:equivalentClass &lowbar;:n9a543e7fc552458ca1c9c33ec325260ab1 ;  &#10;&#32;&#32;&#32;&#32;owl:unionOf &lowbar;:n9a543e7fc552458ca1c9c33ec325260ab4 .</code></pre>|
|[Section top](#minorfail-outcome-number-95)|Pointer|<pre lang="Turtle"><code>:hasNestedTarget a owl:ObjectProperty ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;hasNestedTarget&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:comment &#34;&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy :check&lowbar;method ;  &#10;&#32;&#32;&#32;&#32;rdfs:range &lowbar;:n5ca09fd78b674d7383753a7bcd7da744b1,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#60;http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#Method>,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:Thing,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;:CheckMethod ;  &#10;&#32;&#32;&#32;&#32;rdfs:subPropertyOf :hasNestedTarget ;  &#10;&#32;&#32;&#32;&#32;owl:equivalentProperty :hasNestedTarget .  &#10;&lowbar;:n5ca09fd78b674d7383753a7bcd7da744b2 rdf:first :CheckMethod ;  &#10;&#32;&#32;&#32;&#32;rdf:rest () .  &#10;&lowbar;:n5ca09fd78b674d7383753a7bcd7da744b3 rdf:first :Property ;  &#10;&#32;&#32;&#32;&#32;rdf:rest &lowbar;:n5ca09fd78b674d7383753a7bcd7da744b2 .  &#10;&lowbar;:n5ca09fd78b674d7383753a7bcd7da744b4 rdf:first :FeatureOfInterest ;  &#10;&#32;&#32;&#32;&#32;rdf:rest &lowbar;:n5ca09fd78b674d7383753a7bcd7da744b3 .  &#10;&lowbar;:n5ca09fd78b674d7383753a7bcd7da744b1 a owl:Class ;  &#10;&#32;&#32;&#32;&#32;rdfs:subClassOf &lowbar;:n5ca09fd78b674d7383753a7bcd7da744b1,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:Thing ;  &#10;&#32;&#32;&#32;&#32;owl:equivalentClass &lowbar;:n5ca09fd78b674d7383753a7bcd7da744b1 ;  &#10;&#32;&#32;&#32;&#32;owl:unionOf &lowbar;:n5ca09fd78b674d7383753a7bcd7da744b4 .</code></pre>|

***
### MinorFail Outcome number 96

[Jump to summary definition](#summary-MinorFail-96)	|	[Previous MinorFail outcome](#minorfail-outcome-number-95)	|	[Next MinorFail outcome](#minorfail-outcome-number-97)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-src-check-method|
|----|----|
|Title|Standalone module src/check&lowbar;method.ttl from branch main|
|Composition|- [Module check&lowbar;method](https://github.com/Accord-Project/aec3po/blob/main/src/check_method.ttl)|

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
|[Section top](#minorfail-outcome-number-96)|Description|Class Expression not supported with owl:equivalentClass or owl:intersectionOf|
|[Section top](#minorfail-outcome-number-96)|Pointer|<pre lang="Turtle"><code>&#91;] a owl:Class ;  &#10;&#32;&#32;&#32;&#32;owl:intersectionOf ( aec3po:CheckMethod &#91; a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:allValuesFrom &#91; a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:allValuesFrom aec3po:FeatureOfInterest ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:onProperty &#91; owl:inverseOf aec3po:forDesign ] ] ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:onProperty aec3po:forDesign ] ) .</code></pre>|

***
### MinorFail Outcome number 97

[Jump to summary definition](#summary-MinorFail-97)	|	[Previous MinorFail outcome](#minorfail-outcome-number-96)	|	[Next MinorFail outcome](#minorfail-outcome-number-98)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-src-check-method|
|----|----|
|Title|Standalone module src/check&lowbar;method.ttl from branch main|
|Composition|- [Module check&lowbar;method](https://github.com/Accord-Project/aec3po/blob/main/src/check_method.ttl)|

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
|[Section top](#minorfail-outcome-number-97)|Description|Statement not supported in an Equivalent Class Expression|
|[Section top](#minorfail-outcome-number-97)|Pointer|<pre lang="Turtle"><code>&#91;] a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;owl:allValuesFrom &#91; a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:allValuesFrom aec3po:FeatureOfInterest ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:onProperty &#91; owl:inverseOf aec3po:forDesign ] ] ;  &#10;&#32;&#32;&#32;&#32;owl:onProperty aec3po:forDesign .</code></pre>|

***
### MinorFail Outcome number 98

[Jump to summary definition](#summary-MinorFail-98)	|	[Previous MinorFail outcome](#minorfail-outcome-number-97)	|	[Next MinorFail outcome](#minorfail-outcome-number-99)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-src-check-method|
|----|----|
|Title|Standalone module src/check&lowbar;method.ttl from branch main|
|Composition|- [Module check&lowbar;method](https://github.com/Accord-Project/aec3po/blob/main/src/check_method.ttl)|

#### Criterion detail
|Identifier|[profile-compatibility](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#profile-compatibility)|
|----|----|
|Title|Profile compatibility test|
|Description|A test meant to check whether the test subject is compatible with a profile or not, and if it is not, why.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-98)|Identifier|`owl-rl-profile-error`|
|[Section top](#minorfail-outcome-number-98)|Title|OWL RL Profile incompatible|
|[Section top](#minorfail-outcome-number-98)|Description|Class Expression not supported as object of rdfs:domain or rdfs:range|
|[Section top](#minorfail-outcome-number-98)|Pointer|<pre lang="Turtle"><code>aec3po:hasBSSDDTarget a owl:FunctionalProperty,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:ObjectProperty ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;hasBSSDDTarget&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:comment &#34;The target refers to either the name of an object, the name ...&#34; ;  &#10;&#32;&#32;&#32;&#32;rdfs:domain &#91; a owl:Class ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:unionOf ( aec3po:FeatureOfInterest aec3po:Property aec3po:CheckMethod ) ] ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy aec3po:check&lowbar;method .</code></pre>|
|[Section top](#minorfail-outcome-number-98)|Pointer|<pre lang="Turtle"><code>aec3po:hasUnit a owl:FunctionalProperty,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:ObjectProperty ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;hasUnit&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:comment &#34;the hasUnit property is used to link a specific property or ...&#34; ;  &#10;&#32;&#32;&#32;&#32;rdfs:domain &#91; a owl:Class ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:unionOf ( aec3po:FeatureOfInterest aec3po:Property aec3po:CheckMethod ) ] ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy aec3po:check&lowbar;method ;  &#10;&#32;&#32;&#32;&#32;rdfs:range qudt:Unit ;  &#10;&#32;&#32;&#32;&#32;owl:eqivalentProperty qudt:hasValue .</code></pre>|

***
### MinorFail Outcome number 99

[Jump to summary definition](#summary-MinorFail-99)	|	[Previous MinorFail outcome](#minorfail-outcome-number-98)	|	[Next MinorFail outcome](#minorfail-outcome-number-100)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-src-check-method|
|----|----|
|Title|Standalone module src/check&lowbar;method.ttl from branch main|
|Composition|- [Module check&lowbar;method](https://github.com/Accord-Project/aec3po/blob/main/src/check_method.ttl)|

#### Criterion detail
|Identifier|[profile-compatibility](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#profile-compatibility)|
|----|----|
|Title|Profile compatibility test|
|Description|A test meant to check whether the test subject is compatible with a profile or not, and if it is not, why.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-99)|Identifier|`owl-rl-profile-error`|
|[Section top](#minorfail-outcome-number-99)|Title|OWL RL Profile incompatible|
|[Section top](#minorfail-outcome-number-99)|Description|Class Expression not supported with owl:equivalentClass|
|[Section top](#minorfail-outcome-number-99)|Pointer|<pre lang="Turtle"><code>aec3po:ComponentCheckMethod a owl:Class ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;Component Check Method&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:comment &#34;Component check method refers to a process of inspecting and...&#34; ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy aec3po:check&lowbar;method ;  &#10;&#32;&#32;&#32;&#32;rdfs:subClassOf aec3po:CheckMethod ;  &#10;&#32;&#32;&#32;&#32;owl:equivalentClass &#91; a owl:Class ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:intersectionOf ( aec3po:CheckMethod &#91; a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:allValuesFrom &#91; a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:allValuesFrom aec3po:FeatureOfInterest ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:onProperty &#91; owl:inverseOf aec3po:forDesign ] ] ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:onProperty aec3po:forDesign ] ) ] .</code></pre>|

***
### MinorFail Outcome number 100

[Jump to summary definition](#summary-MinorFail-100)	|	[Previous MinorFail outcome](#minorfail-outcome-number-99)	|	[Next MinorFail outcome](#minorfail-outcome-number-101)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-src-check-method|
|----|----|
|Title|Standalone module src/check&lowbar;method.ttl from branch main|
|Composition|- [Module check&lowbar;method](https://github.com/Accord-Project/aec3po/blob/main/src/check_method.ttl)|

#### Criterion detail
|Identifier|[profile-compatibility](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#profile-compatibility)|
|----|----|
|Title|Profile compatibility test|
|Description|A test meant to check whether the test subject is compatible with a profile or not, and if it is not, why.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-100)|Identifier|`owl-rl-profile-error`|
|[Section top](#minorfail-outcome-number-100)|Title|OWL RL Profile incompatible|
|[Section top](#minorfail-outcome-number-100)|Description|Statement not supported in a Super Class Expression|
|[Section top](#minorfail-outcome-number-100)|Pointer|<pre lang="Turtle"><code>&#91;] a owl:Class ;  &#10;&#32;&#32;&#32;&#32;owl:unionOf ( aec3po:FeatureOfInterest aec3po:Property aec3po:CheckMethod ) .</code></pre>|

***
### MinorFail Outcome number 101

[Jump to summary definition](#summary-MinorFail-101)	|	[Previous MinorFail outcome](#minorfail-outcome-number-100)	|	[Next MinorFail outcome](#minorfail-outcome-number-102)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-src-check-method|
|----|----|
|Title|Standalone module src/check&lowbar;method.ttl from branch main|
|Composition|- [Module check&lowbar;method](https://github.com/Accord-Project/aec3po/blob/main/src/check_method.ttl)|

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
|[Section top](#minorfail-outcome-number-101)|Description|Statement not supported in a Sub Class Expression|
|[Section top](#minorfail-outcome-number-101)|Pointer|<pre lang="Turtle"><code>&#91;] a owl:Class ;  &#10;&#32;&#32;&#32;&#32;owl:intersectionOf ( aec3po:CheckMethod &#91; a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:allValuesFrom &#91; a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:allValuesFrom aec3po:FeatureOfInterest ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:onProperty &#91; owl:inverseOf aec3po:forDesign ] ] ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:onProperty aec3po:forDesign ] ) .</code></pre>|

***
### MinorFail Outcome number 102

[Jump to summary definition](#summary-MinorFail-102)	|	[Previous MinorFail outcome](#minorfail-outcome-number-101)	|	[Next MinorFail outcome](#minorfail-outcome-number-103)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-src-check-method|
|----|----|
|Title|Standalone module src/check&lowbar;method.ttl from branch main|
|Composition|- [Module check&lowbar;method](https://github.com/Accord-Project/aec3po/blob/main/src/check_method.ttl)|

#### Criterion detail
|Identifier|[profile-compatibility](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#profile-compatibility)|
|----|----|
|Title|Profile compatibility test|
|Description|A test meant to check whether the test subject is compatible with a profile or not, and if it is not, why.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-102)|Identifier|`owl-ql-profile-error`|
|[Section top](#minorfail-outcome-number-102)|Title|OWL QL Profile incompatible|
|[Section top](#minorfail-outcome-number-102)|Description|Class Expression not supported as object of rdfs:domain or rdfs:range|
|[Section top](#minorfail-outcome-number-102)|Pointer|<pre lang="Turtle"><code>aec3po:hasBSSDDTarget a owl:FunctionalProperty,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:ObjectProperty ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;hasBSSDDTarget&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:comment &#34;The target refers to either the name of an object, the name ...&#34; ;  &#10;&#32;&#32;&#32;&#32;rdfs:domain &#91; a owl:Class ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:unionOf ( aec3po:FeatureOfInterest aec3po:Property aec3po:CheckMethod ) ] ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy aec3po:check&lowbar;method .</code></pre>|
|[Section top](#minorfail-outcome-number-102)|Pointer|<pre lang="Turtle"><code>aec3po:hasUnit a owl:FunctionalProperty,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:ObjectProperty ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;hasUnit&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:comment &#34;the hasUnit property is used to link a specific property or ...&#34; ;  &#10;&#32;&#32;&#32;&#32;rdfs:domain &#91; a owl:Class ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:unionOf ( aec3po:FeatureOfInterest aec3po:Property aec3po:CheckMethod ) ] ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy aec3po:check&lowbar;method ;  &#10;&#32;&#32;&#32;&#32;rdfs:range qudt:Unit ;  &#10;&#32;&#32;&#32;&#32;owl:eqivalentProperty qudt:hasValue .</code></pre>|

***
### MinorFail Outcome number 103

[Jump to summary definition](#summary-MinorFail-103)	|	[Previous MinorFail outcome](#minorfail-outcome-number-102)	|	[Next MinorFail outcome](#minorfail-outcome-number-104)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-src-check-method|
|----|----|
|Title|Standalone module src/check&lowbar;method.ttl from branch main|
|Composition|- [Module check&lowbar;method](https://github.com/Accord-Project/aec3po/blob/main/src/check_method.ttl)|

#### Criterion detail
|Identifier|[profile-compatibility](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#profile-compatibility)|
|----|----|
|Title|Profile compatibility test|
|Description|A test meant to check whether the test subject is compatible with a profile or not, and if it is not, why.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-103)|Identifier|`owl-ql-profile-error`|
|[Section top](#minorfail-outcome-number-103)|Title|OWL QL Profile incompatible|
|[Section top](#minorfail-outcome-number-103)|Description|Restriction on datatypes|
|[Section top](#minorfail-outcome-number-103)|Pointer|<pre lang="Turtle"><code>aec3po:hasBooleanTarget a owl:DatatypeProperty ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;hasBooleanTarget&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:comment &#34;TBD&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:range xsd:boolean .</code></pre>|

***
### MinorFail Outcome number 104

[Jump to summary definition](#summary-MinorFail-104)	|	[Previous MinorFail outcome](#minorfail-outcome-number-103)	|	[Next MinorFail outcome](#minorfail-outcome-number-105)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-src-check-method|
|----|----|
|Title|Standalone module src/check&lowbar;method.ttl from branch main|
|Composition|- [Module check&lowbar;method](https://github.com/Accord-Project/aec3po/blob/main/src/check_method.ttl)|

#### Criterion detail
|Identifier|[profile-compatibility](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#profile-compatibility)|
|----|----|
|Title|Profile compatibility test|
|Description|A test meant to check whether the test subject is compatible with a profile or not, and if it is not, why.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-104)|Identifier|`owl-ql-profile-error`|
|[Section top](#minorfail-outcome-number-104)|Title|OWL QL Profile incompatible|
|[Section top](#minorfail-outcome-number-104)|Description|Class Expression not supported with owl:equivalentClass|
|[Section top](#minorfail-outcome-number-104)|Pointer|<pre lang="Turtle"><code>aec3po:ComponentCheckMethod a owl:Class ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;Component Check Method&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:comment &#34;Component check method refers to a process of inspecting and...&#34; ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy aec3po:check&lowbar;method ;  &#10;&#32;&#32;&#32;&#32;rdfs:subClassOf aec3po:CheckMethod ;  &#10;&#32;&#32;&#32;&#32;owl:equivalentClass &#91; a owl:Class ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:intersectionOf ( aec3po:CheckMethod &#91; a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:allValuesFrom &#91; a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:allValuesFrom aec3po:FeatureOfInterest ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:onProperty &#91; owl:inverseOf aec3po:forDesign ] ] ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:onProperty aec3po:forDesign ] ) ] .</code></pre>|

***
### MinorFail Outcome number 105

[Jump to summary definition](#summary-MinorFail-105)	|	[Previous MinorFail outcome](#minorfail-outcome-number-104)	|	[Next MinorFail outcome](#minorfail-outcome-number-106)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-src-check-method|
|----|----|
|Title|Standalone module src/check&lowbar;method.ttl from branch main|
|Composition|- [Module check&lowbar;method](https://github.com/Accord-Project/aec3po/blob/main/src/check_method.ttl)|

#### Criterion detail
|Identifier|[profile-compatibility](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#profile-compatibility)|
|----|----|
|Title|Profile compatibility test|
|Description|A test meant to check whether the test subject is compatible with a profile or not, and if it is not, why.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-105)|Identifier|`owl-ql-profile-error`|
|[Section top](#minorfail-outcome-number-105)|Title|OWL QL Profile incompatible|
|[Section top](#minorfail-outcome-number-105)|Description|Statement not supported in a Super Class Expression|
|[Section top](#minorfail-outcome-number-105)|Pointer|<pre lang="Turtle"><code>&#91;] a owl:Class ;  &#10;&#32;&#32;&#32;&#32;owl:unionOf ( aec3po:FeatureOfInterest aec3po:Property aec3po:CheckMethod ) .</code></pre>|

***
### MinorFail Outcome number 106

[Jump to summary definition](#summary-MinorFail-106)	|	[Previous MinorFail outcome](#minorfail-outcome-number-105)	|	[Next MinorFail outcome](#minorfail-outcome-number-107)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-src-check-method|
|----|----|
|Title|Standalone module src/check&lowbar;method.ttl from branch main|
|Composition|- [Module check&lowbar;method](https://github.com/Accord-Project/aec3po/blob/main/src/check_method.ttl)|

#### Criterion detail
|Identifier|[profile-compatibility](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#profile-compatibility)|
|----|----|
|Title|Profile compatibility test|
|Description|A test meant to check whether the test subject is compatible with a profile or not, and if it is not, why.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-106)|Identifier|`owl-el-profile-error`|
|[Section top](#minorfail-outcome-number-106)|Title|OWL EL Profile incompatible|
|[Section top](#minorfail-outcome-number-106)|Description|Statement not supported in a Class Expression|
|[Section top](#minorfail-outcome-number-106)|Pointer|<pre lang="Turtle"><code>&#91;] a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;owl:allValuesFrom &#91; a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:allValuesFrom aec3po:FeatureOfInterest ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:onProperty &#91; owl:inverseOf aec3po:forDesign ] ] ;  &#10;&#32;&#32;&#32;&#32;owl:onProperty aec3po:forDesign .</code></pre>|
|[Section top](#minorfail-outcome-number-106)|Pointer|<pre lang="Turtle"><code>&#91;] a owl:Class ;  &#10;&#32;&#32;&#32;&#32;owl:unionOf ( aec3po:FeatureOfInterest aec3po:Property aec3po:CheckMethod ) .</code></pre>|

***
### MinorFail Outcome number 107

[Jump to summary definition](#summary-MinorFail-107)	|	[Previous MinorFail outcome](#minorfail-outcome-number-106)	|	[Next MinorFail outcome](#minorfail-outcome-number-108)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-src-check-method|
|----|----|
|Title|Standalone module src/check&lowbar;method.ttl from branch main|
|Composition|- [Module check&lowbar;method](https://github.com/Accord-Project/aec3po/blob/main/src/check_method.ttl)|

#### Criterion detail
|Identifier|[profile-compatibility](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#profile-compatibility)|
|----|----|
|Title|Profile compatibility test|
|Description|A test meant to check whether the test subject is compatible with a profile or not, and if it is not, why.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-107)|Identifier|`owl-el-profile-error`|
|[Section top](#minorfail-outcome-number-107)|Title|OWL EL Profile incompatible|
|[Section top](#minorfail-outcome-number-107)|Description|Restriction on datatypes|
|[Section top](#minorfail-outcome-number-107)|Pointer|<pre lang="Turtle"><code>aec3po:hasBooleanTarget a owl:DatatypeProperty ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;hasBooleanTarget&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:comment &#34;TBD&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:range xsd:boolean .</code></pre>|

***
### MinorFail Outcome number 108

[Jump to summary definition](#summary-MinorFail-108)	|	[Previous MinorFail outcome](#minorfail-outcome-number-107)	|	[Next MinorFail outcome](#minorfail-outcome-number-109)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-src-check-method|
|----|----|
|Title|Standalone module src/check&lowbar;method.ttl from branch main|
|Composition|- [Module check&lowbar;method](https://github.com/Accord-Project/aec3po/blob/main/src/check_method.ttl)|

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
|[Section top](#minorfail-outcome-number-108)|Description|Class Expression not supported with owl:equivalentClass|
|[Section top](#minorfail-outcome-number-108)|Pointer|<pre lang="Turtle"><code>aec3po:ComponentCheckMethod a owl:Class ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;Component Check Method&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:comment &#34;Component check method refers to a process of inspecting and...&#34; ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy aec3po:check&lowbar;method ;  &#10;&#32;&#32;&#32;&#32;rdfs:subClassOf aec3po:CheckMethod ;  &#10;&#32;&#32;&#32;&#32;owl:equivalentClass &#91; a owl:Class ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:intersectionOf ( aec3po:CheckMethod &#91; a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:allValuesFrom &#91; a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:allValuesFrom aec3po:FeatureOfInterest ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:onProperty &#91; owl:inverseOf aec3po:forDesign ] ] ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:onProperty aec3po:forDesign ] ) ] .</code></pre>|

***
### MinorFail Outcome number 109

[Jump to summary definition](#summary-MinorFail-109)	|	[Previous MinorFail outcome](#minorfail-outcome-number-108)	|	[Next MinorFail outcome](#minorfail-outcome-number-110)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-src-check-method|
|----|----|
|Title|Standalone module src/check&lowbar;method.ttl from branch main|
|Composition|- [Module check&lowbar;method](https://github.com/Accord-Project/aec3po/blob/main/src/check_method.ttl)|

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
|[Section top](#minorfail-outcome-number-109)|Description|Class Expression not supported as object of rdfs:domain or rdfs:range|
|[Section top](#minorfail-outcome-number-109)|Pointer|<pre lang="Turtle"><code>aec3po:hasBSSDDTarget a owl:FunctionalProperty,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:ObjectProperty ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;hasBSSDDTarget&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:comment &#34;The target refers to either the name of an object, the name ...&#34; ;  &#10;&#32;&#32;&#32;&#32;rdfs:domain &#91; a owl:Class ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:unionOf ( aec3po:FeatureOfInterest aec3po:Property aec3po:CheckMethod ) ] ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy aec3po:check&lowbar;method .</code></pre>|
|[Section top](#minorfail-outcome-number-109)|Pointer|<pre lang="Turtle"><code>aec3po:hasUnit a owl:FunctionalProperty,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:ObjectProperty ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;hasUnit&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:comment &#34;the hasUnit property is used to link a specific property or ...&#34; ;  &#10;&#32;&#32;&#32;&#32;rdfs:domain &#91; a owl:Class ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:unionOf ( aec3po:FeatureOfInterest aec3po:Property aec3po:CheckMethod ) ] ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy aec3po:check&lowbar;method ;  &#10;&#32;&#32;&#32;&#32;rdfs:range qudt:Unit ;  &#10;&#32;&#32;&#32;&#32;owl:eqivalentProperty qudt:hasValue .</code></pre>|

***
### MinorFail Outcome number 110

[Jump to summary definition](#summary-MinorFail-110)	|	[Previous MinorFail outcome](#minorfail-outcome-number-109)	|	[Next MinorFail outcome](#minorfail-outcome-number-111)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-src-check-method|
|----|----|
|Title|Standalone module src/check&lowbar;method.ttl from branch main|
|Composition|- [Module check&lowbar;method](https://github.com/Accord-Project/aec3po/blob/main/src/check_method.ttl)|

#### Criterion detail
|Identifier|[term-referencing](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#term-referencing)|
|----|----|
|Title|Term referencing test|
|Description|A test case from the Best Practices tests checking if each term of the test subject is referenced to a module through a rdfs:isDefinedBy property.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-110)|Identifier|`no-reference-module`|
|[Section top](#minorfail-outcome-number-110)|Title|Term not referenced to a module|
|[Section top](#minorfail-outcome-number-110)|Description|Subject terms not linked to a module by a rdfs:isDefinedBy property|
|[Section top](#minorfail-outcome-number-110)|Pointer|<pre lang="Turtle"><code>:hasTarget a owl:DatatypeProperty ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;hasTarget&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:comment &#34;TBD&#34;@en .</code></pre>|
|[Section top](#minorfail-outcome-number-110)|Pointer|<pre lang="Turtle"><code>:hasBooleanTarget a owl:DatatypeProperty ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;hasBooleanTarget&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:comment &#34;TBD&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:range xsd:boolean .</code></pre>|

***
### MinorFail Outcome number 111

[Jump to summary definition](#summary-MinorFail-111)	|	[Previous MinorFail outcome](#minorfail-outcome-number-110)	|	[Next MinorFail outcome](#minorfail-outcome-number-112)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-src-aec3po|
|----|----|
|Title|Standalone module src/aec3po.ttl from branch main|
|Composition|- [Module aec3po](https://github.com/Accord-Project/aec3po/blob/main/src/aec3po.ttl)|

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
|[Section top](#minorfail-outcome-number-111)|Description|Class Expression not supported as object of rdfs:domain or rdfs:range|
|[Section top](#minorfail-outcome-number-111)|Pointer|<pre lang="Turtle"><code>aec3po:hasValue a owl:DatatypeProperty,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:FunctionalProperty ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;has value&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:comment &#34;de facto used to link something (anything: property, propert...&#34; ;  &#10;&#32;&#32;&#32;&#32;rdfs:domain &#91; a owl:Class ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:unionOf ( aec3po:FeatureOfInterest aec3po:Property aec3po:CheckMethod ) ] ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy aec3po: ;  &#10;&#32;&#32;&#32;&#32;skos:note &#34;The value of the literal may be a XSD literal (boolean, inte...&#34; .</code></pre>|

***
### MinorFail Outcome number 112

[Jump to summary definition](#summary-MinorFail-112)	|	[Previous MinorFail outcome](#minorfail-outcome-number-111)	|	[Next MinorFail outcome](#minorfail-outcome-number-113)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-src-aec3po|
|----|----|
|Title|Standalone module src/aec3po.ttl from branch main|
|Composition|- [Module aec3po](https://github.com/Accord-Project/aec3po/blob/main/src/aec3po.ttl)|

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
|[Section top](#minorfail-outcome-number-112)|Pointer|<pre lang="Turtle"><code>&#91;] a owl:Class ;  &#10;&#32;&#32;&#32;&#32;owl:unionOf ( aec3po:FeatureOfInterest aec3po:Property aec3po:CheckMethod ) .</code></pre>|

***
### MinorFail Outcome number 113

[Jump to summary definition](#summary-MinorFail-113)	|	[Previous MinorFail outcome](#minorfail-outcome-number-112)	|	[Next MinorFail outcome](#minorfail-outcome-number-114)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-src-aec3po|
|----|----|
|Title|Standalone module src/aec3po.ttl from branch main|
|Composition|- [Module aec3po](https://github.com/Accord-Project/aec3po/blob/main/src/aec3po.ttl)|

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
|[Section top](#minorfail-outcome-number-113)|Description|Class Expression not supported as object of rdfs:domain or rdfs:range|
|[Section top](#minorfail-outcome-number-113)|Pointer|<pre lang="Turtle"><code>aec3po:hasValue a owl:DatatypeProperty,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:FunctionalProperty ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;has value&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:comment &#34;de facto used to link something (anything: property, propert...&#34; ;  &#10;&#32;&#32;&#32;&#32;rdfs:domain &#91; a owl:Class ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:unionOf ( aec3po:FeatureOfInterest aec3po:Property aec3po:CheckMethod ) ] ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy aec3po: ;  &#10;&#32;&#32;&#32;&#32;skos:note &#34;The value of the literal may be a XSD literal (boolean, inte...&#34; .</code></pre>|

***
### MinorFail Outcome number 114

[Jump to summary definition](#summary-MinorFail-114)	|	[Previous MinorFail outcome](#minorfail-outcome-number-113)	|	[Next MinorFail outcome](#minorfail-outcome-number-115)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-src-aec3po|
|----|----|
|Title|Standalone module src/aec3po.ttl from branch main|
|Composition|- [Module aec3po](https://github.com/Accord-Project/aec3po/blob/main/src/aec3po.ttl)|

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
|[Section top](#minorfail-outcome-number-114)|Description|Statement not supported in a Super Class Expression|
|[Section top](#minorfail-outcome-number-114)|Pointer|<pre lang="Turtle"><code>&#91;] a owl:Class ;  &#10;&#32;&#32;&#32;&#32;owl:unionOf ( aec3po:FeatureOfInterest aec3po:Property aec3po:CheckMethod ) .</code></pre>|

***
### MinorFail Outcome number 115

[Jump to summary definition](#summary-MinorFail-115)	|	[Previous MinorFail outcome](#minorfail-outcome-number-114)	|	[Next MinorFail outcome](#minorfail-outcome-number-116)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-src-aec3po|
|----|----|
|Title|Standalone module src/aec3po.ttl from branch main|
|Composition|- [Module aec3po](https://github.com/Accord-Project/aec3po/blob/main/src/aec3po.ttl)|

#### Criterion detail
|Identifier|[profile-compatibility](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#profile-compatibility)|
|----|----|
|Title|Profile compatibility test|
|Description|A test meant to check whether the test subject is compatible with a profile or not, and if it is not, why.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-115)|Identifier|`owl-el-profile-error`|
|[Section top](#minorfail-outcome-number-115)|Title|OWL EL Profile incompatible|
|[Section top](#minorfail-outcome-number-115)|Description|Statement not supported in a Class Expression|
|[Section top](#minorfail-outcome-number-115)|Pointer|<pre lang="Turtle"><code>&#91;] a owl:Class ;  &#10;&#32;&#32;&#32;&#32;owl:unionOf ( aec3po:FeatureOfInterest aec3po:Property aec3po:CheckMethod ) .</code></pre>|

***
### MinorFail Outcome number 116

[Jump to summary definition](#summary-MinorFail-116)	|	[Previous MinorFail outcome](#minorfail-outcome-number-115)	|	[Next MinorFail outcome](#minorfail-outcome-number-117)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-src-aec3po|
|----|----|
|Title|Standalone module src/aec3po.ttl from branch main|
|Composition|- [Module aec3po](https://github.com/Accord-Project/aec3po/blob/main/src/aec3po.ttl)|

#### Criterion detail
|Identifier|[profile-compatibility](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#profile-compatibility)|
|----|----|
|Title|Profile compatibility test|
|Description|A test meant to check whether the test subject is compatible with a profile or not, and if it is not, why.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-116)|Identifier|`owl-el-profile-error`|
|[Section top](#minorfail-outcome-number-116)|Title|OWL EL Profile incompatible|
|[Section top](#minorfail-outcome-number-116)|Description|Class Expression not supported as object of rdfs:domain or rdfs:range|
|[Section top](#minorfail-outcome-number-116)|Pointer|<pre lang="Turtle"><code>aec3po:hasValue a owl:DatatypeProperty,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:FunctionalProperty ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;has value&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:comment &#34;de facto used to link something (anything: property, propert...&#34; ;  &#10;&#32;&#32;&#32;&#32;rdfs:domain &#91; a owl:Class ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:unionOf ( aec3po:FeatureOfInterest aec3po:Property aec3po:CheckMethod ) ] ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy aec3po: ;  &#10;&#32;&#32;&#32;&#32;skos:note &#34;The value of the literal may be a XSD literal (boolean, inte...&#34; .</code></pre>|

***
### MinorFail Outcome number 117

[Jump to summary definition](#summary-MinorFail-117)	|	[Previous MinorFail outcome](#minorfail-outcome-number-116)	|	[Next MinorFail outcome](#minorfail-outcome-number-118)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-src-aec3po|
|----|----|
|Title|Standalone module src/aec3po.ttl from branch main|
|Composition|- [Module aec3po](https://github.com/Accord-Project/aec3po/blob/main/src/aec3po.ttl)|

#### Criterion detail
|Identifier|[term-referencing](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#term-referencing)|
|----|----|
|Title|Term referencing test|
|Description|A test case from the Best Practices tests checking if each term of the test subject is referenced to a module through a rdfs:isDefinedBy property.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-117)|Identifier|`no-reference-module`|
|[Section top](#minorfail-outcome-number-117)|Title|Term not referenced to a module|
|[Section top](#minorfail-outcome-number-117)|Description|Subject terms not linked to a module by a rdfs:isDefinedBy property|
|[Section top](#minorfail-outcome-number-117)|Pointer|<pre lang="Turtle"><code>:edlira a schema:Person ;  &#10;&#32;&#32;&#32;&#32;schema:affiliation &#60;https://www.bcu.ac.uk/> ;  &#10;&#32;&#32;&#32;&#32;schema:email &#34;edlira.vakaj@bcu.ac.uk&#34; ;  &#10;&#32;&#32;&#32;&#32;schema:identifier &#60;http://orcid.org/0000-0002-0712-0959> ;  &#10;&#32;&#32;&#32;&#32;schema:name &#34;Edlira Vakaj&#34; ;  &#10;&#32;&#32;&#32;&#32;schema:url &#60;https://www.bcu.ac.uk/computing/about-us/our-staff/edlira-vakaj> .</code></pre>|
|[Section top](#minorfail-outcome-number-117)|Pointer|<pre lang="Turtle"><code>:pan a schema:Person ;  &#10;&#32;&#32;&#32;&#32;schema:affiliation &#60;https://www.bcu.ac.uk/> ;  &#10;&#32;&#32;&#32;&#32;schema:email &#34;Panagiotis.Patlakas@bcu.ac.uk&#34; ;  &#10;&#32;&#32;&#32;&#32;schema:identifier &#60;http://orcid.org/0000-0002-7248-8952> ;  &#10;&#32;&#32;&#32;&#32;schema:name &#34;Panagiotis Patlakas&#34; ;  &#10;&#32;&#32;&#32;&#32;schema:url &#60;https://www.bcu.ac.uk/built-environment/about-us/our-staff/panagiotis-patlakas> .</code></pre>|
|[Section top](#minorfail-outcome-number-117)|Pointer|<pre lang="Turtle"><code>:amna a schema:Person ;  &#10;&#32;&#32;&#32;&#32;schema:affiliation &#60;https://www.bcu.ac.uk/> ;  &#10;&#32;&#32;&#32;&#32;schema:email &#34;Amna.Dridi@bcu.ac.uk&#34; ;  &#10;&#32;&#32;&#32;&#32;schema:identifier &#60;http://orcid.org/0000-0002-0185-103X> ;  &#10;&#32;&#32;&#32;&#32;schema:name &#34;Amna Dridi&#34; ;  &#10;&#32;&#32;&#32;&#32;schema:url &#60;https://www.researchgate.net/profile/Amna-Dridi-3> .</code></pre>|
|[Section top](#minorfail-outcome-number-117)|Pointer|<pre lang="Turtle"><code>:thomas a schema:Person ;  &#10;&#32;&#32;&#32;&#32;schema:affiliation &#60;https://www.cardiff.ac.uk/> ;  &#10;&#32;&#32;&#32;&#32;schema:email &#34;beachth@cardiff.ac.uk&#34; ;  &#10;&#32;&#32;&#32;&#32;schema:identifier &#60;http://orcid.org/0000-0001-5610-8027> ;  &#10;&#32;&#32;&#32;&#32;schema:name &#34;Thomas Beach&#34; ;  &#10;&#32;&#32;&#32;&#32;schema:url &#60;https://profiles.cardiff.ac.uk/staff/beachth> .</code></pre>|
|[Section top](#minorfail-outcome-number-117)|Pointer|<pre lang="Turtle"><code>:vladimir a schema:Person ;  &#10;&#32;&#32;&#32;&#32;schema:affiliation &#60;https://www.ontotext.com/> ;  &#10;&#32;&#32;&#32;&#32;schema:email &#34;vladimir.alexiev@ontotext.com&#34; ;  &#10;&#32;&#32;&#32;&#32;schema:identifier &#60;https://orcid.org/0000-0001-7508-7428> ;  &#10;&#32;&#32;&#32;&#32;schema:name &#34;Vladimir Alexiev&#34; ;  &#10;&#32;&#32;&#32;&#32;schema:url &#60;https://www.ontotext.com/blog/author/vladimir/> .</code></pre>|

***
### MinorFail Outcome number 118

[Jump to summary definition](#summary-MinorFail-118)	|	[Previous MinorFail outcome](#minorfail-outcome-number-117)	|	[Next MinorFail outcome](#minorfail-outcome-number-119)

:exclamation:MinorFail outcome
#### Subject detail
|Name|all-modules|
|----|----|
|Title|All the modules from branch main that are syntaxically correct as well as their recursive imports|
|Composition|- [Module aec3po](https://github.com/Accord-Project/aec3po/blob/main/src/aec3po.ttl)<br/>- [Module checking&lowbar;act](https://github.com/Accord-Project/aec3po/blob/main/src/checking_act.ttl)<br/>- [Module check&lowbar;method](https://github.com/Accord-Project/aec3po/blob/main/src/check_method.ttl)<br/>- [Module compliance&lowbar;verification&lowbar;report](https://github.com/Accord-Project/aec3po/blob/main/src/compliance_verification_report.ttl)<br/>- [Module data&lowbar;requirement](https://github.com/Accord-Project/aec3po/blob/main/src/data_requirement.ttl)<br/>- [Module document](https://github.com/Accord-Project/aec3po/blob/main/src/document.ttl)<br/>- [Module evidence](https://github.com/Accord-Project/aec3po/blob/main/src/evidence.ttl)<br/>- [Module feature&lowbar;of&lowbar;interest](https://github.com/Accord-Project/aec3po/blob/main/src/feature_of_interest.ttl)<br/>- [Module legal&lowbar;verifier](https://github.com/Accord-Project/aec3po/blob/main/src/legal_verifier.ttl)<br/>- [Module model](https://github.com/Accord-Project/aec3po/blob/main/src/model.ttl)<br/>- [Module rase&lowbar;statement](https://github.com/Accord-Project/aec3po/blob/main/src/rase_statement.ttl)<br/>- [Module statement](https://github.com/Accord-Project/aec3po/blob/main/src/statement.ttl)<br/>- [Module table](https://github.com/Accord-Project/aec3po/blob/main/src/table.ttl)<br/>- [Module vocabularies/administrative&lowbar;areas](https://github.com/Accord-Project/aec3po/blob/main/src/vocabularies/administrative_areas.ttl)<br/>- [Module vocabularies/building&lowbar;structure](https://github.com/Accord-Project/aec3po/blob/main/src/vocabularies/building_structure.ttl)<br/>- [Module vocabularies/building&lowbar;usage](https://github.com/Accord-Project/aec3po/blob/main/src/vocabularies/building_usage.ttl)<br/>- [Module vocabularies/check&lowbar;method&lowbar;comparators](https://github.com/Accord-Project/aec3po/blob/main/src/vocabularies/check_method_comparators.ttl)<br/>- [Module vocabularies/check&lowbar;method&lowbar;operators](https://github.com/Accord-Project/aec3po/blob/main/src/vocabularies/check_method_operators.ttl)<br/>- [Module vocabularies/disciplines](https://github.com/Accord-Project/aec3po/blob/main/src/vocabularies/disciplines.ttl)<br/>- [Module vocabularies/permitting&lowbar;stages](https://github.com/Accord-Project/aec3po/blob/main/src/vocabularies/permitting_stages.ttl)<br/>- [Module vocabularies/quantity&lowbar;kinds](https://github.com/Accord-Project/aec3po/blob/main/src/vocabularies/quantity_kinds.ttl)<br/>- [Module vocabularies/&lowbar;shape](https://github.com/Accord-Project/aec3po/blob/main/src/vocabularies/_shape.ttl)|

#### Criterion detail
|Identifier|[domain-and-range-referencing](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#domain-and-range-referencing)|
|----|----|
|Title|Domain and range referencing test|
|Description|A test case from the Best Practices tests checking if all the ranges and domains from the test subject point to terms that are defined in the vocabulary.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-118)|Identifier|`domain-out-of-vocabulary`|
|[Section top](#minorfail-outcome-number-118)|Title|Domain out of vocabulary|
|[Section top](#minorfail-outcome-number-118)|Description|Some properties have a domain out of the ontology|
|[Section top](#minorfail-outcome-number-118)|Pointer|<pre lang="Turtle"><code>:usedMethod a owl:ObjectProperty ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;used method&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:comment &#34;Links a checking act to the method it used (a aec3po:CheckMe...&#34; ;  &#10;&#32;&#32;&#32;&#32;rdfs:domain &#91; a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:onProperty :usedMethod ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:someValuesFrom :CheckMethod ],  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#91; a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:onProperty :madeBy ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:someValuesFrom :ProcessVerifier ],  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#91; a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:onProperty :checked ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:someValuesFrom owl:Thing ],  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#91; a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:onProperty :hasReport ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:someValuesFrom :ComplianceVerificationReport ],  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#60;http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#Event>,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:Thing,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;:CheckingAct ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy :checking&lowbar;act ;  &#10;&#32;&#32;&#32;&#32;rdfs:range &lowbar;:n1157b50cffc947e59de505885909c9c7b5,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#60;http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#Method>,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:Thing,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;:CheckMethod ;  &#10;&#32;&#32;&#32;&#32;rdfs:subPropertyOf :usedMethod ;  &#10;&#32;&#32;&#32;&#32;owl:equivalentProperty :usedMethod .  &#10;&lowbar;:n1157b50cffc947e59de505885909c9c7b6 rdf:first :CheckMethod ;  &#10;&#32;&#32;&#32;&#32;rdf:rest () .  &#10;&lowbar;:n1157b50cffc947e59de505885909c9c7b7 rdf:first :Property ;  &#10;&#32;&#32;&#32;&#32;rdf:rest &lowbar;:n1157b50cffc947e59de505885909c9c7b6 .  &#10;&lowbar;:n1157b50cffc947e59de505885909c9c7b8 rdf:first :FeatureOfInterest ;  &#10;&#32;&#32;&#32;&#32;rdf:rest &lowbar;:n1157b50cffc947e59de505885909c9c7b7 .  &#10;&lowbar;:n1157b50cffc947e59de505885909c9c7b5 a owl:Class ;  &#10;&#32;&#32;&#32;&#32;rdfs:subClassOf &lowbar;:n1157b50cffc947e59de505885909c9c7b5,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:Thing ;  &#10;&#32;&#32;&#32;&#32;owl:equivalentClass &lowbar;:n1157b50cffc947e59de505885909c9c7b5 ;  &#10;&#32;&#32;&#32;&#32;owl:unionOf &lowbar;:n1157b50cffc947e59de505885909c9c7b8 .</code></pre>|
|[Section top](#minorfail-outcome-number-118)|Pointer|<pre lang="Turtle"><code></code></pre>|
|[Section top](#minorfail-outcome-number-118)|Pointer|<pre lang="Turtle"><code>:madeBy a owl:ObjectProperty ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;made by&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:comment &#34;Links a checking act to the process verifier that made it (a...&#34; ;  &#10;&#32;&#32;&#32;&#32;rdfs:domain &#91; a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:onProperty :usedMethod ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:someValuesFrom :CheckMethod ],  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#91; a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:onProperty :madeBy ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:someValuesFrom :ProcessVerifier ],  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#91; a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:onProperty :checked ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:someValuesFrom owl:Thing ],  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#91; a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:onProperty :hasReport ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:someValuesFrom :ComplianceVerificationReport ],  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#60;http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#Event>,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:Thing,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;:CheckingAct ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy :checking&lowbar;act ;  &#10;&#32;&#32;&#32;&#32;rdfs:range :ProcessVerifier ;  &#10;&#32;&#32;&#32;&#32;rdfs:subPropertyOf :madeBy ;  &#10;&#32;&#32;&#32;&#32;owl:equivalentProperty :madeBy .</code></pre>|
|[Section top](#minorfail-outcome-number-118)|Pointer|<pre lang="Turtle"><code>:checked a owl:ObjectProperty ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;checked&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:comment &#34;Links a checking act to some entity (ex. statement, feature ...&#34; ;  &#10;&#32;&#32;&#32;&#32;rdfs:domain &#91; a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:onProperty :usedMethod ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:someValuesFrom :CheckMethod ],  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#91; a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:onProperty :madeBy ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:someValuesFrom :ProcessVerifier ],  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#91; a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:onProperty :checked ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:someValuesFrom owl:Thing ],  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#91; a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:onProperty :hasReport ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:someValuesFrom :ComplianceVerificationReport ],  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#60;http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#Event>,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:Thing,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;:CheckingAct ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy :checking&lowbar;act ;  &#10;&#32;&#32;&#32;&#32;rdfs:subPropertyOf :checked ;  &#10;&#32;&#32;&#32;&#32;owl:equivalentProperty :checked .</code></pre>|
|[Section top](#minorfail-outcome-number-118)|Pointer|<pre lang="Turtle"><code>:hasReport a owl:ObjectProperty ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;has report&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:comment &#34;Links a checking act to the resulting compliance verificatio...&#34; ;  &#10;&#32;&#32;&#32;&#32;rdfs:domain &#91; a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:onProperty :usedMethod ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:someValuesFrom :CheckMethod ],  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#91; a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:onProperty :madeBy ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:someValuesFrom :ProcessVerifier ],  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#91; a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:onProperty :checked ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:someValuesFrom owl:Thing ],  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#91; a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:onProperty :hasReport ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:someValuesFrom :ComplianceVerificationReport ],  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#60;http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#Event>,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:Thing,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;:CheckingAct ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy :checking&lowbar;act ;  &#10;&#32;&#32;&#32;&#32;rdfs:range &#91; a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:onProperty :conforms ],  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:Thing,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;:ComplianceVerificationReport ;  &#10;&#32;&#32;&#32;&#32;rdfs:subPropertyOf :hasReport ;  &#10;&#32;&#32;&#32;&#32;owl:equivalentProperty :hasReport .</code></pre>|
|[Section top](#minorfail-outcome-number-118)|Pointer|<pre lang="Turtle"><code>:operationalizes a owl:ObjectProperty ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;operationalizes&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:comment &#34;Links a check method to a check statement in a document that...&#34; ;  &#10;&#32;&#32;&#32;&#32;rdfs:domain &lowbar;:ne7869838b5c44844a551fc8778c231a1b1,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#60;http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#Method>,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:Thing,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;:CheckMethod ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy :check&lowbar;method ;  &#10;&#32;&#32;&#32;&#32;rdfs:range &#91; a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:allValuesFrom :DocumentSubdivision ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:onProperty :hasSubdivision ],  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#91; owl:unionOf ( :Document :DocumentSubdivision ) ],  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:Thing,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;:CheckStatement,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;:DocumentSubdivision,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;:Statement ;  &#10;&#32;&#32;&#32;&#32;rdfs:subPropertyOf :operationalizes ;  &#10;&#32;&#32;&#32;&#32;owl:equivalentProperty :operationalizes ;  &#10;&#32;&#32;&#32;&#32;owl:inverseOf :isOperationalizedBy .  &#10;&lowbar;:ne7869838b5c44844a551fc8778c231a1b6 rdf:first :CheckMethod ;  &#10;&#32;&#32;&#32;&#32;rdf:rest () .  &#10;&lowbar;:ne7869838b5c44844a551fc8778c231a1b7 rdf:first :Property ;  &#10;&#32;&#32;&#32;&#32;rdf:rest &lowbar;:ne7869838b5c44844a551fc8778c231a1b6 .  &#10;&lowbar;:ne7869838b5c44844a551fc8778c231a1b8 rdf:first :FeatureOfInterest ;  &#10;&#32;&#32;&#32;&#32;rdf:rest &lowbar;:ne7869838b5c44844a551fc8778c231a1b7 .  &#10;&lowbar;:ne7869838b5c44844a551fc8778c231a1b1 a owl:Class ;  &#10;&#32;&#32;&#32;&#32;rdfs:subClassOf &lowbar;:ne7869838b5c44844a551fc8778c231a1b1,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:Thing ;  &#10;&#32;&#32;&#32;&#32;owl:equivalentClass &lowbar;:ne7869838b5c44844a551fc8778c231a1b1 ;  &#10;&#32;&#32;&#32;&#32;owl:unionOf &lowbar;:ne7869838b5c44844a551fc8778c231a1b8 .</code></pre>|
|[Section top](#minorfail-outcome-number-118)|Pointer|<pre lang="Turtle"><code>:Method owl:sameAs :Method .</code></pre>|
|[Section top](#minorfail-outcome-number-118)|Pointer|<pre lang="Turtle"><code>:hasComparator a owl:FunctionalProperty,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:ObjectProperty ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;has comparator&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:comment &#34;Links a numerical check method to the check method comparato...&#34;,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#34;The comparator of a feature of interest or a property of tha...&#34; ;  &#10;&#32;&#32;&#32;&#32;rdfs:domain &lowbar;:n0a90313e6e18422bb0890eaac26c4b38b1,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#60;http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#Method>,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:Thing,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;:CheckMethod,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;:NumericalCheckMethod ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy :check&lowbar;method,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;:check&lowbar;method&lowbar;comparators ;  &#10;&#32;&#32;&#32;&#32;rdfs:range &lowbar;:n0a90313e6e18422bb0890eaac26c4b38b1,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&lowbar;:n0a90313e6e18422bb0890eaac26c4b38b2,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&lowbar;:n0a90313e6e18422bb0890eaac26c4b38b3,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#60;http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#Method>,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:Thing,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;skos:Concept,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;:CheckMethod,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;:CheckMethodComparator ;  &#10;&#32;&#32;&#32;&#32;rdfs:subPropertyOf :hasComparator,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;:hasDesign ;  &#10;&#32;&#32;&#32;&#32;owl:equivalentProperty :hasComparator .  &#10;&lowbar;:n0a90313e6e18422bb0890eaac26c4b38b4 rdf:first :CheckMethod ;  &#10;&#32;&#32;&#32;&#32;rdf:rest () .  &#10;&lowbar;:n0a90313e6e18422bb0890eaac26c4b38b5 rdf:first :Property ;  &#10;&#32;&#32;&#32;&#32;rdf:rest &lowbar;:n0a90313e6e18422bb0890eaac26c4b38b4 .  &#10;&lowbar;:n0a90313e6e18422bb0890eaac26c4b38b6 rdf:first skos:Concept ;  &#10;&#32;&#32;&#32;&#32;rdf:rest ( &lowbar;:n0a90313e6e18422bb0890eaac26c4b38b2 ) .  &#10;&lowbar;:n0a90313e6e18422bb0890eaac26c4b38b8 rdf:first :FeatureOfInterest ;  &#10;&#32;&#32;&#32;&#32;rdf:rest &lowbar;:n0a90313e6e18422bb0890eaac26c4b38b5 .  &#10;&lowbar;:n0a90313e6e18422bb0890eaac26c4b38b3 rdfs:subClassOf &lowbar;:n0a90313e6e18422bb0890eaac26c4b38b1,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&lowbar;:n0a90313e6e18422bb0890eaac26c4b38b2,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&lowbar;:n0a90313e6e18422bb0890eaac26c4b38b3,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#60;http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#Method>,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:Thing,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;skos:Concept,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;:CheckMethod,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;:CheckMethodComparator ;  &#10;&#32;&#32;&#32;&#32;owl:equivalentClass :CheckMethodComparator ;  &#10;&#32;&#32;&#32;&#32;owl:intersectionOf &lowbar;:n0a90313e6e18422bb0890eaac26c4b38b6 .  &#10;&lowbar;:n0a90313e6e18422bb0890eaac26c4b38b2 a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;owl:hasValue :CheckMethodComparatorNomenclature ;  &#10;&#32;&#32;&#32;&#32;owl:onProperty skos:inScheme .  &#10;&lowbar;:n0a90313e6e18422bb0890eaac26c4b38b1 a owl:Class ;  &#10;&#32;&#32;&#32;&#32;rdfs:subClassOf &lowbar;:n0a90313e6e18422bb0890eaac26c4b38b1,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:Thing ;  &#10;&#32;&#32;&#32;&#32;owl:equivalentClass &lowbar;:n0a90313e6e18422bb0890eaac26c4b38b1 ;  &#10;&#32;&#32;&#32;&#32;owl:unionOf &lowbar;:n0a90313e6e18422bb0890eaac26c4b38b8 .</code></pre>|
|[Section top](#minorfail-outcome-number-118)|Pointer|<pre lang="Turtle"><code>:hasNestedValue a owl:ObjectProperty ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;hasNestedValue&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:comment &#34;TBD&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:domain &lowbar;:nc1b82c6daaf1455391107f8847b100b5b1,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#60;http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#Method>,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:Thing,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;:CheckMethod ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy :check&lowbar;method ;  &#10;&#32;&#32;&#32;&#32;rdfs:subPropertyOf :hasNestedValue ;  &#10;&#32;&#32;&#32;&#32;owl:equivalentProperty :hasNestedValue .  &#10;&lowbar;:nc1b82c6daaf1455391107f8847b100b5b2 rdf:first :CheckMethod ;  &#10;&#32;&#32;&#32;&#32;rdf:rest () .  &#10;&lowbar;:nc1b82c6daaf1455391107f8847b100b5b3 rdf:first :Property ;  &#10;&#32;&#32;&#32;&#32;rdf:rest &lowbar;:nc1b82c6daaf1455391107f8847b100b5b2 .  &#10;&lowbar;:nc1b82c6daaf1455391107f8847b100b5b4 rdf:first :FeatureOfInterest ;  &#10;&#32;&#32;&#32;&#32;rdf:rest &lowbar;:nc1b82c6daaf1455391107f8847b100b5b3 .  &#10;&lowbar;:nc1b82c6daaf1455391107f8847b100b5b1 a owl:Class ;  &#10;&#32;&#32;&#32;&#32;rdfs:subClassOf &lowbar;:nc1b82c6daaf1455391107f8847b100b5b1,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:Thing ;  &#10;&#32;&#32;&#32;&#32;owl:equivalentClass &lowbar;:nc1b82c6daaf1455391107f8847b100b5b1 ;  &#10;&#32;&#32;&#32;&#32;owl:unionOf &lowbar;:nc1b82c6daaf1455391107f8847b100b5b4 .</code></pre>|
|[Section top](#minorfail-outcome-number-118)|Pointer|<pre lang="Turtle"><code>:hasOperator a owl:FunctionalProperty,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:ObjectProperty ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;has operator&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:comment &#34;Links a boolean check method to the check method operator it...&#34;,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#34;The operator of a feature of interest or a property of that ...&#34; ;  &#10;&#32;&#32;&#32;&#32;rdfs:domain &lowbar;:n5e2edfa4ac604b8292e3a952d7187d6eb1,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#60;http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#Method>,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:Thing,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;:BooleanCheckMethod,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;:CheckMethod ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy :check&lowbar;method,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;:check&lowbar;method&lowbar;Operators ;  &#10;&#32;&#32;&#32;&#32;rdfs:range &lowbar;:n5e2edfa4ac604b8292e3a952d7187d6eb1,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&lowbar;:n5e2edfa4ac604b8292e3a952d7187d6eb2,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&lowbar;:n5e2edfa4ac604b8292e3a952d7187d6eb3,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#60;http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#Method>,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:Thing,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;skos:Concept,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;:CheckMethod,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;:CheckMethodOperator ;  &#10;&#32;&#32;&#32;&#32;rdfs:subPropertyOf :hasDesign,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;:hasOperator ;  &#10;&#32;&#32;&#32;&#32;owl:equivalentProperty :hasOperator .  &#10;&lowbar;:n5e2edfa4ac604b8292e3a952d7187d6eb4 rdf:first skos:Concept ;  &#10;&#32;&#32;&#32;&#32;rdf:rest ( &lowbar;:n5e2edfa4ac604b8292e3a952d7187d6eb2 ) .  &#10;&lowbar;:n5e2edfa4ac604b8292e3a952d7187d6eb6 rdf:first :CheckMethod ;  &#10;&#32;&#32;&#32;&#32;rdf:rest () .  &#10;&lowbar;:n5e2edfa4ac604b8292e3a952d7187d6eb7 rdf:first :Property ;  &#10;&#32;&#32;&#32;&#32;rdf:rest &lowbar;:n5e2edfa4ac604b8292e3a952d7187d6eb6 .  &#10;&lowbar;:n5e2edfa4ac604b8292e3a952d7187d6eb8 rdf:first :FeatureOfInterest ;  &#10;&#32;&#32;&#32;&#32;rdf:rest &lowbar;:n5e2edfa4ac604b8292e3a952d7187d6eb7 .  &#10;&lowbar;:n5e2edfa4ac604b8292e3a952d7187d6eb3 rdfs:subClassOf &lowbar;:n5e2edfa4ac604b8292e3a952d7187d6eb1,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&lowbar;:n5e2edfa4ac604b8292e3a952d7187d6eb2,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&lowbar;:n5e2edfa4ac604b8292e3a952d7187d6eb3,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#60;http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#Method>,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:Thing,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;skos:Concept,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;:CheckMethod,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;:CheckMethodOperator ;  &#10;&#32;&#32;&#32;&#32;owl:equivalentClass :CheckMethodOperator ;  &#10;&#32;&#32;&#32;&#32;owl:intersectionOf &lowbar;:n5e2edfa4ac604b8292e3a952d7187d6eb4 .  &#10;&lowbar;:n5e2edfa4ac604b8292e3a952d7187d6eb2 a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;owl:hasValue :CheckMethodOperatorNomenclature ;  &#10;&#32;&#32;&#32;&#32;owl:onProperty skos:inScheme .  &#10;&lowbar;:n5e2edfa4ac604b8292e3a952d7187d6eb1 a owl:Class ;  &#10;&#32;&#32;&#32;&#32;rdfs:subClassOf &lowbar;:n5e2edfa4ac604b8292e3a952d7187d6eb1,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:Thing ;  &#10;&#32;&#32;&#32;&#32;owl:equivalentClass &lowbar;:n5e2edfa4ac604b8292e3a952d7187d6eb1 ;  &#10;&#32;&#32;&#32;&#32;owl:unionOf &lowbar;:n5e2edfa4ac604b8292e3a952d7187d6eb8 .</code></pre>|
|[Section top](#minorfail-outcome-number-118)|Pointer|<pre lang="Turtle"><code>:hasProperty a owl:ObjectProperty ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;has Property&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:comment &#34;Links a feature of interest to one of its aspect that is int...&#34; ;  &#10;&#32;&#32;&#32;&#32;rdfs:domain &lowbar;:n0135bd7ef82f4ee99a0ad7f6046128c4b1,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#60;http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#Object>,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:Thing,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#60;https://saref.etsi.org/core/FeatureOfInterest>,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;:FeatureOfInterest ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy :feature&lowbar;of&lowbar;interest ;  &#10;&#32;&#32;&#32;&#32;rdfs:range &lowbar;:n0135bd7ef82f4ee99a0ad7f6046128c4b1,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#60;http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#Quality>,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:Thing,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;:Property ;  &#10;&#32;&#32;&#32;&#32;rdfs:subPropertyOf :hasProperty ;  &#10;&#32;&#32;&#32;&#32;owl:equivalentProperty :hasProperty ;  &#10;&#32;&#32;&#32;&#32;owl:sameAs :hasProperty ;  &#10;&#32;&#32;&#32;&#32;skos:example &#34;Links a space to the area property of that space, a wall to ...&#34; .  &#10;&lowbar;:n0135bd7ef82f4ee99a0ad7f6046128c4b2 rdf:first :CheckMethod ;  &#10;&#32;&#32;&#32;&#32;rdf:rest () .  &#10;&lowbar;:n0135bd7ef82f4ee99a0ad7f6046128c4b3 rdf:first :Property ;  &#10;&#32;&#32;&#32;&#32;rdf:rest &lowbar;:n0135bd7ef82f4ee99a0ad7f6046128c4b2 .  &#10;&lowbar;:n0135bd7ef82f4ee99a0ad7f6046128c4b4 rdf:first :FeatureOfInterest ;  &#10;&#32;&#32;&#32;&#32;rdf:rest &lowbar;:n0135bd7ef82f4ee99a0ad7f6046128c4b3 .  &#10;&lowbar;:n0135bd7ef82f4ee99a0ad7f6046128c4b1 a owl:Class ;  &#10;&#32;&#32;&#32;&#32;rdfs:subClassOf &lowbar;:n0135bd7ef82f4ee99a0ad7f6046128c4b1,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:Thing ;  &#10;&#32;&#32;&#32;&#32;owl:equivalentClass &lowbar;:n0135bd7ef82f4ee99a0ad7f6046128c4b1 ;  &#10;&#32;&#32;&#32;&#32;owl:unionOf &lowbar;:n0135bd7ef82f4ee99a0ad7f6046128c4b4 .</code></pre>|
|[Section top](#minorfail-outcome-number-118)|Pointer|<pre lang="Turtle"><code>:hasProperty a owl:ObjectProperty ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;has Property&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:comment &#34;Links a feature of interest to one of its aspect that is int...&#34; ;  &#10;&#32;&#32;&#32;&#32;rdfs:domain &lowbar;:n5cb88bdf258d4792abac164f41ea4a94b1,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#60;http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#Object>,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:Thing,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#60;https://saref.etsi.org/core/FeatureOfInterest>,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;:FeatureOfInterest ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy :feature&lowbar;of&lowbar;interest ;  &#10;&#32;&#32;&#32;&#32;rdfs:range &lowbar;:n5cb88bdf258d4792abac164f41ea4a94b1,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#60;http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#Quality>,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:Thing,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;:Property ;  &#10;&#32;&#32;&#32;&#32;rdfs:subPropertyOf :hasProperty ;  &#10;&#32;&#32;&#32;&#32;owl:equivalentProperty :hasProperty ;  &#10;&#32;&#32;&#32;&#32;owl:sameAs :hasProperty ;  &#10;&#32;&#32;&#32;&#32;skos:example &#34;Links a space to the area property of that space, a wall to ...&#34; .  &#10;&lowbar;:n5cb88bdf258d4792abac164f41ea4a94b2 rdf:first :CheckMethod ;  &#10;&#32;&#32;&#32;&#32;rdf:rest () .  &#10;&lowbar;:n5cb88bdf258d4792abac164f41ea4a94b3 rdf:first :Property ;  &#10;&#32;&#32;&#32;&#32;rdf:rest &lowbar;:n5cb88bdf258d4792abac164f41ea4a94b2 .  &#10;&lowbar;:n5cb88bdf258d4792abac164f41ea4a94b4 rdf:first :FeatureOfInterest ;  &#10;&#32;&#32;&#32;&#32;rdf:rest &lowbar;:n5cb88bdf258d4792abac164f41ea4a94b3 .  &#10;&lowbar;:n5cb88bdf258d4792abac164f41ea4a94b1 a owl:Class ;  &#10;&#32;&#32;&#32;&#32;rdfs:subClassOf &lowbar;:n5cb88bdf258d4792abac164f41ea4a94b1,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:Thing ;  &#10;&#32;&#32;&#32;&#32;owl:equivalentClass &lowbar;:n5cb88bdf258d4792abac164f41ea4a94b1 ;  &#10;&#32;&#32;&#32;&#32;owl:unionOf &lowbar;:n5cb88bdf258d4792abac164f41ea4a94b4 .</code></pre>|
|[Section top](#minorfail-outcome-number-118)|Pointer|<pre lang="Turtle"><code>:hasQuantityKind a owl:ObjectProperty ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;has quantity kind&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:comment &#34;Links a property to its quantity kind&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:domain &lowbar;:nd867fd53c6e74faf859011674916afdfb1,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#60;http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#Quality>,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:Thing,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;:Property ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy :feature&lowbar;of&lowbar;interest ;  &#10;&#32;&#32;&#32;&#32;rdfs:range &lowbar;:nd867fd53c6e74faf859011674916afdfb2,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&lowbar;:nd867fd53c6e74faf859011674916afdfb3,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;qudt:QuantityKind,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#60;http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#Region>,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:Thing,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;skos:Concept,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;:QuantityKind ;  &#10;&#32;&#32;&#32;&#32;rdfs:subPropertyOf :hasQuantityKind ;  &#10;&#32;&#32;&#32;&#32;owl:equivalentProperty :hasQuantityKind ;  &#10;&#32;&#32;&#32;&#32;owl:sameAs :hasQuantityKind ;  &#10;&#32;&#32;&#32;&#32;skos:example &#34;A space area property to the property kind &#92;&#34;area&#92;&#34;.&#34;@en .  &#10;&lowbar;:nd867fd53c6e74faf859011674916afdfb4 rdf:first skos:Concept ;  &#10;&#32;&#32;&#32;&#32;rdf:rest ( &lowbar;:nd867fd53c6e74faf859011674916afdfb2 ) .  &#10;&lowbar;:nd867fd53c6e74faf859011674916afdfb6 rdf:first :CheckMethod ;  &#10;&#32;&#32;&#32;&#32;rdf:rest () .  &#10;&lowbar;:nd867fd53c6e74faf859011674916afdfb7 rdf:first :Property ;  &#10;&#32;&#32;&#32;&#32;rdf:rest &lowbar;:nd867fd53c6e74faf859011674916afdfb6 .  &#10;&lowbar;:nd867fd53c6e74faf859011674916afdfb8 rdf:first :FeatureOfInterest ;  &#10;&#32;&#32;&#32;&#32;rdf:rest &lowbar;:nd867fd53c6e74faf859011674916afdfb7 .  &#10;&lowbar;:nd867fd53c6e74faf859011674916afdfb3 rdfs:subClassOf &lowbar;:nd867fd53c6e74faf859011674916afdfb2,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&lowbar;:nd867fd53c6e74faf859011674916afdfb3,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;qudt:QuantityKind,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#60;http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#Region>,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:Thing,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;skos:Concept,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;:QuantityKind ;  &#10;&#32;&#32;&#32;&#32;owl:equivalentClass :QuantityKind ;  &#10;&#32;&#32;&#32;&#32;owl:intersectionOf &lowbar;:nd867fd53c6e74faf859011674916afdfb4 .  &#10;&lowbar;:nd867fd53c6e74faf859011674916afdfb1 a owl:Class ;  &#10;&#32;&#32;&#32;&#32;rdfs:subClassOf &lowbar;:nd867fd53c6e74faf859011674916afdfb1,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:Thing ;  &#10;&#32;&#32;&#32;&#32;owl:equivalentClass &lowbar;:nd867fd53c6e74faf859011674916afdfb1 ;  &#10;&#32;&#32;&#32;&#32;owl:unionOf &lowbar;:nd867fd53c6e74faf859011674916afdfb8 .  &#10;&lowbar;:nd867fd53c6e74faf859011674916afdfb2 a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;owl:hasValue :QuantityKindNomenclature ;  &#10;&#32;&#32;&#32;&#32;owl:onProperty skos:inScheme .</code></pre>|

***
### MinorFail Outcome number 119

[Jump to summary definition](#summary-MinorFail-119)	|	[Previous MinorFail outcome](#minorfail-outcome-number-118)	|	[Next MinorFail outcome](#minorfail-outcome-number-120)

:exclamation:MinorFail outcome
#### Subject detail
|Name|all-modules|
|----|----|
|Title|All the modules from branch main that are syntaxically correct as well as their recursive imports|
|Composition|- [Module aec3po](https://github.com/Accord-Project/aec3po/blob/main/src/aec3po.ttl)<br/>- [Module checking&lowbar;act](https://github.com/Accord-Project/aec3po/blob/main/src/checking_act.ttl)<br/>- [Module check&lowbar;method](https://github.com/Accord-Project/aec3po/blob/main/src/check_method.ttl)<br/>- [Module compliance&lowbar;verification&lowbar;report](https://github.com/Accord-Project/aec3po/blob/main/src/compliance_verification_report.ttl)<br/>- [Module data&lowbar;requirement](https://github.com/Accord-Project/aec3po/blob/main/src/data_requirement.ttl)<br/>- [Module document](https://github.com/Accord-Project/aec3po/blob/main/src/document.ttl)<br/>- [Module evidence](https://github.com/Accord-Project/aec3po/blob/main/src/evidence.ttl)<br/>- [Module feature&lowbar;of&lowbar;interest](https://github.com/Accord-Project/aec3po/blob/main/src/feature_of_interest.ttl)<br/>- [Module legal&lowbar;verifier](https://github.com/Accord-Project/aec3po/blob/main/src/legal_verifier.ttl)<br/>- [Module model](https://github.com/Accord-Project/aec3po/blob/main/src/model.ttl)<br/>- [Module rase&lowbar;statement](https://github.com/Accord-Project/aec3po/blob/main/src/rase_statement.ttl)<br/>- [Module statement](https://github.com/Accord-Project/aec3po/blob/main/src/statement.ttl)<br/>- [Module table](https://github.com/Accord-Project/aec3po/blob/main/src/table.ttl)<br/>- [Module vocabularies/administrative&lowbar;areas](https://github.com/Accord-Project/aec3po/blob/main/src/vocabularies/administrative_areas.ttl)<br/>- [Module vocabularies/building&lowbar;structure](https://github.com/Accord-Project/aec3po/blob/main/src/vocabularies/building_structure.ttl)<br/>- [Module vocabularies/building&lowbar;usage](https://github.com/Accord-Project/aec3po/blob/main/src/vocabularies/building_usage.ttl)<br/>- [Module vocabularies/check&lowbar;method&lowbar;comparators](https://github.com/Accord-Project/aec3po/blob/main/src/vocabularies/check_method_comparators.ttl)<br/>- [Module vocabularies/check&lowbar;method&lowbar;operators](https://github.com/Accord-Project/aec3po/blob/main/src/vocabularies/check_method_operators.ttl)<br/>- [Module vocabularies/disciplines](https://github.com/Accord-Project/aec3po/blob/main/src/vocabularies/disciplines.ttl)<br/>- [Module vocabularies/permitting&lowbar;stages](https://github.com/Accord-Project/aec3po/blob/main/src/vocabularies/permitting_stages.ttl)<br/>- [Module vocabularies/quantity&lowbar;kinds](https://github.com/Accord-Project/aec3po/blob/main/src/vocabularies/quantity_kinds.ttl)<br/>- [Module vocabularies/&lowbar;shape](https://github.com/Accord-Project/aec3po/blob/main/src/vocabularies/_shape.ttl)|

#### Criterion detail
|Identifier|[domain-and-range-referencing](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#domain-and-range-referencing)|
|----|----|
|Title|Domain and range referencing test|
|Description|A test case from the Best Practices tests checking if all the ranges and domains from the test subject point to terms that are defined in the vocabulary.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-119)|Identifier|`range-out-of-vocabulary`|
|[Section top](#minorfail-outcome-number-119)|Title|Range out of vocabulary|
|[Section top](#minorfail-outcome-number-119)|Description|Some properties have a range out of the ontology|
|[Section top](#minorfail-outcome-number-119)|Pointer|<pre lang="Turtle"><code>:usedMethod a owl:ObjectProperty ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;used method&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:comment &#34;Links a checking act to the method it used (a aec3po:CheckMe...&#34; ;  &#10;&#32;&#32;&#32;&#32;rdfs:domain &#91; a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:onProperty :usedMethod ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:someValuesFrom :CheckMethod ],  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#91; a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:onProperty :madeBy ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:someValuesFrom :ProcessVerifier ],  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#91; a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:onProperty :checked ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:someValuesFrom owl:Thing ],  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#91; a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:onProperty :hasReport ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:someValuesFrom :ComplianceVerificationReport ],  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#60;http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#Event>,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:Thing,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;:CheckingAct ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy :checking&lowbar;act ;  &#10;&#32;&#32;&#32;&#32;rdfs:range &lowbar;:n51785650b6b24adca63973749afac8e5b5,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#60;http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#Method>,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:Thing,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;:CheckMethod ;  &#10;&#32;&#32;&#32;&#32;rdfs:subPropertyOf :usedMethod ;  &#10;&#32;&#32;&#32;&#32;owl:equivalentProperty :usedMethod .  &#10;&lowbar;:n51785650b6b24adca63973749afac8e5b6 rdf:first :CheckMethod ;  &#10;&#32;&#32;&#32;&#32;rdf:rest () .  &#10;&lowbar;:n51785650b6b24adca63973749afac8e5b7 rdf:first :Property ;  &#10;&#32;&#32;&#32;&#32;rdf:rest &lowbar;:n51785650b6b24adca63973749afac8e5b6 .  &#10;&lowbar;:n51785650b6b24adca63973749afac8e5b8 rdf:first :FeatureOfInterest ;  &#10;&#32;&#32;&#32;&#32;rdf:rest &lowbar;:n51785650b6b24adca63973749afac8e5b7 .  &#10;&lowbar;:n51785650b6b24adca63973749afac8e5b5 a owl:Class ;  &#10;&#32;&#32;&#32;&#32;rdfs:subClassOf &lowbar;:n51785650b6b24adca63973749afac8e5b5,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:Thing ;  &#10;&#32;&#32;&#32;&#32;owl:equivalentClass &lowbar;:n51785650b6b24adca63973749afac8e5b5 ;  &#10;&#32;&#32;&#32;&#32;owl:unionOf &lowbar;:n51785650b6b24adca63973749afac8e5b8 .</code></pre>|
|[Section top](#minorfail-outcome-number-119)|Pointer|<pre lang="Turtle"><code>:Method owl:sameAs :Method .</code></pre>|
|[Section top](#minorfail-outcome-number-119)|Pointer|<pre lang="Turtle"><code>:isOperationalizedBy a owl:ObjectProperty ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;is operationalized by&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:comment &#34;Links a check statement in a document to a check method that...&#34; ;  &#10;&#32;&#32;&#32;&#32;rdfs:domain &#91; a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:allValuesFrom :DocumentSubdivision ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:onProperty :hasSubdivision ],  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#91; owl:unionOf ( :Document :DocumentSubdivision ) ],  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:Thing,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;:CheckStatement,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;:DocumentSubdivision,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;:Statement ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy :check&lowbar;method ;  &#10;&#32;&#32;&#32;&#32;rdfs:range &lowbar;:nb0a23b18abc34bd49492e157b078c3c7b5,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#60;http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#Method>,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:Thing,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;:CheckMethod ;  &#10;&#32;&#32;&#32;&#32;rdfs:subPropertyOf :isOperationalizedBy ;  &#10;&#32;&#32;&#32;&#32;owl:equivalentProperty :isOperationalizedBy ;  &#10;&#32;&#32;&#32;&#32;owl:inverseOf :operationalizes .  &#10;&lowbar;:nb0a23b18abc34bd49492e157b078c3c7b6 rdf:first :CheckMethod ;  &#10;&#32;&#32;&#32;&#32;rdf:rest () .  &#10;&lowbar;:nb0a23b18abc34bd49492e157b078c3c7b7 rdf:first :Property ;  &#10;&#32;&#32;&#32;&#32;rdf:rest &lowbar;:nb0a23b18abc34bd49492e157b078c3c7b6 .  &#10;&lowbar;:nb0a23b18abc34bd49492e157b078c3c7b8 rdf:first :FeatureOfInterest ;  &#10;&#32;&#32;&#32;&#32;rdf:rest &lowbar;:nb0a23b18abc34bd49492e157b078c3c7b7 .  &#10;&lowbar;:nb0a23b18abc34bd49492e157b078c3c7b5 a owl:Class ;  &#10;&#32;&#32;&#32;&#32;rdfs:subClassOf &lowbar;:nb0a23b18abc34bd49492e157b078c3c7b5,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:Thing ;  &#10;&#32;&#32;&#32;&#32;owl:equivalentClass &lowbar;:nb0a23b18abc34bd49492e157b078c3c7b5 ;  &#10;&#32;&#32;&#32;&#32;owl:unionOf &lowbar;:nb0a23b18abc34bd49492e157b078c3c7b8 .</code></pre>|
|[Section top](#minorfail-outcome-number-119)|Pointer|<pre lang="Turtle"><code>:hasComparator a owl:FunctionalProperty,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:ObjectProperty ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;has comparator&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:comment &#34;Links a numerical check method to the check method comparato...&#34;,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#34;The comparator of a feature of interest or a property of tha...&#34; ;  &#10;&#32;&#32;&#32;&#32;rdfs:domain &lowbar;:n9f0722f49aef481bbf672edad18af312b1,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#60;http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#Method>,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:Thing,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;:CheckMethod,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;:NumericalCheckMethod ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy :check&lowbar;method,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;:check&lowbar;method&lowbar;comparators ;  &#10;&#32;&#32;&#32;&#32;rdfs:range &lowbar;:n9f0722f49aef481bbf672edad18af312b1,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&lowbar;:n9f0722f49aef481bbf672edad18af312b2,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&lowbar;:n9f0722f49aef481bbf672edad18af312b3,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#60;http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#Method>,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:Thing,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;skos:Concept,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;:CheckMethod,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;:CheckMethodComparator ;  &#10;&#32;&#32;&#32;&#32;rdfs:subPropertyOf :hasComparator,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;:hasDesign ;  &#10;&#32;&#32;&#32;&#32;owl:equivalentProperty :hasComparator .  &#10;&lowbar;:n9f0722f49aef481bbf672edad18af312b4 rdf:first :CheckMethod ;  &#10;&#32;&#32;&#32;&#32;rdf:rest () .  &#10;&lowbar;:n9f0722f49aef481bbf672edad18af312b5 rdf:first :Property ;  &#10;&#32;&#32;&#32;&#32;rdf:rest &lowbar;:n9f0722f49aef481bbf672edad18af312b4 .  &#10;&lowbar;:n9f0722f49aef481bbf672edad18af312b6 rdf:first skos:Concept ;  &#10;&#32;&#32;&#32;&#32;rdf:rest ( &lowbar;:n9f0722f49aef481bbf672edad18af312b2 ) .  &#10;&lowbar;:n9f0722f49aef481bbf672edad18af312b8 rdf:first :FeatureOfInterest ;  &#10;&#32;&#32;&#32;&#32;rdf:rest &lowbar;:n9f0722f49aef481bbf672edad18af312b5 .  &#10;&lowbar;:n9f0722f49aef481bbf672edad18af312b3 rdfs:subClassOf &lowbar;:n9f0722f49aef481bbf672edad18af312b1,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&lowbar;:n9f0722f49aef481bbf672edad18af312b2,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&lowbar;:n9f0722f49aef481bbf672edad18af312b3,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#60;http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#Method>,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:Thing,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;skos:Concept,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;:CheckMethod,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;:CheckMethodComparator ;  &#10;&#32;&#32;&#32;&#32;owl:equivalentClass :CheckMethodComparator ;  &#10;&#32;&#32;&#32;&#32;owl:intersectionOf &lowbar;:n9f0722f49aef481bbf672edad18af312b6 .  &#10;&lowbar;:n9f0722f49aef481bbf672edad18af312b2 a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;owl:hasValue :CheckMethodComparatorNomenclature ;  &#10;&#32;&#32;&#32;&#32;owl:onProperty skos:inScheme .  &#10;&lowbar;:n9f0722f49aef481bbf672edad18af312b1 a owl:Class ;  &#10;&#32;&#32;&#32;&#32;rdfs:subClassOf &lowbar;:n9f0722f49aef481bbf672edad18af312b1,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:Thing ;  &#10;&#32;&#32;&#32;&#32;owl:equivalentClass &lowbar;:n9f0722f49aef481bbf672edad18af312b1 ;  &#10;&#32;&#32;&#32;&#32;owl:unionOf &lowbar;:n9f0722f49aef481bbf672edad18af312b8 .</code></pre>|
|[Section top](#minorfail-outcome-number-119)|Pointer|<pre lang="Turtle"><code>:hasComparator a owl:FunctionalProperty,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:ObjectProperty ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;has comparator&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:comment &#34;Links a numerical check method to the check method comparato...&#34;,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#34;The comparator of a feature of interest or a property of tha...&#34; ;  &#10;&#32;&#32;&#32;&#32;rdfs:domain &lowbar;:ne40dc74ed8c748d3820673c82c8bc905b1,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#60;http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#Method>,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:Thing,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;:CheckMethod,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;:NumericalCheckMethod ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy :check&lowbar;method,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;:check&lowbar;method&lowbar;comparators ;  &#10;&#32;&#32;&#32;&#32;rdfs:range &lowbar;:ne40dc74ed8c748d3820673c82c8bc905b1,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&lowbar;:ne40dc74ed8c748d3820673c82c8bc905b2,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&lowbar;:ne40dc74ed8c748d3820673c82c8bc905b3,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#60;http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#Method>,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:Thing,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;skos:Concept,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;:CheckMethod,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;:CheckMethodComparator ;  &#10;&#32;&#32;&#32;&#32;rdfs:subPropertyOf :hasComparator,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;:hasDesign ;  &#10;&#32;&#32;&#32;&#32;owl:equivalentProperty :hasComparator .  &#10;&lowbar;:ne40dc74ed8c748d3820673c82c8bc905b4 rdf:first :CheckMethod ;  &#10;&#32;&#32;&#32;&#32;rdf:rest () .  &#10;&lowbar;:ne40dc74ed8c748d3820673c82c8bc905b5 rdf:first :Property ;  &#10;&#32;&#32;&#32;&#32;rdf:rest &lowbar;:ne40dc74ed8c748d3820673c82c8bc905b4 .  &#10;&lowbar;:ne40dc74ed8c748d3820673c82c8bc905b6 rdf:first skos:Concept ;  &#10;&#32;&#32;&#32;&#32;rdf:rest ( &lowbar;:ne40dc74ed8c748d3820673c82c8bc905b2 ) .  &#10;&lowbar;:ne40dc74ed8c748d3820673c82c8bc905b8 rdf:first :FeatureOfInterest ;  &#10;&#32;&#32;&#32;&#32;rdf:rest &lowbar;:ne40dc74ed8c748d3820673c82c8bc905b5 .  &#10;&lowbar;:ne40dc74ed8c748d3820673c82c8bc905b3 rdfs:subClassOf &lowbar;:ne40dc74ed8c748d3820673c82c8bc905b1,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&lowbar;:ne40dc74ed8c748d3820673c82c8bc905b2,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&lowbar;:ne40dc74ed8c748d3820673c82c8bc905b3,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#60;http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#Method>,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:Thing,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;skos:Concept,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;:CheckMethod,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;:CheckMethodComparator ;  &#10;&#32;&#32;&#32;&#32;owl:equivalentClass :CheckMethodComparator ;  &#10;&#32;&#32;&#32;&#32;owl:intersectionOf &lowbar;:ne40dc74ed8c748d3820673c82c8bc905b6 .  &#10;&lowbar;:ne40dc74ed8c748d3820673c82c8bc905b2 a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;owl:hasValue :CheckMethodComparatorNomenclature ;  &#10;&#32;&#32;&#32;&#32;owl:onProperty skos:inScheme .  &#10;&lowbar;:ne40dc74ed8c748d3820673c82c8bc905b1 a owl:Class ;  &#10;&#32;&#32;&#32;&#32;rdfs:subClassOf &lowbar;:ne40dc74ed8c748d3820673c82c8bc905b1,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:Thing ;  &#10;&#32;&#32;&#32;&#32;owl:equivalentClass &lowbar;:ne40dc74ed8c748d3820673c82c8bc905b1 ;  &#10;&#32;&#32;&#32;&#32;owl:unionOf &lowbar;:ne40dc74ed8c748d3820673c82c8bc905b8 .</code></pre>|
|[Section top](#minorfail-outcome-number-119)|Pointer|<pre lang="Turtle"><code>:hasUnit a owl:FunctionalProperty,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:ObjectProperty ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;hasUnit&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:comment &#34;the hasUnit property is used to link a specific property or ...&#34; ;  &#10;&#32;&#32;&#32;&#32;rdfs:domain &lowbar;:ndf4a0a76c5994e87b2c1dcfe0f52d4deb1,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:Thing ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy :check&lowbar;method ;  &#10;&#32;&#32;&#32;&#32;rdfs:range qudt:Unit ;  &#10;&#32;&#32;&#32;&#32;rdfs:subPropertyOf :hasUnit ;  &#10;&#32;&#32;&#32;&#32;owl:eqivalentProperty qudt:hasValue ;  &#10;&#32;&#32;&#32;&#32;owl:equivalentProperty :hasUnit .  &#10;&lowbar;:ndf4a0a76c5994e87b2c1dcfe0f52d4deb2 rdf:first :CheckMethod ;  &#10;&#32;&#32;&#32;&#32;rdf:rest () .  &#10;&lowbar;:ndf4a0a76c5994e87b2c1dcfe0f52d4deb3 rdf:first :Property ;  &#10;&#32;&#32;&#32;&#32;rdf:rest &lowbar;:ndf4a0a76c5994e87b2c1dcfe0f52d4deb2 .  &#10;&lowbar;:ndf4a0a76c5994e87b2c1dcfe0f52d4deb4 rdf:first :FeatureOfInterest ;  &#10;&#32;&#32;&#32;&#32;rdf:rest &lowbar;:ndf4a0a76c5994e87b2c1dcfe0f52d4deb3 .  &#10;&lowbar;:ndf4a0a76c5994e87b2c1dcfe0f52d4deb1 a owl:Class ;  &#10;&#32;&#32;&#32;&#32;rdfs:subClassOf &lowbar;:ndf4a0a76c5994e87b2c1dcfe0f52d4deb1,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:Thing ;  &#10;&#32;&#32;&#32;&#32;owl:equivalentClass &lowbar;:ndf4a0a76c5994e87b2c1dcfe0f52d4deb1 ;  &#10;&#32;&#32;&#32;&#32;owl:unionOf &lowbar;:ndf4a0a76c5994e87b2c1dcfe0f52d4deb4 .</code></pre>|
|[Section top](#minorfail-outcome-number-119)|Pointer|<pre lang="Turtle"><code></code></pre>|
|[Section top](#minorfail-outcome-number-119)|Pointer|<pre lang="Turtle"><code>:hasOperator a owl:FunctionalProperty,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:ObjectProperty ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;has operator&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:comment &#34;Links a boolean check method to the check method operator it...&#34;,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#34;The operator of a feature of interest or a property of that ...&#34; ;  &#10;&#32;&#32;&#32;&#32;rdfs:domain &lowbar;:nfba9e3bc408648f482489c0aafd8a71db1,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#60;http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#Method>,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:Thing,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;:BooleanCheckMethod,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;:CheckMethod ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy :check&lowbar;method,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;:check&lowbar;method&lowbar;Operators ;  &#10;&#32;&#32;&#32;&#32;rdfs:range &lowbar;:nfba9e3bc408648f482489c0aafd8a71db1,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&lowbar;:nfba9e3bc408648f482489c0aafd8a71db2,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&lowbar;:nfba9e3bc408648f482489c0aafd8a71db3,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#60;http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#Method>,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:Thing,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;skos:Concept,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;:CheckMethod,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;:CheckMethodOperator ;  &#10;&#32;&#32;&#32;&#32;rdfs:subPropertyOf :hasDesign,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;:hasOperator ;  &#10;&#32;&#32;&#32;&#32;owl:equivalentProperty :hasOperator .  &#10;&lowbar;:nfba9e3bc408648f482489c0aafd8a71db4 rdf:first skos:Concept ;  &#10;&#32;&#32;&#32;&#32;rdf:rest ( &lowbar;:nfba9e3bc408648f482489c0aafd8a71db2 ) .  &#10;&lowbar;:nfba9e3bc408648f482489c0aafd8a71db6 rdf:first :CheckMethod ;  &#10;&#32;&#32;&#32;&#32;rdf:rest () .  &#10;&lowbar;:nfba9e3bc408648f482489c0aafd8a71db7 rdf:first :Property ;  &#10;&#32;&#32;&#32;&#32;rdf:rest &lowbar;:nfba9e3bc408648f482489c0aafd8a71db6 .  &#10;&lowbar;:nfba9e3bc408648f482489c0aafd8a71db8 rdf:first :FeatureOfInterest ;  &#10;&#32;&#32;&#32;&#32;rdf:rest &lowbar;:nfba9e3bc408648f482489c0aafd8a71db7 .  &#10;&lowbar;:nfba9e3bc408648f482489c0aafd8a71db3 rdfs:subClassOf &lowbar;:nfba9e3bc408648f482489c0aafd8a71db1,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&lowbar;:nfba9e3bc408648f482489c0aafd8a71db2,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&lowbar;:nfba9e3bc408648f482489c0aafd8a71db3,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#60;http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#Method>,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:Thing,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;skos:Concept,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;:CheckMethod,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;:CheckMethodOperator ;  &#10;&#32;&#32;&#32;&#32;owl:equivalentClass :CheckMethodOperator ;  &#10;&#32;&#32;&#32;&#32;owl:intersectionOf &lowbar;:nfba9e3bc408648f482489c0aafd8a71db4 .  &#10;&lowbar;:nfba9e3bc408648f482489c0aafd8a71db2 a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;owl:hasValue :CheckMethodOperatorNomenclature ;  &#10;&#32;&#32;&#32;&#32;owl:onProperty skos:inScheme .  &#10;&lowbar;:nfba9e3bc408648f482489c0aafd8a71db1 a owl:Class ;  &#10;&#32;&#32;&#32;&#32;rdfs:subClassOf &lowbar;:nfba9e3bc408648f482489c0aafd8a71db1,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:Thing ;  &#10;&#32;&#32;&#32;&#32;owl:equivalentClass &lowbar;:nfba9e3bc408648f482489c0aafd8a71db1 ;  &#10;&#32;&#32;&#32;&#32;owl:unionOf &lowbar;:nfba9e3bc408648f482489c0aafd8a71db8 .</code></pre>|
|[Section top](#minorfail-outcome-number-119)|Pointer|<pre lang="Turtle"><code>:hasOperator a owl:FunctionalProperty,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:ObjectProperty ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;has operator&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:comment &#34;Links a boolean check method to the check method operator it...&#34;,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#34;The operator of a feature of interest or a property of that ...&#34; ;  &#10;&#32;&#32;&#32;&#32;rdfs:domain &lowbar;:n19c59d80dca945f1a90e573e024cc861b1,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#60;http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#Method>,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:Thing,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;:BooleanCheckMethod,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;:CheckMethod ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy :check&lowbar;method,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;:check&lowbar;method&lowbar;Operators ;  &#10;&#32;&#32;&#32;&#32;rdfs:range &lowbar;:n19c59d80dca945f1a90e573e024cc861b1,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&lowbar;:n19c59d80dca945f1a90e573e024cc861b2,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&lowbar;:n19c59d80dca945f1a90e573e024cc861b3,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#60;http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#Method>,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:Thing,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;skos:Concept,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;:CheckMethod,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;:CheckMethodOperator ;  &#10;&#32;&#32;&#32;&#32;rdfs:subPropertyOf :hasDesign,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;:hasOperator ;  &#10;&#32;&#32;&#32;&#32;owl:equivalentProperty :hasOperator .  &#10;&lowbar;:n19c59d80dca945f1a90e573e024cc861b4 rdf:first skos:Concept ;  &#10;&#32;&#32;&#32;&#32;rdf:rest ( &lowbar;:n19c59d80dca945f1a90e573e024cc861b2 ) .  &#10;&lowbar;:n19c59d80dca945f1a90e573e024cc861b6 rdf:first :CheckMethod ;  &#10;&#32;&#32;&#32;&#32;rdf:rest () .  &#10;&lowbar;:n19c59d80dca945f1a90e573e024cc861b7 rdf:first :Property ;  &#10;&#32;&#32;&#32;&#32;rdf:rest &lowbar;:n19c59d80dca945f1a90e573e024cc861b6 .  &#10;&lowbar;:n19c59d80dca945f1a90e573e024cc861b8 rdf:first :FeatureOfInterest ;  &#10;&#32;&#32;&#32;&#32;rdf:rest &lowbar;:n19c59d80dca945f1a90e573e024cc861b7 .  &#10;&lowbar;:n19c59d80dca945f1a90e573e024cc861b3 rdfs:subClassOf &lowbar;:n19c59d80dca945f1a90e573e024cc861b1,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&lowbar;:n19c59d80dca945f1a90e573e024cc861b2,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&lowbar;:n19c59d80dca945f1a90e573e024cc861b3,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#60;http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#Method>,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:Thing,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;skos:Concept,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;:CheckMethod,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;:CheckMethodOperator ;  &#10;&#32;&#32;&#32;&#32;owl:equivalentClass :CheckMethodOperator ;  &#10;&#32;&#32;&#32;&#32;owl:intersectionOf &lowbar;:n19c59d80dca945f1a90e573e024cc861b4 .  &#10;&lowbar;:n19c59d80dca945f1a90e573e024cc861b2 a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;owl:hasValue :CheckMethodOperatorNomenclature ;  &#10;&#32;&#32;&#32;&#32;owl:onProperty skos:inScheme .  &#10;&lowbar;:n19c59d80dca945f1a90e573e024cc861b1 a owl:Class ;  &#10;&#32;&#32;&#32;&#32;rdfs:subClassOf &lowbar;:n19c59d80dca945f1a90e573e024cc861b1,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:Thing ;  &#10;&#32;&#32;&#32;&#32;owl:equivalentClass &lowbar;:n19c59d80dca945f1a90e573e024cc861b1 ;  &#10;&#32;&#32;&#32;&#32;owl:unionOf &lowbar;:n19c59d80dca945f1a90e573e024cc861b8 .</code></pre>|
|[Section top](#minorfail-outcome-number-119)|Pointer|<pre lang="Turtle"><code>:hasNestedTarget a owl:ObjectProperty ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;hasNestedTarget&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:comment &#34;&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy :check&lowbar;method ;  &#10;&#32;&#32;&#32;&#32;rdfs:range &lowbar;:n88fc041a99b14f229e20c5ed28e120acb1,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#60;http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#Method>,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:Thing,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;:CheckMethod ;  &#10;&#32;&#32;&#32;&#32;rdfs:subPropertyOf :hasNestedTarget ;  &#10;&#32;&#32;&#32;&#32;owl:equivalentProperty :hasNestedTarget .  &#10;&lowbar;:n88fc041a99b14f229e20c5ed28e120acb2 rdf:first :CheckMethod ;  &#10;&#32;&#32;&#32;&#32;rdf:rest () .  &#10;&lowbar;:n88fc041a99b14f229e20c5ed28e120acb3 rdf:first :Property ;  &#10;&#32;&#32;&#32;&#32;rdf:rest &lowbar;:n88fc041a99b14f229e20c5ed28e120acb2 .  &#10;&lowbar;:n88fc041a99b14f229e20c5ed28e120acb4 rdf:first :FeatureOfInterest ;  &#10;&#32;&#32;&#32;&#32;rdf:rest &lowbar;:n88fc041a99b14f229e20c5ed28e120acb3 .  &#10;&lowbar;:n88fc041a99b14f229e20c5ed28e120acb1 a owl:Class ;  &#10;&#32;&#32;&#32;&#32;rdfs:subClassOf &lowbar;:n88fc041a99b14f229e20c5ed28e120acb1,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:Thing ;  &#10;&#32;&#32;&#32;&#32;owl:equivalentClass &lowbar;:n88fc041a99b14f229e20c5ed28e120acb1 ;  &#10;&#32;&#32;&#32;&#32;owl:unionOf &lowbar;:n88fc041a99b14f229e20c5ed28e120acb4 .</code></pre>|
|[Section top](#minorfail-outcome-number-119)|Pointer|<pre lang="Turtle"><code>:hasFormat a owl:ObjectProperty ;  &#10;&#32;&#32;&#32;&#32;rdfs:comment &#34;Defines the format of an evidence, which is of type dct:form...&#34; ;  &#10;&#32;&#32;&#32;&#32;rdfs:domain &#91; a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:allValuesFrom :DocumentSubdivision ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:onProperty :hasSubdivision ],  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#91; owl:unionOf ( :Document :DocumentSubdivision ) ],  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:Thing,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;:DocumentSubdivision,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;:Statement ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy :evidence ;  &#10;&#32;&#32;&#32;&#32;rdfs:range dc:format ;  &#10;&#32;&#32;&#32;&#32;rdfs:subPropertyOf :hasFormat ;  &#10;&#32;&#32;&#32;&#32;owl:equivalentProperty :hasFormat ;  &#10;&#32;&#32;&#32;&#32;owl:sameAs :hasFormat ;  &#10;&#32;&#32;&#32;&#32;skos:example &#34;an image, a drawing or a model can be an evidence.&#34;@en .</code></pre>|
|[Section top](#minorfail-outcome-number-119)|Pointer|<pre lang="Turtle"><code>:hasProperty a owl:ObjectProperty ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;has Property&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:comment &#34;Links a feature of interest to one of its aspect that is int...&#34; ;  &#10;&#32;&#32;&#32;&#32;rdfs:domain &lowbar;:nb13a306a488849a9b961001647f83bf8b1,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#60;http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#Object>,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:Thing,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#60;https://saref.etsi.org/core/FeatureOfInterest>,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;:FeatureOfInterest ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy :feature&lowbar;of&lowbar;interest ;  &#10;&#32;&#32;&#32;&#32;rdfs:range &lowbar;:nb13a306a488849a9b961001647f83bf8b1,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#60;http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#Quality>,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:Thing,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;:Property ;  &#10;&#32;&#32;&#32;&#32;rdfs:subPropertyOf :hasProperty ;  &#10;&#32;&#32;&#32;&#32;owl:equivalentProperty :hasProperty ;  &#10;&#32;&#32;&#32;&#32;owl:sameAs :hasProperty ;  &#10;&#32;&#32;&#32;&#32;skos:example &#34;Links a space to the area property of that space, a wall to ...&#34; .  &#10;&lowbar;:nb13a306a488849a9b961001647f83bf8b2 rdf:first :CheckMethod ;  &#10;&#32;&#32;&#32;&#32;rdf:rest () .  &#10;&lowbar;:nb13a306a488849a9b961001647f83bf8b3 rdf:first :Property ;  &#10;&#32;&#32;&#32;&#32;rdf:rest &lowbar;:nb13a306a488849a9b961001647f83bf8b2 .  &#10;&lowbar;:nb13a306a488849a9b961001647f83bf8b4 rdf:first :FeatureOfInterest ;  &#10;&#32;&#32;&#32;&#32;rdf:rest &lowbar;:nb13a306a488849a9b961001647f83bf8b3 .  &#10;&lowbar;:nb13a306a488849a9b961001647f83bf8b1 a owl:Class ;  &#10;&#32;&#32;&#32;&#32;rdfs:subClassOf &lowbar;:nb13a306a488849a9b961001647f83bf8b1,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:Thing ;  &#10;&#32;&#32;&#32;&#32;owl:equivalentClass &lowbar;:nb13a306a488849a9b961001647f83bf8b1 ;  &#10;&#32;&#32;&#32;&#32;owl:unionOf &lowbar;:nb13a306a488849a9b961001647f83bf8b4 .</code></pre>|
|[Section top](#minorfail-outcome-number-119)|Pointer|<pre lang="Turtle"><code>:hasQuantityKind a owl:ObjectProperty ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;has quantity kind&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:comment &#34;Links a property to its quantity kind&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:domain &lowbar;:n335f3ddf1ee94faca54c78ca5b04eefeb1,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#60;http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#Quality>,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:Thing,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;:Property ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy :feature&lowbar;of&lowbar;interest ;  &#10;&#32;&#32;&#32;&#32;rdfs:range &lowbar;:n335f3ddf1ee94faca54c78ca5b04eefeb2,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&lowbar;:n335f3ddf1ee94faca54c78ca5b04eefeb3,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;qudt:QuantityKind,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#60;http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#Region>,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:Thing,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;skos:Concept,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;:QuantityKind ;  &#10;&#32;&#32;&#32;&#32;rdfs:subPropertyOf :hasQuantityKind ;  &#10;&#32;&#32;&#32;&#32;owl:equivalentProperty :hasQuantityKind ;  &#10;&#32;&#32;&#32;&#32;owl:sameAs :hasQuantityKind ;  &#10;&#32;&#32;&#32;&#32;skos:example &#34;A space area property to the property kind &#92;&#34;area&#92;&#34;.&#34;@en .  &#10;&lowbar;:n335f3ddf1ee94faca54c78ca5b04eefeb4 rdf:first skos:Concept ;  &#10;&#32;&#32;&#32;&#32;rdf:rest ( &lowbar;:n335f3ddf1ee94faca54c78ca5b04eefeb2 ) .  &#10;&lowbar;:n335f3ddf1ee94faca54c78ca5b04eefeb6 rdf:first :CheckMethod ;  &#10;&#32;&#32;&#32;&#32;rdf:rest () .  &#10;&lowbar;:n335f3ddf1ee94faca54c78ca5b04eefeb7 rdf:first :Property ;  &#10;&#32;&#32;&#32;&#32;rdf:rest &lowbar;:n335f3ddf1ee94faca54c78ca5b04eefeb6 .  &#10;&lowbar;:n335f3ddf1ee94faca54c78ca5b04eefeb8 rdf:first :FeatureOfInterest ;  &#10;&#32;&#32;&#32;&#32;rdf:rest &lowbar;:n335f3ddf1ee94faca54c78ca5b04eefeb7 .  &#10;&lowbar;:n335f3ddf1ee94faca54c78ca5b04eefeb3 rdfs:subClassOf &lowbar;:n335f3ddf1ee94faca54c78ca5b04eefeb2,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&lowbar;:n335f3ddf1ee94faca54c78ca5b04eefeb3,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;qudt:QuantityKind,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#60;http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#Region>,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:Thing,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;skos:Concept,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;:QuantityKind ;  &#10;&#32;&#32;&#32;&#32;owl:equivalentClass :QuantityKind ;  &#10;&#32;&#32;&#32;&#32;owl:intersectionOf &lowbar;:n335f3ddf1ee94faca54c78ca5b04eefeb4 .  &#10;&lowbar;:n335f3ddf1ee94faca54c78ca5b04eefeb1 a owl:Class ;  &#10;&#32;&#32;&#32;&#32;rdfs:subClassOf &lowbar;:n335f3ddf1ee94faca54c78ca5b04eefeb1,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:Thing ;  &#10;&#32;&#32;&#32;&#32;owl:equivalentClass &lowbar;:n335f3ddf1ee94faca54c78ca5b04eefeb1 ;  &#10;&#32;&#32;&#32;&#32;owl:unionOf &lowbar;:n335f3ddf1ee94faca54c78ca5b04eefeb8 .  &#10;&lowbar;:n335f3ddf1ee94faca54c78ca5b04eefeb2 a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;owl:hasValue :QuantityKindNomenclature ;  &#10;&#32;&#32;&#32;&#32;owl:onProperty skos:inScheme .</code></pre>|
|[Section top](#minorfail-outcome-number-119)|Pointer|<pre lang="Turtle"><code>:hasQuantityKind a owl:ObjectProperty ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;has quantity kind&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:comment &#34;Links a property to its quantity kind&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:domain &lowbar;:n34d6c30a27bc4bf184ea673629b38be2b1,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#60;http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#Quality>,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:Thing,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;:Property ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy :feature&lowbar;of&lowbar;interest ;  &#10;&#32;&#32;&#32;&#32;rdfs:range &lowbar;:n34d6c30a27bc4bf184ea673629b38be2b2,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&lowbar;:n34d6c30a27bc4bf184ea673629b38be2b3,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;qudt:QuantityKind,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#60;http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#Region>,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:Thing,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;skos:Concept,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;:QuantityKind ;  &#10;&#32;&#32;&#32;&#32;rdfs:subPropertyOf :hasQuantityKind ;  &#10;&#32;&#32;&#32;&#32;owl:equivalentProperty :hasQuantityKind ;  &#10;&#32;&#32;&#32;&#32;owl:sameAs :hasQuantityKind ;  &#10;&#32;&#32;&#32;&#32;skos:example &#34;A space area property to the property kind &#92;&#34;area&#92;&#34;.&#34;@en .  &#10;&lowbar;:n34d6c30a27bc4bf184ea673629b38be2b4 rdf:first skos:Concept ;  &#10;&#32;&#32;&#32;&#32;rdf:rest ( &lowbar;:n34d6c30a27bc4bf184ea673629b38be2b2 ) .  &#10;&lowbar;:n34d6c30a27bc4bf184ea673629b38be2b6 rdf:first :CheckMethod ;  &#10;&#32;&#32;&#32;&#32;rdf:rest () .  &#10;&lowbar;:n34d6c30a27bc4bf184ea673629b38be2b7 rdf:first :Property ;  &#10;&#32;&#32;&#32;&#32;rdf:rest &lowbar;:n34d6c30a27bc4bf184ea673629b38be2b6 .  &#10;&lowbar;:n34d6c30a27bc4bf184ea673629b38be2b8 rdf:first :FeatureOfInterest ;  &#10;&#32;&#32;&#32;&#32;rdf:rest &lowbar;:n34d6c30a27bc4bf184ea673629b38be2b7 .  &#10;&lowbar;:n34d6c30a27bc4bf184ea673629b38be2b3 rdfs:subClassOf &lowbar;:n34d6c30a27bc4bf184ea673629b38be2b2,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&lowbar;:n34d6c30a27bc4bf184ea673629b38be2b3,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;qudt:QuantityKind,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#60;http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#Region>,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:Thing,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;skos:Concept,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;:QuantityKind ;  &#10;&#32;&#32;&#32;&#32;owl:equivalentClass :QuantityKind ;  &#10;&#32;&#32;&#32;&#32;owl:intersectionOf &lowbar;:n34d6c30a27bc4bf184ea673629b38be2b4 .  &#10;&lowbar;:n34d6c30a27bc4bf184ea673629b38be2b1 a owl:Class ;  &#10;&#32;&#32;&#32;&#32;rdfs:subClassOf &lowbar;:n34d6c30a27bc4bf184ea673629b38be2b1,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:Thing ;  &#10;&#32;&#32;&#32;&#32;owl:equivalentClass &lowbar;:n34d6c30a27bc4bf184ea673629b38be2b1 ;  &#10;&#32;&#32;&#32;&#32;owl:unionOf &lowbar;:n34d6c30a27bc4bf184ea673629b38be2b8 .  &#10;&lowbar;:n34d6c30a27bc4bf184ea673629b38be2b2 a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;owl:hasValue :QuantityKindNomenclature ;  &#10;&#32;&#32;&#32;&#32;owl:onProperty skos:inScheme .</code></pre>|
|[Section top](#minorfail-outcome-number-119)|Pointer|<pre lang="Turtle"><code>:Region owl:sameAs :Region .</code></pre>|
|[Section top](#minorfail-outcome-number-119)|Pointer|<pre lang="Turtle"><code>:hasQuantityKind a owl:ObjectProperty ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;has quantity kind&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:comment &#34;Links a property to its quantity kind&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:domain &lowbar;:nc4e215a522e4447ab34c8eb7516a2031b1,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#60;http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#Quality>,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:Thing,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;:Property ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy :feature&lowbar;of&lowbar;interest ;  &#10;&#32;&#32;&#32;&#32;rdfs:range &lowbar;:nc4e215a522e4447ab34c8eb7516a2031b2,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&lowbar;:nc4e215a522e4447ab34c8eb7516a2031b3,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;qudt:QuantityKind,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#60;http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#Region>,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:Thing,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;skos:Concept,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;:QuantityKind ;  &#10;&#32;&#32;&#32;&#32;rdfs:subPropertyOf :hasQuantityKind ;  &#10;&#32;&#32;&#32;&#32;owl:equivalentProperty :hasQuantityKind ;  &#10;&#32;&#32;&#32;&#32;owl:sameAs :hasQuantityKind ;  &#10;&#32;&#32;&#32;&#32;skos:example &#34;A space area property to the property kind &#92;&#34;area&#92;&#34;.&#34;@en .  &#10;&lowbar;:nc4e215a522e4447ab34c8eb7516a2031b4 rdf:first skos:Concept ;  &#10;&#32;&#32;&#32;&#32;rdf:rest ( &lowbar;:nc4e215a522e4447ab34c8eb7516a2031b2 ) .  &#10;&lowbar;:nc4e215a522e4447ab34c8eb7516a2031b6 rdf:first :CheckMethod ;  &#10;&#32;&#32;&#32;&#32;rdf:rest () .  &#10;&lowbar;:nc4e215a522e4447ab34c8eb7516a2031b7 rdf:first :Property ;  &#10;&#32;&#32;&#32;&#32;rdf:rest &lowbar;:nc4e215a522e4447ab34c8eb7516a2031b6 .  &#10;&lowbar;:nc4e215a522e4447ab34c8eb7516a2031b8 rdf:first :FeatureOfInterest ;  &#10;&#32;&#32;&#32;&#32;rdf:rest &lowbar;:nc4e215a522e4447ab34c8eb7516a2031b7 .  &#10;&lowbar;:nc4e215a522e4447ab34c8eb7516a2031b3 rdfs:subClassOf &lowbar;:nc4e215a522e4447ab34c8eb7516a2031b2,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&lowbar;:nc4e215a522e4447ab34c8eb7516a2031b3,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;qudt:QuantityKind,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#60;http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#Region>,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:Thing,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;skos:Concept,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;:QuantityKind ;  &#10;&#32;&#32;&#32;&#32;owl:equivalentClass :QuantityKind ;  &#10;&#32;&#32;&#32;&#32;owl:intersectionOf &lowbar;:nc4e215a522e4447ab34c8eb7516a2031b4 .  &#10;&lowbar;:nc4e215a522e4447ab34c8eb7516a2031b1 a owl:Class ;  &#10;&#32;&#32;&#32;&#32;rdfs:subClassOf &lowbar;:nc4e215a522e4447ab34c8eb7516a2031b1,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:Thing ;  &#10;&#32;&#32;&#32;&#32;owl:equivalentClass &lowbar;:nc4e215a522e4447ab34c8eb7516a2031b1 ;  &#10;&#32;&#32;&#32;&#32;owl:unionOf &lowbar;:nc4e215a522e4447ab34c8eb7516a2031b8 .  &#10;&lowbar;:nc4e215a522e4447ab34c8eb7516a2031b2 a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;owl:hasValue :QuantityKindNomenclature ;  &#10;&#32;&#32;&#32;&#32;owl:onProperty skos:inScheme .</code></pre>|
|[Section top](#minorfail-outcome-number-119)|Pointer|<pre lang="Turtle"><code>:QuantityKind a owl:Class ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy &#60;http://qudt.org/2.1/schema/qudt> ;  &#10;&#32;&#32;&#32;&#32;rdfs:subClassOf :QuantityKind,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:Thing ;  &#10;&#32;&#32;&#32;&#32;owl:equivalentClass :QuantityKind ;  &#10;&#32;&#32;&#32;&#32;owl:sameAs :QuantityKind .</code></pre>|
|[Section top](#minorfail-outcome-number-119)|Pointer|<pre lang="Turtle"><code>:forAdministrativeArea a owl:ObjectProperty ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;for administrative area&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:comment &#34;&#34;&#34;The administrative area for which something applies.&#92;r  &#10;A se...&#34;&#34;&#34; ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy :administrative&lowbar;areas ;  &#10;&#32;&#32;&#32;&#32;rdfs:range &lowbar;:nca8b0d63bf444b569a8f842af64a0061b1,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&lowbar;:nca8b0d63bf444b569a8f842af64a0061b2,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&lowbar;:nca8b0d63bf444b569a8f842af64a0061b3,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#60;http://data.europa.eu/eli/ontology#AdministrativeArea>,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:Thing,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;skos:Concept,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;:AdministrativeArea ;  &#10;&#32;&#32;&#32;&#32;rdfs:subPropertyOf :forAdministrativeArea ;  &#10;&#32;&#32;&#32;&#32;owl:equivalentProperty :forAdministrativeArea ;  &#10;&#32;&#32;&#32;&#32;owl:sameAs :forAdministrativeArea .  &#10;&lowbar;:nca8b0d63bf444b569a8f842af64a0061b4 rdf:first :AdministrativeArea ;  &#10;&#32;&#32;&#32;&#32;rdf:rest () .  &#10;&lowbar;:nca8b0d63bf444b569a8f842af64a0061b5 rdf:first &#60;https://schema.org/Place> ;  &#10;&#32;&#32;&#32;&#32;rdf:rest &lowbar;:nca8b0d63bf444b569a8f842af64a0061b4 .  &#10;&lowbar;:nca8b0d63bf444b569a8f842af64a0061b6 rdf:first &lowbar;:nca8b0d63bf444b569a8f842af64a0061b2 ;  &#10;&#32;&#32;&#32;&#32;rdf:rest () .  &#10;&lowbar;:nca8b0d63bf444b569a8f842af64a0061b7 rdf:first skos:Concept ;  &#10;&#32;&#32;&#32;&#32;rdf:rest &lowbar;:nca8b0d63bf444b569a8f842af64a0061b6 .  &#10;&lowbar;:nca8b0d63bf444b569a8f842af64a0061b3 rdfs:subClassOf &lowbar;:nca8b0d63bf444b569a8f842af64a0061b1,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&lowbar;:nca8b0d63bf444b569a8f842af64a0061b2,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&lowbar;:nca8b0d63bf444b569a8f842af64a0061b3,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#60;http://data.europa.eu/eli/ontology#AdministrativeArea>,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:Thing,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;skos:Concept,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;:AdministrativeArea ;  &#10;&#32;&#32;&#32;&#32;owl:equivalentClass &#60;http://data.europa.eu/eli/ontology#AdministrativeArea>,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;:AdministrativeArea ;  &#10;&#32;&#32;&#32;&#32;owl:intersectionOf &lowbar;:nca8b0d63bf444b569a8f842af64a0061b7 .  &#10;&lowbar;:nca8b0d63bf444b569a8f842af64a0061b2 a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;owl:hasValue :AdministrativeAreaNomenclature ;  &#10;&#32;&#32;&#32;&#32;owl:onProperty skos:inScheme .  &#10;&lowbar;:nca8b0d63bf444b569a8f842af64a0061b1 a owl:Class ;  &#10;&#32;&#32;&#32;&#32;rdfs:subClassOf &lowbar;:nca8b0d63bf444b569a8f842af64a0061b1,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:Thing ;  &#10;&#32;&#32;&#32;&#32;owl:equivalentClass &lowbar;:nca8b0d63bf444b569a8f842af64a0061b1 ;  &#10;&#32;&#32;&#32;&#32;owl:unionOf &lowbar;:nca8b0d63bf444b569a8f842af64a0061b5 .</code></pre>|
|[Section top](#minorfail-outcome-number-119)|Pointer|<pre lang="Turtle"><code>:forAdministrativeArea a owl:ObjectProperty ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;for administrative area&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:comment &#34;&#34;&#34;The administrative area for which something applies.&#92;r  &#10;A se...&#34;&#34;&#34; ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy :administrative&lowbar;areas ;  &#10;&#32;&#32;&#32;&#32;rdfs:range &lowbar;:nd6fb1146f8af46c9a338c83837bbece8b1,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&lowbar;:nd6fb1146f8af46c9a338c83837bbece8b2,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&lowbar;:nd6fb1146f8af46c9a338c83837bbece8b3,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#60;http://data.europa.eu/eli/ontology#AdministrativeArea>,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:Thing,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;skos:Concept,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;:AdministrativeArea ;  &#10;&#32;&#32;&#32;&#32;rdfs:subPropertyOf :forAdministrativeArea ;  &#10;&#32;&#32;&#32;&#32;owl:equivalentProperty :forAdministrativeArea ;  &#10;&#32;&#32;&#32;&#32;owl:sameAs :forAdministrativeArea .  &#10;&lowbar;:nd6fb1146f8af46c9a338c83837bbece8b4 rdf:first :AdministrativeArea ;  &#10;&#32;&#32;&#32;&#32;rdf:rest () .  &#10;&lowbar;:nd6fb1146f8af46c9a338c83837bbece8b5 rdf:first &#60;https://schema.org/Place> ;  &#10;&#32;&#32;&#32;&#32;rdf:rest &lowbar;:nd6fb1146f8af46c9a338c83837bbece8b4 .  &#10;&lowbar;:nd6fb1146f8af46c9a338c83837bbece8b6 rdf:first &lowbar;:nd6fb1146f8af46c9a338c83837bbece8b2 ;  &#10;&#32;&#32;&#32;&#32;rdf:rest () .  &#10;&lowbar;:nd6fb1146f8af46c9a338c83837bbece8b7 rdf:first skos:Concept ;  &#10;&#32;&#32;&#32;&#32;rdf:rest &lowbar;:nd6fb1146f8af46c9a338c83837bbece8b6 .  &#10;&lowbar;:nd6fb1146f8af46c9a338c83837bbece8b3 rdfs:subClassOf &lowbar;:nd6fb1146f8af46c9a338c83837bbece8b1,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&lowbar;:nd6fb1146f8af46c9a338c83837bbece8b2,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&lowbar;:nd6fb1146f8af46c9a338c83837bbece8b3,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#60;http://data.europa.eu/eli/ontology#AdministrativeArea>,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:Thing,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;skos:Concept,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;:AdministrativeArea ;  &#10;&#32;&#32;&#32;&#32;owl:equivalentClass &#60;http://data.europa.eu/eli/ontology#AdministrativeArea>,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;:AdministrativeArea ;  &#10;&#32;&#32;&#32;&#32;owl:intersectionOf &lowbar;:nd6fb1146f8af46c9a338c83837bbece8b7 .  &#10;&lowbar;:nd6fb1146f8af46c9a338c83837bbece8b2 a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;owl:hasValue :AdministrativeAreaNomenclature ;  &#10;&#32;&#32;&#32;&#32;owl:onProperty skos:inScheme .  &#10;&lowbar;:nd6fb1146f8af46c9a338c83837bbece8b1 a owl:Class ;  &#10;&#32;&#32;&#32;&#32;rdfs:subClassOf &lowbar;:nd6fb1146f8af46c9a338c83837bbece8b1,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:Thing ;  &#10;&#32;&#32;&#32;&#32;owl:equivalentClass &lowbar;:nd6fb1146f8af46c9a338c83837bbece8b1 ;  &#10;&#32;&#32;&#32;&#32;owl:unionOf &lowbar;:nd6fb1146f8af46c9a338c83837bbece8b5 .</code></pre>|
|[Section top](#minorfail-outcome-number-119)|Pointer|<pre lang="Turtle"><code>:AdministrativeArea rdfs:subClassOf &lowbar;:n06348175fa584854bac83ef8592653ecb1,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&lowbar;:n06348175fa584854bac83ef8592653ecb2,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&lowbar;:n06348175fa584854bac83ef8592653ecb3,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;:AdministrativeArea,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:Thing,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;skos:Concept,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;aec3po:AdministrativeArea ;  &#10;&#32;&#32;&#32;&#32;owl:equivalentClass &lowbar;:n06348175fa584854bac83ef8592653ecb3,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;aec3po:AdministrativeArea ;  &#10;&#32;&#32;&#32;&#32;owl:sameAs :AdministrativeArea .  &#10;&lowbar;:n06348175fa584854bac83ef8592653ecb4 rdf:first aec3po:AdministrativeArea ;  &#10;&#32;&#32;&#32;&#32;rdf:rest () .  &#10;&lowbar;:n06348175fa584854bac83ef8592653ecb5 rdf:first &#60;https://schema.org/Place> ;  &#10;&#32;&#32;&#32;&#32;rdf:rest &lowbar;:n06348175fa584854bac83ef8592653ecb4 .  &#10;&lowbar;:n06348175fa584854bac83ef8592653ecb6 rdf:first &lowbar;:n06348175fa584854bac83ef8592653ecb2 ;  &#10;&#32;&#32;&#32;&#32;rdf:rest () .  &#10;&lowbar;:n06348175fa584854bac83ef8592653ecb7 rdf:first skos:Concept ;  &#10;&#32;&#32;&#32;&#32;rdf:rest &lowbar;:n06348175fa584854bac83ef8592653ecb6 .  &#10;&lowbar;:n06348175fa584854bac83ef8592653ecb2 a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;owl:hasValue aec3po:AdministrativeAreaNomenclature ;  &#10;&#32;&#32;&#32;&#32;owl:onProperty skos:inScheme .  &#10;&lowbar;:n06348175fa584854bac83ef8592653ecb3 rdfs:subClassOf &lowbar;:n06348175fa584854bac83ef8592653ecb1,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&lowbar;:n06348175fa584854bac83ef8592653ecb2,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&lowbar;:n06348175fa584854bac83ef8592653ecb3,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;:AdministrativeArea,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:Thing,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;skos:Concept,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;aec3po:AdministrativeArea ;  &#10;&#32;&#32;&#32;&#32;owl:equivalentClass :AdministrativeArea,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;aec3po:AdministrativeArea ;  &#10;&#32;&#32;&#32;&#32;owl:intersectionOf &lowbar;:n06348175fa584854bac83ef8592653ecb7 .  &#10;&lowbar;:n06348175fa584854bac83ef8592653ecb1 a owl:Class ;  &#10;&#32;&#32;&#32;&#32;rdfs:subClassOf &lowbar;:n06348175fa584854bac83ef8592653ecb1,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:Thing ;  &#10;&#32;&#32;&#32;&#32;owl:equivalentClass &lowbar;:n06348175fa584854bac83ef8592653ecb1 ;  &#10;&#32;&#32;&#32;&#32;owl:unionOf &lowbar;:n06348175fa584854bac83ef8592653ecb5 .</code></pre>|
|[Section top](#minorfail-outcome-number-119)|Pointer|<pre lang="Turtle"><code>:forBuildingStructure a owl:ObjectProperty ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;for building structure&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:comment &#34;The building structure for which a specific check, verifier,...&#34; ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy :building&lowbar;structure ;  &#10;&#32;&#32;&#32;&#32;rdfs:range &lowbar;:n70e49b9348ab464bb9ef52f9cf79d58bb1,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&lowbar;:n70e49b9348ab464bb9ef52f9cf79d58bb2,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:Thing,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;skos:Concept,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;:BuildingStructure,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;:Design ;  &#10;&#32;&#32;&#32;&#32;rdfs:subPropertyOf :forBuildingStructure,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;:forDesign ;  &#10;&#32;&#32;&#32;&#32;owl:equivalentProperty :forBuildingStructure .  &#10;&lowbar;:n70e49b9348ab464bb9ef52f9cf79d58bb3 rdf:first skos:Concept ;  &#10;&#32;&#32;&#32;&#32;rdf:rest ( &lowbar;:n70e49b9348ab464bb9ef52f9cf79d58bb1 ) .  &#10;&lowbar;:n70e49b9348ab464bb9ef52f9cf79d58bb2 rdfs:subClassOf &lowbar;:n70e49b9348ab464bb9ef52f9cf79d58bb1,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&lowbar;:n70e49b9348ab464bb9ef52f9cf79d58bb2,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:Thing,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;skos:Concept,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;:BuildingStructure,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;:Design ;  &#10;&#32;&#32;&#32;&#32;owl:equivalentClass :BuildingStructure ;  &#10;&#32;&#32;&#32;&#32;owl:intersectionOf &lowbar;:n70e49b9348ab464bb9ef52f9cf79d58bb3 .  &#10;&lowbar;:n70e49b9348ab464bb9ef52f9cf79d58bb1 a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;owl:hasValue :BuildingStructureNomenclature ;  &#10;&#32;&#32;&#32;&#32;owl:onProperty skos:inScheme .</code></pre>|
|[Section top](#minorfail-outcome-number-119)|Pointer|<pre lang="Turtle"><code>:hasBuildingStructure a owl:FunctionalProperty,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:ObjectProperty ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;has building structure&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:comment &#34;The building structure design of a feature of interest or a ...&#34; ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy :building&lowbar;structure ;  &#10;&#32;&#32;&#32;&#32;rdfs:range &lowbar;:n7649562336b94852a2089e82d9f0de4eb1,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&lowbar;:n7649562336b94852a2089e82d9f0de4eb2,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:Thing,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;skos:Concept,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;:BuildingStructure,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;:Design ;  &#10;&#32;&#32;&#32;&#32;rdfs:subPropertyOf :hasBuildingStructure,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;:hasDesign ;  &#10;&#32;&#32;&#32;&#32;owl:equivalentProperty :hasBuildingStructure .  &#10;&lowbar;:n7649562336b94852a2089e82d9f0de4eb3 rdf:first skos:Concept ;  &#10;&#32;&#32;&#32;&#32;rdf:rest ( &lowbar;:n7649562336b94852a2089e82d9f0de4eb1 ) .  &#10;&lowbar;:n7649562336b94852a2089e82d9f0de4eb2 rdfs:subClassOf &lowbar;:n7649562336b94852a2089e82d9f0de4eb1,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&lowbar;:n7649562336b94852a2089e82d9f0de4eb2,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:Thing,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;skos:Concept,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;:BuildingStructure,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;:Design ;  &#10;&#32;&#32;&#32;&#32;owl:equivalentClass :BuildingStructure ;  &#10;&#32;&#32;&#32;&#32;owl:intersectionOf &lowbar;:n7649562336b94852a2089e82d9f0de4eb3 .  &#10;&lowbar;:n7649562336b94852a2089e82d9f0de4eb1 a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;owl:hasValue :BuildingStructureNomenclature ;  &#10;&#32;&#32;&#32;&#32;owl:onProperty skos:inScheme .</code></pre>|
|[Section top](#minorfail-outcome-number-119)|Pointer|<pre lang="Turtle"><code>:forBuildingUsage a owl:ObjectProperty ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;for building usage&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:comment &#34;The building usage for which a specific check, verifier, or ...&#34; ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy :building&lowbar;usage ;  &#10;&#32;&#32;&#32;&#32;rdfs:range &lowbar;:n5420ea6684d24709a9596807096801d7b1,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&lowbar;:n5420ea6684d24709a9596807096801d7b2,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:Thing,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;skos:Concept,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;:BuildingUsage,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;:Design ;  &#10;&#32;&#32;&#32;&#32;rdfs:subPropertyOf :forBuildingUsage,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;:forDesign ;  &#10;&#32;&#32;&#32;&#32;owl:equivalentProperty :forBuildingUsage .  &#10;&lowbar;:n5420ea6684d24709a9596807096801d7b3 rdf:first skos:Concept ;  &#10;&#32;&#32;&#32;&#32;rdf:rest ( &lowbar;:n5420ea6684d24709a9596807096801d7b1 ) .  &#10;&lowbar;:n5420ea6684d24709a9596807096801d7b2 rdfs:subClassOf &lowbar;:n5420ea6684d24709a9596807096801d7b1,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&lowbar;:n5420ea6684d24709a9596807096801d7b2,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:Thing,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;skos:Concept,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;:BuildingUsage,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;:Design ;  &#10;&#32;&#32;&#32;&#32;owl:equivalentClass :BuildingUsage ;  &#10;&#32;&#32;&#32;&#32;owl:intersectionOf &lowbar;:n5420ea6684d24709a9596807096801d7b3 .  &#10;&lowbar;:n5420ea6684d24709a9596807096801d7b1 a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;owl:hasValue :BuildingUsageNomenclature ;  &#10;&#32;&#32;&#32;&#32;owl:onProperty skos:inScheme .</code></pre>|
|[Section top](#minorfail-outcome-number-119)|Pointer|<pre lang="Turtle"><code>:hasBuildingUsage a owl:FunctionalProperty,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:ObjectProperty ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;has building usage&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:comment &#34;The building usage design of a feature of interest or a prop...&#34; ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy :building&lowbar;usage ;  &#10;&#32;&#32;&#32;&#32;rdfs:range &lowbar;:n21448337cb1e4e9e80da4a3b18983262b1,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&lowbar;:n21448337cb1e4e9e80da4a3b18983262b2,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:Thing,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;skos:Concept,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;:BuildingUsage,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;:Design ;  &#10;&#32;&#32;&#32;&#32;rdfs:subPropertyOf :hasBuildingUsage,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;:hasDesign ;  &#10;&#32;&#32;&#32;&#32;owl:equivalentProperty :hasBuildingUsage .  &#10;&lowbar;:n21448337cb1e4e9e80da4a3b18983262b3 rdf:first skos:Concept ;  &#10;&#32;&#32;&#32;&#32;rdf:rest ( &lowbar;:n21448337cb1e4e9e80da4a3b18983262b1 ) .  &#10;&lowbar;:n21448337cb1e4e9e80da4a3b18983262b2 rdfs:subClassOf &lowbar;:n21448337cb1e4e9e80da4a3b18983262b1,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&lowbar;:n21448337cb1e4e9e80da4a3b18983262b2,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:Thing,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;skos:Concept,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;:BuildingUsage,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;:Design ;  &#10;&#32;&#32;&#32;&#32;owl:equivalentClass :BuildingUsage ;  &#10;&#32;&#32;&#32;&#32;owl:intersectionOf &lowbar;:n21448337cb1e4e9e80da4a3b18983262b3 .  &#10;&lowbar;:n21448337cb1e4e9e80da4a3b18983262b1 a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;owl:hasValue :BuildingUsageNomenclature ;  &#10;&#32;&#32;&#32;&#32;owl:onProperty skos:inScheme .</code></pre>|
|[Section top](#minorfail-outcome-number-119)|Pointer|<pre lang="Turtle"><code>:hasDiscipline a owl:ObjectProperty ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;has discipline&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:comment &#34;Links an entity (procedure, statement, verifier, ...) to the...&#34; ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy :discipline ;  &#10;&#32;&#32;&#32;&#32;rdfs:range &lowbar;:nd9fda1f51cee4e2a8bec860f1c9842f3b1,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&lowbar;:nd9fda1f51cee4e2a8bec860f1c9842f3b2,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:Thing,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;skos:Concept,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;:Discipline ;  &#10;&#32;&#32;&#32;&#32;rdfs:subPropertyOf :hasDiscipline ;  &#10;&#32;&#32;&#32;&#32;owl:equivalentProperty :hasDiscipline .  &#10;&lowbar;:nd9fda1f51cee4e2a8bec860f1c9842f3b3 rdf:first &lowbar;:nd9fda1f51cee4e2a8bec860f1c9842f3b1 ;  &#10;&#32;&#32;&#32;&#32;rdf:rest () .  &#10;&lowbar;:nd9fda1f51cee4e2a8bec860f1c9842f3b4 rdf:first skos:Concept ;  &#10;&#32;&#32;&#32;&#32;rdf:rest &lowbar;:nd9fda1f51cee4e2a8bec860f1c9842f3b3 .  &#10;&lowbar;:nd9fda1f51cee4e2a8bec860f1c9842f3b2 rdfs:subClassOf &lowbar;:nd9fda1f51cee4e2a8bec860f1c9842f3b1,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&lowbar;:nd9fda1f51cee4e2a8bec860f1c9842f3b2,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:Thing,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;skos:Concept,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;:Discipline ;  &#10;&#32;&#32;&#32;&#32;owl:equivalentClass :Discipline ;  &#10;&#32;&#32;&#32;&#32;owl:intersectionOf &lowbar;:nd9fda1f51cee4e2a8bec860f1c9842f3b4 .  &#10;&lowbar;:nd9fda1f51cee4e2a8bec860f1c9842f3b1 a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;owl:hasValue :DisciplineNomenclature ;  &#10;&#32;&#32;&#32;&#32;owl:onProperty skos:inScheme .</code></pre>|
|[Section top](#minorfail-outcome-number-119)|Pointer|<pre lang="Turtle"><code>:hasPermittingStage a owl:ObjectProperty ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;has permitting stage&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:comment &#34;Links an entity to the permitting stage this entity pertains&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy :permitting&lowbar;stage ;  &#10;&#32;&#32;&#32;&#32;rdfs:range &lowbar;:n8ee09bec7c454ac1bf6ed8632f63a4f1b1,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&lowbar;:n8ee09bec7c454ac1bf6ed8632f63a4f1b2,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:Thing,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;skos:Concept,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;:PermittingStage ;  &#10;&#32;&#32;&#32;&#32;rdfs:subPropertyOf &#60;https://w3id.org/digitalconstruction/0.5/Lifecycle#hasStage>,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;:hasPermittingStage ;  &#10;&#32;&#32;&#32;&#32;owl:equivalentProperty &#60;https://w3id.org/digitalconstruction/0.5/Lifecycle#hasStage>,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;:hasPermittingStage .  &#10;&lowbar;:n8ee09bec7c454ac1bf6ed8632f63a4f1b3 rdf:first skos:Concept ;  &#10;&#32;&#32;&#32;&#32;rdf:rest ( &lowbar;:n8ee09bec7c454ac1bf6ed8632f63a4f1b1 ) .  &#10;&lowbar;:n8ee09bec7c454ac1bf6ed8632f63a4f1b2 rdfs:subClassOf &lowbar;:n8ee09bec7c454ac1bf6ed8632f63a4f1b1,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&lowbar;:n8ee09bec7c454ac1bf6ed8632f63a4f1b2,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:Thing,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;skos:Concept,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;:PermittingStage ;  &#10;&#32;&#32;&#32;&#32;owl:equivalentClass :PermittingStage ;  &#10;&#32;&#32;&#32;&#32;owl:intersectionOf &lowbar;:n8ee09bec7c454ac1bf6ed8632f63a4f1b3 .  &#10;&lowbar;:n8ee09bec7c454ac1bf6ed8632f63a4f1b1 a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;owl:hasValue :PermittingStageNomenclature ;  &#10;&#32;&#32;&#32;&#32;owl:onProperty skos:inScheme .</code></pre>|
|[Section top](#minorfail-outcome-number-119)|Pointer|http://www.w3.org/2004/02/skos/core#Concept|
|[Section top](#minorfail-outcome-number-119)|Pointer|http://purl.org/dc/elements/1.1/format|

***
### MinorFail Outcome number 120

[Jump to summary definition](#summary-MinorFail-120)	|	[Previous MinorFail outcome](#minorfail-outcome-number-119)	|	[Next MinorFail outcome](#minorfail-outcome-number-121)

:exclamation:MinorFail outcome
#### Subject detail
|Name|all-modules|
|----|----|
|Title|All the modules from branch main that are syntaxically correct as well as their recursive imports|
|Composition|- [Module aec3po](https://github.com/Accord-Project/aec3po/blob/main/src/aec3po.ttl)<br/>- [Module checking&lowbar;act](https://github.com/Accord-Project/aec3po/blob/main/src/checking_act.ttl)<br/>- [Module check&lowbar;method](https://github.com/Accord-Project/aec3po/blob/main/src/check_method.ttl)<br/>- [Module compliance&lowbar;verification&lowbar;report](https://github.com/Accord-Project/aec3po/blob/main/src/compliance_verification_report.ttl)<br/>- [Module data&lowbar;requirement](https://github.com/Accord-Project/aec3po/blob/main/src/data_requirement.ttl)<br/>- [Module document](https://github.com/Accord-Project/aec3po/blob/main/src/document.ttl)<br/>- [Module evidence](https://github.com/Accord-Project/aec3po/blob/main/src/evidence.ttl)<br/>- [Module feature&lowbar;of&lowbar;interest](https://github.com/Accord-Project/aec3po/blob/main/src/feature_of_interest.ttl)<br/>- [Module legal&lowbar;verifier](https://github.com/Accord-Project/aec3po/blob/main/src/legal_verifier.ttl)<br/>- [Module model](https://github.com/Accord-Project/aec3po/blob/main/src/model.ttl)<br/>- [Module rase&lowbar;statement](https://github.com/Accord-Project/aec3po/blob/main/src/rase_statement.ttl)<br/>- [Module statement](https://github.com/Accord-Project/aec3po/blob/main/src/statement.ttl)<br/>- [Module table](https://github.com/Accord-Project/aec3po/blob/main/src/table.ttl)<br/>- [Module vocabularies/administrative&lowbar;areas](https://github.com/Accord-Project/aec3po/blob/main/src/vocabularies/administrative_areas.ttl)<br/>- [Module vocabularies/building&lowbar;structure](https://github.com/Accord-Project/aec3po/blob/main/src/vocabularies/building_structure.ttl)<br/>- [Module vocabularies/building&lowbar;usage](https://github.com/Accord-Project/aec3po/blob/main/src/vocabularies/building_usage.ttl)<br/>- [Module vocabularies/check&lowbar;method&lowbar;comparators](https://github.com/Accord-Project/aec3po/blob/main/src/vocabularies/check_method_comparators.ttl)<br/>- [Module vocabularies/check&lowbar;method&lowbar;operators](https://github.com/Accord-Project/aec3po/blob/main/src/vocabularies/check_method_operators.ttl)<br/>- [Module vocabularies/disciplines](https://github.com/Accord-Project/aec3po/blob/main/src/vocabularies/disciplines.ttl)<br/>- [Module vocabularies/permitting&lowbar;stages](https://github.com/Accord-Project/aec3po/blob/main/src/vocabularies/permitting_stages.ttl)<br/>- [Module vocabularies/quantity&lowbar;kinds](https://github.com/Accord-Project/aec3po/blob/main/src/vocabularies/quantity_kinds.ttl)<br/>- [Module vocabularies/&lowbar;shape](https://github.com/Accord-Project/aec3po/blob/main/src/vocabularies/_shape.ttl)|

#### Criterion detail
|Identifier|[labeled-terms](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#labeled-terms)|
|----|----|
|Title|Term labeling test|
|Description|A test case from the Best Practices tests checking if all the terms of the subject have a rdfs:label property pointing to a literal in English|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-120)|Identifier|`not-labeled-term`|
|[Section top](#minorfail-outcome-number-120)|Title|Terms not labeled|
|[Section top](#minorfail-outcome-number-120)|Description|The following terms have no rdfs:label to define it in natural language|
|[Section top](#minorfail-outcome-number-120)|Pointer|<pre lang="Turtle"><code>:hasFormat a owl:ObjectProperty ;  &#10;&#32;&#32;&#32;&#32;rdfs:comment &#34;Defines the format of an evidence, which is of type dct:form...&#34; ;  &#10;&#32;&#32;&#32;&#32;rdfs:domain :Statement ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy :evidence ;  &#10;&#32;&#32;&#32;&#32;rdfs:range dc:format ;  &#10;&#32;&#32;&#32;&#32;skos:example &#34;an image, a drawing or a model can be an evidence.&#34;@en .</code></pre>|
|[Section top](#minorfail-outcome-number-120)|Pointer|<pre lang="Turtle"><code>:England a owl:NamedIndividual,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;skos:Concept,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;:AdministrativeArea ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy :administrative&lowbar;areas ;  &#10;&#32;&#32;&#32;&#32;skos:definition &#34;England&#34;@en ;  &#10;&#32;&#32;&#32;&#32;skos:inScheme :AdministrativeAreaNomenclature ;  &#10;&#32;&#32;&#32;&#32;skos:prefLabel &#34;England&#34;@en ;  &#10;&#32;&#32;&#32;&#32;skos:topConceptOf :AdministrativeAreaNomenclature .</code></pre>|
|[Section top](#minorfail-outcome-number-120)|Pointer|<pre lang="Turtle"><code>:Estonia a owl:NamedIndividual,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;skos:Concept,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;:AdministrativeArea ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy :administrative&lowbar;areas ;  &#10;&#32;&#32;&#32;&#32;skos:definition &#34;Estonia&#34;@en ;  &#10;&#32;&#32;&#32;&#32;skos:inScheme :AdministrativeAreaNomenclature ;  &#10;&#32;&#32;&#32;&#32;skos:prefLabel &#34;Estonia&#34;@en ;  &#10;&#32;&#32;&#32;&#32;skos:topConceptOf :AdministrativeAreaNomenclature .</code></pre>|
|[Section top](#minorfail-outcome-number-120)|Pointer|<pre lang="Turtle"><code>:Finland a owl:NamedIndividual,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;skos:Concept,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;:AdministrativeArea ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy :administrative&lowbar;areas ;  &#10;&#32;&#32;&#32;&#32;skos:definition &#34;Finland&#34;@en ;  &#10;&#32;&#32;&#32;&#32;skos:inScheme :AdministrativeAreaNomenclature ;  &#10;&#32;&#32;&#32;&#32;skos:prefLabel &#34;Finland&#34;@en ;  &#10;&#32;&#32;&#32;&#32;skos:topConceptOf :AdministrativeAreaNomenclature .</code></pre>|
|[Section top](#minorfail-outcome-number-120)|Pointer|<pre lang="Turtle"><code>:France a owl:NamedIndividual,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;skos:Concept,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;:AdministrativeArea ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy :administrative&lowbar;areas ;  &#10;&#32;&#32;&#32;&#32;skos:definition &#34;France&#34;@en ;  &#10;&#32;&#32;&#32;&#32;skos:inScheme :AdministrativeAreaNomenclature ;  &#10;&#32;&#32;&#32;&#32;skos:prefLabel &#34;France&#34;@en ;  &#10;&#32;&#32;&#32;&#32;skos:topConceptOf :AdministrativeAreaNomenclature .</code></pre>|
|[Section top](#minorfail-outcome-number-120)|Pointer|<pre lang="Turtle"><code>:Germany a owl:NamedIndividual,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;skos:Concept,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;:AdministrativeArea ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy :administrative&lowbar;areas ;  &#10;&#32;&#32;&#32;&#32;skos:definition &#34;Germany&#34;@en ;  &#10;&#32;&#32;&#32;&#32;skos:inScheme :AdministrativeAreaNomenclature ;  &#10;&#32;&#32;&#32;&#32;skos:prefLabel &#34;Germany&#34;@en ;  &#10;&#32;&#32;&#32;&#32;skos:topConceptOf :AdministrativeAreaNomenclature .</code></pre>|
|[Section top](#minorfail-outcome-number-120)|Pointer|<pre lang="Turtle"><code>:Italy a owl:NamedIndividual,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;skos:Concept,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;:AdministrativeArea ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy :administrative&lowbar;areas ;  &#10;&#32;&#32;&#32;&#32;skos:definition &#34;Italy&#34;@en ;  &#10;&#32;&#32;&#32;&#32;skos:inScheme :AdministrativeAreaNomenclature ;  &#10;&#32;&#32;&#32;&#32;skos:prefLabel &#34;Italy&#34;@en ;  &#10;&#32;&#32;&#32;&#32;skos:topConceptOf :AdministrativeAreaNomenclature .</code></pre>|
|[Section top](#minorfail-outcome-number-120)|Pointer|<pre lang="Turtle"><code>:Spain a owl:NamedIndividual,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;skos:Concept,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;:AdministrativeArea ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy :administrative&lowbar;areas ;  &#10;&#32;&#32;&#32;&#32;skos:definition &#34;Spain&#34;@en ;  &#10;&#32;&#32;&#32;&#32;skos:inScheme :AdministrativeAreaNomenclature ;  &#10;&#32;&#32;&#32;&#32;skos:prefLabel &#34;Spain&#34;@en ;  &#10;&#32;&#32;&#32;&#32;skos:topConceptOf :AdministrativeAreaNomenclature .</code></pre>|
|[Section top](#minorfail-outcome-number-120)|Pointer|<pre lang="Turtle"><code>:BuildingStructure-steel a owl:NamedIndividual,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;skos:Concept,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;:BuildingStructure ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy :building&lowbar;structure ;  &#10;&#32;&#32;&#32;&#32;skos:definition &#34;Building has steel structure.&#34;@en ;  &#10;&#32;&#32;&#32;&#32;skos:inScheme :BuildingStructureNomenclature ;  &#10;&#32;&#32;&#32;&#32;skos:prefLabel &#34;steel&#34;@en ;  &#10;&#32;&#32;&#32;&#32;skos:topConceptOf :BuildingStructureNomenclature .</code></pre>|
|[Section top](#minorfail-outcome-number-120)|Pointer|<pre lang="Turtle"><code>:BuildingStructure-timber a owl:NamedIndividual,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;skos:Concept,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;:BuildingStructure ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy :building&lowbar;structure ;  &#10;&#32;&#32;&#32;&#32;skos:definition &#34;Building has timber structure.&#34;@en ;  &#10;&#32;&#32;&#32;&#32;skos:inScheme :BuildingStructureNomenclature ;  &#10;&#32;&#32;&#32;&#32;skos:prefLabel &#34;timber&#34;@en ;  &#10;&#32;&#32;&#32;&#32;skos:topConceptOf :BuildingStructureNomenclature .</code></pre>|
|[Section top](#minorfail-outcome-number-120)|Pointer|<pre lang="Turtle"><code>:BuildingUsage-commercial a owl:NamedIndividual,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;skos:Concept,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;:BuildingUsage ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy :building&lowbar;usage ;  &#10;&#32;&#32;&#32;&#32;skos:definition &#34;Building has commercial usage.&#34;@en ;  &#10;&#32;&#32;&#32;&#32;skos:inScheme :BuildingUsageNomenclature ;  &#10;&#32;&#32;&#32;&#32;skos:prefLabel &#34;commercial&#34;@en ;  &#10;&#32;&#32;&#32;&#32;skos:topConceptOf :BuildingUsageNomenclature .</code></pre>|
|[Section top](#minorfail-outcome-number-120)|Pointer|<pre lang="Turtle"><code>:BuildingUsage-residential a owl:NamedIndividual,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;skos:Concept,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;:BuildingUsage ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy :building&lowbar;usage ;  &#10;&#32;&#32;&#32;&#32;skos:definition &#34;Building has residential usage.&#34;@en ;  &#10;&#32;&#32;&#32;&#32;skos:inScheme :BuildingUsageNomenclature ;  &#10;&#32;&#32;&#32;&#32;skos:prefLabel &#34;residential&#34;@en ;  &#10;&#32;&#32;&#32;&#32;skos:topConceptOf :BuildingUsageNomenclature .</code></pre>|
|[Section top](#minorfail-outcome-number-120)|Pointer|<pre lang="Turtle"><code>:BuildingUsage-cultural a owl:NamedIndividual,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;skos:Concept,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;:BuildingUsage ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy :building&lowbar;usage ;  &#10;&#32;&#32;&#32;&#32;skos:definition &#34;Building has cultural usage.&#34;@en ;  &#10;&#32;&#32;&#32;&#32;skos:inScheme :BuildingUsageNomenclature ;  &#10;&#32;&#32;&#32;&#32;skos:prefLabel &#34;cultural&#34;@en ;  &#10;&#32;&#32;&#32;&#32;skos:topConceptOf :BuildingUsageNomenclature .</code></pre>|
|[Section top](#minorfail-outcome-number-120)|Pointer|<pre lang="Turtle"><code>:CheckMethodcomparator-logicalAND a owl:NamedIndividual,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;skos:Concept,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;:CheckMethodComparator ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy :check&lowbar;method&lowbar;comparators ;  &#10;&#32;&#32;&#32;&#32;skos:definition &#34;logical AND comparator.&#34;@en ;  &#10;&#32;&#32;&#32;&#32;skos:inScheme :CheckMethodComparatorNomenclature ;  &#10;&#32;&#32;&#32;&#32;skos:prefLabel &#34;logicalAND&#34;@en ;  &#10;&#32;&#32;&#32;&#32;skos:topConceptOf :CheckMethodComparatorNomenclature .</code></pre>|
|[Section top](#minorfail-outcome-number-120)|Pointer|<pre lang="Turtle"><code>:CheckMethodcomparator-eq a owl:NamedIndividual,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;skos:Concept,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;:CheckMethodcomparator ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy :check&lowbar;method&lowbar;comparators ;  &#10;&#32;&#32;&#32;&#32;skos:definition &#34;equal-to comparator.&#34;@en ;  &#10;&#32;&#32;&#32;&#32;skos:inScheme :CheckMethodComparatorNomenclature ;  &#10;&#32;&#32;&#32;&#32;skos:prefLabel &#34;equal-to&#34;@en ;  &#10;&#32;&#32;&#32;&#32;skos:topConceptOf :CheckMethodComparatorNomenclature .</code></pre>|
|[Section top](#minorfail-outcome-number-120)|Pointer|<pre lang="Turtle"><code>:CheckMethodComparator-neq a owl:NamedIndividual,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;skos:Concept,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;:CheckMethodComparator ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy :check&lowbar;method&lowbar;comparators ;  &#10;&#32;&#32;&#32;&#32;skos:definition &#34;not equal-to comparator.&#34;@en ;  &#10;&#32;&#32;&#32;&#32;skos:inScheme :CheckMethodComparatorNomenclature ;  &#10;&#32;&#32;&#32;&#32;skos:prefLabel &#34;not equal-to&#34;@en ;  &#10;&#32;&#32;&#32;&#32;skos:topConceptOf :CheckMethodComparatorNomenclature .</code></pre>|
|[Section top](#minorfail-outcome-number-120)|Pointer|<pre lang="Turtle"><code>:CheckMethodComparator-lt a owl:NamedIndividual,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;skos:Concept,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;:CheckMethodComparator ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy :check&lowbar;method&lowbar;comparators ;  &#10;&#32;&#32;&#32;&#32;skos:definition &#34;less-than comparator.&#34;@en ;  &#10;&#32;&#32;&#32;&#32;skos:inScheme :CheckMethodComparatorNomenclature ;  &#10;&#32;&#32;&#32;&#32;skos:prefLabel &#34;less than&#34;@en ;  &#10;&#32;&#32;&#32;&#32;skos:topConceptOf :CheckMethodComparatorNomenclature .</code></pre>|
|[Section top](#minorfail-outcome-number-120)|Pointer|<pre lang="Turtle"><code>:CheckMethodComparator-le a owl:NamedIndividual,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;skos:Concept,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;:CheckMethodComparator ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy :check&lowbar;method&lowbar;comparators ;  &#10;&#32;&#32;&#32;&#32;skos:definition &#34;less-equal comparator.&#34;@en ;  &#10;&#32;&#32;&#32;&#32;skos:inScheme :CheckMethodComparatorNomenclature ;  &#10;&#32;&#32;&#32;&#32;skos:prefLabel &#34;less equal&#34;@en ;  &#10;&#32;&#32;&#32;&#32;skos:topConceptOf :CheckMethodComparatorNomenclature .</code></pre>|
|[Section top](#minorfail-outcome-number-120)|Pointer|<pre lang="Turtle"><code>:CheckMethodComparator-gt a owl:NamedIndividual,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;skos:Concept,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;:CheckMethodComparator ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy :check&lowbar;method&lowbar;comparators ;  &#10;&#32;&#32;&#32;&#32;skos:definition &#34;greater-than comparator.&#34;@en ;  &#10;&#32;&#32;&#32;&#32;skos:inScheme :CheckMethodComparatorNomenclature ;  &#10;&#32;&#32;&#32;&#32;skos:prefLabel &#34;greater than&#34;@en ;  &#10;&#32;&#32;&#32;&#32;skos:topConceptOf :CheckMethodComparatorNomenclature .</code></pre>|
|[Section top](#minorfail-outcome-number-120)|Pointer|<pre lang="Turtle"><code>:CheckMethodComparator-ge a owl:NamedIndividual,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;skos:Concept,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;:CheckMethodComparator ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy :check&lowbar;method&lowbar;comparators ;  &#10;&#32;&#32;&#32;&#32;skos:definition &#34;greater-equal comparator.&#34;@en ;  &#10;&#32;&#32;&#32;&#32;skos:inScheme :CheckMethodComparatorNomenclature ;  &#10;&#32;&#32;&#32;&#32;skos:prefLabel &#34;greater equal&#34;@en ;  &#10;&#32;&#32;&#32;&#32;skos:topConceptOf :CheckMethodComparatorNomenclature .</code></pre>|
|[Section top](#minorfail-outcome-number-120)|Pointer|<pre lang="Turtle"><code>:CheckMethodComparator-logicalOR a owl:NamedIndividual,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;skos:Concept,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;:CheckMethodComparator ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy :check&lowbar;method&lowbar;comparators ;  &#10;&#32;&#32;&#32;&#32;skos:definition &#34;logical OR comparator.&#34;@en ;  &#10;&#32;&#32;&#32;&#32;skos:inScheme :CheckMethodComparatorNomenclature ;  &#10;&#32;&#32;&#32;&#32;skos:prefLabel &#34;logicalOR&#34;@en ;  &#10;&#32;&#32;&#32;&#32;skos:topConceptOf :CheckMethodComparatorNomenclature .</code></pre>|
|[Section top](#minorfail-outcome-number-120)|Pointer|<pre lang="Turtle"><code>:CheckMethodOperator-exists a owl:NamedIndividual,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;skos:Concept,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;:CheckMethodOperator ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy :check&lowbar;method&lowbar;operators ;  &#10;&#32;&#32;&#32;&#32;skos:definition &#34;exists operator.&#34;@en ;  &#10;&#32;&#32;&#32;&#32;skos:inScheme :CheckMethodOperatorNomenclature ;  &#10;&#32;&#32;&#32;&#32;skos:prefLabel &#34;exists&#34;@en ;  &#10;&#32;&#32;&#32;&#32;skos:topConceptOf :CheckMethodOperatorNomenclature .</code></pre>|
|[Section top](#minorfail-outcome-number-120)|Pointer|<pre lang="Turtle"><code>:CheckMethodOperator-notExists a owl:NamedIndividual,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;skos:Concept,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;:CheckMethodOperator ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy :check&lowbar;method&lowbar;operators ;  &#10;&#32;&#32;&#32;&#32;skos:definition &#34;not exists operator.&#34;@en ;  &#10;&#32;&#32;&#32;&#32;skos:inScheme :CheckMethodOperatorNomenclature ;  &#10;&#32;&#32;&#32;&#32;skos:prefLabel &#34;not exists&#34;@en ;  &#10;&#32;&#32;&#32;&#32;skos:topConceptOf :CheckMethodOperatorNomenclature .</code></pre>|
|[Section top](#minorfail-outcome-number-120)|Pointer|<pre lang="Turtle"><code>:CheckMethodOperator-forall a owl:NamedIndividual,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;skos:Concept,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;:CheckMethodOperator ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy :check&lowbar;method&lowbar;operators ;  &#10;&#32;&#32;&#32;&#32;skos:definition &#34;forall operator.&#34;@en ;  &#10;&#32;&#32;&#32;&#32;skos:inScheme :CheckMethodOperatorNomenclature ;  &#10;&#32;&#32;&#32;&#32;skos:prefLabel &#34;forall&#34;@en ;  &#10;&#32;&#32;&#32;&#32;skos:topConceptOf :CheckMethodOperatorNomenclature .</code></pre>|
|[Section top](#minorfail-outcome-number-120)|Pointer|<pre lang="Turtle"><code>:CheckMethodOperator-addition a owl:NamedIndividual,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;skos:Concept,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;:CheckMethodOperator ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy :check&lowbar;method&lowbar;operators ;  &#10;&#32;&#32;&#32;&#32;skos:definition &#34;addition operator.&#34;@en ;  &#10;&#32;&#32;&#32;&#32;skos:inScheme :CheckMethodOperatorNomenclature ;  &#10;&#32;&#32;&#32;&#32;skos:prefLabel &#34;addition&#34;@en ;  &#10;&#32;&#32;&#32;&#32;skos:topConceptOf :CheckMethodOperatorNomenclature .</code></pre>|
|[Section top](#minorfail-outcome-number-120)|Pointer|<pre lang="Turtle"><code>:CheckMethodOperator-multiplication a owl:NamedIndividual,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;skos:Concept,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;:CheckMethodOperator ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy :check&lowbar;method&lowbar;operators ;  &#10;&#32;&#32;&#32;&#32;skos:definition &#34;multiplication Operator.&#34;@en ;  &#10;&#32;&#32;&#32;&#32;skos:inScheme :CheckMethodOperatorNomenclature ;  &#10;&#32;&#32;&#32;&#32;skos:prefLabel &#34;multiplication&#34;@en ;  &#10;&#32;&#32;&#32;&#32;skos:topConceptOf :CheckMethodOperatorNomenclature .</code></pre>|
|[Section top](#minorfail-outcome-number-120)|Pointer|<pre lang="Turtle"><code>:CheckMethodOperator-subtraction a owl:NamedIndividual,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;skos:Concept,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;:CheckMethodOperator ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy :check&lowbar;method&lowbar;operators ;  &#10;&#32;&#32;&#32;&#32;skos:definition &#34;subtraction operator.&#34;@en ;  &#10;&#32;&#32;&#32;&#32;skos:inScheme :CheckMethodOperatorNomenclature ;  &#10;&#32;&#32;&#32;&#32;skos:prefLabel &#34;subtraction&#34;@en ;  &#10;&#32;&#32;&#32;&#32;skos:topConceptOf :CheckMethodOperatorNomenclature .</code></pre>|
|[Section top](#minorfail-outcome-number-120)|Pointer|<pre lang="Turtle"><code>:CheckMethodOperator-division a owl:NamedIndividual,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;skos:Concept,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;:CheckMethodOperator ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy :check&lowbar;method&lowbar;operators ;  &#10;&#32;&#32;&#32;&#32;skos:definition &#34;division Operator.&#34;@en ;  &#10;&#32;&#32;&#32;&#32;skos:inScheme :CheckMethodOperatorNomenclature ;  &#10;&#32;&#32;&#32;&#32;skos:prefLabel &#34;division&#34;@en ;  &#10;&#32;&#32;&#32;&#32;skos:topConceptOf :CheckMethodOperatorNomenclature .</code></pre>|
|[Section top](#minorfail-outcome-number-120)|Pointer|<pre lang="Turtle"><code>:Discipline-architecture a owl:NamedIndividual,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;skos:Concept,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;:Discipline ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy :discipline ;  &#10;&#32;&#32;&#32;&#32;skos:definition &#34;The Architecture discipline.&#34;@en ;  &#10;&#32;&#32;&#32;&#32;skos:inScheme :DisciplineNomenclature ;  &#10;&#32;&#32;&#32;&#32;skos:prefLabel &#34;architecture&#34;@en ;  &#10;&#32;&#32;&#32;&#32;skos:topConceptOf :DisciplineNomenclature .</code></pre>|
|[Section top](#minorfail-outcome-number-120)|Pointer|<pre lang="Turtle"><code>:Discipline-buildingServices a owl:NamedIndividual,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;skos:Concept,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;:Discipline ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy :discipline ;  &#10;&#32;&#32;&#32;&#32;skos:definition &#34;The Building Services discipline.&#34;@en ;  &#10;&#32;&#32;&#32;&#32;skos:inScheme :DisciplineNomenclature ;  &#10;&#32;&#32;&#32;&#32;skos:prefLabel &#34;building services&#34;@en ;  &#10;&#32;&#32;&#32;&#32;skos:topConceptOf :DisciplineNomenclature .</code></pre>|
|[Section top](#minorfail-outcome-number-120)|Pointer|<pre lang="Turtle"><code>:Discipline-construction a owl:NamedIndividual,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;skos:Concept,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;:Discipline ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy :discipline ;  &#10;&#32;&#32;&#32;&#32;skos:definition &#34;The Construction discipline.&#34;@en ;  &#10;&#32;&#32;&#32;&#32;skos:inScheme :DisciplineNomenclature ;  &#10;&#32;&#32;&#32;&#32;skos:prefLabel &#34;construction&#34;@en ;  &#10;&#32;&#32;&#32;&#32;skos:topConceptOf :DisciplineNomenclature .</code></pre>|
|[Section top](#minorfail-outcome-number-120)|Pointer|<pre lang="Turtle"><code>:Discipline-planning a owl:NamedIndividual,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;skos:Concept,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;:Discipline ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy :discipline ;  &#10;&#32;&#32;&#32;&#32;skos:definition &#34;The Planning discipline.&#34;@en ;  &#10;&#32;&#32;&#32;&#32;skos:inScheme :DisciplineNomenclature ;  &#10;&#32;&#32;&#32;&#32;skos:prefLabel &#34;planning&#34;@en ;  &#10;&#32;&#32;&#32;&#32;skos:topConceptOf :DisciplineNomenclature .</code></pre>|
|[Section top](#minorfail-outcome-number-120)|Pointer|<pre lang="Turtle"><code>:Discipline-structuralEngineering a owl:NamedIndividual,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;skos:Concept,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;:Discipline ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy :discipline ;  &#10;&#32;&#32;&#32;&#32;skos:definition &#34;The Structural Engineering discipline.&#34;@en ;  &#10;&#32;&#32;&#32;&#32;skos:inScheme :DisciplineNomenclature ;  &#10;&#32;&#32;&#32;&#32;skos:prefLabel &#34;structural engineering&#34;@en ;  &#10;&#32;&#32;&#32;&#32;skos:topConceptOf :DisciplineNomenclature .</code></pre>|
|[Section top](#minorfail-outcome-number-120)|Pointer|<pre lang="Turtle"><code>:UK&lowbar;Building&lowbar;Control&lowbar;Submission a owl:NamedIndividual,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;skos:Concept,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;:PermittingStage ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy :permitting&lowbar;stage ;  &#10;&#32;&#32;&#32;&#32;skos:definition &#34;The UK Building Control Submission permitting stage.&#34;@en ;  &#10;&#32;&#32;&#32;&#32;skos:inScheme :PermittingStageNomenclature ;  &#10;&#32;&#32;&#32;&#32;skos:prefLabel &#34;building control submission&#34;@en ;  &#10;&#32;&#32;&#32;&#32;skos:topConceptOf :PermittingStageNomenclature ;  &#10;&#32;&#32;&#32;&#32;:forAdministrativeArea :England .</code></pre>|
|[Section top](#minorfail-outcome-number-120)|Pointer|<pre lang="Turtle"><code>:UK&lowbar;Planning&lowbar;Permission a owl:NamedIndividual,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;skos:Concept,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;:PermittingStage ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy :permitting&lowbar;stage ;  &#10;&#32;&#32;&#32;&#32;skos:definition &#34;The UK Planning Permission permitting stage.&#34;@en ;  &#10;&#32;&#32;&#32;&#32;skos:inScheme :PermittingStageNomenclature ;  &#10;&#32;&#32;&#32;&#32;skos:prefLabel &#34;planning permission&#34;@en ;  &#10;&#32;&#32;&#32;&#32;skos:topConceptOf :PermittingStageNomenclature ;  &#10;&#32;&#32;&#32;&#32;:forAdministrativeArea :England .</code></pre>|
|[Section top](#minorfail-outcome-number-120)|Pointer|<pre lang="Turtle"><code>:QuantityKind a owl:Class ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy &#60;http://qudt.org/2.1/schema/qudt> .</code></pre>|
|[Section top](#minorfail-outcome-number-120)|Pointer|<pre lang="Turtle"><code>:ModularRoomHeight a owl:NamedIndividual,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;skos:Concept,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;:QuantityKind ;  &#10;&#32;&#32;&#32;&#32;qudt:applicableUnit &#60;http://qudt.org/vocab/unit/CentiM>,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#60;http://qudt.org/vocab/unit/IN>,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#60;http://qudt.org/vocab/unit/M>,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#60;http://qudt.org/vocab/unit/MilliIN>,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#60;http://qudt.org/vocab/unit/MilliM> ;  &#10;&#32;&#32;&#32;&#32;qudt:hasDimensionVector &#60;http://qudt.org/vocab/dimensionvector/A0E0L1I0M0H0T0D0> ;  &#10;&#32;&#32;&#32;&#32;qudt:normativeReference &#34;https://www.iso.org/obp/ui/#iso:std:iso:6707:-1:ed-6:v1:en:t...&#34; ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy :quantity&lowbar;kinds ;  &#10;&#32;&#32;&#32;&#32;skos:broader &#60;http://qudt.org/vocab/quantitykind/Length> ;  &#10;&#32;&#32;&#32;&#32;skos:definition &#34;vertical distance within one storey between the modular plan...&#34; ;  &#10;&#32;&#32;&#32;&#32;skos:prefLabel &#34;modular room height&#34;@en .</code></pre>|
|[Section top](#minorfail-outcome-number-120)|Pointer|<pre lang="Turtle"><code>:WidthOfAngledCorridor a owl:NamedIndividual,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;skos:Concept,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;:QuantityKind ;  &#10;&#32;&#32;&#32;&#32;qudt:applicableUnit &#60;http://qudt.org/vocab/unit/CentiM>,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#60;http://qudt.org/vocab/unit/IN>,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#60;http://qudt.org/vocab/unit/M>,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#60;http://qudt.org/vocab/unit/MilliIN>,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#60;http://qudt.org/vocab/unit/MilliM> ;  &#10;&#32;&#32;&#32;&#32;qudt:hasDimensionVector &#60;http://qudt.org/vocab/dimensionvector/A0E0L1I0M0H0T0D0> ;  &#10;&#32;&#32;&#32;&#32;qudt:normativeReference &#34;https://www.iso.org/obp/ui/#iso:std:iso:7176:-5:ed-2:v1:en:t...&#34; ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy :quantity&lowbar;kinds ;  &#10;&#32;&#32;&#32;&#32;skos:broader &#60;http://qudt.org/vocab/quantitykind/Length> ;  &#10;&#32;&#32;&#32;&#32;skos:definition &#34;width of a corridor with a right angled turn in which the wh...&#34; ;  &#10;&#32;&#32;&#32;&#32;skos:prefLabel &#34;width of angled corridor&#34;@en .</code></pre>|
|[Section top](#minorfail-outcome-number-120)|Pointer|<pre lang="Turtle"><code>:CompressiveForce a owl:NamedIndividual,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;skos:Concept,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;:QuantityKind ;  &#10;&#32;&#32;&#32;&#32;qudt:hasDimensionVector &#60;http://qudt.org/vocab/dimensionvector/A0E0L1I0M1H0T-2D0> ;  &#10;&#32;&#32;&#32;&#32;qudt:symbol &#34;C&#34; ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy :quantity&lowbar;kinds ;  &#10;&#32;&#32;&#32;&#32;skos:broader &#60;http://qudt.org/vocab/quantitykind/Force> ;  &#10;&#32;&#32;&#32;&#32;skos:definition &#34;Force tending to reduce the size of a body.&#34; ;  &#10;&#32;&#32;&#32;&#32;skos:prefLabel &#34;compressive force&#34;@en .</code></pre>|
|[Section top](#minorfail-outcome-number-120)|Pointer|<pre lang="Turtle"><code>:PartialSafetyFactor a owl:NamedIndividual,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;skos:Concept,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;:QuantityKind ;  &#10;&#32;&#32;&#32;&#32;qudt:applicableUnit &#60;http://qudt.org/vocab/unit/UNITLESS> ;  &#10;&#32;&#32;&#32;&#32;qudt:hasDimensionVector &#60;http://qudt.org/vocab/dimensionvector/A0E0L0I0M0H0T0D0> ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy :quantity&lowbar;kinds ;  &#10;&#32;&#32;&#32;&#32;skos:definition &#34;Also written γM, the partial safety factor for resistance.&#34;@en ;  &#10;&#32;&#32;&#32;&#32;skos:prefLabel &#34;Partial Safety Factor&#34;@en .</code></pre>|
|[Section top](#minorfail-outcome-number-120)|Pointer|<pre lang="Turtle"><code>:PartialSafetyFactor0 a owl:NamedIndividual,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;skos:Concept,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;:QuantityKind ;  &#10;&#32;&#32;&#32;&#32;qudt:applicableUnit &#60;http://qudt.org/vocab/unit/UNITLESS> ;  &#10;&#32;&#32;&#32;&#32;qudt:hasDimensionVector &#60;http://qudt.org/vocab/dimensionvector/A0E0L0I0M0H0T0D0> ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy :quantity&lowbar;kinds ;  &#10;&#32;&#32;&#32;&#32;skos:broader :PartialSafetyFactor ;  &#10;&#32;&#32;&#32;&#32;skos:definition &#34;Also written γM0, the partial safety factor for resistance r...&#34; ;  &#10;&#32;&#32;&#32;&#32;skos:prefLabel &#34;Partial Safety Factor&#34;@en .</code></pre>|
|[Section top](#minorfail-outcome-number-120)|Pointer|<pre lang="Turtle"><code>:AxialCompressionStress a owl:NamedIndividual,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;skos:Concept,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;:QuantityKind ;  &#10;&#32;&#32;&#32;&#32;qudt:hasDimensionVector &#60;http://qudt.org/vocab/dimensionvector/A0E0L1I0M-1H0T-2D0> ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy :quantity&lowbar;kinds ;  &#10;&#32;&#32;&#32;&#32;skos:definition &#34;also known as fc0k&#34; ;  &#10;&#32;&#32;&#32;&#32;skos:prefLabel &#34;axial compression stress&#34;@en .</code></pre>|
|[Section top](#minorfail-outcome-number-120)|Pointer|<pre lang="Turtle"><code>:ModificationFactorKmod a owl:NamedIndividual,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;skos:Concept,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;:QuantityKind ;  &#10;&#32;&#32;&#32;&#32;qudt:applicableUnit &#60;http://qudt.org/vocab/unit/UNITLESS> ;  &#10;&#32;&#32;&#32;&#32;qudt:hasDimensionVector &#60;http://qudt.org/vocab/dimensionvector/A0E0L0I0M0H0T0D0> ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy :quantity&lowbar;kinds ;  &#10;&#32;&#32;&#32;&#32;skos:definition &#34;Modification Factor to take into account the duration of loa...&#34; ;  &#10;&#32;&#32;&#32;&#32;skos:prefLabel &#34;Modification Factor Kmod&#34;@en .</code></pre>|

***
### MinorFail Outcome number 121

[Jump to summary definition](#summary-MinorFail-121)	|	[Previous MinorFail outcome](#minorfail-outcome-number-120)	|	[Next MinorFail outcome](#minorfail-outcome-number-122)

:exclamation:MinorFail outcome
#### Subject detail
|Name|all-modules|
|----|----|
|Title|All the modules from branch main that are syntaxically correct as well as their recursive imports|
|Composition|- [Module aec3po](https://github.com/Accord-Project/aec3po/blob/main/src/aec3po.ttl)<br/>- [Module checking&lowbar;act](https://github.com/Accord-Project/aec3po/blob/main/src/checking_act.ttl)<br/>- [Module check&lowbar;method](https://github.com/Accord-Project/aec3po/blob/main/src/check_method.ttl)<br/>- [Module compliance&lowbar;verification&lowbar;report](https://github.com/Accord-Project/aec3po/blob/main/src/compliance_verification_report.ttl)<br/>- [Module data&lowbar;requirement](https://github.com/Accord-Project/aec3po/blob/main/src/data_requirement.ttl)<br/>- [Module document](https://github.com/Accord-Project/aec3po/blob/main/src/document.ttl)<br/>- [Module evidence](https://github.com/Accord-Project/aec3po/blob/main/src/evidence.ttl)<br/>- [Module feature&lowbar;of&lowbar;interest](https://github.com/Accord-Project/aec3po/blob/main/src/feature_of_interest.ttl)<br/>- [Module legal&lowbar;verifier](https://github.com/Accord-Project/aec3po/blob/main/src/legal_verifier.ttl)<br/>- [Module model](https://github.com/Accord-Project/aec3po/blob/main/src/model.ttl)<br/>- [Module rase&lowbar;statement](https://github.com/Accord-Project/aec3po/blob/main/src/rase_statement.ttl)<br/>- [Module statement](https://github.com/Accord-Project/aec3po/blob/main/src/statement.ttl)<br/>- [Module table](https://github.com/Accord-Project/aec3po/blob/main/src/table.ttl)<br/>- [Module vocabularies/administrative&lowbar;areas](https://github.com/Accord-Project/aec3po/blob/main/src/vocabularies/administrative_areas.ttl)<br/>- [Module vocabularies/building&lowbar;structure](https://github.com/Accord-Project/aec3po/blob/main/src/vocabularies/building_structure.ttl)<br/>- [Module vocabularies/building&lowbar;usage](https://github.com/Accord-Project/aec3po/blob/main/src/vocabularies/building_usage.ttl)<br/>- [Module vocabularies/check&lowbar;method&lowbar;comparators](https://github.com/Accord-Project/aec3po/blob/main/src/vocabularies/check_method_comparators.ttl)<br/>- [Module vocabularies/check&lowbar;method&lowbar;operators](https://github.com/Accord-Project/aec3po/blob/main/src/vocabularies/check_method_operators.ttl)<br/>- [Module vocabularies/disciplines](https://github.com/Accord-Project/aec3po/blob/main/src/vocabularies/disciplines.ttl)<br/>- [Module vocabularies/permitting&lowbar;stages](https://github.com/Accord-Project/aec3po/blob/main/src/vocabularies/permitting_stages.ttl)<br/>- [Module vocabularies/quantity&lowbar;kinds](https://github.com/Accord-Project/aec3po/blob/main/src/vocabularies/quantity_kinds.ttl)<br/>- [Module vocabularies/&lowbar;shape](https://github.com/Accord-Project/aec3po/blob/main/src/vocabularies/_shape.ttl)|

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
|[Section top](#minorfail-outcome-number-121)|Description|Class Expression not supported with owl:equivalentClass or owl:intersectionOf|
|[Section top](#minorfail-outcome-number-121)|Pointer|<pre lang="Turtle"><code>&#91;] a owl:Class ;  &#10;&#32;&#32;&#32;&#32;owl:intersectionOf ( aec3po:CheckMethod &#91; a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:allValuesFrom &#91; a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:allValuesFrom aec3po:FeatureOfInterest ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:onProperty &#91; owl:inverseOf aec3po:forDesign ] ] ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:onProperty aec3po:forDesign ] ) .</code></pre>|

***
### MinorFail Outcome number 122

[Jump to summary definition](#summary-MinorFail-122)	|	[Previous MinorFail outcome](#minorfail-outcome-number-121)	|	[Next MinorFail outcome](#minorfail-outcome-number-123)

:exclamation:MinorFail outcome
#### Subject detail
|Name|all-modules|
|----|----|
|Title|All the modules from branch main that are syntaxically correct as well as their recursive imports|
|Composition|- [Module aec3po](https://github.com/Accord-Project/aec3po/blob/main/src/aec3po.ttl)<br/>- [Module checking&lowbar;act](https://github.com/Accord-Project/aec3po/blob/main/src/checking_act.ttl)<br/>- [Module check&lowbar;method](https://github.com/Accord-Project/aec3po/blob/main/src/check_method.ttl)<br/>- [Module compliance&lowbar;verification&lowbar;report](https://github.com/Accord-Project/aec3po/blob/main/src/compliance_verification_report.ttl)<br/>- [Module data&lowbar;requirement](https://github.com/Accord-Project/aec3po/blob/main/src/data_requirement.ttl)<br/>- [Module document](https://github.com/Accord-Project/aec3po/blob/main/src/document.ttl)<br/>- [Module evidence](https://github.com/Accord-Project/aec3po/blob/main/src/evidence.ttl)<br/>- [Module feature&lowbar;of&lowbar;interest](https://github.com/Accord-Project/aec3po/blob/main/src/feature_of_interest.ttl)<br/>- [Module legal&lowbar;verifier](https://github.com/Accord-Project/aec3po/blob/main/src/legal_verifier.ttl)<br/>- [Module model](https://github.com/Accord-Project/aec3po/blob/main/src/model.ttl)<br/>- [Module rase&lowbar;statement](https://github.com/Accord-Project/aec3po/blob/main/src/rase_statement.ttl)<br/>- [Module statement](https://github.com/Accord-Project/aec3po/blob/main/src/statement.ttl)<br/>- [Module table](https://github.com/Accord-Project/aec3po/blob/main/src/table.ttl)<br/>- [Module vocabularies/administrative&lowbar;areas](https://github.com/Accord-Project/aec3po/blob/main/src/vocabularies/administrative_areas.ttl)<br/>- [Module vocabularies/building&lowbar;structure](https://github.com/Accord-Project/aec3po/blob/main/src/vocabularies/building_structure.ttl)<br/>- [Module vocabularies/building&lowbar;usage](https://github.com/Accord-Project/aec3po/blob/main/src/vocabularies/building_usage.ttl)<br/>- [Module vocabularies/check&lowbar;method&lowbar;comparators](https://github.com/Accord-Project/aec3po/blob/main/src/vocabularies/check_method_comparators.ttl)<br/>- [Module vocabularies/check&lowbar;method&lowbar;operators](https://github.com/Accord-Project/aec3po/blob/main/src/vocabularies/check_method_operators.ttl)<br/>- [Module vocabularies/disciplines](https://github.com/Accord-Project/aec3po/blob/main/src/vocabularies/disciplines.ttl)<br/>- [Module vocabularies/permitting&lowbar;stages](https://github.com/Accord-Project/aec3po/blob/main/src/vocabularies/permitting_stages.ttl)<br/>- [Module vocabularies/quantity&lowbar;kinds](https://github.com/Accord-Project/aec3po/blob/main/src/vocabularies/quantity_kinds.ttl)<br/>- [Module vocabularies/&lowbar;shape](https://github.com/Accord-Project/aec3po/blob/main/src/vocabularies/_shape.ttl)|

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
|[Section top](#minorfail-outcome-number-122)|Description|Statement not supported in an Equivalent Class Expression|
|[Section top](#minorfail-outcome-number-122)|Pointer|<pre lang="Turtle"><code>&#91;] a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;owl:allValuesFrom &#91; a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:allValuesFrom aec3po:FeatureOfInterest ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:onProperty &#91; owl:inverseOf aec3po:forDesign ] ] ;  &#10;&#32;&#32;&#32;&#32;owl:onProperty aec3po:forDesign .</code></pre>|

***
### MinorFail Outcome number 123

[Jump to summary definition](#summary-MinorFail-123)	|	[Previous MinorFail outcome](#minorfail-outcome-number-122)	|	[Next MinorFail outcome](#minorfail-outcome-number-124)

:exclamation:MinorFail outcome
#### Subject detail
|Name|all-modules|
|----|----|
|Title|All the modules from branch main that are syntaxically correct as well as their recursive imports|
|Composition|- [Module aec3po](https://github.com/Accord-Project/aec3po/blob/main/src/aec3po.ttl)<br/>- [Module checking&lowbar;act](https://github.com/Accord-Project/aec3po/blob/main/src/checking_act.ttl)<br/>- [Module check&lowbar;method](https://github.com/Accord-Project/aec3po/blob/main/src/check_method.ttl)<br/>- [Module compliance&lowbar;verification&lowbar;report](https://github.com/Accord-Project/aec3po/blob/main/src/compliance_verification_report.ttl)<br/>- [Module data&lowbar;requirement](https://github.com/Accord-Project/aec3po/blob/main/src/data_requirement.ttl)<br/>- [Module document](https://github.com/Accord-Project/aec3po/blob/main/src/document.ttl)<br/>- [Module evidence](https://github.com/Accord-Project/aec3po/blob/main/src/evidence.ttl)<br/>- [Module feature&lowbar;of&lowbar;interest](https://github.com/Accord-Project/aec3po/blob/main/src/feature_of_interest.ttl)<br/>- [Module legal&lowbar;verifier](https://github.com/Accord-Project/aec3po/blob/main/src/legal_verifier.ttl)<br/>- [Module model](https://github.com/Accord-Project/aec3po/blob/main/src/model.ttl)<br/>- [Module rase&lowbar;statement](https://github.com/Accord-Project/aec3po/blob/main/src/rase_statement.ttl)<br/>- [Module statement](https://github.com/Accord-Project/aec3po/blob/main/src/statement.ttl)<br/>- [Module table](https://github.com/Accord-Project/aec3po/blob/main/src/table.ttl)<br/>- [Module vocabularies/administrative&lowbar;areas](https://github.com/Accord-Project/aec3po/blob/main/src/vocabularies/administrative_areas.ttl)<br/>- [Module vocabularies/building&lowbar;structure](https://github.com/Accord-Project/aec3po/blob/main/src/vocabularies/building_structure.ttl)<br/>- [Module vocabularies/building&lowbar;usage](https://github.com/Accord-Project/aec3po/blob/main/src/vocabularies/building_usage.ttl)<br/>- [Module vocabularies/check&lowbar;method&lowbar;comparators](https://github.com/Accord-Project/aec3po/blob/main/src/vocabularies/check_method_comparators.ttl)<br/>- [Module vocabularies/check&lowbar;method&lowbar;operators](https://github.com/Accord-Project/aec3po/blob/main/src/vocabularies/check_method_operators.ttl)<br/>- [Module vocabularies/disciplines](https://github.com/Accord-Project/aec3po/blob/main/src/vocabularies/disciplines.ttl)<br/>- [Module vocabularies/permitting&lowbar;stages](https://github.com/Accord-Project/aec3po/blob/main/src/vocabularies/permitting_stages.ttl)<br/>- [Module vocabularies/quantity&lowbar;kinds](https://github.com/Accord-Project/aec3po/blob/main/src/vocabularies/quantity_kinds.ttl)<br/>- [Module vocabularies/&lowbar;shape](https://github.com/Accord-Project/aec3po/blob/main/src/vocabularies/_shape.ttl)|

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
|[Section top](#minorfail-outcome-number-123)|Pointer|<pre lang="Turtle"><code>aec3po:caption a owl:DatatypeProperty ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;caption&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:comment &#34;The caption of a table, image, etc. &#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:domain &#91; a owl:Class ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:unionOf ( aec3po:Table aec3po:Image ) ] ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy aec3po:table .</code></pre>|
|[Section top](#minorfail-outcome-number-123)|Pointer|<pre lang="Turtle"><code>aec3po:contains a owl:ObjectProperty ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;Contains&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:comment &#34;A container contains a table and its caption. A table contai...&#34; ;  &#10;&#32;&#32;&#32;&#32;rdfs:domain &#91; a owl:Class ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:unionOf ( aec3po:Table aec3po:Image aec3po:Row aec3po:Column ) ] ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy aec3po:table .</code></pre>|
|[Section top](#minorfail-outcome-number-123)|Pointer|<pre lang="Turtle"><code>aec3po:hasBSSDDTarget a owl:FunctionalProperty,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:ObjectProperty ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;hasBSSDDTarget&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:comment &#34;The target refers to either the name of an object, the name ...&#34; ;  &#10;&#32;&#32;&#32;&#32;rdfs:domain &#91; a owl:Class ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:unionOf ( aec3po:FeatureOfInterest aec3po:Property aec3po:CheckMethod ) ] ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy aec3po:check&lowbar;method .</code></pre>|
|[Section top](#minorfail-outcome-number-123)|Pointer|<pre lang="Turtle"><code>aec3po:hasFirstSubdivision a owl:FunctionalProperty,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:ObjectProperty ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;has first subdivision&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:comment &#34;Links a document part to the first of its subdivision&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:domain &#91; owl:unionOf ( aec3po:Document aec3po:DocumentSubdivision ) ] ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy aec3po:document ;  &#10;&#32;&#32;&#32;&#32;rdfs:range aec3po:DocumentSubdivision ;  &#10;&#32;&#32;&#32;&#32;rdfs:subPropertyOf aec3po:hasSubdivision .</code></pre>|
|[Section top](#minorfail-outcome-number-123)|Pointer|<pre lang="Turtle"><code>aec3po:hasSubdivision a owl:ObjectProperty ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;has subdivision&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:comment &#34;links a document part to some of its subdivision&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:domain &#91; owl:unionOf ( aec3po:Document aec3po:DocumentSubdivision ) ] ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy aec3po:document ;  &#10;&#32;&#32;&#32;&#32;rdfs:range aec3po:DocumentSubdivision ;  &#10;&#32;&#32;&#32;&#32;rdfs:subPropertyOf dc:hasPart .</code></pre>|
|[Section top](#minorfail-outcome-number-123)|Pointer|<pre lang="Turtle"><code>aec3po:hasUnit a owl:FunctionalProperty,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:ObjectProperty ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;hasUnit&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:comment &#34;the hasUnit property is used to link a specific property or ...&#34; ;  &#10;&#32;&#32;&#32;&#32;rdfs:domain &#91; a owl:Class ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:unionOf ( aec3po:FeatureOfInterest aec3po:Property aec3po:CheckMethod ) ] ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy aec3po:check&lowbar;method ;  &#10;&#32;&#32;&#32;&#32;rdfs:range qudt:Unit ;  &#10;&#32;&#32;&#32;&#32;owl:eqivalentProperty qudt:hasValue .</code></pre>|
|[Section top](#minorfail-outcome-number-123)|Pointer|<pre lang="Turtle"><code>aec3po:hasValue a owl:DatatypeProperty,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:FunctionalProperty ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;has value&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:comment &#34;de facto used to link something (anything: property, propert...&#34; ;  &#10;&#32;&#32;&#32;&#32;rdfs:domain &#91; a owl:Class ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:unionOf ( aec3po:FeatureOfInterest aec3po:Property aec3po:CheckMethod ) ] ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy aec3po: ;  &#10;&#32;&#32;&#32;&#32;skos:note &#34;The value of the literal may be a XSD literal (boolean, inte...&#34; .</code></pre>|
|[Section top](#minorfail-outcome-number-123)|Pointer|<pre lang="Turtle"><code>aec3po:isContainedIn a owl:ObjectProperty ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;is contained by&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:comment &#34;A table contains row, columns and other elements.&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy aec3po:table ;  &#10;&#32;&#32;&#32;&#32;rdfs:range &#91; a owl:Class ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:unionOf ( aec3po:Table aec3po:Image aec3po:Row aec3po:Column aec3po:Cell ) ] .</code></pre>|
|[Section top](#minorfail-outcome-number-123)|Pointer|<pre lang="Turtle"><code>aec3po:locationCoverage a owl:ObjectProperty ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;location coverage&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:comment &#34;The spatialCoverage indicates the place(s) or the administra...&#34; ;  &#10;&#32;&#32;&#32;&#32;rdfs:domain &#60;https://schema.org/Model> ;  &#10;&#32;&#32;&#32;&#32;rdfs:range &#91; a owl:Class ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:unionOf ( &#60;https://schema.org/Place> aec3po:AdministrativeArea ) ] ;  &#10;&#32;&#32;&#32;&#32;owl:equivalentProperty &#60;https://schema.org/spatialCoverage> .</code></pre>|

***
### MinorFail Outcome number 124

[Jump to summary definition](#summary-MinorFail-124)	|	[Previous MinorFail outcome](#minorfail-outcome-number-123)	|	[Next MinorFail outcome](#minorfail-outcome-number-125)

:exclamation:MinorFail outcome
#### Subject detail
|Name|all-modules|
|----|----|
|Title|All the modules from branch main that are syntaxically correct as well as their recursive imports|
|Composition|- [Module aec3po](https://github.com/Accord-Project/aec3po/blob/main/src/aec3po.ttl)<br/>- [Module checking&lowbar;act](https://github.com/Accord-Project/aec3po/blob/main/src/checking_act.ttl)<br/>- [Module check&lowbar;method](https://github.com/Accord-Project/aec3po/blob/main/src/check_method.ttl)<br/>- [Module compliance&lowbar;verification&lowbar;report](https://github.com/Accord-Project/aec3po/blob/main/src/compliance_verification_report.ttl)<br/>- [Module data&lowbar;requirement](https://github.com/Accord-Project/aec3po/blob/main/src/data_requirement.ttl)<br/>- [Module document](https://github.com/Accord-Project/aec3po/blob/main/src/document.ttl)<br/>- [Module evidence](https://github.com/Accord-Project/aec3po/blob/main/src/evidence.ttl)<br/>- [Module feature&lowbar;of&lowbar;interest](https://github.com/Accord-Project/aec3po/blob/main/src/feature_of_interest.ttl)<br/>- [Module legal&lowbar;verifier](https://github.com/Accord-Project/aec3po/blob/main/src/legal_verifier.ttl)<br/>- [Module model](https://github.com/Accord-Project/aec3po/blob/main/src/model.ttl)<br/>- [Module rase&lowbar;statement](https://github.com/Accord-Project/aec3po/blob/main/src/rase_statement.ttl)<br/>- [Module statement](https://github.com/Accord-Project/aec3po/blob/main/src/statement.ttl)<br/>- [Module table](https://github.com/Accord-Project/aec3po/blob/main/src/table.ttl)<br/>- [Module vocabularies/administrative&lowbar;areas](https://github.com/Accord-Project/aec3po/blob/main/src/vocabularies/administrative_areas.ttl)<br/>- [Module vocabularies/building&lowbar;structure](https://github.com/Accord-Project/aec3po/blob/main/src/vocabularies/building_structure.ttl)<br/>- [Module vocabularies/building&lowbar;usage](https://github.com/Accord-Project/aec3po/blob/main/src/vocabularies/building_usage.ttl)<br/>- [Module vocabularies/check&lowbar;method&lowbar;comparators](https://github.com/Accord-Project/aec3po/blob/main/src/vocabularies/check_method_comparators.ttl)<br/>- [Module vocabularies/check&lowbar;method&lowbar;operators](https://github.com/Accord-Project/aec3po/blob/main/src/vocabularies/check_method_operators.ttl)<br/>- [Module vocabularies/disciplines](https://github.com/Accord-Project/aec3po/blob/main/src/vocabularies/disciplines.ttl)<br/>- [Module vocabularies/permitting&lowbar;stages](https://github.com/Accord-Project/aec3po/blob/main/src/vocabularies/permitting_stages.ttl)<br/>- [Module vocabularies/quantity&lowbar;kinds](https://github.com/Accord-Project/aec3po/blob/main/src/vocabularies/quantity_kinds.ttl)<br/>- [Module vocabularies/&lowbar;shape](https://github.com/Accord-Project/aec3po/blob/main/src/vocabularies/_shape.ttl)|

#### Criterion detail
|Identifier|[profile-compatibility](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#profile-compatibility)|
|----|----|
|Title|Profile compatibility test|
|Description|A test meant to check whether the test subject is compatible with a profile or not, and if it is not, why.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-124)|Identifier|`owl-rl-profile-error`|
|[Section top](#minorfail-outcome-number-124)|Title|OWL RL Profile incompatible|
|[Section top](#minorfail-outcome-number-124)|Description|Class Expression not supported with rdfs:subClassOf|
|[Section top](#minorfail-outcome-number-124)|Pointer|<pre lang="Turtle"><code>aec3po:AndCheckStatement a owl:Class ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;And Check Statement&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:comment &#34;Check verified if and only if all of its sub-checks are veri...&#34; ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy aec3po:statement ;  &#10;&#32;&#32;&#32;&#32;rdfs:subClassOf &#91; a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:onProperty aec3po:hasSubdivision ],  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;aec3po:ChecklistStatement .</code></pre>|
|[Section top](#minorfail-outcome-number-124)|Pointer|<pre lang="Turtle"><code>aec3po:CheckingAct a owl:Class ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;Checking Act&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:comment &#34;Act of checking some entities for something and generating a...&#34; ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy aec3po:checking&lowbar;act ;  &#10;&#32;&#32;&#32;&#32;rdfs:subClassOf &#91; a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:onProperty aec3po:usedMethod ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:someValuesFrom aec3po:CheckMethod ],  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#91; a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:onProperty aec3po:madeBy ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:someValuesFrom aec3po:ProcessVerifier ],  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#91; a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:onProperty aec3po:checked ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:someValuesFrom owl:Thing ],  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#91; a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:onProperty aec3po:hasReport ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:someValuesFrom aec3po:ComplianceVerificationReport ],  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#60;http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#Event> .</code></pre>|
|[Section top](#minorfail-outcome-number-124)|Pointer|<pre lang="Turtle"><code>aec3po:ComplianceVerificationReport a owl:Class ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;Compliance Verification Report&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:comment &#34;Result of a checking act. May be compliant or not.&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy aec3po:compliance&lowbar;verification&lowbar;report ;  &#10;&#32;&#32;&#32;&#32;rdfs:subClassOf &#91; a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:onProperty aec3po:conforms ] .</code></pre>|
|[Section top](#minorfail-outcome-number-124)|Pointer|<pre lang="Turtle"><code>aec3po:NotCheckStatement a owl:Class ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;Not Check Statement&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:comment &#34;Check verified if and only if the sub-check is not verified.&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy aec3po:statement ;  &#10;&#32;&#32;&#32;&#32;rdfs:subClassOf &#91; a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:onProperty aec3po:hasSubdivision ] .</code></pre>|
|[Section top](#minorfail-outcome-number-124)|Pointer|<pre lang="Turtle"><code>aec3po:OrCheckStatement a owl:Class ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;Or Check Statement&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:comment &#34;Check verified if and only if at least one of its sub-checks...&#34; ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy aec3po:statement ;  &#10;&#32;&#32;&#32;&#32;rdfs:subClassOf &#91; a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:onProperty aec3po:hasSubdivision ],  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;aec3po:ChecklistStatement .</code></pre>|
|[Section top](#minorfail-outcome-number-124)|Pointer|<pre lang="Turtle"><code>aec3po:VerificationResult a owl:Class ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;Verification Result&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:comment &#34;Individual verification result of a Compliance Verification ...&#34; ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy aec3po:compliance&lowbar;verification&lowbar;report ;  &#10;&#32;&#32;&#32;&#32;rdfs:subClassOf &#91; a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:onProperty aec3po:verificationFocus ],  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#91; a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:onProperty aec3po:hasSeverity ] .</code></pre>|

***
### MinorFail Outcome number 125

[Jump to summary definition](#summary-MinorFail-125)	|	[Previous MinorFail outcome](#minorfail-outcome-number-124)	|	[Next MinorFail outcome](#minorfail-outcome-number-126)

:exclamation:MinorFail outcome
#### Subject detail
|Name|all-modules|
|----|----|
|Title|All the modules from branch main that are syntaxically correct as well as their recursive imports|
|Composition|- [Module aec3po](https://github.com/Accord-Project/aec3po/blob/main/src/aec3po.ttl)<br/>- [Module checking&lowbar;act](https://github.com/Accord-Project/aec3po/blob/main/src/checking_act.ttl)<br/>- [Module check&lowbar;method](https://github.com/Accord-Project/aec3po/blob/main/src/check_method.ttl)<br/>- [Module compliance&lowbar;verification&lowbar;report](https://github.com/Accord-Project/aec3po/blob/main/src/compliance_verification_report.ttl)<br/>- [Module data&lowbar;requirement](https://github.com/Accord-Project/aec3po/blob/main/src/data_requirement.ttl)<br/>- [Module document](https://github.com/Accord-Project/aec3po/blob/main/src/document.ttl)<br/>- [Module evidence](https://github.com/Accord-Project/aec3po/blob/main/src/evidence.ttl)<br/>- [Module feature&lowbar;of&lowbar;interest](https://github.com/Accord-Project/aec3po/blob/main/src/feature_of_interest.ttl)<br/>- [Module legal&lowbar;verifier](https://github.com/Accord-Project/aec3po/blob/main/src/legal_verifier.ttl)<br/>- [Module model](https://github.com/Accord-Project/aec3po/blob/main/src/model.ttl)<br/>- [Module rase&lowbar;statement](https://github.com/Accord-Project/aec3po/blob/main/src/rase_statement.ttl)<br/>- [Module statement](https://github.com/Accord-Project/aec3po/blob/main/src/statement.ttl)<br/>- [Module table](https://github.com/Accord-Project/aec3po/blob/main/src/table.ttl)<br/>- [Module vocabularies/administrative&lowbar;areas](https://github.com/Accord-Project/aec3po/blob/main/src/vocabularies/administrative_areas.ttl)<br/>- [Module vocabularies/building&lowbar;structure](https://github.com/Accord-Project/aec3po/blob/main/src/vocabularies/building_structure.ttl)<br/>- [Module vocabularies/building&lowbar;usage](https://github.com/Accord-Project/aec3po/blob/main/src/vocabularies/building_usage.ttl)<br/>- [Module vocabularies/check&lowbar;method&lowbar;comparators](https://github.com/Accord-Project/aec3po/blob/main/src/vocabularies/check_method_comparators.ttl)<br/>- [Module vocabularies/check&lowbar;method&lowbar;operators](https://github.com/Accord-Project/aec3po/blob/main/src/vocabularies/check_method_operators.ttl)<br/>- [Module vocabularies/disciplines](https://github.com/Accord-Project/aec3po/blob/main/src/vocabularies/disciplines.ttl)<br/>- [Module vocabularies/permitting&lowbar;stages](https://github.com/Accord-Project/aec3po/blob/main/src/vocabularies/permitting_stages.ttl)<br/>- [Module vocabularies/quantity&lowbar;kinds](https://github.com/Accord-Project/aec3po/blob/main/src/vocabularies/quantity_kinds.ttl)<br/>- [Module vocabularies/&lowbar;shape](https://github.com/Accord-Project/aec3po/blob/main/src/vocabularies/_shape.ttl)|

#### Criterion detail
|Identifier|[profile-compatibility](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#profile-compatibility)|
|----|----|
|Title|Profile compatibility test|
|Description|A test meant to check whether the test subject is compatible with a profile or not, and if it is not, why.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-125)|Identifier|`owl-rl-profile-error`|
|[Section top](#minorfail-outcome-number-125)|Title|OWL RL Profile incompatible|
|[Section top](#minorfail-outcome-number-125)|Description|Class Expression not supported with owl:equivalentClass|
|[Section top](#minorfail-outcome-number-125)|Pointer|<pre lang="Turtle"><code>aec3po:ComponentCheckMethod a owl:Class ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;Component Check Method&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:comment &#34;Component check method refers to a process of inspecting and...&#34; ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy aec3po:check&lowbar;method ;  &#10;&#32;&#32;&#32;&#32;rdfs:subClassOf aec3po:CheckMethod ;  &#10;&#32;&#32;&#32;&#32;owl:equivalentClass &#91; a owl:Class ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:intersectionOf ( aec3po:CheckMethod &#91; a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:allValuesFrom &#91; a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:allValuesFrom aec3po:FeatureOfInterest ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:onProperty &#91; owl:inverseOf aec3po:forDesign ] ] ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:onProperty aec3po:forDesign ] ) ] .</code></pre>|

***
### MinorFail Outcome number 126

[Jump to summary definition](#summary-MinorFail-126)	|	[Previous MinorFail outcome](#minorfail-outcome-number-125)	|	[Next MinorFail outcome](#minorfail-outcome-number-127)

:exclamation:MinorFail outcome
#### Subject detail
|Name|all-modules|
|----|----|
|Title|All the modules from branch main that are syntaxically correct as well as their recursive imports|
|Composition|- [Module aec3po](https://github.com/Accord-Project/aec3po/blob/main/src/aec3po.ttl)<br/>- [Module checking&lowbar;act](https://github.com/Accord-Project/aec3po/blob/main/src/checking_act.ttl)<br/>- [Module check&lowbar;method](https://github.com/Accord-Project/aec3po/blob/main/src/check_method.ttl)<br/>- [Module compliance&lowbar;verification&lowbar;report](https://github.com/Accord-Project/aec3po/blob/main/src/compliance_verification_report.ttl)<br/>- [Module data&lowbar;requirement](https://github.com/Accord-Project/aec3po/blob/main/src/data_requirement.ttl)<br/>- [Module document](https://github.com/Accord-Project/aec3po/blob/main/src/document.ttl)<br/>- [Module evidence](https://github.com/Accord-Project/aec3po/blob/main/src/evidence.ttl)<br/>- [Module feature&lowbar;of&lowbar;interest](https://github.com/Accord-Project/aec3po/blob/main/src/feature_of_interest.ttl)<br/>- [Module legal&lowbar;verifier](https://github.com/Accord-Project/aec3po/blob/main/src/legal_verifier.ttl)<br/>- [Module model](https://github.com/Accord-Project/aec3po/blob/main/src/model.ttl)<br/>- [Module rase&lowbar;statement](https://github.com/Accord-Project/aec3po/blob/main/src/rase_statement.ttl)<br/>- [Module statement](https://github.com/Accord-Project/aec3po/blob/main/src/statement.ttl)<br/>- [Module table](https://github.com/Accord-Project/aec3po/blob/main/src/table.ttl)<br/>- [Module vocabularies/administrative&lowbar;areas](https://github.com/Accord-Project/aec3po/blob/main/src/vocabularies/administrative_areas.ttl)<br/>- [Module vocabularies/building&lowbar;structure](https://github.com/Accord-Project/aec3po/blob/main/src/vocabularies/building_structure.ttl)<br/>- [Module vocabularies/building&lowbar;usage](https://github.com/Accord-Project/aec3po/blob/main/src/vocabularies/building_usage.ttl)<br/>- [Module vocabularies/check&lowbar;method&lowbar;comparators](https://github.com/Accord-Project/aec3po/blob/main/src/vocabularies/check_method_comparators.ttl)<br/>- [Module vocabularies/check&lowbar;method&lowbar;operators](https://github.com/Accord-Project/aec3po/blob/main/src/vocabularies/check_method_operators.ttl)<br/>- [Module vocabularies/disciplines](https://github.com/Accord-Project/aec3po/blob/main/src/vocabularies/disciplines.ttl)<br/>- [Module vocabularies/permitting&lowbar;stages](https://github.com/Accord-Project/aec3po/blob/main/src/vocabularies/permitting_stages.ttl)<br/>- [Module vocabularies/quantity&lowbar;kinds](https://github.com/Accord-Project/aec3po/blob/main/src/vocabularies/quantity_kinds.ttl)<br/>- [Module vocabularies/&lowbar;shape](https://github.com/Accord-Project/aec3po/blob/main/src/vocabularies/_shape.ttl)|

#### Criterion detail
|Identifier|[profile-compatibility](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#profile-compatibility)|
|----|----|
|Title|Profile compatibility test|
|Description|A test meant to check whether the test subject is compatible with a profile or not, and if it is not, why.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-126)|Identifier|`owl-rl-profile-error`|
|[Section top](#minorfail-outcome-number-126)|Title|OWL RL Profile incompatible|
|[Section top](#minorfail-outcome-number-126)|Description|Statement not supported in a Super Class Expression|
|[Section top](#minorfail-outcome-number-126)|Pointer|<pre lang="Turtle"><code>&#91;] a owl:Class ;  &#10;&#32;&#32;&#32;&#32;owl:unionOf ( aec3po:FeatureOfInterest aec3po:Property aec3po:CheckMethod ) .</code></pre>|
|[Section top](#minorfail-outcome-number-126)|Pointer|<pre lang="Turtle"><code>&#91;] a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;owl:onProperty aec3po:usedMethod ;  &#10;&#32;&#32;&#32;&#32;owl:someValuesFrom aec3po:CheckMethod .</code></pre>|
|[Section top](#minorfail-outcome-number-126)|Pointer|<pre lang="Turtle"><code>&#91;] a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;owl:onProperty aec3po:madeBy ;  &#10;&#32;&#32;&#32;&#32;owl:someValuesFrom aec3po:ProcessVerifier .</code></pre>|
|[Section top](#minorfail-outcome-number-126)|Pointer|<pre lang="Turtle"><code>&#91;] a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;owl:onProperty aec3po:checked ;  &#10;&#32;&#32;&#32;&#32;owl:someValuesFrom owl:Thing .</code></pre>|
|[Section top](#minorfail-outcome-number-126)|Pointer|<pre lang="Turtle"><code>&#91;] a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;owl:onProperty aec3po:hasReport ;  &#10;&#32;&#32;&#32;&#32;owl:someValuesFrom aec3po:ComplianceVerificationReport .</code></pre>|
|[Section top](#minorfail-outcome-number-126)|Pointer|<pre lang="Turtle"><code>&#91;] a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;owl:onProperty aec3po:conforms .</code></pre>|
|[Section top](#minorfail-outcome-number-126)|Pointer|<pre lang="Turtle"><code>&#91;] a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;owl:onProperty aec3po:verificationFocus .</code></pre>|
|[Section top](#minorfail-outcome-number-126)|Pointer|<pre lang="Turtle"><code>&#91;] a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;owl:onProperty aec3po:hasSeverity .</code></pre>|
|[Section top](#minorfail-outcome-number-126)|Pointer|<pre lang="Turtle"><code>&#91;] owl:unionOf ( aec3po:Document aec3po:DocumentSubdivision ) .</code></pre>|
|[Section top](#minorfail-outcome-number-126)|Pointer|<pre lang="Turtle"><code>&#91;] a owl:Class ;  &#10;&#32;&#32;&#32;&#32;owl:unionOf ( &#60;https://schema.org/Place> aec3po:AdministrativeArea ) .</code></pre>|
|[Section top](#minorfail-outcome-number-126)|Pointer|<pre lang="Turtle"><code>&#91;] a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;owl:onProperty aec3po:hasSubdivision .</code></pre>|
|[Section top](#minorfail-outcome-number-126)|Pointer|<pre lang="Turtle"><code>&#91;] a owl:Class ;  &#10;&#32;&#32;&#32;&#32;owl:unionOf ( aec3po:Table aec3po:Image aec3po:Row aec3po:Column ) .</code></pre>|
|[Section top](#minorfail-outcome-number-126)|Pointer|<pre lang="Turtle"><code>&#91;] a owl:Class ;  &#10;&#32;&#32;&#32;&#32;owl:unionOf ( aec3po:Table aec3po:Image aec3po:Row aec3po:Column aec3po:Cell ) .</code></pre>|
|[Section top](#minorfail-outcome-number-126)|Pointer|<pre lang="Turtle"><code>&#91;] a owl:Class ;  &#10;&#32;&#32;&#32;&#32;owl:unionOf ( aec3po:Table aec3po:Image ) .</code></pre>|

***
### MinorFail Outcome number 127

[Jump to summary definition](#summary-MinorFail-127)	|	[Previous MinorFail outcome](#minorfail-outcome-number-126)	|	[Next MinorFail outcome](#minorfail-outcome-number-128)

:exclamation:MinorFail outcome
#### Subject detail
|Name|all-modules|
|----|----|
|Title|All the modules from branch main that are syntaxically correct as well as their recursive imports|
|Composition|- [Module aec3po](https://github.com/Accord-Project/aec3po/blob/main/src/aec3po.ttl)<br/>- [Module checking&lowbar;act](https://github.com/Accord-Project/aec3po/blob/main/src/checking_act.ttl)<br/>- [Module check&lowbar;method](https://github.com/Accord-Project/aec3po/blob/main/src/check_method.ttl)<br/>- [Module compliance&lowbar;verification&lowbar;report](https://github.com/Accord-Project/aec3po/blob/main/src/compliance_verification_report.ttl)<br/>- [Module data&lowbar;requirement](https://github.com/Accord-Project/aec3po/blob/main/src/data_requirement.ttl)<br/>- [Module document](https://github.com/Accord-Project/aec3po/blob/main/src/document.ttl)<br/>- [Module evidence](https://github.com/Accord-Project/aec3po/blob/main/src/evidence.ttl)<br/>- [Module feature&lowbar;of&lowbar;interest](https://github.com/Accord-Project/aec3po/blob/main/src/feature_of_interest.ttl)<br/>- [Module legal&lowbar;verifier](https://github.com/Accord-Project/aec3po/blob/main/src/legal_verifier.ttl)<br/>- [Module model](https://github.com/Accord-Project/aec3po/blob/main/src/model.ttl)<br/>- [Module rase&lowbar;statement](https://github.com/Accord-Project/aec3po/blob/main/src/rase_statement.ttl)<br/>- [Module statement](https://github.com/Accord-Project/aec3po/blob/main/src/statement.ttl)<br/>- [Module table](https://github.com/Accord-Project/aec3po/blob/main/src/table.ttl)<br/>- [Module vocabularies/administrative&lowbar;areas](https://github.com/Accord-Project/aec3po/blob/main/src/vocabularies/administrative_areas.ttl)<br/>- [Module vocabularies/building&lowbar;structure](https://github.com/Accord-Project/aec3po/blob/main/src/vocabularies/building_structure.ttl)<br/>- [Module vocabularies/building&lowbar;usage](https://github.com/Accord-Project/aec3po/blob/main/src/vocabularies/building_usage.ttl)<br/>- [Module vocabularies/check&lowbar;method&lowbar;comparators](https://github.com/Accord-Project/aec3po/blob/main/src/vocabularies/check_method_comparators.ttl)<br/>- [Module vocabularies/check&lowbar;method&lowbar;operators](https://github.com/Accord-Project/aec3po/blob/main/src/vocabularies/check_method_operators.ttl)<br/>- [Module vocabularies/disciplines](https://github.com/Accord-Project/aec3po/blob/main/src/vocabularies/disciplines.ttl)<br/>- [Module vocabularies/permitting&lowbar;stages](https://github.com/Accord-Project/aec3po/blob/main/src/vocabularies/permitting_stages.ttl)<br/>- [Module vocabularies/quantity&lowbar;kinds](https://github.com/Accord-Project/aec3po/blob/main/src/vocabularies/quantity_kinds.ttl)<br/>- [Module vocabularies/&lowbar;shape](https://github.com/Accord-Project/aec3po/blob/main/src/vocabularies/_shape.ttl)|

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
|[Section top](#minorfail-outcome-number-127)|Description|Statement not supported in a Sub Class Expression|
|[Section top](#minorfail-outcome-number-127)|Pointer|<pre lang="Turtle"><code>&#91;] a owl:Class ;  &#10;&#32;&#32;&#32;&#32;owl:intersectionOf ( aec3po:CheckMethod &#91; a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:allValuesFrom &#91; a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:allValuesFrom aec3po:FeatureOfInterest ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:onProperty &#91; owl:inverseOf aec3po:forDesign ] ] ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:onProperty aec3po:forDesign ] ) .</code></pre>|
|[Section top](#minorfail-outcome-number-127)|Pointer|<pre lang="Turtle"><code>&#91;] owl:intersectionOf ( skos:Concept &#91; a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:hasValue aec3po:AdministrativeAreaNomenclature ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:onProperty skos:inScheme ] ) .</code></pre>|
|[Section top](#minorfail-outcome-number-127)|Pointer|<pre lang="Turtle"><code>&#91;] owl:intersectionOf ( skos:Concept &#91; a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:hasValue aec3po:BuildingStructureNomenclature ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:onProperty skos:inScheme ] ) .</code></pre>|
|[Section top](#minorfail-outcome-number-127)|Pointer|<pre lang="Turtle"><code>&#91;] owl:intersectionOf ( skos:Concept &#91; a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:hasValue aec3po:BuildingUsageNomenclature ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:onProperty skos:inScheme ] ) .</code></pre>|
|[Section top](#minorfail-outcome-number-127)|Pointer|<pre lang="Turtle"><code>&#91;] owl:intersectionOf ( skos:Concept &#91; a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:hasValue aec3po:CheckMethodComparatorNomenclature ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:onProperty skos:inScheme ] ) .</code></pre>|
|[Section top](#minorfail-outcome-number-127)|Pointer|<pre lang="Turtle"><code>&#91;] owl:intersectionOf ( skos:Concept &#91; a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:hasValue aec3po:CheckMethodOperatorNomenclature ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:onProperty skos:inScheme ] ) .</code></pre>|
|[Section top](#minorfail-outcome-number-127)|Pointer|<pre lang="Turtle"><code>&#91;] owl:intersectionOf ( skos:Concept &#91; a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:hasValue aec3po:DisciplineNomenclature ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:onProperty skos:inScheme ] ) .</code></pre>|
|[Section top](#minorfail-outcome-number-127)|Pointer|<pre lang="Turtle"><code>&#91;] owl:intersectionOf ( skos:Concept &#91; a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:hasValue aec3po:PermittingStageNomenclature ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:onProperty skos:inScheme ] ) .</code></pre>|
|[Section top](#minorfail-outcome-number-127)|Pointer|<pre lang="Turtle"><code>&#91;] owl:intersectionOf ( skos:Concept &#91; a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:hasValue aec3po:QuantityKindNomenclature ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:onProperty skos:inScheme ] ) .</code></pre>|

***
### MinorFail Outcome number 128

[Jump to summary definition](#summary-MinorFail-128)	|	[Previous MinorFail outcome](#minorfail-outcome-number-127)	|	[Next MinorFail outcome](#minorfail-outcome-number-129)

:exclamation:MinorFail outcome
#### Subject detail
|Name|all-modules|
|----|----|
|Title|All the modules from branch main that are syntaxically correct as well as their recursive imports|
|Composition|- [Module aec3po](https://github.com/Accord-Project/aec3po/blob/main/src/aec3po.ttl)<br/>- [Module checking&lowbar;act](https://github.com/Accord-Project/aec3po/blob/main/src/checking_act.ttl)<br/>- [Module check&lowbar;method](https://github.com/Accord-Project/aec3po/blob/main/src/check_method.ttl)<br/>- [Module compliance&lowbar;verification&lowbar;report](https://github.com/Accord-Project/aec3po/blob/main/src/compliance_verification_report.ttl)<br/>- [Module data&lowbar;requirement](https://github.com/Accord-Project/aec3po/blob/main/src/data_requirement.ttl)<br/>- [Module document](https://github.com/Accord-Project/aec3po/blob/main/src/document.ttl)<br/>- [Module evidence](https://github.com/Accord-Project/aec3po/blob/main/src/evidence.ttl)<br/>- [Module feature&lowbar;of&lowbar;interest](https://github.com/Accord-Project/aec3po/blob/main/src/feature_of_interest.ttl)<br/>- [Module legal&lowbar;verifier](https://github.com/Accord-Project/aec3po/blob/main/src/legal_verifier.ttl)<br/>- [Module model](https://github.com/Accord-Project/aec3po/blob/main/src/model.ttl)<br/>- [Module rase&lowbar;statement](https://github.com/Accord-Project/aec3po/blob/main/src/rase_statement.ttl)<br/>- [Module statement](https://github.com/Accord-Project/aec3po/blob/main/src/statement.ttl)<br/>- [Module table](https://github.com/Accord-Project/aec3po/blob/main/src/table.ttl)<br/>- [Module vocabularies/administrative&lowbar;areas](https://github.com/Accord-Project/aec3po/blob/main/src/vocabularies/administrative_areas.ttl)<br/>- [Module vocabularies/building&lowbar;structure](https://github.com/Accord-Project/aec3po/blob/main/src/vocabularies/building_structure.ttl)<br/>- [Module vocabularies/building&lowbar;usage](https://github.com/Accord-Project/aec3po/blob/main/src/vocabularies/building_usage.ttl)<br/>- [Module vocabularies/check&lowbar;method&lowbar;comparators](https://github.com/Accord-Project/aec3po/blob/main/src/vocabularies/check_method_comparators.ttl)<br/>- [Module vocabularies/check&lowbar;method&lowbar;operators](https://github.com/Accord-Project/aec3po/blob/main/src/vocabularies/check_method_operators.ttl)<br/>- [Module vocabularies/disciplines](https://github.com/Accord-Project/aec3po/blob/main/src/vocabularies/disciplines.ttl)<br/>- [Module vocabularies/permitting&lowbar;stages](https://github.com/Accord-Project/aec3po/blob/main/src/vocabularies/permitting_stages.ttl)<br/>- [Module vocabularies/quantity&lowbar;kinds](https://github.com/Accord-Project/aec3po/blob/main/src/vocabularies/quantity_kinds.ttl)<br/>- [Module vocabularies/&lowbar;shape](https://github.com/Accord-Project/aec3po/blob/main/src/vocabularies/_shape.ttl)|

#### Criterion detail
|Identifier|[profile-compatibility](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#profile-compatibility)|
|----|----|
|Title|Profile compatibility test|
|Description|A test meant to check whether the test subject is compatible with a profile or not, and if it is not, why.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-128)|Identifier|`owl-ql-profile-error`|
|[Section top](#minorfail-outcome-number-128)|Title|OWL QL Profile incompatible|
|[Section top](#minorfail-outcome-number-128)|Description|Class Expression not supported as object of rdfs:domain or rdfs:range|
|[Section top](#minorfail-outcome-number-128)|Pointer|<pre lang="Turtle"><code>aec3po:caption a owl:DatatypeProperty ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;caption&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:comment &#34;The caption of a table, image, etc. &#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:domain &#91; a owl:Class ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:unionOf ( aec3po:Table aec3po:Image ) ] ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy aec3po:table .</code></pre>|
|[Section top](#minorfail-outcome-number-128)|Pointer|<pre lang="Turtle"><code>aec3po:contains a owl:ObjectProperty ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;Contains&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:comment &#34;A container contains a table and its caption. A table contai...&#34; ;  &#10;&#32;&#32;&#32;&#32;rdfs:domain &#91; a owl:Class ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:unionOf ( aec3po:Table aec3po:Image aec3po:Row aec3po:Column ) ] ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy aec3po:table .</code></pre>|
|[Section top](#minorfail-outcome-number-128)|Pointer|<pre lang="Turtle"><code>aec3po:hasBSSDDTarget a owl:FunctionalProperty,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:ObjectProperty ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;hasBSSDDTarget&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:comment &#34;The target refers to either the name of an object, the name ...&#34; ;  &#10;&#32;&#32;&#32;&#32;rdfs:domain &#91; a owl:Class ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:unionOf ( aec3po:FeatureOfInterest aec3po:Property aec3po:CheckMethod ) ] ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy aec3po:check&lowbar;method .</code></pre>|
|[Section top](#minorfail-outcome-number-128)|Pointer|<pre lang="Turtle"><code>aec3po:hasFirstSubdivision a owl:FunctionalProperty,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:ObjectProperty ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;has first subdivision&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:comment &#34;Links a document part to the first of its subdivision&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:domain &#91; owl:unionOf ( aec3po:Document aec3po:DocumentSubdivision ) ] ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy aec3po:document ;  &#10;&#32;&#32;&#32;&#32;rdfs:range aec3po:DocumentSubdivision ;  &#10;&#32;&#32;&#32;&#32;rdfs:subPropertyOf aec3po:hasSubdivision .</code></pre>|
|[Section top](#minorfail-outcome-number-128)|Pointer|<pre lang="Turtle"><code>aec3po:hasSubdivision a owl:ObjectProperty ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;has subdivision&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:comment &#34;links a document part to some of its subdivision&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:domain &#91; owl:unionOf ( aec3po:Document aec3po:DocumentSubdivision ) ] ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy aec3po:document ;  &#10;&#32;&#32;&#32;&#32;rdfs:range aec3po:DocumentSubdivision ;  &#10;&#32;&#32;&#32;&#32;rdfs:subPropertyOf dc:hasPart .</code></pre>|
|[Section top](#minorfail-outcome-number-128)|Pointer|<pre lang="Turtle"><code>aec3po:hasUnit a owl:FunctionalProperty,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:ObjectProperty ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;hasUnit&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:comment &#34;the hasUnit property is used to link a specific property or ...&#34; ;  &#10;&#32;&#32;&#32;&#32;rdfs:domain &#91; a owl:Class ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:unionOf ( aec3po:FeatureOfInterest aec3po:Property aec3po:CheckMethod ) ] ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy aec3po:check&lowbar;method ;  &#10;&#32;&#32;&#32;&#32;rdfs:range qudt:Unit ;  &#10;&#32;&#32;&#32;&#32;owl:eqivalentProperty qudt:hasValue .</code></pre>|
|[Section top](#minorfail-outcome-number-128)|Pointer|<pre lang="Turtle"><code>aec3po:hasValue a owl:DatatypeProperty,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:FunctionalProperty ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;has value&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:comment &#34;de facto used to link something (anything: property, propert...&#34; ;  &#10;&#32;&#32;&#32;&#32;rdfs:domain &#91; a owl:Class ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:unionOf ( aec3po:FeatureOfInterest aec3po:Property aec3po:CheckMethod ) ] ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy aec3po: ;  &#10;&#32;&#32;&#32;&#32;skos:note &#34;The value of the literal may be a XSD literal (boolean, inte...&#34; .</code></pre>|
|[Section top](#minorfail-outcome-number-128)|Pointer|<pre lang="Turtle"><code>aec3po:isContainedIn a owl:ObjectProperty ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;is contained by&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:comment &#34;A table contains row, columns and other elements.&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy aec3po:table ;  &#10;&#32;&#32;&#32;&#32;rdfs:range &#91; a owl:Class ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:unionOf ( aec3po:Table aec3po:Image aec3po:Row aec3po:Column aec3po:Cell ) ] .</code></pre>|
|[Section top](#minorfail-outcome-number-128)|Pointer|<pre lang="Turtle"><code>aec3po:locationCoverage a owl:ObjectProperty ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;location coverage&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:comment &#34;The spatialCoverage indicates the place(s) or the administra...&#34; ;  &#10;&#32;&#32;&#32;&#32;rdfs:domain &#60;https://schema.org/Model> ;  &#10;&#32;&#32;&#32;&#32;rdfs:range &#91; a owl:Class ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:unionOf ( &#60;https://schema.org/Place> aec3po:AdministrativeArea ) ] ;  &#10;&#32;&#32;&#32;&#32;owl:equivalentProperty &#60;https://schema.org/spatialCoverage> .</code></pre>|

***
### MinorFail Outcome number 129

[Jump to summary definition](#summary-MinorFail-129)	|	[Previous MinorFail outcome](#minorfail-outcome-number-128)	|	[Next MinorFail outcome](#minorfail-outcome-number-130)

:exclamation:MinorFail outcome
#### Subject detail
|Name|all-modules|
|----|----|
|Title|All the modules from branch main that are syntaxically correct as well as their recursive imports|
|Composition|- [Module aec3po](https://github.com/Accord-Project/aec3po/blob/main/src/aec3po.ttl)<br/>- [Module checking&lowbar;act](https://github.com/Accord-Project/aec3po/blob/main/src/checking_act.ttl)<br/>- [Module check&lowbar;method](https://github.com/Accord-Project/aec3po/blob/main/src/check_method.ttl)<br/>- [Module compliance&lowbar;verification&lowbar;report](https://github.com/Accord-Project/aec3po/blob/main/src/compliance_verification_report.ttl)<br/>- [Module data&lowbar;requirement](https://github.com/Accord-Project/aec3po/blob/main/src/data_requirement.ttl)<br/>- [Module document](https://github.com/Accord-Project/aec3po/blob/main/src/document.ttl)<br/>- [Module evidence](https://github.com/Accord-Project/aec3po/blob/main/src/evidence.ttl)<br/>- [Module feature&lowbar;of&lowbar;interest](https://github.com/Accord-Project/aec3po/blob/main/src/feature_of_interest.ttl)<br/>- [Module legal&lowbar;verifier](https://github.com/Accord-Project/aec3po/blob/main/src/legal_verifier.ttl)<br/>- [Module model](https://github.com/Accord-Project/aec3po/blob/main/src/model.ttl)<br/>- [Module rase&lowbar;statement](https://github.com/Accord-Project/aec3po/blob/main/src/rase_statement.ttl)<br/>- [Module statement](https://github.com/Accord-Project/aec3po/blob/main/src/statement.ttl)<br/>- [Module table](https://github.com/Accord-Project/aec3po/blob/main/src/table.ttl)<br/>- [Module vocabularies/administrative&lowbar;areas](https://github.com/Accord-Project/aec3po/blob/main/src/vocabularies/administrative_areas.ttl)<br/>- [Module vocabularies/building&lowbar;structure](https://github.com/Accord-Project/aec3po/blob/main/src/vocabularies/building_structure.ttl)<br/>- [Module vocabularies/building&lowbar;usage](https://github.com/Accord-Project/aec3po/blob/main/src/vocabularies/building_usage.ttl)<br/>- [Module vocabularies/check&lowbar;method&lowbar;comparators](https://github.com/Accord-Project/aec3po/blob/main/src/vocabularies/check_method_comparators.ttl)<br/>- [Module vocabularies/check&lowbar;method&lowbar;operators](https://github.com/Accord-Project/aec3po/blob/main/src/vocabularies/check_method_operators.ttl)<br/>- [Module vocabularies/disciplines](https://github.com/Accord-Project/aec3po/blob/main/src/vocabularies/disciplines.ttl)<br/>- [Module vocabularies/permitting&lowbar;stages](https://github.com/Accord-Project/aec3po/blob/main/src/vocabularies/permitting_stages.ttl)<br/>- [Module vocabularies/quantity&lowbar;kinds](https://github.com/Accord-Project/aec3po/blob/main/src/vocabularies/quantity_kinds.ttl)<br/>- [Module vocabularies/&lowbar;shape](https://github.com/Accord-Project/aec3po/blob/main/src/vocabularies/_shape.ttl)|

#### Criterion detail
|Identifier|[profile-compatibility](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#profile-compatibility)|
|----|----|
|Title|Profile compatibility test|
|Description|A test meant to check whether the test subject is compatible with a profile or not, and if it is not, why.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-129)|Identifier|`owl-ql-profile-error`|
|[Section top](#minorfail-outcome-number-129)|Title|OWL QL Profile incompatible|
|[Section top](#minorfail-outcome-number-129)|Description|Class Expression not supported with rdfs:subClassOf|
|[Section top](#minorfail-outcome-number-129)|Pointer|<pre lang="Turtle"><code>aec3po:AndCheckStatement a owl:Class ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;And Check Statement&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:comment &#34;Check verified if and only if all of its sub-checks are veri...&#34; ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy aec3po:statement ;  &#10;&#32;&#32;&#32;&#32;rdfs:subClassOf &#91; a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:onProperty aec3po:hasSubdivision ],  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;aec3po:ChecklistStatement .</code></pre>|
|[Section top](#minorfail-outcome-number-129)|Pointer|<pre lang="Turtle"><code>aec3po:ComplianceVerificationReport a owl:Class ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;Compliance Verification Report&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:comment &#34;Result of a checking act. May be compliant or not.&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy aec3po:compliance&lowbar;verification&lowbar;report ;  &#10;&#32;&#32;&#32;&#32;rdfs:subClassOf &#91; a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:onProperty aec3po:conforms ] .</code></pre>|
|[Section top](#minorfail-outcome-number-129)|Pointer|<pre lang="Turtle"><code>aec3po:DocumentSubdivision a owl:Class ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;Document Subdivision&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:comment &#34;Any subdivision of a document, including sections, paragraph...&#34; ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy aec3po:document ;  &#10;&#32;&#32;&#32;&#32;rdfs:subClassOf &#91; a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:allValuesFrom aec3po:DocumentSubdivision ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:onProperty aec3po:hasSubdivision ] ;  &#10;&#32;&#32;&#32;&#32;skos:example &#34;Paragraph, section, definition...&#34;@en .</code></pre>|
|[Section top](#minorfail-outcome-number-129)|Pointer|<pre lang="Turtle"><code>aec3po:LegalVerifier a owl:Class ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;Legal Verifier&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:comment &#34;An entity that has the legal capacity to verify compliance w...&#34; ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy aec3po:legal&lowbar;verifier ;  &#10;&#32;&#32;&#32;&#32;rdfs:subClassOf &#91; owl:allValuesFrom aec3po:Document ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:onProperty aec3po:forDocument ],  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;foaf:Agent .</code></pre>|
|[Section top](#minorfail-outcome-number-129)|Pointer|<pre lang="Turtle"><code>aec3po:NotCheckStatement a owl:Class ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;Not Check Statement&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:comment &#34;Check verified if and only if the sub-check is not verified.&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy aec3po:statement ;  &#10;&#32;&#32;&#32;&#32;rdfs:subClassOf &#91; a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:onProperty aec3po:hasSubdivision ] .</code></pre>|
|[Section top](#minorfail-outcome-number-129)|Pointer|<pre lang="Turtle"><code>aec3po:OrCheckStatement a owl:Class ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;Or Check Statement&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:comment &#34;Check verified if and only if at least one of its sub-checks...&#34; ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy aec3po:statement ;  &#10;&#32;&#32;&#32;&#32;rdfs:subClassOf &#91; a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:onProperty aec3po:hasSubdivision ],  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;aec3po:ChecklistStatement .</code></pre>|
|[Section top](#minorfail-outcome-number-129)|Pointer|<pre lang="Turtle"><code>aec3po:VerificationResult a owl:Class ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;Verification Result&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:comment &#34;Individual verification result of a Compliance Verification ...&#34; ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy aec3po:compliance&lowbar;verification&lowbar;report ;  &#10;&#32;&#32;&#32;&#32;rdfs:subClassOf &#91; a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:onProperty aec3po:verificationFocus ],  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#91; a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:onProperty aec3po:hasSeverity ] .</code></pre>|

***
### MinorFail Outcome number 130

[Jump to summary definition](#summary-MinorFail-130)	|	[Previous MinorFail outcome](#minorfail-outcome-number-129)	|	[Next MinorFail outcome](#minorfail-outcome-number-131)

:exclamation:MinorFail outcome
#### Subject detail
|Name|all-modules|
|----|----|
|Title|All the modules from branch main that are syntaxically correct as well as their recursive imports|
|Composition|- [Module aec3po](https://github.com/Accord-Project/aec3po/blob/main/src/aec3po.ttl)<br/>- [Module checking&lowbar;act](https://github.com/Accord-Project/aec3po/blob/main/src/checking_act.ttl)<br/>- [Module check&lowbar;method](https://github.com/Accord-Project/aec3po/blob/main/src/check_method.ttl)<br/>- [Module compliance&lowbar;verification&lowbar;report](https://github.com/Accord-Project/aec3po/blob/main/src/compliance_verification_report.ttl)<br/>- [Module data&lowbar;requirement](https://github.com/Accord-Project/aec3po/blob/main/src/data_requirement.ttl)<br/>- [Module document](https://github.com/Accord-Project/aec3po/blob/main/src/document.ttl)<br/>- [Module evidence](https://github.com/Accord-Project/aec3po/blob/main/src/evidence.ttl)<br/>- [Module feature&lowbar;of&lowbar;interest](https://github.com/Accord-Project/aec3po/blob/main/src/feature_of_interest.ttl)<br/>- [Module legal&lowbar;verifier](https://github.com/Accord-Project/aec3po/blob/main/src/legal_verifier.ttl)<br/>- [Module model](https://github.com/Accord-Project/aec3po/blob/main/src/model.ttl)<br/>- [Module rase&lowbar;statement](https://github.com/Accord-Project/aec3po/blob/main/src/rase_statement.ttl)<br/>- [Module statement](https://github.com/Accord-Project/aec3po/blob/main/src/statement.ttl)<br/>- [Module table](https://github.com/Accord-Project/aec3po/blob/main/src/table.ttl)<br/>- [Module vocabularies/administrative&lowbar;areas](https://github.com/Accord-Project/aec3po/blob/main/src/vocabularies/administrative_areas.ttl)<br/>- [Module vocabularies/building&lowbar;structure](https://github.com/Accord-Project/aec3po/blob/main/src/vocabularies/building_structure.ttl)<br/>- [Module vocabularies/building&lowbar;usage](https://github.com/Accord-Project/aec3po/blob/main/src/vocabularies/building_usage.ttl)<br/>- [Module vocabularies/check&lowbar;method&lowbar;comparators](https://github.com/Accord-Project/aec3po/blob/main/src/vocabularies/check_method_comparators.ttl)<br/>- [Module vocabularies/check&lowbar;method&lowbar;operators](https://github.com/Accord-Project/aec3po/blob/main/src/vocabularies/check_method_operators.ttl)<br/>- [Module vocabularies/disciplines](https://github.com/Accord-Project/aec3po/blob/main/src/vocabularies/disciplines.ttl)<br/>- [Module vocabularies/permitting&lowbar;stages](https://github.com/Accord-Project/aec3po/blob/main/src/vocabularies/permitting_stages.ttl)<br/>- [Module vocabularies/quantity&lowbar;kinds](https://github.com/Accord-Project/aec3po/blob/main/src/vocabularies/quantity_kinds.ttl)<br/>- [Module vocabularies/&lowbar;shape](https://github.com/Accord-Project/aec3po/blob/main/src/vocabularies/_shape.ttl)|

#### Criterion detail
|Identifier|[profile-compatibility](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#profile-compatibility)|
|----|----|
|Title|Profile compatibility test|
|Description|A test meant to check whether the test subject is compatible with a profile or not, and if it is not, why.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-130)|Identifier|`owl-ql-profile-error`|
|[Section top](#minorfail-outcome-number-130)|Title|OWL QL Profile incompatible|
|[Section top](#minorfail-outcome-number-130)|Description|Restriction on datatypes|
|[Section top](#minorfail-outcome-number-130)|Pointer|<pre lang="Turtle"><code>aec3po:conforms a owl:DatatypeProperty ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;conforms&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:comment &#34;True if the Checking act confirms the check was validated, a...&#34; ;  &#10;&#32;&#32;&#32;&#32;rdfs:domain aec3po:ComplianceVerificationReport ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy aec3po:compliance&lowbar;verification&lowbar;report ;  &#10;&#32;&#32;&#32;&#32;rdfs:range xsd:boolean .</code></pre>|
|[Section top](#minorfail-outcome-number-130)|Pointer|<pre lang="Turtle"><code>aec3po:hasBooleanTarget a owl:DatatypeProperty ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;hasBooleanTarget&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:comment &#34;TBD&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:range xsd:boolean .</code></pre>|

***
### MinorFail Outcome number 131

[Jump to summary definition](#summary-MinorFail-131)	|	[Previous MinorFail outcome](#minorfail-outcome-number-130)	|	[Next MinorFail outcome](#minorfail-outcome-number-132)

:exclamation:MinorFail outcome
#### Subject detail
|Name|all-modules|
|----|----|
|Title|All the modules from branch main that are syntaxically correct as well as their recursive imports|
|Composition|- [Module aec3po](https://github.com/Accord-Project/aec3po/blob/main/src/aec3po.ttl)<br/>- [Module checking&lowbar;act](https://github.com/Accord-Project/aec3po/blob/main/src/checking_act.ttl)<br/>- [Module check&lowbar;method](https://github.com/Accord-Project/aec3po/blob/main/src/check_method.ttl)<br/>- [Module compliance&lowbar;verification&lowbar;report](https://github.com/Accord-Project/aec3po/blob/main/src/compliance_verification_report.ttl)<br/>- [Module data&lowbar;requirement](https://github.com/Accord-Project/aec3po/blob/main/src/data_requirement.ttl)<br/>- [Module document](https://github.com/Accord-Project/aec3po/blob/main/src/document.ttl)<br/>- [Module evidence](https://github.com/Accord-Project/aec3po/blob/main/src/evidence.ttl)<br/>- [Module feature&lowbar;of&lowbar;interest](https://github.com/Accord-Project/aec3po/blob/main/src/feature_of_interest.ttl)<br/>- [Module legal&lowbar;verifier](https://github.com/Accord-Project/aec3po/blob/main/src/legal_verifier.ttl)<br/>- [Module model](https://github.com/Accord-Project/aec3po/blob/main/src/model.ttl)<br/>- [Module rase&lowbar;statement](https://github.com/Accord-Project/aec3po/blob/main/src/rase_statement.ttl)<br/>- [Module statement](https://github.com/Accord-Project/aec3po/blob/main/src/statement.ttl)<br/>- [Module table](https://github.com/Accord-Project/aec3po/blob/main/src/table.ttl)<br/>- [Module vocabularies/administrative&lowbar;areas](https://github.com/Accord-Project/aec3po/blob/main/src/vocabularies/administrative_areas.ttl)<br/>- [Module vocabularies/building&lowbar;structure](https://github.com/Accord-Project/aec3po/blob/main/src/vocabularies/building_structure.ttl)<br/>- [Module vocabularies/building&lowbar;usage](https://github.com/Accord-Project/aec3po/blob/main/src/vocabularies/building_usage.ttl)<br/>- [Module vocabularies/check&lowbar;method&lowbar;comparators](https://github.com/Accord-Project/aec3po/blob/main/src/vocabularies/check_method_comparators.ttl)<br/>- [Module vocabularies/check&lowbar;method&lowbar;operators](https://github.com/Accord-Project/aec3po/blob/main/src/vocabularies/check_method_operators.ttl)<br/>- [Module vocabularies/disciplines](https://github.com/Accord-Project/aec3po/blob/main/src/vocabularies/disciplines.ttl)<br/>- [Module vocabularies/permitting&lowbar;stages](https://github.com/Accord-Project/aec3po/blob/main/src/vocabularies/permitting_stages.ttl)<br/>- [Module vocabularies/quantity&lowbar;kinds](https://github.com/Accord-Project/aec3po/blob/main/src/vocabularies/quantity_kinds.ttl)<br/>- [Module vocabularies/&lowbar;shape](https://github.com/Accord-Project/aec3po/blob/main/src/vocabularies/_shape.ttl)|

#### Criterion detail
|Identifier|[profile-compatibility](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#profile-compatibility)|
|----|----|
|Title|Profile compatibility test|
|Description|A test meant to check whether the test subject is compatible with a profile or not, and if it is not, why.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-131)|Identifier|`owl-ql-profile-error`|
|[Section top](#minorfail-outcome-number-131)|Title|OWL QL Profile incompatible|
|[Section top](#minorfail-outcome-number-131)|Description|Class Expression not supported with owl:equivalentClass|
|[Section top](#minorfail-outcome-number-131)|Pointer|<pre lang="Turtle"><code>aec3po:AdministrativeArea a owl:Class ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;Administrative Area&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:comment &#34;Formally defined as the set of skos:Concept either in concep...&#34; ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy aec3po:administrative&lowbar;areas ;  &#10;&#32;&#32;&#32;&#32;rdfs:seeAlso &#60;https://op.europa.eu/en/web/eu-vocabularies/concept-scheme/-/resource?uri=http://publications.europa.eu/resource/authority/atu> ;  &#10;&#32;&#32;&#32;&#32;rdfs:subClassOf skos:Concept ;  &#10;&#32;&#32;&#32;&#32;owl:equivalentClass &#91; owl:intersectionOf ( skos:Concept &#91; a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:hasValue aec3po:AdministrativeAreaNomenclature ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:onProperty skos:inScheme ] ) ],  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#60;http://data.europa.eu/eli/ontology#AdministrativeArea> .</code></pre>|
|[Section top](#minorfail-outcome-number-131)|Pointer|<pre lang="Turtle"><code>aec3po:BuildingStructure a owl:Class ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;building structure&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:comment &#34;Formally defined as the set of skos:Concept in concept schem...&#34; ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy aec3po:building&lowbar;structure ;  &#10;&#32;&#32;&#32;&#32;rdfs:subClassOf skos:Concept,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;aec3po:Design ;  &#10;&#32;&#32;&#32;&#32;owl:equivalentClass &#91; owl:intersectionOf ( skos:Concept &#91; a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:hasValue aec3po:BuildingStructureNomenclature ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:onProperty skos:inScheme ] ) ] .</code></pre>|
|[Section top](#minorfail-outcome-number-131)|Pointer|<pre lang="Turtle"><code>aec3po:BuildingUsage a owl:Class ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;building usage&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:comment &#34;Formally defined as the set of skos:Concept in concept schem...&#34; ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy aec3po:building&lowbar;usage ;  &#10;&#32;&#32;&#32;&#32;rdfs:subClassOf skos:Concept,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;aec3po:Design ;  &#10;&#32;&#32;&#32;&#32;owl:equivalentClass &#91; owl:intersectionOf ( skos:Concept &#91; a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:hasValue aec3po:BuildingUsageNomenclature ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:onProperty skos:inScheme ] ) ] .</code></pre>|
|[Section top](#minorfail-outcome-number-131)|Pointer|<pre lang="Turtle"><code>aec3po:CheckMethodComparator a owl:Class ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;check method comparator&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:comment &#34;Formally defined as the set of skos:Concept in concept schem...&#34; ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy aec3po:check&lowbar;method&lowbar;comparators ;  &#10;&#32;&#32;&#32;&#32;rdfs:subClassOf skos:Concept,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;aec3po:CheckMethod ;  &#10;&#32;&#32;&#32;&#32;owl:equivalentClass &#91; owl:intersectionOf ( skos:Concept &#91; a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:hasValue aec3po:CheckMethodComparatorNomenclature ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:onProperty skos:inScheme ] ) ] .</code></pre>|
|[Section top](#minorfail-outcome-number-131)|Pointer|<pre lang="Turtle"><code>aec3po:CheckMethodOperator a owl:Class ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;check method operator&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:comment &#34;Formally defined as the set of skos:Concept in concept schem...&#34; ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy aec3po:check&lowbar;method&lowbar;operators ;  &#10;&#32;&#32;&#32;&#32;rdfs:subClassOf skos:Concept,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;aec3po:CheckMethod ;  &#10;&#32;&#32;&#32;&#32;owl:equivalentClass &#91; owl:intersectionOf ( skos:Concept &#91; a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:hasValue aec3po:CheckMethodOperatorNomenclature ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:onProperty skos:inScheme ] ) ] .</code></pre>|
|[Section top](#minorfail-outcome-number-131)|Pointer|<pre lang="Turtle"><code>aec3po:ComponentCheckMethod a owl:Class ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;Component Check Method&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:comment &#34;Component check method refers to a process of inspecting and...&#34; ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy aec3po:check&lowbar;method ;  &#10;&#32;&#32;&#32;&#32;rdfs:subClassOf aec3po:CheckMethod ;  &#10;&#32;&#32;&#32;&#32;owl:equivalentClass &#91; a owl:Class ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:intersectionOf ( aec3po:CheckMethod &#91; a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:allValuesFrom &#91; a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:allValuesFrom aec3po:FeatureOfInterest ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:onProperty &#91; owl:inverseOf aec3po:forDesign ] ] ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:onProperty aec3po:forDesign ] ) ] .</code></pre>|
|[Section top](#minorfail-outcome-number-131)|Pointer|<pre lang="Turtle"><code>aec3po:Discipline a owl:Class ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;Discipline&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:comment &#34;The AEC discipline to which something pertains.&#34; ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy aec3po:discipline ;  &#10;&#32;&#32;&#32;&#32;rdfs:subClassOf skos:Concept ;  &#10;&#32;&#32;&#32;&#32;owl:equivalentClass &#91; owl:intersectionOf ( skos:Concept &#91; a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:hasValue aec3po:DisciplineNomenclature ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:onProperty skos:inScheme ] ) ] .</code></pre>|
|[Section top](#minorfail-outcome-number-131)|Pointer|<pre lang="Turtle"><code>aec3po:PermittingStage a owl:Class ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;Permitting Stage&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:comment &#34;The class of permitting stages.&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy aec3po:permitting&lowbar;stage ;  &#10;&#32;&#32;&#32;&#32;rdfs:subClassOf skos:Concept ;  &#10;&#32;&#32;&#32;&#32;owl:equivalentClass &#91; owl:intersectionOf ( skos:Concept &#91; a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:hasValue aec3po:PermittingStageNomenclature ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:onProperty skos:inScheme ] ) ] .</code></pre>|
|[Section top](#minorfail-outcome-number-131)|Pointer|<pre lang="Turtle"><code>aec3po:QuantityKind a owl:Class ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;Quantity Kind&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:comment &#34;A Quantity Kind is any observable property that can be quant...&#34;,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#34;A kind of quantity.&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy aec3po:feature&lowbar;of&lowbar;interest,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;aec3po:quantity&lowbar;kinds ;  &#10;&#32;&#32;&#32;&#32;rdfs:subClassOf qudt:QuantityKind,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#60;http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#Region>,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;skos:Concept ;  &#10;&#32;&#32;&#32;&#32;owl:equivalentClass &#91; owl:intersectionOf ( skos:Concept &#91; a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:hasValue aec3po:QuantityKindNomenclature ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:onProperty skos:inScheme ] ) ] ;  &#10;&#32;&#32;&#32;&#32;skos:example &#34;Length, Area, U-Value.&#34;@en,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#34;height, area, U-value&#34;@en ;  &#10;&#32;&#32;&#32;&#32;skos:note &#34;Maxime Lefrançois argues that both qudt:QuantityKind and qud...&#34; .</code></pre>|

***
### MinorFail Outcome number 132

[Jump to summary definition](#summary-MinorFail-132)	|	[Previous MinorFail outcome](#minorfail-outcome-number-131)	|	[Next MinorFail outcome](#minorfail-outcome-number-133)

:exclamation:MinorFail outcome
#### Subject detail
|Name|all-modules|
|----|----|
|Title|All the modules from branch main that are syntaxically correct as well as their recursive imports|
|Composition|- [Module aec3po](https://github.com/Accord-Project/aec3po/blob/main/src/aec3po.ttl)<br/>- [Module checking&lowbar;act](https://github.com/Accord-Project/aec3po/blob/main/src/checking_act.ttl)<br/>- [Module check&lowbar;method](https://github.com/Accord-Project/aec3po/blob/main/src/check_method.ttl)<br/>- [Module compliance&lowbar;verification&lowbar;report](https://github.com/Accord-Project/aec3po/blob/main/src/compliance_verification_report.ttl)<br/>- [Module data&lowbar;requirement](https://github.com/Accord-Project/aec3po/blob/main/src/data_requirement.ttl)<br/>- [Module document](https://github.com/Accord-Project/aec3po/blob/main/src/document.ttl)<br/>- [Module evidence](https://github.com/Accord-Project/aec3po/blob/main/src/evidence.ttl)<br/>- [Module feature&lowbar;of&lowbar;interest](https://github.com/Accord-Project/aec3po/blob/main/src/feature_of_interest.ttl)<br/>- [Module legal&lowbar;verifier](https://github.com/Accord-Project/aec3po/blob/main/src/legal_verifier.ttl)<br/>- [Module model](https://github.com/Accord-Project/aec3po/blob/main/src/model.ttl)<br/>- [Module rase&lowbar;statement](https://github.com/Accord-Project/aec3po/blob/main/src/rase_statement.ttl)<br/>- [Module statement](https://github.com/Accord-Project/aec3po/blob/main/src/statement.ttl)<br/>- [Module table](https://github.com/Accord-Project/aec3po/blob/main/src/table.ttl)<br/>- [Module vocabularies/administrative&lowbar;areas](https://github.com/Accord-Project/aec3po/blob/main/src/vocabularies/administrative_areas.ttl)<br/>- [Module vocabularies/building&lowbar;structure](https://github.com/Accord-Project/aec3po/blob/main/src/vocabularies/building_structure.ttl)<br/>- [Module vocabularies/building&lowbar;usage](https://github.com/Accord-Project/aec3po/blob/main/src/vocabularies/building_usage.ttl)<br/>- [Module vocabularies/check&lowbar;method&lowbar;comparators](https://github.com/Accord-Project/aec3po/blob/main/src/vocabularies/check_method_comparators.ttl)<br/>- [Module vocabularies/check&lowbar;method&lowbar;operators](https://github.com/Accord-Project/aec3po/blob/main/src/vocabularies/check_method_operators.ttl)<br/>- [Module vocabularies/disciplines](https://github.com/Accord-Project/aec3po/blob/main/src/vocabularies/disciplines.ttl)<br/>- [Module vocabularies/permitting&lowbar;stages](https://github.com/Accord-Project/aec3po/blob/main/src/vocabularies/permitting_stages.ttl)<br/>- [Module vocabularies/quantity&lowbar;kinds](https://github.com/Accord-Project/aec3po/blob/main/src/vocabularies/quantity_kinds.ttl)<br/>- [Module vocabularies/&lowbar;shape](https://github.com/Accord-Project/aec3po/blob/main/src/vocabularies/_shape.ttl)|

#### Criterion detail
|Identifier|[profile-compatibility](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#profile-compatibility)|
|----|----|
|Title|Profile compatibility test|
|Description|A test meant to check whether the test subject is compatible with a profile or not, and if it is not, why.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-132)|Identifier|`owl-ql-profile-error`|
|[Section top](#minorfail-outcome-number-132)|Title|OWL QL Profile incompatible|
|[Section top](#minorfail-outcome-number-132)|Description|Statement not supported in a Super Class Expression|
|[Section top](#minorfail-outcome-number-132)|Pointer|<pre lang="Turtle"><code>&#91;] a owl:Class ;  &#10;&#32;&#32;&#32;&#32;owl:unionOf ( aec3po:FeatureOfInterest aec3po:Property aec3po:CheckMethod ) .</code></pre>|
|[Section top](#minorfail-outcome-number-132)|Pointer|<pre lang="Turtle"><code>&#91;] a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;owl:onProperty aec3po:conforms .</code></pre>|
|[Section top](#minorfail-outcome-number-132)|Pointer|<pre lang="Turtle"><code>&#91;] a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;owl:onProperty aec3po:verificationFocus .</code></pre>|
|[Section top](#minorfail-outcome-number-132)|Pointer|<pre lang="Turtle"><code>&#91;] a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;owl:onProperty aec3po:hasSeverity .</code></pre>|
|[Section top](#minorfail-outcome-number-132)|Pointer|<pre lang="Turtle"><code>&#91;] a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;owl:allValuesFrom aec3po:DocumentSubdivision ;  &#10;&#32;&#32;&#32;&#32;owl:onProperty aec3po:hasSubdivision .</code></pre>|
|[Section top](#minorfail-outcome-number-132)|Pointer|<pre lang="Turtle"><code>&#91;] owl:unionOf ( aec3po:Document aec3po:DocumentSubdivision ) .</code></pre>|
|[Section top](#minorfail-outcome-number-132)|Pointer|<pre lang="Turtle"><code>&#91;] owl:allValuesFrom aec3po:Document ;  &#10;&#32;&#32;&#32;&#32;owl:onProperty aec3po:forDocument .</code></pre>|
|[Section top](#minorfail-outcome-number-132)|Pointer|<pre lang="Turtle"><code>&#91;] a owl:Class ;  &#10;&#32;&#32;&#32;&#32;owl:unionOf ( &#60;https://schema.org/Place> aec3po:AdministrativeArea ) .</code></pre>|
|[Section top](#minorfail-outcome-number-132)|Pointer|<pre lang="Turtle"><code>&#91;] a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;owl:onProperty aec3po:hasSubdivision .</code></pre>|
|[Section top](#minorfail-outcome-number-132)|Pointer|<pre lang="Turtle"><code>&#91;] a owl:Class ;  &#10;&#32;&#32;&#32;&#32;owl:unionOf ( aec3po:Table aec3po:Image aec3po:Row aec3po:Column ) .</code></pre>|
|[Section top](#minorfail-outcome-number-132)|Pointer|<pre lang="Turtle"><code>&#91;] a owl:Class ;  &#10;&#32;&#32;&#32;&#32;owl:unionOf ( aec3po:Table aec3po:Image aec3po:Row aec3po:Column aec3po:Cell ) .</code></pre>|
|[Section top](#minorfail-outcome-number-132)|Pointer|<pre lang="Turtle"><code>&#91;] a owl:Class ;  &#10;&#32;&#32;&#32;&#32;owl:unionOf ( aec3po:Table aec3po:Image ) .</code></pre>|

***
### MinorFail Outcome number 133

[Jump to summary definition](#summary-MinorFail-133)	|	[Previous MinorFail outcome](#minorfail-outcome-number-132)	|	[Next MinorFail outcome](#minorfail-outcome-number-134)

:exclamation:MinorFail outcome
#### Subject detail
|Name|all-modules|
|----|----|
|Title|All the modules from branch main that are syntaxically correct as well as their recursive imports|
|Composition|- [Module aec3po](https://github.com/Accord-Project/aec3po/blob/main/src/aec3po.ttl)<br/>- [Module checking&lowbar;act](https://github.com/Accord-Project/aec3po/blob/main/src/checking_act.ttl)<br/>- [Module check&lowbar;method](https://github.com/Accord-Project/aec3po/blob/main/src/check_method.ttl)<br/>- [Module compliance&lowbar;verification&lowbar;report](https://github.com/Accord-Project/aec3po/blob/main/src/compliance_verification_report.ttl)<br/>- [Module data&lowbar;requirement](https://github.com/Accord-Project/aec3po/blob/main/src/data_requirement.ttl)<br/>- [Module document](https://github.com/Accord-Project/aec3po/blob/main/src/document.ttl)<br/>- [Module evidence](https://github.com/Accord-Project/aec3po/blob/main/src/evidence.ttl)<br/>- [Module feature&lowbar;of&lowbar;interest](https://github.com/Accord-Project/aec3po/blob/main/src/feature_of_interest.ttl)<br/>- [Module legal&lowbar;verifier](https://github.com/Accord-Project/aec3po/blob/main/src/legal_verifier.ttl)<br/>- [Module model](https://github.com/Accord-Project/aec3po/blob/main/src/model.ttl)<br/>- [Module rase&lowbar;statement](https://github.com/Accord-Project/aec3po/blob/main/src/rase_statement.ttl)<br/>- [Module statement](https://github.com/Accord-Project/aec3po/blob/main/src/statement.ttl)<br/>- [Module table](https://github.com/Accord-Project/aec3po/blob/main/src/table.ttl)<br/>- [Module vocabularies/administrative&lowbar;areas](https://github.com/Accord-Project/aec3po/blob/main/src/vocabularies/administrative_areas.ttl)<br/>- [Module vocabularies/building&lowbar;structure](https://github.com/Accord-Project/aec3po/blob/main/src/vocabularies/building_structure.ttl)<br/>- [Module vocabularies/building&lowbar;usage](https://github.com/Accord-Project/aec3po/blob/main/src/vocabularies/building_usage.ttl)<br/>- [Module vocabularies/check&lowbar;method&lowbar;comparators](https://github.com/Accord-Project/aec3po/blob/main/src/vocabularies/check_method_comparators.ttl)<br/>- [Module vocabularies/check&lowbar;method&lowbar;operators](https://github.com/Accord-Project/aec3po/blob/main/src/vocabularies/check_method_operators.ttl)<br/>- [Module vocabularies/disciplines](https://github.com/Accord-Project/aec3po/blob/main/src/vocabularies/disciplines.ttl)<br/>- [Module vocabularies/permitting&lowbar;stages](https://github.com/Accord-Project/aec3po/blob/main/src/vocabularies/permitting_stages.ttl)<br/>- [Module vocabularies/quantity&lowbar;kinds](https://github.com/Accord-Project/aec3po/blob/main/src/vocabularies/quantity_kinds.ttl)<br/>- [Module vocabularies/&lowbar;shape](https://github.com/Accord-Project/aec3po/blob/main/src/vocabularies/_shape.ttl)|

#### Criterion detail
|Identifier|[profile-compatibility](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#profile-compatibility)|
|----|----|
|Title|Profile compatibility test|
|Description|A test meant to check whether the test subject is compatible with a profile or not, and if it is not, why.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-133)|Identifier|`owl-el-profile-error`|
|[Section top](#minorfail-outcome-number-133)|Title|OWL EL Profile incompatible|
|[Section top](#minorfail-outcome-number-133)|Description|Statement not supported in a Class Expression|
|[Section top](#minorfail-outcome-number-133)|Pointer|<pre lang="Turtle"><code>&#91;] a owl:Class ;  &#10;&#32;&#32;&#32;&#32;owl:unionOf ( aec3po:FeatureOfInterest aec3po:Property aec3po:CheckMethod ) .</code></pre>|
|[Section top](#minorfail-outcome-number-133)|Pointer|<pre lang="Turtle"><code>&#91;] a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;owl:allValuesFrom &#91; a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:allValuesFrom aec3po:FeatureOfInterest ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:onProperty &#91; owl:inverseOf aec3po:forDesign ] ] ;  &#10;&#32;&#32;&#32;&#32;owl:onProperty aec3po:forDesign .</code></pre>|
|[Section top](#minorfail-outcome-number-133)|Pointer|<pre lang="Turtle"><code>&#91;] a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;owl:onProperty aec3po:conforms .</code></pre>|
|[Section top](#minorfail-outcome-number-133)|Pointer|<pre lang="Turtle"><code>&#91;] a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;owl:onProperty aec3po:verificationFocus .</code></pre>|
|[Section top](#minorfail-outcome-number-133)|Pointer|<pre lang="Turtle"><code>&#91;] a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;owl:onProperty aec3po:hasSeverity .</code></pre>|
|[Section top](#minorfail-outcome-number-133)|Pointer|<pre lang="Turtle"><code>&#91;] a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;owl:allValuesFrom aec3po:DocumentSubdivision ;  &#10;&#32;&#32;&#32;&#32;owl:onProperty aec3po:hasSubdivision .</code></pre>|
|[Section top](#minorfail-outcome-number-133)|Pointer|<pre lang="Turtle"><code>&#91;] owl:unionOf ( aec3po:Document aec3po:DocumentSubdivision ) .</code></pre>|
|[Section top](#minorfail-outcome-number-133)|Pointer|<pre lang="Turtle"><code>&#91;] owl:allValuesFrom aec3po:Document ;  &#10;&#32;&#32;&#32;&#32;owl:onProperty aec3po:forDocument .</code></pre>|
|[Section top](#minorfail-outcome-number-133)|Pointer|<pre lang="Turtle"><code>&#91;] a owl:Class ;  &#10;&#32;&#32;&#32;&#32;owl:unionOf ( &#60;https://schema.org/Place> aec3po:AdministrativeArea ) .</code></pre>|
|[Section top](#minorfail-outcome-number-133)|Pointer|<pre lang="Turtle"><code>&#91;] a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;owl:onProperty aec3po:hasSubdivision .</code></pre>|
|[Section top](#minorfail-outcome-number-133)|Pointer|<pre lang="Turtle"><code>&#91;] a owl:Class ;  &#10;&#32;&#32;&#32;&#32;owl:unionOf ( aec3po:Table aec3po:Image aec3po:Row aec3po:Column ) .</code></pre>|
|[Section top](#minorfail-outcome-number-133)|Pointer|<pre lang="Turtle"><code>&#91;] a owl:Class ;  &#10;&#32;&#32;&#32;&#32;owl:unionOf ( aec3po:Table aec3po:Image aec3po:Row aec3po:Column aec3po:Cell ) .</code></pre>|
|[Section top](#minorfail-outcome-number-133)|Pointer|<pre lang="Turtle"><code>&#91;] a owl:Class ;  &#10;&#32;&#32;&#32;&#32;owl:unionOf ( aec3po:Table aec3po:Image ) .</code></pre>|

***
### MinorFail Outcome number 134

[Jump to summary definition](#summary-MinorFail-134)	|	[Previous MinorFail outcome](#minorfail-outcome-number-133)	|	[Next MinorFail outcome](#minorfail-outcome-number-135)

:exclamation:MinorFail outcome
#### Subject detail
|Name|all-modules|
|----|----|
|Title|All the modules from branch main that are syntaxically correct as well as their recursive imports|
|Composition|- [Module aec3po](https://github.com/Accord-Project/aec3po/blob/main/src/aec3po.ttl)<br/>- [Module checking&lowbar;act](https://github.com/Accord-Project/aec3po/blob/main/src/checking_act.ttl)<br/>- [Module check&lowbar;method](https://github.com/Accord-Project/aec3po/blob/main/src/check_method.ttl)<br/>- [Module compliance&lowbar;verification&lowbar;report](https://github.com/Accord-Project/aec3po/blob/main/src/compliance_verification_report.ttl)<br/>- [Module data&lowbar;requirement](https://github.com/Accord-Project/aec3po/blob/main/src/data_requirement.ttl)<br/>- [Module document](https://github.com/Accord-Project/aec3po/blob/main/src/document.ttl)<br/>- [Module evidence](https://github.com/Accord-Project/aec3po/blob/main/src/evidence.ttl)<br/>- [Module feature&lowbar;of&lowbar;interest](https://github.com/Accord-Project/aec3po/blob/main/src/feature_of_interest.ttl)<br/>- [Module legal&lowbar;verifier](https://github.com/Accord-Project/aec3po/blob/main/src/legal_verifier.ttl)<br/>- [Module model](https://github.com/Accord-Project/aec3po/blob/main/src/model.ttl)<br/>- [Module rase&lowbar;statement](https://github.com/Accord-Project/aec3po/blob/main/src/rase_statement.ttl)<br/>- [Module statement](https://github.com/Accord-Project/aec3po/blob/main/src/statement.ttl)<br/>- [Module table](https://github.com/Accord-Project/aec3po/blob/main/src/table.ttl)<br/>- [Module vocabularies/administrative&lowbar;areas](https://github.com/Accord-Project/aec3po/blob/main/src/vocabularies/administrative_areas.ttl)<br/>- [Module vocabularies/building&lowbar;structure](https://github.com/Accord-Project/aec3po/blob/main/src/vocabularies/building_structure.ttl)<br/>- [Module vocabularies/building&lowbar;usage](https://github.com/Accord-Project/aec3po/blob/main/src/vocabularies/building_usage.ttl)<br/>- [Module vocabularies/check&lowbar;method&lowbar;comparators](https://github.com/Accord-Project/aec3po/blob/main/src/vocabularies/check_method_comparators.ttl)<br/>- [Module vocabularies/check&lowbar;method&lowbar;operators](https://github.com/Accord-Project/aec3po/blob/main/src/vocabularies/check_method_operators.ttl)<br/>- [Module vocabularies/disciplines](https://github.com/Accord-Project/aec3po/blob/main/src/vocabularies/disciplines.ttl)<br/>- [Module vocabularies/permitting&lowbar;stages](https://github.com/Accord-Project/aec3po/blob/main/src/vocabularies/permitting_stages.ttl)<br/>- [Module vocabularies/quantity&lowbar;kinds](https://github.com/Accord-Project/aec3po/blob/main/src/vocabularies/quantity_kinds.ttl)<br/>- [Module vocabularies/&lowbar;shape](https://github.com/Accord-Project/aec3po/blob/main/src/vocabularies/_shape.ttl)|

#### Criterion detail
|Identifier|[profile-compatibility](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#profile-compatibility)|
|----|----|
|Title|Profile compatibility test|
|Description|A test meant to check whether the test subject is compatible with a profile or not, and if it is not, why.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-134)|Identifier|`owl-el-profile-error`|
|[Section top](#minorfail-outcome-number-134)|Title|OWL EL Profile incompatible|
|[Section top](#minorfail-outcome-number-134)|Description|Class Expression not supported as object of rdfs:domain or rdfs:range|
|[Section top](#minorfail-outcome-number-134)|Pointer|<pre lang="Turtle"><code>aec3po:caption a owl:DatatypeProperty ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;caption&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:comment &#34;The caption of a table, image, etc. &#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:domain &#91; a owl:Class ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:unionOf ( aec3po:Table aec3po:Image ) ] ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy aec3po:table .</code></pre>|
|[Section top](#minorfail-outcome-number-134)|Pointer|<pre lang="Turtle"><code>aec3po:contains a owl:ObjectProperty ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;Contains&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:comment &#34;A container contains a table and its caption. A table contai...&#34; ;  &#10;&#32;&#32;&#32;&#32;rdfs:domain &#91; a owl:Class ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:unionOf ( aec3po:Table aec3po:Image aec3po:Row aec3po:Column ) ] ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy aec3po:table .</code></pre>|
|[Section top](#minorfail-outcome-number-134)|Pointer|<pre lang="Turtle"><code>aec3po:hasBSSDDTarget a owl:FunctionalProperty,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:ObjectProperty ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;hasBSSDDTarget&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:comment &#34;The target refers to either the name of an object, the name ...&#34; ;  &#10;&#32;&#32;&#32;&#32;rdfs:domain &#91; a owl:Class ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:unionOf ( aec3po:FeatureOfInterest aec3po:Property aec3po:CheckMethod ) ] ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy aec3po:check&lowbar;method .</code></pre>|
|[Section top](#minorfail-outcome-number-134)|Pointer|<pre lang="Turtle"><code>aec3po:hasFirstSubdivision a owl:FunctionalProperty,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:ObjectProperty ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;has first subdivision&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:comment &#34;Links a document part to the first of its subdivision&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:domain &#91; owl:unionOf ( aec3po:Document aec3po:DocumentSubdivision ) ] ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy aec3po:document ;  &#10;&#32;&#32;&#32;&#32;rdfs:range aec3po:DocumentSubdivision ;  &#10;&#32;&#32;&#32;&#32;rdfs:subPropertyOf aec3po:hasSubdivision .</code></pre>|
|[Section top](#minorfail-outcome-number-134)|Pointer|<pre lang="Turtle"><code>aec3po:hasSubdivision a owl:ObjectProperty ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;has subdivision&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:comment &#34;links a document part to some of its subdivision&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:domain &#91; owl:unionOf ( aec3po:Document aec3po:DocumentSubdivision ) ] ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy aec3po:document ;  &#10;&#32;&#32;&#32;&#32;rdfs:range aec3po:DocumentSubdivision ;  &#10;&#32;&#32;&#32;&#32;rdfs:subPropertyOf dc:hasPart .</code></pre>|
|[Section top](#minorfail-outcome-number-134)|Pointer|<pre lang="Turtle"><code>aec3po:hasUnit a owl:FunctionalProperty,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:ObjectProperty ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;hasUnit&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:comment &#34;the hasUnit property is used to link a specific property or ...&#34; ;  &#10;&#32;&#32;&#32;&#32;rdfs:domain &#91; a owl:Class ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:unionOf ( aec3po:FeatureOfInterest aec3po:Property aec3po:CheckMethod ) ] ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy aec3po:check&lowbar;method ;  &#10;&#32;&#32;&#32;&#32;rdfs:range qudt:Unit ;  &#10;&#32;&#32;&#32;&#32;owl:eqivalentProperty qudt:hasValue .</code></pre>|
|[Section top](#minorfail-outcome-number-134)|Pointer|<pre lang="Turtle"><code>aec3po:hasValue a owl:DatatypeProperty,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:FunctionalProperty ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;has value&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:comment &#34;de facto used to link something (anything: property, propert...&#34; ;  &#10;&#32;&#32;&#32;&#32;rdfs:domain &#91; a owl:Class ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:unionOf ( aec3po:FeatureOfInterest aec3po:Property aec3po:CheckMethod ) ] ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy aec3po: ;  &#10;&#32;&#32;&#32;&#32;skos:note &#34;The value of the literal may be a XSD literal (boolean, inte...&#34; .</code></pre>|
|[Section top](#minorfail-outcome-number-134)|Pointer|<pre lang="Turtle"><code>aec3po:isContainedIn a owl:ObjectProperty ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;is contained by&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:comment &#34;A table contains row, columns and other elements.&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy aec3po:table ;  &#10;&#32;&#32;&#32;&#32;rdfs:range &#91; a owl:Class ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:unionOf ( aec3po:Table aec3po:Image aec3po:Row aec3po:Column aec3po:Cell ) ] .</code></pre>|
|[Section top](#minorfail-outcome-number-134)|Pointer|<pre lang="Turtle"><code>aec3po:locationCoverage a owl:ObjectProperty ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;location coverage&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:comment &#34;The spatialCoverage indicates the place(s) or the administra...&#34; ;  &#10;&#32;&#32;&#32;&#32;rdfs:domain &#60;https://schema.org/Model> ;  &#10;&#32;&#32;&#32;&#32;rdfs:range &#91; a owl:Class ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:unionOf ( &#60;https://schema.org/Place> aec3po:AdministrativeArea ) ] ;  &#10;&#32;&#32;&#32;&#32;owl:equivalentProperty &#60;https://schema.org/spatialCoverage> .</code></pre>|

***
### MinorFail Outcome number 135

[Jump to summary definition](#summary-MinorFail-135)	|	[Previous MinorFail outcome](#minorfail-outcome-number-134)	|	[Next MinorFail outcome](#minorfail-outcome-number-136)

:exclamation:MinorFail outcome
#### Subject detail
|Name|all-modules|
|----|----|
|Title|All the modules from branch main that are syntaxically correct as well as their recursive imports|
|Composition|- [Module aec3po](https://github.com/Accord-Project/aec3po/blob/main/src/aec3po.ttl)<br/>- [Module checking&lowbar;act](https://github.com/Accord-Project/aec3po/blob/main/src/checking_act.ttl)<br/>- [Module check&lowbar;method](https://github.com/Accord-Project/aec3po/blob/main/src/check_method.ttl)<br/>- [Module compliance&lowbar;verification&lowbar;report](https://github.com/Accord-Project/aec3po/blob/main/src/compliance_verification_report.ttl)<br/>- [Module data&lowbar;requirement](https://github.com/Accord-Project/aec3po/blob/main/src/data_requirement.ttl)<br/>- [Module document](https://github.com/Accord-Project/aec3po/blob/main/src/document.ttl)<br/>- [Module evidence](https://github.com/Accord-Project/aec3po/blob/main/src/evidence.ttl)<br/>- [Module feature&lowbar;of&lowbar;interest](https://github.com/Accord-Project/aec3po/blob/main/src/feature_of_interest.ttl)<br/>- [Module legal&lowbar;verifier](https://github.com/Accord-Project/aec3po/blob/main/src/legal_verifier.ttl)<br/>- [Module model](https://github.com/Accord-Project/aec3po/blob/main/src/model.ttl)<br/>- [Module rase&lowbar;statement](https://github.com/Accord-Project/aec3po/blob/main/src/rase_statement.ttl)<br/>- [Module statement](https://github.com/Accord-Project/aec3po/blob/main/src/statement.ttl)<br/>- [Module table](https://github.com/Accord-Project/aec3po/blob/main/src/table.ttl)<br/>- [Module vocabularies/administrative&lowbar;areas](https://github.com/Accord-Project/aec3po/blob/main/src/vocabularies/administrative_areas.ttl)<br/>- [Module vocabularies/building&lowbar;structure](https://github.com/Accord-Project/aec3po/blob/main/src/vocabularies/building_structure.ttl)<br/>- [Module vocabularies/building&lowbar;usage](https://github.com/Accord-Project/aec3po/blob/main/src/vocabularies/building_usage.ttl)<br/>- [Module vocabularies/check&lowbar;method&lowbar;comparators](https://github.com/Accord-Project/aec3po/blob/main/src/vocabularies/check_method_comparators.ttl)<br/>- [Module vocabularies/check&lowbar;method&lowbar;operators](https://github.com/Accord-Project/aec3po/blob/main/src/vocabularies/check_method_operators.ttl)<br/>- [Module vocabularies/disciplines](https://github.com/Accord-Project/aec3po/blob/main/src/vocabularies/disciplines.ttl)<br/>- [Module vocabularies/permitting&lowbar;stages](https://github.com/Accord-Project/aec3po/blob/main/src/vocabularies/permitting_stages.ttl)<br/>- [Module vocabularies/quantity&lowbar;kinds](https://github.com/Accord-Project/aec3po/blob/main/src/vocabularies/quantity_kinds.ttl)<br/>- [Module vocabularies/&lowbar;shape](https://github.com/Accord-Project/aec3po/blob/main/src/vocabularies/_shape.ttl)|

#### Criterion detail
|Identifier|[profile-compatibility](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#profile-compatibility)|
|----|----|
|Title|Profile compatibility test|
|Description|A test meant to check whether the test subject is compatible with a profile or not, and if it is not, why.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-135)|Identifier|`owl-el-profile-error`|
|[Section top](#minorfail-outcome-number-135)|Title|OWL EL Profile incompatible|
|[Section top](#minorfail-outcome-number-135)|Description|Class Expression not supported with rdfs:subClassOf|
|[Section top](#minorfail-outcome-number-135)|Pointer|<pre lang="Turtle"><code>aec3po:AndCheckStatement a owl:Class ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;And Check Statement&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:comment &#34;Check verified if and only if all of its sub-checks are veri...&#34; ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy aec3po:statement ;  &#10;&#32;&#32;&#32;&#32;rdfs:subClassOf &#91; a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:onProperty aec3po:hasSubdivision ],  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;aec3po:ChecklistStatement .</code></pre>|
|[Section top](#minorfail-outcome-number-135)|Pointer|<pre lang="Turtle"><code>aec3po:ComplianceVerificationReport a owl:Class ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;Compliance Verification Report&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:comment &#34;Result of a checking act. May be compliant or not.&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy aec3po:compliance&lowbar;verification&lowbar;report ;  &#10;&#32;&#32;&#32;&#32;rdfs:subClassOf &#91; a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:onProperty aec3po:conforms ] .</code></pre>|
|[Section top](#minorfail-outcome-number-135)|Pointer|<pre lang="Turtle"><code>aec3po:DocumentSubdivision a owl:Class ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;Document Subdivision&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:comment &#34;Any subdivision of a document, including sections, paragraph...&#34; ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy aec3po:document ;  &#10;&#32;&#32;&#32;&#32;rdfs:subClassOf &#91; a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:allValuesFrom aec3po:DocumentSubdivision ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:onProperty aec3po:hasSubdivision ] ;  &#10;&#32;&#32;&#32;&#32;skos:example &#34;Paragraph, section, definition...&#34;@en .</code></pre>|
|[Section top](#minorfail-outcome-number-135)|Pointer|<pre lang="Turtle"><code>aec3po:LegalVerifier a owl:Class ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;Legal Verifier&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:comment &#34;An entity that has the legal capacity to verify compliance w...&#34; ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy aec3po:legal&lowbar;verifier ;  &#10;&#32;&#32;&#32;&#32;rdfs:subClassOf &#91; owl:allValuesFrom aec3po:Document ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:onProperty aec3po:forDocument ],  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;foaf:Agent .</code></pre>|
|[Section top](#minorfail-outcome-number-135)|Pointer|<pre lang="Turtle"><code>aec3po:NotCheckStatement a owl:Class ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;Not Check Statement&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:comment &#34;Check verified if and only if the sub-check is not verified.&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy aec3po:statement ;  &#10;&#32;&#32;&#32;&#32;rdfs:subClassOf &#91; a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:onProperty aec3po:hasSubdivision ] .</code></pre>|
|[Section top](#minorfail-outcome-number-135)|Pointer|<pre lang="Turtle"><code>aec3po:OrCheckStatement a owl:Class ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;Or Check Statement&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:comment &#34;Check verified if and only if at least one of its sub-checks...&#34; ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy aec3po:statement ;  &#10;&#32;&#32;&#32;&#32;rdfs:subClassOf &#91; a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:onProperty aec3po:hasSubdivision ],  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;aec3po:ChecklistStatement .</code></pre>|
|[Section top](#minorfail-outcome-number-135)|Pointer|<pre lang="Turtle"><code>aec3po:VerificationResult a owl:Class ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;Verification Result&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:comment &#34;Individual verification result of a Compliance Verification ...&#34; ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy aec3po:compliance&lowbar;verification&lowbar;report ;  &#10;&#32;&#32;&#32;&#32;rdfs:subClassOf &#91; a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:onProperty aec3po:verificationFocus ],  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#91; a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:onProperty aec3po:hasSeverity ] .</code></pre>|

***
### MinorFail Outcome number 136

[Jump to summary definition](#summary-MinorFail-136)	|	[Previous MinorFail outcome](#minorfail-outcome-number-135)	|	[Next MinorFail outcome](#minorfail-outcome-number-137)

:exclamation:MinorFail outcome
#### Subject detail
|Name|all-modules|
|----|----|
|Title|All the modules from branch main that are syntaxically correct as well as their recursive imports|
|Composition|- [Module aec3po](https://github.com/Accord-Project/aec3po/blob/main/src/aec3po.ttl)<br/>- [Module checking&lowbar;act](https://github.com/Accord-Project/aec3po/blob/main/src/checking_act.ttl)<br/>- [Module check&lowbar;method](https://github.com/Accord-Project/aec3po/blob/main/src/check_method.ttl)<br/>- [Module compliance&lowbar;verification&lowbar;report](https://github.com/Accord-Project/aec3po/blob/main/src/compliance_verification_report.ttl)<br/>- [Module data&lowbar;requirement](https://github.com/Accord-Project/aec3po/blob/main/src/data_requirement.ttl)<br/>- [Module document](https://github.com/Accord-Project/aec3po/blob/main/src/document.ttl)<br/>- [Module evidence](https://github.com/Accord-Project/aec3po/blob/main/src/evidence.ttl)<br/>- [Module feature&lowbar;of&lowbar;interest](https://github.com/Accord-Project/aec3po/blob/main/src/feature_of_interest.ttl)<br/>- [Module legal&lowbar;verifier](https://github.com/Accord-Project/aec3po/blob/main/src/legal_verifier.ttl)<br/>- [Module model](https://github.com/Accord-Project/aec3po/blob/main/src/model.ttl)<br/>- [Module rase&lowbar;statement](https://github.com/Accord-Project/aec3po/blob/main/src/rase_statement.ttl)<br/>- [Module statement](https://github.com/Accord-Project/aec3po/blob/main/src/statement.ttl)<br/>- [Module table](https://github.com/Accord-Project/aec3po/blob/main/src/table.ttl)<br/>- [Module vocabularies/administrative&lowbar;areas](https://github.com/Accord-Project/aec3po/blob/main/src/vocabularies/administrative_areas.ttl)<br/>- [Module vocabularies/building&lowbar;structure](https://github.com/Accord-Project/aec3po/blob/main/src/vocabularies/building_structure.ttl)<br/>- [Module vocabularies/building&lowbar;usage](https://github.com/Accord-Project/aec3po/blob/main/src/vocabularies/building_usage.ttl)<br/>- [Module vocabularies/check&lowbar;method&lowbar;comparators](https://github.com/Accord-Project/aec3po/blob/main/src/vocabularies/check_method_comparators.ttl)<br/>- [Module vocabularies/check&lowbar;method&lowbar;operators](https://github.com/Accord-Project/aec3po/blob/main/src/vocabularies/check_method_operators.ttl)<br/>- [Module vocabularies/disciplines](https://github.com/Accord-Project/aec3po/blob/main/src/vocabularies/disciplines.ttl)<br/>- [Module vocabularies/permitting&lowbar;stages](https://github.com/Accord-Project/aec3po/blob/main/src/vocabularies/permitting_stages.ttl)<br/>- [Module vocabularies/quantity&lowbar;kinds](https://github.com/Accord-Project/aec3po/blob/main/src/vocabularies/quantity_kinds.ttl)<br/>- [Module vocabularies/&lowbar;shape](https://github.com/Accord-Project/aec3po/blob/main/src/vocabularies/_shape.ttl)|

#### Criterion detail
|Identifier|[profile-compatibility](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#profile-compatibility)|
|----|----|
|Title|Profile compatibility test|
|Description|A test meant to check whether the test subject is compatible with a profile or not, and if it is not, why.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-136)|Identifier|`owl-el-profile-error`|
|[Section top](#minorfail-outcome-number-136)|Title|OWL EL Profile incompatible|
|[Section top](#minorfail-outcome-number-136)|Description|Restriction on datatypes|
|[Section top](#minorfail-outcome-number-136)|Pointer|<pre lang="Turtle"><code>aec3po:conforms a owl:DatatypeProperty ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;conforms&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:comment &#34;True if the Checking act confirms the check was validated, a...&#34; ;  &#10;&#32;&#32;&#32;&#32;rdfs:domain aec3po:ComplianceVerificationReport ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy aec3po:compliance&lowbar;verification&lowbar;report ;  &#10;&#32;&#32;&#32;&#32;rdfs:range xsd:boolean .</code></pre>|
|[Section top](#minorfail-outcome-number-136)|Pointer|<pre lang="Turtle"><code>aec3po:hasBooleanTarget a owl:DatatypeProperty ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;hasBooleanTarget&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:comment &#34;TBD&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:range xsd:boolean .</code></pre>|

***
### MinorFail Outcome number 137

[Jump to summary definition](#summary-MinorFail-137)	|	[Previous MinorFail outcome](#minorfail-outcome-number-136)	|	[Next MinorFail outcome](#minorfail-outcome-number-138)

:exclamation:MinorFail outcome
#### Subject detail
|Name|all-modules|
|----|----|
|Title|All the modules from branch main that are syntaxically correct as well as their recursive imports|
|Composition|- [Module aec3po](https://github.com/Accord-Project/aec3po/blob/main/src/aec3po.ttl)<br/>- [Module checking&lowbar;act](https://github.com/Accord-Project/aec3po/blob/main/src/checking_act.ttl)<br/>- [Module check&lowbar;method](https://github.com/Accord-Project/aec3po/blob/main/src/check_method.ttl)<br/>- [Module compliance&lowbar;verification&lowbar;report](https://github.com/Accord-Project/aec3po/blob/main/src/compliance_verification_report.ttl)<br/>- [Module data&lowbar;requirement](https://github.com/Accord-Project/aec3po/blob/main/src/data_requirement.ttl)<br/>- [Module document](https://github.com/Accord-Project/aec3po/blob/main/src/document.ttl)<br/>- [Module evidence](https://github.com/Accord-Project/aec3po/blob/main/src/evidence.ttl)<br/>- [Module feature&lowbar;of&lowbar;interest](https://github.com/Accord-Project/aec3po/blob/main/src/feature_of_interest.ttl)<br/>- [Module legal&lowbar;verifier](https://github.com/Accord-Project/aec3po/blob/main/src/legal_verifier.ttl)<br/>- [Module model](https://github.com/Accord-Project/aec3po/blob/main/src/model.ttl)<br/>- [Module rase&lowbar;statement](https://github.com/Accord-Project/aec3po/blob/main/src/rase_statement.ttl)<br/>- [Module statement](https://github.com/Accord-Project/aec3po/blob/main/src/statement.ttl)<br/>- [Module table](https://github.com/Accord-Project/aec3po/blob/main/src/table.ttl)<br/>- [Module vocabularies/administrative&lowbar;areas](https://github.com/Accord-Project/aec3po/blob/main/src/vocabularies/administrative_areas.ttl)<br/>- [Module vocabularies/building&lowbar;structure](https://github.com/Accord-Project/aec3po/blob/main/src/vocabularies/building_structure.ttl)<br/>- [Module vocabularies/building&lowbar;usage](https://github.com/Accord-Project/aec3po/blob/main/src/vocabularies/building_usage.ttl)<br/>- [Module vocabularies/check&lowbar;method&lowbar;comparators](https://github.com/Accord-Project/aec3po/blob/main/src/vocabularies/check_method_comparators.ttl)<br/>- [Module vocabularies/check&lowbar;method&lowbar;operators](https://github.com/Accord-Project/aec3po/blob/main/src/vocabularies/check_method_operators.ttl)<br/>- [Module vocabularies/disciplines](https://github.com/Accord-Project/aec3po/blob/main/src/vocabularies/disciplines.ttl)<br/>- [Module vocabularies/permitting&lowbar;stages](https://github.com/Accord-Project/aec3po/blob/main/src/vocabularies/permitting_stages.ttl)<br/>- [Module vocabularies/quantity&lowbar;kinds](https://github.com/Accord-Project/aec3po/blob/main/src/vocabularies/quantity_kinds.ttl)<br/>- [Module vocabularies/&lowbar;shape](https://github.com/Accord-Project/aec3po/blob/main/src/vocabularies/_shape.ttl)|

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
|[Section top](#minorfail-outcome-number-137)|Description|Class Expression not supported with owl:equivalentClass|
|[Section top](#minorfail-outcome-number-137)|Pointer|<pre lang="Turtle"><code>aec3po:ComponentCheckMethod a owl:Class ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;Component Check Method&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:comment &#34;Component check method refers to a process of inspecting and...&#34; ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy aec3po:check&lowbar;method ;  &#10;&#32;&#32;&#32;&#32;rdfs:subClassOf aec3po:CheckMethod ;  &#10;&#32;&#32;&#32;&#32;owl:equivalentClass &#91; a owl:Class ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:intersectionOf ( aec3po:CheckMethod &#91; a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:allValuesFrom &#91; a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:allValuesFrom aec3po:FeatureOfInterest ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:onProperty &#91; owl:inverseOf aec3po:forDesign ] ] ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:onProperty aec3po:forDesign ] ) ] .</code></pre>|

***
### MinorFail Outcome number 138

[Jump to summary definition](#summary-MinorFail-138)	|	[Previous MinorFail outcome](#minorfail-outcome-number-137)	|	[Next MinorFail outcome](#minorfail-outcome-number-139)

:exclamation:MinorFail outcome
#### Subject detail
|Name|all-modules|
|----|----|
|Title|All the modules from branch main that are syntaxically correct as well as their recursive imports|
|Composition|- [Module aec3po](https://github.com/Accord-Project/aec3po/blob/main/src/aec3po.ttl)<br/>- [Module checking&lowbar;act](https://github.com/Accord-Project/aec3po/blob/main/src/checking_act.ttl)<br/>- [Module check&lowbar;method](https://github.com/Accord-Project/aec3po/blob/main/src/check_method.ttl)<br/>- [Module compliance&lowbar;verification&lowbar;report](https://github.com/Accord-Project/aec3po/blob/main/src/compliance_verification_report.ttl)<br/>- [Module data&lowbar;requirement](https://github.com/Accord-Project/aec3po/blob/main/src/data_requirement.ttl)<br/>- [Module document](https://github.com/Accord-Project/aec3po/blob/main/src/document.ttl)<br/>- [Module evidence](https://github.com/Accord-Project/aec3po/blob/main/src/evidence.ttl)<br/>- [Module feature&lowbar;of&lowbar;interest](https://github.com/Accord-Project/aec3po/blob/main/src/feature_of_interest.ttl)<br/>- [Module legal&lowbar;verifier](https://github.com/Accord-Project/aec3po/blob/main/src/legal_verifier.ttl)<br/>- [Module model](https://github.com/Accord-Project/aec3po/blob/main/src/model.ttl)<br/>- [Module rase&lowbar;statement](https://github.com/Accord-Project/aec3po/blob/main/src/rase_statement.ttl)<br/>- [Module statement](https://github.com/Accord-Project/aec3po/blob/main/src/statement.ttl)<br/>- [Module table](https://github.com/Accord-Project/aec3po/blob/main/src/table.ttl)<br/>- [Module vocabularies/administrative&lowbar;areas](https://github.com/Accord-Project/aec3po/blob/main/src/vocabularies/administrative_areas.ttl)<br/>- [Module vocabularies/building&lowbar;structure](https://github.com/Accord-Project/aec3po/blob/main/src/vocabularies/building_structure.ttl)<br/>- [Module vocabularies/building&lowbar;usage](https://github.com/Accord-Project/aec3po/blob/main/src/vocabularies/building_usage.ttl)<br/>- [Module vocabularies/check&lowbar;method&lowbar;comparators](https://github.com/Accord-Project/aec3po/blob/main/src/vocabularies/check_method_comparators.ttl)<br/>- [Module vocabularies/check&lowbar;method&lowbar;operators](https://github.com/Accord-Project/aec3po/blob/main/src/vocabularies/check_method_operators.ttl)<br/>- [Module vocabularies/disciplines](https://github.com/Accord-Project/aec3po/blob/main/src/vocabularies/disciplines.ttl)<br/>- [Module vocabularies/permitting&lowbar;stages](https://github.com/Accord-Project/aec3po/blob/main/src/vocabularies/permitting_stages.ttl)<br/>- [Module vocabularies/quantity&lowbar;kinds](https://github.com/Accord-Project/aec3po/blob/main/src/vocabularies/quantity_kinds.ttl)<br/>- [Module vocabularies/&lowbar;shape](https://github.com/Accord-Project/aec3po/blob/main/src/vocabularies/_shape.ttl)|

#### Criterion detail
|Identifier|[term-referencing](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#term-referencing)|
|----|----|
|Title|Term referencing test|
|Description|A test case from the Best Practices tests checking if each term of the test subject is referenced to a module through a rdfs:isDefinedBy property.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-138)|Identifier|`no-reference-module`|
|[Section top](#minorfail-outcome-number-138)|Title|Term not referenced to a module|
|[Section top](#minorfail-outcome-number-138)|Description|Subject terms not linked to a module by a rdfs:isDefinedBy property|
|[Section top](#minorfail-outcome-number-138)|Pointer|<pre lang="Turtle"><code>:edlira a schema:Person ;  &#10;&#32;&#32;&#32;&#32;schema:affiliation &#60;https://www.bcu.ac.uk/> ;  &#10;&#32;&#32;&#32;&#32;schema:email &#34;edlira.vakaj@bcu.ac.uk&#34; ;  &#10;&#32;&#32;&#32;&#32;schema:identifier &#60;http://orcid.org/0000-0002-0712-0959> ;  &#10;&#32;&#32;&#32;&#32;schema:name &#34;Edlira Vakaj&#34; ;  &#10;&#32;&#32;&#32;&#32;schema:url &#60;https://www.bcu.ac.uk/computing/about-us/our-staff/edlira-vakaj> .</code></pre>|
|[Section top](#minorfail-outcome-number-138)|Pointer|<pre lang="Turtle"><code>:pan a schema:Person ;  &#10;&#32;&#32;&#32;&#32;schema:affiliation &#60;https://www.bcu.ac.uk/> ;  &#10;&#32;&#32;&#32;&#32;schema:email &#34;Panagiotis.Patlakas@bcu.ac.uk&#34; ;  &#10;&#32;&#32;&#32;&#32;schema:identifier &#60;http://orcid.org/0000-0002-7248-8952> ;  &#10;&#32;&#32;&#32;&#32;schema:name &#34;Panagiotis Patlakas&#34; ;  &#10;&#32;&#32;&#32;&#32;schema:url &#60;https://www.bcu.ac.uk/built-environment/about-us/our-staff/panagiotis-patlakas> .</code></pre>|
|[Section top](#minorfail-outcome-number-138)|Pointer|<pre lang="Turtle"><code>:amna a schema:Person ;  &#10;&#32;&#32;&#32;&#32;schema:affiliation &#60;https://www.bcu.ac.uk/> ;  &#10;&#32;&#32;&#32;&#32;schema:email &#34;Amna.Dridi@bcu.ac.uk&#34; ;  &#10;&#32;&#32;&#32;&#32;schema:identifier &#60;http://orcid.org/0000-0002-0185-103X> ;  &#10;&#32;&#32;&#32;&#32;schema:name &#34;Amna Dridi&#34; ;  &#10;&#32;&#32;&#32;&#32;schema:url &#60;https://www.researchgate.net/profile/Amna-Dridi-3> .</code></pre>|
|[Section top](#minorfail-outcome-number-138)|Pointer|<pre lang="Turtle"><code>:thomas a schema:Person ;  &#10;&#32;&#32;&#32;&#32;schema:affiliation &#60;https://www.cardiff.ac.uk/> ;  &#10;&#32;&#32;&#32;&#32;schema:email &#34;beachth@cardiff.ac.uk&#34; ;  &#10;&#32;&#32;&#32;&#32;schema:identifier &#60;http://orcid.org/0000-0001-5610-8027> ;  &#10;&#32;&#32;&#32;&#32;schema:name &#34;Thomas Beach&#34; ;  &#10;&#32;&#32;&#32;&#32;schema:url &#60;https://profiles.cardiff.ac.uk/staff/beachth> .</code></pre>|
|[Section top](#minorfail-outcome-number-138)|Pointer|<pre lang="Turtle"><code>:vladimir a schema:Person ;  &#10;&#32;&#32;&#32;&#32;schema:affiliation &#60;https://www.ontotext.com/> ;  &#10;&#32;&#32;&#32;&#32;schema:email &#34;vladimir.alexiev@ontotext.com&#34; ;  &#10;&#32;&#32;&#32;&#32;schema:identifier &#60;https://orcid.org/0000-0001-7508-7428> ;  &#10;&#32;&#32;&#32;&#32;schema:name &#34;Vladimir Alexiev&#34; ;  &#10;&#32;&#32;&#32;&#32;schema:url &#60;https://www.ontotext.com/blog/author/vladimir/> .</code></pre>|
|[Section top](#minorfail-outcome-number-138)|Pointer|<pre lang="Turtle"><code>:hasTarget a owl:DatatypeProperty ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;hasTarget&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:comment &#34;TBD&#34;@en .</code></pre>|
|[Section top](#minorfail-outcome-number-138)|Pointer|<pre lang="Turtle"><code>:hasBooleanTarget a owl:DatatypeProperty ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;hasBooleanTarget&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:comment &#34;TBD&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:range xsd:boolean .</code></pre>|
|[Section top](#minorfail-outcome-number-138)|Pointer|<pre lang="Turtle"><code>:name a owl:DatatypeProperty ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;name&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:comment &#34;The name or the identifier of the BIM model.&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:domain &#60;https://schema.org/Model> ;  &#10;&#32;&#32;&#32;&#32;rdfs:range xsd:string ;  &#10;&#32;&#32;&#32;&#32;owl:equivalentProperty &#60;https://schema.org/about> ;  &#10;&#32;&#32;&#32;&#32;owl:inverseOf &#60;https://schema.org/subjectOf> .</code></pre>|
|[Section top](#minorfail-outcome-number-138)|Pointer|<pre lang="Turtle"><code>:description a owl:DatatypeProperty ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;description&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:comment &#34;A textual description providing additional details about the...&#34; ;  &#10;&#32;&#32;&#32;&#32;rdfs:domain &#60;https://schema.org/Model> ;  &#10;&#32;&#32;&#32;&#32;rdfs:range xsd:string ;  &#10;&#32;&#32;&#32;&#32;owl:equivalentProperty &#60;https://schema.org/abstract> .</code></pre>|
|[Section top](#minorfail-outcome-number-138)|Pointer|<pre lang="Turtle"><code>:location a owl:ObjectProperty ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;location&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:comment &#34;The physical or geographic location of the building or struc...&#34; ;  &#10;&#32;&#32;&#32;&#32;rdfs:domain &#60;https://schema.org/Model> ;  &#10;&#32;&#32;&#32;&#32;rdfs:range &#60;https://schema.org/Place> ;  &#10;&#32;&#32;&#32;&#32;owl:equivalentProperty &#60;https://schema.org/spatial> .</code></pre>|
|[Section top](#minorfail-outcome-number-138)|Pointer|<pre lang="Turtle"><code>:locationCoverage a owl:ObjectProperty ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;location coverage&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:comment &#34;The spatialCoverage indicates the place(s) or the administra...&#34; ;  &#10;&#32;&#32;&#32;&#32;rdfs:domain &#60;https://schema.org/Model> ;  &#10;&#32;&#32;&#32;&#32;rdfs:range &#91; a owl:Class ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:unionOf ( &#60;https://schema.org/Place> :AdministrativeArea ) ] ;  &#10;&#32;&#32;&#32;&#32;owl:equivalentProperty &#60;https://schema.org/spatialCoverage> .</code></pre>|
|[Section top](#minorfail-outcome-number-138)|Pointer|<pre lang="Turtle"><code>:material a owl:DatatypeProperty ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;material&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:comment &#34;The materials used for different parts of the building, such...&#34; ;  &#10;&#32;&#32;&#32;&#32;rdfs:domain &#60;https://schema.org/Model> ;  &#10;&#32;&#32;&#32;&#32;rdfs:range xsd:string ;  &#10;&#32;&#32;&#32;&#32;owl:equivalentProperty &#60;https://schema.org/material> .</code></pre>|
|[Section top](#minorfail-outcome-number-138)|Pointer|<pre lang="Turtle"><code>:hasBuildingPhase a owl:ObjectProperty ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;has building phase&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:comment &#34;describes the relationship between a construction-related en...&#34; ;  &#10;&#32;&#32;&#32;&#32;rdfs:domain :Model ;  &#10;&#32;&#32;&#32;&#32;rdfs:range :Phase .</code></pre>|
|[Section top](#minorfail-outcome-number-138)|Pointer|<pre lang="Turtle"><code>:hasElementPhase a owl:ObjectProperty ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;has element phase&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:comment &#34;is used to establish a relationship between a construction e...&#34; ;  &#10;&#32;&#32;&#32;&#32;rdfs:domain :Model ;  &#10;&#32;&#32;&#32;&#32;rdfs:range :Phase .</code></pre>|
|[Section top](#minorfail-outcome-number-138)|Pointer|<pre lang="Turtle"><code>:hasDimension a owl:ObjectProperty ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;has dimension&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:comment &#34;is used to represent the physical dimensions or measurements...&#34; ;  &#10;&#32;&#32;&#32;&#32;rdfs:domain :Model ;  &#10;&#32;&#32;&#32;&#32;rdfs:range :Dimension .</code></pre>|
|[Section top](#minorfail-outcome-number-138)|Pointer|<pre lang="Turtle"><code>:hasClassification a owl:ObjectProperty ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;has dimension&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:comment &#34;is used to link building components, elements, or other enti...&#34; ;  &#10;&#32;&#32;&#32;&#32;rdfs:domain :Model ;  &#10;&#32;&#32;&#32;&#32;rdfs:range :Classification .</code></pre>|

***
### MinorFail Outcome number 139

[Jump to summary definition](#summary-MinorFail-139)	|	[Previous MinorFail outcome](#minorfail-outcome-number-138)	|	[Next MinorFail outcome](#minorfail-outcome-number-140)

:exclamation:MinorFail outcome
#### Subject detail
|Name|all-modules|
|----|----|
|Title|All the modules from branch main that are syntaxically correct as well as their recursive imports|
|Composition|- [Module aec3po](https://github.com/Accord-Project/aec3po/blob/main/src/aec3po.ttl)<br/>- [Module checking&lowbar;act](https://github.com/Accord-Project/aec3po/blob/main/src/checking_act.ttl)<br/>- [Module check&lowbar;method](https://github.com/Accord-Project/aec3po/blob/main/src/check_method.ttl)<br/>- [Module compliance&lowbar;verification&lowbar;report](https://github.com/Accord-Project/aec3po/blob/main/src/compliance_verification_report.ttl)<br/>- [Module data&lowbar;requirement](https://github.com/Accord-Project/aec3po/blob/main/src/data_requirement.ttl)<br/>- [Module document](https://github.com/Accord-Project/aec3po/blob/main/src/document.ttl)<br/>- [Module evidence](https://github.com/Accord-Project/aec3po/blob/main/src/evidence.ttl)<br/>- [Module feature&lowbar;of&lowbar;interest](https://github.com/Accord-Project/aec3po/blob/main/src/feature_of_interest.ttl)<br/>- [Module legal&lowbar;verifier](https://github.com/Accord-Project/aec3po/blob/main/src/legal_verifier.ttl)<br/>- [Module model](https://github.com/Accord-Project/aec3po/blob/main/src/model.ttl)<br/>- [Module rase&lowbar;statement](https://github.com/Accord-Project/aec3po/blob/main/src/rase_statement.ttl)<br/>- [Module statement](https://github.com/Accord-Project/aec3po/blob/main/src/statement.ttl)<br/>- [Module table](https://github.com/Accord-Project/aec3po/blob/main/src/table.ttl)<br/>- [Module vocabularies/administrative&lowbar;areas](https://github.com/Accord-Project/aec3po/blob/main/src/vocabularies/administrative_areas.ttl)<br/>- [Module vocabularies/building&lowbar;structure](https://github.com/Accord-Project/aec3po/blob/main/src/vocabularies/building_structure.ttl)<br/>- [Module vocabularies/building&lowbar;usage](https://github.com/Accord-Project/aec3po/blob/main/src/vocabularies/building_usage.ttl)<br/>- [Module vocabularies/check&lowbar;method&lowbar;comparators](https://github.com/Accord-Project/aec3po/blob/main/src/vocabularies/check_method_comparators.ttl)<br/>- [Module vocabularies/check&lowbar;method&lowbar;operators](https://github.com/Accord-Project/aec3po/blob/main/src/vocabularies/check_method_operators.ttl)<br/>- [Module vocabularies/disciplines](https://github.com/Accord-Project/aec3po/blob/main/src/vocabularies/disciplines.ttl)<br/>- [Module vocabularies/permitting&lowbar;stages](https://github.com/Accord-Project/aec3po/blob/main/src/vocabularies/permitting_stages.ttl)<br/>- [Module vocabularies/quantity&lowbar;kinds](https://github.com/Accord-Project/aec3po/blob/main/src/vocabularies/quantity_kinds.ttl)<br/>- [Module vocabularies/&lowbar;shape](https://github.com/Accord-Project/aec3po/blob/main/src/vocabularies/_shape.ttl)|

#### Criterion detail
|Identifier|[terms-differenciation](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#terms-differenciation)|
|----|----|
|Title|Terms differenciation test|
|Description|A test case from the Best Practices tests checking if all the terms are different enough from each other according to the Levenshtein distance metric.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-139)|Identifier|`too-close-terms`|
|[Section top](#minorfail-outcome-number-139)|Title|Too close terms|
|[Section top](#minorfail-outcome-number-139)|Description|Some terms are too similar|
|[Section top](#minorfail-outcome-number-139)|Pointer|<pre lang="Turtle"><code>:CheckMethodComparator-gt a owl:NamedIndividual,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;skos:Concept,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;:CheckMethodComparator ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy :check&lowbar;method&lowbar;comparators ;  &#10;&#32;&#32;&#32;&#32;skos:definition &#34;greater-than comparator.&#34;@en ;  &#10;&#32;&#32;&#32;&#32;skos:inScheme :CheckMethodComparatorNomenclature ;  &#10;&#32;&#32;&#32;&#32;skos:prefLabel &#34;greater than&#34;@en ;  &#10;&#32;&#32;&#32;&#32;skos:topConceptOf :CheckMethodComparatorNomenclature .</code></pre>|
|[Section top](#minorfail-outcome-number-139)|Pointer|<pre lang="Turtle"><code>:CheckMethodComparator-ge a owl:NamedIndividual,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;skos:Concept,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;:CheckMethodComparator ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy :check&lowbar;method&lowbar;comparators ;  &#10;&#32;&#32;&#32;&#32;skos:definition &#34;greater-equal comparator.&#34;@en ;  &#10;&#32;&#32;&#32;&#32;skos:inScheme :CheckMethodComparatorNomenclature ;  &#10;&#32;&#32;&#32;&#32;skos:prefLabel &#34;greater equal&#34;@en ;  &#10;&#32;&#32;&#32;&#32;skos:topConceptOf :CheckMethodComparatorNomenclature .</code></pre>|
|[Section top](#minorfail-outcome-number-139)|Pointer|<pre lang="Turtle"><code>:CheckMethodComparator-le a owl:NamedIndividual,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;skos:Concept,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;:CheckMethodComparator ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy :check&lowbar;method&lowbar;comparators ;  &#10;&#32;&#32;&#32;&#32;skos:definition &#34;less-equal comparator.&#34;@en ;  &#10;&#32;&#32;&#32;&#32;skos:inScheme :CheckMethodComparatorNomenclature ;  &#10;&#32;&#32;&#32;&#32;skos:prefLabel &#34;less equal&#34;@en ;  &#10;&#32;&#32;&#32;&#32;skos:topConceptOf :CheckMethodComparatorNomenclature .</code></pre>|
|[Section top](#minorfail-outcome-number-139)|Pointer|<pre lang="Turtle"><code>:CheckMethodComparator-lt a owl:NamedIndividual,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;skos:Concept,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;:CheckMethodComparator ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy :check&lowbar;method&lowbar;comparators ;  &#10;&#32;&#32;&#32;&#32;skos:definition &#34;less-than comparator.&#34;@en ;  &#10;&#32;&#32;&#32;&#32;skos:inScheme :CheckMethodComparatorNomenclature ;  &#10;&#32;&#32;&#32;&#32;skos:prefLabel &#34;less than&#34;@en ;  &#10;&#32;&#32;&#32;&#32;skos:topConceptOf :CheckMethodComparatorNomenclature .</code></pre>|
|[Section top](#minorfail-outcome-number-139)|Pointer|<pre lang="Turtle"><code>:CheckMethodComparator-neq a owl:NamedIndividual,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;skos:Concept,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;:CheckMethodComparator ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy :check&lowbar;method&lowbar;comparators ;  &#10;&#32;&#32;&#32;&#32;skos:definition &#34;not equal-to comparator.&#34;@en ;  &#10;&#32;&#32;&#32;&#32;skos:inScheme :CheckMethodComparatorNomenclature ;  &#10;&#32;&#32;&#32;&#32;skos:prefLabel &#34;not equal-to&#34;@en ;  &#10;&#32;&#32;&#32;&#32;skos:topConceptOf :CheckMethodComparatorNomenclature .</code></pre>|
|[Section top](#minorfail-outcome-number-139)|Pointer|<pre lang="Turtle"><code>:CheckMethodcomparator-eq a owl:NamedIndividual,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;skos:Concept,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;:CheckMethodcomparator ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy :check&lowbar;method&lowbar;comparators ;  &#10;&#32;&#32;&#32;&#32;skos:definition &#34;equal-to comparator.&#34;@en ;  &#10;&#32;&#32;&#32;&#32;skos:inScheme :CheckMethodComparatorNomenclature ;  &#10;&#32;&#32;&#32;&#32;skos:prefLabel &#34;equal-to&#34;@en ;  &#10;&#32;&#32;&#32;&#32;skos:topConceptOf :CheckMethodComparatorNomenclature .</code></pre>|
|[Section top](#minorfail-outcome-number-139)|Pointer|<pre lang="Turtle"><code>:OrCheckStatement a owl:Class ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;Or Check Statement&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:comment &#34;Check verified if and only if at least one of its sub-checks...&#34; ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy :statement ;  &#10;&#32;&#32;&#32;&#32;rdfs:subClassOf &#91; a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:onProperty :hasSubdivision ],  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;:ChecklistStatement .</code></pre>|
|[Section top](#minorfail-outcome-number-139)|Pointer|<pre lang="Turtle"><code>:CheckStatement a owl:Class ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;Check Statement&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:comment &#34;refers to a type of statement that is used to specify condit...&#34; ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy :statement ;  &#10;&#32;&#32;&#32;&#32;rdfs:subClassOf :Statement .</code></pre>|
|[Section top](#minorfail-outcome-number-139)|Pointer|<pre lang="Turtle"><code>:PartialSafetyFactor0 a owl:NamedIndividual,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;skos:Concept,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;:QuantityKind ;  &#10;&#32;&#32;&#32;&#32;qudt:applicableUnit &#60;http://qudt.org/vocab/unit/UNITLESS> ;  &#10;&#32;&#32;&#32;&#32;qudt:hasDimensionVector &#60;http://qudt.org/vocab/dimensionvector/A0E0L0I0M0H0T0D0> ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy :quantity&lowbar;kinds ;  &#10;&#32;&#32;&#32;&#32;skos:broader :PartialSafetyFactor ;  &#10;&#32;&#32;&#32;&#32;skos:definition &#34;Also written γM0, the partial safety factor for resistance r...&#34; ;  &#10;&#32;&#32;&#32;&#32;skos:prefLabel &#34;Partial Safety Factor&#34;@en .</code></pre>|
|[Section top](#minorfail-outcome-number-139)|Pointer|<pre lang="Turtle"><code>:PartialSafetyFactor a owl:NamedIndividual,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;skos:Concept,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;:QuantityKind ;  &#10;&#32;&#32;&#32;&#32;qudt:applicableUnit &#60;http://qudt.org/vocab/unit/UNITLESS> ;  &#10;&#32;&#32;&#32;&#32;qudt:hasDimensionVector &#60;http://qudt.org/vocab/dimensionvector/A0E0L0I0M0H0T0D0> ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy :quantity&lowbar;kinds ;  &#10;&#32;&#32;&#32;&#32;skos:definition &#34;Also written γM, the partial safety factor for resistance.&#34;@en ;  &#10;&#32;&#32;&#32;&#32;skos:prefLabel &#34;Partial Safety Factor&#34;@en .</code></pre>|
|[Section top](#minorfail-outcome-number-139)|Pointer|<pre lang="Turtle"><code>:PartialSafetyFactor1 a owl:NamedIndividual,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;skos:Concept,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;:QuantityKind ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;Partial Safety Factor&#34;@en ;  &#10;&#32;&#32;&#32;&#32;qudt:applicableUnit &#60;http://qudt.org/vocab/unit/UNITLESS> ;  &#10;&#32;&#32;&#32;&#32;qudt:hasDimensionVector &#60;http://qudt.org/vocab/dimensionvector/A0E0L0I0M0H0T0D0> ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy :quantity&lowbar;kinds ;  &#10;&#32;&#32;&#32;&#32;skos:broader :PartialSafetyFactor ;  &#10;&#32;&#32;&#32;&#32;skos:definition &#34;Also written γM1, the partial safety factor for resistance r...&#34; .</code></pre>|
|[Section top](#minorfail-outcome-number-139)|Pointer|<pre lang="Turtle"><code>:QuantityKind a owl:Class ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;Quantity Kind&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:comment &#34;A Quantity Kind is any observable property that can be quant...&#34;,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#34;A kind of quantity.&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy :feature&lowbar;of&lowbar;interest,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;:quantity&lowbar;kinds ;  &#10;&#32;&#32;&#32;&#32;rdfs:subClassOf qudt:QuantityKind,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#60;http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#Region>,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;skos:Concept ;  &#10;&#32;&#32;&#32;&#32;owl:equivalentClass &#91; owl:intersectionOf ( skos:Concept &#91; a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:hasValue :QuantityKindNomenclature ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:onProperty skos:inScheme ] ) ] ;  &#10;&#32;&#32;&#32;&#32;skos:example &#34;Length, Area, U-Value.&#34;@en,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#34;height, area, U-value&#34;@en ;  &#10;&#32;&#32;&#32;&#32;skos:note &#34;Maxime Lefrançois argues that both qudt:QuantityKind and qud...&#34; .</code></pre>|
|[Section top](#minorfail-outcome-number-139)|Pointer|<pre lang="Turtle"><code>:severity a owl:ObjectProperty ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;severity&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:comment &#34;Each verification result has exactly one value for the prope...&#34; ;  &#10;&#32;&#32;&#32;&#32;rdfs:domain :VerificationResult ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy :compliance&lowbar;verification&lowbar;report ;  &#10;&#32;&#32;&#32;&#32;rdfs:range :Severity .</code></pre>|
|[Section top](#minorfail-outcome-number-139)|Pointer|<pre lang="Turtle"><code>:Severity a owl:Class ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;Severity&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:comment &#34;The class of validation result severity levels, including vi...&#34; ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy :compliance&lowbar;verification&lowbar;report .</code></pre>|

***
### MinorFail Outcome number 140

[Jump to summary definition](#summary-MinorFail-140)	|	[Previous MinorFail outcome](#minorfail-outcome-number-139)	|	[Next MinorFail outcome](#minorfail-outcome-number-141)

:exclamation:MinorFail outcome
#### Subject detail
|Name|all-fragments|
|----|----|
|Title|All the fragments from branch main that are syntaxically correct as well as their recursive imports|
|Composition|- [Module aec3po](https://github.com/Accord-Project/aec3po/blob/main/src/aec3po.ttl)<br/>- [Module checking&lowbar;act](https://github.com/Accord-Project/aec3po/blob/main/src/checking_act.ttl)<br/>- [Module check&lowbar;method](https://github.com/Accord-Project/aec3po/blob/main/src/check_method.ttl)<br/>- [Module compliance&lowbar;verification&lowbar;report](https://github.com/Accord-Project/aec3po/blob/main/src/compliance_verification_report.ttl)<br/>- [Module data&lowbar;requirement](https://github.com/Accord-Project/aec3po/blob/main/src/data_requirement.ttl)<br/>- [Module document](https://github.com/Accord-Project/aec3po/blob/main/src/document.ttl)<br/>- [Module evidence](https://github.com/Accord-Project/aec3po/blob/main/src/evidence.ttl)<br/>- [Module feature&lowbar;of&lowbar;interest](https://github.com/Accord-Project/aec3po/blob/main/src/feature_of_interest.ttl)<br/>- [Module legal&lowbar;verifier](https://github.com/Accord-Project/aec3po/blob/main/src/legal_verifier.ttl)<br/>- [Module model](https://github.com/Accord-Project/aec3po/blob/main/src/model.ttl)<br/>- [Module rase&lowbar;statement](https://github.com/Accord-Project/aec3po/blob/main/src/rase_statement.ttl)<br/>- [Module statement](https://github.com/Accord-Project/aec3po/blob/main/src/statement.ttl)<br/>- [Module table](https://github.com/Accord-Project/aec3po/blob/main/src/table.ttl)<br/>- [Module vocabularies/administrative&lowbar;areas](https://github.com/Accord-Project/aec3po/blob/main/src/vocabularies/administrative_areas.ttl)<br/>- [Module vocabularies/building&lowbar;structure](https://github.com/Accord-Project/aec3po/blob/main/src/vocabularies/building_structure.ttl)<br/>- [Module vocabularies/building&lowbar;usage](https://github.com/Accord-Project/aec3po/blob/main/src/vocabularies/building_usage.ttl)<br/>- [Module vocabularies/check&lowbar;method&lowbar;comparators](https://github.com/Accord-Project/aec3po/blob/main/src/vocabularies/check_method_comparators.ttl)<br/>- [Module vocabularies/check&lowbar;method&lowbar;operators](https://github.com/Accord-Project/aec3po/blob/main/src/vocabularies/check_method_operators.ttl)<br/>- [Module vocabularies/disciplines](https://github.com/Accord-Project/aec3po/blob/main/src/vocabularies/disciplines.ttl)<br/>- [Module vocabularies/permitting&lowbar;stages](https://github.com/Accord-Project/aec3po/blob/main/src/vocabularies/permitting_stages.ttl)<br/>- [Module vocabularies/quantity&lowbar;kinds](https://github.com/Accord-Project/aec3po/blob/main/src/vocabularies/quantity_kinds.ttl)<br/>- [Module vocabularies/&lowbar;shape](https://github.com/Accord-Project/aec3po/blob/main/src/vocabularies/_shape.ttl)|

#### Criterion detail
|Identifier|[domain-and-range-referencing](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#domain-and-range-referencing)|
|----|----|
|Title|Domain and range referencing test|
|Description|A test case from the Best Practices tests checking if all the ranges and domains from the test subject point to terms that are defined in the vocabulary.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-140)|Identifier|`domain-out-of-vocabulary`|
|[Section top](#minorfail-outcome-number-140)|Title|Domain out of vocabulary|
|[Section top](#minorfail-outcome-number-140)|Description|Some properties have a domain out of the ontology|
|[Section top](#minorfail-outcome-number-140)|Pointer|<pre lang="Turtle"><code>:usedMethod a owl:ObjectProperty ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;used method&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:comment &#34;Links a checking act to the method it used (a aec3po:CheckMe...&#34; ;  &#10;&#32;&#32;&#32;&#32;rdfs:domain &#91; a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:onProperty :usedMethod ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:someValuesFrom :CheckMethod ],  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#91; a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:onProperty :madeBy ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:someValuesFrom :ProcessVerifier ],  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#91; a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:onProperty :checked ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:someValuesFrom owl:Thing ],  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#91; a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:onProperty :hasReport ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:someValuesFrom :ComplianceVerificationReport ],  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#60;http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#Event>,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:Thing,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;:CheckingAct ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy :checking&lowbar;act ;  &#10;&#32;&#32;&#32;&#32;rdfs:range &lowbar;:n59f67d43de7741e68ffb0f540836c440b5,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#60;http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#Method>,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:Thing,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;:CheckMethod ;  &#10;&#32;&#32;&#32;&#32;rdfs:subPropertyOf :usedMethod ;  &#10;&#32;&#32;&#32;&#32;owl:equivalentProperty :usedMethod .  &#10;&lowbar;:n59f67d43de7741e68ffb0f540836c440b6 rdf:first :CheckMethod ;  &#10;&#32;&#32;&#32;&#32;rdf:rest () .  &#10;&lowbar;:n59f67d43de7741e68ffb0f540836c440b7 rdf:first :Property ;  &#10;&#32;&#32;&#32;&#32;rdf:rest &lowbar;:n59f67d43de7741e68ffb0f540836c440b6 .  &#10;&lowbar;:n59f67d43de7741e68ffb0f540836c440b8 rdf:first :FeatureOfInterest ;  &#10;&#32;&#32;&#32;&#32;rdf:rest &lowbar;:n59f67d43de7741e68ffb0f540836c440b7 .  &#10;&lowbar;:n59f67d43de7741e68ffb0f540836c440b5 a owl:Class ;  &#10;&#32;&#32;&#32;&#32;rdfs:subClassOf &lowbar;:n59f67d43de7741e68ffb0f540836c440b5,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:Thing ;  &#10;&#32;&#32;&#32;&#32;owl:equivalentClass &lowbar;:n59f67d43de7741e68ffb0f540836c440b5 ;  &#10;&#32;&#32;&#32;&#32;owl:unionOf &lowbar;:n59f67d43de7741e68ffb0f540836c440b8 .</code></pre>|
|[Section top](#minorfail-outcome-number-140)|Pointer|<pre lang="Turtle"><code></code></pre>|
|[Section top](#minorfail-outcome-number-140)|Pointer|<pre lang="Turtle"><code>:madeBy a owl:ObjectProperty ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;made by&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:comment &#34;Links a checking act to the process verifier that made it (a...&#34; ;  &#10;&#32;&#32;&#32;&#32;rdfs:domain &#91; a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:onProperty :usedMethod ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:someValuesFrom :CheckMethod ],  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#91; a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:onProperty :madeBy ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:someValuesFrom :ProcessVerifier ],  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#91; a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:onProperty :checked ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:someValuesFrom owl:Thing ],  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#91; a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:onProperty :hasReport ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:someValuesFrom :ComplianceVerificationReport ],  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#60;http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#Event>,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:Thing,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;:CheckingAct ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy :checking&lowbar;act ;  &#10;&#32;&#32;&#32;&#32;rdfs:range :ProcessVerifier ;  &#10;&#32;&#32;&#32;&#32;rdfs:subPropertyOf :madeBy ;  &#10;&#32;&#32;&#32;&#32;owl:equivalentProperty :madeBy .</code></pre>|
|[Section top](#minorfail-outcome-number-140)|Pointer|<pre lang="Turtle"><code>:checked a owl:ObjectProperty ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;checked&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:comment &#34;Links a checking act to some entity (ex. statement, feature ...&#34; ;  &#10;&#32;&#32;&#32;&#32;rdfs:domain &#91; a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:onProperty :usedMethod ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:someValuesFrom :CheckMethod ],  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#91; a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:onProperty :madeBy ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:someValuesFrom :ProcessVerifier ],  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#91; a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:onProperty :checked ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:someValuesFrom owl:Thing ],  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#91; a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:onProperty :hasReport ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:someValuesFrom :ComplianceVerificationReport ],  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#60;http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#Event>,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:Thing,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;:CheckingAct ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy :checking&lowbar;act ;  &#10;&#32;&#32;&#32;&#32;rdfs:subPropertyOf :checked ;  &#10;&#32;&#32;&#32;&#32;owl:equivalentProperty :checked .</code></pre>|
|[Section top](#minorfail-outcome-number-140)|Pointer|<pre lang="Turtle"><code>:hasReport a owl:ObjectProperty ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;has report&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:comment &#34;Links a checking act to the resulting compliance verificatio...&#34; ;  &#10;&#32;&#32;&#32;&#32;rdfs:domain &#91; a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:onProperty :usedMethod ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:someValuesFrom :CheckMethod ],  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#91; a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:onProperty :madeBy ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:someValuesFrom :ProcessVerifier ],  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#91; a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:onProperty :checked ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:someValuesFrom owl:Thing ],  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#91; a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:onProperty :hasReport ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:someValuesFrom :ComplianceVerificationReport ],  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#60;http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#Event>,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:Thing,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;:CheckingAct ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy :checking&lowbar;act ;  &#10;&#32;&#32;&#32;&#32;rdfs:range &#91; a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:onProperty :conforms ],  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:Thing,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;:ComplianceVerificationReport ;  &#10;&#32;&#32;&#32;&#32;rdfs:subPropertyOf :hasReport ;  &#10;&#32;&#32;&#32;&#32;owl:equivalentProperty :hasReport .</code></pre>|
|[Section top](#minorfail-outcome-number-140)|Pointer|<pre lang="Turtle"><code>:operationalizes a owl:ObjectProperty ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;operationalizes&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:comment &#34;Links a check method to a check statement in a document that...&#34; ;  &#10;&#32;&#32;&#32;&#32;rdfs:domain &lowbar;:n0d98de6f177146c6be17e12b2c708b90b1,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#60;http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#Method>,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:Thing,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;:CheckMethod ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy :check&lowbar;method ;  &#10;&#32;&#32;&#32;&#32;rdfs:range &#91; a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:allValuesFrom :DocumentSubdivision ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:onProperty :hasSubdivision ],  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#91; owl:unionOf ( :Document :DocumentSubdivision ) ],  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:Thing,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;:CheckStatement,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;:DocumentSubdivision,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;:Statement ;  &#10;&#32;&#32;&#32;&#32;rdfs:subPropertyOf :operationalizes ;  &#10;&#32;&#32;&#32;&#32;owl:equivalentProperty :operationalizes ;  &#10;&#32;&#32;&#32;&#32;owl:inverseOf :isOperationalizedBy .  &#10;&lowbar;:n0d98de6f177146c6be17e12b2c708b90b6 rdf:first :CheckMethod ;  &#10;&#32;&#32;&#32;&#32;rdf:rest () .  &#10;&lowbar;:n0d98de6f177146c6be17e12b2c708b90b7 rdf:first :Property ;  &#10;&#32;&#32;&#32;&#32;rdf:rest &lowbar;:n0d98de6f177146c6be17e12b2c708b90b6 .  &#10;&lowbar;:n0d98de6f177146c6be17e12b2c708b90b8 rdf:first :FeatureOfInterest ;  &#10;&#32;&#32;&#32;&#32;rdf:rest &lowbar;:n0d98de6f177146c6be17e12b2c708b90b7 .  &#10;&lowbar;:n0d98de6f177146c6be17e12b2c708b90b1 a owl:Class ;  &#10;&#32;&#32;&#32;&#32;rdfs:subClassOf &lowbar;:n0d98de6f177146c6be17e12b2c708b90b1,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:Thing ;  &#10;&#32;&#32;&#32;&#32;owl:equivalentClass &lowbar;:n0d98de6f177146c6be17e12b2c708b90b1 ;  &#10;&#32;&#32;&#32;&#32;owl:unionOf &lowbar;:n0d98de6f177146c6be17e12b2c708b90b8 .</code></pre>|
|[Section top](#minorfail-outcome-number-140)|Pointer|<pre lang="Turtle"><code>:Method owl:sameAs :Method .</code></pre>|
|[Section top](#minorfail-outcome-number-140)|Pointer|<pre lang="Turtle"><code>:hasComparator a owl:FunctionalProperty,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:ObjectProperty ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;has comparator&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:comment &#34;Links a numerical check method to the check method comparato...&#34;,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#34;The comparator of a feature of interest or a property of tha...&#34; ;  &#10;&#32;&#32;&#32;&#32;rdfs:domain &lowbar;:nb92c5a5a628b4fdc98569b584c6851e9b1,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#60;http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#Method>,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:Thing,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;:CheckMethod,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;:NumericalCheckMethod ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy :check&lowbar;method,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;:check&lowbar;method&lowbar;comparators ;  &#10;&#32;&#32;&#32;&#32;rdfs:range &lowbar;:nb92c5a5a628b4fdc98569b584c6851e9b1,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&lowbar;:nb92c5a5a628b4fdc98569b584c6851e9b2,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&lowbar;:nb92c5a5a628b4fdc98569b584c6851e9b3,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#60;http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#Method>,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:Thing,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;skos:Concept,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;:CheckMethod,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;:CheckMethodComparator ;  &#10;&#32;&#32;&#32;&#32;rdfs:subPropertyOf :hasComparator,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;:hasDesign ;  &#10;&#32;&#32;&#32;&#32;owl:equivalentProperty :hasComparator .  &#10;&lowbar;:nb92c5a5a628b4fdc98569b584c6851e9b4 rdf:first :CheckMethod ;  &#10;&#32;&#32;&#32;&#32;rdf:rest () .  &#10;&lowbar;:nb92c5a5a628b4fdc98569b584c6851e9b5 rdf:first :Property ;  &#10;&#32;&#32;&#32;&#32;rdf:rest &lowbar;:nb92c5a5a628b4fdc98569b584c6851e9b4 .  &#10;&lowbar;:nb92c5a5a628b4fdc98569b584c6851e9b6 rdf:first :FeatureOfInterest ;  &#10;&#32;&#32;&#32;&#32;rdf:rest &lowbar;:nb92c5a5a628b4fdc98569b584c6851e9b5 .  &#10;&lowbar;:nb92c5a5a628b4fdc98569b584c6851e9b7 rdf:first skos:Concept ;  &#10;&#32;&#32;&#32;&#32;rdf:rest ( &lowbar;:nb92c5a5a628b4fdc98569b584c6851e9b2 ) .  &#10;&lowbar;:nb92c5a5a628b4fdc98569b584c6851e9b3 rdfs:subClassOf &lowbar;:nb92c5a5a628b4fdc98569b584c6851e9b1,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&lowbar;:nb92c5a5a628b4fdc98569b584c6851e9b2,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&lowbar;:nb92c5a5a628b4fdc98569b584c6851e9b3,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#60;http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#Method>,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:Thing,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;skos:Concept,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;:CheckMethod,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;:CheckMethodComparator ;  &#10;&#32;&#32;&#32;&#32;owl:equivalentClass :CheckMethodComparator ;  &#10;&#32;&#32;&#32;&#32;owl:intersectionOf &lowbar;:nb92c5a5a628b4fdc98569b584c6851e9b7 .  &#10;&lowbar;:nb92c5a5a628b4fdc98569b584c6851e9b2 a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;owl:hasValue :CheckMethodComparatorNomenclature ;  &#10;&#32;&#32;&#32;&#32;owl:onProperty skos:inScheme .  &#10;&lowbar;:nb92c5a5a628b4fdc98569b584c6851e9b1 a owl:Class ;  &#10;&#32;&#32;&#32;&#32;rdfs:subClassOf &lowbar;:nb92c5a5a628b4fdc98569b584c6851e9b1,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:Thing ;  &#10;&#32;&#32;&#32;&#32;owl:equivalentClass &lowbar;:nb92c5a5a628b4fdc98569b584c6851e9b1 ;  &#10;&#32;&#32;&#32;&#32;owl:unionOf &lowbar;:nb92c5a5a628b4fdc98569b584c6851e9b6 .</code></pre>|
|[Section top](#minorfail-outcome-number-140)|Pointer|<pre lang="Turtle"><code>:hasNestedValue a owl:ObjectProperty ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;hasNestedValue&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:comment &#34;TBD&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:domain &lowbar;:n57ea329882d940e7bab86bab1c783830b1,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#60;http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#Method>,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:Thing,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;:CheckMethod ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy :check&lowbar;method ;  &#10;&#32;&#32;&#32;&#32;rdfs:subPropertyOf :hasNestedValue ;  &#10;&#32;&#32;&#32;&#32;owl:equivalentProperty :hasNestedValue .  &#10;&lowbar;:n57ea329882d940e7bab86bab1c783830b2 rdf:first :CheckMethod ;  &#10;&#32;&#32;&#32;&#32;rdf:rest () .  &#10;&lowbar;:n57ea329882d940e7bab86bab1c783830b3 rdf:first :Property ;  &#10;&#32;&#32;&#32;&#32;rdf:rest &lowbar;:n57ea329882d940e7bab86bab1c783830b2 .  &#10;&lowbar;:n57ea329882d940e7bab86bab1c783830b4 rdf:first :FeatureOfInterest ;  &#10;&#32;&#32;&#32;&#32;rdf:rest &lowbar;:n57ea329882d940e7bab86bab1c783830b3 .  &#10;&lowbar;:n57ea329882d940e7bab86bab1c783830b1 a owl:Class ;  &#10;&#32;&#32;&#32;&#32;rdfs:subClassOf &lowbar;:n57ea329882d940e7bab86bab1c783830b1,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:Thing ;  &#10;&#32;&#32;&#32;&#32;owl:equivalentClass &lowbar;:n57ea329882d940e7bab86bab1c783830b1 ;  &#10;&#32;&#32;&#32;&#32;owl:unionOf &lowbar;:n57ea329882d940e7bab86bab1c783830b4 .</code></pre>|
|[Section top](#minorfail-outcome-number-140)|Pointer|<pre lang="Turtle"><code>:hasOperator a owl:FunctionalProperty,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:ObjectProperty ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;has operator&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:comment &#34;Links a boolean check method to the check method operator it...&#34;,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#34;The operator of a feature of interest or a property of that ...&#34; ;  &#10;&#32;&#32;&#32;&#32;rdfs:domain &lowbar;:n8902bf48cda5425b881352f9936e791eb1,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#60;http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#Method>,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:Thing,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;:BooleanCheckMethod,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;:CheckMethod ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy :check&lowbar;method,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;:check&lowbar;method&lowbar;Operators ;  &#10;&#32;&#32;&#32;&#32;rdfs:range &lowbar;:n8902bf48cda5425b881352f9936e791eb1,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&lowbar;:n8902bf48cda5425b881352f9936e791eb2,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&lowbar;:n8902bf48cda5425b881352f9936e791eb3,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#60;http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#Method>,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:Thing,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;skos:Concept,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;:CheckMethod,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;:CheckMethodOperator ;  &#10;&#32;&#32;&#32;&#32;rdfs:subPropertyOf :hasDesign,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;:hasOperator ;  &#10;&#32;&#32;&#32;&#32;owl:equivalentProperty :hasOperator .  &#10;&lowbar;:n8902bf48cda5425b881352f9936e791eb4 rdf:first skos:Concept ;  &#10;&#32;&#32;&#32;&#32;rdf:rest ( &lowbar;:n8902bf48cda5425b881352f9936e791eb2 ) .  &#10;&lowbar;:n8902bf48cda5425b881352f9936e791eb6 rdf:first :CheckMethod ;  &#10;&#32;&#32;&#32;&#32;rdf:rest () .  &#10;&lowbar;:n8902bf48cda5425b881352f9936e791eb7 rdf:first :Property ;  &#10;&#32;&#32;&#32;&#32;rdf:rest &lowbar;:n8902bf48cda5425b881352f9936e791eb6 .  &#10;&lowbar;:n8902bf48cda5425b881352f9936e791eb8 rdf:first :FeatureOfInterest ;  &#10;&#32;&#32;&#32;&#32;rdf:rest &lowbar;:n8902bf48cda5425b881352f9936e791eb7 .  &#10;&lowbar;:n8902bf48cda5425b881352f9936e791eb3 rdfs:subClassOf &lowbar;:n8902bf48cda5425b881352f9936e791eb1,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&lowbar;:n8902bf48cda5425b881352f9936e791eb2,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&lowbar;:n8902bf48cda5425b881352f9936e791eb3,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#60;http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#Method>,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:Thing,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;skos:Concept,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;:CheckMethod,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;:CheckMethodOperator ;  &#10;&#32;&#32;&#32;&#32;owl:equivalentClass :CheckMethodOperator ;  &#10;&#32;&#32;&#32;&#32;owl:intersectionOf &lowbar;:n8902bf48cda5425b881352f9936e791eb4 .  &#10;&lowbar;:n8902bf48cda5425b881352f9936e791eb2 a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;owl:hasValue :CheckMethodOperatorNomenclature ;  &#10;&#32;&#32;&#32;&#32;owl:onProperty skos:inScheme .  &#10;&lowbar;:n8902bf48cda5425b881352f9936e791eb1 a owl:Class ;  &#10;&#32;&#32;&#32;&#32;rdfs:subClassOf &lowbar;:n8902bf48cda5425b881352f9936e791eb1,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:Thing ;  &#10;&#32;&#32;&#32;&#32;owl:equivalentClass &lowbar;:n8902bf48cda5425b881352f9936e791eb1 ;  &#10;&#32;&#32;&#32;&#32;owl:unionOf &lowbar;:n8902bf48cda5425b881352f9936e791eb8 .</code></pre>|
|[Section top](#minorfail-outcome-number-140)|Pointer|<pre lang="Turtle"><code>:hasProperty a owl:ObjectProperty ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;has Property&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:comment &#34;Links a feature of interest to one of its aspect that is int...&#34; ;  &#10;&#32;&#32;&#32;&#32;rdfs:domain &lowbar;:nda42faf41b904a1b9263bab2c78c23b1b1,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#60;http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#Object>,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:Thing,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#60;https://saref.etsi.org/core/FeatureOfInterest>,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;:FeatureOfInterest ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy :feature&lowbar;of&lowbar;interest ;  &#10;&#32;&#32;&#32;&#32;rdfs:range &lowbar;:nda42faf41b904a1b9263bab2c78c23b1b1,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#60;http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#Quality>,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:Thing,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;:Property ;  &#10;&#32;&#32;&#32;&#32;rdfs:subPropertyOf :hasProperty ;  &#10;&#32;&#32;&#32;&#32;owl:equivalentProperty :hasProperty ;  &#10;&#32;&#32;&#32;&#32;owl:sameAs :hasProperty ;  &#10;&#32;&#32;&#32;&#32;skos:example &#34;Links a space to the area property of that space, a wall to ...&#34; .  &#10;&lowbar;:nda42faf41b904a1b9263bab2c78c23b1b2 rdf:first :CheckMethod ;  &#10;&#32;&#32;&#32;&#32;rdf:rest () .  &#10;&lowbar;:nda42faf41b904a1b9263bab2c78c23b1b3 rdf:first :Property ;  &#10;&#32;&#32;&#32;&#32;rdf:rest &lowbar;:nda42faf41b904a1b9263bab2c78c23b1b2 .  &#10;&lowbar;:nda42faf41b904a1b9263bab2c78c23b1b4 rdf:first :FeatureOfInterest ;  &#10;&#32;&#32;&#32;&#32;rdf:rest &lowbar;:nda42faf41b904a1b9263bab2c78c23b1b3 .  &#10;&lowbar;:nda42faf41b904a1b9263bab2c78c23b1b1 a owl:Class ;  &#10;&#32;&#32;&#32;&#32;rdfs:subClassOf &lowbar;:nda42faf41b904a1b9263bab2c78c23b1b1,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:Thing ;  &#10;&#32;&#32;&#32;&#32;owl:equivalentClass &lowbar;:nda42faf41b904a1b9263bab2c78c23b1b1 ;  &#10;&#32;&#32;&#32;&#32;owl:unionOf &lowbar;:nda42faf41b904a1b9263bab2c78c23b1b4 .</code></pre>|
|[Section top](#minorfail-outcome-number-140)|Pointer|<pre lang="Turtle"><code>:hasProperty a owl:ObjectProperty ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;has Property&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:comment &#34;Links a feature of interest to one of its aspect that is int...&#34; ;  &#10;&#32;&#32;&#32;&#32;rdfs:domain &lowbar;:n865a0b897119449995ab6f8f7d1e981ab1,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#60;http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#Object>,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:Thing,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#60;https://saref.etsi.org/core/FeatureOfInterest>,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;:FeatureOfInterest ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy :feature&lowbar;of&lowbar;interest ;  &#10;&#32;&#32;&#32;&#32;rdfs:range &lowbar;:n865a0b897119449995ab6f8f7d1e981ab1,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#60;http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#Quality>,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:Thing,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;:Property ;  &#10;&#32;&#32;&#32;&#32;rdfs:subPropertyOf :hasProperty ;  &#10;&#32;&#32;&#32;&#32;owl:equivalentProperty :hasProperty ;  &#10;&#32;&#32;&#32;&#32;owl:sameAs :hasProperty ;  &#10;&#32;&#32;&#32;&#32;skos:example &#34;Links a space to the area property of that space, a wall to ...&#34; .  &#10;&lowbar;:n865a0b897119449995ab6f8f7d1e981ab2 rdf:first :CheckMethod ;  &#10;&#32;&#32;&#32;&#32;rdf:rest () .  &#10;&lowbar;:n865a0b897119449995ab6f8f7d1e981ab3 rdf:first :Property ;  &#10;&#32;&#32;&#32;&#32;rdf:rest &lowbar;:n865a0b897119449995ab6f8f7d1e981ab2 .  &#10;&lowbar;:n865a0b897119449995ab6f8f7d1e981ab4 rdf:first :FeatureOfInterest ;  &#10;&#32;&#32;&#32;&#32;rdf:rest &lowbar;:n865a0b897119449995ab6f8f7d1e981ab3 .  &#10;&lowbar;:n865a0b897119449995ab6f8f7d1e981ab1 a owl:Class ;  &#10;&#32;&#32;&#32;&#32;rdfs:subClassOf &lowbar;:n865a0b897119449995ab6f8f7d1e981ab1,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:Thing ;  &#10;&#32;&#32;&#32;&#32;owl:equivalentClass &lowbar;:n865a0b897119449995ab6f8f7d1e981ab1 ;  &#10;&#32;&#32;&#32;&#32;owl:unionOf &lowbar;:n865a0b897119449995ab6f8f7d1e981ab4 .</code></pre>|
|[Section top](#minorfail-outcome-number-140)|Pointer|<pre lang="Turtle"><code>:hasQuantityKind a owl:ObjectProperty ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;has quantity kind&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:comment &#34;Links a property to its quantity kind&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:domain &lowbar;:n5c72ec56d8d345b882faa163ae43031db1,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#60;http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#Quality>,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:Thing,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;:Property ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy :feature&lowbar;of&lowbar;interest ;  &#10;&#32;&#32;&#32;&#32;rdfs:range &lowbar;:n5c72ec56d8d345b882faa163ae43031db2,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&lowbar;:n5c72ec56d8d345b882faa163ae43031db3,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;qudt:QuantityKind,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#60;http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#Region>,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:Thing,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;skos:Concept,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;:QuantityKind ;  &#10;&#32;&#32;&#32;&#32;rdfs:subPropertyOf :hasQuantityKind ;  &#10;&#32;&#32;&#32;&#32;owl:equivalentProperty :hasQuantityKind ;  &#10;&#32;&#32;&#32;&#32;owl:sameAs :hasQuantityKind ;  &#10;&#32;&#32;&#32;&#32;skos:example &#34;A space area property to the property kind &#92;&#34;area&#92;&#34;.&#34;@en .  &#10;&lowbar;:n5c72ec56d8d345b882faa163ae43031db4 rdf:first skos:Concept ;  &#10;&#32;&#32;&#32;&#32;rdf:rest ( &lowbar;:n5c72ec56d8d345b882faa163ae43031db2 ) .  &#10;&lowbar;:n5c72ec56d8d345b882faa163ae43031db6 rdf:first :CheckMethod ;  &#10;&#32;&#32;&#32;&#32;rdf:rest () .  &#10;&lowbar;:n5c72ec56d8d345b882faa163ae43031db7 rdf:first :Property ;  &#10;&#32;&#32;&#32;&#32;rdf:rest &lowbar;:n5c72ec56d8d345b882faa163ae43031db6 .  &#10;&lowbar;:n5c72ec56d8d345b882faa163ae43031db8 rdf:first :FeatureOfInterest ;  &#10;&#32;&#32;&#32;&#32;rdf:rest &lowbar;:n5c72ec56d8d345b882faa163ae43031db7 .  &#10;&lowbar;:n5c72ec56d8d345b882faa163ae43031db3 rdfs:subClassOf &lowbar;:n5c72ec56d8d345b882faa163ae43031db2,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&lowbar;:n5c72ec56d8d345b882faa163ae43031db3,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;qudt:QuantityKind,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#60;http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#Region>,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:Thing,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;skos:Concept,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;:QuantityKind ;  &#10;&#32;&#32;&#32;&#32;owl:equivalentClass :QuantityKind ;  &#10;&#32;&#32;&#32;&#32;owl:intersectionOf &lowbar;:n5c72ec56d8d345b882faa163ae43031db4 .  &#10;&lowbar;:n5c72ec56d8d345b882faa163ae43031db1 a owl:Class ;  &#10;&#32;&#32;&#32;&#32;rdfs:subClassOf &lowbar;:n5c72ec56d8d345b882faa163ae43031db1,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:Thing ;  &#10;&#32;&#32;&#32;&#32;owl:equivalentClass &lowbar;:n5c72ec56d8d345b882faa163ae43031db1 ;  &#10;&#32;&#32;&#32;&#32;owl:unionOf &lowbar;:n5c72ec56d8d345b882faa163ae43031db8 .  &#10;&lowbar;:n5c72ec56d8d345b882faa163ae43031db2 a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;owl:hasValue :QuantityKindNomenclature ;  &#10;&#32;&#32;&#32;&#32;owl:onProperty skos:inScheme .</code></pre>|

***
### MinorFail Outcome number 141

[Jump to summary definition](#summary-MinorFail-141)	|	[Previous MinorFail outcome](#minorfail-outcome-number-140)	|	[Next MinorFail outcome](#minorfail-outcome-number-142)

:exclamation:MinorFail outcome
#### Subject detail
|Name|all-fragments|
|----|----|
|Title|All the fragments from branch main that are syntaxically correct as well as their recursive imports|
|Composition|- [Module aec3po](https://github.com/Accord-Project/aec3po/blob/main/src/aec3po.ttl)<br/>- [Module checking&lowbar;act](https://github.com/Accord-Project/aec3po/blob/main/src/checking_act.ttl)<br/>- [Module check&lowbar;method](https://github.com/Accord-Project/aec3po/blob/main/src/check_method.ttl)<br/>- [Module compliance&lowbar;verification&lowbar;report](https://github.com/Accord-Project/aec3po/blob/main/src/compliance_verification_report.ttl)<br/>- [Module data&lowbar;requirement](https://github.com/Accord-Project/aec3po/blob/main/src/data_requirement.ttl)<br/>- [Module document](https://github.com/Accord-Project/aec3po/blob/main/src/document.ttl)<br/>- [Module evidence](https://github.com/Accord-Project/aec3po/blob/main/src/evidence.ttl)<br/>- [Module feature&lowbar;of&lowbar;interest](https://github.com/Accord-Project/aec3po/blob/main/src/feature_of_interest.ttl)<br/>- [Module legal&lowbar;verifier](https://github.com/Accord-Project/aec3po/blob/main/src/legal_verifier.ttl)<br/>- [Module model](https://github.com/Accord-Project/aec3po/blob/main/src/model.ttl)<br/>- [Module rase&lowbar;statement](https://github.com/Accord-Project/aec3po/blob/main/src/rase_statement.ttl)<br/>- [Module statement](https://github.com/Accord-Project/aec3po/blob/main/src/statement.ttl)<br/>- [Module table](https://github.com/Accord-Project/aec3po/blob/main/src/table.ttl)<br/>- [Module vocabularies/administrative&lowbar;areas](https://github.com/Accord-Project/aec3po/blob/main/src/vocabularies/administrative_areas.ttl)<br/>- [Module vocabularies/building&lowbar;structure](https://github.com/Accord-Project/aec3po/blob/main/src/vocabularies/building_structure.ttl)<br/>- [Module vocabularies/building&lowbar;usage](https://github.com/Accord-Project/aec3po/blob/main/src/vocabularies/building_usage.ttl)<br/>- [Module vocabularies/check&lowbar;method&lowbar;comparators](https://github.com/Accord-Project/aec3po/blob/main/src/vocabularies/check_method_comparators.ttl)<br/>- [Module vocabularies/check&lowbar;method&lowbar;operators](https://github.com/Accord-Project/aec3po/blob/main/src/vocabularies/check_method_operators.ttl)<br/>- [Module vocabularies/disciplines](https://github.com/Accord-Project/aec3po/blob/main/src/vocabularies/disciplines.ttl)<br/>- [Module vocabularies/permitting&lowbar;stages](https://github.com/Accord-Project/aec3po/blob/main/src/vocabularies/permitting_stages.ttl)<br/>- [Module vocabularies/quantity&lowbar;kinds](https://github.com/Accord-Project/aec3po/blob/main/src/vocabularies/quantity_kinds.ttl)<br/>- [Module vocabularies/&lowbar;shape](https://github.com/Accord-Project/aec3po/blob/main/src/vocabularies/_shape.ttl)|

#### Criterion detail
|Identifier|[domain-and-range-referencing](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#domain-and-range-referencing)|
|----|----|
|Title|Domain and range referencing test|
|Description|A test case from the Best Practices tests checking if all the ranges and domains from the test subject point to terms that are defined in the vocabulary.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-141)|Identifier|`range-out-of-vocabulary`|
|[Section top](#minorfail-outcome-number-141)|Title|Range out of vocabulary|
|[Section top](#minorfail-outcome-number-141)|Description|Some properties have a range out of the ontology|
|[Section top](#minorfail-outcome-number-141)|Pointer|<pre lang="Turtle"><code>:usedMethod a owl:ObjectProperty ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;used method&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:comment &#34;Links a checking act to the method it used (a aec3po:CheckMe...&#34; ;  &#10;&#32;&#32;&#32;&#32;rdfs:domain &#91; a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:onProperty :usedMethod ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:someValuesFrom :CheckMethod ],  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#91; a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:onProperty :madeBy ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:someValuesFrom :ProcessVerifier ],  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#91; a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:onProperty :checked ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:someValuesFrom owl:Thing ],  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#91; a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:onProperty :hasReport ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:someValuesFrom :ComplianceVerificationReport ],  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#60;http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#Event>,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:Thing,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;:CheckingAct ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy :checking&lowbar;act ;  &#10;&#32;&#32;&#32;&#32;rdfs:range &lowbar;:n6c0347db4d85437d872be602ce8fb02db5,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#60;http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#Method>,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:Thing,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;:CheckMethod ;  &#10;&#32;&#32;&#32;&#32;rdfs:subPropertyOf :usedMethod ;  &#10;&#32;&#32;&#32;&#32;owl:equivalentProperty :usedMethod .  &#10;&lowbar;:n6c0347db4d85437d872be602ce8fb02db6 rdf:first :CheckMethod ;  &#10;&#32;&#32;&#32;&#32;rdf:rest () .  &#10;&lowbar;:n6c0347db4d85437d872be602ce8fb02db7 rdf:first :Property ;  &#10;&#32;&#32;&#32;&#32;rdf:rest &lowbar;:n6c0347db4d85437d872be602ce8fb02db6 .  &#10;&lowbar;:n6c0347db4d85437d872be602ce8fb02db8 rdf:first :FeatureOfInterest ;  &#10;&#32;&#32;&#32;&#32;rdf:rest &lowbar;:n6c0347db4d85437d872be602ce8fb02db7 .  &#10;&lowbar;:n6c0347db4d85437d872be602ce8fb02db5 a owl:Class ;  &#10;&#32;&#32;&#32;&#32;rdfs:subClassOf &lowbar;:n6c0347db4d85437d872be602ce8fb02db5,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:Thing ;  &#10;&#32;&#32;&#32;&#32;owl:equivalentClass &lowbar;:n6c0347db4d85437d872be602ce8fb02db5 ;  &#10;&#32;&#32;&#32;&#32;owl:unionOf &lowbar;:n6c0347db4d85437d872be602ce8fb02db8 .</code></pre>|
|[Section top](#minorfail-outcome-number-141)|Pointer|<pre lang="Turtle"><code>:Method owl:sameAs :Method .</code></pre>|
|[Section top](#minorfail-outcome-number-141)|Pointer|<pre lang="Turtle"><code>:isOperationalizedBy a owl:ObjectProperty ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;is operationalized by&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:comment &#34;Links a check statement in a document to a check method that...&#34; ;  &#10;&#32;&#32;&#32;&#32;rdfs:domain &#91; a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:allValuesFrom :DocumentSubdivision ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:onProperty :hasSubdivision ],  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#91; owl:unionOf ( :Document :DocumentSubdivision ) ],  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:Thing,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;:CheckStatement,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;:DocumentSubdivision,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;:Statement ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy :check&lowbar;method ;  &#10;&#32;&#32;&#32;&#32;rdfs:range &lowbar;:nb2596bbfb804469891e50e5e53b9ae37b5,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#60;http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#Method>,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:Thing,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;:CheckMethod ;  &#10;&#32;&#32;&#32;&#32;rdfs:subPropertyOf :isOperationalizedBy ;  &#10;&#32;&#32;&#32;&#32;owl:equivalentProperty :isOperationalizedBy ;  &#10;&#32;&#32;&#32;&#32;owl:inverseOf :operationalizes .  &#10;&lowbar;:nb2596bbfb804469891e50e5e53b9ae37b6 rdf:first :CheckMethod ;  &#10;&#32;&#32;&#32;&#32;rdf:rest () .  &#10;&lowbar;:nb2596bbfb804469891e50e5e53b9ae37b7 rdf:first :Property ;  &#10;&#32;&#32;&#32;&#32;rdf:rest &lowbar;:nb2596bbfb804469891e50e5e53b9ae37b6 .  &#10;&lowbar;:nb2596bbfb804469891e50e5e53b9ae37b8 rdf:first :FeatureOfInterest ;  &#10;&#32;&#32;&#32;&#32;rdf:rest &lowbar;:nb2596bbfb804469891e50e5e53b9ae37b7 .  &#10;&lowbar;:nb2596bbfb804469891e50e5e53b9ae37b5 a owl:Class ;  &#10;&#32;&#32;&#32;&#32;rdfs:subClassOf &lowbar;:nb2596bbfb804469891e50e5e53b9ae37b5,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:Thing ;  &#10;&#32;&#32;&#32;&#32;owl:equivalentClass &lowbar;:nb2596bbfb804469891e50e5e53b9ae37b5 ;  &#10;&#32;&#32;&#32;&#32;owl:unionOf &lowbar;:nb2596bbfb804469891e50e5e53b9ae37b8 .</code></pre>|
|[Section top](#minorfail-outcome-number-141)|Pointer|<pre lang="Turtle"><code>:hasComparator a owl:FunctionalProperty,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:ObjectProperty ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;has comparator&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:comment &#34;Links a numerical check method to the check method comparato...&#34;,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#34;The comparator of a feature of interest or a property of tha...&#34; ;  &#10;&#32;&#32;&#32;&#32;rdfs:domain &lowbar;:n5bca972bafc54ea287c1449307edff2fb1,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#60;http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#Method>,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:Thing,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;:CheckMethod,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;:NumericalCheckMethod ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy :check&lowbar;method,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;:check&lowbar;method&lowbar;comparators ;  &#10;&#32;&#32;&#32;&#32;rdfs:range &lowbar;:n5bca972bafc54ea287c1449307edff2fb1,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&lowbar;:n5bca972bafc54ea287c1449307edff2fb2,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&lowbar;:n5bca972bafc54ea287c1449307edff2fb3,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#60;http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#Method>,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:Thing,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;skos:Concept,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;:CheckMethod,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;:CheckMethodComparator ;  &#10;&#32;&#32;&#32;&#32;rdfs:subPropertyOf :hasComparator,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;:hasDesign ;  &#10;&#32;&#32;&#32;&#32;owl:equivalentProperty :hasComparator .  &#10;&lowbar;:n5bca972bafc54ea287c1449307edff2fb4 rdf:first :CheckMethod ;  &#10;&#32;&#32;&#32;&#32;rdf:rest () .  &#10;&lowbar;:n5bca972bafc54ea287c1449307edff2fb5 rdf:first :Property ;  &#10;&#32;&#32;&#32;&#32;rdf:rest &lowbar;:n5bca972bafc54ea287c1449307edff2fb4 .  &#10;&lowbar;:n5bca972bafc54ea287c1449307edff2fb6 rdf:first :FeatureOfInterest ;  &#10;&#32;&#32;&#32;&#32;rdf:rest &lowbar;:n5bca972bafc54ea287c1449307edff2fb5 .  &#10;&lowbar;:n5bca972bafc54ea287c1449307edff2fb7 rdf:first skos:Concept ;  &#10;&#32;&#32;&#32;&#32;rdf:rest ( &lowbar;:n5bca972bafc54ea287c1449307edff2fb2 ) .  &#10;&lowbar;:n5bca972bafc54ea287c1449307edff2fb3 rdfs:subClassOf &lowbar;:n5bca972bafc54ea287c1449307edff2fb1,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&lowbar;:n5bca972bafc54ea287c1449307edff2fb2,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&lowbar;:n5bca972bafc54ea287c1449307edff2fb3,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#60;http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#Method>,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:Thing,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;skos:Concept,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;:CheckMethod,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;:CheckMethodComparator ;  &#10;&#32;&#32;&#32;&#32;owl:equivalentClass :CheckMethodComparator ;  &#10;&#32;&#32;&#32;&#32;owl:intersectionOf &lowbar;:n5bca972bafc54ea287c1449307edff2fb7 .  &#10;&lowbar;:n5bca972bafc54ea287c1449307edff2fb2 a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;owl:hasValue :CheckMethodComparatorNomenclature ;  &#10;&#32;&#32;&#32;&#32;owl:onProperty skos:inScheme .  &#10;&lowbar;:n5bca972bafc54ea287c1449307edff2fb1 a owl:Class ;  &#10;&#32;&#32;&#32;&#32;rdfs:subClassOf &lowbar;:n5bca972bafc54ea287c1449307edff2fb1,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:Thing ;  &#10;&#32;&#32;&#32;&#32;owl:equivalentClass &lowbar;:n5bca972bafc54ea287c1449307edff2fb1 ;  &#10;&#32;&#32;&#32;&#32;owl:unionOf &lowbar;:n5bca972bafc54ea287c1449307edff2fb6 .</code></pre>|
|[Section top](#minorfail-outcome-number-141)|Pointer|<pre lang="Turtle"><code>:hasComparator a owl:FunctionalProperty,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:ObjectProperty ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;has comparator&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:comment &#34;Links a numerical check method to the check method comparato...&#34;,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#34;The comparator of a feature of interest or a property of tha...&#34; ;  &#10;&#32;&#32;&#32;&#32;rdfs:domain &lowbar;:n35cf961869c842e2a5baae6becce8002b1,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#60;http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#Method>,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:Thing,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;:CheckMethod,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;:NumericalCheckMethod ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy :check&lowbar;method,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;:check&lowbar;method&lowbar;comparators ;  &#10;&#32;&#32;&#32;&#32;rdfs:range &lowbar;:n35cf961869c842e2a5baae6becce8002b1,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&lowbar;:n35cf961869c842e2a5baae6becce8002b2,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&lowbar;:n35cf961869c842e2a5baae6becce8002b3,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#60;http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#Method>,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:Thing,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;skos:Concept,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;:CheckMethod,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;:CheckMethodComparator ;  &#10;&#32;&#32;&#32;&#32;rdfs:subPropertyOf :hasComparator,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;:hasDesign ;  &#10;&#32;&#32;&#32;&#32;owl:equivalentProperty :hasComparator .  &#10;&lowbar;:n35cf961869c842e2a5baae6becce8002b4 rdf:first :CheckMethod ;  &#10;&#32;&#32;&#32;&#32;rdf:rest () .  &#10;&lowbar;:n35cf961869c842e2a5baae6becce8002b5 rdf:first :Property ;  &#10;&#32;&#32;&#32;&#32;rdf:rest &lowbar;:n35cf961869c842e2a5baae6becce8002b4 .  &#10;&lowbar;:n35cf961869c842e2a5baae6becce8002b6 rdf:first :FeatureOfInterest ;  &#10;&#32;&#32;&#32;&#32;rdf:rest &lowbar;:n35cf961869c842e2a5baae6becce8002b5 .  &#10;&lowbar;:n35cf961869c842e2a5baae6becce8002b7 rdf:first skos:Concept ;  &#10;&#32;&#32;&#32;&#32;rdf:rest ( &lowbar;:n35cf961869c842e2a5baae6becce8002b2 ) .  &#10;&lowbar;:n35cf961869c842e2a5baae6becce8002b3 rdfs:subClassOf &lowbar;:n35cf961869c842e2a5baae6becce8002b1,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&lowbar;:n35cf961869c842e2a5baae6becce8002b2,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&lowbar;:n35cf961869c842e2a5baae6becce8002b3,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#60;http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#Method>,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:Thing,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;skos:Concept,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;:CheckMethod,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;:CheckMethodComparator ;  &#10;&#32;&#32;&#32;&#32;owl:equivalentClass :CheckMethodComparator ;  &#10;&#32;&#32;&#32;&#32;owl:intersectionOf &lowbar;:n35cf961869c842e2a5baae6becce8002b7 .  &#10;&lowbar;:n35cf961869c842e2a5baae6becce8002b2 a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;owl:hasValue :CheckMethodComparatorNomenclature ;  &#10;&#32;&#32;&#32;&#32;owl:onProperty skos:inScheme .  &#10;&lowbar;:n35cf961869c842e2a5baae6becce8002b1 a owl:Class ;  &#10;&#32;&#32;&#32;&#32;rdfs:subClassOf &lowbar;:n35cf961869c842e2a5baae6becce8002b1,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:Thing ;  &#10;&#32;&#32;&#32;&#32;owl:equivalentClass &lowbar;:n35cf961869c842e2a5baae6becce8002b1 ;  &#10;&#32;&#32;&#32;&#32;owl:unionOf &lowbar;:n35cf961869c842e2a5baae6becce8002b6 .</code></pre>|
|[Section top](#minorfail-outcome-number-141)|Pointer|<pre lang="Turtle"><code>:hasUnit a owl:FunctionalProperty,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:ObjectProperty ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;hasUnit&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:comment &#34;the hasUnit property is used to link a specific property or ...&#34; ;  &#10;&#32;&#32;&#32;&#32;rdfs:domain &lowbar;:nb90f82e010194da7a83f408bab11aa6eb1,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:Thing ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy :check&lowbar;method ;  &#10;&#32;&#32;&#32;&#32;rdfs:range qudt:Unit ;  &#10;&#32;&#32;&#32;&#32;rdfs:subPropertyOf :hasUnit ;  &#10;&#32;&#32;&#32;&#32;owl:eqivalentProperty qudt:hasValue ;  &#10;&#32;&#32;&#32;&#32;owl:equivalentProperty :hasUnit .  &#10;&lowbar;:nb90f82e010194da7a83f408bab11aa6eb2 rdf:first :CheckMethod ;  &#10;&#32;&#32;&#32;&#32;rdf:rest () .  &#10;&lowbar;:nb90f82e010194da7a83f408bab11aa6eb3 rdf:first :Property ;  &#10;&#32;&#32;&#32;&#32;rdf:rest &lowbar;:nb90f82e010194da7a83f408bab11aa6eb2 .  &#10;&lowbar;:nb90f82e010194da7a83f408bab11aa6eb4 rdf:first :FeatureOfInterest ;  &#10;&#32;&#32;&#32;&#32;rdf:rest &lowbar;:nb90f82e010194da7a83f408bab11aa6eb3 .  &#10;&lowbar;:nb90f82e010194da7a83f408bab11aa6eb1 a owl:Class ;  &#10;&#32;&#32;&#32;&#32;rdfs:subClassOf &lowbar;:nb90f82e010194da7a83f408bab11aa6eb1,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:Thing ;  &#10;&#32;&#32;&#32;&#32;owl:equivalentClass &lowbar;:nb90f82e010194da7a83f408bab11aa6eb1 ;  &#10;&#32;&#32;&#32;&#32;owl:unionOf &lowbar;:nb90f82e010194da7a83f408bab11aa6eb4 .</code></pre>|
|[Section top](#minorfail-outcome-number-141)|Pointer|<pre lang="Turtle"><code></code></pre>|
|[Section top](#minorfail-outcome-number-141)|Pointer|<pre lang="Turtle"><code>:hasOperator a owl:FunctionalProperty,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:ObjectProperty ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;has operator&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:comment &#34;Links a boolean check method to the check method operator it...&#34;,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#34;The operator of a feature of interest or a property of that ...&#34; ;  &#10;&#32;&#32;&#32;&#32;rdfs:domain &lowbar;:nf7c7cef0687849e7815fc43acb16250fb1,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#60;http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#Method>,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:Thing,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;:BooleanCheckMethod,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;:CheckMethod ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy :check&lowbar;method,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;:check&lowbar;method&lowbar;Operators ;  &#10;&#32;&#32;&#32;&#32;rdfs:range &lowbar;:nf7c7cef0687849e7815fc43acb16250fb1,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&lowbar;:nf7c7cef0687849e7815fc43acb16250fb2,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&lowbar;:nf7c7cef0687849e7815fc43acb16250fb3,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#60;http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#Method>,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:Thing,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;skos:Concept,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;:CheckMethod,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;:CheckMethodOperator ;  &#10;&#32;&#32;&#32;&#32;rdfs:subPropertyOf :hasDesign,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;:hasOperator ;  &#10;&#32;&#32;&#32;&#32;owl:equivalentProperty :hasOperator .  &#10;&lowbar;:nf7c7cef0687849e7815fc43acb16250fb4 rdf:first skos:Concept ;  &#10;&#32;&#32;&#32;&#32;rdf:rest ( &lowbar;:nf7c7cef0687849e7815fc43acb16250fb2 ) .  &#10;&lowbar;:nf7c7cef0687849e7815fc43acb16250fb6 rdf:first :CheckMethod ;  &#10;&#32;&#32;&#32;&#32;rdf:rest () .  &#10;&lowbar;:nf7c7cef0687849e7815fc43acb16250fb7 rdf:first :Property ;  &#10;&#32;&#32;&#32;&#32;rdf:rest &lowbar;:nf7c7cef0687849e7815fc43acb16250fb6 .  &#10;&lowbar;:nf7c7cef0687849e7815fc43acb16250fb8 rdf:first :FeatureOfInterest ;  &#10;&#32;&#32;&#32;&#32;rdf:rest &lowbar;:nf7c7cef0687849e7815fc43acb16250fb7 .  &#10;&lowbar;:nf7c7cef0687849e7815fc43acb16250fb3 rdfs:subClassOf &lowbar;:nf7c7cef0687849e7815fc43acb16250fb1,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&lowbar;:nf7c7cef0687849e7815fc43acb16250fb2,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&lowbar;:nf7c7cef0687849e7815fc43acb16250fb3,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#60;http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#Method>,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:Thing,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;skos:Concept,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;:CheckMethod,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;:CheckMethodOperator ;  &#10;&#32;&#32;&#32;&#32;owl:equivalentClass :CheckMethodOperator ;  &#10;&#32;&#32;&#32;&#32;owl:intersectionOf &lowbar;:nf7c7cef0687849e7815fc43acb16250fb4 .  &#10;&lowbar;:nf7c7cef0687849e7815fc43acb16250fb2 a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;owl:hasValue :CheckMethodOperatorNomenclature ;  &#10;&#32;&#32;&#32;&#32;owl:onProperty skos:inScheme .  &#10;&lowbar;:nf7c7cef0687849e7815fc43acb16250fb1 a owl:Class ;  &#10;&#32;&#32;&#32;&#32;rdfs:subClassOf &lowbar;:nf7c7cef0687849e7815fc43acb16250fb1,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:Thing ;  &#10;&#32;&#32;&#32;&#32;owl:equivalentClass &lowbar;:nf7c7cef0687849e7815fc43acb16250fb1 ;  &#10;&#32;&#32;&#32;&#32;owl:unionOf &lowbar;:nf7c7cef0687849e7815fc43acb16250fb8 .</code></pre>|
|[Section top](#minorfail-outcome-number-141)|Pointer|<pre lang="Turtle"><code>:hasOperator a owl:FunctionalProperty,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:ObjectProperty ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;has operator&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:comment &#34;Links a boolean check method to the check method operator it...&#34;,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#34;The operator of a feature of interest or a property of that ...&#34; ;  &#10;&#32;&#32;&#32;&#32;rdfs:domain &lowbar;:n12d6d8110f33480dbf294767e46a3adbb1,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#60;http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#Method>,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:Thing,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;:BooleanCheckMethod,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;:CheckMethod ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy :check&lowbar;method,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;:check&lowbar;method&lowbar;Operators ;  &#10;&#32;&#32;&#32;&#32;rdfs:range &lowbar;:n12d6d8110f33480dbf294767e46a3adbb1,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&lowbar;:n12d6d8110f33480dbf294767e46a3adbb2,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&lowbar;:n12d6d8110f33480dbf294767e46a3adbb3,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#60;http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#Method>,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:Thing,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;skos:Concept,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;:CheckMethod,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;:CheckMethodOperator ;  &#10;&#32;&#32;&#32;&#32;rdfs:subPropertyOf :hasDesign,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;:hasOperator ;  &#10;&#32;&#32;&#32;&#32;owl:equivalentProperty :hasOperator .  &#10;&lowbar;:n12d6d8110f33480dbf294767e46a3adbb4 rdf:first skos:Concept ;  &#10;&#32;&#32;&#32;&#32;rdf:rest ( &lowbar;:n12d6d8110f33480dbf294767e46a3adbb2 ) .  &#10;&lowbar;:n12d6d8110f33480dbf294767e46a3adbb6 rdf:first :CheckMethod ;  &#10;&#32;&#32;&#32;&#32;rdf:rest () .  &#10;&lowbar;:n12d6d8110f33480dbf294767e46a3adbb7 rdf:first :Property ;  &#10;&#32;&#32;&#32;&#32;rdf:rest &lowbar;:n12d6d8110f33480dbf294767e46a3adbb6 .  &#10;&lowbar;:n12d6d8110f33480dbf294767e46a3adbb8 rdf:first :FeatureOfInterest ;  &#10;&#32;&#32;&#32;&#32;rdf:rest &lowbar;:n12d6d8110f33480dbf294767e46a3adbb7 .  &#10;&lowbar;:n12d6d8110f33480dbf294767e46a3adbb3 rdfs:subClassOf &lowbar;:n12d6d8110f33480dbf294767e46a3adbb1,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&lowbar;:n12d6d8110f33480dbf294767e46a3adbb2,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&lowbar;:n12d6d8110f33480dbf294767e46a3adbb3,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#60;http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#Method>,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:Thing,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;skos:Concept,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;:CheckMethod,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;:CheckMethodOperator ;  &#10;&#32;&#32;&#32;&#32;owl:equivalentClass :CheckMethodOperator ;  &#10;&#32;&#32;&#32;&#32;owl:intersectionOf &lowbar;:n12d6d8110f33480dbf294767e46a3adbb4 .  &#10;&lowbar;:n12d6d8110f33480dbf294767e46a3adbb2 a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;owl:hasValue :CheckMethodOperatorNomenclature ;  &#10;&#32;&#32;&#32;&#32;owl:onProperty skos:inScheme .  &#10;&lowbar;:n12d6d8110f33480dbf294767e46a3adbb1 a owl:Class ;  &#10;&#32;&#32;&#32;&#32;rdfs:subClassOf &lowbar;:n12d6d8110f33480dbf294767e46a3adbb1,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:Thing ;  &#10;&#32;&#32;&#32;&#32;owl:equivalentClass &lowbar;:n12d6d8110f33480dbf294767e46a3adbb1 ;  &#10;&#32;&#32;&#32;&#32;owl:unionOf &lowbar;:n12d6d8110f33480dbf294767e46a3adbb8 .</code></pre>|
|[Section top](#minorfail-outcome-number-141)|Pointer|<pre lang="Turtle"><code>:hasNestedTarget a owl:ObjectProperty ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;hasNestedTarget&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:comment &#34;&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy :check&lowbar;method ;  &#10;&#32;&#32;&#32;&#32;rdfs:range &lowbar;:n0ba4349ddb4644df9a17d6cc9bb6a436b1,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#60;http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#Method>,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:Thing,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;:CheckMethod ;  &#10;&#32;&#32;&#32;&#32;rdfs:subPropertyOf :hasNestedTarget ;  &#10;&#32;&#32;&#32;&#32;owl:equivalentProperty :hasNestedTarget .  &#10;&lowbar;:n0ba4349ddb4644df9a17d6cc9bb6a436b2 rdf:first :CheckMethod ;  &#10;&#32;&#32;&#32;&#32;rdf:rest () .  &#10;&lowbar;:n0ba4349ddb4644df9a17d6cc9bb6a436b3 rdf:first :Property ;  &#10;&#32;&#32;&#32;&#32;rdf:rest &lowbar;:n0ba4349ddb4644df9a17d6cc9bb6a436b2 .  &#10;&lowbar;:n0ba4349ddb4644df9a17d6cc9bb6a436b4 rdf:first :FeatureOfInterest ;  &#10;&#32;&#32;&#32;&#32;rdf:rest &lowbar;:n0ba4349ddb4644df9a17d6cc9bb6a436b3 .  &#10;&lowbar;:n0ba4349ddb4644df9a17d6cc9bb6a436b1 a owl:Class ;  &#10;&#32;&#32;&#32;&#32;rdfs:subClassOf &lowbar;:n0ba4349ddb4644df9a17d6cc9bb6a436b1,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:Thing ;  &#10;&#32;&#32;&#32;&#32;owl:equivalentClass &lowbar;:n0ba4349ddb4644df9a17d6cc9bb6a436b1 ;  &#10;&#32;&#32;&#32;&#32;owl:unionOf &lowbar;:n0ba4349ddb4644df9a17d6cc9bb6a436b4 .</code></pre>|
|[Section top](#minorfail-outcome-number-141)|Pointer|<pre lang="Turtle"><code>:hasFormat a owl:ObjectProperty ;  &#10;&#32;&#32;&#32;&#32;rdfs:comment &#34;Defines the format of an evidence, which is of type dct:form...&#34; ;  &#10;&#32;&#32;&#32;&#32;rdfs:domain &#91; a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:allValuesFrom :DocumentSubdivision ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:onProperty :hasSubdivision ],  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#91; owl:unionOf ( :Document :DocumentSubdivision ) ],  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:Thing,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;:DocumentSubdivision,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;:Statement ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy :evidence ;  &#10;&#32;&#32;&#32;&#32;rdfs:range dc:format ;  &#10;&#32;&#32;&#32;&#32;rdfs:subPropertyOf :hasFormat ;  &#10;&#32;&#32;&#32;&#32;owl:equivalentProperty :hasFormat ;  &#10;&#32;&#32;&#32;&#32;owl:sameAs :hasFormat ;  &#10;&#32;&#32;&#32;&#32;skos:example &#34;an image, a drawing or a model can be an evidence.&#34;@en .</code></pre>|
|[Section top](#minorfail-outcome-number-141)|Pointer|<pre lang="Turtle"><code>:hasProperty a owl:ObjectProperty ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;has Property&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:comment &#34;Links a feature of interest to one of its aspect that is int...&#34; ;  &#10;&#32;&#32;&#32;&#32;rdfs:domain &lowbar;:nf08456e3d7744cebafdab6e681926558b1,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#60;http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#Object>,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:Thing,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#60;https://saref.etsi.org/core/FeatureOfInterest>,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;:FeatureOfInterest ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy :feature&lowbar;of&lowbar;interest ;  &#10;&#32;&#32;&#32;&#32;rdfs:range &lowbar;:nf08456e3d7744cebafdab6e681926558b1,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#60;http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#Quality>,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:Thing,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;:Property ;  &#10;&#32;&#32;&#32;&#32;rdfs:subPropertyOf :hasProperty ;  &#10;&#32;&#32;&#32;&#32;owl:equivalentProperty :hasProperty ;  &#10;&#32;&#32;&#32;&#32;owl:sameAs :hasProperty ;  &#10;&#32;&#32;&#32;&#32;skos:example &#34;Links a space to the area property of that space, a wall to ...&#34; .  &#10;&lowbar;:nf08456e3d7744cebafdab6e681926558b2 rdf:first :CheckMethod ;  &#10;&#32;&#32;&#32;&#32;rdf:rest () .  &#10;&lowbar;:nf08456e3d7744cebafdab6e681926558b3 rdf:first :Property ;  &#10;&#32;&#32;&#32;&#32;rdf:rest &lowbar;:nf08456e3d7744cebafdab6e681926558b2 .  &#10;&lowbar;:nf08456e3d7744cebafdab6e681926558b4 rdf:first :FeatureOfInterest ;  &#10;&#32;&#32;&#32;&#32;rdf:rest &lowbar;:nf08456e3d7744cebafdab6e681926558b3 .  &#10;&lowbar;:nf08456e3d7744cebafdab6e681926558b1 a owl:Class ;  &#10;&#32;&#32;&#32;&#32;rdfs:subClassOf &lowbar;:nf08456e3d7744cebafdab6e681926558b1,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:Thing ;  &#10;&#32;&#32;&#32;&#32;owl:equivalentClass &lowbar;:nf08456e3d7744cebafdab6e681926558b1 ;  &#10;&#32;&#32;&#32;&#32;owl:unionOf &lowbar;:nf08456e3d7744cebafdab6e681926558b4 .</code></pre>|
|[Section top](#minorfail-outcome-number-141)|Pointer|<pre lang="Turtle"><code>:hasQuantityKind a owl:ObjectProperty ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;has quantity kind&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:comment &#34;Links a property to its quantity kind&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:domain &lowbar;:nafe85455017f4f5589226cb603785d88b1,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#60;http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#Quality>,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:Thing,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;:Property ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy :feature&lowbar;of&lowbar;interest ;  &#10;&#32;&#32;&#32;&#32;rdfs:range &lowbar;:nafe85455017f4f5589226cb603785d88b2,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&lowbar;:nafe85455017f4f5589226cb603785d88b3,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;qudt:QuantityKind,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#60;http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#Region>,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:Thing,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;skos:Concept,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;:QuantityKind ;  &#10;&#32;&#32;&#32;&#32;rdfs:subPropertyOf :hasQuantityKind ;  &#10;&#32;&#32;&#32;&#32;owl:equivalentProperty :hasQuantityKind ;  &#10;&#32;&#32;&#32;&#32;owl:sameAs :hasQuantityKind ;  &#10;&#32;&#32;&#32;&#32;skos:example &#34;A space area property to the property kind &#92;&#34;area&#92;&#34;.&#34;@en .  &#10;&lowbar;:nafe85455017f4f5589226cb603785d88b4 rdf:first skos:Concept ;  &#10;&#32;&#32;&#32;&#32;rdf:rest ( &lowbar;:nafe85455017f4f5589226cb603785d88b2 ) .  &#10;&lowbar;:nafe85455017f4f5589226cb603785d88b6 rdf:first :CheckMethod ;  &#10;&#32;&#32;&#32;&#32;rdf:rest () .  &#10;&lowbar;:nafe85455017f4f5589226cb603785d88b7 rdf:first :Property ;  &#10;&#32;&#32;&#32;&#32;rdf:rest &lowbar;:nafe85455017f4f5589226cb603785d88b6 .  &#10;&lowbar;:nafe85455017f4f5589226cb603785d88b8 rdf:first :FeatureOfInterest ;  &#10;&#32;&#32;&#32;&#32;rdf:rest &lowbar;:nafe85455017f4f5589226cb603785d88b7 .  &#10;&lowbar;:nafe85455017f4f5589226cb603785d88b3 rdfs:subClassOf &lowbar;:nafe85455017f4f5589226cb603785d88b2,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&lowbar;:nafe85455017f4f5589226cb603785d88b3,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;qudt:QuantityKind,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#60;http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#Region>,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:Thing,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;skos:Concept,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;:QuantityKind ;  &#10;&#32;&#32;&#32;&#32;owl:equivalentClass :QuantityKind ;  &#10;&#32;&#32;&#32;&#32;owl:intersectionOf &lowbar;:nafe85455017f4f5589226cb603785d88b4 .  &#10;&lowbar;:nafe85455017f4f5589226cb603785d88b1 a owl:Class ;  &#10;&#32;&#32;&#32;&#32;rdfs:subClassOf &lowbar;:nafe85455017f4f5589226cb603785d88b1,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:Thing ;  &#10;&#32;&#32;&#32;&#32;owl:equivalentClass &lowbar;:nafe85455017f4f5589226cb603785d88b1 ;  &#10;&#32;&#32;&#32;&#32;owl:unionOf &lowbar;:nafe85455017f4f5589226cb603785d88b8 .  &#10;&lowbar;:nafe85455017f4f5589226cb603785d88b2 a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;owl:hasValue :QuantityKindNomenclature ;  &#10;&#32;&#32;&#32;&#32;owl:onProperty skos:inScheme .</code></pre>|
|[Section top](#minorfail-outcome-number-141)|Pointer|<pre lang="Turtle"><code>:hasQuantityKind a owl:ObjectProperty ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;has quantity kind&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:comment &#34;Links a property to its quantity kind&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:domain &lowbar;:naa718e9f416c4030994eccca90de78ddb1,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#60;http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#Quality>,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:Thing,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;:Property ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy :feature&lowbar;of&lowbar;interest ;  &#10;&#32;&#32;&#32;&#32;rdfs:range &lowbar;:naa718e9f416c4030994eccca90de78ddb2,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&lowbar;:naa718e9f416c4030994eccca90de78ddb3,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;qudt:QuantityKind,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#60;http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#Region>,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:Thing,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;skos:Concept,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;:QuantityKind ;  &#10;&#32;&#32;&#32;&#32;rdfs:subPropertyOf :hasQuantityKind ;  &#10;&#32;&#32;&#32;&#32;owl:equivalentProperty :hasQuantityKind ;  &#10;&#32;&#32;&#32;&#32;owl:sameAs :hasQuantityKind ;  &#10;&#32;&#32;&#32;&#32;skos:example &#34;A space area property to the property kind &#92;&#34;area&#92;&#34;.&#34;@en .  &#10;&lowbar;:naa718e9f416c4030994eccca90de78ddb4 rdf:first skos:Concept ;  &#10;&#32;&#32;&#32;&#32;rdf:rest ( &lowbar;:naa718e9f416c4030994eccca90de78ddb2 ) .  &#10;&lowbar;:naa718e9f416c4030994eccca90de78ddb6 rdf:first :CheckMethod ;  &#10;&#32;&#32;&#32;&#32;rdf:rest () .  &#10;&lowbar;:naa718e9f416c4030994eccca90de78ddb7 rdf:first :Property ;  &#10;&#32;&#32;&#32;&#32;rdf:rest &lowbar;:naa718e9f416c4030994eccca90de78ddb6 .  &#10;&lowbar;:naa718e9f416c4030994eccca90de78ddb8 rdf:first :FeatureOfInterest ;  &#10;&#32;&#32;&#32;&#32;rdf:rest &lowbar;:naa718e9f416c4030994eccca90de78ddb7 .  &#10;&lowbar;:naa718e9f416c4030994eccca90de78ddb3 rdfs:subClassOf &lowbar;:naa718e9f416c4030994eccca90de78ddb2,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&lowbar;:naa718e9f416c4030994eccca90de78ddb3,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;qudt:QuantityKind,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#60;http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#Region>,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:Thing,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;skos:Concept,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;:QuantityKind ;  &#10;&#32;&#32;&#32;&#32;owl:equivalentClass :QuantityKind ;  &#10;&#32;&#32;&#32;&#32;owl:intersectionOf &lowbar;:naa718e9f416c4030994eccca90de78ddb4 .  &#10;&lowbar;:naa718e9f416c4030994eccca90de78ddb1 a owl:Class ;  &#10;&#32;&#32;&#32;&#32;rdfs:subClassOf &lowbar;:naa718e9f416c4030994eccca90de78ddb1,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:Thing ;  &#10;&#32;&#32;&#32;&#32;owl:equivalentClass &lowbar;:naa718e9f416c4030994eccca90de78ddb1 ;  &#10;&#32;&#32;&#32;&#32;owl:unionOf &lowbar;:naa718e9f416c4030994eccca90de78ddb8 .  &#10;&lowbar;:naa718e9f416c4030994eccca90de78ddb2 a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;owl:hasValue :QuantityKindNomenclature ;  &#10;&#32;&#32;&#32;&#32;owl:onProperty skos:inScheme .</code></pre>|
|[Section top](#minorfail-outcome-number-141)|Pointer|<pre lang="Turtle"><code>:Region owl:sameAs :Region .</code></pre>|
|[Section top](#minorfail-outcome-number-141)|Pointer|<pre lang="Turtle"><code>:hasQuantityKind a owl:ObjectProperty ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;has quantity kind&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:comment &#34;Links a property to its quantity kind&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:domain &lowbar;:n896d559a5e6e4d28b8667be2bff11409b1,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#60;http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#Quality>,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:Thing,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;:Property ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy :feature&lowbar;of&lowbar;interest ;  &#10;&#32;&#32;&#32;&#32;rdfs:range &lowbar;:n896d559a5e6e4d28b8667be2bff11409b2,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&lowbar;:n896d559a5e6e4d28b8667be2bff11409b3,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;qudt:QuantityKind,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#60;http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#Region>,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:Thing,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;skos:Concept,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;:QuantityKind ;  &#10;&#32;&#32;&#32;&#32;rdfs:subPropertyOf :hasQuantityKind ;  &#10;&#32;&#32;&#32;&#32;owl:equivalentProperty :hasQuantityKind ;  &#10;&#32;&#32;&#32;&#32;owl:sameAs :hasQuantityKind ;  &#10;&#32;&#32;&#32;&#32;skos:example &#34;A space area property to the property kind &#92;&#34;area&#92;&#34;.&#34;@en .  &#10;&lowbar;:n896d559a5e6e4d28b8667be2bff11409b4 rdf:first skos:Concept ;  &#10;&#32;&#32;&#32;&#32;rdf:rest ( &lowbar;:n896d559a5e6e4d28b8667be2bff11409b2 ) .  &#10;&lowbar;:n896d559a5e6e4d28b8667be2bff11409b6 rdf:first :CheckMethod ;  &#10;&#32;&#32;&#32;&#32;rdf:rest () .  &#10;&lowbar;:n896d559a5e6e4d28b8667be2bff11409b7 rdf:first :Property ;  &#10;&#32;&#32;&#32;&#32;rdf:rest &lowbar;:n896d559a5e6e4d28b8667be2bff11409b6 .  &#10;&lowbar;:n896d559a5e6e4d28b8667be2bff11409b8 rdf:first :FeatureOfInterest ;  &#10;&#32;&#32;&#32;&#32;rdf:rest &lowbar;:n896d559a5e6e4d28b8667be2bff11409b7 .  &#10;&lowbar;:n896d559a5e6e4d28b8667be2bff11409b3 rdfs:subClassOf &lowbar;:n896d559a5e6e4d28b8667be2bff11409b2,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&lowbar;:n896d559a5e6e4d28b8667be2bff11409b3,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;qudt:QuantityKind,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#60;http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#Region>,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:Thing,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;skos:Concept,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;:QuantityKind ;  &#10;&#32;&#32;&#32;&#32;owl:equivalentClass :QuantityKind ;  &#10;&#32;&#32;&#32;&#32;owl:intersectionOf &lowbar;:n896d559a5e6e4d28b8667be2bff11409b4 .  &#10;&lowbar;:n896d559a5e6e4d28b8667be2bff11409b1 a owl:Class ;  &#10;&#32;&#32;&#32;&#32;rdfs:subClassOf &lowbar;:n896d559a5e6e4d28b8667be2bff11409b1,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:Thing ;  &#10;&#32;&#32;&#32;&#32;owl:equivalentClass &lowbar;:n896d559a5e6e4d28b8667be2bff11409b1 ;  &#10;&#32;&#32;&#32;&#32;owl:unionOf &lowbar;:n896d559a5e6e4d28b8667be2bff11409b8 .  &#10;&lowbar;:n896d559a5e6e4d28b8667be2bff11409b2 a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;owl:hasValue :QuantityKindNomenclature ;  &#10;&#32;&#32;&#32;&#32;owl:onProperty skos:inScheme .</code></pre>|
|[Section top](#minorfail-outcome-number-141)|Pointer|<pre lang="Turtle"><code>:QuantityKind a owl:Class ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy &#60;http://qudt.org/2.1/schema/qudt> ;  &#10;&#32;&#32;&#32;&#32;rdfs:subClassOf :QuantityKind,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:Thing ;  &#10;&#32;&#32;&#32;&#32;owl:equivalentClass :QuantityKind ;  &#10;&#32;&#32;&#32;&#32;owl:sameAs :QuantityKind .</code></pre>|
|[Section top](#minorfail-outcome-number-141)|Pointer|<pre lang="Turtle"><code>:forAdministrativeArea a owl:ObjectProperty ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;for administrative area&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:comment &#34;&#34;&#34;The administrative area for which something applies.&#92;r  &#10;A se...&#34;&#34;&#34; ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy :administrative&lowbar;areas ;  &#10;&#32;&#32;&#32;&#32;rdfs:range &lowbar;:n681404b6ac9d4be98dbda3bff634b19ab1,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&lowbar;:n681404b6ac9d4be98dbda3bff634b19ab2,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&lowbar;:n681404b6ac9d4be98dbda3bff634b19ab3,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#60;http://data.europa.eu/eli/ontology#AdministrativeArea>,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:Thing,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;skos:Concept,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;:AdministrativeArea ;  &#10;&#32;&#32;&#32;&#32;rdfs:subPropertyOf :forAdministrativeArea ;  &#10;&#32;&#32;&#32;&#32;owl:equivalentProperty :forAdministrativeArea ;  &#10;&#32;&#32;&#32;&#32;owl:sameAs :forAdministrativeArea .  &#10;&lowbar;:n681404b6ac9d4be98dbda3bff634b19ab4 rdf:first skos:Concept ;  &#10;&#32;&#32;&#32;&#32;rdf:rest ( &lowbar;:n681404b6ac9d4be98dbda3bff634b19ab2 ) .  &#10;&lowbar;:n681404b6ac9d4be98dbda3bff634b19ab6 rdf:first :AdministrativeArea ;  &#10;&#32;&#32;&#32;&#32;rdf:rest () .  &#10;&lowbar;:n681404b6ac9d4be98dbda3bff634b19ab7 rdf:first &#60;https://schema.org/Place> ;  &#10;&#32;&#32;&#32;&#32;rdf:rest &lowbar;:n681404b6ac9d4be98dbda3bff634b19ab6 .  &#10;&lowbar;:n681404b6ac9d4be98dbda3bff634b19ab3 rdfs:subClassOf &lowbar;:n681404b6ac9d4be98dbda3bff634b19ab1,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&lowbar;:n681404b6ac9d4be98dbda3bff634b19ab2,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&lowbar;:n681404b6ac9d4be98dbda3bff634b19ab3,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#60;http://data.europa.eu/eli/ontology#AdministrativeArea>,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:Thing,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;skos:Concept,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;:AdministrativeArea ;  &#10;&#32;&#32;&#32;&#32;owl:equivalentClass &#60;http://data.europa.eu/eli/ontology#AdministrativeArea>,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;:AdministrativeArea ;  &#10;&#32;&#32;&#32;&#32;owl:intersectionOf &lowbar;:n681404b6ac9d4be98dbda3bff634b19ab4 .  &#10;&lowbar;:n681404b6ac9d4be98dbda3bff634b19ab2 a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;owl:hasValue :AdministrativeAreaNomenclature ;  &#10;&#32;&#32;&#32;&#32;owl:onProperty skos:inScheme .  &#10;&lowbar;:n681404b6ac9d4be98dbda3bff634b19ab1 a owl:Class ;  &#10;&#32;&#32;&#32;&#32;rdfs:subClassOf &lowbar;:n681404b6ac9d4be98dbda3bff634b19ab1,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:Thing ;  &#10;&#32;&#32;&#32;&#32;owl:equivalentClass &lowbar;:n681404b6ac9d4be98dbda3bff634b19ab1 ;  &#10;&#32;&#32;&#32;&#32;owl:unionOf &lowbar;:n681404b6ac9d4be98dbda3bff634b19ab7 .</code></pre>|
|[Section top](#minorfail-outcome-number-141)|Pointer|<pre lang="Turtle"><code>:forAdministrativeArea a owl:ObjectProperty ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;for administrative area&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:comment &#34;&#34;&#34;The administrative area for which something applies.&#92;r  &#10;A se...&#34;&#34;&#34; ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy :administrative&lowbar;areas ;  &#10;&#32;&#32;&#32;&#32;rdfs:range &lowbar;:n11f92bded8a14ebbbda471a8d8f4b4adb1,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&lowbar;:n11f92bded8a14ebbbda471a8d8f4b4adb2,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&lowbar;:n11f92bded8a14ebbbda471a8d8f4b4adb3,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#60;http://data.europa.eu/eli/ontology#AdministrativeArea>,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:Thing,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;skos:Concept,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;:AdministrativeArea ;  &#10;&#32;&#32;&#32;&#32;rdfs:subPropertyOf :forAdministrativeArea ;  &#10;&#32;&#32;&#32;&#32;owl:equivalentProperty :forAdministrativeArea ;  &#10;&#32;&#32;&#32;&#32;owl:sameAs :forAdministrativeArea .  &#10;&lowbar;:n11f92bded8a14ebbbda471a8d8f4b4adb4 rdf:first skos:Concept ;  &#10;&#32;&#32;&#32;&#32;rdf:rest ( &lowbar;:n11f92bded8a14ebbbda471a8d8f4b4adb2 ) .  &#10;&lowbar;:n11f92bded8a14ebbbda471a8d8f4b4adb6 rdf:first :AdministrativeArea ;  &#10;&#32;&#32;&#32;&#32;rdf:rest () .  &#10;&lowbar;:n11f92bded8a14ebbbda471a8d8f4b4adb7 rdf:first &#60;https://schema.org/Place> ;  &#10;&#32;&#32;&#32;&#32;rdf:rest &lowbar;:n11f92bded8a14ebbbda471a8d8f4b4adb6 .  &#10;&lowbar;:n11f92bded8a14ebbbda471a8d8f4b4adb3 rdfs:subClassOf &lowbar;:n11f92bded8a14ebbbda471a8d8f4b4adb1,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&lowbar;:n11f92bded8a14ebbbda471a8d8f4b4adb2,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&lowbar;:n11f92bded8a14ebbbda471a8d8f4b4adb3,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#60;http://data.europa.eu/eli/ontology#AdministrativeArea>,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:Thing,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;skos:Concept,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;:AdministrativeArea ;  &#10;&#32;&#32;&#32;&#32;owl:equivalentClass &#60;http://data.europa.eu/eli/ontology#AdministrativeArea>,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;:AdministrativeArea ;  &#10;&#32;&#32;&#32;&#32;owl:intersectionOf &lowbar;:n11f92bded8a14ebbbda471a8d8f4b4adb4 .  &#10;&lowbar;:n11f92bded8a14ebbbda471a8d8f4b4adb2 a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;owl:hasValue :AdministrativeAreaNomenclature ;  &#10;&#32;&#32;&#32;&#32;owl:onProperty skos:inScheme .  &#10;&lowbar;:n11f92bded8a14ebbbda471a8d8f4b4adb1 a owl:Class ;  &#10;&#32;&#32;&#32;&#32;rdfs:subClassOf &lowbar;:n11f92bded8a14ebbbda471a8d8f4b4adb1,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:Thing ;  &#10;&#32;&#32;&#32;&#32;owl:equivalentClass &lowbar;:n11f92bded8a14ebbbda471a8d8f4b4adb1 ;  &#10;&#32;&#32;&#32;&#32;owl:unionOf &lowbar;:n11f92bded8a14ebbbda471a8d8f4b4adb7 .</code></pre>|
|[Section top](#minorfail-outcome-number-141)|Pointer|<pre lang="Turtle"><code>:AdministrativeArea rdfs:subClassOf &lowbar;:n77be1b7c43464bd8892ae5d5178b1e23b1,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&lowbar;:n77be1b7c43464bd8892ae5d5178b1e23b2,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&lowbar;:n77be1b7c43464bd8892ae5d5178b1e23b3,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;:AdministrativeArea,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:Thing,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;skos:Concept,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;aec3po:AdministrativeArea ;  &#10;&#32;&#32;&#32;&#32;owl:equivalentClass &lowbar;:n77be1b7c43464bd8892ae5d5178b1e23b3,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;aec3po:AdministrativeArea ;  &#10;&#32;&#32;&#32;&#32;owl:sameAs :AdministrativeArea .  &#10;&lowbar;:n77be1b7c43464bd8892ae5d5178b1e23b4 rdf:first skos:Concept ;  &#10;&#32;&#32;&#32;&#32;rdf:rest ( &lowbar;:n77be1b7c43464bd8892ae5d5178b1e23b2 ) .  &#10;&lowbar;:n77be1b7c43464bd8892ae5d5178b1e23b6 rdf:first aec3po:AdministrativeArea ;  &#10;&#32;&#32;&#32;&#32;rdf:rest () .  &#10;&lowbar;:n77be1b7c43464bd8892ae5d5178b1e23b7 rdf:first &#60;https://schema.org/Place> ;  &#10;&#32;&#32;&#32;&#32;rdf:rest &lowbar;:n77be1b7c43464bd8892ae5d5178b1e23b6 .  &#10;&lowbar;:n77be1b7c43464bd8892ae5d5178b1e23b2 a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;owl:hasValue aec3po:AdministrativeAreaNomenclature ;  &#10;&#32;&#32;&#32;&#32;owl:onProperty skos:inScheme .  &#10;&lowbar;:n77be1b7c43464bd8892ae5d5178b1e23b3 rdfs:subClassOf &lowbar;:n77be1b7c43464bd8892ae5d5178b1e23b1,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&lowbar;:n77be1b7c43464bd8892ae5d5178b1e23b2,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&lowbar;:n77be1b7c43464bd8892ae5d5178b1e23b3,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;:AdministrativeArea,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:Thing,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;skos:Concept,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;aec3po:AdministrativeArea ;  &#10;&#32;&#32;&#32;&#32;owl:equivalentClass :AdministrativeArea,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;aec3po:AdministrativeArea ;  &#10;&#32;&#32;&#32;&#32;owl:intersectionOf &lowbar;:n77be1b7c43464bd8892ae5d5178b1e23b4 .  &#10;&lowbar;:n77be1b7c43464bd8892ae5d5178b1e23b1 a owl:Class ;  &#10;&#32;&#32;&#32;&#32;rdfs:subClassOf &lowbar;:n77be1b7c43464bd8892ae5d5178b1e23b1,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:Thing ;  &#10;&#32;&#32;&#32;&#32;owl:equivalentClass &lowbar;:n77be1b7c43464bd8892ae5d5178b1e23b1 ;  &#10;&#32;&#32;&#32;&#32;owl:unionOf &lowbar;:n77be1b7c43464bd8892ae5d5178b1e23b7 .</code></pre>|
|[Section top](#minorfail-outcome-number-141)|Pointer|<pre lang="Turtle"><code>:forBuildingStructure a owl:ObjectProperty ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;for building structure&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:comment &#34;The building structure for which a specific check, verifier,...&#34; ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy :building&lowbar;structure ;  &#10;&#32;&#32;&#32;&#32;rdfs:range &lowbar;:n14a9e23ac9714c8eb6c0b0cda57aa004b1,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&lowbar;:n14a9e23ac9714c8eb6c0b0cda57aa004b2,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:Thing,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;skos:Concept,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;:BuildingStructure,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;:Design ;  &#10;&#32;&#32;&#32;&#32;rdfs:subPropertyOf :forBuildingStructure,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;:forDesign ;  &#10;&#32;&#32;&#32;&#32;owl:equivalentProperty :forBuildingStructure .  &#10;&lowbar;:n14a9e23ac9714c8eb6c0b0cda57aa004b3 rdf:first skos:Concept ;  &#10;&#32;&#32;&#32;&#32;rdf:rest ( &lowbar;:n14a9e23ac9714c8eb6c0b0cda57aa004b1 ) .  &#10;&lowbar;:n14a9e23ac9714c8eb6c0b0cda57aa004b2 rdfs:subClassOf &lowbar;:n14a9e23ac9714c8eb6c0b0cda57aa004b1,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&lowbar;:n14a9e23ac9714c8eb6c0b0cda57aa004b2,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:Thing,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;skos:Concept,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;:BuildingStructure,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;:Design ;  &#10;&#32;&#32;&#32;&#32;owl:equivalentClass :BuildingStructure ;  &#10;&#32;&#32;&#32;&#32;owl:intersectionOf &lowbar;:n14a9e23ac9714c8eb6c0b0cda57aa004b3 .  &#10;&lowbar;:n14a9e23ac9714c8eb6c0b0cda57aa004b1 a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;owl:hasValue :BuildingStructureNomenclature ;  &#10;&#32;&#32;&#32;&#32;owl:onProperty skos:inScheme .</code></pre>|
|[Section top](#minorfail-outcome-number-141)|Pointer|<pre lang="Turtle"><code>:hasBuildingStructure a owl:FunctionalProperty,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:ObjectProperty ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;has building structure&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:comment &#34;The building structure design of a feature of interest or a ...&#34; ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy :building&lowbar;structure ;  &#10;&#32;&#32;&#32;&#32;rdfs:range &lowbar;:n81437594fa424d248157d84ae225eebbb1,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&lowbar;:n81437594fa424d248157d84ae225eebbb2,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:Thing,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;skos:Concept,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;:BuildingStructure,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;:Design ;  &#10;&#32;&#32;&#32;&#32;rdfs:subPropertyOf :hasBuildingStructure,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;:hasDesign ;  &#10;&#32;&#32;&#32;&#32;owl:equivalentProperty :hasBuildingStructure .  &#10;&lowbar;:n81437594fa424d248157d84ae225eebbb3 rdf:first skos:Concept ;  &#10;&#32;&#32;&#32;&#32;rdf:rest ( &lowbar;:n81437594fa424d248157d84ae225eebbb1 ) .  &#10;&lowbar;:n81437594fa424d248157d84ae225eebbb2 rdfs:subClassOf &lowbar;:n81437594fa424d248157d84ae225eebbb1,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&lowbar;:n81437594fa424d248157d84ae225eebbb2,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:Thing,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;skos:Concept,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;:BuildingStructure,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;:Design ;  &#10;&#32;&#32;&#32;&#32;owl:equivalentClass :BuildingStructure ;  &#10;&#32;&#32;&#32;&#32;owl:intersectionOf &lowbar;:n81437594fa424d248157d84ae225eebbb3 .  &#10;&lowbar;:n81437594fa424d248157d84ae225eebbb1 a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;owl:hasValue :BuildingStructureNomenclature ;  &#10;&#32;&#32;&#32;&#32;owl:onProperty skos:inScheme .</code></pre>|
|[Section top](#minorfail-outcome-number-141)|Pointer|<pre lang="Turtle"><code>:forBuildingUsage a owl:ObjectProperty ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;for building usage&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:comment &#34;The building usage for which a specific check, verifier, or ...&#34; ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy :building&lowbar;usage ;  &#10;&#32;&#32;&#32;&#32;rdfs:range &lowbar;:ne7c1868d1a5146ecaa02334db5bee19ab1,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&lowbar;:ne7c1868d1a5146ecaa02334db5bee19ab2,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:Thing,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;skos:Concept,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;:BuildingUsage,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;:Design ;  &#10;&#32;&#32;&#32;&#32;rdfs:subPropertyOf :forBuildingUsage,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;:forDesign ;  &#10;&#32;&#32;&#32;&#32;owl:equivalentProperty :forBuildingUsage .  &#10;&lowbar;:ne7c1868d1a5146ecaa02334db5bee19ab3 rdf:first skos:Concept ;  &#10;&#32;&#32;&#32;&#32;rdf:rest ( &lowbar;:ne7c1868d1a5146ecaa02334db5bee19ab1 ) .  &#10;&lowbar;:ne7c1868d1a5146ecaa02334db5bee19ab2 rdfs:subClassOf &lowbar;:ne7c1868d1a5146ecaa02334db5bee19ab1,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&lowbar;:ne7c1868d1a5146ecaa02334db5bee19ab2,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:Thing,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;skos:Concept,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;:BuildingUsage,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;:Design ;  &#10;&#32;&#32;&#32;&#32;owl:equivalentClass :BuildingUsage ;  &#10;&#32;&#32;&#32;&#32;owl:intersectionOf &lowbar;:ne7c1868d1a5146ecaa02334db5bee19ab3 .  &#10;&lowbar;:ne7c1868d1a5146ecaa02334db5bee19ab1 a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;owl:hasValue :BuildingUsageNomenclature ;  &#10;&#32;&#32;&#32;&#32;owl:onProperty skos:inScheme .</code></pre>|
|[Section top](#minorfail-outcome-number-141)|Pointer|<pre lang="Turtle"><code>:hasBuildingUsage a owl:FunctionalProperty,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:ObjectProperty ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;has building usage&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:comment &#34;The building usage design of a feature of interest or a prop...&#34; ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy :building&lowbar;usage ;  &#10;&#32;&#32;&#32;&#32;rdfs:range &lowbar;:n8092a74dfc2342e594ab6466b42c1c61b1,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&lowbar;:n8092a74dfc2342e594ab6466b42c1c61b2,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:Thing,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;skos:Concept,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;:BuildingUsage,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;:Design ;  &#10;&#32;&#32;&#32;&#32;rdfs:subPropertyOf :hasBuildingUsage,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;:hasDesign ;  &#10;&#32;&#32;&#32;&#32;owl:equivalentProperty :hasBuildingUsage .  &#10;&lowbar;:n8092a74dfc2342e594ab6466b42c1c61b3 rdf:first skos:Concept ;  &#10;&#32;&#32;&#32;&#32;rdf:rest ( &lowbar;:n8092a74dfc2342e594ab6466b42c1c61b1 ) .  &#10;&lowbar;:n8092a74dfc2342e594ab6466b42c1c61b2 rdfs:subClassOf &lowbar;:n8092a74dfc2342e594ab6466b42c1c61b1,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&lowbar;:n8092a74dfc2342e594ab6466b42c1c61b2,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:Thing,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;skos:Concept,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;:BuildingUsage,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;:Design ;  &#10;&#32;&#32;&#32;&#32;owl:equivalentClass :BuildingUsage ;  &#10;&#32;&#32;&#32;&#32;owl:intersectionOf &lowbar;:n8092a74dfc2342e594ab6466b42c1c61b3 .  &#10;&lowbar;:n8092a74dfc2342e594ab6466b42c1c61b1 a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;owl:hasValue :BuildingUsageNomenclature ;  &#10;&#32;&#32;&#32;&#32;owl:onProperty skos:inScheme .</code></pre>|
|[Section top](#minorfail-outcome-number-141)|Pointer|<pre lang="Turtle"><code>:hasDiscipline a owl:ObjectProperty ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;has discipline&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:comment &#34;Links an entity (procedure, statement, verifier, ...) to the...&#34; ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy :discipline ;  &#10;&#32;&#32;&#32;&#32;rdfs:range &lowbar;:nb474520bfd554a18a178f4d893706fd5b1,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&lowbar;:nb474520bfd554a18a178f4d893706fd5b2,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:Thing,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;skos:Concept,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;:Discipline ;  &#10;&#32;&#32;&#32;&#32;rdfs:subPropertyOf :hasDiscipline ;  &#10;&#32;&#32;&#32;&#32;owl:equivalentProperty :hasDiscipline .  &#10;&lowbar;:nb474520bfd554a18a178f4d893706fd5b3 rdf:first skos:Concept ;  &#10;&#32;&#32;&#32;&#32;rdf:rest ( &lowbar;:nb474520bfd554a18a178f4d893706fd5b1 ) .  &#10;&lowbar;:nb474520bfd554a18a178f4d893706fd5b2 rdfs:subClassOf &lowbar;:nb474520bfd554a18a178f4d893706fd5b1,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&lowbar;:nb474520bfd554a18a178f4d893706fd5b2,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:Thing,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;skos:Concept,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;:Discipline ;  &#10;&#32;&#32;&#32;&#32;owl:equivalentClass :Discipline ;  &#10;&#32;&#32;&#32;&#32;owl:intersectionOf &lowbar;:nb474520bfd554a18a178f4d893706fd5b3 .  &#10;&lowbar;:nb474520bfd554a18a178f4d893706fd5b1 a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;owl:hasValue :DisciplineNomenclature ;  &#10;&#32;&#32;&#32;&#32;owl:onProperty skos:inScheme .</code></pre>|
|[Section top](#minorfail-outcome-number-141)|Pointer|<pre lang="Turtle"><code>:hasPermittingStage a owl:ObjectProperty ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;has permitting stage&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:comment &#34;Links an entity to the permitting stage this entity pertains&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy :permitting&lowbar;stage ;  &#10;&#32;&#32;&#32;&#32;rdfs:range &lowbar;:n63e583c25cb344d79968ce6f8a77ef8eb1,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&lowbar;:n63e583c25cb344d79968ce6f8a77ef8eb2,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:Thing,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;skos:Concept,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;:PermittingStage ;  &#10;&#32;&#32;&#32;&#32;rdfs:subPropertyOf &#60;https://w3id.org/digitalconstruction/0.5/Lifecycle#hasStage>,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;:hasPermittingStage ;  &#10;&#32;&#32;&#32;&#32;owl:equivalentProperty &#60;https://w3id.org/digitalconstruction/0.5/Lifecycle#hasStage>,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;:hasPermittingStage .  &#10;&lowbar;:n63e583c25cb344d79968ce6f8a77ef8eb3 rdf:first skos:Concept ;  &#10;&#32;&#32;&#32;&#32;rdf:rest ( &lowbar;:n63e583c25cb344d79968ce6f8a77ef8eb1 ) .  &#10;&lowbar;:n63e583c25cb344d79968ce6f8a77ef8eb2 rdfs:subClassOf &lowbar;:n63e583c25cb344d79968ce6f8a77ef8eb1,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&lowbar;:n63e583c25cb344d79968ce6f8a77ef8eb2,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:Thing,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;skos:Concept,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;:PermittingStage ;  &#10;&#32;&#32;&#32;&#32;owl:equivalentClass :PermittingStage ;  &#10;&#32;&#32;&#32;&#32;owl:intersectionOf &lowbar;:n63e583c25cb344d79968ce6f8a77ef8eb3 .  &#10;&lowbar;:n63e583c25cb344d79968ce6f8a77ef8eb1 a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;owl:hasValue :PermittingStageNomenclature ;  &#10;&#32;&#32;&#32;&#32;owl:onProperty skos:inScheme .</code></pre>|
|[Section top](#minorfail-outcome-number-141)|Pointer|http://www.w3.org/2004/02/skos/core#Concept|
|[Section top](#minorfail-outcome-number-141)|Pointer|http://purl.org/dc/elements/1.1/format|

***
### MinorFail Outcome number 142

[Jump to summary definition](#summary-MinorFail-142)	|	[Previous MinorFail outcome](#minorfail-outcome-number-141)	|	[Next MinorFail outcome](#minorfail-outcome-number-143)

:exclamation:MinorFail outcome
#### Subject detail
|Name|all-fragments|
|----|----|
|Title|All the fragments from branch main that are syntaxically correct as well as their recursive imports|
|Composition|- [Module aec3po](https://github.com/Accord-Project/aec3po/blob/main/src/aec3po.ttl)<br/>- [Module checking&lowbar;act](https://github.com/Accord-Project/aec3po/blob/main/src/checking_act.ttl)<br/>- [Module check&lowbar;method](https://github.com/Accord-Project/aec3po/blob/main/src/check_method.ttl)<br/>- [Module compliance&lowbar;verification&lowbar;report](https://github.com/Accord-Project/aec3po/blob/main/src/compliance_verification_report.ttl)<br/>- [Module data&lowbar;requirement](https://github.com/Accord-Project/aec3po/blob/main/src/data_requirement.ttl)<br/>- [Module document](https://github.com/Accord-Project/aec3po/blob/main/src/document.ttl)<br/>- [Module evidence](https://github.com/Accord-Project/aec3po/blob/main/src/evidence.ttl)<br/>- [Module feature&lowbar;of&lowbar;interest](https://github.com/Accord-Project/aec3po/blob/main/src/feature_of_interest.ttl)<br/>- [Module legal&lowbar;verifier](https://github.com/Accord-Project/aec3po/blob/main/src/legal_verifier.ttl)<br/>- [Module model](https://github.com/Accord-Project/aec3po/blob/main/src/model.ttl)<br/>- [Module rase&lowbar;statement](https://github.com/Accord-Project/aec3po/blob/main/src/rase_statement.ttl)<br/>- [Module statement](https://github.com/Accord-Project/aec3po/blob/main/src/statement.ttl)<br/>- [Module table](https://github.com/Accord-Project/aec3po/blob/main/src/table.ttl)<br/>- [Module vocabularies/administrative&lowbar;areas](https://github.com/Accord-Project/aec3po/blob/main/src/vocabularies/administrative_areas.ttl)<br/>- [Module vocabularies/building&lowbar;structure](https://github.com/Accord-Project/aec3po/blob/main/src/vocabularies/building_structure.ttl)<br/>- [Module vocabularies/building&lowbar;usage](https://github.com/Accord-Project/aec3po/blob/main/src/vocabularies/building_usage.ttl)<br/>- [Module vocabularies/check&lowbar;method&lowbar;comparators](https://github.com/Accord-Project/aec3po/blob/main/src/vocabularies/check_method_comparators.ttl)<br/>- [Module vocabularies/check&lowbar;method&lowbar;operators](https://github.com/Accord-Project/aec3po/blob/main/src/vocabularies/check_method_operators.ttl)<br/>- [Module vocabularies/disciplines](https://github.com/Accord-Project/aec3po/blob/main/src/vocabularies/disciplines.ttl)<br/>- [Module vocabularies/permitting&lowbar;stages](https://github.com/Accord-Project/aec3po/blob/main/src/vocabularies/permitting_stages.ttl)<br/>- [Module vocabularies/quantity&lowbar;kinds](https://github.com/Accord-Project/aec3po/blob/main/src/vocabularies/quantity_kinds.ttl)<br/>- [Module vocabularies/&lowbar;shape](https://github.com/Accord-Project/aec3po/blob/main/src/vocabularies/_shape.ttl)|

#### Criterion detail
|Identifier|[labeled-terms](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#labeled-terms)|
|----|----|
|Title|Term labeling test|
|Description|A test case from the Best Practices tests checking if all the terms of the subject have a rdfs:label property pointing to a literal in English|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-142)|Identifier|`not-labeled-term`|
|[Section top](#minorfail-outcome-number-142)|Title|Terms not labeled|
|[Section top](#minorfail-outcome-number-142)|Description|The following terms have no rdfs:label to define it in natural language|
|[Section top](#minorfail-outcome-number-142)|Pointer|<pre lang="Turtle"><code>:hasFormat a owl:ObjectProperty ;  &#10;&#32;&#32;&#32;&#32;rdfs:comment &#34;Defines the format of an evidence, which is of type dct:form...&#34; ;  &#10;&#32;&#32;&#32;&#32;rdfs:domain :Statement ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy :evidence ;  &#10;&#32;&#32;&#32;&#32;rdfs:range dc:format ;  &#10;&#32;&#32;&#32;&#32;skos:example &#34;an image, a drawing or a model can be an evidence.&#34;@en .</code></pre>|
|[Section top](#minorfail-outcome-number-142)|Pointer|<pre lang="Turtle"><code>:England a owl:NamedIndividual,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;skos:Concept,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;:AdministrativeArea ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy :administrative&lowbar;areas ;  &#10;&#32;&#32;&#32;&#32;skos:definition &#34;England&#34;@en ;  &#10;&#32;&#32;&#32;&#32;skos:inScheme :AdministrativeAreaNomenclature ;  &#10;&#32;&#32;&#32;&#32;skos:prefLabel &#34;England&#34;@en ;  &#10;&#32;&#32;&#32;&#32;skos:topConceptOf :AdministrativeAreaNomenclature .</code></pre>|
|[Section top](#minorfail-outcome-number-142)|Pointer|<pre lang="Turtle"><code>:Estonia a owl:NamedIndividual,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;skos:Concept,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;:AdministrativeArea ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy :administrative&lowbar;areas ;  &#10;&#32;&#32;&#32;&#32;skos:definition &#34;Estonia&#34;@en ;  &#10;&#32;&#32;&#32;&#32;skos:inScheme :AdministrativeAreaNomenclature ;  &#10;&#32;&#32;&#32;&#32;skos:prefLabel &#34;Estonia&#34;@en ;  &#10;&#32;&#32;&#32;&#32;skos:topConceptOf :AdministrativeAreaNomenclature .</code></pre>|
|[Section top](#minorfail-outcome-number-142)|Pointer|<pre lang="Turtle"><code>:Finland a owl:NamedIndividual,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;skos:Concept,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;:AdministrativeArea ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy :administrative&lowbar;areas ;  &#10;&#32;&#32;&#32;&#32;skos:definition &#34;Finland&#34;@en ;  &#10;&#32;&#32;&#32;&#32;skos:inScheme :AdministrativeAreaNomenclature ;  &#10;&#32;&#32;&#32;&#32;skos:prefLabel &#34;Finland&#34;@en ;  &#10;&#32;&#32;&#32;&#32;skos:topConceptOf :AdministrativeAreaNomenclature .</code></pre>|
|[Section top](#minorfail-outcome-number-142)|Pointer|<pre lang="Turtle"><code>:France a owl:NamedIndividual,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;skos:Concept,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;:AdministrativeArea ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy :administrative&lowbar;areas ;  &#10;&#32;&#32;&#32;&#32;skos:definition &#34;France&#34;@en ;  &#10;&#32;&#32;&#32;&#32;skos:inScheme :AdministrativeAreaNomenclature ;  &#10;&#32;&#32;&#32;&#32;skos:prefLabel &#34;France&#34;@en ;  &#10;&#32;&#32;&#32;&#32;skos:topConceptOf :AdministrativeAreaNomenclature .</code></pre>|
|[Section top](#minorfail-outcome-number-142)|Pointer|<pre lang="Turtle"><code>:Germany a owl:NamedIndividual,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;skos:Concept,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;:AdministrativeArea ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy :administrative&lowbar;areas ;  &#10;&#32;&#32;&#32;&#32;skos:definition &#34;Germany&#34;@en ;  &#10;&#32;&#32;&#32;&#32;skos:inScheme :AdministrativeAreaNomenclature ;  &#10;&#32;&#32;&#32;&#32;skos:prefLabel &#34;Germany&#34;@en ;  &#10;&#32;&#32;&#32;&#32;skos:topConceptOf :AdministrativeAreaNomenclature .</code></pre>|
|[Section top](#minorfail-outcome-number-142)|Pointer|<pre lang="Turtle"><code>:Italy a owl:NamedIndividual,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;skos:Concept,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;:AdministrativeArea ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy :administrative&lowbar;areas ;  &#10;&#32;&#32;&#32;&#32;skos:definition &#34;Italy&#34;@en ;  &#10;&#32;&#32;&#32;&#32;skos:inScheme :AdministrativeAreaNomenclature ;  &#10;&#32;&#32;&#32;&#32;skos:prefLabel &#34;Italy&#34;@en ;  &#10;&#32;&#32;&#32;&#32;skos:topConceptOf :AdministrativeAreaNomenclature .</code></pre>|
|[Section top](#minorfail-outcome-number-142)|Pointer|<pre lang="Turtle"><code>:Spain a owl:NamedIndividual,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;skos:Concept,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;:AdministrativeArea ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy :administrative&lowbar;areas ;  &#10;&#32;&#32;&#32;&#32;skos:definition &#34;Spain&#34;@en ;  &#10;&#32;&#32;&#32;&#32;skos:inScheme :AdministrativeAreaNomenclature ;  &#10;&#32;&#32;&#32;&#32;skos:prefLabel &#34;Spain&#34;@en ;  &#10;&#32;&#32;&#32;&#32;skos:topConceptOf :AdministrativeAreaNomenclature .</code></pre>|
|[Section top](#minorfail-outcome-number-142)|Pointer|<pre lang="Turtle"><code>:BuildingStructure-steel a owl:NamedIndividual,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;skos:Concept,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;:BuildingStructure ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy :building&lowbar;structure ;  &#10;&#32;&#32;&#32;&#32;skos:definition &#34;Building has steel structure.&#34;@en ;  &#10;&#32;&#32;&#32;&#32;skos:inScheme :BuildingStructureNomenclature ;  &#10;&#32;&#32;&#32;&#32;skos:prefLabel &#34;steel&#34;@en ;  &#10;&#32;&#32;&#32;&#32;skos:topConceptOf :BuildingStructureNomenclature .</code></pre>|
|[Section top](#minorfail-outcome-number-142)|Pointer|<pre lang="Turtle"><code>:BuildingStructure-timber a owl:NamedIndividual,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;skos:Concept,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;:BuildingStructure ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy :building&lowbar;structure ;  &#10;&#32;&#32;&#32;&#32;skos:definition &#34;Building has timber structure.&#34;@en ;  &#10;&#32;&#32;&#32;&#32;skos:inScheme :BuildingStructureNomenclature ;  &#10;&#32;&#32;&#32;&#32;skos:prefLabel &#34;timber&#34;@en ;  &#10;&#32;&#32;&#32;&#32;skos:topConceptOf :BuildingStructureNomenclature .</code></pre>|
|[Section top](#minorfail-outcome-number-142)|Pointer|<pre lang="Turtle"><code>:BuildingUsage-commercial a owl:NamedIndividual,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;skos:Concept,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;:BuildingUsage ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy :building&lowbar;usage ;  &#10;&#32;&#32;&#32;&#32;skos:definition &#34;Building has commercial usage.&#34;@en ;  &#10;&#32;&#32;&#32;&#32;skos:inScheme :BuildingUsageNomenclature ;  &#10;&#32;&#32;&#32;&#32;skos:prefLabel &#34;commercial&#34;@en ;  &#10;&#32;&#32;&#32;&#32;skos:topConceptOf :BuildingUsageNomenclature .</code></pre>|
|[Section top](#minorfail-outcome-number-142)|Pointer|<pre lang="Turtle"><code>:BuildingUsage-residential a owl:NamedIndividual,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;skos:Concept,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;:BuildingUsage ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy :building&lowbar;usage ;  &#10;&#32;&#32;&#32;&#32;skos:definition &#34;Building has residential usage.&#34;@en ;  &#10;&#32;&#32;&#32;&#32;skos:inScheme :BuildingUsageNomenclature ;  &#10;&#32;&#32;&#32;&#32;skos:prefLabel &#34;residential&#34;@en ;  &#10;&#32;&#32;&#32;&#32;skos:topConceptOf :BuildingUsageNomenclature .</code></pre>|
|[Section top](#minorfail-outcome-number-142)|Pointer|<pre lang="Turtle"><code>:BuildingUsage-cultural a owl:NamedIndividual,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;skos:Concept,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;:BuildingUsage ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy :building&lowbar;usage ;  &#10;&#32;&#32;&#32;&#32;skos:definition &#34;Building has cultural usage.&#34;@en ;  &#10;&#32;&#32;&#32;&#32;skos:inScheme :BuildingUsageNomenclature ;  &#10;&#32;&#32;&#32;&#32;skos:prefLabel &#34;cultural&#34;@en ;  &#10;&#32;&#32;&#32;&#32;skos:topConceptOf :BuildingUsageNomenclature .</code></pre>|
|[Section top](#minorfail-outcome-number-142)|Pointer|<pre lang="Turtle"><code>:CheckMethodcomparator-logicalAND a owl:NamedIndividual,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;skos:Concept,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;:CheckMethodComparator ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy :check&lowbar;method&lowbar;comparators ;  &#10;&#32;&#32;&#32;&#32;skos:definition &#34;logical AND comparator.&#34;@en ;  &#10;&#32;&#32;&#32;&#32;skos:inScheme :CheckMethodComparatorNomenclature ;  &#10;&#32;&#32;&#32;&#32;skos:prefLabel &#34;logicalAND&#34;@en ;  &#10;&#32;&#32;&#32;&#32;skos:topConceptOf :CheckMethodComparatorNomenclature .</code></pre>|
|[Section top](#minorfail-outcome-number-142)|Pointer|<pre lang="Turtle"><code>:CheckMethodcomparator-eq a owl:NamedIndividual,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;skos:Concept,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;:CheckMethodcomparator ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy :check&lowbar;method&lowbar;comparators ;  &#10;&#32;&#32;&#32;&#32;skos:definition &#34;equal-to comparator.&#34;@en ;  &#10;&#32;&#32;&#32;&#32;skos:inScheme :CheckMethodComparatorNomenclature ;  &#10;&#32;&#32;&#32;&#32;skos:prefLabel &#34;equal-to&#34;@en ;  &#10;&#32;&#32;&#32;&#32;skos:topConceptOf :CheckMethodComparatorNomenclature .</code></pre>|
|[Section top](#minorfail-outcome-number-142)|Pointer|<pre lang="Turtle"><code>:CheckMethodComparator-neq a owl:NamedIndividual,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;skos:Concept,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;:CheckMethodComparator ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy :check&lowbar;method&lowbar;comparators ;  &#10;&#32;&#32;&#32;&#32;skos:definition &#34;not equal-to comparator.&#34;@en ;  &#10;&#32;&#32;&#32;&#32;skos:inScheme :CheckMethodComparatorNomenclature ;  &#10;&#32;&#32;&#32;&#32;skos:prefLabel &#34;not equal-to&#34;@en ;  &#10;&#32;&#32;&#32;&#32;skos:topConceptOf :CheckMethodComparatorNomenclature .</code></pre>|
|[Section top](#minorfail-outcome-number-142)|Pointer|<pre lang="Turtle"><code>:CheckMethodComparator-lt a owl:NamedIndividual,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;skos:Concept,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;:CheckMethodComparator ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy :check&lowbar;method&lowbar;comparators ;  &#10;&#32;&#32;&#32;&#32;skos:definition &#34;less-than comparator.&#34;@en ;  &#10;&#32;&#32;&#32;&#32;skos:inScheme :CheckMethodComparatorNomenclature ;  &#10;&#32;&#32;&#32;&#32;skos:prefLabel &#34;less than&#34;@en ;  &#10;&#32;&#32;&#32;&#32;skos:topConceptOf :CheckMethodComparatorNomenclature .</code></pre>|
|[Section top](#minorfail-outcome-number-142)|Pointer|<pre lang="Turtle"><code>:CheckMethodComparator-le a owl:NamedIndividual,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;skos:Concept,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;:CheckMethodComparator ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy :check&lowbar;method&lowbar;comparators ;  &#10;&#32;&#32;&#32;&#32;skos:definition &#34;less-equal comparator.&#34;@en ;  &#10;&#32;&#32;&#32;&#32;skos:inScheme :CheckMethodComparatorNomenclature ;  &#10;&#32;&#32;&#32;&#32;skos:prefLabel &#34;less equal&#34;@en ;  &#10;&#32;&#32;&#32;&#32;skos:topConceptOf :CheckMethodComparatorNomenclature .</code></pre>|
|[Section top](#minorfail-outcome-number-142)|Pointer|<pre lang="Turtle"><code>:CheckMethodComparator-gt a owl:NamedIndividual,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;skos:Concept,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;:CheckMethodComparator ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy :check&lowbar;method&lowbar;comparators ;  &#10;&#32;&#32;&#32;&#32;skos:definition &#34;greater-than comparator.&#34;@en ;  &#10;&#32;&#32;&#32;&#32;skos:inScheme :CheckMethodComparatorNomenclature ;  &#10;&#32;&#32;&#32;&#32;skos:prefLabel &#34;greater than&#34;@en ;  &#10;&#32;&#32;&#32;&#32;skos:topConceptOf :CheckMethodComparatorNomenclature .</code></pre>|
|[Section top](#minorfail-outcome-number-142)|Pointer|<pre lang="Turtle"><code>:CheckMethodComparator-ge a owl:NamedIndividual,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;skos:Concept,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;:CheckMethodComparator ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy :check&lowbar;method&lowbar;comparators ;  &#10;&#32;&#32;&#32;&#32;skos:definition &#34;greater-equal comparator.&#34;@en ;  &#10;&#32;&#32;&#32;&#32;skos:inScheme :CheckMethodComparatorNomenclature ;  &#10;&#32;&#32;&#32;&#32;skos:prefLabel &#34;greater equal&#34;@en ;  &#10;&#32;&#32;&#32;&#32;skos:topConceptOf :CheckMethodComparatorNomenclature .</code></pre>|
|[Section top](#minorfail-outcome-number-142)|Pointer|<pre lang="Turtle"><code>:CheckMethodComparator-logicalOR a owl:NamedIndividual,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;skos:Concept,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;:CheckMethodComparator ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy :check&lowbar;method&lowbar;comparators ;  &#10;&#32;&#32;&#32;&#32;skos:definition &#34;logical OR comparator.&#34;@en ;  &#10;&#32;&#32;&#32;&#32;skos:inScheme :CheckMethodComparatorNomenclature ;  &#10;&#32;&#32;&#32;&#32;skos:prefLabel &#34;logicalOR&#34;@en ;  &#10;&#32;&#32;&#32;&#32;skos:topConceptOf :CheckMethodComparatorNomenclature .</code></pre>|
|[Section top](#minorfail-outcome-number-142)|Pointer|<pre lang="Turtle"><code>:CheckMethodOperator-exists a owl:NamedIndividual,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;skos:Concept,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;:CheckMethodOperator ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy :check&lowbar;method&lowbar;operators ;  &#10;&#32;&#32;&#32;&#32;skos:definition &#34;exists operator.&#34;@en ;  &#10;&#32;&#32;&#32;&#32;skos:inScheme :CheckMethodOperatorNomenclature ;  &#10;&#32;&#32;&#32;&#32;skos:prefLabel &#34;exists&#34;@en ;  &#10;&#32;&#32;&#32;&#32;skos:topConceptOf :CheckMethodOperatorNomenclature .</code></pre>|
|[Section top](#minorfail-outcome-number-142)|Pointer|<pre lang="Turtle"><code>:CheckMethodOperator-notExists a owl:NamedIndividual,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;skos:Concept,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;:CheckMethodOperator ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy :check&lowbar;method&lowbar;operators ;  &#10;&#32;&#32;&#32;&#32;skos:definition &#34;not exists operator.&#34;@en ;  &#10;&#32;&#32;&#32;&#32;skos:inScheme :CheckMethodOperatorNomenclature ;  &#10;&#32;&#32;&#32;&#32;skos:prefLabel &#34;not exists&#34;@en ;  &#10;&#32;&#32;&#32;&#32;skos:topConceptOf :CheckMethodOperatorNomenclature .</code></pre>|
|[Section top](#minorfail-outcome-number-142)|Pointer|<pre lang="Turtle"><code>:CheckMethodOperator-forall a owl:NamedIndividual,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;skos:Concept,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;:CheckMethodOperator ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy :check&lowbar;method&lowbar;operators ;  &#10;&#32;&#32;&#32;&#32;skos:definition &#34;forall operator.&#34;@en ;  &#10;&#32;&#32;&#32;&#32;skos:inScheme :CheckMethodOperatorNomenclature ;  &#10;&#32;&#32;&#32;&#32;skos:prefLabel &#34;forall&#34;@en ;  &#10;&#32;&#32;&#32;&#32;skos:topConceptOf :CheckMethodOperatorNomenclature .</code></pre>|
|[Section top](#minorfail-outcome-number-142)|Pointer|<pre lang="Turtle"><code>:CheckMethodOperator-addition a owl:NamedIndividual,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;skos:Concept,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;:CheckMethodOperator ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy :check&lowbar;method&lowbar;operators ;  &#10;&#32;&#32;&#32;&#32;skos:definition &#34;addition operator.&#34;@en ;  &#10;&#32;&#32;&#32;&#32;skos:inScheme :CheckMethodOperatorNomenclature ;  &#10;&#32;&#32;&#32;&#32;skos:prefLabel &#34;addition&#34;@en ;  &#10;&#32;&#32;&#32;&#32;skos:topConceptOf :CheckMethodOperatorNomenclature .</code></pre>|
|[Section top](#minorfail-outcome-number-142)|Pointer|<pre lang="Turtle"><code>:CheckMethodOperator-multiplication a owl:NamedIndividual,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;skos:Concept,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;:CheckMethodOperator ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy :check&lowbar;method&lowbar;operators ;  &#10;&#32;&#32;&#32;&#32;skos:definition &#34;multiplication Operator.&#34;@en ;  &#10;&#32;&#32;&#32;&#32;skos:inScheme :CheckMethodOperatorNomenclature ;  &#10;&#32;&#32;&#32;&#32;skos:prefLabel &#34;multiplication&#34;@en ;  &#10;&#32;&#32;&#32;&#32;skos:topConceptOf :CheckMethodOperatorNomenclature .</code></pre>|
|[Section top](#minorfail-outcome-number-142)|Pointer|<pre lang="Turtle"><code>:CheckMethodOperator-subtraction a owl:NamedIndividual,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;skos:Concept,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;:CheckMethodOperator ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy :check&lowbar;method&lowbar;operators ;  &#10;&#32;&#32;&#32;&#32;skos:definition &#34;subtraction operator.&#34;@en ;  &#10;&#32;&#32;&#32;&#32;skos:inScheme :CheckMethodOperatorNomenclature ;  &#10;&#32;&#32;&#32;&#32;skos:prefLabel &#34;subtraction&#34;@en ;  &#10;&#32;&#32;&#32;&#32;skos:topConceptOf :CheckMethodOperatorNomenclature .</code></pre>|
|[Section top](#minorfail-outcome-number-142)|Pointer|<pre lang="Turtle"><code>:CheckMethodOperator-division a owl:NamedIndividual,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;skos:Concept,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;:CheckMethodOperator ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy :check&lowbar;method&lowbar;operators ;  &#10;&#32;&#32;&#32;&#32;skos:definition &#34;division Operator.&#34;@en ;  &#10;&#32;&#32;&#32;&#32;skos:inScheme :CheckMethodOperatorNomenclature ;  &#10;&#32;&#32;&#32;&#32;skos:prefLabel &#34;division&#34;@en ;  &#10;&#32;&#32;&#32;&#32;skos:topConceptOf :CheckMethodOperatorNomenclature .</code></pre>|
|[Section top](#minorfail-outcome-number-142)|Pointer|<pre lang="Turtle"><code>:Discipline-architecture a owl:NamedIndividual,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;skos:Concept,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;:Discipline ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy :discipline ;  &#10;&#32;&#32;&#32;&#32;skos:definition &#34;The Architecture discipline.&#34;@en ;  &#10;&#32;&#32;&#32;&#32;skos:inScheme :DisciplineNomenclature ;  &#10;&#32;&#32;&#32;&#32;skos:prefLabel &#34;architecture&#34;@en ;  &#10;&#32;&#32;&#32;&#32;skos:topConceptOf :DisciplineNomenclature .</code></pre>|
|[Section top](#minorfail-outcome-number-142)|Pointer|<pre lang="Turtle"><code>:Discipline-buildingServices a owl:NamedIndividual,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;skos:Concept,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;:Discipline ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy :discipline ;  &#10;&#32;&#32;&#32;&#32;skos:definition &#34;The Building Services discipline.&#34;@en ;  &#10;&#32;&#32;&#32;&#32;skos:inScheme :DisciplineNomenclature ;  &#10;&#32;&#32;&#32;&#32;skos:prefLabel &#34;building services&#34;@en ;  &#10;&#32;&#32;&#32;&#32;skos:topConceptOf :DisciplineNomenclature .</code></pre>|
|[Section top](#minorfail-outcome-number-142)|Pointer|<pre lang="Turtle"><code>:Discipline-construction a owl:NamedIndividual,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;skos:Concept,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;:Discipline ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy :discipline ;  &#10;&#32;&#32;&#32;&#32;skos:definition &#34;The Construction discipline.&#34;@en ;  &#10;&#32;&#32;&#32;&#32;skos:inScheme :DisciplineNomenclature ;  &#10;&#32;&#32;&#32;&#32;skos:prefLabel &#34;construction&#34;@en ;  &#10;&#32;&#32;&#32;&#32;skos:topConceptOf :DisciplineNomenclature .</code></pre>|
|[Section top](#minorfail-outcome-number-142)|Pointer|<pre lang="Turtle"><code>:Discipline-planning a owl:NamedIndividual,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;skos:Concept,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;:Discipline ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy :discipline ;  &#10;&#32;&#32;&#32;&#32;skos:definition &#34;The Planning discipline.&#34;@en ;  &#10;&#32;&#32;&#32;&#32;skos:inScheme :DisciplineNomenclature ;  &#10;&#32;&#32;&#32;&#32;skos:prefLabel &#34;planning&#34;@en ;  &#10;&#32;&#32;&#32;&#32;skos:topConceptOf :DisciplineNomenclature .</code></pre>|
|[Section top](#minorfail-outcome-number-142)|Pointer|<pre lang="Turtle"><code>:Discipline-structuralEngineering a owl:NamedIndividual,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;skos:Concept,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;:Discipline ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy :discipline ;  &#10;&#32;&#32;&#32;&#32;skos:definition &#34;The Structural Engineering discipline.&#34;@en ;  &#10;&#32;&#32;&#32;&#32;skos:inScheme :DisciplineNomenclature ;  &#10;&#32;&#32;&#32;&#32;skos:prefLabel &#34;structural engineering&#34;@en ;  &#10;&#32;&#32;&#32;&#32;skos:topConceptOf :DisciplineNomenclature .</code></pre>|
|[Section top](#minorfail-outcome-number-142)|Pointer|<pre lang="Turtle"><code>:UK&lowbar;Building&lowbar;Control&lowbar;Submission a owl:NamedIndividual,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;skos:Concept,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;:PermittingStage ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy :permitting&lowbar;stage ;  &#10;&#32;&#32;&#32;&#32;skos:definition &#34;The UK Building Control Submission permitting stage.&#34;@en ;  &#10;&#32;&#32;&#32;&#32;skos:inScheme :PermittingStageNomenclature ;  &#10;&#32;&#32;&#32;&#32;skos:prefLabel &#34;building control submission&#34;@en ;  &#10;&#32;&#32;&#32;&#32;skos:topConceptOf :PermittingStageNomenclature ;  &#10;&#32;&#32;&#32;&#32;:forAdministrativeArea :England .</code></pre>|
|[Section top](#minorfail-outcome-number-142)|Pointer|<pre lang="Turtle"><code>:UK&lowbar;Planning&lowbar;Permission a owl:NamedIndividual,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;skos:Concept,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;:PermittingStage ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy :permitting&lowbar;stage ;  &#10;&#32;&#32;&#32;&#32;skos:definition &#34;The UK Planning Permission permitting stage.&#34;@en ;  &#10;&#32;&#32;&#32;&#32;skos:inScheme :PermittingStageNomenclature ;  &#10;&#32;&#32;&#32;&#32;skos:prefLabel &#34;planning permission&#34;@en ;  &#10;&#32;&#32;&#32;&#32;skos:topConceptOf :PermittingStageNomenclature ;  &#10;&#32;&#32;&#32;&#32;:forAdministrativeArea :England .</code></pre>|
|[Section top](#minorfail-outcome-number-142)|Pointer|<pre lang="Turtle"><code>:QuantityKind a owl:Class ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy &#60;http://qudt.org/2.1/schema/qudt> .</code></pre>|
|[Section top](#minorfail-outcome-number-142)|Pointer|<pre lang="Turtle"><code>:ModularRoomHeight a owl:NamedIndividual,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;skos:Concept,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;:QuantityKind ;  &#10;&#32;&#32;&#32;&#32;qudt:applicableUnit &#60;http://qudt.org/vocab/unit/CentiM>,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#60;http://qudt.org/vocab/unit/IN>,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#60;http://qudt.org/vocab/unit/M>,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#60;http://qudt.org/vocab/unit/MilliIN>,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#60;http://qudt.org/vocab/unit/MilliM> ;  &#10;&#32;&#32;&#32;&#32;qudt:hasDimensionVector &#60;http://qudt.org/vocab/dimensionvector/A0E0L1I0M0H0T0D0> ;  &#10;&#32;&#32;&#32;&#32;qudt:normativeReference &#34;https://www.iso.org/obp/ui/#iso:std:iso:6707:-1:ed-6:v1:en:t...&#34; ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy :quantity&lowbar;kinds ;  &#10;&#32;&#32;&#32;&#32;skos:broader &#60;http://qudt.org/vocab/quantitykind/Length> ;  &#10;&#32;&#32;&#32;&#32;skos:definition &#34;vertical distance within one storey between the modular plan...&#34; ;  &#10;&#32;&#32;&#32;&#32;skos:prefLabel &#34;modular room height&#34;@en .</code></pre>|
|[Section top](#minorfail-outcome-number-142)|Pointer|<pre lang="Turtle"><code>:WidthOfAngledCorridor a owl:NamedIndividual,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;skos:Concept,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;:QuantityKind ;  &#10;&#32;&#32;&#32;&#32;qudt:applicableUnit &#60;http://qudt.org/vocab/unit/CentiM>,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#60;http://qudt.org/vocab/unit/IN>,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#60;http://qudt.org/vocab/unit/M>,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#60;http://qudt.org/vocab/unit/MilliIN>,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#60;http://qudt.org/vocab/unit/MilliM> ;  &#10;&#32;&#32;&#32;&#32;qudt:hasDimensionVector &#60;http://qudt.org/vocab/dimensionvector/A0E0L1I0M0H0T0D0> ;  &#10;&#32;&#32;&#32;&#32;qudt:normativeReference &#34;https://www.iso.org/obp/ui/#iso:std:iso:7176:-5:ed-2:v1:en:t...&#34; ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy :quantity&lowbar;kinds ;  &#10;&#32;&#32;&#32;&#32;skos:broader &#60;http://qudt.org/vocab/quantitykind/Length> ;  &#10;&#32;&#32;&#32;&#32;skos:definition &#34;width of a corridor with a right angled turn in which the wh...&#34; ;  &#10;&#32;&#32;&#32;&#32;skos:prefLabel &#34;width of angled corridor&#34;@en .</code></pre>|
|[Section top](#minorfail-outcome-number-142)|Pointer|<pre lang="Turtle"><code>:CompressiveForce a owl:NamedIndividual,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;skos:Concept,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;:QuantityKind ;  &#10;&#32;&#32;&#32;&#32;qudt:hasDimensionVector &#60;http://qudt.org/vocab/dimensionvector/A0E0L1I0M1H0T-2D0> ;  &#10;&#32;&#32;&#32;&#32;qudt:symbol &#34;C&#34; ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy :quantity&lowbar;kinds ;  &#10;&#32;&#32;&#32;&#32;skos:broader &#60;http://qudt.org/vocab/quantitykind/Force> ;  &#10;&#32;&#32;&#32;&#32;skos:definition &#34;Force tending to reduce the size of a body.&#34; ;  &#10;&#32;&#32;&#32;&#32;skos:prefLabel &#34;compressive force&#34;@en .</code></pre>|
|[Section top](#minorfail-outcome-number-142)|Pointer|<pre lang="Turtle"><code>:PartialSafetyFactor a owl:NamedIndividual,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;skos:Concept,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;:QuantityKind ;  &#10;&#32;&#32;&#32;&#32;qudt:applicableUnit &#60;http://qudt.org/vocab/unit/UNITLESS> ;  &#10;&#32;&#32;&#32;&#32;qudt:hasDimensionVector &#60;http://qudt.org/vocab/dimensionvector/A0E0L0I0M0H0T0D0> ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy :quantity&lowbar;kinds ;  &#10;&#32;&#32;&#32;&#32;skos:definition &#34;Also written γM, the partial safety factor for resistance.&#34;@en ;  &#10;&#32;&#32;&#32;&#32;skos:prefLabel &#34;Partial Safety Factor&#34;@en .</code></pre>|
|[Section top](#minorfail-outcome-number-142)|Pointer|<pre lang="Turtle"><code>:PartialSafetyFactor0 a owl:NamedIndividual,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;skos:Concept,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;:QuantityKind ;  &#10;&#32;&#32;&#32;&#32;qudt:applicableUnit &#60;http://qudt.org/vocab/unit/UNITLESS> ;  &#10;&#32;&#32;&#32;&#32;qudt:hasDimensionVector &#60;http://qudt.org/vocab/dimensionvector/A0E0L0I0M0H0T0D0> ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy :quantity&lowbar;kinds ;  &#10;&#32;&#32;&#32;&#32;skos:broader :PartialSafetyFactor ;  &#10;&#32;&#32;&#32;&#32;skos:definition &#34;Also written γM0, the partial safety factor for resistance r...&#34; ;  &#10;&#32;&#32;&#32;&#32;skos:prefLabel &#34;Partial Safety Factor&#34;@en .</code></pre>|
|[Section top](#minorfail-outcome-number-142)|Pointer|<pre lang="Turtle"><code>:AxialCompressionStress a owl:NamedIndividual,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;skos:Concept,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;:QuantityKind ;  &#10;&#32;&#32;&#32;&#32;qudt:hasDimensionVector &#60;http://qudt.org/vocab/dimensionvector/A0E0L1I0M-1H0T-2D0> ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy :quantity&lowbar;kinds ;  &#10;&#32;&#32;&#32;&#32;skos:definition &#34;also known as fc0k&#34; ;  &#10;&#32;&#32;&#32;&#32;skos:prefLabel &#34;axial compression stress&#34;@en .</code></pre>|
|[Section top](#minorfail-outcome-number-142)|Pointer|<pre lang="Turtle"><code>:ModificationFactorKmod a owl:NamedIndividual,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;skos:Concept,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;:QuantityKind ;  &#10;&#32;&#32;&#32;&#32;qudt:applicableUnit &#60;http://qudt.org/vocab/unit/UNITLESS> ;  &#10;&#32;&#32;&#32;&#32;qudt:hasDimensionVector &#60;http://qudt.org/vocab/dimensionvector/A0E0L0I0M0H0T0D0> ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy :quantity&lowbar;kinds ;  &#10;&#32;&#32;&#32;&#32;skos:definition &#34;Modification Factor to take into account the duration of loa...&#34; ;  &#10;&#32;&#32;&#32;&#32;skos:prefLabel &#34;Modification Factor Kmod&#34;@en .</code></pre>|

***
### MinorFail Outcome number 143

[Jump to summary definition](#summary-MinorFail-143)	|	[Previous MinorFail outcome](#minorfail-outcome-number-142)	|	[Next MinorFail outcome](#minorfail-outcome-number-144)

:exclamation:MinorFail outcome
#### Subject detail
|Name|all-fragments|
|----|----|
|Title|All the fragments from branch main that are syntaxically correct as well as their recursive imports|
|Composition|- [Module aec3po](https://github.com/Accord-Project/aec3po/blob/main/src/aec3po.ttl)<br/>- [Module checking&lowbar;act](https://github.com/Accord-Project/aec3po/blob/main/src/checking_act.ttl)<br/>- [Module check&lowbar;method](https://github.com/Accord-Project/aec3po/blob/main/src/check_method.ttl)<br/>- [Module compliance&lowbar;verification&lowbar;report](https://github.com/Accord-Project/aec3po/blob/main/src/compliance_verification_report.ttl)<br/>- [Module data&lowbar;requirement](https://github.com/Accord-Project/aec3po/blob/main/src/data_requirement.ttl)<br/>- [Module document](https://github.com/Accord-Project/aec3po/blob/main/src/document.ttl)<br/>- [Module evidence](https://github.com/Accord-Project/aec3po/blob/main/src/evidence.ttl)<br/>- [Module feature&lowbar;of&lowbar;interest](https://github.com/Accord-Project/aec3po/blob/main/src/feature_of_interest.ttl)<br/>- [Module legal&lowbar;verifier](https://github.com/Accord-Project/aec3po/blob/main/src/legal_verifier.ttl)<br/>- [Module model](https://github.com/Accord-Project/aec3po/blob/main/src/model.ttl)<br/>- [Module rase&lowbar;statement](https://github.com/Accord-Project/aec3po/blob/main/src/rase_statement.ttl)<br/>- [Module statement](https://github.com/Accord-Project/aec3po/blob/main/src/statement.ttl)<br/>- [Module table](https://github.com/Accord-Project/aec3po/blob/main/src/table.ttl)<br/>- [Module vocabularies/administrative&lowbar;areas](https://github.com/Accord-Project/aec3po/blob/main/src/vocabularies/administrative_areas.ttl)<br/>- [Module vocabularies/building&lowbar;structure](https://github.com/Accord-Project/aec3po/blob/main/src/vocabularies/building_structure.ttl)<br/>- [Module vocabularies/building&lowbar;usage](https://github.com/Accord-Project/aec3po/blob/main/src/vocabularies/building_usage.ttl)<br/>- [Module vocabularies/check&lowbar;method&lowbar;comparators](https://github.com/Accord-Project/aec3po/blob/main/src/vocabularies/check_method_comparators.ttl)<br/>- [Module vocabularies/check&lowbar;method&lowbar;operators](https://github.com/Accord-Project/aec3po/blob/main/src/vocabularies/check_method_operators.ttl)<br/>- [Module vocabularies/disciplines](https://github.com/Accord-Project/aec3po/blob/main/src/vocabularies/disciplines.ttl)<br/>- [Module vocabularies/permitting&lowbar;stages](https://github.com/Accord-Project/aec3po/blob/main/src/vocabularies/permitting_stages.ttl)<br/>- [Module vocabularies/quantity&lowbar;kinds](https://github.com/Accord-Project/aec3po/blob/main/src/vocabularies/quantity_kinds.ttl)<br/>- [Module vocabularies/&lowbar;shape](https://github.com/Accord-Project/aec3po/blob/main/src/vocabularies/_shape.ttl)|

#### Criterion detail
|Identifier|[profile-compatibility](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#profile-compatibility)|
|----|----|
|Title|Profile compatibility test|
|Description|A test meant to check whether the test subject is compatible with a profile or not, and if it is not, why.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-143)|Identifier|`owl-rl-profile-error`|
|[Section top](#minorfail-outcome-number-143)|Title|OWL RL Profile incompatible|
|[Section top](#minorfail-outcome-number-143)|Description|Class Expression not supported with owl:equivalentClass or owl:intersectionOf|
|[Section top](#minorfail-outcome-number-143)|Pointer|<pre lang="Turtle"><code>&#91;] a owl:Class ;  &#10;&#32;&#32;&#32;&#32;owl:intersectionOf ( aec3po:CheckMethod &#91; a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:allValuesFrom &#91; a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:allValuesFrom aec3po:FeatureOfInterest ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:onProperty &#91; owl:inverseOf aec3po:forDesign ] ] ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:onProperty aec3po:forDesign ] ) .</code></pre>|

***
### MinorFail Outcome number 144

[Jump to summary definition](#summary-MinorFail-144)	|	[Previous MinorFail outcome](#minorfail-outcome-number-143)	|	[Next MinorFail outcome](#minorfail-outcome-number-145)

:exclamation:MinorFail outcome
#### Subject detail
|Name|all-fragments|
|----|----|
|Title|All the fragments from branch main that are syntaxically correct as well as their recursive imports|
|Composition|- [Module aec3po](https://github.com/Accord-Project/aec3po/blob/main/src/aec3po.ttl)<br/>- [Module checking&lowbar;act](https://github.com/Accord-Project/aec3po/blob/main/src/checking_act.ttl)<br/>- [Module check&lowbar;method](https://github.com/Accord-Project/aec3po/blob/main/src/check_method.ttl)<br/>- [Module compliance&lowbar;verification&lowbar;report](https://github.com/Accord-Project/aec3po/blob/main/src/compliance_verification_report.ttl)<br/>- [Module data&lowbar;requirement](https://github.com/Accord-Project/aec3po/blob/main/src/data_requirement.ttl)<br/>- [Module document](https://github.com/Accord-Project/aec3po/blob/main/src/document.ttl)<br/>- [Module evidence](https://github.com/Accord-Project/aec3po/blob/main/src/evidence.ttl)<br/>- [Module feature&lowbar;of&lowbar;interest](https://github.com/Accord-Project/aec3po/blob/main/src/feature_of_interest.ttl)<br/>- [Module legal&lowbar;verifier](https://github.com/Accord-Project/aec3po/blob/main/src/legal_verifier.ttl)<br/>- [Module model](https://github.com/Accord-Project/aec3po/blob/main/src/model.ttl)<br/>- [Module rase&lowbar;statement](https://github.com/Accord-Project/aec3po/blob/main/src/rase_statement.ttl)<br/>- [Module statement](https://github.com/Accord-Project/aec3po/blob/main/src/statement.ttl)<br/>- [Module table](https://github.com/Accord-Project/aec3po/blob/main/src/table.ttl)<br/>- [Module vocabularies/administrative&lowbar;areas](https://github.com/Accord-Project/aec3po/blob/main/src/vocabularies/administrative_areas.ttl)<br/>- [Module vocabularies/building&lowbar;structure](https://github.com/Accord-Project/aec3po/blob/main/src/vocabularies/building_structure.ttl)<br/>- [Module vocabularies/building&lowbar;usage](https://github.com/Accord-Project/aec3po/blob/main/src/vocabularies/building_usage.ttl)<br/>- [Module vocabularies/check&lowbar;method&lowbar;comparators](https://github.com/Accord-Project/aec3po/blob/main/src/vocabularies/check_method_comparators.ttl)<br/>- [Module vocabularies/check&lowbar;method&lowbar;operators](https://github.com/Accord-Project/aec3po/blob/main/src/vocabularies/check_method_operators.ttl)<br/>- [Module vocabularies/disciplines](https://github.com/Accord-Project/aec3po/blob/main/src/vocabularies/disciplines.ttl)<br/>- [Module vocabularies/permitting&lowbar;stages](https://github.com/Accord-Project/aec3po/blob/main/src/vocabularies/permitting_stages.ttl)<br/>- [Module vocabularies/quantity&lowbar;kinds](https://github.com/Accord-Project/aec3po/blob/main/src/vocabularies/quantity_kinds.ttl)<br/>- [Module vocabularies/&lowbar;shape](https://github.com/Accord-Project/aec3po/blob/main/src/vocabularies/_shape.ttl)|

#### Criterion detail
|Identifier|[profile-compatibility](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#profile-compatibility)|
|----|----|
|Title|Profile compatibility test|
|Description|A test meant to check whether the test subject is compatible with a profile or not, and if it is not, why.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-144)|Identifier|`owl-rl-profile-error`|
|[Section top](#minorfail-outcome-number-144)|Title|OWL RL Profile incompatible|
|[Section top](#minorfail-outcome-number-144)|Description|Statement not supported in an Equivalent Class Expression|
|[Section top](#minorfail-outcome-number-144)|Pointer|<pre lang="Turtle"><code>&#91;] a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;owl:allValuesFrom &#91; a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:allValuesFrom aec3po:FeatureOfInterest ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:onProperty &#91; owl:inverseOf aec3po:forDesign ] ] ;  &#10;&#32;&#32;&#32;&#32;owl:onProperty aec3po:forDesign .</code></pre>|

***
### MinorFail Outcome number 145

[Jump to summary definition](#summary-MinorFail-145)	|	[Previous MinorFail outcome](#minorfail-outcome-number-144)	|	[Next MinorFail outcome](#minorfail-outcome-number-146)

:exclamation:MinorFail outcome
#### Subject detail
|Name|all-fragments|
|----|----|
|Title|All the fragments from branch main that are syntaxically correct as well as their recursive imports|
|Composition|- [Module aec3po](https://github.com/Accord-Project/aec3po/blob/main/src/aec3po.ttl)<br/>- [Module checking&lowbar;act](https://github.com/Accord-Project/aec3po/blob/main/src/checking_act.ttl)<br/>- [Module check&lowbar;method](https://github.com/Accord-Project/aec3po/blob/main/src/check_method.ttl)<br/>- [Module compliance&lowbar;verification&lowbar;report](https://github.com/Accord-Project/aec3po/blob/main/src/compliance_verification_report.ttl)<br/>- [Module data&lowbar;requirement](https://github.com/Accord-Project/aec3po/blob/main/src/data_requirement.ttl)<br/>- [Module document](https://github.com/Accord-Project/aec3po/blob/main/src/document.ttl)<br/>- [Module evidence](https://github.com/Accord-Project/aec3po/blob/main/src/evidence.ttl)<br/>- [Module feature&lowbar;of&lowbar;interest](https://github.com/Accord-Project/aec3po/blob/main/src/feature_of_interest.ttl)<br/>- [Module legal&lowbar;verifier](https://github.com/Accord-Project/aec3po/blob/main/src/legal_verifier.ttl)<br/>- [Module model](https://github.com/Accord-Project/aec3po/blob/main/src/model.ttl)<br/>- [Module rase&lowbar;statement](https://github.com/Accord-Project/aec3po/blob/main/src/rase_statement.ttl)<br/>- [Module statement](https://github.com/Accord-Project/aec3po/blob/main/src/statement.ttl)<br/>- [Module table](https://github.com/Accord-Project/aec3po/blob/main/src/table.ttl)<br/>- [Module vocabularies/administrative&lowbar;areas](https://github.com/Accord-Project/aec3po/blob/main/src/vocabularies/administrative_areas.ttl)<br/>- [Module vocabularies/building&lowbar;structure](https://github.com/Accord-Project/aec3po/blob/main/src/vocabularies/building_structure.ttl)<br/>- [Module vocabularies/building&lowbar;usage](https://github.com/Accord-Project/aec3po/blob/main/src/vocabularies/building_usage.ttl)<br/>- [Module vocabularies/check&lowbar;method&lowbar;comparators](https://github.com/Accord-Project/aec3po/blob/main/src/vocabularies/check_method_comparators.ttl)<br/>- [Module vocabularies/check&lowbar;method&lowbar;operators](https://github.com/Accord-Project/aec3po/blob/main/src/vocabularies/check_method_operators.ttl)<br/>- [Module vocabularies/disciplines](https://github.com/Accord-Project/aec3po/blob/main/src/vocabularies/disciplines.ttl)<br/>- [Module vocabularies/permitting&lowbar;stages](https://github.com/Accord-Project/aec3po/blob/main/src/vocabularies/permitting_stages.ttl)<br/>- [Module vocabularies/quantity&lowbar;kinds](https://github.com/Accord-Project/aec3po/blob/main/src/vocabularies/quantity_kinds.ttl)<br/>- [Module vocabularies/&lowbar;shape](https://github.com/Accord-Project/aec3po/blob/main/src/vocabularies/_shape.ttl)|

#### Criterion detail
|Identifier|[profile-compatibility](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#profile-compatibility)|
|----|----|
|Title|Profile compatibility test|
|Description|A test meant to check whether the test subject is compatible with a profile or not, and if it is not, why.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-145)|Identifier|`owl-rl-profile-error`|
|[Section top](#minorfail-outcome-number-145)|Title|OWL RL Profile incompatible|
|[Section top](#minorfail-outcome-number-145)|Description|Class Expression not supported as object of rdfs:domain or rdfs:range|
|[Section top](#minorfail-outcome-number-145)|Pointer|<pre lang="Turtle"><code>aec3po:caption a owl:DatatypeProperty ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;caption&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:comment &#34;The caption of a table, image, etc. &#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:domain &#91; a owl:Class ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:unionOf ( aec3po:Table aec3po:Image ) ] ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy aec3po:table .</code></pre>|
|[Section top](#minorfail-outcome-number-145)|Pointer|<pre lang="Turtle"><code>aec3po:contains a owl:ObjectProperty ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;Contains&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:comment &#34;A container contains a table and its caption. A table contai...&#34; ;  &#10;&#32;&#32;&#32;&#32;rdfs:domain &#91; a owl:Class ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:unionOf ( aec3po:Table aec3po:Image aec3po:Row aec3po:Column ) ] ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy aec3po:table .</code></pre>|
|[Section top](#minorfail-outcome-number-145)|Pointer|<pre lang="Turtle"><code>aec3po:hasBSSDDTarget a owl:FunctionalProperty,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:ObjectProperty ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;hasBSSDDTarget&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:comment &#34;The target refers to either the name of an object, the name ...&#34; ;  &#10;&#32;&#32;&#32;&#32;rdfs:domain &#91; a owl:Class ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:unionOf ( aec3po:FeatureOfInterest aec3po:Property aec3po:CheckMethod ) ] ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy aec3po:check&lowbar;method .</code></pre>|
|[Section top](#minorfail-outcome-number-145)|Pointer|<pre lang="Turtle"><code>aec3po:hasFirstSubdivision a owl:FunctionalProperty,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:ObjectProperty ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;has first subdivision&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:comment &#34;Links a document part to the first of its subdivision&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:domain &#91; owl:unionOf ( aec3po:Document aec3po:DocumentSubdivision ) ] ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy aec3po:document ;  &#10;&#32;&#32;&#32;&#32;rdfs:range aec3po:DocumentSubdivision ;  &#10;&#32;&#32;&#32;&#32;rdfs:subPropertyOf aec3po:hasSubdivision .</code></pre>|
|[Section top](#minorfail-outcome-number-145)|Pointer|<pre lang="Turtle"><code>aec3po:hasSubdivision a owl:ObjectProperty ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;has subdivision&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:comment &#34;links a document part to some of its subdivision&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:domain &#91; owl:unionOf ( aec3po:Document aec3po:DocumentSubdivision ) ] ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy aec3po:document ;  &#10;&#32;&#32;&#32;&#32;rdfs:range aec3po:DocumentSubdivision ;  &#10;&#32;&#32;&#32;&#32;rdfs:subPropertyOf dc:hasPart .</code></pre>|
|[Section top](#minorfail-outcome-number-145)|Pointer|<pre lang="Turtle"><code>aec3po:hasUnit a owl:FunctionalProperty,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:ObjectProperty ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;hasUnit&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:comment &#34;the hasUnit property is used to link a specific property or ...&#34; ;  &#10;&#32;&#32;&#32;&#32;rdfs:domain &#91; a owl:Class ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:unionOf ( aec3po:FeatureOfInterest aec3po:Property aec3po:CheckMethod ) ] ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy aec3po:check&lowbar;method ;  &#10;&#32;&#32;&#32;&#32;rdfs:range qudt:Unit ;  &#10;&#32;&#32;&#32;&#32;owl:eqivalentProperty qudt:hasValue .</code></pre>|
|[Section top](#minorfail-outcome-number-145)|Pointer|<pre lang="Turtle"><code>aec3po:hasValue a owl:DatatypeProperty,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:FunctionalProperty ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;has value&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:comment &#34;de facto used to link something (anything: property, propert...&#34; ;  &#10;&#32;&#32;&#32;&#32;rdfs:domain &#91; a owl:Class ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:unionOf ( aec3po:FeatureOfInterest aec3po:Property aec3po:CheckMethod ) ] ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy aec3po: ;  &#10;&#32;&#32;&#32;&#32;skos:note &#34;The value of the literal may be a XSD literal (boolean, inte...&#34; .</code></pre>|
|[Section top](#minorfail-outcome-number-145)|Pointer|<pre lang="Turtle"><code>aec3po:isContainedIn a owl:ObjectProperty ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;is contained by&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:comment &#34;A table contains row, columns and other elements.&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy aec3po:table ;  &#10;&#32;&#32;&#32;&#32;rdfs:range &#91; a owl:Class ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:unionOf ( aec3po:Table aec3po:Image aec3po:Row aec3po:Column aec3po:Cell ) ] .</code></pre>|
|[Section top](#minorfail-outcome-number-145)|Pointer|<pre lang="Turtle"><code>aec3po:locationCoverage a owl:ObjectProperty ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;location coverage&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:comment &#34;The spatialCoverage indicates the place(s) or the administra...&#34; ;  &#10;&#32;&#32;&#32;&#32;rdfs:domain &#60;https://schema.org/Model> ;  &#10;&#32;&#32;&#32;&#32;rdfs:range &#91; a owl:Class ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:unionOf ( &#60;https://schema.org/Place> aec3po:AdministrativeArea ) ] ;  &#10;&#32;&#32;&#32;&#32;owl:equivalentProperty &#60;https://schema.org/spatialCoverage> .</code></pre>|

***
### MinorFail Outcome number 146

[Jump to summary definition](#summary-MinorFail-146)	|	[Previous MinorFail outcome](#minorfail-outcome-number-145)	|	[Next MinorFail outcome](#minorfail-outcome-number-147)

:exclamation:MinorFail outcome
#### Subject detail
|Name|all-fragments|
|----|----|
|Title|All the fragments from branch main that are syntaxically correct as well as their recursive imports|
|Composition|- [Module aec3po](https://github.com/Accord-Project/aec3po/blob/main/src/aec3po.ttl)<br/>- [Module checking&lowbar;act](https://github.com/Accord-Project/aec3po/blob/main/src/checking_act.ttl)<br/>- [Module check&lowbar;method](https://github.com/Accord-Project/aec3po/blob/main/src/check_method.ttl)<br/>- [Module compliance&lowbar;verification&lowbar;report](https://github.com/Accord-Project/aec3po/blob/main/src/compliance_verification_report.ttl)<br/>- [Module data&lowbar;requirement](https://github.com/Accord-Project/aec3po/blob/main/src/data_requirement.ttl)<br/>- [Module document](https://github.com/Accord-Project/aec3po/blob/main/src/document.ttl)<br/>- [Module evidence](https://github.com/Accord-Project/aec3po/blob/main/src/evidence.ttl)<br/>- [Module feature&lowbar;of&lowbar;interest](https://github.com/Accord-Project/aec3po/blob/main/src/feature_of_interest.ttl)<br/>- [Module legal&lowbar;verifier](https://github.com/Accord-Project/aec3po/blob/main/src/legal_verifier.ttl)<br/>- [Module model](https://github.com/Accord-Project/aec3po/blob/main/src/model.ttl)<br/>- [Module rase&lowbar;statement](https://github.com/Accord-Project/aec3po/blob/main/src/rase_statement.ttl)<br/>- [Module statement](https://github.com/Accord-Project/aec3po/blob/main/src/statement.ttl)<br/>- [Module table](https://github.com/Accord-Project/aec3po/blob/main/src/table.ttl)<br/>- [Module vocabularies/administrative&lowbar;areas](https://github.com/Accord-Project/aec3po/blob/main/src/vocabularies/administrative_areas.ttl)<br/>- [Module vocabularies/building&lowbar;structure](https://github.com/Accord-Project/aec3po/blob/main/src/vocabularies/building_structure.ttl)<br/>- [Module vocabularies/building&lowbar;usage](https://github.com/Accord-Project/aec3po/blob/main/src/vocabularies/building_usage.ttl)<br/>- [Module vocabularies/check&lowbar;method&lowbar;comparators](https://github.com/Accord-Project/aec3po/blob/main/src/vocabularies/check_method_comparators.ttl)<br/>- [Module vocabularies/check&lowbar;method&lowbar;operators](https://github.com/Accord-Project/aec3po/blob/main/src/vocabularies/check_method_operators.ttl)<br/>- [Module vocabularies/disciplines](https://github.com/Accord-Project/aec3po/blob/main/src/vocabularies/disciplines.ttl)<br/>- [Module vocabularies/permitting&lowbar;stages](https://github.com/Accord-Project/aec3po/blob/main/src/vocabularies/permitting_stages.ttl)<br/>- [Module vocabularies/quantity&lowbar;kinds](https://github.com/Accord-Project/aec3po/blob/main/src/vocabularies/quantity_kinds.ttl)<br/>- [Module vocabularies/&lowbar;shape](https://github.com/Accord-Project/aec3po/blob/main/src/vocabularies/_shape.ttl)|

#### Criterion detail
|Identifier|[profile-compatibility](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#profile-compatibility)|
|----|----|
|Title|Profile compatibility test|
|Description|A test meant to check whether the test subject is compatible with a profile or not, and if it is not, why.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-146)|Identifier|`owl-rl-profile-error`|
|[Section top](#minorfail-outcome-number-146)|Title|OWL RL Profile incompatible|
|[Section top](#minorfail-outcome-number-146)|Description|Class Expression not supported with rdfs:subClassOf|
|[Section top](#minorfail-outcome-number-146)|Pointer|<pre lang="Turtle"><code>aec3po:AndCheckStatement a owl:Class ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;And Check Statement&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:comment &#34;Check verified if and only if all of its sub-checks are veri...&#34; ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy aec3po:statement ;  &#10;&#32;&#32;&#32;&#32;rdfs:subClassOf &#91; a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:onProperty aec3po:hasSubdivision ],  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;aec3po:ChecklistStatement .</code></pre>|
|[Section top](#minorfail-outcome-number-146)|Pointer|<pre lang="Turtle"><code>aec3po:CheckingAct a owl:Class ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;Checking Act&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:comment &#34;Act of checking some entities for something and generating a...&#34; ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy aec3po:checking&lowbar;act ;  &#10;&#32;&#32;&#32;&#32;rdfs:subClassOf &#91; a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:onProperty aec3po:usedMethod ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:someValuesFrom aec3po:CheckMethod ],  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#91; a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:onProperty aec3po:madeBy ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:someValuesFrom aec3po:ProcessVerifier ],  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#91; a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:onProperty aec3po:checked ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:someValuesFrom owl:Thing ],  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#91; a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:onProperty aec3po:hasReport ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:someValuesFrom aec3po:ComplianceVerificationReport ],  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#60;http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#Event> .</code></pre>|
|[Section top](#minorfail-outcome-number-146)|Pointer|<pre lang="Turtle"><code>aec3po:ComplianceVerificationReport a owl:Class ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;Compliance Verification Report&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:comment &#34;Result of a checking act. May be compliant or not.&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy aec3po:compliance&lowbar;verification&lowbar;report ;  &#10;&#32;&#32;&#32;&#32;rdfs:subClassOf &#91; a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:onProperty aec3po:conforms ] .</code></pre>|
|[Section top](#minorfail-outcome-number-146)|Pointer|<pre lang="Turtle"><code>aec3po:NotCheckStatement a owl:Class ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;Not Check Statement&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:comment &#34;Check verified if and only if the sub-check is not verified.&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy aec3po:statement ;  &#10;&#32;&#32;&#32;&#32;rdfs:subClassOf &#91; a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:onProperty aec3po:hasSubdivision ] .</code></pre>|
|[Section top](#minorfail-outcome-number-146)|Pointer|<pre lang="Turtle"><code>aec3po:OrCheckStatement a owl:Class ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;Or Check Statement&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:comment &#34;Check verified if and only if at least one of its sub-checks...&#34; ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy aec3po:statement ;  &#10;&#32;&#32;&#32;&#32;rdfs:subClassOf &#91; a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:onProperty aec3po:hasSubdivision ],  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;aec3po:ChecklistStatement .</code></pre>|
|[Section top](#minorfail-outcome-number-146)|Pointer|<pre lang="Turtle"><code>aec3po:VerificationResult a owl:Class ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;Verification Result&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:comment &#34;Individual verification result of a Compliance Verification ...&#34; ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy aec3po:compliance&lowbar;verification&lowbar;report ;  &#10;&#32;&#32;&#32;&#32;rdfs:subClassOf &#91; a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:onProperty aec3po:verificationFocus ],  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#91; a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:onProperty aec3po:hasSeverity ] .</code></pre>|

***
### MinorFail Outcome number 147

[Jump to summary definition](#summary-MinorFail-147)	|	[Previous MinorFail outcome](#minorfail-outcome-number-146)	|	[Next MinorFail outcome](#minorfail-outcome-number-148)

:exclamation:MinorFail outcome
#### Subject detail
|Name|all-fragments|
|----|----|
|Title|All the fragments from branch main that are syntaxically correct as well as their recursive imports|
|Composition|- [Module aec3po](https://github.com/Accord-Project/aec3po/blob/main/src/aec3po.ttl)<br/>- [Module checking&lowbar;act](https://github.com/Accord-Project/aec3po/blob/main/src/checking_act.ttl)<br/>- [Module check&lowbar;method](https://github.com/Accord-Project/aec3po/blob/main/src/check_method.ttl)<br/>- [Module compliance&lowbar;verification&lowbar;report](https://github.com/Accord-Project/aec3po/blob/main/src/compliance_verification_report.ttl)<br/>- [Module data&lowbar;requirement](https://github.com/Accord-Project/aec3po/blob/main/src/data_requirement.ttl)<br/>- [Module document](https://github.com/Accord-Project/aec3po/blob/main/src/document.ttl)<br/>- [Module evidence](https://github.com/Accord-Project/aec3po/blob/main/src/evidence.ttl)<br/>- [Module feature&lowbar;of&lowbar;interest](https://github.com/Accord-Project/aec3po/blob/main/src/feature_of_interest.ttl)<br/>- [Module legal&lowbar;verifier](https://github.com/Accord-Project/aec3po/blob/main/src/legal_verifier.ttl)<br/>- [Module model](https://github.com/Accord-Project/aec3po/blob/main/src/model.ttl)<br/>- [Module rase&lowbar;statement](https://github.com/Accord-Project/aec3po/blob/main/src/rase_statement.ttl)<br/>- [Module statement](https://github.com/Accord-Project/aec3po/blob/main/src/statement.ttl)<br/>- [Module table](https://github.com/Accord-Project/aec3po/blob/main/src/table.ttl)<br/>- [Module vocabularies/administrative&lowbar;areas](https://github.com/Accord-Project/aec3po/blob/main/src/vocabularies/administrative_areas.ttl)<br/>- [Module vocabularies/building&lowbar;structure](https://github.com/Accord-Project/aec3po/blob/main/src/vocabularies/building_structure.ttl)<br/>- [Module vocabularies/building&lowbar;usage](https://github.com/Accord-Project/aec3po/blob/main/src/vocabularies/building_usage.ttl)<br/>- [Module vocabularies/check&lowbar;method&lowbar;comparators](https://github.com/Accord-Project/aec3po/blob/main/src/vocabularies/check_method_comparators.ttl)<br/>- [Module vocabularies/check&lowbar;method&lowbar;operators](https://github.com/Accord-Project/aec3po/blob/main/src/vocabularies/check_method_operators.ttl)<br/>- [Module vocabularies/disciplines](https://github.com/Accord-Project/aec3po/blob/main/src/vocabularies/disciplines.ttl)<br/>- [Module vocabularies/permitting&lowbar;stages](https://github.com/Accord-Project/aec3po/blob/main/src/vocabularies/permitting_stages.ttl)<br/>- [Module vocabularies/quantity&lowbar;kinds](https://github.com/Accord-Project/aec3po/blob/main/src/vocabularies/quantity_kinds.ttl)<br/>- [Module vocabularies/&lowbar;shape](https://github.com/Accord-Project/aec3po/blob/main/src/vocabularies/_shape.ttl)|

#### Criterion detail
|Identifier|[profile-compatibility](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#profile-compatibility)|
|----|----|
|Title|Profile compatibility test|
|Description|A test meant to check whether the test subject is compatible with a profile or not, and if it is not, why.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-147)|Identifier|`owl-rl-profile-error`|
|[Section top](#minorfail-outcome-number-147)|Title|OWL RL Profile incompatible|
|[Section top](#minorfail-outcome-number-147)|Description|Class Expression not supported with owl:equivalentClass|
|[Section top](#minorfail-outcome-number-147)|Pointer|<pre lang="Turtle"><code>aec3po:ComponentCheckMethod a owl:Class ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;Component Check Method&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:comment &#34;Component check method refers to a process of inspecting and...&#34; ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy aec3po:check&lowbar;method ;  &#10;&#32;&#32;&#32;&#32;rdfs:subClassOf aec3po:CheckMethod ;  &#10;&#32;&#32;&#32;&#32;owl:equivalentClass &#91; a owl:Class ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:intersectionOf ( aec3po:CheckMethod &#91; a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:allValuesFrom &#91; a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:allValuesFrom aec3po:FeatureOfInterest ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:onProperty &#91; owl:inverseOf aec3po:forDesign ] ] ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:onProperty aec3po:forDesign ] ) ] .</code></pre>|

***
### MinorFail Outcome number 148

[Jump to summary definition](#summary-MinorFail-148)	|	[Previous MinorFail outcome](#minorfail-outcome-number-147)	|	[Next MinorFail outcome](#minorfail-outcome-number-149)

:exclamation:MinorFail outcome
#### Subject detail
|Name|all-fragments|
|----|----|
|Title|All the fragments from branch main that are syntaxically correct as well as their recursive imports|
|Composition|- [Module aec3po](https://github.com/Accord-Project/aec3po/blob/main/src/aec3po.ttl)<br/>- [Module checking&lowbar;act](https://github.com/Accord-Project/aec3po/blob/main/src/checking_act.ttl)<br/>- [Module check&lowbar;method](https://github.com/Accord-Project/aec3po/blob/main/src/check_method.ttl)<br/>- [Module compliance&lowbar;verification&lowbar;report](https://github.com/Accord-Project/aec3po/blob/main/src/compliance_verification_report.ttl)<br/>- [Module data&lowbar;requirement](https://github.com/Accord-Project/aec3po/blob/main/src/data_requirement.ttl)<br/>- [Module document](https://github.com/Accord-Project/aec3po/blob/main/src/document.ttl)<br/>- [Module evidence](https://github.com/Accord-Project/aec3po/blob/main/src/evidence.ttl)<br/>- [Module feature&lowbar;of&lowbar;interest](https://github.com/Accord-Project/aec3po/blob/main/src/feature_of_interest.ttl)<br/>- [Module legal&lowbar;verifier](https://github.com/Accord-Project/aec3po/blob/main/src/legal_verifier.ttl)<br/>- [Module model](https://github.com/Accord-Project/aec3po/blob/main/src/model.ttl)<br/>- [Module rase&lowbar;statement](https://github.com/Accord-Project/aec3po/blob/main/src/rase_statement.ttl)<br/>- [Module statement](https://github.com/Accord-Project/aec3po/blob/main/src/statement.ttl)<br/>- [Module table](https://github.com/Accord-Project/aec3po/blob/main/src/table.ttl)<br/>- [Module vocabularies/administrative&lowbar;areas](https://github.com/Accord-Project/aec3po/blob/main/src/vocabularies/administrative_areas.ttl)<br/>- [Module vocabularies/building&lowbar;structure](https://github.com/Accord-Project/aec3po/blob/main/src/vocabularies/building_structure.ttl)<br/>- [Module vocabularies/building&lowbar;usage](https://github.com/Accord-Project/aec3po/blob/main/src/vocabularies/building_usage.ttl)<br/>- [Module vocabularies/check&lowbar;method&lowbar;comparators](https://github.com/Accord-Project/aec3po/blob/main/src/vocabularies/check_method_comparators.ttl)<br/>- [Module vocabularies/check&lowbar;method&lowbar;operators](https://github.com/Accord-Project/aec3po/blob/main/src/vocabularies/check_method_operators.ttl)<br/>- [Module vocabularies/disciplines](https://github.com/Accord-Project/aec3po/blob/main/src/vocabularies/disciplines.ttl)<br/>- [Module vocabularies/permitting&lowbar;stages](https://github.com/Accord-Project/aec3po/blob/main/src/vocabularies/permitting_stages.ttl)<br/>- [Module vocabularies/quantity&lowbar;kinds](https://github.com/Accord-Project/aec3po/blob/main/src/vocabularies/quantity_kinds.ttl)<br/>- [Module vocabularies/&lowbar;shape](https://github.com/Accord-Project/aec3po/blob/main/src/vocabularies/_shape.ttl)|

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
|[Section top](#minorfail-outcome-number-148)|Description|Statement not supported in a Super Class Expression|
|[Section top](#minorfail-outcome-number-148)|Pointer|<pre lang="Turtle"><code>&#91;] a owl:Class ;  &#10;&#32;&#32;&#32;&#32;owl:unionOf ( aec3po:FeatureOfInterest aec3po:Property aec3po:CheckMethod ) .</code></pre>|
|[Section top](#minorfail-outcome-number-148)|Pointer|<pre lang="Turtle"><code>&#91;] a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;owl:onProperty aec3po:usedMethod ;  &#10;&#32;&#32;&#32;&#32;owl:someValuesFrom aec3po:CheckMethod .</code></pre>|
|[Section top](#minorfail-outcome-number-148)|Pointer|<pre lang="Turtle"><code>&#91;] a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;owl:onProperty aec3po:madeBy ;  &#10;&#32;&#32;&#32;&#32;owl:someValuesFrom aec3po:ProcessVerifier .</code></pre>|
|[Section top](#minorfail-outcome-number-148)|Pointer|<pre lang="Turtle"><code>&#91;] a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;owl:onProperty aec3po:checked ;  &#10;&#32;&#32;&#32;&#32;owl:someValuesFrom owl:Thing .</code></pre>|
|[Section top](#minorfail-outcome-number-148)|Pointer|<pre lang="Turtle"><code>&#91;] a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;owl:onProperty aec3po:hasReport ;  &#10;&#32;&#32;&#32;&#32;owl:someValuesFrom aec3po:ComplianceVerificationReport .</code></pre>|
|[Section top](#minorfail-outcome-number-148)|Pointer|<pre lang="Turtle"><code>&#91;] a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;owl:onProperty aec3po:conforms .</code></pre>|
|[Section top](#minorfail-outcome-number-148)|Pointer|<pre lang="Turtle"><code>&#91;] a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;owl:onProperty aec3po:verificationFocus .</code></pre>|
|[Section top](#minorfail-outcome-number-148)|Pointer|<pre lang="Turtle"><code>&#91;] a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;owl:onProperty aec3po:hasSeverity .</code></pre>|
|[Section top](#minorfail-outcome-number-148)|Pointer|<pre lang="Turtle"><code>&#91;] owl:unionOf ( aec3po:Document aec3po:DocumentSubdivision ) .</code></pre>|
|[Section top](#minorfail-outcome-number-148)|Pointer|<pre lang="Turtle"><code>&#91;] a owl:Class ;  &#10;&#32;&#32;&#32;&#32;owl:unionOf ( &#60;https://schema.org/Place> aec3po:AdministrativeArea ) .</code></pre>|
|[Section top](#minorfail-outcome-number-148)|Pointer|<pre lang="Turtle"><code>&#91;] a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;owl:onProperty aec3po:hasSubdivision .</code></pre>|
|[Section top](#minorfail-outcome-number-148)|Pointer|<pre lang="Turtle"><code>&#91;] a owl:Class ;  &#10;&#32;&#32;&#32;&#32;owl:unionOf ( aec3po:Table aec3po:Image aec3po:Row aec3po:Column ) .</code></pre>|
|[Section top](#minorfail-outcome-number-148)|Pointer|<pre lang="Turtle"><code>&#91;] a owl:Class ;  &#10;&#32;&#32;&#32;&#32;owl:unionOf ( aec3po:Table aec3po:Image aec3po:Row aec3po:Column aec3po:Cell ) .</code></pre>|
|[Section top](#minorfail-outcome-number-148)|Pointer|<pre lang="Turtle"><code>&#91;] a owl:Class ;  &#10;&#32;&#32;&#32;&#32;owl:unionOf ( aec3po:Table aec3po:Image ) .</code></pre>|

***
### MinorFail Outcome number 149

[Jump to summary definition](#summary-MinorFail-149)	|	[Previous MinorFail outcome](#minorfail-outcome-number-148)	|	[Next MinorFail outcome](#minorfail-outcome-number-150)

:exclamation:MinorFail outcome
#### Subject detail
|Name|all-fragments|
|----|----|
|Title|All the fragments from branch main that are syntaxically correct as well as their recursive imports|
|Composition|- [Module aec3po](https://github.com/Accord-Project/aec3po/blob/main/src/aec3po.ttl)<br/>- [Module checking&lowbar;act](https://github.com/Accord-Project/aec3po/blob/main/src/checking_act.ttl)<br/>- [Module check&lowbar;method](https://github.com/Accord-Project/aec3po/blob/main/src/check_method.ttl)<br/>- [Module compliance&lowbar;verification&lowbar;report](https://github.com/Accord-Project/aec3po/blob/main/src/compliance_verification_report.ttl)<br/>- [Module data&lowbar;requirement](https://github.com/Accord-Project/aec3po/blob/main/src/data_requirement.ttl)<br/>- [Module document](https://github.com/Accord-Project/aec3po/blob/main/src/document.ttl)<br/>- [Module evidence](https://github.com/Accord-Project/aec3po/blob/main/src/evidence.ttl)<br/>- [Module feature&lowbar;of&lowbar;interest](https://github.com/Accord-Project/aec3po/blob/main/src/feature_of_interest.ttl)<br/>- [Module legal&lowbar;verifier](https://github.com/Accord-Project/aec3po/blob/main/src/legal_verifier.ttl)<br/>- [Module model](https://github.com/Accord-Project/aec3po/blob/main/src/model.ttl)<br/>- [Module rase&lowbar;statement](https://github.com/Accord-Project/aec3po/blob/main/src/rase_statement.ttl)<br/>- [Module statement](https://github.com/Accord-Project/aec3po/blob/main/src/statement.ttl)<br/>- [Module table](https://github.com/Accord-Project/aec3po/blob/main/src/table.ttl)<br/>- [Module vocabularies/administrative&lowbar;areas](https://github.com/Accord-Project/aec3po/blob/main/src/vocabularies/administrative_areas.ttl)<br/>- [Module vocabularies/building&lowbar;structure](https://github.com/Accord-Project/aec3po/blob/main/src/vocabularies/building_structure.ttl)<br/>- [Module vocabularies/building&lowbar;usage](https://github.com/Accord-Project/aec3po/blob/main/src/vocabularies/building_usage.ttl)<br/>- [Module vocabularies/check&lowbar;method&lowbar;comparators](https://github.com/Accord-Project/aec3po/blob/main/src/vocabularies/check_method_comparators.ttl)<br/>- [Module vocabularies/check&lowbar;method&lowbar;operators](https://github.com/Accord-Project/aec3po/blob/main/src/vocabularies/check_method_operators.ttl)<br/>- [Module vocabularies/disciplines](https://github.com/Accord-Project/aec3po/blob/main/src/vocabularies/disciplines.ttl)<br/>- [Module vocabularies/permitting&lowbar;stages](https://github.com/Accord-Project/aec3po/blob/main/src/vocabularies/permitting_stages.ttl)<br/>- [Module vocabularies/quantity&lowbar;kinds](https://github.com/Accord-Project/aec3po/blob/main/src/vocabularies/quantity_kinds.ttl)<br/>- [Module vocabularies/&lowbar;shape](https://github.com/Accord-Project/aec3po/blob/main/src/vocabularies/_shape.ttl)|

#### Criterion detail
|Identifier|[profile-compatibility](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#profile-compatibility)|
|----|----|
|Title|Profile compatibility test|
|Description|A test meant to check whether the test subject is compatible with a profile or not, and if it is not, why.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-149)|Identifier|`owl-ql-profile-error`|
|[Section top](#minorfail-outcome-number-149)|Title|OWL QL Profile incompatible|
|[Section top](#minorfail-outcome-number-149)|Description|Statement not supported in a Sub Class Expression|
|[Section top](#minorfail-outcome-number-149)|Pointer|<pre lang="Turtle"><code>&#91;] a owl:Class ;  &#10;&#32;&#32;&#32;&#32;owl:intersectionOf ( aec3po:CheckMethod &#91; a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:allValuesFrom &#91; a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:allValuesFrom aec3po:FeatureOfInterest ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:onProperty &#91; owl:inverseOf aec3po:forDesign ] ] ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:onProperty aec3po:forDesign ] ) .</code></pre>|
|[Section top](#minorfail-outcome-number-149)|Pointer|<pre lang="Turtle"><code>&#91;] owl:intersectionOf ( skos:Concept &#91; a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:hasValue aec3po:AdministrativeAreaNomenclature ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:onProperty skos:inScheme ] ) .</code></pre>|
|[Section top](#minorfail-outcome-number-149)|Pointer|<pre lang="Turtle"><code>&#91;] owl:intersectionOf ( skos:Concept &#91; a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:hasValue aec3po:BuildingStructureNomenclature ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:onProperty skos:inScheme ] ) .</code></pre>|
|[Section top](#minorfail-outcome-number-149)|Pointer|<pre lang="Turtle"><code>&#91;] owl:intersectionOf ( skos:Concept &#91; a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:hasValue aec3po:BuildingUsageNomenclature ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:onProperty skos:inScheme ] ) .</code></pre>|
|[Section top](#minorfail-outcome-number-149)|Pointer|<pre lang="Turtle"><code>&#91;] owl:intersectionOf ( skos:Concept &#91; a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:hasValue aec3po:CheckMethodComparatorNomenclature ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:onProperty skos:inScheme ] ) .</code></pre>|
|[Section top](#minorfail-outcome-number-149)|Pointer|<pre lang="Turtle"><code>&#91;] owl:intersectionOf ( skos:Concept &#91; a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:hasValue aec3po:CheckMethodOperatorNomenclature ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:onProperty skos:inScheme ] ) .</code></pre>|
|[Section top](#minorfail-outcome-number-149)|Pointer|<pre lang="Turtle"><code>&#91;] owl:intersectionOf ( skos:Concept &#91; a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:hasValue aec3po:DisciplineNomenclature ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:onProperty skos:inScheme ] ) .</code></pre>|
|[Section top](#minorfail-outcome-number-149)|Pointer|<pre lang="Turtle"><code>&#91;] owl:intersectionOf ( skos:Concept &#91; a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:hasValue aec3po:PermittingStageNomenclature ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:onProperty skos:inScheme ] ) .</code></pre>|
|[Section top](#minorfail-outcome-number-149)|Pointer|<pre lang="Turtle"><code>&#91;] owl:intersectionOf ( skos:Concept &#91; a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:hasValue aec3po:QuantityKindNomenclature ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:onProperty skos:inScheme ] ) .</code></pre>|

***
### MinorFail Outcome number 150

[Jump to summary definition](#summary-MinorFail-150)	|	[Previous MinorFail outcome](#minorfail-outcome-number-149)	|	[Next MinorFail outcome](#minorfail-outcome-number-151)

:exclamation:MinorFail outcome
#### Subject detail
|Name|all-fragments|
|----|----|
|Title|All the fragments from branch main that are syntaxically correct as well as their recursive imports|
|Composition|- [Module aec3po](https://github.com/Accord-Project/aec3po/blob/main/src/aec3po.ttl)<br/>- [Module checking&lowbar;act](https://github.com/Accord-Project/aec3po/blob/main/src/checking_act.ttl)<br/>- [Module check&lowbar;method](https://github.com/Accord-Project/aec3po/blob/main/src/check_method.ttl)<br/>- [Module compliance&lowbar;verification&lowbar;report](https://github.com/Accord-Project/aec3po/blob/main/src/compliance_verification_report.ttl)<br/>- [Module data&lowbar;requirement](https://github.com/Accord-Project/aec3po/blob/main/src/data_requirement.ttl)<br/>- [Module document](https://github.com/Accord-Project/aec3po/blob/main/src/document.ttl)<br/>- [Module evidence](https://github.com/Accord-Project/aec3po/blob/main/src/evidence.ttl)<br/>- [Module feature&lowbar;of&lowbar;interest](https://github.com/Accord-Project/aec3po/blob/main/src/feature_of_interest.ttl)<br/>- [Module legal&lowbar;verifier](https://github.com/Accord-Project/aec3po/blob/main/src/legal_verifier.ttl)<br/>- [Module model](https://github.com/Accord-Project/aec3po/blob/main/src/model.ttl)<br/>- [Module rase&lowbar;statement](https://github.com/Accord-Project/aec3po/blob/main/src/rase_statement.ttl)<br/>- [Module statement](https://github.com/Accord-Project/aec3po/blob/main/src/statement.ttl)<br/>- [Module table](https://github.com/Accord-Project/aec3po/blob/main/src/table.ttl)<br/>- [Module vocabularies/administrative&lowbar;areas](https://github.com/Accord-Project/aec3po/blob/main/src/vocabularies/administrative_areas.ttl)<br/>- [Module vocabularies/building&lowbar;structure](https://github.com/Accord-Project/aec3po/blob/main/src/vocabularies/building_structure.ttl)<br/>- [Module vocabularies/building&lowbar;usage](https://github.com/Accord-Project/aec3po/blob/main/src/vocabularies/building_usage.ttl)<br/>- [Module vocabularies/check&lowbar;method&lowbar;comparators](https://github.com/Accord-Project/aec3po/blob/main/src/vocabularies/check_method_comparators.ttl)<br/>- [Module vocabularies/check&lowbar;method&lowbar;operators](https://github.com/Accord-Project/aec3po/blob/main/src/vocabularies/check_method_operators.ttl)<br/>- [Module vocabularies/disciplines](https://github.com/Accord-Project/aec3po/blob/main/src/vocabularies/disciplines.ttl)<br/>- [Module vocabularies/permitting&lowbar;stages](https://github.com/Accord-Project/aec3po/blob/main/src/vocabularies/permitting_stages.ttl)<br/>- [Module vocabularies/quantity&lowbar;kinds](https://github.com/Accord-Project/aec3po/blob/main/src/vocabularies/quantity_kinds.ttl)<br/>- [Module vocabularies/&lowbar;shape](https://github.com/Accord-Project/aec3po/blob/main/src/vocabularies/_shape.ttl)|

#### Criterion detail
|Identifier|[profile-compatibility](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#profile-compatibility)|
|----|----|
|Title|Profile compatibility test|
|Description|A test meant to check whether the test subject is compatible with a profile or not, and if it is not, why.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-150)|Identifier|`owl-ql-profile-error`|
|[Section top](#minorfail-outcome-number-150)|Title|OWL QL Profile incompatible|
|[Section top](#minorfail-outcome-number-150)|Description|Class Expression not supported as object of rdfs:domain or rdfs:range|
|[Section top](#minorfail-outcome-number-150)|Pointer|<pre lang="Turtle"><code>aec3po:caption a owl:DatatypeProperty ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;caption&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:comment &#34;The caption of a table, image, etc. &#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:domain &#91; a owl:Class ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:unionOf ( aec3po:Table aec3po:Image ) ] ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy aec3po:table .</code></pre>|
|[Section top](#minorfail-outcome-number-150)|Pointer|<pre lang="Turtle"><code>aec3po:contains a owl:ObjectProperty ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;Contains&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:comment &#34;A container contains a table and its caption. A table contai...&#34; ;  &#10;&#32;&#32;&#32;&#32;rdfs:domain &#91; a owl:Class ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:unionOf ( aec3po:Table aec3po:Image aec3po:Row aec3po:Column ) ] ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy aec3po:table .</code></pre>|
|[Section top](#minorfail-outcome-number-150)|Pointer|<pre lang="Turtle"><code>aec3po:hasBSSDDTarget a owl:FunctionalProperty,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:ObjectProperty ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;hasBSSDDTarget&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:comment &#34;The target refers to either the name of an object, the name ...&#34; ;  &#10;&#32;&#32;&#32;&#32;rdfs:domain &#91; a owl:Class ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:unionOf ( aec3po:FeatureOfInterest aec3po:Property aec3po:CheckMethod ) ] ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy aec3po:check&lowbar;method .</code></pre>|
|[Section top](#minorfail-outcome-number-150)|Pointer|<pre lang="Turtle"><code>aec3po:hasFirstSubdivision a owl:FunctionalProperty,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:ObjectProperty ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;has first subdivision&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:comment &#34;Links a document part to the first of its subdivision&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:domain &#91; owl:unionOf ( aec3po:Document aec3po:DocumentSubdivision ) ] ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy aec3po:document ;  &#10;&#32;&#32;&#32;&#32;rdfs:range aec3po:DocumentSubdivision ;  &#10;&#32;&#32;&#32;&#32;rdfs:subPropertyOf aec3po:hasSubdivision .</code></pre>|
|[Section top](#minorfail-outcome-number-150)|Pointer|<pre lang="Turtle"><code>aec3po:hasSubdivision a owl:ObjectProperty ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;has subdivision&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:comment &#34;links a document part to some of its subdivision&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:domain &#91; owl:unionOf ( aec3po:Document aec3po:DocumentSubdivision ) ] ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy aec3po:document ;  &#10;&#32;&#32;&#32;&#32;rdfs:range aec3po:DocumentSubdivision ;  &#10;&#32;&#32;&#32;&#32;rdfs:subPropertyOf dc:hasPart .</code></pre>|
|[Section top](#minorfail-outcome-number-150)|Pointer|<pre lang="Turtle"><code>aec3po:hasUnit a owl:FunctionalProperty,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:ObjectProperty ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;hasUnit&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:comment &#34;the hasUnit property is used to link a specific property or ...&#34; ;  &#10;&#32;&#32;&#32;&#32;rdfs:domain &#91; a owl:Class ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:unionOf ( aec3po:FeatureOfInterest aec3po:Property aec3po:CheckMethod ) ] ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy aec3po:check&lowbar;method ;  &#10;&#32;&#32;&#32;&#32;rdfs:range qudt:Unit ;  &#10;&#32;&#32;&#32;&#32;owl:eqivalentProperty qudt:hasValue .</code></pre>|
|[Section top](#minorfail-outcome-number-150)|Pointer|<pre lang="Turtle"><code>aec3po:hasValue a owl:DatatypeProperty,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:FunctionalProperty ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;has value&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:comment &#34;de facto used to link something (anything: property, propert...&#34; ;  &#10;&#32;&#32;&#32;&#32;rdfs:domain &#91; a owl:Class ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:unionOf ( aec3po:FeatureOfInterest aec3po:Property aec3po:CheckMethod ) ] ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy aec3po: ;  &#10;&#32;&#32;&#32;&#32;skos:note &#34;The value of the literal may be a XSD literal (boolean, inte...&#34; .</code></pre>|
|[Section top](#minorfail-outcome-number-150)|Pointer|<pre lang="Turtle"><code>aec3po:isContainedIn a owl:ObjectProperty ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;is contained by&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:comment &#34;A table contains row, columns and other elements.&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy aec3po:table ;  &#10;&#32;&#32;&#32;&#32;rdfs:range &#91; a owl:Class ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:unionOf ( aec3po:Table aec3po:Image aec3po:Row aec3po:Column aec3po:Cell ) ] .</code></pre>|
|[Section top](#minorfail-outcome-number-150)|Pointer|<pre lang="Turtle"><code>aec3po:locationCoverage a owl:ObjectProperty ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;location coverage&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:comment &#34;The spatialCoverage indicates the place(s) or the administra...&#34; ;  &#10;&#32;&#32;&#32;&#32;rdfs:domain &#60;https://schema.org/Model> ;  &#10;&#32;&#32;&#32;&#32;rdfs:range &#91; a owl:Class ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:unionOf ( &#60;https://schema.org/Place> aec3po:AdministrativeArea ) ] ;  &#10;&#32;&#32;&#32;&#32;owl:equivalentProperty &#60;https://schema.org/spatialCoverage> .</code></pre>|

***
### MinorFail Outcome number 151

[Jump to summary definition](#summary-MinorFail-151)	|	[Previous MinorFail outcome](#minorfail-outcome-number-150)	|	[Next MinorFail outcome](#minorfail-outcome-number-152)

:exclamation:MinorFail outcome
#### Subject detail
|Name|all-fragments|
|----|----|
|Title|All the fragments from branch main that are syntaxically correct as well as their recursive imports|
|Composition|- [Module aec3po](https://github.com/Accord-Project/aec3po/blob/main/src/aec3po.ttl)<br/>- [Module checking&lowbar;act](https://github.com/Accord-Project/aec3po/blob/main/src/checking_act.ttl)<br/>- [Module check&lowbar;method](https://github.com/Accord-Project/aec3po/blob/main/src/check_method.ttl)<br/>- [Module compliance&lowbar;verification&lowbar;report](https://github.com/Accord-Project/aec3po/blob/main/src/compliance_verification_report.ttl)<br/>- [Module data&lowbar;requirement](https://github.com/Accord-Project/aec3po/blob/main/src/data_requirement.ttl)<br/>- [Module document](https://github.com/Accord-Project/aec3po/blob/main/src/document.ttl)<br/>- [Module evidence](https://github.com/Accord-Project/aec3po/blob/main/src/evidence.ttl)<br/>- [Module feature&lowbar;of&lowbar;interest](https://github.com/Accord-Project/aec3po/blob/main/src/feature_of_interest.ttl)<br/>- [Module legal&lowbar;verifier](https://github.com/Accord-Project/aec3po/blob/main/src/legal_verifier.ttl)<br/>- [Module model](https://github.com/Accord-Project/aec3po/blob/main/src/model.ttl)<br/>- [Module rase&lowbar;statement](https://github.com/Accord-Project/aec3po/blob/main/src/rase_statement.ttl)<br/>- [Module statement](https://github.com/Accord-Project/aec3po/blob/main/src/statement.ttl)<br/>- [Module table](https://github.com/Accord-Project/aec3po/blob/main/src/table.ttl)<br/>- [Module vocabularies/administrative&lowbar;areas](https://github.com/Accord-Project/aec3po/blob/main/src/vocabularies/administrative_areas.ttl)<br/>- [Module vocabularies/building&lowbar;structure](https://github.com/Accord-Project/aec3po/blob/main/src/vocabularies/building_structure.ttl)<br/>- [Module vocabularies/building&lowbar;usage](https://github.com/Accord-Project/aec3po/blob/main/src/vocabularies/building_usage.ttl)<br/>- [Module vocabularies/check&lowbar;method&lowbar;comparators](https://github.com/Accord-Project/aec3po/blob/main/src/vocabularies/check_method_comparators.ttl)<br/>- [Module vocabularies/check&lowbar;method&lowbar;operators](https://github.com/Accord-Project/aec3po/blob/main/src/vocabularies/check_method_operators.ttl)<br/>- [Module vocabularies/disciplines](https://github.com/Accord-Project/aec3po/blob/main/src/vocabularies/disciplines.ttl)<br/>- [Module vocabularies/permitting&lowbar;stages](https://github.com/Accord-Project/aec3po/blob/main/src/vocabularies/permitting_stages.ttl)<br/>- [Module vocabularies/quantity&lowbar;kinds](https://github.com/Accord-Project/aec3po/blob/main/src/vocabularies/quantity_kinds.ttl)<br/>- [Module vocabularies/&lowbar;shape](https://github.com/Accord-Project/aec3po/blob/main/src/vocabularies/_shape.ttl)|

#### Criterion detail
|Identifier|[profile-compatibility](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#profile-compatibility)|
|----|----|
|Title|Profile compatibility test|
|Description|A test meant to check whether the test subject is compatible with a profile or not, and if it is not, why.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-151)|Identifier|`owl-ql-profile-error`|
|[Section top](#minorfail-outcome-number-151)|Title|OWL QL Profile incompatible|
|[Section top](#minorfail-outcome-number-151)|Description|Class Expression not supported with rdfs:subClassOf|
|[Section top](#minorfail-outcome-number-151)|Pointer|<pre lang="Turtle"><code>aec3po:AndCheckStatement a owl:Class ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;And Check Statement&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:comment &#34;Check verified if and only if all of its sub-checks are veri...&#34; ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy aec3po:statement ;  &#10;&#32;&#32;&#32;&#32;rdfs:subClassOf &#91; a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:onProperty aec3po:hasSubdivision ],  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;aec3po:ChecklistStatement .</code></pre>|
|[Section top](#minorfail-outcome-number-151)|Pointer|<pre lang="Turtle"><code>aec3po:ComplianceVerificationReport a owl:Class ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;Compliance Verification Report&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:comment &#34;Result of a checking act. May be compliant or not.&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy aec3po:compliance&lowbar;verification&lowbar;report ;  &#10;&#32;&#32;&#32;&#32;rdfs:subClassOf &#91; a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:onProperty aec3po:conforms ] .</code></pre>|
|[Section top](#minorfail-outcome-number-151)|Pointer|<pre lang="Turtle"><code>aec3po:DocumentSubdivision a owl:Class ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;Document Subdivision&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:comment &#34;Any subdivision of a document, including sections, paragraph...&#34; ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy aec3po:document ;  &#10;&#32;&#32;&#32;&#32;rdfs:subClassOf &#91; a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:allValuesFrom aec3po:DocumentSubdivision ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:onProperty aec3po:hasSubdivision ] ;  &#10;&#32;&#32;&#32;&#32;skos:example &#34;Paragraph, section, definition...&#34;@en .</code></pre>|
|[Section top](#minorfail-outcome-number-151)|Pointer|<pre lang="Turtle"><code>aec3po:LegalVerifier a owl:Class ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;Legal Verifier&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:comment &#34;An entity that has the legal capacity to verify compliance w...&#34; ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy aec3po:legal&lowbar;verifier ;  &#10;&#32;&#32;&#32;&#32;rdfs:subClassOf &#91; owl:allValuesFrom aec3po:Document ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:onProperty aec3po:forDocument ],  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;foaf:Agent .</code></pre>|
|[Section top](#minorfail-outcome-number-151)|Pointer|<pre lang="Turtle"><code>aec3po:NotCheckStatement a owl:Class ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;Not Check Statement&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:comment &#34;Check verified if and only if the sub-check is not verified.&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy aec3po:statement ;  &#10;&#32;&#32;&#32;&#32;rdfs:subClassOf &#91; a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:onProperty aec3po:hasSubdivision ] .</code></pre>|
|[Section top](#minorfail-outcome-number-151)|Pointer|<pre lang="Turtle"><code>aec3po:OrCheckStatement a owl:Class ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;Or Check Statement&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:comment &#34;Check verified if and only if at least one of its sub-checks...&#34; ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy aec3po:statement ;  &#10;&#32;&#32;&#32;&#32;rdfs:subClassOf &#91; a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:onProperty aec3po:hasSubdivision ],  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;aec3po:ChecklistStatement .</code></pre>|
|[Section top](#minorfail-outcome-number-151)|Pointer|<pre lang="Turtle"><code>aec3po:VerificationResult a owl:Class ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;Verification Result&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:comment &#34;Individual verification result of a Compliance Verification ...&#34; ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy aec3po:compliance&lowbar;verification&lowbar;report ;  &#10;&#32;&#32;&#32;&#32;rdfs:subClassOf &#91; a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:onProperty aec3po:verificationFocus ],  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#91; a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:onProperty aec3po:hasSeverity ] .</code></pre>|

***
### MinorFail Outcome number 152

[Jump to summary definition](#summary-MinorFail-152)	|	[Previous MinorFail outcome](#minorfail-outcome-number-151)	|	[Next MinorFail outcome](#minorfail-outcome-number-153)

:exclamation:MinorFail outcome
#### Subject detail
|Name|all-fragments|
|----|----|
|Title|All the fragments from branch main that are syntaxically correct as well as their recursive imports|
|Composition|- [Module aec3po](https://github.com/Accord-Project/aec3po/blob/main/src/aec3po.ttl)<br/>- [Module checking&lowbar;act](https://github.com/Accord-Project/aec3po/blob/main/src/checking_act.ttl)<br/>- [Module check&lowbar;method](https://github.com/Accord-Project/aec3po/blob/main/src/check_method.ttl)<br/>- [Module compliance&lowbar;verification&lowbar;report](https://github.com/Accord-Project/aec3po/blob/main/src/compliance_verification_report.ttl)<br/>- [Module data&lowbar;requirement](https://github.com/Accord-Project/aec3po/blob/main/src/data_requirement.ttl)<br/>- [Module document](https://github.com/Accord-Project/aec3po/blob/main/src/document.ttl)<br/>- [Module evidence](https://github.com/Accord-Project/aec3po/blob/main/src/evidence.ttl)<br/>- [Module feature&lowbar;of&lowbar;interest](https://github.com/Accord-Project/aec3po/blob/main/src/feature_of_interest.ttl)<br/>- [Module legal&lowbar;verifier](https://github.com/Accord-Project/aec3po/blob/main/src/legal_verifier.ttl)<br/>- [Module model](https://github.com/Accord-Project/aec3po/blob/main/src/model.ttl)<br/>- [Module rase&lowbar;statement](https://github.com/Accord-Project/aec3po/blob/main/src/rase_statement.ttl)<br/>- [Module statement](https://github.com/Accord-Project/aec3po/blob/main/src/statement.ttl)<br/>- [Module table](https://github.com/Accord-Project/aec3po/blob/main/src/table.ttl)<br/>- [Module vocabularies/administrative&lowbar;areas](https://github.com/Accord-Project/aec3po/blob/main/src/vocabularies/administrative_areas.ttl)<br/>- [Module vocabularies/building&lowbar;structure](https://github.com/Accord-Project/aec3po/blob/main/src/vocabularies/building_structure.ttl)<br/>- [Module vocabularies/building&lowbar;usage](https://github.com/Accord-Project/aec3po/blob/main/src/vocabularies/building_usage.ttl)<br/>- [Module vocabularies/check&lowbar;method&lowbar;comparators](https://github.com/Accord-Project/aec3po/blob/main/src/vocabularies/check_method_comparators.ttl)<br/>- [Module vocabularies/check&lowbar;method&lowbar;operators](https://github.com/Accord-Project/aec3po/blob/main/src/vocabularies/check_method_operators.ttl)<br/>- [Module vocabularies/disciplines](https://github.com/Accord-Project/aec3po/blob/main/src/vocabularies/disciplines.ttl)<br/>- [Module vocabularies/permitting&lowbar;stages](https://github.com/Accord-Project/aec3po/blob/main/src/vocabularies/permitting_stages.ttl)<br/>- [Module vocabularies/quantity&lowbar;kinds](https://github.com/Accord-Project/aec3po/blob/main/src/vocabularies/quantity_kinds.ttl)<br/>- [Module vocabularies/&lowbar;shape](https://github.com/Accord-Project/aec3po/blob/main/src/vocabularies/_shape.ttl)|

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
|[Section top](#minorfail-outcome-number-152)|Description|Restriction on datatypes|
|[Section top](#minorfail-outcome-number-152)|Pointer|<pre lang="Turtle"><code>aec3po:conforms a owl:DatatypeProperty ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;conforms&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:comment &#34;True if the Checking act confirms the check was validated, a...&#34; ;  &#10;&#32;&#32;&#32;&#32;rdfs:domain aec3po:ComplianceVerificationReport ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy aec3po:compliance&lowbar;verification&lowbar;report ;  &#10;&#32;&#32;&#32;&#32;rdfs:range xsd:boolean .</code></pre>|
|[Section top](#minorfail-outcome-number-152)|Pointer|<pre lang="Turtle"><code>aec3po:hasBooleanTarget a owl:DatatypeProperty ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;hasBooleanTarget&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:comment &#34;TBD&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:range xsd:boolean .</code></pre>|

***
### MinorFail Outcome number 153

[Jump to summary definition](#summary-MinorFail-153)	|	[Previous MinorFail outcome](#minorfail-outcome-number-152)	|	[Next MinorFail outcome](#minorfail-outcome-number-154)

:exclamation:MinorFail outcome
#### Subject detail
|Name|all-fragments|
|----|----|
|Title|All the fragments from branch main that are syntaxically correct as well as their recursive imports|
|Composition|- [Module aec3po](https://github.com/Accord-Project/aec3po/blob/main/src/aec3po.ttl)<br/>- [Module checking&lowbar;act](https://github.com/Accord-Project/aec3po/blob/main/src/checking_act.ttl)<br/>- [Module check&lowbar;method](https://github.com/Accord-Project/aec3po/blob/main/src/check_method.ttl)<br/>- [Module compliance&lowbar;verification&lowbar;report](https://github.com/Accord-Project/aec3po/blob/main/src/compliance_verification_report.ttl)<br/>- [Module data&lowbar;requirement](https://github.com/Accord-Project/aec3po/blob/main/src/data_requirement.ttl)<br/>- [Module document](https://github.com/Accord-Project/aec3po/blob/main/src/document.ttl)<br/>- [Module evidence](https://github.com/Accord-Project/aec3po/blob/main/src/evidence.ttl)<br/>- [Module feature&lowbar;of&lowbar;interest](https://github.com/Accord-Project/aec3po/blob/main/src/feature_of_interest.ttl)<br/>- [Module legal&lowbar;verifier](https://github.com/Accord-Project/aec3po/blob/main/src/legal_verifier.ttl)<br/>- [Module model](https://github.com/Accord-Project/aec3po/blob/main/src/model.ttl)<br/>- [Module rase&lowbar;statement](https://github.com/Accord-Project/aec3po/blob/main/src/rase_statement.ttl)<br/>- [Module statement](https://github.com/Accord-Project/aec3po/blob/main/src/statement.ttl)<br/>- [Module table](https://github.com/Accord-Project/aec3po/blob/main/src/table.ttl)<br/>- [Module vocabularies/administrative&lowbar;areas](https://github.com/Accord-Project/aec3po/blob/main/src/vocabularies/administrative_areas.ttl)<br/>- [Module vocabularies/building&lowbar;structure](https://github.com/Accord-Project/aec3po/blob/main/src/vocabularies/building_structure.ttl)<br/>- [Module vocabularies/building&lowbar;usage](https://github.com/Accord-Project/aec3po/blob/main/src/vocabularies/building_usage.ttl)<br/>- [Module vocabularies/check&lowbar;method&lowbar;comparators](https://github.com/Accord-Project/aec3po/blob/main/src/vocabularies/check_method_comparators.ttl)<br/>- [Module vocabularies/check&lowbar;method&lowbar;operators](https://github.com/Accord-Project/aec3po/blob/main/src/vocabularies/check_method_operators.ttl)<br/>- [Module vocabularies/disciplines](https://github.com/Accord-Project/aec3po/blob/main/src/vocabularies/disciplines.ttl)<br/>- [Module vocabularies/permitting&lowbar;stages](https://github.com/Accord-Project/aec3po/blob/main/src/vocabularies/permitting_stages.ttl)<br/>- [Module vocabularies/quantity&lowbar;kinds](https://github.com/Accord-Project/aec3po/blob/main/src/vocabularies/quantity_kinds.ttl)<br/>- [Module vocabularies/&lowbar;shape](https://github.com/Accord-Project/aec3po/blob/main/src/vocabularies/_shape.ttl)|

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
|[Section top](#minorfail-outcome-number-153)|Description|Class Expression not supported with owl:equivalentClass|
|[Section top](#minorfail-outcome-number-153)|Pointer|<pre lang="Turtle"><code>aec3po:AdministrativeArea a owl:Class ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;Administrative Area&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:comment &#34;Formally defined as the set of skos:Concept either in concep...&#34; ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy aec3po:administrative&lowbar;areas ;  &#10;&#32;&#32;&#32;&#32;rdfs:seeAlso &#60;https://op.europa.eu/en/web/eu-vocabularies/concept-scheme/-/resource?uri=http://publications.europa.eu/resource/authority/atu> ;  &#10;&#32;&#32;&#32;&#32;rdfs:subClassOf skos:Concept ;  &#10;&#32;&#32;&#32;&#32;owl:equivalentClass &#91; owl:intersectionOf ( skos:Concept &#91; a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:hasValue aec3po:AdministrativeAreaNomenclature ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:onProperty skos:inScheme ] ) ],  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#60;http://data.europa.eu/eli/ontology#AdministrativeArea> .</code></pre>|
|[Section top](#minorfail-outcome-number-153)|Pointer|<pre lang="Turtle"><code>aec3po:BuildingStructure a owl:Class ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;building structure&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:comment &#34;Formally defined as the set of skos:Concept in concept schem...&#34; ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy aec3po:building&lowbar;structure ;  &#10;&#32;&#32;&#32;&#32;rdfs:subClassOf skos:Concept,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;aec3po:Design ;  &#10;&#32;&#32;&#32;&#32;owl:equivalentClass &#91; owl:intersectionOf ( skos:Concept &#91; a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:hasValue aec3po:BuildingStructureNomenclature ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:onProperty skos:inScheme ] ) ] .</code></pre>|
|[Section top](#minorfail-outcome-number-153)|Pointer|<pre lang="Turtle"><code>aec3po:BuildingUsage a owl:Class ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;building usage&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:comment &#34;Formally defined as the set of skos:Concept in concept schem...&#34; ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy aec3po:building&lowbar;usage ;  &#10;&#32;&#32;&#32;&#32;rdfs:subClassOf skos:Concept,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;aec3po:Design ;  &#10;&#32;&#32;&#32;&#32;owl:equivalentClass &#91; owl:intersectionOf ( skos:Concept &#91; a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:hasValue aec3po:BuildingUsageNomenclature ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:onProperty skos:inScheme ] ) ] .</code></pre>|
|[Section top](#minorfail-outcome-number-153)|Pointer|<pre lang="Turtle"><code>aec3po:CheckMethodComparator a owl:Class ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;check method comparator&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:comment &#34;Formally defined as the set of skos:Concept in concept schem...&#34; ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy aec3po:check&lowbar;method&lowbar;comparators ;  &#10;&#32;&#32;&#32;&#32;rdfs:subClassOf skos:Concept,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;aec3po:CheckMethod ;  &#10;&#32;&#32;&#32;&#32;owl:equivalentClass &#91; owl:intersectionOf ( skos:Concept &#91; a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:hasValue aec3po:CheckMethodComparatorNomenclature ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:onProperty skos:inScheme ] ) ] .</code></pre>|
|[Section top](#minorfail-outcome-number-153)|Pointer|<pre lang="Turtle"><code>aec3po:CheckMethodOperator a owl:Class ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;check method operator&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:comment &#34;Formally defined as the set of skos:Concept in concept schem...&#34; ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy aec3po:check&lowbar;method&lowbar;operators ;  &#10;&#32;&#32;&#32;&#32;rdfs:subClassOf skos:Concept,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;aec3po:CheckMethod ;  &#10;&#32;&#32;&#32;&#32;owl:equivalentClass &#91; owl:intersectionOf ( skos:Concept &#91; a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:hasValue aec3po:CheckMethodOperatorNomenclature ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:onProperty skos:inScheme ] ) ] .</code></pre>|
|[Section top](#minorfail-outcome-number-153)|Pointer|<pre lang="Turtle"><code>aec3po:ComponentCheckMethod a owl:Class ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;Component Check Method&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:comment &#34;Component check method refers to a process of inspecting and...&#34; ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy aec3po:check&lowbar;method ;  &#10;&#32;&#32;&#32;&#32;rdfs:subClassOf aec3po:CheckMethod ;  &#10;&#32;&#32;&#32;&#32;owl:equivalentClass &#91; a owl:Class ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:intersectionOf ( aec3po:CheckMethod &#91; a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:allValuesFrom &#91; a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:allValuesFrom aec3po:FeatureOfInterest ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:onProperty &#91; owl:inverseOf aec3po:forDesign ] ] ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:onProperty aec3po:forDesign ] ) ] .</code></pre>|
|[Section top](#minorfail-outcome-number-153)|Pointer|<pre lang="Turtle"><code>aec3po:Discipline a owl:Class ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;Discipline&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:comment &#34;The AEC discipline to which something pertains.&#34; ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy aec3po:discipline ;  &#10;&#32;&#32;&#32;&#32;rdfs:subClassOf skos:Concept ;  &#10;&#32;&#32;&#32;&#32;owl:equivalentClass &#91; owl:intersectionOf ( skos:Concept &#91; a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:hasValue aec3po:DisciplineNomenclature ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:onProperty skos:inScheme ] ) ] .</code></pre>|
|[Section top](#minorfail-outcome-number-153)|Pointer|<pre lang="Turtle"><code>aec3po:PermittingStage a owl:Class ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;Permitting Stage&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:comment &#34;The class of permitting stages.&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy aec3po:permitting&lowbar;stage ;  &#10;&#32;&#32;&#32;&#32;rdfs:subClassOf skos:Concept ;  &#10;&#32;&#32;&#32;&#32;owl:equivalentClass &#91; owl:intersectionOf ( skos:Concept &#91; a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:hasValue aec3po:PermittingStageNomenclature ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:onProperty skos:inScheme ] ) ] .</code></pre>|
|[Section top](#minorfail-outcome-number-153)|Pointer|<pre lang="Turtle"><code>aec3po:QuantityKind a owl:Class ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;Quantity Kind&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:comment &#34;A Quantity Kind is any observable property that can be quant...&#34;,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#34;A kind of quantity.&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy aec3po:feature&lowbar;of&lowbar;interest,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;aec3po:quantity&lowbar;kinds ;  &#10;&#32;&#32;&#32;&#32;rdfs:subClassOf qudt:QuantityKind,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#60;http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#Region>,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;skos:Concept ;  &#10;&#32;&#32;&#32;&#32;owl:equivalentClass &#91; owl:intersectionOf ( skos:Concept &#91; a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:hasValue aec3po:QuantityKindNomenclature ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:onProperty skos:inScheme ] ) ] ;  &#10;&#32;&#32;&#32;&#32;skos:example &#34;Length, Area, U-Value.&#34;@en,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#34;height, area, U-value&#34;@en ;  &#10;&#32;&#32;&#32;&#32;skos:note &#34;Maxime Lefrançois argues that both qudt:QuantityKind and qud...&#34; .</code></pre>|

***
### MinorFail Outcome number 154

[Jump to summary definition](#summary-MinorFail-154)	|	[Previous MinorFail outcome](#minorfail-outcome-number-153)	|	[Next MinorFail outcome](#minorfail-outcome-number-155)

:exclamation:MinorFail outcome
#### Subject detail
|Name|all-fragments|
|----|----|
|Title|All the fragments from branch main that are syntaxically correct as well as their recursive imports|
|Composition|- [Module aec3po](https://github.com/Accord-Project/aec3po/blob/main/src/aec3po.ttl)<br/>- [Module checking&lowbar;act](https://github.com/Accord-Project/aec3po/blob/main/src/checking_act.ttl)<br/>- [Module check&lowbar;method](https://github.com/Accord-Project/aec3po/blob/main/src/check_method.ttl)<br/>- [Module compliance&lowbar;verification&lowbar;report](https://github.com/Accord-Project/aec3po/blob/main/src/compliance_verification_report.ttl)<br/>- [Module data&lowbar;requirement](https://github.com/Accord-Project/aec3po/blob/main/src/data_requirement.ttl)<br/>- [Module document](https://github.com/Accord-Project/aec3po/blob/main/src/document.ttl)<br/>- [Module evidence](https://github.com/Accord-Project/aec3po/blob/main/src/evidence.ttl)<br/>- [Module feature&lowbar;of&lowbar;interest](https://github.com/Accord-Project/aec3po/blob/main/src/feature_of_interest.ttl)<br/>- [Module legal&lowbar;verifier](https://github.com/Accord-Project/aec3po/blob/main/src/legal_verifier.ttl)<br/>- [Module model](https://github.com/Accord-Project/aec3po/blob/main/src/model.ttl)<br/>- [Module rase&lowbar;statement](https://github.com/Accord-Project/aec3po/blob/main/src/rase_statement.ttl)<br/>- [Module statement](https://github.com/Accord-Project/aec3po/blob/main/src/statement.ttl)<br/>- [Module table](https://github.com/Accord-Project/aec3po/blob/main/src/table.ttl)<br/>- [Module vocabularies/administrative&lowbar;areas](https://github.com/Accord-Project/aec3po/blob/main/src/vocabularies/administrative_areas.ttl)<br/>- [Module vocabularies/building&lowbar;structure](https://github.com/Accord-Project/aec3po/blob/main/src/vocabularies/building_structure.ttl)<br/>- [Module vocabularies/building&lowbar;usage](https://github.com/Accord-Project/aec3po/blob/main/src/vocabularies/building_usage.ttl)<br/>- [Module vocabularies/check&lowbar;method&lowbar;comparators](https://github.com/Accord-Project/aec3po/blob/main/src/vocabularies/check_method_comparators.ttl)<br/>- [Module vocabularies/check&lowbar;method&lowbar;operators](https://github.com/Accord-Project/aec3po/blob/main/src/vocabularies/check_method_operators.ttl)<br/>- [Module vocabularies/disciplines](https://github.com/Accord-Project/aec3po/blob/main/src/vocabularies/disciplines.ttl)<br/>- [Module vocabularies/permitting&lowbar;stages](https://github.com/Accord-Project/aec3po/blob/main/src/vocabularies/permitting_stages.ttl)<br/>- [Module vocabularies/quantity&lowbar;kinds](https://github.com/Accord-Project/aec3po/blob/main/src/vocabularies/quantity_kinds.ttl)<br/>- [Module vocabularies/&lowbar;shape](https://github.com/Accord-Project/aec3po/blob/main/src/vocabularies/_shape.ttl)|

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
|[Section top](#minorfail-outcome-number-154)|Pointer|<pre lang="Turtle"><code>&#91;] a owl:Class ;  &#10;&#32;&#32;&#32;&#32;owl:unionOf ( aec3po:FeatureOfInterest aec3po:Property aec3po:CheckMethod ) .</code></pre>|
|[Section top](#minorfail-outcome-number-154)|Pointer|<pre lang="Turtle"><code>&#91;] a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;owl:onProperty aec3po:conforms .</code></pre>|
|[Section top](#minorfail-outcome-number-154)|Pointer|<pre lang="Turtle"><code>&#91;] a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;owl:onProperty aec3po:verificationFocus .</code></pre>|
|[Section top](#minorfail-outcome-number-154)|Pointer|<pre lang="Turtle"><code>&#91;] a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;owl:onProperty aec3po:hasSeverity .</code></pre>|
|[Section top](#minorfail-outcome-number-154)|Pointer|<pre lang="Turtle"><code>&#91;] a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;owl:allValuesFrom aec3po:DocumentSubdivision ;  &#10;&#32;&#32;&#32;&#32;owl:onProperty aec3po:hasSubdivision .</code></pre>|
|[Section top](#minorfail-outcome-number-154)|Pointer|<pre lang="Turtle"><code>&#91;] owl:unionOf ( aec3po:Document aec3po:DocumentSubdivision ) .</code></pre>|
|[Section top](#minorfail-outcome-number-154)|Pointer|<pre lang="Turtle"><code>&#91;] owl:allValuesFrom aec3po:Document ;  &#10;&#32;&#32;&#32;&#32;owl:onProperty aec3po:forDocument .</code></pre>|
|[Section top](#minorfail-outcome-number-154)|Pointer|<pre lang="Turtle"><code>&#91;] a owl:Class ;  &#10;&#32;&#32;&#32;&#32;owl:unionOf ( &#60;https://schema.org/Place> aec3po:AdministrativeArea ) .</code></pre>|
|[Section top](#minorfail-outcome-number-154)|Pointer|<pre lang="Turtle"><code>&#91;] a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;owl:onProperty aec3po:hasSubdivision .</code></pre>|
|[Section top](#minorfail-outcome-number-154)|Pointer|<pre lang="Turtle"><code>&#91;] a owl:Class ;  &#10;&#32;&#32;&#32;&#32;owl:unionOf ( aec3po:Table aec3po:Image aec3po:Row aec3po:Column ) .</code></pre>|
|[Section top](#minorfail-outcome-number-154)|Pointer|<pre lang="Turtle"><code>&#91;] a owl:Class ;  &#10;&#32;&#32;&#32;&#32;owl:unionOf ( aec3po:Table aec3po:Image aec3po:Row aec3po:Column aec3po:Cell ) .</code></pre>|
|[Section top](#minorfail-outcome-number-154)|Pointer|<pre lang="Turtle"><code>&#91;] a owl:Class ;  &#10;&#32;&#32;&#32;&#32;owl:unionOf ( aec3po:Table aec3po:Image ) .</code></pre>|

***
### MinorFail Outcome number 155

[Jump to summary definition](#summary-MinorFail-155)	|	[Previous MinorFail outcome](#minorfail-outcome-number-154)	|	[Next MinorFail outcome](#minorfail-outcome-number-156)

:exclamation:MinorFail outcome
#### Subject detail
|Name|all-fragments|
|----|----|
|Title|All the fragments from branch main that are syntaxically correct as well as their recursive imports|
|Composition|- [Module aec3po](https://github.com/Accord-Project/aec3po/blob/main/src/aec3po.ttl)<br/>- [Module checking&lowbar;act](https://github.com/Accord-Project/aec3po/blob/main/src/checking_act.ttl)<br/>- [Module check&lowbar;method](https://github.com/Accord-Project/aec3po/blob/main/src/check_method.ttl)<br/>- [Module compliance&lowbar;verification&lowbar;report](https://github.com/Accord-Project/aec3po/blob/main/src/compliance_verification_report.ttl)<br/>- [Module data&lowbar;requirement](https://github.com/Accord-Project/aec3po/blob/main/src/data_requirement.ttl)<br/>- [Module document](https://github.com/Accord-Project/aec3po/blob/main/src/document.ttl)<br/>- [Module evidence](https://github.com/Accord-Project/aec3po/blob/main/src/evidence.ttl)<br/>- [Module feature&lowbar;of&lowbar;interest](https://github.com/Accord-Project/aec3po/blob/main/src/feature_of_interest.ttl)<br/>- [Module legal&lowbar;verifier](https://github.com/Accord-Project/aec3po/blob/main/src/legal_verifier.ttl)<br/>- [Module model](https://github.com/Accord-Project/aec3po/blob/main/src/model.ttl)<br/>- [Module rase&lowbar;statement](https://github.com/Accord-Project/aec3po/blob/main/src/rase_statement.ttl)<br/>- [Module statement](https://github.com/Accord-Project/aec3po/blob/main/src/statement.ttl)<br/>- [Module table](https://github.com/Accord-Project/aec3po/blob/main/src/table.ttl)<br/>- [Module vocabularies/administrative&lowbar;areas](https://github.com/Accord-Project/aec3po/blob/main/src/vocabularies/administrative_areas.ttl)<br/>- [Module vocabularies/building&lowbar;structure](https://github.com/Accord-Project/aec3po/blob/main/src/vocabularies/building_structure.ttl)<br/>- [Module vocabularies/building&lowbar;usage](https://github.com/Accord-Project/aec3po/blob/main/src/vocabularies/building_usage.ttl)<br/>- [Module vocabularies/check&lowbar;method&lowbar;comparators](https://github.com/Accord-Project/aec3po/blob/main/src/vocabularies/check_method_comparators.ttl)<br/>- [Module vocabularies/check&lowbar;method&lowbar;operators](https://github.com/Accord-Project/aec3po/blob/main/src/vocabularies/check_method_operators.ttl)<br/>- [Module vocabularies/disciplines](https://github.com/Accord-Project/aec3po/blob/main/src/vocabularies/disciplines.ttl)<br/>- [Module vocabularies/permitting&lowbar;stages](https://github.com/Accord-Project/aec3po/blob/main/src/vocabularies/permitting_stages.ttl)<br/>- [Module vocabularies/quantity&lowbar;kinds](https://github.com/Accord-Project/aec3po/blob/main/src/vocabularies/quantity_kinds.ttl)<br/>- [Module vocabularies/&lowbar;shape](https://github.com/Accord-Project/aec3po/blob/main/src/vocabularies/_shape.ttl)|

#### Criterion detail
|Identifier|[profile-compatibility](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#profile-compatibility)|
|----|----|
|Title|Profile compatibility test|
|Description|A test meant to check whether the test subject is compatible with a profile or not, and if it is not, why.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-155)|Identifier|`owl-el-profile-error`|
|[Section top](#minorfail-outcome-number-155)|Title|OWL EL Profile incompatible|
|[Section top](#minorfail-outcome-number-155)|Description|Statement not supported in a Class Expression|
|[Section top](#minorfail-outcome-number-155)|Pointer|<pre lang="Turtle"><code>&#91;] a owl:Class ;  &#10;&#32;&#32;&#32;&#32;owl:unionOf ( aec3po:FeatureOfInterest aec3po:Property aec3po:CheckMethod ) .</code></pre>|
|[Section top](#minorfail-outcome-number-155)|Pointer|<pre lang="Turtle"><code>&#91;] a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;owl:allValuesFrom &#91; a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:allValuesFrom aec3po:FeatureOfInterest ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:onProperty &#91; owl:inverseOf aec3po:forDesign ] ] ;  &#10;&#32;&#32;&#32;&#32;owl:onProperty aec3po:forDesign .</code></pre>|
|[Section top](#minorfail-outcome-number-155)|Pointer|<pre lang="Turtle"><code>&#91;] a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;owl:onProperty aec3po:conforms .</code></pre>|
|[Section top](#minorfail-outcome-number-155)|Pointer|<pre lang="Turtle"><code>&#91;] a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;owl:onProperty aec3po:verificationFocus .</code></pre>|
|[Section top](#minorfail-outcome-number-155)|Pointer|<pre lang="Turtle"><code>&#91;] a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;owl:onProperty aec3po:hasSeverity .</code></pre>|
|[Section top](#minorfail-outcome-number-155)|Pointer|<pre lang="Turtle"><code>&#91;] a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;owl:allValuesFrom aec3po:DocumentSubdivision ;  &#10;&#32;&#32;&#32;&#32;owl:onProperty aec3po:hasSubdivision .</code></pre>|
|[Section top](#minorfail-outcome-number-155)|Pointer|<pre lang="Turtle"><code>&#91;] owl:unionOf ( aec3po:Document aec3po:DocumentSubdivision ) .</code></pre>|
|[Section top](#minorfail-outcome-number-155)|Pointer|<pre lang="Turtle"><code>&#91;] owl:allValuesFrom aec3po:Document ;  &#10;&#32;&#32;&#32;&#32;owl:onProperty aec3po:forDocument .</code></pre>|
|[Section top](#minorfail-outcome-number-155)|Pointer|<pre lang="Turtle"><code>&#91;] a owl:Class ;  &#10;&#32;&#32;&#32;&#32;owl:unionOf ( &#60;https://schema.org/Place> aec3po:AdministrativeArea ) .</code></pre>|
|[Section top](#minorfail-outcome-number-155)|Pointer|<pre lang="Turtle"><code>&#91;] a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;owl:onProperty aec3po:hasSubdivision .</code></pre>|
|[Section top](#minorfail-outcome-number-155)|Pointer|<pre lang="Turtle"><code>&#91;] a owl:Class ;  &#10;&#32;&#32;&#32;&#32;owl:unionOf ( aec3po:Table aec3po:Image aec3po:Row aec3po:Column ) .</code></pre>|
|[Section top](#minorfail-outcome-number-155)|Pointer|<pre lang="Turtle"><code>&#91;] a owl:Class ;  &#10;&#32;&#32;&#32;&#32;owl:unionOf ( aec3po:Table aec3po:Image aec3po:Row aec3po:Column aec3po:Cell ) .</code></pre>|
|[Section top](#minorfail-outcome-number-155)|Pointer|<pre lang="Turtle"><code>&#91;] a owl:Class ;  &#10;&#32;&#32;&#32;&#32;owl:unionOf ( aec3po:Table aec3po:Image ) .</code></pre>|

***
### MinorFail Outcome number 156

[Jump to summary definition](#summary-MinorFail-156)	|	[Previous MinorFail outcome](#minorfail-outcome-number-155)	|	[Next MinorFail outcome](#minorfail-outcome-number-157)

:exclamation:MinorFail outcome
#### Subject detail
|Name|all-fragments|
|----|----|
|Title|All the fragments from branch main that are syntaxically correct as well as their recursive imports|
|Composition|- [Module aec3po](https://github.com/Accord-Project/aec3po/blob/main/src/aec3po.ttl)<br/>- [Module checking&lowbar;act](https://github.com/Accord-Project/aec3po/blob/main/src/checking_act.ttl)<br/>- [Module check&lowbar;method](https://github.com/Accord-Project/aec3po/blob/main/src/check_method.ttl)<br/>- [Module compliance&lowbar;verification&lowbar;report](https://github.com/Accord-Project/aec3po/blob/main/src/compliance_verification_report.ttl)<br/>- [Module data&lowbar;requirement](https://github.com/Accord-Project/aec3po/blob/main/src/data_requirement.ttl)<br/>- [Module document](https://github.com/Accord-Project/aec3po/blob/main/src/document.ttl)<br/>- [Module evidence](https://github.com/Accord-Project/aec3po/blob/main/src/evidence.ttl)<br/>- [Module feature&lowbar;of&lowbar;interest](https://github.com/Accord-Project/aec3po/blob/main/src/feature_of_interest.ttl)<br/>- [Module legal&lowbar;verifier](https://github.com/Accord-Project/aec3po/blob/main/src/legal_verifier.ttl)<br/>- [Module model](https://github.com/Accord-Project/aec3po/blob/main/src/model.ttl)<br/>- [Module rase&lowbar;statement](https://github.com/Accord-Project/aec3po/blob/main/src/rase_statement.ttl)<br/>- [Module statement](https://github.com/Accord-Project/aec3po/blob/main/src/statement.ttl)<br/>- [Module table](https://github.com/Accord-Project/aec3po/blob/main/src/table.ttl)<br/>- [Module vocabularies/administrative&lowbar;areas](https://github.com/Accord-Project/aec3po/blob/main/src/vocabularies/administrative_areas.ttl)<br/>- [Module vocabularies/building&lowbar;structure](https://github.com/Accord-Project/aec3po/blob/main/src/vocabularies/building_structure.ttl)<br/>- [Module vocabularies/building&lowbar;usage](https://github.com/Accord-Project/aec3po/blob/main/src/vocabularies/building_usage.ttl)<br/>- [Module vocabularies/check&lowbar;method&lowbar;comparators](https://github.com/Accord-Project/aec3po/blob/main/src/vocabularies/check_method_comparators.ttl)<br/>- [Module vocabularies/check&lowbar;method&lowbar;operators](https://github.com/Accord-Project/aec3po/blob/main/src/vocabularies/check_method_operators.ttl)<br/>- [Module vocabularies/disciplines](https://github.com/Accord-Project/aec3po/blob/main/src/vocabularies/disciplines.ttl)<br/>- [Module vocabularies/permitting&lowbar;stages](https://github.com/Accord-Project/aec3po/blob/main/src/vocabularies/permitting_stages.ttl)<br/>- [Module vocabularies/quantity&lowbar;kinds](https://github.com/Accord-Project/aec3po/blob/main/src/vocabularies/quantity_kinds.ttl)<br/>- [Module vocabularies/&lowbar;shape](https://github.com/Accord-Project/aec3po/blob/main/src/vocabularies/_shape.ttl)|

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
|[Section top](#minorfail-outcome-number-156)|Description|Class Expression not supported as object of rdfs:domain or rdfs:range|
|[Section top](#minorfail-outcome-number-156)|Pointer|<pre lang="Turtle"><code>aec3po:caption a owl:DatatypeProperty ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;caption&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:comment &#34;The caption of a table, image, etc. &#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:domain &#91; a owl:Class ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:unionOf ( aec3po:Table aec3po:Image ) ] ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy aec3po:table .</code></pre>|
|[Section top](#minorfail-outcome-number-156)|Pointer|<pre lang="Turtle"><code>aec3po:contains a owl:ObjectProperty ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;Contains&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:comment &#34;A container contains a table and its caption. A table contai...&#34; ;  &#10;&#32;&#32;&#32;&#32;rdfs:domain &#91; a owl:Class ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:unionOf ( aec3po:Table aec3po:Image aec3po:Row aec3po:Column ) ] ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy aec3po:table .</code></pre>|
|[Section top](#minorfail-outcome-number-156)|Pointer|<pre lang="Turtle"><code>aec3po:hasBSSDDTarget a owl:FunctionalProperty,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:ObjectProperty ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;hasBSSDDTarget&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:comment &#34;The target refers to either the name of an object, the name ...&#34; ;  &#10;&#32;&#32;&#32;&#32;rdfs:domain &#91; a owl:Class ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:unionOf ( aec3po:FeatureOfInterest aec3po:Property aec3po:CheckMethod ) ] ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy aec3po:check&lowbar;method .</code></pre>|
|[Section top](#minorfail-outcome-number-156)|Pointer|<pre lang="Turtle"><code>aec3po:hasFirstSubdivision a owl:FunctionalProperty,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:ObjectProperty ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;has first subdivision&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:comment &#34;Links a document part to the first of its subdivision&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:domain &#91; owl:unionOf ( aec3po:Document aec3po:DocumentSubdivision ) ] ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy aec3po:document ;  &#10;&#32;&#32;&#32;&#32;rdfs:range aec3po:DocumentSubdivision ;  &#10;&#32;&#32;&#32;&#32;rdfs:subPropertyOf aec3po:hasSubdivision .</code></pre>|
|[Section top](#minorfail-outcome-number-156)|Pointer|<pre lang="Turtle"><code>aec3po:hasSubdivision a owl:ObjectProperty ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;has subdivision&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:comment &#34;links a document part to some of its subdivision&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:domain &#91; owl:unionOf ( aec3po:Document aec3po:DocumentSubdivision ) ] ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy aec3po:document ;  &#10;&#32;&#32;&#32;&#32;rdfs:range aec3po:DocumentSubdivision ;  &#10;&#32;&#32;&#32;&#32;rdfs:subPropertyOf dc:hasPart .</code></pre>|
|[Section top](#minorfail-outcome-number-156)|Pointer|<pre lang="Turtle"><code>aec3po:hasUnit a owl:FunctionalProperty,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:ObjectProperty ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;hasUnit&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:comment &#34;the hasUnit property is used to link a specific property or ...&#34; ;  &#10;&#32;&#32;&#32;&#32;rdfs:domain &#91; a owl:Class ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:unionOf ( aec3po:FeatureOfInterest aec3po:Property aec3po:CheckMethod ) ] ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy aec3po:check&lowbar;method ;  &#10;&#32;&#32;&#32;&#32;rdfs:range qudt:Unit ;  &#10;&#32;&#32;&#32;&#32;owl:eqivalentProperty qudt:hasValue .</code></pre>|
|[Section top](#minorfail-outcome-number-156)|Pointer|<pre lang="Turtle"><code>aec3po:hasValue a owl:DatatypeProperty,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:FunctionalProperty ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;has value&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:comment &#34;de facto used to link something (anything: property, propert...&#34; ;  &#10;&#32;&#32;&#32;&#32;rdfs:domain &#91; a owl:Class ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:unionOf ( aec3po:FeatureOfInterest aec3po:Property aec3po:CheckMethod ) ] ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy aec3po: ;  &#10;&#32;&#32;&#32;&#32;skos:note &#34;The value of the literal may be a XSD literal (boolean, inte...&#34; .</code></pre>|
|[Section top](#minorfail-outcome-number-156)|Pointer|<pre lang="Turtle"><code>aec3po:isContainedIn a owl:ObjectProperty ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;is contained by&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:comment &#34;A table contains row, columns and other elements.&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy aec3po:table ;  &#10;&#32;&#32;&#32;&#32;rdfs:range &#91; a owl:Class ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:unionOf ( aec3po:Table aec3po:Image aec3po:Row aec3po:Column aec3po:Cell ) ] .</code></pre>|
|[Section top](#minorfail-outcome-number-156)|Pointer|<pre lang="Turtle"><code>aec3po:locationCoverage a owl:ObjectProperty ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;location coverage&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:comment &#34;The spatialCoverage indicates the place(s) or the administra...&#34; ;  &#10;&#32;&#32;&#32;&#32;rdfs:domain &#60;https://schema.org/Model> ;  &#10;&#32;&#32;&#32;&#32;rdfs:range &#91; a owl:Class ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:unionOf ( &#60;https://schema.org/Place> aec3po:AdministrativeArea ) ] ;  &#10;&#32;&#32;&#32;&#32;owl:equivalentProperty &#60;https://schema.org/spatialCoverage> .</code></pre>|

***
### MinorFail Outcome number 157

[Jump to summary definition](#summary-MinorFail-157)	|	[Previous MinorFail outcome](#minorfail-outcome-number-156)	|	[Next MinorFail outcome](#minorfail-outcome-number-158)

:exclamation:MinorFail outcome
#### Subject detail
|Name|all-fragments|
|----|----|
|Title|All the fragments from branch main that are syntaxically correct as well as their recursive imports|
|Composition|- [Module aec3po](https://github.com/Accord-Project/aec3po/blob/main/src/aec3po.ttl)<br/>- [Module checking&lowbar;act](https://github.com/Accord-Project/aec3po/blob/main/src/checking_act.ttl)<br/>- [Module check&lowbar;method](https://github.com/Accord-Project/aec3po/blob/main/src/check_method.ttl)<br/>- [Module compliance&lowbar;verification&lowbar;report](https://github.com/Accord-Project/aec3po/blob/main/src/compliance_verification_report.ttl)<br/>- [Module data&lowbar;requirement](https://github.com/Accord-Project/aec3po/blob/main/src/data_requirement.ttl)<br/>- [Module document](https://github.com/Accord-Project/aec3po/blob/main/src/document.ttl)<br/>- [Module evidence](https://github.com/Accord-Project/aec3po/blob/main/src/evidence.ttl)<br/>- [Module feature&lowbar;of&lowbar;interest](https://github.com/Accord-Project/aec3po/blob/main/src/feature_of_interest.ttl)<br/>- [Module legal&lowbar;verifier](https://github.com/Accord-Project/aec3po/blob/main/src/legal_verifier.ttl)<br/>- [Module model](https://github.com/Accord-Project/aec3po/blob/main/src/model.ttl)<br/>- [Module rase&lowbar;statement](https://github.com/Accord-Project/aec3po/blob/main/src/rase_statement.ttl)<br/>- [Module statement](https://github.com/Accord-Project/aec3po/blob/main/src/statement.ttl)<br/>- [Module table](https://github.com/Accord-Project/aec3po/blob/main/src/table.ttl)<br/>- [Module vocabularies/administrative&lowbar;areas](https://github.com/Accord-Project/aec3po/blob/main/src/vocabularies/administrative_areas.ttl)<br/>- [Module vocabularies/building&lowbar;structure](https://github.com/Accord-Project/aec3po/blob/main/src/vocabularies/building_structure.ttl)<br/>- [Module vocabularies/building&lowbar;usage](https://github.com/Accord-Project/aec3po/blob/main/src/vocabularies/building_usage.ttl)<br/>- [Module vocabularies/check&lowbar;method&lowbar;comparators](https://github.com/Accord-Project/aec3po/blob/main/src/vocabularies/check_method_comparators.ttl)<br/>- [Module vocabularies/check&lowbar;method&lowbar;operators](https://github.com/Accord-Project/aec3po/blob/main/src/vocabularies/check_method_operators.ttl)<br/>- [Module vocabularies/disciplines](https://github.com/Accord-Project/aec3po/blob/main/src/vocabularies/disciplines.ttl)<br/>- [Module vocabularies/permitting&lowbar;stages](https://github.com/Accord-Project/aec3po/blob/main/src/vocabularies/permitting_stages.ttl)<br/>- [Module vocabularies/quantity&lowbar;kinds](https://github.com/Accord-Project/aec3po/blob/main/src/vocabularies/quantity_kinds.ttl)<br/>- [Module vocabularies/&lowbar;shape](https://github.com/Accord-Project/aec3po/blob/main/src/vocabularies/_shape.ttl)|

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
|[Section top](#minorfail-outcome-number-157)|Description|Class Expression not supported with rdfs:subClassOf|
|[Section top](#minorfail-outcome-number-157)|Pointer|<pre lang="Turtle"><code>aec3po:AndCheckStatement a owl:Class ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;And Check Statement&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:comment &#34;Check verified if and only if all of its sub-checks are veri...&#34; ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy aec3po:statement ;  &#10;&#32;&#32;&#32;&#32;rdfs:subClassOf &#91; a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:onProperty aec3po:hasSubdivision ],  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;aec3po:ChecklistStatement .</code></pre>|
|[Section top](#minorfail-outcome-number-157)|Pointer|<pre lang="Turtle"><code>aec3po:ComplianceVerificationReport a owl:Class ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;Compliance Verification Report&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:comment &#34;Result of a checking act. May be compliant or not.&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy aec3po:compliance&lowbar;verification&lowbar;report ;  &#10;&#32;&#32;&#32;&#32;rdfs:subClassOf &#91; a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:onProperty aec3po:conforms ] .</code></pre>|
|[Section top](#minorfail-outcome-number-157)|Pointer|<pre lang="Turtle"><code>aec3po:DocumentSubdivision a owl:Class ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;Document Subdivision&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:comment &#34;Any subdivision of a document, including sections, paragraph...&#34; ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy aec3po:document ;  &#10;&#32;&#32;&#32;&#32;rdfs:subClassOf &#91; a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:allValuesFrom aec3po:DocumentSubdivision ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:onProperty aec3po:hasSubdivision ] ;  &#10;&#32;&#32;&#32;&#32;skos:example &#34;Paragraph, section, definition...&#34;@en .</code></pre>|
|[Section top](#minorfail-outcome-number-157)|Pointer|<pre lang="Turtle"><code>aec3po:LegalVerifier a owl:Class ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;Legal Verifier&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:comment &#34;An entity that has the legal capacity to verify compliance w...&#34; ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy aec3po:legal&lowbar;verifier ;  &#10;&#32;&#32;&#32;&#32;rdfs:subClassOf &#91; owl:allValuesFrom aec3po:Document ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:onProperty aec3po:forDocument ],  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;foaf:Agent .</code></pre>|
|[Section top](#minorfail-outcome-number-157)|Pointer|<pre lang="Turtle"><code>aec3po:NotCheckStatement a owl:Class ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;Not Check Statement&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:comment &#34;Check verified if and only if the sub-check is not verified.&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy aec3po:statement ;  &#10;&#32;&#32;&#32;&#32;rdfs:subClassOf &#91; a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:onProperty aec3po:hasSubdivision ] .</code></pre>|
|[Section top](#minorfail-outcome-number-157)|Pointer|<pre lang="Turtle"><code>aec3po:OrCheckStatement a owl:Class ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;Or Check Statement&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:comment &#34;Check verified if and only if at least one of its sub-checks...&#34; ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy aec3po:statement ;  &#10;&#32;&#32;&#32;&#32;rdfs:subClassOf &#91; a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:onProperty aec3po:hasSubdivision ],  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;aec3po:ChecklistStatement .</code></pre>|
|[Section top](#minorfail-outcome-number-157)|Pointer|<pre lang="Turtle"><code>aec3po:VerificationResult a owl:Class ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;Verification Result&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:comment &#34;Individual verification result of a Compliance Verification ...&#34; ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy aec3po:compliance&lowbar;verification&lowbar;report ;  &#10;&#32;&#32;&#32;&#32;rdfs:subClassOf &#91; a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:onProperty aec3po:verificationFocus ],  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#91; a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:onProperty aec3po:hasSeverity ] .</code></pre>|

***
### MinorFail Outcome number 158

[Jump to summary definition](#summary-MinorFail-158)	|	[Previous MinorFail outcome](#minorfail-outcome-number-157)	|	[Next MinorFail outcome](#minorfail-outcome-number-159)

:exclamation:MinorFail outcome
#### Subject detail
|Name|all-fragments|
|----|----|
|Title|All the fragments from branch main that are syntaxically correct as well as their recursive imports|
|Composition|- [Module aec3po](https://github.com/Accord-Project/aec3po/blob/main/src/aec3po.ttl)<br/>- [Module checking&lowbar;act](https://github.com/Accord-Project/aec3po/blob/main/src/checking_act.ttl)<br/>- [Module check&lowbar;method](https://github.com/Accord-Project/aec3po/blob/main/src/check_method.ttl)<br/>- [Module compliance&lowbar;verification&lowbar;report](https://github.com/Accord-Project/aec3po/blob/main/src/compliance_verification_report.ttl)<br/>- [Module data&lowbar;requirement](https://github.com/Accord-Project/aec3po/blob/main/src/data_requirement.ttl)<br/>- [Module document](https://github.com/Accord-Project/aec3po/blob/main/src/document.ttl)<br/>- [Module evidence](https://github.com/Accord-Project/aec3po/blob/main/src/evidence.ttl)<br/>- [Module feature&lowbar;of&lowbar;interest](https://github.com/Accord-Project/aec3po/blob/main/src/feature_of_interest.ttl)<br/>- [Module legal&lowbar;verifier](https://github.com/Accord-Project/aec3po/blob/main/src/legal_verifier.ttl)<br/>- [Module model](https://github.com/Accord-Project/aec3po/blob/main/src/model.ttl)<br/>- [Module rase&lowbar;statement](https://github.com/Accord-Project/aec3po/blob/main/src/rase_statement.ttl)<br/>- [Module statement](https://github.com/Accord-Project/aec3po/blob/main/src/statement.ttl)<br/>- [Module table](https://github.com/Accord-Project/aec3po/blob/main/src/table.ttl)<br/>- [Module vocabularies/administrative&lowbar;areas](https://github.com/Accord-Project/aec3po/blob/main/src/vocabularies/administrative_areas.ttl)<br/>- [Module vocabularies/building&lowbar;structure](https://github.com/Accord-Project/aec3po/blob/main/src/vocabularies/building_structure.ttl)<br/>- [Module vocabularies/building&lowbar;usage](https://github.com/Accord-Project/aec3po/blob/main/src/vocabularies/building_usage.ttl)<br/>- [Module vocabularies/check&lowbar;method&lowbar;comparators](https://github.com/Accord-Project/aec3po/blob/main/src/vocabularies/check_method_comparators.ttl)<br/>- [Module vocabularies/check&lowbar;method&lowbar;operators](https://github.com/Accord-Project/aec3po/blob/main/src/vocabularies/check_method_operators.ttl)<br/>- [Module vocabularies/disciplines](https://github.com/Accord-Project/aec3po/blob/main/src/vocabularies/disciplines.ttl)<br/>- [Module vocabularies/permitting&lowbar;stages](https://github.com/Accord-Project/aec3po/blob/main/src/vocabularies/permitting_stages.ttl)<br/>- [Module vocabularies/quantity&lowbar;kinds](https://github.com/Accord-Project/aec3po/blob/main/src/vocabularies/quantity_kinds.ttl)<br/>- [Module vocabularies/&lowbar;shape](https://github.com/Accord-Project/aec3po/blob/main/src/vocabularies/_shape.ttl)|

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
|[Section top](#minorfail-outcome-number-158)|Description|Restriction on datatypes|
|[Section top](#minorfail-outcome-number-158)|Pointer|<pre lang="Turtle"><code>aec3po:conforms a owl:DatatypeProperty ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;conforms&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:comment &#34;True if the Checking act confirms the check was validated, a...&#34; ;  &#10;&#32;&#32;&#32;&#32;rdfs:domain aec3po:ComplianceVerificationReport ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy aec3po:compliance&lowbar;verification&lowbar;report ;  &#10;&#32;&#32;&#32;&#32;rdfs:range xsd:boolean .</code></pre>|
|[Section top](#minorfail-outcome-number-158)|Pointer|<pre lang="Turtle"><code>aec3po:hasBooleanTarget a owl:DatatypeProperty ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;hasBooleanTarget&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:comment &#34;TBD&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:range xsd:boolean .</code></pre>|

***
### MinorFail Outcome number 159

[Jump to summary definition](#summary-MinorFail-159)	|	[Previous MinorFail outcome](#minorfail-outcome-number-158)	|	[Next MinorFail outcome](#minorfail-outcome-number-160)

:exclamation:MinorFail outcome
#### Subject detail
|Name|all-fragments|
|----|----|
|Title|All the fragments from branch main that are syntaxically correct as well as their recursive imports|
|Composition|- [Module aec3po](https://github.com/Accord-Project/aec3po/blob/main/src/aec3po.ttl)<br/>- [Module checking&lowbar;act](https://github.com/Accord-Project/aec3po/blob/main/src/checking_act.ttl)<br/>- [Module check&lowbar;method](https://github.com/Accord-Project/aec3po/blob/main/src/check_method.ttl)<br/>- [Module compliance&lowbar;verification&lowbar;report](https://github.com/Accord-Project/aec3po/blob/main/src/compliance_verification_report.ttl)<br/>- [Module data&lowbar;requirement](https://github.com/Accord-Project/aec3po/blob/main/src/data_requirement.ttl)<br/>- [Module document](https://github.com/Accord-Project/aec3po/blob/main/src/document.ttl)<br/>- [Module evidence](https://github.com/Accord-Project/aec3po/blob/main/src/evidence.ttl)<br/>- [Module feature&lowbar;of&lowbar;interest](https://github.com/Accord-Project/aec3po/blob/main/src/feature_of_interest.ttl)<br/>- [Module legal&lowbar;verifier](https://github.com/Accord-Project/aec3po/blob/main/src/legal_verifier.ttl)<br/>- [Module model](https://github.com/Accord-Project/aec3po/blob/main/src/model.ttl)<br/>- [Module rase&lowbar;statement](https://github.com/Accord-Project/aec3po/blob/main/src/rase_statement.ttl)<br/>- [Module statement](https://github.com/Accord-Project/aec3po/blob/main/src/statement.ttl)<br/>- [Module table](https://github.com/Accord-Project/aec3po/blob/main/src/table.ttl)<br/>- [Module vocabularies/administrative&lowbar;areas](https://github.com/Accord-Project/aec3po/blob/main/src/vocabularies/administrative_areas.ttl)<br/>- [Module vocabularies/building&lowbar;structure](https://github.com/Accord-Project/aec3po/blob/main/src/vocabularies/building_structure.ttl)<br/>- [Module vocabularies/building&lowbar;usage](https://github.com/Accord-Project/aec3po/blob/main/src/vocabularies/building_usage.ttl)<br/>- [Module vocabularies/check&lowbar;method&lowbar;comparators](https://github.com/Accord-Project/aec3po/blob/main/src/vocabularies/check_method_comparators.ttl)<br/>- [Module vocabularies/check&lowbar;method&lowbar;operators](https://github.com/Accord-Project/aec3po/blob/main/src/vocabularies/check_method_operators.ttl)<br/>- [Module vocabularies/disciplines](https://github.com/Accord-Project/aec3po/blob/main/src/vocabularies/disciplines.ttl)<br/>- [Module vocabularies/permitting&lowbar;stages](https://github.com/Accord-Project/aec3po/blob/main/src/vocabularies/permitting_stages.ttl)<br/>- [Module vocabularies/quantity&lowbar;kinds](https://github.com/Accord-Project/aec3po/blob/main/src/vocabularies/quantity_kinds.ttl)<br/>- [Module vocabularies/&lowbar;shape](https://github.com/Accord-Project/aec3po/blob/main/src/vocabularies/_shape.ttl)|

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
|[Section top](#minorfail-outcome-number-159)|Description|Class Expression not supported with owl:equivalentClass|
|[Section top](#minorfail-outcome-number-159)|Pointer|<pre lang="Turtle"><code>aec3po:ComponentCheckMethod a owl:Class ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;Component Check Method&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:comment &#34;Component check method refers to a process of inspecting and...&#34; ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy aec3po:check&lowbar;method ;  &#10;&#32;&#32;&#32;&#32;rdfs:subClassOf aec3po:CheckMethod ;  &#10;&#32;&#32;&#32;&#32;owl:equivalentClass &#91; a owl:Class ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:intersectionOf ( aec3po:CheckMethod &#91; a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:allValuesFrom &#91; a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:allValuesFrom aec3po:FeatureOfInterest ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:onProperty &#91; owl:inverseOf aec3po:forDesign ] ] ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:onProperty aec3po:forDesign ] ) ] .</code></pre>|

***
### MinorFail Outcome number 160

[Jump to summary definition](#summary-MinorFail-160)	|	[Previous MinorFail outcome](#minorfail-outcome-number-159)	|	[Next MinorFail outcome](#minorfail-outcome-number-161)

:exclamation:MinorFail outcome
#### Subject detail
|Name|all-fragments|
|----|----|
|Title|All the fragments from branch main that are syntaxically correct as well as their recursive imports|
|Composition|- [Module aec3po](https://github.com/Accord-Project/aec3po/blob/main/src/aec3po.ttl)<br/>- [Module checking&lowbar;act](https://github.com/Accord-Project/aec3po/blob/main/src/checking_act.ttl)<br/>- [Module check&lowbar;method](https://github.com/Accord-Project/aec3po/blob/main/src/check_method.ttl)<br/>- [Module compliance&lowbar;verification&lowbar;report](https://github.com/Accord-Project/aec3po/blob/main/src/compliance_verification_report.ttl)<br/>- [Module data&lowbar;requirement](https://github.com/Accord-Project/aec3po/blob/main/src/data_requirement.ttl)<br/>- [Module document](https://github.com/Accord-Project/aec3po/blob/main/src/document.ttl)<br/>- [Module evidence](https://github.com/Accord-Project/aec3po/blob/main/src/evidence.ttl)<br/>- [Module feature&lowbar;of&lowbar;interest](https://github.com/Accord-Project/aec3po/blob/main/src/feature_of_interest.ttl)<br/>- [Module legal&lowbar;verifier](https://github.com/Accord-Project/aec3po/blob/main/src/legal_verifier.ttl)<br/>- [Module model](https://github.com/Accord-Project/aec3po/blob/main/src/model.ttl)<br/>- [Module rase&lowbar;statement](https://github.com/Accord-Project/aec3po/blob/main/src/rase_statement.ttl)<br/>- [Module statement](https://github.com/Accord-Project/aec3po/blob/main/src/statement.ttl)<br/>- [Module table](https://github.com/Accord-Project/aec3po/blob/main/src/table.ttl)<br/>- [Module vocabularies/administrative&lowbar;areas](https://github.com/Accord-Project/aec3po/blob/main/src/vocabularies/administrative_areas.ttl)<br/>- [Module vocabularies/building&lowbar;structure](https://github.com/Accord-Project/aec3po/blob/main/src/vocabularies/building_structure.ttl)<br/>- [Module vocabularies/building&lowbar;usage](https://github.com/Accord-Project/aec3po/blob/main/src/vocabularies/building_usage.ttl)<br/>- [Module vocabularies/check&lowbar;method&lowbar;comparators](https://github.com/Accord-Project/aec3po/blob/main/src/vocabularies/check_method_comparators.ttl)<br/>- [Module vocabularies/check&lowbar;method&lowbar;operators](https://github.com/Accord-Project/aec3po/blob/main/src/vocabularies/check_method_operators.ttl)<br/>- [Module vocabularies/disciplines](https://github.com/Accord-Project/aec3po/blob/main/src/vocabularies/disciplines.ttl)<br/>- [Module vocabularies/permitting&lowbar;stages](https://github.com/Accord-Project/aec3po/blob/main/src/vocabularies/permitting_stages.ttl)<br/>- [Module vocabularies/quantity&lowbar;kinds](https://github.com/Accord-Project/aec3po/blob/main/src/vocabularies/quantity_kinds.ttl)<br/>- [Module vocabularies/&lowbar;shape](https://github.com/Accord-Project/aec3po/blob/main/src/vocabularies/_shape.ttl)|

#### Criterion detail
|Identifier|[term-referencing](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#term-referencing)|
|----|----|
|Title|Term referencing test|
|Description|A test case from the Best Practices tests checking if each term of the test subject is referenced to a module through a rdfs:isDefinedBy property.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-160)|Identifier|`no-reference-module`|
|[Section top](#minorfail-outcome-number-160)|Title|Term not referenced to a module|
|[Section top](#minorfail-outcome-number-160)|Description|Subject terms not linked to a module by a rdfs:isDefinedBy property|
|[Section top](#minorfail-outcome-number-160)|Pointer|<pre lang="Turtle"><code>:edlira a schema:Person ;  &#10;&#32;&#32;&#32;&#32;schema:affiliation &#60;https://www.bcu.ac.uk/> ;  &#10;&#32;&#32;&#32;&#32;schema:email &#34;edlira.vakaj@bcu.ac.uk&#34; ;  &#10;&#32;&#32;&#32;&#32;schema:identifier &#60;http://orcid.org/0000-0002-0712-0959> ;  &#10;&#32;&#32;&#32;&#32;schema:name &#34;Edlira Vakaj&#34; ;  &#10;&#32;&#32;&#32;&#32;schema:url &#60;https://www.bcu.ac.uk/computing/about-us/our-staff/edlira-vakaj> .</code></pre>|
|[Section top](#minorfail-outcome-number-160)|Pointer|<pre lang="Turtle"><code>:pan a schema:Person ;  &#10;&#32;&#32;&#32;&#32;schema:affiliation &#60;https://www.bcu.ac.uk/> ;  &#10;&#32;&#32;&#32;&#32;schema:email &#34;Panagiotis.Patlakas@bcu.ac.uk&#34; ;  &#10;&#32;&#32;&#32;&#32;schema:identifier &#60;http://orcid.org/0000-0002-7248-8952> ;  &#10;&#32;&#32;&#32;&#32;schema:name &#34;Panagiotis Patlakas&#34; ;  &#10;&#32;&#32;&#32;&#32;schema:url &#60;https://www.bcu.ac.uk/built-environment/about-us/our-staff/panagiotis-patlakas> .</code></pre>|
|[Section top](#minorfail-outcome-number-160)|Pointer|<pre lang="Turtle"><code>:amna a schema:Person ;  &#10;&#32;&#32;&#32;&#32;schema:affiliation &#60;https://www.bcu.ac.uk/> ;  &#10;&#32;&#32;&#32;&#32;schema:email &#34;Amna.Dridi@bcu.ac.uk&#34; ;  &#10;&#32;&#32;&#32;&#32;schema:identifier &#60;http://orcid.org/0000-0002-0185-103X> ;  &#10;&#32;&#32;&#32;&#32;schema:name &#34;Amna Dridi&#34; ;  &#10;&#32;&#32;&#32;&#32;schema:url &#60;https://www.researchgate.net/profile/Amna-Dridi-3> .</code></pre>|
|[Section top](#minorfail-outcome-number-160)|Pointer|<pre lang="Turtle"><code>:thomas a schema:Person ;  &#10;&#32;&#32;&#32;&#32;schema:affiliation &#60;https://www.cardiff.ac.uk/> ;  &#10;&#32;&#32;&#32;&#32;schema:email &#34;beachth@cardiff.ac.uk&#34; ;  &#10;&#32;&#32;&#32;&#32;schema:identifier &#60;http://orcid.org/0000-0001-5610-8027> ;  &#10;&#32;&#32;&#32;&#32;schema:name &#34;Thomas Beach&#34; ;  &#10;&#32;&#32;&#32;&#32;schema:url &#60;https://profiles.cardiff.ac.uk/staff/beachth> .</code></pre>|
|[Section top](#minorfail-outcome-number-160)|Pointer|<pre lang="Turtle"><code>:vladimir a schema:Person ;  &#10;&#32;&#32;&#32;&#32;schema:affiliation &#60;https://www.ontotext.com/> ;  &#10;&#32;&#32;&#32;&#32;schema:email &#34;vladimir.alexiev@ontotext.com&#34; ;  &#10;&#32;&#32;&#32;&#32;schema:identifier &#60;https://orcid.org/0000-0001-7508-7428> ;  &#10;&#32;&#32;&#32;&#32;schema:name &#34;Vladimir Alexiev&#34; ;  &#10;&#32;&#32;&#32;&#32;schema:url &#60;https://www.ontotext.com/blog/author/vladimir/> .</code></pre>|
|[Section top](#minorfail-outcome-number-160)|Pointer|<pre lang="Turtle"><code>:hasTarget a owl:DatatypeProperty ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;hasTarget&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:comment &#34;TBD&#34;@en .</code></pre>|
|[Section top](#minorfail-outcome-number-160)|Pointer|<pre lang="Turtle"><code>:hasBooleanTarget a owl:DatatypeProperty ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;hasBooleanTarget&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:comment &#34;TBD&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:range xsd:boolean .</code></pre>|
|[Section top](#minorfail-outcome-number-160)|Pointer|<pre lang="Turtle"><code>:name a owl:DatatypeProperty ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;name&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:comment &#34;The name or the identifier of the BIM model.&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:domain &#60;https://schema.org/Model> ;  &#10;&#32;&#32;&#32;&#32;rdfs:range xsd:string ;  &#10;&#32;&#32;&#32;&#32;owl:equivalentProperty &#60;https://schema.org/about> ;  &#10;&#32;&#32;&#32;&#32;owl:inverseOf &#60;https://schema.org/subjectOf> .</code></pre>|
|[Section top](#minorfail-outcome-number-160)|Pointer|<pre lang="Turtle"><code>:description a owl:DatatypeProperty ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;description&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:comment &#34;A textual description providing additional details about the...&#34; ;  &#10;&#32;&#32;&#32;&#32;rdfs:domain &#60;https://schema.org/Model> ;  &#10;&#32;&#32;&#32;&#32;rdfs:range xsd:string ;  &#10;&#32;&#32;&#32;&#32;owl:equivalentProperty &#60;https://schema.org/abstract> .</code></pre>|
|[Section top](#minorfail-outcome-number-160)|Pointer|<pre lang="Turtle"><code>:location a owl:ObjectProperty ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;location&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:comment &#34;The physical or geographic location of the building or struc...&#34; ;  &#10;&#32;&#32;&#32;&#32;rdfs:domain &#60;https://schema.org/Model> ;  &#10;&#32;&#32;&#32;&#32;rdfs:range &#60;https://schema.org/Place> ;  &#10;&#32;&#32;&#32;&#32;owl:equivalentProperty &#60;https://schema.org/spatial> .</code></pre>|
|[Section top](#minorfail-outcome-number-160)|Pointer|<pre lang="Turtle"><code>:locationCoverage a owl:ObjectProperty ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;location coverage&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:comment &#34;The spatialCoverage indicates the place(s) or the administra...&#34; ;  &#10;&#32;&#32;&#32;&#32;rdfs:domain &#60;https://schema.org/Model> ;  &#10;&#32;&#32;&#32;&#32;rdfs:range &#91; a owl:Class ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:unionOf ( &#60;https://schema.org/Place> :AdministrativeArea ) ] ;  &#10;&#32;&#32;&#32;&#32;owl:equivalentProperty &#60;https://schema.org/spatialCoverage> .</code></pre>|
|[Section top](#minorfail-outcome-number-160)|Pointer|<pre lang="Turtle"><code>:material a owl:DatatypeProperty ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;material&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:comment &#34;The materials used for different parts of the building, such...&#34; ;  &#10;&#32;&#32;&#32;&#32;rdfs:domain &#60;https://schema.org/Model> ;  &#10;&#32;&#32;&#32;&#32;rdfs:range xsd:string ;  &#10;&#32;&#32;&#32;&#32;owl:equivalentProperty &#60;https://schema.org/material> .</code></pre>|
|[Section top](#minorfail-outcome-number-160)|Pointer|<pre lang="Turtle"><code>:hasBuildingPhase a owl:ObjectProperty ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;has building phase&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:comment &#34;describes the relationship between a construction-related en...&#34; ;  &#10;&#32;&#32;&#32;&#32;rdfs:domain :Model ;  &#10;&#32;&#32;&#32;&#32;rdfs:range :Phase .</code></pre>|
|[Section top](#minorfail-outcome-number-160)|Pointer|<pre lang="Turtle"><code>:hasElementPhase a owl:ObjectProperty ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;has element phase&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:comment &#34;is used to establish a relationship between a construction e...&#34; ;  &#10;&#32;&#32;&#32;&#32;rdfs:domain :Model ;  &#10;&#32;&#32;&#32;&#32;rdfs:range :Phase .</code></pre>|
|[Section top](#minorfail-outcome-number-160)|Pointer|<pre lang="Turtle"><code>:hasDimension a owl:ObjectProperty ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;has dimension&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:comment &#34;is used to represent the physical dimensions or measurements...&#34; ;  &#10;&#32;&#32;&#32;&#32;rdfs:domain :Model ;  &#10;&#32;&#32;&#32;&#32;rdfs:range :Dimension .</code></pre>|
|[Section top](#minorfail-outcome-number-160)|Pointer|<pre lang="Turtle"><code>:hasClassification a owl:ObjectProperty ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;has dimension&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:comment &#34;is used to link building components, elements, or other enti...&#34; ;  &#10;&#32;&#32;&#32;&#32;rdfs:domain :Model ;  &#10;&#32;&#32;&#32;&#32;rdfs:range :Classification .</code></pre>|

***
### MinorFail Outcome number 161

[Jump to summary definition](#summary-MinorFail-161)	|	[Previous MinorFail outcome](#minorfail-outcome-number-160)	|	Next MinorFail outcome

:exclamation:MinorFail outcome
#### Subject detail
|Name|all-fragments|
|----|----|
|Title|All the fragments from branch main that are syntaxically correct as well as their recursive imports|
|Composition|- [Module aec3po](https://github.com/Accord-Project/aec3po/blob/main/src/aec3po.ttl)<br/>- [Module checking&lowbar;act](https://github.com/Accord-Project/aec3po/blob/main/src/checking_act.ttl)<br/>- [Module check&lowbar;method](https://github.com/Accord-Project/aec3po/blob/main/src/check_method.ttl)<br/>- [Module compliance&lowbar;verification&lowbar;report](https://github.com/Accord-Project/aec3po/blob/main/src/compliance_verification_report.ttl)<br/>- [Module data&lowbar;requirement](https://github.com/Accord-Project/aec3po/blob/main/src/data_requirement.ttl)<br/>- [Module document](https://github.com/Accord-Project/aec3po/blob/main/src/document.ttl)<br/>- [Module evidence](https://github.com/Accord-Project/aec3po/blob/main/src/evidence.ttl)<br/>- [Module feature&lowbar;of&lowbar;interest](https://github.com/Accord-Project/aec3po/blob/main/src/feature_of_interest.ttl)<br/>- [Module legal&lowbar;verifier](https://github.com/Accord-Project/aec3po/blob/main/src/legal_verifier.ttl)<br/>- [Module model](https://github.com/Accord-Project/aec3po/blob/main/src/model.ttl)<br/>- [Module rase&lowbar;statement](https://github.com/Accord-Project/aec3po/blob/main/src/rase_statement.ttl)<br/>- [Module statement](https://github.com/Accord-Project/aec3po/blob/main/src/statement.ttl)<br/>- [Module table](https://github.com/Accord-Project/aec3po/blob/main/src/table.ttl)<br/>- [Module vocabularies/administrative&lowbar;areas](https://github.com/Accord-Project/aec3po/blob/main/src/vocabularies/administrative_areas.ttl)<br/>- [Module vocabularies/building&lowbar;structure](https://github.com/Accord-Project/aec3po/blob/main/src/vocabularies/building_structure.ttl)<br/>- [Module vocabularies/building&lowbar;usage](https://github.com/Accord-Project/aec3po/blob/main/src/vocabularies/building_usage.ttl)<br/>- [Module vocabularies/check&lowbar;method&lowbar;comparators](https://github.com/Accord-Project/aec3po/blob/main/src/vocabularies/check_method_comparators.ttl)<br/>- [Module vocabularies/check&lowbar;method&lowbar;operators](https://github.com/Accord-Project/aec3po/blob/main/src/vocabularies/check_method_operators.ttl)<br/>- [Module vocabularies/disciplines](https://github.com/Accord-Project/aec3po/blob/main/src/vocabularies/disciplines.ttl)<br/>- [Module vocabularies/permitting&lowbar;stages](https://github.com/Accord-Project/aec3po/blob/main/src/vocabularies/permitting_stages.ttl)<br/>- [Module vocabularies/quantity&lowbar;kinds](https://github.com/Accord-Project/aec3po/blob/main/src/vocabularies/quantity_kinds.ttl)<br/>- [Module vocabularies/&lowbar;shape](https://github.com/Accord-Project/aec3po/blob/main/src/vocabularies/_shape.ttl)|

#### Criterion detail
|Identifier|[terms-differenciation](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#terms-differenciation)|
|----|----|
|Title|Terms differenciation test|
|Description|A test case from the Best Practices tests checking if all the terms are different enough from each other according to the Levenshtein distance metric.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-161)|Identifier|`too-close-terms`|
|[Section top](#minorfail-outcome-number-161)|Title|Too close terms|
|[Section top](#minorfail-outcome-number-161)|Description|Some terms are too similar|
|[Section top](#minorfail-outcome-number-161)|Pointer|<pre lang="Turtle"><code>:CheckMethodComparator-gt a owl:NamedIndividual,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;skos:Concept,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;:CheckMethodComparator ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy :check&lowbar;method&lowbar;comparators ;  &#10;&#32;&#32;&#32;&#32;skos:definition &#34;greater-than comparator.&#34;@en ;  &#10;&#32;&#32;&#32;&#32;skos:inScheme :CheckMethodComparatorNomenclature ;  &#10;&#32;&#32;&#32;&#32;skos:prefLabel &#34;greater than&#34;@en ;  &#10;&#32;&#32;&#32;&#32;skos:topConceptOf :CheckMethodComparatorNomenclature .</code></pre>|
|[Section top](#minorfail-outcome-number-161)|Pointer|<pre lang="Turtle"><code>:CheckMethodComparator-ge a owl:NamedIndividual,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;skos:Concept,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;:CheckMethodComparator ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy :check&lowbar;method&lowbar;comparators ;  &#10;&#32;&#32;&#32;&#32;skos:definition &#34;greater-equal comparator.&#34;@en ;  &#10;&#32;&#32;&#32;&#32;skos:inScheme :CheckMethodComparatorNomenclature ;  &#10;&#32;&#32;&#32;&#32;skos:prefLabel &#34;greater equal&#34;@en ;  &#10;&#32;&#32;&#32;&#32;skos:topConceptOf :CheckMethodComparatorNomenclature .</code></pre>|
|[Section top](#minorfail-outcome-number-161)|Pointer|<pre lang="Turtle"><code>:CheckMethodComparator-le a owl:NamedIndividual,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;skos:Concept,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;:CheckMethodComparator ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy :check&lowbar;method&lowbar;comparators ;  &#10;&#32;&#32;&#32;&#32;skos:definition &#34;less-equal comparator.&#34;@en ;  &#10;&#32;&#32;&#32;&#32;skos:inScheme :CheckMethodComparatorNomenclature ;  &#10;&#32;&#32;&#32;&#32;skos:prefLabel &#34;less equal&#34;@en ;  &#10;&#32;&#32;&#32;&#32;skos:topConceptOf :CheckMethodComparatorNomenclature .</code></pre>|
|[Section top](#minorfail-outcome-number-161)|Pointer|<pre lang="Turtle"><code>:CheckMethodComparator-lt a owl:NamedIndividual,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;skos:Concept,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;:CheckMethodComparator ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy :check&lowbar;method&lowbar;comparators ;  &#10;&#32;&#32;&#32;&#32;skos:definition &#34;less-than comparator.&#34;@en ;  &#10;&#32;&#32;&#32;&#32;skos:inScheme :CheckMethodComparatorNomenclature ;  &#10;&#32;&#32;&#32;&#32;skos:prefLabel &#34;less than&#34;@en ;  &#10;&#32;&#32;&#32;&#32;skos:topConceptOf :CheckMethodComparatorNomenclature .</code></pre>|
|[Section top](#minorfail-outcome-number-161)|Pointer|<pre lang="Turtle"><code>:CheckMethodComparator-neq a owl:NamedIndividual,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;skos:Concept,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;:CheckMethodComparator ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy :check&lowbar;method&lowbar;comparators ;  &#10;&#32;&#32;&#32;&#32;skos:definition &#34;not equal-to comparator.&#34;@en ;  &#10;&#32;&#32;&#32;&#32;skos:inScheme :CheckMethodComparatorNomenclature ;  &#10;&#32;&#32;&#32;&#32;skos:prefLabel &#34;not equal-to&#34;@en ;  &#10;&#32;&#32;&#32;&#32;skos:topConceptOf :CheckMethodComparatorNomenclature .</code></pre>|
|[Section top](#minorfail-outcome-number-161)|Pointer|<pre lang="Turtle"><code>:CheckMethodcomparator-eq a owl:NamedIndividual,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;skos:Concept,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;:CheckMethodcomparator ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy :check&lowbar;method&lowbar;comparators ;  &#10;&#32;&#32;&#32;&#32;skos:definition &#34;equal-to comparator.&#34;@en ;  &#10;&#32;&#32;&#32;&#32;skos:inScheme :CheckMethodComparatorNomenclature ;  &#10;&#32;&#32;&#32;&#32;skos:prefLabel &#34;equal-to&#34;@en ;  &#10;&#32;&#32;&#32;&#32;skos:topConceptOf :CheckMethodComparatorNomenclature .</code></pre>|
|[Section top](#minorfail-outcome-number-161)|Pointer|<pre lang="Turtle"><code>:OrCheckStatement a owl:Class ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;Or Check Statement&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:comment &#34;Check verified if and only if at least one of its sub-checks...&#34; ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy :statement ;  &#10;&#32;&#32;&#32;&#32;rdfs:subClassOf &#91; a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:onProperty :hasSubdivision ],  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;:ChecklistStatement .</code></pre>|
|[Section top](#minorfail-outcome-number-161)|Pointer|<pre lang="Turtle"><code>:CheckStatement a owl:Class ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;Check Statement&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:comment &#34;refers to a type of statement that is used to specify condit...&#34; ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy :statement ;  &#10;&#32;&#32;&#32;&#32;rdfs:subClassOf :Statement .</code></pre>|
|[Section top](#minorfail-outcome-number-161)|Pointer|<pre lang="Turtle"><code>:PartialSafetyFactor0 a owl:NamedIndividual,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;skos:Concept,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;:QuantityKind ;  &#10;&#32;&#32;&#32;&#32;qudt:applicableUnit &#60;http://qudt.org/vocab/unit/UNITLESS> ;  &#10;&#32;&#32;&#32;&#32;qudt:hasDimensionVector &#60;http://qudt.org/vocab/dimensionvector/A0E0L0I0M0H0T0D0> ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy :quantity&lowbar;kinds ;  &#10;&#32;&#32;&#32;&#32;skos:broader :PartialSafetyFactor ;  &#10;&#32;&#32;&#32;&#32;skos:definition &#34;Also written γM0, the partial safety factor for resistance r...&#34; ;  &#10;&#32;&#32;&#32;&#32;skos:prefLabel &#34;Partial Safety Factor&#34;@en .</code></pre>|
|[Section top](#minorfail-outcome-number-161)|Pointer|<pre lang="Turtle"><code>:PartialSafetyFactor a owl:NamedIndividual,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;skos:Concept,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;:QuantityKind ;  &#10;&#32;&#32;&#32;&#32;qudt:applicableUnit &#60;http://qudt.org/vocab/unit/UNITLESS> ;  &#10;&#32;&#32;&#32;&#32;qudt:hasDimensionVector &#60;http://qudt.org/vocab/dimensionvector/A0E0L0I0M0H0T0D0> ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy :quantity&lowbar;kinds ;  &#10;&#32;&#32;&#32;&#32;skos:definition &#34;Also written γM, the partial safety factor for resistance.&#34;@en ;  &#10;&#32;&#32;&#32;&#32;skos:prefLabel &#34;Partial Safety Factor&#34;@en .</code></pre>|
|[Section top](#minorfail-outcome-number-161)|Pointer|<pre lang="Turtle"><code>:PartialSafetyFactor1 a owl:NamedIndividual,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;skos:Concept,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;:QuantityKind ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;Partial Safety Factor&#34;@en ;  &#10;&#32;&#32;&#32;&#32;qudt:applicableUnit &#60;http://qudt.org/vocab/unit/UNITLESS> ;  &#10;&#32;&#32;&#32;&#32;qudt:hasDimensionVector &#60;http://qudt.org/vocab/dimensionvector/A0E0L0I0M0H0T0D0> ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy :quantity&lowbar;kinds ;  &#10;&#32;&#32;&#32;&#32;skos:broader :PartialSafetyFactor ;  &#10;&#32;&#32;&#32;&#32;skos:definition &#34;Also written γM1, the partial safety factor for resistance r...&#34; .</code></pre>|
|[Section top](#minorfail-outcome-number-161)|Pointer|<pre lang="Turtle"><code>:QuantityKind a owl:Class ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;Quantity Kind&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:comment &#34;A Quantity Kind is any observable property that can be quant...&#34;,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#34;A kind of quantity.&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy :feature&lowbar;of&lowbar;interest,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;:quantity&lowbar;kinds ;  &#10;&#32;&#32;&#32;&#32;rdfs:subClassOf qudt:QuantityKind,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#60;http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#Region>,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;skos:Concept ;  &#10;&#32;&#32;&#32;&#32;owl:equivalentClass &#91; owl:intersectionOf ( skos:Concept &#91; a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:hasValue :QuantityKindNomenclature ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:onProperty skos:inScheme ] ) ] ;  &#10;&#32;&#32;&#32;&#32;skos:example &#34;Length, Area, U-Value.&#34;@en,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#34;height, area, U-value&#34;@en ;  &#10;&#32;&#32;&#32;&#32;skos:note &#34;Maxime Lefrançois argues that both qudt:QuantityKind and qud...&#34; .</code></pre>|
|[Section top](#minorfail-outcome-number-161)|Pointer|<pre lang="Turtle"><code>:severity a owl:ObjectProperty ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;severity&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:comment &#34;Each verification result has exactly one value for the prope...&#34; ;  &#10;&#32;&#32;&#32;&#32;rdfs:domain :VerificationResult ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy :compliance&lowbar;verification&lowbar;report ;  &#10;&#32;&#32;&#32;&#32;rdfs:range :Severity .</code></pre>|
|[Section top](#minorfail-outcome-number-161)|Pointer|<pre lang="Turtle"><code>:Severity a owl:Class ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;Severity&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:comment &#34;The class of validation result severity levels, including vi...&#34; ;  &#10;&#32;&#32;&#32;&#32;rdfs:isDefinedBy :compliance&lowbar;verification&lowbar;report .</code></pre>|

***

</details>

***
