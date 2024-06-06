# Test Report Markdown Export

This file is an export of the RDF test report made out of [EARL vocabulary](https://www.w3.org/TR/EARL10/)

This test is powered by Corese, check the [website](https://project.inria.fr/corese/) and the [repository](https://github.com/Wimmics/corese)

The original test report is available in turtle syntax [here](./model-test-manual-NicoRobertIn-2024-06-06T14-22-30.ttl).

# Test Context

Here is some context about under which context this test was made

|Assertor|[NicoRobertIn](https://github.com/NicoRobertIn)|
|----|-----|
|Title|NicoRobertIn using manual script|
|Description|Test triggered by [@NicoRobertIn](https://github.com/NicoRobertIn) by manual trigger|
|Script|[model test suite](https://github.com/Wimmics/olivaw/blob/main/olivaw/test/model/suite.py)
|Date|2024-06-06 14:22:29|

***


# Statistic summary

Here is a short overview for this test report

9 Outcomes

:boom:0 MajorFail, :exclamation:4 MinorFail, :warning:0 CannotTell, :grey_question:0 NotTested, :white_check_mark:5 Pass

<div  style="border-radius: 12px; height: 25px; overflow: hidden"><img src="../assets/red.png" width="0%" height="25px"/><img src="../assets/orange.png" width="44%" height="25px"/><img src="../assets/grey.png" width="0%" height="25px"/><img src="../assets/white.png" width="0%" height="25px"/><img src="../assets/green.png" width="56%" height="25px"/></div>

<br/>

The different status types are an extension of the [EARL](https://www.w3.org/TR/EARL10-Schema/) vocabulary where the nextended terms can be found in the [olivaw-earl dataset](https://github.com/Wimmics/olivaw/blob/main/olivaw/test/olivaw-earl.ttl), each outcome type means:
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
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-1">1/4</div>|:exclamation:MinorFail|`module-src-munc`|[profile-compatibility](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#profile-compatibility)|OWL RL Profile incompatible|[Jump](#minorfail-outcome-number-1)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-2">2/4</div>|:exclamation:MinorFail|`module-src-munc`|[profile-compatibility](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#profile-compatibility)|OWL QL Profile incompatible|[Jump](#minorfail-outcome-number-2)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-3">3/4</div>|:exclamation:MinorFail|`module-src-munc`|[profile-compatibility](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#profile-compatibility)|OWL EL Profile incompatible|[Jump](#minorfail-outcome-number-3)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-4">4/4</div>|:exclamation:MinorFail|`module-src-munc`|[term-referencing](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#term-referencing)|Term not referenced to a module|[Jump](#minorfail-outcome-number-4)|

***

## MinorFail Outcomes Details

This subchapter gives more details to the :exclamation:MinorFail outcomes

### MinorFail Outcome number 1

[Jump to summary definition](#summary-MinorFail-1)	|	Previous MinorFail outcome	|	[Next MinorFail outcome](#minorfail-outcome-number-2)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-src-munc|
|----|----|
|Title|Standalone module src/munc.ttl from branch main|
|Composition|- [Module munc](https://github.com/acimov-tools/model-test/blob/main/src/munc.ttl)|

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
|[Section top](#minorfail-outcome-number-1)|Description|Statement not supported|
|[Section top](#minorfail-outcome-number-1)|Pointer|<pre lang="Turtle"><code>munc:hasFullTranslation a owl:ReflexiveProperty,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:SymmetricProperty,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:TransitiveProperty ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;hasFullTranslation&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:domain munc:UncertaintyApproach ;  &#10;&#32;&#32;&#32;&#32;rdfs:range munc:UncertaintyApproach ;  &#10;&#32;&#32;&#32;&#32;rdfs:subPropertyOf munc:hasIdealTranslation .</code></pre>|

***
### MinorFail Outcome number 2

[Jump to summary definition](#summary-MinorFail-2)	|	[Previous MinorFail outcome](#minorfail-outcome-number-1)	|	[Next MinorFail outcome](#minorfail-outcome-number-3)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-src-munc|
|----|----|
|Title|Standalone module src/munc.ttl from branch main|
|Composition|- [Module munc](https://github.com/acimov-tools/model-test/blob/main/src/munc.ttl)|

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
|[Section top](#minorfail-outcome-number-2)|Description|Statement not supported|
|[Section top](#minorfail-outcome-number-2)|Pointer|<pre lang="Turtle"><code>munc:hasFullTranslation a owl:ReflexiveProperty,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:SymmetricProperty,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:TransitiveProperty ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;hasFullTranslation&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:domain munc:UncertaintyApproach ;  &#10;&#32;&#32;&#32;&#32;rdfs:range munc:UncertaintyApproach ;  &#10;&#32;&#32;&#32;&#32;rdfs:subPropertyOf munc:hasIdealTranslation .</code></pre>|

***
### MinorFail Outcome number 3

[Jump to summary definition](#summary-MinorFail-3)	|	[Previous MinorFail outcome](#minorfail-outcome-number-2)	|	[Next MinorFail outcome](#minorfail-outcome-number-4)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-src-munc|
|----|----|
|Title|Standalone module src/munc.ttl from branch main|
|Composition|- [Module munc](https://github.com/acimov-tools/model-test/blob/main/src/munc.ttl)|

#### Criterion detail
|Identifier|[profile-compatibility](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#profile-compatibility)|
|----|----|
|Title|Profile compatibility test|
|Description|A test meant to check whether the test subject is compatible with a profile or not, and if it is not, why.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-3)|Identifier|`owl-el-profile-error`|
|[Section top](#minorfail-outcome-number-3)|Title|OWL EL Profile incompatible|
|[Section top](#minorfail-outcome-number-3)|Description|Statement not supported|
|[Section top](#minorfail-outcome-number-3)|Pointer|<pre lang="Turtle"><code>munc:hasFullTranslation a owl:ReflexiveProperty,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:SymmetricProperty,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:TransitiveProperty ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;hasFullTranslation&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:domain munc:UncertaintyApproach ;  &#10;&#32;&#32;&#32;&#32;rdfs:range munc:UncertaintyApproach ;  &#10;&#32;&#32;&#32;&#32;rdfs:subPropertyOf munc:hasIdealTranslation .</code></pre>|

***
### MinorFail Outcome number 4

[Jump to summary definition](#summary-MinorFail-4)	|	[Previous MinorFail outcome](#minorfail-outcome-number-3)	|	Next MinorFail outcome

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-src-munc|
|----|----|
|Title|Standalone module src/munc.ttl from branch main|
|Composition|- [Module munc](https://github.com/acimov-tools/model-test/blob/main/src/munc.ttl)|

#### Criterion detail
|Identifier|[term-referencing](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#term-referencing)|
|----|----|
|Title|Term referencing test|
|Description|A test case from the Best Practices tests checking if each term of the test subject is referenced to a module through a rdfs:isDefinedBy property.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-4)|Identifier|`no-reference-module`|
|[Section top](#minorfail-outcome-number-4)|Title|Term not referenced to a module|
|[Section top](#minorfail-outcome-number-4)|Description|Subject terms not linked to a module by a rdfs:isDefinedBy property|
|[Section top](#minorfail-outcome-number-4)|Pointer|<pre lang="Turtle"><code>:UncertaintyOperation a owl:Class ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;Uncertainty Operation&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:comment &#34;The Calculus to apply on the Values of a defined Uncertainty...&#34; .</code></pre>|
|[Section top](#minorfail-outcome-number-4)|Pointer|<pre lang="Turtle"><code>:UncertaintyValue a owl:Class ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;Uncertainty Value&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:comment &#34;For each Uncertainty Feature, exists (when declared) a corre...&#34; .</code></pre>|
|[Section top](#minorfail-outcome-number-4)|Pointer|<pre lang="Turtle"><code>:Meta a owl:Class ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;Meta&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:comment &#34;The metadata associated to a Sentence in a certain World (Co...&#34; .</code></pre>|
|[Section top](#minorfail-outcome-number-4)|Pointer|<pre lang="Turtle"><code>:Sentence a owl:Class ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;Sentence&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:comment &#34;The Sentence (Triple, Graph, Graph Pattern) to which Meta is...&#34; .</code></pre>|
|[Section top](#minorfail-outcome-number-4)|Pointer|<pre lang="Turtle"><code>:Uncertainty a owl:Class ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;Uncertainty&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:comment &#34;A subclass of Meta, it enables annotating the Sentence assoc...&#34; ;  &#10;&#32;&#32;&#32;&#32;rdfs:subClassOf :Meta .</code></pre>|
|[Section top](#minorfail-outcome-number-4)|Pointer|<pre lang="Turtle"><code>:World a owl:Class ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;World&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:comment &#34;The context (Graph, Default Graph, etc.) in which the Senten...&#34; .</code></pre>|
|[Section top](#minorfail-outcome-number-4)|Pointer|<pre lang="Turtle"><code>:UncertaintyApproach a owl:Class ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;Uncertainty Approach&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:comment &#34;Individuals of this class represent uncertainty approaches, ...&#34; .</code></pre>|
|[Section top](#minorfail-outcome-number-4)|Pointer|<pre lang="Turtle"><code>:TranslationFunction a owl:Class ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;Translation Function&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:comment &#34;Individuals of this class are LDScript functions enabling tr...&#34; .</code></pre>|
|[Section top](#minorfail-outcome-number-4)|Pointer|<pre lang="Turtle"><code>:uncertaintyOperator a owl:ObjectProperty ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;uncertaintyOperator&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:comment &#34;Each Uncertainty approach has its own logic to reason over m...&#34; ;  &#10;&#32;&#32;&#32;&#32;rdfs:domain :uncertaintyFeature ;  &#10;&#32;&#32;&#32;&#32;rdfs:range :UncertaintyOperation .</code></pre>|
|[Section top](#minorfail-outcome-number-4)|Pointer|<pre lang="Turtle"><code>:uncertaintyFeature a owl:ObjectProperty ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;uncertaintyFeature&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:comment &#34;Each Uncertainty approach has some features, which can be me...&#34; ;  &#10;&#32;&#32;&#32;&#32;rdfs:domain :Uncertainty ;  &#10;&#32;&#32;&#32;&#32;rdfs:range :UncertaintyValue .</code></pre>|
|[Section top](#minorfail-outcome-number-4)|Pointer|<pre lang="Turtle"><code>:hasMeta a owl:ObjectProperty ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;hasMeta&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:domain :Sentence,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;:World ;  &#10;&#32;&#32;&#32;&#32;rdfs:range :Meta .</code></pre>|
|[Section top](#minorfail-outcome-number-4)|Pointer|<pre lang="Turtle"><code>:hasUncertaintyApproach a owl:ObjectProperty ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;hasUncertaintyApproach&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:domain :Uncertainty ;  &#10;&#32;&#32;&#32;&#32;rdfs:range :UncertaintyApproach .</code></pre>|
|[Section top](#minorfail-outcome-number-4)|Pointer|<pre lang="Turtle"><code>:hasUncertaintyFeature a owl:ObjectProperty ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;hasUncertaintyFeature&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:domain :UncertaintyApproach ;  &#10;&#32;&#32;&#32;&#32;rdfs:range :uncertaintyFeature .</code></pre>|
|[Section top](#minorfail-outcome-number-4)|Pointer|<pre lang="Turtle"><code>:hasUncertaintyOperator a owl:ObjectProperty ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;hasUncertaintyOperator&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:domain :UncertaintyApproach ;  &#10;&#32;&#32;&#32;&#32;rdfs:range :uncertaintyOperator .</code></pre>|
|[Section top](#minorfail-outcome-number-4)|Pointer|<pre lang="Turtle"><code>:statedIn a owl:ObjectProperty ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;statedIn&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:domain :Sentence ;  &#10;&#32;&#32;&#32;&#32;rdfs:range :World .</code></pre>|
|[Section top](#minorfail-outcome-number-4)|Pointer|<pre lang="Turtle"><code>:translateFrom a owl:ObjectProperty ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;translateFrom&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:domain :TranslationFunction ;  &#10;&#32;&#32;&#32;&#32;rdfs:range :UncertaintyApproach .</code></pre>|
|[Section top](#minorfail-outcome-number-4)|Pointer|<pre lang="Turtle"><code>:translateTo a owl:ObjectProperty ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;translateFrom&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:domain :TranslationFunction ;  &#10;&#32;&#32;&#32;&#32;rdfs:range :UncertaintyApproach .</code></pre>|
|[Section top](#minorfail-outcome-number-4)|Pointer|<pre lang="Turtle"><code>:hasTranslation a owl:ObjectProperty ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;hasTranslation&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:domain :UncertaintyApproach ;  &#10;&#32;&#32;&#32;&#32;rdfs:range :UncertaintyApproach .</code></pre>|
|[Section top](#minorfail-outcome-number-4)|Pointer|<pre lang="Turtle"><code>:hasIdealTranslation a owl:ObjectProperty ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;hasIdealTranslation&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:domain :UncertaintyApproach ;  &#10;&#32;&#32;&#32;&#32;rdfs:range :UncertaintyApproach ;  &#10;&#32;&#32;&#32;&#32;rdfs:subPropertyOf :hasTranslation .</code></pre>|
|[Section top](#minorfail-outcome-number-4)|Pointer|<pre lang="Turtle"><code>:hasFullTranslation a owl:ReflexiveProperty,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:SymmetricProperty,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:TransitiveProperty ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;hasFullTranslation&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:domain :UncertaintyApproach ;  &#10;&#32;&#32;&#32;&#32;rdfs:range :UncertaintyApproach ;  &#10;&#32;&#32;&#32;&#32;rdfs:subPropertyOf :hasIdealTranslation .</code></pre>|

***

</details>

***


# Pass Outcomes

[Jump to statistic summary](#statistic-summary)	|	[Previous section](#minorfail-outcomes)	|	Next section

Here is the chapter related to the Pass outcome

:white_check_mark:5 Pass outcomes

<details>
<summary>Fold/Unfold the 5 summary and details</summary>

## Pass Outcomes Summary

:white_check_mark:5 Pass outcomes

|*Jump*|*Number*|*Status*|*Subject*|*Criterion*|*Title*|*Link*|
|------|--------|--------|---------|-----------|-------|------|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-1">1/5</div>|:white_check_mark:Pass|`module-src-munc`|[domain-and-range-referencing](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#domain-and-range-referencing)|Domains properly defined|[Jump](#pass-outcome-number-1)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-2">2/5</div>|:white_check_mark:Pass|`module-src-munc`|[domain-and-range-referencing](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#domain-and-range-referencing)|Ranges properly defined|[Jump](#pass-outcome-number-2)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-3">3/5</div>|:white_check_mark:Pass|`module-src-munc`|[labeled-terms](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#labeled-terms)|All terms labeled|[Jump](#pass-outcome-number-3)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-4">4/5</div>|:white_check_mark:Pass|`module-src-munc`|[owl-rl-constraint](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#owl-rl-constraint)|OWL RL consistent|[Jump](#pass-outcome-number-4)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-5">5/5</div>|:white_check_mark:Pass|`module-src-munc`|[terms-differenciation](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#terms-differenciation)|Terms differenciated enough|[Jump](#pass-outcome-number-5)|

***

## Pass Outcomes Details

This subchapter gives more details to the :white_check_mark:Pass outcomes

### Pass Outcome number 1

[Jump to summary definition](#summary-Pass-1)	|	Previous Pass outcome	|	[Next Pass outcome](#pass-outcome-number-2)

:white_check_mark:Pass outcome
#### Subject detail
|Name|module-src-munc|
|----|----|
|Title|Standalone module src/munc.ttl from branch main|
|Composition|- [Module munc](https://github.com/acimov-tools/model-test/blob/main/src/munc.ttl)|

#### Criterion detail
|Identifier|[domain-and-range-referencing](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#domain-and-range-referencing)|
|----|----|
|Title|Domain and range referencing test|
|Description|A test case from the Best Practices tests checking if all the ranges and domains from the test subject point to terms that are defined in the vocabulary.|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-1)|Identifier|`domain-out-of-vocabulary`|
|[Section top](#pass-outcome-number-1)|Title|Domains properly defined|
|[Section top](#pass-outcome-number-1)|Description|Each rdfs:domain is defined within the fragment|

***
### Pass Outcome number 2

[Jump to summary definition](#summary-Pass-2)	|	[Previous Pass outcome](#pass-outcome-number-1)	|	[Next Pass outcome](#pass-outcome-number-3)

:white_check_mark:Pass outcome
#### Subject detail
|Name|module-src-munc|
|----|----|
|Title|Standalone module src/munc.ttl from branch main|
|Composition|- [Module munc](https://github.com/acimov-tools/model-test/blob/main/src/munc.ttl)|

#### Criterion detail
|Identifier|[domain-and-range-referencing](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#domain-and-range-referencing)|
|----|----|
|Title|Domain and range referencing test|
|Description|A test case from the Best Practices tests checking if all the ranges and domains from the test subject point to terms that are defined in the vocabulary.|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-2)|Identifier|`range-out-of-vocabulary`|
|[Section top](#pass-outcome-number-2)|Title|Ranges properly defined|
|[Section top](#pass-outcome-number-2)|Description|Each rdfs:range is defined within the fragment|

***
### Pass Outcome number 3

[Jump to summary definition](#summary-Pass-3)	|	[Previous Pass outcome](#pass-outcome-number-2)	|	[Next Pass outcome](#pass-outcome-number-4)

:white_check_mark:Pass outcome
#### Subject detail
|Name|module-src-munc|
|----|----|
|Title|Standalone module src/munc.ttl from branch main|
|Composition|- [Module munc](https://github.com/acimov-tools/model-test/blob/main/src/munc.ttl)|

#### Criterion detail
|Identifier|[labeled-terms](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#labeled-terms)|
|----|----|
|Title|Term labeling test|
|Description|A test case from the Best Practices tests checking if all the terms of the subject have a rdfs:label property pointing to a literal in English|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-3)|Identifier|`not-labeled-term`|
|[Section top](#pass-outcome-number-3)|Title|All terms labeled|
|[Section top](#pass-outcome-number-3)|Description|All the terms defined in the subject have a rdfs:label in English|

***
### Pass Outcome number 4

[Jump to summary definition](#summary-Pass-4)	|	[Previous Pass outcome](#pass-outcome-number-3)	|	[Next Pass outcome](#pass-outcome-number-5)

:white_check_mark:Pass outcome
#### Subject detail
|Name|module-src-munc|
|----|----|
|Title|Standalone module src/munc.ttl from branch main|
|Composition|- [Module munc](https://github.com/acimov-tools/model-test/blob/main/src/munc.ttl)|

#### Criterion detail
|Identifier|[owl-rl-constraint](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#owl-rl-constraint)|
|----|----|
|Title|OWL RL Constraint test|
|Description|A test meant to check wether the test subject is syntaxically correct or not.|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-4)|Identifier|`owl-rl-constraint-violation`|
|[Section top](#pass-outcome-number-4)|Title|OWL RL consistent|
|[Section top](#pass-outcome-number-4)|Description|The provided graph is consistent for any OWL RL constraint|

***
### Pass Outcome number 5

[Jump to summary definition](#summary-Pass-5)	|	[Previous Pass outcome](#pass-outcome-number-4)	|	Next Pass outcome

:white_check_mark:Pass outcome
#### Subject detail
|Name|module-src-munc|
|----|----|
|Title|Standalone module src/munc.ttl from branch main|
|Composition|- [Module munc](https://github.com/acimov-tools/model-test/blob/main/src/munc.ttl)|

#### Criterion detail
|Identifier|[terms-differenciation](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#terms-differenciation)|
|----|----|
|Title|Terms differenciation test|
|Description|A test case from the Best Practices tests checking if all the terms are different enough from each other according to the Levenshtein distance metric.|

#### Outcome Detail
|Jump|Type|:white_check_mark:Pass|
|----|----|----|
|[Section top](#pass-outcome-number-5)|Identifier|`too-close-terms`|
|[Section top](#pass-outcome-number-5)|Title|Terms differenciated enough|
|[Section top](#pass-outcome-number-5)|Description|All the terms have have a satisfying Levenshtein distance from each other term.|

***

</details>

***
