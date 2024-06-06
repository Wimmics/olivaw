# Test Report Markdown Export

This file is an export of the RDF test report made out of [EARL vocabulary](https://www.w3.org/TR/EARL10/)

This test is powered by Corese, check the [website](https://project.inria.fr/corese/) and the [repository](https://github.com/Wimmics/corese)

The original test report is available in turtle syntax [here](./model-test-manual-NicoRobertIn-2024-06-06T14-38-00.ttl).

# Test Context

Here is some context about under which context this test was made

|Assertor|[NicoRobertIn](https://github.com/NicoRobertIn)|
|----|-----|
|Title|NicoRobertIn using manual script|
|Description|Test triggered by [@NicoRobertIn](https://github.com/NicoRobertIn) by manual trigger|
|Script|[model test suite](https://github.com/Wimmics/olivaw/blob/main/olivaw/test/model/suite.py)
|Date|2024-06-06 14:37:59|

***


# Statistic summary

Here is a short overview for this test report

12 Outcomes

:boom:0 MajorFail, :exclamation:7 MinorFail, :warning:0 CannotTell, :grey_question:0 NotTested, :white_check_mark:5 Pass

<div  style="border-radius: 12px; height: 25px; overflow: hidden"><img src="../assets/red.png" width="0%" height="25px"/><img src="../assets/orange.png" width="58%" height="25px"/><img src="../assets/grey.png" width="0%" height="25px"/><img src="../assets/white.png" width="0%" height="25px"/><img src="../assets/green.png" width="42%" height="25px"/></div>

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

:exclamation:7 MinorFail outcomes

<details>
<summary>Fold/Unfold the 7 summary and details</summary>

## MinorFail Outcomes Summary

:exclamation:7 MinorFail outcomes

|*Jump*|*Number*|*Status*|*Subject*|*Criterion*|*Title*|*Link*|
|------|--------|--------|---------|-----------|-------|------|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-1">1/7</div>|:exclamation:MinorFail|`module-src-pwkso`|[profile-compatibility](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#profile-compatibility)|OWL RL Profile incompatible|[Jump](#minorfail-outcome-number-1)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-2">2/7</div>|:exclamation:MinorFail|`module-src-pwkso`|[profile-compatibility](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#profile-compatibility)|OWL RL Profile incompatible|[Jump](#minorfail-outcome-number-2)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-3">3/7</div>|:exclamation:MinorFail|`module-src-pwkso`|[profile-compatibility](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#profile-compatibility)|OWL QL Profile incompatible|[Jump](#minorfail-outcome-number-3)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-4">4/7</div>|:exclamation:MinorFail|`module-src-pwkso`|[profile-compatibility](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#profile-compatibility)|OWL QL Profile incompatible|[Jump](#minorfail-outcome-number-4)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-5">5/7</div>|:exclamation:MinorFail|`module-src-pwkso`|[profile-compatibility](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#profile-compatibility)|OWL EL Profile incompatible|[Jump](#minorfail-outcome-number-5)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-6">6/7</div>|:exclamation:MinorFail|`module-src-pwkso`|[profile-compatibility](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#profile-compatibility)|OWL EL Profile incompatible|[Jump](#minorfail-outcome-number-6)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-7">7/7</div>|:exclamation:MinorFail|`module-src-pwkso`|[term-referencing](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#term-referencing)|Term not referenced to a module|[Jump](#minorfail-outcome-number-7)|

***

## MinorFail Outcomes Details

This subchapter gives more details to the :exclamation:MinorFail outcomes

### MinorFail Outcome number 1

[Jump to summary definition](#summary-MinorFail-1)	|	Previous MinorFail outcome	|	[Next MinorFail outcome](#minorfail-outcome-number-2)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-src-pwkso|
|----|----|
|Title|Standalone module src/pwkso.ttl from branch main|
|Composition|- [Module pwkso](https://github.com/acimov-tools/model-test/blob/main/src/pwkso.ttl)|

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
|[Section top](#minorfail-outcome-number-1)|Pointer|<pre lang="Turtle"><code>pwkso:BinaryKripkeRelation rdfs:label &#34;binary Kripke relation&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:comment &#34;relation that links a possible world with another to represe...&#34; ;  &#10;&#32;&#32;&#32;&#32;rdfs:subClassOf &#91; a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:onProperty pwkso:param ],  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;pwkso:KripkeRelation .</code></pre>|
|[Section top](#minorfail-outcome-number-1)|Pointer|<pre lang="Turtle"><code>pwkso:UnaryKripkeRelation rdfs:label &#34;unary Kripke relation&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:comment &#34;relation that links a possible world with another to represe...&#34; ;  &#10;&#32;&#32;&#32;&#32;rdfs:subClassOf &#91; a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:onProperty pwkso:param ],  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;pwkso:KripkeRelation .</code></pre>|

***
### MinorFail Outcome number 2

[Jump to summary definition](#summary-MinorFail-2)	|	[Previous MinorFail outcome](#minorfail-outcome-number-1)	|	[Next MinorFail outcome](#minorfail-outcome-number-3)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-src-pwkso|
|----|----|
|Title|Standalone module src/pwkso.ttl from branch main|
|Composition|- [Module pwkso](https://github.com/acimov-tools/model-test/blob/main/src/pwkso.ttl)|

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
|[Section top](#minorfail-outcome-number-2)|Pointer|<pre lang="Turtle"><code>&#91;] a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;owl:onProperty pwkso:param .</code></pre>|

***
### MinorFail Outcome number 3

[Jump to summary definition](#summary-MinorFail-3)	|	[Previous MinorFail outcome](#minorfail-outcome-number-2)	|	[Next MinorFail outcome](#minorfail-outcome-number-4)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-src-pwkso|
|----|----|
|Title|Standalone module src/pwkso.ttl from branch main|
|Composition|- [Module pwkso](https://github.com/acimov-tools/model-test/blob/main/src/pwkso.ttl)|

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
|[Section top](#minorfail-outcome-number-3)|Description|Class Expression not supported with rdfs:subClassOf|
|[Section top](#minorfail-outcome-number-3)|Pointer|<pre lang="Turtle"><code>pwkso:BinaryKripkeRelation rdfs:label &#34;binary Kripke relation&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:comment &#34;relation that links a possible world with another to represe...&#34; ;  &#10;&#32;&#32;&#32;&#32;rdfs:subClassOf &#91; a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:onProperty pwkso:param ],  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;pwkso:KripkeRelation .</code></pre>|
|[Section top](#minorfail-outcome-number-3)|Pointer|<pre lang="Turtle"><code>pwkso:UnaryKripkeRelation rdfs:label &#34;unary Kripke relation&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:comment &#34;relation that links a possible world with another to represe...&#34; ;  &#10;&#32;&#32;&#32;&#32;rdfs:subClassOf &#91; a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:onProperty pwkso:param ],  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;pwkso:KripkeRelation .</code></pre>|

***
### MinorFail Outcome number 4

[Jump to summary definition](#summary-MinorFail-4)	|	[Previous MinorFail outcome](#minorfail-outcome-number-3)	|	[Next MinorFail outcome](#minorfail-outcome-number-5)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-src-pwkso|
|----|----|
|Title|Standalone module src/pwkso.ttl from branch main|
|Composition|- [Module pwkso](https://github.com/acimov-tools/model-test/blob/main/src/pwkso.ttl)|

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
|[Section top](#minorfail-outcome-number-4)|Description|Statement not supported in a Super Class Expression|
|[Section top](#minorfail-outcome-number-4)|Pointer|<pre lang="Turtle"><code>&#91;] a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;owl:onProperty pwkso:param .</code></pre>|

***
### MinorFail Outcome number 5

[Jump to summary definition](#summary-MinorFail-5)	|	[Previous MinorFail outcome](#minorfail-outcome-number-4)	|	[Next MinorFail outcome](#minorfail-outcome-number-6)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-src-pwkso|
|----|----|
|Title|Standalone module src/pwkso.ttl from branch main|
|Composition|- [Module pwkso](https://github.com/acimov-tools/model-test/blob/main/src/pwkso.ttl)|

#### Criterion detail
|Identifier|[profile-compatibility](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#profile-compatibility)|
|----|----|
|Title|Profile compatibility test|
|Description|A test meant to check whether the test subject is compatible with a profile or not, and if it is not, why.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-5)|Identifier|`owl-el-profile-error`|
|[Section top](#minorfail-outcome-number-5)|Title|OWL EL Profile incompatible|
|[Section top](#minorfail-outcome-number-5)|Description|Class Expression not supported with rdfs:subClassOf|
|[Section top](#minorfail-outcome-number-5)|Pointer|<pre lang="Turtle"><code>pwkso:BinaryKripkeRelation rdfs:label &#34;binary Kripke relation&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:comment &#34;relation that links a possible world with another to represe...&#34; ;  &#10;&#32;&#32;&#32;&#32;rdfs:subClassOf &#91; a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:onProperty pwkso:param ],  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;pwkso:KripkeRelation .</code></pre>|
|[Section top](#minorfail-outcome-number-5)|Pointer|<pre lang="Turtle"><code>pwkso:UnaryKripkeRelation rdfs:label &#34;unary Kripke relation&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:comment &#34;relation that links a possible world with another to represe...&#34; ;  &#10;&#32;&#32;&#32;&#32;rdfs:subClassOf &#91; a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:onProperty pwkso:param ],  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;pwkso:KripkeRelation .</code></pre>|

***
### MinorFail Outcome number 6

[Jump to summary definition](#summary-MinorFail-6)	|	[Previous MinorFail outcome](#minorfail-outcome-number-5)	|	[Next MinorFail outcome](#minorfail-outcome-number-7)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-src-pwkso|
|----|----|
|Title|Standalone module src/pwkso.ttl from branch main|
|Composition|- [Module pwkso](https://github.com/acimov-tools/model-test/blob/main/src/pwkso.ttl)|

#### Criterion detail
|Identifier|[profile-compatibility](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#profile-compatibility)|
|----|----|
|Title|Profile compatibility test|
|Description|A test meant to check whether the test subject is compatible with a profile or not, and if it is not, why.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-6)|Identifier|`owl-el-profile-error`|
|[Section top](#minorfail-outcome-number-6)|Title|OWL EL Profile incompatible|
|[Section top](#minorfail-outcome-number-6)|Description|Statement not supported in a Class Expression|
|[Section top](#minorfail-outcome-number-6)|Pointer|<pre lang="Turtle"><code>&#91;] a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;owl:onProperty pwkso:param .</code></pre>|

***
### MinorFail Outcome number 7

[Jump to summary definition](#summary-MinorFail-7)	|	[Previous MinorFail outcome](#minorfail-outcome-number-6)	|	Next MinorFail outcome

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-src-pwkso|
|----|----|
|Title|Standalone module src/pwkso.ttl from branch main|
|Composition|- [Module pwkso](https://github.com/acimov-tools/model-test/blob/main/src/pwkso.ttl)|

#### Criterion detail
|Identifier|[term-referencing](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#term-referencing)|
|----|----|
|Title|Term referencing test|
|Description|A test case from the Best Practices tests checking if each term of the test subject is referenced to a module through a rdfs:isDefinedBy property.|

#### Outcome Detail
|Jump|Type|:exclamation:MinorFail|
|----|----|----|
|[Section top](#minorfail-outcome-number-7)|Identifier|`no-reference-module`|
|[Section top](#minorfail-outcome-number-7)|Title|Term not referenced to a module|
|[Section top](#minorfail-outcome-number-7)|Description|Subject terms not linked to a module by a rdfs:isDefinedBy property|
|[Section top](#minorfail-outcome-number-7)|Pointer|<pre lang="Turtle"><code>:PossibleWorld a owl:Class ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;possible world&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:comment &#34;a consistent representation of how the world is, could have ...&#34; .</code></pre>|
|[Section top](#minorfail-outcome-number-7)|Pointer|<pre lang="Turtle"><code>:verifiedIn a owl:ObjectProperty ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;verified in&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:comment &#34;links triples to a possible world in which their associated ...&#34; ;  &#10;&#32;&#32;&#32;&#32;rdfs:range :PossibleWorld ;  &#10;&#32;&#32;&#32;&#32;owl:propertyDisjointWith :notVerifiedIn .</code></pre>|
|[Section top](#minorfail-outcome-number-7)|Pointer|<pre lang="Turtle"><code>:notVerifiedIn a owl:ObjectProperty ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;not verified in&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:comment &#34;links triples to a possible world in which associated formul...&#34; ;  &#10;&#32;&#32;&#32;&#32;rdfs:range :PossibleWorld ;  &#10;&#32;&#32;&#32;&#32;owl:propertyDisjointWith :verifiedIn .</code></pre>|
|[Section top](#minorfail-outcome-number-7)|Pointer|<pre lang="Turtle"><code>:ClosedPossibleWorld a owl:Class ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;closed possible world&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:comment &#34;represents a possible world with the Closed-World Assumption&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:subClassOf :PossibleWorld .</code></pre>|
|[Section top](#minorfail-outcome-number-7)|Pointer|<pre lang="Turtle"><code>:OpenPossibleWorld a owl:Class ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;open possible world&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:comment &#34;represents a possible world with the Open-World Assumption&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:subClassOf :PossibleWorld .</code></pre>|
|[Section top](#minorfail-outcome-number-7)|Pointer|<pre lang="Turtle"><code>:KripkeRelation a owl:Class ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;Kripke relation&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:comment &#34;represents the Kripke relations between possible worlds. Ins...&#34; .</code></pre>|
|[Section top](#minorfail-outcome-number-7)|Pointer|<pre lang="Turtle"><code>:param a owl:ObjectProperty ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;parameter&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:comment &#34;parameter of a Kripke relation&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:domain :KripkeRelation ;  &#10;&#32;&#32;&#32;&#32;rdfs:range :PossibleWorld .</code></pre>|
|[Section top](#minorfail-outcome-number-7)|Pointer|<pre lang="Turtle"><code>:index a owl:ObjectProperty ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;index&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:comment &#34;index of a Kripke relation&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:domain :KripkeRelation .</code></pre>|
|[Section top](#minorfail-outcome-number-7)|Pointer|<pre lang="Turtle"><code>:hasRelation a owl:ObjectProperty ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;has relation&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:comment &#34;links a possible world to one of its N-ary relations&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:domain :PossibleWorld ;  &#10;&#32;&#32;&#32;&#32;rdfs:range :KripkeRelation .</code></pre>|
|[Section top](#minorfail-outcome-number-7)|Pointer|<pre lang="Turtle"><code>:BinaryKripkeRelation rdfs:label &#34;binary Kripke relation&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:comment &#34;relation that links a possible world with another to represe...&#34; ;  &#10;&#32;&#32;&#32;&#32;rdfs:subClassOf &#91; a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:onProperty :param ],  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;:KripkeRelation .</code></pre>|
|[Section top](#minorfail-outcome-number-7)|Pointer|<pre lang="Turtle"><code>:UnaryKripkeRelation rdfs:label &#34;unary Kripke relation&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:comment &#34;relation that links a possible world with another to represe...&#34; ;  &#10;&#32;&#32;&#32;&#32;rdfs:subClassOf &#91; a owl:Restriction ;  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;owl:onProperty :param ],  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;:KripkeRelation .</code></pre>|

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
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-1">1/5</div>|:white_check_mark:Pass|`module-src-pwkso`|[domain-and-range-referencing](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#domain-and-range-referencing)|Domains properly defined|[Jump](#pass-outcome-number-1)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-2">2/5</div>|:white_check_mark:Pass|`module-src-pwkso`|[domain-and-range-referencing](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#domain-and-range-referencing)|Ranges properly defined|[Jump](#pass-outcome-number-2)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-3">3/5</div>|:white_check_mark:Pass|`module-src-pwkso`|[labeled-terms](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#labeled-terms)|All terms labeled|[Jump](#pass-outcome-number-3)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-4">4/5</div>|:white_check_mark:Pass|`module-src-pwkso`|[owl-rl-constraint](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#owl-rl-constraint)|OWL RL consistent|[Jump](#pass-outcome-number-4)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-5">5/5</div>|:white_check_mark:Pass|`module-src-pwkso`|[terms-differenciation](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#terms-differenciation)|Terms differenciated enough|[Jump](#pass-outcome-number-5)|

***

## Pass Outcomes Details

This subchapter gives more details to the :white_check_mark:Pass outcomes

### Pass Outcome number 1

[Jump to summary definition](#summary-Pass-1)	|	Previous Pass outcome	|	[Next Pass outcome](#pass-outcome-number-2)

:white_check_mark:Pass outcome
#### Subject detail
|Name|module-src-pwkso|
|----|----|
|Title|Standalone module src/pwkso.ttl from branch main|
|Composition|- [Module pwkso](https://github.com/acimov-tools/model-test/blob/main/src/pwkso.ttl)|

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
|Name|module-src-pwkso|
|----|----|
|Title|Standalone module src/pwkso.ttl from branch main|
|Composition|- [Module pwkso](https://github.com/acimov-tools/model-test/blob/main/src/pwkso.ttl)|

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
|Name|module-src-pwkso|
|----|----|
|Title|Standalone module src/pwkso.ttl from branch main|
|Composition|- [Module pwkso](https://github.com/acimov-tools/model-test/blob/main/src/pwkso.ttl)|

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
|Name|module-src-pwkso|
|----|----|
|Title|Standalone module src/pwkso.ttl from branch main|
|Composition|- [Module pwkso](https://github.com/acimov-tools/model-test/blob/main/src/pwkso.ttl)|

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
|Name|module-src-pwkso|
|----|----|
|Title|Standalone module src/pwkso.ttl from branch main|
|Composition|- [Module pwkso](https://github.com/acimov-tools/model-test/blob/main/src/pwkso.ttl)|

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
