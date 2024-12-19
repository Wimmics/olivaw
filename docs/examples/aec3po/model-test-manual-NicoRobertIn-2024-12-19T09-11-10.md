# Test Report Markdown Export

This file is an export of the RDF test report made out of [EARL vocabulary](https://www.w3.org/TR/EARL10/)

This test is powered by Corese, check [Corese website](https://project.inria.fr/corese/) and [Corese repository](https://github.com/Wimmics/corese)

The original test report is available in turtle syntax [here](./model-test-manual-NicoRobertIn-2024-12-19T09-11-10.ttl).

# Test Activity

Here is some information about the testing activity that led to this report

|Title|Model&#32;tests&#32;of&#32;[Accord-Project/aec3po](https://github.com/Accord-Project/aec3po)&#32;on&#32;branch&#32;HEAD|
|--|--|
|Description|[NicoRobertIn](https://github.com/NicoRobertIn)&#32;launch&#32;manual&#32;run&#32;of&#32;model&#32;tests&#32;against&#32;[Accord-Project/aec3po](https://github.com/Accord-Project/aec3po)&#32;on&#32;branch&#32;HEAD|
|Tester|[NicoRobertIn](https://github.com/NicoRobertIn)|
|Ontology|[Accord-Project/aec3po](https://github.com/Accord-Project/aec3po)|
|Ontology version|Local state `f59cb31e783bd6fe54e8c5c413eeddc401c57f13`|
|Ontology version date|2024-12-19 09:10:42|
|Ontology previous version|[ef1ac8a152d8a37bf92cdaa007ecf5573c741bc8](https://github.com/Accord-Project/aec3po/tree/ef1ac8a152d8a37bf92cdaa007ecf5573c741bc8)|
|Ontology branch|[HEAD](https://github.com/Accord-Project/aec3po/tree/HEAD)|
|Olivaw suite|[olivaw model test suite](https://github.com/Wimmics/olivaw/blob/v0.0.7/olivaw/test/model/suite.py)|
|Olivaw version|[v0.0.7](https://pypi.org/project/olivaw/0.0.7)|
|Generated turtle|[Turtle report](./model-test-manual-NicoRobertIn-2024-12-19T09-11-10.ttl)|
|Generated Markdown|[Markdown report](./model-test-manual-NicoRobertIn-2024-12-19T09-11-10.md)|

# Statistic summary

Here is a short overview for this test report

161 Outcomes

:boom:0 MajorFail, :exclamation:161 MinorFail, :warning:0 CannotTell, :grey_question:0 NotTested, :white_check_mark:0 Pass

<div  style="border-radius: 12px; height: 25px; overflow: hidden"><img src="../assets/red.png" width="0%" height="25px"/><img src="../assets/orange.png" width="100%" height="25px"/><img src="../assets/grey.png" width="0%" height="25px"/><img src="../assets/white.png" width="0%" height="25px"/><img src="../assets/green.png" width="0%" height="25px"/></div>

<br/>

The different status types are an extension of the [EARL](https://www.w3.org/TR/EARL10-Schema/) vocabulary where the nextended terms can be found in the [olivaw ontology](https://ns.inria.fr/olivaw#), each outcome type means:
* :boom: MajorFail: This is an error that is critical and considered as blocking for production
* :exclamation: MinorFail: This is an error that should be fixed, but it cannot be considered as critical error
* :warning: CannotTell: It is unclear if the subject passed or failed the test. This happens when an automated test requires human judgement to make a final decision.
* :grey_question: NotTested:  The test has not been carried out. It is because some prerequisite tests did not end up as Pass.
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
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-1">1/161</div>|:exclamation:MinorFail|`module-src-vocabularies-quantity-kinds`|[labeled-terms](https://ns.inria.fr/olivaw#labeled-terms)|Terms not labeled|[Jump](#minorfail-outcome-number-1)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-2">2/161</div>|:exclamation:MinorFail|`module-src-vocabularies-quantity-kinds`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL QL Profile incompatible|[Jump](#minorfail-outcome-number-2)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-3">3/161</div>|:exclamation:MinorFail|`module-src-vocabularies-quantity-kinds`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL QL Profile incompatible|[Jump](#minorfail-outcome-number-3)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-4">4/161</div>|:exclamation:MinorFail|`module-src-vocabularies-quantity-kinds`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL QL Profile incompatible|[Jump](#minorfail-outcome-number-4)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-5">5/161</div>|:exclamation:MinorFail|`module-src-vocabularies-quantity-kinds`|[terms-differenciation](https://ns.inria.fr/olivaw#terms-differenciation)|Too close terms|[Jump](#minorfail-outcome-number-5)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-6">6/161</div>|:exclamation:MinorFail|`module-src-vocabularies-permitting-stages`|[domain-and-range-referencing](https://ns.inria.fr/olivaw#domain-and-range-referencing)|Range out of vocabulary|[Jump](#minorfail-outcome-number-6)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-7">7/161</div>|:exclamation:MinorFail|`module-src-vocabularies-permitting-stages`|[labeled-terms](https://ns.inria.fr/olivaw#labeled-terms)|Terms not labeled|[Jump](#minorfail-outcome-number-7)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-8">8/161</div>|:exclamation:MinorFail|`module-src-vocabularies-permitting-stages`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL QL Profile incompatible|[Jump](#minorfail-outcome-number-8)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-9">9/161</div>|:exclamation:MinorFail|`module-src-vocabularies-permitting-stages`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL QL Profile incompatible|[Jump](#minorfail-outcome-number-9)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-10">10/161</div>|:exclamation:MinorFail|`module-src-vocabularies-permitting-stages`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL QL Profile incompatible|[Jump](#minorfail-outcome-number-10)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-11">11/161</div>|:exclamation:MinorFail|`module-src-vocabularies-disciplines`|[domain-and-range-referencing](https://ns.inria.fr/olivaw#domain-and-range-referencing)|Range out of vocabulary|[Jump](#minorfail-outcome-number-11)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-12">12/161</div>|:exclamation:MinorFail|`module-src-vocabularies-disciplines`|[labeled-terms](https://ns.inria.fr/olivaw#labeled-terms)|Terms not labeled|[Jump](#minorfail-outcome-number-12)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-13">13/161</div>|:exclamation:MinorFail|`module-src-vocabularies-disciplines`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL QL Profile incompatible|[Jump](#minorfail-outcome-number-13)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-14">14/161</div>|:exclamation:MinorFail|`module-src-vocabularies-disciplines`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL QL Profile incompatible|[Jump](#minorfail-outcome-number-14)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-15">15/161</div>|:exclamation:MinorFail|`module-src-vocabularies-disciplines`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL QL Profile incompatible|[Jump](#minorfail-outcome-number-15)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-16">16/161</div>|:exclamation:MinorFail|`module-src-vocabularies-check-method-operators`|[labeled-terms](https://ns.inria.fr/olivaw#labeled-terms)|Terms not labeled|[Jump](#minorfail-outcome-number-16)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-17">17/161</div>|:exclamation:MinorFail|`module-src-vocabularies-check-method-operators`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL EL Profile incompatible|[Jump](#minorfail-outcome-number-17)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-18">18/161</div>|:exclamation:MinorFail|`module-src-vocabularies-check-method-operators`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL QL Profile incompatible|[Jump](#minorfail-outcome-number-18)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-19">19/161</div>|:exclamation:MinorFail|`module-src-vocabularies-check-method-operators`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL QL Profile incompatible|[Jump](#minorfail-outcome-number-19)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-20">20/161</div>|:exclamation:MinorFail|`module-src-vocabularies-check-method-operators`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL QL Profile incompatible|[Jump](#minorfail-outcome-number-20)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-21">21/161</div>|:exclamation:MinorFail|`module-src-vocabularies-check-method-comparators`|[labeled-terms](https://ns.inria.fr/olivaw#labeled-terms)|Terms not labeled|[Jump](#minorfail-outcome-number-21)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-22">22/161</div>|:exclamation:MinorFail|`module-src-vocabularies-check-method-comparators`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL EL Profile incompatible|[Jump](#minorfail-outcome-number-22)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-23">23/161</div>|:exclamation:MinorFail|`module-src-vocabularies-check-method-comparators`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL QL Profile incompatible|[Jump](#minorfail-outcome-number-23)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-24">24/161</div>|:exclamation:MinorFail|`module-src-vocabularies-check-method-comparators`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL QL Profile incompatible|[Jump](#minorfail-outcome-number-24)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-25">25/161</div>|:exclamation:MinorFail|`module-src-vocabularies-check-method-comparators`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL QL Profile incompatible|[Jump](#minorfail-outcome-number-25)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-26">26/161</div>|:exclamation:MinorFail|`module-src-vocabularies-check-method-comparators`|[terms-differenciation](https://ns.inria.fr/olivaw#terms-differenciation)|Too close terms|[Jump](#minorfail-outcome-number-26)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-27">27/161</div>|:exclamation:MinorFail|`module-src-vocabularies-building-usage`|[domain-and-range-referencing](https://ns.inria.fr/olivaw#domain-and-range-referencing)|Range out of vocabulary|[Jump](#minorfail-outcome-number-27)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-28">28/161</div>|:exclamation:MinorFail|`module-src-vocabularies-building-usage`|[labeled-terms](https://ns.inria.fr/olivaw#labeled-terms)|Terms not labeled|[Jump](#minorfail-outcome-number-28)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-29">29/161</div>|:exclamation:MinorFail|`module-src-vocabularies-building-usage`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL EL Profile incompatible|[Jump](#minorfail-outcome-number-29)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-30">30/161</div>|:exclamation:MinorFail|`module-src-vocabularies-building-usage`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL QL Profile incompatible|[Jump](#minorfail-outcome-number-30)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-31">31/161</div>|:exclamation:MinorFail|`module-src-vocabularies-building-usage`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL QL Profile incompatible|[Jump](#minorfail-outcome-number-31)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-32">32/161</div>|:exclamation:MinorFail|`module-src-vocabularies-building-usage`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL QL Profile incompatible|[Jump](#minorfail-outcome-number-32)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-33">33/161</div>|:exclamation:MinorFail|`module-src-vocabularies-building-structure`|[domain-and-range-referencing](https://ns.inria.fr/olivaw#domain-and-range-referencing)|Range out of vocabulary|[Jump](#minorfail-outcome-number-33)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-34">34/161</div>|:exclamation:MinorFail|`module-src-vocabularies-building-structure`|[labeled-terms](https://ns.inria.fr/olivaw#labeled-terms)|Terms not labeled|[Jump](#minorfail-outcome-number-34)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-35">35/161</div>|:exclamation:MinorFail|`module-src-vocabularies-building-structure`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL EL Profile incompatible|[Jump](#minorfail-outcome-number-35)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-36">36/161</div>|:exclamation:MinorFail|`module-src-vocabularies-building-structure`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL QL Profile incompatible|[Jump](#minorfail-outcome-number-36)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-37">37/161</div>|:exclamation:MinorFail|`module-src-vocabularies-building-structure`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL QL Profile incompatible|[Jump](#minorfail-outcome-number-37)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-38">38/161</div>|:exclamation:MinorFail|`module-src-vocabularies-building-structure`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL QL Profile incompatible|[Jump](#minorfail-outcome-number-38)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-39">39/161</div>|:exclamation:MinorFail|`module-src-vocabularies-administrative-areas`|[domain-and-range-referencing](https://ns.inria.fr/olivaw#domain-and-range-referencing)|Range out of vocabulary|[Jump](#minorfail-outcome-number-39)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-40">40/161</div>|:exclamation:MinorFail|`module-src-vocabularies-administrative-areas`|[labeled-terms](https://ns.inria.fr/olivaw#labeled-terms)|Terms not labeled|[Jump](#minorfail-outcome-number-40)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-41">41/161</div>|:exclamation:MinorFail|`module-src-vocabularies-administrative-areas`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL QL Profile incompatible|[Jump](#minorfail-outcome-number-41)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-42">42/161</div>|:exclamation:MinorFail|`module-src-vocabularies-administrative-areas`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL QL Profile incompatible|[Jump](#minorfail-outcome-number-42)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-43">43/161</div>|:exclamation:MinorFail|`module-src-vocabularies-administrative-areas`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL QL Profile incompatible|[Jump](#minorfail-outcome-number-43)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-44">44/161</div>|:exclamation:MinorFail|`module-src-table`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL EL Profile incompatible|[Jump](#minorfail-outcome-number-44)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-45">45/161</div>|:exclamation:MinorFail|`module-src-table`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL EL Profile incompatible|[Jump](#minorfail-outcome-number-45)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-46">46/161</div>|:exclamation:MinorFail|`module-src-table`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL QL Profile incompatible|[Jump](#minorfail-outcome-number-46)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-47">47/161</div>|:exclamation:MinorFail|`module-src-table`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL QL Profile incompatible|[Jump](#minorfail-outcome-number-47)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-48">48/161</div>|:exclamation:MinorFail|`module-src-table`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL RL Profile incompatible|[Jump](#minorfail-outcome-number-48)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-49">49/161</div>|:exclamation:MinorFail|`module-src-table`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL RL Profile incompatible|[Jump](#minorfail-outcome-number-49)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-50">50/161</div>|:exclamation:MinorFail|`module-src-statement`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL EL Profile incompatible|[Jump](#minorfail-outcome-number-50)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-51">51/161</div>|:exclamation:MinorFail|`module-src-statement`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL EL Profile incompatible|[Jump](#minorfail-outcome-number-51)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-52">52/161</div>|:exclamation:MinorFail|`module-src-statement`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL EL Profile incompatible|[Jump](#minorfail-outcome-number-52)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-53">53/161</div>|:exclamation:MinorFail|`module-src-statement`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL QL Profile incompatible|[Jump](#minorfail-outcome-number-53)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-54">54/161</div>|:exclamation:MinorFail|`module-src-statement`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL QL Profile incompatible|[Jump](#minorfail-outcome-number-54)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-55">55/161</div>|:exclamation:MinorFail|`module-src-statement`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL QL Profile incompatible|[Jump](#minorfail-outcome-number-55)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-56">56/161</div>|:exclamation:MinorFail|`module-src-statement`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL RL Profile incompatible|[Jump](#minorfail-outcome-number-56)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-57">57/161</div>|:exclamation:MinorFail|`module-src-statement`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL RL Profile incompatible|[Jump](#minorfail-outcome-number-57)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-58">58/161</div>|:exclamation:MinorFail|`module-src-statement`|[terms-differenciation](https://ns.inria.fr/olivaw#terms-differenciation)|Too close terms|[Jump](#minorfail-outcome-number-58)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-59">59/161</div>|:exclamation:MinorFail|`module-src-model`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL EL Profile incompatible|[Jump](#minorfail-outcome-number-59)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-60">60/161</div>|:exclamation:MinorFail|`module-src-model`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL EL Profile incompatible|[Jump](#minorfail-outcome-number-60)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-61">61/161</div>|:exclamation:MinorFail|`module-src-model`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL QL Profile incompatible|[Jump](#minorfail-outcome-number-61)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-62">62/161</div>|:exclamation:MinorFail|`module-src-model`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL QL Profile incompatible|[Jump](#minorfail-outcome-number-62)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-63">63/161</div>|:exclamation:MinorFail|`module-src-model`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL RL Profile incompatible|[Jump](#minorfail-outcome-number-63)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-64">64/161</div>|:exclamation:MinorFail|`module-src-model`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL RL Profile incompatible|[Jump](#minorfail-outcome-number-64)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-65">65/161</div>|:exclamation:MinorFail|`module-src-model`|[term-referencing](https://ns.inria.fr/olivaw#term-referencing)|Term not referenced to a module|[Jump](#minorfail-outcome-number-65)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-66">66/161</div>|:exclamation:MinorFail|`module-src-legal-verifier`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL EL Profile incompatible|[Jump](#minorfail-outcome-number-66)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-67">67/161</div>|:exclamation:MinorFail|`module-src-legal-verifier`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL EL Profile incompatible|[Jump](#minorfail-outcome-number-67)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-68">68/161</div>|:exclamation:MinorFail|`module-src-legal-verifier`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL QL Profile incompatible|[Jump](#minorfail-outcome-number-68)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-69">69/161</div>|:exclamation:MinorFail|`module-src-legal-verifier`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL QL Profile incompatible|[Jump](#minorfail-outcome-number-69)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-70">70/161</div>|:exclamation:MinorFail|`module-src-feature-of-interest`|[domain-and-range-referencing](https://ns.inria.fr/olivaw#domain-and-range-referencing)|Domain out of vocabulary|[Jump](#minorfail-outcome-number-70)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-71">71/161</div>|:exclamation:MinorFail|`module-src-feature-of-interest`|[domain-and-range-referencing](https://ns.inria.fr/olivaw#domain-and-range-referencing)|Range out of vocabulary|[Jump](#minorfail-outcome-number-71)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-72">72/161</div>|:exclamation:MinorFail|`module-src-evidence`|[domain-and-range-referencing](https://ns.inria.fr/olivaw#domain-and-range-referencing)|Range out of vocabulary|[Jump](#minorfail-outcome-number-72)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-73">73/161</div>|:exclamation:MinorFail|`module-src-evidence`|[labeled-terms](https://ns.inria.fr/olivaw#labeled-terms)|Terms not labeled|[Jump](#minorfail-outcome-number-73)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-74">74/161</div>|:exclamation:MinorFail|`module-src-document`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL EL Profile incompatible|[Jump](#minorfail-outcome-number-74)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-75">75/161</div>|:exclamation:MinorFail|`module-src-document`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL EL Profile incompatible|[Jump](#minorfail-outcome-number-75)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-76">76/161</div>|:exclamation:MinorFail|`module-src-document`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL EL Profile incompatible|[Jump](#minorfail-outcome-number-76)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-77">77/161</div>|:exclamation:MinorFail|`module-src-document`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL QL Profile incompatible|[Jump](#minorfail-outcome-number-77)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-78">78/161</div>|:exclamation:MinorFail|`module-src-document`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL QL Profile incompatible|[Jump](#minorfail-outcome-number-78)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-79">79/161</div>|:exclamation:MinorFail|`module-src-document`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL QL Profile incompatible|[Jump](#minorfail-outcome-number-79)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-80">80/161</div>|:exclamation:MinorFail|`module-src-document`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL RL Profile incompatible|[Jump](#minorfail-outcome-number-80)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-81">81/161</div>|:exclamation:MinorFail|`module-src-document`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL RL Profile incompatible|[Jump](#minorfail-outcome-number-81)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-82">82/161</div>|:exclamation:MinorFail|`module-src-compliance-verification-report`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL EL Profile incompatible|[Jump](#minorfail-outcome-number-82)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-83">83/161</div>|:exclamation:MinorFail|`module-src-compliance-verification-report`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL EL Profile incompatible|[Jump](#minorfail-outcome-number-83)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-84">84/161</div>|:exclamation:MinorFail|`module-src-compliance-verification-report`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL EL Profile incompatible|[Jump](#minorfail-outcome-number-84)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-85">85/161</div>|:exclamation:MinorFail|`module-src-compliance-verification-report`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL QL Profile incompatible|[Jump](#minorfail-outcome-number-85)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-86">86/161</div>|:exclamation:MinorFail|`module-src-compliance-verification-report`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL QL Profile incompatible|[Jump](#minorfail-outcome-number-86)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-87">87/161</div>|:exclamation:MinorFail|`module-src-compliance-verification-report`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL QL Profile incompatible|[Jump](#minorfail-outcome-number-87)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-88">88/161</div>|:exclamation:MinorFail|`module-src-compliance-verification-report`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL RL Profile incompatible|[Jump](#minorfail-outcome-number-88)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-89">89/161</div>|:exclamation:MinorFail|`module-src-compliance-verification-report`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL RL Profile incompatible|[Jump](#minorfail-outcome-number-89)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-90">90/161</div>|:exclamation:MinorFail|`module-src-compliance-verification-report`|[terms-differenciation](https://ns.inria.fr/olivaw#terms-differenciation)|Too close terms|[Jump](#minorfail-outcome-number-90)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-91">91/161</div>|:exclamation:MinorFail|`module-src-checking-act`|[domain-and-range-referencing](https://ns.inria.fr/olivaw#domain-and-range-referencing)|Domain out of vocabulary|[Jump](#minorfail-outcome-number-91)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-92">92/161</div>|:exclamation:MinorFail|`module-src-checking-act`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL RL Profile incompatible|[Jump](#minorfail-outcome-number-92)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-93">93/161</div>|:exclamation:MinorFail|`module-src-checking-act`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL RL Profile incompatible|[Jump](#minorfail-outcome-number-93)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-94">94/161</div>|:exclamation:MinorFail|`module-src-check-method`|[domain-and-range-referencing](https://ns.inria.fr/olivaw#domain-and-range-referencing)|Domain out of vocabulary|[Jump](#minorfail-outcome-number-94)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-95">95/161</div>|:exclamation:MinorFail|`module-src-check-method`|[domain-and-range-referencing](https://ns.inria.fr/olivaw#domain-and-range-referencing)|Range out of vocabulary|[Jump](#minorfail-outcome-number-95)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-96">96/161</div>|:exclamation:MinorFail|`module-src-check-method`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL EL Profile incompatible|[Jump](#minorfail-outcome-number-96)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-97">97/161</div>|:exclamation:MinorFail|`module-src-check-method`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL EL Profile incompatible|[Jump](#minorfail-outcome-number-97)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-98">98/161</div>|:exclamation:MinorFail|`module-src-check-method`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL EL Profile incompatible|[Jump](#minorfail-outcome-number-98)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-99">99/161</div>|:exclamation:MinorFail|`module-src-check-method`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL EL Profile incompatible|[Jump](#minorfail-outcome-number-99)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-100">100/161</div>|:exclamation:MinorFail|`module-src-check-method`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL QL Profile incompatible|[Jump](#minorfail-outcome-number-100)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-101">101/161</div>|:exclamation:MinorFail|`module-src-check-method`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL QL Profile incompatible|[Jump](#minorfail-outcome-number-101)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-102">102/161</div>|:exclamation:MinorFail|`module-src-check-method`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL QL Profile incompatible|[Jump](#minorfail-outcome-number-102)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-103">103/161</div>|:exclamation:MinorFail|`module-src-check-method`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL QL Profile incompatible|[Jump](#minorfail-outcome-number-103)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-104">104/161</div>|:exclamation:MinorFail|`module-src-check-method`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL QL Profile incompatible|[Jump](#minorfail-outcome-number-104)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-105">105/161</div>|:exclamation:MinorFail|`module-src-check-method`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL RL Profile incompatible|[Jump](#minorfail-outcome-number-105)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-106">106/161</div>|:exclamation:MinorFail|`module-src-check-method`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL RL Profile incompatible|[Jump](#minorfail-outcome-number-106)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-107">107/161</div>|:exclamation:MinorFail|`module-src-check-method`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL RL Profile incompatible|[Jump](#minorfail-outcome-number-107)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-108">108/161</div>|:exclamation:MinorFail|`module-src-check-method`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL RL Profile incompatible|[Jump](#minorfail-outcome-number-108)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-109">109/161</div>|:exclamation:MinorFail|`module-src-check-method`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL RL Profile incompatible|[Jump](#minorfail-outcome-number-109)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-110">110/161</div>|:exclamation:MinorFail|`module-src-check-method`|[term-referencing](https://ns.inria.fr/olivaw#term-referencing)|Term not referenced to a module|[Jump](#minorfail-outcome-number-110)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-111">111/161</div>|:exclamation:MinorFail|`module-src-aec3po`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL EL Profile incompatible|[Jump](#minorfail-outcome-number-111)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-112">112/161</div>|:exclamation:MinorFail|`module-src-aec3po`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL EL Profile incompatible|[Jump](#minorfail-outcome-number-112)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-113">113/161</div>|:exclamation:MinorFail|`module-src-aec3po`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL QL Profile incompatible|[Jump](#minorfail-outcome-number-113)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-114">114/161</div>|:exclamation:MinorFail|`module-src-aec3po`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL QL Profile incompatible|[Jump](#minorfail-outcome-number-114)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-115">115/161</div>|:exclamation:MinorFail|`module-src-aec3po`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL RL Profile incompatible|[Jump](#minorfail-outcome-number-115)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-116">116/161</div>|:exclamation:MinorFail|`module-src-aec3po`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL RL Profile incompatible|[Jump](#minorfail-outcome-number-116)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-117">117/161</div>|:exclamation:MinorFail|`module-src-aec3po`|[term-referencing](https://ns.inria.fr/olivaw#term-referencing)|Term not referenced to a module|[Jump](#minorfail-outcome-number-117)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-118">118/161</div>|:exclamation:MinorFail|`all-modules`|[domain-and-range-referencing](https://ns.inria.fr/olivaw#domain-and-range-referencing)|Domain out of vocabulary|[Jump](#minorfail-outcome-number-118)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-119">119/161</div>|:exclamation:MinorFail|`all-modules`|[domain-and-range-referencing](https://ns.inria.fr/olivaw#domain-and-range-referencing)|Range out of vocabulary|[Jump](#minorfail-outcome-number-119)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-120">120/161</div>|:exclamation:MinorFail|`all-modules`|[labeled-terms](https://ns.inria.fr/olivaw#labeled-terms)|Terms not labeled|[Jump](#minorfail-outcome-number-120)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-121">121/161</div>|:exclamation:MinorFail|`all-modules`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL EL Profile incompatible|[Jump](#minorfail-outcome-number-121)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-122">122/161</div>|:exclamation:MinorFail|`all-modules`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL EL Profile incompatible|[Jump](#minorfail-outcome-number-122)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-123">123/161</div>|:exclamation:MinorFail|`all-modules`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL EL Profile incompatible|[Jump](#minorfail-outcome-number-123)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-124">124/161</div>|:exclamation:MinorFail|`all-modules`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL EL Profile incompatible|[Jump](#minorfail-outcome-number-124)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-125">125/161</div>|:exclamation:MinorFail|`all-modules`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL EL Profile incompatible|[Jump](#minorfail-outcome-number-125)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-126">126/161</div>|:exclamation:MinorFail|`all-modules`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL QL Profile incompatible|[Jump](#minorfail-outcome-number-126)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-127">127/161</div>|:exclamation:MinorFail|`all-modules`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL QL Profile incompatible|[Jump](#minorfail-outcome-number-127)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-128">128/161</div>|:exclamation:MinorFail|`all-modules`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL QL Profile incompatible|[Jump](#minorfail-outcome-number-128)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-129">129/161</div>|:exclamation:MinorFail|`all-modules`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL QL Profile incompatible|[Jump](#minorfail-outcome-number-129)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-130">130/161</div>|:exclamation:MinorFail|`all-modules`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL QL Profile incompatible|[Jump](#minorfail-outcome-number-130)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-131">131/161</div>|:exclamation:MinorFail|`all-modules`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL QL Profile incompatible|[Jump](#minorfail-outcome-number-131)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-132">132/161</div>|:exclamation:MinorFail|`all-modules`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL RL Profile incompatible|[Jump](#minorfail-outcome-number-132)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-133">133/161</div>|:exclamation:MinorFail|`all-modules`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL RL Profile incompatible|[Jump](#minorfail-outcome-number-133)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-134">134/161</div>|:exclamation:MinorFail|`all-modules`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL RL Profile incompatible|[Jump](#minorfail-outcome-number-134)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-135">135/161</div>|:exclamation:MinorFail|`all-modules`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL RL Profile incompatible|[Jump](#minorfail-outcome-number-135)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-136">136/161</div>|:exclamation:MinorFail|`all-modules`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL RL Profile incompatible|[Jump](#minorfail-outcome-number-136)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-137">137/161</div>|:exclamation:MinorFail|`all-modules`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL RL Profile incompatible|[Jump](#minorfail-outcome-number-137)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-138">138/161</div>|:exclamation:MinorFail|`all-modules`|[term-referencing](https://ns.inria.fr/olivaw#term-referencing)|Term not referenced to a module|[Jump](#minorfail-outcome-number-138)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-139">139/161</div>|:exclamation:MinorFail|`all-modules`|[terms-differenciation](https://ns.inria.fr/olivaw#terms-differenciation)|Too close terms|[Jump](#minorfail-outcome-number-139)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-140">140/161</div>|:exclamation:MinorFail|`all-fragments`|[domain-and-range-referencing](https://ns.inria.fr/olivaw#domain-and-range-referencing)|Domain out of vocabulary|[Jump](#minorfail-outcome-number-140)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-141">141/161</div>|:exclamation:MinorFail|`all-fragments`|[domain-and-range-referencing](https://ns.inria.fr/olivaw#domain-and-range-referencing)|Range out of vocabulary|[Jump](#minorfail-outcome-number-141)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-142">142/161</div>|:exclamation:MinorFail|`all-fragments`|[labeled-terms](https://ns.inria.fr/olivaw#labeled-terms)|Terms not labeled|[Jump](#minorfail-outcome-number-142)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-143">143/161</div>|:exclamation:MinorFail|`all-fragments`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL EL Profile incompatible|[Jump](#minorfail-outcome-number-143)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-144">144/161</div>|:exclamation:MinorFail|`all-fragments`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL EL Profile incompatible|[Jump](#minorfail-outcome-number-144)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-145">145/161</div>|:exclamation:MinorFail|`all-fragments`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL EL Profile incompatible|[Jump](#minorfail-outcome-number-145)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-146">146/161</div>|:exclamation:MinorFail|`all-fragments`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL EL Profile incompatible|[Jump](#minorfail-outcome-number-146)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-147">147/161</div>|:exclamation:MinorFail|`all-fragments`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL EL Profile incompatible|[Jump](#minorfail-outcome-number-147)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-148">148/161</div>|:exclamation:MinorFail|`all-fragments`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL QL Profile incompatible|[Jump](#minorfail-outcome-number-148)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-149">149/161</div>|:exclamation:MinorFail|`all-fragments`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL QL Profile incompatible|[Jump](#minorfail-outcome-number-149)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-150">150/161</div>|:exclamation:MinorFail|`all-fragments`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL QL Profile incompatible|[Jump](#minorfail-outcome-number-150)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-151">151/161</div>|:exclamation:MinorFail|`all-fragments`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL QL Profile incompatible|[Jump](#minorfail-outcome-number-151)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-152">152/161</div>|:exclamation:MinorFail|`all-fragments`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL QL Profile incompatible|[Jump](#minorfail-outcome-number-152)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-153">153/161</div>|:exclamation:MinorFail|`all-fragments`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL QL Profile incompatible|[Jump](#minorfail-outcome-number-153)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-154">154/161</div>|:exclamation:MinorFail|`all-fragments`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL RL Profile incompatible|[Jump](#minorfail-outcome-number-154)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-155">155/161</div>|:exclamation:MinorFail|`all-fragments`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL RL Profile incompatible|[Jump](#minorfail-outcome-number-155)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-156">156/161</div>|:exclamation:MinorFail|`all-fragments`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL RL Profile incompatible|[Jump](#minorfail-outcome-number-156)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-157">157/161</div>|:exclamation:MinorFail|`all-fragments`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL RL Profile incompatible|[Jump](#minorfail-outcome-number-157)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-158">158/161</div>|:exclamation:MinorFail|`all-fragments`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL RL Profile incompatible|[Jump](#minorfail-outcome-number-158)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-159">159/161</div>|:exclamation:MinorFail|`all-fragments`|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|OWL RL Profile incompatible|[Jump](#minorfail-outcome-number-159)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-160">160/161</div>|:exclamation:MinorFail|`all-fragments`|[term-referencing](https://ns.inria.fr/olivaw#term-referencing)|Term not referenced to a module|[Jump](#minorfail-outcome-number-160)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-161">161/161</div>|:exclamation:MinorFail|`all-fragments`|[terms-differenciation](https://ns.inria.fr/olivaw#terms-differenciation)|Too close terms|[Jump](#minorfail-outcome-number-161)|

***

## MinorFail Outcomes Details

This subchapter gives more details to the :exclamation:MinorFail outcomes

### MinorFail Outcome number 1

[Jump to summary definition](#summary-MinorFail-1)	|	Previous MinorFail outcome	|	[Next MinorFail outcome](#minorfail-outcome-number-2)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-src-vocabularies-quantity-kinds|
|----|----|
|Title|Standalone&#32;module&#32;src/vocabularies/quantity&lowbar;kinds.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Module vocabularies/quantity&lowbar;kinds](https://github.com/Accord-Project/aec3po/blob/HEAD/src/vocabularies/quantity_kinds.ttl)|

#### Criterion detail
|Identifier|[labeled-terms](https://ns.inria.fr/olivaw#labeled-terms)|
|----|----|
|Title|Term&#32;labeling&#32;test|
|Description|A&#32;test&#32;case&#32;from&#32;the&#32;Best&#32;Practices&#32;tests&#32;checking&#32;if&#32;all&#32;the&#32;terms&#32;of&#32;the&#32;subject&#32;have&#32;a&#32;rdfs:label&#32;property&#32;pointing&#32;to&#32;a&#32;literal&#32;in&#32;English|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-1)|Identifier|`not-labeled-term`|
|[Section top](#minorfail-outcome-number-1)|Title|Terms&#32;not&#32;labeled|
|[Section top](#minorfail-outcome-number-1)|Description|The&#32;following&#32;terms&#32;have&#32;no&#32;rdfs:label&#32;to&#32;define&#32;it&#32;in&#32;natural&#32;language|
|[Section top](#minorfail-outcome-number-1)|Pointer|<pre lang="Turtle"><code>:QuantityKind&#32;a&#32;owl:Class&#32;;  &#10; &#32; &#32;&#32; &#32;rdfs:isDefinedBy&#32; &#60;http://qudt.org/2.1/schema/qudt> &#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-1)|Pointer|<pre lang="Turtle"><code>:ModularRoomHeight&#32;a&#32;owl:NamedIndividual,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;skos:Concept,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;:QuantityKind&#32;;  &#10; &#32; &#32; &#32; &#32;qudt:applicableUnit&#32; &#60;http://qudt.org/vocab/unit/CentiM>,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#60;http://qudt.org/vocab/unit/IN>,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#60;http://qudt.org/vocab/unit/M>,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#60;http://qudt.org/vocab/unit/MilliIN>,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#60;http://qudt.org/vocab/unit/MilliM> &#32;;  &#10; &#32; &#32; &#32; &#32;qudt:hasDimensionVector&#32; &#60;http://qudt.org/vocab/dimensionvector/A0E0L1I0M0H0T0D0> &#32;;  &#10; &#32; &#32; &#32; &#32;qudt:normativeReference&#32; &#34;https://www.iso.org/obp/ui/#iso:std:iso:6707:-1:ed-6:v1:en:t...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32;:quantity&lowbar;kinds&#32;;  &#10; &#32; &#32; &#32; &#32;skos:broader&#32; &#60;http://qudt.org/vocab/quantitykind/Length> &#32;;  &#10; &#32; &#32; &#32; &#32;skos:definition&#32; &#34;vertical&#32;distance&#32;within&#32;one&#32;storey&#32;between&#32;the&#32;modular&#32;plan...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;skos:prefLabel&#32; &#34;modular&#32;room&#32;height&#34;@en&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-1)|Pointer|<pre lang="Turtle"><code>:WidthOfAngledCorridor&#32;a&#32;owl:NamedIndividual,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;skos:Concept,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;:QuantityKind&#32;;  &#10; &#32; &#32; &#32; &#32;qudt:applicableUnit&#32; &#60;http://qudt.org/vocab/unit/CentiM>,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#60;http://qudt.org/vocab/unit/IN>,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#60;http://qudt.org/vocab/unit/M>,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#60;http://qudt.org/vocab/unit/MilliIN>,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#60;http://qudt.org/vocab/unit/MilliM> &#32;;  &#10; &#32; &#32; &#32; &#32;qudt:hasDimensionVector&#32; &#60;http://qudt.org/vocab/dimensionvector/A0E0L1I0M0H0T0D0> &#32;;  &#10; &#32; &#32; &#32; &#32;qudt:normativeReference&#32; &#34;https://www.iso.org/obp/ui/#iso:std:iso:7176:-5:ed-2:v1:en:t...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32;:quantity&lowbar;kinds&#32;;  &#10; &#32; &#32; &#32; &#32;skos:broader&#32; &#60;http://qudt.org/vocab/quantitykind/Length> &#32;;  &#10; &#32; &#32; &#32; &#32;skos:definition&#32; &#34;width&#32;of&#32;a&#32;corridor&#32;with&#32;a&#32;right&#32;angled&#32;turn&#32;in&#32;which&#32;the&#32;wh...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;skos:prefLabel&#32; &#34;width&#32;of&#32;angled&#32;corridor&#34;@en&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-1)|Pointer|<pre lang="Turtle"><code>:CompressiveForce&#32;a&#32;owl:NamedIndividual,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;skos:Concept,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;:QuantityKind&#32;;  &#10; &#32; &#32; &#32; &#32;qudt:hasDimensionVector&#32; &#60;http://qudt.org/vocab/dimensionvector/A0E0L1I0M1H0T-2D0> &#32;;  &#10; &#32; &#32; &#32; &#32;qudt:symbol&#32; &#34;C&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32;:quantity&lowbar;kinds&#32;;  &#10; &#32; &#32; &#32; &#32;skos:broader&#32; &#60;http://qudt.org/vocab/quantitykind/Force> &#32;;  &#10; &#32; &#32; &#32; &#32;skos:definition&#32; &#34;Force&#32;tending&#32;to&#32;reduce&#32;the&#32;size&#32;of&#32;a&#32;body.&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;skos:prefLabel&#32; &#34;compressive&#32;force&#34;@en&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-1)|Pointer|<pre lang="Turtle"><code>:PartialSafetyFactor&#32;a&#32;owl:NamedIndividual,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;skos:Concept,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;:QuantityKind&#32;;  &#10; &#32; &#32; &#32; &#32;qudt:applicableUnit&#32; &#60;http://qudt.org/vocab/unit/UNITLESS> &#32;;  &#10; &#32; &#32; &#32; &#32;qudt:hasDimensionVector&#32; &#60;http://qudt.org/vocab/dimensionvector/A0E0L0I0M0H0T0D0> &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32;:quantity&lowbar;kinds&#32;;  &#10; &#32; &#32; &#32; &#32;skos:definition&#32; &#34;Also&#32;written&#32;γM,&#32;the&#32;partial&#32;safety&#32;factor&#32;for&#32;resistance.&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;skos:prefLabel&#32; &#34;Partial&#32;Safety&#32;Factor&#34;@en&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-1)|Pointer|<pre lang="Turtle"><code>:PartialSafetyFactor0&#32;a&#32;owl:NamedIndividual,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;skos:Concept,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;:QuantityKind&#32;;  &#10; &#32; &#32; &#32; &#32;qudt:applicableUnit&#32; &#60;http://qudt.org/vocab/unit/UNITLESS> &#32;;  &#10; &#32; &#32; &#32; &#32;qudt:hasDimensionVector&#32; &#60;http://qudt.org/vocab/dimensionvector/A0E0L0I0M0H0T0D0> &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32;:quantity&lowbar;kinds&#32;;  &#10; &#32; &#32; &#32; &#32;skos:broader&#32;:PartialSafetyFactor&#32;;  &#10; &#32; &#32; &#32; &#32;skos:definition&#32; &#34;Also&#32;written&#32;γM0,&#32;the&#32;partial&#32;safety&#32;factor&#32;for&#32;resistance&#32;r...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;skos:prefLabel&#32; &#34;Partial&#32;Safety&#32;Factor&#34;@en&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-1)|Pointer|<pre lang="Turtle"><code>:AxialCompressionStress&#32;a&#32;owl:NamedIndividual,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;skos:Concept,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;:QuantityKind&#32;;  &#10; &#32; &#32; &#32; &#32;qudt:hasDimensionVector&#32; &#60;http://qudt.org/vocab/dimensionvector/A0E0L1I0M-1H0T-2D0> &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32;:quantity&lowbar;kinds&#32;;  &#10; &#32; &#32; &#32; &#32;skos:definition&#32; &#34;also&#32;known&#32;as&#32;fc0k&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;skos:prefLabel&#32; &#34;axial&#32;compression&#32;stress&#34;@en&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-1)|Pointer|<pre lang="Turtle"><code>:ModificationFactorKmod&#32;a&#32;owl:NamedIndividual,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;skos:Concept,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;:QuantityKind&#32;;  &#10; &#32; &#32; &#32; &#32;qudt:applicableUnit&#32; &#60;http://qudt.org/vocab/unit/UNITLESS> &#32;;  &#10; &#32; &#32; &#32; &#32;qudt:hasDimensionVector&#32; &#60;http://qudt.org/vocab/dimensionvector/A0E0L0I0M0H0T0D0> &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32;:quantity&lowbar;kinds&#32;;  &#10; &#32; &#32; &#32; &#32;skos:definition&#32; &#34;Modification&#32;Factor&#32;to&#32;take&#32;into&#32;account&#32;the&#32;duration&#32;of&#32;loa...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;skos:prefLabel&#32; &#34;Modification&#32;Factor&#32;Kmod&#34;@en&#32;.</code></pre>|

***
### MinorFail Outcome number 2

[Jump to summary definition](#summary-MinorFail-2)	|	[Previous MinorFail outcome](#minorfail-outcome-number-1)	|	[Next MinorFail outcome](#minorfail-outcome-number-3)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-src-vocabularies-quantity-kinds|
|----|----|
|Title|Standalone&#32;module&#32;src/vocabularies/quantity&lowbar;kinds.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Module vocabularies/quantity&lowbar;kinds](https://github.com/Accord-Project/aec3po/blob/HEAD/src/vocabularies/quantity_kinds.ttl)|

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
|[Section top](#minorfail-outcome-number-2)|Description|Class&#32;Expression&#32;not&#32;supported&#32;with&#32;owl:equivalentClass|
|[Section top](#minorfail-outcome-number-2)|Pointer|<pre lang="Turtle"><code>aec3po:QuantityKind&#32;a&#32;owl:Class&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;Quantity&#32;Kind&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;A&#32;Quantity&#32;Kind&#32;is&#32;any&#32;observable&#32;property&#32;that&#32;can&#32;be&#32;quant...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32;aec3po:quantity&lowbar;kinds&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:subClassOf&#32;qudt:QuantityKind,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#60;http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#Region>,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;skos:Concept&#32;;  &#10; &#32; &#32; &#32; &#32;owl:equivalentClass&#32; &#91;&#32;owl:intersectionOf&#32;(&#32;skos:Concept&#32; &#91;&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:hasValue&#32;aec3po:QuantityKindNomenclature&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:onProperty&#32;skos:inScheme&#32;]&#32;)&#32;]&#32;;  &#10; &#32; &#32; &#32; &#32;skos:example&#32; &#34;Length,&#32;Area,&#32;U-Value.&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;skos:note&#32; &#34;Maxime&#32;Lefrançois&#32;argues&#32;that&#32;both&#32;qudt:QuantityKind&#32;and&#32;qud...&#34; &#32;.</code></pre>|

***
### MinorFail Outcome number 3

[Jump to summary definition](#summary-MinorFail-3)	|	[Previous MinorFail outcome](#minorfail-outcome-number-2)	|	[Next MinorFail outcome](#minorfail-outcome-number-4)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-src-vocabularies-quantity-kinds|
|----|----|
|Title|Standalone&#32;module&#32;src/vocabularies/quantity&lowbar;kinds.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Module vocabularies/quantity&lowbar;kinds](https://github.com/Accord-Project/aec3po/blob/HEAD/src/vocabularies/quantity_kinds.ttl)|

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
|[Section top](#minorfail-outcome-number-3)|Description|Statement&#32;not&#32;supported|
|[Section top](#minorfail-outcome-number-3)|Pointer|<pre lang="Turtle"><code>&#91;]&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32;owl:hasValue&#32;aec3po:QuantityKindNomenclature&#32;;  &#10; &#32; &#32; &#32; &#32;owl:onProperty&#32;skos:inScheme&#32;.</code></pre>|

***
### MinorFail Outcome number 4

[Jump to summary definition](#summary-MinorFail-4)	|	[Previous MinorFail outcome](#minorfail-outcome-number-3)	|	[Next MinorFail outcome](#minorfail-outcome-number-5)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-src-vocabularies-quantity-kinds|
|----|----|
|Title|Standalone&#32;module&#32;src/vocabularies/quantity&lowbar;kinds.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Module vocabularies/quantity&lowbar;kinds](https://github.com/Accord-Project/aec3po/blob/HEAD/src/vocabularies/quantity_kinds.ttl)|

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
|[Section top](#minorfail-outcome-number-4)|Description|Statement&#32;not&#32;supported&#32;in&#32;a&#32;Sub&#32;Class&#32;Expression|
|[Section top](#minorfail-outcome-number-4)|Pointer|<pre lang="Turtle"><code>&#91;]&#32;owl:intersectionOf&#32;(&#32;skos:Concept&#32; &#91;&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:hasValue&#32;aec3po:QuantityKindNomenclature&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:onProperty&#32;skos:inScheme&#32;]&#32;)&#32;.</code></pre>|

***
### MinorFail Outcome number 5

[Jump to summary definition](#summary-MinorFail-5)	|	[Previous MinorFail outcome](#minorfail-outcome-number-4)	|	[Next MinorFail outcome](#minorfail-outcome-number-6)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-src-vocabularies-quantity-kinds|
|----|----|
|Title|Standalone&#32;module&#32;src/vocabularies/quantity&lowbar;kinds.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Module vocabularies/quantity&lowbar;kinds](https://github.com/Accord-Project/aec3po/blob/HEAD/src/vocabularies/quantity_kinds.ttl)|

#### Criterion detail
|Identifier|[terms-differenciation](https://ns.inria.fr/olivaw#terms-differenciation)|
|----|----|
|Title|Terms&#32;differenciation&#32;test|
|Description|A&#32;test&#32;case&#32;from&#32;the&#32;Best&#32;Practices&#32;tests&#32;checking&#32;if&#32;all&#32;the&#32;terms&#32;are&#32;different&#32;enough&#32;from&#32;each&#32;other&#32;according&#32;to&#32;the&#32;Levenshtein&#32;distance&#32;metric.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-5)|Identifier|`too-close-terms`|
|[Section top](#minorfail-outcome-number-5)|Title|Too&#32;close&#32;terms|
|[Section top](#minorfail-outcome-number-5)|Description|Some&#32;terms&#32;are&#32;too&#32;similar|
|[Section top](#minorfail-outcome-number-5)|Pointer|<pre lang="Turtle"><code>:PartialSafetyFactor0&#32;a&#32;owl:NamedIndividual,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;skos:Concept,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;:QuantityKind&#32;;  &#10; &#32; &#32; &#32; &#32;qudt:applicableUnit&#32; &#60;http://qudt.org/vocab/unit/UNITLESS> &#32;;  &#10; &#32; &#32; &#32; &#32;qudt:hasDimensionVector&#32; &#60;http://qudt.org/vocab/dimensionvector/A0E0L0I0M0H0T0D0> &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32;:quantity&lowbar;kinds&#32;;  &#10; &#32; &#32; &#32; &#32;skos:broader&#32;:PartialSafetyFactor&#32;;  &#10; &#32; &#32; &#32; &#32;skos:definition&#32; &#34;Also&#32;written&#32;γM0,&#32;the&#32;partial&#32;safety&#32;factor&#32;for&#32;resistance&#32;r...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;skos:prefLabel&#32; &#34;Partial&#32;Safety&#32;Factor&#34;@en&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-5)|Pointer|<pre lang="Turtle"><code>:PartialSafetyFactor&#32;a&#32;owl:NamedIndividual,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;skos:Concept,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;:QuantityKind&#32;;  &#10; &#32; &#32; &#32; &#32;qudt:applicableUnit&#32; &#60;http://qudt.org/vocab/unit/UNITLESS> &#32;;  &#10; &#32; &#32; &#32; &#32;qudt:hasDimensionVector&#32; &#60;http://qudt.org/vocab/dimensionvector/A0E0L0I0M0H0T0D0> &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32;:quantity&lowbar;kinds&#32;;  &#10; &#32; &#32; &#32; &#32;skos:definition&#32; &#34;Also&#32;written&#32;γM,&#32;the&#32;partial&#32;safety&#32;factor&#32;for&#32;resistance.&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;skos:prefLabel&#32; &#34;Partial&#32;Safety&#32;Factor&#34;@en&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-5)|Pointer|<pre lang="Turtle"><code>:PartialSafetyFactor1&#32;a&#32;owl:NamedIndividual,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;skos:Concept,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;:QuantityKind&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;Partial&#32;Safety&#32;Factor&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;qudt:applicableUnit&#32; &#60;http://qudt.org/vocab/unit/UNITLESS> &#32;;  &#10; &#32; &#32; &#32; &#32;qudt:hasDimensionVector&#32; &#60;http://qudt.org/vocab/dimensionvector/A0E0L0I0M0H0T0D0> &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32;:quantity&lowbar;kinds&#32;;  &#10; &#32; &#32; &#32; &#32;skos:broader&#32;:PartialSafetyFactor&#32;;  &#10; &#32; &#32; &#32; &#32;skos:definition&#32; &#34;Also&#32;written&#32;γM1,&#32;the&#32;partial&#32;safety&#32;factor&#32;for&#32;resistance&#32;r...&#34; &#32;.</code></pre>|

***
### MinorFail Outcome number 6

[Jump to summary definition](#summary-MinorFail-6)	|	[Previous MinorFail outcome](#minorfail-outcome-number-5)	|	[Next MinorFail outcome](#minorfail-outcome-number-7)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-src-vocabularies-permitting-stages|
|----|----|
|Title|Standalone&#32;module&#32;src/vocabularies/permitting&lowbar;stages.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Module vocabularies/permitting&lowbar;stages](https://github.com/Accord-Project/aec3po/blob/HEAD/src/vocabularies/permitting_stages.ttl)|

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
|[Section top](#minorfail-outcome-number-6)|Pointer|<pre lang="Turtle"><code>:hasPermittingStage&#32;a&#32;owl:ObjectProperty&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;has&#32;permitting&#32;stage&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;Links&#32;an&#32;entity&#32;to&#32;the&#32;permitting&#32;stage&#32;this&#32;entity&#32;pertains&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32;:permitting&lowbar;stage&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:range&#32;&lowbar;:nfd6c027292f24febbf9920729a244c55b1,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#91;&#32;rdfs:subClassOf&#32;&lowbar;:nfd6c027292f24febbf9920729a244c55b1,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;skos:Concept,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;:PermittingStage&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:equivalentClass&#32;:PermittingStage&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:intersectionOf&#32;(&#32;skos:Concept&#32;&lowbar;:nfd6c027292f24febbf9920729a244c55b1&#32;)&#32;],  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;skos:Concept,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;:PermittingStage&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:subPropertyOf&#32; &#60;https://w3id.org/digitalconstruction/0.5/Lifecycle#hasStage> &#32;;  &#10; &#32; &#32; &#32; &#32;owl:equivalentProperty&#32; &#60;https://w3id.org/digitalconstruction/0.5/Lifecycle#hasStage> &#32;.  &#10;&lowbar;:nfd6c027292f24febbf9920729a244c55b1&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32;owl:hasValue&#32;:PermittingStageNomenclature&#32;;  &#10; &#32; &#32; &#32; &#32;owl:onProperty&#32;skos:inScheme&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-6)|Pointer|http://www.w3.org/2004/02/skos/core#Concept|

***
### MinorFail Outcome number 7

[Jump to summary definition](#summary-MinorFail-7)	|	[Previous MinorFail outcome](#minorfail-outcome-number-6)	|	[Next MinorFail outcome](#minorfail-outcome-number-8)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-src-vocabularies-permitting-stages|
|----|----|
|Title|Standalone&#32;module&#32;src/vocabularies/permitting&lowbar;stages.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Module vocabularies/permitting&lowbar;stages](https://github.com/Accord-Project/aec3po/blob/HEAD/src/vocabularies/permitting_stages.ttl)|

#### Criterion detail
|Identifier|[labeled-terms](https://ns.inria.fr/olivaw#labeled-terms)|
|----|----|
|Title|Term&#32;labeling&#32;test|
|Description|A&#32;test&#32;case&#32;from&#32;the&#32;Best&#32;Practices&#32;tests&#32;checking&#32;if&#32;all&#32;the&#32;terms&#32;of&#32;the&#32;subject&#32;have&#32;a&#32;rdfs:label&#32;property&#32;pointing&#32;to&#32;a&#32;literal&#32;in&#32;English|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-7)|Identifier|`not-labeled-term`|
|[Section top](#minorfail-outcome-number-7)|Title|Terms&#32;not&#32;labeled|
|[Section top](#minorfail-outcome-number-7)|Description|The&#32;following&#32;terms&#32;have&#32;no&#32;rdfs:label&#32;to&#32;define&#32;it&#32;in&#32;natural&#32;language|
|[Section top](#minorfail-outcome-number-7)|Pointer|<pre lang="Turtle"><code>:UK&lowbar;Building&lowbar;Control&lowbar;Submission&#32;a&#32;owl:NamedIndividual,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;skos:Concept,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;:PermittingStage&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32;:permitting&lowbar;stage&#32;;  &#10; &#32; &#32; &#32; &#32;skos:definition&#32; &#34;The&#32;UK&#32;Building&#32;Control&#32;Submission&#32;permitting&#32;stage.&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;skos:inScheme&#32;:PermittingStageNomenclature&#32;;  &#10; &#32; &#32; &#32; &#32;skos:prefLabel&#32; &#34;building&#32;control&#32;submission&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;skos:topConceptOf&#32;:PermittingStageNomenclature&#32;;  &#10; &#32; &#32; &#32; &#32;:forAdministrativeArea&#32;:England&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-7)|Pointer|<pre lang="Turtle"><code>:UK&lowbar;Planning&lowbar;Permission&#32;a&#32;owl:NamedIndividual,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;skos:Concept,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;:PermittingStage&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32;:permitting&lowbar;stage&#32;;  &#10; &#32; &#32; &#32; &#32;skos:definition&#32; &#34;The&#32;UK&#32;Planning&#32;Permission&#32;permitting&#32;stage.&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;skos:inScheme&#32;:PermittingStageNomenclature&#32;;  &#10; &#32; &#32; &#32; &#32;skos:prefLabel&#32; &#34;planning&#32;permission&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;skos:topConceptOf&#32;:PermittingStageNomenclature&#32;;  &#10; &#32; &#32; &#32; &#32;:forAdministrativeArea&#32;:England&#32;.</code></pre>|

***
### MinorFail Outcome number 8

[Jump to summary definition](#summary-MinorFail-8)	|	[Previous MinorFail outcome](#minorfail-outcome-number-7)	|	[Next MinorFail outcome](#minorfail-outcome-number-9)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-src-vocabularies-permitting-stages|
|----|----|
|Title|Standalone&#32;module&#32;src/vocabularies/permitting&lowbar;stages.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Module vocabularies/permitting&lowbar;stages](https://github.com/Accord-Project/aec3po/blob/HEAD/src/vocabularies/permitting_stages.ttl)|

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
|[Section top](#minorfail-outcome-number-8)|Description|Class&#32;Expression&#32;not&#32;supported&#32;with&#32;owl:equivalentClass|
|[Section top](#minorfail-outcome-number-8)|Pointer|<pre lang="Turtle"><code>aec3po:PermittingStage&#32;a&#32;owl:Class&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;Permitting&#32;Stage&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;The&#32;class&#32;of&#32;permitting&#32;stages.&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32;aec3po:permitting&lowbar;stage&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:subClassOf&#32;skos:Concept&#32;;  &#10; &#32; &#32; &#32; &#32;owl:equivalentClass&#32; &#91;&#32;owl:intersectionOf&#32;(&#32;skos:Concept&#32; &#91;&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:hasValue&#32;aec3po:PermittingStageNomenclature&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:onProperty&#32;skos:inScheme&#32;]&#32;)&#32;]&#32;.</code></pre>|

***
### MinorFail Outcome number 9

[Jump to summary definition](#summary-MinorFail-9)	|	[Previous MinorFail outcome](#minorfail-outcome-number-8)	|	[Next MinorFail outcome](#minorfail-outcome-number-10)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-src-vocabularies-permitting-stages|
|----|----|
|Title|Standalone&#32;module&#32;src/vocabularies/permitting&lowbar;stages.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Module vocabularies/permitting&lowbar;stages](https://github.com/Accord-Project/aec3po/blob/HEAD/src/vocabularies/permitting_stages.ttl)|

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
|[Section top](#minorfail-outcome-number-9)|Description|Statement&#32;not&#32;supported|
|[Section top](#minorfail-outcome-number-9)|Pointer|<pre lang="Turtle"><code>&#91;]&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32;owl:hasValue&#32;aec3po:PermittingStageNomenclature&#32;;  &#10; &#32; &#32; &#32; &#32;owl:onProperty&#32;skos:inScheme&#32;.</code></pre>|

***
### MinorFail Outcome number 10

[Jump to summary definition](#summary-MinorFail-10)	|	[Previous MinorFail outcome](#minorfail-outcome-number-9)	|	[Next MinorFail outcome](#minorfail-outcome-number-11)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-src-vocabularies-permitting-stages|
|----|----|
|Title|Standalone&#32;module&#32;src/vocabularies/permitting&lowbar;stages.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Module vocabularies/permitting&lowbar;stages](https://github.com/Accord-Project/aec3po/blob/HEAD/src/vocabularies/permitting_stages.ttl)|

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
|[Section top](#minorfail-outcome-number-10)|Description|Statement&#32;not&#32;supported&#32;in&#32;a&#32;Sub&#32;Class&#32;Expression|
|[Section top](#minorfail-outcome-number-10)|Pointer|<pre lang="Turtle"><code>&#91;]&#32;owl:intersectionOf&#32;(&#32;skos:Concept&#32; &#91;&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:hasValue&#32;aec3po:PermittingStageNomenclature&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:onProperty&#32;skos:inScheme&#32;]&#32;)&#32;.</code></pre>|

***
### MinorFail Outcome number 11

[Jump to summary definition](#summary-MinorFail-11)	|	[Previous MinorFail outcome](#minorfail-outcome-number-10)	|	[Next MinorFail outcome](#minorfail-outcome-number-12)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-src-vocabularies-disciplines|
|----|----|
|Title|Standalone&#32;module&#32;src/vocabularies/disciplines.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Module vocabularies/disciplines](https://github.com/Accord-Project/aec3po/blob/HEAD/src/vocabularies/disciplines.ttl)|

#### Criterion detail
|Identifier|[domain-and-range-referencing](https://ns.inria.fr/olivaw#domain-and-range-referencing)|
|----|----|
|Title|Domain&#32;and&#32;range&#32;referencing&#32;test|
|Description|A&#32;test&#32;case&#32;from&#32;the&#32;Best&#32;Practices&#32;tests&#32;checking&#32;if&#32;all&#32;the&#32;ranges&#32;and&#32;domains&#32;from&#32;the&#32;test&#32;subject&#32;point&#32;to&#32;terms&#32;that&#32;are&#32;defined&#32;in&#32;the&#32;vocabulary.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-11)|Identifier|`range-out-of-vocabulary`|
|[Section top](#minorfail-outcome-number-11)|Title|Range&#32;out&#32;of&#32;vocabulary|
|[Section top](#minorfail-outcome-number-11)|Description|Some&#32;properties&#32;have&#32;a&#32;range&#32;out&#32;of&#32;the&#32;ontology|
|[Section top](#minorfail-outcome-number-11)|Pointer|<pre lang="Turtle"><code>:hasDiscipline&#32;a&#32;owl:ObjectProperty&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;has&#32;discipline&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;Links&#32;an&#32;entity&#32;(procedure,&#32;statement,&#32;verifier,&#32;...)&#32;to&#32;the...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32;:discipline&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:range&#32;&lowbar;:n44c9384d349b4d27a65bb63d7ad8cd57b1,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#91;&#32;rdfs:subClassOf&#32;&lowbar;:n44c9384d349b4d27a65bb63d7ad8cd57b1,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;skos:Concept,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;:Discipline&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:equivalentClass&#32;:Discipline&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:intersectionOf&#32;(&#32;skos:Concept&#32;&lowbar;:n44c9384d349b4d27a65bb63d7ad8cd57b1&#32;)&#32;],  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;skos:Concept,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;:Discipline&#32;.  &#10;&lowbar;:n44c9384d349b4d27a65bb63d7ad8cd57b1&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32;owl:hasValue&#32;:DisciplineNomenclature&#32;;  &#10; &#32; &#32; &#32; &#32;owl:onProperty&#32;skos:inScheme&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-11)|Pointer|http://www.w3.org/2004/02/skos/core#Concept|

***
### MinorFail Outcome number 12

[Jump to summary definition](#summary-MinorFail-12)	|	[Previous MinorFail outcome](#minorfail-outcome-number-11)	|	[Next MinorFail outcome](#minorfail-outcome-number-13)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-src-vocabularies-disciplines|
|----|----|
|Title|Standalone&#32;module&#32;src/vocabularies/disciplines.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Module vocabularies/disciplines](https://github.com/Accord-Project/aec3po/blob/HEAD/src/vocabularies/disciplines.ttl)|

#### Criterion detail
|Identifier|[labeled-terms](https://ns.inria.fr/olivaw#labeled-terms)|
|----|----|
|Title|Term&#32;labeling&#32;test|
|Description|A&#32;test&#32;case&#32;from&#32;the&#32;Best&#32;Practices&#32;tests&#32;checking&#32;if&#32;all&#32;the&#32;terms&#32;of&#32;the&#32;subject&#32;have&#32;a&#32;rdfs:label&#32;property&#32;pointing&#32;to&#32;a&#32;literal&#32;in&#32;English|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-12)|Identifier|`not-labeled-term`|
|[Section top](#minorfail-outcome-number-12)|Title|Terms&#32;not&#32;labeled|
|[Section top](#minorfail-outcome-number-12)|Description|The&#32;following&#32;terms&#32;have&#32;no&#32;rdfs:label&#32;to&#32;define&#32;it&#32;in&#32;natural&#32;language|
|[Section top](#minorfail-outcome-number-12)|Pointer|<pre lang="Turtle"><code>:Discipline-architecture&#32;a&#32;owl:NamedIndividual,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;skos:Concept,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;:Discipline&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32;:discipline&#32;;  &#10; &#32; &#32; &#32; &#32;skos:definition&#32; &#34;The&#32;Architecture&#32;discipline.&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;skos:inScheme&#32;:DisciplineNomenclature&#32;;  &#10; &#32; &#32; &#32; &#32;skos:prefLabel&#32; &#34;architecture&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;skos:topConceptOf&#32;:DisciplineNomenclature&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-12)|Pointer|<pre lang="Turtle"><code>:Discipline-buildingServices&#32;a&#32;owl:NamedIndividual,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;skos:Concept,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;:Discipline&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32;:discipline&#32;;  &#10; &#32; &#32; &#32; &#32;skos:definition&#32; &#34;The&#32;Building&#32;Services&#32;discipline.&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;skos:inScheme&#32;:DisciplineNomenclature&#32;;  &#10; &#32; &#32; &#32; &#32;skos:prefLabel&#32; &#34;building&#32;services&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;skos:topConceptOf&#32;:DisciplineNomenclature&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-12)|Pointer|<pre lang="Turtle"><code>:Discipline-construction&#32;a&#32;owl:NamedIndividual,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;skos:Concept,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;:Discipline&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32;:discipline&#32;;  &#10; &#32; &#32; &#32; &#32;skos:definition&#32; &#34;The&#32;Construction&#32;discipline.&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;skos:inScheme&#32;:DisciplineNomenclature&#32;;  &#10; &#32; &#32; &#32; &#32;skos:prefLabel&#32; &#34;construction&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;skos:topConceptOf&#32;:DisciplineNomenclature&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-12)|Pointer|<pre lang="Turtle"><code>:Discipline-planning&#32;a&#32;owl:NamedIndividual,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;skos:Concept,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;:Discipline&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32;:discipline&#32;;  &#10; &#32; &#32; &#32; &#32;skos:definition&#32; &#34;The&#32;Planning&#32;discipline.&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;skos:inScheme&#32;:DisciplineNomenclature&#32;;  &#10; &#32; &#32; &#32; &#32;skos:prefLabel&#32; &#34;planning&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;skos:topConceptOf&#32;:DisciplineNomenclature&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-12)|Pointer|<pre lang="Turtle"><code>:Discipline-structuralEngineering&#32;a&#32;owl:NamedIndividual,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;skos:Concept,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;:Discipline&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32;:discipline&#32;;  &#10; &#32; &#32; &#32; &#32;skos:definition&#32; &#34;The&#32;Structural&#32;Engineering&#32;discipline.&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;skos:inScheme&#32;:DisciplineNomenclature&#32;;  &#10; &#32; &#32; &#32; &#32;skos:prefLabel&#32; &#34;structural&#32;engineering&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;skos:topConceptOf&#32;:DisciplineNomenclature&#32;.</code></pre>|

***
### MinorFail Outcome number 13

[Jump to summary definition](#summary-MinorFail-13)	|	[Previous MinorFail outcome](#minorfail-outcome-number-12)	|	[Next MinorFail outcome](#minorfail-outcome-number-14)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-src-vocabularies-disciplines|
|----|----|
|Title|Standalone&#32;module&#32;src/vocabularies/disciplines.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Module vocabularies/disciplines](https://github.com/Accord-Project/aec3po/blob/HEAD/src/vocabularies/disciplines.ttl)|

#### Criterion detail
|Identifier|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|
|----|----|
|Title|Profile&#32;compatibility&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;check&#32;whether&#32;the&#32;test&#32;subject&#32;is&#32;compatible&#32;with&#32;a&#32;profile&#32;or&#32;not,&#32;and&#32;if&#32;it&#32;is&#32;not,&#32;why.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-13)|Identifier|`owl-ql-profile-error`|
|[Section top](#minorfail-outcome-number-13)|Title|OWL&#32;QL&#32;Profile&#32;incompatible|
|[Section top](#minorfail-outcome-number-13)|Description|Class&#32;Expression&#32;not&#32;supported&#32;with&#32;owl:equivalentClass|
|[Section top](#minorfail-outcome-number-13)|Pointer|<pre lang="Turtle"><code>aec3po:Discipline&#32;a&#32;owl:Class&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;Discipline&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;The&#32;AEC&#32;discipline&#32;to&#32;which&#32;something&#32;pertains.&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32;aec3po:discipline&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:subClassOf&#32;skos:Concept&#32;;  &#10; &#32; &#32; &#32; &#32;owl:equivalentClass&#32; &#91;&#32;owl:intersectionOf&#32;(&#32;skos:Concept&#32; &#91;&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:hasValue&#32;aec3po:DisciplineNomenclature&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:onProperty&#32;skos:inScheme&#32;]&#32;)&#32;]&#32;.</code></pre>|

***
### MinorFail Outcome number 14

[Jump to summary definition](#summary-MinorFail-14)	|	[Previous MinorFail outcome](#minorfail-outcome-number-13)	|	[Next MinorFail outcome](#minorfail-outcome-number-15)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-src-vocabularies-disciplines|
|----|----|
|Title|Standalone&#32;module&#32;src/vocabularies/disciplines.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Module vocabularies/disciplines](https://github.com/Accord-Project/aec3po/blob/HEAD/src/vocabularies/disciplines.ttl)|

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
|[Section top](#minorfail-outcome-number-14)|Description|Statement&#32;not&#32;supported|
|[Section top](#minorfail-outcome-number-14)|Pointer|<pre lang="Turtle"><code>&#91;]&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32;owl:hasValue&#32;aec3po:DisciplineNomenclature&#32;;  &#10; &#32; &#32; &#32; &#32;owl:onProperty&#32;skos:inScheme&#32;.</code></pre>|

***
### MinorFail Outcome number 15

[Jump to summary definition](#summary-MinorFail-15)	|	[Previous MinorFail outcome](#minorfail-outcome-number-14)	|	[Next MinorFail outcome](#minorfail-outcome-number-16)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-src-vocabularies-disciplines|
|----|----|
|Title|Standalone&#32;module&#32;src/vocabularies/disciplines.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Module vocabularies/disciplines](https://github.com/Accord-Project/aec3po/blob/HEAD/src/vocabularies/disciplines.ttl)|

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
|[Section top](#minorfail-outcome-number-15)|Description|Statement&#32;not&#32;supported&#32;in&#32;a&#32;Sub&#32;Class&#32;Expression|
|[Section top](#minorfail-outcome-number-15)|Pointer|<pre lang="Turtle"><code>&#91;]&#32;owl:intersectionOf&#32;(&#32;skos:Concept&#32; &#91;&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:hasValue&#32;aec3po:DisciplineNomenclature&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:onProperty&#32;skos:inScheme&#32;]&#32;)&#32;.</code></pre>|

***
### MinorFail Outcome number 16

[Jump to summary definition](#summary-MinorFail-16)	|	[Previous MinorFail outcome](#minorfail-outcome-number-15)	|	[Next MinorFail outcome](#minorfail-outcome-number-17)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-src-vocabularies-check-method-operators|
|----|----|
|Title|Standalone&#32;module&#32;src/vocabularies/check&lowbar;method&lowbar;operators.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Module vocabularies/check&lowbar;method&lowbar;operators](https://github.com/Accord-Project/aec3po/blob/HEAD/src/vocabularies/check_method_operators.ttl)|

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
|[Section top](#minorfail-outcome-number-16)|Pointer|<pre lang="Turtle"><code>:CheckMethodOperator-exists&#32;a&#32;owl:NamedIndividual,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;skos:Concept,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;:CheckMethodOperator&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32;:check&lowbar;method&lowbar;operators&#32;;  &#10; &#32; &#32; &#32; &#32;skos:definition&#32; &#34;exists&#32;operator.&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;skos:inScheme&#32;:CheckMethodOperatorNomenclature&#32;;  &#10; &#32; &#32; &#32; &#32;skos:prefLabel&#32; &#34;exists&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;skos:topConceptOf&#32;:CheckMethodOperatorNomenclature&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-16)|Pointer|<pre lang="Turtle"><code>:CheckMethodOperator-notExists&#32;a&#32;owl:NamedIndividual,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;skos:Concept,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;:CheckMethodOperator&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32;:check&lowbar;method&lowbar;operators&#32;;  &#10; &#32; &#32; &#32; &#32;skos:definition&#32; &#34;not&#32;exists&#32;operator.&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;skos:inScheme&#32;:CheckMethodOperatorNomenclature&#32;;  &#10; &#32; &#32; &#32; &#32;skos:prefLabel&#32; &#34;not&#32;exists&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;skos:topConceptOf&#32;:CheckMethodOperatorNomenclature&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-16)|Pointer|<pre lang="Turtle"><code>:CheckMethodOperator-forall&#32;a&#32;owl:NamedIndividual,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;skos:Concept,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;:CheckMethodOperator&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32;:check&lowbar;method&lowbar;operators&#32;;  &#10; &#32; &#32; &#32; &#32;skos:definition&#32; &#34;forall&#32;operator.&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;skos:inScheme&#32;:CheckMethodOperatorNomenclature&#32;;  &#10; &#32; &#32; &#32; &#32;skos:prefLabel&#32; &#34;forall&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;skos:topConceptOf&#32;:CheckMethodOperatorNomenclature&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-16)|Pointer|<pre lang="Turtle"><code>:CheckMethodOperator-addition&#32;a&#32;owl:NamedIndividual,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;skos:Concept,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;:CheckMethodOperator&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32;:check&lowbar;method&lowbar;operators&#32;;  &#10; &#32; &#32; &#32; &#32;skos:definition&#32; &#34;addition&#32;operator.&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;skos:inScheme&#32;:CheckMethodOperatorNomenclature&#32;;  &#10; &#32; &#32; &#32; &#32;skos:prefLabel&#32; &#34;addition&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;skos:topConceptOf&#32;:CheckMethodOperatorNomenclature&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-16)|Pointer|<pre lang="Turtle"><code>:CheckMethodOperator-multiplication&#32;a&#32;owl:NamedIndividual,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;skos:Concept,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;:CheckMethodOperator&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32;:check&lowbar;method&lowbar;operators&#32;;  &#10; &#32; &#32; &#32; &#32;skos:definition&#32; &#34;multiplication&#32;Operator.&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;skos:inScheme&#32;:CheckMethodOperatorNomenclature&#32;;  &#10; &#32; &#32; &#32; &#32;skos:prefLabel&#32; &#34;multiplication&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;skos:topConceptOf&#32;:CheckMethodOperatorNomenclature&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-16)|Pointer|<pre lang="Turtle"><code>:CheckMethodOperator-subtraction&#32;a&#32;owl:NamedIndividual,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;skos:Concept,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;:CheckMethodOperator&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32;:check&lowbar;method&lowbar;operators&#32;;  &#10; &#32; &#32; &#32; &#32;skos:definition&#32; &#34;subtraction&#32;operator.&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;skos:inScheme&#32;:CheckMethodOperatorNomenclature&#32;;  &#10; &#32; &#32; &#32; &#32;skos:prefLabel&#32; &#34;subtraction&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;skos:topConceptOf&#32;:CheckMethodOperatorNomenclature&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-16)|Pointer|<pre lang="Turtle"><code>:CheckMethodOperator-division&#32;a&#32;owl:NamedIndividual,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;skos:Concept,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;:CheckMethodOperator&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32;:check&lowbar;method&lowbar;operators&#32;;  &#10; &#32; &#32; &#32; &#32;skos:definition&#32; &#34;division&#32;Operator.&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;skos:inScheme&#32;:CheckMethodOperatorNomenclature&#32;;  &#10; &#32; &#32; &#32; &#32;skos:prefLabel&#32; &#34;division&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;skos:topConceptOf&#32;:CheckMethodOperatorNomenclature&#32;.</code></pre>|

***
### MinorFail Outcome number 17

[Jump to summary definition](#summary-MinorFail-17)	|	[Previous MinorFail outcome](#minorfail-outcome-number-16)	|	[Next MinorFail outcome](#minorfail-outcome-number-18)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-src-vocabularies-check-method-operators|
|----|----|
|Title|Standalone&#32;module&#32;src/vocabularies/check&lowbar;method&lowbar;operators.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Module vocabularies/check&lowbar;method&lowbar;operators](https://github.com/Accord-Project/aec3po/blob/HEAD/src/vocabularies/check_method_operators.ttl)|

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
|[Section top](#minorfail-outcome-number-17)|Description|Statement&#32;not&#32;supported|
|[Section top](#minorfail-outcome-number-17)|Pointer|<pre lang="Turtle"><code>aec3po:hasOperator&#32;a&#32;owl:FunctionalProperty,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:ObjectProperty&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;has&#32;operator&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;The&#32;operator&#32;of&#32;a&#32;feature&#32;of&#32;interest&#32;or&#32;a&#32;property&#32;of&#32;that&#32;...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32;aec3po:check&lowbar;method&lowbar;Operators&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:range&#32;aec3po:CheckMethod&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:subPropertyOf&#32;aec3po:hasDesign&#32;.</code></pre>|

***
### MinorFail Outcome number 18

[Jump to summary definition](#summary-MinorFail-18)	|	[Previous MinorFail outcome](#minorfail-outcome-number-17)	|	[Next MinorFail outcome](#minorfail-outcome-number-19)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-src-vocabularies-check-method-operators|
|----|----|
|Title|Standalone&#32;module&#32;src/vocabularies/check&lowbar;method&lowbar;operators.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Module vocabularies/check&lowbar;method&lowbar;operators](https://github.com/Accord-Project/aec3po/blob/HEAD/src/vocabularies/check_method_operators.ttl)|

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
|[Section top](#minorfail-outcome-number-18)|Description|Class&#32;Expression&#32;not&#32;supported&#32;with&#32;owl:equivalentClass|
|[Section top](#minorfail-outcome-number-18)|Pointer|<pre lang="Turtle"><code>aec3po:CheckMethodOperator&#32;a&#32;owl:Class&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;check&#32;method&#32;operator&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;Formally&#32;defined&#32;as&#32;the&#32;set&#32;of&#32;skos:Concept&#32;in&#32;concept&#32;schem...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32;aec3po:check&lowbar;method&lowbar;operators&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:subClassOf&#32;skos:Concept,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;aec3po:CheckMethod&#32;;  &#10; &#32; &#32; &#32; &#32;owl:equivalentClass&#32; &#91;&#32;owl:intersectionOf&#32;(&#32;skos:Concept&#32; &#91;&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:hasValue&#32;aec3po:CheckMethodOperatorNomenclature&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:onProperty&#32;skos:inScheme&#32;]&#32;)&#32;]&#32;.</code></pre>|

***
### MinorFail Outcome number 19

[Jump to summary definition](#summary-MinorFail-19)	|	[Previous MinorFail outcome](#minorfail-outcome-number-18)	|	[Next MinorFail outcome](#minorfail-outcome-number-20)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-src-vocabularies-check-method-operators|
|----|----|
|Title|Standalone&#32;module&#32;src/vocabularies/check&lowbar;method&lowbar;operators.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Module vocabularies/check&lowbar;method&lowbar;operators](https://github.com/Accord-Project/aec3po/blob/HEAD/src/vocabularies/check_method_operators.ttl)|

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
|[Section top](#minorfail-outcome-number-19)|Description|Statement&#32;not&#32;supported|
|[Section top](#minorfail-outcome-number-19)|Pointer|<pre lang="Turtle"><code>&#91;]&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32;owl:hasValue&#32;aec3po:CheckMethodOperatorNomenclature&#32;;  &#10; &#32; &#32; &#32; &#32;owl:onProperty&#32;skos:inScheme&#32;.</code></pre>|

***
### MinorFail Outcome number 20

[Jump to summary definition](#summary-MinorFail-20)	|	[Previous MinorFail outcome](#minorfail-outcome-number-19)	|	[Next MinorFail outcome](#minorfail-outcome-number-21)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-src-vocabularies-check-method-operators|
|----|----|
|Title|Standalone&#32;module&#32;src/vocabularies/check&lowbar;method&lowbar;operators.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Module vocabularies/check&lowbar;method&lowbar;operators](https://github.com/Accord-Project/aec3po/blob/HEAD/src/vocabularies/check_method_operators.ttl)|

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
|[Section top](#minorfail-outcome-number-20)|Description|Statement&#32;not&#32;supported&#32;in&#32;a&#32;Sub&#32;Class&#32;Expression|
|[Section top](#minorfail-outcome-number-20)|Pointer|<pre lang="Turtle"><code>&#91;]&#32;owl:intersectionOf&#32;(&#32;skos:Concept&#32; &#91;&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:hasValue&#32;aec3po:CheckMethodOperatorNomenclature&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:onProperty&#32;skos:inScheme&#32;]&#32;)&#32;.</code></pre>|

***
### MinorFail Outcome number 21

[Jump to summary definition](#summary-MinorFail-21)	|	[Previous MinorFail outcome](#minorfail-outcome-number-20)	|	[Next MinorFail outcome](#minorfail-outcome-number-22)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-src-vocabularies-check-method-comparators|
|----|----|
|Title|Standalone&#32;module&#32;src/vocabularies/check&lowbar;method&lowbar;comparators.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Module vocabularies/check&lowbar;method&lowbar;comparators](https://github.com/Accord-Project/aec3po/blob/HEAD/src/vocabularies/check_method_comparators.ttl)|

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
|[Section top](#minorfail-outcome-number-21)|Pointer|<pre lang="Turtle"><code>:CheckMethodcomparator-logicalAND&#32;a&#32;owl:NamedIndividual,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;skos:Concept,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;:CheckMethodComparator&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32;:check&lowbar;method&lowbar;comparators&#32;;  &#10; &#32; &#32; &#32; &#32;skos:definition&#32; &#34;logical&#32;AND&#32;comparator.&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;skos:inScheme&#32;:CheckMethodComparatorNomenclature&#32;;  &#10; &#32; &#32; &#32; &#32;skos:prefLabel&#32; &#34;logicalAND&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;skos:topConceptOf&#32;:CheckMethodComparatorNomenclature&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-21)|Pointer|<pre lang="Turtle"><code>:CheckMethodcomparator-eq&#32;a&#32;owl:NamedIndividual,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;skos:Concept,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;:CheckMethodcomparator&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32;:check&lowbar;method&lowbar;comparators&#32;;  &#10; &#32; &#32; &#32; &#32;skos:definition&#32; &#34;equal-to&#32;comparator.&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;skos:inScheme&#32;:CheckMethodComparatorNomenclature&#32;;  &#10; &#32; &#32; &#32; &#32;skos:prefLabel&#32; &#34;equal-to&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;skos:topConceptOf&#32;:CheckMethodComparatorNomenclature&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-21)|Pointer|<pre lang="Turtle"><code>:CheckMethodComparator-neq&#32;a&#32;owl:NamedIndividual,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;skos:Concept,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;:CheckMethodComparator&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32;:check&lowbar;method&lowbar;comparators&#32;;  &#10; &#32; &#32; &#32; &#32;skos:definition&#32; &#34;not&#32;equal-to&#32;comparator.&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;skos:inScheme&#32;:CheckMethodComparatorNomenclature&#32;;  &#10; &#32; &#32; &#32; &#32;skos:prefLabel&#32; &#34;not&#32;equal-to&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;skos:topConceptOf&#32;:CheckMethodComparatorNomenclature&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-21)|Pointer|<pre lang="Turtle"><code>:CheckMethodComparator-lt&#32;a&#32;owl:NamedIndividual,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;skos:Concept,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;:CheckMethodComparator&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32;:check&lowbar;method&lowbar;comparators&#32;;  &#10; &#32; &#32; &#32; &#32;skos:definition&#32; &#34;less-than&#32;comparator.&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;skos:inScheme&#32;:CheckMethodComparatorNomenclature&#32;;  &#10; &#32; &#32; &#32; &#32;skos:prefLabel&#32; &#34;less&#32;than&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;skos:topConceptOf&#32;:CheckMethodComparatorNomenclature&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-21)|Pointer|<pre lang="Turtle"><code>:CheckMethodComparator-le&#32;a&#32;owl:NamedIndividual,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;skos:Concept,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;:CheckMethodComparator&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32;:check&lowbar;method&lowbar;comparators&#32;;  &#10; &#32; &#32; &#32; &#32;skos:definition&#32; &#34;less-equal&#32;comparator.&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;skos:inScheme&#32;:CheckMethodComparatorNomenclature&#32;;  &#10; &#32; &#32; &#32; &#32;skos:prefLabel&#32; &#34;less&#32;equal&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;skos:topConceptOf&#32;:CheckMethodComparatorNomenclature&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-21)|Pointer|<pre lang="Turtle"><code>:CheckMethodComparator-gt&#32;a&#32;owl:NamedIndividual,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;skos:Concept,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;:CheckMethodComparator&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32;:check&lowbar;method&lowbar;comparators&#32;;  &#10; &#32; &#32; &#32; &#32;skos:definition&#32; &#34;greater-than&#32;comparator.&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;skos:inScheme&#32;:CheckMethodComparatorNomenclature&#32;;  &#10; &#32; &#32; &#32; &#32;skos:prefLabel&#32; &#34;greater&#32;than&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;skos:topConceptOf&#32;:CheckMethodComparatorNomenclature&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-21)|Pointer|<pre lang="Turtle"><code>:CheckMethodComparator-ge&#32;a&#32;owl:NamedIndividual,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;skos:Concept,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;:CheckMethodComparator&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32;:check&lowbar;method&lowbar;comparators&#32;;  &#10; &#32; &#32; &#32; &#32;skos:definition&#32; &#34;greater-equal&#32;comparator.&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;skos:inScheme&#32;:CheckMethodComparatorNomenclature&#32;;  &#10; &#32; &#32; &#32; &#32;skos:prefLabel&#32; &#34;greater&#32;equal&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;skos:topConceptOf&#32;:CheckMethodComparatorNomenclature&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-21)|Pointer|<pre lang="Turtle"><code>:CheckMethodComparator-logicalOR&#32;a&#32;owl:NamedIndividual,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;skos:Concept,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;:CheckMethodComparator&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32;:check&lowbar;method&lowbar;comparators&#32;;  &#10; &#32; &#32; &#32; &#32;skos:definition&#32; &#34;logical&#32;OR&#32;comparator.&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;skos:inScheme&#32;:CheckMethodComparatorNomenclature&#32;;  &#10; &#32; &#32; &#32; &#32;skos:prefLabel&#32; &#34;logicalOR&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;skos:topConceptOf&#32;:CheckMethodComparatorNomenclature&#32;.</code></pre>|

***
### MinorFail Outcome number 22

[Jump to summary definition](#summary-MinorFail-22)	|	[Previous MinorFail outcome](#minorfail-outcome-number-21)	|	[Next MinorFail outcome](#minorfail-outcome-number-23)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-src-vocabularies-check-method-comparators|
|----|----|
|Title|Standalone&#32;module&#32;src/vocabularies/check&lowbar;method&lowbar;comparators.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Module vocabularies/check&lowbar;method&lowbar;comparators](https://github.com/Accord-Project/aec3po/blob/HEAD/src/vocabularies/check_method_comparators.ttl)|

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
|[Section top](#minorfail-outcome-number-22)|Description|Statement&#32;not&#32;supported|
|[Section top](#minorfail-outcome-number-22)|Pointer|<pre lang="Turtle"><code>aec3po:hasComparator&#32;a&#32;owl:FunctionalProperty,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:ObjectProperty&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;has&#32;comparator&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;The&#32;comparator&#32;of&#32;a&#32;feature&#32;of&#32;interest&#32;or&#32;a&#32;property&#32;of&#32;tha...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32;aec3po:check&lowbar;method&lowbar;comparators&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:range&#32;aec3po:CheckMethod&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:subPropertyOf&#32;aec3po:hasDesign&#32;.</code></pre>|

***
### MinorFail Outcome number 23

[Jump to summary definition](#summary-MinorFail-23)	|	[Previous MinorFail outcome](#minorfail-outcome-number-22)	|	[Next MinorFail outcome](#minorfail-outcome-number-24)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-src-vocabularies-check-method-comparators|
|----|----|
|Title|Standalone&#32;module&#32;src/vocabularies/check&lowbar;method&lowbar;comparators.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Module vocabularies/check&lowbar;method&lowbar;comparators](https://github.com/Accord-Project/aec3po/blob/HEAD/src/vocabularies/check_method_comparators.ttl)|

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
|[Section top](#minorfail-outcome-number-23)|Description|Class&#32;Expression&#32;not&#32;supported&#32;with&#32;owl:equivalentClass|
|[Section top](#minorfail-outcome-number-23)|Pointer|<pre lang="Turtle"><code>aec3po:CheckMethodComparator&#32;a&#32;owl:Class&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;check&#32;method&#32;comparator&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;Formally&#32;defined&#32;as&#32;the&#32;set&#32;of&#32;skos:Concept&#32;in&#32;concept&#32;schem...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32;aec3po:check&lowbar;method&lowbar;comparators&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:subClassOf&#32;skos:Concept,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;aec3po:CheckMethod&#32;;  &#10; &#32; &#32; &#32; &#32;owl:equivalentClass&#32; &#91;&#32;owl:intersectionOf&#32;(&#32;skos:Concept&#32; &#91;&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:hasValue&#32;aec3po:CheckMethodComparatorNomenclature&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:onProperty&#32;skos:inScheme&#32;]&#32;)&#32;]&#32;.</code></pre>|

***
### MinorFail Outcome number 24

[Jump to summary definition](#summary-MinorFail-24)	|	[Previous MinorFail outcome](#minorfail-outcome-number-23)	|	[Next MinorFail outcome](#minorfail-outcome-number-25)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-src-vocabularies-check-method-comparators|
|----|----|
|Title|Standalone&#32;module&#32;src/vocabularies/check&lowbar;method&lowbar;comparators.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Module vocabularies/check&lowbar;method&lowbar;comparators](https://github.com/Accord-Project/aec3po/blob/HEAD/src/vocabularies/check_method_comparators.ttl)|

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
|[Section top](#minorfail-outcome-number-24)|Description|Statement&#32;not&#32;supported|
|[Section top](#minorfail-outcome-number-24)|Pointer|<pre lang="Turtle"><code>&#91;]&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32;owl:hasValue&#32;aec3po:CheckMethodComparatorNomenclature&#32;;  &#10; &#32; &#32; &#32; &#32;owl:onProperty&#32;skos:inScheme&#32;.</code></pre>|

***
### MinorFail Outcome number 25

[Jump to summary definition](#summary-MinorFail-25)	|	[Previous MinorFail outcome](#minorfail-outcome-number-24)	|	[Next MinorFail outcome](#minorfail-outcome-number-26)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-src-vocabularies-check-method-comparators|
|----|----|
|Title|Standalone&#32;module&#32;src/vocabularies/check&lowbar;method&lowbar;comparators.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Module vocabularies/check&lowbar;method&lowbar;comparators](https://github.com/Accord-Project/aec3po/blob/HEAD/src/vocabularies/check_method_comparators.ttl)|

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
|[Section top](#minorfail-outcome-number-25)|Description|Statement&#32;not&#32;supported&#32;in&#32;a&#32;Sub&#32;Class&#32;Expression|
|[Section top](#minorfail-outcome-number-25)|Pointer|<pre lang="Turtle"><code>&#91;]&#32;owl:intersectionOf&#32;(&#32;skos:Concept&#32; &#91;&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:hasValue&#32;aec3po:CheckMethodComparatorNomenclature&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:onProperty&#32;skos:inScheme&#32;]&#32;)&#32;.</code></pre>|

***
### MinorFail Outcome number 26

[Jump to summary definition](#summary-MinorFail-26)	|	[Previous MinorFail outcome](#minorfail-outcome-number-25)	|	[Next MinorFail outcome](#minorfail-outcome-number-27)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-src-vocabularies-check-method-comparators|
|----|----|
|Title|Standalone&#32;module&#32;src/vocabularies/check&lowbar;method&lowbar;comparators.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Module vocabularies/check&lowbar;method&lowbar;comparators](https://github.com/Accord-Project/aec3po/blob/HEAD/src/vocabularies/check_method_comparators.ttl)|

#### Criterion detail
|Identifier|[terms-differenciation](https://ns.inria.fr/olivaw#terms-differenciation)|
|----|----|
|Title|Terms&#32;differenciation&#32;test|
|Description|A&#32;test&#32;case&#32;from&#32;the&#32;Best&#32;Practices&#32;tests&#32;checking&#32;if&#32;all&#32;the&#32;terms&#32;are&#32;different&#32;enough&#32;from&#32;each&#32;other&#32;according&#32;to&#32;the&#32;Levenshtein&#32;distance&#32;metric.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-26)|Identifier|`too-close-terms`|
|[Section top](#minorfail-outcome-number-26)|Title|Too&#32;close&#32;terms|
|[Section top](#minorfail-outcome-number-26)|Description|Some&#32;terms&#32;are&#32;too&#32;similar|
|[Section top](#minorfail-outcome-number-26)|Pointer|<pre lang="Turtle"><code>:CheckMethodComparator-gt&#32;a&#32;owl:NamedIndividual,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;skos:Concept,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;:CheckMethodComparator&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32;:check&lowbar;method&lowbar;comparators&#32;;  &#10; &#32; &#32; &#32; &#32;skos:definition&#32; &#34;greater-than&#32;comparator.&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;skos:inScheme&#32;:CheckMethodComparatorNomenclature&#32;;  &#10; &#32; &#32; &#32; &#32;skos:prefLabel&#32; &#34;greater&#32;than&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;skos:topConceptOf&#32;:CheckMethodComparatorNomenclature&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-26)|Pointer|<pre lang="Turtle"><code>:CheckMethodComparator-ge&#32;a&#32;owl:NamedIndividual,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;skos:Concept,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;:CheckMethodComparator&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32;:check&lowbar;method&lowbar;comparators&#32;;  &#10; &#32; &#32; &#32; &#32;skos:definition&#32; &#34;greater-equal&#32;comparator.&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;skos:inScheme&#32;:CheckMethodComparatorNomenclature&#32;;  &#10; &#32; &#32; &#32; &#32;skos:prefLabel&#32; &#34;greater&#32;equal&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;skos:topConceptOf&#32;:CheckMethodComparatorNomenclature&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-26)|Pointer|<pre lang="Turtle"><code>:CheckMethodComparator-le&#32;a&#32;owl:NamedIndividual,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;skos:Concept,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;:CheckMethodComparator&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32;:check&lowbar;method&lowbar;comparators&#32;;  &#10; &#32; &#32; &#32; &#32;skos:definition&#32; &#34;less-equal&#32;comparator.&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;skos:inScheme&#32;:CheckMethodComparatorNomenclature&#32;;  &#10; &#32; &#32; &#32; &#32;skos:prefLabel&#32; &#34;less&#32;equal&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;skos:topConceptOf&#32;:CheckMethodComparatorNomenclature&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-26)|Pointer|<pre lang="Turtle"><code>:CheckMethodComparator-lt&#32;a&#32;owl:NamedIndividual,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;skos:Concept,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;:CheckMethodComparator&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32;:check&lowbar;method&lowbar;comparators&#32;;  &#10; &#32; &#32; &#32; &#32;skos:definition&#32; &#34;less-than&#32;comparator.&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;skos:inScheme&#32;:CheckMethodComparatorNomenclature&#32;;  &#10; &#32; &#32; &#32; &#32;skos:prefLabel&#32; &#34;less&#32;than&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;skos:topConceptOf&#32;:CheckMethodComparatorNomenclature&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-26)|Pointer|<pre lang="Turtle"><code>:CheckMethodComparator-neq&#32;a&#32;owl:NamedIndividual,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;skos:Concept,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;:CheckMethodComparator&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32;:check&lowbar;method&lowbar;comparators&#32;;  &#10; &#32; &#32; &#32; &#32;skos:definition&#32; &#34;not&#32;equal-to&#32;comparator.&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;skos:inScheme&#32;:CheckMethodComparatorNomenclature&#32;;  &#10; &#32; &#32; &#32; &#32;skos:prefLabel&#32; &#34;not&#32;equal-to&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;skos:topConceptOf&#32;:CheckMethodComparatorNomenclature&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-26)|Pointer|<pre lang="Turtle"><code>:CheckMethodcomparator-eq&#32;a&#32;owl:NamedIndividual,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;skos:Concept,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;:CheckMethodcomparator&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32;:check&lowbar;method&lowbar;comparators&#32;;  &#10; &#32; &#32; &#32; &#32;skos:definition&#32; &#34;equal-to&#32;comparator.&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;skos:inScheme&#32;:CheckMethodComparatorNomenclature&#32;;  &#10; &#32; &#32; &#32; &#32;skos:prefLabel&#32; &#34;equal-to&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;skos:topConceptOf&#32;:CheckMethodComparatorNomenclature&#32;.</code></pre>|

***
### MinorFail Outcome number 27

[Jump to summary definition](#summary-MinorFail-27)	|	[Previous MinorFail outcome](#minorfail-outcome-number-26)	|	[Next MinorFail outcome](#minorfail-outcome-number-28)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-src-vocabularies-building-usage|
|----|----|
|Title|Standalone&#32;module&#32;src/vocabularies/building&lowbar;usage.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Module vocabularies/building&lowbar;usage](https://github.com/Accord-Project/aec3po/blob/HEAD/src/vocabularies/building_usage.ttl)|

#### Criterion detail
|Identifier|[domain-and-range-referencing](https://ns.inria.fr/olivaw#domain-and-range-referencing)|
|----|----|
|Title|Domain&#32;and&#32;range&#32;referencing&#32;test|
|Description|A&#32;test&#32;case&#32;from&#32;the&#32;Best&#32;Practices&#32;tests&#32;checking&#32;if&#32;all&#32;the&#32;ranges&#32;and&#32;domains&#32;from&#32;the&#32;test&#32;subject&#32;point&#32;to&#32;terms&#32;that&#32;are&#32;defined&#32;in&#32;the&#32;vocabulary.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-27)|Identifier|`range-out-of-vocabulary`|
|[Section top](#minorfail-outcome-number-27)|Title|Range&#32;out&#32;of&#32;vocabulary|
|[Section top](#minorfail-outcome-number-27)|Description|Some&#32;properties&#32;have&#32;a&#32;range&#32;out&#32;of&#32;the&#32;ontology|
|[Section top](#minorfail-outcome-number-27)|Pointer|<pre lang="Turtle"><code>:forBuildingUsage&#32;a&#32;owl:ObjectProperty&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;for&#32;building&#32;usage&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;The&#32;building&#32;usage&#32;for&#32;which&#32;a&#32;specific&#32;check,&#32;verifier,&#32;or&#32;...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32;:building&lowbar;usage&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:range&#32;&lowbar;:na1115b2f76a94270b3d2dc2ce60a85b2b1,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#91;&#32;rdfs:subClassOf&#32;&lowbar;:na1115b2f76a94270b3d2dc2ce60a85b2b1,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;skos:Concept,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;:BuildingUsage,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;:Design&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:equivalentClass&#32;:BuildingUsage&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:intersectionOf&#32;(&#32;skos:Concept&#32;&lowbar;:na1115b2f76a94270b3d2dc2ce60a85b2b1&#32;)&#32;],  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;skos:Concept,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;:BuildingUsage,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;:Design&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:subPropertyOf&#32;:forDesign&#32;.  &#10;&lowbar;:na1115b2f76a94270b3d2dc2ce60a85b2b1&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32;owl:hasValue&#32;:BuildingUsageNomenclature&#32;;  &#10; &#32; &#32; &#32; &#32;owl:onProperty&#32;skos:inScheme&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-27)|Pointer|<pre lang="Turtle"><code>:hasBuildingUsage&#32;a&#32;owl:FunctionalProperty,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:ObjectProperty&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;has&#32;building&#32;usage&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;The&#32;building&#32;usage&#32;design&#32;of&#32;a&#32;feature&#32;of&#32;interest&#32;or&#32;a&#32;prop...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32;:building&lowbar;usage&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:range&#32;&lowbar;:n4bb81fc0d09b4db692ffcfb556bc290db1,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#91;&#32;rdfs:subClassOf&#32;&lowbar;:n4bb81fc0d09b4db692ffcfb556bc290db1,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;skos:Concept,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;:BuildingUsage,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;:Design&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:equivalentClass&#32;:BuildingUsage&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:intersectionOf&#32;(&#32;skos:Concept&#32;&lowbar;:n4bb81fc0d09b4db692ffcfb556bc290db1&#32;)&#32;],  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;skos:Concept,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;:BuildingUsage,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;:Design&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:subPropertyOf&#32;:hasDesign&#32;.  &#10;&lowbar;:n4bb81fc0d09b4db692ffcfb556bc290db1&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32;owl:hasValue&#32;:BuildingUsageNomenclature&#32;;  &#10; &#32; &#32; &#32; &#32;owl:onProperty&#32;skos:inScheme&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-27)|Pointer|http://www.w3.org/2004/02/skos/core#Concept|

***
### MinorFail Outcome number 28

[Jump to summary definition](#summary-MinorFail-28)	|	[Previous MinorFail outcome](#minorfail-outcome-number-27)	|	[Next MinorFail outcome](#minorfail-outcome-number-29)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-src-vocabularies-building-usage|
|----|----|
|Title|Standalone&#32;module&#32;src/vocabularies/building&lowbar;usage.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Module vocabularies/building&lowbar;usage](https://github.com/Accord-Project/aec3po/blob/HEAD/src/vocabularies/building_usage.ttl)|

#### Criterion detail
|Identifier|[labeled-terms](https://ns.inria.fr/olivaw#labeled-terms)|
|----|----|
|Title|Term&#32;labeling&#32;test|
|Description|A&#32;test&#32;case&#32;from&#32;the&#32;Best&#32;Practices&#32;tests&#32;checking&#32;if&#32;all&#32;the&#32;terms&#32;of&#32;the&#32;subject&#32;have&#32;a&#32;rdfs:label&#32;property&#32;pointing&#32;to&#32;a&#32;literal&#32;in&#32;English|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-28)|Identifier|`not-labeled-term`|
|[Section top](#minorfail-outcome-number-28)|Title|Terms&#32;not&#32;labeled|
|[Section top](#minorfail-outcome-number-28)|Description|The&#32;following&#32;terms&#32;have&#32;no&#32;rdfs:label&#32;to&#32;define&#32;it&#32;in&#32;natural&#32;language|
|[Section top](#minorfail-outcome-number-28)|Pointer|<pre lang="Turtle"><code>:BuildingUsage-commercial&#32;a&#32;owl:NamedIndividual,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;skos:Concept,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;:BuildingUsage&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32;:building&lowbar;usage&#32;;  &#10; &#32; &#32; &#32; &#32;skos:definition&#32; &#34;Building&#32;has&#32;commercial&#32;usage.&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;skos:inScheme&#32;:BuildingUsageNomenclature&#32;;  &#10; &#32; &#32; &#32; &#32;skos:prefLabel&#32; &#34;commercial&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;skos:topConceptOf&#32;:BuildingUsageNomenclature&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-28)|Pointer|<pre lang="Turtle"><code>:BuildingUsage-residential&#32;a&#32;owl:NamedIndividual,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;skos:Concept,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;:BuildingUsage&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32;:building&lowbar;usage&#32;;  &#10; &#32; &#32; &#32; &#32;skos:definition&#32; &#34;Building&#32;has&#32;residential&#32;usage.&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;skos:inScheme&#32;:BuildingUsageNomenclature&#32;;  &#10; &#32; &#32; &#32; &#32;skos:prefLabel&#32; &#34;residential&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;skos:topConceptOf&#32;:BuildingUsageNomenclature&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-28)|Pointer|<pre lang="Turtle"><code>:BuildingUsage-cultural&#32;a&#32;owl:NamedIndividual,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;skos:Concept,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;:BuildingUsage&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32;:building&lowbar;usage&#32;;  &#10; &#32; &#32; &#32; &#32;skos:definition&#32; &#34;Building&#32;has&#32;cultural&#32;usage.&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;skos:inScheme&#32;:BuildingUsageNomenclature&#32;;  &#10; &#32; &#32; &#32; &#32;skos:prefLabel&#32; &#34;cultural&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;skos:topConceptOf&#32;:BuildingUsageNomenclature&#32;.</code></pre>|

***
### MinorFail Outcome number 29

[Jump to summary definition](#summary-MinorFail-29)	|	[Previous MinorFail outcome](#minorfail-outcome-number-28)	|	[Next MinorFail outcome](#minorfail-outcome-number-30)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-src-vocabularies-building-usage|
|----|----|
|Title|Standalone&#32;module&#32;src/vocabularies/building&lowbar;usage.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Module vocabularies/building&lowbar;usage](https://github.com/Accord-Project/aec3po/blob/HEAD/src/vocabularies/building_usage.ttl)|

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
|[Section top](#minorfail-outcome-number-29)|Description|Statement&#32;not&#32;supported|
|[Section top](#minorfail-outcome-number-29)|Pointer|<pre lang="Turtle"><code>aec3po:hasBuildingUsage&#32;a&#32;owl:FunctionalProperty,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:ObjectProperty&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;has&#32;building&#32;usage&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;The&#32;building&#32;usage&#32;design&#32;of&#32;a&#32;feature&#32;of&#32;interest&#32;or&#32;a&#32;prop...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32;aec3po:building&lowbar;usage&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:range&#32;aec3po:BuildingUsage&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:subPropertyOf&#32;aec3po:hasDesign&#32;.</code></pre>|

***
### MinorFail Outcome number 30

[Jump to summary definition](#summary-MinorFail-30)	|	[Previous MinorFail outcome](#minorfail-outcome-number-29)	|	[Next MinorFail outcome](#minorfail-outcome-number-31)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-src-vocabularies-building-usage|
|----|----|
|Title|Standalone&#32;module&#32;src/vocabularies/building&lowbar;usage.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Module vocabularies/building&lowbar;usage](https://github.com/Accord-Project/aec3po/blob/HEAD/src/vocabularies/building_usage.ttl)|

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
|[Section top](#minorfail-outcome-number-30)|Description|Class&#32;Expression&#32;not&#32;supported&#32;with&#32;owl:equivalentClass|
|[Section top](#minorfail-outcome-number-30)|Pointer|<pre lang="Turtle"><code>aec3po:BuildingUsage&#32;a&#32;owl:Class&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;building&#32;usage&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;Formally&#32;defined&#32;as&#32;the&#32;set&#32;of&#32;skos:Concept&#32;in&#32;concept&#32;schem...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32;aec3po:building&lowbar;usage&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:subClassOf&#32;skos:Concept,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;aec3po:Design&#32;;  &#10; &#32; &#32; &#32; &#32;owl:equivalentClass&#32; &#91;&#32;owl:intersectionOf&#32;(&#32;skos:Concept&#32; &#91;&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:hasValue&#32;aec3po:BuildingUsageNomenclature&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:onProperty&#32;skos:inScheme&#32;]&#32;)&#32;]&#32;.</code></pre>|

***
### MinorFail Outcome number 31

[Jump to summary definition](#summary-MinorFail-31)	|	[Previous MinorFail outcome](#minorfail-outcome-number-30)	|	[Next MinorFail outcome](#minorfail-outcome-number-32)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-src-vocabularies-building-usage|
|----|----|
|Title|Standalone&#32;module&#32;src/vocabularies/building&lowbar;usage.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Module vocabularies/building&lowbar;usage](https://github.com/Accord-Project/aec3po/blob/HEAD/src/vocabularies/building_usage.ttl)|

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
|[Section top](#minorfail-outcome-number-31)|Description|Statement&#32;not&#32;supported|
|[Section top](#minorfail-outcome-number-31)|Pointer|<pre lang="Turtle"><code>&#91;]&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32;owl:hasValue&#32;aec3po:BuildingUsageNomenclature&#32;;  &#10; &#32; &#32; &#32; &#32;owl:onProperty&#32;skos:inScheme&#32;.</code></pre>|

***
### MinorFail Outcome number 32

[Jump to summary definition](#summary-MinorFail-32)	|	[Previous MinorFail outcome](#minorfail-outcome-number-31)	|	[Next MinorFail outcome](#minorfail-outcome-number-33)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-src-vocabularies-building-usage|
|----|----|
|Title|Standalone&#32;module&#32;src/vocabularies/building&lowbar;usage.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Module vocabularies/building&lowbar;usage](https://github.com/Accord-Project/aec3po/blob/HEAD/src/vocabularies/building_usage.ttl)|

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
|[Section top](#minorfail-outcome-number-32)|Description|Statement&#32;not&#32;supported&#32;in&#32;a&#32;Sub&#32;Class&#32;Expression|
|[Section top](#minorfail-outcome-number-32)|Pointer|<pre lang="Turtle"><code>&#91;]&#32;owl:intersectionOf&#32;(&#32;skos:Concept&#32; &#91;&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:hasValue&#32;aec3po:BuildingUsageNomenclature&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:onProperty&#32;skos:inScheme&#32;]&#32;)&#32;.</code></pre>|

***
### MinorFail Outcome number 33

[Jump to summary definition](#summary-MinorFail-33)	|	[Previous MinorFail outcome](#minorfail-outcome-number-32)	|	[Next MinorFail outcome](#minorfail-outcome-number-34)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-src-vocabularies-building-structure|
|----|----|
|Title|Standalone&#32;module&#32;src/vocabularies/building&lowbar;structure.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Module vocabularies/building&lowbar;structure](https://github.com/Accord-Project/aec3po/blob/HEAD/src/vocabularies/building_structure.ttl)|

#### Criterion detail
|Identifier|[domain-and-range-referencing](https://ns.inria.fr/olivaw#domain-and-range-referencing)|
|----|----|
|Title|Domain&#32;and&#32;range&#32;referencing&#32;test|
|Description|A&#32;test&#32;case&#32;from&#32;the&#32;Best&#32;Practices&#32;tests&#32;checking&#32;if&#32;all&#32;the&#32;ranges&#32;and&#32;domains&#32;from&#32;the&#32;test&#32;subject&#32;point&#32;to&#32;terms&#32;that&#32;are&#32;defined&#32;in&#32;the&#32;vocabulary.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-33)|Identifier|`range-out-of-vocabulary`|
|[Section top](#minorfail-outcome-number-33)|Title|Range&#32;out&#32;of&#32;vocabulary|
|[Section top](#minorfail-outcome-number-33)|Description|Some&#32;properties&#32;have&#32;a&#32;range&#32;out&#32;of&#32;the&#32;ontology|
|[Section top](#minorfail-outcome-number-33)|Pointer|<pre lang="Turtle"><code>:forBuildingStructure&#32;a&#32;owl:ObjectProperty&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;for&#32;building&#32;structure&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;The&#32;building&#32;structure&#32;for&#32;which&#32;a&#32;specific&#32;check,&#32;verifier,...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32;:building&lowbar;structure&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:range&#32;&lowbar;:nc74c64fcbab74fb397a9a8e5684aaf37b1,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#91;&#32;rdfs:subClassOf&#32;&lowbar;:nc74c64fcbab74fb397a9a8e5684aaf37b1,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;skos:Concept,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;:BuildingStructure,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;:Design&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:equivalentClass&#32;:BuildingStructure&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:intersectionOf&#32;(&#32;skos:Concept&#32;&lowbar;:nc74c64fcbab74fb397a9a8e5684aaf37b1&#32;)&#32;],  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;skos:Concept,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;:BuildingStructure,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;:Design&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:subPropertyOf&#32;:forDesign&#32;.  &#10;&lowbar;:nc74c64fcbab74fb397a9a8e5684aaf37b1&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32;owl:hasValue&#32;:BuildingStructureNomenclature&#32;;  &#10; &#32; &#32; &#32; &#32;owl:onProperty&#32;skos:inScheme&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-33)|Pointer|<pre lang="Turtle"><code>:hasBuildingStructure&#32;a&#32;owl:FunctionalProperty,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:ObjectProperty&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;has&#32;building&#32;structure&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;The&#32;building&#32;structure&#32;design&#32;of&#32;a&#32;feature&#32;of&#32;interest&#32;or&#32;a&#32;...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32;:building&lowbar;structure&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:range&#32;&lowbar;:n65b176c9e4444d4d821973949c027dafb1,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#91;&#32;rdfs:subClassOf&#32;&lowbar;:n65b176c9e4444d4d821973949c027dafb1,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;skos:Concept,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;:BuildingStructure,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;:Design&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:equivalentClass&#32;:BuildingStructure&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:intersectionOf&#32;(&#32;skos:Concept&#32;&lowbar;:n65b176c9e4444d4d821973949c027dafb1&#32;)&#32;],  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;skos:Concept,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;:BuildingStructure,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;:Design&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:subPropertyOf&#32;:hasDesign&#32;.  &#10;&lowbar;:n65b176c9e4444d4d821973949c027dafb1&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32;owl:hasValue&#32;:BuildingStructureNomenclature&#32;;  &#10; &#32; &#32; &#32; &#32;owl:onProperty&#32;skos:inScheme&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-33)|Pointer|http://www.w3.org/2004/02/skos/core#Concept|

***
### MinorFail Outcome number 34

[Jump to summary definition](#summary-MinorFail-34)	|	[Previous MinorFail outcome](#minorfail-outcome-number-33)	|	[Next MinorFail outcome](#minorfail-outcome-number-35)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-src-vocabularies-building-structure|
|----|----|
|Title|Standalone&#32;module&#32;src/vocabularies/building&lowbar;structure.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Module vocabularies/building&lowbar;structure](https://github.com/Accord-Project/aec3po/blob/HEAD/src/vocabularies/building_structure.ttl)|

#### Criterion detail
|Identifier|[labeled-terms](https://ns.inria.fr/olivaw#labeled-terms)|
|----|----|
|Title|Term&#32;labeling&#32;test|
|Description|A&#32;test&#32;case&#32;from&#32;the&#32;Best&#32;Practices&#32;tests&#32;checking&#32;if&#32;all&#32;the&#32;terms&#32;of&#32;the&#32;subject&#32;have&#32;a&#32;rdfs:label&#32;property&#32;pointing&#32;to&#32;a&#32;literal&#32;in&#32;English|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-34)|Identifier|`not-labeled-term`|
|[Section top](#minorfail-outcome-number-34)|Title|Terms&#32;not&#32;labeled|
|[Section top](#minorfail-outcome-number-34)|Description|The&#32;following&#32;terms&#32;have&#32;no&#32;rdfs:label&#32;to&#32;define&#32;it&#32;in&#32;natural&#32;language|
|[Section top](#minorfail-outcome-number-34)|Pointer|<pre lang="Turtle"><code>:BuildingStructure-steel&#32;a&#32;owl:NamedIndividual,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;skos:Concept,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;:BuildingStructure&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32;:building&lowbar;structure&#32;;  &#10; &#32; &#32; &#32; &#32;skos:definition&#32; &#34;Building&#32;has&#32;steel&#32;structure.&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;skos:inScheme&#32;:BuildingStructureNomenclature&#32;;  &#10; &#32; &#32; &#32; &#32;skos:prefLabel&#32; &#34;steel&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;skos:topConceptOf&#32;:BuildingStructureNomenclature&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-34)|Pointer|<pre lang="Turtle"><code>:BuildingStructure-timber&#32;a&#32;owl:NamedIndividual,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;skos:Concept,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;:BuildingStructure&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32;:building&lowbar;structure&#32;;  &#10; &#32; &#32; &#32; &#32;skos:definition&#32; &#34;Building&#32;has&#32;timber&#32;structure.&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;skos:inScheme&#32;:BuildingStructureNomenclature&#32;;  &#10; &#32; &#32; &#32; &#32;skos:prefLabel&#32; &#34;timber&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;skos:topConceptOf&#32;:BuildingStructureNomenclature&#32;.</code></pre>|

***
### MinorFail Outcome number 35

[Jump to summary definition](#summary-MinorFail-35)	|	[Previous MinorFail outcome](#minorfail-outcome-number-34)	|	[Next MinorFail outcome](#minorfail-outcome-number-36)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-src-vocabularies-building-structure|
|----|----|
|Title|Standalone&#32;module&#32;src/vocabularies/building&lowbar;structure.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Module vocabularies/building&lowbar;structure](https://github.com/Accord-Project/aec3po/blob/HEAD/src/vocabularies/building_structure.ttl)|

#### Criterion detail
|Identifier|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|
|----|----|
|Title|Profile&#32;compatibility&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;check&#32;whether&#32;the&#32;test&#32;subject&#32;is&#32;compatible&#32;with&#32;a&#32;profile&#32;or&#32;not,&#32;and&#32;if&#32;it&#32;is&#32;not,&#32;why.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-35)|Identifier|`owl-el-profile-error`|
|[Section top](#minorfail-outcome-number-35)|Title|OWL&#32;EL&#32;Profile&#32;incompatible|
|[Section top](#minorfail-outcome-number-35)|Description|Statement&#32;not&#32;supported|
|[Section top](#minorfail-outcome-number-35)|Pointer|<pre lang="Turtle"><code>aec3po:hasBuildingStructure&#32;a&#32;owl:FunctionalProperty,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:ObjectProperty&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;has&#32;building&#32;structure&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;The&#32;building&#32;structure&#32;design&#32;of&#32;a&#32;feature&#32;of&#32;interest&#32;or&#32;a&#32;...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32;aec3po:building&lowbar;structure&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:range&#32;aec3po:BuildingStructure&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:subPropertyOf&#32;aec3po:hasDesign&#32;.</code></pre>|

***
### MinorFail Outcome number 36

[Jump to summary definition](#summary-MinorFail-36)	|	[Previous MinorFail outcome](#minorfail-outcome-number-35)	|	[Next MinorFail outcome](#minorfail-outcome-number-37)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-src-vocabularies-building-structure|
|----|----|
|Title|Standalone&#32;module&#32;src/vocabularies/building&lowbar;structure.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Module vocabularies/building&lowbar;structure](https://github.com/Accord-Project/aec3po/blob/HEAD/src/vocabularies/building_structure.ttl)|

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
|[Section top](#minorfail-outcome-number-36)|Description|Class&#32;Expression&#32;not&#32;supported&#32;with&#32;owl:equivalentClass|
|[Section top](#minorfail-outcome-number-36)|Pointer|<pre lang="Turtle"><code>aec3po:BuildingStructure&#32;a&#32;owl:Class&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;building&#32;structure&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;Formally&#32;defined&#32;as&#32;the&#32;set&#32;of&#32;skos:Concept&#32;in&#32;concept&#32;schem...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32;aec3po:building&lowbar;structure&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:subClassOf&#32;skos:Concept,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;aec3po:Design&#32;;  &#10; &#32; &#32; &#32; &#32;owl:equivalentClass&#32; &#91;&#32;owl:intersectionOf&#32;(&#32;skos:Concept&#32; &#91;&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:hasValue&#32;aec3po:BuildingStructureNomenclature&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:onProperty&#32;skos:inScheme&#32;]&#32;)&#32;]&#32;.</code></pre>|

***
### MinorFail Outcome number 37

[Jump to summary definition](#summary-MinorFail-37)	|	[Previous MinorFail outcome](#minorfail-outcome-number-36)	|	[Next MinorFail outcome](#minorfail-outcome-number-38)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-src-vocabularies-building-structure|
|----|----|
|Title|Standalone&#32;module&#32;src/vocabularies/building&lowbar;structure.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Module vocabularies/building&lowbar;structure](https://github.com/Accord-Project/aec3po/blob/HEAD/src/vocabularies/building_structure.ttl)|

#### Criterion detail
|Identifier|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|
|----|----|
|Title|Profile&#32;compatibility&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;check&#32;whether&#32;the&#32;test&#32;subject&#32;is&#32;compatible&#32;with&#32;a&#32;profile&#32;or&#32;not,&#32;and&#32;if&#32;it&#32;is&#32;not,&#32;why.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-37)|Identifier|`owl-ql-profile-error`|
|[Section top](#minorfail-outcome-number-37)|Title|OWL&#32;QL&#32;Profile&#32;incompatible|
|[Section top](#minorfail-outcome-number-37)|Description|Statement&#32;not&#32;supported|
|[Section top](#minorfail-outcome-number-37)|Pointer|<pre lang="Turtle"><code>&#91;]&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32;owl:hasValue&#32;aec3po:BuildingStructureNomenclature&#32;;  &#10; &#32; &#32; &#32; &#32;owl:onProperty&#32;skos:inScheme&#32;.</code></pre>|

***
### MinorFail Outcome number 38

[Jump to summary definition](#summary-MinorFail-38)	|	[Previous MinorFail outcome](#minorfail-outcome-number-37)	|	[Next MinorFail outcome](#minorfail-outcome-number-39)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-src-vocabularies-building-structure|
|----|----|
|Title|Standalone&#32;module&#32;src/vocabularies/building&lowbar;structure.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Module vocabularies/building&lowbar;structure](https://github.com/Accord-Project/aec3po/blob/HEAD/src/vocabularies/building_structure.ttl)|

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
|[Section top](#minorfail-outcome-number-38)|Description|Statement&#32;not&#32;supported&#32;in&#32;a&#32;Sub&#32;Class&#32;Expression|
|[Section top](#minorfail-outcome-number-38)|Pointer|<pre lang="Turtle"><code>&#91;]&#32;owl:intersectionOf&#32;(&#32;skos:Concept&#32; &#91;&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:hasValue&#32;aec3po:BuildingStructureNomenclature&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:onProperty&#32;skos:inScheme&#32;]&#32;)&#32;.</code></pre>|

***
### MinorFail Outcome number 39

[Jump to summary definition](#summary-MinorFail-39)	|	[Previous MinorFail outcome](#minorfail-outcome-number-38)	|	[Next MinorFail outcome](#minorfail-outcome-number-40)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-src-vocabularies-administrative-areas|
|----|----|
|Title|Standalone&#32;module&#32;src/vocabularies/administrative&lowbar;areas.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Module vocabularies/administrative&lowbar;areas](https://github.com/Accord-Project/aec3po/blob/HEAD/src/vocabularies/administrative_areas.ttl)|

#### Criterion detail
|Identifier|[domain-and-range-referencing](https://ns.inria.fr/olivaw#domain-and-range-referencing)|
|----|----|
|Title|Domain&#32;and&#32;range&#32;referencing&#32;test|
|Description|A&#32;test&#32;case&#32;from&#32;the&#32;Best&#32;Practices&#32;tests&#32;checking&#32;if&#32;all&#32;the&#32;ranges&#32;and&#32;domains&#32;from&#32;the&#32;test&#32;subject&#32;point&#32;to&#32;terms&#32;that&#32;are&#32;defined&#32;in&#32;the&#32;vocabulary.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-39)|Identifier|`range-out-of-vocabulary`|
|[Section top](#minorfail-outcome-number-39)|Title|Range&#32;out&#32;of&#32;vocabulary|
|[Section top](#minorfail-outcome-number-39)|Description|Some&#32;properties&#32;have&#32;a&#32;range&#32;out&#32;of&#32;the&#32;ontology|
|[Section top](#minorfail-outcome-number-39)|Pointer|<pre lang="Turtle"><code>:forAdministrativeArea&#32;a&#32;owl:ObjectProperty&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;for&#32;administrative&#32;area&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34; &#34; &#34;The&#32;administrative&#32;area&#32;for&#32;which&#32;something&#32;applies.&#92;r  &#10; &#32; &#32;A&#32;se...&#34; &#34; &#34; &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32;:administrative&lowbar;areas&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:range&#32;&lowbar;:nbf83d28ea4a64284af7b7fdd99740079b1,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#91;&#32;rdfs:subClassOf&#32;&lowbar;:nbf83d28ea4a64284af7b7fdd99740079b1,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#60;http://data.europa.eu/eli/ontology#AdministrativeArea>,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;skos:Concept,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;:AdministrativeArea&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:equivalentClass&#32; &#60;http://data.europa.eu/eli/ontology#AdministrativeArea>,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;:AdministrativeArea&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:intersectionOf&#32;(&#32;skos:Concept&#32;&lowbar;:nbf83d28ea4a64284af7b7fdd99740079b1&#32;)&#32;],  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#60;http://data.europa.eu/eli/ontology#AdministrativeArea>,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;skos:Concept,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;:AdministrativeArea&#32;.  &#10;&lowbar;:nbf83d28ea4a64284af7b7fdd99740079b1&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32;owl:hasValue&#32;:AdministrativeAreaNomenclature&#32;;  &#10; &#32; &#32; &#32; &#32;owl:onProperty&#32;skos:inScheme&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-39)|Pointer|<pre lang="Turtle"><code>:forAdministrativeArea&#32;a&#32;owl:ObjectProperty&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;for&#32;administrative&#32;area&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34; &#34; &#34;The&#32;administrative&#32;area&#32;for&#32;which&#32;something&#32;applies.&#92;r  &#10; &#32; &#32;A&#32;se...&#34; &#34; &#34; &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32;:administrative&lowbar;areas&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:range&#32;&lowbar;:na88a442ff004448a905bf679039baf1cb1,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#91;&#32;rdfs:subClassOf&#32;&lowbar;:na88a442ff004448a905bf679039baf1cb1,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#60;http://data.europa.eu/eli/ontology#AdministrativeArea>,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;skos:Concept,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;:AdministrativeArea&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:equivalentClass&#32; &#60;http://data.europa.eu/eli/ontology#AdministrativeArea>,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;:AdministrativeArea&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:intersectionOf&#32;(&#32;skos:Concept&#32;&lowbar;:na88a442ff004448a905bf679039baf1cb1&#32;)&#32;],  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#60;http://data.europa.eu/eli/ontology#AdministrativeArea>,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;skos:Concept,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;:AdministrativeArea&#32;.  &#10;&lowbar;:na88a442ff004448a905bf679039baf1cb1&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32;owl:hasValue&#32;:AdministrativeAreaNomenclature&#32;;  &#10; &#32; &#32; &#32; &#32;owl:onProperty&#32;skos:inScheme&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-39)|Pointer|<pre lang="Turtle"><code>:AdministrativeArea&#32;rdfs:subClassOf&#32;&lowbar;:nf8fe30113dce48ff87056a71905a4630b1,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;&lowbar;:nf8fe30113dce48ff87056a71905a4630b2,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;skos:Concept,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;aec3po:AdministrativeArea&#32;;  &#10; &#32; &#32; &#32; &#32;owl:equivalentClass&#32;&lowbar;:nf8fe30113dce48ff87056a71905a4630b2,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;aec3po:AdministrativeArea&#32;.  &#10;&lowbar;:nf8fe30113dce48ff87056a71905a4630b3&#32;rdf:first&#32;skos:Concept&#32;;  &#10; &#32; &#32; &#32; &#32;rdf:rest&#32;(&#32;&lowbar;:nf8fe30113dce48ff87056a71905a4630b1&#32;)&#32;.  &#10;&lowbar;:nf8fe30113dce48ff87056a71905a4630b2&#32;rdfs:subClassOf&#32;&lowbar;:nf8fe30113dce48ff87056a71905a4630b1,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;:AdministrativeArea,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;skos:Concept,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;aec3po:AdministrativeArea&#32;;  &#10; &#32; &#32; &#32; &#32;owl:equivalentClass&#32;:AdministrativeArea,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;aec3po:AdministrativeArea&#32;;  &#10; &#32; &#32; &#32; &#32;owl:intersectionOf&#32;&lowbar;:nf8fe30113dce48ff87056a71905a4630b3&#32;.  &#10;&lowbar;:nf8fe30113dce48ff87056a71905a4630b1&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32;owl:hasValue&#32;aec3po:AdministrativeAreaNomenclature&#32;;  &#10; &#32; &#32; &#32; &#32;owl:onProperty&#32;skos:inScheme&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-39)|Pointer|http://www.w3.org/2004/02/skos/core#Concept|

***
### MinorFail Outcome number 40

[Jump to summary definition](#summary-MinorFail-40)	|	[Previous MinorFail outcome](#minorfail-outcome-number-39)	|	[Next MinorFail outcome](#minorfail-outcome-number-41)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-src-vocabularies-administrative-areas|
|----|----|
|Title|Standalone&#32;module&#32;src/vocabularies/administrative&lowbar;areas.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Module vocabularies/administrative&lowbar;areas](https://github.com/Accord-Project/aec3po/blob/HEAD/src/vocabularies/administrative_areas.ttl)|

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
|[Section top](#minorfail-outcome-number-40)|Pointer|<pre lang="Turtle"><code>:England&#32;a&#32;owl:NamedIndividual,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;skos:Concept,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;:AdministrativeArea&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32;:administrative&lowbar;areas&#32;;  &#10; &#32; &#32; &#32; &#32;skos:definition&#32; &#34;England&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;skos:inScheme&#32;:AdministrativeAreaNomenclature&#32;;  &#10; &#32; &#32; &#32; &#32;skos:prefLabel&#32; &#34;England&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;skos:topConceptOf&#32;:AdministrativeAreaNomenclature&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-40)|Pointer|<pre lang="Turtle"><code>:Estonia&#32;a&#32;owl:NamedIndividual,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;skos:Concept,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;:AdministrativeArea&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32;:administrative&lowbar;areas&#32;;  &#10; &#32; &#32; &#32; &#32;skos:definition&#32; &#34;Estonia&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;skos:inScheme&#32;:AdministrativeAreaNomenclature&#32;;  &#10; &#32; &#32; &#32; &#32;skos:prefLabel&#32; &#34;Estonia&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;skos:topConceptOf&#32;:AdministrativeAreaNomenclature&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-40)|Pointer|<pre lang="Turtle"><code>:Finland&#32;a&#32;owl:NamedIndividual,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;skos:Concept,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;:AdministrativeArea&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32;:administrative&lowbar;areas&#32;;  &#10; &#32; &#32; &#32; &#32;skos:definition&#32; &#34;Finland&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;skos:inScheme&#32;:AdministrativeAreaNomenclature&#32;;  &#10; &#32; &#32; &#32; &#32;skos:prefLabel&#32; &#34;Finland&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;skos:topConceptOf&#32;:AdministrativeAreaNomenclature&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-40)|Pointer|<pre lang="Turtle"><code>:France&#32;a&#32;owl:NamedIndividual,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;skos:Concept,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;:AdministrativeArea&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32;:administrative&lowbar;areas&#32;;  &#10; &#32; &#32; &#32; &#32;skos:definition&#32; &#34;France&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;skos:inScheme&#32;:AdministrativeAreaNomenclature&#32;;  &#10; &#32; &#32; &#32; &#32;skos:prefLabel&#32; &#34;France&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;skos:topConceptOf&#32;:AdministrativeAreaNomenclature&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-40)|Pointer|<pre lang="Turtle"><code>:Germany&#32;a&#32;owl:NamedIndividual,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;skos:Concept,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;:AdministrativeArea&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32;:administrative&lowbar;areas&#32;;  &#10; &#32; &#32; &#32; &#32;skos:definition&#32; &#34;Germany&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;skos:inScheme&#32;:AdministrativeAreaNomenclature&#32;;  &#10; &#32; &#32; &#32; &#32;skos:prefLabel&#32; &#34;Germany&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;skos:topConceptOf&#32;:AdministrativeAreaNomenclature&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-40)|Pointer|<pre lang="Turtle"><code>:Italy&#32;a&#32;owl:NamedIndividual,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;skos:Concept,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;:AdministrativeArea&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32;:administrative&lowbar;areas&#32;;  &#10; &#32; &#32; &#32; &#32;skos:definition&#32; &#34;Italy&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;skos:inScheme&#32;:AdministrativeAreaNomenclature&#32;;  &#10; &#32; &#32; &#32; &#32;skos:prefLabel&#32; &#34;Italy&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;skos:topConceptOf&#32;:AdministrativeAreaNomenclature&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-40)|Pointer|<pre lang="Turtle"><code>:Spain&#32;a&#32;owl:NamedIndividual,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;skos:Concept,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;:AdministrativeArea&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32;:administrative&lowbar;areas&#32;;  &#10; &#32; &#32; &#32; &#32;skos:definition&#32; &#34;Spain&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;skos:inScheme&#32;:AdministrativeAreaNomenclature&#32;;  &#10; &#32; &#32; &#32; &#32;skos:prefLabel&#32; &#34;Spain&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;skos:topConceptOf&#32;:AdministrativeAreaNomenclature&#32;.</code></pre>|

***
### MinorFail Outcome number 41

[Jump to summary definition](#summary-MinorFail-41)	|	[Previous MinorFail outcome](#minorfail-outcome-number-40)	|	[Next MinorFail outcome](#minorfail-outcome-number-42)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-src-vocabularies-administrative-areas|
|----|----|
|Title|Standalone&#32;module&#32;src/vocabularies/administrative&lowbar;areas.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Module vocabularies/administrative&lowbar;areas](https://github.com/Accord-Project/aec3po/blob/HEAD/src/vocabularies/administrative_areas.ttl)|

#### Criterion detail
|Identifier|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|
|----|----|
|Title|Profile&#32;compatibility&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;check&#32;whether&#32;the&#32;test&#32;subject&#32;is&#32;compatible&#32;with&#32;a&#32;profile&#32;or&#32;not,&#32;and&#32;if&#32;it&#32;is&#32;not,&#32;why.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-41)|Identifier|`owl-ql-profile-error`|
|[Section top](#minorfail-outcome-number-41)|Title|OWL&#32;QL&#32;Profile&#32;incompatible|
|[Section top](#minorfail-outcome-number-41)|Description|Class&#32;Expression&#32;not&#32;supported&#32;with&#32;owl:equivalentClass|
|[Section top](#minorfail-outcome-number-41)|Pointer|<pre lang="Turtle"><code>aec3po:AdministrativeArea&#32;a&#32;owl:Class&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;Administrative&#32;Area&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;Formally&#32;defined&#32;as&#32;the&#32;set&#32;of&#32;skos:Concept&#32;either&#32;in&#32;concep...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32;aec3po:administrative&lowbar;areas&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:seeAlso&#32; &#60;https://op.europa.eu/en/web/eu-vocabularies/concept-scheme/-/resource?uri=http://publications.europa.eu/resource/authority/atu> &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:subClassOf&#32;skos:Concept&#32;;  &#10; &#32; &#32; &#32; &#32;owl:equivalentClass&#32; &#91;&#32;owl:intersectionOf&#32;(&#32;skos:Concept&#32; &#91;&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:hasValue&#32;aec3po:AdministrativeAreaNomenclature&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:onProperty&#32;skos:inScheme&#32;]&#32;)&#32;],  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#60;http://data.europa.eu/eli/ontology#AdministrativeArea> &#32;.</code></pre>|

***
### MinorFail Outcome number 42

[Jump to summary definition](#summary-MinorFail-42)	|	[Previous MinorFail outcome](#minorfail-outcome-number-41)	|	[Next MinorFail outcome](#minorfail-outcome-number-43)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-src-vocabularies-administrative-areas|
|----|----|
|Title|Standalone&#32;module&#32;src/vocabularies/administrative&lowbar;areas.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Module vocabularies/administrative&lowbar;areas](https://github.com/Accord-Project/aec3po/blob/HEAD/src/vocabularies/administrative_areas.ttl)|

#### Criterion detail
|Identifier|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|
|----|----|
|Title|Profile&#32;compatibility&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;check&#32;whether&#32;the&#32;test&#32;subject&#32;is&#32;compatible&#32;with&#32;a&#32;profile&#32;or&#32;not,&#32;and&#32;if&#32;it&#32;is&#32;not,&#32;why.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-42)|Identifier|`owl-ql-profile-error`|
|[Section top](#minorfail-outcome-number-42)|Title|OWL&#32;QL&#32;Profile&#32;incompatible|
|[Section top](#minorfail-outcome-number-42)|Description|Statement&#32;not&#32;supported|
|[Section top](#minorfail-outcome-number-42)|Pointer|<pre lang="Turtle"><code>&#91;]&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32;owl:hasValue&#32;aec3po:AdministrativeAreaNomenclature&#32;;  &#10; &#32; &#32; &#32; &#32;owl:onProperty&#32;skos:inScheme&#32;.</code></pre>|

***
### MinorFail Outcome number 43

[Jump to summary definition](#summary-MinorFail-43)	|	[Previous MinorFail outcome](#minorfail-outcome-number-42)	|	[Next MinorFail outcome](#minorfail-outcome-number-44)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-src-vocabularies-administrative-areas|
|----|----|
|Title|Standalone&#32;module&#32;src/vocabularies/administrative&lowbar;areas.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Module vocabularies/administrative&lowbar;areas](https://github.com/Accord-Project/aec3po/blob/HEAD/src/vocabularies/administrative_areas.ttl)|

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
|[Section top](#minorfail-outcome-number-43)|Description|Statement&#32;not&#32;supported&#32;in&#32;a&#32;Sub&#32;Class&#32;Expression|
|[Section top](#minorfail-outcome-number-43)|Pointer|<pre lang="Turtle"><code>&#91;]&#32;owl:intersectionOf&#32;(&#32;skos:Concept&#32; &#91;&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:hasValue&#32;aec3po:AdministrativeAreaNomenclature&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:onProperty&#32;skos:inScheme&#32;]&#32;)&#32;.</code></pre>|

***
### MinorFail Outcome number 44

[Jump to summary definition](#summary-MinorFail-44)	|	[Previous MinorFail outcome](#minorfail-outcome-number-43)	|	[Next MinorFail outcome](#minorfail-outcome-number-45)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-src-table|
|----|----|
|Title|Standalone&#32;module&#32;src/table.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Module table](https://github.com/Accord-Project/aec3po/blob/HEAD/src/table.ttl)|

#### Criterion detail
|Identifier|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|
|----|----|
|Title|Profile&#32;compatibility&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;check&#32;whether&#32;the&#32;test&#32;subject&#32;is&#32;compatible&#32;with&#32;a&#32;profile&#32;or&#32;not,&#32;and&#32;if&#32;it&#32;is&#32;not,&#32;why.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-44)|Identifier|`owl-el-profile-error`|
|[Section top](#minorfail-outcome-number-44)|Title|OWL&#32;EL&#32;Profile&#32;incompatible|
|[Section top](#minorfail-outcome-number-44)|Description|Class&#32;Expression&#32;not&#32;supported&#32;as&#32;object&#32;of&#32;rdfs:domain&#32;or&#32;rdfs:range|
|[Section top](#minorfail-outcome-number-44)|Pointer|<pre lang="Turtle"><code>aec3po:caption&#32;a&#32;owl:DatatypeProperty&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;caption&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;The&#32;caption&#32;of&#32;a&#32;table,&#32;image,&#32;etc.&#32; &#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:domain&#32; &#91;&#32;a&#32;owl:Class&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:unionOf&#32;(&#32;aec3po:Table&#32;aec3po:Image&#32;)&#32;]&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32;aec3po:table&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-44)|Pointer|<pre lang="Turtle"><code>aec3po:contains&#32;a&#32;owl:ObjectProperty&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;Contains&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;A&#32;container&#32;contains&#32;a&#32;table&#32;and&#32;its&#32;caption.&#32;A&#32;table&#32;contai...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:domain&#32; &#91;&#32;a&#32;owl:Class&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:unionOf&#32;(&#32;aec3po:Table&#32;aec3po:Image&#32;aec3po:Row&#32;aec3po:Column&#32;)&#32;]&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32;aec3po:table&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-44)|Pointer|<pre lang="Turtle"><code>aec3po:isContainedIn&#32;a&#32;owl:ObjectProperty&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;is&#32;contained&#32;by&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;A&#32;table&#32;contains&#32;row,&#32;columns&#32;and&#32;other&#32;elements.&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32;aec3po:table&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:range&#32; &#91;&#32;a&#32;owl:Class&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:unionOf&#32;(&#32;aec3po:Table&#32;aec3po:Image&#32;aec3po:Row&#32;aec3po:Column&#32;aec3po:Cell&#32;)&#32;]&#32;.</code></pre>|

***
### MinorFail Outcome number 45

[Jump to summary definition](#summary-MinorFail-45)	|	[Previous MinorFail outcome](#minorfail-outcome-number-44)	|	[Next MinorFail outcome](#minorfail-outcome-number-46)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-src-table|
|----|----|
|Title|Standalone&#32;module&#32;src/table.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Module table](https://github.com/Accord-Project/aec3po/blob/HEAD/src/table.ttl)|

#### Criterion detail
|Identifier|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|
|----|----|
|Title|Profile&#32;compatibility&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;check&#32;whether&#32;the&#32;test&#32;subject&#32;is&#32;compatible&#32;with&#32;a&#32;profile&#32;or&#32;not,&#32;and&#32;if&#32;it&#32;is&#32;not,&#32;why.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-45)|Identifier|`owl-el-profile-error`|
|[Section top](#minorfail-outcome-number-45)|Title|OWL&#32;EL&#32;Profile&#32;incompatible|
|[Section top](#minorfail-outcome-number-45)|Description|Statement&#32;not&#32;supported&#32;in&#32;a&#32;Class&#32;Expression|
|[Section top](#minorfail-outcome-number-45)|Pointer|<pre lang="Turtle"><code>&#91;]&#32;a&#32;owl:Class&#32;;  &#10; &#32; &#32;&#32; &#32;owl:unionOf&#32;(&#32;aec3po:Table&#32;aec3po:Image&#32;aec3po:Row&#32;aec3po:Column&#32;)&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-45)|Pointer|<pre lang="Turtle"><code>&#91;]&#32;a&#32;owl:Class&#32;;  &#10; &#32; &#32;&#32; &#32;owl:unionOf&#32;(&#32;aec3po:Table&#32;aec3po:Image&#32;aec3po:Row&#32;aec3po:Column&#32;aec3po:Cell&#32;)&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-45)|Pointer|<pre lang="Turtle"><code>&#91;]&#32;a&#32;owl:Class&#32;;  &#10; &#32; &#32;&#32; &#32;owl:unionOf&#32;(&#32;aec3po:Table&#32;aec3po:Image&#32;)&#32;.</code></pre>|

***
### MinorFail Outcome number 46

[Jump to summary definition](#summary-MinorFail-46)	|	[Previous MinorFail outcome](#minorfail-outcome-number-45)	|	[Next MinorFail outcome](#minorfail-outcome-number-47)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-src-table|
|----|----|
|Title|Standalone&#32;module&#32;src/table.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Module table](https://github.com/Accord-Project/aec3po/blob/HEAD/src/table.ttl)|

#### Criterion detail
|Identifier|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|
|----|----|
|Title|Profile&#32;compatibility&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;check&#32;whether&#32;the&#32;test&#32;subject&#32;is&#32;compatible&#32;with&#32;a&#32;profile&#32;or&#32;not,&#32;and&#32;if&#32;it&#32;is&#32;not,&#32;why.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-46)|Identifier|`owl-ql-profile-error`|
|[Section top](#minorfail-outcome-number-46)|Title|OWL&#32;QL&#32;Profile&#32;incompatible|
|[Section top](#minorfail-outcome-number-46)|Description|Class&#32;Expression&#32;not&#32;supported&#32;as&#32;object&#32;of&#32;rdfs:domain&#32;or&#32;rdfs:range|
|[Section top](#minorfail-outcome-number-46)|Pointer|<pre lang="Turtle"><code>aec3po:caption&#32;a&#32;owl:DatatypeProperty&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;caption&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;The&#32;caption&#32;of&#32;a&#32;table,&#32;image,&#32;etc.&#32; &#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:domain&#32; &#91;&#32;a&#32;owl:Class&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:unionOf&#32;(&#32;aec3po:Table&#32;aec3po:Image&#32;)&#32;]&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32;aec3po:table&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-46)|Pointer|<pre lang="Turtle"><code>aec3po:contains&#32;a&#32;owl:ObjectProperty&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;Contains&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;A&#32;container&#32;contains&#32;a&#32;table&#32;and&#32;its&#32;caption.&#32;A&#32;table&#32;contai...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:domain&#32; &#91;&#32;a&#32;owl:Class&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:unionOf&#32;(&#32;aec3po:Table&#32;aec3po:Image&#32;aec3po:Row&#32;aec3po:Column&#32;)&#32;]&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32;aec3po:table&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-46)|Pointer|<pre lang="Turtle"><code>aec3po:isContainedIn&#32;a&#32;owl:ObjectProperty&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;is&#32;contained&#32;by&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;A&#32;table&#32;contains&#32;row,&#32;columns&#32;and&#32;other&#32;elements.&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32;aec3po:table&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:range&#32; &#91;&#32;a&#32;owl:Class&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:unionOf&#32;(&#32;aec3po:Table&#32;aec3po:Image&#32;aec3po:Row&#32;aec3po:Column&#32;aec3po:Cell&#32;)&#32;]&#32;.</code></pre>|

***
### MinorFail Outcome number 47

[Jump to summary definition](#summary-MinorFail-47)	|	[Previous MinorFail outcome](#minorfail-outcome-number-46)	|	[Next MinorFail outcome](#minorfail-outcome-number-48)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-src-table|
|----|----|
|Title|Standalone&#32;module&#32;src/table.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Module table](https://github.com/Accord-Project/aec3po/blob/HEAD/src/table.ttl)|

#### Criterion detail
|Identifier|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|
|----|----|
|Title|Profile&#32;compatibility&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;check&#32;whether&#32;the&#32;test&#32;subject&#32;is&#32;compatible&#32;with&#32;a&#32;profile&#32;or&#32;not,&#32;and&#32;if&#32;it&#32;is&#32;not,&#32;why.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-47)|Identifier|`owl-ql-profile-error`|
|[Section top](#minorfail-outcome-number-47)|Title|OWL&#32;QL&#32;Profile&#32;incompatible|
|[Section top](#minorfail-outcome-number-47)|Description|Statement&#32;not&#32;supported&#32;in&#32;a&#32;Super&#32;Class&#32;Expression|
|[Section top](#minorfail-outcome-number-47)|Pointer|<pre lang="Turtle"><code>&#91;]&#32;a&#32;owl:Class&#32;;  &#10; &#32; &#32;&#32; &#32;owl:unionOf&#32;(&#32;aec3po:Table&#32;aec3po:Image&#32;aec3po:Row&#32;aec3po:Column&#32;)&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-47)|Pointer|<pre lang="Turtle"><code>&#91;]&#32;a&#32;owl:Class&#32;;  &#10; &#32; &#32;&#32; &#32;owl:unionOf&#32;(&#32;aec3po:Table&#32;aec3po:Image&#32;aec3po:Row&#32;aec3po:Column&#32;aec3po:Cell&#32;)&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-47)|Pointer|<pre lang="Turtle"><code>&#91;]&#32;a&#32;owl:Class&#32;;  &#10; &#32; &#32;&#32; &#32;owl:unionOf&#32;(&#32;aec3po:Table&#32;aec3po:Image&#32;)&#32;.</code></pre>|

***
### MinorFail Outcome number 48

[Jump to summary definition](#summary-MinorFail-48)	|	[Previous MinorFail outcome](#minorfail-outcome-number-47)	|	[Next MinorFail outcome](#minorfail-outcome-number-49)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-src-table|
|----|----|
|Title|Standalone&#32;module&#32;src/table.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Module table](https://github.com/Accord-Project/aec3po/blob/HEAD/src/table.ttl)|

#### Criterion detail
|Identifier|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|
|----|----|
|Title|Profile&#32;compatibility&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;check&#32;whether&#32;the&#32;test&#32;subject&#32;is&#32;compatible&#32;with&#32;a&#32;profile&#32;or&#32;not,&#32;and&#32;if&#32;it&#32;is&#32;not,&#32;why.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-48)|Identifier|`owl-rl-profile-error`|
|[Section top](#minorfail-outcome-number-48)|Title|OWL&#32;RL&#32;Profile&#32;incompatible|
|[Section top](#minorfail-outcome-number-48)|Description|Class&#32;Expression&#32;not&#32;supported&#32;as&#32;object&#32;of&#32;rdfs:domain&#32;or&#32;rdfs:range|
|[Section top](#minorfail-outcome-number-48)|Pointer|<pre lang="Turtle"><code>aec3po:caption&#32;a&#32;owl:DatatypeProperty&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;caption&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;The&#32;caption&#32;of&#32;a&#32;table,&#32;image,&#32;etc.&#32; &#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:domain&#32; &#91;&#32;a&#32;owl:Class&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:unionOf&#32;(&#32;aec3po:Table&#32;aec3po:Image&#32;)&#32;]&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32;aec3po:table&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-48)|Pointer|<pre lang="Turtle"><code>aec3po:contains&#32;a&#32;owl:ObjectProperty&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;Contains&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;A&#32;container&#32;contains&#32;a&#32;table&#32;and&#32;its&#32;caption.&#32;A&#32;table&#32;contai...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:domain&#32; &#91;&#32;a&#32;owl:Class&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:unionOf&#32;(&#32;aec3po:Table&#32;aec3po:Image&#32;aec3po:Row&#32;aec3po:Column&#32;)&#32;]&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32;aec3po:table&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-48)|Pointer|<pre lang="Turtle"><code>aec3po:isContainedIn&#32;a&#32;owl:ObjectProperty&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;is&#32;contained&#32;by&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;A&#32;table&#32;contains&#32;row,&#32;columns&#32;and&#32;other&#32;elements.&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32;aec3po:table&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:range&#32; &#91;&#32;a&#32;owl:Class&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:unionOf&#32;(&#32;aec3po:Table&#32;aec3po:Image&#32;aec3po:Row&#32;aec3po:Column&#32;aec3po:Cell&#32;)&#32;]&#32;.</code></pre>|

***
### MinorFail Outcome number 49

[Jump to summary definition](#summary-MinorFail-49)	|	[Previous MinorFail outcome](#minorfail-outcome-number-48)	|	[Next MinorFail outcome](#minorfail-outcome-number-50)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-src-table|
|----|----|
|Title|Standalone&#32;module&#32;src/table.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Module table](https://github.com/Accord-Project/aec3po/blob/HEAD/src/table.ttl)|

#### Criterion detail
|Identifier|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|
|----|----|
|Title|Profile&#32;compatibility&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;check&#32;whether&#32;the&#32;test&#32;subject&#32;is&#32;compatible&#32;with&#32;a&#32;profile&#32;or&#32;not,&#32;and&#32;if&#32;it&#32;is&#32;not,&#32;why.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-49)|Identifier|`owl-rl-profile-error`|
|[Section top](#minorfail-outcome-number-49)|Title|OWL&#32;RL&#32;Profile&#32;incompatible|
|[Section top](#minorfail-outcome-number-49)|Description|Statement&#32;not&#32;supported&#32;in&#32;a&#32;Super&#32;Class&#32;Expression|
|[Section top](#minorfail-outcome-number-49)|Pointer|<pre lang="Turtle"><code>&#91;]&#32;a&#32;owl:Class&#32;;  &#10; &#32; &#32;&#32; &#32;owl:unionOf&#32;(&#32;aec3po:Table&#32;aec3po:Image&#32;aec3po:Row&#32;aec3po:Column&#32;)&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-49)|Pointer|<pre lang="Turtle"><code>&#91;]&#32;a&#32;owl:Class&#32;;  &#10; &#32; &#32;&#32; &#32;owl:unionOf&#32;(&#32;aec3po:Table&#32;aec3po:Image&#32;aec3po:Row&#32;aec3po:Column&#32;aec3po:Cell&#32;)&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-49)|Pointer|<pre lang="Turtle"><code>&#91;]&#32;a&#32;owl:Class&#32;;  &#10; &#32; &#32;&#32; &#32;owl:unionOf&#32;(&#32;aec3po:Table&#32;aec3po:Image&#32;)&#32;.</code></pre>|

***
### MinorFail Outcome number 50

[Jump to summary definition](#summary-MinorFail-50)	|	[Previous MinorFail outcome](#minorfail-outcome-number-49)	|	[Next MinorFail outcome](#minorfail-outcome-number-51)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-src-statement|
|----|----|
|Title|Standalone&#32;module&#32;src/statement.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Module statement](https://github.com/Accord-Project/aec3po/blob/HEAD/src/statement.ttl)|

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
|[Section top](#minorfail-outcome-number-50)|Description|Class&#32;Expression&#32;not&#32;supported&#32;with&#32;rdfs:subClassOf|
|[Section top](#minorfail-outcome-number-50)|Pointer|<pre lang="Turtle"><code>aec3po:AndCheckStatement&#32;a&#32;owl:Class&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;And&#32;Check&#32;Statement&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;Check&#32;verified&#32;if&#32;and&#32;only&#32;if&#32;all&#32;of&#32;its&#32;sub-checks&#32;are&#32;veri...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32;aec3po:statement&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:subClassOf&#32; &#91;&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:onProperty&#32;aec3po:hasSubdivision&#32;],  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;aec3po:ChecklistStatement&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-50)|Pointer|<pre lang="Turtle"><code>aec3po:NotCheckStatement&#32;a&#32;owl:Class&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;Not&#32;Check&#32;Statement&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;Check&#32;verified&#32;if&#32;and&#32;only&#32;if&#32;the&#32;sub-check&#32;is&#32;not&#32;verified.&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32;aec3po:statement&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:subClassOf&#32; &#91;&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:onProperty&#32;aec3po:hasSubdivision&#32;]&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-50)|Pointer|<pre lang="Turtle"><code>aec3po:OrCheckStatement&#32;a&#32;owl:Class&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;Or&#32;Check&#32;Statement&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;Check&#32;verified&#32;if&#32;and&#32;only&#32;if&#32;at&#32;least&#32;one&#32;of&#32;its&#32;sub-checks...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32;aec3po:statement&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:subClassOf&#32; &#91;&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:onProperty&#32;aec3po:hasSubdivision&#32;],  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;aec3po:ChecklistStatement&#32;.</code></pre>|

***
### MinorFail Outcome number 51

[Jump to summary definition](#summary-MinorFail-51)	|	[Previous MinorFail outcome](#minorfail-outcome-number-50)	|	[Next MinorFail outcome](#minorfail-outcome-number-52)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-src-statement|
|----|----|
|Title|Standalone&#32;module&#32;src/statement.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Module statement](https://github.com/Accord-Project/aec3po/blob/HEAD/src/statement.ttl)|

#### Criterion detail
|Identifier|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|
|----|----|
|Title|Profile&#32;compatibility&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;check&#32;whether&#32;the&#32;test&#32;subject&#32;is&#32;compatible&#32;with&#32;a&#32;profile&#32;or&#32;not,&#32;and&#32;if&#32;it&#32;is&#32;not,&#32;why.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-51)|Identifier|`owl-el-profile-error`|
|[Section top](#minorfail-outcome-number-51)|Title|OWL&#32;EL&#32;Profile&#32;incompatible|
|[Section top](#minorfail-outcome-number-51)|Description|Statement&#32;not&#32;supported  &#10;Statement&#32;not&#32;supported&#32;in&#32;a&#32;Class&#32;Expression|
|[Section top](#minorfail-outcome-number-51)|Pointer|<pre lang="Turtle"><code>&#91;]&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32;&#32; &#32;owl:onProperty&#32;aec3po:hasSubdivision&#32;.</code></pre>|

***
### MinorFail Outcome number 52

[Jump to summary definition](#summary-MinorFail-52)	|	[Previous MinorFail outcome](#minorfail-outcome-number-51)	|	[Next MinorFail outcome](#minorfail-outcome-number-53)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-src-statement|
|----|----|
|Title|Standalone&#32;module&#32;src/statement.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Module statement](https://github.com/Accord-Project/aec3po/blob/HEAD/src/statement.ttl)|

#### Criterion detail
|Identifier|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|
|----|----|
|Title|Profile&#32;compatibility&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;check&#32;whether&#32;the&#32;test&#32;subject&#32;is&#32;compatible&#32;with&#32;a&#32;profile&#32;or&#32;not,&#32;and&#32;if&#32;it&#32;is&#32;not,&#32;why.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-52)|Identifier|`owl-el-profile-error`|
|[Section top](#minorfail-outcome-number-52)|Title|OWL&#32;EL&#32;Profile&#32;incompatible|
|[Section top](#minorfail-outcome-number-52)|Description|Statement&#32;not&#32;supported&#32;in&#32;a&#32;Class&#32;Expression|
|[Section top](#minorfail-outcome-number-52)|Pointer|<pre lang="Turtle"><code>&#91;]&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32;&#32; &#32;owl:onProperty&#32;aec3po:hasSubdivision&#32;.</code></pre>|

***
### MinorFail Outcome number 53

[Jump to summary definition](#summary-MinorFail-53)	|	[Previous MinorFail outcome](#minorfail-outcome-number-52)	|	[Next MinorFail outcome](#minorfail-outcome-number-54)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-src-statement|
|----|----|
|Title|Standalone&#32;module&#32;src/statement.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Module statement](https://github.com/Accord-Project/aec3po/blob/HEAD/src/statement.ttl)|

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
|[Section top](#minorfail-outcome-number-53)|Description|Class&#32;Expression&#32;not&#32;supported&#32;with&#32;rdfs:subClassOf|
|[Section top](#minorfail-outcome-number-53)|Pointer|<pre lang="Turtle"><code>aec3po:AndCheckStatement&#32;a&#32;owl:Class&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;And&#32;Check&#32;Statement&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;Check&#32;verified&#32;if&#32;and&#32;only&#32;if&#32;all&#32;of&#32;its&#32;sub-checks&#32;are&#32;veri...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32;aec3po:statement&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:subClassOf&#32; &#91;&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:onProperty&#32;aec3po:hasSubdivision&#32;],  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;aec3po:ChecklistStatement&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-53)|Pointer|<pre lang="Turtle"><code>aec3po:NotCheckStatement&#32;a&#32;owl:Class&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;Not&#32;Check&#32;Statement&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;Check&#32;verified&#32;if&#32;and&#32;only&#32;if&#32;the&#32;sub-check&#32;is&#32;not&#32;verified.&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32;aec3po:statement&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:subClassOf&#32; &#91;&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:onProperty&#32;aec3po:hasSubdivision&#32;]&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-53)|Pointer|<pre lang="Turtle"><code>aec3po:OrCheckStatement&#32;a&#32;owl:Class&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;Or&#32;Check&#32;Statement&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;Check&#32;verified&#32;if&#32;and&#32;only&#32;if&#32;at&#32;least&#32;one&#32;of&#32;its&#32;sub-checks...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32;aec3po:statement&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:subClassOf&#32; &#91;&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:onProperty&#32;aec3po:hasSubdivision&#32;],  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;aec3po:ChecklistStatement&#32;.</code></pre>|

***
### MinorFail Outcome number 54

[Jump to summary definition](#summary-MinorFail-54)	|	[Previous MinorFail outcome](#minorfail-outcome-number-53)	|	[Next MinorFail outcome](#minorfail-outcome-number-55)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-src-statement|
|----|----|
|Title|Standalone&#32;module&#32;src/statement.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Module statement](https://github.com/Accord-Project/aec3po/blob/HEAD/src/statement.ttl)|

#### Criterion detail
|Identifier|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|
|----|----|
|Title|Profile&#32;compatibility&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;check&#32;whether&#32;the&#32;test&#32;subject&#32;is&#32;compatible&#32;with&#32;a&#32;profile&#32;or&#32;not,&#32;and&#32;if&#32;it&#32;is&#32;not,&#32;why.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-54)|Identifier|`owl-ql-profile-error`|
|[Section top](#minorfail-outcome-number-54)|Title|OWL&#32;QL&#32;Profile&#32;incompatible|
|[Section top](#minorfail-outcome-number-54)|Description|Statement&#32;not&#32;supported  &#10;Statement&#32;not&#32;supported&#32;in&#32;a&#32;Super&#32;Class&#32;Expression|
|[Section top](#minorfail-outcome-number-54)|Pointer|<pre lang="Turtle"><code>&#91;]&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32;&#32; &#32;owl:onProperty&#32;aec3po:hasSubdivision&#32;.</code></pre>|

***
### MinorFail Outcome number 55

[Jump to summary definition](#summary-MinorFail-55)	|	[Previous MinorFail outcome](#minorfail-outcome-number-54)	|	[Next MinorFail outcome](#minorfail-outcome-number-56)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-src-statement|
|----|----|
|Title|Standalone&#32;module&#32;src/statement.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Module statement](https://github.com/Accord-Project/aec3po/blob/HEAD/src/statement.ttl)|

#### Criterion detail
|Identifier|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|
|----|----|
|Title|Profile&#32;compatibility&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;check&#32;whether&#32;the&#32;test&#32;subject&#32;is&#32;compatible&#32;with&#32;a&#32;profile&#32;or&#32;not,&#32;and&#32;if&#32;it&#32;is&#32;not,&#32;why.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-55)|Identifier|`owl-ql-profile-error`|
|[Section top](#minorfail-outcome-number-55)|Title|OWL&#32;QL&#32;Profile&#32;incompatible|
|[Section top](#minorfail-outcome-number-55)|Description|Statement&#32;not&#32;supported&#32;in&#32;a&#32;Super&#32;Class&#32;Expression|
|[Section top](#minorfail-outcome-number-55)|Pointer|<pre lang="Turtle"><code>&#91;]&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32;&#32; &#32;owl:onProperty&#32;aec3po:hasSubdivision&#32;.</code></pre>|

***
### MinorFail Outcome number 56

[Jump to summary definition](#summary-MinorFail-56)	|	[Previous MinorFail outcome](#minorfail-outcome-number-55)	|	[Next MinorFail outcome](#minorfail-outcome-number-57)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-src-statement|
|----|----|
|Title|Standalone&#32;module&#32;src/statement.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Module statement](https://github.com/Accord-Project/aec3po/blob/HEAD/src/statement.ttl)|

#### Criterion detail
|Identifier|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|
|----|----|
|Title|Profile&#32;compatibility&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;check&#32;whether&#32;the&#32;test&#32;subject&#32;is&#32;compatible&#32;with&#32;a&#32;profile&#32;or&#32;not,&#32;and&#32;if&#32;it&#32;is&#32;not,&#32;why.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-56)|Identifier|`owl-rl-profile-error`|
|[Section top](#minorfail-outcome-number-56)|Title|OWL&#32;RL&#32;Profile&#32;incompatible|
|[Section top](#minorfail-outcome-number-56)|Description|Class&#32;Expression&#32;not&#32;supported&#32;with&#32;rdfs:subClassOf|
|[Section top](#minorfail-outcome-number-56)|Pointer|<pre lang="Turtle"><code>aec3po:AndCheckStatement&#32;a&#32;owl:Class&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;And&#32;Check&#32;Statement&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;Check&#32;verified&#32;if&#32;and&#32;only&#32;if&#32;all&#32;of&#32;its&#32;sub-checks&#32;are&#32;veri...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32;aec3po:statement&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:subClassOf&#32; &#91;&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:onProperty&#32;aec3po:hasSubdivision&#32;],  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;aec3po:ChecklistStatement&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-56)|Pointer|<pre lang="Turtle"><code>aec3po:NotCheckStatement&#32;a&#32;owl:Class&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;Not&#32;Check&#32;Statement&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;Check&#32;verified&#32;if&#32;and&#32;only&#32;if&#32;the&#32;sub-check&#32;is&#32;not&#32;verified.&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32;aec3po:statement&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:subClassOf&#32; &#91;&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:onProperty&#32;aec3po:hasSubdivision&#32;]&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-56)|Pointer|<pre lang="Turtle"><code>aec3po:OrCheckStatement&#32;a&#32;owl:Class&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;Or&#32;Check&#32;Statement&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;Check&#32;verified&#32;if&#32;and&#32;only&#32;if&#32;at&#32;least&#32;one&#32;of&#32;its&#32;sub-checks...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32;aec3po:statement&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:subClassOf&#32; &#91;&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:onProperty&#32;aec3po:hasSubdivision&#32;],  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;aec3po:ChecklistStatement&#32;.</code></pre>|

***
### MinorFail Outcome number 57

[Jump to summary definition](#summary-MinorFail-57)	|	[Previous MinorFail outcome](#minorfail-outcome-number-56)	|	[Next MinorFail outcome](#minorfail-outcome-number-58)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-src-statement|
|----|----|
|Title|Standalone&#32;module&#32;src/statement.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Module statement](https://github.com/Accord-Project/aec3po/blob/HEAD/src/statement.ttl)|

#### Criterion detail
|Identifier|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|
|----|----|
|Title|Profile&#32;compatibility&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;check&#32;whether&#32;the&#32;test&#32;subject&#32;is&#32;compatible&#32;with&#32;a&#32;profile&#32;or&#32;not,&#32;and&#32;if&#32;it&#32;is&#32;not,&#32;why.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-57)|Identifier|`owl-rl-profile-error`|
|[Section top](#minorfail-outcome-number-57)|Title|OWL&#32;RL&#32;Profile&#32;incompatible|
|[Section top](#minorfail-outcome-number-57)|Description|Statement&#32;not&#32;supported&#32;in&#32;a&#32;Super&#32;Class&#32;Expression|
|[Section top](#minorfail-outcome-number-57)|Pointer|<pre lang="Turtle"><code>&#91;]&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32;&#32; &#32;owl:onProperty&#32;aec3po:hasSubdivision&#32;.</code></pre>|

***
### MinorFail Outcome number 58

[Jump to summary definition](#summary-MinorFail-58)	|	[Previous MinorFail outcome](#minorfail-outcome-number-57)	|	[Next MinorFail outcome](#minorfail-outcome-number-59)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-src-statement|
|----|----|
|Title|Standalone&#32;module&#32;src/statement.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Module statement](https://github.com/Accord-Project/aec3po/blob/HEAD/src/statement.ttl)|

#### Criterion detail
|Identifier|[terms-differenciation](https://ns.inria.fr/olivaw#terms-differenciation)|
|----|----|
|Title|Terms&#32;differenciation&#32;test|
|Description|A&#32;test&#32;case&#32;from&#32;the&#32;Best&#32;Practices&#32;tests&#32;checking&#32;if&#32;all&#32;the&#32;terms&#32;are&#32;different&#32;enough&#32;from&#32;each&#32;other&#32;according&#32;to&#32;the&#32;Levenshtein&#32;distance&#32;metric.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-58)|Identifier|`too-close-terms`|
|[Section top](#minorfail-outcome-number-58)|Title|Too&#32;close&#32;terms|
|[Section top](#minorfail-outcome-number-58)|Description|Some&#32;terms&#32;are&#32;too&#32;similar|
|[Section top](#minorfail-outcome-number-58)|Pointer|<pre lang="Turtle"><code>:OrCheckStatement&#32;a&#32;owl:Class&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;Or&#32;Check&#32;Statement&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;Check&#32;verified&#32;if&#32;and&#32;only&#32;if&#32;at&#32;least&#32;one&#32;of&#32;its&#32;sub-checks...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32;:statement&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:subClassOf&#32; &#91;&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:onProperty&#32;:hasSubdivision&#32;],  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;:ChecklistStatement&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-58)|Pointer|<pre lang="Turtle"><code>:CheckStatement&#32;a&#32;owl:Class&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;Check&#32;Statement&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;refers&#32;to&#32;a&#32;type&#32;of&#32;statement&#32;that&#32;is&#32;used&#32;to&#32;specify&#32;condit...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32;:statement&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:subClassOf&#32;:Statement&#32;.</code></pre>|

***
### MinorFail Outcome number 59

[Jump to summary definition](#summary-MinorFail-59)	|	[Previous MinorFail outcome](#minorfail-outcome-number-58)	|	[Next MinorFail outcome](#minorfail-outcome-number-60)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-src-model|
|----|----|
|Title|Standalone&#32;module&#32;src/model.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Module model](https://github.com/Accord-Project/aec3po/blob/HEAD/src/model.ttl)|

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
|[Section top](#minorfail-outcome-number-59)|Description|Class&#32;Expression&#32;not&#32;supported&#32;as&#32;object&#32;of&#32;rdfs:domain&#32;or&#32;rdfs:range|
|[Section top](#minorfail-outcome-number-59)|Pointer|<pre lang="Turtle"><code>aec3po:locationCoverage&#32;a&#32;owl:ObjectProperty&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;location&#32;coverage&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;The&#32;spatialCoverage&#32;indicates&#32;the&#32;place(s)&#32;or&#32;the&#32;administra...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:domain&#32; &#60;https://schema.org/Model> &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:range&#32; &#91;&#32;a&#32;owl:Class&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:unionOf&#32;(&#32; &#60;https://schema.org/Place> &#32;aec3po:AdministrativeArea&#32;)&#32;]&#32;;  &#10; &#32; &#32; &#32; &#32;owl:equivalentProperty&#32; &#60;https://schema.org/spatialCoverage> &#32;.</code></pre>|

***
### MinorFail Outcome number 60

[Jump to summary definition](#summary-MinorFail-60)	|	[Previous MinorFail outcome](#minorfail-outcome-number-59)	|	[Next MinorFail outcome](#minorfail-outcome-number-61)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-src-model|
|----|----|
|Title|Standalone&#32;module&#32;src/model.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Module model](https://github.com/Accord-Project/aec3po/blob/HEAD/src/model.ttl)|

#### Criterion detail
|Identifier|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|
|----|----|
|Title|Profile&#32;compatibility&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;check&#32;whether&#32;the&#32;test&#32;subject&#32;is&#32;compatible&#32;with&#32;a&#32;profile&#32;or&#32;not,&#32;and&#32;if&#32;it&#32;is&#32;not,&#32;why.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-60)|Identifier|`owl-el-profile-error`|
|[Section top](#minorfail-outcome-number-60)|Title|OWL&#32;EL&#32;Profile&#32;incompatible|
|[Section top](#minorfail-outcome-number-60)|Description|Statement&#32;not&#32;supported&#32;in&#32;a&#32;Class&#32;Expression|
|[Section top](#minorfail-outcome-number-60)|Pointer|<pre lang="Turtle"><code>&#91;]&#32;a&#32;owl:Class&#32;;  &#10; &#32; &#32;&#32; &#32;owl:unionOf&#32;(&#32; &#60;https://schema.org/Place> &#32;aec3po:AdministrativeArea&#32;)&#32;.</code></pre>|

***
### MinorFail Outcome number 61

[Jump to summary definition](#summary-MinorFail-61)	|	[Previous MinorFail outcome](#minorfail-outcome-number-60)	|	[Next MinorFail outcome](#minorfail-outcome-number-62)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-src-model|
|----|----|
|Title|Standalone&#32;module&#32;src/model.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Module model](https://github.com/Accord-Project/aec3po/blob/HEAD/src/model.ttl)|

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
|[Section top](#minorfail-outcome-number-61)|Description|Class&#32;Expression&#32;not&#32;supported&#32;as&#32;object&#32;of&#32;rdfs:domain&#32;or&#32;rdfs:range|
|[Section top](#minorfail-outcome-number-61)|Pointer|<pre lang="Turtle"><code>aec3po:locationCoverage&#32;a&#32;owl:ObjectProperty&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;location&#32;coverage&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;The&#32;spatialCoverage&#32;indicates&#32;the&#32;place(s)&#32;or&#32;the&#32;administra...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:domain&#32; &#60;https://schema.org/Model> &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:range&#32; &#91;&#32;a&#32;owl:Class&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:unionOf&#32;(&#32; &#60;https://schema.org/Place> &#32;aec3po:AdministrativeArea&#32;)&#32;]&#32;;  &#10; &#32; &#32; &#32; &#32;owl:equivalentProperty&#32; &#60;https://schema.org/spatialCoverage> &#32;.</code></pre>|

***
### MinorFail Outcome number 62

[Jump to summary definition](#summary-MinorFail-62)	|	[Previous MinorFail outcome](#minorfail-outcome-number-61)	|	[Next MinorFail outcome](#minorfail-outcome-number-63)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-src-model|
|----|----|
|Title|Standalone&#32;module&#32;src/model.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Module model](https://github.com/Accord-Project/aec3po/blob/HEAD/src/model.ttl)|

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
|[Section top](#minorfail-outcome-number-62)|Pointer|<pre lang="Turtle"><code>&#91;]&#32;a&#32;owl:Class&#32;;  &#10; &#32; &#32;&#32; &#32;owl:unionOf&#32;(&#32; &#60;https://schema.org/Place> &#32;aec3po:AdministrativeArea&#32;)&#32;.</code></pre>|

***
### MinorFail Outcome number 63

[Jump to summary definition](#summary-MinorFail-63)	|	[Previous MinorFail outcome](#minorfail-outcome-number-62)	|	[Next MinorFail outcome](#minorfail-outcome-number-64)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-src-model|
|----|----|
|Title|Standalone&#32;module&#32;src/model.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Module model](https://github.com/Accord-Project/aec3po/blob/HEAD/src/model.ttl)|

#### Criterion detail
|Identifier|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|
|----|----|
|Title|Profile&#32;compatibility&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;check&#32;whether&#32;the&#32;test&#32;subject&#32;is&#32;compatible&#32;with&#32;a&#32;profile&#32;or&#32;not,&#32;and&#32;if&#32;it&#32;is&#32;not,&#32;why.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-63)|Identifier|`owl-rl-profile-error`|
|[Section top](#minorfail-outcome-number-63)|Title|OWL&#32;RL&#32;Profile&#32;incompatible|
|[Section top](#minorfail-outcome-number-63)|Description|Class&#32;Expression&#32;not&#32;supported&#32;as&#32;object&#32;of&#32;rdfs:domain&#32;or&#32;rdfs:range|
|[Section top](#minorfail-outcome-number-63)|Pointer|<pre lang="Turtle"><code>aec3po:locationCoverage&#32;a&#32;owl:ObjectProperty&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;location&#32;coverage&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;The&#32;spatialCoverage&#32;indicates&#32;the&#32;place(s)&#32;or&#32;the&#32;administra...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:domain&#32; &#60;https://schema.org/Model> &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:range&#32; &#91;&#32;a&#32;owl:Class&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:unionOf&#32;(&#32; &#60;https://schema.org/Place> &#32;aec3po:AdministrativeArea&#32;)&#32;]&#32;;  &#10; &#32; &#32; &#32; &#32;owl:equivalentProperty&#32; &#60;https://schema.org/spatialCoverage> &#32;.</code></pre>|

***
### MinorFail Outcome number 64

[Jump to summary definition](#summary-MinorFail-64)	|	[Previous MinorFail outcome](#minorfail-outcome-number-63)	|	[Next MinorFail outcome](#minorfail-outcome-number-65)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-src-model|
|----|----|
|Title|Standalone&#32;module&#32;src/model.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Module model](https://github.com/Accord-Project/aec3po/blob/HEAD/src/model.ttl)|

#### Criterion detail
|Identifier|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|
|----|----|
|Title|Profile&#32;compatibility&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;check&#32;whether&#32;the&#32;test&#32;subject&#32;is&#32;compatible&#32;with&#32;a&#32;profile&#32;or&#32;not,&#32;and&#32;if&#32;it&#32;is&#32;not,&#32;why.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-64)|Identifier|`owl-rl-profile-error`|
|[Section top](#minorfail-outcome-number-64)|Title|OWL&#32;RL&#32;Profile&#32;incompatible|
|[Section top](#minorfail-outcome-number-64)|Description|Statement&#32;not&#32;supported&#32;in&#32;a&#32;Super&#32;Class&#32;Expression|
|[Section top](#minorfail-outcome-number-64)|Pointer|<pre lang="Turtle"><code>&#91;]&#32;a&#32;owl:Class&#32;;  &#10; &#32; &#32;&#32; &#32;owl:unionOf&#32;(&#32; &#60;https://schema.org/Place> &#32;aec3po:AdministrativeArea&#32;)&#32;.</code></pre>|

***
### MinorFail Outcome number 65

[Jump to summary definition](#summary-MinorFail-65)	|	[Previous MinorFail outcome](#minorfail-outcome-number-64)	|	[Next MinorFail outcome](#minorfail-outcome-number-66)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-src-model|
|----|----|
|Title|Standalone&#32;module&#32;src/model.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Module model](https://github.com/Accord-Project/aec3po/blob/HEAD/src/model.ttl)|

#### Criterion detail
|Identifier|[term-referencing](https://ns.inria.fr/olivaw#term-referencing)|
|----|----|
|Title|Term&#32;referencing&#32;test|
|Description|A&#32;test&#32;case&#32;from&#32;the&#32;Best&#32;Practices&#32;tests&#32;checking&#32;if&#32;each&#32;term&#32;of&#32;the&#32;test&#32;subject&#32;is&#32;referenced&#32;to&#32;a&#32;module&#32;through&#32;a&#32;rdfs:isDefinedBy&#32;property.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-65)|Identifier|`no-reference-module`|
|[Section top](#minorfail-outcome-number-65)|Title|Term&#32;not&#32;referenced&#32;to&#32;a&#32;module|
|[Section top](#minorfail-outcome-number-65)|Description|Subject&#32;terms&#32;not&#32;linked&#32;to&#32;a&#32;module&#32;by&#32;a&#32;rdfs:isDefinedBy&#32;property|
|[Section top](#minorfail-outcome-number-65)|Pointer|<pre lang="Turtle"><code>:name&#32;a&#32;owl:DatatypeProperty&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;name&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;The&#32;name&#32;or&#32;the&#32;identifier&#32;of&#32;the&#32;BIM&#32;model.&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:domain&#32; &#60;https://schema.org/Model> &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:range&#32;xsd:string&#32;;  &#10; &#32; &#32; &#32; &#32;owl:equivalentProperty&#32; &#60;https://schema.org/about> &#32;;  &#10; &#32; &#32; &#32; &#32;owl:inverseOf&#32; &#60;https://schema.org/subjectOf> &#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-65)|Pointer|<pre lang="Turtle"><code>:description&#32;a&#32;owl:DatatypeProperty&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;description&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;A&#32;textual&#32;description&#32;providing&#32;additional&#32;details&#32;about&#32;the...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:domain&#32; &#60;https://schema.org/Model> &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:range&#32;xsd:string&#32;;  &#10; &#32; &#32; &#32; &#32;owl:equivalentProperty&#32; &#60;https://schema.org/abstract> &#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-65)|Pointer|<pre lang="Turtle"><code>:location&#32;a&#32;owl:ObjectProperty&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;location&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;The&#32;physical&#32;or&#32;geographic&#32;location&#32;of&#32;the&#32;building&#32;or&#32;struc...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:domain&#32; &#60;https://schema.org/Model> &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:range&#32; &#60;https://schema.org/Place> &#32;;  &#10; &#32; &#32; &#32; &#32;owl:equivalentProperty&#32; &#60;https://schema.org/spatial> &#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-65)|Pointer|<pre lang="Turtle"><code>:locationCoverage&#32;a&#32;owl:ObjectProperty&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;location&#32;coverage&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;The&#32;spatialCoverage&#32;indicates&#32;the&#32;place(s)&#32;or&#32;the&#32;administra...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:domain&#32; &#60;https://schema.org/Model> &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:range&#32; &#91;&#32;a&#32;owl:Class&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:unionOf&#32;(&#32; &#60;https://schema.org/Place> &#32;:AdministrativeArea&#32;)&#32;]&#32;;  &#10; &#32; &#32; &#32; &#32;owl:equivalentProperty&#32; &#60;https://schema.org/spatialCoverage> &#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-65)|Pointer|<pre lang="Turtle"><code>:material&#32;a&#32;owl:DatatypeProperty&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;material&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;The&#32;materials&#32;used&#32;for&#32;different&#32;parts&#32;of&#32;the&#32;building,&#32;such...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:domain&#32; &#60;https://schema.org/Model> &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:range&#32;xsd:string&#32;;  &#10; &#32; &#32; &#32; &#32;owl:equivalentProperty&#32; &#60;https://schema.org/material> &#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-65)|Pointer|<pre lang="Turtle"><code>:hasBuildingPhase&#32;a&#32;owl:ObjectProperty&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;has&#32;building&#32;phase&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;describes&#32;the&#32;relationship&#32;between&#32;a&#32;construction-related&#32;en...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:domain&#32;:Model&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:range&#32;:Phase&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-65)|Pointer|<pre lang="Turtle"><code>:hasElementPhase&#32;a&#32;owl:ObjectProperty&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;has&#32;element&#32;phase&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;is&#32;used&#32;to&#32;establish&#32;a&#32;relationship&#32;between&#32;a&#32;construction&#32;e...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:domain&#32;:Model&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:range&#32;:Phase&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-65)|Pointer|<pre lang="Turtle"><code>:hasDimension&#32;a&#32;owl:ObjectProperty&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;has&#32;dimension&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;is&#32;used&#32;to&#32;represent&#32;the&#32;physical&#32;dimensions&#32;or&#32;measurements...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:domain&#32;:Model&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:range&#32;:Dimension&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-65)|Pointer|<pre lang="Turtle"><code>:hasClassification&#32;a&#32;owl:ObjectProperty&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;has&#32;dimension&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;is&#32;used&#32;to&#32;link&#32;building&#32;components,&#32;elements,&#32;or&#32;other&#32;enti...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:domain&#32;:Model&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:range&#32;:Classification&#32;.</code></pre>|

***
### MinorFail Outcome number 66

[Jump to summary definition](#summary-MinorFail-66)	|	[Previous MinorFail outcome](#minorfail-outcome-number-65)	|	[Next MinorFail outcome](#minorfail-outcome-number-67)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-src-legal-verifier|
|----|----|
|Title|Standalone&#32;module&#32;src/legal&lowbar;verifier.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Module legal&lowbar;verifier](https://github.com/Accord-Project/aec3po/blob/HEAD/src/legal_verifier.ttl)|

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
|[Section top](#minorfail-outcome-number-66)|Description|Class&#32;Expression&#32;not&#32;supported&#32;with&#32;rdfs:subClassOf|
|[Section top](#minorfail-outcome-number-66)|Pointer|<pre lang="Turtle"><code>aec3po:LegalVerifier&#32;a&#32;owl:Class&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;Legal&#32;Verifier&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;An&#32;entity&#32;that&#32;has&#32;the&#32;legal&#32;capacity&#32;to&#32;verify&#32;compliance&#32;w...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32;aec3po:legal&lowbar;verifier&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:subClassOf&#32; &#91;&#32;owl:allValuesFrom&#32;aec3po:Document&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:onProperty&#32;aec3po:forDocument&#32;],  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;foaf:Agent&#32;.</code></pre>|

***
### MinorFail Outcome number 67

[Jump to summary definition](#summary-MinorFail-67)	|	[Previous MinorFail outcome](#minorfail-outcome-number-66)	|	[Next MinorFail outcome](#minorfail-outcome-number-68)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-src-legal-verifier|
|----|----|
|Title|Standalone&#32;module&#32;src/legal&lowbar;verifier.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Module legal&lowbar;verifier](https://github.com/Accord-Project/aec3po/blob/HEAD/src/legal_verifier.ttl)|

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
|[Section top](#minorfail-outcome-number-67)|Pointer|<pre lang="Turtle"><code>&#91;]&#32;owl:allValuesFrom&#32;aec3po:Document&#32;;  &#10; &#32; &#32;&#32; &#32;owl:onProperty&#32;aec3po:forDocument&#32;.</code></pre>|

***
### MinorFail Outcome number 68

[Jump to summary definition](#summary-MinorFail-68)	|	[Previous MinorFail outcome](#minorfail-outcome-number-67)	|	[Next MinorFail outcome](#minorfail-outcome-number-69)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-src-legal-verifier|
|----|----|
|Title|Standalone&#32;module&#32;src/legal&lowbar;verifier.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Module legal&lowbar;verifier](https://github.com/Accord-Project/aec3po/blob/HEAD/src/legal_verifier.ttl)|

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
|[Section top](#minorfail-outcome-number-68)|Pointer|<pre lang="Turtle"><code>aec3po:LegalVerifier&#32;a&#32;owl:Class&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;Legal&#32;Verifier&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;An&#32;entity&#32;that&#32;has&#32;the&#32;legal&#32;capacity&#32;to&#32;verify&#32;compliance&#32;w...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32;aec3po:legal&lowbar;verifier&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:subClassOf&#32; &#91;&#32;owl:allValuesFrom&#32;aec3po:Document&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:onProperty&#32;aec3po:forDocument&#32;],  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;foaf:Agent&#32;.</code></pre>|

***
### MinorFail Outcome number 69

[Jump to summary definition](#summary-MinorFail-69)	|	[Previous MinorFail outcome](#minorfail-outcome-number-68)	|	[Next MinorFail outcome](#minorfail-outcome-number-70)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-src-legal-verifier|
|----|----|
|Title|Standalone&#32;module&#32;src/legal&lowbar;verifier.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Module legal&lowbar;verifier](https://github.com/Accord-Project/aec3po/blob/HEAD/src/legal_verifier.ttl)|

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
|[Section top](#minorfail-outcome-number-69)|Description|Statement&#32;not&#32;supported&#32;in&#32;a&#32;Super&#32;Class&#32;Expression|
|[Section top](#minorfail-outcome-number-69)|Pointer|<pre lang="Turtle"><code>&#91;]&#32;owl:allValuesFrom&#32;aec3po:Document&#32;;  &#10; &#32; &#32;&#32; &#32;owl:onProperty&#32;aec3po:forDocument&#32;.</code></pre>|

***
### MinorFail Outcome number 70

[Jump to summary definition](#summary-MinorFail-70)	|	[Previous MinorFail outcome](#minorfail-outcome-number-69)	|	[Next MinorFail outcome](#minorfail-outcome-number-71)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-src-feature-of-interest|
|----|----|
|Title|Standalone&#32;module&#32;src/feature&lowbar;of&lowbar;interest.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Module feature&lowbar;of&lowbar;interest](https://github.com/Accord-Project/aec3po/blob/HEAD/src/feature_of_interest.ttl)|

#### Criterion detail
|Identifier|[domain-and-range-referencing](https://ns.inria.fr/olivaw#domain-and-range-referencing)|
|----|----|
|Title|Domain&#32;and&#32;range&#32;referencing&#32;test|
|Description|A&#32;test&#32;case&#32;from&#32;the&#32;Best&#32;Practices&#32;tests&#32;checking&#32;if&#32;all&#32;the&#32;ranges&#32;and&#32;domains&#32;from&#32;the&#32;test&#32;subject&#32;point&#32;to&#32;terms&#32;that&#32;are&#32;defined&#32;in&#32;the&#32;vocabulary.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-70)|Identifier|`domain-out-of-vocabulary`|
|[Section top](#minorfail-outcome-number-70)|Title|Domain&#32;out&#32;of&#32;vocabulary|
|[Section top](#minorfail-outcome-number-70)|Description|Some&#32;properties&#32;have&#32;a&#32;domain&#32;out&#32;of&#32;the&#32;ontology|
|[Section top](#minorfail-outcome-number-70)|Pointer|<pre lang="Turtle"><code>:hasProperty&#32;a&#32;owl:ObjectProperty&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;has&#32;Property&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;Links&#32;a&#32;feature&#32;of&#32;interest&#32;to&#32;one&#32;of&#32;its&#32;aspect&#32;that&#32;is&#32;int...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:domain&#32; &#60;http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#Object>,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#60;https://saref.etsi.org/core/FeatureOfInterest>,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;:FeatureOfInterest&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32;:feature&lowbar;of&lowbar;interest&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:range&#32; &#60;http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#Quality>,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;:Property&#32;;  &#10; &#32; &#32; &#32; &#32;skos:example&#32; &#34;Links&#32;a&#32;space&#32;to&#32;the&#32;area&#32;property&#32;of&#32;that&#32;space,&#32;a&#32;wall&#32;to&#32;...&#34; &#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-70)|Pointer|<pre lang="Turtle"><code>http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#Object</code></pre>|
|[Section top](#minorfail-outcome-number-70)|Pointer|<pre lang="Turtle"><code>https://saref.etsi.org/core/FeatureOfInterest</code></pre>|
|[Section top](#minorfail-outcome-number-70)|Pointer|<pre lang="Turtle"><code>:hasQuantityKind&#32;a&#32;owl:ObjectProperty&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;has&#32;quantity&#32;kind&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;Links&#32;a&#32;property&#32;to&#32;its&#32;quantity&#32;kind&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:domain&#32; &#60;http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#Quality>,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;:Property&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32;:feature&lowbar;of&lowbar;interest&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:range&#32;:QuantityKind&#32;;  &#10; &#32; &#32; &#32; &#32;skos:example&#32; &#34;A&#32;space&#32;area&#32;property&#32;to&#32;the&#32;property&#32;kind&#32; &#92; &#34;area&#92; &#34;.&#34;@en&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-70)|Pointer|<pre lang="Turtle"><code>http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#Quality</code></pre>|

***
### MinorFail Outcome number 71

[Jump to summary definition](#summary-MinorFail-71)	|	[Previous MinorFail outcome](#minorfail-outcome-number-70)	|	[Next MinorFail outcome](#minorfail-outcome-number-72)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-src-feature-of-interest|
|----|----|
|Title|Standalone&#32;module&#32;src/feature&lowbar;of&lowbar;interest.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Module feature&lowbar;of&lowbar;interest](https://github.com/Accord-Project/aec3po/blob/HEAD/src/feature_of_interest.ttl)|

#### Criterion detail
|Identifier|[domain-and-range-referencing](https://ns.inria.fr/olivaw#domain-and-range-referencing)|
|----|----|
|Title|Domain&#32;and&#32;range&#32;referencing&#32;test|
|Description|A&#32;test&#32;case&#32;from&#32;the&#32;Best&#32;Practices&#32;tests&#32;checking&#32;if&#32;all&#32;the&#32;ranges&#32;and&#32;domains&#32;from&#32;the&#32;test&#32;subject&#32;point&#32;to&#32;terms&#32;that&#32;are&#32;defined&#32;in&#32;the&#32;vocabulary.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-71)|Identifier|`range-out-of-vocabulary`|
|[Section top](#minorfail-outcome-number-71)|Title|Range&#32;out&#32;of&#32;vocabulary|
|[Section top](#minorfail-outcome-number-71)|Description|Some&#32;properties&#32;have&#32;a&#32;range&#32;out&#32;of&#32;the&#32;ontology|
|[Section top](#minorfail-outcome-number-71)|Pointer|<pre lang="Turtle"><code>:hasProperty&#32;a&#32;owl:ObjectProperty&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;has&#32;Property&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;Links&#32;a&#32;feature&#32;of&#32;interest&#32;to&#32;one&#32;of&#32;its&#32;aspect&#32;that&#32;is&#32;int...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:domain&#32; &#60;http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#Object>,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#60;https://saref.etsi.org/core/FeatureOfInterest>,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;:FeatureOfInterest&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32;:feature&lowbar;of&lowbar;interest&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:range&#32; &#60;http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#Quality>,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;:Property&#32;;  &#10; &#32; &#32; &#32; &#32;skos:example&#32; &#34;Links&#32;a&#32;space&#32;to&#32;the&#32;area&#32;property&#32;of&#32;that&#32;space,&#32;a&#32;wall&#32;to&#32;...&#34; &#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-71)|Pointer|<pre lang="Turtle"><code>http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#Quality</code></pre>|

***
### MinorFail Outcome number 72

[Jump to summary definition](#summary-MinorFail-72)	|	[Previous MinorFail outcome](#minorfail-outcome-number-71)	|	[Next MinorFail outcome](#minorfail-outcome-number-73)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-src-evidence|
|----|----|
|Title|Standalone&#32;module&#32;src/evidence.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Module evidence](https://github.com/Accord-Project/aec3po/blob/HEAD/src/evidence.ttl)|

#### Criterion detail
|Identifier|[domain-and-range-referencing](https://ns.inria.fr/olivaw#domain-and-range-referencing)|
|----|----|
|Title|Domain&#32;and&#32;range&#32;referencing&#32;test|
|Description|A&#32;test&#32;case&#32;from&#32;the&#32;Best&#32;Practices&#32;tests&#32;checking&#32;if&#32;all&#32;the&#32;ranges&#32;and&#32;domains&#32;from&#32;the&#32;test&#32;subject&#32;point&#32;to&#32;terms&#32;that&#32;are&#32;defined&#32;in&#32;the&#32;vocabulary.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-72)|Identifier|`range-out-of-vocabulary`|
|[Section top](#minorfail-outcome-number-72)|Title|Range&#32;out&#32;of&#32;vocabulary|
|[Section top](#minorfail-outcome-number-72)|Description|Some&#32;properties&#32;have&#32;a&#32;range&#32;out&#32;of&#32;the&#32;ontology|
|[Section top](#minorfail-outcome-number-72)|Pointer|<pre lang="Turtle"><code>:hasFormat&#32;a&#32;owl:ObjectProperty&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;Defines&#32;the&#32;format&#32;of&#32;an&#32;evidence,&#32;which&#32;is&#32;of&#32;type&#32;dct:form...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:domain&#32;:Statement&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32;:evidence&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:range&#32;dc:format&#32;;  &#10; &#32; &#32; &#32; &#32;skos:example&#32; &#34;an&#32;image,&#32;a&#32;drawing&#32;or&#32;a&#32;model&#32;can&#32;be&#32;an&#32;evidence.&#34;@en&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-72)|Pointer|http://purl.org/dc/elements/1.1/format|

***
### MinorFail Outcome number 73

[Jump to summary definition](#summary-MinorFail-73)	|	[Previous MinorFail outcome](#minorfail-outcome-number-72)	|	[Next MinorFail outcome](#minorfail-outcome-number-74)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-src-evidence|
|----|----|
|Title|Standalone&#32;module&#32;src/evidence.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Module evidence](https://github.com/Accord-Project/aec3po/blob/HEAD/src/evidence.ttl)|

#### Criterion detail
|Identifier|[labeled-terms](https://ns.inria.fr/olivaw#labeled-terms)|
|----|----|
|Title|Term&#32;labeling&#32;test|
|Description|A&#32;test&#32;case&#32;from&#32;the&#32;Best&#32;Practices&#32;tests&#32;checking&#32;if&#32;all&#32;the&#32;terms&#32;of&#32;the&#32;subject&#32;have&#32;a&#32;rdfs:label&#32;property&#32;pointing&#32;to&#32;a&#32;literal&#32;in&#32;English|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-73)|Identifier|`not-labeled-term`|
|[Section top](#minorfail-outcome-number-73)|Title|Terms&#32;not&#32;labeled|
|[Section top](#minorfail-outcome-number-73)|Description|The&#32;following&#32;terms&#32;have&#32;no&#32;rdfs:label&#32;to&#32;define&#32;it&#32;in&#32;natural&#32;language|
|[Section top](#minorfail-outcome-number-73)|Pointer|<pre lang="Turtle"><code>:hasEvidence&#32;a&#32;owl:ObjectProperty&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;Links&#32;a&#32;statement&#32;to&#32;a&#32;piece&#32;of&#32;evidence&#32;for&#32;that&#32;statement&#32;...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:domain&#32;:Statement&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32;:statement&#32;;  &#10; &#32; &#32; &#32; &#32;skos:note&#32; &#34;Unstable.&#32;Need&#32;evidence&#32;of&#32;how&#32;this&#32;property&#32;is&#32;intended&#32;to&#32;...&#34; &#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-73)|Pointer|<pre lang="Turtle"><code>:hasFormat&#32;a&#32;owl:ObjectProperty&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;Defines&#32;the&#32;format&#32;of&#32;an&#32;evidence,&#32;which&#32;is&#32;of&#32;type&#32;dct:form...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:domain&#32;:Statement&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32;:evidence&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:range&#32;dc:format&#32;;  &#10; &#32; &#32; &#32; &#32;skos:example&#32; &#34;an&#32;image,&#32;a&#32;drawing&#32;or&#32;a&#32;model&#32;can&#32;be&#32;an&#32;evidence.&#34;@en&#32;.</code></pre>|

***
### MinorFail Outcome number 74

[Jump to summary definition](#summary-MinorFail-74)	|	[Previous MinorFail outcome](#minorfail-outcome-number-73)	|	[Next MinorFail outcome](#minorfail-outcome-number-75)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-src-document|
|----|----|
|Title|Standalone&#32;module&#32;src/document.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Module document](https://github.com/Accord-Project/aec3po/blob/HEAD/src/document.ttl)|

#### Criterion detail
|Identifier|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|
|----|----|
|Title|Profile&#32;compatibility&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;check&#32;whether&#32;the&#32;test&#32;subject&#32;is&#32;compatible&#32;with&#32;a&#32;profile&#32;or&#32;not,&#32;and&#32;if&#32;it&#32;is&#32;not,&#32;why.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-74)|Identifier|`owl-el-profile-error`|
|[Section top](#minorfail-outcome-number-74)|Title|OWL&#32;EL&#32;Profile&#32;incompatible|
|[Section top](#minorfail-outcome-number-74)|Description|Class&#32;Expression&#32;not&#32;supported&#32;as&#32;object&#32;of&#32;rdfs:domain&#32;or&#32;rdfs:range|
|[Section top](#minorfail-outcome-number-74)|Pointer|<pre lang="Turtle"><code>aec3po:hasFirstSubdivision&#32;a&#32;owl:FunctionalProperty,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:ObjectProperty&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;has&#32;first&#32;subdivision&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;Links&#32;a&#32;document&#32;part&#32;to&#32;the&#32;first&#32;of&#32;its&#32;subdivision&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:domain&#32; &#91;&#32;owl:unionOf&#32;(&#32;aec3po:Document&#32;aec3po:DocumentSubdivision&#32;)&#32;]&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32;aec3po:document&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:range&#32;aec3po:DocumentSubdivision&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:subPropertyOf&#32;aec3po:hasSubdivision&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-74)|Pointer|<pre lang="Turtle"><code>aec3po:hasSubdivision&#32;a&#32;owl:ObjectProperty&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;has&#32;subdivision&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;links&#32;a&#32;document&#32;part&#32;to&#32;some&#32;of&#32;its&#32;subdivision&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:domain&#32; &#91;&#32;owl:unionOf&#32;(&#32;aec3po:Document&#32;aec3po:DocumentSubdivision&#32;)&#32;]&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32;aec3po:document&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:range&#32;aec3po:DocumentSubdivision&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:subPropertyOf&#32;dc:hasPart&#32;.</code></pre>|

***
### MinorFail Outcome number 75

[Jump to summary definition](#summary-MinorFail-75)	|	[Previous MinorFail outcome](#minorfail-outcome-number-74)	|	[Next MinorFail outcome](#minorfail-outcome-number-76)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-src-document|
|----|----|
|Title|Standalone&#32;module&#32;src/document.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Module document](https://github.com/Accord-Project/aec3po/blob/HEAD/src/document.ttl)|

#### Criterion detail
|Identifier|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|
|----|----|
|Title|Profile&#32;compatibility&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;check&#32;whether&#32;the&#32;test&#32;subject&#32;is&#32;compatible&#32;with&#32;a&#32;profile&#32;or&#32;not,&#32;and&#32;if&#32;it&#32;is&#32;not,&#32;why.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-75)|Identifier|`owl-el-profile-error`|
|[Section top](#minorfail-outcome-number-75)|Title|OWL&#32;EL&#32;Profile&#32;incompatible|
|[Section top](#minorfail-outcome-number-75)|Description|Class&#32;Expression&#32;not&#32;supported&#32;with&#32;rdfs:subClassOf|
|[Section top](#minorfail-outcome-number-75)|Pointer|<pre lang="Turtle"><code>aec3po:DocumentSubdivision&#32;a&#32;owl:Class&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;Document&#32;Subdivision&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;Any&#32;subdivision&#32;of&#32;a&#32;document,&#32;including&#32;sections,&#32;paragraph...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32;aec3po:document&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:subClassOf&#32; &#91;&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:allValuesFrom&#32;aec3po:DocumentSubdivision&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:onProperty&#32;aec3po:hasSubdivision&#32;]&#32;;  &#10; &#32; &#32; &#32; &#32;skos:example&#32; &#34;Paragraph,&#32;section,&#32;definition...&#34;@en&#32;.</code></pre>|

***
### MinorFail Outcome number 76

[Jump to summary definition](#summary-MinorFail-76)	|	[Previous MinorFail outcome](#minorfail-outcome-number-75)	|	[Next MinorFail outcome](#minorfail-outcome-number-77)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-src-document|
|----|----|
|Title|Standalone&#32;module&#32;src/document.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Module document](https://github.com/Accord-Project/aec3po/blob/HEAD/src/document.ttl)|

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
|[Section top](#minorfail-outcome-number-76)|Description|Statement&#32;not&#32;supported&#32;in&#32;a&#32;Class&#32;Expression|
|[Section top](#minorfail-outcome-number-76)|Pointer|<pre lang="Turtle"><code>&#91;]&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32;owl:allValuesFrom&#32;aec3po:DocumentSubdivision&#32;;  &#10; &#32; &#32; &#32; &#32;owl:onProperty&#32;aec3po:hasSubdivision&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-76)|Pointer|<pre lang="Turtle"><code>&#91;]&#32;owl:unionOf&#32;(&#32;aec3po:Document&#32;aec3po:DocumentSubdivision&#32;)&#32;.</code></pre>|

***
### MinorFail Outcome number 77

[Jump to summary definition](#summary-MinorFail-77)	|	[Previous MinorFail outcome](#minorfail-outcome-number-76)	|	[Next MinorFail outcome](#minorfail-outcome-number-78)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-src-document|
|----|----|
|Title|Standalone&#32;module&#32;src/document.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Module document](https://github.com/Accord-Project/aec3po/blob/HEAD/src/document.ttl)|

#### Criterion detail
|Identifier|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|
|----|----|
|Title|Profile&#32;compatibility&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;check&#32;whether&#32;the&#32;test&#32;subject&#32;is&#32;compatible&#32;with&#32;a&#32;profile&#32;or&#32;not,&#32;and&#32;if&#32;it&#32;is&#32;not,&#32;why.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-77)|Identifier|`owl-ql-profile-error`|
|[Section top](#minorfail-outcome-number-77)|Title|OWL&#32;QL&#32;Profile&#32;incompatible|
|[Section top](#minorfail-outcome-number-77)|Description|Class&#32;Expression&#32;not&#32;supported&#32;as&#32;object&#32;of&#32;rdfs:domain&#32;or&#32;rdfs:range|
|[Section top](#minorfail-outcome-number-77)|Pointer|<pre lang="Turtle"><code>aec3po:hasFirstSubdivision&#32;a&#32;owl:FunctionalProperty,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:ObjectProperty&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;has&#32;first&#32;subdivision&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;Links&#32;a&#32;document&#32;part&#32;to&#32;the&#32;first&#32;of&#32;its&#32;subdivision&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:domain&#32; &#91;&#32;owl:unionOf&#32;(&#32;aec3po:Document&#32;aec3po:DocumentSubdivision&#32;)&#32;]&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32;aec3po:document&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:range&#32;aec3po:DocumentSubdivision&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:subPropertyOf&#32;aec3po:hasSubdivision&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-77)|Pointer|<pre lang="Turtle"><code>aec3po:hasSubdivision&#32;a&#32;owl:ObjectProperty&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;has&#32;subdivision&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;links&#32;a&#32;document&#32;part&#32;to&#32;some&#32;of&#32;its&#32;subdivision&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:domain&#32; &#91;&#32;owl:unionOf&#32;(&#32;aec3po:Document&#32;aec3po:DocumentSubdivision&#32;)&#32;]&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32;aec3po:document&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:range&#32;aec3po:DocumentSubdivision&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:subPropertyOf&#32;dc:hasPart&#32;.</code></pre>|

***
### MinorFail Outcome number 78

[Jump to summary definition](#summary-MinorFail-78)	|	[Previous MinorFail outcome](#minorfail-outcome-number-77)	|	[Next MinorFail outcome](#minorfail-outcome-number-79)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-src-document|
|----|----|
|Title|Standalone&#32;module&#32;src/document.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Module document](https://github.com/Accord-Project/aec3po/blob/HEAD/src/document.ttl)|

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
|[Section top](#minorfail-outcome-number-78)|Description|Class&#32;Expression&#32;not&#32;supported&#32;with&#32;rdfs:subClassOf|
|[Section top](#minorfail-outcome-number-78)|Pointer|<pre lang="Turtle"><code>aec3po:DocumentSubdivision&#32;a&#32;owl:Class&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;Document&#32;Subdivision&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;Any&#32;subdivision&#32;of&#32;a&#32;document,&#32;including&#32;sections,&#32;paragraph...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32;aec3po:document&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:subClassOf&#32; &#91;&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:allValuesFrom&#32;aec3po:DocumentSubdivision&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:onProperty&#32;aec3po:hasSubdivision&#32;]&#32;;  &#10; &#32; &#32; &#32; &#32;skos:example&#32; &#34;Paragraph,&#32;section,&#32;definition...&#34;@en&#32;.</code></pre>|

***
### MinorFail Outcome number 79

[Jump to summary definition](#summary-MinorFail-79)	|	[Previous MinorFail outcome](#minorfail-outcome-number-78)	|	[Next MinorFail outcome](#minorfail-outcome-number-80)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-src-document|
|----|----|
|Title|Standalone&#32;module&#32;src/document.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Module document](https://github.com/Accord-Project/aec3po/blob/HEAD/src/document.ttl)|

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
|[Section top](#minorfail-outcome-number-79)|Description|Statement&#32;not&#32;supported&#32;in&#32;a&#32;Super&#32;Class&#32;Expression|
|[Section top](#minorfail-outcome-number-79)|Pointer|<pre lang="Turtle"><code>&#91;]&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32;owl:allValuesFrom&#32;aec3po:DocumentSubdivision&#32;;  &#10; &#32; &#32; &#32; &#32;owl:onProperty&#32;aec3po:hasSubdivision&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-79)|Pointer|<pre lang="Turtle"><code>&#91;]&#32;owl:unionOf&#32;(&#32;aec3po:Document&#32;aec3po:DocumentSubdivision&#32;)&#32;.</code></pre>|

***
### MinorFail Outcome number 80

[Jump to summary definition](#summary-MinorFail-80)	|	[Previous MinorFail outcome](#minorfail-outcome-number-79)	|	[Next MinorFail outcome](#minorfail-outcome-number-81)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-src-document|
|----|----|
|Title|Standalone&#32;module&#32;src/document.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Module document](https://github.com/Accord-Project/aec3po/blob/HEAD/src/document.ttl)|

#### Criterion detail
|Identifier|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|
|----|----|
|Title|Profile&#32;compatibility&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;check&#32;whether&#32;the&#32;test&#32;subject&#32;is&#32;compatible&#32;with&#32;a&#32;profile&#32;or&#32;not,&#32;and&#32;if&#32;it&#32;is&#32;not,&#32;why.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-80)|Identifier|`owl-rl-profile-error`|
|[Section top](#minorfail-outcome-number-80)|Title|OWL&#32;RL&#32;Profile&#32;incompatible|
|[Section top](#minorfail-outcome-number-80)|Description|Class&#32;Expression&#32;not&#32;supported&#32;as&#32;object&#32;of&#32;rdfs:domain&#32;or&#32;rdfs:range|
|[Section top](#minorfail-outcome-number-80)|Pointer|<pre lang="Turtle"><code>aec3po:hasFirstSubdivision&#32;a&#32;owl:FunctionalProperty,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:ObjectProperty&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;has&#32;first&#32;subdivision&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;Links&#32;a&#32;document&#32;part&#32;to&#32;the&#32;first&#32;of&#32;its&#32;subdivision&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:domain&#32; &#91;&#32;owl:unionOf&#32;(&#32;aec3po:Document&#32;aec3po:DocumentSubdivision&#32;)&#32;]&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32;aec3po:document&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:range&#32;aec3po:DocumentSubdivision&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:subPropertyOf&#32;aec3po:hasSubdivision&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-80)|Pointer|<pre lang="Turtle"><code>aec3po:hasSubdivision&#32;a&#32;owl:ObjectProperty&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;has&#32;subdivision&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;links&#32;a&#32;document&#32;part&#32;to&#32;some&#32;of&#32;its&#32;subdivision&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:domain&#32; &#91;&#32;owl:unionOf&#32;(&#32;aec3po:Document&#32;aec3po:DocumentSubdivision&#32;)&#32;]&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32;aec3po:document&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:range&#32;aec3po:DocumentSubdivision&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:subPropertyOf&#32;dc:hasPart&#32;.</code></pre>|

***
### MinorFail Outcome number 81

[Jump to summary definition](#summary-MinorFail-81)	|	[Previous MinorFail outcome](#minorfail-outcome-number-80)	|	[Next MinorFail outcome](#minorfail-outcome-number-82)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-src-document|
|----|----|
|Title|Standalone&#32;module&#32;src/document.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Module document](https://github.com/Accord-Project/aec3po/blob/HEAD/src/document.ttl)|

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
|[Section top](#minorfail-outcome-number-81)|Description|Statement&#32;not&#32;supported&#32;in&#32;a&#32;Super&#32;Class&#32;Expression|
|[Section top](#minorfail-outcome-number-81)|Pointer|<pre lang="Turtle"><code>&#91;]&#32;owl:unionOf&#32;(&#32;aec3po:Document&#32;aec3po:DocumentSubdivision&#32;)&#32;.</code></pre>|

***
### MinorFail Outcome number 82

[Jump to summary definition](#summary-MinorFail-82)	|	[Previous MinorFail outcome](#minorfail-outcome-number-81)	|	[Next MinorFail outcome](#minorfail-outcome-number-83)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-src-compliance-verification-report|
|----|----|
|Title|Standalone&#32;module&#32;src/compliance&lowbar;verification&lowbar;report.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Module compliance&lowbar;verification&lowbar;report](https://github.com/Accord-Project/aec3po/blob/HEAD/src/compliance_verification_report.ttl)|

#### Criterion detail
|Identifier|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|
|----|----|
|Title|Profile&#32;compatibility&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;check&#32;whether&#32;the&#32;test&#32;subject&#32;is&#32;compatible&#32;with&#32;a&#32;profile&#32;or&#32;not,&#32;and&#32;if&#32;it&#32;is&#32;not,&#32;why.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-82)|Identifier|`owl-el-profile-error`|
|[Section top](#minorfail-outcome-number-82)|Title|OWL&#32;EL&#32;Profile&#32;incompatible|
|[Section top](#minorfail-outcome-number-82)|Description|Class&#32;Expression&#32;not&#32;supported&#32;with&#32;rdfs:subClassOf|
|[Section top](#minorfail-outcome-number-82)|Pointer|<pre lang="Turtle"><code>aec3po:ComplianceVerificationReport&#32;a&#32;owl:Class&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;Compliance&#32;Verification&#32;Report&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;Result&#32;of&#32;a&#32;checking&#32;act.&#32;May&#32;be&#32;compliant&#32;or&#32;not.&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32;aec3po:compliance&lowbar;verification&lowbar;report&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:subClassOf&#32; &#91;&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:onProperty&#32;aec3po:conforms&#32;]&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-82)|Pointer|<pre lang="Turtle"><code>aec3po:VerificationResult&#32;a&#32;owl:Class&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;Verification&#32;Result&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;Individual&#32;verification&#32;result&#32;of&#32;a&#32;Compliance&#32;Verification&#32;...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32;aec3po:compliance&lowbar;verification&lowbar;report&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:subClassOf&#32; &#91;&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:onProperty&#32;aec3po:verificationFocus&#32;],  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#91;&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:onProperty&#32;aec3po:hasSeverity&#32;]&#32;.</code></pre>|

***
### MinorFail Outcome number 83

[Jump to summary definition](#summary-MinorFail-83)	|	[Previous MinorFail outcome](#minorfail-outcome-number-82)	|	[Next MinorFail outcome](#minorfail-outcome-number-84)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-src-compliance-verification-report|
|----|----|
|Title|Standalone&#32;module&#32;src/compliance&lowbar;verification&lowbar;report.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Module compliance&lowbar;verification&lowbar;report](https://github.com/Accord-Project/aec3po/blob/HEAD/src/compliance_verification_report.ttl)|

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
|[Section top](#minorfail-outcome-number-83)|Description|Restriction&#32;on&#32;datatypes|
|[Section top](#minorfail-outcome-number-83)|Pointer|<pre lang="Turtle"><code>aec3po:conforms&#32;a&#32;owl:DatatypeProperty&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;conforms&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;True&#32;if&#32;the&#32;Checking&#32;act&#32;confirms&#32;the&#32;check&#32;was&#32;validated,&#32;a...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:domain&#32;aec3po:ComplianceVerificationReport&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32;aec3po:compliance&lowbar;verification&lowbar;report&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:range&#32;xsd:boolean&#32;.</code></pre>|

***
### MinorFail Outcome number 84

[Jump to summary definition](#summary-MinorFail-84)	|	[Previous MinorFail outcome](#minorfail-outcome-number-83)	|	[Next MinorFail outcome](#minorfail-outcome-number-85)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-src-compliance-verification-report|
|----|----|
|Title|Standalone&#32;module&#32;src/compliance&lowbar;verification&lowbar;report.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Module compliance&lowbar;verification&lowbar;report](https://github.com/Accord-Project/aec3po/blob/HEAD/src/compliance_verification_report.ttl)|

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
|[Section top](#minorfail-outcome-number-84)|Description|Statement&#32;not&#32;supported&#32;in&#32;a&#32;Class&#32;Expression|
|[Section top](#minorfail-outcome-number-84)|Pointer|<pre lang="Turtle"><code>&#91;]&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32;&#32; &#32;owl:onProperty&#32;aec3po:conforms&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-84)|Pointer|<pre lang="Turtle"><code>&#91;]&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32;&#32; &#32;owl:onProperty&#32;aec3po:verificationFocus&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-84)|Pointer|<pre lang="Turtle"><code>&#91;]&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32;&#32; &#32;owl:onProperty&#32;aec3po:hasSeverity&#32;.</code></pre>|

***
### MinorFail Outcome number 85

[Jump to summary definition](#summary-MinorFail-85)	|	[Previous MinorFail outcome](#minorfail-outcome-number-84)	|	[Next MinorFail outcome](#minorfail-outcome-number-86)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-src-compliance-verification-report|
|----|----|
|Title|Standalone&#32;module&#32;src/compliance&lowbar;verification&lowbar;report.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Module compliance&lowbar;verification&lowbar;report](https://github.com/Accord-Project/aec3po/blob/HEAD/src/compliance_verification_report.ttl)|

#### Criterion detail
|Identifier|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|
|----|----|
|Title|Profile&#32;compatibility&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;check&#32;whether&#32;the&#32;test&#32;subject&#32;is&#32;compatible&#32;with&#32;a&#32;profile&#32;or&#32;not,&#32;and&#32;if&#32;it&#32;is&#32;not,&#32;why.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-85)|Identifier|`owl-ql-profile-error`|
|[Section top](#minorfail-outcome-number-85)|Title|OWL&#32;QL&#32;Profile&#32;incompatible|
|[Section top](#minorfail-outcome-number-85)|Description|Class&#32;Expression&#32;not&#32;supported&#32;with&#32;rdfs:subClassOf|
|[Section top](#minorfail-outcome-number-85)|Pointer|<pre lang="Turtle"><code>aec3po:ComplianceVerificationReport&#32;a&#32;owl:Class&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;Compliance&#32;Verification&#32;Report&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;Result&#32;of&#32;a&#32;checking&#32;act.&#32;May&#32;be&#32;compliant&#32;or&#32;not.&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32;aec3po:compliance&lowbar;verification&lowbar;report&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:subClassOf&#32; &#91;&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:onProperty&#32;aec3po:conforms&#32;]&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-85)|Pointer|<pre lang="Turtle"><code>aec3po:VerificationResult&#32;a&#32;owl:Class&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;Verification&#32;Result&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;Individual&#32;verification&#32;result&#32;of&#32;a&#32;Compliance&#32;Verification&#32;...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32;aec3po:compliance&lowbar;verification&lowbar;report&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:subClassOf&#32; &#91;&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:onProperty&#32;aec3po:verificationFocus&#32;],  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#91;&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:onProperty&#32;aec3po:hasSeverity&#32;]&#32;.</code></pre>|

***
### MinorFail Outcome number 86

[Jump to summary definition](#summary-MinorFail-86)	|	[Previous MinorFail outcome](#minorfail-outcome-number-85)	|	[Next MinorFail outcome](#minorfail-outcome-number-87)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-src-compliance-verification-report|
|----|----|
|Title|Standalone&#32;module&#32;src/compliance&lowbar;verification&lowbar;report.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Module compliance&lowbar;verification&lowbar;report](https://github.com/Accord-Project/aec3po/blob/HEAD/src/compliance_verification_report.ttl)|

#### Criterion detail
|Identifier|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|
|----|----|
|Title|Profile&#32;compatibility&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;check&#32;whether&#32;the&#32;test&#32;subject&#32;is&#32;compatible&#32;with&#32;a&#32;profile&#32;or&#32;not,&#32;and&#32;if&#32;it&#32;is&#32;not,&#32;why.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-86)|Identifier|`owl-ql-profile-error`|
|[Section top](#minorfail-outcome-number-86)|Title|OWL&#32;QL&#32;Profile&#32;incompatible|
|[Section top](#minorfail-outcome-number-86)|Description|Restriction&#32;on&#32;datatypes|
|[Section top](#minorfail-outcome-number-86)|Pointer|<pre lang="Turtle"><code>aec3po:conforms&#32;a&#32;owl:DatatypeProperty&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;conforms&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;True&#32;if&#32;the&#32;Checking&#32;act&#32;confirms&#32;the&#32;check&#32;was&#32;validated,&#32;a...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:domain&#32;aec3po:ComplianceVerificationReport&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32;aec3po:compliance&lowbar;verification&lowbar;report&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:range&#32;xsd:boolean&#32;.</code></pre>|

***
### MinorFail Outcome number 87

[Jump to summary definition](#summary-MinorFail-87)	|	[Previous MinorFail outcome](#minorfail-outcome-number-86)	|	[Next MinorFail outcome](#minorfail-outcome-number-88)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-src-compliance-verification-report|
|----|----|
|Title|Standalone&#32;module&#32;src/compliance&lowbar;verification&lowbar;report.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Module compliance&lowbar;verification&lowbar;report](https://github.com/Accord-Project/aec3po/blob/HEAD/src/compliance_verification_report.ttl)|

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
|[Section top](#minorfail-outcome-number-87)|Description|Statement&#32;not&#32;supported&#32;in&#32;a&#32;Super&#32;Class&#32;Expression|
|[Section top](#minorfail-outcome-number-87)|Pointer|<pre lang="Turtle"><code>&#91;]&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32;&#32; &#32;owl:onProperty&#32;aec3po:conforms&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-87)|Pointer|<pre lang="Turtle"><code>&#91;]&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32;&#32; &#32;owl:onProperty&#32;aec3po:verificationFocus&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-87)|Pointer|<pre lang="Turtle"><code>&#91;]&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32;&#32; &#32;owl:onProperty&#32;aec3po:hasSeverity&#32;.</code></pre>|

***
### MinorFail Outcome number 88

[Jump to summary definition](#summary-MinorFail-88)	|	[Previous MinorFail outcome](#minorfail-outcome-number-87)	|	[Next MinorFail outcome](#minorfail-outcome-number-89)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-src-compliance-verification-report|
|----|----|
|Title|Standalone&#32;module&#32;src/compliance&lowbar;verification&lowbar;report.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Module compliance&lowbar;verification&lowbar;report](https://github.com/Accord-Project/aec3po/blob/HEAD/src/compliance_verification_report.ttl)|

#### Criterion detail
|Identifier|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|
|----|----|
|Title|Profile&#32;compatibility&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;check&#32;whether&#32;the&#32;test&#32;subject&#32;is&#32;compatible&#32;with&#32;a&#32;profile&#32;or&#32;not,&#32;and&#32;if&#32;it&#32;is&#32;not,&#32;why.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-88)|Identifier|`owl-rl-profile-error`|
|[Section top](#minorfail-outcome-number-88)|Title|OWL&#32;RL&#32;Profile&#32;incompatible|
|[Section top](#minorfail-outcome-number-88)|Description|Class&#32;Expression&#32;not&#32;supported&#32;with&#32;rdfs:subClassOf|
|[Section top](#minorfail-outcome-number-88)|Pointer|<pre lang="Turtle"><code>aec3po:ComplianceVerificationReport&#32;a&#32;owl:Class&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;Compliance&#32;Verification&#32;Report&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;Result&#32;of&#32;a&#32;checking&#32;act.&#32;May&#32;be&#32;compliant&#32;or&#32;not.&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32;aec3po:compliance&lowbar;verification&lowbar;report&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:subClassOf&#32; &#91;&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:onProperty&#32;aec3po:conforms&#32;]&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-88)|Pointer|<pre lang="Turtle"><code>aec3po:VerificationResult&#32;a&#32;owl:Class&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;Verification&#32;Result&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;Individual&#32;verification&#32;result&#32;of&#32;a&#32;Compliance&#32;Verification&#32;...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32;aec3po:compliance&lowbar;verification&lowbar;report&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:subClassOf&#32; &#91;&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:onProperty&#32;aec3po:verificationFocus&#32;],  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#91;&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:onProperty&#32;aec3po:hasSeverity&#32;]&#32;.</code></pre>|

***
### MinorFail Outcome number 89

[Jump to summary definition](#summary-MinorFail-89)	|	[Previous MinorFail outcome](#minorfail-outcome-number-88)	|	[Next MinorFail outcome](#minorfail-outcome-number-90)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-src-compliance-verification-report|
|----|----|
|Title|Standalone&#32;module&#32;src/compliance&lowbar;verification&lowbar;report.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Module compliance&lowbar;verification&lowbar;report](https://github.com/Accord-Project/aec3po/blob/HEAD/src/compliance_verification_report.ttl)|

#### Criterion detail
|Identifier|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|
|----|----|
|Title|Profile&#32;compatibility&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;check&#32;whether&#32;the&#32;test&#32;subject&#32;is&#32;compatible&#32;with&#32;a&#32;profile&#32;or&#32;not,&#32;and&#32;if&#32;it&#32;is&#32;not,&#32;why.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-89)|Identifier|`owl-rl-profile-error`|
|[Section top](#minorfail-outcome-number-89)|Title|OWL&#32;RL&#32;Profile&#32;incompatible|
|[Section top](#minorfail-outcome-number-89)|Description|Statement&#32;not&#32;supported&#32;in&#32;a&#32;Super&#32;Class&#32;Expression|
|[Section top](#minorfail-outcome-number-89)|Pointer|<pre lang="Turtle"><code>&#91;]&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32;&#32; &#32;owl:onProperty&#32;aec3po:conforms&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-89)|Pointer|<pre lang="Turtle"><code>&#91;]&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32;&#32; &#32;owl:onProperty&#32;aec3po:verificationFocus&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-89)|Pointer|<pre lang="Turtle"><code>&#91;]&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32;&#32; &#32;owl:onProperty&#32;aec3po:hasSeverity&#32;.</code></pre>|

***
### MinorFail Outcome number 90

[Jump to summary definition](#summary-MinorFail-90)	|	[Previous MinorFail outcome](#minorfail-outcome-number-89)	|	[Next MinorFail outcome](#minorfail-outcome-number-91)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-src-compliance-verification-report|
|----|----|
|Title|Standalone&#32;module&#32;src/compliance&lowbar;verification&lowbar;report.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Module compliance&lowbar;verification&lowbar;report](https://github.com/Accord-Project/aec3po/blob/HEAD/src/compliance_verification_report.ttl)|

#### Criterion detail
|Identifier|[terms-differenciation](https://ns.inria.fr/olivaw#terms-differenciation)|
|----|----|
|Title|Terms&#32;differenciation&#32;test|
|Description|A&#32;test&#32;case&#32;from&#32;the&#32;Best&#32;Practices&#32;tests&#32;checking&#32;if&#32;all&#32;the&#32;terms&#32;are&#32;different&#32;enough&#32;from&#32;each&#32;other&#32;according&#32;to&#32;the&#32;Levenshtein&#32;distance&#32;metric.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-90)|Identifier|`too-close-terms`|
|[Section top](#minorfail-outcome-number-90)|Title|Too&#32;close&#32;terms|
|[Section top](#minorfail-outcome-number-90)|Description|Some&#32;terms&#32;are&#32;too&#32;similar|
|[Section top](#minorfail-outcome-number-90)|Pointer|<pre lang="Turtle"><code>:severity&#32;a&#32;owl:ObjectProperty&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;severity&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;Each&#32;verification&#32;result&#32;has&#32;exactly&#32;one&#32;value&#32;for&#32;the&#32;prope...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:domain&#32;:VerificationResult&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32;:compliance&lowbar;verification&lowbar;report&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:range&#32;:Severity&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-90)|Pointer|<pre lang="Turtle"><code>:Severity&#32;a&#32;owl:Class&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;Severity&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;The&#32;class&#32;of&#32;validation&#32;result&#32;severity&#32;levels,&#32;including&#32;vi...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32;:compliance&lowbar;verification&lowbar;report&#32;.</code></pre>|

***
### MinorFail Outcome number 91

[Jump to summary definition](#summary-MinorFail-91)	|	[Previous MinorFail outcome](#minorfail-outcome-number-90)	|	[Next MinorFail outcome](#minorfail-outcome-number-92)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-src-checking-act|
|----|----|
|Title|Standalone&#32;module&#32;src/checking&lowbar;act.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Module checking&lowbar;act](https://github.com/Accord-Project/aec3po/blob/HEAD/src/checking_act.ttl)|

#### Criterion detail
|Identifier|[domain-and-range-referencing](https://ns.inria.fr/olivaw#domain-and-range-referencing)|
|----|----|
|Title|Domain&#32;and&#32;range&#32;referencing&#32;test|
|Description|A&#32;test&#32;case&#32;from&#32;the&#32;Best&#32;Practices&#32;tests&#32;checking&#32;if&#32;all&#32;the&#32;ranges&#32;and&#32;domains&#32;from&#32;the&#32;test&#32;subject&#32;point&#32;to&#32;terms&#32;that&#32;are&#32;defined&#32;in&#32;the&#32;vocabulary.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-91)|Identifier|`domain-out-of-vocabulary`|
|[Section top](#minorfail-outcome-number-91)|Title|Domain&#32;out&#32;of&#32;vocabulary|
|[Section top](#minorfail-outcome-number-91)|Description|Some&#32;properties&#32;have&#32;a&#32;domain&#32;out&#32;of&#32;the&#32;ontology|
|[Section top](#minorfail-outcome-number-91)|Pointer|<pre lang="Turtle"><code>:usedMethod&#32;a&#32;owl:ObjectProperty&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;used&#32;method&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;Links&#32;a&#32;checking&#32;act&#32;to&#32;the&#32;method&#32;it&#32;used&#32;(a&#32;aec3po:CheckMe...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:domain&#32; &#91;&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:onProperty&#32;:usedMethod&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:someValuesFrom&#32;:CheckMethod&#32;],  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#91;&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:onProperty&#32;:madeBy&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:someValuesFrom&#32;:ProcessVerifier&#32;],  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#91;&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:onProperty&#32;:checked&#32;],  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#91;&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:onProperty&#32;:hasReport&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:someValuesFrom&#32;:ComplianceVerificationReport&#32;],  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#60;http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#Event>,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;:CheckingAct&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32;:checking&lowbar;act&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:range&#32;:CheckMethod&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-91)|Pointer|<pre lang="Turtle"><code>http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#Event</code></pre>|
|[Section top](#minorfail-outcome-number-91)|Pointer|<pre lang="Turtle"><code>:madeBy&#32;a&#32;owl:ObjectProperty&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;made&#32;by&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;Links&#32;a&#32;checking&#32;act&#32;to&#32;the&#32;process&#32;verifier&#32;that&#32;made&#32;it&#32;(a...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:domain&#32; &#91;&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:onProperty&#32;:usedMethod&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:someValuesFrom&#32;:CheckMethod&#32;],  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#91;&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:onProperty&#32;:madeBy&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:someValuesFrom&#32;:ProcessVerifier&#32;],  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#91;&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:onProperty&#32;:checked&#32;],  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#91;&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:onProperty&#32;:hasReport&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:someValuesFrom&#32;:ComplianceVerificationReport&#32;],  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#60;http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#Event>,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;:CheckingAct&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32;:checking&lowbar;act&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:range&#32;:ProcessVerifier&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-91)|Pointer|<pre lang="Turtle"><code>:checked&#32;a&#32;owl:ObjectProperty&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;checked&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;Links&#32;a&#32;checking&#32;act&#32;to&#32;some&#32;entity&#32;(ex.&#32;statement,&#32;feature&#32;...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:domain&#32; &#91;&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:onProperty&#32;:usedMethod&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:someValuesFrom&#32;:CheckMethod&#32;],  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#91;&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:onProperty&#32;:madeBy&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:someValuesFrom&#32;:ProcessVerifier&#32;],  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#91;&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:onProperty&#32;:checked&#32;],  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#91;&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:onProperty&#32;:hasReport&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:someValuesFrom&#32;:ComplianceVerificationReport&#32;],  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#60;http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#Event>,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;:CheckingAct&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32;:checking&lowbar;act&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-91)|Pointer|<pre lang="Turtle"><code>:hasReport&#32;a&#32;owl:ObjectProperty&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;has&#32;report&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;Links&#32;a&#32;checking&#32;act&#32;to&#32;the&#32;resulting&#32;compliance&#32;verificatio...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:domain&#32; &#91;&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:onProperty&#32;:usedMethod&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:someValuesFrom&#32;:CheckMethod&#32;],  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#91;&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:onProperty&#32;:madeBy&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:someValuesFrom&#32;:ProcessVerifier&#32;],  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#91;&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:onProperty&#32;:checked&#32;],  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#91;&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:onProperty&#32;:hasReport&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:someValuesFrom&#32;:ComplianceVerificationReport&#32;],  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#60;http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#Event>,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;:CheckingAct&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32;:checking&lowbar;act&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:range&#32;:ComplianceVerificationReport&#32;.</code></pre>|

***
### MinorFail Outcome number 92

[Jump to summary definition](#summary-MinorFail-92)	|	[Previous MinorFail outcome](#minorfail-outcome-number-91)	|	[Next MinorFail outcome](#minorfail-outcome-number-93)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-src-checking-act|
|----|----|
|Title|Standalone&#32;module&#32;src/checking&lowbar;act.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Module checking&lowbar;act](https://github.com/Accord-Project/aec3po/blob/HEAD/src/checking_act.ttl)|

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
|[Section top](#minorfail-outcome-number-92)|Pointer|<pre lang="Turtle"><code>aec3po:CheckingAct&#32;a&#32;owl:Class&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;Checking&#32;Act&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;Act&#32;of&#32;checking&#32;some&#32;entities&#32;for&#32;something&#32;and&#32;generating&#32;a...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32;aec3po:checking&lowbar;act&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:subClassOf&#32; &#91;&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:onProperty&#32;aec3po:usedMethod&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:someValuesFrom&#32;aec3po:CheckMethod&#32;],  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#91;&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:onProperty&#32;aec3po:madeBy&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:someValuesFrom&#32;aec3po:ProcessVerifier&#32;],  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#91;&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:onProperty&#32;aec3po:checked&#32;],  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#91;&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:onProperty&#32;aec3po:hasReport&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:someValuesFrom&#32;aec3po:ComplianceVerificationReport&#32;],  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#60;http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#Event> &#32;.</code></pre>|

***
### MinorFail Outcome number 93

[Jump to summary definition](#summary-MinorFail-93)	|	[Previous MinorFail outcome](#minorfail-outcome-number-92)	|	[Next MinorFail outcome](#minorfail-outcome-number-94)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-src-checking-act|
|----|----|
|Title|Standalone&#32;module&#32;src/checking&lowbar;act.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Module checking&lowbar;act](https://github.com/Accord-Project/aec3po/blob/HEAD/src/checking_act.ttl)|

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
|[Section top](#minorfail-outcome-number-93)|Description|Statement&#32;not&#32;supported&#32;in&#32;a&#32;Super&#32;Class&#32;Expression|
|[Section top](#minorfail-outcome-number-93)|Pointer|<pre lang="Turtle"><code>&#91;]&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32;owl:onProperty&#32;aec3po:usedMethod&#32;;  &#10; &#32; &#32; &#32; &#32;owl:someValuesFrom&#32;aec3po:CheckMethod&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-93)|Pointer|<pre lang="Turtle"><code>&#91;]&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32;owl:onProperty&#32;aec3po:madeBy&#32;;  &#10; &#32; &#32; &#32; &#32;owl:someValuesFrom&#32;aec3po:ProcessVerifier&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-93)|Pointer|<pre lang="Turtle"><code>&#91;]&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32;&#32; &#32;owl:onProperty&#32;aec3po:checked&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-93)|Pointer|<pre lang="Turtle"><code>&#91;]&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32;owl:onProperty&#32;aec3po:hasReport&#32;;  &#10; &#32; &#32; &#32; &#32;owl:someValuesFrom&#32;aec3po:ComplianceVerificationReport&#32;.</code></pre>|

***
### MinorFail Outcome number 94

[Jump to summary definition](#summary-MinorFail-94)	|	[Previous MinorFail outcome](#minorfail-outcome-number-93)	|	[Next MinorFail outcome](#minorfail-outcome-number-95)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-src-check-method|
|----|----|
|Title|Standalone&#32;module&#32;src/check&lowbar;method.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Module check&lowbar;method](https://github.com/Accord-Project/aec3po/blob/HEAD/src/check_method.ttl)|

#### Criterion detail
|Identifier|[domain-and-range-referencing](https://ns.inria.fr/olivaw#domain-and-range-referencing)|
|----|----|
|Title|Domain&#32;and&#32;range&#32;referencing&#32;test|
|Description|A&#32;test&#32;case&#32;from&#32;the&#32;Best&#32;Practices&#32;tests&#32;checking&#32;if&#32;all&#32;the&#32;ranges&#32;and&#32;domains&#32;from&#32;the&#32;test&#32;subject&#32;point&#32;to&#32;terms&#32;that&#32;are&#32;defined&#32;in&#32;the&#32;vocabulary.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-94)|Identifier|`domain-out-of-vocabulary`|
|[Section top](#minorfail-outcome-number-94)|Title|Domain&#32;out&#32;of&#32;vocabulary|
|[Section top](#minorfail-outcome-number-94)|Description|Some&#32;properties&#32;have&#32;a&#32;domain&#32;out&#32;of&#32;the&#32;ontology|
|[Section top](#minorfail-outcome-number-94)|Pointer|<pre lang="Turtle"><code>:operationalizes&#32;a&#32;owl:ObjectProperty&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;operationalizes&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;Links&#32;a&#32;check&#32;method&#32;to&#32;a&#32;check&#32;statement&#32;in&#32;a&#32;document&#32;that...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:domain&#32; &#91;&#32;a&#32;owl:Class&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:unionOf&#32;(&#32;:FeatureOfInterest&#32;:Property&#32;:CheckMethod&#32;)&#32;],  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#60;http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#Method>,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;:CheckMethod&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32;:check&lowbar;method&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:range&#32;:CheckStatement&#32;;  &#10; &#32; &#32; &#32; &#32;owl:inverseOf&#32;:isOperationalizedBy&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-94)|Pointer|<pre lang="Turtle"><code>http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#Method</code></pre>|
|[Section top](#minorfail-outcome-number-94)|Pointer|<pre lang="Turtle"><code>:hasComparator&#32;a&#32;owl:ObjectProperty&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;has&#32;comparator&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;Links&#32;a&#32;numerical&#32;check&#32;method&#32;to&#32;the&#32;check&#32;method&#32;comparato...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:domain&#32; &#91;&#32;a&#32;owl:Class&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:unionOf&#32;(&#32;:FeatureOfInterest&#32;:Property&#32;:CheckMethod&#32;)&#32;],  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#60;http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#Method>,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;:CheckMethod,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;:NumericalCheckMethod&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32;:check&lowbar;method&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:range&#32;:CheckMethodComparator&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-94)|Pointer|<pre lang="Turtle"><code>:hasNestedValue&#32;a&#32;owl:ObjectProperty&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;hasNestedValue&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;TBD&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:domain&#32; &#91;&#32;a&#32;owl:Class&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:unionOf&#32;(&#32;:FeatureOfInterest&#32;:Property&#32;:CheckMethod&#32;)&#32;],  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#60;http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#Method>,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;:CheckMethod&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32;:check&lowbar;method&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-94)|Pointer|<pre lang="Turtle"><code>:hasOperator&#32;a&#32;owl:ObjectProperty&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;has&#32;operator&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;Links&#32;a&#32;boolean&#32;check&#32;method&#32;to&#32;the&#32;check&#32;method&#32;operator&#32;it...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:domain&#32; &#91;&#32;a&#32;owl:Class&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:unionOf&#32;(&#32;:FeatureOfInterest&#32;:Property&#32;:CheckMethod&#32;)&#32;],  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#60;http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#Method>,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;:BooleanCheckMethod,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;:CheckMethod&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32;:check&lowbar;method&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:range&#32;:CheckMethodOperator&#32;.</code></pre>|

***
### MinorFail Outcome number 95

[Jump to summary definition](#summary-MinorFail-95)	|	[Previous MinorFail outcome](#minorfail-outcome-number-94)	|	[Next MinorFail outcome](#minorfail-outcome-number-96)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-src-check-method|
|----|----|
|Title|Standalone&#32;module&#32;src/check&lowbar;method.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Module check&lowbar;method](https://github.com/Accord-Project/aec3po/blob/HEAD/src/check_method.ttl)|

#### Criterion detail
|Identifier|[domain-and-range-referencing](https://ns.inria.fr/olivaw#domain-and-range-referencing)|
|----|----|
|Title|Domain&#32;and&#32;range&#32;referencing&#32;test|
|Description|A&#32;test&#32;case&#32;from&#32;the&#32;Best&#32;Practices&#32;tests&#32;checking&#32;if&#32;all&#32;the&#32;ranges&#32;and&#32;domains&#32;from&#32;the&#32;test&#32;subject&#32;point&#32;to&#32;terms&#32;that&#32;are&#32;defined&#32;in&#32;the&#32;vocabulary.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-95)|Identifier|`range-out-of-vocabulary`|
|[Section top](#minorfail-outcome-number-95)|Title|Range&#32;out&#32;of&#32;vocabulary|
|[Section top](#minorfail-outcome-number-95)|Description|Some&#32;properties&#32;have&#32;a&#32;range&#32;out&#32;of&#32;the&#32;ontology|
|[Section top](#minorfail-outcome-number-95)|Pointer|<pre lang="Turtle"><code>:isOperationalizedBy&#32;a&#32;owl:ObjectProperty&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;is&#32;operationalized&#32;by&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;Links&#32;a&#32;check&#32;statement&#32;in&#32;a&#32;document&#32;to&#32;a&#32;check&#32;method&#32;that...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:domain&#32;:CheckStatement&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32;:check&lowbar;method&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:range&#32; &#91;&#32;a&#32;owl:Class&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:unionOf&#32;(&#32;:FeatureOfInterest&#32;:Property&#32;:CheckMethod&#32;)&#32;],  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#60;http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#Method>,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;:CheckMethod&#32;;  &#10; &#32; &#32; &#32; &#32;owl:inverseOf&#32;:operationalizes&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-95)|Pointer|<pre lang="Turtle"><code>http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#Method</code></pre>|
|[Section top](#minorfail-outcome-number-95)|Pointer|<pre lang="Turtle"><code>:hasUnit&#32;a&#32;owl:FunctionalProperty,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:ObjectProperty&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;hasUnit&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;the&#32;hasUnit&#32;property&#32;is&#32;used&#32;to&#32;link&#32;a&#32;specific&#32;property&#32;or&#32;...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:domain&#32; &#91;&#32;a&#32;owl:Class&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:unionOf&#32;(&#32;:FeatureOfInterest&#32;:Property&#32;:CheckMethod&#32;)&#32;]&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32;:check&lowbar;method&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:range&#32;qudt:Unit&#32;;  &#10; &#32; &#32; &#32; &#32;owl:eqivalentProperty&#32;qudt:hasValue&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-95)|Pointer|<pre lang="Turtle"><code>http://qudt.org/schema/qudt/Unit</code></pre>|
|[Section top](#minorfail-outcome-number-95)|Pointer|<pre lang="Turtle"><code>:hasNestedTarget&#32;a&#32;owl:ObjectProperty&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;hasNestedTarget&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32;:check&lowbar;method&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:range&#32; &#91;&#32;a&#32;owl:Class&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:unionOf&#32;(&#32;:FeatureOfInterest&#32;:Property&#32;:CheckMethod&#32;)&#32;],  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#60;http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#Method>,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;:CheckMethod&#32;.</code></pre>|

***
### MinorFail Outcome number 96

[Jump to summary definition](#summary-MinorFail-96)	|	[Previous MinorFail outcome](#minorfail-outcome-number-95)	|	[Next MinorFail outcome](#minorfail-outcome-number-97)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-src-check-method|
|----|----|
|Title|Standalone&#32;module&#32;src/check&lowbar;method.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Module check&lowbar;method](https://github.com/Accord-Project/aec3po/blob/HEAD/src/check_method.ttl)|

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
|[Section top](#minorfail-outcome-number-96)|Description|Class&#32;Expression&#32;not&#32;supported&#32;as&#32;object&#32;of&#32;rdfs:domain&#32;or&#32;rdfs:range|
|[Section top](#minorfail-outcome-number-96)|Pointer|<pre lang="Turtle"><code>aec3po:hasBSSDDTarget&#32;a&#32;owl:FunctionalProperty,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:ObjectProperty&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;hasBSSDDTarget&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;The&#32;target&#32;refers&#32;to&#32;either&#32;the&#32;name&#32;of&#32;an&#32;object,&#32;the&#32;name&#32;...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:domain&#32; &#91;&#32;a&#32;owl:Class&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:unionOf&#32;(&#32;aec3po:FeatureOfInterest&#32;aec3po:Property&#32;aec3po:CheckMethod&#32;)&#32;]&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32;aec3po:check&lowbar;method&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-96)|Pointer|<pre lang="Turtle"><code>aec3po:hasUnit&#32;a&#32;owl:FunctionalProperty,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:ObjectProperty&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;hasUnit&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;the&#32;hasUnit&#32;property&#32;is&#32;used&#32;to&#32;link&#32;a&#32;specific&#32;property&#32;or&#32;...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:domain&#32; &#91;&#32;a&#32;owl:Class&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:unionOf&#32;(&#32;aec3po:FeatureOfInterest&#32;aec3po:Property&#32;aec3po:CheckMethod&#32;)&#32;]&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32;aec3po:check&lowbar;method&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:range&#32;qudt:Unit&#32;;  &#10; &#32; &#32; &#32; &#32;owl:eqivalentProperty&#32;qudt:hasValue&#32;.</code></pre>|

***
### MinorFail Outcome number 97

[Jump to summary definition](#summary-MinorFail-97)	|	[Previous MinorFail outcome](#minorfail-outcome-number-96)	|	[Next MinorFail outcome](#minorfail-outcome-number-98)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-src-check-method|
|----|----|
|Title|Standalone&#32;module&#32;src/check&lowbar;method.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Module check&lowbar;method](https://github.com/Accord-Project/aec3po/blob/HEAD/src/check_method.ttl)|

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
|[Section top](#minorfail-outcome-number-97)|Description|Class&#32;Expression&#32;not&#32;supported&#32;with&#32;owl:equivalentClass|
|[Section top](#minorfail-outcome-number-97)|Pointer|<pre lang="Turtle"><code>aec3po:ComponentCheckMethod&#32;a&#32;owl:Class&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;Component&#32;Check&#32;Method&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;Component&#32;check&#32;method&#32;refers&#32;to&#32;a&#32;process&#32;of&#32;inspecting&#32;and...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32;aec3po:check&lowbar;method&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:subClassOf&#32;aec3po:CheckMethod&#32;;  &#10; &#32; &#32; &#32; &#32;owl:equivalentClass&#32; &#91;&#32;a&#32;owl:Class&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:intersectionOf&#32;(&#32;aec3po:CheckMethod&#32; &#91;&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:allValuesFrom&#32; &#91;&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:allValuesFrom&#32;aec3po:FeatureOfInterest&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:onProperty&#32; &#91;&#32;owl:inverseOf&#32;aec3po:forDesign&#32;]&#32;]&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:onProperty&#32;aec3po:forDesign&#32;]&#32;)&#32;]&#32;.</code></pre>|

***
### MinorFail Outcome number 98

[Jump to summary definition](#summary-MinorFail-98)	|	[Previous MinorFail outcome](#minorfail-outcome-number-97)	|	[Next MinorFail outcome](#minorfail-outcome-number-99)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-src-check-method|
|----|----|
|Title|Standalone&#32;module&#32;src/check&lowbar;method.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Module check&lowbar;method](https://github.com/Accord-Project/aec3po/blob/HEAD/src/check_method.ttl)|

#### Criterion detail
|Identifier|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|
|----|----|
|Title|Profile&#32;compatibility&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;check&#32;whether&#32;the&#32;test&#32;subject&#32;is&#32;compatible&#32;with&#32;a&#32;profile&#32;or&#32;not,&#32;and&#32;if&#32;it&#32;is&#32;not,&#32;why.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-98)|Identifier|`owl-el-profile-error`|
|[Section top](#minorfail-outcome-number-98)|Title|OWL&#32;EL&#32;Profile&#32;incompatible|
|[Section top](#minorfail-outcome-number-98)|Description|Restriction&#32;on&#32;datatypes|
|[Section top](#minorfail-outcome-number-98)|Pointer|<pre lang="Turtle"><code>aec3po:hasBooleanTarget&#32;a&#32;owl:DatatypeProperty&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;hasBooleanTarget&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;TBD&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:range&#32;xsd:boolean&#32;.</code></pre>|

***
### MinorFail Outcome number 99

[Jump to summary definition](#summary-MinorFail-99)	|	[Previous MinorFail outcome](#minorfail-outcome-number-98)	|	[Next MinorFail outcome](#minorfail-outcome-number-100)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-src-check-method|
|----|----|
|Title|Standalone&#32;module&#32;src/check&lowbar;method.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Module check&lowbar;method](https://github.com/Accord-Project/aec3po/blob/HEAD/src/check_method.ttl)|

#### Criterion detail
|Identifier|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|
|----|----|
|Title|Profile&#32;compatibility&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;check&#32;whether&#32;the&#32;test&#32;subject&#32;is&#32;compatible&#32;with&#32;a&#32;profile&#32;or&#32;not,&#32;and&#32;if&#32;it&#32;is&#32;not,&#32;why.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-99)|Identifier|`owl-el-profile-error`|
|[Section top](#minorfail-outcome-number-99)|Title|OWL&#32;EL&#32;Profile&#32;incompatible|
|[Section top](#minorfail-outcome-number-99)|Description|Statement&#32;not&#32;supported&#32;in&#32;a&#32;Class&#32;Expression|
|[Section top](#minorfail-outcome-number-99)|Pointer|<pre lang="Turtle"><code>&#91;]&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32;owl:allValuesFrom&#32; &#91;&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:allValuesFrom&#32;aec3po:FeatureOfInterest&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:onProperty&#32; &#91;&#32;owl:inverseOf&#32;aec3po:forDesign&#32;]&#32;]&#32;;  &#10; &#32; &#32; &#32; &#32;owl:onProperty&#32;aec3po:forDesign&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-99)|Pointer|<pre lang="Turtle"><code>&#91;]&#32;a&#32;owl:Class&#32;;  &#10; &#32; &#32;&#32; &#32;owl:unionOf&#32;(&#32;aec3po:FeatureOfInterest&#32;aec3po:Property&#32;aec3po:CheckMethod&#32;)&#32;.</code></pre>|

***
### MinorFail Outcome number 100

[Jump to summary definition](#summary-MinorFail-100)	|	[Previous MinorFail outcome](#minorfail-outcome-number-99)	|	[Next MinorFail outcome](#minorfail-outcome-number-101)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-src-check-method|
|----|----|
|Title|Standalone&#32;module&#32;src/check&lowbar;method.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Module check&lowbar;method](https://github.com/Accord-Project/aec3po/blob/HEAD/src/check_method.ttl)|

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
|[Section top](#minorfail-outcome-number-100)|Description|Class&#32;Expression&#32;not&#32;supported&#32;as&#32;object&#32;of&#32;rdfs:domain&#32;or&#32;rdfs:range|
|[Section top](#minorfail-outcome-number-100)|Pointer|<pre lang="Turtle"><code>aec3po:hasBSSDDTarget&#32;a&#32;owl:FunctionalProperty,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:ObjectProperty&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;hasBSSDDTarget&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;The&#32;target&#32;refers&#32;to&#32;either&#32;the&#32;name&#32;of&#32;an&#32;object,&#32;the&#32;name&#32;...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:domain&#32; &#91;&#32;a&#32;owl:Class&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:unionOf&#32;(&#32;aec3po:FeatureOfInterest&#32;aec3po:Property&#32;aec3po:CheckMethod&#32;)&#32;]&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32;aec3po:check&lowbar;method&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-100)|Pointer|<pre lang="Turtle"><code>aec3po:hasUnit&#32;a&#32;owl:FunctionalProperty,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:ObjectProperty&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;hasUnit&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;the&#32;hasUnit&#32;property&#32;is&#32;used&#32;to&#32;link&#32;a&#32;specific&#32;property&#32;or&#32;...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:domain&#32; &#91;&#32;a&#32;owl:Class&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:unionOf&#32;(&#32;aec3po:FeatureOfInterest&#32;aec3po:Property&#32;aec3po:CheckMethod&#32;)&#32;]&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32;aec3po:check&lowbar;method&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:range&#32;qudt:Unit&#32;;  &#10; &#32; &#32; &#32; &#32;owl:eqivalentProperty&#32;qudt:hasValue&#32;.</code></pre>|

***
### MinorFail Outcome number 101

[Jump to summary definition](#summary-MinorFail-101)	|	[Previous MinorFail outcome](#minorfail-outcome-number-100)	|	[Next MinorFail outcome](#minorfail-outcome-number-102)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-src-check-method|
|----|----|
|Title|Standalone&#32;module&#32;src/check&lowbar;method.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Module check&lowbar;method](https://github.com/Accord-Project/aec3po/blob/HEAD/src/check_method.ttl)|

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
|[Section top](#minorfail-outcome-number-101)|Description|Class&#32;Expression&#32;not&#32;supported&#32;with&#32;owl:equivalentClass|
|[Section top](#minorfail-outcome-number-101)|Pointer|<pre lang="Turtle"><code>aec3po:ComponentCheckMethod&#32;a&#32;owl:Class&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;Component&#32;Check&#32;Method&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;Component&#32;check&#32;method&#32;refers&#32;to&#32;a&#32;process&#32;of&#32;inspecting&#32;and...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32;aec3po:check&lowbar;method&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:subClassOf&#32;aec3po:CheckMethod&#32;;  &#10; &#32; &#32; &#32; &#32;owl:equivalentClass&#32; &#91;&#32;a&#32;owl:Class&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:intersectionOf&#32;(&#32;aec3po:CheckMethod&#32; &#91;&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:allValuesFrom&#32; &#91;&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:allValuesFrom&#32;aec3po:FeatureOfInterest&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:onProperty&#32; &#91;&#32;owl:inverseOf&#32;aec3po:forDesign&#32;]&#32;]&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:onProperty&#32;aec3po:forDesign&#32;]&#32;)&#32;]&#32;.</code></pre>|

***
### MinorFail Outcome number 102

[Jump to summary definition](#summary-MinorFail-102)	|	[Previous MinorFail outcome](#minorfail-outcome-number-101)	|	[Next MinorFail outcome](#minorfail-outcome-number-103)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-src-check-method|
|----|----|
|Title|Standalone&#32;module&#32;src/check&lowbar;method.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Module check&lowbar;method](https://github.com/Accord-Project/aec3po/blob/HEAD/src/check_method.ttl)|

#### Criterion detail
|Identifier|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|
|----|----|
|Title|Profile&#32;compatibility&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;check&#32;whether&#32;the&#32;test&#32;subject&#32;is&#32;compatible&#32;with&#32;a&#32;profile&#32;or&#32;not,&#32;and&#32;if&#32;it&#32;is&#32;not,&#32;why.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-102)|Identifier|`owl-ql-profile-error`|
|[Section top](#minorfail-outcome-number-102)|Title|OWL&#32;QL&#32;Profile&#32;incompatible|
|[Section top](#minorfail-outcome-number-102)|Description|Restriction&#32;on&#32;datatypes|
|[Section top](#minorfail-outcome-number-102)|Pointer|<pre lang="Turtle"><code>aec3po:hasBooleanTarget&#32;a&#32;owl:DatatypeProperty&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;hasBooleanTarget&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;TBD&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:range&#32;xsd:boolean&#32;.</code></pre>|

***
### MinorFail Outcome number 103

[Jump to summary definition](#summary-MinorFail-103)	|	[Previous MinorFail outcome](#minorfail-outcome-number-102)	|	[Next MinorFail outcome](#minorfail-outcome-number-104)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-src-check-method|
|----|----|
|Title|Standalone&#32;module&#32;src/check&lowbar;method.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Module check&lowbar;method](https://github.com/Accord-Project/aec3po/blob/HEAD/src/check_method.ttl)|

#### Criterion detail
|Identifier|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|
|----|----|
|Title|Profile&#32;compatibility&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;check&#32;whether&#32;the&#32;test&#32;subject&#32;is&#32;compatible&#32;with&#32;a&#32;profile&#32;or&#32;not,&#32;and&#32;if&#32;it&#32;is&#32;not,&#32;why.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-103)|Identifier|`owl-ql-profile-error`|
|[Section top](#minorfail-outcome-number-103)|Title|OWL&#32;QL&#32;Profile&#32;incompatible|
|[Section top](#minorfail-outcome-number-103)|Description|Statement&#32;not&#32;supported&#32;in&#32;a&#32;Sub&#32;Class&#32;Expression|
|[Section top](#minorfail-outcome-number-103)|Pointer|<pre lang="Turtle"><code>&#91;]&#32;a&#32;owl:Class&#32;;  &#10; &#32; &#32; &#32; &#32;owl:intersectionOf&#32;(&#32;aec3po:CheckMethod&#32; &#91;&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:allValuesFrom&#32; &#91;&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:allValuesFrom&#32;aec3po:FeatureOfInterest&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:onProperty&#32; &#91;&#32;owl:inverseOf&#32;aec3po:forDesign&#32;]&#32;]&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:onProperty&#32;aec3po:forDesign&#32;]&#32;)&#32;.</code></pre>|

***
### MinorFail Outcome number 104

[Jump to summary definition](#summary-MinorFail-104)	|	[Previous MinorFail outcome](#minorfail-outcome-number-103)	|	[Next MinorFail outcome](#minorfail-outcome-number-105)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-src-check-method|
|----|----|
|Title|Standalone&#32;module&#32;src/check&lowbar;method.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Module check&lowbar;method](https://github.com/Accord-Project/aec3po/blob/HEAD/src/check_method.ttl)|

#### Criterion detail
|Identifier|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|
|----|----|
|Title|Profile&#32;compatibility&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;check&#32;whether&#32;the&#32;test&#32;subject&#32;is&#32;compatible&#32;with&#32;a&#32;profile&#32;or&#32;not,&#32;and&#32;if&#32;it&#32;is&#32;not,&#32;why.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-104)|Identifier|`owl-ql-profile-error`|
|[Section top](#minorfail-outcome-number-104)|Title|OWL&#32;QL&#32;Profile&#32;incompatible|
|[Section top](#minorfail-outcome-number-104)|Description|Statement&#32;not&#32;supported&#32;in&#32;a&#32;Super&#32;Class&#32;Expression|
|[Section top](#minorfail-outcome-number-104)|Pointer|<pre lang="Turtle"><code>&#91;]&#32;a&#32;owl:Class&#32;;  &#10; &#32; &#32;&#32; &#32;owl:unionOf&#32;(&#32;aec3po:FeatureOfInterest&#32;aec3po:Property&#32;aec3po:CheckMethod&#32;)&#32;.</code></pre>|

***
### MinorFail Outcome number 105

[Jump to summary definition](#summary-MinorFail-105)	|	[Previous MinorFail outcome](#minorfail-outcome-number-104)	|	[Next MinorFail outcome](#minorfail-outcome-number-106)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-src-check-method|
|----|----|
|Title|Standalone&#32;module&#32;src/check&lowbar;method.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Module check&lowbar;method](https://github.com/Accord-Project/aec3po/blob/HEAD/src/check_method.ttl)|

#### Criterion detail
|Identifier|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|
|----|----|
|Title|Profile&#32;compatibility&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;check&#32;whether&#32;the&#32;test&#32;subject&#32;is&#32;compatible&#32;with&#32;a&#32;profile&#32;or&#32;not,&#32;and&#32;if&#32;it&#32;is&#32;not,&#32;why.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-105)|Identifier|`owl-rl-profile-error`|
|[Section top](#minorfail-outcome-number-105)|Title|OWL&#32;RL&#32;Profile&#32;incompatible|
|[Section top](#minorfail-outcome-number-105)|Description|Class&#32;Expression&#32;not&#32;supported&#32;as&#32;object&#32;of&#32;rdfs:domain&#32;or&#32;rdfs:range|
|[Section top](#minorfail-outcome-number-105)|Pointer|<pre lang="Turtle"><code>aec3po:hasBSSDDTarget&#32;a&#32;owl:FunctionalProperty,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:ObjectProperty&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;hasBSSDDTarget&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;The&#32;target&#32;refers&#32;to&#32;either&#32;the&#32;name&#32;of&#32;an&#32;object,&#32;the&#32;name&#32;...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:domain&#32; &#91;&#32;a&#32;owl:Class&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:unionOf&#32;(&#32;aec3po:FeatureOfInterest&#32;aec3po:Property&#32;aec3po:CheckMethod&#32;)&#32;]&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32;aec3po:check&lowbar;method&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-105)|Pointer|<pre lang="Turtle"><code>aec3po:hasUnit&#32;a&#32;owl:FunctionalProperty,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:ObjectProperty&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;hasUnit&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;the&#32;hasUnit&#32;property&#32;is&#32;used&#32;to&#32;link&#32;a&#32;specific&#32;property&#32;or&#32;...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:domain&#32; &#91;&#32;a&#32;owl:Class&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:unionOf&#32;(&#32;aec3po:FeatureOfInterest&#32;aec3po:Property&#32;aec3po:CheckMethod&#32;)&#32;]&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32;aec3po:check&lowbar;method&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:range&#32;qudt:Unit&#32;;  &#10; &#32; &#32; &#32; &#32;owl:eqivalentProperty&#32;qudt:hasValue&#32;.</code></pre>|

***
### MinorFail Outcome number 106

[Jump to summary definition](#summary-MinorFail-106)	|	[Previous MinorFail outcome](#minorfail-outcome-number-105)	|	[Next MinorFail outcome](#minorfail-outcome-number-107)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-src-check-method|
|----|----|
|Title|Standalone&#32;module&#32;src/check&lowbar;method.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Module check&lowbar;method](https://github.com/Accord-Project/aec3po/blob/HEAD/src/check_method.ttl)|

#### Criterion detail
|Identifier|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|
|----|----|
|Title|Profile&#32;compatibility&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;check&#32;whether&#32;the&#32;test&#32;subject&#32;is&#32;compatible&#32;with&#32;a&#32;profile&#32;or&#32;not,&#32;and&#32;if&#32;it&#32;is&#32;not,&#32;why.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-106)|Identifier|`owl-rl-profile-error`|
|[Section top](#minorfail-outcome-number-106)|Title|OWL&#32;RL&#32;Profile&#32;incompatible|
|[Section top](#minorfail-outcome-number-106)|Description|Class&#32;Expression&#32;not&#32;supported&#32;with&#32;owl:equivalentClass|
|[Section top](#minorfail-outcome-number-106)|Pointer|<pre lang="Turtle"><code>aec3po:ComponentCheckMethod&#32;a&#32;owl:Class&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;Component&#32;Check&#32;Method&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;Component&#32;check&#32;method&#32;refers&#32;to&#32;a&#32;process&#32;of&#32;inspecting&#32;and...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32;aec3po:check&lowbar;method&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:subClassOf&#32;aec3po:CheckMethod&#32;;  &#10; &#32; &#32; &#32; &#32;owl:equivalentClass&#32; &#91;&#32;a&#32;owl:Class&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:intersectionOf&#32;(&#32;aec3po:CheckMethod&#32; &#91;&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:allValuesFrom&#32; &#91;&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:allValuesFrom&#32;aec3po:FeatureOfInterest&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:onProperty&#32; &#91;&#32;owl:inverseOf&#32;aec3po:forDesign&#32;]&#32;]&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:onProperty&#32;aec3po:forDesign&#32;]&#32;)&#32;]&#32;.</code></pre>|

***
### MinorFail Outcome number 107

[Jump to summary definition](#summary-MinorFail-107)	|	[Previous MinorFail outcome](#minorfail-outcome-number-106)	|	[Next MinorFail outcome](#minorfail-outcome-number-108)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-src-check-method|
|----|----|
|Title|Standalone&#32;module&#32;src/check&lowbar;method.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Module check&lowbar;method](https://github.com/Accord-Project/aec3po/blob/HEAD/src/check_method.ttl)|

#### Criterion detail
|Identifier|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|
|----|----|
|Title|Profile&#32;compatibility&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;check&#32;whether&#32;the&#32;test&#32;subject&#32;is&#32;compatible&#32;with&#32;a&#32;profile&#32;or&#32;not,&#32;and&#32;if&#32;it&#32;is&#32;not,&#32;why.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-107)|Identifier|`owl-rl-profile-error`|
|[Section top](#minorfail-outcome-number-107)|Title|OWL&#32;RL&#32;Profile&#32;incompatible|
|[Section top](#minorfail-outcome-number-107)|Description|Class&#32;Expression&#32;not&#32;supported&#32;with&#32;owl:equivalentClass&#32;or&#32;owl:intersectionOf|
|[Section top](#minorfail-outcome-number-107)|Pointer|<pre lang="Turtle"><code>&#91;]&#32;a&#32;owl:Class&#32;;  &#10; &#32; &#32; &#32; &#32;owl:intersectionOf&#32;(&#32;aec3po:CheckMethod&#32; &#91;&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:allValuesFrom&#32; &#91;&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:allValuesFrom&#32;aec3po:FeatureOfInterest&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:onProperty&#32; &#91;&#32;owl:inverseOf&#32;aec3po:forDesign&#32;]&#32;]&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:onProperty&#32;aec3po:forDesign&#32;]&#32;)&#32;.</code></pre>|

***
### MinorFail Outcome number 108

[Jump to summary definition](#summary-MinorFail-108)	|	[Previous MinorFail outcome](#minorfail-outcome-number-107)	|	[Next MinorFail outcome](#minorfail-outcome-number-109)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-src-check-method|
|----|----|
|Title|Standalone&#32;module&#32;src/check&lowbar;method.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Module check&lowbar;method](https://github.com/Accord-Project/aec3po/blob/HEAD/src/check_method.ttl)|

#### Criterion detail
|Identifier|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|
|----|----|
|Title|Profile&#32;compatibility&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;check&#32;whether&#32;the&#32;test&#32;subject&#32;is&#32;compatible&#32;with&#32;a&#32;profile&#32;or&#32;not,&#32;and&#32;if&#32;it&#32;is&#32;not,&#32;why.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-108)|Identifier|`owl-rl-profile-error`|
|[Section top](#minorfail-outcome-number-108)|Title|OWL&#32;RL&#32;Profile&#32;incompatible|
|[Section top](#minorfail-outcome-number-108)|Description|Statement&#32;not&#32;supported&#32;in&#32;a&#32;Super&#32;Class&#32;Expression|
|[Section top](#minorfail-outcome-number-108)|Pointer|<pre lang="Turtle"><code>&#91;]&#32;a&#32;owl:Class&#32;;  &#10; &#32; &#32;&#32; &#32;owl:unionOf&#32;(&#32;aec3po:FeatureOfInterest&#32;aec3po:Property&#32;aec3po:CheckMethod&#32;)&#32;.</code></pre>|

***
### MinorFail Outcome number 109

[Jump to summary definition](#summary-MinorFail-109)	|	[Previous MinorFail outcome](#minorfail-outcome-number-108)	|	[Next MinorFail outcome](#minorfail-outcome-number-110)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-src-check-method|
|----|----|
|Title|Standalone&#32;module&#32;src/check&lowbar;method.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Module check&lowbar;method](https://github.com/Accord-Project/aec3po/blob/HEAD/src/check_method.ttl)|

#### Criterion detail
|Identifier|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|
|----|----|
|Title|Profile&#32;compatibility&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;check&#32;whether&#32;the&#32;test&#32;subject&#32;is&#32;compatible&#32;with&#32;a&#32;profile&#32;or&#32;not,&#32;and&#32;if&#32;it&#32;is&#32;not,&#32;why.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-109)|Identifier|`owl-rl-profile-error`|
|[Section top](#minorfail-outcome-number-109)|Title|OWL&#32;RL&#32;Profile&#32;incompatible|
|[Section top](#minorfail-outcome-number-109)|Description|Statement&#32;not&#32;supported&#32;in&#32;an&#32;Equivalent&#32;Class&#32;Expression|
|[Section top](#minorfail-outcome-number-109)|Pointer|<pre lang="Turtle"><code>&#91;]&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32;owl:allValuesFrom&#32; &#91;&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:allValuesFrom&#32;aec3po:FeatureOfInterest&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:onProperty&#32; &#91;&#32;owl:inverseOf&#32;aec3po:forDesign&#32;]&#32;]&#32;;  &#10; &#32; &#32; &#32; &#32;owl:onProperty&#32;aec3po:forDesign&#32;.</code></pre>|

***
### MinorFail Outcome number 110

[Jump to summary definition](#summary-MinorFail-110)	|	[Previous MinorFail outcome](#minorfail-outcome-number-109)	|	[Next MinorFail outcome](#minorfail-outcome-number-111)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-src-check-method|
|----|----|
|Title|Standalone&#32;module&#32;src/check&lowbar;method.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Module check&lowbar;method](https://github.com/Accord-Project/aec3po/blob/HEAD/src/check_method.ttl)|

#### Criterion detail
|Identifier|[term-referencing](https://ns.inria.fr/olivaw#term-referencing)|
|----|----|
|Title|Term&#32;referencing&#32;test|
|Description|A&#32;test&#32;case&#32;from&#32;the&#32;Best&#32;Practices&#32;tests&#32;checking&#32;if&#32;each&#32;term&#32;of&#32;the&#32;test&#32;subject&#32;is&#32;referenced&#32;to&#32;a&#32;module&#32;through&#32;a&#32;rdfs:isDefinedBy&#32;property.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-110)|Identifier|`no-reference-module`|
|[Section top](#minorfail-outcome-number-110)|Title|Term&#32;not&#32;referenced&#32;to&#32;a&#32;module|
|[Section top](#minorfail-outcome-number-110)|Description|Subject&#32;terms&#32;not&#32;linked&#32;to&#32;a&#32;module&#32;by&#32;a&#32;rdfs:isDefinedBy&#32;property|
|[Section top](#minorfail-outcome-number-110)|Pointer|<pre lang="Turtle"><code>:hasTarget&#32;a&#32;owl:DatatypeProperty&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;hasTarget&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;TBD&#34;@en&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-110)|Pointer|<pre lang="Turtle"><code>:hasBooleanTarget&#32;a&#32;owl:DatatypeProperty&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;hasBooleanTarget&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;TBD&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:range&#32;xsd:boolean&#32;.</code></pre>|

***
### MinorFail Outcome number 111

[Jump to summary definition](#summary-MinorFail-111)	|	[Previous MinorFail outcome](#minorfail-outcome-number-110)	|	[Next MinorFail outcome](#minorfail-outcome-number-112)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-src-aec3po|
|----|----|
|Title|Standalone&#32;module&#32;src/aec3po.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Module aec3po](https://github.com/Accord-Project/aec3po/blob/HEAD/src/aec3po.ttl)|

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
|[Section top](#minorfail-outcome-number-111)|Description|Class&#32;Expression&#32;not&#32;supported&#32;as&#32;object&#32;of&#32;rdfs:domain&#32;or&#32;rdfs:range|
|[Section top](#minorfail-outcome-number-111)|Pointer|<pre lang="Turtle"><code>aec3po:hasValue&#32;a&#32;owl:DatatypeProperty,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:FunctionalProperty&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;has&#32;value&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;de&#32;facto&#32;used&#32;to&#32;link&#32;something&#32;(anything:&#32;property,&#32;propert...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:domain&#32; &#91;&#32;a&#32;owl:Class&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:unionOf&#32;(&#32;aec3po:FeatureOfInterest&#32;aec3po:Property&#32;aec3po:CheckMethod&#32;)&#32;]&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32;aec3po:&#32;;  &#10; &#32; &#32; &#32; &#32;skos:note&#32; &#34;The&#32;value&#32;of&#32;the&#32;literal&#32;may&#32;be&#32;a&#32;XSD&#32;literal&#32;(boolean,&#32;inte...&#34; &#32;.</code></pre>|

***
### MinorFail Outcome number 112

[Jump to summary definition](#summary-MinorFail-112)	|	[Previous MinorFail outcome](#minorfail-outcome-number-111)	|	[Next MinorFail outcome](#minorfail-outcome-number-113)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-src-aec3po|
|----|----|
|Title|Standalone&#32;module&#32;src/aec3po.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Module aec3po](https://github.com/Accord-Project/aec3po/blob/HEAD/src/aec3po.ttl)|

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
|[Section top](#minorfail-outcome-number-112)|Pointer|<pre lang="Turtle"><code>&#91;]&#32;a&#32;owl:Class&#32;;  &#10; &#32; &#32;&#32; &#32;owl:unionOf&#32;(&#32;aec3po:FeatureOfInterest&#32;aec3po:Property&#32;aec3po:CheckMethod&#32;)&#32;.</code></pre>|

***
### MinorFail Outcome number 113

[Jump to summary definition](#summary-MinorFail-113)	|	[Previous MinorFail outcome](#minorfail-outcome-number-112)	|	[Next MinorFail outcome](#minorfail-outcome-number-114)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-src-aec3po|
|----|----|
|Title|Standalone&#32;module&#32;src/aec3po.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Module aec3po](https://github.com/Accord-Project/aec3po/blob/HEAD/src/aec3po.ttl)|

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
|[Section top](#minorfail-outcome-number-113)|Description|Class&#32;Expression&#32;not&#32;supported&#32;as&#32;object&#32;of&#32;rdfs:domain&#32;or&#32;rdfs:range|
|[Section top](#minorfail-outcome-number-113)|Pointer|<pre lang="Turtle"><code>aec3po:hasValue&#32;a&#32;owl:DatatypeProperty,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:FunctionalProperty&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;has&#32;value&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;de&#32;facto&#32;used&#32;to&#32;link&#32;something&#32;(anything:&#32;property,&#32;propert...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:domain&#32; &#91;&#32;a&#32;owl:Class&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:unionOf&#32;(&#32;aec3po:FeatureOfInterest&#32;aec3po:Property&#32;aec3po:CheckMethod&#32;)&#32;]&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32;aec3po:&#32;;  &#10; &#32; &#32; &#32; &#32;skos:note&#32; &#34;The&#32;value&#32;of&#32;the&#32;literal&#32;may&#32;be&#32;a&#32;XSD&#32;literal&#32;(boolean,&#32;inte...&#34; &#32;.</code></pre>|

***
### MinorFail Outcome number 114

[Jump to summary definition](#summary-MinorFail-114)	|	[Previous MinorFail outcome](#minorfail-outcome-number-113)	|	[Next MinorFail outcome](#minorfail-outcome-number-115)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-src-aec3po|
|----|----|
|Title|Standalone&#32;module&#32;src/aec3po.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Module aec3po](https://github.com/Accord-Project/aec3po/blob/HEAD/src/aec3po.ttl)|

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
|[Section top](#minorfail-outcome-number-114)|Description|Statement&#32;not&#32;supported&#32;in&#32;a&#32;Super&#32;Class&#32;Expression|
|[Section top](#minorfail-outcome-number-114)|Pointer|<pre lang="Turtle"><code>&#91;]&#32;a&#32;owl:Class&#32;;  &#10; &#32; &#32;&#32; &#32;owl:unionOf&#32;(&#32;aec3po:FeatureOfInterest&#32;aec3po:Property&#32;aec3po:CheckMethod&#32;)&#32;.</code></pre>|

***
### MinorFail Outcome number 115

[Jump to summary definition](#summary-MinorFail-115)	|	[Previous MinorFail outcome](#minorfail-outcome-number-114)	|	[Next MinorFail outcome](#minorfail-outcome-number-116)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-src-aec3po|
|----|----|
|Title|Standalone&#32;module&#32;src/aec3po.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Module aec3po](https://github.com/Accord-Project/aec3po/blob/HEAD/src/aec3po.ttl)|

#### Criterion detail
|Identifier|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|
|----|----|
|Title|Profile&#32;compatibility&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;check&#32;whether&#32;the&#32;test&#32;subject&#32;is&#32;compatible&#32;with&#32;a&#32;profile&#32;or&#32;not,&#32;and&#32;if&#32;it&#32;is&#32;not,&#32;why.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-115)|Identifier|`owl-rl-profile-error`|
|[Section top](#minorfail-outcome-number-115)|Title|OWL&#32;RL&#32;Profile&#32;incompatible|
|[Section top](#minorfail-outcome-number-115)|Description|Class&#32;Expression&#32;not&#32;supported&#32;as&#32;object&#32;of&#32;rdfs:domain&#32;or&#32;rdfs:range|
|[Section top](#minorfail-outcome-number-115)|Pointer|<pre lang="Turtle"><code>aec3po:hasValue&#32;a&#32;owl:DatatypeProperty,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:FunctionalProperty&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;has&#32;value&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;de&#32;facto&#32;used&#32;to&#32;link&#32;something&#32;(anything:&#32;property,&#32;propert...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:domain&#32; &#91;&#32;a&#32;owl:Class&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:unionOf&#32;(&#32;aec3po:FeatureOfInterest&#32;aec3po:Property&#32;aec3po:CheckMethod&#32;)&#32;]&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32;aec3po:&#32;;  &#10; &#32; &#32; &#32; &#32;skos:note&#32; &#34;The&#32;value&#32;of&#32;the&#32;literal&#32;may&#32;be&#32;a&#32;XSD&#32;literal&#32;(boolean,&#32;inte...&#34; &#32;.</code></pre>|

***
### MinorFail Outcome number 116

[Jump to summary definition](#summary-MinorFail-116)	|	[Previous MinorFail outcome](#minorfail-outcome-number-115)	|	[Next MinorFail outcome](#minorfail-outcome-number-117)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-src-aec3po|
|----|----|
|Title|Standalone&#32;module&#32;src/aec3po.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Module aec3po](https://github.com/Accord-Project/aec3po/blob/HEAD/src/aec3po.ttl)|

#### Criterion detail
|Identifier|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|
|----|----|
|Title|Profile&#32;compatibility&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;check&#32;whether&#32;the&#32;test&#32;subject&#32;is&#32;compatible&#32;with&#32;a&#32;profile&#32;or&#32;not,&#32;and&#32;if&#32;it&#32;is&#32;not,&#32;why.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-116)|Identifier|`owl-rl-profile-error`|
|[Section top](#minorfail-outcome-number-116)|Title|OWL&#32;RL&#32;Profile&#32;incompatible|
|[Section top](#minorfail-outcome-number-116)|Description|Statement&#32;not&#32;supported&#32;in&#32;a&#32;Super&#32;Class&#32;Expression|
|[Section top](#minorfail-outcome-number-116)|Pointer|<pre lang="Turtle"><code>&#91;]&#32;a&#32;owl:Class&#32;;  &#10; &#32; &#32;&#32; &#32;owl:unionOf&#32;(&#32;aec3po:FeatureOfInterest&#32;aec3po:Property&#32;aec3po:CheckMethod&#32;)&#32;.</code></pre>|

***
### MinorFail Outcome number 117

[Jump to summary definition](#summary-MinorFail-117)	|	[Previous MinorFail outcome](#minorfail-outcome-number-116)	|	[Next MinorFail outcome](#minorfail-outcome-number-118)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-src-aec3po|
|----|----|
|Title|Standalone&#32;module&#32;src/aec3po.ttl&#32;from&#32;branch&#32;HEAD|
|Composition|- [Module aec3po](https://github.com/Accord-Project/aec3po/blob/HEAD/src/aec3po.ttl)|

#### Criterion detail
|Identifier|[term-referencing](https://ns.inria.fr/olivaw#term-referencing)|
|----|----|
|Title|Term&#32;referencing&#32;test|
|Description|A&#32;test&#32;case&#32;from&#32;the&#32;Best&#32;Practices&#32;tests&#32;checking&#32;if&#32;each&#32;term&#32;of&#32;the&#32;test&#32;subject&#32;is&#32;referenced&#32;to&#32;a&#32;module&#32;through&#32;a&#32;rdfs:isDefinedBy&#32;property.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-117)|Identifier|`no-reference-module`|
|[Section top](#minorfail-outcome-number-117)|Title|Term&#32;not&#32;referenced&#32;to&#32;a&#32;module|
|[Section top](#minorfail-outcome-number-117)|Description|Subject&#32;terms&#32;not&#32;linked&#32;to&#32;a&#32;module&#32;by&#32;a&#32;rdfs:isDefinedBy&#32;property|
|[Section top](#minorfail-outcome-number-117)|Pointer|<pre lang="Turtle"><code>:edlira&#32;a&#32;schema:Person&#32;;  &#10; &#32; &#32; &#32; &#32;schema:affiliation&#32; &#60;https://www.bcu.ac.uk/> &#32;;  &#10; &#32; &#32; &#32; &#32;schema:email&#32; &#34;edlira.vakaj@bcu.ac.uk&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;schema:identifier&#32; &#60;http://orcid.org/0000-0002-0712-0959> &#32;;  &#10; &#32; &#32; &#32; &#32;schema:name&#32; &#34;Edlira&#32;Vakaj&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;schema:url&#32; &#60;https://www.bcu.ac.uk/computing/about-us/our-staff/edlira-vakaj> &#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-117)|Pointer|<pre lang="Turtle"><code>:pan&#32;a&#32;schema:Person&#32;;  &#10; &#32; &#32; &#32; &#32;schema:affiliation&#32; &#60;https://www.bcu.ac.uk/> &#32;;  &#10; &#32; &#32; &#32; &#32;schema:email&#32; &#34;Panagiotis.Patlakas@bcu.ac.uk&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;schema:identifier&#32; &#60;http://orcid.org/0000-0002-7248-8952> &#32;;  &#10; &#32; &#32; &#32; &#32;schema:name&#32; &#34;Panagiotis&#32;Patlakas&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;schema:url&#32; &#60;https://www.bcu.ac.uk/built-environment/about-us/our-staff/panagiotis-patlakas> &#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-117)|Pointer|<pre lang="Turtle"><code>:amna&#32;a&#32;schema:Person&#32;;  &#10; &#32; &#32; &#32; &#32;schema:affiliation&#32; &#60;https://www.bcu.ac.uk/> &#32;;  &#10; &#32; &#32; &#32; &#32;schema:email&#32; &#34;Amna.Dridi@bcu.ac.uk&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;schema:identifier&#32; &#60;http://orcid.org/0000-0002-0185-103X> &#32;;  &#10; &#32; &#32; &#32; &#32;schema:name&#32; &#34;Amna&#32;Dridi&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;schema:url&#32; &#60;https://www.researchgate.net/profile/Amna-Dridi-3> &#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-117)|Pointer|<pre lang="Turtle"><code>:thomas&#32;a&#32;schema:Person&#32;;  &#10; &#32; &#32; &#32; &#32;schema:affiliation&#32; &#60;https://www.cardiff.ac.uk/> &#32;;  &#10; &#32; &#32; &#32; &#32;schema:email&#32; &#34;beachth@cardiff.ac.uk&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;schema:identifier&#32; &#60;http://orcid.org/0000-0001-5610-8027> &#32;;  &#10; &#32; &#32; &#32; &#32;schema:name&#32; &#34;Thomas&#32;Beach&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;schema:url&#32; &#60;https://profiles.cardiff.ac.uk/staff/beachth> &#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-117)|Pointer|<pre lang="Turtle"><code>:vladimir&#32;a&#32;schema:Person&#32;;  &#10; &#32; &#32; &#32; &#32;schema:affiliation&#32; &#60;https://www.ontotext.com/> &#32;;  &#10; &#32; &#32; &#32; &#32;schema:email&#32; &#34;vladimir.alexiev@ontotext.com&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;schema:identifier&#32; &#60;https://orcid.org/0000-0001-7508-7428> &#32;;  &#10; &#32; &#32; &#32; &#32;schema:name&#32; &#34;Vladimir&#32;Alexiev&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;schema:url&#32; &#60;https://www.ontotext.com/blog/author/vladimir/> &#32;.</code></pre>|

***
### MinorFail Outcome number 118

[Jump to summary definition](#summary-MinorFail-118)	|	[Previous MinorFail outcome](#minorfail-outcome-number-117)	|	[Next MinorFail outcome](#minorfail-outcome-number-119)

:exclamation:MinorFail outcome
#### Subject detail
|Name|all-modules|
|----|----|
|Title|All&#32;the&#32;modules&#32;from&#32;branch&#32;HEAD&#32;that&#32;are&#32;syntaxically&#32;correct&#32;as&#32;well&#32;as&#32;their&#32;recursive&#32;imports|
|Composition|- [Module aec3po](https://github.com/Accord-Project/aec3po/blob/HEAD/src/aec3po.ttl)<br/>- [Module check&lowbar;method](https://github.com/Accord-Project/aec3po/blob/HEAD/src/check_method.ttl)<br/>- [Module checking&lowbar;act](https://github.com/Accord-Project/aec3po/blob/HEAD/src/checking_act.ttl)<br/>- [Module compliance&lowbar;verification&lowbar;report](https://github.com/Accord-Project/aec3po/blob/HEAD/src/compliance_verification_report.ttl)<br/>- [Module data&lowbar;requirement](https://github.com/Accord-Project/aec3po/blob/HEAD/src/data_requirement.ttl)<br/>- [Module document](https://github.com/Accord-Project/aec3po/blob/HEAD/src/document.ttl)<br/>- [Module evidence](https://github.com/Accord-Project/aec3po/blob/HEAD/src/evidence.ttl)<br/>- [Module feature&lowbar;of&lowbar;interest](https://github.com/Accord-Project/aec3po/blob/HEAD/src/feature_of_interest.ttl)<br/>- [Module legal&lowbar;verifier](https://github.com/Accord-Project/aec3po/blob/HEAD/src/legal_verifier.ttl)<br/>- [Module model](https://github.com/Accord-Project/aec3po/blob/HEAD/src/model.ttl)<br/>- [Module rase&lowbar;statement](https://github.com/Accord-Project/aec3po/blob/HEAD/src/rase_statement.ttl)<br/>- [Module statement](https://github.com/Accord-Project/aec3po/blob/HEAD/src/statement.ttl)<br/>- [Module table](https://github.com/Accord-Project/aec3po/blob/HEAD/src/table.ttl)<br/>- [Module vocabularies/&lowbar;shape](https://github.com/Accord-Project/aec3po/blob/HEAD/src/vocabularies/_shape.ttl)<br/>- [Module vocabularies/administrative&lowbar;areas](https://github.com/Accord-Project/aec3po/blob/HEAD/src/vocabularies/administrative_areas.ttl)<br/>- [Module vocabularies/building&lowbar;structure](https://github.com/Accord-Project/aec3po/blob/HEAD/src/vocabularies/building_structure.ttl)<br/>- [Module vocabularies/building&lowbar;usage](https://github.com/Accord-Project/aec3po/blob/HEAD/src/vocabularies/building_usage.ttl)<br/>- [Module vocabularies/check&lowbar;method&lowbar;comparators](https://github.com/Accord-Project/aec3po/blob/HEAD/src/vocabularies/check_method_comparators.ttl)<br/>- [Module vocabularies/check&lowbar;method&lowbar;operators](https://github.com/Accord-Project/aec3po/blob/HEAD/src/vocabularies/check_method_operators.ttl)<br/>- [Module vocabularies/disciplines](https://github.com/Accord-Project/aec3po/blob/HEAD/src/vocabularies/disciplines.ttl)<br/>- [Module vocabularies/permitting&lowbar;stages](https://github.com/Accord-Project/aec3po/blob/HEAD/src/vocabularies/permitting_stages.ttl)<br/>- [Module vocabularies/quantity&lowbar;kinds](https://github.com/Accord-Project/aec3po/blob/HEAD/src/vocabularies/quantity_kinds.ttl)|

#### Criterion detail
|Identifier|[domain-and-range-referencing](https://ns.inria.fr/olivaw#domain-and-range-referencing)|
|----|----|
|Title|Domain&#32;and&#32;range&#32;referencing&#32;test|
|Description|A&#32;test&#32;case&#32;from&#32;the&#32;Best&#32;Practices&#32;tests&#32;checking&#32;if&#32;all&#32;the&#32;ranges&#32;and&#32;domains&#32;from&#32;the&#32;test&#32;subject&#32;point&#32;to&#32;terms&#32;that&#32;are&#32;defined&#32;in&#32;the&#32;vocabulary.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-118)|Identifier|`domain-out-of-vocabulary`|
|[Section top](#minorfail-outcome-number-118)|Title|Domain&#32;out&#32;of&#32;vocabulary|
|[Section top](#minorfail-outcome-number-118)|Description|Some&#32;properties&#32;have&#32;a&#32;domain&#32;out&#32;of&#32;the&#32;ontology|
|[Section top](#minorfail-outcome-number-118)|Pointer|<pre lang="Turtle"><code>:usedMethod&#32;a&#32;owl:ObjectProperty&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;used&#32;method&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;Links&#32;a&#32;checking&#32;act&#32;to&#32;the&#32;method&#32;it&#32;used&#32;(a&#32;aec3po:CheckMe...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:domain&#32; &#91;&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:onProperty&#32;:usedMethod&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:someValuesFrom&#32;:CheckMethod&#32;],  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#91;&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:onProperty&#32;:madeBy&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:someValuesFrom&#32;:ProcessVerifier&#32;],  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#91;&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:onProperty&#32;:checked&#32;],  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#91;&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:onProperty&#32;:hasReport&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:someValuesFrom&#32;:ComplianceVerificationReport&#32;],  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#60;http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#Event>,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;:CheckingAct&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32;:checking&lowbar;act&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:range&#32; &#91;&#32;a&#32;owl:Class&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:unionOf&#32;(&#32;:FeatureOfInterest&#32;:Property&#32;:CheckMethod&#32;)&#32;],  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#60;http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#Method>,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;:CheckMethod&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-118)|Pointer|<pre lang="Turtle"><code>http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#Event</code></pre>|
|[Section top](#minorfail-outcome-number-118)|Pointer|<pre lang="Turtle"><code>:madeBy&#32;a&#32;owl:ObjectProperty&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;made&#32;by&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;Links&#32;a&#32;checking&#32;act&#32;to&#32;the&#32;process&#32;verifier&#32;that&#32;made&#32;it&#32;(a...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:domain&#32; &#91;&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:onProperty&#32;:usedMethod&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:someValuesFrom&#32;:CheckMethod&#32;],  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#91;&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:onProperty&#32;:madeBy&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:someValuesFrom&#32;:ProcessVerifier&#32;],  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#91;&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:onProperty&#32;:checked&#32;],  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#91;&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:onProperty&#32;:hasReport&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:someValuesFrom&#32;:ComplianceVerificationReport&#32;],  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#60;http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#Event>,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;:CheckingAct&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32;:checking&lowbar;act&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:range&#32;:ProcessVerifier&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-118)|Pointer|<pre lang="Turtle"><code>:checked&#32;a&#32;owl:ObjectProperty&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;checked&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;Links&#32;a&#32;checking&#32;act&#32;to&#32;some&#32;entity&#32;(ex.&#32;statement,&#32;feature&#32;...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:domain&#32; &#91;&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:onProperty&#32;:usedMethod&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:someValuesFrom&#32;:CheckMethod&#32;],  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#91;&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:onProperty&#32;:madeBy&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:someValuesFrom&#32;:ProcessVerifier&#32;],  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#91;&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:onProperty&#32;:checked&#32;],  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#91;&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:onProperty&#32;:hasReport&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:someValuesFrom&#32;:ComplianceVerificationReport&#32;],  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#60;http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#Event>,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;:CheckingAct&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32;:checking&lowbar;act&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-118)|Pointer|<pre lang="Turtle"><code>:hasReport&#32;a&#32;owl:ObjectProperty&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;has&#32;report&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;Links&#32;a&#32;checking&#32;act&#32;to&#32;the&#32;resulting&#32;compliance&#32;verificatio...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:domain&#32; &#91;&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:onProperty&#32;:usedMethod&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:someValuesFrom&#32;:CheckMethod&#32;],  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#91;&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:onProperty&#32;:madeBy&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:someValuesFrom&#32;:ProcessVerifier&#32;],  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#91;&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:onProperty&#32;:checked&#32;],  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#91;&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:onProperty&#32;:hasReport&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:someValuesFrom&#32;:ComplianceVerificationReport&#32;],  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#60;http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#Event>,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;:CheckingAct&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32;:checking&lowbar;act&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:range&#32; &#91;&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:onProperty&#32;:conforms&#32;],  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;:ComplianceVerificationReport&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-118)|Pointer|<pre lang="Turtle"><code>:operationalizes&#32;a&#32;owl:ObjectProperty&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;operationalizes&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;Links&#32;a&#32;check&#32;method&#32;to&#32;a&#32;check&#32;statement&#32;in&#32;a&#32;document&#32;that...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:domain&#32; &#91;&#32;a&#32;owl:Class&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:unionOf&#32;(&#32;:FeatureOfInterest&#32;:Property&#32;:CheckMethod&#32;)&#32;],  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#60;http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#Method>,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;:CheckMethod&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32;:check&lowbar;method&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:range&#32; &#91;&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:allValuesFrom&#32;:DocumentSubdivision&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:onProperty&#32;:hasSubdivision&#32;],  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#91;&#32;owl:unionOf&#32;(&#32;:Document&#32;:DocumentSubdivision&#32;)&#32;],  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;:CheckStatement,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;:DocumentSubdivision,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;:Statement&#32;;  &#10; &#32; &#32; &#32; &#32;owl:inverseOf&#32;:isOperationalizedBy&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-118)|Pointer|<pre lang="Turtle"><code>http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#Method</code></pre>|
|[Section top](#minorfail-outcome-number-118)|Pointer|<pre lang="Turtle"><code>:hasComparator&#32;a&#32;owl:FunctionalProperty,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:ObjectProperty&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;has&#32;comparator&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;Links&#32;a&#32;numerical&#32;check&#32;method&#32;to&#32;the&#32;check&#32;method&#32;comparato...&#34;,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#34;The&#32;comparator&#32;of&#32;a&#32;feature&#32;of&#32;interest&#32;or&#32;a&#32;property&#32;of&#32;tha...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:domain&#32;&lowbar;:n218ae2b85f2b47bdb85f7e4e76a2560ab1,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#60;http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#Method>,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;:CheckMethod,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;:NumericalCheckMethod&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32;:check&lowbar;method,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;:check&lowbar;method&lowbar;comparators&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:range&#32;&lowbar;:n218ae2b85f2b47bdb85f7e4e76a2560ab1,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;&lowbar;:n218ae2b85f2b47bdb85f7e4e76a2560ab2,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#91;&#32;rdfs:subClassOf&#32;&lowbar;:n218ae2b85f2b47bdb85f7e4e76a2560ab1,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;&lowbar;:n218ae2b85f2b47bdb85f7e4e76a2560ab2,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#60;http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#Method>,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;skos:Concept,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;:CheckMethod,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;:CheckMethodComparator&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:equivalentClass&#32;:CheckMethodComparator&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:intersectionOf&#32;(&#32;skos:Concept&#32;&lowbar;:n218ae2b85f2b47bdb85f7e4e76a2560ab2&#32;)&#32;],  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#60;http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#Method>,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;skos:Concept,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;:CheckMethod,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;:CheckMethodComparator&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:subPropertyOf&#32;:hasDesign&#32;.  &#10;&lowbar;:n218ae2b85f2b47bdb85f7e4e76a2560ab6&#32;rdf:first&#32;:CheckMethod&#32;;  &#10; &#32; &#32; &#32; &#32;rdf:rest&#32;()&#32;.  &#10;&lowbar;:n218ae2b85f2b47bdb85f7e4e76a2560ab7&#32;rdf:first&#32;:Property&#32;;  &#10; &#32; &#32; &#32; &#32;rdf:rest&#32;&lowbar;:n218ae2b85f2b47bdb85f7e4e76a2560ab6&#32;.  &#10;&lowbar;:n218ae2b85f2b47bdb85f7e4e76a2560ab8&#32;rdf:first&#32;:FeatureOfInterest&#32;;  &#10; &#32; &#32; &#32; &#32;rdf:rest&#32;&lowbar;:n218ae2b85f2b47bdb85f7e4e76a2560ab7&#32;.  &#10;&lowbar;:n218ae2b85f2b47bdb85f7e4e76a2560ab1&#32;a&#32;owl:Class&#32;;  &#10; &#32; &#32; &#32; &#32;owl:unionOf&#32;&lowbar;:n218ae2b85f2b47bdb85f7e4e76a2560ab8&#32;.  &#10;&lowbar;:n218ae2b85f2b47bdb85f7e4e76a2560ab2&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32;owl:hasValue&#32;:CheckMethodComparatorNomenclature&#32;;  &#10; &#32; &#32; &#32; &#32;owl:onProperty&#32;skos:inScheme&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-118)|Pointer|<pre lang="Turtle"><code>:hasNestedValue&#32;a&#32;owl:ObjectProperty&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;hasNestedValue&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;TBD&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:domain&#32; &#91;&#32;a&#32;owl:Class&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:unionOf&#32;(&#32;:FeatureOfInterest&#32;:Property&#32;:CheckMethod&#32;)&#32;],  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#60;http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#Method>,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;:CheckMethod&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32;:check&lowbar;method&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-118)|Pointer|<pre lang="Turtle"><code>:hasOperator&#32;a&#32;owl:FunctionalProperty,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:ObjectProperty&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;has&#32;operator&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;Links&#32;a&#32;boolean&#32;check&#32;method&#32;to&#32;the&#32;check&#32;method&#32;operator&#32;it...&#34;,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#34;The&#32;operator&#32;of&#32;a&#32;feature&#32;of&#32;interest&#32;or&#32;a&#32;property&#32;of&#32;that&#32;...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:domain&#32;&lowbar;:n11d99d9266fe4a79bd48283a3f373e8cb1,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#60;http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#Method>,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;:BooleanCheckMethod,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;:CheckMethod&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32;:check&lowbar;method,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;:check&lowbar;method&lowbar;Operators&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:range&#32;&lowbar;:n11d99d9266fe4a79bd48283a3f373e8cb1,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;&lowbar;:n11d99d9266fe4a79bd48283a3f373e8cb2,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#91;&#32;rdfs:subClassOf&#32;&lowbar;:n11d99d9266fe4a79bd48283a3f373e8cb1,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;&lowbar;:n11d99d9266fe4a79bd48283a3f373e8cb2,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#60;http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#Method>,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;skos:Concept,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;:CheckMethod,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;:CheckMethodOperator&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:equivalentClass&#32;:CheckMethodOperator&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:intersectionOf&#32;(&#32;skos:Concept&#32;&lowbar;:n11d99d9266fe4a79bd48283a3f373e8cb2&#32;)&#32;],  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#60;http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#Method>,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;skos:Concept,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;:CheckMethod,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;:CheckMethodOperator&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:subPropertyOf&#32;:hasDesign&#32;.  &#10;&lowbar;:n11d99d9266fe4a79bd48283a3f373e8cb6&#32;rdf:first&#32;:CheckMethod&#32;;  &#10; &#32; &#32; &#32; &#32;rdf:rest&#32;()&#32;.  &#10;&lowbar;:n11d99d9266fe4a79bd48283a3f373e8cb7&#32;rdf:first&#32;:Property&#32;;  &#10; &#32; &#32; &#32; &#32;rdf:rest&#32;&lowbar;:n11d99d9266fe4a79bd48283a3f373e8cb6&#32;.  &#10;&lowbar;:n11d99d9266fe4a79bd48283a3f373e8cb8&#32;rdf:first&#32;:FeatureOfInterest&#32;;  &#10; &#32; &#32; &#32; &#32;rdf:rest&#32;&lowbar;:n11d99d9266fe4a79bd48283a3f373e8cb7&#32;.  &#10;&lowbar;:n11d99d9266fe4a79bd48283a3f373e8cb1&#32;a&#32;owl:Class&#32;;  &#10; &#32; &#32; &#32; &#32;owl:unionOf&#32;&lowbar;:n11d99d9266fe4a79bd48283a3f373e8cb8&#32;.  &#10;&lowbar;:n11d99d9266fe4a79bd48283a3f373e8cb2&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32;owl:hasValue&#32;:CheckMethodOperatorNomenclature&#32;;  &#10; &#32; &#32; &#32; &#32;owl:onProperty&#32;skos:inScheme&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-118)|Pointer|<pre lang="Turtle"><code>:hasProperty&#32;a&#32;owl:ObjectProperty&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;has&#32;Property&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;Links&#32;a&#32;feature&#32;of&#32;interest&#32;to&#32;one&#32;of&#32;its&#32;aspect&#32;that&#32;is&#32;int...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:domain&#32;&lowbar;:n09800c3927ab4088b73e07e1c21fa9b7b1,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#60;http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#Object>,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#60;https://saref.etsi.org/core/FeatureOfInterest>,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;:FeatureOfInterest&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32;:feature&lowbar;of&lowbar;interest&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:range&#32;&lowbar;:n09800c3927ab4088b73e07e1c21fa9b7b1,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#60;http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#Quality>,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;:Property&#32;;  &#10; &#32; &#32; &#32; &#32;skos:example&#32; &#34;Links&#32;a&#32;space&#32;to&#32;the&#32;area&#32;property&#32;of&#32;that&#32;space,&#32;a&#32;wall&#32;to&#32;...&#34; &#32;.  &#10;&lowbar;:n09800c3927ab4088b73e07e1c21fa9b7b2&#32;rdf:first&#32;:CheckMethod&#32;;  &#10; &#32; &#32; &#32; &#32;rdf:rest&#32;()&#32;.  &#10;&lowbar;:n09800c3927ab4088b73e07e1c21fa9b7b3&#32;rdf:first&#32;:Property&#32;;  &#10; &#32; &#32; &#32; &#32;rdf:rest&#32;&lowbar;:n09800c3927ab4088b73e07e1c21fa9b7b2&#32;.  &#10;&lowbar;:n09800c3927ab4088b73e07e1c21fa9b7b4&#32;rdf:first&#32;:FeatureOfInterest&#32;;  &#10; &#32; &#32; &#32; &#32;rdf:rest&#32;&lowbar;:n09800c3927ab4088b73e07e1c21fa9b7b3&#32;.  &#10;&lowbar;:n09800c3927ab4088b73e07e1c21fa9b7b1&#32;a&#32;owl:Class&#32;;  &#10; &#32; &#32; &#32; &#32;owl:unionOf&#32;&lowbar;:n09800c3927ab4088b73e07e1c21fa9b7b4&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-118)|Pointer|<pre lang="Turtle"><code>http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#Object</code></pre>|
|[Section top](#minorfail-outcome-number-118)|Pointer|<pre lang="Turtle"><code>:hasProperty&#32;a&#32;owl:ObjectProperty&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;has&#32;Property&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;Links&#32;a&#32;feature&#32;of&#32;interest&#32;to&#32;one&#32;of&#32;its&#32;aspect&#32;that&#32;is&#32;int...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:domain&#32;&lowbar;:neea2f620c40141908fd84811cc1d70e1b1,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#60;http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#Object>,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#60;https://saref.etsi.org/core/FeatureOfInterest>,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;:FeatureOfInterest&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32;:feature&lowbar;of&lowbar;interest&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:range&#32;&lowbar;:neea2f620c40141908fd84811cc1d70e1b1,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#60;http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#Quality>,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;:Property&#32;;  &#10; &#32; &#32; &#32; &#32;skos:example&#32; &#34;Links&#32;a&#32;space&#32;to&#32;the&#32;area&#32;property&#32;of&#32;that&#32;space,&#32;a&#32;wall&#32;to&#32;...&#34; &#32;.  &#10;&lowbar;:neea2f620c40141908fd84811cc1d70e1b2&#32;rdf:first&#32;:CheckMethod&#32;;  &#10; &#32; &#32; &#32; &#32;rdf:rest&#32;()&#32;.  &#10;&lowbar;:neea2f620c40141908fd84811cc1d70e1b3&#32;rdf:first&#32;:Property&#32;;  &#10; &#32; &#32; &#32; &#32;rdf:rest&#32;&lowbar;:neea2f620c40141908fd84811cc1d70e1b2&#32;.  &#10;&lowbar;:neea2f620c40141908fd84811cc1d70e1b4&#32;rdf:first&#32;:FeatureOfInterest&#32;;  &#10; &#32; &#32; &#32; &#32;rdf:rest&#32;&lowbar;:neea2f620c40141908fd84811cc1d70e1b3&#32;.  &#10;&lowbar;:neea2f620c40141908fd84811cc1d70e1b1&#32;a&#32;owl:Class&#32;;  &#10; &#32; &#32; &#32; &#32;owl:unionOf&#32;&lowbar;:neea2f620c40141908fd84811cc1d70e1b4&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-118)|Pointer|<pre lang="Turtle"><code>https://saref.etsi.org/core/FeatureOfInterest</code></pre>|
|[Section top](#minorfail-outcome-number-118)|Pointer|<pre lang="Turtle"><code>:hasQuantityKind&#32;a&#32;owl:ObjectProperty&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;has&#32;quantity&#32;kind&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;Links&#32;a&#32;property&#32;to&#32;its&#32;quantity&#32;kind&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:domain&#32; &#91;&#32;a&#32;owl:Class&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:unionOf&#32;(&#32;:FeatureOfInterest&#32;:Property&#32;:CheckMethod&#32;)&#32;],  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#60;http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#Quality>,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;:Property&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32;:feature&lowbar;of&lowbar;interest&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:range&#32;&lowbar;:na2b9d00b74c24f7c80f4abee9bc445a4b5,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#91;&#32;rdfs:subClassOf&#32;&lowbar;:na2b9d00b74c24f7c80f4abee9bc445a4b5,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;qudt:QuantityKind,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#60;http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#Region>,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;skos:Concept,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;:QuantityKind&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:equivalentClass&#32;:QuantityKind&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:intersectionOf&#32;(&#32;skos:Concept&#32;&lowbar;:na2b9d00b74c24f7c80f4abee9bc445a4b5&#32;)&#32;],  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;qudt:QuantityKind,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#60;http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#Region>,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;skos:Concept,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;:QuantityKind&#32;;  &#10; &#32; &#32; &#32; &#32;skos:example&#32; &#34;A&#32;space&#32;area&#32;property&#32;to&#32;the&#32;property&#32;kind&#32; &#92; &#34;area&#92; &#34;.&#34;@en&#32;.  &#10;&lowbar;:na2b9d00b74c24f7c80f4abee9bc445a4b5&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32;owl:hasValue&#32;:QuantityKindNomenclature&#32;;  &#10; &#32; &#32; &#32; &#32;owl:onProperty&#32;skos:inScheme&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-118)|Pointer|<pre lang="Turtle"><code>http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#Quality</code></pre>|

***
### MinorFail Outcome number 119

[Jump to summary definition](#summary-MinorFail-119)	|	[Previous MinorFail outcome](#minorfail-outcome-number-118)	|	[Next MinorFail outcome](#minorfail-outcome-number-120)

:exclamation:MinorFail outcome
#### Subject detail
|Name|all-modules|
|----|----|
|Title|All&#32;the&#32;modules&#32;from&#32;branch&#32;HEAD&#32;that&#32;are&#32;syntaxically&#32;correct&#32;as&#32;well&#32;as&#32;their&#32;recursive&#32;imports|
|Composition|- [Module aec3po](https://github.com/Accord-Project/aec3po/blob/HEAD/src/aec3po.ttl)<br/>- [Module check&lowbar;method](https://github.com/Accord-Project/aec3po/blob/HEAD/src/check_method.ttl)<br/>- [Module checking&lowbar;act](https://github.com/Accord-Project/aec3po/blob/HEAD/src/checking_act.ttl)<br/>- [Module compliance&lowbar;verification&lowbar;report](https://github.com/Accord-Project/aec3po/blob/HEAD/src/compliance_verification_report.ttl)<br/>- [Module data&lowbar;requirement](https://github.com/Accord-Project/aec3po/blob/HEAD/src/data_requirement.ttl)<br/>- [Module document](https://github.com/Accord-Project/aec3po/blob/HEAD/src/document.ttl)<br/>- [Module evidence](https://github.com/Accord-Project/aec3po/blob/HEAD/src/evidence.ttl)<br/>- [Module feature&lowbar;of&lowbar;interest](https://github.com/Accord-Project/aec3po/blob/HEAD/src/feature_of_interest.ttl)<br/>- [Module legal&lowbar;verifier](https://github.com/Accord-Project/aec3po/blob/HEAD/src/legal_verifier.ttl)<br/>- [Module model](https://github.com/Accord-Project/aec3po/blob/HEAD/src/model.ttl)<br/>- [Module rase&lowbar;statement](https://github.com/Accord-Project/aec3po/blob/HEAD/src/rase_statement.ttl)<br/>- [Module statement](https://github.com/Accord-Project/aec3po/blob/HEAD/src/statement.ttl)<br/>- [Module table](https://github.com/Accord-Project/aec3po/blob/HEAD/src/table.ttl)<br/>- [Module vocabularies/&lowbar;shape](https://github.com/Accord-Project/aec3po/blob/HEAD/src/vocabularies/_shape.ttl)<br/>- [Module vocabularies/administrative&lowbar;areas](https://github.com/Accord-Project/aec3po/blob/HEAD/src/vocabularies/administrative_areas.ttl)<br/>- [Module vocabularies/building&lowbar;structure](https://github.com/Accord-Project/aec3po/blob/HEAD/src/vocabularies/building_structure.ttl)<br/>- [Module vocabularies/building&lowbar;usage](https://github.com/Accord-Project/aec3po/blob/HEAD/src/vocabularies/building_usage.ttl)<br/>- [Module vocabularies/check&lowbar;method&lowbar;comparators](https://github.com/Accord-Project/aec3po/blob/HEAD/src/vocabularies/check_method_comparators.ttl)<br/>- [Module vocabularies/check&lowbar;method&lowbar;operators](https://github.com/Accord-Project/aec3po/blob/HEAD/src/vocabularies/check_method_operators.ttl)<br/>- [Module vocabularies/disciplines](https://github.com/Accord-Project/aec3po/blob/HEAD/src/vocabularies/disciplines.ttl)<br/>- [Module vocabularies/permitting&lowbar;stages](https://github.com/Accord-Project/aec3po/blob/HEAD/src/vocabularies/permitting_stages.ttl)<br/>- [Module vocabularies/quantity&lowbar;kinds](https://github.com/Accord-Project/aec3po/blob/HEAD/src/vocabularies/quantity_kinds.ttl)|

#### Criterion detail
|Identifier|[domain-and-range-referencing](https://ns.inria.fr/olivaw#domain-and-range-referencing)|
|----|----|
|Title|Domain&#32;and&#32;range&#32;referencing&#32;test|
|Description|A&#32;test&#32;case&#32;from&#32;the&#32;Best&#32;Practices&#32;tests&#32;checking&#32;if&#32;all&#32;the&#32;ranges&#32;and&#32;domains&#32;from&#32;the&#32;test&#32;subject&#32;point&#32;to&#32;terms&#32;that&#32;are&#32;defined&#32;in&#32;the&#32;vocabulary.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-119)|Identifier|`range-out-of-vocabulary`|
|[Section top](#minorfail-outcome-number-119)|Title|Range&#32;out&#32;of&#32;vocabulary|
|[Section top](#minorfail-outcome-number-119)|Description|Some&#32;properties&#32;have&#32;a&#32;range&#32;out&#32;of&#32;the&#32;ontology|
|[Section top](#minorfail-outcome-number-119)|Pointer|<pre lang="Turtle"><code>:usedMethod&#32;a&#32;owl:ObjectProperty&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;used&#32;method&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;Links&#32;a&#32;checking&#32;act&#32;to&#32;the&#32;method&#32;it&#32;used&#32;(a&#32;aec3po:CheckMe...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:domain&#32; &#91;&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:onProperty&#32;:usedMethod&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:someValuesFrom&#32;:CheckMethod&#32;],  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#91;&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:onProperty&#32;:madeBy&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:someValuesFrom&#32;:ProcessVerifier&#32;],  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#91;&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:onProperty&#32;:checked&#32;],  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#91;&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:onProperty&#32;:hasReport&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:someValuesFrom&#32;:ComplianceVerificationReport&#32;],  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#60;http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#Event>,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;:CheckingAct&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32;:checking&lowbar;act&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:range&#32; &#91;&#32;a&#32;owl:Class&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:unionOf&#32;(&#32;:FeatureOfInterest&#32;:Property&#32;:CheckMethod&#32;)&#32;],  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#60;http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#Method>,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;:CheckMethod&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-119)|Pointer|<pre lang="Turtle"><code>http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#Method</code></pre>|
|[Section top](#minorfail-outcome-number-119)|Pointer|<pre lang="Turtle"><code>:isOperationalizedBy&#32;a&#32;owl:ObjectProperty&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;is&#32;operationalized&#32;by&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;Links&#32;a&#32;check&#32;statement&#32;in&#32;a&#32;document&#32;to&#32;a&#32;check&#32;method&#32;that...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:domain&#32; &#91;&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:allValuesFrom&#32;:DocumentSubdivision&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:onProperty&#32;:hasSubdivision&#32;],  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#91;&#32;owl:unionOf&#32;(&#32;:Document&#32;:DocumentSubdivision&#32;)&#32;],  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;:CheckStatement,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;:DocumentSubdivision,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;:Statement&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32;:check&lowbar;method&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:range&#32; &#91;&#32;a&#32;owl:Class&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:unionOf&#32;(&#32;:FeatureOfInterest&#32;:Property&#32;:CheckMethod&#32;)&#32;],  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#60;http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#Method>,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;:CheckMethod&#32;;  &#10; &#32; &#32; &#32; &#32;owl:inverseOf&#32;:operationalizes&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-119)|Pointer|<pre lang="Turtle"><code>:hasComparator&#32;a&#32;owl:FunctionalProperty,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:ObjectProperty&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;has&#32;comparator&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;Links&#32;a&#32;numerical&#32;check&#32;method&#32;to&#32;the&#32;check&#32;method&#32;comparato...&#34;,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#34;The&#32;comparator&#32;of&#32;a&#32;feature&#32;of&#32;interest&#32;or&#32;a&#32;property&#32;of&#32;tha...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:domain&#32;&lowbar;:n9929c8ee88694909981f4d4cca15e417b1,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#60;http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#Method>,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;:CheckMethod,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;:NumericalCheckMethod&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32;:check&lowbar;method,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;:check&lowbar;method&lowbar;comparators&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:range&#32;&lowbar;:n9929c8ee88694909981f4d4cca15e417b1,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;&lowbar;:n9929c8ee88694909981f4d4cca15e417b2,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#91;&#32;rdfs:subClassOf&#32;&lowbar;:n9929c8ee88694909981f4d4cca15e417b1,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;&lowbar;:n9929c8ee88694909981f4d4cca15e417b2,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#60;http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#Method>,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;skos:Concept,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;:CheckMethod,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;:CheckMethodComparator&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:equivalentClass&#32;:CheckMethodComparator&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:intersectionOf&#32;(&#32;skos:Concept&#32;&lowbar;:n9929c8ee88694909981f4d4cca15e417b2&#32;)&#32;],  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#60;http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#Method>,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;skos:Concept,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;:CheckMethod,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;:CheckMethodComparator&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:subPropertyOf&#32;:hasDesign&#32;.  &#10;&lowbar;:n9929c8ee88694909981f4d4cca15e417b6&#32;rdf:first&#32;:CheckMethod&#32;;  &#10; &#32; &#32; &#32; &#32;rdf:rest&#32;()&#32;.  &#10;&lowbar;:n9929c8ee88694909981f4d4cca15e417b7&#32;rdf:first&#32;:Property&#32;;  &#10; &#32; &#32; &#32; &#32;rdf:rest&#32;&lowbar;:n9929c8ee88694909981f4d4cca15e417b6&#32;.  &#10;&lowbar;:n9929c8ee88694909981f4d4cca15e417b8&#32;rdf:first&#32;:FeatureOfInterest&#32;;  &#10; &#32; &#32; &#32; &#32;rdf:rest&#32;&lowbar;:n9929c8ee88694909981f4d4cca15e417b7&#32;.  &#10;&lowbar;:n9929c8ee88694909981f4d4cca15e417b1&#32;a&#32;owl:Class&#32;;  &#10; &#32; &#32; &#32; &#32;owl:unionOf&#32;&lowbar;:n9929c8ee88694909981f4d4cca15e417b8&#32;.  &#10;&lowbar;:n9929c8ee88694909981f4d4cca15e417b2&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32;owl:hasValue&#32;:CheckMethodComparatorNomenclature&#32;;  &#10; &#32; &#32; &#32; &#32;owl:onProperty&#32;skos:inScheme&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-119)|Pointer|<pre lang="Turtle"><code>:hasComparator&#32;a&#32;owl:FunctionalProperty,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:ObjectProperty&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;has&#32;comparator&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;Links&#32;a&#32;numerical&#32;check&#32;method&#32;to&#32;the&#32;check&#32;method&#32;comparato...&#34;,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#34;The&#32;comparator&#32;of&#32;a&#32;feature&#32;of&#32;interest&#32;or&#32;a&#32;property&#32;of&#32;tha...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:domain&#32;&lowbar;:nc6d1870d5c264c53bdbc4c9dd7371d44b1,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#60;http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#Method>,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;:CheckMethod,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;:NumericalCheckMethod&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32;:check&lowbar;method,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;:check&lowbar;method&lowbar;comparators&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:range&#32;&lowbar;:nc6d1870d5c264c53bdbc4c9dd7371d44b1,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;&lowbar;:nc6d1870d5c264c53bdbc4c9dd7371d44b2,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#91;&#32;rdfs:subClassOf&#32;&lowbar;:nc6d1870d5c264c53bdbc4c9dd7371d44b1,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;&lowbar;:nc6d1870d5c264c53bdbc4c9dd7371d44b2,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#60;http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#Method>,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;skos:Concept,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;:CheckMethod,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;:CheckMethodComparator&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:equivalentClass&#32;:CheckMethodComparator&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:intersectionOf&#32;(&#32;skos:Concept&#32;&lowbar;:nc6d1870d5c264c53bdbc4c9dd7371d44b2&#32;)&#32;],  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#60;http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#Method>,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;skos:Concept,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;:CheckMethod,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;:CheckMethodComparator&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:subPropertyOf&#32;:hasDesign&#32;.  &#10;&lowbar;:nc6d1870d5c264c53bdbc4c9dd7371d44b6&#32;rdf:first&#32;:CheckMethod&#32;;  &#10; &#32; &#32; &#32; &#32;rdf:rest&#32;()&#32;.  &#10;&lowbar;:nc6d1870d5c264c53bdbc4c9dd7371d44b7&#32;rdf:first&#32;:Property&#32;;  &#10; &#32; &#32; &#32; &#32;rdf:rest&#32;&lowbar;:nc6d1870d5c264c53bdbc4c9dd7371d44b6&#32;.  &#10;&lowbar;:nc6d1870d5c264c53bdbc4c9dd7371d44b8&#32;rdf:first&#32;:FeatureOfInterest&#32;;  &#10; &#32; &#32; &#32; &#32;rdf:rest&#32;&lowbar;:nc6d1870d5c264c53bdbc4c9dd7371d44b7&#32;.  &#10;&lowbar;:nc6d1870d5c264c53bdbc4c9dd7371d44b1&#32;a&#32;owl:Class&#32;;  &#10; &#32; &#32; &#32; &#32;owl:unionOf&#32;&lowbar;:nc6d1870d5c264c53bdbc4c9dd7371d44b8&#32;.  &#10;&lowbar;:nc6d1870d5c264c53bdbc4c9dd7371d44b2&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32;owl:hasValue&#32;:CheckMethodComparatorNomenclature&#32;;  &#10; &#32; &#32; &#32; &#32;owl:onProperty&#32;skos:inScheme&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-119)|Pointer|<pre lang="Turtle"><code>:hasUnit&#32;a&#32;owl:FunctionalProperty,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:ObjectProperty&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;hasUnit&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;the&#32;hasUnit&#32;property&#32;is&#32;used&#32;to&#32;link&#32;a&#32;specific&#32;property&#32;or&#32;...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:domain&#32; &#91;&#32;a&#32;owl:Class&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:unionOf&#32;(&#32;:FeatureOfInterest&#32;:Property&#32;:CheckMethod&#32;)&#32;]&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32;:check&lowbar;method&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:range&#32;qudt:Unit&#32;;  &#10; &#32; &#32; &#32; &#32;owl:eqivalentProperty&#32;qudt:hasValue&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-119)|Pointer|<pre lang="Turtle"><code>http://qudt.org/schema/qudt/Unit</code></pre>|
|[Section top](#minorfail-outcome-number-119)|Pointer|<pre lang="Turtle"><code>:hasOperator&#32;a&#32;owl:FunctionalProperty,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:ObjectProperty&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;has&#32;operator&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;Links&#32;a&#32;boolean&#32;check&#32;method&#32;to&#32;the&#32;check&#32;method&#32;operator&#32;it...&#34;,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#34;The&#32;operator&#32;of&#32;a&#32;feature&#32;of&#32;interest&#32;or&#32;a&#32;property&#32;of&#32;that&#32;...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:domain&#32;&lowbar;:n394062ec90cf4b03bdc2fc6be43f9c9fb1,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#60;http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#Method>,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;:BooleanCheckMethod,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;:CheckMethod&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32;:check&lowbar;method,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;:check&lowbar;method&lowbar;Operators&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:range&#32;&lowbar;:n394062ec90cf4b03bdc2fc6be43f9c9fb1,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;&lowbar;:n394062ec90cf4b03bdc2fc6be43f9c9fb2,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#91;&#32;rdfs:subClassOf&#32;&lowbar;:n394062ec90cf4b03bdc2fc6be43f9c9fb1,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;&lowbar;:n394062ec90cf4b03bdc2fc6be43f9c9fb2,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#60;http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#Method>,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;skos:Concept,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;:CheckMethod,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;:CheckMethodOperator&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:equivalentClass&#32;:CheckMethodOperator&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:intersectionOf&#32;(&#32;skos:Concept&#32;&lowbar;:n394062ec90cf4b03bdc2fc6be43f9c9fb2&#32;)&#32;],  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#60;http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#Method>,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;skos:Concept,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;:CheckMethod,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;:CheckMethodOperator&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:subPropertyOf&#32;:hasDesign&#32;.  &#10;&lowbar;:n394062ec90cf4b03bdc2fc6be43f9c9fb6&#32;rdf:first&#32;:CheckMethod&#32;;  &#10; &#32; &#32; &#32; &#32;rdf:rest&#32;()&#32;.  &#10;&lowbar;:n394062ec90cf4b03bdc2fc6be43f9c9fb7&#32;rdf:first&#32;:Property&#32;;  &#10; &#32; &#32; &#32; &#32;rdf:rest&#32;&lowbar;:n394062ec90cf4b03bdc2fc6be43f9c9fb6&#32;.  &#10;&lowbar;:n394062ec90cf4b03bdc2fc6be43f9c9fb8&#32;rdf:first&#32;:FeatureOfInterest&#32;;  &#10; &#32; &#32; &#32; &#32;rdf:rest&#32;&lowbar;:n394062ec90cf4b03bdc2fc6be43f9c9fb7&#32;.  &#10;&lowbar;:n394062ec90cf4b03bdc2fc6be43f9c9fb1&#32;a&#32;owl:Class&#32;;  &#10; &#32; &#32; &#32; &#32;owl:unionOf&#32;&lowbar;:n394062ec90cf4b03bdc2fc6be43f9c9fb8&#32;.  &#10;&lowbar;:n394062ec90cf4b03bdc2fc6be43f9c9fb2&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32;owl:hasValue&#32;:CheckMethodOperatorNomenclature&#32;;  &#10; &#32; &#32; &#32; &#32;owl:onProperty&#32;skos:inScheme&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-119)|Pointer|<pre lang="Turtle"><code>:hasOperator&#32;a&#32;owl:FunctionalProperty,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:ObjectProperty&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;has&#32;operator&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;Links&#32;a&#32;boolean&#32;check&#32;method&#32;to&#32;the&#32;check&#32;method&#32;operator&#32;it...&#34;,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#34;The&#32;operator&#32;of&#32;a&#32;feature&#32;of&#32;interest&#32;or&#32;a&#32;property&#32;of&#32;that&#32;...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:domain&#32;&lowbar;:nc619f6b3e9c94bf5bacd624e456b6bd8b1,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#60;http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#Method>,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;:BooleanCheckMethod,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;:CheckMethod&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32;:check&lowbar;method,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;:check&lowbar;method&lowbar;Operators&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:range&#32;&lowbar;:nc619f6b3e9c94bf5bacd624e456b6bd8b1,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;&lowbar;:nc619f6b3e9c94bf5bacd624e456b6bd8b2,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#91;&#32;rdfs:subClassOf&#32;&lowbar;:nc619f6b3e9c94bf5bacd624e456b6bd8b1,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;&lowbar;:nc619f6b3e9c94bf5bacd624e456b6bd8b2,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#60;http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#Method>,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;skos:Concept,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;:CheckMethod,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;:CheckMethodOperator&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:equivalentClass&#32;:CheckMethodOperator&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:intersectionOf&#32;(&#32;skos:Concept&#32;&lowbar;:nc619f6b3e9c94bf5bacd624e456b6bd8b2&#32;)&#32;],  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#60;http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#Method>,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;skos:Concept,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;:CheckMethod,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;:CheckMethodOperator&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:subPropertyOf&#32;:hasDesign&#32;.  &#10;&lowbar;:nc619f6b3e9c94bf5bacd624e456b6bd8b6&#32;rdf:first&#32;:CheckMethod&#32;;  &#10; &#32; &#32; &#32; &#32;rdf:rest&#32;()&#32;.  &#10;&lowbar;:nc619f6b3e9c94bf5bacd624e456b6bd8b7&#32;rdf:first&#32;:Property&#32;;  &#10; &#32; &#32; &#32; &#32;rdf:rest&#32;&lowbar;:nc619f6b3e9c94bf5bacd624e456b6bd8b6&#32;.  &#10;&lowbar;:nc619f6b3e9c94bf5bacd624e456b6bd8b8&#32;rdf:first&#32;:FeatureOfInterest&#32;;  &#10; &#32; &#32; &#32; &#32;rdf:rest&#32;&lowbar;:nc619f6b3e9c94bf5bacd624e456b6bd8b7&#32;.  &#10;&lowbar;:nc619f6b3e9c94bf5bacd624e456b6bd8b1&#32;a&#32;owl:Class&#32;;  &#10; &#32; &#32; &#32; &#32;owl:unionOf&#32;&lowbar;:nc619f6b3e9c94bf5bacd624e456b6bd8b8&#32;.  &#10;&lowbar;:nc619f6b3e9c94bf5bacd624e456b6bd8b2&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32;owl:hasValue&#32;:CheckMethodOperatorNomenclature&#32;;  &#10; &#32; &#32; &#32; &#32;owl:onProperty&#32;skos:inScheme&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-119)|Pointer|<pre lang="Turtle"><code>:hasNestedTarget&#32;a&#32;owl:ObjectProperty&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;hasNestedTarget&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32;:check&lowbar;method&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:range&#32; &#91;&#32;a&#32;owl:Class&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:unionOf&#32;(&#32;:FeatureOfInterest&#32;:Property&#32;:CheckMethod&#32;)&#32;],  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#60;http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#Method>,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;:CheckMethod&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-119)|Pointer|<pre lang="Turtle"><code>:hasFormat&#32;a&#32;owl:ObjectProperty&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;Defines&#32;the&#32;format&#32;of&#32;an&#32;evidence,&#32;which&#32;is&#32;of&#32;type&#32;dct:form...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:domain&#32; &#91;&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:allValuesFrom&#32;:DocumentSubdivision&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:onProperty&#32;:hasSubdivision&#32;],  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#91;&#32;owl:unionOf&#32;(&#32;:Document&#32;:DocumentSubdivision&#32;)&#32;],  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;:DocumentSubdivision,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;:Statement&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32;:evidence&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:range&#32;dc:format&#32;;  &#10; &#32; &#32; &#32; &#32;skos:example&#32; &#34;an&#32;image,&#32;a&#32;drawing&#32;or&#32;a&#32;model&#32;can&#32;be&#32;an&#32;evidence.&#34;@en&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-119)|Pointer|<pre lang="Turtle"><code>:hasProperty&#32;a&#32;owl:ObjectProperty&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;has&#32;Property&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;Links&#32;a&#32;feature&#32;of&#32;interest&#32;to&#32;one&#32;of&#32;its&#32;aspect&#32;that&#32;is&#32;int...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:domain&#32;&lowbar;:nbc28dcec1db64c88bf8299f9eb970932b1,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#60;http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#Object>,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#60;https://saref.etsi.org/core/FeatureOfInterest>,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;:FeatureOfInterest&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32;:feature&lowbar;of&lowbar;interest&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:range&#32;&lowbar;:nbc28dcec1db64c88bf8299f9eb970932b1,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#60;http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#Quality>,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;:Property&#32;;  &#10; &#32; &#32; &#32; &#32;skos:example&#32; &#34;Links&#32;a&#32;space&#32;to&#32;the&#32;area&#32;property&#32;of&#32;that&#32;space,&#32;a&#32;wall&#32;to&#32;...&#34; &#32;.  &#10;&lowbar;:nbc28dcec1db64c88bf8299f9eb970932b2&#32;rdf:first&#32;:CheckMethod&#32;;  &#10; &#32; &#32; &#32; &#32;rdf:rest&#32;()&#32;.  &#10;&lowbar;:nbc28dcec1db64c88bf8299f9eb970932b3&#32;rdf:first&#32;:Property&#32;;  &#10; &#32; &#32; &#32; &#32;rdf:rest&#32;&lowbar;:nbc28dcec1db64c88bf8299f9eb970932b2&#32;.  &#10;&lowbar;:nbc28dcec1db64c88bf8299f9eb970932b4&#32;rdf:first&#32;:FeatureOfInterest&#32;;  &#10; &#32; &#32; &#32; &#32;rdf:rest&#32;&lowbar;:nbc28dcec1db64c88bf8299f9eb970932b3&#32;.  &#10;&lowbar;:nbc28dcec1db64c88bf8299f9eb970932b1&#32;a&#32;owl:Class&#32;;  &#10; &#32; &#32; &#32; &#32;owl:unionOf&#32;&lowbar;:nbc28dcec1db64c88bf8299f9eb970932b4&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-119)|Pointer|<pre lang="Turtle"><code>http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#Quality</code></pre>|
|[Section top](#minorfail-outcome-number-119)|Pointer|<pre lang="Turtle"><code>:hasQuantityKind&#32;a&#32;owl:ObjectProperty&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;has&#32;quantity&#32;kind&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;Links&#32;a&#32;property&#32;to&#32;its&#32;quantity&#32;kind&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:domain&#32; &#91;&#32;a&#32;owl:Class&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:unionOf&#32;(&#32;:FeatureOfInterest&#32;:Property&#32;:CheckMethod&#32;)&#32;],  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#60;http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#Quality>,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;:Property&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32;:feature&lowbar;of&lowbar;interest&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:range&#32;&lowbar;:n39dec571ceb84f089722b481cdfffee7b5,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#91;&#32;rdfs:subClassOf&#32;&lowbar;:n39dec571ceb84f089722b481cdfffee7b5,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;qudt:QuantityKind,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#60;http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#Region>,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;skos:Concept,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;:QuantityKind&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:equivalentClass&#32;:QuantityKind&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:intersectionOf&#32;(&#32;skos:Concept&#32;&lowbar;:n39dec571ceb84f089722b481cdfffee7b5&#32;)&#32;],  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;qudt:QuantityKind,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#60;http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#Region>,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;skos:Concept,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;:QuantityKind&#32;;  &#10; &#32; &#32; &#32; &#32;skos:example&#32; &#34;A&#32;space&#32;area&#32;property&#32;to&#32;the&#32;property&#32;kind&#32; &#92; &#34;area&#92; &#34;.&#34;@en&#32;.  &#10;&lowbar;:n39dec571ceb84f089722b481cdfffee7b5&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32;owl:hasValue&#32;:QuantityKindNomenclature&#32;;  &#10; &#32; &#32; &#32; &#32;owl:onProperty&#32;skos:inScheme&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-119)|Pointer|<pre lang="Turtle"><code>:hasQuantityKind&#32;a&#32;owl:ObjectProperty&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;has&#32;quantity&#32;kind&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;Links&#32;a&#32;property&#32;to&#32;its&#32;quantity&#32;kind&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:domain&#32; &#91;&#32;a&#32;owl:Class&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:unionOf&#32;(&#32;:FeatureOfInterest&#32;:Property&#32;:CheckMethod&#32;)&#32;],  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#60;http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#Quality>,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;:Property&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32;:feature&lowbar;of&lowbar;interest&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:range&#32;&lowbar;:nd6363267bb294efd899758dd663c710cb5,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#91;&#32;rdfs:subClassOf&#32;&lowbar;:nd6363267bb294efd899758dd663c710cb5,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;qudt:QuantityKind,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#60;http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#Region>,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;skos:Concept,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;:QuantityKind&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:equivalentClass&#32;:QuantityKind&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:intersectionOf&#32;(&#32;skos:Concept&#32;&lowbar;:nd6363267bb294efd899758dd663c710cb5&#32;)&#32;],  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;qudt:QuantityKind,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#60;http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#Region>,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;skos:Concept,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;:QuantityKind&#32;;  &#10; &#32; &#32; &#32; &#32;skos:example&#32; &#34;A&#32;space&#32;area&#32;property&#32;to&#32;the&#32;property&#32;kind&#32; &#92; &#34;area&#92; &#34;.&#34;@en&#32;.  &#10;&lowbar;:nd6363267bb294efd899758dd663c710cb5&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32;owl:hasValue&#32;:QuantityKindNomenclature&#32;;  &#10; &#32; &#32; &#32; &#32;owl:onProperty&#32;skos:inScheme&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-119)|Pointer|<pre lang="Turtle"><code>http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#Region</code></pre>|
|[Section top](#minorfail-outcome-number-119)|Pointer|<pre lang="Turtle"><code>:hasQuantityKind&#32;a&#32;owl:ObjectProperty&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;has&#32;quantity&#32;kind&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;Links&#32;a&#32;property&#32;to&#32;its&#32;quantity&#32;kind&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:domain&#32; &#91;&#32;a&#32;owl:Class&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:unionOf&#32;(&#32;:FeatureOfInterest&#32;:Property&#32;:CheckMethod&#32;)&#32;],  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#60;http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#Quality>,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;:Property&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32;:feature&lowbar;of&lowbar;interest&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:range&#32;&lowbar;:n959c9bb6d28b48d9beee4049b992dab5b5,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#91;&#32;rdfs:subClassOf&#32;&lowbar;:n959c9bb6d28b48d9beee4049b992dab5b5,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;qudt:QuantityKind,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#60;http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#Region>,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;skos:Concept,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;:QuantityKind&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:equivalentClass&#32;:QuantityKind&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:intersectionOf&#32;(&#32;skos:Concept&#32;&lowbar;:n959c9bb6d28b48d9beee4049b992dab5b5&#32;)&#32;],  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;qudt:QuantityKind,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#60;http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#Region>,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;skos:Concept,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;:QuantityKind&#32;;  &#10; &#32; &#32; &#32; &#32;skos:example&#32; &#34;A&#32;space&#32;area&#32;property&#32;to&#32;the&#32;property&#32;kind&#32; &#92; &#34;area&#92; &#34;.&#34;@en&#32;.  &#10;&lowbar;:n959c9bb6d28b48d9beee4049b992dab5b5&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32;owl:hasValue&#32;:QuantityKindNomenclature&#32;;  &#10; &#32; &#32; &#32; &#32;owl:onProperty&#32;skos:inScheme&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-119)|Pointer|<pre lang="Turtle"><code>:QuantityKind&#32;a&#32;owl:Class&#32;;  &#10; &#32; &#32;&#32; &#32;rdfs:isDefinedBy&#32; &#60;http://qudt.org/2.1/schema/qudt> &#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-119)|Pointer|<pre lang="Turtle"><code>:forAdministrativeArea&#32;a&#32;owl:ObjectProperty&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;for&#32;administrative&#32;area&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34; &#34; &#34;The&#32;administrative&#32;area&#32;for&#32;which&#32;something&#32;applies.&#92;r  &#10; &#32; &#32;A&#32;se...&#34; &#34; &#34; &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32;:administrative&lowbar;areas&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:range&#32;&lowbar;:n1079952f6e9949fd9f85b8c2ec279810b1,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;&lowbar;:n1079952f6e9949fd9f85b8c2ec279810b2,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#91;&#32;rdfs:subClassOf&#32;&lowbar;:n1079952f6e9949fd9f85b8c2ec279810b1,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;&lowbar;:n1079952f6e9949fd9f85b8c2ec279810b2,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#60;http://data.europa.eu/eli/ontology#AdministrativeArea>,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;skos:Concept,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;:AdministrativeArea&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:equivalentClass&#32; &#60;http://data.europa.eu/eli/ontology#AdministrativeArea>,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;:AdministrativeArea&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:intersectionOf&#32;(&#32;skos:Concept&#32;&lowbar;:n1079952f6e9949fd9f85b8c2ec279810b2&#32;)&#32;],  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#60;http://data.europa.eu/eli/ontology#AdministrativeArea>,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;skos:Concept,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;:AdministrativeArea&#32;.  &#10;&lowbar;:n1079952f6e9949fd9f85b8c2ec279810b6&#32;rdf:first&#32;:AdministrativeArea&#32;;  &#10; &#32; &#32; &#32; &#32;rdf:rest&#32;()&#32;.  &#10;&lowbar;:n1079952f6e9949fd9f85b8c2ec279810b7&#32;rdf:first&#32; &#60;https://schema.org/Place> &#32;;  &#10; &#32; &#32; &#32; &#32;rdf:rest&#32;&lowbar;:n1079952f6e9949fd9f85b8c2ec279810b6&#32;.  &#10;&lowbar;:n1079952f6e9949fd9f85b8c2ec279810b1&#32;a&#32;owl:Class&#32;;  &#10; &#32; &#32; &#32; &#32;owl:unionOf&#32;&lowbar;:n1079952f6e9949fd9f85b8c2ec279810b7&#32;.  &#10;&lowbar;:n1079952f6e9949fd9f85b8c2ec279810b2&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32;owl:hasValue&#32;:AdministrativeAreaNomenclature&#32;;  &#10; &#32; &#32; &#32; &#32;owl:onProperty&#32;skos:inScheme&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-119)|Pointer|<pre lang="Turtle"><code>:forAdministrativeArea&#32;a&#32;owl:ObjectProperty&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;for&#32;administrative&#32;area&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34; &#34; &#34;The&#32;administrative&#32;area&#32;for&#32;which&#32;something&#32;applies.&#92;r  &#10; &#32; &#32;A&#32;se...&#34; &#34; &#34; &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32;:administrative&lowbar;areas&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:range&#32;&lowbar;:n6840d4fa8df443c1b06f07bdfdf51632b1,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;&lowbar;:n6840d4fa8df443c1b06f07bdfdf51632b2,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#91;&#32;rdfs:subClassOf&#32;&lowbar;:n6840d4fa8df443c1b06f07bdfdf51632b1,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;&lowbar;:n6840d4fa8df443c1b06f07bdfdf51632b2,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#60;http://data.europa.eu/eli/ontology#AdministrativeArea>,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;skos:Concept,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;:AdministrativeArea&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:equivalentClass&#32; &#60;http://data.europa.eu/eli/ontology#AdministrativeArea>,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;:AdministrativeArea&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:intersectionOf&#32;(&#32;skos:Concept&#32;&lowbar;:n6840d4fa8df443c1b06f07bdfdf51632b2&#32;)&#32;],  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#60;http://data.europa.eu/eli/ontology#AdministrativeArea>,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;skos:Concept,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;:AdministrativeArea&#32;.  &#10;&lowbar;:n6840d4fa8df443c1b06f07bdfdf51632b6&#32;rdf:first&#32;:AdministrativeArea&#32;;  &#10; &#32; &#32; &#32; &#32;rdf:rest&#32;()&#32;.  &#10;&lowbar;:n6840d4fa8df443c1b06f07bdfdf51632b7&#32;rdf:first&#32; &#60;https://schema.org/Place> &#32;;  &#10; &#32; &#32; &#32; &#32;rdf:rest&#32;&lowbar;:n6840d4fa8df443c1b06f07bdfdf51632b6&#32;.  &#10;&lowbar;:n6840d4fa8df443c1b06f07bdfdf51632b1&#32;a&#32;owl:Class&#32;;  &#10; &#32; &#32; &#32; &#32;owl:unionOf&#32;&lowbar;:n6840d4fa8df443c1b06f07bdfdf51632b7&#32;.  &#10;&lowbar;:n6840d4fa8df443c1b06f07bdfdf51632b2&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32;owl:hasValue&#32;:AdministrativeAreaNomenclature&#32;;  &#10; &#32; &#32; &#32; &#32;owl:onProperty&#32;skos:inScheme&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-119)|Pointer|<pre lang="Turtle"><code>:AdministrativeArea&#32;rdfs:subClassOf&#32;&lowbar;:n2e2c974fbf2649e1959dced6e896dc32b1,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;&lowbar;:n2e2c974fbf2649e1959dced6e896dc32b2,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;&lowbar;:n2e2c974fbf2649e1959dced6e896dc32b3,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;skos:Concept,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;aec3po:AdministrativeArea&#32;;  &#10; &#32; &#32; &#32; &#32;owl:equivalentClass&#32;&lowbar;:n2e2c974fbf2649e1959dced6e896dc32b3,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;aec3po:AdministrativeArea&#32;.  &#10;&lowbar;:n2e2c974fbf2649e1959dced6e896dc32b4&#32;rdf:first&#32;aec3po:AdministrativeArea&#32;;  &#10; &#32; &#32; &#32; &#32;rdf:rest&#32;()&#32;.  &#10;&lowbar;:n2e2c974fbf2649e1959dced6e896dc32b5&#32;rdf:first&#32; &#60;https://schema.org/Place> &#32;;  &#10; &#32; &#32; &#32; &#32;rdf:rest&#32;&lowbar;:n2e2c974fbf2649e1959dced6e896dc32b4&#32;.  &#10;&lowbar;:n2e2c974fbf2649e1959dced6e896dc32b6&#32;rdf:first&#32;&lowbar;:n2e2c974fbf2649e1959dced6e896dc32b2&#32;;  &#10; &#32; &#32; &#32; &#32;rdf:rest&#32;()&#32;.  &#10;&lowbar;:n2e2c974fbf2649e1959dced6e896dc32b7&#32;rdf:first&#32;skos:Concept&#32;;  &#10; &#32; &#32; &#32; &#32;rdf:rest&#32;&lowbar;:n2e2c974fbf2649e1959dced6e896dc32b6&#32;.  &#10;&lowbar;:n2e2c974fbf2649e1959dced6e896dc32b1&#32;a&#32;owl:Class&#32;;  &#10; &#32; &#32; &#32; &#32;owl:unionOf&#32;&lowbar;:n2e2c974fbf2649e1959dced6e896dc32b5&#32;.  &#10;&lowbar;:n2e2c974fbf2649e1959dced6e896dc32b3&#32;rdfs:subClassOf&#32;&lowbar;:n2e2c974fbf2649e1959dced6e896dc32b1,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;&lowbar;:n2e2c974fbf2649e1959dced6e896dc32b2,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;:AdministrativeArea,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;skos:Concept,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;aec3po:AdministrativeArea&#32;;  &#10; &#32; &#32; &#32; &#32;owl:equivalentClass&#32;:AdministrativeArea,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;aec3po:AdministrativeArea&#32;;  &#10; &#32; &#32; &#32; &#32;owl:intersectionOf&#32;&lowbar;:n2e2c974fbf2649e1959dced6e896dc32b7&#32;.  &#10;&lowbar;:n2e2c974fbf2649e1959dced6e896dc32b2&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32;owl:hasValue&#32;aec3po:AdministrativeAreaNomenclature&#32;;  &#10; &#32; &#32; &#32; &#32;owl:onProperty&#32;skos:inScheme&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-119)|Pointer|<pre lang="Turtle"><code>:forBuildingStructure&#32;a&#32;owl:ObjectProperty&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;for&#32;building&#32;structure&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;The&#32;building&#32;structure&#32;for&#32;which&#32;a&#32;specific&#32;check,&#32;verifier,...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32;:building&lowbar;structure&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:range&#32;&lowbar;:n18c84f1b399f41b38de2a5d7a87a87c2b1,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#91;&#32;rdfs:subClassOf&#32;&lowbar;:n18c84f1b399f41b38de2a5d7a87a87c2b1,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;skos:Concept,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;:BuildingStructure,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;:Design&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:equivalentClass&#32;:BuildingStructure&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:intersectionOf&#32;(&#32;skos:Concept&#32;&lowbar;:n18c84f1b399f41b38de2a5d7a87a87c2b1&#32;)&#32;],  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;skos:Concept,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;:BuildingStructure,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;:Design&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:subPropertyOf&#32;:forDesign&#32;.  &#10;&lowbar;:n18c84f1b399f41b38de2a5d7a87a87c2b1&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32;owl:hasValue&#32;:BuildingStructureNomenclature&#32;;  &#10; &#32; &#32; &#32; &#32;owl:onProperty&#32;skos:inScheme&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-119)|Pointer|<pre lang="Turtle"><code>:hasBuildingStructure&#32;a&#32;owl:FunctionalProperty,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:ObjectProperty&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;has&#32;building&#32;structure&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;The&#32;building&#32;structure&#32;design&#32;of&#32;a&#32;feature&#32;of&#32;interest&#32;or&#32;a&#32;...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32;:building&lowbar;structure&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:range&#32;&lowbar;:na6434e47863c4973843a4ad2269d360cb1,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#91;&#32;rdfs:subClassOf&#32;&lowbar;:na6434e47863c4973843a4ad2269d360cb1,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;skos:Concept,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;:BuildingStructure,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;:Design&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:equivalentClass&#32;:BuildingStructure&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:intersectionOf&#32;(&#32;skos:Concept&#32;&lowbar;:na6434e47863c4973843a4ad2269d360cb1&#32;)&#32;],  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;skos:Concept,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;:BuildingStructure,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;:Design&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:subPropertyOf&#32;:hasDesign&#32;.  &#10;&lowbar;:na6434e47863c4973843a4ad2269d360cb1&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32;owl:hasValue&#32;:BuildingStructureNomenclature&#32;;  &#10; &#32; &#32; &#32; &#32;owl:onProperty&#32;skos:inScheme&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-119)|Pointer|<pre lang="Turtle"><code>:forBuildingUsage&#32;a&#32;owl:ObjectProperty&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;for&#32;building&#32;usage&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;The&#32;building&#32;usage&#32;for&#32;which&#32;a&#32;specific&#32;check,&#32;verifier,&#32;or&#32;...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32;:building&lowbar;usage&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:range&#32;&lowbar;:nf6f2d40338394b50984ad686032b48abb1,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#91;&#32;rdfs:subClassOf&#32;&lowbar;:nf6f2d40338394b50984ad686032b48abb1,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;skos:Concept,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;:BuildingUsage,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;:Design&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:equivalentClass&#32;:BuildingUsage&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:intersectionOf&#32;(&#32;skos:Concept&#32;&lowbar;:nf6f2d40338394b50984ad686032b48abb1&#32;)&#32;],  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;skos:Concept,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;:BuildingUsage,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;:Design&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:subPropertyOf&#32;:forDesign&#32;.  &#10;&lowbar;:nf6f2d40338394b50984ad686032b48abb1&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32;owl:hasValue&#32;:BuildingUsageNomenclature&#32;;  &#10; &#32; &#32; &#32; &#32;owl:onProperty&#32;skos:inScheme&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-119)|Pointer|<pre lang="Turtle"><code>:hasBuildingUsage&#32;a&#32;owl:FunctionalProperty,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:ObjectProperty&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;has&#32;building&#32;usage&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;The&#32;building&#32;usage&#32;design&#32;of&#32;a&#32;feature&#32;of&#32;interest&#32;or&#32;a&#32;prop...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32;:building&lowbar;usage&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:range&#32;&lowbar;:nab2d37911cb04a57a7f84a3aeaacea40b1,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#91;&#32;rdfs:subClassOf&#32;&lowbar;:nab2d37911cb04a57a7f84a3aeaacea40b1,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;skos:Concept,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;:BuildingUsage,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;:Design&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:equivalentClass&#32;:BuildingUsage&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:intersectionOf&#32;(&#32;skos:Concept&#32;&lowbar;:nab2d37911cb04a57a7f84a3aeaacea40b1&#32;)&#32;],  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;skos:Concept,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;:BuildingUsage,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;:Design&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:subPropertyOf&#32;:hasDesign&#32;.  &#10;&lowbar;:nab2d37911cb04a57a7f84a3aeaacea40b1&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32;owl:hasValue&#32;:BuildingUsageNomenclature&#32;;  &#10; &#32; &#32; &#32; &#32;owl:onProperty&#32;skos:inScheme&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-119)|Pointer|<pre lang="Turtle"><code>:hasDiscipline&#32;a&#32;owl:ObjectProperty&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;has&#32;discipline&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;Links&#32;an&#32;entity&#32;(procedure,&#32;statement,&#32;verifier,&#32;...)&#32;to&#32;the...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32;:discipline&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:range&#32;&lowbar;:n9c33d0a302a845e9a86965d2e4415054b1,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#91;&#32;rdfs:subClassOf&#32;&lowbar;:n9c33d0a302a845e9a86965d2e4415054b1,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;skos:Concept,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;:Discipline&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:equivalentClass&#32;:Discipline&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:intersectionOf&#32;(&#32;skos:Concept&#32;&lowbar;:n9c33d0a302a845e9a86965d2e4415054b1&#32;)&#32;],  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;skos:Concept,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;:Discipline&#32;.  &#10;&lowbar;:n9c33d0a302a845e9a86965d2e4415054b1&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32;owl:hasValue&#32;:DisciplineNomenclature&#32;;  &#10; &#32; &#32; &#32; &#32;owl:onProperty&#32;skos:inScheme&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-119)|Pointer|<pre lang="Turtle"><code>:hasPermittingStage&#32;a&#32;owl:ObjectProperty&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;has&#32;permitting&#32;stage&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;Links&#32;an&#32;entity&#32;to&#32;the&#32;permitting&#32;stage&#32;this&#32;entity&#32;pertains&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32;:permitting&lowbar;stage&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:range&#32;&lowbar;:nc8ea7fa1311348279b3a55eff8570ec3b1,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#91;&#32;rdfs:subClassOf&#32;&lowbar;:nc8ea7fa1311348279b3a55eff8570ec3b1,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;skos:Concept,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;:PermittingStage&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:equivalentClass&#32;:PermittingStage&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:intersectionOf&#32;(&#32;skos:Concept&#32;&lowbar;:nc8ea7fa1311348279b3a55eff8570ec3b1&#32;)&#32;],  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;skos:Concept,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;:PermittingStage&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:subPropertyOf&#32; &#60;https://w3id.org/digitalconstruction/0.5/Lifecycle#hasStage> &#32;;  &#10; &#32; &#32; &#32; &#32;owl:equivalentProperty&#32; &#60;https://w3id.org/digitalconstruction/0.5/Lifecycle#hasStage> &#32;.  &#10;&lowbar;:nc8ea7fa1311348279b3a55eff8570ec3b1&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32;owl:hasValue&#32;:PermittingStageNomenclature&#32;;  &#10; &#32; &#32; &#32; &#32;owl:onProperty&#32;skos:inScheme&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-119)|Pointer|http://www.w3.org/2004/02/skos/core#Concept|
|[Section top](#minorfail-outcome-number-119)|Pointer|http://purl.org/dc/elements/1.1/format|

***
### MinorFail Outcome number 120

[Jump to summary definition](#summary-MinorFail-120)	|	[Previous MinorFail outcome](#minorfail-outcome-number-119)	|	[Next MinorFail outcome](#minorfail-outcome-number-121)

:exclamation:MinorFail outcome
#### Subject detail
|Name|all-modules|
|----|----|
|Title|All&#32;the&#32;modules&#32;from&#32;branch&#32;HEAD&#32;that&#32;are&#32;syntaxically&#32;correct&#32;as&#32;well&#32;as&#32;their&#32;recursive&#32;imports|
|Composition|- [Module aec3po](https://github.com/Accord-Project/aec3po/blob/HEAD/src/aec3po.ttl)<br/>- [Module check&lowbar;method](https://github.com/Accord-Project/aec3po/blob/HEAD/src/check_method.ttl)<br/>- [Module checking&lowbar;act](https://github.com/Accord-Project/aec3po/blob/HEAD/src/checking_act.ttl)<br/>- [Module compliance&lowbar;verification&lowbar;report](https://github.com/Accord-Project/aec3po/blob/HEAD/src/compliance_verification_report.ttl)<br/>- [Module data&lowbar;requirement](https://github.com/Accord-Project/aec3po/blob/HEAD/src/data_requirement.ttl)<br/>- [Module document](https://github.com/Accord-Project/aec3po/blob/HEAD/src/document.ttl)<br/>- [Module evidence](https://github.com/Accord-Project/aec3po/blob/HEAD/src/evidence.ttl)<br/>- [Module feature&lowbar;of&lowbar;interest](https://github.com/Accord-Project/aec3po/blob/HEAD/src/feature_of_interest.ttl)<br/>- [Module legal&lowbar;verifier](https://github.com/Accord-Project/aec3po/blob/HEAD/src/legal_verifier.ttl)<br/>- [Module model](https://github.com/Accord-Project/aec3po/blob/HEAD/src/model.ttl)<br/>- [Module rase&lowbar;statement](https://github.com/Accord-Project/aec3po/blob/HEAD/src/rase_statement.ttl)<br/>- [Module statement](https://github.com/Accord-Project/aec3po/blob/HEAD/src/statement.ttl)<br/>- [Module table](https://github.com/Accord-Project/aec3po/blob/HEAD/src/table.ttl)<br/>- [Module vocabularies/&lowbar;shape](https://github.com/Accord-Project/aec3po/blob/HEAD/src/vocabularies/_shape.ttl)<br/>- [Module vocabularies/administrative&lowbar;areas](https://github.com/Accord-Project/aec3po/blob/HEAD/src/vocabularies/administrative_areas.ttl)<br/>- [Module vocabularies/building&lowbar;structure](https://github.com/Accord-Project/aec3po/blob/HEAD/src/vocabularies/building_structure.ttl)<br/>- [Module vocabularies/building&lowbar;usage](https://github.com/Accord-Project/aec3po/blob/HEAD/src/vocabularies/building_usage.ttl)<br/>- [Module vocabularies/check&lowbar;method&lowbar;comparators](https://github.com/Accord-Project/aec3po/blob/HEAD/src/vocabularies/check_method_comparators.ttl)<br/>- [Module vocabularies/check&lowbar;method&lowbar;operators](https://github.com/Accord-Project/aec3po/blob/HEAD/src/vocabularies/check_method_operators.ttl)<br/>- [Module vocabularies/disciplines](https://github.com/Accord-Project/aec3po/blob/HEAD/src/vocabularies/disciplines.ttl)<br/>- [Module vocabularies/permitting&lowbar;stages](https://github.com/Accord-Project/aec3po/blob/HEAD/src/vocabularies/permitting_stages.ttl)<br/>- [Module vocabularies/quantity&lowbar;kinds](https://github.com/Accord-Project/aec3po/blob/HEAD/src/vocabularies/quantity_kinds.ttl)|

#### Criterion detail
|Identifier|[labeled-terms](https://ns.inria.fr/olivaw#labeled-terms)|
|----|----|
|Title|Term&#32;labeling&#32;test|
|Description|A&#32;test&#32;case&#32;from&#32;the&#32;Best&#32;Practices&#32;tests&#32;checking&#32;if&#32;all&#32;the&#32;terms&#32;of&#32;the&#32;subject&#32;have&#32;a&#32;rdfs:label&#32;property&#32;pointing&#32;to&#32;a&#32;literal&#32;in&#32;English|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-120)|Identifier|`not-labeled-term`|
|[Section top](#minorfail-outcome-number-120)|Title|Terms&#32;not&#32;labeled|
|[Section top](#minorfail-outcome-number-120)|Description|The&#32;following&#32;terms&#32;have&#32;no&#32;rdfs:label&#32;to&#32;define&#32;it&#32;in&#32;natural&#32;language|
|[Section top](#minorfail-outcome-number-120)|Pointer|<pre lang="Turtle"><code>:hasFormat&#32;a&#32;owl:ObjectProperty&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;Defines&#32;the&#32;format&#32;of&#32;an&#32;evidence,&#32;which&#32;is&#32;of&#32;type&#32;dct:form...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:domain&#32;:Statement&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32;:evidence&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:range&#32;dc:format&#32;;  &#10; &#32; &#32; &#32; &#32;skos:example&#32; &#34;an&#32;image,&#32;a&#32;drawing&#32;or&#32;a&#32;model&#32;can&#32;be&#32;an&#32;evidence.&#34;@en&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-120)|Pointer|<pre lang="Turtle"><code>:England&#32;a&#32;owl:NamedIndividual,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;skos:Concept,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;:AdministrativeArea&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32;:administrative&lowbar;areas&#32;;  &#10; &#32; &#32; &#32; &#32;skos:definition&#32; &#34;England&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;skos:inScheme&#32;:AdministrativeAreaNomenclature&#32;;  &#10; &#32; &#32; &#32; &#32;skos:prefLabel&#32; &#34;England&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;skos:topConceptOf&#32;:AdministrativeAreaNomenclature&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-120)|Pointer|<pre lang="Turtle"><code>:Estonia&#32;a&#32;owl:NamedIndividual,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;skos:Concept,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;:AdministrativeArea&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32;:administrative&lowbar;areas&#32;;  &#10; &#32; &#32; &#32; &#32;skos:definition&#32; &#34;Estonia&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;skos:inScheme&#32;:AdministrativeAreaNomenclature&#32;;  &#10; &#32; &#32; &#32; &#32;skos:prefLabel&#32; &#34;Estonia&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;skos:topConceptOf&#32;:AdministrativeAreaNomenclature&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-120)|Pointer|<pre lang="Turtle"><code>:Finland&#32;a&#32;owl:NamedIndividual,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;skos:Concept,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;:AdministrativeArea&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32;:administrative&lowbar;areas&#32;;  &#10; &#32; &#32; &#32; &#32;skos:definition&#32; &#34;Finland&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;skos:inScheme&#32;:AdministrativeAreaNomenclature&#32;;  &#10; &#32; &#32; &#32; &#32;skos:prefLabel&#32; &#34;Finland&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;skos:topConceptOf&#32;:AdministrativeAreaNomenclature&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-120)|Pointer|<pre lang="Turtle"><code>:France&#32;a&#32;owl:NamedIndividual,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;skos:Concept,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;:AdministrativeArea&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32;:administrative&lowbar;areas&#32;;  &#10; &#32; &#32; &#32; &#32;skos:definition&#32; &#34;France&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;skos:inScheme&#32;:AdministrativeAreaNomenclature&#32;;  &#10; &#32; &#32; &#32; &#32;skos:prefLabel&#32; &#34;France&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;skos:topConceptOf&#32;:AdministrativeAreaNomenclature&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-120)|Pointer|<pre lang="Turtle"><code>:Germany&#32;a&#32;owl:NamedIndividual,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;skos:Concept,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;:AdministrativeArea&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32;:administrative&lowbar;areas&#32;;  &#10; &#32; &#32; &#32; &#32;skos:definition&#32; &#34;Germany&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;skos:inScheme&#32;:AdministrativeAreaNomenclature&#32;;  &#10; &#32; &#32; &#32; &#32;skos:prefLabel&#32; &#34;Germany&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;skos:topConceptOf&#32;:AdministrativeAreaNomenclature&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-120)|Pointer|<pre lang="Turtle"><code>:Italy&#32;a&#32;owl:NamedIndividual,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;skos:Concept,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;:AdministrativeArea&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32;:administrative&lowbar;areas&#32;;  &#10; &#32; &#32; &#32; &#32;skos:definition&#32; &#34;Italy&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;skos:inScheme&#32;:AdministrativeAreaNomenclature&#32;;  &#10; &#32; &#32; &#32; &#32;skos:prefLabel&#32; &#34;Italy&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;skos:topConceptOf&#32;:AdministrativeAreaNomenclature&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-120)|Pointer|<pre lang="Turtle"><code>:Spain&#32;a&#32;owl:NamedIndividual,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;skos:Concept,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;:AdministrativeArea&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32;:administrative&lowbar;areas&#32;;  &#10; &#32; &#32; &#32; &#32;skos:definition&#32; &#34;Spain&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;skos:inScheme&#32;:AdministrativeAreaNomenclature&#32;;  &#10; &#32; &#32; &#32; &#32;skos:prefLabel&#32; &#34;Spain&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;skos:topConceptOf&#32;:AdministrativeAreaNomenclature&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-120)|Pointer|<pre lang="Turtle"><code>:BuildingStructure-steel&#32;a&#32;owl:NamedIndividual,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;skos:Concept,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;:BuildingStructure&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32;:building&lowbar;structure&#32;;  &#10; &#32; &#32; &#32; &#32;skos:definition&#32; &#34;Building&#32;has&#32;steel&#32;structure.&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;skos:inScheme&#32;:BuildingStructureNomenclature&#32;;  &#10; &#32; &#32; &#32; &#32;skos:prefLabel&#32; &#34;steel&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;skos:topConceptOf&#32;:BuildingStructureNomenclature&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-120)|Pointer|<pre lang="Turtle"><code>:BuildingStructure-timber&#32;a&#32;owl:NamedIndividual,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;skos:Concept,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;:BuildingStructure&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32;:building&lowbar;structure&#32;;  &#10; &#32; &#32; &#32; &#32;skos:definition&#32; &#34;Building&#32;has&#32;timber&#32;structure.&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;skos:inScheme&#32;:BuildingStructureNomenclature&#32;;  &#10; &#32; &#32; &#32; &#32;skos:prefLabel&#32; &#34;timber&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;skos:topConceptOf&#32;:BuildingStructureNomenclature&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-120)|Pointer|<pre lang="Turtle"><code>:BuildingUsage-commercial&#32;a&#32;owl:NamedIndividual,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;skos:Concept,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;:BuildingUsage&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32;:building&lowbar;usage&#32;;  &#10; &#32; &#32; &#32; &#32;skos:definition&#32; &#34;Building&#32;has&#32;commercial&#32;usage.&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;skos:inScheme&#32;:BuildingUsageNomenclature&#32;;  &#10; &#32; &#32; &#32; &#32;skos:prefLabel&#32; &#34;commercial&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;skos:topConceptOf&#32;:BuildingUsageNomenclature&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-120)|Pointer|<pre lang="Turtle"><code>:BuildingUsage-residential&#32;a&#32;owl:NamedIndividual,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;skos:Concept,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;:BuildingUsage&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32;:building&lowbar;usage&#32;;  &#10; &#32; &#32; &#32; &#32;skos:definition&#32; &#34;Building&#32;has&#32;residential&#32;usage.&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;skos:inScheme&#32;:BuildingUsageNomenclature&#32;;  &#10; &#32; &#32; &#32; &#32;skos:prefLabel&#32; &#34;residential&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;skos:topConceptOf&#32;:BuildingUsageNomenclature&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-120)|Pointer|<pre lang="Turtle"><code>:BuildingUsage-cultural&#32;a&#32;owl:NamedIndividual,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;skos:Concept,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;:BuildingUsage&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32;:building&lowbar;usage&#32;;  &#10; &#32; &#32; &#32; &#32;skos:definition&#32; &#34;Building&#32;has&#32;cultural&#32;usage.&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;skos:inScheme&#32;:BuildingUsageNomenclature&#32;;  &#10; &#32; &#32; &#32; &#32;skos:prefLabel&#32; &#34;cultural&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;skos:topConceptOf&#32;:BuildingUsageNomenclature&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-120)|Pointer|<pre lang="Turtle"><code>:CheckMethodcomparator-logicalAND&#32;a&#32;owl:NamedIndividual,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;skos:Concept,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;:CheckMethodComparator&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32;:check&lowbar;method&lowbar;comparators&#32;;  &#10; &#32; &#32; &#32; &#32;skos:definition&#32; &#34;logical&#32;AND&#32;comparator.&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;skos:inScheme&#32;:CheckMethodComparatorNomenclature&#32;;  &#10; &#32; &#32; &#32; &#32;skos:prefLabel&#32; &#34;logicalAND&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;skos:topConceptOf&#32;:CheckMethodComparatorNomenclature&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-120)|Pointer|<pre lang="Turtle"><code>:CheckMethodcomparator-eq&#32;a&#32;owl:NamedIndividual,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;skos:Concept,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;:CheckMethodcomparator&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32;:check&lowbar;method&lowbar;comparators&#32;;  &#10; &#32; &#32; &#32; &#32;skos:definition&#32; &#34;equal-to&#32;comparator.&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;skos:inScheme&#32;:CheckMethodComparatorNomenclature&#32;;  &#10; &#32; &#32; &#32; &#32;skos:prefLabel&#32; &#34;equal-to&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;skos:topConceptOf&#32;:CheckMethodComparatorNomenclature&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-120)|Pointer|<pre lang="Turtle"><code>:CheckMethodComparator-neq&#32;a&#32;owl:NamedIndividual,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;skos:Concept,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;:CheckMethodComparator&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32;:check&lowbar;method&lowbar;comparators&#32;;  &#10; &#32; &#32; &#32; &#32;skos:definition&#32; &#34;not&#32;equal-to&#32;comparator.&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;skos:inScheme&#32;:CheckMethodComparatorNomenclature&#32;;  &#10; &#32; &#32; &#32; &#32;skos:prefLabel&#32; &#34;not&#32;equal-to&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;skos:topConceptOf&#32;:CheckMethodComparatorNomenclature&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-120)|Pointer|<pre lang="Turtle"><code>:CheckMethodComparator-lt&#32;a&#32;owl:NamedIndividual,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;skos:Concept,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;:CheckMethodComparator&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32;:check&lowbar;method&lowbar;comparators&#32;;  &#10; &#32; &#32; &#32; &#32;skos:definition&#32; &#34;less-than&#32;comparator.&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;skos:inScheme&#32;:CheckMethodComparatorNomenclature&#32;;  &#10; &#32; &#32; &#32; &#32;skos:prefLabel&#32; &#34;less&#32;than&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;skos:topConceptOf&#32;:CheckMethodComparatorNomenclature&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-120)|Pointer|<pre lang="Turtle"><code>:CheckMethodComparator-le&#32;a&#32;owl:NamedIndividual,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;skos:Concept,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;:CheckMethodComparator&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32;:check&lowbar;method&lowbar;comparators&#32;;  &#10; &#32; &#32; &#32; &#32;skos:definition&#32; &#34;less-equal&#32;comparator.&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;skos:inScheme&#32;:CheckMethodComparatorNomenclature&#32;;  &#10; &#32; &#32; &#32; &#32;skos:prefLabel&#32; &#34;less&#32;equal&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;skos:topConceptOf&#32;:CheckMethodComparatorNomenclature&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-120)|Pointer|<pre lang="Turtle"><code>:CheckMethodComparator-gt&#32;a&#32;owl:NamedIndividual,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;skos:Concept,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;:CheckMethodComparator&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32;:check&lowbar;method&lowbar;comparators&#32;;  &#10; &#32; &#32; &#32; &#32;skos:definition&#32; &#34;greater-than&#32;comparator.&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;skos:inScheme&#32;:CheckMethodComparatorNomenclature&#32;;  &#10; &#32; &#32; &#32; &#32;skos:prefLabel&#32; &#34;greater&#32;than&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;skos:topConceptOf&#32;:CheckMethodComparatorNomenclature&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-120)|Pointer|<pre lang="Turtle"><code>:CheckMethodComparator-ge&#32;a&#32;owl:NamedIndividual,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;skos:Concept,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;:CheckMethodComparator&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32;:check&lowbar;method&lowbar;comparators&#32;;  &#10; &#32; &#32; &#32; &#32;skos:definition&#32; &#34;greater-equal&#32;comparator.&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;skos:inScheme&#32;:CheckMethodComparatorNomenclature&#32;;  &#10; &#32; &#32; &#32; &#32;skos:prefLabel&#32; &#34;greater&#32;equal&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;skos:topConceptOf&#32;:CheckMethodComparatorNomenclature&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-120)|Pointer|<pre lang="Turtle"><code>:CheckMethodComparator-logicalOR&#32;a&#32;owl:NamedIndividual,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;skos:Concept,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;:CheckMethodComparator&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32;:check&lowbar;method&lowbar;comparators&#32;;  &#10; &#32; &#32; &#32; &#32;skos:definition&#32; &#34;logical&#32;OR&#32;comparator.&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;skos:inScheme&#32;:CheckMethodComparatorNomenclature&#32;;  &#10; &#32; &#32; &#32; &#32;skos:prefLabel&#32; &#34;logicalOR&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;skos:topConceptOf&#32;:CheckMethodComparatorNomenclature&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-120)|Pointer|<pre lang="Turtle"><code>:CheckMethodOperator-exists&#32;a&#32;owl:NamedIndividual,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;skos:Concept,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;:CheckMethodOperator&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32;:check&lowbar;method&lowbar;operators&#32;;  &#10; &#32; &#32; &#32; &#32;skos:definition&#32; &#34;exists&#32;operator.&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;skos:inScheme&#32;:CheckMethodOperatorNomenclature&#32;;  &#10; &#32; &#32; &#32; &#32;skos:prefLabel&#32; &#34;exists&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;skos:topConceptOf&#32;:CheckMethodOperatorNomenclature&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-120)|Pointer|<pre lang="Turtle"><code>:CheckMethodOperator-notExists&#32;a&#32;owl:NamedIndividual,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;skos:Concept,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;:CheckMethodOperator&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32;:check&lowbar;method&lowbar;operators&#32;;  &#10; &#32; &#32; &#32; &#32;skos:definition&#32; &#34;not&#32;exists&#32;operator.&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;skos:inScheme&#32;:CheckMethodOperatorNomenclature&#32;;  &#10; &#32; &#32; &#32; &#32;skos:prefLabel&#32; &#34;not&#32;exists&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;skos:topConceptOf&#32;:CheckMethodOperatorNomenclature&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-120)|Pointer|<pre lang="Turtle"><code>:CheckMethodOperator-forall&#32;a&#32;owl:NamedIndividual,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;skos:Concept,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;:CheckMethodOperator&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32;:check&lowbar;method&lowbar;operators&#32;;  &#10; &#32; &#32; &#32; &#32;skos:definition&#32; &#34;forall&#32;operator.&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;skos:inScheme&#32;:CheckMethodOperatorNomenclature&#32;;  &#10; &#32; &#32; &#32; &#32;skos:prefLabel&#32; &#34;forall&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;skos:topConceptOf&#32;:CheckMethodOperatorNomenclature&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-120)|Pointer|<pre lang="Turtle"><code>:CheckMethodOperator-addition&#32;a&#32;owl:NamedIndividual,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;skos:Concept,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;:CheckMethodOperator&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32;:check&lowbar;method&lowbar;operators&#32;;  &#10; &#32; &#32; &#32; &#32;skos:definition&#32; &#34;addition&#32;operator.&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;skos:inScheme&#32;:CheckMethodOperatorNomenclature&#32;;  &#10; &#32; &#32; &#32; &#32;skos:prefLabel&#32; &#34;addition&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;skos:topConceptOf&#32;:CheckMethodOperatorNomenclature&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-120)|Pointer|<pre lang="Turtle"><code>:CheckMethodOperator-multiplication&#32;a&#32;owl:NamedIndividual,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;skos:Concept,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;:CheckMethodOperator&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32;:check&lowbar;method&lowbar;operators&#32;;  &#10; &#32; &#32; &#32; &#32;skos:definition&#32; &#34;multiplication&#32;Operator.&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;skos:inScheme&#32;:CheckMethodOperatorNomenclature&#32;;  &#10; &#32; &#32; &#32; &#32;skos:prefLabel&#32; &#34;multiplication&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;skos:topConceptOf&#32;:CheckMethodOperatorNomenclature&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-120)|Pointer|<pre lang="Turtle"><code>:CheckMethodOperator-subtraction&#32;a&#32;owl:NamedIndividual,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;skos:Concept,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;:CheckMethodOperator&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32;:check&lowbar;method&lowbar;operators&#32;;  &#10; &#32; &#32; &#32; &#32;skos:definition&#32; &#34;subtraction&#32;operator.&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;skos:inScheme&#32;:CheckMethodOperatorNomenclature&#32;;  &#10; &#32; &#32; &#32; &#32;skos:prefLabel&#32; &#34;subtraction&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;skos:topConceptOf&#32;:CheckMethodOperatorNomenclature&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-120)|Pointer|<pre lang="Turtle"><code>:CheckMethodOperator-division&#32;a&#32;owl:NamedIndividual,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;skos:Concept,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;:CheckMethodOperator&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32;:check&lowbar;method&lowbar;operators&#32;;  &#10; &#32; &#32; &#32; &#32;skos:definition&#32; &#34;division&#32;Operator.&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;skos:inScheme&#32;:CheckMethodOperatorNomenclature&#32;;  &#10; &#32; &#32; &#32; &#32;skos:prefLabel&#32; &#34;division&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;skos:topConceptOf&#32;:CheckMethodOperatorNomenclature&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-120)|Pointer|<pre lang="Turtle"><code>:Discipline-architecture&#32;a&#32;owl:NamedIndividual,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;skos:Concept,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;:Discipline&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32;:discipline&#32;;  &#10; &#32; &#32; &#32; &#32;skos:definition&#32; &#34;The&#32;Architecture&#32;discipline.&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;skos:inScheme&#32;:DisciplineNomenclature&#32;;  &#10; &#32; &#32; &#32; &#32;skos:prefLabel&#32; &#34;architecture&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;skos:topConceptOf&#32;:DisciplineNomenclature&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-120)|Pointer|<pre lang="Turtle"><code>:Discipline-buildingServices&#32;a&#32;owl:NamedIndividual,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;skos:Concept,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;:Discipline&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32;:discipline&#32;;  &#10; &#32; &#32; &#32; &#32;skos:definition&#32; &#34;The&#32;Building&#32;Services&#32;discipline.&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;skos:inScheme&#32;:DisciplineNomenclature&#32;;  &#10; &#32; &#32; &#32; &#32;skos:prefLabel&#32; &#34;building&#32;services&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;skos:topConceptOf&#32;:DisciplineNomenclature&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-120)|Pointer|<pre lang="Turtle"><code>:Discipline-construction&#32;a&#32;owl:NamedIndividual,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;skos:Concept,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;:Discipline&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32;:discipline&#32;;  &#10; &#32; &#32; &#32; &#32;skos:definition&#32; &#34;The&#32;Construction&#32;discipline.&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;skos:inScheme&#32;:DisciplineNomenclature&#32;;  &#10; &#32; &#32; &#32; &#32;skos:prefLabel&#32; &#34;construction&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;skos:topConceptOf&#32;:DisciplineNomenclature&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-120)|Pointer|<pre lang="Turtle"><code>:Discipline-planning&#32;a&#32;owl:NamedIndividual,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;skos:Concept,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;:Discipline&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32;:discipline&#32;;  &#10; &#32; &#32; &#32; &#32;skos:definition&#32; &#34;The&#32;Planning&#32;discipline.&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;skos:inScheme&#32;:DisciplineNomenclature&#32;;  &#10; &#32; &#32; &#32; &#32;skos:prefLabel&#32; &#34;planning&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;skos:topConceptOf&#32;:DisciplineNomenclature&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-120)|Pointer|<pre lang="Turtle"><code>:Discipline-structuralEngineering&#32;a&#32;owl:NamedIndividual,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;skos:Concept,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;:Discipline&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32;:discipline&#32;;  &#10; &#32; &#32; &#32; &#32;skos:definition&#32; &#34;The&#32;Structural&#32;Engineering&#32;discipline.&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;skos:inScheme&#32;:DisciplineNomenclature&#32;;  &#10; &#32; &#32; &#32; &#32;skos:prefLabel&#32; &#34;structural&#32;engineering&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;skos:topConceptOf&#32;:DisciplineNomenclature&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-120)|Pointer|<pre lang="Turtle"><code>:UK&lowbar;Building&lowbar;Control&lowbar;Submission&#32;a&#32;owl:NamedIndividual,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;skos:Concept,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;:PermittingStage&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32;:permitting&lowbar;stage&#32;;  &#10; &#32; &#32; &#32; &#32;skos:definition&#32; &#34;The&#32;UK&#32;Building&#32;Control&#32;Submission&#32;permitting&#32;stage.&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;skos:inScheme&#32;:PermittingStageNomenclature&#32;;  &#10; &#32; &#32; &#32; &#32;skos:prefLabel&#32; &#34;building&#32;control&#32;submission&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;skos:topConceptOf&#32;:PermittingStageNomenclature&#32;;  &#10; &#32; &#32; &#32; &#32;:forAdministrativeArea&#32;:England&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-120)|Pointer|<pre lang="Turtle"><code>:UK&lowbar;Planning&lowbar;Permission&#32;a&#32;owl:NamedIndividual,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;skos:Concept,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;:PermittingStage&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32;:permitting&lowbar;stage&#32;;  &#10; &#32; &#32; &#32; &#32;skos:definition&#32; &#34;The&#32;UK&#32;Planning&#32;Permission&#32;permitting&#32;stage.&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;skos:inScheme&#32;:PermittingStageNomenclature&#32;;  &#10; &#32; &#32; &#32; &#32;skos:prefLabel&#32; &#34;planning&#32;permission&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;skos:topConceptOf&#32;:PermittingStageNomenclature&#32;;  &#10; &#32; &#32; &#32; &#32;:forAdministrativeArea&#32;:England&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-120)|Pointer|<pre lang="Turtle"><code>:QuantityKind&#32;a&#32;owl:Class&#32;;  &#10; &#32; &#32;&#32; &#32;rdfs:isDefinedBy&#32; &#60;http://qudt.org/2.1/schema/qudt> &#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-120)|Pointer|<pre lang="Turtle"><code>:ModularRoomHeight&#32;a&#32;owl:NamedIndividual,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;skos:Concept,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;:QuantityKind&#32;;  &#10; &#32; &#32; &#32; &#32;qudt:applicableUnit&#32; &#60;http://qudt.org/vocab/unit/CentiM>,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#60;http://qudt.org/vocab/unit/IN>,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#60;http://qudt.org/vocab/unit/M>,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#60;http://qudt.org/vocab/unit/MilliIN>,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#60;http://qudt.org/vocab/unit/MilliM> &#32;;  &#10; &#32; &#32; &#32; &#32;qudt:hasDimensionVector&#32; &#60;http://qudt.org/vocab/dimensionvector/A0E0L1I0M0H0T0D0> &#32;;  &#10; &#32; &#32; &#32; &#32;qudt:normativeReference&#32; &#34;https://www.iso.org/obp/ui/#iso:std:iso:6707:-1:ed-6:v1:en:t...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32;:quantity&lowbar;kinds&#32;;  &#10; &#32; &#32; &#32; &#32;skos:broader&#32; &#60;http://qudt.org/vocab/quantitykind/Length> &#32;;  &#10; &#32; &#32; &#32; &#32;skos:definition&#32; &#34;vertical&#32;distance&#32;within&#32;one&#32;storey&#32;between&#32;the&#32;modular&#32;plan...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;skos:prefLabel&#32; &#34;modular&#32;room&#32;height&#34;@en&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-120)|Pointer|<pre lang="Turtle"><code>:WidthOfAngledCorridor&#32;a&#32;owl:NamedIndividual,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;skos:Concept,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;:QuantityKind&#32;;  &#10; &#32; &#32; &#32; &#32;qudt:applicableUnit&#32; &#60;http://qudt.org/vocab/unit/CentiM>,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#60;http://qudt.org/vocab/unit/IN>,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#60;http://qudt.org/vocab/unit/M>,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#60;http://qudt.org/vocab/unit/MilliIN>,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#60;http://qudt.org/vocab/unit/MilliM> &#32;;  &#10; &#32; &#32; &#32; &#32;qudt:hasDimensionVector&#32; &#60;http://qudt.org/vocab/dimensionvector/A0E0L1I0M0H0T0D0> &#32;;  &#10; &#32; &#32; &#32; &#32;qudt:normativeReference&#32; &#34;https://www.iso.org/obp/ui/#iso:std:iso:7176:-5:ed-2:v1:en:t...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32;:quantity&lowbar;kinds&#32;;  &#10; &#32; &#32; &#32; &#32;skos:broader&#32; &#60;http://qudt.org/vocab/quantitykind/Length> &#32;;  &#10; &#32; &#32; &#32; &#32;skos:definition&#32; &#34;width&#32;of&#32;a&#32;corridor&#32;with&#32;a&#32;right&#32;angled&#32;turn&#32;in&#32;which&#32;the&#32;wh...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;skos:prefLabel&#32; &#34;width&#32;of&#32;angled&#32;corridor&#34;@en&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-120)|Pointer|<pre lang="Turtle"><code>:CompressiveForce&#32;a&#32;owl:NamedIndividual,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;skos:Concept,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;:QuantityKind&#32;;  &#10; &#32; &#32; &#32; &#32;qudt:hasDimensionVector&#32; &#60;http://qudt.org/vocab/dimensionvector/A0E0L1I0M1H0T-2D0> &#32;;  &#10; &#32; &#32; &#32; &#32;qudt:symbol&#32; &#34;C&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32;:quantity&lowbar;kinds&#32;;  &#10; &#32; &#32; &#32; &#32;skos:broader&#32; &#60;http://qudt.org/vocab/quantitykind/Force> &#32;;  &#10; &#32; &#32; &#32; &#32;skos:definition&#32; &#34;Force&#32;tending&#32;to&#32;reduce&#32;the&#32;size&#32;of&#32;a&#32;body.&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;skos:prefLabel&#32; &#34;compressive&#32;force&#34;@en&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-120)|Pointer|<pre lang="Turtle"><code>:PartialSafetyFactor&#32;a&#32;owl:NamedIndividual,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;skos:Concept,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;:QuantityKind&#32;;  &#10; &#32; &#32; &#32; &#32;qudt:applicableUnit&#32; &#60;http://qudt.org/vocab/unit/UNITLESS> &#32;;  &#10; &#32; &#32; &#32; &#32;qudt:hasDimensionVector&#32; &#60;http://qudt.org/vocab/dimensionvector/A0E0L0I0M0H0T0D0> &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32;:quantity&lowbar;kinds&#32;;  &#10; &#32; &#32; &#32; &#32;skos:definition&#32; &#34;Also&#32;written&#32;γM,&#32;the&#32;partial&#32;safety&#32;factor&#32;for&#32;resistance.&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;skos:prefLabel&#32; &#34;Partial&#32;Safety&#32;Factor&#34;@en&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-120)|Pointer|<pre lang="Turtle"><code>:PartialSafetyFactor0&#32;a&#32;owl:NamedIndividual,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;skos:Concept,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;:QuantityKind&#32;;  &#10; &#32; &#32; &#32; &#32;qudt:applicableUnit&#32; &#60;http://qudt.org/vocab/unit/UNITLESS> &#32;;  &#10; &#32; &#32; &#32; &#32;qudt:hasDimensionVector&#32; &#60;http://qudt.org/vocab/dimensionvector/A0E0L0I0M0H0T0D0> &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32;:quantity&lowbar;kinds&#32;;  &#10; &#32; &#32; &#32; &#32;skos:broader&#32;:PartialSafetyFactor&#32;;  &#10; &#32; &#32; &#32; &#32;skos:definition&#32; &#34;Also&#32;written&#32;γM0,&#32;the&#32;partial&#32;safety&#32;factor&#32;for&#32;resistance&#32;r...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;skos:prefLabel&#32; &#34;Partial&#32;Safety&#32;Factor&#34;@en&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-120)|Pointer|<pre lang="Turtle"><code>:AxialCompressionStress&#32;a&#32;owl:NamedIndividual,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;skos:Concept,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;:QuantityKind&#32;;  &#10; &#32; &#32; &#32; &#32;qudt:hasDimensionVector&#32; &#60;http://qudt.org/vocab/dimensionvector/A0E0L1I0M-1H0T-2D0> &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32;:quantity&lowbar;kinds&#32;;  &#10; &#32; &#32; &#32; &#32;skos:definition&#32; &#34;also&#32;known&#32;as&#32;fc0k&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;skos:prefLabel&#32; &#34;axial&#32;compression&#32;stress&#34;@en&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-120)|Pointer|<pre lang="Turtle"><code>:ModificationFactorKmod&#32;a&#32;owl:NamedIndividual,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;skos:Concept,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;:QuantityKind&#32;;  &#10; &#32; &#32; &#32; &#32;qudt:applicableUnit&#32; &#60;http://qudt.org/vocab/unit/UNITLESS> &#32;;  &#10; &#32; &#32; &#32; &#32;qudt:hasDimensionVector&#32; &#60;http://qudt.org/vocab/dimensionvector/A0E0L0I0M0H0T0D0> &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32;:quantity&lowbar;kinds&#32;;  &#10; &#32; &#32; &#32; &#32;skos:definition&#32; &#34;Modification&#32;Factor&#32;to&#32;take&#32;into&#32;account&#32;the&#32;duration&#32;of&#32;loa...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;skos:prefLabel&#32; &#34;Modification&#32;Factor&#32;Kmod&#34;@en&#32;.</code></pre>|

***
### MinorFail Outcome number 121

[Jump to summary definition](#summary-MinorFail-121)	|	[Previous MinorFail outcome](#minorfail-outcome-number-120)	|	[Next MinorFail outcome](#minorfail-outcome-number-122)

:exclamation:MinorFail outcome
#### Subject detail
|Name|all-modules|
|----|----|
|Title|All&#32;the&#32;modules&#32;from&#32;branch&#32;HEAD&#32;that&#32;are&#32;syntaxically&#32;correct&#32;as&#32;well&#32;as&#32;their&#32;recursive&#32;imports|
|Composition|- [Module aec3po](https://github.com/Accord-Project/aec3po/blob/HEAD/src/aec3po.ttl)<br/>- [Module check&lowbar;method](https://github.com/Accord-Project/aec3po/blob/HEAD/src/check_method.ttl)<br/>- [Module checking&lowbar;act](https://github.com/Accord-Project/aec3po/blob/HEAD/src/checking_act.ttl)<br/>- [Module compliance&lowbar;verification&lowbar;report](https://github.com/Accord-Project/aec3po/blob/HEAD/src/compliance_verification_report.ttl)<br/>- [Module data&lowbar;requirement](https://github.com/Accord-Project/aec3po/blob/HEAD/src/data_requirement.ttl)<br/>- [Module document](https://github.com/Accord-Project/aec3po/blob/HEAD/src/document.ttl)<br/>- [Module evidence](https://github.com/Accord-Project/aec3po/blob/HEAD/src/evidence.ttl)<br/>- [Module feature&lowbar;of&lowbar;interest](https://github.com/Accord-Project/aec3po/blob/HEAD/src/feature_of_interest.ttl)<br/>- [Module legal&lowbar;verifier](https://github.com/Accord-Project/aec3po/blob/HEAD/src/legal_verifier.ttl)<br/>- [Module model](https://github.com/Accord-Project/aec3po/blob/HEAD/src/model.ttl)<br/>- [Module rase&lowbar;statement](https://github.com/Accord-Project/aec3po/blob/HEAD/src/rase_statement.ttl)<br/>- [Module statement](https://github.com/Accord-Project/aec3po/blob/HEAD/src/statement.ttl)<br/>- [Module table](https://github.com/Accord-Project/aec3po/blob/HEAD/src/table.ttl)<br/>- [Module vocabularies/&lowbar;shape](https://github.com/Accord-Project/aec3po/blob/HEAD/src/vocabularies/_shape.ttl)<br/>- [Module vocabularies/administrative&lowbar;areas](https://github.com/Accord-Project/aec3po/blob/HEAD/src/vocabularies/administrative_areas.ttl)<br/>- [Module vocabularies/building&lowbar;structure](https://github.com/Accord-Project/aec3po/blob/HEAD/src/vocabularies/building_structure.ttl)<br/>- [Module vocabularies/building&lowbar;usage](https://github.com/Accord-Project/aec3po/blob/HEAD/src/vocabularies/building_usage.ttl)<br/>- [Module vocabularies/check&lowbar;method&lowbar;comparators](https://github.com/Accord-Project/aec3po/blob/HEAD/src/vocabularies/check_method_comparators.ttl)<br/>- [Module vocabularies/check&lowbar;method&lowbar;operators](https://github.com/Accord-Project/aec3po/blob/HEAD/src/vocabularies/check_method_operators.ttl)<br/>- [Module vocabularies/disciplines](https://github.com/Accord-Project/aec3po/blob/HEAD/src/vocabularies/disciplines.ttl)<br/>- [Module vocabularies/permitting&lowbar;stages](https://github.com/Accord-Project/aec3po/blob/HEAD/src/vocabularies/permitting_stages.ttl)<br/>- [Module vocabularies/quantity&lowbar;kinds](https://github.com/Accord-Project/aec3po/blob/HEAD/src/vocabularies/quantity_kinds.ttl)|

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
|[Section top](#minorfail-outcome-number-121)|Description|Class&#32;Expression&#32;not&#32;supported&#32;as&#32;object&#32;of&#32;rdfs:domain&#32;or&#32;rdfs:range|
|[Section top](#minorfail-outcome-number-121)|Pointer|<pre lang="Turtle"><code>aec3po:caption&#32;a&#32;owl:DatatypeProperty&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;caption&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;The&#32;caption&#32;of&#32;a&#32;table,&#32;image,&#32;etc.&#32; &#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:domain&#32; &#91;&#32;a&#32;owl:Class&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:unionOf&#32;(&#32;aec3po:Table&#32;aec3po:Image&#32;)&#32;]&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32;aec3po:table&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-121)|Pointer|<pre lang="Turtle"><code>aec3po:contains&#32;a&#32;owl:ObjectProperty&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;Contains&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;A&#32;container&#32;contains&#32;a&#32;table&#32;and&#32;its&#32;caption.&#32;A&#32;table&#32;contai...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:domain&#32; &#91;&#32;a&#32;owl:Class&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:unionOf&#32;(&#32;aec3po:Table&#32;aec3po:Image&#32;aec3po:Row&#32;aec3po:Column&#32;)&#32;]&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32;aec3po:table&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-121)|Pointer|<pre lang="Turtle"><code>aec3po:hasBSSDDTarget&#32;a&#32;owl:FunctionalProperty,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:ObjectProperty&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;hasBSSDDTarget&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;The&#32;target&#32;refers&#32;to&#32;either&#32;the&#32;name&#32;of&#32;an&#32;object,&#32;the&#32;name&#32;...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:domain&#32; &#91;&#32;a&#32;owl:Class&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:unionOf&#32;(&#32;aec3po:FeatureOfInterest&#32;aec3po:Property&#32;aec3po:CheckMethod&#32;)&#32;]&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32;aec3po:check&lowbar;method&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-121)|Pointer|<pre lang="Turtle"><code>aec3po:hasFirstSubdivision&#32;a&#32;owl:FunctionalProperty,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:ObjectProperty&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;has&#32;first&#32;subdivision&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;Links&#32;a&#32;document&#32;part&#32;to&#32;the&#32;first&#32;of&#32;its&#32;subdivision&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:domain&#32; &#91;&#32;owl:unionOf&#32;(&#32;aec3po:Document&#32;aec3po:DocumentSubdivision&#32;)&#32;]&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32;aec3po:document&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:range&#32;aec3po:DocumentSubdivision&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:subPropertyOf&#32;aec3po:hasSubdivision&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-121)|Pointer|<pre lang="Turtle"><code>aec3po:hasSubdivision&#32;a&#32;owl:ObjectProperty&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;has&#32;subdivision&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;links&#32;a&#32;document&#32;part&#32;to&#32;some&#32;of&#32;its&#32;subdivision&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:domain&#32; &#91;&#32;owl:unionOf&#32;(&#32;aec3po:Document&#32;aec3po:DocumentSubdivision&#32;)&#32;]&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32;aec3po:document&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:range&#32;aec3po:DocumentSubdivision&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:subPropertyOf&#32;dc:hasPart&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-121)|Pointer|<pre lang="Turtle"><code>aec3po:hasUnit&#32;a&#32;owl:FunctionalProperty,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:ObjectProperty&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;hasUnit&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;the&#32;hasUnit&#32;property&#32;is&#32;used&#32;to&#32;link&#32;a&#32;specific&#32;property&#32;or&#32;...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:domain&#32; &#91;&#32;a&#32;owl:Class&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:unionOf&#32;(&#32;aec3po:FeatureOfInterest&#32;aec3po:Property&#32;aec3po:CheckMethod&#32;)&#32;]&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32;aec3po:check&lowbar;method&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:range&#32;qudt:Unit&#32;;  &#10; &#32; &#32; &#32; &#32;owl:eqivalentProperty&#32;qudt:hasValue&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-121)|Pointer|<pre lang="Turtle"><code>aec3po:hasValue&#32;a&#32;owl:DatatypeProperty,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:FunctionalProperty&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;has&#32;value&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;de&#32;facto&#32;used&#32;to&#32;link&#32;something&#32;(anything:&#32;property,&#32;propert...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:domain&#32; &#91;&#32;a&#32;owl:Class&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:unionOf&#32;(&#32;aec3po:FeatureOfInterest&#32;aec3po:Property&#32;aec3po:CheckMethod&#32;)&#32;]&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32;aec3po:&#32;;  &#10; &#32; &#32; &#32; &#32;skos:note&#32; &#34;The&#32;value&#32;of&#32;the&#32;literal&#32;may&#32;be&#32;a&#32;XSD&#32;literal&#32;(boolean,&#32;inte...&#34; &#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-121)|Pointer|<pre lang="Turtle"><code>aec3po:isContainedIn&#32;a&#32;owl:ObjectProperty&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;is&#32;contained&#32;by&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;A&#32;table&#32;contains&#32;row,&#32;columns&#32;and&#32;other&#32;elements.&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32;aec3po:table&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:range&#32; &#91;&#32;a&#32;owl:Class&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:unionOf&#32;(&#32;aec3po:Table&#32;aec3po:Image&#32;aec3po:Row&#32;aec3po:Column&#32;aec3po:Cell&#32;)&#32;]&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-121)|Pointer|<pre lang="Turtle"><code>aec3po:locationCoverage&#32;a&#32;owl:ObjectProperty&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;location&#32;coverage&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;The&#32;spatialCoverage&#32;indicates&#32;the&#32;place(s)&#32;or&#32;the&#32;administra...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:domain&#32; &#60;https://schema.org/Model> &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:range&#32; &#91;&#32;a&#32;owl:Class&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:unionOf&#32;(&#32; &#60;https://schema.org/Place> &#32;aec3po:AdministrativeArea&#32;)&#32;]&#32;;  &#10; &#32; &#32; &#32; &#32;owl:equivalentProperty&#32; &#60;https://schema.org/spatialCoverage> &#32;.</code></pre>|

***
### MinorFail Outcome number 122

[Jump to summary definition](#summary-MinorFail-122)	|	[Previous MinorFail outcome](#minorfail-outcome-number-121)	|	[Next MinorFail outcome](#minorfail-outcome-number-123)

:exclamation:MinorFail outcome
#### Subject detail
|Name|all-modules|
|----|----|
|Title|All&#32;the&#32;modules&#32;from&#32;branch&#32;HEAD&#32;that&#32;are&#32;syntaxically&#32;correct&#32;as&#32;well&#32;as&#32;their&#32;recursive&#32;imports|
|Composition|- [Module aec3po](https://github.com/Accord-Project/aec3po/blob/HEAD/src/aec3po.ttl)<br/>- [Module check&lowbar;method](https://github.com/Accord-Project/aec3po/blob/HEAD/src/check_method.ttl)<br/>- [Module checking&lowbar;act](https://github.com/Accord-Project/aec3po/blob/HEAD/src/checking_act.ttl)<br/>- [Module compliance&lowbar;verification&lowbar;report](https://github.com/Accord-Project/aec3po/blob/HEAD/src/compliance_verification_report.ttl)<br/>- [Module data&lowbar;requirement](https://github.com/Accord-Project/aec3po/blob/HEAD/src/data_requirement.ttl)<br/>- [Module document](https://github.com/Accord-Project/aec3po/blob/HEAD/src/document.ttl)<br/>- [Module evidence](https://github.com/Accord-Project/aec3po/blob/HEAD/src/evidence.ttl)<br/>- [Module feature&lowbar;of&lowbar;interest](https://github.com/Accord-Project/aec3po/blob/HEAD/src/feature_of_interest.ttl)<br/>- [Module legal&lowbar;verifier](https://github.com/Accord-Project/aec3po/blob/HEAD/src/legal_verifier.ttl)<br/>- [Module model](https://github.com/Accord-Project/aec3po/blob/HEAD/src/model.ttl)<br/>- [Module rase&lowbar;statement](https://github.com/Accord-Project/aec3po/blob/HEAD/src/rase_statement.ttl)<br/>- [Module statement](https://github.com/Accord-Project/aec3po/blob/HEAD/src/statement.ttl)<br/>- [Module table](https://github.com/Accord-Project/aec3po/blob/HEAD/src/table.ttl)<br/>- [Module vocabularies/&lowbar;shape](https://github.com/Accord-Project/aec3po/blob/HEAD/src/vocabularies/_shape.ttl)<br/>- [Module vocabularies/administrative&lowbar;areas](https://github.com/Accord-Project/aec3po/blob/HEAD/src/vocabularies/administrative_areas.ttl)<br/>- [Module vocabularies/building&lowbar;structure](https://github.com/Accord-Project/aec3po/blob/HEAD/src/vocabularies/building_structure.ttl)<br/>- [Module vocabularies/building&lowbar;usage](https://github.com/Accord-Project/aec3po/blob/HEAD/src/vocabularies/building_usage.ttl)<br/>- [Module vocabularies/check&lowbar;method&lowbar;comparators](https://github.com/Accord-Project/aec3po/blob/HEAD/src/vocabularies/check_method_comparators.ttl)<br/>- [Module vocabularies/check&lowbar;method&lowbar;operators](https://github.com/Accord-Project/aec3po/blob/HEAD/src/vocabularies/check_method_operators.ttl)<br/>- [Module vocabularies/disciplines](https://github.com/Accord-Project/aec3po/blob/HEAD/src/vocabularies/disciplines.ttl)<br/>- [Module vocabularies/permitting&lowbar;stages](https://github.com/Accord-Project/aec3po/blob/HEAD/src/vocabularies/permitting_stages.ttl)<br/>- [Module vocabularies/quantity&lowbar;kinds](https://github.com/Accord-Project/aec3po/blob/HEAD/src/vocabularies/quantity_kinds.ttl)|

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
|[Section top](#minorfail-outcome-number-122)|Description|Class&#32;Expression&#32;not&#32;supported&#32;with&#32;owl:equivalentClass|
|[Section top](#minorfail-outcome-number-122)|Pointer|<pre lang="Turtle"><code>aec3po:ComponentCheckMethod&#32;a&#32;owl:Class&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;Component&#32;Check&#32;Method&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;Component&#32;check&#32;method&#32;refers&#32;to&#32;a&#32;process&#32;of&#32;inspecting&#32;and...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32;aec3po:check&lowbar;method&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:subClassOf&#32;aec3po:CheckMethod&#32;;  &#10; &#32; &#32; &#32; &#32;owl:equivalentClass&#32; &#91;&#32;a&#32;owl:Class&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:intersectionOf&#32;(&#32;aec3po:CheckMethod&#32; &#91;&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:allValuesFrom&#32; &#91;&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:allValuesFrom&#32;aec3po:FeatureOfInterest&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:onProperty&#32; &#91;&#32;owl:inverseOf&#32;aec3po:forDesign&#32;]&#32;]&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:onProperty&#32;aec3po:forDesign&#32;]&#32;)&#32;]&#32;.</code></pre>|

***
### MinorFail Outcome number 123

[Jump to summary definition](#summary-MinorFail-123)	|	[Previous MinorFail outcome](#minorfail-outcome-number-122)	|	[Next MinorFail outcome](#minorfail-outcome-number-124)

:exclamation:MinorFail outcome
#### Subject detail
|Name|all-modules|
|----|----|
|Title|All&#32;the&#32;modules&#32;from&#32;branch&#32;HEAD&#32;that&#32;are&#32;syntaxically&#32;correct&#32;as&#32;well&#32;as&#32;their&#32;recursive&#32;imports|
|Composition|- [Module aec3po](https://github.com/Accord-Project/aec3po/blob/HEAD/src/aec3po.ttl)<br/>- [Module check&lowbar;method](https://github.com/Accord-Project/aec3po/blob/HEAD/src/check_method.ttl)<br/>- [Module checking&lowbar;act](https://github.com/Accord-Project/aec3po/blob/HEAD/src/checking_act.ttl)<br/>- [Module compliance&lowbar;verification&lowbar;report](https://github.com/Accord-Project/aec3po/blob/HEAD/src/compliance_verification_report.ttl)<br/>- [Module data&lowbar;requirement](https://github.com/Accord-Project/aec3po/blob/HEAD/src/data_requirement.ttl)<br/>- [Module document](https://github.com/Accord-Project/aec3po/blob/HEAD/src/document.ttl)<br/>- [Module evidence](https://github.com/Accord-Project/aec3po/blob/HEAD/src/evidence.ttl)<br/>- [Module feature&lowbar;of&lowbar;interest](https://github.com/Accord-Project/aec3po/blob/HEAD/src/feature_of_interest.ttl)<br/>- [Module legal&lowbar;verifier](https://github.com/Accord-Project/aec3po/blob/HEAD/src/legal_verifier.ttl)<br/>- [Module model](https://github.com/Accord-Project/aec3po/blob/HEAD/src/model.ttl)<br/>- [Module rase&lowbar;statement](https://github.com/Accord-Project/aec3po/blob/HEAD/src/rase_statement.ttl)<br/>- [Module statement](https://github.com/Accord-Project/aec3po/blob/HEAD/src/statement.ttl)<br/>- [Module table](https://github.com/Accord-Project/aec3po/blob/HEAD/src/table.ttl)<br/>- [Module vocabularies/&lowbar;shape](https://github.com/Accord-Project/aec3po/blob/HEAD/src/vocabularies/_shape.ttl)<br/>- [Module vocabularies/administrative&lowbar;areas](https://github.com/Accord-Project/aec3po/blob/HEAD/src/vocabularies/administrative_areas.ttl)<br/>- [Module vocabularies/building&lowbar;structure](https://github.com/Accord-Project/aec3po/blob/HEAD/src/vocabularies/building_structure.ttl)<br/>- [Module vocabularies/building&lowbar;usage](https://github.com/Accord-Project/aec3po/blob/HEAD/src/vocabularies/building_usage.ttl)<br/>- [Module vocabularies/check&lowbar;method&lowbar;comparators](https://github.com/Accord-Project/aec3po/blob/HEAD/src/vocabularies/check_method_comparators.ttl)<br/>- [Module vocabularies/check&lowbar;method&lowbar;operators](https://github.com/Accord-Project/aec3po/blob/HEAD/src/vocabularies/check_method_operators.ttl)<br/>- [Module vocabularies/disciplines](https://github.com/Accord-Project/aec3po/blob/HEAD/src/vocabularies/disciplines.ttl)<br/>- [Module vocabularies/permitting&lowbar;stages](https://github.com/Accord-Project/aec3po/blob/HEAD/src/vocabularies/permitting_stages.ttl)<br/>- [Module vocabularies/quantity&lowbar;kinds](https://github.com/Accord-Project/aec3po/blob/HEAD/src/vocabularies/quantity_kinds.ttl)|

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
|[Section top](#minorfail-outcome-number-123)|Description|Class&#32;Expression&#32;not&#32;supported&#32;with&#32;rdfs:subClassOf|
|[Section top](#minorfail-outcome-number-123)|Pointer|<pre lang="Turtle"><code>aec3po:AndCheckStatement&#32;a&#32;owl:Class&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;And&#32;Check&#32;Statement&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;Check&#32;verified&#32;if&#32;and&#32;only&#32;if&#32;all&#32;of&#32;its&#32;sub-checks&#32;are&#32;veri...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32;aec3po:statement&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:subClassOf&#32; &#91;&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:onProperty&#32;aec3po:hasSubdivision&#32;],  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;aec3po:ChecklistStatement&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-123)|Pointer|<pre lang="Turtle"><code>aec3po:ComplianceVerificationReport&#32;a&#32;owl:Class&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;Compliance&#32;Verification&#32;Report&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;Result&#32;of&#32;a&#32;checking&#32;act.&#32;May&#32;be&#32;compliant&#32;or&#32;not.&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32;aec3po:compliance&lowbar;verification&lowbar;report&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:subClassOf&#32; &#91;&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:onProperty&#32;aec3po:conforms&#32;]&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-123)|Pointer|<pre lang="Turtle"><code>aec3po:DocumentSubdivision&#32;a&#32;owl:Class&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;Document&#32;Subdivision&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;Any&#32;subdivision&#32;of&#32;a&#32;document,&#32;including&#32;sections,&#32;paragraph...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32;aec3po:document&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:subClassOf&#32; &#91;&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:allValuesFrom&#32;aec3po:DocumentSubdivision&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:onProperty&#32;aec3po:hasSubdivision&#32;]&#32;;  &#10; &#32; &#32; &#32; &#32;skos:example&#32; &#34;Paragraph,&#32;section,&#32;definition...&#34;@en&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-123)|Pointer|<pre lang="Turtle"><code>aec3po:LegalVerifier&#32;a&#32;owl:Class&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;Legal&#32;Verifier&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;An&#32;entity&#32;that&#32;has&#32;the&#32;legal&#32;capacity&#32;to&#32;verify&#32;compliance&#32;w...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32;aec3po:legal&lowbar;verifier&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:subClassOf&#32; &#91;&#32;owl:allValuesFrom&#32;aec3po:Document&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:onProperty&#32;aec3po:forDocument&#32;],  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;foaf:Agent&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-123)|Pointer|<pre lang="Turtle"><code>aec3po:NotCheckStatement&#32;a&#32;owl:Class&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;Not&#32;Check&#32;Statement&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;Check&#32;verified&#32;if&#32;and&#32;only&#32;if&#32;the&#32;sub-check&#32;is&#32;not&#32;verified.&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32;aec3po:statement&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:subClassOf&#32; &#91;&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:onProperty&#32;aec3po:hasSubdivision&#32;]&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-123)|Pointer|<pre lang="Turtle"><code>aec3po:OrCheckStatement&#32;a&#32;owl:Class&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;Or&#32;Check&#32;Statement&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;Check&#32;verified&#32;if&#32;and&#32;only&#32;if&#32;at&#32;least&#32;one&#32;of&#32;its&#32;sub-checks...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32;aec3po:statement&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:subClassOf&#32; &#91;&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:onProperty&#32;aec3po:hasSubdivision&#32;],  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;aec3po:ChecklistStatement&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-123)|Pointer|<pre lang="Turtle"><code>aec3po:VerificationResult&#32;a&#32;owl:Class&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;Verification&#32;Result&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;Individual&#32;verification&#32;result&#32;of&#32;a&#32;Compliance&#32;Verification&#32;...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32;aec3po:compliance&lowbar;verification&lowbar;report&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:subClassOf&#32; &#91;&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:onProperty&#32;aec3po:verificationFocus&#32;],  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#91;&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:onProperty&#32;aec3po:hasSeverity&#32;]&#32;.</code></pre>|

***
### MinorFail Outcome number 124

[Jump to summary definition](#summary-MinorFail-124)	|	[Previous MinorFail outcome](#minorfail-outcome-number-123)	|	[Next MinorFail outcome](#minorfail-outcome-number-125)

:exclamation:MinorFail outcome
#### Subject detail
|Name|all-modules|
|----|----|
|Title|All&#32;the&#32;modules&#32;from&#32;branch&#32;HEAD&#32;that&#32;are&#32;syntaxically&#32;correct&#32;as&#32;well&#32;as&#32;their&#32;recursive&#32;imports|
|Composition|- [Module aec3po](https://github.com/Accord-Project/aec3po/blob/HEAD/src/aec3po.ttl)<br/>- [Module check&lowbar;method](https://github.com/Accord-Project/aec3po/blob/HEAD/src/check_method.ttl)<br/>- [Module checking&lowbar;act](https://github.com/Accord-Project/aec3po/blob/HEAD/src/checking_act.ttl)<br/>- [Module compliance&lowbar;verification&lowbar;report](https://github.com/Accord-Project/aec3po/blob/HEAD/src/compliance_verification_report.ttl)<br/>- [Module data&lowbar;requirement](https://github.com/Accord-Project/aec3po/blob/HEAD/src/data_requirement.ttl)<br/>- [Module document](https://github.com/Accord-Project/aec3po/blob/HEAD/src/document.ttl)<br/>- [Module evidence](https://github.com/Accord-Project/aec3po/blob/HEAD/src/evidence.ttl)<br/>- [Module feature&lowbar;of&lowbar;interest](https://github.com/Accord-Project/aec3po/blob/HEAD/src/feature_of_interest.ttl)<br/>- [Module legal&lowbar;verifier](https://github.com/Accord-Project/aec3po/blob/HEAD/src/legal_verifier.ttl)<br/>- [Module model](https://github.com/Accord-Project/aec3po/blob/HEAD/src/model.ttl)<br/>- [Module rase&lowbar;statement](https://github.com/Accord-Project/aec3po/blob/HEAD/src/rase_statement.ttl)<br/>- [Module statement](https://github.com/Accord-Project/aec3po/blob/HEAD/src/statement.ttl)<br/>- [Module table](https://github.com/Accord-Project/aec3po/blob/HEAD/src/table.ttl)<br/>- [Module vocabularies/&lowbar;shape](https://github.com/Accord-Project/aec3po/blob/HEAD/src/vocabularies/_shape.ttl)<br/>- [Module vocabularies/administrative&lowbar;areas](https://github.com/Accord-Project/aec3po/blob/HEAD/src/vocabularies/administrative_areas.ttl)<br/>- [Module vocabularies/building&lowbar;structure](https://github.com/Accord-Project/aec3po/blob/HEAD/src/vocabularies/building_structure.ttl)<br/>- [Module vocabularies/building&lowbar;usage](https://github.com/Accord-Project/aec3po/blob/HEAD/src/vocabularies/building_usage.ttl)<br/>- [Module vocabularies/check&lowbar;method&lowbar;comparators](https://github.com/Accord-Project/aec3po/blob/HEAD/src/vocabularies/check_method_comparators.ttl)<br/>- [Module vocabularies/check&lowbar;method&lowbar;operators](https://github.com/Accord-Project/aec3po/blob/HEAD/src/vocabularies/check_method_operators.ttl)<br/>- [Module vocabularies/disciplines](https://github.com/Accord-Project/aec3po/blob/HEAD/src/vocabularies/disciplines.ttl)<br/>- [Module vocabularies/permitting&lowbar;stages](https://github.com/Accord-Project/aec3po/blob/HEAD/src/vocabularies/permitting_stages.ttl)<br/>- [Module vocabularies/quantity&lowbar;kinds](https://github.com/Accord-Project/aec3po/blob/HEAD/src/vocabularies/quantity_kinds.ttl)|

#### Criterion detail
|Identifier|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|
|----|----|
|Title|Profile&#32;compatibility&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;check&#32;whether&#32;the&#32;test&#32;subject&#32;is&#32;compatible&#32;with&#32;a&#32;profile&#32;or&#32;not,&#32;and&#32;if&#32;it&#32;is&#32;not,&#32;why.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-124)|Identifier|`owl-el-profile-error`|
|[Section top](#minorfail-outcome-number-124)|Title|OWL&#32;EL&#32;Profile&#32;incompatible|
|[Section top](#minorfail-outcome-number-124)|Description|Restriction&#32;on&#32;datatypes|
|[Section top](#minorfail-outcome-number-124)|Pointer|<pre lang="Turtle"><code>aec3po:conforms&#32;a&#32;owl:DatatypeProperty&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;conforms&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;True&#32;if&#32;the&#32;Checking&#32;act&#32;confirms&#32;the&#32;check&#32;was&#32;validated,&#32;a...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:domain&#32;aec3po:ComplianceVerificationReport&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32;aec3po:compliance&lowbar;verification&lowbar;report&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:range&#32;xsd:boolean&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-124)|Pointer|<pre lang="Turtle"><code>aec3po:hasBooleanTarget&#32;a&#32;owl:DatatypeProperty&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;hasBooleanTarget&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;TBD&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:range&#32;xsd:boolean&#32;.</code></pre>|

***
### MinorFail Outcome number 125

[Jump to summary definition](#summary-MinorFail-125)	|	[Previous MinorFail outcome](#minorfail-outcome-number-124)	|	[Next MinorFail outcome](#minorfail-outcome-number-126)

:exclamation:MinorFail outcome
#### Subject detail
|Name|all-modules|
|----|----|
|Title|All&#32;the&#32;modules&#32;from&#32;branch&#32;HEAD&#32;that&#32;are&#32;syntaxically&#32;correct&#32;as&#32;well&#32;as&#32;their&#32;recursive&#32;imports|
|Composition|- [Module aec3po](https://github.com/Accord-Project/aec3po/blob/HEAD/src/aec3po.ttl)<br/>- [Module check&lowbar;method](https://github.com/Accord-Project/aec3po/blob/HEAD/src/check_method.ttl)<br/>- [Module checking&lowbar;act](https://github.com/Accord-Project/aec3po/blob/HEAD/src/checking_act.ttl)<br/>- [Module compliance&lowbar;verification&lowbar;report](https://github.com/Accord-Project/aec3po/blob/HEAD/src/compliance_verification_report.ttl)<br/>- [Module data&lowbar;requirement](https://github.com/Accord-Project/aec3po/blob/HEAD/src/data_requirement.ttl)<br/>- [Module document](https://github.com/Accord-Project/aec3po/blob/HEAD/src/document.ttl)<br/>- [Module evidence](https://github.com/Accord-Project/aec3po/blob/HEAD/src/evidence.ttl)<br/>- [Module feature&lowbar;of&lowbar;interest](https://github.com/Accord-Project/aec3po/blob/HEAD/src/feature_of_interest.ttl)<br/>- [Module legal&lowbar;verifier](https://github.com/Accord-Project/aec3po/blob/HEAD/src/legal_verifier.ttl)<br/>- [Module model](https://github.com/Accord-Project/aec3po/blob/HEAD/src/model.ttl)<br/>- [Module rase&lowbar;statement](https://github.com/Accord-Project/aec3po/blob/HEAD/src/rase_statement.ttl)<br/>- [Module statement](https://github.com/Accord-Project/aec3po/blob/HEAD/src/statement.ttl)<br/>- [Module table](https://github.com/Accord-Project/aec3po/blob/HEAD/src/table.ttl)<br/>- [Module vocabularies/&lowbar;shape](https://github.com/Accord-Project/aec3po/blob/HEAD/src/vocabularies/_shape.ttl)<br/>- [Module vocabularies/administrative&lowbar;areas](https://github.com/Accord-Project/aec3po/blob/HEAD/src/vocabularies/administrative_areas.ttl)<br/>- [Module vocabularies/building&lowbar;structure](https://github.com/Accord-Project/aec3po/blob/HEAD/src/vocabularies/building_structure.ttl)<br/>- [Module vocabularies/building&lowbar;usage](https://github.com/Accord-Project/aec3po/blob/HEAD/src/vocabularies/building_usage.ttl)<br/>- [Module vocabularies/check&lowbar;method&lowbar;comparators](https://github.com/Accord-Project/aec3po/blob/HEAD/src/vocabularies/check_method_comparators.ttl)<br/>- [Module vocabularies/check&lowbar;method&lowbar;operators](https://github.com/Accord-Project/aec3po/blob/HEAD/src/vocabularies/check_method_operators.ttl)<br/>- [Module vocabularies/disciplines](https://github.com/Accord-Project/aec3po/blob/HEAD/src/vocabularies/disciplines.ttl)<br/>- [Module vocabularies/permitting&lowbar;stages](https://github.com/Accord-Project/aec3po/blob/HEAD/src/vocabularies/permitting_stages.ttl)<br/>- [Module vocabularies/quantity&lowbar;kinds](https://github.com/Accord-Project/aec3po/blob/HEAD/src/vocabularies/quantity_kinds.ttl)|

#### Criterion detail
|Identifier|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|
|----|----|
|Title|Profile&#32;compatibility&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;check&#32;whether&#32;the&#32;test&#32;subject&#32;is&#32;compatible&#32;with&#32;a&#32;profile&#32;or&#32;not,&#32;and&#32;if&#32;it&#32;is&#32;not,&#32;why.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-125)|Identifier|`owl-el-profile-error`|
|[Section top](#minorfail-outcome-number-125)|Title|OWL&#32;EL&#32;Profile&#32;incompatible|
|[Section top](#minorfail-outcome-number-125)|Description|Statement&#32;not&#32;supported&#32;in&#32;a&#32;Class&#32;Expression|
|[Section top](#minorfail-outcome-number-125)|Pointer|<pre lang="Turtle"><code>&#91;]&#32;a&#32;owl:Class&#32;;  &#10; &#32; &#32;&#32; &#32;owl:unionOf&#32;(&#32;aec3po:FeatureOfInterest&#32;aec3po:Property&#32;aec3po:CheckMethod&#32;)&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-125)|Pointer|<pre lang="Turtle"><code>&#91;]&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32;owl:allValuesFrom&#32; &#91;&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:allValuesFrom&#32;aec3po:FeatureOfInterest&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:onProperty&#32; &#91;&#32;owl:inverseOf&#32;aec3po:forDesign&#32;]&#32;]&#32;;  &#10; &#32; &#32; &#32; &#32;owl:onProperty&#32;aec3po:forDesign&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-125)|Pointer|<pre lang="Turtle"><code>&#91;]&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32;&#32; &#32;owl:onProperty&#32;aec3po:conforms&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-125)|Pointer|<pre lang="Turtle"><code>&#91;]&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32;&#32; &#32;owl:onProperty&#32;aec3po:verificationFocus&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-125)|Pointer|<pre lang="Turtle"><code>&#91;]&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32;&#32; &#32;owl:onProperty&#32;aec3po:hasSeverity&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-125)|Pointer|<pre lang="Turtle"><code>&#91;]&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32;owl:allValuesFrom&#32;aec3po:DocumentSubdivision&#32;;  &#10; &#32; &#32; &#32; &#32;owl:onProperty&#32;aec3po:hasSubdivision&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-125)|Pointer|<pre lang="Turtle"><code>&#91;]&#32;owl:unionOf&#32;(&#32;aec3po:Document&#32;aec3po:DocumentSubdivision&#32;)&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-125)|Pointer|<pre lang="Turtle"><code>&#91;]&#32;owl:allValuesFrom&#32;aec3po:Document&#32;;  &#10; &#32; &#32;&#32; &#32;owl:onProperty&#32;aec3po:forDocument&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-125)|Pointer|<pre lang="Turtle"><code>&#91;]&#32;a&#32;owl:Class&#32;;  &#10; &#32; &#32;&#32; &#32;owl:unionOf&#32;(&#32; &#60;https://schema.org/Place> &#32;aec3po:AdministrativeArea&#32;)&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-125)|Pointer|<pre lang="Turtle"><code>&#91;]&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32;&#32; &#32;owl:onProperty&#32;aec3po:hasSubdivision&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-125)|Pointer|<pre lang="Turtle"><code>&#91;]&#32;a&#32;owl:Class&#32;;  &#10; &#32; &#32;&#32; &#32;owl:unionOf&#32;(&#32;aec3po:Table&#32;aec3po:Image&#32;aec3po:Row&#32;aec3po:Column&#32;)&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-125)|Pointer|<pre lang="Turtle"><code>&#91;]&#32;a&#32;owl:Class&#32;;  &#10; &#32; &#32;&#32; &#32;owl:unionOf&#32;(&#32;aec3po:Table&#32;aec3po:Image&#32;aec3po:Row&#32;aec3po:Column&#32;aec3po:Cell&#32;)&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-125)|Pointer|<pre lang="Turtle"><code>&#91;]&#32;a&#32;owl:Class&#32;;  &#10; &#32; &#32;&#32; &#32;owl:unionOf&#32;(&#32;aec3po:Table&#32;aec3po:Image&#32;)&#32;.</code></pre>|

***
### MinorFail Outcome number 126

[Jump to summary definition](#summary-MinorFail-126)	|	[Previous MinorFail outcome](#minorfail-outcome-number-125)	|	[Next MinorFail outcome](#minorfail-outcome-number-127)

:exclamation:MinorFail outcome
#### Subject detail
|Name|all-modules|
|----|----|
|Title|All&#32;the&#32;modules&#32;from&#32;branch&#32;HEAD&#32;that&#32;are&#32;syntaxically&#32;correct&#32;as&#32;well&#32;as&#32;their&#32;recursive&#32;imports|
|Composition|- [Module aec3po](https://github.com/Accord-Project/aec3po/blob/HEAD/src/aec3po.ttl)<br/>- [Module check&lowbar;method](https://github.com/Accord-Project/aec3po/blob/HEAD/src/check_method.ttl)<br/>- [Module checking&lowbar;act](https://github.com/Accord-Project/aec3po/blob/HEAD/src/checking_act.ttl)<br/>- [Module compliance&lowbar;verification&lowbar;report](https://github.com/Accord-Project/aec3po/blob/HEAD/src/compliance_verification_report.ttl)<br/>- [Module data&lowbar;requirement](https://github.com/Accord-Project/aec3po/blob/HEAD/src/data_requirement.ttl)<br/>- [Module document](https://github.com/Accord-Project/aec3po/blob/HEAD/src/document.ttl)<br/>- [Module evidence](https://github.com/Accord-Project/aec3po/blob/HEAD/src/evidence.ttl)<br/>- [Module feature&lowbar;of&lowbar;interest](https://github.com/Accord-Project/aec3po/blob/HEAD/src/feature_of_interest.ttl)<br/>- [Module legal&lowbar;verifier](https://github.com/Accord-Project/aec3po/blob/HEAD/src/legal_verifier.ttl)<br/>- [Module model](https://github.com/Accord-Project/aec3po/blob/HEAD/src/model.ttl)<br/>- [Module rase&lowbar;statement](https://github.com/Accord-Project/aec3po/blob/HEAD/src/rase_statement.ttl)<br/>- [Module statement](https://github.com/Accord-Project/aec3po/blob/HEAD/src/statement.ttl)<br/>- [Module table](https://github.com/Accord-Project/aec3po/blob/HEAD/src/table.ttl)<br/>- [Module vocabularies/&lowbar;shape](https://github.com/Accord-Project/aec3po/blob/HEAD/src/vocabularies/_shape.ttl)<br/>- [Module vocabularies/administrative&lowbar;areas](https://github.com/Accord-Project/aec3po/blob/HEAD/src/vocabularies/administrative_areas.ttl)<br/>- [Module vocabularies/building&lowbar;structure](https://github.com/Accord-Project/aec3po/blob/HEAD/src/vocabularies/building_structure.ttl)<br/>- [Module vocabularies/building&lowbar;usage](https://github.com/Accord-Project/aec3po/blob/HEAD/src/vocabularies/building_usage.ttl)<br/>- [Module vocabularies/check&lowbar;method&lowbar;comparators](https://github.com/Accord-Project/aec3po/blob/HEAD/src/vocabularies/check_method_comparators.ttl)<br/>- [Module vocabularies/check&lowbar;method&lowbar;operators](https://github.com/Accord-Project/aec3po/blob/HEAD/src/vocabularies/check_method_operators.ttl)<br/>- [Module vocabularies/disciplines](https://github.com/Accord-Project/aec3po/blob/HEAD/src/vocabularies/disciplines.ttl)<br/>- [Module vocabularies/permitting&lowbar;stages](https://github.com/Accord-Project/aec3po/blob/HEAD/src/vocabularies/permitting_stages.ttl)<br/>- [Module vocabularies/quantity&lowbar;kinds](https://github.com/Accord-Project/aec3po/blob/HEAD/src/vocabularies/quantity_kinds.ttl)|

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
|[Section top](#minorfail-outcome-number-126)|Description|Class&#32;Expression&#32;not&#32;supported&#32;as&#32;object&#32;of&#32;rdfs:domain&#32;or&#32;rdfs:range|
|[Section top](#minorfail-outcome-number-126)|Pointer|<pre lang="Turtle"><code>aec3po:caption&#32;a&#32;owl:DatatypeProperty&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;caption&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;The&#32;caption&#32;of&#32;a&#32;table,&#32;image,&#32;etc.&#32; &#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:domain&#32; &#91;&#32;a&#32;owl:Class&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:unionOf&#32;(&#32;aec3po:Table&#32;aec3po:Image&#32;)&#32;]&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32;aec3po:table&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-126)|Pointer|<pre lang="Turtle"><code>aec3po:contains&#32;a&#32;owl:ObjectProperty&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;Contains&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;A&#32;container&#32;contains&#32;a&#32;table&#32;and&#32;its&#32;caption.&#32;A&#32;table&#32;contai...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:domain&#32; &#91;&#32;a&#32;owl:Class&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:unionOf&#32;(&#32;aec3po:Table&#32;aec3po:Image&#32;aec3po:Row&#32;aec3po:Column&#32;)&#32;]&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32;aec3po:table&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-126)|Pointer|<pre lang="Turtle"><code>aec3po:hasBSSDDTarget&#32;a&#32;owl:FunctionalProperty,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:ObjectProperty&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;hasBSSDDTarget&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;The&#32;target&#32;refers&#32;to&#32;either&#32;the&#32;name&#32;of&#32;an&#32;object,&#32;the&#32;name&#32;...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:domain&#32; &#91;&#32;a&#32;owl:Class&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:unionOf&#32;(&#32;aec3po:FeatureOfInterest&#32;aec3po:Property&#32;aec3po:CheckMethod&#32;)&#32;]&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32;aec3po:check&lowbar;method&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-126)|Pointer|<pre lang="Turtle"><code>aec3po:hasFirstSubdivision&#32;a&#32;owl:FunctionalProperty,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:ObjectProperty&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;has&#32;first&#32;subdivision&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;Links&#32;a&#32;document&#32;part&#32;to&#32;the&#32;first&#32;of&#32;its&#32;subdivision&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:domain&#32; &#91;&#32;owl:unionOf&#32;(&#32;aec3po:Document&#32;aec3po:DocumentSubdivision&#32;)&#32;]&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32;aec3po:document&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:range&#32;aec3po:DocumentSubdivision&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:subPropertyOf&#32;aec3po:hasSubdivision&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-126)|Pointer|<pre lang="Turtle"><code>aec3po:hasSubdivision&#32;a&#32;owl:ObjectProperty&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;has&#32;subdivision&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;links&#32;a&#32;document&#32;part&#32;to&#32;some&#32;of&#32;its&#32;subdivision&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:domain&#32; &#91;&#32;owl:unionOf&#32;(&#32;aec3po:Document&#32;aec3po:DocumentSubdivision&#32;)&#32;]&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32;aec3po:document&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:range&#32;aec3po:DocumentSubdivision&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:subPropertyOf&#32;dc:hasPart&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-126)|Pointer|<pre lang="Turtle"><code>aec3po:hasUnit&#32;a&#32;owl:FunctionalProperty,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:ObjectProperty&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;hasUnit&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;the&#32;hasUnit&#32;property&#32;is&#32;used&#32;to&#32;link&#32;a&#32;specific&#32;property&#32;or&#32;...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:domain&#32; &#91;&#32;a&#32;owl:Class&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:unionOf&#32;(&#32;aec3po:FeatureOfInterest&#32;aec3po:Property&#32;aec3po:CheckMethod&#32;)&#32;]&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32;aec3po:check&lowbar;method&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:range&#32;qudt:Unit&#32;;  &#10; &#32; &#32; &#32; &#32;owl:eqivalentProperty&#32;qudt:hasValue&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-126)|Pointer|<pre lang="Turtle"><code>aec3po:hasValue&#32;a&#32;owl:DatatypeProperty,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:FunctionalProperty&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;has&#32;value&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;de&#32;facto&#32;used&#32;to&#32;link&#32;something&#32;(anything:&#32;property,&#32;propert...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:domain&#32; &#91;&#32;a&#32;owl:Class&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:unionOf&#32;(&#32;aec3po:FeatureOfInterest&#32;aec3po:Property&#32;aec3po:CheckMethod&#32;)&#32;]&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32;aec3po:&#32;;  &#10; &#32; &#32; &#32; &#32;skos:note&#32; &#34;The&#32;value&#32;of&#32;the&#32;literal&#32;may&#32;be&#32;a&#32;XSD&#32;literal&#32;(boolean,&#32;inte...&#34; &#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-126)|Pointer|<pre lang="Turtle"><code>aec3po:isContainedIn&#32;a&#32;owl:ObjectProperty&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;is&#32;contained&#32;by&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;A&#32;table&#32;contains&#32;row,&#32;columns&#32;and&#32;other&#32;elements.&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32;aec3po:table&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:range&#32; &#91;&#32;a&#32;owl:Class&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:unionOf&#32;(&#32;aec3po:Table&#32;aec3po:Image&#32;aec3po:Row&#32;aec3po:Column&#32;aec3po:Cell&#32;)&#32;]&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-126)|Pointer|<pre lang="Turtle"><code>aec3po:locationCoverage&#32;a&#32;owl:ObjectProperty&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;location&#32;coverage&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;The&#32;spatialCoverage&#32;indicates&#32;the&#32;place(s)&#32;or&#32;the&#32;administra...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:domain&#32; &#60;https://schema.org/Model> &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:range&#32; &#91;&#32;a&#32;owl:Class&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:unionOf&#32;(&#32; &#60;https://schema.org/Place> &#32;aec3po:AdministrativeArea&#32;)&#32;]&#32;;  &#10; &#32; &#32; &#32; &#32;owl:equivalentProperty&#32; &#60;https://schema.org/spatialCoverage> &#32;.</code></pre>|

***
### MinorFail Outcome number 127

[Jump to summary definition](#summary-MinorFail-127)	|	[Previous MinorFail outcome](#minorfail-outcome-number-126)	|	[Next MinorFail outcome](#minorfail-outcome-number-128)

:exclamation:MinorFail outcome
#### Subject detail
|Name|all-modules|
|----|----|
|Title|All&#32;the&#32;modules&#32;from&#32;branch&#32;HEAD&#32;that&#32;are&#32;syntaxically&#32;correct&#32;as&#32;well&#32;as&#32;their&#32;recursive&#32;imports|
|Composition|- [Module aec3po](https://github.com/Accord-Project/aec3po/blob/HEAD/src/aec3po.ttl)<br/>- [Module check&lowbar;method](https://github.com/Accord-Project/aec3po/blob/HEAD/src/check_method.ttl)<br/>- [Module checking&lowbar;act](https://github.com/Accord-Project/aec3po/blob/HEAD/src/checking_act.ttl)<br/>- [Module compliance&lowbar;verification&lowbar;report](https://github.com/Accord-Project/aec3po/blob/HEAD/src/compliance_verification_report.ttl)<br/>- [Module data&lowbar;requirement](https://github.com/Accord-Project/aec3po/blob/HEAD/src/data_requirement.ttl)<br/>- [Module document](https://github.com/Accord-Project/aec3po/blob/HEAD/src/document.ttl)<br/>- [Module evidence](https://github.com/Accord-Project/aec3po/blob/HEAD/src/evidence.ttl)<br/>- [Module feature&lowbar;of&lowbar;interest](https://github.com/Accord-Project/aec3po/blob/HEAD/src/feature_of_interest.ttl)<br/>- [Module legal&lowbar;verifier](https://github.com/Accord-Project/aec3po/blob/HEAD/src/legal_verifier.ttl)<br/>- [Module model](https://github.com/Accord-Project/aec3po/blob/HEAD/src/model.ttl)<br/>- [Module rase&lowbar;statement](https://github.com/Accord-Project/aec3po/blob/HEAD/src/rase_statement.ttl)<br/>- [Module statement](https://github.com/Accord-Project/aec3po/blob/HEAD/src/statement.ttl)<br/>- [Module table](https://github.com/Accord-Project/aec3po/blob/HEAD/src/table.ttl)<br/>- [Module vocabularies/&lowbar;shape](https://github.com/Accord-Project/aec3po/blob/HEAD/src/vocabularies/_shape.ttl)<br/>- [Module vocabularies/administrative&lowbar;areas](https://github.com/Accord-Project/aec3po/blob/HEAD/src/vocabularies/administrative_areas.ttl)<br/>- [Module vocabularies/building&lowbar;structure](https://github.com/Accord-Project/aec3po/blob/HEAD/src/vocabularies/building_structure.ttl)<br/>- [Module vocabularies/building&lowbar;usage](https://github.com/Accord-Project/aec3po/blob/HEAD/src/vocabularies/building_usage.ttl)<br/>- [Module vocabularies/check&lowbar;method&lowbar;comparators](https://github.com/Accord-Project/aec3po/blob/HEAD/src/vocabularies/check_method_comparators.ttl)<br/>- [Module vocabularies/check&lowbar;method&lowbar;operators](https://github.com/Accord-Project/aec3po/blob/HEAD/src/vocabularies/check_method_operators.ttl)<br/>- [Module vocabularies/disciplines](https://github.com/Accord-Project/aec3po/blob/HEAD/src/vocabularies/disciplines.ttl)<br/>- [Module vocabularies/permitting&lowbar;stages](https://github.com/Accord-Project/aec3po/blob/HEAD/src/vocabularies/permitting_stages.ttl)<br/>- [Module vocabularies/quantity&lowbar;kinds](https://github.com/Accord-Project/aec3po/blob/HEAD/src/vocabularies/quantity_kinds.ttl)|

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
|[Section top](#minorfail-outcome-number-127)|Description|Class&#32;Expression&#32;not&#32;supported&#32;with&#32;owl:equivalentClass|
|[Section top](#minorfail-outcome-number-127)|Pointer|<pre lang="Turtle"><code>aec3po:AdministrativeArea&#32;a&#32;owl:Class&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;Administrative&#32;Area&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;Formally&#32;defined&#32;as&#32;the&#32;set&#32;of&#32;skos:Concept&#32;either&#32;in&#32;concep...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32;aec3po:administrative&lowbar;areas&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:seeAlso&#32; &#60;https://op.europa.eu/en/web/eu-vocabularies/concept-scheme/-/resource?uri=http://publications.europa.eu/resource/authority/atu> &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:subClassOf&#32;skos:Concept&#32;;  &#10; &#32; &#32; &#32; &#32;owl:equivalentClass&#32; &#91;&#32;owl:intersectionOf&#32;(&#32;skos:Concept&#32; &#91;&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:hasValue&#32;aec3po:AdministrativeAreaNomenclature&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:onProperty&#32;skos:inScheme&#32;]&#32;)&#32;],  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#60;http://data.europa.eu/eli/ontology#AdministrativeArea> &#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-127)|Pointer|<pre lang="Turtle"><code>aec3po:BuildingStructure&#32;a&#32;owl:Class&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;building&#32;structure&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;Formally&#32;defined&#32;as&#32;the&#32;set&#32;of&#32;skos:Concept&#32;in&#32;concept&#32;schem...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32;aec3po:building&lowbar;structure&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:subClassOf&#32;skos:Concept,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;aec3po:Design&#32;;  &#10; &#32; &#32; &#32; &#32;owl:equivalentClass&#32; &#91;&#32;owl:intersectionOf&#32;(&#32;skos:Concept&#32; &#91;&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:hasValue&#32;aec3po:BuildingStructureNomenclature&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:onProperty&#32;skos:inScheme&#32;]&#32;)&#32;]&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-127)|Pointer|<pre lang="Turtle"><code>aec3po:BuildingUsage&#32;a&#32;owl:Class&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;building&#32;usage&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;Formally&#32;defined&#32;as&#32;the&#32;set&#32;of&#32;skos:Concept&#32;in&#32;concept&#32;schem...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32;aec3po:building&lowbar;usage&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:subClassOf&#32;skos:Concept,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;aec3po:Design&#32;;  &#10; &#32; &#32; &#32; &#32;owl:equivalentClass&#32; &#91;&#32;owl:intersectionOf&#32;(&#32;skos:Concept&#32; &#91;&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:hasValue&#32;aec3po:BuildingUsageNomenclature&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:onProperty&#32;skos:inScheme&#32;]&#32;)&#32;]&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-127)|Pointer|<pre lang="Turtle"><code>aec3po:CheckMethodComparator&#32;a&#32;owl:Class&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;check&#32;method&#32;comparator&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;Formally&#32;defined&#32;as&#32;the&#32;set&#32;of&#32;skos:Concept&#32;in&#32;concept&#32;schem...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32;aec3po:check&lowbar;method&lowbar;comparators&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:subClassOf&#32;skos:Concept,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;aec3po:CheckMethod&#32;;  &#10; &#32; &#32; &#32; &#32;owl:equivalentClass&#32; &#91;&#32;owl:intersectionOf&#32;(&#32;skos:Concept&#32; &#91;&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:hasValue&#32;aec3po:CheckMethodComparatorNomenclature&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:onProperty&#32;skos:inScheme&#32;]&#32;)&#32;]&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-127)|Pointer|<pre lang="Turtle"><code>aec3po:CheckMethodOperator&#32;a&#32;owl:Class&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;check&#32;method&#32;operator&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;Formally&#32;defined&#32;as&#32;the&#32;set&#32;of&#32;skos:Concept&#32;in&#32;concept&#32;schem...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32;aec3po:check&lowbar;method&lowbar;operators&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:subClassOf&#32;skos:Concept,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;aec3po:CheckMethod&#32;;  &#10; &#32; &#32; &#32; &#32;owl:equivalentClass&#32; &#91;&#32;owl:intersectionOf&#32;(&#32;skos:Concept&#32; &#91;&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:hasValue&#32;aec3po:CheckMethodOperatorNomenclature&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:onProperty&#32;skos:inScheme&#32;]&#32;)&#32;]&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-127)|Pointer|<pre lang="Turtle"><code>aec3po:ComponentCheckMethod&#32;a&#32;owl:Class&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;Component&#32;Check&#32;Method&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;Component&#32;check&#32;method&#32;refers&#32;to&#32;a&#32;process&#32;of&#32;inspecting&#32;and...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32;aec3po:check&lowbar;method&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:subClassOf&#32;aec3po:CheckMethod&#32;;  &#10; &#32; &#32; &#32; &#32;owl:equivalentClass&#32; &#91;&#32;a&#32;owl:Class&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:intersectionOf&#32;(&#32;aec3po:CheckMethod&#32; &#91;&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:allValuesFrom&#32; &#91;&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:allValuesFrom&#32;aec3po:FeatureOfInterest&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:onProperty&#32; &#91;&#32;owl:inverseOf&#32;aec3po:forDesign&#32;]&#32;]&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:onProperty&#32;aec3po:forDesign&#32;]&#32;)&#32;]&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-127)|Pointer|<pre lang="Turtle"><code>aec3po:Discipline&#32;a&#32;owl:Class&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;Discipline&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;The&#32;AEC&#32;discipline&#32;to&#32;which&#32;something&#32;pertains.&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32;aec3po:discipline&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:subClassOf&#32;skos:Concept&#32;;  &#10; &#32; &#32; &#32; &#32;owl:equivalentClass&#32; &#91;&#32;owl:intersectionOf&#32;(&#32;skos:Concept&#32; &#91;&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:hasValue&#32;aec3po:DisciplineNomenclature&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:onProperty&#32;skos:inScheme&#32;]&#32;)&#32;]&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-127)|Pointer|<pre lang="Turtle"><code>aec3po:PermittingStage&#32;a&#32;owl:Class&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;Permitting&#32;Stage&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;The&#32;class&#32;of&#32;permitting&#32;stages.&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32;aec3po:permitting&lowbar;stage&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:subClassOf&#32;skos:Concept&#32;;  &#10; &#32; &#32; &#32; &#32;owl:equivalentClass&#32; &#91;&#32;owl:intersectionOf&#32;(&#32;skos:Concept&#32; &#91;&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:hasValue&#32;aec3po:PermittingStageNomenclature&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:onProperty&#32;skos:inScheme&#32;]&#32;)&#32;]&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-127)|Pointer|<pre lang="Turtle"><code>aec3po:QuantityKind&#32;a&#32;owl:Class&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;Quantity&#32;Kind&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;A&#32;Quantity&#32;Kind&#32;is&#32;any&#32;observable&#32;property&#32;that&#32;can&#32;be&#32;quant...&#34;,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#34;A&#32;kind&#32;of&#32;quantity.&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32;aec3po:feature&lowbar;of&lowbar;interest,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;aec3po:quantity&lowbar;kinds&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:subClassOf&#32;qudt:QuantityKind,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#60;http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#Region>,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;skos:Concept&#32;;  &#10; &#32; &#32; &#32; &#32;owl:equivalentClass&#32; &#91;&#32;owl:intersectionOf&#32;(&#32;skos:Concept&#32; &#91;&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:hasValue&#32;aec3po:QuantityKindNomenclature&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:onProperty&#32;skos:inScheme&#32;]&#32;)&#32;]&#32;;  &#10; &#32; &#32; &#32; &#32;skos:example&#32; &#34;Length,&#32;Area,&#32;U-Value.&#34;@en,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#34;height,&#32;area,&#32;U-value&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;skos:note&#32; &#34;Maxime&#32;Lefrançois&#32;argues&#32;that&#32;both&#32;qudt:QuantityKind&#32;and&#32;qud...&#34; &#32;.</code></pre>|

***
### MinorFail Outcome number 128

[Jump to summary definition](#summary-MinorFail-128)	|	[Previous MinorFail outcome](#minorfail-outcome-number-127)	|	[Next MinorFail outcome](#minorfail-outcome-number-129)

:exclamation:MinorFail outcome
#### Subject detail
|Name|all-modules|
|----|----|
|Title|All&#32;the&#32;modules&#32;from&#32;branch&#32;HEAD&#32;that&#32;are&#32;syntaxically&#32;correct&#32;as&#32;well&#32;as&#32;their&#32;recursive&#32;imports|
|Composition|- [Module aec3po](https://github.com/Accord-Project/aec3po/blob/HEAD/src/aec3po.ttl)<br/>- [Module check&lowbar;method](https://github.com/Accord-Project/aec3po/blob/HEAD/src/check_method.ttl)<br/>- [Module checking&lowbar;act](https://github.com/Accord-Project/aec3po/blob/HEAD/src/checking_act.ttl)<br/>- [Module compliance&lowbar;verification&lowbar;report](https://github.com/Accord-Project/aec3po/blob/HEAD/src/compliance_verification_report.ttl)<br/>- [Module data&lowbar;requirement](https://github.com/Accord-Project/aec3po/blob/HEAD/src/data_requirement.ttl)<br/>- [Module document](https://github.com/Accord-Project/aec3po/blob/HEAD/src/document.ttl)<br/>- [Module evidence](https://github.com/Accord-Project/aec3po/blob/HEAD/src/evidence.ttl)<br/>- [Module feature&lowbar;of&lowbar;interest](https://github.com/Accord-Project/aec3po/blob/HEAD/src/feature_of_interest.ttl)<br/>- [Module legal&lowbar;verifier](https://github.com/Accord-Project/aec3po/blob/HEAD/src/legal_verifier.ttl)<br/>- [Module model](https://github.com/Accord-Project/aec3po/blob/HEAD/src/model.ttl)<br/>- [Module rase&lowbar;statement](https://github.com/Accord-Project/aec3po/blob/HEAD/src/rase_statement.ttl)<br/>- [Module statement](https://github.com/Accord-Project/aec3po/blob/HEAD/src/statement.ttl)<br/>- [Module table](https://github.com/Accord-Project/aec3po/blob/HEAD/src/table.ttl)<br/>- [Module vocabularies/&lowbar;shape](https://github.com/Accord-Project/aec3po/blob/HEAD/src/vocabularies/_shape.ttl)<br/>- [Module vocabularies/administrative&lowbar;areas](https://github.com/Accord-Project/aec3po/blob/HEAD/src/vocabularies/administrative_areas.ttl)<br/>- [Module vocabularies/building&lowbar;structure](https://github.com/Accord-Project/aec3po/blob/HEAD/src/vocabularies/building_structure.ttl)<br/>- [Module vocabularies/building&lowbar;usage](https://github.com/Accord-Project/aec3po/blob/HEAD/src/vocabularies/building_usage.ttl)<br/>- [Module vocabularies/check&lowbar;method&lowbar;comparators](https://github.com/Accord-Project/aec3po/blob/HEAD/src/vocabularies/check_method_comparators.ttl)<br/>- [Module vocabularies/check&lowbar;method&lowbar;operators](https://github.com/Accord-Project/aec3po/blob/HEAD/src/vocabularies/check_method_operators.ttl)<br/>- [Module vocabularies/disciplines](https://github.com/Accord-Project/aec3po/blob/HEAD/src/vocabularies/disciplines.ttl)<br/>- [Module vocabularies/permitting&lowbar;stages](https://github.com/Accord-Project/aec3po/blob/HEAD/src/vocabularies/permitting_stages.ttl)<br/>- [Module vocabularies/quantity&lowbar;kinds](https://github.com/Accord-Project/aec3po/blob/HEAD/src/vocabularies/quantity_kinds.ttl)|

#### Criterion detail
|Identifier|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|
|----|----|
|Title|Profile&#32;compatibility&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;check&#32;whether&#32;the&#32;test&#32;subject&#32;is&#32;compatible&#32;with&#32;a&#32;profile&#32;or&#32;not,&#32;and&#32;if&#32;it&#32;is&#32;not,&#32;why.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-128)|Identifier|`owl-ql-profile-error`|
|[Section top](#minorfail-outcome-number-128)|Title|OWL&#32;QL&#32;Profile&#32;incompatible|
|[Section top](#minorfail-outcome-number-128)|Description|Class&#32;Expression&#32;not&#32;supported&#32;with&#32;rdfs:subClassOf|
|[Section top](#minorfail-outcome-number-128)|Pointer|<pre lang="Turtle"><code>aec3po:AndCheckStatement&#32;a&#32;owl:Class&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;And&#32;Check&#32;Statement&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;Check&#32;verified&#32;if&#32;and&#32;only&#32;if&#32;all&#32;of&#32;its&#32;sub-checks&#32;are&#32;veri...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32;aec3po:statement&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:subClassOf&#32; &#91;&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:onProperty&#32;aec3po:hasSubdivision&#32;],  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;aec3po:ChecklistStatement&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-128)|Pointer|<pre lang="Turtle"><code>aec3po:ComplianceVerificationReport&#32;a&#32;owl:Class&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;Compliance&#32;Verification&#32;Report&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;Result&#32;of&#32;a&#32;checking&#32;act.&#32;May&#32;be&#32;compliant&#32;or&#32;not.&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32;aec3po:compliance&lowbar;verification&lowbar;report&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:subClassOf&#32; &#91;&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:onProperty&#32;aec3po:conforms&#32;]&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-128)|Pointer|<pre lang="Turtle"><code>aec3po:DocumentSubdivision&#32;a&#32;owl:Class&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;Document&#32;Subdivision&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;Any&#32;subdivision&#32;of&#32;a&#32;document,&#32;including&#32;sections,&#32;paragraph...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32;aec3po:document&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:subClassOf&#32; &#91;&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:allValuesFrom&#32;aec3po:DocumentSubdivision&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:onProperty&#32;aec3po:hasSubdivision&#32;]&#32;;  &#10; &#32; &#32; &#32; &#32;skos:example&#32; &#34;Paragraph,&#32;section,&#32;definition...&#34;@en&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-128)|Pointer|<pre lang="Turtle"><code>aec3po:LegalVerifier&#32;a&#32;owl:Class&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;Legal&#32;Verifier&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;An&#32;entity&#32;that&#32;has&#32;the&#32;legal&#32;capacity&#32;to&#32;verify&#32;compliance&#32;w...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32;aec3po:legal&lowbar;verifier&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:subClassOf&#32; &#91;&#32;owl:allValuesFrom&#32;aec3po:Document&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:onProperty&#32;aec3po:forDocument&#32;],  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;foaf:Agent&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-128)|Pointer|<pre lang="Turtle"><code>aec3po:NotCheckStatement&#32;a&#32;owl:Class&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;Not&#32;Check&#32;Statement&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;Check&#32;verified&#32;if&#32;and&#32;only&#32;if&#32;the&#32;sub-check&#32;is&#32;not&#32;verified.&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32;aec3po:statement&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:subClassOf&#32; &#91;&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:onProperty&#32;aec3po:hasSubdivision&#32;]&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-128)|Pointer|<pre lang="Turtle"><code>aec3po:OrCheckStatement&#32;a&#32;owl:Class&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;Or&#32;Check&#32;Statement&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;Check&#32;verified&#32;if&#32;and&#32;only&#32;if&#32;at&#32;least&#32;one&#32;of&#32;its&#32;sub-checks...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32;aec3po:statement&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:subClassOf&#32; &#91;&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:onProperty&#32;aec3po:hasSubdivision&#32;],  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;aec3po:ChecklistStatement&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-128)|Pointer|<pre lang="Turtle"><code>aec3po:VerificationResult&#32;a&#32;owl:Class&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;Verification&#32;Result&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;Individual&#32;verification&#32;result&#32;of&#32;a&#32;Compliance&#32;Verification&#32;...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32;aec3po:compliance&lowbar;verification&lowbar;report&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:subClassOf&#32; &#91;&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:onProperty&#32;aec3po:verificationFocus&#32;],  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#91;&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:onProperty&#32;aec3po:hasSeverity&#32;]&#32;.</code></pre>|

***
### MinorFail Outcome number 129

[Jump to summary definition](#summary-MinorFail-129)	|	[Previous MinorFail outcome](#minorfail-outcome-number-128)	|	[Next MinorFail outcome](#minorfail-outcome-number-130)

:exclamation:MinorFail outcome
#### Subject detail
|Name|all-modules|
|----|----|
|Title|All&#32;the&#32;modules&#32;from&#32;branch&#32;HEAD&#32;that&#32;are&#32;syntaxically&#32;correct&#32;as&#32;well&#32;as&#32;their&#32;recursive&#32;imports|
|Composition|- [Module aec3po](https://github.com/Accord-Project/aec3po/blob/HEAD/src/aec3po.ttl)<br/>- [Module check&lowbar;method](https://github.com/Accord-Project/aec3po/blob/HEAD/src/check_method.ttl)<br/>- [Module checking&lowbar;act](https://github.com/Accord-Project/aec3po/blob/HEAD/src/checking_act.ttl)<br/>- [Module compliance&lowbar;verification&lowbar;report](https://github.com/Accord-Project/aec3po/blob/HEAD/src/compliance_verification_report.ttl)<br/>- [Module data&lowbar;requirement](https://github.com/Accord-Project/aec3po/blob/HEAD/src/data_requirement.ttl)<br/>- [Module document](https://github.com/Accord-Project/aec3po/blob/HEAD/src/document.ttl)<br/>- [Module evidence](https://github.com/Accord-Project/aec3po/blob/HEAD/src/evidence.ttl)<br/>- [Module feature&lowbar;of&lowbar;interest](https://github.com/Accord-Project/aec3po/blob/HEAD/src/feature_of_interest.ttl)<br/>- [Module legal&lowbar;verifier](https://github.com/Accord-Project/aec3po/blob/HEAD/src/legal_verifier.ttl)<br/>- [Module model](https://github.com/Accord-Project/aec3po/blob/HEAD/src/model.ttl)<br/>- [Module rase&lowbar;statement](https://github.com/Accord-Project/aec3po/blob/HEAD/src/rase_statement.ttl)<br/>- [Module statement](https://github.com/Accord-Project/aec3po/blob/HEAD/src/statement.ttl)<br/>- [Module table](https://github.com/Accord-Project/aec3po/blob/HEAD/src/table.ttl)<br/>- [Module vocabularies/&lowbar;shape](https://github.com/Accord-Project/aec3po/blob/HEAD/src/vocabularies/_shape.ttl)<br/>- [Module vocabularies/administrative&lowbar;areas](https://github.com/Accord-Project/aec3po/blob/HEAD/src/vocabularies/administrative_areas.ttl)<br/>- [Module vocabularies/building&lowbar;structure](https://github.com/Accord-Project/aec3po/blob/HEAD/src/vocabularies/building_structure.ttl)<br/>- [Module vocabularies/building&lowbar;usage](https://github.com/Accord-Project/aec3po/blob/HEAD/src/vocabularies/building_usage.ttl)<br/>- [Module vocabularies/check&lowbar;method&lowbar;comparators](https://github.com/Accord-Project/aec3po/blob/HEAD/src/vocabularies/check_method_comparators.ttl)<br/>- [Module vocabularies/check&lowbar;method&lowbar;operators](https://github.com/Accord-Project/aec3po/blob/HEAD/src/vocabularies/check_method_operators.ttl)<br/>- [Module vocabularies/disciplines](https://github.com/Accord-Project/aec3po/blob/HEAD/src/vocabularies/disciplines.ttl)<br/>- [Module vocabularies/permitting&lowbar;stages](https://github.com/Accord-Project/aec3po/blob/HEAD/src/vocabularies/permitting_stages.ttl)<br/>- [Module vocabularies/quantity&lowbar;kinds](https://github.com/Accord-Project/aec3po/blob/HEAD/src/vocabularies/quantity_kinds.ttl)|

#### Criterion detail
|Identifier|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|
|----|----|
|Title|Profile&#32;compatibility&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;check&#32;whether&#32;the&#32;test&#32;subject&#32;is&#32;compatible&#32;with&#32;a&#32;profile&#32;or&#32;not,&#32;and&#32;if&#32;it&#32;is&#32;not,&#32;why.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-129)|Identifier|`owl-ql-profile-error`|
|[Section top](#minorfail-outcome-number-129)|Title|OWL&#32;QL&#32;Profile&#32;incompatible|
|[Section top](#minorfail-outcome-number-129)|Description|Restriction&#32;on&#32;datatypes|
|[Section top](#minorfail-outcome-number-129)|Pointer|<pre lang="Turtle"><code>aec3po:conforms&#32;a&#32;owl:DatatypeProperty&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;conforms&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;True&#32;if&#32;the&#32;Checking&#32;act&#32;confirms&#32;the&#32;check&#32;was&#32;validated,&#32;a...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:domain&#32;aec3po:ComplianceVerificationReport&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32;aec3po:compliance&lowbar;verification&lowbar;report&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:range&#32;xsd:boolean&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-129)|Pointer|<pre lang="Turtle"><code>aec3po:hasBooleanTarget&#32;a&#32;owl:DatatypeProperty&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;hasBooleanTarget&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;TBD&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:range&#32;xsd:boolean&#32;.</code></pre>|

***
### MinorFail Outcome number 130

[Jump to summary definition](#summary-MinorFail-130)	|	[Previous MinorFail outcome](#minorfail-outcome-number-129)	|	[Next MinorFail outcome](#minorfail-outcome-number-131)

:exclamation:MinorFail outcome
#### Subject detail
|Name|all-modules|
|----|----|
|Title|All&#32;the&#32;modules&#32;from&#32;branch&#32;HEAD&#32;that&#32;are&#32;syntaxically&#32;correct&#32;as&#32;well&#32;as&#32;their&#32;recursive&#32;imports|
|Composition|- [Module aec3po](https://github.com/Accord-Project/aec3po/blob/HEAD/src/aec3po.ttl)<br/>- [Module check&lowbar;method](https://github.com/Accord-Project/aec3po/blob/HEAD/src/check_method.ttl)<br/>- [Module checking&lowbar;act](https://github.com/Accord-Project/aec3po/blob/HEAD/src/checking_act.ttl)<br/>- [Module compliance&lowbar;verification&lowbar;report](https://github.com/Accord-Project/aec3po/blob/HEAD/src/compliance_verification_report.ttl)<br/>- [Module data&lowbar;requirement](https://github.com/Accord-Project/aec3po/blob/HEAD/src/data_requirement.ttl)<br/>- [Module document](https://github.com/Accord-Project/aec3po/blob/HEAD/src/document.ttl)<br/>- [Module evidence](https://github.com/Accord-Project/aec3po/blob/HEAD/src/evidence.ttl)<br/>- [Module feature&lowbar;of&lowbar;interest](https://github.com/Accord-Project/aec3po/blob/HEAD/src/feature_of_interest.ttl)<br/>- [Module legal&lowbar;verifier](https://github.com/Accord-Project/aec3po/blob/HEAD/src/legal_verifier.ttl)<br/>- [Module model](https://github.com/Accord-Project/aec3po/blob/HEAD/src/model.ttl)<br/>- [Module rase&lowbar;statement](https://github.com/Accord-Project/aec3po/blob/HEAD/src/rase_statement.ttl)<br/>- [Module statement](https://github.com/Accord-Project/aec3po/blob/HEAD/src/statement.ttl)<br/>- [Module table](https://github.com/Accord-Project/aec3po/blob/HEAD/src/table.ttl)<br/>- [Module vocabularies/&lowbar;shape](https://github.com/Accord-Project/aec3po/blob/HEAD/src/vocabularies/_shape.ttl)<br/>- [Module vocabularies/administrative&lowbar;areas](https://github.com/Accord-Project/aec3po/blob/HEAD/src/vocabularies/administrative_areas.ttl)<br/>- [Module vocabularies/building&lowbar;structure](https://github.com/Accord-Project/aec3po/blob/HEAD/src/vocabularies/building_structure.ttl)<br/>- [Module vocabularies/building&lowbar;usage](https://github.com/Accord-Project/aec3po/blob/HEAD/src/vocabularies/building_usage.ttl)<br/>- [Module vocabularies/check&lowbar;method&lowbar;comparators](https://github.com/Accord-Project/aec3po/blob/HEAD/src/vocabularies/check_method_comparators.ttl)<br/>- [Module vocabularies/check&lowbar;method&lowbar;operators](https://github.com/Accord-Project/aec3po/blob/HEAD/src/vocabularies/check_method_operators.ttl)<br/>- [Module vocabularies/disciplines](https://github.com/Accord-Project/aec3po/blob/HEAD/src/vocabularies/disciplines.ttl)<br/>- [Module vocabularies/permitting&lowbar;stages](https://github.com/Accord-Project/aec3po/blob/HEAD/src/vocabularies/permitting_stages.ttl)<br/>- [Module vocabularies/quantity&lowbar;kinds](https://github.com/Accord-Project/aec3po/blob/HEAD/src/vocabularies/quantity_kinds.ttl)|

#### Criterion detail
|Identifier|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|
|----|----|
|Title|Profile&#32;compatibility&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;check&#32;whether&#32;the&#32;test&#32;subject&#32;is&#32;compatible&#32;with&#32;a&#32;profile&#32;or&#32;not,&#32;and&#32;if&#32;it&#32;is&#32;not,&#32;why.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-130)|Identifier|`owl-ql-profile-error`|
|[Section top](#minorfail-outcome-number-130)|Title|OWL&#32;QL&#32;Profile&#32;incompatible|
|[Section top](#minorfail-outcome-number-130)|Description|Statement&#32;not&#32;supported&#32;in&#32;a&#32;Sub&#32;Class&#32;Expression|
|[Section top](#minorfail-outcome-number-130)|Pointer|<pre lang="Turtle"><code>&#91;]&#32;a&#32;owl:Class&#32;;  &#10; &#32; &#32; &#32; &#32;owl:intersectionOf&#32;(&#32;aec3po:CheckMethod&#32; &#91;&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:allValuesFrom&#32; &#91;&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:allValuesFrom&#32;aec3po:FeatureOfInterest&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:onProperty&#32; &#91;&#32;owl:inverseOf&#32;aec3po:forDesign&#32;]&#32;]&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:onProperty&#32;aec3po:forDesign&#32;]&#32;)&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-130)|Pointer|<pre lang="Turtle"><code>&#91;]&#32;owl:intersectionOf&#32;(&#32;skos:Concept&#32; &#91;&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:hasValue&#32;aec3po:AdministrativeAreaNomenclature&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:onProperty&#32;skos:inScheme&#32;]&#32;)&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-130)|Pointer|<pre lang="Turtle"><code>&#91;]&#32;owl:intersectionOf&#32;(&#32;skos:Concept&#32; &#91;&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:hasValue&#32;aec3po:BuildingStructureNomenclature&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:onProperty&#32;skos:inScheme&#32;]&#32;)&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-130)|Pointer|<pre lang="Turtle"><code>&#91;]&#32;owl:intersectionOf&#32;(&#32;skos:Concept&#32; &#91;&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:hasValue&#32;aec3po:BuildingUsageNomenclature&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:onProperty&#32;skos:inScheme&#32;]&#32;)&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-130)|Pointer|<pre lang="Turtle"><code>&#91;]&#32;owl:intersectionOf&#32;(&#32;skos:Concept&#32; &#91;&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:hasValue&#32;aec3po:CheckMethodComparatorNomenclature&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:onProperty&#32;skos:inScheme&#32;]&#32;)&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-130)|Pointer|<pre lang="Turtle"><code>&#91;]&#32;owl:intersectionOf&#32;(&#32;skos:Concept&#32; &#91;&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:hasValue&#32;aec3po:CheckMethodOperatorNomenclature&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:onProperty&#32;skos:inScheme&#32;]&#32;)&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-130)|Pointer|<pre lang="Turtle"><code>&#91;]&#32;owl:intersectionOf&#32;(&#32;skos:Concept&#32; &#91;&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:hasValue&#32;aec3po:DisciplineNomenclature&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:onProperty&#32;skos:inScheme&#32;]&#32;)&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-130)|Pointer|<pre lang="Turtle"><code>&#91;]&#32;owl:intersectionOf&#32;(&#32;skos:Concept&#32; &#91;&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:hasValue&#32;aec3po:PermittingStageNomenclature&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:onProperty&#32;skos:inScheme&#32;]&#32;)&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-130)|Pointer|<pre lang="Turtle"><code>&#91;]&#32;owl:intersectionOf&#32;(&#32;skos:Concept&#32; &#91;&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:hasValue&#32;aec3po:QuantityKindNomenclature&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:onProperty&#32;skos:inScheme&#32;]&#32;)&#32;.</code></pre>|

***
### MinorFail Outcome number 131

[Jump to summary definition](#summary-MinorFail-131)	|	[Previous MinorFail outcome](#minorfail-outcome-number-130)	|	[Next MinorFail outcome](#minorfail-outcome-number-132)

:exclamation:MinorFail outcome
#### Subject detail
|Name|all-modules|
|----|----|
|Title|All&#32;the&#32;modules&#32;from&#32;branch&#32;HEAD&#32;that&#32;are&#32;syntaxically&#32;correct&#32;as&#32;well&#32;as&#32;their&#32;recursive&#32;imports|
|Composition|- [Module aec3po](https://github.com/Accord-Project/aec3po/blob/HEAD/src/aec3po.ttl)<br/>- [Module check&lowbar;method](https://github.com/Accord-Project/aec3po/blob/HEAD/src/check_method.ttl)<br/>- [Module checking&lowbar;act](https://github.com/Accord-Project/aec3po/blob/HEAD/src/checking_act.ttl)<br/>- [Module compliance&lowbar;verification&lowbar;report](https://github.com/Accord-Project/aec3po/blob/HEAD/src/compliance_verification_report.ttl)<br/>- [Module data&lowbar;requirement](https://github.com/Accord-Project/aec3po/blob/HEAD/src/data_requirement.ttl)<br/>- [Module document](https://github.com/Accord-Project/aec3po/blob/HEAD/src/document.ttl)<br/>- [Module evidence](https://github.com/Accord-Project/aec3po/blob/HEAD/src/evidence.ttl)<br/>- [Module feature&lowbar;of&lowbar;interest](https://github.com/Accord-Project/aec3po/blob/HEAD/src/feature_of_interest.ttl)<br/>- [Module legal&lowbar;verifier](https://github.com/Accord-Project/aec3po/blob/HEAD/src/legal_verifier.ttl)<br/>- [Module model](https://github.com/Accord-Project/aec3po/blob/HEAD/src/model.ttl)<br/>- [Module rase&lowbar;statement](https://github.com/Accord-Project/aec3po/blob/HEAD/src/rase_statement.ttl)<br/>- [Module statement](https://github.com/Accord-Project/aec3po/blob/HEAD/src/statement.ttl)<br/>- [Module table](https://github.com/Accord-Project/aec3po/blob/HEAD/src/table.ttl)<br/>- [Module vocabularies/&lowbar;shape](https://github.com/Accord-Project/aec3po/blob/HEAD/src/vocabularies/_shape.ttl)<br/>- [Module vocabularies/administrative&lowbar;areas](https://github.com/Accord-Project/aec3po/blob/HEAD/src/vocabularies/administrative_areas.ttl)<br/>- [Module vocabularies/building&lowbar;structure](https://github.com/Accord-Project/aec3po/blob/HEAD/src/vocabularies/building_structure.ttl)<br/>- [Module vocabularies/building&lowbar;usage](https://github.com/Accord-Project/aec3po/blob/HEAD/src/vocabularies/building_usage.ttl)<br/>- [Module vocabularies/check&lowbar;method&lowbar;comparators](https://github.com/Accord-Project/aec3po/blob/HEAD/src/vocabularies/check_method_comparators.ttl)<br/>- [Module vocabularies/check&lowbar;method&lowbar;operators](https://github.com/Accord-Project/aec3po/blob/HEAD/src/vocabularies/check_method_operators.ttl)<br/>- [Module vocabularies/disciplines](https://github.com/Accord-Project/aec3po/blob/HEAD/src/vocabularies/disciplines.ttl)<br/>- [Module vocabularies/permitting&lowbar;stages](https://github.com/Accord-Project/aec3po/blob/HEAD/src/vocabularies/permitting_stages.ttl)<br/>- [Module vocabularies/quantity&lowbar;kinds](https://github.com/Accord-Project/aec3po/blob/HEAD/src/vocabularies/quantity_kinds.ttl)|

#### Criterion detail
|Identifier|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|
|----|----|
|Title|Profile&#32;compatibility&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;check&#32;whether&#32;the&#32;test&#32;subject&#32;is&#32;compatible&#32;with&#32;a&#32;profile&#32;or&#32;not,&#32;and&#32;if&#32;it&#32;is&#32;not,&#32;why.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-131)|Identifier|`owl-ql-profile-error`|
|[Section top](#minorfail-outcome-number-131)|Title|OWL&#32;QL&#32;Profile&#32;incompatible|
|[Section top](#minorfail-outcome-number-131)|Description|Statement&#32;not&#32;supported&#32;in&#32;a&#32;Super&#32;Class&#32;Expression|
|[Section top](#minorfail-outcome-number-131)|Pointer|<pre lang="Turtle"><code>&#91;]&#32;a&#32;owl:Class&#32;;  &#10; &#32; &#32;&#32; &#32;owl:unionOf&#32;(&#32;aec3po:FeatureOfInterest&#32;aec3po:Property&#32;aec3po:CheckMethod&#32;)&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-131)|Pointer|<pre lang="Turtle"><code>&#91;]&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32;&#32; &#32;owl:onProperty&#32;aec3po:conforms&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-131)|Pointer|<pre lang="Turtle"><code>&#91;]&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32;&#32; &#32;owl:onProperty&#32;aec3po:verificationFocus&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-131)|Pointer|<pre lang="Turtle"><code>&#91;]&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32;&#32; &#32;owl:onProperty&#32;aec3po:hasSeverity&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-131)|Pointer|<pre lang="Turtle"><code>&#91;]&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32;owl:allValuesFrom&#32;aec3po:DocumentSubdivision&#32;;  &#10; &#32; &#32; &#32; &#32;owl:onProperty&#32;aec3po:hasSubdivision&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-131)|Pointer|<pre lang="Turtle"><code>&#91;]&#32;owl:unionOf&#32;(&#32;aec3po:Document&#32;aec3po:DocumentSubdivision&#32;)&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-131)|Pointer|<pre lang="Turtle"><code>&#91;]&#32;owl:allValuesFrom&#32;aec3po:Document&#32;;  &#10; &#32; &#32;&#32; &#32;owl:onProperty&#32;aec3po:forDocument&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-131)|Pointer|<pre lang="Turtle"><code>&#91;]&#32;a&#32;owl:Class&#32;;  &#10; &#32; &#32;&#32; &#32;owl:unionOf&#32;(&#32; &#60;https://schema.org/Place> &#32;aec3po:AdministrativeArea&#32;)&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-131)|Pointer|<pre lang="Turtle"><code>&#91;]&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32;&#32; &#32;owl:onProperty&#32;aec3po:hasSubdivision&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-131)|Pointer|<pre lang="Turtle"><code>&#91;]&#32;a&#32;owl:Class&#32;;  &#10; &#32; &#32;&#32; &#32;owl:unionOf&#32;(&#32;aec3po:Table&#32;aec3po:Image&#32;aec3po:Row&#32;aec3po:Column&#32;)&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-131)|Pointer|<pre lang="Turtle"><code>&#91;]&#32;a&#32;owl:Class&#32;;  &#10; &#32; &#32;&#32; &#32;owl:unionOf&#32;(&#32;aec3po:Table&#32;aec3po:Image&#32;aec3po:Row&#32;aec3po:Column&#32;aec3po:Cell&#32;)&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-131)|Pointer|<pre lang="Turtle"><code>&#91;]&#32;a&#32;owl:Class&#32;;  &#10; &#32; &#32;&#32; &#32;owl:unionOf&#32;(&#32;aec3po:Table&#32;aec3po:Image&#32;)&#32;.</code></pre>|

***
### MinorFail Outcome number 132

[Jump to summary definition](#summary-MinorFail-132)	|	[Previous MinorFail outcome](#minorfail-outcome-number-131)	|	[Next MinorFail outcome](#minorfail-outcome-number-133)

:exclamation:MinorFail outcome
#### Subject detail
|Name|all-modules|
|----|----|
|Title|All&#32;the&#32;modules&#32;from&#32;branch&#32;HEAD&#32;that&#32;are&#32;syntaxically&#32;correct&#32;as&#32;well&#32;as&#32;their&#32;recursive&#32;imports|
|Composition|- [Module aec3po](https://github.com/Accord-Project/aec3po/blob/HEAD/src/aec3po.ttl)<br/>- [Module check&lowbar;method](https://github.com/Accord-Project/aec3po/blob/HEAD/src/check_method.ttl)<br/>- [Module checking&lowbar;act](https://github.com/Accord-Project/aec3po/blob/HEAD/src/checking_act.ttl)<br/>- [Module compliance&lowbar;verification&lowbar;report](https://github.com/Accord-Project/aec3po/blob/HEAD/src/compliance_verification_report.ttl)<br/>- [Module data&lowbar;requirement](https://github.com/Accord-Project/aec3po/blob/HEAD/src/data_requirement.ttl)<br/>- [Module document](https://github.com/Accord-Project/aec3po/blob/HEAD/src/document.ttl)<br/>- [Module evidence](https://github.com/Accord-Project/aec3po/blob/HEAD/src/evidence.ttl)<br/>- [Module feature&lowbar;of&lowbar;interest](https://github.com/Accord-Project/aec3po/blob/HEAD/src/feature_of_interest.ttl)<br/>- [Module legal&lowbar;verifier](https://github.com/Accord-Project/aec3po/blob/HEAD/src/legal_verifier.ttl)<br/>- [Module model](https://github.com/Accord-Project/aec3po/blob/HEAD/src/model.ttl)<br/>- [Module rase&lowbar;statement](https://github.com/Accord-Project/aec3po/blob/HEAD/src/rase_statement.ttl)<br/>- [Module statement](https://github.com/Accord-Project/aec3po/blob/HEAD/src/statement.ttl)<br/>- [Module table](https://github.com/Accord-Project/aec3po/blob/HEAD/src/table.ttl)<br/>- [Module vocabularies/&lowbar;shape](https://github.com/Accord-Project/aec3po/blob/HEAD/src/vocabularies/_shape.ttl)<br/>- [Module vocabularies/administrative&lowbar;areas](https://github.com/Accord-Project/aec3po/blob/HEAD/src/vocabularies/administrative_areas.ttl)<br/>- [Module vocabularies/building&lowbar;structure](https://github.com/Accord-Project/aec3po/blob/HEAD/src/vocabularies/building_structure.ttl)<br/>- [Module vocabularies/building&lowbar;usage](https://github.com/Accord-Project/aec3po/blob/HEAD/src/vocabularies/building_usage.ttl)<br/>- [Module vocabularies/check&lowbar;method&lowbar;comparators](https://github.com/Accord-Project/aec3po/blob/HEAD/src/vocabularies/check_method_comparators.ttl)<br/>- [Module vocabularies/check&lowbar;method&lowbar;operators](https://github.com/Accord-Project/aec3po/blob/HEAD/src/vocabularies/check_method_operators.ttl)<br/>- [Module vocabularies/disciplines](https://github.com/Accord-Project/aec3po/blob/HEAD/src/vocabularies/disciplines.ttl)<br/>- [Module vocabularies/permitting&lowbar;stages](https://github.com/Accord-Project/aec3po/blob/HEAD/src/vocabularies/permitting_stages.ttl)<br/>- [Module vocabularies/quantity&lowbar;kinds](https://github.com/Accord-Project/aec3po/blob/HEAD/src/vocabularies/quantity_kinds.ttl)|

#### Criterion detail
|Identifier|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|
|----|----|
|Title|Profile&#32;compatibility&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;check&#32;whether&#32;the&#32;test&#32;subject&#32;is&#32;compatible&#32;with&#32;a&#32;profile&#32;or&#32;not,&#32;and&#32;if&#32;it&#32;is&#32;not,&#32;why.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-132)|Identifier|`owl-rl-profile-error`|
|[Section top](#minorfail-outcome-number-132)|Title|OWL&#32;RL&#32;Profile&#32;incompatible|
|[Section top](#minorfail-outcome-number-132)|Description|Class&#32;Expression&#32;not&#32;supported&#32;as&#32;object&#32;of&#32;rdfs:domain&#32;or&#32;rdfs:range|
|[Section top](#minorfail-outcome-number-132)|Pointer|<pre lang="Turtle"><code>aec3po:caption&#32;a&#32;owl:DatatypeProperty&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;caption&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;The&#32;caption&#32;of&#32;a&#32;table,&#32;image,&#32;etc.&#32; &#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:domain&#32; &#91;&#32;a&#32;owl:Class&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:unionOf&#32;(&#32;aec3po:Table&#32;aec3po:Image&#32;)&#32;]&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32;aec3po:table&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-132)|Pointer|<pre lang="Turtle"><code>aec3po:contains&#32;a&#32;owl:ObjectProperty&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;Contains&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;A&#32;container&#32;contains&#32;a&#32;table&#32;and&#32;its&#32;caption.&#32;A&#32;table&#32;contai...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:domain&#32; &#91;&#32;a&#32;owl:Class&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:unionOf&#32;(&#32;aec3po:Table&#32;aec3po:Image&#32;aec3po:Row&#32;aec3po:Column&#32;)&#32;]&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32;aec3po:table&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-132)|Pointer|<pre lang="Turtle"><code>aec3po:hasBSSDDTarget&#32;a&#32;owl:FunctionalProperty,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:ObjectProperty&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;hasBSSDDTarget&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;The&#32;target&#32;refers&#32;to&#32;either&#32;the&#32;name&#32;of&#32;an&#32;object,&#32;the&#32;name&#32;...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:domain&#32; &#91;&#32;a&#32;owl:Class&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:unionOf&#32;(&#32;aec3po:FeatureOfInterest&#32;aec3po:Property&#32;aec3po:CheckMethod&#32;)&#32;]&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32;aec3po:check&lowbar;method&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-132)|Pointer|<pre lang="Turtle"><code>aec3po:hasFirstSubdivision&#32;a&#32;owl:FunctionalProperty,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:ObjectProperty&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;has&#32;first&#32;subdivision&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;Links&#32;a&#32;document&#32;part&#32;to&#32;the&#32;first&#32;of&#32;its&#32;subdivision&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:domain&#32; &#91;&#32;owl:unionOf&#32;(&#32;aec3po:Document&#32;aec3po:DocumentSubdivision&#32;)&#32;]&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32;aec3po:document&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:range&#32;aec3po:DocumentSubdivision&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:subPropertyOf&#32;aec3po:hasSubdivision&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-132)|Pointer|<pre lang="Turtle"><code>aec3po:hasSubdivision&#32;a&#32;owl:ObjectProperty&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;has&#32;subdivision&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;links&#32;a&#32;document&#32;part&#32;to&#32;some&#32;of&#32;its&#32;subdivision&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:domain&#32; &#91;&#32;owl:unionOf&#32;(&#32;aec3po:Document&#32;aec3po:DocumentSubdivision&#32;)&#32;]&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32;aec3po:document&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:range&#32;aec3po:DocumentSubdivision&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:subPropertyOf&#32;dc:hasPart&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-132)|Pointer|<pre lang="Turtle"><code>aec3po:hasUnit&#32;a&#32;owl:FunctionalProperty,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:ObjectProperty&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;hasUnit&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;the&#32;hasUnit&#32;property&#32;is&#32;used&#32;to&#32;link&#32;a&#32;specific&#32;property&#32;or&#32;...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:domain&#32; &#91;&#32;a&#32;owl:Class&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:unionOf&#32;(&#32;aec3po:FeatureOfInterest&#32;aec3po:Property&#32;aec3po:CheckMethod&#32;)&#32;]&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32;aec3po:check&lowbar;method&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:range&#32;qudt:Unit&#32;;  &#10; &#32; &#32; &#32; &#32;owl:eqivalentProperty&#32;qudt:hasValue&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-132)|Pointer|<pre lang="Turtle"><code>aec3po:hasValue&#32;a&#32;owl:DatatypeProperty,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:FunctionalProperty&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;has&#32;value&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;de&#32;facto&#32;used&#32;to&#32;link&#32;something&#32;(anything:&#32;property,&#32;propert...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:domain&#32; &#91;&#32;a&#32;owl:Class&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:unionOf&#32;(&#32;aec3po:FeatureOfInterest&#32;aec3po:Property&#32;aec3po:CheckMethod&#32;)&#32;]&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32;aec3po:&#32;;  &#10; &#32; &#32; &#32; &#32;skos:note&#32; &#34;The&#32;value&#32;of&#32;the&#32;literal&#32;may&#32;be&#32;a&#32;XSD&#32;literal&#32;(boolean,&#32;inte...&#34; &#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-132)|Pointer|<pre lang="Turtle"><code>aec3po:isContainedIn&#32;a&#32;owl:ObjectProperty&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;is&#32;contained&#32;by&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;A&#32;table&#32;contains&#32;row,&#32;columns&#32;and&#32;other&#32;elements.&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32;aec3po:table&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:range&#32; &#91;&#32;a&#32;owl:Class&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:unionOf&#32;(&#32;aec3po:Table&#32;aec3po:Image&#32;aec3po:Row&#32;aec3po:Column&#32;aec3po:Cell&#32;)&#32;]&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-132)|Pointer|<pre lang="Turtle"><code>aec3po:locationCoverage&#32;a&#32;owl:ObjectProperty&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;location&#32;coverage&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;The&#32;spatialCoverage&#32;indicates&#32;the&#32;place(s)&#32;or&#32;the&#32;administra...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:domain&#32; &#60;https://schema.org/Model> &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:range&#32; &#91;&#32;a&#32;owl:Class&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:unionOf&#32;(&#32; &#60;https://schema.org/Place> &#32;aec3po:AdministrativeArea&#32;)&#32;]&#32;;  &#10; &#32; &#32; &#32; &#32;owl:equivalentProperty&#32; &#60;https://schema.org/spatialCoverage> &#32;.</code></pre>|

***
### MinorFail Outcome number 133

[Jump to summary definition](#summary-MinorFail-133)	|	[Previous MinorFail outcome](#minorfail-outcome-number-132)	|	[Next MinorFail outcome](#minorfail-outcome-number-134)

:exclamation:MinorFail outcome
#### Subject detail
|Name|all-modules|
|----|----|
|Title|All&#32;the&#32;modules&#32;from&#32;branch&#32;HEAD&#32;that&#32;are&#32;syntaxically&#32;correct&#32;as&#32;well&#32;as&#32;their&#32;recursive&#32;imports|
|Composition|- [Module aec3po](https://github.com/Accord-Project/aec3po/blob/HEAD/src/aec3po.ttl)<br/>- [Module check&lowbar;method](https://github.com/Accord-Project/aec3po/blob/HEAD/src/check_method.ttl)<br/>- [Module checking&lowbar;act](https://github.com/Accord-Project/aec3po/blob/HEAD/src/checking_act.ttl)<br/>- [Module compliance&lowbar;verification&lowbar;report](https://github.com/Accord-Project/aec3po/blob/HEAD/src/compliance_verification_report.ttl)<br/>- [Module data&lowbar;requirement](https://github.com/Accord-Project/aec3po/blob/HEAD/src/data_requirement.ttl)<br/>- [Module document](https://github.com/Accord-Project/aec3po/blob/HEAD/src/document.ttl)<br/>- [Module evidence](https://github.com/Accord-Project/aec3po/blob/HEAD/src/evidence.ttl)<br/>- [Module feature&lowbar;of&lowbar;interest](https://github.com/Accord-Project/aec3po/blob/HEAD/src/feature_of_interest.ttl)<br/>- [Module legal&lowbar;verifier](https://github.com/Accord-Project/aec3po/blob/HEAD/src/legal_verifier.ttl)<br/>- [Module model](https://github.com/Accord-Project/aec3po/blob/HEAD/src/model.ttl)<br/>- [Module rase&lowbar;statement](https://github.com/Accord-Project/aec3po/blob/HEAD/src/rase_statement.ttl)<br/>- [Module statement](https://github.com/Accord-Project/aec3po/blob/HEAD/src/statement.ttl)<br/>- [Module table](https://github.com/Accord-Project/aec3po/blob/HEAD/src/table.ttl)<br/>- [Module vocabularies/&lowbar;shape](https://github.com/Accord-Project/aec3po/blob/HEAD/src/vocabularies/_shape.ttl)<br/>- [Module vocabularies/administrative&lowbar;areas](https://github.com/Accord-Project/aec3po/blob/HEAD/src/vocabularies/administrative_areas.ttl)<br/>- [Module vocabularies/building&lowbar;structure](https://github.com/Accord-Project/aec3po/blob/HEAD/src/vocabularies/building_structure.ttl)<br/>- [Module vocabularies/building&lowbar;usage](https://github.com/Accord-Project/aec3po/blob/HEAD/src/vocabularies/building_usage.ttl)<br/>- [Module vocabularies/check&lowbar;method&lowbar;comparators](https://github.com/Accord-Project/aec3po/blob/HEAD/src/vocabularies/check_method_comparators.ttl)<br/>- [Module vocabularies/check&lowbar;method&lowbar;operators](https://github.com/Accord-Project/aec3po/blob/HEAD/src/vocabularies/check_method_operators.ttl)<br/>- [Module vocabularies/disciplines](https://github.com/Accord-Project/aec3po/blob/HEAD/src/vocabularies/disciplines.ttl)<br/>- [Module vocabularies/permitting&lowbar;stages](https://github.com/Accord-Project/aec3po/blob/HEAD/src/vocabularies/permitting_stages.ttl)<br/>- [Module vocabularies/quantity&lowbar;kinds](https://github.com/Accord-Project/aec3po/blob/HEAD/src/vocabularies/quantity_kinds.ttl)|

#### Criterion detail
|Identifier|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|
|----|----|
|Title|Profile&#32;compatibility&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;check&#32;whether&#32;the&#32;test&#32;subject&#32;is&#32;compatible&#32;with&#32;a&#32;profile&#32;or&#32;not,&#32;and&#32;if&#32;it&#32;is&#32;not,&#32;why.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-133)|Identifier|`owl-rl-profile-error`|
|[Section top](#minorfail-outcome-number-133)|Title|OWL&#32;RL&#32;Profile&#32;incompatible|
|[Section top](#minorfail-outcome-number-133)|Description|Class&#32;Expression&#32;not&#32;supported&#32;with&#32;owl:equivalentClass|
|[Section top](#minorfail-outcome-number-133)|Pointer|<pre lang="Turtle"><code>aec3po:ComponentCheckMethod&#32;a&#32;owl:Class&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;Component&#32;Check&#32;Method&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;Component&#32;check&#32;method&#32;refers&#32;to&#32;a&#32;process&#32;of&#32;inspecting&#32;and...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32;aec3po:check&lowbar;method&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:subClassOf&#32;aec3po:CheckMethod&#32;;  &#10; &#32; &#32; &#32; &#32;owl:equivalentClass&#32; &#91;&#32;a&#32;owl:Class&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:intersectionOf&#32;(&#32;aec3po:CheckMethod&#32; &#91;&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:allValuesFrom&#32; &#91;&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:allValuesFrom&#32;aec3po:FeatureOfInterest&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:onProperty&#32; &#91;&#32;owl:inverseOf&#32;aec3po:forDesign&#32;]&#32;]&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:onProperty&#32;aec3po:forDesign&#32;]&#32;)&#32;]&#32;.</code></pre>|

***
### MinorFail Outcome number 134

[Jump to summary definition](#summary-MinorFail-134)	|	[Previous MinorFail outcome](#minorfail-outcome-number-133)	|	[Next MinorFail outcome](#minorfail-outcome-number-135)

:exclamation:MinorFail outcome
#### Subject detail
|Name|all-modules|
|----|----|
|Title|All&#32;the&#32;modules&#32;from&#32;branch&#32;HEAD&#32;that&#32;are&#32;syntaxically&#32;correct&#32;as&#32;well&#32;as&#32;their&#32;recursive&#32;imports|
|Composition|- [Module aec3po](https://github.com/Accord-Project/aec3po/blob/HEAD/src/aec3po.ttl)<br/>- [Module check&lowbar;method](https://github.com/Accord-Project/aec3po/blob/HEAD/src/check_method.ttl)<br/>- [Module checking&lowbar;act](https://github.com/Accord-Project/aec3po/blob/HEAD/src/checking_act.ttl)<br/>- [Module compliance&lowbar;verification&lowbar;report](https://github.com/Accord-Project/aec3po/blob/HEAD/src/compliance_verification_report.ttl)<br/>- [Module data&lowbar;requirement](https://github.com/Accord-Project/aec3po/blob/HEAD/src/data_requirement.ttl)<br/>- [Module document](https://github.com/Accord-Project/aec3po/blob/HEAD/src/document.ttl)<br/>- [Module evidence](https://github.com/Accord-Project/aec3po/blob/HEAD/src/evidence.ttl)<br/>- [Module feature&lowbar;of&lowbar;interest](https://github.com/Accord-Project/aec3po/blob/HEAD/src/feature_of_interest.ttl)<br/>- [Module legal&lowbar;verifier](https://github.com/Accord-Project/aec3po/blob/HEAD/src/legal_verifier.ttl)<br/>- [Module model](https://github.com/Accord-Project/aec3po/blob/HEAD/src/model.ttl)<br/>- [Module rase&lowbar;statement](https://github.com/Accord-Project/aec3po/blob/HEAD/src/rase_statement.ttl)<br/>- [Module statement](https://github.com/Accord-Project/aec3po/blob/HEAD/src/statement.ttl)<br/>- [Module table](https://github.com/Accord-Project/aec3po/blob/HEAD/src/table.ttl)<br/>- [Module vocabularies/&lowbar;shape](https://github.com/Accord-Project/aec3po/blob/HEAD/src/vocabularies/_shape.ttl)<br/>- [Module vocabularies/administrative&lowbar;areas](https://github.com/Accord-Project/aec3po/blob/HEAD/src/vocabularies/administrative_areas.ttl)<br/>- [Module vocabularies/building&lowbar;structure](https://github.com/Accord-Project/aec3po/blob/HEAD/src/vocabularies/building_structure.ttl)<br/>- [Module vocabularies/building&lowbar;usage](https://github.com/Accord-Project/aec3po/blob/HEAD/src/vocabularies/building_usage.ttl)<br/>- [Module vocabularies/check&lowbar;method&lowbar;comparators](https://github.com/Accord-Project/aec3po/blob/HEAD/src/vocabularies/check_method_comparators.ttl)<br/>- [Module vocabularies/check&lowbar;method&lowbar;operators](https://github.com/Accord-Project/aec3po/blob/HEAD/src/vocabularies/check_method_operators.ttl)<br/>- [Module vocabularies/disciplines](https://github.com/Accord-Project/aec3po/blob/HEAD/src/vocabularies/disciplines.ttl)<br/>- [Module vocabularies/permitting&lowbar;stages](https://github.com/Accord-Project/aec3po/blob/HEAD/src/vocabularies/permitting_stages.ttl)<br/>- [Module vocabularies/quantity&lowbar;kinds](https://github.com/Accord-Project/aec3po/blob/HEAD/src/vocabularies/quantity_kinds.ttl)|

#### Criterion detail
|Identifier|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|
|----|----|
|Title|Profile&#32;compatibility&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;check&#32;whether&#32;the&#32;test&#32;subject&#32;is&#32;compatible&#32;with&#32;a&#32;profile&#32;or&#32;not,&#32;and&#32;if&#32;it&#32;is&#32;not,&#32;why.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-134)|Identifier|`owl-rl-profile-error`|
|[Section top](#minorfail-outcome-number-134)|Title|OWL&#32;RL&#32;Profile&#32;incompatible|
|[Section top](#minorfail-outcome-number-134)|Description|Class&#32;Expression&#32;not&#32;supported&#32;with&#32;owl:equivalentClass&#32;or&#32;owl:intersectionOf|
|[Section top](#minorfail-outcome-number-134)|Pointer|<pre lang="Turtle"><code>&#91;]&#32;a&#32;owl:Class&#32;;  &#10; &#32; &#32; &#32; &#32;owl:intersectionOf&#32;(&#32;aec3po:CheckMethod&#32; &#91;&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:allValuesFrom&#32; &#91;&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:allValuesFrom&#32;aec3po:FeatureOfInterest&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:onProperty&#32; &#91;&#32;owl:inverseOf&#32;aec3po:forDesign&#32;]&#32;]&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:onProperty&#32;aec3po:forDesign&#32;]&#32;)&#32;.</code></pre>|

***
### MinorFail Outcome number 135

[Jump to summary definition](#summary-MinorFail-135)	|	[Previous MinorFail outcome](#minorfail-outcome-number-134)	|	[Next MinorFail outcome](#minorfail-outcome-number-136)

:exclamation:MinorFail outcome
#### Subject detail
|Name|all-modules|
|----|----|
|Title|All&#32;the&#32;modules&#32;from&#32;branch&#32;HEAD&#32;that&#32;are&#32;syntaxically&#32;correct&#32;as&#32;well&#32;as&#32;their&#32;recursive&#32;imports|
|Composition|- [Module aec3po](https://github.com/Accord-Project/aec3po/blob/HEAD/src/aec3po.ttl)<br/>- [Module check&lowbar;method](https://github.com/Accord-Project/aec3po/blob/HEAD/src/check_method.ttl)<br/>- [Module checking&lowbar;act](https://github.com/Accord-Project/aec3po/blob/HEAD/src/checking_act.ttl)<br/>- [Module compliance&lowbar;verification&lowbar;report](https://github.com/Accord-Project/aec3po/blob/HEAD/src/compliance_verification_report.ttl)<br/>- [Module data&lowbar;requirement](https://github.com/Accord-Project/aec3po/blob/HEAD/src/data_requirement.ttl)<br/>- [Module document](https://github.com/Accord-Project/aec3po/blob/HEAD/src/document.ttl)<br/>- [Module evidence](https://github.com/Accord-Project/aec3po/blob/HEAD/src/evidence.ttl)<br/>- [Module feature&lowbar;of&lowbar;interest](https://github.com/Accord-Project/aec3po/blob/HEAD/src/feature_of_interest.ttl)<br/>- [Module legal&lowbar;verifier](https://github.com/Accord-Project/aec3po/blob/HEAD/src/legal_verifier.ttl)<br/>- [Module model](https://github.com/Accord-Project/aec3po/blob/HEAD/src/model.ttl)<br/>- [Module rase&lowbar;statement](https://github.com/Accord-Project/aec3po/blob/HEAD/src/rase_statement.ttl)<br/>- [Module statement](https://github.com/Accord-Project/aec3po/blob/HEAD/src/statement.ttl)<br/>- [Module table](https://github.com/Accord-Project/aec3po/blob/HEAD/src/table.ttl)<br/>- [Module vocabularies/&lowbar;shape](https://github.com/Accord-Project/aec3po/blob/HEAD/src/vocabularies/_shape.ttl)<br/>- [Module vocabularies/administrative&lowbar;areas](https://github.com/Accord-Project/aec3po/blob/HEAD/src/vocabularies/administrative_areas.ttl)<br/>- [Module vocabularies/building&lowbar;structure](https://github.com/Accord-Project/aec3po/blob/HEAD/src/vocabularies/building_structure.ttl)<br/>- [Module vocabularies/building&lowbar;usage](https://github.com/Accord-Project/aec3po/blob/HEAD/src/vocabularies/building_usage.ttl)<br/>- [Module vocabularies/check&lowbar;method&lowbar;comparators](https://github.com/Accord-Project/aec3po/blob/HEAD/src/vocabularies/check_method_comparators.ttl)<br/>- [Module vocabularies/check&lowbar;method&lowbar;operators](https://github.com/Accord-Project/aec3po/blob/HEAD/src/vocabularies/check_method_operators.ttl)<br/>- [Module vocabularies/disciplines](https://github.com/Accord-Project/aec3po/blob/HEAD/src/vocabularies/disciplines.ttl)<br/>- [Module vocabularies/permitting&lowbar;stages](https://github.com/Accord-Project/aec3po/blob/HEAD/src/vocabularies/permitting_stages.ttl)<br/>- [Module vocabularies/quantity&lowbar;kinds](https://github.com/Accord-Project/aec3po/blob/HEAD/src/vocabularies/quantity_kinds.ttl)|

#### Criterion detail
|Identifier|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|
|----|----|
|Title|Profile&#32;compatibility&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;check&#32;whether&#32;the&#32;test&#32;subject&#32;is&#32;compatible&#32;with&#32;a&#32;profile&#32;or&#32;not,&#32;and&#32;if&#32;it&#32;is&#32;not,&#32;why.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-135)|Identifier|`owl-rl-profile-error`|
|[Section top](#minorfail-outcome-number-135)|Title|OWL&#32;RL&#32;Profile&#32;incompatible|
|[Section top](#minorfail-outcome-number-135)|Description|Class&#32;Expression&#32;not&#32;supported&#32;with&#32;rdfs:subClassOf|
|[Section top](#minorfail-outcome-number-135)|Pointer|<pre lang="Turtle"><code>aec3po:AndCheckStatement&#32;a&#32;owl:Class&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;And&#32;Check&#32;Statement&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;Check&#32;verified&#32;if&#32;and&#32;only&#32;if&#32;all&#32;of&#32;its&#32;sub-checks&#32;are&#32;veri...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32;aec3po:statement&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:subClassOf&#32; &#91;&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:onProperty&#32;aec3po:hasSubdivision&#32;],  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;aec3po:ChecklistStatement&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-135)|Pointer|<pre lang="Turtle"><code>aec3po:CheckingAct&#32;a&#32;owl:Class&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;Checking&#32;Act&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;Act&#32;of&#32;checking&#32;some&#32;entities&#32;for&#32;something&#32;and&#32;generating&#32;a...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32;aec3po:checking&lowbar;act&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:subClassOf&#32; &#91;&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:onProperty&#32;aec3po:usedMethod&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:someValuesFrom&#32;aec3po:CheckMethod&#32;],  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#91;&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:onProperty&#32;aec3po:madeBy&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:someValuesFrom&#32;aec3po:ProcessVerifier&#32;],  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#91;&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:onProperty&#32;aec3po:checked&#32;],  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#91;&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:onProperty&#32;aec3po:hasReport&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:someValuesFrom&#32;aec3po:ComplianceVerificationReport&#32;],  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#60;http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#Event> &#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-135)|Pointer|<pre lang="Turtle"><code>aec3po:ComplianceVerificationReport&#32;a&#32;owl:Class&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;Compliance&#32;Verification&#32;Report&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;Result&#32;of&#32;a&#32;checking&#32;act.&#32;May&#32;be&#32;compliant&#32;or&#32;not.&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32;aec3po:compliance&lowbar;verification&lowbar;report&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:subClassOf&#32; &#91;&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:onProperty&#32;aec3po:conforms&#32;]&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-135)|Pointer|<pre lang="Turtle"><code>aec3po:NotCheckStatement&#32;a&#32;owl:Class&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;Not&#32;Check&#32;Statement&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;Check&#32;verified&#32;if&#32;and&#32;only&#32;if&#32;the&#32;sub-check&#32;is&#32;not&#32;verified.&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32;aec3po:statement&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:subClassOf&#32; &#91;&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:onProperty&#32;aec3po:hasSubdivision&#32;]&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-135)|Pointer|<pre lang="Turtle"><code>aec3po:OrCheckStatement&#32;a&#32;owl:Class&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;Or&#32;Check&#32;Statement&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;Check&#32;verified&#32;if&#32;and&#32;only&#32;if&#32;at&#32;least&#32;one&#32;of&#32;its&#32;sub-checks...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32;aec3po:statement&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:subClassOf&#32; &#91;&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:onProperty&#32;aec3po:hasSubdivision&#32;],  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;aec3po:ChecklistStatement&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-135)|Pointer|<pre lang="Turtle"><code>aec3po:VerificationResult&#32;a&#32;owl:Class&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;Verification&#32;Result&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;Individual&#32;verification&#32;result&#32;of&#32;a&#32;Compliance&#32;Verification&#32;...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32;aec3po:compliance&lowbar;verification&lowbar;report&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:subClassOf&#32; &#91;&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:onProperty&#32;aec3po:verificationFocus&#32;],  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#91;&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:onProperty&#32;aec3po:hasSeverity&#32;]&#32;.</code></pre>|

***
### MinorFail Outcome number 136

[Jump to summary definition](#summary-MinorFail-136)	|	[Previous MinorFail outcome](#minorfail-outcome-number-135)	|	[Next MinorFail outcome](#minorfail-outcome-number-137)

:exclamation:MinorFail outcome
#### Subject detail
|Name|all-modules|
|----|----|
|Title|All&#32;the&#32;modules&#32;from&#32;branch&#32;HEAD&#32;that&#32;are&#32;syntaxically&#32;correct&#32;as&#32;well&#32;as&#32;their&#32;recursive&#32;imports|
|Composition|- [Module aec3po](https://github.com/Accord-Project/aec3po/blob/HEAD/src/aec3po.ttl)<br/>- [Module check&lowbar;method](https://github.com/Accord-Project/aec3po/blob/HEAD/src/check_method.ttl)<br/>- [Module checking&lowbar;act](https://github.com/Accord-Project/aec3po/blob/HEAD/src/checking_act.ttl)<br/>- [Module compliance&lowbar;verification&lowbar;report](https://github.com/Accord-Project/aec3po/blob/HEAD/src/compliance_verification_report.ttl)<br/>- [Module data&lowbar;requirement](https://github.com/Accord-Project/aec3po/blob/HEAD/src/data_requirement.ttl)<br/>- [Module document](https://github.com/Accord-Project/aec3po/blob/HEAD/src/document.ttl)<br/>- [Module evidence](https://github.com/Accord-Project/aec3po/blob/HEAD/src/evidence.ttl)<br/>- [Module feature&lowbar;of&lowbar;interest](https://github.com/Accord-Project/aec3po/blob/HEAD/src/feature_of_interest.ttl)<br/>- [Module legal&lowbar;verifier](https://github.com/Accord-Project/aec3po/blob/HEAD/src/legal_verifier.ttl)<br/>- [Module model](https://github.com/Accord-Project/aec3po/blob/HEAD/src/model.ttl)<br/>- [Module rase&lowbar;statement](https://github.com/Accord-Project/aec3po/blob/HEAD/src/rase_statement.ttl)<br/>- [Module statement](https://github.com/Accord-Project/aec3po/blob/HEAD/src/statement.ttl)<br/>- [Module table](https://github.com/Accord-Project/aec3po/blob/HEAD/src/table.ttl)<br/>- [Module vocabularies/&lowbar;shape](https://github.com/Accord-Project/aec3po/blob/HEAD/src/vocabularies/_shape.ttl)<br/>- [Module vocabularies/administrative&lowbar;areas](https://github.com/Accord-Project/aec3po/blob/HEAD/src/vocabularies/administrative_areas.ttl)<br/>- [Module vocabularies/building&lowbar;structure](https://github.com/Accord-Project/aec3po/blob/HEAD/src/vocabularies/building_structure.ttl)<br/>- [Module vocabularies/building&lowbar;usage](https://github.com/Accord-Project/aec3po/blob/HEAD/src/vocabularies/building_usage.ttl)<br/>- [Module vocabularies/check&lowbar;method&lowbar;comparators](https://github.com/Accord-Project/aec3po/blob/HEAD/src/vocabularies/check_method_comparators.ttl)<br/>- [Module vocabularies/check&lowbar;method&lowbar;operators](https://github.com/Accord-Project/aec3po/blob/HEAD/src/vocabularies/check_method_operators.ttl)<br/>- [Module vocabularies/disciplines](https://github.com/Accord-Project/aec3po/blob/HEAD/src/vocabularies/disciplines.ttl)<br/>- [Module vocabularies/permitting&lowbar;stages](https://github.com/Accord-Project/aec3po/blob/HEAD/src/vocabularies/permitting_stages.ttl)<br/>- [Module vocabularies/quantity&lowbar;kinds](https://github.com/Accord-Project/aec3po/blob/HEAD/src/vocabularies/quantity_kinds.ttl)|

#### Criterion detail
|Identifier|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|
|----|----|
|Title|Profile&#32;compatibility&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;check&#32;whether&#32;the&#32;test&#32;subject&#32;is&#32;compatible&#32;with&#32;a&#32;profile&#32;or&#32;not,&#32;and&#32;if&#32;it&#32;is&#32;not,&#32;why.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-136)|Identifier|`owl-rl-profile-error`|
|[Section top](#minorfail-outcome-number-136)|Title|OWL&#32;RL&#32;Profile&#32;incompatible|
|[Section top](#minorfail-outcome-number-136)|Description|Statement&#32;not&#32;supported&#32;in&#32;a&#32;Super&#32;Class&#32;Expression|
|[Section top](#minorfail-outcome-number-136)|Pointer|<pre lang="Turtle"><code>&#91;]&#32;a&#32;owl:Class&#32;;  &#10; &#32; &#32;&#32; &#32;owl:unionOf&#32;(&#32;aec3po:FeatureOfInterest&#32;aec3po:Property&#32;aec3po:CheckMethod&#32;)&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-136)|Pointer|<pre lang="Turtle"><code>&#91;]&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32;owl:onProperty&#32;aec3po:usedMethod&#32;;  &#10; &#32; &#32; &#32; &#32;owl:someValuesFrom&#32;aec3po:CheckMethod&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-136)|Pointer|<pre lang="Turtle"><code>&#91;]&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32;owl:onProperty&#32;aec3po:madeBy&#32;;  &#10; &#32; &#32; &#32; &#32;owl:someValuesFrom&#32;aec3po:ProcessVerifier&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-136)|Pointer|<pre lang="Turtle"><code>&#91;]&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32;&#32; &#32;owl:onProperty&#32;aec3po:checked&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-136)|Pointer|<pre lang="Turtle"><code>&#91;]&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32;owl:onProperty&#32;aec3po:hasReport&#32;;  &#10; &#32; &#32; &#32; &#32;owl:someValuesFrom&#32;aec3po:ComplianceVerificationReport&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-136)|Pointer|<pre lang="Turtle"><code>&#91;]&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32;&#32; &#32;owl:onProperty&#32;aec3po:conforms&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-136)|Pointer|<pre lang="Turtle"><code>&#91;]&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32;&#32; &#32;owl:onProperty&#32;aec3po:verificationFocus&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-136)|Pointer|<pre lang="Turtle"><code>&#91;]&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32;&#32; &#32;owl:onProperty&#32;aec3po:hasSeverity&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-136)|Pointer|<pre lang="Turtle"><code>&#91;]&#32;owl:unionOf&#32;(&#32;aec3po:Document&#32;aec3po:DocumentSubdivision&#32;)&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-136)|Pointer|<pre lang="Turtle"><code>&#91;]&#32;a&#32;owl:Class&#32;;  &#10; &#32; &#32;&#32; &#32;owl:unionOf&#32;(&#32; &#60;https://schema.org/Place> &#32;aec3po:AdministrativeArea&#32;)&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-136)|Pointer|<pre lang="Turtle"><code>&#91;]&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32;&#32; &#32;owl:onProperty&#32;aec3po:hasSubdivision&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-136)|Pointer|<pre lang="Turtle"><code>&#91;]&#32;a&#32;owl:Class&#32;;  &#10; &#32; &#32;&#32; &#32;owl:unionOf&#32;(&#32;aec3po:Table&#32;aec3po:Image&#32;aec3po:Row&#32;aec3po:Column&#32;)&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-136)|Pointer|<pre lang="Turtle"><code>&#91;]&#32;a&#32;owl:Class&#32;;  &#10; &#32; &#32;&#32; &#32;owl:unionOf&#32;(&#32;aec3po:Table&#32;aec3po:Image&#32;aec3po:Row&#32;aec3po:Column&#32;aec3po:Cell&#32;)&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-136)|Pointer|<pre lang="Turtle"><code>&#91;]&#32;a&#32;owl:Class&#32;;  &#10; &#32; &#32;&#32; &#32;owl:unionOf&#32;(&#32;aec3po:Table&#32;aec3po:Image&#32;)&#32;.</code></pre>|

***
### MinorFail Outcome number 137

[Jump to summary definition](#summary-MinorFail-137)	|	[Previous MinorFail outcome](#minorfail-outcome-number-136)	|	[Next MinorFail outcome](#minorfail-outcome-number-138)

:exclamation:MinorFail outcome
#### Subject detail
|Name|all-modules|
|----|----|
|Title|All&#32;the&#32;modules&#32;from&#32;branch&#32;HEAD&#32;that&#32;are&#32;syntaxically&#32;correct&#32;as&#32;well&#32;as&#32;their&#32;recursive&#32;imports|
|Composition|- [Module aec3po](https://github.com/Accord-Project/aec3po/blob/HEAD/src/aec3po.ttl)<br/>- [Module check&lowbar;method](https://github.com/Accord-Project/aec3po/blob/HEAD/src/check_method.ttl)<br/>- [Module checking&lowbar;act](https://github.com/Accord-Project/aec3po/blob/HEAD/src/checking_act.ttl)<br/>- [Module compliance&lowbar;verification&lowbar;report](https://github.com/Accord-Project/aec3po/blob/HEAD/src/compliance_verification_report.ttl)<br/>- [Module data&lowbar;requirement](https://github.com/Accord-Project/aec3po/blob/HEAD/src/data_requirement.ttl)<br/>- [Module document](https://github.com/Accord-Project/aec3po/blob/HEAD/src/document.ttl)<br/>- [Module evidence](https://github.com/Accord-Project/aec3po/blob/HEAD/src/evidence.ttl)<br/>- [Module feature&lowbar;of&lowbar;interest](https://github.com/Accord-Project/aec3po/blob/HEAD/src/feature_of_interest.ttl)<br/>- [Module legal&lowbar;verifier](https://github.com/Accord-Project/aec3po/blob/HEAD/src/legal_verifier.ttl)<br/>- [Module model](https://github.com/Accord-Project/aec3po/blob/HEAD/src/model.ttl)<br/>- [Module rase&lowbar;statement](https://github.com/Accord-Project/aec3po/blob/HEAD/src/rase_statement.ttl)<br/>- [Module statement](https://github.com/Accord-Project/aec3po/blob/HEAD/src/statement.ttl)<br/>- [Module table](https://github.com/Accord-Project/aec3po/blob/HEAD/src/table.ttl)<br/>- [Module vocabularies/&lowbar;shape](https://github.com/Accord-Project/aec3po/blob/HEAD/src/vocabularies/_shape.ttl)<br/>- [Module vocabularies/administrative&lowbar;areas](https://github.com/Accord-Project/aec3po/blob/HEAD/src/vocabularies/administrative_areas.ttl)<br/>- [Module vocabularies/building&lowbar;structure](https://github.com/Accord-Project/aec3po/blob/HEAD/src/vocabularies/building_structure.ttl)<br/>- [Module vocabularies/building&lowbar;usage](https://github.com/Accord-Project/aec3po/blob/HEAD/src/vocabularies/building_usage.ttl)<br/>- [Module vocabularies/check&lowbar;method&lowbar;comparators](https://github.com/Accord-Project/aec3po/blob/HEAD/src/vocabularies/check_method_comparators.ttl)<br/>- [Module vocabularies/check&lowbar;method&lowbar;operators](https://github.com/Accord-Project/aec3po/blob/HEAD/src/vocabularies/check_method_operators.ttl)<br/>- [Module vocabularies/disciplines](https://github.com/Accord-Project/aec3po/blob/HEAD/src/vocabularies/disciplines.ttl)<br/>- [Module vocabularies/permitting&lowbar;stages](https://github.com/Accord-Project/aec3po/blob/HEAD/src/vocabularies/permitting_stages.ttl)<br/>- [Module vocabularies/quantity&lowbar;kinds](https://github.com/Accord-Project/aec3po/blob/HEAD/src/vocabularies/quantity_kinds.ttl)|

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
|[Section top](#minorfail-outcome-number-137)|Description|Statement&#32;not&#32;supported&#32;in&#32;an&#32;Equivalent&#32;Class&#32;Expression|
|[Section top](#minorfail-outcome-number-137)|Pointer|<pre lang="Turtle"><code>&#91;]&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32;owl:allValuesFrom&#32; &#91;&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:allValuesFrom&#32;aec3po:FeatureOfInterest&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:onProperty&#32; &#91;&#32;owl:inverseOf&#32;aec3po:forDesign&#32;]&#32;]&#32;;  &#10; &#32; &#32; &#32; &#32;owl:onProperty&#32;aec3po:forDesign&#32;.</code></pre>|

***
### MinorFail Outcome number 138

[Jump to summary definition](#summary-MinorFail-138)	|	[Previous MinorFail outcome](#minorfail-outcome-number-137)	|	[Next MinorFail outcome](#minorfail-outcome-number-139)

:exclamation:MinorFail outcome
#### Subject detail
|Name|all-modules|
|----|----|
|Title|All&#32;the&#32;modules&#32;from&#32;branch&#32;HEAD&#32;that&#32;are&#32;syntaxically&#32;correct&#32;as&#32;well&#32;as&#32;their&#32;recursive&#32;imports|
|Composition|- [Module aec3po](https://github.com/Accord-Project/aec3po/blob/HEAD/src/aec3po.ttl)<br/>- [Module check&lowbar;method](https://github.com/Accord-Project/aec3po/blob/HEAD/src/check_method.ttl)<br/>- [Module checking&lowbar;act](https://github.com/Accord-Project/aec3po/blob/HEAD/src/checking_act.ttl)<br/>- [Module compliance&lowbar;verification&lowbar;report](https://github.com/Accord-Project/aec3po/blob/HEAD/src/compliance_verification_report.ttl)<br/>- [Module data&lowbar;requirement](https://github.com/Accord-Project/aec3po/blob/HEAD/src/data_requirement.ttl)<br/>- [Module document](https://github.com/Accord-Project/aec3po/blob/HEAD/src/document.ttl)<br/>- [Module evidence](https://github.com/Accord-Project/aec3po/blob/HEAD/src/evidence.ttl)<br/>- [Module feature&lowbar;of&lowbar;interest](https://github.com/Accord-Project/aec3po/blob/HEAD/src/feature_of_interest.ttl)<br/>- [Module legal&lowbar;verifier](https://github.com/Accord-Project/aec3po/blob/HEAD/src/legal_verifier.ttl)<br/>- [Module model](https://github.com/Accord-Project/aec3po/blob/HEAD/src/model.ttl)<br/>- [Module rase&lowbar;statement](https://github.com/Accord-Project/aec3po/blob/HEAD/src/rase_statement.ttl)<br/>- [Module statement](https://github.com/Accord-Project/aec3po/blob/HEAD/src/statement.ttl)<br/>- [Module table](https://github.com/Accord-Project/aec3po/blob/HEAD/src/table.ttl)<br/>- [Module vocabularies/&lowbar;shape](https://github.com/Accord-Project/aec3po/blob/HEAD/src/vocabularies/_shape.ttl)<br/>- [Module vocabularies/administrative&lowbar;areas](https://github.com/Accord-Project/aec3po/blob/HEAD/src/vocabularies/administrative_areas.ttl)<br/>- [Module vocabularies/building&lowbar;structure](https://github.com/Accord-Project/aec3po/blob/HEAD/src/vocabularies/building_structure.ttl)<br/>- [Module vocabularies/building&lowbar;usage](https://github.com/Accord-Project/aec3po/blob/HEAD/src/vocabularies/building_usage.ttl)<br/>- [Module vocabularies/check&lowbar;method&lowbar;comparators](https://github.com/Accord-Project/aec3po/blob/HEAD/src/vocabularies/check_method_comparators.ttl)<br/>- [Module vocabularies/check&lowbar;method&lowbar;operators](https://github.com/Accord-Project/aec3po/blob/HEAD/src/vocabularies/check_method_operators.ttl)<br/>- [Module vocabularies/disciplines](https://github.com/Accord-Project/aec3po/blob/HEAD/src/vocabularies/disciplines.ttl)<br/>- [Module vocabularies/permitting&lowbar;stages](https://github.com/Accord-Project/aec3po/blob/HEAD/src/vocabularies/permitting_stages.ttl)<br/>- [Module vocabularies/quantity&lowbar;kinds](https://github.com/Accord-Project/aec3po/blob/HEAD/src/vocabularies/quantity_kinds.ttl)|

#### Criterion detail
|Identifier|[term-referencing](https://ns.inria.fr/olivaw#term-referencing)|
|----|----|
|Title|Term&#32;referencing&#32;test|
|Description|A&#32;test&#32;case&#32;from&#32;the&#32;Best&#32;Practices&#32;tests&#32;checking&#32;if&#32;each&#32;term&#32;of&#32;the&#32;test&#32;subject&#32;is&#32;referenced&#32;to&#32;a&#32;module&#32;through&#32;a&#32;rdfs:isDefinedBy&#32;property.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-138)|Identifier|`no-reference-module`|
|[Section top](#minorfail-outcome-number-138)|Title|Term&#32;not&#32;referenced&#32;to&#32;a&#32;module|
|[Section top](#minorfail-outcome-number-138)|Description|Subject&#32;terms&#32;not&#32;linked&#32;to&#32;a&#32;module&#32;by&#32;a&#32;rdfs:isDefinedBy&#32;property|
|[Section top](#minorfail-outcome-number-138)|Pointer|<pre lang="Turtle"><code>:edlira&#32;a&#32;schema:Person&#32;;  &#10; &#32; &#32; &#32; &#32;schema:affiliation&#32; &#60;https://www.bcu.ac.uk/> &#32;;  &#10; &#32; &#32; &#32; &#32;schema:email&#32; &#34;edlira.vakaj@bcu.ac.uk&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;schema:identifier&#32; &#60;http://orcid.org/0000-0002-0712-0959> &#32;;  &#10; &#32; &#32; &#32; &#32;schema:name&#32; &#34;Edlira&#32;Vakaj&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;schema:url&#32; &#60;https://www.bcu.ac.uk/computing/about-us/our-staff/edlira-vakaj> &#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-138)|Pointer|<pre lang="Turtle"><code>:pan&#32;a&#32;schema:Person&#32;;  &#10; &#32; &#32; &#32; &#32;schema:affiliation&#32; &#60;https://www.bcu.ac.uk/> &#32;;  &#10; &#32; &#32; &#32; &#32;schema:email&#32; &#34;Panagiotis.Patlakas@bcu.ac.uk&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;schema:identifier&#32; &#60;http://orcid.org/0000-0002-7248-8952> &#32;;  &#10; &#32; &#32; &#32; &#32;schema:name&#32; &#34;Panagiotis&#32;Patlakas&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;schema:url&#32; &#60;https://www.bcu.ac.uk/built-environment/about-us/our-staff/panagiotis-patlakas> &#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-138)|Pointer|<pre lang="Turtle"><code>:amna&#32;a&#32;schema:Person&#32;;  &#10; &#32; &#32; &#32; &#32;schema:affiliation&#32; &#60;https://www.bcu.ac.uk/> &#32;;  &#10; &#32; &#32; &#32; &#32;schema:email&#32; &#34;Amna.Dridi@bcu.ac.uk&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;schema:identifier&#32; &#60;http://orcid.org/0000-0002-0185-103X> &#32;;  &#10; &#32; &#32; &#32; &#32;schema:name&#32; &#34;Amna&#32;Dridi&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;schema:url&#32; &#60;https://www.researchgate.net/profile/Amna-Dridi-3> &#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-138)|Pointer|<pre lang="Turtle"><code>:thomas&#32;a&#32;schema:Person&#32;;  &#10; &#32; &#32; &#32; &#32;schema:affiliation&#32; &#60;https://www.cardiff.ac.uk/> &#32;;  &#10; &#32; &#32; &#32; &#32;schema:email&#32; &#34;beachth@cardiff.ac.uk&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;schema:identifier&#32; &#60;http://orcid.org/0000-0001-5610-8027> &#32;;  &#10; &#32; &#32; &#32; &#32;schema:name&#32; &#34;Thomas&#32;Beach&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;schema:url&#32; &#60;https://profiles.cardiff.ac.uk/staff/beachth> &#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-138)|Pointer|<pre lang="Turtle"><code>:vladimir&#32;a&#32;schema:Person&#32;;  &#10; &#32; &#32; &#32; &#32;schema:affiliation&#32; &#60;https://www.ontotext.com/> &#32;;  &#10; &#32; &#32; &#32; &#32;schema:email&#32; &#34;vladimir.alexiev@ontotext.com&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;schema:identifier&#32; &#60;https://orcid.org/0000-0001-7508-7428> &#32;;  &#10; &#32; &#32; &#32; &#32;schema:name&#32; &#34;Vladimir&#32;Alexiev&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;schema:url&#32; &#60;https://www.ontotext.com/blog/author/vladimir/> &#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-138)|Pointer|<pre lang="Turtle"><code>:hasTarget&#32;a&#32;owl:DatatypeProperty&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;hasTarget&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;TBD&#34;@en&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-138)|Pointer|<pre lang="Turtle"><code>:hasBooleanTarget&#32;a&#32;owl:DatatypeProperty&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;hasBooleanTarget&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;TBD&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:range&#32;xsd:boolean&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-138)|Pointer|<pre lang="Turtle"><code>:name&#32;a&#32;owl:DatatypeProperty&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;name&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;The&#32;name&#32;or&#32;the&#32;identifier&#32;of&#32;the&#32;BIM&#32;model.&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:domain&#32; &#60;https://schema.org/Model> &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:range&#32;xsd:string&#32;;  &#10; &#32; &#32; &#32; &#32;owl:equivalentProperty&#32; &#60;https://schema.org/about> &#32;;  &#10; &#32; &#32; &#32; &#32;owl:inverseOf&#32; &#60;https://schema.org/subjectOf> &#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-138)|Pointer|<pre lang="Turtle"><code>:description&#32;a&#32;owl:DatatypeProperty&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;description&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;A&#32;textual&#32;description&#32;providing&#32;additional&#32;details&#32;about&#32;the...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:domain&#32; &#60;https://schema.org/Model> &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:range&#32;xsd:string&#32;;  &#10; &#32; &#32; &#32; &#32;owl:equivalentProperty&#32; &#60;https://schema.org/abstract> &#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-138)|Pointer|<pre lang="Turtle"><code>:location&#32;a&#32;owl:ObjectProperty&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;location&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;The&#32;physical&#32;or&#32;geographic&#32;location&#32;of&#32;the&#32;building&#32;or&#32;struc...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:domain&#32; &#60;https://schema.org/Model> &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:range&#32; &#60;https://schema.org/Place> &#32;;  &#10; &#32; &#32; &#32; &#32;owl:equivalentProperty&#32; &#60;https://schema.org/spatial> &#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-138)|Pointer|<pre lang="Turtle"><code>:locationCoverage&#32;a&#32;owl:ObjectProperty&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;location&#32;coverage&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;The&#32;spatialCoverage&#32;indicates&#32;the&#32;place(s)&#32;or&#32;the&#32;administra...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:domain&#32; &#60;https://schema.org/Model> &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:range&#32; &#91;&#32;a&#32;owl:Class&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:unionOf&#32;(&#32; &#60;https://schema.org/Place> &#32;:AdministrativeArea&#32;)&#32;]&#32;;  &#10; &#32; &#32; &#32; &#32;owl:equivalentProperty&#32; &#60;https://schema.org/spatialCoverage> &#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-138)|Pointer|<pre lang="Turtle"><code>:material&#32;a&#32;owl:DatatypeProperty&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;material&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;The&#32;materials&#32;used&#32;for&#32;different&#32;parts&#32;of&#32;the&#32;building,&#32;such...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:domain&#32; &#60;https://schema.org/Model> &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:range&#32;xsd:string&#32;;  &#10; &#32; &#32; &#32; &#32;owl:equivalentProperty&#32; &#60;https://schema.org/material> &#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-138)|Pointer|<pre lang="Turtle"><code>:hasBuildingPhase&#32;a&#32;owl:ObjectProperty&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;has&#32;building&#32;phase&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;describes&#32;the&#32;relationship&#32;between&#32;a&#32;construction-related&#32;en...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:domain&#32;:Model&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:range&#32;:Phase&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-138)|Pointer|<pre lang="Turtle"><code>:hasElementPhase&#32;a&#32;owl:ObjectProperty&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;has&#32;element&#32;phase&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;is&#32;used&#32;to&#32;establish&#32;a&#32;relationship&#32;between&#32;a&#32;construction&#32;e...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:domain&#32;:Model&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:range&#32;:Phase&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-138)|Pointer|<pre lang="Turtle"><code>:hasDimension&#32;a&#32;owl:ObjectProperty&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;has&#32;dimension&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;is&#32;used&#32;to&#32;represent&#32;the&#32;physical&#32;dimensions&#32;or&#32;measurements...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:domain&#32;:Model&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:range&#32;:Dimension&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-138)|Pointer|<pre lang="Turtle"><code>:hasClassification&#32;a&#32;owl:ObjectProperty&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;has&#32;dimension&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;is&#32;used&#32;to&#32;link&#32;building&#32;components,&#32;elements,&#32;or&#32;other&#32;enti...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:domain&#32;:Model&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:range&#32;:Classification&#32;.</code></pre>|

***
### MinorFail Outcome number 139

[Jump to summary definition](#summary-MinorFail-139)	|	[Previous MinorFail outcome](#minorfail-outcome-number-138)	|	[Next MinorFail outcome](#minorfail-outcome-number-140)

:exclamation:MinorFail outcome
#### Subject detail
|Name|all-modules|
|----|----|
|Title|All&#32;the&#32;modules&#32;from&#32;branch&#32;HEAD&#32;that&#32;are&#32;syntaxically&#32;correct&#32;as&#32;well&#32;as&#32;their&#32;recursive&#32;imports|
|Composition|- [Module aec3po](https://github.com/Accord-Project/aec3po/blob/HEAD/src/aec3po.ttl)<br/>- [Module check&lowbar;method](https://github.com/Accord-Project/aec3po/blob/HEAD/src/check_method.ttl)<br/>- [Module checking&lowbar;act](https://github.com/Accord-Project/aec3po/blob/HEAD/src/checking_act.ttl)<br/>- [Module compliance&lowbar;verification&lowbar;report](https://github.com/Accord-Project/aec3po/blob/HEAD/src/compliance_verification_report.ttl)<br/>- [Module data&lowbar;requirement](https://github.com/Accord-Project/aec3po/blob/HEAD/src/data_requirement.ttl)<br/>- [Module document](https://github.com/Accord-Project/aec3po/blob/HEAD/src/document.ttl)<br/>- [Module evidence](https://github.com/Accord-Project/aec3po/blob/HEAD/src/evidence.ttl)<br/>- [Module feature&lowbar;of&lowbar;interest](https://github.com/Accord-Project/aec3po/blob/HEAD/src/feature_of_interest.ttl)<br/>- [Module legal&lowbar;verifier](https://github.com/Accord-Project/aec3po/blob/HEAD/src/legal_verifier.ttl)<br/>- [Module model](https://github.com/Accord-Project/aec3po/blob/HEAD/src/model.ttl)<br/>- [Module rase&lowbar;statement](https://github.com/Accord-Project/aec3po/blob/HEAD/src/rase_statement.ttl)<br/>- [Module statement](https://github.com/Accord-Project/aec3po/blob/HEAD/src/statement.ttl)<br/>- [Module table](https://github.com/Accord-Project/aec3po/blob/HEAD/src/table.ttl)<br/>- [Module vocabularies/&lowbar;shape](https://github.com/Accord-Project/aec3po/blob/HEAD/src/vocabularies/_shape.ttl)<br/>- [Module vocabularies/administrative&lowbar;areas](https://github.com/Accord-Project/aec3po/blob/HEAD/src/vocabularies/administrative_areas.ttl)<br/>- [Module vocabularies/building&lowbar;structure](https://github.com/Accord-Project/aec3po/blob/HEAD/src/vocabularies/building_structure.ttl)<br/>- [Module vocabularies/building&lowbar;usage](https://github.com/Accord-Project/aec3po/blob/HEAD/src/vocabularies/building_usage.ttl)<br/>- [Module vocabularies/check&lowbar;method&lowbar;comparators](https://github.com/Accord-Project/aec3po/blob/HEAD/src/vocabularies/check_method_comparators.ttl)<br/>- [Module vocabularies/check&lowbar;method&lowbar;operators](https://github.com/Accord-Project/aec3po/blob/HEAD/src/vocabularies/check_method_operators.ttl)<br/>- [Module vocabularies/disciplines](https://github.com/Accord-Project/aec3po/blob/HEAD/src/vocabularies/disciplines.ttl)<br/>- [Module vocabularies/permitting&lowbar;stages](https://github.com/Accord-Project/aec3po/blob/HEAD/src/vocabularies/permitting_stages.ttl)<br/>- [Module vocabularies/quantity&lowbar;kinds](https://github.com/Accord-Project/aec3po/blob/HEAD/src/vocabularies/quantity_kinds.ttl)|

#### Criterion detail
|Identifier|[terms-differenciation](https://ns.inria.fr/olivaw#terms-differenciation)|
|----|----|
|Title|Terms&#32;differenciation&#32;test|
|Description|A&#32;test&#32;case&#32;from&#32;the&#32;Best&#32;Practices&#32;tests&#32;checking&#32;if&#32;all&#32;the&#32;terms&#32;are&#32;different&#32;enough&#32;from&#32;each&#32;other&#32;according&#32;to&#32;the&#32;Levenshtein&#32;distance&#32;metric.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-139)|Identifier|`too-close-terms`|
|[Section top](#minorfail-outcome-number-139)|Title|Too&#32;close&#32;terms|
|[Section top](#minorfail-outcome-number-139)|Description|Some&#32;terms&#32;are&#32;too&#32;similar|
|[Section top](#minorfail-outcome-number-139)|Pointer|<pre lang="Turtle"><code>:CheckMethodComparator-gt&#32;a&#32;owl:NamedIndividual,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;skos:Concept,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;:CheckMethodComparator&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32;:check&lowbar;method&lowbar;comparators&#32;;  &#10; &#32; &#32; &#32; &#32;skos:definition&#32; &#34;greater-than&#32;comparator.&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;skos:inScheme&#32;:CheckMethodComparatorNomenclature&#32;;  &#10; &#32; &#32; &#32; &#32;skos:prefLabel&#32; &#34;greater&#32;than&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;skos:topConceptOf&#32;:CheckMethodComparatorNomenclature&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-139)|Pointer|<pre lang="Turtle"><code>:CheckMethodComparator-ge&#32;a&#32;owl:NamedIndividual,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;skos:Concept,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;:CheckMethodComparator&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32;:check&lowbar;method&lowbar;comparators&#32;;  &#10; &#32; &#32; &#32; &#32;skos:definition&#32; &#34;greater-equal&#32;comparator.&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;skos:inScheme&#32;:CheckMethodComparatorNomenclature&#32;;  &#10; &#32; &#32; &#32; &#32;skos:prefLabel&#32; &#34;greater&#32;equal&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;skos:topConceptOf&#32;:CheckMethodComparatorNomenclature&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-139)|Pointer|<pre lang="Turtle"><code>:CheckMethodComparator-le&#32;a&#32;owl:NamedIndividual,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;skos:Concept,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;:CheckMethodComparator&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32;:check&lowbar;method&lowbar;comparators&#32;;  &#10; &#32; &#32; &#32; &#32;skos:definition&#32; &#34;less-equal&#32;comparator.&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;skos:inScheme&#32;:CheckMethodComparatorNomenclature&#32;;  &#10; &#32; &#32; &#32; &#32;skos:prefLabel&#32; &#34;less&#32;equal&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;skos:topConceptOf&#32;:CheckMethodComparatorNomenclature&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-139)|Pointer|<pre lang="Turtle"><code>:CheckMethodComparator-lt&#32;a&#32;owl:NamedIndividual,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;skos:Concept,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;:CheckMethodComparator&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32;:check&lowbar;method&lowbar;comparators&#32;;  &#10; &#32; &#32; &#32; &#32;skos:definition&#32; &#34;less-than&#32;comparator.&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;skos:inScheme&#32;:CheckMethodComparatorNomenclature&#32;;  &#10; &#32; &#32; &#32; &#32;skos:prefLabel&#32; &#34;less&#32;than&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;skos:topConceptOf&#32;:CheckMethodComparatorNomenclature&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-139)|Pointer|<pre lang="Turtle"><code>:CheckMethodComparator-neq&#32;a&#32;owl:NamedIndividual,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;skos:Concept,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;:CheckMethodComparator&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32;:check&lowbar;method&lowbar;comparators&#32;;  &#10; &#32; &#32; &#32; &#32;skos:definition&#32; &#34;not&#32;equal-to&#32;comparator.&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;skos:inScheme&#32;:CheckMethodComparatorNomenclature&#32;;  &#10; &#32; &#32; &#32; &#32;skos:prefLabel&#32; &#34;not&#32;equal-to&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;skos:topConceptOf&#32;:CheckMethodComparatorNomenclature&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-139)|Pointer|<pre lang="Turtle"><code>:CheckMethodcomparator-eq&#32;a&#32;owl:NamedIndividual,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;skos:Concept,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;:CheckMethodcomparator&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32;:check&lowbar;method&lowbar;comparators&#32;;  &#10; &#32; &#32; &#32; &#32;skos:definition&#32; &#34;equal-to&#32;comparator.&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;skos:inScheme&#32;:CheckMethodComparatorNomenclature&#32;;  &#10; &#32; &#32; &#32; &#32;skos:prefLabel&#32; &#34;equal-to&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;skos:topConceptOf&#32;:CheckMethodComparatorNomenclature&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-139)|Pointer|<pre lang="Turtle"><code>:OrCheckStatement&#32;a&#32;owl:Class&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;Or&#32;Check&#32;Statement&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;Check&#32;verified&#32;if&#32;and&#32;only&#32;if&#32;at&#32;least&#32;one&#32;of&#32;its&#32;sub-checks...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32;:statement&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:subClassOf&#32; &#91;&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:onProperty&#32;:hasSubdivision&#32;],  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;:ChecklistStatement&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-139)|Pointer|<pre lang="Turtle"><code>:CheckStatement&#32;a&#32;owl:Class&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;Check&#32;Statement&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;refers&#32;to&#32;a&#32;type&#32;of&#32;statement&#32;that&#32;is&#32;used&#32;to&#32;specify&#32;condit...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32;:statement&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:subClassOf&#32;:Statement&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-139)|Pointer|<pre lang="Turtle"><code>:PartialSafetyFactor0&#32;a&#32;owl:NamedIndividual,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;skos:Concept,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;:QuantityKind&#32;;  &#10; &#32; &#32; &#32; &#32;qudt:applicableUnit&#32; &#60;http://qudt.org/vocab/unit/UNITLESS> &#32;;  &#10; &#32; &#32; &#32; &#32;qudt:hasDimensionVector&#32; &#60;http://qudt.org/vocab/dimensionvector/A0E0L0I0M0H0T0D0> &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32;:quantity&lowbar;kinds&#32;;  &#10; &#32; &#32; &#32; &#32;skos:broader&#32;:PartialSafetyFactor&#32;;  &#10; &#32; &#32; &#32; &#32;skos:definition&#32; &#34;Also&#32;written&#32;γM0,&#32;the&#32;partial&#32;safety&#32;factor&#32;for&#32;resistance&#32;r...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;skos:prefLabel&#32; &#34;Partial&#32;Safety&#32;Factor&#34;@en&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-139)|Pointer|<pre lang="Turtle"><code>:PartialSafetyFactor&#32;a&#32;owl:NamedIndividual,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;skos:Concept,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;:QuantityKind&#32;;  &#10; &#32; &#32; &#32; &#32;qudt:applicableUnit&#32; &#60;http://qudt.org/vocab/unit/UNITLESS> &#32;;  &#10; &#32; &#32; &#32; &#32;qudt:hasDimensionVector&#32; &#60;http://qudt.org/vocab/dimensionvector/A0E0L0I0M0H0T0D0> &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32;:quantity&lowbar;kinds&#32;;  &#10; &#32; &#32; &#32; &#32;skos:definition&#32; &#34;Also&#32;written&#32;γM,&#32;the&#32;partial&#32;safety&#32;factor&#32;for&#32;resistance.&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;skos:prefLabel&#32; &#34;Partial&#32;Safety&#32;Factor&#34;@en&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-139)|Pointer|<pre lang="Turtle"><code>:PartialSafetyFactor1&#32;a&#32;owl:NamedIndividual,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;skos:Concept,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;:QuantityKind&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;Partial&#32;Safety&#32;Factor&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;qudt:applicableUnit&#32; &#60;http://qudt.org/vocab/unit/UNITLESS> &#32;;  &#10; &#32; &#32; &#32; &#32;qudt:hasDimensionVector&#32; &#60;http://qudt.org/vocab/dimensionvector/A0E0L0I0M0H0T0D0> &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32;:quantity&lowbar;kinds&#32;;  &#10; &#32; &#32; &#32; &#32;skos:broader&#32;:PartialSafetyFactor&#32;;  &#10; &#32; &#32; &#32; &#32;skos:definition&#32; &#34;Also&#32;written&#32;γM1,&#32;the&#32;partial&#32;safety&#32;factor&#32;for&#32;resistance&#32;r...&#34; &#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-139)|Pointer|<pre lang="Turtle"><code>:severity&#32;a&#32;owl:ObjectProperty&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;severity&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;Each&#32;verification&#32;result&#32;has&#32;exactly&#32;one&#32;value&#32;for&#32;the&#32;prope...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:domain&#32;:VerificationResult&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32;:compliance&lowbar;verification&lowbar;report&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:range&#32;:Severity&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-139)|Pointer|<pre lang="Turtle"><code>:Severity&#32;a&#32;owl:Class&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;Severity&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;The&#32;class&#32;of&#32;validation&#32;result&#32;severity&#32;levels,&#32;including&#32;vi...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32;:compliance&lowbar;verification&lowbar;report&#32;.</code></pre>|

***
### MinorFail Outcome number 140

[Jump to summary definition](#summary-MinorFail-140)	|	[Previous MinorFail outcome](#minorfail-outcome-number-139)	|	[Next MinorFail outcome](#minorfail-outcome-number-141)

:exclamation:MinorFail outcome
#### Subject detail
|Name|all-fragments|
|----|----|
|Title|All&#32;the&#32;fragments&#32;from&#32;branch&#32;HEAD&#32;that&#32;are&#32;syntaxically&#32;correct&#32;as&#32;well&#32;as&#32;their&#32;recursive&#32;imports|
|Composition|- [Module aec3po](https://github.com/Accord-Project/aec3po/blob/HEAD/src/aec3po.ttl)<br/>- [Module check&lowbar;method](https://github.com/Accord-Project/aec3po/blob/HEAD/src/check_method.ttl)<br/>- [Module checking&lowbar;act](https://github.com/Accord-Project/aec3po/blob/HEAD/src/checking_act.ttl)<br/>- [Module compliance&lowbar;verification&lowbar;report](https://github.com/Accord-Project/aec3po/blob/HEAD/src/compliance_verification_report.ttl)<br/>- [Module data&lowbar;requirement](https://github.com/Accord-Project/aec3po/blob/HEAD/src/data_requirement.ttl)<br/>- [Module document](https://github.com/Accord-Project/aec3po/blob/HEAD/src/document.ttl)<br/>- [Module evidence](https://github.com/Accord-Project/aec3po/blob/HEAD/src/evidence.ttl)<br/>- [Module feature&lowbar;of&lowbar;interest](https://github.com/Accord-Project/aec3po/blob/HEAD/src/feature_of_interest.ttl)<br/>- [Module legal&lowbar;verifier](https://github.com/Accord-Project/aec3po/blob/HEAD/src/legal_verifier.ttl)<br/>- [Module model](https://github.com/Accord-Project/aec3po/blob/HEAD/src/model.ttl)<br/>- [Module rase&lowbar;statement](https://github.com/Accord-Project/aec3po/blob/HEAD/src/rase_statement.ttl)<br/>- [Module statement](https://github.com/Accord-Project/aec3po/blob/HEAD/src/statement.ttl)<br/>- [Module table](https://github.com/Accord-Project/aec3po/blob/HEAD/src/table.ttl)<br/>- [Module vocabularies/&lowbar;shape](https://github.com/Accord-Project/aec3po/blob/HEAD/src/vocabularies/_shape.ttl)<br/>- [Module vocabularies/administrative&lowbar;areas](https://github.com/Accord-Project/aec3po/blob/HEAD/src/vocabularies/administrative_areas.ttl)<br/>- [Module vocabularies/building&lowbar;structure](https://github.com/Accord-Project/aec3po/blob/HEAD/src/vocabularies/building_structure.ttl)<br/>- [Module vocabularies/building&lowbar;usage](https://github.com/Accord-Project/aec3po/blob/HEAD/src/vocabularies/building_usage.ttl)<br/>- [Module vocabularies/check&lowbar;method&lowbar;comparators](https://github.com/Accord-Project/aec3po/blob/HEAD/src/vocabularies/check_method_comparators.ttl)<br/>- [Module vocabularies/check&lowbar;method&lowbar;operators](https://github.com/Accord-Project/aec3po/blob/HEAD/src/vocabularies/check_method_operators.ttl)<br/>- [Module vocabularies/disciplines](https://github.com/Accord-Project/aec3po/blob/HEAD/src/vocabularies/disciplines.ttl)<br/>- [Module vocabularies/permitting&lowbar;stages](https://github.com/Accord-Project/aec3po/blob/HEAD/src/vocabularies/permitting_stages.ttl)<br/>- [Module vocabularies/quantity&lowbar;kinds](https://github.com/Accord-Project/aec3po/blob/HEAD/src/vocabularies/quantity_kinds.ttl)|

#### Criterion detail
|Identifier|[domain-and-range-referencing](https://ns.inria.fr/olivaw#domain-and-range-referencing)|
|----|----|
|Title|Domain&#32;and&#32;range&#32;referencing&#32;test|
|Description|A&#32;test&#32;case&#32;from&#32;the&#32;Best&#32;Practices&#32;tests&#32;checking&#32;if&#32;all&#32;the&#32;ranges&#32;and&#32;domains&#32;from&#32;the&#32;test&#32;subject&#32;point&#32;to&#32;terms&#32;that&#32;are&#32;defined&#32;in&#32;the&#32;vocabulary.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-140)|Identifier|`domain-out-of-vocabulary`|
|[Section top](#minorfail-outcome-number-140)|Title|Domain&#32;out&#32;of&#32;vocabulary|
|[Section top](#minorfail-outcome-number-140)|Description|Some&#32;properties&#32;have&#32;a&#32;domain&#32;out&#32;of&#32;the&#32;ontology|
|[Section top](#minorfail-outcome-number-140)|Pointer|<pre lang="Turtle"><code>:usedMethod&#32;a&#32;owl:ObjectProperty&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;used&#32;method&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;Links&#32;a&#32;checking&#32;act&#32;to&#32;the&#32;method&#32;it&#32;used&#32;(a&#32;aec3po:CheckMe...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:domain&#32; &#91;&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:onProperty&#32;:usedMethod&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:someValuesFrom&#32;:CheckMethod&#32;],  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#91;&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:onProperty&#32;:madeBy&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:someValuesFrom&#32;:ProcessVerifier&#32;],  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#91;&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:onProperty&#32;:checked&#32;],  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#91;&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:onProperty&#32;:hasReport&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:someValuesFrom&#32;:ComplianceVerificationReport&#32;],  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#60;http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#Event>,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;:CheckingAct&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32;:checking&lowbar;act&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:range&#32; &#91;&#32;a&#32;owl:Class&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:unionOf&#32;(&#32;:FeatureOfInterest&#32;:Property&#32;:CheckMethod&#32;)&#32;],  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#60;http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#Method>,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;:CheckMethod&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-140)|Pointer|<pre lang="Turtle"><code>http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#Event</code></pre>|
|[Section top](#minorfail-outcome-number-140)|Pointer|<pre lang="Turtle"><code>:madeBy&#32;a&#32;owl:ObjectProperty&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;made&#32;by&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;Links&#32;a&#32;checking&#32;act&#32;to&#32;the&#32;process&#32;verifier&#32;that&#32;made&#32;it&#32;(a...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:domain&#32; &#91;&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:onProperty&#32;:usedMethod&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:someValuesFrom&#32;:CheckMethod&#32;],  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#91;&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:onProperty&#32;:madeBy&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:someValuesFrom&#32;:ProcessVerifier&#32;],  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#91;&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:onProperty&#32;:checked&#32;],  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#91;&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:onProperty&#32;:hasReport&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:someValuesFrom&#32;:ComplianceVerificationReport&#32;],  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#60;http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#Event>,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;:CheckingAct&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32;:checking&lowbar;act&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:range&#32;:ProcessVerifier&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-140)|Pointer|<pre lang="Turtle"><code>:checked&#32;a&#32;owl:ObjectProperty&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;checked&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;Links&#32;a&#32;checking&#32;act&#32;to&#32;some&#32;entity&#32;(ex.&#32;statement,&#32;feature&#32;...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:domain&#32; &#91;&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:onProperty&#32;:usedMethod&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:someValuesFrom&#32;:CheckMethod&#32;],  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#91;&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:onProperty&#32;:madeBy&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:someValuesFrom&#32;:ProcessVerifier&#32;],  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#91;&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:onProperty&#32;:checked&#32;],  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#91;&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:onProperty&#32;:hasReport&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:someValuesFrom&#32;:ComplianceVerificationReport&#32;],  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#60;http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#Event>,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;:CheckingAct&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32;:checking&lowbar;act&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-140)|Pointer|<pre lang="Turtle"><code>:hasReport&#32;a&#32;owl:ObjectProperty&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;has&#32;report&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;Links&#32;a&#32;checking&#32;act&#32;to&#32;the&#32;resulting&#32;compliance&#32;verificatio...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:domain&#32; &#91;&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:onProperty&#32;:usedMethod&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:someValuesFrom&#32;:CheckMethod&#32;],  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#91;&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:onProperty&#32;:madeBy&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:someValuesFrom&#32;:ProcessVerifier&#32;],  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#91;&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:onProperty&#32;:checked&#32;],  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#91;&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:onProperty&#32;:hasReport&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:someValuesFrom&#32;:ComplianceVerificationReport&#32;],  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#60;http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#Event>,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;:CheckingAct&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32;:checking&lowbar;act&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:range&#32; &#91;&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:onProperty&#32;:conforms&#32;],  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;:ComplianceVerificationReport&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-140)|Pointer|<pre lang="Turtle"><code>:operationalizes&#32;a&#32;owl:ObjectProperty&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;operationalizes&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;Links&#32;a&#32;check&#32;method&#32;to&#32;a&#32;check&#32;statement&#32;in&#32;a&#32;document&#32;that...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:domain&#32; &#91;&#32;a&#32;owl:Class&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:unionOf&#32;(&#32;:FeatureOfInterest&#32;:Property&#32;:CheckMethod&#32;)&#32;],  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#60;http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#Method>,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;:CheckMethod&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32;:check&lowbar;method&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:range&#32; &#91;&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:allValuesFrom&#32;:DocumentSubdivision&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:onProperty&#32;:hasSubdivision&#32;],  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#91;&#32;owl:unionOf&#32;(&#32;:Document&#32;:DocumentSubdivision&#32;)&#32;],  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;:CheckStatement,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;:DocumentSubdivision,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;:Statement&#32;;  &#10; &#32; &#32; &#32; &#32;owl:inverseOf&#32;:isOperationalizedBy&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-140)|Pointer|<pre lang="Turtle"><code>http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#Method</code></pre>|
|[Section top](#minorfail-outcome-number-140)|Pointer|<pre lang="Turtle"><code>:hasComparator&#32;a&#32;owl:FunctionalProperty,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:ObjectProperty&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;has&#32;comparator&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;Links&#32;a&#32;numerical&#32;check&#32;method&#32;to&#32;the&#32;check&#32;method&#32;comparato...&#34;,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#34;The&#32;comparator&#32;of&#32;a&#32;feature&#32;of&#32;interest&#32;or&#32;a&#32;property&#32;of&#32;tha...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:domain&#32;&lowbar;:n015ea156b1b847fd8cda0d232221dd04b1,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#60;http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#Method>,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;:CheckMethod,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;:NumericalCheckMethod&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32;:check&lowbar;method,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;:check&lowbar;method&lowbar;comparators&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:range&#32;&lowbar;:n015ea156b1b847fd8cda0d232221dd04b1,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;&lowbar;:n015ea156b1b847fd8cda0d232221dd04b2,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#91;&#32;rdfs:subClassOf&#32;&lowbar;:n015ea156b1b847fd8cda0d232221dd04b1,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;&lowbar;:n015ea156b1b847fd8cda0d232221dd04b2,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#60;http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#Method>,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;skos:Concept,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;:CheckMethod,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;:CheckMethodComparator&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:equivalentClass&#32;:CheckMethodComparator&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:intersectionOf&#32;(&#32;skos:Concept&#32;&lowbar;:n015ea156b1b847fd8cda0d232221dd04b2&#32;)&#32;],  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#60;http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#Method>,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;skos:Concept,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;:CheckMethod,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;:CheckMethodComparator&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:subPropertyOf&#32;:hasDesign&#32;.  &#10;&lowbar;:n015ea156b1b847fd8cda0d232221dd04b6&#32;rdf:first&#32;:CheckMethod&#32;;  &#10; &#32; &#32; &#32; &#32;rdf:rest&#32;()&#32;.  &#10;&lowbar;:n015ea156b1b847fd8cda0d232221dd04b7&#32;rdf:first&#32;:Property&#32;;  &#10; &#32; &#32; &#32; &#32;rdf:rest&#32;&lowbar;:n015ea156b1b847fd8cda0d232221dd04b6&#32;.  &#10;&lowbar;:n015ea156b1b847fd8cda0d232221dd04b8&#32;rdf:first&#32;:FeatureOfInterest&#32;;  &#10; &#32; &#32; &#32; &#32;rdf:rest&#32;&lowbar;:n015ea156b1b847fd8cda0d232221dd04b7&#32;.  &#10;&lowbar;:n015ea156b1b847fd8cda0d232221dd04b1&#32;a&#32;owl:Class&#32;;  &#10; &#32; &#32; &#32; &#32;owl:unionOf&#32;&lowbar;:n015ea156b1b847fd8cda0d232221dd04b8&#32;.  &#10;&lowbar;:n015ea156b1b847fd8cda0d232221dd04b2&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32;owl:hasValue&#32;:CheckMethodComparatorNomenclature&#32;;  &#10; &#32; &#32; &#32; &#32;owl:onProperty&#32;skos:inScheme&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-140)|Pointer|<pre lang="Turtle"><code>:hasNestedValue&#32;a&#32;owl:ObjectProperty&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;hasNestedValue&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;TBD&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:domain&#32; &#91;&#32;a&#32;owl:Class&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:unionOf&#32;(&#32;:FeatureOfInterest&#32;:Property&#32;:CheckMethod&#32;)&#32;],  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#60;http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#Method>,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;:CheckMethod&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32;:check&lowbar;method&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-140)|Pointer|<pre lang="Turtle"><code>:hasOperator&#32;a&#32;owl:FunctionalProperty,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:ObjectProperty&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;has&#32;operator&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;Links&#32;a&#32;boolean&#32;check&#32;method&#32;to&#32;the&#32;check&#32;method&#32;operator&#32;it...&#34;,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#34;The&#32;operator&#32;of&#32;a&#32;feature&#32;of&#32;interest&#32;or&#32;a&#32;property&#32;of&#32;that&#32;...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:domain&#32;&lowbar;:n67732396a67e48b2a6143b20e385db23b1,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#60;http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#Method>,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;:BooleanCheckMethod,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;:CheckMethod&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32;:check&lowbar;method,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;:check&lowbar;method&lowbar;Operators&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:range&#32;&lowbar;:n67732396a67e48b2a6143b20e385db23b1,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;&lowbar;:n67732396a67e48b2a6143b20e385db23b2,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#91;&#32;rdfs:subClassOf&#32;&lowbar;:n67732396a67e48b2a6143b20e385db23b1,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;&lowbar;:n67732396a67e48b2a6143b20e385db23b2,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#60;http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#Method>,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;skos:Concept,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;:CheckMethod,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;:CheckMethodOperator&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:equivalentClass&#32;:CheckMethodOperator&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:intersectionOf&#32;(&#32;skos:Concept&#32;&lowbar;:n67732396a67e48b2a6143b20e385db23b2&#32;)&#32;],  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#60;http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#Method>,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;skos:Concept,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;:CheckMethod,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;:CheckMethodOperator&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:subPropertyOf&#32;:hasDesign&#32;.  &#10;&lowbar;:n67732396a67e48b2a6143b20e385db23b6&#32;rdf:first&#32;:CheckMethod&#32;;  &#10; &#32; &#32; &#32; &#32;rdf:rest&#32;()&#32;.  &#10;&lowbar;:n67732396a67e48b2a6143b20e385db23b7&#32;rdf:first&#32;:Property&#32;;  &#10; &#32; &#32; &#32; &#32;rdf:rest&#32;&lowbar;:n67732396a67e48b2a6143b20e385db23b6&#32;.  &#10;&lowbar;:n67732396a67e48b2a6143b20e385db23b8&#32;rdf:first&#32;:FeatureOfInterest&#32;;  &#10; &#32; &#32; &#32; &#32;rdf:rest&#32;&lowbar;:n67732396a67e48b2a6143b20e385db23b7&#32;.  &#10;&lowbar;:n67732396a67e48b2a6143b20e385db23b1&#32;a&#32;owl:Class&#32;;  &#10; &#32; &#32; &#32; &#32;owl:unionOf&#32;&lowbar;:n67732396a67e48b2a6143b20e385db23b8&#32;.  &#10;&lowbar;:n67732396a67e48b2a6143b20e385db23b2&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32;owl:hasValue&#32;:CheckMethodOperatorNomenclature&#32;;  &#10; &#32; &#32; &#32; &#32;owl:onProperty&#32;skos:inScheme&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-140)|Pointer|<pre lang="Turtle"><code>:hasProperty&#32;a&#32;owl:ObjectProperty&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;has&#32;Property&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;Links&#32;a&#32;feature&#32;of&#32;interest&#32;to&#32;one&#32;of&#32;its&#32;aspect&#32;that&#32;is&#32;int...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:domain&#32;&lowbar;:nd6f1295539934bdf9567cf3ae0b04b73b1,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#60;http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#Object>,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#60;https://saref.etsi.org/core/FeatureOfInterest>,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;:FeatureOfInterest&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32;:feature&lowbar;of&lowbar;interest&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:range&#32;&lowbar;:nd6f1295539934bdf9567cf3ae0b04b73b1,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#60;http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#Quality>,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;:Property&#32;;  &#10; &#32; &#32; &#32; &#32;skos:example&#32; &#34;Links&#32;a&#32;space&#32;to&#32;the&#32;area&#32;property&#32;of&#32;that&#32;space,&#32;a&#32;wall&#32;to&#32;...&#34; &#32;.  &#10;&lowbar;:nd6f1295539934bdf9567cf3ae0b04b73b2&#32;rdf:first&#32;:CheckMethod&#32;;  &#10; &#32; &#32; &#32; &#32;rdf:rest&#32;()&#32;.  &#10;&lowbar;:nd6f1295539934bdf9567cf3ae0b04b73b3&#32;rdf:first&#32;:Property&#32;;  &#10; &#32; &#32; &#32; &#32;rdf:rest&#32;&lowbar;:nd6f1295539934bdf9567cf3ae0b04b73b2&#32;.  &#10;&lowbar;:nd6f1295539934bdf9567cf3ae0b04b73b4&#32;rdf:first&#32;:FeatureOfInterest&#32;;  &#10; &#32; &#32; &#32; &#32;rdf:rest&#32;&lowbar;:nd6f1295539934bdf9567cf3ae0b04b73b3&#32;.  &#10;&lowbar;:nd6f1295539934bdf9567cf3ae0b04b73b1&#32;a&#32;owl:Class&#32;;  &#10; &#32; &#32; &#32; &#32;owl:unionOf&#32;&lowbar;:nd6f1295539934bdf9567cf3ae0b04b73b4&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-140)|Pointer|<pre lang="Turtle"><code>http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#Object</code></pre>|
|[Section top](#minorfail-outcome-number-140)|Pointer|<pre lang="Turtle"><code>:hasProperty&#32;a&#32;owl:ObjectProperty&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;has&#32;Property&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;Links&#32;a&#32;feature&#32;of&#32;interest&#32;to&#32;one&#32;of&#32;its&#32;aspect&#32;that&#32;is&#32;int...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:domain&#32;&lowbar;:nbe5b0ec01add4e4d8084ea6b4b2e3af8b1,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#60;http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#Object>,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#60;https://saref.etsi.org/core/FeatureOfInterest>,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;:FeatureOfInterest&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32;:feature&lowbar;of&lowbar;interest&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:range&#32;&lowbar;:nbe5b0ec01add4e4d8084ea6b4b2e3af8b1,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#60;http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#Quality>,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;:Property&#32;;  &#10; &#32; &#32; &#32; &#32;skos:example&#32; &#34;Links&#32;a&#32;space&#32;to&#32;the&#32;area&#32;property&#32;of&#32;that&#32;space,&#32;a&#32;wall&#32;to&#32;...&#34; &#32;.  &#10;&lowbar;:nbe5b0ec01add4e4d8084ea6b4b2e3af8b2&#32;rdf:first&#32;:CheckMethod&#32;;  &#10; &#32; &#32; &#32; &#32;rdf:rest&#32;()&#32;.  &#10;&lowbar;:nbe5b0ec01add4e4d8084ea6b4b2e3af8b3&#32;rdf:first&#32;:Property&#32;;  &#10; &#32; &#32; &#32; &#32;rdf:rest&#32;&lowbar;:nbe5b0ec01add4e4d8084ea6b4b2e3af8b2&#32;.  &#10;&lowbar;:nbe5b0ec01add4e4d8084ea6b4b2e3af8b4&#32;rdf:first&#32;:FeatureOfInterest&#32;;  &#10; &#32; &#32; &#32; &#32;rdf:rest&#32;&lowbar;:nbe5b0ec01add4e4d8084ea6b4b2e3af8b3&#32;.  &#10;&lowbar;:nbe5b0ec01add4e4d8084ea6b4b2e3af8b1&#32;a&#32;owl:Class&#32;;  &#10; &#32; &#32; &#32; &#32;owl:unionOf&#32;&lowbar;:nbe5b0ec01add4e4d8084ea6b4b2e3af8b4&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-140)|Pointer|<pre lang="Turtle"><code>https://saref.etsi.org/core/FeatureOfInterest</code></pre>|
|[Section top](#minorfail-outcome-number-140)|Pointer|<pre lang="Turtle"><code>:hasQuantityKind&#32;a&#32;owl:ObjectProperty&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;has&#32;quantity&#32;kind&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;Links&#32;a&#32;property&#32;to&#32;its&#32;quantity&#32;kind&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:domain&#32; &#91;&#32;a&#32;owl:Class&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:unionOf&#32;(&#32;:FeatureOfInterest&#32;:Property&#32;:CheckMethod&#32;)&#32;],  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#60;http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#Quality>,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;:Property&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32;:feature&lowbar;of&lowbar;interest&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:range&#32;&lowbar;:n412771b6d3bc4697a29e39a3a54f1721b5,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#91;&#32;rdfs:subClassOf&#32;&lowbar;:n412771b6d3bc4697a29e39a3a54f1721b5,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;qudt:QuantityKind,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#60;http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#Region>,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;skos:Concept,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;:QuantityKind&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:equivalentClass&#32;:QuantityKind&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:intersectionOf&#32;(&#32;skos:Concept&#32;&lowbar;:n412771b6d3bc4697a29e39a3a54f1721b5&#32;)&#32;],  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;qudt:QuantityKind,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#60;http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#Region>,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;skos:Concept,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;:QuantityKind&#32;;  &#10; &#32; &#32; &#32; &#32;skos:example&#32; &#34;A&#32;space&#32;area&#32;property&#32;to&#32;the&#32;property&#32;kind&#32; &#92; &#34;area&#92; &#34;.&#34;@en&#32;.  &#10;&lowbar;:n412771b6d3bc4697a29e39a3a54f1721b5&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32;owl:hasValue&#32;:QuantityKindNomenclature&#32;;  &#10; &#32; &#32; &#32; &#32;owl:onProperty&#32;skos:inScheme&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-140)|Pointer|<pre lang="Turtle"><code>http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#Quality</code></pre>|

***
### MinorFail Outcome number 141

[Jump to summary definition](#summary-MinorFail-141)	|	[Previous MinorFail outcome](#minorfail-outcome-number-140)	|	[Next MinorFail outcome](#minorfail-outcome-number-142)

:exclamation:MinorFail outcome
#### Subject detail
|Name|all-fragments|
|----|----|
|Title|All&#32;the&#32;fragments&#32;from&#32;branch&#32;HEAD&#32;that&#32;are&#32;syntaxically&#32;correct&#32;as&#32;well&#32;as&#32;their&#32;recursive&#32;imports|
|Composition|- [Module aec3po](https://github.com/Accord-Project/aec3po/blob/HEAD/src/aec3po.ttl)<br/>- [Module check&lowbar;method](https://github.com/Accord-Project/aec3po/blob/HEAD/src/check_method.ttl)<br/>- [Module checking&lowbar;act](https://github.com/Accord-Project/aec3po/blob/HEAD/src/checking_act.ttl)<br/>- [Module compliance&lowbar;verification&lowbar;report](https://github.com/Accord-Project/aec3po/blob/HEAD/src/compliance_verification_report.ttl)<br/>- [Module data&lowbar;requirement](https://github.com/Accord-Project/aec3po/blob/HEAD/src/data_requirement.ttl)<br/>- [Module document](https://github.com/Accord-Project/aec3po/blob/HEAD/src/document.ttl)<br/>- [Module evidence](https://github.com/Accord-Project/aec3po/blob/HEAD/src/evidence.ttl)<br/>- [Module feature&lowbar;of&lowbar;interest](https://github.com/Accord-Project/aec3po/blob/HEAD/src/feature_of_interest.ttl)<br/>- [Module legal&lowbar;verifier](https://github.com/Accord-Project/aec3po/blob/HEAD/src/legal_verifier.ttl)<br/>- [Module model](https://github.com/Accord-Project/aec3po/blob/HEAD/src/model.ttl)<br/>- [Module rase&lowbar;statement](https://github.com/Accord-Project/aec3po/blob/HEAD/src/rase_statement.ttl)<br/>- [Module statement](https://github.com/Accord-Project/aec3po/blob/HEAD/src/statement.ttl)<br/>- [Module table](https://github.com/Accord-Project/aec3po/blob/HEAD/src/table.ttl)<br/>- [Module vocabularies/&lowbar;shape](https://github.com/Accord-Project/aec3po/blob/HEAD/src/vocabularies/_shape.ttl)<br/>- [Module vocabularies/administrative&lowbar;areas](https://github.com/Accord-Project/aec3po/blob/HEAD/src/vocabularies/administrative_areas.ttl)<br/>- [Module vocabularies/building&lowbar;structure](https://github.com/Accord-Project/aec3po/blob/HEAD/src/vocabularies/building_structure.ttl)<br/>- [Module vocabularies/building&lowbar;usage](https://github.com/Accord-Project/aec3po/blob/HEAD/src/vocabularies/building_usage.ttl)<br/>- [Module vocabularies/check&lowbar;method&lowbar;comparators](https://github.com/Accord-Project/aec3po/blob/HEAD/src/vocabularies/check_method_comparators.ttl)<br/>- [Module vocabularies/check&lowbar;method&lowbar;operators](https://github.com/Accord-Project/aec3po/blob/HEAD/src/vocabularies/check_method_operators.ttl)<br/>- [Module vocabularies/disciplines](https://github.com/Accord-Project/aec3po/blob/HEAD/src/vocabularies/disciplines.ttl)<br/>- [Module vocabularies/permitting&lowbar;stages](https://github.com/Accord-Project/aec3po/blob/HEAD/src/vocabularies/permitting_stages.ttl)<br/>- [Module vocabularies/quantity&lowbar;kinds](https://github.com/Accord-Project/aec3po/blob/HEAD/src/vocabularies/quantity_kinds.ttl)|

#### Criterion detail
|Identifier|[domain-and-range-referencing](https://ns.inria.fr/olivaw#domain-and-range-referencing)|
|----|----|
|Title|Domain&#32;and&#32;range&#32;referencing&#32;test|
|Description|A&#32;test&#32;case&#32;from&#32;the&#32;Best&#32;Practices&#32;tests&#32;checking&#32;if&#32;all&#32;the&#32;ranges&#32;and&#32;domains&#32;from&#32;the&#32;test&#32;subject&#32;point&#32;to&#32;terms&#32;that&#32;are&#32;defined&#32;in&#32;the&#32;vocabulary.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-141)|Identifier|`range-out-of-vocabulary`|
|[Section top](#minorfail-outcome-number-141)|Title|Range&#32;out&#32;of&#32;vocabulary|
|[Section top](#minorfail-outcome-number-141)|Description|Some&#32;properties&#32;have&#32;a&#32;range&#32;out&#32;of&#32;the&#32;ontology|
|[Section top](#minorfail-outcome-number-141)|Pointer|<pre lang="Turtle"><code>:usedMethod&#32;a&#32;owl:ObjectProperty&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;used&#32;method&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;Links&#32;a&#32;checking&#32;act&#32;to&#32;the&#32;method&#32;it&#32;used&#32;(a&#32;aec3po:CheckMe...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:domain&#32; &#91;&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:onProperty&#32;:usedMethod&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:someValuesFrom&#32;:CheckMethod&#32;],  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#91;&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:onProperty&#32;:madeBy&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:someValuesFrom&#32;:ProcessVerifier&#32;],  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#91;&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:onProperty&#32;:checked&#32;],  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#91;&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:onProperty&#32;:hasReport&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:someValuesFrom&#32;:ComplianceVerificationReport&#32;],  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#60;http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#Event>,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;:CheckingAct&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32;:checking&lowbar;act&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:range&#32; &#91;&#32;a&#32;owl:Class&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:unionOf&#32;(&#32;:FeatureOfInterest&#32;:Property&#32;:CheckMethod&#32;)&#32;],  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#60;http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#Method>,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;:CheckMethod&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-141)|Pointer|<pre lang="Turtle"><code>http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#Method</code></pre>|
|[Section top](#minorfail-outcome-number-141)|Pointer|<pre lang="Turtle"><code>:isOperationalizedBy&#32;a&#32;owl:ObjectProperty&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;is&#32;operationalized&#32;by&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;Links&#32;a&#32;check&#32;statement&#32;in&#32;a&#32;document&#32;to&#32;a&#32;check&#32;method&#32;that...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:domain&#32; &#91;&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:allValuesFrom&#32;:DocumentSubdivision&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:onProperty&#32;:hasSubdivision&#32;],  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#91;&#32;owl:unionOf&#32;(&#32;:Document&#32;:DocumentSubdivision&#32;)&#32;],  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;:CheckStatement,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;:DocumentSubdivision,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;:Statement&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32;:check&lowbar;method&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:range&#32; &#91;&#32;a&#32;owl:Class&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:unionOf&#32;(&#32;:FeatureOfInterest&#32;:Property&#32;:CheckMethod&#32;)&#32;],  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#60;http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#Method>,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;:CheckMethod&#32;;  &#10; &#32; &#32; &#32; &#32;owl:inverseOf&#32;:operationalizes&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-141)|Pointer|<pre lang="Turtle"><code>:hasComparator&#32;a&#32;owl:FunctionalProperty,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:ObjectProperty&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;has&#32;comparator&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;Links&#32;a&#32;numerical&#32;check&#32;method&#32;to&#32;the&#32;check&#32;method&#32;comparato...&#34;,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#34;The&#32;comparator&#32;of&#32;a&#32;feature&#32;of&#32;interest&#32;or&#32;a&#32;property&#32;of&#32;tha...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:domain&#32;&lowbar;:n6b185c1daac64a7d8662d39bda3b80f5b1,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#60;http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#Method>,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;:CheckMethod,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;:NumericalCheckMethod&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32;:check&lowbar;method,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;:check&lowbar;method&lowbar;comparators&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:range&#32;&lowbar;:n6b185c1daac64a7d8662d39bda3b80f5b1,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;&lowbar;:n6b185c1daac64a7d8662d39bda3b80f5b2,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#91;&#32;rdfs:subClassOf&#32;&lowbar;:n6b185c1daac64a7d8662d39bda3b80f5b1,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;&lowbar;:n6b185c1daac64a7d8662d39bda3b80f5b2,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#60;http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#Method>,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;skos:Concept,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;:CheckMethod,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;:CheckMethodComparator&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:equivalentClass&#32;:CheckMethodComparator&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:intersectionOf&#32;(&#32;skos:Concept&#32;&lowbar;:n6b185c1daac64a7d8662d39bda3b80f5b2&#32;)&#32;],  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#60;http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#Method>,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;skos:Concept,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;:CheckMethod,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;:CheckMethodComparator&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:subPropertyOf&#32;:hasDesign&#32;.  &#10;&lowbar;:n6b185c1daac64a7d8662d39bda3b80f5b6&#32;rdf:first&#32;:CheckMethod&#32;;  &#10; &#32; &#32; &#32; &#32;rdf:rest&#32;()&#32;.  &#10;&lowbar;:n6b185c1daac64a7d8662d39bda3b80f5b7&#32;rdf:first&#32;:Property&#32;;  &#10; &#32; &#32; &#32; &#32;rdf:rest&#32;&lowbar;:n6b185c1daac64a7d8662d39bda3b80f5b6&#32;.  &#10;&lowbar;:n6b185c1daac64a7d8662d39bda3b80f5b8&#32;rdf:first&#32;:FeatureOfInterest&#32;;  &#10; &#32; &#32; &#32; &#32;rdf:rest&#32;&lowbar;:n6b185c1daac64a7d8662d39bda3b80f5b7&#32;.  &#10;&lowbar;:n6b185c1daac64a7d8662d39bda3b80f5b1&#32;a&#32;owl:Class&#32;;  &#10; &#32; &#32; &#32; &#32;owl:unionOf&#32;&lowbar;:n6b185c1daac64a7d8662d39bda3b80f5b8&#32;.  &#10;&lowbar;:n6b185c1daac64a7d8662d39bda3b80f5b2&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32;owl:hasValue&#32;:CheckMethodComparatorNomenclature&#32;;  &#10; &#32; &#32; &#32; &#32;owl:onProperty&#32;skos:inScheme&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-141)|Pointer|<pre lang="Turtle"><code>:hasComparator&#32;a&#32;owl:FunctionalProperty,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:ObjectProperty&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;has&#32;comparator&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;Links&#32;a&#32;numerical&#32;check&#32;method&#32;to&#32;the&#32;check&#32;method&#32;comparato...&#34;,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#34;The&#32;comparator&#32;of&#32;a&#32;feature&#32;of&#32;interest&#32;or&#32;a&#32;property&#32;of&#32;tha...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:domain&#32;&lowbar;:n9f261d66b5854a8c818b81aa4922eccdb1,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#60;http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#Method>,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;:CheckMethod,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;:NumericalCheckMethod&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32;:check&lowbar;method,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;:check&lowbar;method&lowbar;comparators&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:range&#32;&lowbar;:n9f261d66b5854a8c818b81aa4922eccdb1,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;&lowbar;:n9f261d66b5854a8c818b81aa4922eccdb2,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#91;&#32;rdfs:subClassOf&#32;&lowbar;:n9f261d66b5854a8c818b81aa4922eccdb1,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;&lowbar;:n9f261d66b5854a8c818b81aa4922eccdb2,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#60;http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#Method>,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;skos:Concept,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;:CheckMethod,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;:CheckMethodComparator&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:equivalentClass&#32;:CheckMethodComparator&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:intersectionOf&#32;(&#32;skos:Concept&#32;&lowbar;:n9f261d66b5854a8c818b81aa4922eccdb2&#32;)&#32;],  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#60;http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#Method>,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;skos:Concept,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;:CheckMethod,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;:CheckMethodComparator&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:subPropertyOf&#32;:hasDesign&#32;.  &#10;&lowbar;:n9f261d66b5854a8c818b81aa4922eccdb6&#32;rdf:first&#32;:CheckMethod&#32;;  &#10; &#32; &#32; &#32; &#32;rdf:rest&#32;()&#32;.  &#10;&lowbar;:n9f261d66b5854a8c818b81aa4922eccdb7&#32;rdf:first&#32;:Property&#32;;  &#10; &#32; &#32; &#32; &#32;rdf:rest&#32;&lowbar;:n9f261d66b5854a8c818b81aa4922eccdb6&#32;.  &#10;&lowbar;:n9f261d66b5854a8c818b81aa4922eccdb8&#32;rdf:first&#32;:FeatureOfInterest&#32;;  &#10; &#32; &#32; &#32; &#32;rdf:rest&#32;&lowbar;:n9f261d66b5854a8c818b81aa4922eccdb7&#32;.  &#10;&lowbar;:n9f261d66b5854a8c818b81aa4922eccdb1&#32;a&#32;owl:Class&#32;;  &#10; &#32; &#32; &#32; &#32;owl:unionOf&#32;&lowbar;:n9f261d66b5854a8c818b81aa4922eccdb8&#32;.  &#10;&lowbar;:n9f261d66b5854a8c818b81aa4922eccdb2&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32;owl:hasValue&#32;:CheckMethodComparatorNomenclature&#32;;  &#10; &#32; &#32; &#32; &#32;owl:onProperty&#32;skos:inScheme&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-141)|Pointer|<pre lang="Turtle"><code>:hasUnit&#32;a&#32;owl:FunctionalProperty,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:ObjectProperty&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;hasUnit&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;the&#32;hasUnit&#32;property&#32;is&#32;used&#32;to&#32;link&#32;a&#32;specific&#32;property&#32;or&#32;...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:domain&#32; &#91;&#32;a&#32;owl:Class&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:unionOf&#32;(&#32;:FeatureOfInterest&#32;:Property&#32;:CheckMethod&#32;)&#32;]&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32;:check&lowbar;method&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:range&#32;qudt:Unit&#32;;  &#10; &#32; &#32; &#32; &#32;owl:eqivalentProperty&#32;qudt:hasValue&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-141)|Pointer|<pre lang="Turtle"><code>http://qudt.org/schema/qudt/Unit</code></pre>|
|[Section top](#minorfail-outcome-number-141)|Pointer|<pre lang="Turtle"><code>:hasOperator&#32;a&#32;owl:FunctionalProperty,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:ObjectProperty&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;has&#32;operator&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;Links&#32;a&#32;boolean&#32;check&#32;method&#32;to&#32;the&#32;check&#32;method&#32;operator&#32;it...&#34;,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#34;The&#32;operator&#32;of&#32;a&#32;feature&#32;of&#32;interest&#32;or&#32;a&#32;property&#32;of&#32;that&#32;...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:domain&#32;&lowbar;:n648b05c08c1947a1b1207c6487863932b1,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#60;http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#Method>,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;:BooleanCheckMethod,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;:CheckMethod&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32;:check&lowbar;method,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;:check&lowbar;method&lowbar;Operators&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:range&#32;&lowbar;:n648b05c08c1947a1b1207c6487863932b1,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;&lowbar;:n648b05c08c1947a1b1207c6487863932b2,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#91;&#32;rdfs:subClassOf&#32;&lowbar;:n648b05c08c1947a1b1207c6487863932b1,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;&lowbar;:n648b05c08c1947a1b1207c6487863932b2,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#60;http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#Method>,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;skos:Concept,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;:CheckMethod,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;:CheckMethodOperator&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:equivalentClass&#32;:CheckMethodOperator&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:intersectionOf&#32;(&#32;skos:Concept&#32;&lowbar;:n648b05c08c1947a1b1207c6487863932b2&#32;)&#32;],  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#60;http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#Method>,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;skos:Concept,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;:CheckMethod,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;:CheckMethodOperator&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:subPropertyOf&#32;:hasDesign&#32;.  &#10;&lowbar;:n648b05c08c1947a1b1207c6487863932b6&#32;rdf:first&#32;:CheckMethod&#32;;  &#10; &#32; &#32; &#32; &#32;rdf:rest&#32;()&#32;.  &#10;&lowbar;:n648b05c08c1947a1b1207c6487863932b7&#32;rdf:first&#32;:Property&#32;;  &#10; &#32; &#32; &#32; &#32;rdf:rest&#32;&lowbar;:n648b05c08c1947a1b1207c6487863932b6&#32;.  &#10;&lowbar;:n648b05c08c1947a1b1207c6487863932b8&#32;rdf:first&#32;:FeatureOfInterest&#32;;  &#10; &#32; &#32; &#32; &#32;rdf:rest&#32;&lowbar;:n648b05c08c1947a1b1207c6487863932b7&#32;.  &#10;&lowbar;:n648b05c08c1947a1b1207c6487863932b1&#32;a&#32;owl:Class&#32;;  &#10; &#32; &#32; &#32; &#32;owl:unionOf&#32;&lowbar;:n648b05c08c1947a1b1207c6487863932b8&#32;.  &#10;&lowbar;:n648b05c08c1947a1b1207c6487863932b2&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32;owl:hasValue&#32;:CheckMethodOperatorNomenclature&#32;;  &#10; &#32; &#32; &#32; &#32;owl:onProperty&#32;skos:inScheme&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-141)|Pointer|<pre lang="Turtle"><code>:hasOperator&#32;a&#32;owl:FunctionalProperty,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:ObjectProperty&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;has&#32;operator&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;Links&#32;a&#32;boolean&#32;check&#32;method&#32;to&#32;the&#32;check&#32;method&#32;operator&#32;it...&#34;,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#34;The&#32;operator&#32;of&#32;a&#32;feature&#32;of&#32;interest&#32;or&#32;a&#32;property&#32;of&#32;that&#32;...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:domain&#32;&lowbar;:n999cfe83fe65422ca3c753d562739650b1,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#60;http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#Method>,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;:BooleanCheckMethod,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;:CheckMethod&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32;:check&lowbar;method,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;:check&lowbar;method&lowbar;Operators&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:range&#32;&lowbar;:n999cfe83fe65422ca3c753d562739650b1,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;&lowbar;:n999cfe83fe65422ca3c753d562739650b2,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#91;&#32;rdfs:subClassOf&#32;&lowbar;:n999cfe83fe65422ca3c753d562739650b1,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;&lowbar;:n999cfe83fe65422ca3c753d562739650b2,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#60;http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#Method>,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;skos:Concept,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;:CheckMethod,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;:CheckMethodOperator&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:equivalentClass&#32;:CheckMethodOperator&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:intersectionOf&#32;(&#32;skos:Concept&#32;&lowbar;:n999cfe83fe65422ca3c753d562739650b2&#32;)&#32;],  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#60;http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#Method>,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;skos:Concept,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;:CheckMethod,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;:CheckMethodOperator&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:subPropertyOf&#32;:hasDesign&#32;.  &#10;&lowbar;:n999cfe83fe65422ca3c753d562739650b6&#32;rdf:first&#32;:CheckMethod&#32;;  &#10; &#32; &#32; &#32; &#32;rdf:rest&#32;()&#32;.  &#10;&lowbar;:n999cfe83fe65422ca3c753d562739650b7&#32;rdf:first&#32;:Property&#32;;  &#10; &#32; &#32; &#32; &#32;rdf:rest&#32;&lowbar;:n999cfe83fe65422ca3c753d562739650b6&#32;.  &#10;&lowbar;:n999cfe83fe65422ca3c753d562739650b8&#32;rdf:first&#32;:FeatureOfInterest&#32;;  &#10; &#32; &#32; &#32; &#32;rdf:rest&#32;&lowbar;:n999cfe83fe65422ca3c753d562739650b7&#32;.  &#10;&lowbar;:n999cfe83fe65422ca3c753d562739650b1&#32;a&#32;owl:Class&#32;;  &#10; &#32; &#32; &#32; &#32;owl:unionOf&#32;&lowbar;:n999cfe83fe65422ca3c753d562739650b8&#32;.  &#10;&lowbar;:n999cfe83fe65422ca3c753d562739650b2&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32;owl:hasValue&#32;:CheckMethodOperatorNomenclature&#32;;  &#10; &#32; &#32; &#32; &#32;owl:onProperty&#32;skos:inScheme&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-141)|Pointer|<pre lang="Turtle"><code>:hasNestedTarget&#32;a&#32;owl:ObjectProperty&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;hasNestedTarget&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32;:check&lowbar;method&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:range&#32; &#91;&#32;a&#32;owl:Class&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:unionOf&#32;(&#32;:FeatureOfInterest&#32;:Property&#32;:CheckMethod&#32;)&#32;],  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#60;http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#Method>,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;:CheckMethod&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-141)|Pointer|<pre lang="Turtle"><code>:hasFormat&#32;a&#32;owl:ObjectProperty&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;Defines&#32;the&#32;format&#32;of&#32;an&#32;evidence,&#32;which&#32;is&#32;of&#32;type&#32;dct:form...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:domain&#32; &#91;&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:allValuesFrom&#32;:DocumentSubdivision&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:onProperty&#32;:hasSubdivision&#32;],  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#91;&#32;owl:unionOf&#32;(&#32;:Document&#32;:DocumentSubdivision&#32;)&#32;],  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;:DocumentSubdivision,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;:Statement&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32;:evidence&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:range&#32;dc:format&#32;;  &#10; &#32; &#32; &#32; &#32;skos:example&#32; &#34;an&#32;image,&#32;a&#32;drawing&#32;or&#32;a&#32;model&#32;can&#32;be&#32;an&#32;evidence.&#34;@en&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-141)|Pointer|<pre lang="Turtle"><code>:hasProperty&#32;a&#32;owl:ObjectProperty&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;has&#32;Property&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;Links&#32;a&#32;feature&#32;of&#32;interest&#32;to&#32;one&#32;of&#32;its&#32;aspect&#32;that&#32;is&#32;int...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:domain&#32;&lowbar;:nc70015c185ba46e2850273dbf819895fb1,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#60;http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#Object>,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#60;https://saref.etsi.org/core/FeatureOfInterest>,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;:FeatureOfInterest&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32;:feature&lowbar;of&lowbar;interest&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:range&#32;&lowbar;:nc70015c185ba46e2850273dbf819895fb1,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#60;http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#Quality>,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;:Property&#32;;  &#10; &#32; &#32; &#32; &#32;skos:example&#32; &#34;Links&#32;a&#32;space&#32;to&#32;the&#32;area&#32;property&#32;of&#32;that&#32;space,&#32;a&#32;wall&#32;to&#32;...&#34; &#32;.  &#10;&lowbar;:nc70015c185ba46e2850273dbf819895fb2&#32;rdf:first&#32;:CheckMethod&#32;;  &#10; &#32; &#32; &#32; &#32;rdf:rest&#32;()&#32;.  &#10;&lowbar;:nc70015c185ba46e2850273dbf819895fb3&#32;rdf:first&#32;:Property&#32;;  &#10; &#32; &#32; &#32; &#32;rdf:rest&#32;&lowbar;:nc70015c185ba46e2850273dbf819895fb2&#32;.  &#10;&lowbar;:nc70015c185ba46e2850273dbf819895fb4&#32;rdf:first&#32;:FeatureOfInterest&#32;;  &#10; &#32; &#32; &#32; &#32;rdf:rest&#32;&lowbar;:nc70015c185ba46e2850273dbf819895fb3&#32;.  &#10;&lowbar;:nc70015c185ba46e2850273dbf819895fb1&#32;a&#32;owl:Class&#32;;  &#10; &#32; &#32; &#32; &#32;owl:unionOf&#32;&lowbar;:nc70015c185ba46e2850273dbf819895fb4&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-141)|Pointer|<pre lang="Turtle"><code>http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#Quality</code></pre>|
|[Section top](#minorfail-outcome-number-141)|Pointer|<pre lang="Turtle"><code>:hasQuantityKind&#32;a&#32;owl:ObjectProperty&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;has&#32;quantity&#32;kind&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;Links&#32;a&#32;property&#32;to&#32;its&#32;quantity&#32;kind&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:domain&#32; &#91;&#32;a&#32;owl:Class&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:unionOf&#32;(&#32;:FeatureOfInterest&#32;:Property&#32;:CheckMethod&#32;)&#32;],  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#60;http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#Quality>,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;:Property&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32;:feature&lowbar;of&lowbar;interest&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:range&#32;&lowbar;:n3934dcd8936b44968182d44e5f51696ab5,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#91;&#32;rdfs:subClassOf&#32;&lowbar;:n3934dcd8936b44968182d44e5f51696ab5,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;qudt:QuantityKind,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#60;http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#Region>,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;skos:Concept,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;:QuantityKind&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:equivalentClass&#32;:QuantityKind&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:intersectionOf&#32;(&#32;skos:Concept&#32;&lowbar;:n3934dcd8936b44968182d44e5f51696ab5&#32;)&#32;],  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;qudt:QuantityKind,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#60;http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#Region>,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;skos:Concept,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;:QuantityKind&#32;;  &#10; &#32; &#32; &#32; &#32;skos:example&#32; &#34;A&#32;space&#32;area&#32;property&#32;to&#32;the&#32;property&#32;kind&#32; &#92; &#34;area&#92; &#34;.&#34;@en&#32;.  &#10;&lowbar;:n3934dcd8936b44968182d44e5f51696ab5&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32;owl:hasValue&#32;:QuantityKindNomenclature&#32;;  &#10; &#32; &#32; &#32; &#32;owl:onProperty&#32;skos:inScheme&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-141)|Pointer|<pre lang="Turtle"><code>:hasQuantityKind&#32;a&#32;owl:ObjectProperty&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;has&#32;quantity&#32;kind&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;Links&#32;a&#32;property&#32;to&#32;its&#32;quantity&#32;kind&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:domain&#32; &#91;&#32;a&#32;owl:Class&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:unionOf&#32;(&#32;:FeatureOfInterest&#32;:Property&#32;:CheckMethod&#32;)&#32;],  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#60;http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#Quality>,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;:Property&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32;:feature&lowbar;of&lowbar;interest&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:range&#32;&lowbar;:n40c9d2135a0446ef93103dd19bcc2944b5,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#91;&#32;rdfs:subClassOf&#32;&lowbar;:n40c9d2135a0446ef93103dd19bcc2944b5,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;qudt:QuantityKind,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#60;http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#Region>,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;skos:Concept,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;:QuantityKind&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:equivalentClass&#32;:QuantityKind&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:intersectionOf&#32;(&#32;skos:Concept&#32;&lowbar;:n40c9d2135a0446ef93103dd19bcc2944b5&#32;)&#32;],  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;qudt:QuantityKind,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#60;http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#Region>,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;skos:Concept,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;:QuantityKind&#32;;  &#10; &#32; &#32; &#32; &#32;skos:example&#32; &#34;A&#32;space&#32;area&#32;property&#32;to&#32;the&#32;property&#32;kind&#32; &#92; &#34;area&#92; &#34;.&#34;@en&#32;.  &#10;&lowbar;:n40c9d2135a0446ef93103dd19bcc2944b5&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32;owl:hasValue&#32;:QuantityKindNomenclature&#32;;  &#10; &#32; &#32; &#32; &#32;owl:onProperty&#32;skos:inScheme&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-141)|Pointer|<pre lang="Turtle"><code>http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#Region</code></pre>|
|[Section top](#minorfail-outcome-number-141)|Pointer|<pre lang="Turtle"><code>:hasQuantityKind&#32;a&#32;owl:ObjectProperty&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;has&#32;quantity&#32;kind&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;Links&#32;a&#32;property&#32;to&#32;its&#32;quantity&#32;kind&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:domain&#32; &#91;&#32;a&#32;owl:Class&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:unionOf&#32;(&#32;:FeatureOfInterest&#32;:Property&#32;:CheckMethod&#32;)&#32;],  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#60;http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#Quality>,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;:Property&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32;:feature&lowbar;of&lowbar;interest&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:range&#32;&lowbar;:n0d5aa4937d4c4bd4973bbc94d39b4776b5,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#91;&#32;rdfs:subClassOf&#32;&lowbar;:n0d5aa4937d4c4bd4973bbc94d39b4776b5,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;qudt:QuantityKind,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#60;http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#Region>,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;skos:Concept,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;:QuantityKind&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:equivalentClass&#32;:QuantityKind&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:intersectionOf&#32;(&#32;skos:Concept&#32;&lowbar;:n0d5aa4937d4c4bd4973bbc94d39b4776b5&#32;)&#32;],  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;qudt:QuantityKind,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#60;http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#Region>,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;skos:Concept,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;:QuantityKind&#32;;  &#10; &#32; &#32; &#32; &#32;skos:example&#32; &#34;A&#32;space&#32;area&#32;property&#32;to&#32;the&#32;property&#32;kind&#32; &#92; &#34;area&#92; &#34;.&#34;@en&#32;.  &#10;&lowbar;:n0d5aa4937d4c4bd4973bbc94d39b4776b5&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32;owl:hasValue&#32;:QuantityKindNomenclature&#32;;  &#10; &#32; &#32; &#32; &#32;owl:onProperty&#32;skos:inScheme&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-141)|Pointer|<pre lang="Turtle"><code>:QuantityKind&#32;a&#32;owl:Class&#32;;  &#10; &#32; &#32;&#32; &#32;rdfs:isDefinedBy&#32; &#60;http://qudt.org/2.1/schema/qudt> &#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-141)|Pointer|<pre lang="Turtle"><code>:forAdministrativeArea&#32;a&#32;owl:ObjectProperty&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;for&#32;administrative&#32;area&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34; &#34; &#34;The&#32;administrative&#32;area&#32;for&#32;which&#32;something&#32;applies.&#92;r  &#10; &#32; &#32;A&#32;se...&#34; &#34; &#34; &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32;:administrative&lowbar;areas&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:range&#32;&lowbar;:n6c42b2146c7c465a969e3628a2de4e52b1,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;&lowbar;:n6c42b2146c7c465a969e3628a2de4e52b2,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#91;&#32;rdfs:subClassOf&#32;&lowbar;:n6c42b2146c7c465a969e3628a2de4e52b1,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;&lowbar;:n6c42b2146c7c465a969e3628a2de4e52b2,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#60;http://data.europa.eu/eli/ontology#AdministrativeArea>,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;skos:Concept,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;:AdministrativeArea&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:equivalentClass&#32; &#60;http://data.europa.eu/eli/ontology#AdministrativeArea>,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;:AdministrativeArea&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:intersectionOf&#32;(&#32;skos:Concept&#32;&lowbar;:n6c42b2146c7c465a969e3628a2de4e52b2&#32;)&#32;],  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#60;http://data.europa.eu/eli/ontology#AdministrativeArea>,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;skos:Concept,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;:AdministrativeArea&#32;.  &#10;&lowbar;:n6c42b2146c7c465a969e3628a2de4e52b6&#32;rdf:first&#32;:AdministrativeArea&#32;;  &#10; &#32; &#32; &#32; &#32;rdf:rest&#32;()&#32;.  &#10;&lowbar;:n6c42b2146c7c465a969e3628a2de4e52b7&#32;rdf:first&#32; &#60;https://schema.org/Place> &#32;;  &#10; &#32; &#32; &#32; &#32;rdf:rest&#32;&lowbar;:n6c42b2146c7c465a969e3628a2de4e52b6&#32;.  &#10;&lowbar;:n6c42b2146c7c465a969e3628a2de4e52b1&#32;a&#32;owl:Class&#32;;  &#10; &#32; &#32; &#32; &#32;owl:unionOf&#32;&lowbar;:n6c42b2146c7c465a969e3628a2de4e52b7&#32;.  &#10;&lowbar;:n6c42b2146c7c465a969e3628a2de4e52b2&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32;owl:hasValue&#32;:AdministrativeAreaNomenclature&#32;;  &#10; &#32; &#32; &#32; &#32;owl:onProperty&#32;skos:inScheme&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-141)|Pointer|<pre lang="Turtle"><code>:forAdministrativeArea&#32;a&#32;owl:ObjectProperty&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;for&#32;administrative&#32;area&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34; &#34; &#34;The&#32;administrative&#32;area&#32;for&#32;which&#32;something&#32;applies.&#92;r  &#10; &#32; &#32;A&#32;se...&#34; &#34; &#34; &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32;:administrative&lowbar;areas&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:range&#32;&lowbar;:n8f81787d70ef460d98b5afabca6b4e1cb1,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;&lowbar;:n8f81787d70ef460d98b5afabca6b4e1cb2,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#91;&#32;rdfs:subClassOf&#32;&lowbar;:n8f81787d70ef460d98b5afabca6b4e1cb1,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;&lowbar;:n8f81787d70ef460d98b5afabca6b4e1cb2,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#60;http://data.europa.eu/eli/ontology#AdministrativeArea>,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;skos:Concept,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;:AdministrativeArea&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:equivalentClass&#32; &#60;http://data.europa.eu/eli/ontology#AdministrativeArea>,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;:AdministrativeArea&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:intersectionOf&#32;(&#32;skos:Concept&#32;&lowbar;:n8f81787d70ef460d98b5afabca6b4e1cb2&#32;)&#32;],  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#60;http://data.europa.eu/eli/ontology#AdministrativeArea>,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;skos:Concept,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;:AdministrativeArea&#32;.  &#10;&lowbar;:n8f81787d70ef460d98b5afabca6b4e1cb6&#32;rdf:first&#32;:AdministrativeArea&#32;;  &#10; &#32; &#32; &#32; &#32;rdf:rest&#32;()&#32;.  &#10;&lowbar;:n8f81787d70ef460d98b5afabca6b4e1cb7&#32;rdf:first&#32; &#60;https://schema.org/Place> &#32;;  &#10; &#32; &#32; &#32; &#32;rdf:rest&#32;&lowbar;:n8f81787d70ef460d98b5afabca6b4e1cb6&#32;.  &#10;&lowbar;:n8f81787d70ef460d98b5afabca6b4e1cb1&#32;a&#32;owl:Class&#32;;  &#10; &#32; &#32; &#32; &#32;owl:unionOf&#32;&lowbar;:n8f81787d70ef460d98b5afabca6b4e1cb7&#32;.  &#10;&lowbar;:n8f81787d70ef460d98b5afabca6b4e1cb2&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32;owl:hasValue&#32;:AdministrativeAreaNomenclature&#32;;  &#10; &#32; &#32; &#32; &#32;owl:onProperty&#32;skos:inScheme&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-141)|Pointer|<pre lang="Turtle"><code>:AdministrativeArea&#32;rdfs:subClassOf&#32;&lowbar;:n283ccbe6a97c47a2be0a984ec100d4c1b1,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;&lowbar;:n283ccbe6a97c47a2be0a984ec100d4c1b2,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;&lowbar;:n283ccbe6a97c47a2be0a984ec100d4c1b3,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;skos:Concept,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;aec3po:AdministrativeArea&#32;;  &#10; &#32; &#32; &#32; &#32;owl:equivalentClass&#32;&lowbar;:n283ccbe6a97c47a2be0a984ec100d4c1b3,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;aec3po:AdministrativeArea&#32;.  &#10;&lowbar;:n283ccbe6a97c47a2be0a984ec100d4c1b4&#32;rdf:first&#32;skos:Concept&#32;;  &#10; &#32; &#32; &#32; &#32;rdf:rest&#32;(&#32;&lowbar;:n283ccbe6a97c47a2be0a984ec100d4c1b2&#32;)&#32;.  &#10;&lowbar;:n283ccbe6a97c47a2be0a984ec100d4c1b6&#32;rdf:first&#32;aec3po:AdministrativeArea&#32;;  &#10; &#32; &#32; &#32; &#32;rdf:rest&#32;()&#32;.  &#10;&lowbar;:n283ccbe6a97c47a2be0a984ec100d4c1b7&#32;rdf:first&#32; &#60;https://schema.org/Place> &#32;;  &#10; &#32; &#32; &#32; &#32;rdf:rest&#32;&lowbar;:n283ccbe6a97c47a2be0a984ec100d4c1b6&#32;.  &#10;&lowbar;:n283ccbe6a97c47a2be0a984ec100d4c1b1&#32;a&#32;owl:Class&#32;;  &#10; &#32; &#32; &#32; &#32;owl:unionOf&#32;&lowbar;:n283ccbe6a97c47a2be0a984ec100d4c1b7&#32;.  &#10;&lowbar;:n283ccbe6a97c47a2be0a984ec100d4c1b3&#32;rdfs:subClassOf&#32;&lowbar;:n283ccbe6a97c47a2be0a984ec100d4c1b1,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;&lowbar;:n283ccbe6a97c47a2be0a984ec100d4c1b2,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;:AdministrativeArea,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;skos:Concept,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;aec3po:AdministrativeArea&#32;;  &#10; &#32; &#32; &#32; &#32;owl:equivalentClass&#32;:AdministrativeArea,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;aec3po:AdministrativeArea&#32;;  &#10; &#32; &#32; &#32; &#32;owl:intersectionOf&#32;&lowbar;:n283ccbe6a97c47a2be0a984ec100d4c1b4&#32;.  &#10;&lowbar;:n283ccbe6a97c47a2be0a984ec100d4c1b2&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32;owl:hasValue&#32;aec3po:AdministrativeAreaNomenclature&#32;;  &#10; &#32; &#32; &#32; &#32;owl:onProperty&#32;skos:inScheme&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-141)|Pointer|<pre lang="Turtle"><code>:forBuildingStructure&#32;a&#32;owl:ObjectProperty&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;for&#32;building&#32;structure&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;The&#32;building&#32;structure&#32;for&#32;which&#32;a&#32;specific&#32;check,&#32;verifier,...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32;:building&lowbar;structure&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:range&#32;&lowbar;:n170cdfbdc96d40cbb1917d1784765247b1,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#91;&#32;rdfs:subClassOf&#32;&lowbar;:n170cdfbdc96d40cbb1917d1784765247b1,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;skos:Concept,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;:BuildingStructure,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;:Design&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:equivalentClass&#32;:BuildingStructure&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:intersectionOf&#32;(&#32;skos:Concept&#32;&lowbar;:n170cdfbdc96d40cbb1917d1784765247b1&#32;)&#32;],  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;skos:Concept,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;:BuildingStructure,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;:Design&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:subPropertyOf&#32;:forDesign&#32;.  &#10;&lowbar;:n170cdfbdc96d40cbb1917d1784765247b1&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32;owl:hasValue&#32;:BuildingStructureNomenclature&#32;;  &#10; &#32; &#32; &#32; &#32;owl:onProperty&#32;skos:inScheme&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-141)|Pointer|<pre lang="Turtle"><code>:hasBuildingStructure&#32;a&#32;owl:FunctionalProperty,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:ObjectProperty&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;has&#32;building&#32;structure&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;The&#32;building&#32;structure&#32;design&#32;of&#32;a&#32;feature&#32;of&#32;interest&#32;or&#32;a&#32;...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32;:building&lowbar;structure&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:range&#32;&lowbar;:n51183e38e1524e499ec259d5a14aaea8b1,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#91;&#32;rdfs:subClassOf&#32;&lowbar;:n51183e38e1524e499ec259d5a14aaea8b1,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;skos:Concept,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;:BuildingStructure,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;:Design&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:equivalentClass&#32;:BuildingStructure&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:intersectionOf&#32;(&#32;skos:Concept&#32;&lowbar;:n51183e38e1524e499ec259d5a14aaea8b1&#32;)&#32;],  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;skos:Concept,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;:BuildingStructure,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;:Design&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:subPropertyOf&#32;:hasDesign&#32;.  &#10;&lowbar;:n51183e38e1524e499ec259d5a14aaea8b1&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32;owl:hasValue&#32;:BuildingStructureNomenclature&#32;;  &#10; &#32; &#32; &#32; &#32;owl:onProperty&#32;skos:inScheme&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-141)|Pointer|<pre lang="Turtle"><code>:forBuildingUsage&#32;a&#32;owl:ObjectProperty&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;for&#32;building&#32;usage&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;The&#32;building&#32;usage&#32;for&#32;which&#32;a&#32;specific&#32;check,&#32;verifier,&#32;or&#32;...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32;:building&lowbar;usage&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:range&#32;&lowbar;:n36febd8c43c54cbf9141f7a1ff5e70b5b1,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#91;&#32;rdfs:subClassOf&#32;&lowbar;:n36febd8c43c54cbf9141f7a1ff5e70b5b1,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;skos:Concept,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;:BuildingUsage,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;:Design&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:equivalentClass&#32;:BuildingUsage&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:intersectionOf&#32;(&#32;skos:Concept&#32;&lowbar;:n36febd8c43c54cbf9141f7a1ff5e70b5b1&#32;)&#32;],  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;skos:Concept,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;:BuildingUsage,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;:Design&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:subPropertyOf&#32;:forDesign&#32;.  &#10;&lowbar;:n36febd8c43c54cbf9141f7a1ff5e70b5b1&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32;owl:hasValue&#32;:BuildingUsageNomenclature&#32;;  &#10; &#32; &#32; &#32; &#32;owl:onProperty&#32;skos:inScheme&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-141)|Pointer|<pre lang="Turtle"><code>:hasBuildingUsage&#32;a&#32;owl:FunctionalProperty,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:ObjectProperty&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;has&#32;building&#32;usage&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;The&#32;building&#32;usage&#32;design&#32;of&#32;a&#32;feature&#32;of&#32;interest&#32;or&#32;a&#32;prop...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32;:building&lowbar;usage&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:range&#32;&lowbar;:n0fc0cfeb7c744eb4b8e0e63bebde5ebbb1,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#91;&#32;rdfs:subClassOf&#32;&lowbar;:n0fc0cfeb7c744eb4b8e0e63bebde5ebbb1,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;skos:Concept,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;:BuildingUsage,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;:Design&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:equivalentClass&#32;:BuildingUsage&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:intersectionOf&#32;(&#32;skos:Concept&#32;&lowbar;:n0fc0cfeb7c744eb4b8e0e63bebde5ebbb1&#32;)&#32;],  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;skos:Concept,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;:BuildingUsage,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;:Design&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:subPropertyOf&#32;:hasDesign&#32;.  &#10;&lowbar;:n0fc0cfeb7c744eb4b8e0e63bebde5ebbb1&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32;owl:hasValue&#32;:BuildingUsageNomenclature&#32;;  &#10; &#32; &#32; &#32; &#32;owl:onProperty&#32;skos:inScheme&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-141)|Pointer|<pre lang="Turtle"><code>:hasDiscipline&#32;a&#32;owl:ObjectProperty&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;has&#32;discipline&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;Links&#32;an&#32;entity&#32;(procedure,&#32;statement,&#32;verifier,&#32;...)&#32;to&#32;the...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32;:discipline&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:range&#32;&lowbar;:n6807978c5e914a29a946ffb908359af4b1,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#91;&#32;rdfs:subClassOf&#32;&lowbar;:n6807978c5e914a29a946ffb908359af4b1,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;skos:Concept,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;:Discipline&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:equivalentClass&#32;:Discipline&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:intersectionOf&#32;(&#32;skos:Concept&#32;&lowbar;:n6807978c5e914a29a946ffb908359af4b1&#32;)&#32;],  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;skos:Concept,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;:Discipline&#32;.  &#10;&lowbar;:n6807978c5e914a29a946ffb908359af4b1&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32;owl:hasValue&#32;:DisciplineNomenclature&#32;;  &#10; &#32; &#32; &#32; &#32;owl:onProperty&#32;skos:inScheme&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-141)|Pointer|<pre lang="Turtle"><code>:hasPermittingStage&#32;a&#32;owl:ObjectProperty&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;has&#32;permitting&#32;stage&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;Links&#32;an&#32;entity&#32;to&#32;the&#32;permitting&#32;stage&#32;this&#32;entity&#32;pertains&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32;:permitting&lowbar;stage&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:range&#32;&lowbar;:na96e5765ff6f418db973bd36bde7a376b1,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#91;&#32;rdfs:subClassOf&#32;&lowbar;:na96e5765ff6f418db973bd36bde7a376b1,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;skos:Concept,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;:PermittingStage&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:equivalentClass&#32;:PermittingStage&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:intersectionOf&#32;(&#32;skos:Concept&#32;&lowbar;:na96e5765ff6f418db973bd36bde7a376b1&#32;)&#32;],  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;skos:Concept,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;:PermittingStage&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:subPropertyOf&#32; &#60;https://w3id.org/digitalconstruction/0.5/Lifecycle#hasStage> &#32;;  &#10; &#32; &#32; &#32; &#32;owl:equivalentProperty&#32; &#60;https://w3id.org/digitalconstruction/0.5/Lifecycle#hasStage> &#32;.  &#10;&lowbar;:na96e5765ff6f418db973bd36bde7a376b1&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32;owl:hasValue&#32;:PermittingStageNomenclature&#32;;  &#10; &#32; &#32; &#32; &#32;owl:onProperty&#32;skos:inScheme&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-141)|Pointer|http://www.w3.org/2004/02/skos/core#Concept|
|[Section top](#minorfail-outcome-number-141)|Pointer|http://purl.org/dc/elements/1.1/format|

***
### MinorFail Outcome number 142

[Jump to summary definition](#summary-MinorFail-142)	|	[Previous MinorFail outcome](#minorfail-outcome-number-141)	|	[Next MinorFail outcome](#minorfail-outcome-number-143)

:exclamation:MinorFail outcome
#### Subject detail
|Name|all-fragments|
|----|----|
|Title|All&#32;the&#32;fragments&#32;from&#32;branch&#32;HEAD&#32;that&#32;are&#32;syntaxically&#32;correct&#32;as&#32;well&#32;as&#32;their&#32;recursive&#32;imports|
|Composition|- [Module aec3po](https://github.com/Accord-Project/aec3po/blob/HEAD/src/aec3po.ttl)<br/>- [Module check&lowbar;method](https://github.com/Accord-Project/aec3po/blob/HEAD/src/check_method.ttl)<br/>- [Module checking&lowbar;act](https://github.com/Accord-Project/aec3po/blob/HEAD/src/checking_act.ttl)<br/>- [Module compliance&lowbar;verification&lowbar;report](https://github.com/Accord-Project/aec3po/blob/HEAD/src/compliance_verification_report.ttl)<br/>- [Module data&lowbar;requirement](https://github.com/Accord-Project/aec3po/blob/HEAD/src/data_requirement.ttl)<br/>- [Module document](https://github.com/Accord-Project/aec3po/blob/HEAD/src/document.ttl)<br/>- [Module evidence](https://github.com/Accord-Project/aec3po/blob/HEAD/src/evidence.ttl)<br/>- [Module feature&lowbar;of&lowbar;interest](https://github.com/Accord-Project/aec3po/blob/HEAD/src/feature_of_interest.ttl)<br/>- [Module legal&lowbar;verifier](https://github.com/Accord-Project/aec3po/blob/HEAD/src/legal_verifier.ttl)<br/>- [Module model](https://github.com/Accord-Project/aec3po/blob/HEAD/src/model.ttl)<br/>- [Module rase&lowbar;statement](https://github.com/Accord-Project/aec3po/blob/HEAD/src/rase_statement.ttl)<br/>- [Module statement](https://github.com/Accord-Project/aec3po/blob/HEAD/src/statement.ttl)<br/>- [Module table](https://github.com/Accord-Project/aec3po/blob/HEAD/src/table.ttl)<br/>- [Module vocabularies/&lowbar;shape](https://github.com/Accord-Project/aec3po/blob/HEAD/src/vocabularies/_shape.ttl)<br/>- [Module vocabularies/administrative&lowbar;areas](https://github.com/Accord-Project/aec3po/blob/HEAD/src/vocabularies/administrative_areas.ttl)<br/>- [Module vocabularies/building&lowbar;structure](https://github.com/Accord-Project/aec3po/blob/HEAD/src/vocabularies/building_structure.ttl)<br/>- [Module vocabularies/building&lowbar;usage](https://github.com/Accord-Project/aec3po/blob/HEAD/src/vocabularies/building_usage.ttl)<br/>- [Module vocabularies/check&lowbar;method&lowbar;comparators](https://github.com/Accord-Project/aec3po/blob/HEAD/src/vocabularies/check_method_comparators.ttl)<br/>- [Module vocabularies/check&lowbar;method&lowbar;operators](https://github.com/Accord-Project/aec3po/blob/HEAD/src/vocabularies/check_method_operators.ttl)<br/>- [Module vocabularies/disciplines](https://github.com/Accord-Project/aec3po/blob/HEAD/src/vocabularies/disciplines.ttl)<br/>- [Module vocabularies/permitting&lowbar;stages](https://github.com/Accord-Project/aec3po/blob/HEAD/src/vocabularies/permitting_stages.ttl)<br/>- [Module vocabularies/quantity&lowbar;kinds](https://github.com/Accord-Project/aec3po/blob/HEAD/src/vocabularies/quantity_kinds.ttl)|

#### Criterion detail
|Identifier|[labeled-terms](https://ns.inria.fr/olivaw#labeled-terms)|
|----|----|
|Title|Term&#32;labeling&#32;test|
|Description|A&#32;test&#32;case&#32;from&#32;the&#32;Best&#32;Practices&#32;tests&#32;checking&#32;if&#32;all&#32;the&#32;terms&#32;of&#32;the&#32;subject&#32;have&#32;a&#32;rdfs:label&#32;property&#32;pointing&#32;to&#32;a&#32;literal&#32;in&#32;English|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-142)|Identifier|`not-labeled-term`|
|[Section top](#minorfail-outcome-number-142)|Title|Terms&#32;not&#32;labeled|
|[Section top](#minorfail-outcome-number-142)|Description|The&#32;following&#32;terms&#32;have&#32;no&#32;rdfs:label&#32;to&#32;define&#32;it&#32;in&#32;natural&#32;language|
|[Section top](#minorfail-outcome-number-142)|Pointer|<pre lang="Turtle"><code>:hasFormat&#32;a&#32;owl:ObjectProperty&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;Defines&#32;the&#32;format&#32;of&#32;an&#32;evidence,&#32;which&#32;is&#32;of&#32;type&#32;dct:form...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:domain&#32;:Statement&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32;:evidence&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:range&#32;dc:format&#32;;  &#10; &#32; &#32; &#32; &#32;skos:example&#32; &#34;an&#32;image,&#32;a&#32;drawing&#32;or&#32;a&#32;model&#32;can&#32;be&#32;an&#32;evidence.&#34;@en&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-142)|Pointer|<pre lang="Turtle"><code>:England&#32;a&#32;owl:NamedIndividual,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;skos:Concept,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;:AdministrativeArea&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32;:administrative&lowbar;areas&#32;;  &#10; &#32; &#32; &#32; &#32;skos:definition&#32; &#34;England&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;skos:inScheme&#32;:AdministrativeAreaNomenclature&#32;;  &#10; &#32; &#32; &#32; &#32;skos:prefLabel&#32; &#34;England&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;skos:topConceptOf&#32;:AdministrativeAreaNomenclature&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-142)|Pointer|<pre lang="Turtle"><code>:Estonia&#32;a&#32;owl:NamedIndividual,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;skos:Concept,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;:AdministrativeArea&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32;:administrative&lowbar;areas&#32;;  &#10; &#32; &#32; &#32; &#32;skos:definition&#32; &#34;Estonia&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;skos:inScheme&#32;:AdministrativeAreaNomenclature&#32;;  &#10; &#32; &#32; &#32; &#32;skos:prefLabel&#32; &#34;Estonia&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;skos:topConceptOf&#32;:AdministrativeAreaNomenclature&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-142)|Pointer|<pre lang="Turtle"><code>:Finland&#32;a&#32;owl:NamedIndividual,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;skos:Concept,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;:AdministrativeArea&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32;:administrative&lowbar;areas&#32;;  &#10; &#32; &#32; &#32; &#32;skos:definition&#32; &#34;Finland&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;skos:inScheme&#32;:AdministrativeAreaNomenclature&#32;;  &#10; &#32; &#32; &#32; &#32;skos:prefLabel&#32; &#34;Finland&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;skos:topConceptOf&#32;:AdministrativeAreaNomenclature&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-142)|Pointer|<pre lang="Turtle"><code>:France&#32;a&#32;owl:NamedIndividual,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;skos:Concept,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;:AdministrativeArea&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32;:administrative&lowbar;areas&#32;;  &#10; &#32; &#32; &#32; &#32;skos:definition&#32; &#34;France&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;skos:inScheme&#32;:AdministrativeAreaNomenclature&#32;;  &#10; &#32; &#32; &#32; &#32;skos:prefLabel&#32; &#34;France&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;skos:topConceptOf&#32;:AdministrativeAreaNomenclature&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-142)|Pointer|<pre lang="Turtle"><code>:Germany&#32;a&#32;owl:NamedIndividual,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;skos:Concept,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;:AdministrativeArea&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32;:administrative&lowbar;areas&#32;;  &#10; &#32; &#32; &#32; &#32;skos:definition&#32; &#34;Germany&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;skos:inScheme&#32;:AdministrativeAreaNomenclature&#32;;  &#10; &#32; &#32; &#32; &#32;skos:prefLabel&#32; &#34;Germany&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;skos:topConceptOf&#32;:AdministrativeAreaNomenclature&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-142)|Pointer|<pre lang="Turtle"><code>:Italy&#32;a&#32;owl:NamedIndividual,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;skos:Concept,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;:AdministrativeArea&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32;:administrative&lowbar;areas&#32;;  &#10; &#32; &#32; &#32; &#32;skos:definition&#32; &#34;Italy&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;skos:inScheme&#32;:AdministrativeAreaNomenclature&#32;;  &#10; &#32; &#32; &#32; &#32;skos:prefLabel&#32; &#34;Italy&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;skos:topConceptOf&#32;:AdministrativeAreaNomenclature&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-142)|Pointer|<pre lang="Turtle"><code>:Spain&#32;a&#32;owl:NamedIndividual,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;skos:Concept,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;:AdministrativeArea&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32;:administrative&lowbar;areas&#32;;  &#10; &#32; &#32; &#32; &#32;skos:definition&#32; &#34;Spain&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;skos:inScheme&#32;:AdministrativeAreaNomenclature&#32;;  &#10; &#32; &#32; &#32; &#32;skos:prefLabel&#32; &#34;Spain&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;skos:topConceptOf&#32;:AdministrativeAreaNomenclature&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-142)|Pointer|<pre lang="Turtle"><code>:BuildingStructure-steel&#32;a&#32;owl:NamedIndividual,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;skos:Concept,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;:BuildingStructure&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32;:building&lowbar;structure&#32;;  &#10; &#32; &#32; &#32; &#32;skos:definition&#32; &#34;Building&#32;has&#32;steel&#32;structure.&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;skos:inScheme&#32;:BuildingStructureNomenclature&#32;;  &#10; &#32; &#32; &#32; &#32;skos:prefLabel&#32; &#34;steel&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;skos:topConceptOf&#32;:BuildingStructureNomenclature&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-142)|Pointer|<pre lang="Turtle"><code>:BuildingStructure-timber&#32;a&#32;owl:NamedIndividual,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;skos:Concept,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;:BuildingStructure&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32;:building&lowbar;structure&#32;;  &#10; &#32; &#32; &#32; &#32;skos:definition&#32; &#34;Building&#32;has&#32;timber&#32;structure.&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;skos:inScheme&#32;:BuildingStructureNomenclature&#32;;  &#10; &#32; &#32; &#32; &#32;skos:prefLabel&#32; &#34;timber&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;skos:topConceptOf&#32;:BuildingStructureNomenclature&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-142)|Pointer|<pre lang="Turtle"><code>:BuildingUsage-commercial&#32;a&#32;owl:NamedIndividual,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;skos:Concept,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;:BuildingUsage&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32;:building&lowbar;usage&#32;;  &#10; &#32; &#32; &#32; &#32;skos:definition&#32; &#34;Building&#32;has&#32;commercial&#32;usage.&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;skos:inScheme&#32;:BuildingUsageNomenclature&#32;;  &#10; &#32; &#32; &#32; &#32;skos:prefLabel&#32; &#34;commercial&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;skos:topConceptOf&#32;:BuildingUsageNomenclature&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-142)|Pointer|<pre lang="Turtle"><code>:BuildingUsage-residential&#32;a&#32;owl:NamedIndividual,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;skos:Concept,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;:BuildingUsage&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32;:building&lowbar;usage&#32;;  &#10; &#32; &#32; &#32; &#32;skos:definition&#32; &#34;Building&#32;has&#32;residential&#32;usage.&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;skos:inScheme&#32;:BuildingUsageNomenclature&#32;;  &#10; &#32; &#32; &#32; &#32;skos:prefLabel&#32; &#34;residential&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;skos:topConceptOf&#32;:BuildingUsageNomenclature&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-142)|Pointer|<pre lang="Turtle"><code>:BuildingUsage-cultural&#32;a&#32;owl:NamedIndividual,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;skos:Concept,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;:BuildingUsage&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32;:building&lowbar;usage&#32;;  &#10; &#32; &#32; &#32; &#32;skos:definition&#32; &#34;Building&#32;has&#32;cultural&#32;usage.&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;skos:inScheme&#32;:BuildingUsageNomenclature&#32;;  &#10; &#32; &#32; &#32; &#32;skos:prefLabel&#32; &#34;cultural&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;skos:topConceptOf&#32;:BuildingUsageNomenclature&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-142)|Pointer|<pre lang="Turtle"><code>:CheckMethodcomparator-logicalAND&#32;a&#32;owl:NamedIndividual,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;skos:Concept,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;:CheckMethodComparator&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32;:check&lowbar;method&lowbar;comparators&#32;;  &#10; &#32; &#32; &#32; &#32;skos:definition&#32; &#34;logical&#32;AND&#32;comparator.&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;skos:inScheme&#32;:CheckMethodComparatorNomenclature&#32;;  &#10; &#32; &#32; &#32; &#32;skos:prefLabel&#32; &#34;logicalAND&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;skos:topConceptOf&#32;:CheckMethodComparatorNomenclature&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-142)|Pointer|<pre lang="Turtle"><code>:CheckMethodcomparator-eq&#32;a&#32;owl:NamedIndividual,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;skos:Concept,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;:CheckMethodcomparator&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32;:check&lowbar;method&lowbar;comparators&#32;;  &#10; &#32; &#32; &#32; &#32;skos:definition&#32; &#34;equal-to&#32;comparator.&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;skos:inScheme&#32;:CheckMethodComparatorNomenclature&#32;;  &#10; &#32; &#32; &#32; &#32;skos:prefLabel&#32; &#34;equal-to&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;skos:topConceptOf&#32;:CheckMethodComparatorNomenclature&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-142)|Pointer|<pre lang="Turtle"><code>:CheckMethodComparator-neq&#32;a&#32;owl:NamedIndividual,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;skos:Concept,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;:CheckMethodComparator&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32;:check&lowbar;method&lowbar;comparators&#32;;  &#10; &#32; &#32; &#32; &#32;skos:definition&#32; &#34;not&#32;equal-to&#32;comparator.&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;skos:inScheme&#32;:CheckMethodComparatorNomenclature&#32;;  &#10; &#32; &#32; &#32; &#32;skos:prefLabel&#32; &#34;not&#32;equal-to&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;skos:topConceptOf&#32;:CheckMethodComparatorNomenclature&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-142)|Pointer|<pre lang="Turtle"><code>:CheckMethodComparator-lt&#32;a&#32;owl:NamedIndividual,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;skos:Concept,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;:CheckMethodComparator&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32;:check&lowbar;method&lowbar;comparators&#32;;  &#10; &#32; &#32; &#32; &#32;skos:definition&#32; &#34;less-than&#32;comparator.&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;skos:inScheme&#32;:CheckMethodComparatorNomenclature&#32;;  &#10; &#32; &#32; &#32; &#32;skos:prefLabel&#32; &#34;less&#32;than&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;skos:topConceptOf&#32;:CheckMethodComparatorNomenclature&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-142)|Pointer|<pre lang="Turtle"><code>:CheckMethodComparator-le&#32;a&#32;owl:NamedIndividual,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;skos:Concept,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;:CheckMethodComparator&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32;:check&lowbar;method&lowbar;comparators&#32;;  &#10; &#32; &#32; &#32; &#32;skos:definition&#32; &#34;less-equal&#32;comparator.&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;skos:inScheme&#32;:CheckMethodComparatorNomenclature&#32;;  &#10; &#32; &#32; &#32; &#32;skos:prefLabel&#32; &#34;less&#32;equal&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;skos:topConceptOf&#32;:CheckMethodComparatorNomenclature&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-142)|Pointer|<pre lang="Turtle"><code>:CheckMethodComparator-gt&#32;a&#32;owl:NamedIndividual,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;skos:Concept,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;:CheckMethodComparator&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32;:check&lowbar;method&lowbar;comparators&#32;;  &#10; &#32; &#32; &#32; &#32;skos:definition&#32; &#34;greater-than&#32;comparator.&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;skos:inScheme&#32;:CheckMethodComparatorNomenclature&#32;;  &#10; &#32; &#32; &#32; &#32;skos:prefLabel&#32; &#34;greater&#32;than&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;skos:topConceptOf&#32;:CheckMethodComparatorNomenclature&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-142)|Pointer|<pre lang="Turtle"><code>:CheckMethodComparator-ge&#32;a&#32;owl:NamedIndividual,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;skos:Concept,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;:CheckMethodComparator&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32;:check&lowbar;method&lowbar;comparators&#32;;  &#10; &#32; &#32; &#32; &#32;skos:definition&#32; &#34;greater-equal&#32;comparator.&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;skos:inScheme&#32;:CheckMethodComparatorNomenclature&#32;;  &#10; &#32; &#32; &#32; &#32;skos:prefLabel&#32; &#34;greater&#32;equal&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;skos:topConceptOf&#32;:CheckMethodComparatorNomenclature&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-142)|Pointer|<pre lang="Turtle"><code>:CheckMethodComparator-logicalOR&#32;a&#32;owl:NamedIndividual,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;skos:Concept,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;:CheckMethodComparator&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32;:check&lowbar;method&lowbar;comparators&#32;;  &#10; &#32; &#32; &#32; &#32;skos:definition&#32; &#34;logical&#32;OR&#32;comparator.&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;skos:inScheme&#32;:CheckMethodComparatorNomenclature&#32;;  &#10; &#32; &#32; &#32; &#32;skos:prefLabel&#32; &#34;logicalOR&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;skos:topConceptOf&#32;:CheckMethodComparatorNomenclature&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-142)|Pointer|<pre lang="Turtle"><code>:CheckMethodOperator-exists&#32;a&#32;owl:NamedIndividual,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;skos:Concept,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;:CheckMethodOperator&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32;:check&lowbar;method&lowbar;operators&#32;;  &#10; &#32; &#32; &#32; &#32;skos:definition&#32; &#34;exists&#32;operator.&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;skos:inScheme&#32;:CheckMethodOperatorNomenclature&#32;;  &#10; &#32; &#32; &#32; &#32;skos:prefLabel&#32; &#34;exists&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;skos:topConceptOf&#32;:CheckMethodOperatorNomenclature&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-142)|Pointer|<pre lang="Turtle"><code>:CheckMethodOperator-notExists&#32;a&#32;owl:NamedIndividual,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;skos:Concept,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;:CheckMethodOperator&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32;:check&lowbar;method&lowbar;operators&#32;;  &#10; &#32; &#32; &#32; &#32;skos:definition&#32; &#34;not&#32;exists&#32;operator.&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;skos:inScheme&#32;:CheckMethodOperatorNomenclature&#32;;  &#10; &#32; &#32; &#32; &#32;skos:prefLabel&#32; &#34;not&#32;exists&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;skos:topConceptOf&#32;:CheckMethodOperatorNomenclature&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-142)|Pointer|<pre lang="Turtle"><code>:CheckMethodOperator-forall&#32;a&#32;owl:NamedIndividual,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;skos:Concept,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;:CheckMethodOperator&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32;:check&lowbar;method&lowbar;operators&#32;;  &#10; &#32; &#32; &#32; &#32;skos:definition&#32; &#34;forall&#32;operator.&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;skos:inScheme&#32;:CheckMethodOperatorNomenclature&#32;;  &#10; &#32; &#32; &#32; &#32;skos:prefLabel&#32; &#34;forall&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;skos:topConceptOf&#32;:CheckMethodOperatorNomenclature&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-142)|Pointer|<pre lang="Turtle"><code>:CheckMethodOperator-addition&#32;a&#32;owl:NamedIndividual,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;skos:Concept,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;:CheckMethodOperator&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32;:check&lowbar;method&lowbar;operators&#32;;  &#10; &#32; &#32; &#32; &#32;skos:definition&#32; &#34;addition&#32;operator.&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;skos:inScheme&#32;:CheckMethodOperatorNomenclature&#32;;  &#10; &#32; &#32; &#32; &#32;skos:prefLabel&#32; &#34;addition&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;skos:topConceptOf&#32;:CheckMethodOperatorNomenclature&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-142)|Pointer|<pre lang="Turtle"><code>:CheckMethodOperator-multiplication&#32;a&#32;owl:NamedIndividual,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;skos:Concept,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;:CheckMethodOperator&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32;:check&lowbar;method&lowbar;operators&#32;;  &#10; &#32; &#32; &#32; &#32;skos:definition&#32; &#34;multiplication&#32;Operator.&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;skos:inScheme&#32;:CheckMethodOperatorNomenclature&#32;;  &#10; &#32; &#32; &#32; &#32;skos:prefLabel&#32; &#34;multiplication&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;skos:topConceptOf&#32;:CheckMethodOperatorNomenclature&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-142)|Pointer|<pre lang="Turtle"><code>:CheckMethodOperator-subtraction&#32;a&#32;owl:NamedIndividual,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;skos:Concept,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;:CheckMethodOperator&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32;:check&lowbar;method&lowbar;operators&#32;;  &#10; &#32; &#32; &#32; &#32;skos:definition&#32; &#34;subtraction&#32;operator.&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;skos:inScheme&#32;:CheckMethodOperatorNomenclature&#32;;  &#10; &#32; &#32; &#32; &#32;skos:prefLabel&#32; &#34;subtraction&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;skos:topConceptOf&#32;:CheckMethodOperatorNomenclature&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-142)|Pointer|<pre lang="Turtle"><code>:CheckMethodOperator-division&#32;a&#32;owl:NamedIndividual,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;skos:Concept,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;:CheckMethodOperator&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32;:check&lowbar;method&lowbar;operators&#32;;  &#10; &#32; &#32; &#32; &#32;skos:definition&#32; &#34;division&#32;Operator.&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;skos:inScheme&#32;:CheckMethodOperatorNomenclature&#32;;  &#10; &#32; &#32; &#32; &#32;skos:prefLabel&#32; &#34;division&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;skos:topConceptOf&#32;:CheckMethodOperatorNomenclature&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-142)|Pointer|<pre lang="Turtle"><code>:Discipline-architecture&#32;a&#32;owl:NamedIndividual,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;skos:Concept,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;:Discipline&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32;:discipline&#32;;  &#10; &#32; &#32; &#32; &#32;skos:definition&#32; &#34;The&#32;Architecture&#32;discipline.&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;skos:inScheme&#32;:DisciplineNomenclature&#32;;  &#10; &#32; &#32; &#32; &#32;skos:prefLabel&#32; &#34;architecture&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;skos:topConceptOf&#32;:DisciplineNomenclature&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-142)|Pointer|<pre lang="Turtle"><code>:Discipline-buildingServices&#32;a&#32;owl:NamedIndividual,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;skos:Concept,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;:Discipline&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32;:discipline&#32;;  &#10; &#32; &#32; &#32; &#32;skos:definition&#32; &#34;The&#32;Building&#32;Services&#32;discipline.&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;skos:inScheme&#32;:DisciplineNomenclature&#32;;  &#10; &#32; &#32; &#32; &#32;skos:prefLabel&#32; &#34;building&#32;services&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;skos:topConceptOf&#32;:DisciplineNomenclature&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-142)|Pointer|<pre lang="Turtle"><code>:Discipline-construction&#32;a&#32;owl:NamedIndividual,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;skos:Concept,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;:Discipline&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32;:discipline&#32;;  &#10; &#32; &#32; &#32; &#32;skos:definition&#32; &#34;The&#32;Construction&#32;discipline.&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;skos:inScheme&#32;:DisciplineNomenclature&#32;;  &#10; &#32; &#32; &#32; &#32;skos:prefLabel&#32; &#34;construction&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;skos:topConceptOf&#32;:DisciplineNomenclature&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-142)|Pointer|<pre lang="Turtle"><code>:Discipline-planning&#32;a&#32;owl:NamedIndividual,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;skos:Concept,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;:Discipline&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32;:discipline&#32;;  &#10; &#32; &#32; &#32; &#32;skos:definition&#32; &#34;The&#32;Planning&#32;discipline.&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;skos:inScheme&#32;:DisciplineNomenclature&#32;;  &#10; &#32; &#32; &#32; &#32;skos:prefLabel&#32; &#34;planning&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;skos:topConceptOf&#32;:DisciplineNomenclature&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-142)|Pointer|<pre lang="Turtle"><code>:Discipline-structuralEngineering&#32;a&#32;owl:NamedIndividual,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;skos:Concept,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;:Discipline&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32;:discipline&#32;;  &#10; &#32; &#32; &#32; &#32;skos:definition&#32; &#34;The&#32;Structural&#32;Engineering&#32;discipline.&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;skos:inScheme&#32;:DisciplineNomenclature&#32;;  &#10; &#32; &#32; &#32; &#32;skos:prefLabel&#32; &#34;structural&#32;engineering&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;skos:topConceptOf&#32;:DisciplineNomenclature&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-142)|Pointer|<pre lang="Turtle"><code>:UK&lowbar;Building&lowbar;Control&lowbar;Submission&#32;a&#32;owl:NamedIndividual,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;skos:Concept,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;:PermittingStage&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32;:permitting&lowbar;stage&#32;;  &#10; &#32; &#32; &#32; &#32;skos:definition&#32; &#34;The&#32;UK&#32;Building&#32;Control&#32;Submission&#32;permitting&#32;stage.&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;skos:inScheme&#32;:PermittingStageNomenclature&#32;;  &#10; &#32; &#32; &#32; &#32;skos:prefLabel&#32; &#34;building&#32;control&#32;submission&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;skos:topConceptOf&#32;:PermittingStageNomenclature&#32;;  &#10; &#32; &#32; &#32; &#32;:forAdministrativeArea&#32;:England&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-142)|Pointer|<pre lang="Turtle"><code>:UK&lowbar;Planning&lowbar;Permission&#32;a&#32;owl:NamedIndividual,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;skos:Concept,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;:PermittingStage&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32;:permitting&lowbar;stage&#32;;  &#10; &#32; &#32; &#32; &#32;skos:definition&#32; &#34;The&#32;UK&#32;Planning&#32;Permission&#32;permitting&#32;stage.&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;skos:inScheme&#32;:PermittingStageNomenclature&#32;;  &#10; &#32; &#32; &#32; &#32;skos:prefLabel&#32; &#34;planning&#32;permission&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;skos:topConceptOf&#32;:PermittingStageNomenclature&#32;;  &#10; &#32; &#32; &#32; &#32;:forAdministrativeArea&#32;:England&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-142)|Pointer|<pre lang="Turtle"><code>:QuantityKind&#32;a&#32;owl:Class&#32;;  &#10; &#32; &#32;&#32; &#32;rdfs:isDefinedBy&#32; &#60;http://qudt.org/2.1/schema/qudt> &#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-142)|Pointer|<pre lang="Turtle"><code>:ModularRoomHeight&#32;a&#32;owl:NamedIndividual,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;skos:Concept,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;:QuantityKind&#32;;  &#10; &#32; &#32; &#32; &#32;qudt:applicableUnit&#32; &#60;http://qudt.org/vocab/unit/CentiM>,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#60;http://qudt.org/vocab/unit/IN>,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#60;http://qudt.org/vocab/unit/M>,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#60;http://qudt.org/vocab/unit/MilliIN>,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#60;http://qudt.org/vocab/unit/MilliM> &#32;;  &#10; &#32; &#32; &#32; &#32;qudt:hasDimensionVector&#32; &#60;http://qudt.org/vocab/dimensionvector/A0E0L1I0M0H0T0D0> &#32;;  &#10; &#32; &#32; &#32; &#32;qudt:normativeReference&#32; &#34;https://www.iso.org/obp/ui/#iso:std:iso:6707:-1:ed-6:v1:en:t...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32;:quantity&lowbar;kinds&#32;;  &#10; &#32; &#32; &#32; &#32;skos:broader&#32; &#60;http://qudt.org/vocab/quantitykind/Length> &#32;;  &#10; &#32; &#32; &#32; &#32;skos:definition&#32; &#34;vertical&#32;distance&#32;within&#32;one&#32;storey&#32;between&#32;the&#32;modular&#32;plan...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;skos:prefLabel&#32; &#34;modular&#32;room&#32;height&#34;@en&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-142)|Pointer|<pre lang="Turtle"><code>:WidthOfAngledCorridor&#32;a&#32;owl:NamedIndividual,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;skos:Concept,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;:QuantityKind&#32;;  &#10; &#32; &#32; &#32; &#32;qudt:applicableUnit&#32; &#60;http://qudt.org/vocab/unit/CentiM>,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#60;http://qudt.org/vocab/unit/IN>,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#60;http://qudt.org/vocab/unit/M>,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#60;http://qudt.org/vocab/unit/MilliIN>,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#60;http://qudt.org/vocab/unit/MilliM> &#32;;  &#10; &#32; &#32; &#32; &#32;qudt:hasDimensionVector&#32; &#60;http://qudt.org/vocab/dimensionvector/A0E0L1I0M0H0T0D0> &#32;;  &#10; &#32; &#32; &#32; &#32;qudt:normativeReference&#32; &#34;https://www.iso.org/obp/ui/#iso:std:iso:7176:-5:ed-2:v1:en:t...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32;:quantity&lowbar;kinds&#32;;  &#10; &#32; &#32; &#32; &#32;skos:broader&#32; &#60;http://qudt.org/vocab/quantitykind/Length> &#32;;  &#10; &#32; &#32; &#32; &#32;skos:definition&#32; &#34;width&#32;of&#32;a&#32;corridor&#32;with&#32;a&#32;right&#32;angled&#32;turn&#32;in&#32;which&#32;the&#32;wh...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;skos:prefLabel&#32; &#34;width&#32;of&#32;angled&#32;corridor&#34;@en&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-142)|Pointer|<pre lang="Turtle"><code>:CompressiveForce&#32;a&#32;owl:NamedIndividual,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;skos:Concept,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;:QuantityKind&#32;;  &#10; &#32; &#32; &#32; &#32;qudt:hasDimensionVector&#32; &#60;http://qudt.org/vocab/dimensionvector/A0E0L1I0M1H0T-2D0> &#32;;  &#10; &#32; &#32; &#32; &#32;qudt:symbol&#32; &#34;C&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32;:quantity&lowbar;kinds&#32;;  &#10; &#32; &#32; &#32; &#32;skos:broader&#32; &#60;http://qudt.org/vocab/quantitykind/Force> &#32;;  &#10; &#32; &#32; &#32; &#32;skos:definition&#32; &#34;Force&#32;tending&#32;to&#32;reduce&#32;the&#32;size&#32;of&#32;a&#32;body.&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;skos:prefLabel&#32; &#34;compressive&#32;force&#34;@en&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-142)|Pointer|<pre lang="Turtle"><code>:PartialSafetyFactor&#32;a&#32;owl:NamedIndividual,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;skos:Concept,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;:QuantityKind&#32;;  &#10; &#32; &#32; &#32; &#32;qudt:applicableUnit&#32; &#60;http://qudt.org/vocab/unit/UNITLESS> &#32;;  &#10; &#32; &#32; &#32; &#32;qudt:hasDimensionVector&#32; &#60;http://qudt.org/vocab/dimensionvector/A0E0L0I0M0H0T0D0> &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32;:quantity&lowbar;kinds&#32;;  &#10; &#32; &#32; &#32; &#32;skos:definition&#32; &#34;Also&#32;written&#32;γM,&#32;the&#32;partial&#32;safety&#32;factor&#32;for&#32;resistance.&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;skos:prefLabel&#32; &#34;Partial&#32;Safety&#32;Factor&#34;@en&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-142)|Pointer|<pre lang="Turtle"><code>:PartialSafetyFactor0&#32;a&#32;owl:NamedIndividual,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;skos:Concept,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;:QuantityKind&#32;;  &#10; &#32; &#32; &#32; &#32;qudt:applicableUnit&#32; &#60;http://qudt.org/vocab/unit/UNITLESS> &#32;;  &#10; &#32; &#32; &#32; &#32;qudt:hasDimensionVector&#32; &#60;http://qudt.org/vocab/dimensionvector/A0E0L0I0M0H0T0D0> &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32;:quantity&lowbar;kinds&#32;;  &#10; &#32; &#32; &#32; &#32;skos:broader&#32;:PartialSafetyFactor&#32;;  &#10; &#32; &#32; &#32; &#32;skos:definition&#32; &#34;Also&#32;written&#32;γM0,&#32;the&#32;partial&#32;safety&#32;factor&#32;for&#32;resistance&#32;r...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;skos:prefLabel&#32; &#34;Partial&#32;Safety&#32;Factor&#34;@en&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-142)|Pointer|<pre lang="Turtle"><code>:AxialCompressionStress&#32;a&#32;owl:NamedIndividual,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;skos:Concept,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;:QuantityKind&#32;;  &#10; &#32; &#32; &#32; &#32;qudt:hasDimensionVector&#32; &#60;http://qudt.org/vocab/dimensionvector/A0E0L1I0M-1H0T-2D0> &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32;:quantity&lowbar;kinds&#32;;  &#10; &#32; &#32; &#32; &#32;skos:definition&#32; &#34;also&#32;known&#32;as&#32;fc0k&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;skos:prefLabel&#32; &#34;axial&#32;compression&#32;stress&#34;@en&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-142)|Pointer|<pre lang="Turtle"><code>:ModificationFactorKmod&#32;a&#32;owl:NamedIndividual,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;skos:Concept,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;:QuantityKind&#32;;  &#10; &#32; &#32; &#32; &#32;qudt:applicableUnit&#32; &#60;http://qudt.org/vocab/unit/UNITLESS> &#32;;  &#10; &#32; &#32; &#32; &#32;qudt:hasDimensionVector&#32; &#60;http://qudt.org/vocab/dimensionvector/A0E0L0I0M0H0T0D0> &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32;:quantity&lowbar;kinds&#32;;  &#10; &#32; &#32; &#32; &#32;skos:definition&#32; &#34;Modification&#32;Factor&#32;to&#32;take&#32;into&#32;account&#32;the&#32;duration&#32;of&#32;loa...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;skos:prefLabel&#32; &#34;Modification&#32;Factor&#32;Kmod&#34;@en&#32;.</code></pre>|

***
### MinorFail Outcome number 143

[Jump to summary definition](#summary-MinorFail-143)	|	[Previous MinorFail outcome](#minorfail-outcome-number-142)	|	[Next MinorFail outcome](#minorfail-outcome-number-144)

:exclamation:MinorFail outcome
#### Subject detail
|Name|all-fragments|
|----|----|
|Title|All&#32;the&#32;fragments&#32;from&#32;branch&#32;HEAD&#32;that&#32;are&#32;syntaxically&#32;correct&#32;as&#32;well&#32;as&#32;their&#32;recursive&#32;imports|
|Composition|- [Module aec3po](https://github.com/Accord-Project/aec3po/blob/HEAD/src/aec3po.ttl)<br/>- [Module check&lowbar;method](https://github.com/Accord-Project/aec3po/blob/HEAD/src/check_method.ttl)<br/>- [Module checking&lowbar;act](https://github.com/Accord-Project/aec3po/blob/HEAD/src/checking_act.ttl)<br/>- [Module compliance&lowbar;verification&lowbar;report](https://github.com/Accord-Project/aec3po/blob/HEAD/src/compliance_verification_report.ttl)<br/>- [Module data&lowbar;requirement](https://github.com/Accord-Project/aec3po/blob/HEAD/src/data_requirement.ttl)<br/>- [Module document](https://github.com/Accord-Project/aec3po/blob/HEAD/src/document.ttl)<br/>- [Module evidence](https://github.com/Accord-Project/aec3po/blob/HEAD/src/evidence.ttl)<br/>- [Module feature&lowbar;of&lowbar;interest](https://github.com/Accord-Project/aec3po/blob/HEAD/src/feature_of_interest.ttl)<br/>- [Module legal&lowbar;verifier](https://github.com/Accord-Project/aec3po/blob/HEAD/src/legal_verifier.ttl)<br/>- [Module model](https://github.com/Accord-Project/aec3po/blob/HEAD/src/model.ttl)<br/>- [Module rase&lowbar;statement](https://github.com/Accord-Project/aec3po/blob/HEAD/src/rase_statement.ttl)<br/>- [Module statement](https://github.com/Accord-Project/aec3po/blob/HEAD/src/statement.ttl)<br/>- [Module table](https://github.com/Accord-Project/aec3po/blob/HEAD/src/table.ttl)<br/>- [Module vocabularies/&lowbar;shape](https://github.com/Accord-Project/aec3po/blob/HEAD/src/vocabularies/_shape.ttl)<br/>- [Module vocabularies/administrative&lowbar;areas](https://github.com/Accord-Project/aec3po/blob/HEAD/src/vocabularies/administrative_areas.ttl)<br/>- [Module vocabularies/building&lowbar;structure](https://github.com/Accord-Project/aec3po/blob/HEAD/src/vocabularies/building_structure.ttl)<br/>- [Module vocabularies/building&lowbar;usage](https://github.com/Accord-Project/aec3po/blob/HEAD/src/vocabularies/building_usage.ttl)<br/>- [Module vocabularies/check&lowbar;method&lowbar;comparators](https://github.com/Accord-Project/aec3po/blob/HEAD/src/vocabularies/check_method_comparators.ttl)<br/>- [Module vocabularies/check&lowbar;method&lowbar;operators](https://github.com/Accord-Project/aec3po/blob/HEAD/src/vocabularies/check_method_operators.ttl)<br/>- [Module vocabularies/disciplines](https://github.com/Accord-Project/aec3po/blob/HEAD/src/vocabularies/disciplines.ttl)<br/>- [Module vocabularies/permitting&lowbar;stages](https://github.com/Accord-Project/aec3po/blob/HEAD/src/vocabularies/permitting_stages.ttl)<br/>- [Module vocabularies/quantity&lowbar;kinds](https://github.com/Accord-Project/aec3po/blob/HEAD/src/vocabularies/quantity_kinds.ttl)|

#### Criterion detail
|Identifier|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|
|----|----|
|Title|Profile&#32;compatibility&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;check&#32;whether&#32;the&#32;test&#32;subject&#32;is&#32;compatible&#32;with&#32;a&#32;profile&#32;or&#32;not,&#32;and&#32;if&#32;it&#32;is&#32;not,&#32;why.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-143)|Identifier|`owl-el-profile-error`|
|[Section top](#minorfail-outcome-number-143)|Title|OWL&#32;EL&#32;Profile&#32;incompatible|
|[Section top](#minorfail-outcome-number-143)|Description|Class&#32;Expression&#32;not&#32;supported&#32;as&#32;object&#32;of&#32;rdfs:domain&#32;or&#32;rdfs:range|
|[Section top](#minorfail-outcome-number-143)|Pointer|<pre lang="Turtle"><code>aec3po:caption&#32;a&#32;owl:DatatypeProperty&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;caption&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;The&#32;caption&#32;of&#32;a&#32;table,&#32;image,&#32;etc.&#32; &#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:domain&#32; &#91;&#32;a&#32;owl:Class&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:unionOf&#32;(&#32;aec3po:Table&#32;aec3po:Image&#32;)&#32;]&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32;aec3po:table&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-143)|Pointer|<pre lang="Turtle"><code>aec3po:contains&#32;a&#32;owl:ObjectProperty&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;Contains&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;A&#32;container&#32;contains&#32;a&#32;table&#32;and&#32;its&#32;caption.&#32;A&#32;table&#32;contai...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:domain&#32; &#91;&#32;a&#32;owl:Class&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:unionOf&#32;(&#32;aec3po:Table&#32;aec3po:Image&#32;aec3po:Row&#32;aec3po:Column&#32;)&#32;]&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32;aec3po:table&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-143)|Pointer|<pre lang="Turtle"><code>aec3po:hasBSSDDTarget&#32;a&#32;owl:FunctionalProperty,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:ObjectProperty&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;hasBSSDDTarget&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;The&#32;target&#32;refers&#32;to&#32;either&#32;the&#32;name&#32;of&#32;an&#32;object,&#32;the&#32;name&#32;...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:domain&#32; &#91;&#32;a&#32;owl:Class&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:unionOf&#32;(&#32;aec3po:FeatureOfInterest&#32;aec3po:Property&#32;aec3po:CheckMethod&#32;)&#32;]&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32;aec3po:check&lowbar;method&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-143)|Pointer|<pre lang="Turtle"><code>aec3po:hasFirstSubdivision&#32;a&#32;owl:FunctionalProperty,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:ObjectProperty&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;has&#32;first&#32;subdivision&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;Links&#32;a&#32;document&#32;part&#32;to&#32;the&#32;first&#32;of&#32;its&#32;subdivision&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:domain&#32; &#91;&#32;owl:unionOf&#32;(&#32;aec3po:Document&#32;aec3po:DocumentSubdivision&#32;)&#32;]&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32;aec3po:document&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:range&#32;aec3po:DocumentSubdivision&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:subPropertyOf&#32;aec3po:hasSubdivision&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-143)|Pointer|<pre lang="Turtle"><code>aec3po:hasSubdivision&#32;a&#32;owl:ObjectProperty&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;has&#32;subdivision&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;links&#32;a&#32;document&#32;part&#32;to&#32;some&#32;of&#32;its&#32;subdivision&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:domain&#32; &#91;&#32;owl:unionOf&#32;(&#32;aec3po:Document&#32;aec3po:DocumentSubdivision&#32;)&#32;]&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32;aec3po:document&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:range&#32;aec3po:DocumentSubdivision&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:subPropertyOf&#32;dc:hasPart&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-143)|Pointer|<pre lang="Turtle"><code>aec3po:hasUnit&#32;a&#32;owl:FunctionalProperty,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:ObjectProperty&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;hasUnit&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;the&#32;hasUnit&#32;property&#32;is&#32;used&#32;to&#32;link&#32;a&#32;specific&#32;property&#32;or&#32;...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:domain&#32; &#91;&#32;a&#32;owl:Class&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:unionOf&#32;(&#32;aec3po:FeatureOfInterest&#32;aec3po:Property&#32;aec3po:CheckMethod&#32;)&#32;]&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32;aec3po:check&lowbar;method&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:range&#32;qudt:Unit&#32;;  &#10; &#32; &#32; &#32; &#32;owl:eqivalentProperty&#32;qudt:hasValue&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-143)|Pointer|<pre lang="Turtle"><code>aec3po:hasValue&#32;a&#32;owl:DatatypeProperty,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:FunctionalProperty&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;has&#32;value&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;de&#32;facto&#32;used&#32;to&#32;link&#32;something&#32;(anything:&#32;property,&#32;propert...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:domain&#32; &#91;&#32;a&#32;owl:Class&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:unionOf&#32;(&#32;aec3po:FeatureOfInterest&#32;aec3po:Property&#32;aec3po:CheckMethod&#32;)&#32;]&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32;aec3po:&#32;;  &#10; &#32; &#32; &#32; &#32;skos:note&#32; &#34;The&#32;value&#32;of&#32;the&#32;literal&#32;may&#32;be&#32;a&#32;XSD&#32;literal&#32;(boolean,&#32;inte...&#34; &#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-143)|Pointer|<pre lang="Turtle"><code>aec3po:isContainedIn&#32;a&#32;owl:ObjectProperty&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;is&#32;contained&#32;by&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;A&#32;table&#32;contains&#32;row,&#32;columns&#32;and&#32;other&#32;elements.&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32;aec3po:table&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:range&#32; &#91;&#32;a&#32;owl:Class&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:unionOf&#32;(&#32;aec3po:Table&#32;aec3po:Image&#32;aec3po:Row&#32;aec3po:Column&#32;aec3po:Cell&#32;)&#32;]&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-143)|Pointer|<pre lang="Turtle"><code>aec3po:locationCoverage&#32;a&#32;owl:ObjectProperty&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;location&#32;coverage&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;The&#32;spatialCoverage&#32;indicates&#32;the&#32;place(s)&#32;or&#32;the&#32;administra...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:domain&#32; &#60;https://schema.org/Model> &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:range&#32; &#91;&#32;a&#32;owl:Class&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:unionOf&#32;(&#32; &#60;https://schema.org/Place> &#32;aec3po:AdministrativeArea&#32;)&#32;]&#32;;  &#10; &#32; &#32; &#32; &#32;owl:equivalentProperty&#32; &#60;https://schema.org/spatialCoverage> &#32;.</code></pre>|

***
### MinorFail Outcome number 144

[Jump to summary definition](#summary-MinorFail-144)	|	[Previous MinorFail outcome](#minorfail-outcome-number-143)	|	[Next MinorFail outcome](#minorfail-outcome-number-145)

:exclamation:MinorFail outcome
#### Subject detail
|Name|all-fragments|
|----|----|
|Title|All&#32;the&#32;fragments&#32;from&#32;branch&#32;HEAD&#32;that&#32;are&#32;syntaxically&#32;correct&#32;as&#32;well&#32;as&#32;their&#32;recursive&#32;imports|
|Composition|- [Module aec3po](https://github.com/Accord-Project/aec3po/blob/HEAD/src/aec3po.ttl)<br/>- [Module check&lowbar;method](https://github.com/Accord-Project/aec3po/blob/HEAD/src/check_method.ttl)<br/>- [Module checking&lowbar;act](https://github.com/Accord-Project/aec3po/blob/HEAD/src/checking_act.ttl)<br/>- [Module compliance&lowbar;verification&lowbar;report](https://github.com/Accord-Project/aec3po/blob/HEAD/src/compliance_verification_report.ttl)<br/>- [Module data&lowbar;requirement](https://github.com/Accord-Project/aec3po/blob/HEAD/src/data_requirement.ttl)<br/>- [Module document](https://github.com/Accord-Project/aec3po/blob/HEAD/src/document.ttl)<br/>- [Module evidence](https://github.com/Accord-Project/aec3po/blob/HEAD/src/evidence.ttl)<br/>- [Module feature&lowbar;of&lowbar;interest](https://github.com/Accord-Project/aec3po/blob/HEAD/src/feature_of_interest.ttl)<br/>- [Module legal&lowbar;verifier](https://github.com/Accord-Project/aec3po/blob/HEAD/src/legal_verifier.ttl)<br/>- [Module model](https://github.com/Accord-Project/aec3po/blob/HEAD/src/model.ttl)<br/>- [Module rase&lowbar;statement](https://github.com/Accord-Project/aec3po/blob/HEAD/src/rase_statement.ttl)<br/>- [Module statement](https://github.com/Accord-Project/aec3po/blob/HEAD/src/statement.ttl)<br/>- [Module table](https://github.com/Accord-Project/aec3po/blob/HEAD/src/table.ttl)<br/>- [Module vocabularies/&lowbar;shape](https://github.com/Accord-Project/aec3po/blob/HEAD/src/vocabularies/_shape.ttl)<br/>- [Module vocabularies/administrative&lowbar;areas](https://github.com/Accord-Project/aec3po/blob/HEAD/src/vocabularies/administrative_areas.ttl)<br/>- [Module vocabularies/building&lowbar;structure](https://github.com/Accord-Project/aec3po/blob/HEAD/src/vocabularies/building_structure.ttl)<br/>- [Module vocabularies/building&lowbar;usage](https://github.com/Accord-Project/aec3po/blob/HEAD/src/vocabularies/building_usage.ttl)<br/>- [Module vocabularies/check&lowbar;method&lowbar;comparators](https://github.com/Accord-Project/aec3po/blob/HEAD/src/vocabularies/check_method_comparators.ttl)<br/>- [Module vocabularies/check&lowbar;method&lowbar;operators](https://github.com/Accord-Project/aec3po/blob/HEAD/src/vocabularies/check_method_operators.ttl)<br/>- [Module vocabularies/disciplines](https://github.com/Accord-Project/aec3po/blob/HEAD/src/vocabularies/disciplines.ttl)<br/>- [Module vocabularies/permitting&lowbar;stages](https://github.com/Accord-Project/aec3po/blob/HEAD/src/vocabularies/permitting_stages.ttl)<br/>- [Module vocabularies/quantity&lowbar;kinds](https://github.com/Accord-Project/aec3po/blob/HEAD/src/vocabularies/quantity_kinds.ttl)|

#### Criterion detail
|Identifier|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|
|----|----|
|Title|Profile&#32;compatibility&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;check&#32;whether&#32;the&#32;test&#32;subject&#32;is&#32;compatible&#32;with&#32;a&#32;profile&#32;or&#32;not,&#32;and&#32;if&#32;it&#32;is&#32;not,&#32;why.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-144)|Identifier|`owl-el-profile-error`|
|[Section top](#minorfail-outcome-number-144)|Title|OWL&#32;EL&#32;Profile&#32;incompatible|
|[Section top](#minorfail-outcome-number-144)|Description|Class&#32;Expression&#32;not&#32;supported&#32;with&#32;owl:equivalentClass|
|[Section top](#minorfail-outcome-number-144)|Pointer|<pre lang="Turtle"><code>aec3po:ComponentCheckMethod&#32;a&#32;owl:Class&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;Component&#32;Check&#32;Method&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;Component&#32;check&#32;method&#32;refers&#32;to&#32;a&#32;process&#32;of&#32;inspecting&#32;and...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32;aec3po:check&lowbar;method&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:subClassOf&#32;aec3po:CheckMethod&#32;;  &#10; &#32; &#32; &#32; &#32;owl:equivalentClass&#32; &#91;&#32;a&#32;owl:Class&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:intersectionOf&#32;(&#32;aec3po:CheckMethod&#32; &#91;&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:allValuesFrom&#32; &#91;&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:allValuesFrom&#32;aec3po:FeatureOfInterest&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:onProperty&#32; &#91;&#32;owl:inverseOf&#32;aec3po:forDesign&#32;]&#32;]&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:onProperty&#32;aec3po:forDesign&#32;]&#32;)&#32;]&#32;.</code></pre>|

***
### MinorFail Outcome number 145

[Jump to summary definition](#summary-MinorFail-145)	|	[Previous MinorFail outcome](#minorfail-outcome-number-144)	|	[Next MinorFail outcome](#minorfail-outcome-number-146)

:exclamation:MinorFail outcome
#### Subject detail
|Name|all-fragments|
|----|----|
|Title|All&#32;the&#32;fragments&#32;from&#32;branch&#32;HEAD&#32;that&#32;are&#32;syntaxically&#32;correct&#32;as&#32;well&#32;as&#32;their&#32;recursive&#32;imports|
|Composition|- [Module aec3po](https://github.com/Accord-Project/aec3po/blob/HEAD/src/aec3po.ttl)<br/>- [Module check&lowbar;method](https://github.com/Accord-Project/aec3po/blob/HEAD/src/check_method.ttl)<br/>- [Module checking&lowbar;act](https://github.com/Accord-Project/aec3po/blob/HEAD/src/checking_act.ttl)<br/>- [Module compliance&lowbar;verification&lowbar;report](https://github.com/Accord-Project/aec3po/blob/HEAD/src/compliance_verification_report.ttl)<br/>- [Module data&lowbar;requirement](https://github.com/Accord-Project/aec3po/blob/HEAD/src/data_requirement.ttl)<br/>- [Module document](https://github.com/Accord-Project/aec3po/blob/HEAD/src/document.ttl)<br/>- [Module evidence](https://github.com/Accord-Project/aec3po/blob/HEAD/src/evidence.ttl)<br/>- [Module feature&lowbar;of&lowbar;interest](https://github.com/Accord-Project/aec3po/blob/HEAD/src/feature_of_interest.ttl)<br/>- [Module legal&lowbar;verifier](https://github.com/Accord-Project/aec3po/blob/HEAD/src/legal_verifier.ttl)<br/>- [Module model](https://github.com/Accord-Project/aec3po/blob/HEAD/src/model.ttl)<br/>- [Module rase&lowbar;statement](https://github.com/Accord-Project/aec3po/blob/HEAD/src/rase_statement.ttl)<br/>- [Module statement](https://github.com/Accord-Project/aec3po/blob/HEAD/src/statement.ttl)<br/>- [Module table](https://github.com/Accord-Project/aec3po/blob/HEAD/src/table.ttl)<br/>- [Module vocabularies/&lowbar;shape](https://github.com/Accord-Project/aec3po/blob/HEAD/src/vocabularies/_shape.ttl)<br/>- [Module vocabularies/administrative&lowbar;areas](https://github.com/Accord-Project/aec3po/blob/HEAD/src/vocabularies/administrative_areas.ttl)<br/>- [Module vocabularies/building&lowbar;structure](https://github.com/Accord-Project/aec3po/blob/HEAD/src/vocabularies/building_structure.ttl)<br/>- [Module vocabularies/building&lowbar;usage](https://github.com/Accord-Project/aec3po/blob/HEAD/src/vocabularies/building_usage.ttl)<br/>- [Module vocabularies/check&lowbar;method&lowbar;comparators](https://github.com/Accord-Project/aec3po/blob/HEAD/src/vocabularies/check_method_comparators.ttl)<br/>- [Module vocabularies/check&lowbar;method&lowbar;operators](https://github.com/Accord-Project/aec3po/blob/HEAD/src/vocabularies/check_method_operators.ttl)<br/>- [Module vocabularies/disciplines](https://github.com/Accord-Project/aec3po/blob/HEAD/src/vocabularies/disciplines.ttl)<br/>- [Module vocabularies/permitting&lowbar;stages](https://github.com/Accord-Project/aec3po/blob/HEAD/src/vocabularies/permitting_stages.ttl)<br/>- [Module vocabularies/quantity&lowbar;kinds](https://github.com/Accord-Project/aec3po/blob/HEAD/src/vocabularies/quantity_kinds.ttl)|

#### Criterion detail
|Identifier|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|
|----|----|
|Title|Profile&#32;compatibility&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;check&#32;whether&#32;the&#32;test&#32;subject&#32;is&#32;compatible&#32;with&#32;a&#32;profile&#32;or&#32;not,&#32;and&#32;if&#32;it&#32;is&#32;not,&#32;why.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-145)|Identifier|`owl-el-profile-error`|
|[Section top](#minorfail-outcome-number-145)|Title|OWL&#32;EL&#32;Profile&#32;incompatible|
|[Section top](#minorfail-outcome-number-145)|Description|Class&#32;Expression&#32;not&#32;supported&#32;with&#32;rdfs:subClassOf|
|[Section top](#minorfail-outcome-number-145)|Pointer|<pre lang="Turtle"><code>aec3po:AndCheckStatement&#32;a&#32;owl:Class&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;And&#32;Check&#32;Statement&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;Check&#32;verified&#32;if&#32;and&#32;only&#32;if&#32;all&#32;of&#32;its&#32;sub-checks&#32;are&#32;veri...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32;aec3po:statement&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:subClassOf&#32; &#91;&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:onProperty&#32;aec3po:hasSubdivision&#32;],  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;aec3po:ChecklistStatement&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-145)|Pointer|<pre lang="Turtle"><code>aec3po:ComplianceVerificationReport&#32;a&#32;owl:Class&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;Compliance&#32;Verification&#32;Report&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;Result&#32;of&#32;a&#32;checking&#32;act.&#32;May&#32;be&#32;compliant&#32;or&#32;not.&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32;aec3po:compliance&lowbar;verification&lowbar;report&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:subClassOf&#32; &#91;&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:onProperty&#32;aec3po:conforms&#32;]&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-145)|Pointer|<pre lang="Turtle"><code>aec3po:DocumentSubdivision&#32;a&#32;owl:Class&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;Document&#32;Subdivision&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;Any&#32;subdivision&#32;of&#32;a&#32;document,&#32;including&#32;sections,&#32;paragraph...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32;aec3po:document&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:subClassOf&#32; &#91;&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:allValuesFrom&#32;aec3po:DocumentSubdivision&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:onProperty&#32;aec3po:hasSubdivision&#32;]&#32;;  &#10; &#32; &#32; &#32; &#32;skos:example&#32; &#34;Paragraph,&#32;section,&#32;definition...&#34;@en&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-145)|Pointer|<pre lang="Turtle"><code>aec3po:LegalVerifier&#32;a&#32;owl:Class&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;Legal&#32;Verifier&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;An&#32;entity&#32;that&#32;has&#32;the&#32;legal&#32;capacity&#32;to&#32;verify&#32;compliance&#32;w...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32;aec3po:legal&lowbar;verifier&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:subClassOf&#32; &#91;&#32;owl:allValuesFrom&#32;aec3po:Document&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:onProperty&#32;aec3po:forDocument&#32;],  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;foaf:Agent&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-145)|Pointer|<pre lang="Turtle"><code>aec3po:NotCheckStatement&#32;a&#32;owl:Class&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;Not&#32;Check&#32;Statement&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;Check&#32;verified&#32;if&#32;and&#32;only&#32;if&#32;the&#32;sub-check&#32;is&#32;not&#32;verified.&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32;aec3po:statement&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:subClassOf&#32; &#91;&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:onProperty&#32;aec3po:hasSubdivision&#32;]&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-145)|Pointer|<pre lang="Turtle"><code>aec3po:OrCheckStatement&#32;a&#32;owl:Class&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;Or&#32;Check&#32;Statement&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;Check&#32;verified&#32;if&#32;and&#32;only&#32;if&#32;at&#32;least&#32;one&#32;of&#32;its&#32;sub-checks...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32;aec3po:statement&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:subClassOf&#32; &#91;&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:onProperty&#32;aec3po:hasSubdivision&#32;],  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;aec3po:ChecklistStatement&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-145)|Pointer|<pre lang="Turtle"><code>aec3po:VerificationResult&#32;a&#32;owl:Class&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;Verification&#32;Result&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;Individual&#32;verification&#32;result&#32;of&#32;a&#32;Compliance&#32;Verification&#32;...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32;aec3po:compliance&lowbar;verification&lowbar;report&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:subClassOf&#32; &#91;&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:onProperty&#32;aec3po:verificationFocus&#32;],  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#91;&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:onProperty&#32;aec3po:hasSeverity&#32;]&#32;.</code></pre>|

***
### MinorFail Outcome number 146

[Jump to summary definition](#summary-MinorFail-146)	|	[Previous MinorFail outcome](#minorfail-outcome-number-145)	|	[Next MinorFail outcome](#minorfail-outcome-number-147)

:exclamation:MinorFail outcome
#### Subject detail
|Name|all-fragments|
|----|----|
|Title|All&#32;the&#32;fragments&#32;from&#32;branch&#32;HEAD&#32;that&#32;are&#32;syntaxically&#32;correct&#32;as&#32;well&#32;as&#32;their&#32;recursive&#32;imports|
|Composition|- [Module aec3po](https://github.com/Accord-Project/aec3po/blob/HEAD/src/aec3po.ttl)<br/>- [Module check&lowbar;method](https://github.com/Accord-Project/aec3po/blob/HEAD/src/check_method.ttl)<br/>- [Module checking&lowbar;act](https://github.com/Accord-Project/aec3po/blob/HEAD/src/checking_act.ttl)<br/>- [Module compliance&lowbar;verification&lowbar;report](https://github.com/Accord-Project/aec3po/blob/HEAD/src/compliance_verification_report.ttl)<br/>- [Module data&lowbar;requirement](https://github.com/Accord-Project/aec3po/blob/HEAD/src/data_requirement.ttl)<br/>- [Module document](https://github.com/Accord-Project/aec3po/blob/HEAD/src/document.ttl)<br/>- [Module evidence](https://github.com/Accord-Project/aec3po/blob/HEAD/src/evidence.ttl)<br/>- [Module feature&lowbar;of&lowbar;interest](https://github.com/Accord-Project/aec3po/blob/HEAD/src/feature_of_interest.ttl)<br/>- [Module legal&lowbar;verifier](https://github.com/Accord-Project/aec3po/blob/HEAD/src/legal_verifier.ttl)<br/>- [Module model](https://github.com/Accord-Project/aec3po/blob/HEAD/src/model.ttl)<br/>- [Module rase&lowbar;statement](https://github.com/Accord-Project/aec3po/blob/HEAD/src/rase_statement.ttl)<br/>- [Module statement](https://github.com/Accord-Project/aec3po/blob/HEAD/src/statement.ttl)<br/>- [Module table](https://github.com/Accord-Project/aec3po/blob/HEAD/src/table.ttl)<br/>- [Module vocabularies/&lowbar;shape](https://github.com/Accord-Project/aec3po/blob/HEAD/src/vocabularies/_shape.ttl)<br/>- [Module vocabularies/administrative&lowbar;areas](https://github.com/Accord-Project/aec3po/blob/HEAD/src/vocabularies/administrative_areas.ttl)<br/>- [Module vocabularies/building&lowbar;structure](https://github.com/Accord-Project/aec3po/blob/HEAD/src/vocabularies/building_structure.ttl)<br/>- [Module vocabularies/building&lowbar;usage](https://github.com/Accord-Project/aec3po/blob/HEAD/src/vocabularies/building_usage.ttl)<br/>- [Module vocabularies/check&lowbar;method&lowbar;comparators](https://github.com/Accord-Project/aec3po/blob/HEAD/src/vocabularies/check_method_comparators.ttl)<br/>- [Module vocabularies/check&lowbar;method&lowbar;operators](https://github.com/Accord-Project/aec3po/blob/HEAD/src/vocabularies/check_method_operators.ttl)<br/>- [Module vocabularies/disciplines](https://github.com/Accord-Project/aec3po/blob/HEAD/src/vocabularies/disciplines.ttl)<br/>- [Module vocabularies/permitting&lowbar;stages](https://github.com/Accord-Project/aec3po/blob/HEAD/src/vocabularies/permitting_stages.ttl)<br/>- [Module vocabularies/quantity&lowbar;kinds](https://github.com/Accord-Project/aec3po/blob/HEAD/src/vocabularies/quantity_kinds.ttl)|

#### Criterion detail
|Identifier|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|
|----|----|
|Title|Profile&#32;compatibility&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;check&#32;whether&#32;the&#32;test&#32;subject&#32;is&#32;compatible&#32;with&#32;a&#32;profile&#32;or&#32;not,&#32;and&#32;if&#32;it&#32;is&#32;not,&#32;why.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-146)|Identifier|`owl-el-profile-error`|
|[Section top](#minorfail-outcome-number-146)|Title|OWL&#32;EL&#32;Profile&#32;incompatible|
|[Section top](#minorfail-outcome-number-146)|Description|Restriction&#32;on&#32;datatypes|
|[Section top](#minorfail-outcome-number-146)|Pointer|<pre lang="Turtle"><code>aec3po:conforms&#32;a&#32;owl:DatatypeProperty&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;conforms&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;True&#32;if&#32;the&#32;Checking&#32;act&#32;confirms&#32;the&#32;check&#32;was&#32;validated,&#32;a...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:domain&#32;aec3po:ComplianceVerificationReport&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32;aec3po:compliance&lowbar;verification&lowbar;report&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:range&#32;xsd:boolean&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-146)|Pointer|<pre lang="Turtle"><code>aec3po:hasBooleanTarget&#32;a&#32;owl:DatatypeProperty&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;hasBooleanTarget&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;TBD&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:range&#32;xsd:boolean&#32;.</code></pre>|

***
### MinorFail Outcome number 147

[Jump to summary definition](#summary-MinorFail-147)	|	[Previous MinorFail outcome](#minorfail-outcome-number-146)	|	[Next MinorFail outcome](#minorfail-outcome-number-148)

:exclamation:MinorFail outcome
#### Subject detail
|Name|all-fragments|
|----|----|
|Title|All&#32;the&#32;fragments&#32;from&#32;branch&#32;HEAD&#32;that&#32;are&#32;syntaxically&#32;correct&#32;as&#32;well&#32;as&#32;their&#32;recursive&#32;imports|
|Composition|- [Module aec3po](https://github.com/Accord-Project/aec3po/blob/HEAD/src/aec3po.ttl)<br/>- [Module check&lowbar;method](https://github.com/Accord-Project/aec3po/blob/HEAD/src/check_method.ttl)<br/>- [Module checking&lowbar;act](https://github.com/Accord-Project/aec3po/blob/HEAD/src/checking_act.ttl)<br/>- [Module compliance&lowbar;verification&lowbar;report](https://github.com/Accord-Project/aec3po/blob/HEAD/src/compliance_verification_report.ttl)<br/>- [Module data&lowbar;requirement](https://github.com/Accord-Project/aec3po/blob/HEAD/src/data_requirement.ttl)<br/>- [Module document](https://github.com/Accord-Project/aec3po/blob/HEAD/src/document.ttl)<br/>- [Module evidence](https://github.com/Accord-Project/aec3po/blob/HEAD/src/evidence.ttl)<br/>- [Module feature&lowbar;of&lowbar;interest](https://github.com/Accord-Project/aec3po/blob/HEAD/src/feature_of_interest.ttl)<br/>- [Module legal&lowbar;verifier](https://github.com/Accord-Project/aec3po/blob/HEAD/src/legal_verifier.ttl)<br/>- [Module model](https://github.com/Accord-Project/aec3po/blob/HEAD/src/model.ttl)<br/>- [Module rase&lowbar;statement](https://github.com/Accord-Project/aec3po/blob/HEAD/src/rase_statement.ttl)<br/>- [Module statement](https://github.com/Accord-Project/aec3po/blob/HEAD/src/statement.ttl)<br/>- [Module table](https://github.com/Accord-Project/aec3po/blob/HEAD/src/table.ttl)<br/>- [Module vocabularies/&lowbar;shape](https://github.com/Accord-Project/aec3po/blob/HEAD/src/vocabularies/_shape.ttl)<br/>- [Module vocabularies/administrative&lowbar;areas](https://github.com/Accord-Project/aec3po/blob/HEAD/src/vocabularies/administrative_areas.ttl)<br/>- [Module vocabularies/building&lowbar;structure](https://github.com/Accord-Project/aec3po/blob/HEAD/src/vocabularies/building_structure.ttl)<br/>- [Module vocabularies/building&lowbar;usage](https://github.com/Accord-Project/aec3po/blob/HEAD/src/vocabularies/building_usage.ttl)<br/>- [Module vocabularies/check&lowbar;method&lowbar;comparators](https://github.com/Accord-Project/aec3po/blob/HEAD/src/vocabularies/check_method_comparators.ttl)<br/>- [Module vocabularies/check&lowbar;method&lowbar;operators](https://github.com/Accord-Project/aec3po/blob/HEAD/src/vocabularies/check_method_operators.ttl)<br/>- [Module vocabularies/disciplines](https://github.com/Accord-Project/aec3po/blob/HEAD/src/vocabularies/disciplines.ttl)<br/>- [Module vocabularies/permitting&lowbar;stages](https://github.com/Accord-Project/aec3po/blob/HEAD/src/vocabularies/permitting_stages.ttl)<br/>- [Module vocabularies/quantity&lowbar;kinds](https://github.com/Accord-Project/aec3po/blob/HEAD/src/vocabularies/quantity_kinds.ttl)|

#### Criterion detail
|Identifier|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|
|----|----|
|Title|Profile&#32;compatibility&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;check&#32;whether&#32;the&#32;test&#32;subject&#32;is&#32;compatible&#32;with&#32;a&#32;profile&#32;or&#32;not,&#32;and&#32;if&#32;it&#32;is&#32;not,&#32;why.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-147)|Identifier|`owl-el-profile-error`|
|[Section top](#minorfail-outcome-number-147)|Title|OWL&#32;EL&#32;Profile&#32;incompatible|
|[Section top](#minorfail-outcome-number-147)|Description|Statement&#32;not&#32;supported&#32;in&#32;a&#32;Class&#32;Expression|
|[Section top](#minorfail-outcome-number-147)|Pointer|<pre lang="Turtle"><code>&#91;]&#32;a&#32;owl:Class&#32;;  &#10; &#32; &#32;&#32; &#32;owl:unionOf&#32;(&#32;aec3po:FeatureOfInterest&#32;aec3po:Property&#32;aec3po:CheckMethod&#32;)&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-147)|Pointer|<pre lang="Turtle"><code>&#91;]&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32;owl:allValuesFrom&#32; &#91;&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:allValuesFrom&#32;aec3po:FeatureOfInterest&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:onProperty&#32; &#91;&#32;owl:inverseOf&#32;aec3po:forDesign&#32;]&#32;]&#32;;  &#10; &#32; &#32; &#32; &#32;owl:onProperty&#32;aec3po:forDesign&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-147)|Pointer|<pre lang="Turtle"><code>&#91;]&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32;&#32; &#32;owl:onProperty&#32;aec3po:conforms&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-147)|Pointer|<pre lang="Turtle"><code>&#91;]&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32;&#32; &#32;owl:onProperty&#32;aec3po:verificationFocus&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-147)|Pointer|<pre lang="Turtle"><code>&#91;]&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32;&#32; &#32;owl:onProperty&#32;aec3po:hasSeverity&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-147)|Pointer|<pre lang="Turtle"><code>&#91;]&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32;owl:allValuesFrom&#32;aec3po:DocumentSubdivision&#32;;  &#10; &#32; &#32; &#32; &#32;owl:onProperty&#32;aec3po:hasSubdivision&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-147)|Pointer|<pre lang="Turtle"><code>&#91;]&#32;owl:unionOf&#32;(&#32;aec3po:Document&#32;aec3po:DocumentSubdivision&#32;)&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-147)|Pointer|<pre lang="Turtle"><code>&#91;]&#32;owl:allValuesFrom&#32;aec3po:Document&#32;;  &#10; &#32; &#32;&#32; &#32;owl:onProperty&#32;aec3po:forDocument&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-147)|Pointer|<pre lang="Turtle"><code>&#91;]&#32;a&#32;owl:Class&#32;;  &#10; &#32; &#32;&#32; &#32;owl:unionOf&#32;(&#32; &#60;https://schema.org/Place> &#32;aec3po:AdministrativeArea&#32;)&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-147)|Pointer|<pre lang="Turtle"><code>&#91;]&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32;&#32; &#32;owl:onProperty&#32;aec3po:hasSubdivision&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-147)|Pointer|<pre lang="Turtle"><code>&#91;]&#32;a&#32;owl:Class&#32;;  &#10; &#32; &#32;&#32; &#32;owl:unionOf&#32;(&#32;aec3po:Table&#32;aec3po:Image&#32;aec3po:Row&#32;aec3po:Column&#32;)&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-147)|Pointer|<pre lang="Turtle"><code>&#91;]&#32;a&#32;owl:Class&#32;;  &#10; &#32; &#32;&#32; &#32;owl:unionOf&#32;(&#32;aec3po:Table&#32;aec3po:Image&#32;aec3po:Row&#32;aec3po:Column&#32;aec3po:Cell&#32;)&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-147)|Pointer|<pre lang="Turtle"><code>&#91;]&#32;a&#32;owl:Class&#32;;  &#10; &#32; &#32;&#32; &#32;owl:unionOf&#32;(&#32;aec3po:Table&#32;aec3po:Image&#32;)&#32;.</code></pre>|

***
### MinorFail Outcome number 148

[Jump to summary definition](#summary-MinorFail-148)	|	[Previous MinorFail outcome](#minorfail-outcome-number-147)	|	[Next MinorFail outcome](#minorfail-outcome-number-149)

:exclamation:MinorFail outcome
#### Subject detail
|Name|all-fragments|
|----|----|
|Title|All&#32;the&#32;fragments&#32;from&#32;branch&#32;HEAD&#32;that&#32;are&#32;syntaxically&#32;correct&#32;as&#32;well&#32;as&#32;their&#32;recursive&#32;imports|
|Composition|- [Module aec3po](https://github.com/Accord-Project/aec3po/blob/HEAD/src/aec3po.ttl)<br/>- [Module check&lowbar;method](https://github.com/Accord-Project/aec3po/blob/HEAD/src/check_method.ttl)<br/>- [Module checking&lowbar;act](https://github.com/Accord-Project/aec3po/blob/HEAD/src/checking_act.ttl)<br/>- [Module compliance&lowbar;verification&lowbar;report](https://github.com/Accord-Project/aec3po/blob/HEAD/src/compliance_verification_report.ttl)<br/>- [Module data&lowbar;requirement](https://github.com/Accord-Project/aec3po/blob/HEAD/src/data_requirement.ttl)<br/>- [Module document](https://github.com/Accord-Project/aec3po/blob/HEAD/src/document.ttl)<br/>- [Module evidence](https://github.com/Accord-Project/aec3po/blob/HEAD/src/evidence.ttl)<br/>- [Module feature&lowbar;of&lowbar;interest](https://github.com/Accord-Project/aec3po/blob/HEAD/src/feature_of_interest.ttl)<br/>- [Module legal&lowbar;verifier](https://github.com/Accord-Project/aec3po/blob/HEAD/src/legal_verifier.ttl)<br/>- [Module model](https://github.com/Accord-Project/aec3po/blob/HEAD/src/model.ttl)<br/>- [Module rase&lowbar;statement](https://github.com/Accord-Project/aec3po/blob/HEAD/src/rase_statement.ttl)<br/>- [Module statement](https://github.com/Accord-Project/aec3po/blob/HEAD/src/statement.ttl)<br/>- [Module table](https://github.com/Accord-Project/aec3po/blob/HEAD/src/table.ttl)<br/>- [Module vocabularies/&lowbar;shape](https://github.com/Accord-Project/aec3po/blob/HEAD/src/vocabularies/_shape.ttl)<br/>- [Module vocabularies/administrative&lowbar;areas](https://github.com/Accord-Project/aec3po/blob/HEAD/src/vocabularies/administrative_areas.ttl)<br/>- [Module vocabularies/building&lowbar;structure](https://github.com/Accord-Project/aec3po/blob/HEAD/src/vocabularies/building_structure.ttl)<br/>- [Module vocabularies/building&lowbar;usage](https://github.com/Accord-Project/aec3po/blob/HEAD/src/vocabularies/building_usage.ttl)<br/>- [Module vocabularies/check&lowbar;method&lowbar;comparators](https://github.com/Accord-Project/aec3po/blob/HEAD/src/vocabularies/check_method_comparators.ttl)<br/>- [Module vocabularies/check&lowbar;method&lowbar;operators](https://github.com/Accord-Project/aec3po/blob/HEAD/src/vocabularies/check_method_operators.ttl)<br/>- [Module vocabularies/disciplines](https://github.com/Accord-Project/aec3po/blob/HEAD/src/vocabularies/disciplines.ttl)<br/>- [Module vocabularies/permitting&lowbar;stages](https://github.com/Accord-Project/aec3po/blob/HEAD/src/vocabularies/permitting_stages.ttl)<br/>- [Module vocabularies/quantity&lowbar;kinds](https://github.com/Accord-Project/aec3po/blob/HEAD/src/vocabularies/quantity_kinds.ttl)|

#### Criterion detail
|Identifier|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|
|----|----|
|Title|Profile&#32;compatibility&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;check&#32;whether&#32;the&#32;test&#32;subject&#32;is&#32;compatible&#32;with&#32;a&#32;profile&#32;or&#32;not,&#32;and&#32;if&#32;it&#32;is&#32;not,&#32;why.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-148)|Identifier|`owl-ql-profile-error`|
|[Section top](#minorfail-outcome-number-148)|Title|OWL&#32;QL&#32;Profile&#32;incompatible|
|[Section top](#minorfail-outcome-number-148)|Description|Class&#32;Expression&#32;not&#32;supported&#32;as&#32;object&#32;of&#32;rdfs:domain&#32;or&#32;rdfs:range|
|[Section top](#minorfail-outcome-number-148)|Pointer|<pre lang="Turtle"><code>aec3po:caption&#32;a&#32;owl:DatatypeProperty&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;caption&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;The&#32;caption&#32;of&#32;a&#32;table,&#32;image,&#32;etc.&#32; &#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:domain&#32; &#91;&#32;a&#32;owl:Class&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:unionOf&#32;(&#32;aec3po:Table&#32;aec3po:Image&#32;)&#32;]&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32;aec3po:table&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-148)|Pointer|<pre lang="Turtle"><code>aec3po:contains&#32;a&#32;owl:ObjectProperty&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;Contains&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;A&#32;container&#32;contains&#32;a&#32;table&#32;and&#32;its&#32;caption.&#32;A&#32;table&#32;contai...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:domain&#32; &#91;&#32;a&#32;owl:Class&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:unionOf&#32;(&#32;aec3po:Table&#32;aec3po:Image&#32;aec3po:Row&#32;aec3po:Column&#32;)&#32;]&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32;aec3po:table&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-148)|Pointer|<pre lang="Turtle"><code>aec3po:hasBSSDDTarget&#32;a&#32;owl:FunctionalProperty,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:ObjectProperty&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;hasBSSDDTarget&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;The&#32;target&#32;refers&#32;to&#32;either&#32;the&#32;name&#32;of&#32;an&#32;object,&#32;the&#32;name&#32;...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:domain&#32; &#91;&#32;a&#32;owl:Class&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:unionOf&#32;(&#32;aec3po:FeatureOfInterest&#32;aec3po:Property&#32;aec3po:CheckMethod&#32;)&#32;]&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32;aec3po:check&lowbar;method&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-148)|Pointer|<pre lang="Turtle"><code>aec3po:hasFirstSubdivision&#32;a&#32;owl:FunctionalProperty,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:ObjectProperty&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;has&#32;first&#32;subdivision&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;Links&#32;a&#32;document&#32;part&#32;to&#32;the&#32;first&#32;of&#32;its&#32;subdivision&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:domain&#32; &#91;&#32;owl:unionOf&#32;(&#32;aec3po:Document&#32;aec3po:DocumentSubdivision&#32;)&#32;]&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32;aec3po:document&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:range&#32;aec3po:DocumentSubdivision&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:subPropertyOf&#32;aec3po:hasSubdivision&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-148)|Pointer|<pre lang="Turtle"><code>aec3po:hasSubdivision&#32;a&#32;owl:ObjectProperty&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;has&#32;subdivision&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;links&#32;a&#32;document&#32;part&#32;to&#32;some&#32;of&#32;its&#32;subdivision&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:domain&#32; &#91;&#32;owl:unionOf&#32;(&#32;aec3po:Document&#32;aec3po:DocumentSubdivision&#32;)&#32;]&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32;aec3po:document&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:range&#32;aec3po:DocumentSubdivision&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:subPropertyOf&#32;dc:hasPart&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-148)|Pointer|<pre lang="Turtle"><code>aec3po:hasUnit&#32;a&#32;owl:FunctionalProperty,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:ObjectProperty&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;hasUnit&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;the&#32;hasUnit&#32;property&#32;is&#32;used&#32;to&#32;link&#32;a&#32;specific&#32;property&#32;or&#32;...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:domain&#32; &#91;&#32;a&#32;owl:Class&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:unionOf&#32;(&#32;aec3po:FeatureOfInterest&#32;aec3po:Property&#32;aec3po:CheckMethod&#32;)&#32;]&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32;aec3po:check&lowbar;method&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:range&#32;qudt:Unit&#32;;  &#10; &#32; &#32; &#32; &#32;owl:eqivalentProperty&#32;qudt:hasValue&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-148)|Pointer|<pre lang="Turtle"><code>aec3po:hasValue&#32;a&#32;owl:DatatypeProperty,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:FunctionalProperty&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;has&#32;value&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;de&#32;facto&#32;used&#32;to&#32;link&#32;something&#32;(anything:&#32;property,&#32;propert...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:domain&#32; &#91;&#32;a&#32;owl:Class&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:unionOf&#32;(&#32;aec3po:FeatureOfInterest&#32;aec3po:Property&#32;aec3po:CheckMethod&#32;)&#32;]&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32;aec3po:&#32;;  &#10; &#32; &#32; &#32; &#32;skos:note&#32; &#34;The&#32;value&#32;of&#32;the&#32;literal&#32;may&#32;be&#32;a&#32;XSD&#32;literal&#32;(boolean,&#32;inte...&#34; &#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-148)|Pointer|<pre lang="Turtle"><code>aec3po:isContainedIn&#32;a&#32;owl:ObjectProperty&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;is&#32;contained&#32;by&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;A&#32;table&#32;contains&#32;row,&#32;columns&#32;and&#32;other&#32;elements.&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32;aec3po:table&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:range&#32; &#91;&#32;a&#32;owl:Class&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:unionOf&#32;(&#32;aec3po:Table&#32;aec3po:Image&#32;aec3po:Row&#32;aec3po:Column&#32;aec3po:Cell&#32;)&#32;]&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-148)|Pointer|<pre lang="Turtle"><code>aec3po:locationCoverage&#32;a&#32;owl:ObjectProperty&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;location&#32;coverage&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;The&#32;spatialCoverage&#32;indicates&#32;the&#32;place(s)&#32;or&#32;the&#32;administra...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:domain&#32; &#60;https://schema.org/Model> &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:range&#32; &#91;&#32;a&#32;owl:Class&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:unionOf&#32;(&#32; &#60;https://schema.org/Place> &#32;aec3po:AdministrativeArea&#32;)&#32;]&#32;;  &#10; &#32; &#32; &#32; &#32;owl:equivalentProperty&#32; &#60;https://schema.org/spatialCoverage> &#32;.</code></pre>|

***
### MinorFail Outcome number 149

[Jump to summary definition](#summary-MinorFail-149)	|	[Previous MinorFail outcome](#minorfail-outcome-number-148)	|	[Next MinorFail outcome](#minorfail-outcome-number-150)

:exclamation:MinorFail outcome
#### Subject detail
|Name|all-fragments|
|----|----|
|Title|All&#32;the&#32;fragments&#32;from&#32;branch&#32;HEAD&#32;that&#32;are&#32;syntaxically&#32;correct&#32;as&#32;well&#32;as&#32;their&#32;recursive&#32;imports|
|Composition|- [Module aec3po](https://github.com/Accord-Project/aec3po/blob/HEAD/src/aec3po.ttl)<br/>- [Module check&lowbar;method](https://github.com/Accord-Project/aec3po/blob/HEAD/src/check_method.ttl)<br/>- [Module checking&lowbar;act](https://github.com/Accord-Project/aec3po/blob/HEAD/src/checking_act.ttl)<br/>- [Module compliance&lowbar;verification&lowbar;report](https://github.com/Accord-Project/aec3po/blob/HEAD/src/compliance_verification_report.ttl)<br/>- [Module data&lowbar;requirement](https://github.com/Accord-Project/aec3po/blob/HEAD/src/data_requirement.ttl)<br/>- [Module document](https://github.com/Accord-Project/aec3po/blob/HEAD/src/document.ttl)<br/>- [Module evidence](https://github.com/Accord-Project/aec3po/blob/HEAD/src/evidence.ttl)<br/>- [Module feature&lowbar;of&lowbar;interest](https://github.com/Accord-Project/aec3po/blob/HEAD/src/feature_of_interest.ttl)<br/>- [Module legal&lowbar;verifier](https://github.com/Accord-Project/aec3po/blob/HEAD/src/legal_verifier.ttl)<br/>- [Module model](https://github.com/Accord-Project/aec3po/blob/HEAD/src/model.ttl)<br/>- [Module rase&lowbar;statement](https://github.com/Accord-Project/aec3po/blob/HEAD/src/rase_statement.ttl)<br/>- [Module statement](https://github.com/Accord-Project/aec3po/blob/HEAD/src/statement.ttl)<br/>- [Module table](https://github.com/Accord-Project/aec3po/blob/HEAD/src/table.ttl)<br/>- [Module vocabularies/&lowbar;shape](https://github.com/Accord-Project/aec3po/blob/HEAD/src/vocabularies/_shape.ttl)<br/>- [Module vocabularies/administrative&lowbar;areas](https://github.com/Accord-Project/aec3po/blob/HEAD/src/vocabularies/administrative_areas.ttl)<br/>- [Module vocabularies/building&lowbar;structure](https://github.com/Accord-Project/aec3po/blob/HEAD/src/vocabularies/building_structure.ttl)<br/>- [Module vocabularies/building&lowbar;usage](https://github.com/Accord-Project/aec3po/blob/HEAD/src/vocabularies/building_usage.ttl)<br/>- [Module vocabularies/check&lowbar;method&lowbar;comparators](https://github.com/Accord-Project/aec3po/blob/HEAD/src/vocabularies/check_method_comparators.ttl)<br/>- [Module vocabularies/check&lowbar;method&lowbar;operators](https://github.com/Accord-Project/aec3po/blob/HEAD/src/vocabularies/check_method_operators.ttl)<br/>- [Module vocabularies/disciplines](https://github.com/Accord-Project/aec3po/blob/HEAD/src/vocabularies/disciplines.ttl)<br/>- [Module vocabularies/permitting&lowbar;stages](https://github.com/Accord-Project/aec3po/blob/HEAD/src/vocabularies/permitting_stages.ttl)<br/>- [Module vocabularies/quantity&lowbar;kinds](https://github.com/Accord-Project/aec3po/blob/HEAD/src/vocabularies/quantity_kinds.ttl)|

#### Criterion detail
|Identifier|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|
|----|----|
|Title|Profile&#32;compatibility&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;check&#32;whether&#32;the&#32;test&#32;subject&#32;is&#32;compatible&#32;with&#32;a&#32;profile&#32;or&#32;not,&#32;and&#32;if&#32;it&#32;is&#32;not,&#32;why.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-149)|Identifier|`owl-ql-profile-error`|
|[Section top](#minorfail-outcome-number-149)|Title|OWL&#32;QL&#32;Profile&#32;incompatible|
|[Section top](#minorfail-outcome-number-149)|Description|Class&#32;Expression&#32;not&#32;supported&#32;with&#32;owl:equivalentClass|
|[Section top](#minorfail-outcome-number-149)|Pointer|<pre lang="Turtle"><code>aec3po:AdministrativeArea&#32;a&#32;owl:Class&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;Administrative&#32;Area&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;Formally&#32;defined&#32;as&#32;the&#32;set&#32;of&#32;skos:Concept&#32;either&#32;in&#32;concep...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32;aec3po:administrative&lowbar;areas&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:seeAlso&#32; &#60;https://op.europa.eu/en/web/eu-vocabularies/concept-scheme/-/resource?uri=http://publications.europa.eu/resource/authority/atu> &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:subClassOf&#32;skos:Concept&#32;;  &#10; &#32; &#32; &#32; &#32;owl:equivalentClass&#32; &#91;&#32;owl:intersectionOf&#32;(&#32;skos:Concept&#32; &#91;&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:hasValue&#32;aec3po:AdministrativeAreaNomenclature&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:onProperty&#32;skos:inScheme&#32;]&#32;)&#32;],  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#60;http://data.europa.eu/eli/ontology#AdministrativeArea> &#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-149)|Pointer|<pre lang="Turtle"><code>aec3po:BuildingStructure&#32;a&#32;owl:Class&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;building&#32;structure&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;Formally&#32;defined&#32;as&#32;the&#32;set&#32;of&#32;skos:Concept&#32;in&#32;concept&#32;schem...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32;aec3po:building&lowbar;structure&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:subClassOf&#32;skos:Concept,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;aec3po:Design&#32;;  &#10; &#32; &#32; &#32; &#32;owl:equivalentClass&#32; &#91;&#32;owl:intersectionOf&#32;(&#32;skos:Concept&#32; &#91;&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:hasValue&#32;aec3po:BuildingStructureNomenclature&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:onProperty&#32;skos:inScheme&#32;]&#32;)&#32;]&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-149)|Pointer|<pre lang="Turtle"><code>aec3po:BuildingUsage&#32;a&#32;owl:Class&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;building&#32;usage&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;Formally&#32;defined&#32;as&#32;the&#32;set&#32;of&#32;skos:Concept&#32;in&#32;concept&#32;schem...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32;aec3po:building&lowbar;usage&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:subClassOf&#32;skos:Concept,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;aec3po:Design&#32;;  &#10; &#32; &#32; &#32; &#32;owl:equivalentClass&#32; &#91;&#32;owl:intersectionOf&#32;(&#32;skos:Concept&#32; &#91;&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:hasValue&#32;aec3po:BuildingUsageNomenclature&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:onProperty&#32;skos:inScheme&#32;]&#32;)&#32;]&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-149)|Pointer|<pre lang="Turtle"><code>aec3po:CheckMethodComparator&#32;a&#32;owl:Class&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;check&#32;method&#32;comparator&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;Formally&#32;defined&#32;as&#32;the&#32;set&#32;of&#32;skos:Concept&#32;in&#32;concept&#32;schem...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32;aec3po:check&lowbar;method&lowbar;comparators&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:subClassOf&#32;skos:Concept,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;aec3po:CheckMethod&#32;;  &#10; &#32; &#32; &#32; &#32;owl:equivalentClass&#32; &#91;&#32;owl:intersectionOf&#32;(&#32;skos:Concept&#32; &#91;&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:hasValue&#32;aec3po:CheckMethodComparatorNomenclature&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:onProperty&#32;skos:inScheme&#32;]&#32;)&#32;]&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-149)|Pointer|<pre lang="Turtle"><code>aec3po:CheckMethodOperator&#32;a&#32;owl:Class&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;check&#32;method&#32;operator&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;Formally&#32;defined&#32;as&#32;the&#32;set&#32;of&#32;skos:Concept&#32;in&#32;concept&#32;schem...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32;aec3po:check&lowbar;method&lowbar;operators&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:subClassOf&#32;skos:Concept,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;aec3po:CheckMethod&#32;;  &#10; &#32; &#32; &#32; &#32;owl:equivalentClass&#32; &#91;&#32;owl:intersectionOf&#32;(&#32;skos:Concept&#32; &#91;&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:hasValue&#32;aec3po:CheckMethodOperatorNomenclature&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:onProperty&#32;skos:inScheme&#32;]&#32;)&#32;]&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-149)|Pointer|<pre lang="Turtle"><code>aec3po:ComponentCheckMethod&#32;a&#32;owl:Class&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;Component&#32;Check&#32;Method&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;Component&#32;check&#32;method&#32;refers&#32;to&#32;a&#32;process&#32;of&#32;inspecting&#32;and...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32;aec3po:check&lowbar;method&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:subClassOf&#32;aec3po:CheckMethod&#32;;  &#10; &#32; &#32; &#32; &#32;owl:equivalentClass&#32; &#91;&#32;a&#32;owl:Class&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:intersectionOf&#32;(&#32;aec3po:CheckMethod&#32; &#91;&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:allValuesFrom&#32; &#91;&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:allValuesFrom&#32;aec3po:FeatureOfInterest&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:onProperty&#32; &#91;&#32;owl:inverseOf&#32;aec3po:forDesign&#32;]&#32;]&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:onProperty&#32;aec3po:forDesign&#32;]&#32;)&#32;]&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-149)|Pointer|<pre lang="Turtle"><code>aec3po:Discipline&#32;a&#32;owl:Class&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;Discipline&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;The&#32;AEC&#32;discipline&#32;to&#32;which&#32;something&#32;pertains.&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32;aec3po:discipline&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:subClassOf&#32;skos:Concept&#32;;  &#10; &#32; &#32; &#32; &#32;owl:equivalentClass&#32; &#91;&#32;owl:intersectionOf&#32;(&#32;skos:Concept&#32; &#91;&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:hasValue&#32;aec3po:DisciplineNomenclature&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:onProperty&#32;skos:inScheme&#32;]&#32;)&#32;]&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-149)|Pointer|<pre lang="Turtle"><code>aec3po:PermittingStage&#32;a&#32;owl:Class&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;Permitting&#32;Stage&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;The&#32;class&#32;of&#32;permitting&#32;stages.&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32;aec3po:permitting&lowbar;stage&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:subClassOf&#32;skos:Concept&#32;;  &#10; &#32; &#32; &#32; &#32;owl:equivalentClass&#32; &#91;&#32;owl:intersectionOf&#32;(&#32;skos:Concept&#32; &#91;&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:hasValue&#32;aec3po:PermittingStageNomenclature&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:onProperty&#32;skos:inScheme&#32;]&#32;)&#32;]&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-149)|Pointer|<pre lang="Turtle"><code>aec3po:QuantityKind&#32;a&#32;owl:Class&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;Quantity&#32;Kind&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;A&#32;Quantity&#32;Kind&#32;is&#32;any&#32;observable&#32;property&#32;that&#32;can&#32;be&#32;quant...&#34;,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#34;A&#32;kind&#32;of&#32;quantity.&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32;aec3po:feature&lowbar;of&lowbar;interest,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;aec3po:quantity&lowbar;kinds&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:subClassOf&#32;qudt:QuantityKind,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#60;http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#Region>,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;skos:Concept&#32;;  &#10; &#32; &#32; &#32; &#32;owl:equivalentClass&#32; &#91;&#32;owl:intersectionOf&#32;(&#32;skos:Concept&#32; &#91;&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:hasValue&#32;aec3po:QuantityKindNomenclature&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:onProperty&#32;skos:inScheme&#32;]&#32;)&#32;]&#32;;  &#10; &#32; &#32; &#32; &#32;skos:example&#32; &#34;Length,&#32;Area,&#32;U-Value.&#34;@en,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#34;height,&#32;area,&#32;U-value&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;skos:note&#32; &#34;Maxime&#32;Lefrançois&#32;argues&#32;that&#32;both&#32;qudt:QuantityKind&#32;and&#32;qud...&#34; &#32;.</code></pre>|

***
### MinorFail Outcome number 150

[Jump to summary definition](#summary-MinorFail-150)	|	[Previous MinorFail outcome](#minorfail-outcome-number-149)	|	[Next MinorFail outcome](#minorfail-outcome-number-151)

:exclamation:MinorFail outcome
#### Subject detail
|Name|all-fragments|
|----|----|
|Title|All&#32;the&#32;fragments&#32;from&#32;branch&#32;HEAD&#32;that&#32;are&#32;syntaxically&#32;correct&#32;as&#32;well&#32;as&#32;their&#32;recursive&#32;imports|
|Composition|- [Module aec3po](https://github.com/Accord-Project/aec3po/blob/HEAD/src/aec3po.ttl)<br/>- [Module check&lowbar;method](https://github.com/Accord-Project/aec3po/blob/HEAD/src/check_method.ttl)<br/>- [Module checking&lowbar;act](https://github.com/Accord-Project/aec3po/blob/HEAD/src/checking_act.ttl)<br/>- [Module compliance&lowbar;verification&lowbar;report](https://github.com/Accord-Project/aec3po/blob/HEAD/src/compliance_verification_report.ttl)<br/>- [Module data&lowbar;requirement](https://github.com/Accord-Project/aec3po/blob/HEAD/src/data_requirement.ttl)<br/>- [Module document](https://github.com/Accord-Project/aec3po/blob/HEAD/src/document.ttl)<br/>- [Module evidence](https://github.com/Accord-Project/aec3po/blob/HEAD/src/evidence.ttl)<br/>- [Module feature&lowbar;of&lowbar;interest](https://github.com/Accord-Project/aec3po/blob/HEAD/src/feature_of_interest.ttl)<br/>- [Module legal&lowbar;verifier](https://github.com/Accord-Project/aec3po/blob/HEAD/src/legal_verifier.ttl)<br/>- [Module model](https://github.com/Accord-Project/aec3po/blob/HEAD/src/model.ttl)<br/>- [Module rase&lowbar;statement](https://github.com/Accord-Project/aec3po/blob/HEAD/src/rase_statement.ttl)<br/>- [Module statement](https://github.com/Accord-Project/aec3po/blob/HEAD/src/statement.ttl)<br/>- [Module table](https://github.com/Accord-Project/aec3po/blob/HEAD/src/table.ttl)<br/>- [Module vocabularies/&lowbar;shape](https://github.com/Accord-Project/aec3po/blob/HEAD/src/vocabularies/_shape.ttl)<br/>- [Module vocabularies/administrative&lowbar;areas](https://github.com/Accord-Project/aec3po/blob/HEAD/src/vocabularies/administrative_areas.ttl)<br/>- [Module vocabularies/building&lowbar;structure](https://github.com/Accord-Project/aec3po/blob/HEAD/src/vocabularies/building_structure.ttl)<br/>- [Module vocabularies/building&lowbar;usage](https://github.com/Accord-Project/aec3po/blob/HEAD/src/vocabularies/building_usage.ttl)<br/>- [Module vocabularies/check&lowbar;method&lowbar;comparators](https://github.com/Accord-Project/aec3po/blob/HEAD/src/vocabularies/check_method_comparators.ttl)<br/>- [Module vocabularies/check&lowbar;method&lowbar;operators](https://github.com/Accord-Project/aec3po/blob/HEAD/src/vocabularies/check_method_operators.ttl)<br/>- [Module vocabularies/disciplines](https://github.com/Accord-Project/aec3po/blob/HEAD/src/vocabularies/disciplines.ttl)<br/>- [Module vocabularies/permitting&lowbar;stages](https://github.com/Accord-Project/aec3po/blob/HEAD/src/vocabularies/permitting_stages.ttl)<br/>- [Module vocabularies/quantity&lowbar;kinds](https://github.com/Accord-Project/aec3po/blob/HEAD/src/vocabularies/quantity_kinds.ttl)|

#### Criterion detail
|Identifier|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|
|----|----|
|Title|Profile&#32;compatibility&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;check&#32;whether&#32;the&#32;test&#32;subject&#32;is&#32;compatible&#32;with&#32;a&#32;profile&#32;or&#32;not,&#32;and&#32;if&#32;it&#32;is&#32;not,&#32;why.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-150)|Identifier|`owl-ql-profile-error`|
|[Section top](#minorfail-outcome-number-150)|Title|OWL&#32;QL&#32;Profile&#32;incompatible|
|[Section top](#minorfail-outcome-number-150)|Description|Class&#32;Expression&#32;not&#32;supported&#32;with&#32;rdfs:subClassOf|
|[Section top](#minorfail-outcome-number-150)|Pointer|<pre lang="Turtle"><code>aec3po:AndCheckStatement&#32;a&#32;owl:Class&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;And&#32;Check&#32;Statement&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;Check&#32;verified&#32;if&#32;and&#32;only&#32;if&#32;all&#32;of&#32;its&#32;sub-checks&#32;are&#32;veri...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32;aec3po:statement&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:subClassOf&#32; &#91;&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:onProperty&#32;aec3po:hasSubdivision&#32;],  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;aec3po:ChecklistStatement&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-150)|Pointer|<pre lang="Turtle"><code>aec3po:ComplianceVerificationReport&#32;a&#32;owl:Class&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;Compliance&#32;Verification&#32;Report&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;Result&#32;of&#32;a&#32;checking&#32;act.&#32;May&#32;be&#32;compliant&#32;or&#32;not.&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32;aec3po:compliance&lowbar;verification&lowbar;report&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:subClassOf&#32; &#91;&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:onProperty&#32;aec3po:conforms&#32;]&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-150)|Pointer|<pre lang="Turtle"><code>aec3po:DocumentSubdivision&#32;a&#32;owl:Class&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;Document&#32;Subdivision&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;Any&#32;subdivision&#32;of&#32;a&#32;document,&#32;including&#32;sections,&#32;paragraph...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32;aec3po:document&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:subClassOf&#32; &#91;&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:allValuesFrom&#32;aec3po:DocumentSubdivision&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:onProperty&#32;aec3po:hasSubdivision&#32;]&#32;;  &#10; &#32; &#32; &#32; &#32;skos:example&#32; &#34;Paragraph,&#32;section,&#32;definition...&#34;@en&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-150)|Pointer|<pre lang="Turtle"><code>aec3po:LegalVerifier&#32;a&#32;owl:Class&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;Legal&#32;Verifier&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;An&#32;entity&#32;that&#32;has&#32;the&#32;legal&#32;capacity&#32;to&#32;verify&#32;compliance&#32;w...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32;aec3po:legal&lowbar;verifier&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:subClassOf&#32; &#91;&#32;owl:allValuesFrom&#32;aec3po:Document&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:onProperty&#32;aec3po:forDocument&#32;],  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;foaf:Agent&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-150)|Pointer|<pre lang="Turtle"><code>aec3po:NotCheckStatement&#32;a&#32;owl:Class&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;Not&#32;Check&#32;Statement&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;Check&#32;verified&#32;if&#32;and&#32;only&#32;if&#32;the&#32;sub-check&#32;is&#32;not&#32;verified.&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32;aec3po:statement&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:subClassOf&#32; &#91;&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:onProperty&#32;aec3po:hasSubdivision&#32;]&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-150)|Pointer|<pre lang="Turtle"><code>aec3po:OrCheckStatement&#32;a&#32;owl:Class&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;Or&#32;Check&#32;Statement&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;Check&#32;verified&#32;if&#32;and&#32;only&#32;if&#32;at&#32;least&#32;one&#32;of&#32;its&#32;sub-checks...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32;aec3po:statement&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:subClassOf&#32; &#91;&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:onProperty&#32;aec3po:hasSubdivision&#32;],  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;aec3po:ChecklistStatement&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-150)|Pointer|<pre lang="Turtle"><code>aec3po:VerificationResult&#32;a&#32;owl:Class&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;Verification&#32;Result&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;Individual&#32;verification&#32;result&#32;of&#32;a&#32;Compliance&#32;Verification&#32;...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32;aec3po:compliance&lowbar;verification&lowbar;report&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:subClassOf&#32; &#91;&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:onProperty&#32;aec3po:verificationFocus&#32;],  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#91;&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:onProperty&#32;aec3po:hasSeverity&#32;]&#32;.</code></pre>|

***
### MinorFail Outcome number 151

[Jump to summary definition](#summary-MinorFail-151)	|	[Previous MinorFail outcome](#minorfail-outcome-number-150)	|	[Next MinorFail outcome](#minorfail-outcome-number-152)

:exclamation:MinorFail outcome
#### Subject detail
|Name|all-fragments|
|----|----|
|Title|All&#32;the&#32;fragments&#32;from&#32;branch&#32;HEAD&#32;that&#32;are&#32;syntaxically&#32;correct&#32;as&#32;well&#32;as&#32;their&#32;recursive&#32;imports|
|Composition|- [Module aec3po](https://github.com/Accord-Project/aec3po/blob/HEAD/src/aec3po.ttl)<br/>- [Module check&lowbar;method](https://github.com/Accord-Project/aec3po/blob/HEAD/src/check_method.ttl)<br/>- [Module checking&lowbar;act](https://github.com/Accord-Project/aec3po/blob/HEAD/src/checking_act.ttl)<br/>- [Module compliance&lowbar;verification&lowbar;report](https://github.com/Accord-Project/aec3po/blob/HEAD/src/compliance_verification_report.ttl)<br/>- [Module data&lowbar;requirement](https://github.com/Accord-Project/aec3po/blob/HEAD/src/data_requirement.ttl)<br/>- [Module document](https://github.com/Accord-Project/aec3po/blob/HEAD/src/document.ttl)<br/>- [Module evidence](https://github.com/Accord-Project/aec3po/blob/HEAD/src/evidence.ttl)<br/>- [Module feature&lowbar;of&lowbar;interest](https://github.com/Accord-Project/aec3po/blob/HEAD/src/feature_of_interest.ttl)<br/>- [Module legal&lowbar;verifier](https://github.com/Accord-Project/aec3po/blob/HEAD/src/legal_verifier.ttl)<br/>- [Module model](https://github.com/Accord-Project/aec3po/blob/HEAD/src/model.ttl)<br/>- [Module rase&lowbar;statement](https://github.com/Accord-Project/aec3po/blob/HEAD/src/rase_statement.ttl)<br/>- [Module statement](https://github.com/Accord-Project/aec3po/blob/HEAD/src/statement.ttl)<br/>- [Module table](https://github.com/Accord-Project/aec3po/blob/HEAD/src/table.ttl)<br/>- [Module vocabularies/&lowbar;shape](https://github.com/Accord-Project/aec3po/blob/HEAD/src/vocabularies/_shape.ttl)<br/>- [Module vocabularies/administrative&lowbar;areas](https://github.com/Accord-Project/aec3po/blob/HEAD/src/vocabularies/administrative_areas.ttl)<br/>- [Module vocabularies/building&lowbar;structure](https://github.com/Accord-Project/aec3po/blob/HEAD/src/vocabularies/building_structure.ttl)<br/>- [Module vocabularies/building&lowbar;usage](https://github.com/Accord-Project/aec3po/blob/HEAD/src/vocabularies/building_usage.ttl)<br/>- [Module vocabularies/check&lowbar;method&lowbar;comparators](https://github.com/Accord-Project/aec3po/blob/HEAD/src/vocabularies/check_method_comparators.ttl)<br/>- [Module vocabularies/check&lowbar;method&lowbar;operators](https://github.com/Accord-Project/aec3po/blob/HEAD/src/vocabularies/check_method_operators.ttl)<br/>- [Module vocabularies/disciplines](https://github.com/Accord-Project/aec3po/blob/HEAD/src/vocabularies/disciplines.ttl)<br/>- [Module vocabularies/permitting&lowbar;stages](https://github.com/Accord-Project/aec3po/blob/HEAD/src/vocabularies/permitting_stages.ttl)<br/>- [Module vocabularies/quantity&lowbar;kinds](https://github.com/Accord-Project/aec3po/blob/HEAD/src/vocabularies/quantity_kinds.ttl)|

#### Criterion detail
|Identifier|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|
|----|----|
|Title|Profile&#32;compatibility&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;check&#32;whether&#32;the&#32;test&#32;subject&#32;is&#32;compatible&#32;with&#32;a&#32;profile&#32;or&#32;not,&#32;and&#32;if&#32;it&#32;is&#32;not,&#32;why.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-151)|Identifier|`owl-ql-profile-error`|
|[Section top](#minorfail-outcome-number-151)|Title|OWL&#32;QL&#32;Profile&#32;incompatible|
|[Section top](#minorfail-outcome-number-151)|Description|Restriction&#32;on&#32;datatypes|
|[Section top](#minorfail-outcome-number-151)|Pointer|<pre lang="Turtle"><code>aec3po:conforms&#32;a&#32;owl:DatatypeProperty&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;conforms&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;True&#32;if&#32;the&#32;Checking&#32;act&#32;confirms&#32;the&#32;check&#32;was&#32;validated,&#32;a...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:domain&#32;aec3po:ComplianceVerificationReport&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32;aec3po:compliance&lowbar;verification&lowbar;report&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:range&#32;xsd:boolean&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-151)|Pointer|<pre lang="Turtle"><code>aec3po:hasBooleanTarget&#32;a&#32;owl:DatatypeProperty&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;hasBooleanTarget&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;TBD&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:range&#32;xsd:boolean&#32;.</code></pre>|

***
### MinorFail Outcome number 152

[Jump to summary definition](#summary-MinorFail-152)	|	[Previous MinorFail outcome](#minorfail-outcome-number-151)	|	[Next MinorFail outcome](#minorfail-outcome-number-153)

:exclamation:MinorFail outcome
#### Subject detail
|Name|all-fragments|
|----|----|
|Title|All&#32;the&#32;fragments&#32;from&#32;branch&#32;HEAD&#32;that&#32;are&#32;syntaxically&#32;correct&#32;as&#32;well&#32;as&#32;their&#32;recursive&#32;imports|
|Composition|- [Module aec3po](https://github.com/Accord-Project/aec3po/blob/HEAD/src/aec3po.ttl)<br/>- [Module check&lowbar;method](https://github.com/Accord-Project/aec3po/blob/HEAD/src/check_method.ttl)<br/>- [Module checking&lowbar;act](https://github.com/Accord-Project/aec3po/blob/HEAD/src/checking_act.ttl)<br/>- [Module compliance&lowbar;verification&lowbar;report](https://github.com/Accord-Project/aec3po/blob/HEAD/src/compliance_verification_report.ttl)<br/>- [Module data&lowbar;requirement](https://github.com/Accord-Project/aec3po/blob/HEAD/src/data_requirement.ttl)<br/>- [Module document](https://github.com/Accord-Project/aec3po/blob/HEAD/src/document.ttl)<br/>- [Module evidence](https://github.com/Accord-Project/aec3po/blob/HEAD/src/evidence.ttl)<br/>- [Module feature&lowbar;of&lowbar;interest](https://github.com/Accord-Project/aec3po/blob/HEAD/src/feature_of_interest.ttl)<br/>- [Module legal&lowbar;verifier](https://github.com/Accord-Project/aec3po/blob/HEAD/src/legal_verifier.ttl)<br/>- [Module model](https://github.com/Accord-Project/aec3po/blob/HEAD/src/model.ttl)<br/>- [Module rase&lowbar;statement](https://github.com/Accord-Project/aec3po/blob/HEAD/src/rase_statement.ttl)<br/>- [Module statement](https://github.com/Accord-Project/aec3po/blob/HEAD/src/statement.ttl)<br/>- [Module table](https://github.com/Accord-Project/aec3po/blob/HEAD/src/table.ttl)<br/>- [Module vocabularies/&lowbar;shape](https://github.com/Accord-Project/aec3po/blob/HEAD/src/vocabularies/_shape.ttl)<br/>- [Module vocabularies/administrative&lowbar;areas](https://github.com/Accord-Project/aec3po/blob/HEAD/src/vocabularies/administrative_areas.ttl)<br/>- [Module vocabularies/building&lowbar;structure](https://github.com/Accord-Project/aec3po/blob/HEAD/src/vocabularies/building_structure.ttl)<br/>- [Module vocabularies/building&lowbar;usage](https://github.com/Accord-Project/aec3po/blob/HEAD/src/vocabularies/building_usage.ttl)<br/>- [Module vocabularies/check&lowbar;method&lowbar;comparators](https://github.com/Accord-Project/aec3po/blob/HEAD/src/vocabularies/check_method_comparators.ttl)<br/>- [Module vocabularies/check&lowbar;method&lowbar;operators](https://github.com/Accord-Project/aec3po/blob/HEAD/src/vocabularies/check_method_operators.ttl)<br/>- [Module vocabularies/disciplines](https://github.com/Accord-Project/aec3po/blob/HEAD/src/vocabularies/disciplines.ttl)<br/>- [Module vocabularies/permitting&lowbar;stages](https://github.com/Accord-Project/aec3po/blob/HEAD/src/vocabularies/permitting_stages.ttl)<br/>- [Module vocabularies/quantity&lowbar;kinds](https://github.com/Accord-Project/aec3po/blob/HEAD/src/vocabularies/quantity_kinds.ttl)|

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
|[Section top](#minorfail-outcome-number-152)|Description|Statement&#32;not&#32;supported&#32;in&#32;a&#32;Sub&#32;Class&#32;Expression|
|[Section top](#minorfail-outcome-number-152)|Pointer|<pre lang="Turtle"><code>&#91;]&#32;a&#32;owl:Class&#32;;  &#10; &#32; &#32; &#32; &#32;owl:intersectionOf&#32;(&#32;aec3po:CheckMethod&#32; &#91;&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:allValuesFrom&#32; &#91;&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:allValuesFrom&#32;aec3po:FeatureOfInterest&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:onProperty&#32; &#91;&#32;owl:inverseOf&#32;aec3po:forDesign&#32;]&#32;]&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:onProperty&#32;aec3po:forDesign&#32;]&#32;)&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-152)|Pointer|<pre lang="Turtle"><code>&#91;]&#32;owl:intersectionOf&#32;(&#32;skos:Concept&#32; &#91;&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:hasValue&#32;aec3po:AdministrativeAreaNomenclature&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:onProperty&#32;skos:inScheme&#32;]&#32;)&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-152)|Pointer|<pre lang="Turtle"><code>&#91;]&#32;owl:intersectionOf&#32;(&#32;skos:Concept&#32; &#91;&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:hasValue&#32;aec3po:BuildingStructureNomenclature&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:onProperty&#32;skos:inScheme&#32;]&#32;)&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-152)|Pointer|<pre lang="Turtle"><code>&#91;]&#32;owl:intersectionOf&#32;(&#32;skos:Concept&#32; &#91;&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:hasValue&#32;aec3po:BuildingUsageNomenclature&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:onProperty&#32;skos:inScheme&#32;]&#32;)&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-152)|Pointer|<pre lang="Turtle"><code>&#91;]&#32;owl:intersectionOf&#32;(&#32;skos:Concept&#32; &#91;&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:hasValue&#32;aec3po:CheckMethodComparatorNomenclature&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:onProperty&#32;skos:inScheme&#32;]&#32;)&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-152)|Pointer|<pre lang="Turtle"><code>&#91;]&#32;owl:intersectionOf&#32;(&#32;skos:Concept&#32; &#91;&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:hasValue&#32;aec3po:CheckMethodOperatorNomenclature&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:onProperty&#32;skos:inScheme&#32;]&#32;)&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-152)|Pointer|<pre lang="Turtle"><code>&#91;]&#32;owl:intersectionOf&#32;(&#32;skos:Concept&#32; &#91;&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:hasValue&#32;aec3po:DisciplineNomenclature&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:onProperty&#32;skos:inScheme&#32;]&#32;)&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-152)|Pointer|<pre lang="Turtle"><code>&#91;]&#32;owl:intersectionOf&#32;(&#32;skos:Concept&#32; &#91;&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:hasValue&#32;aec3po:PermittingStageNomenclature&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:onProperty&#32;skos:inScheme&#32;]&#32;)&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-152)|Pointer|<pre lang="Turtle"><code>&#91;]&#32;owl:intersectionOf&#32;(&#32;skos:Concept&#32; &#91;&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:hasValue&#32;aec3po:QuantityKindNomenclature&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:onProperty&#32;skos:inScheme&#32;]&#32;)&#32;.</code></pre>|

***
### MinorFail Outcome number 153

[Jump to summary definition](#summary-MinorFail-153)	|	[Previous MinorFail outcome](#minorfail-outcome-number-152)	|	[Next MinorFail outcome](#minorfail-outcome-number-154)

:exclamation:MinorFail outcome
#### Subject detail
|Name|all-fragments|
|----|----|
|Title|All&#32;the&#32;fragments&#32;from&#32;branch&#32;HEAD&#32;that&#32;are&#32;syntaxically&#32;correct&#32;as&#32;well&#32;as&#32;their&#32;recursive&#32;imports|
|Composition|- [Module aec3po](https://github.com/Accord-Project/aec3po/blob/HEAD/src/aec3po.ttl)<br/>- [Module check&lowbar;method](https://github.com/Accord-Project/aec3po/blob/HEAD/src/check_method.ttl)<br/>- [Module checking&lowbar;act](https://github.com/Accord-Project/aec3po/blob/HEAD/src/checking_act.ttl)<br/>- [Module compliance&lowbar;verification&lowbar;report](https://github.com/Accord-Project/aec3po/blob/HEAD/src/compliance_verification_report.ttl)<br/>- [Module data&lowbar;requirement](https://github.com/Accord-Project/aec3po/blob/HEAD/src/data_requirement.ttl)<br/>- [Module document](https://github.com/Accord-Project/aec3po/blob/HEAD/src/document.ttl)<br/>- [Module evidence](https://github.com/Accord-Project/aec3po/blob/HEAD/src/evidence.ttl)<br/>- [Module feature&lowbar;of&lowbar;interest](https://github.com/Accord-Project/aec3po/blob/HEAD/src/feature_of_interest.ttl)<br/>- [Module legal&lowbar;verifier](https://github.com/Accord-Project/aec3po/blob/HEAD/src/legal_verifier.ttl)<br/>- [Module model](https://github.com/Accord-Project/aec3po/blob/HEAD/src/model.ttl)<br/>- [Module rase&lowbar;statement](https://github.com/Accord-Project/aec3po/blob/HEAD/src/rase_statement.ttl)<br/>- [Module statement](https://github.com/Accord-Project/aec3po/blob/HEAD/src/statement.ttl)<br/>- [Module table](https://github.com/Accord-Project/aec3po/blob/HEAD/src/table.ttl)<br/>- [Module vocabularies/&lowbar;shape](https://github.com/Accord-Project/aec3po/blob/HEAD/src/vocabularies/_shape.ttl)<br/>- [Module vocabularies/administrative&lowbar;areas](https://github.com/Accord-Project/aec3po/blob/HEAD/src/vocabularies/administrative_areas.ttl)<br/>- [Module vocabularies/building&lowbar;structure](https://github.com/Accord-Project/aec3po/blob/HEAD/src/vocabularies/building_structure.ttl)<br/>- [Module vocabularies/building&lowbar;usage](https://github.com/Accord-Project/aec3po/blob/HEAD/src/vocabularies/building_usage.ttl)<br/>- [Module vocabularies/check&lowbar;method&lowbar;comparators](https://github.com/Accord-Project/aec3po/blob/HEAD/src/vocabularies/check_method_comparators.ttl)<br/>- [Module vocabularies/check&lowbar;method&lowbar;operators](https://github.com/Accord-Project/aec3po/blob/HEAD/src/vocabularies/check_method_operators.ttl)<br/>- [Module vocabularies/disciplines](https://github.com/Accord-Project/aec3po/blob/HEAD/src/vocabularies/disciplines.ttl)<br/>- [Module vocabularies/permitting&lowbar;stages](https://github.com/Accord-Project/aec3po/blob/HEAD/src/vocabularies/permitting_stages.ttl)<br/>- [Module vocabularies/quantity&lowbar;kinds](https://github.com/Accord-Project/aec3po/blob/HEAD/src/vocabularies/quantity_kinds.ttl)|

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
|[Section top](#minorfail-outcome-number-153)|Description|Statement&#32;not&#32;supported&#32;in&#32;a&#32;Super&#32;Class&#32;Expression|
|[Section top](#minorfail-outcome-number-153)|Pointer|<pre lang="Turtle"><code>&#91;]&#32;a&#32;owl:Class&#32;;  &#10; &#32; &#32;&#32; &#32;owl:unionOf&#32;(&#32;aec3po:FeatureOfInterest&#32;aec3po:Property&#32;aec3po:CheckMethod&#32;)&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-153)|Pointer|<pre lang="Turtle"><code>&#91;]&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32;&#32; &#32;owl:onProperty&#32;aec3po:conforms&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-153)|Pointer|<pre lang="Turtle"><code>&#91;]&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32;&#32; &#32;owl:onProperty&#32;aec3po:verificationFocus&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-153)|Pointer|<pre lang="Turtle"><code>&#91;]&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32;&#32; &#32;owl:onProperty&#32;aec3po:hasSeverity&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-153)|Pointer|<pre lang="Turtle"><code>&#91;]&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32;owl:allValuesFrom&#32;aec3po:DocumentSubdivision&#32;;  &#10; &#32; &#32; &#32; &#32;owl:onProperty&#32;aec3po:hasSubdivision&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-153)|Pointer|<pre lang="Turtle"><code>&#91;]&#32;owl:unionOf&#32;(&#32;aec3po:Document&#32;aec3po:DocumentSubdivision&#32;)&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-153)|Pointer|<pre lang="Turtle"><code>&#91;]&#32;owl:allValuesFrom&#32;aec3po:Document&#32;;  &#10; &#32; &#32;&#32; &#32;owl:onProperty&#32;aec3po:forDocument&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-153)|Pointer|<pre lang="Turtle"><code>&#91;]&#32;a&#32;owl:Class&#32;;  &#10; &#32; &#32;&#32; &#32;owl:unionOf&#32;(&#32; &#60;https://schema.org/Place> &#32;aec3po:AdministrativeArea&#32;)&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-153)|Pointer|<pre lang="Turtle"><code>&#91;]&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32;&#32; &#32;owl:onProperty&#32;aec3po:hasSubdivision&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-153)|Pointer|<pre lang="Turtle"><code>&#91;]&#32;a&#32;owl:Class&#32;;  &#10; &#32; &#32;&#32; &#32;owl:unionOf&#32;(&#32;aec3po:Table&#32;aec3po:Image&#32;aec3po:Row&#32;aec3po:Column&#32;)&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-153)|Pointer|<pre lang="Turtle"><code>&#91;]&#32;a&#32;owl:Class&#32;;  &#10; &#32; &#32;&#32; &#32;owl:unionOf&#32;(&#32;aec3po:Table&#32;aec3po:Image&#32;aec3po:Row&#32;aec3po:Column&#32;aec3po:Cell&#32;)&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-153)|Pointer|<pre lang="Turtle"><code>&#91;]&#32;a&#32;owl:Class&#32;;  &#10; &#32; &#32;&#32; &#32;owl:unionOf&#32;(&#32;aec3po:Table&#32;aec3po:Image&#32;)&#32;.</code></pre>|

***
### MinorFail Outcome number 154

[Jump to summary definition](#summary-MinorFail-154)	|	[Previous MinorFail outcome](#minorfail-outcome-number-153)	|	[Next MinorFail outcome](#minorfail-outcome-number-155)

:exclamation:MinorFail outcome
#### Subject detail
|Name|all-fragments|
|----|----|
|Title|All&#32;the&#32;fragments&#32;from&#32;branch&#32;HEAD&#32;that&#32;are&#32;syntaxically&#32;correct&#32;as&#32;well&#32;as&#32;their&#32;recursive&#32;imports|
|Composition|- [Module aec3po](https://github.com/Accord-Project/aec3po/blob/HEAD/src/aec3po.ttl)<br/>- [Module check&lowbar;method](https://github.com/Accord-Project/aec3po/blob/HEAD/src/check_method.ttl)<br/>- [Module checking&lowbar;act](https://github.com/Accord-Project/aec3po/blob/HEAD/src/checking_act.ttl)<br/>- [Module compliance&lowbar;verification&lowbar;report](https://github.com/Accord-Project/aec3po/blob/HEAD/src/compliance_verification_report.ttl)<br/>- [Module data&lowbar;requirement](https://github.com/Accord-Project/aec3po/blob/HEAD/src/data_requirement.ttl)<br/>- [Module document](https://github.com/Accord-Project/aec3po/blob/HEAD/src/document.ttl)<br/>- [Module evidence](https://github.com/Accord-Project/aec3po/blob/HEAD/src/evidence.ttl)<br/>- [Module feature&lowbar;of&lowbar;interest](https://github.com/Accord-Project/aec3po/blob/HEAD/src/feature_of_interest.ttl)<br/>- [Module legal&lowbar;verifier](https://github.com/Accord-Project/aec3po/blob/HEAD/src/legal_verifier.ttl)<br/>- [Module model](https://github.com/Accord-Project/aec3po/blob/HEAD/src/model.ttl)<br/>- [Module rase&lowbar;statement](https://github.com/Accord-Project/aec3po/blob/HEAD/src/rase_statement.ttl)<br/>- [Module statement](https://github.com/Accord-Project/aec3po/blob/HEAD/src/statement.ttl)<br/>- [Module table](https://github.com/Accord-Project/aec3po/blob/HEAD/src/table.ttl)<br/>- [Module vocabularies/&lowbar;shape](https://github.com/Accord-Project/aec3po/blob/HEAD/src/vocabularies/_shape.ttl)<br/>- [Module vocabularies/administrative&lowbar;areas](https://github.com/Accord-Project/aec3po/blob/HEAD/src/vocabularies/administrative_areas.ttl)<br/>- [Module vocabularies/building&lowbar;structure](https://github.com/Accord-Project/aec3po/blob/HEAD/src/vocabularies/building_structure.ttl)<br/>- [Module vocabularies/building&lowbar;usage](https://github.com/Accord-Project/aec3po/blob/HEAD/src/vocabularies/building_usage.ttl)<br/>- [Module vocabularies/check&lowbar;method&lowbar;comparators](https://github.com/Accord-Project/aec3po/blob/HEAD/src/vocabularies/check_method_comparators.ttl)<br/>- [Module vocabularies/check&lowbar;method&lowbar;operators](https://github.com/Accord-Project/aec3po/blob/HEAD/src/vocabularies/check_method_operators.ttl)<br/>- [Module vocabularies/disciplines](https://github.com/Accord-Project/aec3po/blob/HEAD/src/vocabularies/disciplines.ttl)<br/>- [Module vocabularies/permitting&lowbar;stages](https://github.com/Accord-Project/aec3po/blob/HEAD/src/vocabularies/permitting_stages.ttl)<br/>- [Module vocabularies/quantity&lowbar;kinds](https://github.com/Accord-Project/aec3po/blob/HEAD/src/vocabularies/quantity_kinds.ttl)|

#### Criterion detail
|Identifier|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|
|----|----|
|Title|Profile&#32;compatibility&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;check&#32;whether&#32;the&#32;test&#32;subject&#32;is&#32;compatible&#32;with&#32;a&#32;profile&#32;or&#32;not,&#32;and&#32;if&#32;it&#32;is&#32;not,&#32;why.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-154)|Identifier|`owl-rl-profile-error`|
|[Section top](#minorfail-outcome-number-154)|Title|OWL&#32;RL&#32;Profile&#32;incompatible|
|[Section top](#minorfail-outcome-number-154)|Description|Class&#32;Expression&#32;not&#32;supported&#32;as&#32;object&#32;of&#32;rdfs:domain&#32;or&#32;rdfs:range|
|[Section top](#minorfail-outcome-number-154)|Pointer|<pre lang="Turtle"><code>aec3po:caption&#32;a&#32;owl:DatatypeProperty&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;caption&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;The&#32;caption&#32;of&#32;a&#32;table,&#32;image,&#32;etc.&#32; &#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:domain&#32; &#91;&#32;a&#32;owl:Class&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:unionOf&#32;(&#32;aec3po:Table&#32;aec3po:Image&#32;)&#32;]&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32;aec3po:table&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-154)|Pointer|<pre lang="Turtle"><code>aec3po:contains&#32;a&#32;owl:ObjectProperty&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;Contains&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;A&#32;container&#32;contains&#32;a&#32;table&#32;and&#32;its&#32;caption.&#32;A&#32;table&#32;contai...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:domain&#32; &#91;&#32;a&#32;owl:Class&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:unionOf&#32;(&#32;aec3po:Table&#32;aec3po:Image&#32;aec3po:Row&#32;aec3po:Column&#32;)&#32;]&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32;aec3po:table&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-154)|Pointer|<pre lang="Turtle"><code>aec3po:hasBSSDDTarget&#32;a&#32;owl:FunctionalProperty,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:ObjectProperty&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;hasBSSDDTarget&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;The&#32;target&#32;refers&#32;to&#32;either&#32;the&#32;name&#32;of&#32;an&#32;object,&#32;the&#32;name&#32;...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:domain&#32; &#91;&#32;a&#32;owl:Class&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:unionOf&#32;(&#32;aec3po:FeatureOfInterest&#32;aec3po:Property&#32;aec3po:CheckMethod&#32;)&#32;]&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32;aec3po:check&lowbar;method&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-154)|Pointer|<pre lang="Turtle"><code>aec3po:hasFirstSubdivision&#32;a&#32;owl:FunctionalProperty,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:ObjectProperty&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;has&#32;first&#32;subdivision&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;Links&#32;a&#32;document&#32;part&#32;to&#32;the&#32;first&#32;of&#32;its&#32;subdivision&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:domain&#32; &#91;&#32;owl:unionOf&#32;(&#32;aec3po:Document&#32;aec3po:DocumentSubdivision&#32;)&#32;]&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32;aec3po:document&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:range&#32;aec3po:DocumentSubdivision&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:subPropertyOf&#32;aec3po:hasSubdivision&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-154)|Pointer|<pre lang="Turtle"><code>aec3po:hasSubdivision&#32;a&#32;owl:ObjectProperty&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;has&#32;subdivision&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;links&#32;a&#32;document&#32;part&#32;to&#32;some&#32;of&#32;its&#32;subdivision&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:domain&#32; &#91;&#32;owl:unionOf&#32;(&#32;aec3po:Document&#32;aec3po:DocumentSubdivision&#32;)&#32;]&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32;aec3po:document&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:range&#32;aec3po:DocumentSubdivision&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:subPropertyOf&#32;dc:hasPart&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-154)|Pointer|<pre lang="Turtle"><code>aec3po:hasUnit&#32;a&#32;owl:FunctionalProperty,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:ObjectProperty&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;hasUnit&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;the&#32;hasUnit&#32;property&#32;is&#32;used&#32;to&#32;link&#32;a&#32;specific&#32;property&#32;or&#32;...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:domain&#32; &#91;&#32;a&#32;owl:Class&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:unionOf&#32;(&#32;aec3po:FeatureOfInterest&#32;aec3po:Property&#32;aec3po:CheckMethod&#32;)&#32;]&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32;aec3po:check&lowbar;method&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:range&#32;qudt:Unit&#32;;  &#10; &#32; &#32; &#32; &#32;owl:eqivalentProperty&#32;qudt:hasValue&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-154)|Pointer|<pre lang="Turtle"><code>aec3po:hasValue&#32;a&#32;owl:DatatypeProperty,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:FunctionalProperty&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;has&#32;value&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;de&#32;facto&#32;used&#32;to&#32;link&#32;something&#32;(anything:&#32;property,&#32;propert...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:domain&#32; &#91;&#32;a&#32;owl:Class&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:unionOf&#32;(&#32;aec3po:FeatureOfInterest&#32;aec3po:Property&#32;aec3po:CheckMethod&#32;)&#32;]&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32;aec3po:&#32;;  &#10; &#32; &#32; &#32; &#32;skos:note&#32; &#34;The&#32;value&#32;of&#32;the&#32;literal&#32;may&#32;be&#32;a&#32;XSD&#32;literal&#32;(boolean,&#32;inte...&#34; &#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-154)|Pointer|<pre lang="Turtle"><code>aec3po:isContainedIn&#32;a&#32;owl:ObjectProperty&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;is&#32;contained&#32;by&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;A&#32;table&#32;contains&#32;row,&#32;columns&#32;and&#32;other&#32;elements.&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32;aec3po:table&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:range&#32; &#91;&#32;a&#32;owl:Class&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:unionOf&#32;(&#32;aec3po:Table&#32;aec3po:Image&#32;aec3po:Row&#32;aec3po:Column&#32;aec3po:Cell&#32;)&#32;]&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-154)|Pointer|<pre lang="Turtle"><code>aec3po:locationCoverage&#32;a&#32;owl:ObjectProperty&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;location&#32;coverage&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;The&#32;spatialCoverage&#32;indicates&#32;the&#32;place(s)&#32;or&#32;the&#32;administra...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:domain&#32; &#60;https://schema.org/Model> &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:range&#32; &#91;&#32;a&#32;owl:Class&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:unionOf&#32;(&#32; &#60;https://schema.org/Place> &#32;aec3po:AdministrativeArea&#32;)&#32;]&#32;;  &#10; &#32; &#32; &#32; &#32;owl:equivalentProperty&#32; &#60;https://schema.org/spatialCoverage> &#32;.</code></pre>|

***
### MinorFail Outcome number 155

[Jump to summary definition](#summary-MinorFail-155)	|	[Previous MinorFail outcome](#minorfail-outcome-number-154)	|	[Next MinorFail outcome](#minorfail-outcome-number-156)

:exclamation:MinorFail outcome
#### Subject detail
|Name|all-fragments|
|----|----|
|Title|All&#32;the&#32;fragments&#32;from&#32;branch&#32;HEAD&#32;that&#32;are&#32;syntaxically&#32;correct&#32;as&#32;well&#32;as&#32;their&#32;recursive&#32;imports|
|Composition|- [Module aec3po](https://github.com/Accord-Project/aec3po/blob/HEAD/src/aec3po.ttl)<br/>- [Module check&lowbar;method](https://github.com/Accord-Project/aec3po/blob/HEAD/src/check_method.ttl)<br/>- [Module checking&lowbar;act](https://github.com/Accord-Project/aec3po/blob/HEAD/src/checking_act.ttl)<br/>- [Module compliance&lowbar;verification&lowbar;report](https://github.com/Accord-Project/aec3po/blob/HEAD/src/compliance_verification_report.ttl)<br/>- [Module data&lowbar;requirement](https://github.com/Accord-Project/aec3po/blob/HEAD/src/data_requirement.ttl)<br/>- [Module document](https://github.com/Accord-Project/aec3po/blob/HEAD/src/document.ttl)<br/>- [Module evidence](https://github.com/Accord-Project/aec3po/blob/HEAD/src/evidence.ttl)<br/>- [Module feature&lowbar;of&lowbar;interest](https://github.com/Accord-Project/aec3po/blob/HEAD/src/feature_of_interest.ttl)<br/>- [Module legal&lowbar;verifier](https://github.com/Accord-Project/aec3po/blob/HEAD/src/legal_verifier.ttl)<br/>- [Module model](https://github.com/Accord-Project/aec3po/blob/HEAD/src/model.ttl)<br/>- [Module rase&lowbar;statement](https://github.com/Accord-Project/aec3po/blob/HEAD/src/rase_statement.ttl)<br/>- [Module statement](https://github.com/Accord-Project/aec3po/blob/HEAD/src/statement.ttl)<br/>- [Module table](https://github.com/Accord-Project/aec3po/blob/HEAD/src/table.ttl)<br/>- [Module vocabularies/&lowbar;shape](https://github.com/Accord-Project/aec3po/blob/HEAD/src/vocabularies/_shape.ttl)<br/>- [Module vocabularies/administrative&lowbar;areas](https://github.com/Accord-Project/aec3po/blob/HEAD/src/vocabularies/administrative_areas.ttl)<br/>- [Module vocabularies/building&lowbar;structure](https://github.com/Accord-Project/aec3po/blob/HEAD/src/vocabularies/building_structure.ttl)<br/>- [Module vocabularies/building&lowbar;usage](https://github.com/Accord-Project/aec3po/blob/HEAD/src/vocabularies/building_usage.ttl)<br/>- [Module vocabularies/check&lowbar;method&lowbar;comparators](https://github.com/Accord-Project/aec3po/blob/HEAD/src/vocabularies/check_method_comparators.ttl)<br/>- [Module vocabularies/check&lowbar;method&lowbar;operators](https://github.com/Accord-Project/aec3po/blob/HEAD/src/vocabularies/check_method_operators.ttl)<br/>- [Module vocabularies/disciplines](https://github.com/Accord-Project/aec3po/blob/HEAD/src/vocabularies/disciplines.ttl)<br/>- [Module vocabularies/permitting&lowbar;stages](https://github.com/Accord-Project/aec3po/blob/HEAD/src/vocabularies/permitting_stages.ttl)<br/>- [Module vocabularies/quantity&lowbar;kinds](https://github.com/Accord-Project/aec3po/blob/HEAD/src/vocabularies/quantity_kinds.ttl)|

#### Criterion detail
|Identifier|[profile-compatibility](https://ns.inria.fr/olivaw#profile-compatibility)|
|----|----|
|Title|Profile&#32;compatibility&#32;test|
|Description|A&#32;test&#32;meant&#32;to&#32;check&#32;whether&#32;the&#32;test&#32;subject&#32;is&#32;compatible&#32;with&#32;a&#32;profile&#32;or&#32;not,&#32;and&#32;if&#32;it&#32;is&#32;not,&#32;why.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-155)|Identifier|`owl-rl-profile-error`|
|[Section top](#minorfail-outcome-number-155)|Title|OWL&#32;RL&#32;Profile&#32;incompatible|
|[Section top](#minorfail-outcome-number-155)|Description|Class&#32;Expression&#32;not&#32;supported&#32;with&#32;owl:equivalentClass|
|[Section top](#minorfail-outcome-number-155)|Pointer|<pre lang="Turtle"><code>aec3po:ComponentCheckMethod&#32;a&#32;owl:Class&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;Component&#32;Check&#32;Method&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;Component&#32;check&#32;method&#32;refers&#32;to&#32;a&#32;process&#32;of&#32;inspecting&#32;and...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32;aec3po:check&lowbar;method&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:subClassOf&#32;aec3po:CheckMethod&#32;;  &#10; &#32; &#32; &#32; &#32;owl:equivalentClass&#32; &#91;&#32;a&#32;owl:Class&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:intersectionOf&#32;(&#32;aec3po:CheckMethod&#32; &#91;&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:allValuesFrom&#32; &#91;&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:allValuesFrom&#32;aec3po:FeatureOfInterest&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:onProperty&#32; &#91;&#32;owl:inverseOf&#32;aec3po:forDesign&#32;]&#32;]&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:onProperty&#32;aec3po:forDesign&#32;]&#32;)&#32;]&#32;.</code></pre>|

***
### MinorFail Outcome number 156

[Jump to summary definition](#summary-MinorFail-156)	|	[Previous MinorFail outcome](#minorfail-outcome-number-155)	|	[Next MinorFail outcome](#minorfail-outcome-number-157)

:exclamation:MinorFail outcome
#### Subject detail
|Name|all-fragments|
|----|----|
|Title|All&#32;the&#32;fragments&#32;from&#32;branch&#32;HEAD&#32;that&#32;are&#32;syntaxically&#32;correct&#32;as&#32;well&#32;as&#32;their&#32;recursive&#32;imports|
|Composition|- [Module aec3po](https://github.com/Accord-Project/aec3po/blob/HEAD/src/aec3po.ttl)<br/>- [Module check&lowbar;method](https://github.com/Accord-Project/aec3po/blob/HEAD/src/check_method.ttl)<br/>- [Module checking&lowbar;act](https://github.com/Accord-Project/aec3po/blob/HEAD/src/checking_act.ttl)<br/>- [Module compliance&lowbar;verification&lowbar;report](https://github.com/Accord-Project/aec3po/blob/HEAD/src/compliance_verification_report.ttl)<br/>- [Module data&lowbar;requirement](https://github.com/Accord-Project/aec3po/blob/HEAD/src/data_requirement.ttl)<br/>- [Module document](https://github.com/Accord-Project/aec3po/blob/HEAD/src/document.ttl)<br/>- [Module evidence](https://github.com/Accord-Project/aec3po/blob/HEAD/src/evidence.ttl)<br/>- [Module feature&lowbar;of&lowbar;interest](https://github.com/Accord-Project/aec3po/blob/HEAD/src/feature_of_interest.ttl)<br/>- [Module legal&lowbar;verifier](https://github.com/Accord-Project/aec3po/blob/HEAD/src/legal_verifier.ttl)<br/>- [Module model](https://github.com/Accord-Project/aec3po/blob/HEAD/src/model.ttl)<br/>- [Module rase&lowbar;statement](https://github.com/Accord-Project/aec3po/blob/HEAD/src/rase_statement.ttl)<br/>- [Module statement](https://github.com/Accord-Project/aec3po/blob/HEAD/src/statement.ttl)<br/>- [Module table](https://github.com/Accord-Project/aec3po/blob/HEAD/src/table.ttl)<br/>- [Module vocabularies/&lowbar;shape](https://github.com/Accord-Project/aec3po/blob/HEAD/src/vocabularies/_shape.ttl)<br/>- [Module vocabularies/administrative&lowbar;areas](https://github.com/Accord-Project/aec3po/blob/HEAD/src/vocabularies/administrative_areas.ttl)<br/>- [Module vocabularies/building&lowbar;structure](https://github.com/Accord-Project/aec3po/blob/HEAD/src/vocabularies/building_structure.ttl)<br/>- [Module vocabularies/building&lowbar;usage](https://github.com/Accord-Project/aec3po/blob/HEAD/src/vocabularies/building_usage.ttl)<br/>- [Module vocabularies/check&lowbar;method&lowbar;comparators](https://github.com/Accord-Project/aec3po/blob/HEAD/src/vocabularies/check_method_comparators.ttl)<br/>- [Module vocabularies/check&lowbar;method&lowbar;operators](https://github.com/Accord-Project/aec3po/blob/HEAD/src/vocabularies/check_method_operators.ttl)<br/>- [Module vocabularies/disciplines](https://github.com/Accord-Project/aec3po/blob/HEAD/src/vocabularies/disciplines.ttl)<br/>- [Module vocabularies/permitting&lowbar;stages](https://github.com/Accord-Project/aec3po/blob/HEAD/src/vocabularies/permitting_stages.ttl)<br/>- [Module vocabularies/quantity&lowbar;kinds](https://github.com/Accord-Project/aec3po/blob/HEAD/src/vocabularies/quantity_kinds.ttl)|

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
|[Section top](#minorfail-outcome-number-156)|Description|Class&#32;Expression&#32;not&#32;supported&#32;with&#32;owl:equivalentClass&#32;or&#32;owl:intersectionOf|
|[Section top](#minorfail-outcome-number-156)|Pointer|<pre lang="Turtle"><code>&#91;]&#32;a&#32;owl:Class&#32;;  &#10; &#32; &#32; &#32; &#32;owl:intersectionOf&#32;(&#32;aec3po:CheckMethod&#32; &#91;&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:allValuesFrom&#32; &#91;&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:allValuesFrom&#32;aec3po:FeatureOfInterest&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:onProperty&#32; &#91;&#32;owl:inverseOf&#32;aec3po:forDesign&#32;]&#32;]&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:onProperty&#32;aec3po:forDesign&#32;]&#32;)&#32;.</code></pre>|

***
### MinorFail Outcome number 157

[Jump to summary definition](#summary-MinorFail-157)	|	[Previous MinorFail outcome](#minorfail-outcome-number-156)	|	[Next MinorFail outcome](#minorfail-outcome-number-158)

:exclamation:MinorFail outcome
#### Subject detail
|Name|all-fragments|
|----|----|
|Title|All&#32;the&#32;fragments&#32;from&#32;branch&#32;HEAD&#32;that&#32;are&#32;syntaxically&#32;correct&#32;as&#32;well&#32;as&#32;their&#32;recursive&#32;imports|
|Composition|- [Module aec3po](https://github.com/Accord-Project/aec3po/blob/HEAD/src/aec3po.ttl)<br/>- [Module check&lowbar;method](https://github.com/Accord-Project/aec3po/blob/HEAD/src/check_method.ttl)<br/>- [Module checking&lowbar;act](https://github.com/Accord-Project/aec3po/blob/HEAD/src/checking_act.ttl)<br/>- [Module compliance&lowbar;verification&lowbar;report](https://github.com/Accord-Project/aec3po/blob/HEAD/src/compliance_verification_report.ttl)<br/>- [Module data&lowbar;requirement](https://github.com/Accord-Project/aec3po/blob/HEAD/src/data_requirement.ttl)<br/>- [Module document](https://github.com/Accord-Project/aec3po/blob/HEAD/src/document.ttl)<br/>- [Module evidence](https://github.com/Accord-Project/aec3po/blob/HEAD/src/evidence.ttl)<br/>- [Module feature&lowbar;of&lowbar;interest](https://github.com/Accord-Project/aec3po/blob/HEAD/src/feature_of_interest.ttl)<br/>- [Module legal&lowbar;verifier](https://github.com/Accord-Project/aec3po/blob/HEAD/src/legal_verifier.ttl)<br/>- [Module model](https://github.com/Accord-Project/aec3po/blob/HEAD/src/model.ttl)<br/>- [Module rase&lowbar;statement](https://github.com/Accord-Project/aec3po/blob/HEAD/src/rase_statement.ttl)<br/>- [Module statement](https://github.com/Accord-Project/aec3po/blob/HEAD/src/statement.ttl)<br/>- [Module table](https://github.com/Accord-Project/aec3po/blob/HEAD/src/table.ttl)<br/>- [Module vocabularies/&lowbar;shape](https://github.com/Accord-Project/aec3po/blob/HEAD/src/vocabularies/_shape.ttl)<br/>- [Module vocabularies/administrative&lowbar;areas](https://github.com/Accord-Project/aec3po/blob/HEAD/src/vocabularies/administrative_areas.ttl)<br/>- [Module vocabularies/building&lowbar;structure](https://github.com/Accord-Project/aec3po/blob/HEAD/src/vocabularies/building_structure.ttl)<br/>- [Module vocabularies/building&lowbar;usage](https://github.com/Accord-Project/aec3po/blob/HEAD/src/vocabularies/building_usage.ttl)<br/>- [Module vocabularies/check&lowbar;method&lowbar;comparators](https://github.com/Accord-Project/aec3po/blob/HEAD/src/vocabularies/check_method_comparators.ttl)<br/>- [Module vocabularies/check&lowbar;method&lowbar;operators](https://github.com/Accord-Project/aec3po/blob/HEAD/src/vocabularies/check_method_operators.ttl)<br/>- [Module vocabularies/disciplines](https://github.com/Accord-Project/aec3po/blob/HEAD/src/vocabularies/disciplines.ttl)<br/>- [Module vocabularies/permitting&lowbar;stages](https://github.com/Accord-Project/aec3po/blob/HEAD/src/vocabularies/permitting_stages.ttl)<br/>- [Module vocabularies/quantity&lowbar;kinds](https://github.com/Accord-Project/aec3po/blob/HEAD/src/vocabularies/quantity_kinds.ttl)|

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
|[Section top](#minorfail-outcome-number-157)|Pointer|<pre lang="Turtle"><code>aec3po:AndCheckStatement&#32;a&#32;owl:Class&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;And&#32;Check&#32;Statement&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;Check&#32;verified&#32;if&#32;and&#32;only&#32;if&#32;all&#32;of&#32;its&#32;sub-checks&#32;are&#32;veri...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32;aec3po:statement&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:subClassOf&#32; &#91;&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:onProperty&#32;aec3po:hasSubdivision&#32;],  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;aec3po:ChecklistStatement&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-157)|Pointer|<pre lang="Turtle"><code>aec3po:CheckingAct&#32;a&#32;owl:Class&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;Checking&#32;Act&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;Act&#32;of&#32;checking&#32;some&#32;entities&#32;for&#32;something&#32;and&#32;generating&#32;a...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32;aec3po:checking&lowbar;act&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:subClassOf&#32; &#91;&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:onProperty&#32;aec3po:usedMethod&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:someValuesFrom&#32;aec3po:CheckMethod&#32;],  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#91;&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:onProperty&#32;aec3po:madeBy&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:someValuesFrom&#32;aec3po:ProcessVerifier&#32;],  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#91;&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:onProperty&#32;aec3po:checked&#32;],  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#91;&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:onProperty&#32;aec3po:hasReport&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:someValuesFrom&#32;aec3po:ComplianceVerificationReport&#32;],  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#60;http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#Event> &#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-157)|Pointer|<pre lang="Turtle"><code>aec3po:ComplianceVerificationReport&#32;a&#32;owl:Class&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;Compliance&#32;Verification&#32;Report&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;Result&#32;of&#32;a&#32;checking&#32;act.&#32;May&#32;be&#32;compliant&#32;or&#32;not.&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32;aec3po:compliance&lowbar;verification&lowbar;report&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:subClassOf&#32; &#91;&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:onProperty&#32;aec3po:conforms&#32;]&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-157)|Pointer|<pre lang="Turtle"><code>aec3po:NotCheckStatement&#32;a&#32;owl:Class&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;Not&#32;Check&#32;Statement&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;Check&#32;verified&#32;if&#32;and&#32;only&#32;if&#32;the&#32;sub-check&#32;is&#32;not&#32;verified.&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32;aec3po:statement&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:subClassOf&#32; &#91;&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:onProperty&#32;aec3po:hasSubdivision&#32;]&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-157)|Pointer|<pre lang="Turtle"><code>aec3po:OrCheckStatement&#32;a&#32;owl:Class&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;Or&#32;Check&#32;Statement&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;Check&#32;verified&#32;if&#32;and&#32;only&#32;if&#32;at&#32;least&#32;one&#32;of&#32;its&#32;sub-checks...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32;aec3po:statement&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:subClassOf&#32; &#91;&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:onProperty&#32;aec3po:hasSubdivision&#32;],  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;aec3po:ChecklistStatement&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-157)|Pointer|<pre lang="Turtle"><code>aec3po:VerificationResult&#32;a&#32;owl:Class&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;Verification&#32;Result&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;Individual&#32;verification&#32;result&#32;of&#32;a&#32;Compliance&#32;Verification&#32;...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32;aec3po:compliance&lowbar;verification&lowbar;report&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:subClassOf&#32; &#91;&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:onProperty&#32;aec3po:verificationFocus&#32;],  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#91;&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:onProperty&#32;aec3po:hasSeverity&#32;]&#32;.</code></pre>|

***
### MinorFail Outcome number 158

[Jump to summary definition](#summary-MinorFail-158)	|	[Previous MinorFail outcome](#minorfail-outcome-number-157)	|	[Next MinorFail outcome](#minorfail-outcome-number-159)

:exclamation:MinorFail outcome
#### Subject detail
|Name|all-fragments|
|----|----|
|Title|All&#32;the&#32;fragments&#32;from&#32;branch&#32;HEAD&#32;that&#32;are&#32;syntaxically&#32;correct&#32;as&#32;well&#32;as&#32;their&#32;recursive&#32;imports|
|Composition|- [Module aec3po](https://github.com/Accord-Project/aec3po/blob/HEAD/src/aec3po.ttl)<br/>- [Module check&lowbar;method](https://github.com/Accord-Project/aec3po/blob/HEAD/src/check_method.ttl)<br/>- [Module checking&lowbar;act](https://github.com/Accord-Project/aec3po/blob/HEAD/src/checking_act.ttl)<br/>- [Module compliance&lowbar;verification&lowbar;report](https://github.com/Accord-Project/aec3po/blob/HEAD/src/compliance_verification_report.ttl)<br/>- [Module data&lowbar;requirement](https://github.com/Accord-Project/aec3po/blob/HEAD/src/data_requirement.ttl)<br/>- [Module document](https://github.com/Accord-Project/aec3po/blob/HEAD/src/document.ttl)<br/>- [Module evidence](https://github.com/Accord-Project/aec3po/blob/HEAD/src/evidence.ttl)<br/>- [Module feature&lowbar;of&lowbar;interest](https://github.com/Accord-Project/aec3po/blob/HEAD/src/feature_of_interest.ttl)<br/>- [Module legal&lowbar;verifier](https://github.com/Accord-Project/aec3po/blob/HEAD/src/legal_verifier.ttl)<br/>- [Module model](https://github.com/Accord-Project/aec3po/blob/HEAD/src/model.ttl)<br/>- [Module rase&lowbar;statement](https://github.com/Accord-Project/aec3po/blob/HEAD/src/rase_statement.ttl)<br/>- [Module statement](https://github.com/Accord-Project/aec3po/blob/HEAD/src/statement.ttl)<br/>- [Module table](https://github.com/Accord-Project/aec3po/blob/HEAD/src/table.ttl)<br/>- [Module vocabularies/&lowbar;shape](https://github.com/Accord-Project/aec3po/blob/HEAD/src/vocabularies/_shape.ttl)<br/>- [Module vocabularies/administrative&lowbar;areas](https://github.com/Accord-Project/aec3po/blob/HEAD/src/vocabularies/administrative_areas.ttl)<br/>- [Module vocabularies/building&lowbar;structure](https://github.com/Accord-Project/aec3po/blob/HEAD/src/vocabularies/building_structure.ttl)<br/>- [Module vocabularies/building&lowbar;usage](https://github.com/Accord-Project/aec3po/blob/HEAD/src/vocabularies/building_usage.ttl)<br/>- [Module vocabularies/check&lowbar;method&lowbar;comparators](https://github.com/Accord-Project/aec3po/blob/HEAD/src/vocabularies/check_method_comparators.ttl)<br/>- [Module vocabularies/check&lowbar;method&lowbar;operators](https://github.com/Accord-Project/aec3po/blob/HEAD/src/vocabularies/check_method_operators.ttl)<br/>- [Module vocabularies/disciplines](https://github.com/Accord-Project/aec3po/blob/HEAD/src/vocabularies/disciplines.ttl)<br/>- [Module vocabularies/permitting&lowbar;stages](https://github.com/Accord-Project/aec3po/blob/HEAD/src/vocabularies/permitting_stages.ttl)<br/>- [Module vocabularies/quantity&lowbar;kinds](https://github.com/Accord-Project/aec3po/blob/HEAD/src/vocabularies/quantity_kinds.ttl)|

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
|[Section top](#minorfail-outcome-number-158)|Description|Statement&#32;not&#32;supported&#32;in&#32;a&#32;Super&#32;Class&#32;Expression|
|[Section top](#minorfail-outcome-number-158)|Pointer|<pre lang="Turtle"><code>&#91;]&#32;a&#32;owl:Class&#32;;  &#10; &#32; &#32;&#32; &#32;owl:unionOf&#32;(&#32;aec3po:FeatureOfInterest&#32;aec3po:Property&#32;aec3po:CheckMethod&#32;)&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-158)|Pointer|<pre lang="Turtle"><code>&#91;]&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32;owl:onProperty&#32;aec3po:usedMethod&#32;;  &#10; &#32; &#32; &#32; &#32;owl:someValuesFrom&#32;aec3po:CheckMethod&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-158)|Pointer|<pre lang="Turtle"><code>&#91;]&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32;owl:onProperty&#32;aec3po:madeBy&#32;;  &#10; &#32; &#32; &#32; &#32;owl:someValuesFrom&#32;aec3po:ProcessVerifier&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-158)|Pointer|<pre lang="Turtle"><code>&#91;]&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32;&#32; &#32;owl:onProperty&#32;aec3po:checked&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-158)|Pointer|<pre lang="Turtle"><code>&#91;]&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32;owl:onProperty&#32;aec3po:hasReport&#32;;  &#10; &#32; &#32; &#32; &#32;owl:someValuesFrom&#32;aec3po:ComplianceVerificationReport&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-158)|Pointer|<pre lang="Turtle"><code>&#91;]&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32;&#32; &#32;owl:onProperty&#32;aec3po:conforms&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-158)|Pointer|<pre lang="Turtle"><code>&#91;]&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32;&#32; &#32;owl:onProperty&#32;aec3po:verificationFocus&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-158)|Pointer|<pre lang="Turtle"><code>&#91;]&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32;&#32; &#32;owl:onProperty&#32;aec3po:hasSeverity&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-158)|Pointer|<pre lang="Turtle"><code>&#91;]&#32;owl:unionOf&#32;(&#32;aec3po:Document&#32;aec3po:DocumentSubdivision&#32;)&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-158)|Pointer|<pre lang="Turtle"><code>&#91;]&#32;a&#32;owl:Class&#32;;  &#10; &#32; &#32;&#32; &#32;owl:unionOf&#32;(&#32; &#60;https://schema.org/Place> &#32;aec3po:AdministrativeArea&#32;)&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-158)|Pointer|<pre lang="Turtle"><code>&#91;]&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32;&#32; &#32;owl:onProperty&#32;aec3po:hasSubdivision&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-158)|Pointer|<pre lang="Turtle"><code>&#91;]&#32;a&#32;owl:Class&#32;;  &#10; &#32; &#32;&#32; &#32;owl:unionOf&#32;(&#32;aec3po:Table&#32;aec3po:Image&#32;aec3po:Row&#32;aec3po:Column&#32;)&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-158)|Pointer|<pre lang="Turtle"><code>&#91;]&#32;a&#32;owl:Class&#32;;  &#10; &#32; &#32;&#32; &#32;owl:unionOf&#32;(&#32;aec3po:Table&#32;aec3po:Image&#32;aec3po:Row&#32;aec3po:Column&#32;aec3po:Cell&#32;)&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-158)|Pointer|<pre lang="Turtle"><code>&#91;]&#32;a&#32;owl:Class&#32;;  &#10; &#32; &#32;&#32; &#32;owl:unionOf&#32;(&#32;aec3po:Table&#32;aec3po:Image&#32;)&#32;.</code></pre>|

***
### MinorFail Outcome number 159

[Jump to summary definition](#summary-MinorFail-159)	|	[Previous MinorFail outcome](#minorfail-outcome-number-158)	|	[Next MinorFail outcome](#minorfail-outcome-number-160)

:exclamation:MinorFail outcome
#### Subject detail
|Name|all-fragments|
|----|----|
|Title|All&#32;the&#32;fragments&#32;from&#32;branch&#32;HEAD&#32;that&#32;are&#32;syntaxically&#32;correct&#32;as&#32;well&#32;as&#32;their&#32;recursive&#32;imports|
|Composition|- [Module aec3po](https://github.com/Accord-Project/aec3po/blob/HEAD/src/aec3po.ttl)<br/>- [Module check&lowbar;method](https://github.com/Accord-Project/aec3po/blob/HEAD/src/check_method.ttl)<br/>- [Module checking&lowbar;act](https://github.com/Accord-Project/aec3po/blob/HEAD/src/checking_act.ttl)<br/>- [Module compliance&lowbar;verification&lowbar;report](https://github.com/Accord-Project/aec3po/blob/HEAD/src/compliance_verification_report.ttl)<br/>- [Module data&lowbar;requirement](https://github.com/Accord-Project/aec3po/blob/HEAD/src/data_requirement.ttl)<br/>- [Module document](https://github.com/Accord-Project/aec3po/blob/HEAD/src/document.ttl)<br/>- [Module evidence](https://github.com/Accord-Project/aec3po/blob/HEAD/src/evidence.ttl)<br/>- [Module feature&lowbar;of&lowbar;interest](https://github.com/Accord-Project/aec3po/blob/HEAD/src/feature_of_interest.ttl)<br/>- [Module legal&lowbar;verifier](https://github.com/Accord-Project/aec3po/blob/HEAD/src/legal_verifier.ttl)<br/>- [Module model](https://github.com/Accord-Project/aec3po/blob/HEAD/src/model.ttl)<br/>- [Module rase&lowbar;statement](https://github.com/Accord-Project/aec3po/blob/HEAD/src/rase_statement.ttl)<br/>- [Module statement](https://github.com/Accord-Project/aec3po/blob/HEAD/src/statement.ttl)<br/>- [Module table](https://github.com/Accord-Project/aec3po/blob/HEAD/src/table.ttl)<br/>- [Module vocabularies/&lowbar;shape](https://github.com/Accord-Project/aec3po/blob/HEAD/src/vocabularies/_shape.ttl)<br/>- [Module vocabularies/administrative&lowbar;areas](https://github.com/Accord-Project/aec3po/blob/HEAD/src/vocabularies/administrative_areas.ttl)<br/>- [Module vocabularies/building&lowbar;structure](https://github.com/Accord-Project/aec3po/blob/HEAD/src/vocabularies/building_structure.ttl)<br/>- [Module vocabularies/building&lowbar;usage](https://github.com/Accord-Project/aec3po/blob/HEAD/src/vocabularies/building_usage.ttl)<br/>- [Module vocabularies/check&lowbar;method&lowbar;comparators](https://github.com/Accord-Project/aec3po/blob/HEAD/src/vocabularies/check_method_comparators.ttl)<br/>- [Module vocabularies/check&lowbar;method&lowbar;operators](https://github.com/Accord-Project/aec3po/blob/HEAD/src/vocabularies/check_method_operators.ttl)<br/>- [Module vocabularies/disciplines](https://github.com/Accord-Project/aec3po/blob/HEAD/src/vocabularies/disciplines.ttl)<br/>- [Module vocabularies/permitting&lowbar;stages](https://github.com/Accord-Project/aec3po/blob/HEAD/src/vocabularies/permitting_stages.ttl)<br/>- [Module vocabularies/quantity&lowbar;kinds](https://github.com/Accord-Project/aec3po/blob/HEAD/src/vocabularies/quantity_kinds.ttl)|

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
|[Section top](#minorfail-outcome-number-159)|Description|Statement&#32;not&#32;supported&#32;in&#32;an&#32;Equivalent&#32;Class&#32;Expression|
|[Section top](#minorfail-outcome-number-159)|Pointer|<pre lang="Turtle"><code>&#91;]&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32;owl:allValuesFrom&#32; &#91;&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:allValuesFrom&#32;aec3po:FeatureOfInterest&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:onProperty&#32; &#91;&#32;owl:inverseOf&#32;aec3po:forDesign&#32;]&#32;]&#32;;  &#10; &#32; &#32; &#32; &#32;owl:onProperty&#32;aec3po:forDesign&#32;.</code></pre>|

***
### MinorFail Outcome number 160

[Jump to summary definition](#summary-MinorFail-160)	|	[Previous MinorFail outcome](#minorfail-outcome-number-159)	|	[Next MinorFail outcome](#minorfail-outcome-number-161)

:exclamation:MinorFail outcome
#### Subject detail
|Name|all-fragments|
|----|----|
|Title|All&#32;the&#32;fragments&#32;from&#32;branch&#32;HEAD&#32;that&#32;are&#32;syntaxically&#32;correct&#32;as&#32;well&#32;as&#32;their&#32;recursive&#32;imports|
|Composition|- [Module aec3po](https://github.com/Accord-Project/aec3po/blob/HEAD/src/aec3po.ttl)<br/>- [Module check&lowbar;method](https://github.com/Accord-Project/aec3po/blob/HEAD/src/check_method.ttl)<br/>- [Module checking&lowbar;act](https://github.com/Accord-Project/aec3po/blob/HEAD/src/checking_act.ttl)<br/>- [Module compliance&lowbar;verification&lowbar;report](https://github.com/Accord-Project/aec3po/blob/HEAD/src/compliance_verification_report.ttl)<br/>- [Module data&lowbar;requirement](https://github.com/Accord-Project/aec3po/blob/HEAD/src/data_requirement.ttl)<br/>- [Module document](https://github.com/Accord-Project/aec3po/blob/HEAD/src/document.ttl)<br/>- [Module evidence](https://github.com/Accord-Project/aec3po/blob/HEAD/src/evidence.ttl)<br/>- [Module feature&lowbar;of&lowbar;interest](https://github.com/Accord-Project/aec3po/blob/HEAD/src/feature_of_interest.ttl)<br/>- [Module legal&lowbar;verifier](https://github.com/Accord-Project/aec3po/blob/HEAD/src/legal_verifier.ttl)<br/>- [Module model](https://github.com/Accord-Project/aec3po/blob/HEAD/src/model.ttl)<br/>- [Module rase&lowbar;statement](https://github.com/Accord-Project/aec3po/blob/HEAD/src/rase_statement.ttl)<br/>- [Module statement](https://github.com/Accord-Project/aec3po/blob/HEAD/src/statement.ttl)<br/>- [Module table](https://github.com/Accord-Project/aec3po/blob/HEAD/src/table.ttl)<br/>- [Module vocabularies/&lowbar;shape](https://github.com/Accord-Project/aec3po/blob/HEAD/src/vocabularies/_shape.ttl)<br/>- [Module vocabularies/administrative&lowbar;areas](https://github.com/Accord-Project/aec3po/blob/HEAD/src/vocabularies/administrative_areas.ttl)<br/>- [Module vocabularies/building&lowbar;structure](https://github.com/Accord-Project/aec3po/blob/HEAD/src/vocabularies/building_structure.ttl)<br/>- [Module vocabularies/building&lowbar;usage](https://github.com/Accord-Project/aec3po/blob/HEAD/src/vocabularies/building_usage.ttl)<br/>- [Module vocabularies/check&lowbar;method&lowbar;comparators](https://github.com/Accord-Project/aec3po/blob/HEAD/src/vocabularies/check_method_comparators.ttl)<br/>- [Module vocabularies/check&lowbar;method&lowbar;operators](https://github.com/Accord-Project/aec3po/blob/HEAD/src/vocabularies/check_method_operators.ttl)<br/>- [Module vocabularies/disciplines](https://github.com/Accord-Project/aec3po/blob/HEAD/src/vocabularies/disciplines.ttl)<br/>- [Module vocabularies/permitting&lowbar;stages](https://github.com/Accord-Project/aec3po/blob/HEAD/src/vocabularies/permitting_stages.ttl)<br/>- [Module vocabularies/quantity&lowbar;kinds](https://github.com/Accord-Project/aec3po/blob/HEAD/src/vocabularies/quantity_kinds.ttl)|

#### Criterion detail
|Identifier|[term-referencing](https://ns.inria.fr/olivaw#term-referencing)|
|----|----|
|Title|Term&#32;referencing&#32;test|
|Description|A&#32;test&#32;case&#32;from&#32;the&#32;Best&#32;Practices&#32;tests&#32;checking&#32;if&#32;each&#32;term&#32;of&#32;the&#32;test&#32;subject&#32;is&#32;referenced&#32;to&#32;a&#32;module&#32;through&#32;a&#32;rdfs:isDefinedBy&#32;property.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-160)|Identifier|`no-reference-module`|
|[Section top](#minorfail-outcome-number-160)|Title|Term&#32;not&#32;referenced&#32;to&#32;a&#32;module|
|[Section top](#minorfail-outcome-number-160)|Description|Subject&#32;terms&#32;not&#32;linked&#32;to&#32;a&#32;module&#32;by&#32;a&#32;rdfs:isDefinedBy&#32;property|
|[Section top](#minorfail-outcome-number-160)|Pointer|<pre lang="Turtle"><code>:edlira&#32;a&#32;schema:Person&#32;;  &#10; &#32; &#32; &#32; &#32;schema:affiliation&#32; &#60;https://www.bcu.ac.uk/> &#32;;  &#10; &#32; &#32; &#32; &#32;schema:email&#32; &#34;edlira.vakaj@bcu.ac.uk&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;schema:identifier&#32; &#60;http://orcid.org/0000-0002-0712-0959> &#32;;  &#10; &#32; &#32; &#32; &#32;schema:name&#32; &#34;Edlira&#32;Vakaj&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;schema:url&#32; &#60;https://www.bcu.ac.uk/computing/about-us/our-staff/edlira-vakaj> &#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-160)|Pointer|<pre lang="Turtle"><code>:pan&#32;a&#32;schema:Person&#32;;  &#10; &#32; &#32; &#32; &#32;schema:affiliation&#32; &#60;https://www.bcu.ac.uk/> &#32;;  &#10; &#32; &#32; &#32; &#32;schema:email&#32; &#34;Panagiotis.Patlakas@bcu.ac.uk&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;schema:identifier&#32; &#60;http://orcid.org/0000-0002-7248-8952> &#32;;  &#10; &#32; &#32; &#32; &#32;schema:name&#32; &#34;Panagiotis&#32;Patlakas&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;schema:url&#32; &#60;https://www.bcu.ac.uk/built-environment/about-us/our-staff/panagiotis-patlakas> &#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-160)|Pointer|<pre lang="Turtle"><code>:amna&#32;a&#32;schema:Person&#32;;  &#10; &#32; &#32; &#32; &#32;schema:affiliation&#32; &#60;https://www.bcu.ac.uk/> &#32;;  &#10; &#32; &#32; &#32; &#32;schema:email&#32; &#34;Amna.Dridi@bcu.ac.uk&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;schema:identifier&#32; &#60;http://orcid.org/0000-0002-0185-103X> &#32;;  &#10; &#32; &#32; &#32; &#32;schema:name&#32; &#34;Amna&#32;Dridi&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;schema:url&#32; &#60;https://www.researchgate.net/profile/Amna-Dridi-3> &#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-160)|Pointer|<pre lang="Turtle"><code>:thomas&#32;a&#32;schema:Person&#32;;  &#10; &#32; &#32; &#32; &#32;schema:affiliation&#32; &#60;https://www.cardiff.ac.uk/> &#32;;  &#10; &#32; &#32; &#32; &#32;schema:email&#32; &#34;beachth@cardiff.ac.uk&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;schema:identifier&#32; &#60;http://orcid.org/0000-0001-5610-8027> &#32;;  &#10; &#32; &#32; &#32; &#32;schema:name&#32; &#34;Thomas&#32;Beach&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;schema:url&#32; &#60;https://profiles.cardiff.ac.uk/staff/beachth> &#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-160)|Pointer|<pre lang="Turtle"><code>:vladimir&#32;a&#32;schema:Person&#32;;  &#10; &#32; &#32; &#32; &#32;schema:affiliation&#32; &#60;https://www.ontotext.com/> &#32;;  &#10; &#32; &#32; &#32; &#32;schema:email&#32; &#34;vladimir.alexiev@ontotext.com&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;schema:identifier&#32; &#60;https://orcid.org/0000-0001-7508-7428> &#32;;  &#10; &#32; &#32; &#32; &#32;schema:name&#32; &#34;Vladimir&#32;Alexiev&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;schema:url&#32; &#60;https://www.ontotext.com/blog/author/vladimir/> &#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-160)|Pointer|<pre lang="Turtle"><code>:hasTarget&#32;a&#32;owl:DatatypeProperty&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;hasTarget&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;TBD&#34;@en&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-160)|Pointer|<pre lang="Turtle"><code>:hasBooleanTarget&#32;a&#32;owl:DatatypeProperty&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;hasBooleanTarget&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;TBD&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:range&#32;xsd:boolean&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-160)|Pointer|<pre lang="Turtle"><code>:name&#32;a&#32;owl:DatatypeProperty&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;name&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;The&#32;name&#32;or&#32;the&#32;identifier&#32;of&#32;the&#32;BIM&#32;model.&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:domain&#32; &#60;https://schema.org/Model> &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:range&#32;xsd:string&#32;;  &#10; &#32; &#32; &#32; &#32;owl:equivalentProperty&#32; &#60;https://schema.org/about> &#32;;  &#10; &#32; &#32; &#32; &#32;owl:inverseOf&#32; &#60;https://schema.org/subjectOf> &#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-160)|Pointer|<pre lang="Turtle"><code>:description&#32;a&#32;owl:DatatypeProperty&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;description&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;A&#32;textual&#32;description&#32;providing&#32;additional&#32;details&#32;about&#32;the...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:domain&#32; &#60;https://schema.org/Model> &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:range&#32;xsd:string&#32;;  &#10; &#32; &#32; &#32; &#32;owl:equivalentProperty&#32; &#60;https://schema.org/abstract> &#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-160)|Pointer|<pre lang="Turtle"><code>:location&#32;a&#32;owl:ObjectProperty&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;location&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;The&#32;physical&#32;or&#32;geographic&#32;location&#32;of&#32;the&#32;building&#32;or&#32;struc...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:domain&#32; &#60;https://schema.org/Model> &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:range&#32; &#60;https://schema.org/Place> &#32;;  &#10; &#32; &#32; &#32; &#32;owl:equivalentProperty&#32; &#60;https://schema.org/spatial> &#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-160)|Pointer|<pre lang="Turtle"><code>:locationCoverage&#32;a&#32;owl:ObjectProperty&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;location&#32;coverage&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;The&#32;spatialCoverage&#32;indicates&#32;the&#32;place(s)&#32;or&#32;the&#32;administra...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:domain&#32; &#60;https://schema.org/Model> &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:range&#32; &#91;&#32;a&#32;owl:Class&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:unionOf&#32;(&#32; &#60;https://schema.org/Place> &#32;:AdministrativeArea&#32;)&#32;]&#32;;  &#10; &#32; &#32; &#32; &#32;owl:equivalentProperty&#32; &#60;https://schema.org/spatialCoverage> &#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-160)|Pointer|<pre lang="Turtle"><code>:material&#32;a&#32;owl:DatatypeProperty&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;material&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;The&#32;materials&#32;used&#32;for&#32;different&#32;parts&#32;of&#32;the&#32;building,&#32;such...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:domain&#32; &#60;https://schema.org/Model> &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:range&#32;xsd:string&#32;;  &#10; &#32; &#32; &#32; &#32;owl:equivalentProperty&#32; &#60;https://schema.org/material> &#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-160)|Pointer|<pre lang="Turtle"><code>:hasBuildingPhase&#32;a&#32;owl:ObjectProperty&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;has&#32;building&#32;phase&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;describes&#32;the&#32;relationship&#32;between&#32;a&#32;construction-related&#32;en...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:domain&#32;:Model&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:range&#32;:Phase&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-160)|Pointer|<pre lang="Turtle"><code>:hasElementPhase&#32;a&#32;owl:ObjectProperty&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;has&#32;element&#32;phase&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;is&#32;used&#32;to&#32;establish&#32;a&#32;relationship&#32;between&#32;a&#32;construction&#32;e...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:domain&#32;:Model&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:range&#32;:Phase&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-160)|Pointer|<pre lang="Turtle"><code>:hasDimension&#32;a&#32;owl:ObjectProperty&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;has&#32;dimension&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;is&#32;used&#32;to&#32;represent&#32;the&#32;physical&#32;dimensions&#32;or&#32;measurements...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:domain&#32;:Model&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:range&#32;:Dimension&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-160)|Pointer|<pre lang="Turtle"><code>:hasClassification&#32;a&#32;owl:ObjectProperty&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;has&#32;dimension&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;is&#32;used&#32;to&#32;link&#32;building&#32;components,&#32;elements,&#32;or&#32;other&#32;enti...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:domain&#32;:Model&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:range&#32;:Classification&#32;.</code></pre>|

***
### MinorFail Outcome number 161

[Jump to summary definition](#summary-MinorFail-161)	|	[Previous MinorFail outcome](#minorfail-outcome-number-160)	|	Next MinorFail outcome

:exclamation:MinorFail outcome
#### Subject detail
|Name|all-fragments|
|----|----|
|Title|All&#32;the&#32;fragments&#32;from&#32;branch&#32;HEAD&#32;that&#32;are&#32;syntaxically&#32;correct&#32;as&#32;well&#32;as&#32;their&#32;recursive&#32;imports|
|Composition|- [Module aec3po](https://github.com/Accord-Project/aec3po/blob/HEAD/src/aec3po.ttl)<br/>- [Module check&lowbar;method](https://github.com/Accord-Project/aec3po/blob/HEAD/src/check_method.ttl)<br/>- [Module checking&lowbar;act](https://github.com/Accord-Project/aec3po/blob/HEAD/src/checking_act.ttl)<br/>- [Module compliance&lowbar;verification&lowbar;report](https://github.com/Accord-Project/aec3po/blob/HEAD/src/compliance_verification_report.ttl)<br/>- [Module data&lowbar;requirement](https://github.com/Accord-Project/aec3po/blob/HEAD/src/data_requirement.ttl)<br/>- [Module document](https://github.com/Accord-Project/aec3po/blob/HEAD/src/document.ttl)<br/>- [Module evidence](https://github.com/Accord-Project/aec3po/blob/HEAD/src/evidence.ttl)<br/>- [Module feature&lowbar;of&lowbar;interest](https://github.com/Accord-Project/aec3po/blob/HEAD/src/feature_of_interest.ttl)<br/>- [Module legal&lowbar;verifier](https://github.com/Accord-Project/aec3po/blob/HEAD/src/legal_verifier.ttl)<br/>- [Module model](https://github.com/Accord-Project/aec3po/blob/HEAD/src/model.ttl)<br/>- [Module rase&lowbar;statement](https://github.com/Accord-Project/aec3po/blob/HEAD/src/rase_statement.ttl)<br/>- [Module statement](https://github.com/Accord-Project/aec3po/blob/HEAD/src/statement.ttl)<br/>- [Module table](https://github.com/Accord-Project/aec3po/blob/HEAD/src/table.ttl)<br/>- [Module vocabularies/&lowbar;shape](https://github.com/Accord-Project/aec3po/blob/HEAD/src/vocabularies/_shape.ttl)<br/>- [Module vocabularies/administrative&lowbar;areas](https://github.com/Accord-Project/aec3po/blob/HEAD/src/vocabularies/administrative_areas.ttl)<br/>- [Module vocabularies/building&lowbar;structure](https://github.com/Accord-Project/aec3po/blob/HEAD/src/vocabularies/building_structure.ttl)<br/>- [Module vocabularies/building&lowbar;usage](https://github.com/Accord-Project/aec3po/blob/HEAD/src/vocabularies/building_usage.ttl)<br/>- [Module vocabularies/check&lowbar;method&lowbar;comparators](https://github.com/Accord-Project/aec3po/blob/HEAD/src/vocabularies/check_method_comparators.ttl)<br/>- [Module vocabularies/check&lowbar;method&lowbar;operators](https://github.com/Accord-Project/aec3po/blob/HEAD/src/vocabularies/check_method_operators.ttl)<br/>- [Module vocabularies/disciplines](https://github.com/Accord-Project/aec3po/blob/HEAD/src/vocabularies/disciplines.ttl)<br/>- [Module vocabularies/permitting&lowbar;stages](https://github.com/Accord-Project/aec3po/blob/HEAD/src/vocabularies/permitting_stages.ttl)<br/>- [Module vocabularies/quantity&lowbar;kinds](https://github.com/Accord-Project/aec3po/blob/HEAD/src/vocabularies/quantity_kinds.ttl)|

#### Criterion detail
|Identifier|[terms-differenciation](https://ns.inria.fr/olivaw#terms-differenciation)|
|----|----|
|Title|Terms&#32;differenciation&#32;test|
|Description|A&#32;test&#32;case&#32;from&#32;the&#32;Best&#32;Practices&#32;tests&#32;checking&#32;if&#32;all&#32;the&#32;terms&#32;are&#32;different&#32;enough&#32;from&#32;each&#32;other&#32;according&#32;to&#32;the&#32;Levenshtein&#32;distance&#32;metric.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-161)|Identifier|`too-close-terms`|
|[Section top](#minorfail-outcome-number-161)|Title|Too&#32;close&#32;terms|
|[Section top](#minorfail-outcome-number-161)|Description|Some&#32;terms&#32;are&#32;too&#32;similar|
|[Section top](#minorfail-outcome-number-161)|Pointer|<pre lang="Turtle"><code>:CheckMethodComparator-gt&#32;a&#32;owl:NamedIndividual,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;skos:Concept,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;:CheckMethodComparator&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32;:check&lowbar;method&lowbar;comparators&#32;;  &#10; &#32; &#32; &#32; &#32;skos:definition&#32; &#34;greater-than&#32;comparator.&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;skos:inScheme&#32;:CheckMethodComparatorNomenclature&#32;;  &#10; &#32; &#32; &#32; &#32;skos:prefLabel&#32; &#34;greater&#32;than&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;skos:topConceptOf&#32;:CheckMethodComparatorNomenclature&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-161)|Pointer|<pre lang="Turtle"><code>:CheckMethodComparator-ge&#32;a&#32;owl:NamedIndividual,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;skos:Concept,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;:CheckMethodComparator&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32;:check&lowbar;method&lowbar;comparators&#32;;  &#10; &#32; &#32; &#32; &#32;skos:definition&#32; &#34;greater-equal&#32;comparator.&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;skos:inScheme&#32;:CheckMethodComparatorNomenclature&#32;;  &#10; &#32; &#32; &#32; &#32;skos:prefLabel&#32; &#34;greater&#32;equal&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;skos:topConceptOf&#32;:CheckMethodComparatorNomenclature&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-161)|Pointer|<pre lang="Turtle"><code>:CheckMethodComparator-le&#32;a&#32;owl:NamedIndividual,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;skos:Concept,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;:CheckMethodComparator&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32;:check&lowbar;method&lowbar;comparators&#32;;  &#10; &#32; &#32; &#32; &#32;skos:definition&#32; &#34;less-equal&#32;comparator.&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;skos:inScheme&#32;:CheckMethodComparatorNomenclature&#32;;  &#10; &#32; &#32; &#32; &#32;skos:prefLabel&#32; &#34;less&#32;equal&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;skos:topConceptOf&#32;:CheckMethodComparatorNomenclature&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-161)|Pointer|<pre lang="Turtle"><code>:CheckMethodComparator-lt&#32;a&#32;owl:NamedIndividual,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;skos:Concept,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;:CheckMethodComparator&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32;:check&lowbar;method&lowbar;comparators&#32;;  &#10; &#32; &#32; &#32; &#32;skos:definition&#32; &#34;less-than&#32;comparator.&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;skos:inScheme&#32;:CheckMethodComparatorNomenclature&#32;;  &#10; &#32; &#32; &#32; &#32;skos:prefLabel&#32; &#34;less&#32;than&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;skos:topConceptOf&#32;:CheckMethodComparatorNomenclature&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-161)|Pointer|<pre lang="Turtle"><code>:CheckMethodComparator-neq&#32;a&#32;owl:NamedIndividual,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;skos:Concept,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;:CheckMethodComparator&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32;:check&lowbar;method&lowbar;comparators&#32;;  &#10; &#32; &#32; &#32; &#32;skos:definition&#32; &#34;not&#32;equal-to&#32;comparator.&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;skos:inScheme&#32;:CheckMethodComparatorNomenclature&#32;;  &#10; &#32; &#32; &#32; &#32;skos:prefLabel&#32; &#34;not&#32;equal-to&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;skos:topConceptOf&#32;:CheckMethodComparatorNomenclature&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-161)|Pointer|<pre lang="Turtle"><code>:CheckMethodcomparator-eq&#32;a&#32;owl:NamedIndividual,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;skos:Concept,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;:CheckMethodcomparator&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32;:check&lowbar;method&lowbar;comparators&#32;;  &#10; &#32; &#32; &#32; &#32;skos:definition&#32; &#34;equal-to&#32;comparator.&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;skos:inScheme&#32;:CheckMethodComparatorNomenclature&#32;;  &#10; &#32; &#32; &#32; &#32;skos:prefLabel&#32; &#34;equal-to&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;skos:topConceptOf&#32;:CheckMethodComparatorNomenclature&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-161)|Pointer|<pre lang="Turtle"><code>:OrCheckStatement&#32;a&#32;owl:Class&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;Or&#32;Check&#32;Statement&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;Check&#32;verified&#32;if&#32;and&#32;only&#32;if&#32;at&#32;least&#32;one&#32;of&#32;its&#32;sub-checks...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32;:statement&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:subClassOf&#32; &#91;&#32;a&#32;owl:Restriction&#32;;  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;owl:onProperty&#32;:hasSubdivision&#32;],  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;:ChecklistStatement&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-161)|Pointer|<pre lang="Turtle"><code>:CheckStatement&#32;a&#32;owl:Class&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;Check&#32;Statement&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;refers&#32;to&#32;a&#32;type&#32;of&#32;statement&#32;that&#32;is&#32;used&#32;to&#32;specify&#32;condit...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32;:statement&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:subClassOf&#32;:Statement&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-161)|Pointer|<pre lang="Turtle"><code>:PartialSafetyFactor0&#32;a&#32;owl:NamedIndividual,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;skos:Concept,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;:QuantityKind&#32;;  &#10; &#32; &#32; &#32; &#32;qudt:applicableUnit&#32; &#60;http://qudt.org/vocab/unit/UNITLESS> &#32;;  &#10; &#32; &#32; &#32; &#32;qudt:hasDimensionVector&#32; &#60;http://qudt.org/vocab/dimensionvector/A0E0L0I0M0H0T0D0> &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32;:quantity&lowbar;kinds&#32;;  &#10; &#32; &#32; &#32; &#32;skos:broader&#32;:PartialSafetyFactor&#32;;  &#10; &#32; &#32; &#32; &#32;skos:definition&#32; &#34;Also&#32;written&#32;γM0,&#32;the&#32;partial&#32;safety&#32;factor&#32;for&#32;resistance&#32;r...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;skos:prefLabel&#32; &#34;Partial&#32;Safety&#32;Factor&#34;@en&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-161)|Pointer|<pre lang="Turtle"><code>:PartialSafetyFactor&#32;a&#32;owl:NamedIndividual,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;skos:Concept,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;:QuantityKind&#32;;  &#10; &#32; &#32; &#32; &#32;qudt:applicableUnit&#32; &#60;http://qudt.org/vocab/unit/UNITLESS> &#32;;  &#10; &#32; &#32; &#32; &#32;qudt:hasDimensionVector&#32; &#60;http://qudt.org/vocab/dimensionvector/A0E0L0I0M0H0T0D0> &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32;:quantity&lowbar;kinds&#32;;  &#10; &#32; &#32; &#32; &#32;skos:definition&#32; &#34;Also&#32;written&#32;γM,&#32;the&#32;partial&#32;safety&#32;factor&#32;for&#32;resistance.&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;skos:prefLabel&#32; &#34;Partial&#32;Safety&#32;Factor&#34;@en&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-161)|Pointer|<pre lang="Turtle"><code>:PartialSafetyFactor1&#32;a&#32;owl:NamedIndividual,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;skos:Concept,  &#10; &#32; &#32; &#32; &#32; &#32; &#32; &#32; &#32;:QuantityKind&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;Partial&#32;Safety&#32;Factor&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;qudt:applicableUnit&#32; &#60;http://qudt.org/vocab/unit/UNITLESS> &#32;;  &#10; &#32; &#32; &#32; &#32;qudt:hasDimensionVector&#32; &#60;http://qudt.org/vocab/dimensionvector/A0E0L0I0M0H0T0D0> &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32;:quantity&lowbar;kinds&#32;;  &#10; &#32; &#32; &#32; &#32;skos:broader&#32;:PartialSafetyFactor&#32;;  &#10; &#32; &#32; &#32; &#32;skos:definition&#32; &#34;Also&#32;written&#32;γM1,&#32;the&#32;partial&#32;safety&#32;factor&#32;for&#32;resistance&#32;r...&#34; &#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-161)|Pointer|<pre lang="Turtle"><code>:severity&#32;a&#32;owl:ObjectProperty&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;severity&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;Each&#32;verification&#32;result&#32;has&#32;exactly&#32;one&#32;value&#32;for&#32;the&#32;prope...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:domain&#32;:VerificationResult&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32;:compliance&lowbar;verification&lowbar;report&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:range&#32;:Severity&#32;.</code></pre>|
|[Section top](#minorfail-outcome-number-161)|Pointer|<pre lang="Turtle"><code>:Severity&#32;a&#32;owl:Class&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:label&#32; &#34;Severity&#34;@en&#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:comment&#32; &#34;The&#32;class&#32;of&#32;validation&#32;result&#32;severity&#32;levels,&#32;including&#32;vi...&#34; &#32;;  &#10; &#32; &#32; &#32; &#32;rdfs:isDefinedBy&#32;:compliance&lowbar;verification&lowbar;report&#32;.</code></pre>|

***

</details>

***
