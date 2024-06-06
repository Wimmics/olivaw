# Test Report Markdown Export

This file is an export of the RDF test report made out of [EARL vocabulary](https://www.w3.org/TR/EARL10/)

This test is powered by Corese, check the [website](https://project.inria.fr/corese/) and the [repository](https://github.com/Wimmics/corese)

The original test report is available in turtle syntax [here](./model-test-manual-NicoRobertIn-2024-06-06T14-32-37.ttl).

# Test Context

Here is some context about under which context this test was made

|Assertor|[NicoRobertIn](https://github.com/NicoRobertIn)|
|----|-----|
|Title|NicoRobertIn using manual script|
|Description|Test triggered by [@NicoRobertIn](https://github.com/NicoRobertIn) by manual trigger|
|Script|[model test suite](https://github.com/Wimmics/olivaw/blob/main/olivaw/test/model/suite.py)
|Date|2024-06-06 14:32:36|

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
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-1">1/4</div>|:exclamation:MinorFail|`module-src-nrv-v1`|[profile-compatibility](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#profile-compatibility)|OWL RL Profile incompatible|[Jump](#minorfail-outcome-number-1)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-2">2/4</div>|:exclamation:MinorFail|`module-src-nrv-v1`|[profile-compatibility](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#profile-compatibility)|OWL QL Profile incompatible|[Jump](#minorfail-outcome-number-2)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-3">3/4</div>|:exclamation:MinorFail|`module-src-nrv-v1`|[profile-compatibility](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#profile-compatibility)|OWL EL Profile incompatible|[Jump](#minorfail-outcome-number-3)|
|[Chapter top](#minorfail-outcomes)|<div id="summary-MinorFail-4">4/4</div>|:exclamation:MinorFail|`module-src-nrv-v1`|[term-referencing](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#term-referencing)|Term not referenced to a module|[Jump](#minorfail-outcome-number-4)|

***

## MinorFail Outcomes Details

This subchapter gives more details to the :exclamation:MinorFail outcomes

### MinorFail Outcome number 1

[Jump to summary definition](#summary-MinorFail-1)	|	Previous MinorFail outcome	|	[Next MinorFail outcome](#minorfail-outcome-number-2)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-src-nrv-v1|
|----|----|
|Title|Standalone module src/nrv&lowbar;v1.ttl from branch main|
|Composition|- [Module nrv&lowbar;v1](https://github.com/acimov-tools/model-test/blob/main/src/nrv_v1.ttl)|

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
|[Section top](#minorfail-outcome-number-1)|Pointer|<pre lang="Turtle"><code>&#60;http://docs.oasis-open.org/legalruleml/ns/v1.0/metamodel#Obligation> a rdfs:Class ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;obligation&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:comment &#34;a Deontic Specification for a state, an act, or a course of ...&#34;,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#34;a situation, an act, or a course of action(s) to which a bea...&#34; ;  &#10;&#32;&#32;&#32;&#32;rdfs:subClassOf &#60;http://docs.oasis-open.org/legalruleml/ns/v1.0/metamodel#DeonticSpecification>,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;nrv:CompensableRequirement,  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;nrv:ViolableRequirement ;  &#10;&#32;&#32;&#32;&#32;owl:unionOf ( nrv:Achievement nrv:Maintenance ) .</code></pre>|
|[Section top](#minorfail-outcome-number-1)|Pointer|<pre lang="Turtle"><code>nrv:NormativeRequirement a rdfs:Class ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;Normative Requirement&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:comment &#34;a requirement implying, creating, or prescribing a norm.&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:subClassOf &#60;http://docs.oasis-open.org/legalruleml/ns/v1.0/metamodel#DeonticSpecification> ;  &#10;&#32;&#32;&#32;&#32;owl:disjointUnionOf ( nrv:CompensableRequirement nrv:NonCompensableRequirement ),  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;( nrv:ViolableRequirement nrv:NonViolableRequirement ),  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;( nrv:PersistentRequirement nrv:NonPersistentRequirement ) .</code></pre>|

***
### MinorFail Outcome number 2

[Jump to summary definition](#summary-MinorFail-2)	|	[Previous MinorFail outcome](#minorfail-outcome-number-1)	|	[Next MinorFail outcome](#minorfail-outcome-number-3)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-src-nrv-v1|
|----|----|
|Title|Standalone module src/nrv&lowbar;v1.ttl from branch main|
|Composition|- [Module nrv&lowbar;v1](https://github.com/acimov-tools/model-test/blob/main/src/nrv_v1.ttl)|

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
|[Section top](#minorfail-outcome-number-2)|Pointer|<pre lang="Turtle"><code>nrv:NormativeRequirement a rdfs:Class ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;Normative Requirement&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:comment &#34;a requirement implying, creating, or prescribing a norm.&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:subClassOf &#60;http://docs.oasis-open.org/legalruleml/ns/v1.0/metamodel#DeonticSpecification> ;  &#10;&#32;&#32;&#32;&#32;owl:disjointUnionOf ( nrv:CompensableRequirement nrv:NonCompensableRequirement ),  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;( nrv:ViolableRequirement nrv:NonViolableRequirement ),  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;( nrv:PersistentRequirement nrv:NonPersistentRequirement ) .</code></pre>|

***
### MinorFail Outcome number 3

[Jump to summary definition](#summary-MinorFail-3)	|	[Previous MinorFail outcome](#minorfail-outcome-number-2)	|	[Next MinorFail outcome](#minorfail-outcome-number-4)

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-src-nrv-v1|
|----|----|
|Title|Standalone module src/nrv&lowbar;v1.ttl from branch main|
|Composition|- [Module nrv&lowbar;v1](https://github.com/acimov-tools/model-test/blob/main/src/nrv_v1.ttl)|

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
|[Section top](#minorfail-outcome-number-3)|Pointer|<pre lang="Turtle"><code>nrv:NormativeRequirement a rdfs:Class ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;Normative Requirement&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:comment &#34;a requirement implying, creating, or prescribing a norm.&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:subClassOf &#60;http://docs.oasis-open.org/legalruleml/ns/v1.0/metamodel#DeonticSpecification> ;  &#10;&#32;&#32;&#32;&#32;owl:disjointUnionOf ( nrv:CompensableRequirement nrv:NonCompensableRequirement ),  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;( nrv:ViolableRequirement nrv:NonViolableRequirement ),  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;( nrv:PersistentRequirement nrv:NonPersistentRequirement ) .</code></pre>|

***
### MinorFail Outcome number 4

[Jump to summary definition](#summary-MinorFail-4)	|	[Previous MinorFail outcome](#minorfail-outcome-number-3)	|	Next MinorFail outcome

:exclamation:MinorFail outcome
#### Subject detail
|Name|module-src-nrv-v1|
|----|----|
|Title|Standalone module src/nrv&lowbar;v1.ttl from branch main|
|Composition|- [Module nrv&lowbar;v1](https://github.com/acimov-tools/model-test/blob/main/src/nrv_v1.ttl)|

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
|[Section top](#minorfail-outcome-number-4)|Pointer|<pre lang="Turtle"><code>:NormativeRequirement a rdfs:Class ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;Normative Requirement&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:comment &#34;a requirement implying, creating, or prescribing a norm.&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:subClassOf &#60;http://docs.oasis-open.org/legalruleml/ns/v1.0/metamodel#DeonticSpecification> ;  &#10;&#32;&#32;&#32;&#32;owl:disjointUnionOf ( :CompensableRequirement :NonCompensableRequirement ),  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;( :ViolableRequirement :NonViolableRequirement ),  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;( :PersistentRequirement :NonPersistentRequirement ) .</code></pre>|
|[Section top](#minorfail-outcome-number-4)|Pointer|<pre lang="Turtle"><code>:CompensableRequirement a rdfs:Class ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;compensable requirement&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:comment &#34;a requirement that can be compensated.&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:subClassOf :NormativeRequirement ;  &#10;&#32;&#32;&#32;&#32;owl:disjointWith :NonCompensableRequirement .</code></pre>|
|[Section top](#minorfail-outcome-number-4)|Pointer|<pre lang="Turtle"><code>:NonCompensableRequirement a rdfs:Class ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;non compensable requirement&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:comment &#34;a requirement that cannot be compensated.&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:subClassOf :NormativeRequirement ;  &#10;&#32;&#32;&#32;&#32;owl:disjointWith :CompensableRequirement .</code></pre>|
|[Section top](#minorfail-outcome-number-4)|Pointer|<pre lang="Turtle"><code>:ViolableRequirement a rdfs:Class ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;violable requirement&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:comment &#34;a requirement that can be violated.&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:subClassOf :NormativeRequirement ;  &#10;&#32;&#32;&#32;&#32;owl:disjointWith :NonViolableRequirement .</code></pre>|
|[Section top](#minorfail-outcome-number-4)|Pointer|<pre lang="Turtle"><code>:NonViolableRequirement a rdfs:Class ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;non violable requirement&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:comment &#34;a requirement that cannot be violated.&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:subClassOf :NormativeRequirement ;  &#10;&#32;&#32;&#32;&#32;owl:disjointWith :ViolableRequirement .</code></pre>|
|[Section top](#minorfail-outcome-number-4)|Pointer|<pre lang="Turtle"><code>:PersistentRequirement a rdfs:Class ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;persistent requirement&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:comment &#34;a requirement that needs to be obeyed for the whole duration...&#34; ;  &#10;&#32;&#32;&#32;&#32;rdfs:subClassOf :NormativeRequirement ;  &#10;&#32;&#32;&#32;&#32;owl:disjointWith :NonPersistentRequirement .</code></pre>|
|[Section top](#minorfail-outcome-number-4)|Pointer|<pre lang="Turtle"><code>:NonPersistentRequirement a rdfs:Class ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;non persistent requirement&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:comment &#34;a requirement that is in force at a particular time point on...&#34; ;  &#10;&#32;&#32;&#32;&#32;rdfs:subClassOf :NormativeRequirement ;  &#10;&#32;&#32;&#32;&#32;owl:disjointWith :PersistentRequirement .</code></pre>|
|[Section top](#minorfail-outcome-number-4)|Pointer|<pre lang="Turtle"><code>:Achievement a rdfs:Class ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;achievement&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:comment &#34;an obligation for which achieving the content at least once ...&#34; ;  &#10;&#32;&#32;&#32;&#32;rdfs:subClassOf &#60;http://docs.oasis-open.org/legalruleml/ns/v1.0/metamodel#Obligation> ;  &#10;&#32;&#32;&#32;&#32;owl:disjointUnionOf ( :PreemptiveAchievement :NonPreemptiveAchievement ),  &#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;( :PerdurantAchievement :NonPerdurantAchievement ) .</code></pre>|
|[Section top](#minorfail-outcome-number-4)|Pointer|<pre lang="Turtle"><code>:Maintenance a rdfs:Class ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;maintenance&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:comment &#34;an obligation that needs to be obeyed for the whole duration...&#34; ;  &#10;&#32;&#32;&#32;&#32;rdfs:subClassOf &#60;http://docs.oasis-open.org/legalruleml/ns/v1.0/metamodel#Obligation> .</code></pre>|
|[Section top](#minorfail-outcome-number-4)|Pointer|<pre lang="Turtle"><code>:Compensation a rdfs:Class ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;compensation&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:comment &#34;a set of penalties or sanctions imposed on the violator ; fu...&#34; ;  &#10;&#32;&#32;&#32;&#32;rdfs:subClassOf &#60;http://docs.oasis-open.org/legalruleml/ns/v1.0/metamodel#Obligation> .</code></pre>|
|[Section top](#minorfail-outcome-number-4)|Pointer|<pre lang="Turtle"><code>:hasCompensation a owl:ObjectProperty ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;has for compensation&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:comment &#34;links a compensable requirement to a compensation.&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:domain :CompensableRequirement ;  &#10;&#32;&#32;&#32;&#32;rdfs:range :Compensation .</code></pre>|
|[Section top](#minorfail-outcome-number-4)|Pointer|<pre lang="Turtle"><code>:CompensatedRequirement a rdfs:Class ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;compensated requirement&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:comment &#34;a requirement violated in a state of affairs and compensated...&#34; ;  &#10;&#32;&#32;&#32;&#32;rdfs:subClassOf :CompensableRequirement .</code></pre>|
|[Section top](#minorfail-outcome-number-4)|Pointer|<pre lang="Turtle"><code>:hasViolation a owl:ObjectProperty ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;has for violation&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:comment &#34;links a violable requirement to a violation.&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:domain :ViolableRequirement ;  &#10;&#32;&#32;&#32;&#32;rdfs:range &#60;http://docs.oasis-open.org/legalruleml/ns/v1.0/metamodel#Violation> .</code></pre>|
|[Section top](#minorfail-outcome-number-4)|Pointer|<pre lang="Turtle"><code>:ViolatedRequirement a rdfs:Class ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;violated requirement&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:comment &#34;a requirement violated by a state of affairs.&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:subClassOf :ViolableRequirement .</code></pre>|
|[Section top](#minorfail-outcome-number-4)|Pointer|<pre lang="Turtle"><code>:hasCompliance a owl:ObjectProperty ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;has for compliance&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:comment &#34;links a violable requirement to compliance.&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:domain :ViolableRequirement ;  &#10;&#32;&#32;&#32;&#32;rdfs:range &#60;http://docs.oasis-open.org/legalruleml/ns/v1.0/metamodel#Compliance> ;  &#10;&#32;&#32;&#32;&#32;owl:propertyDisjointWith :hasViolation .</code></pre>|
|[Section top](#minorfail-outcome-number-4)|Pointer|<pre lang="Turtle"><code>:CompliantRequirement a rdfs:Class ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;compliant requirement&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:comment &#34;a requirement being compliant with a state of affairs.&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:subClassOf :ViolableRequirement .</code></pre>|
|[Section top](#minorfail-outcome-number-4)|Pointer|<pre lang="Turtle"><code>:PreemptiveAchievement a rdfs:Class ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;preemptive achievement requirement&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:comment &#34;an achievement requirement that can be fulfilled even before...&#34; ;  &#10;&#32;&#32;&#32;&#32;rdfs:subClassOf :Achievement .</code></pre>|
|[Section top](#minorfail-outcome-number-4)|Pointer|<pre lang="Turtle"><code>:NonPreemptiveAchievement a rdfs:Class ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;non preemptive achievement requirement&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:comment &#34;an achievement requirement that cannot be fulfilled even bef...&#34; ;  &#10;&#32;&#32;&#32;&#32;rdfs:subClassOf :Achievement .</code></pre>|
|[Section top](#minorfail-outcome-number-4)|Pointer|<pre lang="Turtle"><code>:PerdurantAchievement a rdfs:Class ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;perdurant achievement requirement&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:comment &#34;achievement requirement that persists after being violated.&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:subClassOf :Achievement ;  &#10;&#32;&#32;&#32;&#32;owl:disjointWith :NonPerdurantAchievement .</code></pre>|
|[Section top](#minorfail-outcome-number-4)|Pointer|<pre lang="Turtle"><code>:NonPerdurantAchievement a rdfs:Class ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;non perdurant requirement&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:comment &#34;achievement requirement that does not persist after being vi...&#34; ;  &#10;&#32;&#32;&#32;&#32;rdfs:subClassOf :Achievement ;  &#10;&#32;&#32;&#32;&#32;owl:disjointWith :PerdurantAchievement .</code></pre>|
|[Section top](#minorfail-outcome-number-4)|Pointer|<pre lang="Turtle"><code>:Punctual a rdfs:Class ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;punctual&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:comment &#34;an obligation for which the contents must be immediately ach...&#34; ;  &#10;&#32;&#32;&#32;&#32;rdfs:subClassOf :NonPersistentRequirement ;  &#10;&#32;&#32;&#32;&#32;owl:disjointUnionOf ( :CoOccurantPunctual :NonCoOccurantPunctual ) ;  &#10;&#32;&#32;&#32;&#32;owl:intersectionOf ( :Achievement :Maintenance ) .</code></pre>|
|[Section top](#minorfail-outcome-number-4)|Pointer|<pre lang="Turtle"><code>:CoOccurantPunctual a rdfs:Class ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;co-occurant punctual requirement&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:comment &#34;TODO.&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:subClassOf :Punctual ;  &#10;&#32;&#32;&#32;&#32;owl:disjointWith :NonCoOccurantPunctual .</code></pre>|
|[Section top](#minorfail-outcome-number-4)|Pointer|<pre lang="Turtle"><code>:NonCoOccurantPunctual a rdfs:Class ;  &#10;&#32;&#32;&#32;&#32;rdfs:label &#34;non co-occurant punctual requirement&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:comment &#34;TODO.&#34;@en ;  &#10;&#32;&#32;&#32;&#32;rdfs:subClassOf :Punctual ;  &#10;&#32;&#32;&#32;&#32;owl:disjointWith :CoOccurantPunctual .</code></pre>|

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
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-1">1/5</div>|:white_check_mark:Pass|`module-src-nrv-v1`|[domain-and-range-referencing](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#domain-and-range-referencing)|Domains properly defined|[Jump](#pass-outcome-number-1)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-2">2/5</div>|:white_check_mark:Pass|`module-src-nrv-v1`|[domain-and-range-referencing](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#domain-and-range-referencing)|Ranges properly defined|[Jump](#pass-outcome-number-2)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-3">3/5</div>|:white_check_mark:Pass|`module-src-nrv-v1`|[labeled-terms](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#labeled-terms)|All terms labeled|[Jump](#pass-outcome-number-3)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-4">4/5</div>|:white_check_mark:Pass|`module-src-nrv-v1`|[owl-rl-constraint](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#owl-rl-constraint)|OWL RL consistent|[Jump](#pass-outcome-number-4)|
|[Chapter top](#pass-outcomes)|<div id="summary-Pass-5">5/5</div>|:white_check_mark:Pass|`module-src-nrv-v1`|[terms-differenciation](https://raw.githubusercontent.com/Wimmics/olivaw/main/olivaw/test/olivaw-earl.ttl#terms-differenciation)|Terms differenciated enough|[Jump](#pass-outcome-number-5)|

***

## Pass Outcomes Details

This subchapter gives more details to the :white_check_mark:Pass outcomes

### Pass Outcome number 1

[Jump to summary definition](#summary-Pass-1)	|	Previous Pass outcome	|	[Next Pass outcome](#pass-outcome-number-2)

:white_check_mark:Pass outcome
#### Subject detail
|Name|module-src-nrv-v1|
|----|----|
|Title|Standalone module src/nrv&lowbar;v1.ttl from branch main|
|Composition|- [Module nrv&lowbar;v1](https://github.com/acimov-tools/model-test/blob/main/src/nrv_v1.ttl)|

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
|Name|module-src-nrv-v1|
|----|----|
|Title|Standalone module src/nrv&lowbar;v1.ttl from branch main|
|Composition|- [Module nrv&lowbar;v1](https://github.com/acimov-tools/model-test/blob/main/src/nrv_v1.ttl)|

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
|Name|module-src-nrv-v1|
|----|----|
|Title|Standalone module src/nrv&lowbar;v1.ttl from branch main|
|Composition|- [Module nrv&lowbar;v1](https://github.com/acimov-tools/model-test/blob/main/src/nrv_v1.ttl)|

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
|Name|module-src-nrv-v1|
|----|----|
|Title|Standalone module src/nrv&lowbar;v1.ttl from branch main|
|Composition|- [Module nrv&lowbar;v1](https://github.com/acimov-tools/model-test/blob/main/src/nrv_v1.ttl)|

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
|Name|module-src-nrv-v1|
|----|----|
|Title|Standalone module src/nrv&lowbar;v1.ttl from branch main|
|Composition|- [Module nrv&lowbar;v1](https://github.com/acimov-tools/model-test/blob/main/src/nrv_v1.ttl)|

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
