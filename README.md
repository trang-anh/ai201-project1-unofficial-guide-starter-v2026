# The Unofficial Guide

Anh Nguyen - `city_guides`

> **This file is your submission.** Fill it in as you go — most sections get
> written during the milestone that produces them, not at the end.
>
> How the starter works, and every command you'll need, is in `RUNNING.md`.
> Leave that file alone.
>
> **Paste everything as text.** No screenshots, no video. A typed table gets
> full credit; a picture of the same table gets none.
>
> Delete these instruction blocks as you replace them. The `<!-- -->` comments
> are notes to you and don't show up when the page renders — you can leave them
> or remove them.

---

# Unit 1

## What This Does

<!-- Three or four sentences. Which corpus you picked, and the kinds of
     questions your system answers. Write it for someone who has never seen
     this repo.

     Milestone 5. -->
I picked `city_guides` corpus which contains specific documents about 9 cities and some 
generalized documents (accessibility, eating, walking, regional transportation, season to visit) about the regions which contains the 9 cities/areas. This system answers 
factual travel questions about the nine cities and the surrounding region using 
information from the city-specific and regional guides.

## Chunking Strategy

**Chunk size:** Variable — one level-2 (##) section per chunk, with the document's level-1 (#) heading included as context.

**Overlap:** None

<!-- What about YOUR documents made you pick these numbers? Short posts and
     long sectioned guides don't want the same chunking, and "800 seemed
     reasonable" earns nothing. Point at something you noticed when you read
     the documents in Milestone 1.

     If you changed your mind partway through, say so and say why. That's worth
     more than pretending you got it right first time.

     Milestone 3. -->

**Reasoning**: 

My city_guides corpus contains relatively long documents (~2,068 characters each), 
but the documents are already organized into meaningful sections using headings. 
Because of that, I decided that one level-2 (##) section should be one chunk instead 
of using a fixed character limit.

I also keep the level-1 (#) document heading in each chunk because some section 
headings, such as ## Straightforward, do not make sense on their own without 
the broader document topic.

I originally used the fixed 800-character chunker, but when I inspected the output, 
some chunks started or ended in the middle of sentences and combined multiple 
unrelated sections. Splitting by existing section boundaries keeps each chunk focused 
on one topic and avoids cutting thoughts in half. For the same reason, I do not use 
overlap, since the chunk boundaries are no longer arbitrary.


## Sample Chunks

<!-- Five chunks, pasted as text. Label each one and name the file it came from
     AND the function that produced it — the grader checks your code against
     what you claim here.

     `python app.py chunks -n 5` prints all three for you. Copy them straight
     across.

     Milestone 3. -->

**Chunk 1** — source: guide_accessibility.md#0 `` — produced by: chunker.py::split_documents ``

```
======================================================================
Chunk 1  |  source: guide_accessibility.md#0  |  produced by: chunker.py::split_documents
======================================================================
# Getting around the region with limited mobility

## Straightforward

**Thornby Wells** is the easiest town in the region. It is flat, compact, and
everything is within three minutes of everything else. Parking is free for two
hours anywhere in town and the station is central. The pump room and gardens
are level throughout.

**Marchwood** has a modern tram network with level boarding on all four lines,
running every 8 minutes on weekdays. The city museum and covered market are both
step-free. The distances between districts are the main consideration.

**Brightwater** is level along the river and through the centre. The mill museum
is step-free. The station is a 15-minute walk from campus on flat ground, or the
shuttle meets the four busiest arrivals.
```

**Chunk 2** — source: guide_corry_vale.md#5 `` — produced by: chunker.py::split_documents ``

```
======================================================================
Chunk 2  |  source: guide_corry_vale.md#5  |  produced by: chunker.py::split_documents
======================================================================
# Corry Vale

## When to go

May to September. Outside those months the pub in the third village closes, the farm shop reduces its hours, and several footpaths become genuinely boggy rather than merely wet. The road is not gritted above the second village and is impassable in snow.
```

**Chunk 3** — source: guide_givens_mill.md#2 `` — produced by: chunker.py::split_documents ``

```
======================================================================
Chunk 3  |  source: guide_givens_mill.md#2  |  produced by: chunker.py::split_documents
======================================================================
# Givens Mill

## Eat and drink

A tearoom attached to the mill, open 10 to 4 daily except Tuesdays, which sells bread made from the flour ground twenty metres away and is the reason most people come. One pub, food served lunchtimes and Thursday to Saturday evenings.
```

**Chunk 4** — source: guide_kestrelford.md#4 `` — produced by: chunker.py::split_documents ``

```
======================================================================
Chunk 4  |  source: guide_kestrelford.md#4  |  produced by: chunker.py::split_documents
======================================================================
# Kestrelford

## Where to stay

Two inns on the square and a handful of rooms above the pubs. Booking ahead matters between May and September and not at all otherwise. There is no accommodation of any kind within four miles of the town in either direction.
```

**Chunk 5** — source: guide_pellew_sands.md#6 `` — produced by: chunker.py::split_documents ``

```
======================================================================
Chunk 5  |  source: guide_pellew_sands.md#6  |  produced by: chunker.py::split_documents
======================================================================
# Pellew Sands

## Practical notes

Cash is still useful at the market and in smaller places, though cards are
accepted almost everywhere now. Mobile coverage is good in the centre and
patchy on the outskirts. The nearest full hospital is in Brightwater; there is
a minor injuries unit locally with limited hours.
```

## Sample Answer

<!-- One complete question and answer, pasted as text, with the source line
     visible. Milestone 4. -->

**Question:**

What is a good place to visit in Corry Vale?

**Answer:**

```
  (best distance 0.262, cutoff 0.6)

According to the documents, the valley itself is the main attraction, and the 12th-century chapel in the second village is also something to see (*guide_corry_vale.md*). Additionally, the Corry Vale circuit is a good walk that takes in three of the four villages (*guide_walking.md* and *guide_corry_vale.md*).

Sources retrieved: guide_corry_vale.md, guide_walking.md

1 model calls this session, 616 tokens (536 in, 80 out)
```

**My relevance cutoff:** 0.45

I chose a cutoff of 0.45 because there was a clear gap
between the in-corpus and out-of-scope questions. 
The highest distance for an in-corpus question was 0.3752, 
while the lowest distance for an out-of-scope question was 0.8350. 
Since my corpus mostly contains specific factual information, 
I wanted a relatively strict cutoff, and 0.45 leaves some room above 
the in-corpus results without getting close to the out-of-scope range.

<!-- The number you set in config.py, and how you got there.

     You ran five questions your corpus covers and the five in OUT_OF_SCOPE
     that it clearly doesn't, and wrote down the best distance for each. What
     did those two groups look like? Where was the gap? Put the actual numbers
     here — the table below wants all ten rows.

     Milestone 4. -->

| Question | In corpus? | Best distance |
|---|---|---|
| Is Brightwater busy in October? | Yes | 0.2983 |
| What are the operation hours of Kestrelford's pub? | Yes | 0.3509 |
| What is a good place to visit in Corry Vale? | Yes | 0.2624 |
| What transportation option is recommended for getting around Marchwood? | Yes | 0.3638 |
| In what area is cash still useful? | Yes | 0.3752 |
| What is the capital of Mongolia? | No | 0.8463 |
| How do I change the oil in a diesel engine? | No | 0.8881 |
| Who won the 1994 World Cup? | No | 0.9968 |
| What is the recommended dosage of ibuprofen for a headache?| No | 0.8350 |
| How do I write a for loop in Rust? | No | 0.8365 |

## How I Used AI

<!-- Two specific moments. For each: what you asked for, what came back, and
     what you changed about it.

     "I asked Claude to write the chunking function from my notes. It ignored
     the overlap, so I added | What are the operation hours of Kestrelford's pub? | Yes |  |that myself" is the level of detail we're after.
     "I used AI to help me code" is not.

     Milestone 5. -->

**1.**

I asked Claude to write my chunking function based on the information i gather of the corpus (long documents, sectioned by headings). 

The first version of the chunking fucntion produce mostly strong chunks but there was one where it was a top level title and introduction of the document by itself. This is because the function was treating all heading levels equally. 

Hence, after checking the chunk outputs, I asked Claude to revise the strategy so that the chunks were spls while also keeping the level 1 heading as context. 

**2.**

I gave Claude the best retrieval distances for my five in-corpus and five out-of-scope questions and asked where it would place the relevance cutoff. It pointed out the large gap between the highest in-corpus distance (`0.3752`) and the lowest out-of-scope distance (`0.8350`), which helped me choose and justify a cutoff of `0.45`.

<!-- ── Stretch features ─────────────────────────────────────────────────────
     Doing one? Say so here BEFORE you start. A feature this README never
     claims earns nothing.
     ───────────────────────────────────────────────────────────────────────── -->

---

# Unit 2

<!-- These sections get ADDED to what's already above. Don't delete or rewrite unit 1 — the point is that someone can see what you said before you knew how it went. -->

## Run Log — Before

<!-- Your five criteria, three runs each. `python run_eval.py --label before`
     runs the questions, puts the OUT_OF_SCOPE ones through the gate, and
     writes it all into results/ for you. Targets come from criteria.md; the
     verdict column is your call.

     Criterion 3 is measured in one deterministic pass rather than three, so
     the same number goes in all three run columns. That's correct, not lazy.

     Milestone 1. -->

| Criterion | Target | Run 1 | Run 2 | Run 3 | Verdict |
|---|---|---|---|---|---|
| 1. Retrieved chunk contains the answer | 4 of 5 | 5/5 | 5/5 | 5/5 | MET |
| 2. Every answer names a source | 5 of 5 | 5/5 | 5/5 | 5/5 | MET |
| 3. Gate stops out-of-corpus questions | 4 of 5 | 5/5 | 5/5 | 5/5 | MET |
| 4. Sampled chunks should contain enough context | 4 of 5 | 5/5 | 5/5 | 5/5 | MET|
| 5. Paraphrased question pairs should retrieve the same key source material | 4 of 5 | 5/5 | 5/5 | 5/5 | MET |

### Criterion 1 (Retrieved chunk contains the answer), Criterion 4 (Sampled chunks should contain enough context) Evidence 
**Function**: `python app.py chunks`

**Output**:
```
python app.py chunks
84 chunks total. Showing 5, spread across the corpus.

Paste these into your README under Sample Chunks. The rubric asks
for the source file and the function that produced them — both are
printed for you below.

======================================================================
Chunk 1  |  source: guide_accessibility.md#0  |  produced by: chunker.py::split_documents
======================================================================
# Getting around the region with limited mobility

## Straightforward

**Thornby Wells** is the easiest town in the region. It is flat, compact, and everything is within three minutes of everything else. Parking is free for two hours anywhere in town and the station is central. The pump room and gardens are level throughout.

**Marchwood** has a modern tram network with level boarding on all four lines, running every 8 minutes on weekdays. The city museum and covered market are both step-free. The distances between districts are the main consideration.

**Brightwater** is level along the river and through the centre. The mill museum is step-free. The station is a 15-minute walk from campus on flat ground, or the shuttle meets the four busiest arrivals.

======================================================================
Chunk 2  |  source: guide_corry_vale.md#5  |  produced by: chunker.py::split_documents
======================================================================
# Corry Vale

## When to go

May to September. Outside those months the pub in the third village closes, the farm shop reduces its hours, and several footpaths become genuinely boggy rather than merely wet. The road is not gritted above the second village and is impassable in snow.

======================================================================
Chunk 3  |  source: guide_givens_mill.md#2  |  produced by: chunker.py::split_documents
======================================================================
# Givens Mill

## Eat and drink

A tearoom attached to the mill, open 10 to 4 daily except Tuesdays, which sells bread made from the flour ground twenty metres away and is the reason most people come. One pub, food served lunchtimes and Thursday to Saturday evenings.

======================================================================
Chunk 4  |  source: guide_kestrelford.md#4  |  produced by: chunker.py::split_documents
======================================================================
# Kestrelford

## Where to stay

Two inns on the square and a handful of rooms above the pubs. Booking ahead matters between May and September and not at all otherwise. There is no accommodation of any kind within four miles of the town in either direction.

======================================================================
Chunk 5  |  source: guide_pellew_sands.md#6  |  produced by: chunker.py::split_documents
======================================================================
# Pellew Sands

## Practical notes

Cash is still useful at the market and in smaller places, though cards are accepted almost everywhere now. Mobile coverage is good in the centre and patchy on the outskirts. The nearest full hospital is in Brightwater; there is a minor injuries unit locally with limited hours.

For each one, ask: could someone answer a question using only this,
without reading what came before or after?
```

### Criterion 2 Evidence:

**Function**: `python run_eval.py --label before`

**From** `results/run_2026-09-23_1926_before.md`:

```
Question: `What are the operation hours of Kestrelford's pub?`

Kestrelford's pubs serve food between 12 and 2 and again between 6 and 8:30
(*guide_kestrelford.md* and *guide_eating.md*).
```
### Criterion 3 Evidence (Gate stops out-of-corpus questions)

**Function**: `python run_eval.py --label before`

**From** `results/run_2026-09-23_1926_before.md`:
```
## The relevance gate on out-of-corpus questions

Produced by `run_eval.py::check_out_of_scope`, cutoff 0.45. Refused 5 of 5.

Retrieval is deterministic and the gate is a comparison against a
fixed number, so these do not vary between runs — one pass over the
list is the whole measurement.

| Out-of-scope question | Best distance | Gate |
|---|---|---|
| What is the capital of Mongolia? | 0.846 | refused |
| How do I change the oil in a diesel engine? | 0.888 | refused |
| Who won the 1994 World Cup? | 0.997 | refused |
| What is the recommended dosage of ibuprofen for a headache? | 0.835 | refused |
| How do I write a for loop in Rust? | 0.836 | refused |
```

### Criterion 5 Evidence (Paraphrased question pairs should retrieve the same key source material)

#### Q1: 

Original: *Is Brightwater busy in October?*

Paraphrase: *Is October a busy time to visit Brightwater?*

**Function**: `python app.py retrieve "Is Brightwater busy in October?"`

`python app.py retrieve "Is October a busy time to visit Brightwater?"`

**Output**:
```
Question: Is Brightwater busy in October?

#   distance   source                           preview
----------------------------------------------------------------------------------------------------
1   0.2983     guide_seasons.md                 # When to visit the region  ## Autumn, September to ...
2   0.3414     guide_brightwater.md             # Brightwater  ## When to go  May and June are the b...
3   0.3869     guide_seasons.md                 # When to visit the region  ## Winter, December to F...
4   0.3888     guide_seasons.md                 # When to visit the region  ## Spring, March to May ...
5   0.3893     guide_regional_transport.md      # Getting around the region  ## The railway  The lin...

Gate: best distance 0.298 is under the 0.45 cutoff
```

```
Question: Is October a busy time to visit Brightwater?

#   distance   source                           preview
----------------------------------------------------------------------------------------------------
1   0.2800     guide_seasons.md                 # When to visit the region  ## Autumn, September to ...
2   0.3310     guide_brightwater.md             # Brightwater  ## When to go  May and June are the b...
3   0.3833     guide_seasons.md                 # When to visit the region  ## Spring, March to May ...
4   0.3983     guide_seasons.md                 # When to visit the region  ## Winter, December to F...
5   0.4147     guide_regional_transport.md      # Getting around the region  ## The railway  The lin...

Gate: best distance 0.280 is under the 0.45 cutoff
```

#### Q2: 

Original: *What are the operation hours of Kestrelford's pub?*

Paraphrase: *When does the pub in Kestrelford serve food?*

**Function**: `python app.py retrieve "What are the operation hours of Kestrelford's pub?"`

`python app.py retrieve "When does the pub in Kestrelford serve food?"`

**Output**:
```
Question: What are the operation hours of Kestrelford's pub?

#   distance   source                           preview
----------------------------------------------------------------------------------------------------
1   0.3509     guide_kestrelford.md             # Kestrelford  ## Eat and drink  Four pubs, two café...
2   0.3906     guide_kestrelford.md             # Kestrelford  ## Where to stay  Two inns on the squ...
3   0.4558     guide_eating.md                  # Eating across the region  ## Opening hours  This c...
4   0.4732     guide_kestrelford.md             # Kestrelford  ## What to see  The market square on ...
5   0.4860     guide_regional_transport.md      # Getting around the region  ## Buses  Three operato...

Gate: best distance 0.351 is under the 0.45 cutoff
```

```
Question: When does the pub in Kestrelford serve food?

#   distance   source                           preview
----------------------------------------------------------------------------------------------------
1   0.2124     guide_kestrelford.md             # Kestrelford  ## Eat and drink  Four pubs, two café...
2   0.2941     guide_eating.md                  # Eating across the region  ## Opening hours  This c...
3   0.3962     guide_kestrelford.md             # Kestrelford  ## Where to stay  Two inns on the squ...
4   0.4388     guide_givens_mill.md             # Givens Mill  ## Eat and drink  A tearoom attached ...
5   0.4399     guide_corry_vale.md              # Corry Vale  ## Eat and drink  One pub in the large...

Gate: best distance 0.212 is under the 0.45 cutoff
```

#### Q3: 

Original: *What is a good place to visit in Corry Vale?*

Paraphrase: *What is worth seeing in Corry Vale?*

**Function**: `python app.py retrieve "What is a good place to visit in Corry Vale?"`

`python app.py retrieve "What is worth seeing in Corry Vale?"`

**Output**:
```
Question: What is a good place to visit in Corry Vale?

#   distance   source                           preview
----------------------------------------------------------------------------------------------------
1   0.2624     guide_corry_vale.md              # Corry Vale  ## Where to stay  Perhaps thirty beds ...
2   0.3416     guide_walking.md                 # Walking in the region  ## Moderate, with hills  Th...
3   0.3480     guide_corry_vale.md              # Corry Vale  ## Getting around  Nothing within the ...
4   0.3726     guide_corry_vale.md              # Corry Vale  ## What to see  The valley itself is t...
5   0.3834     guide_corry_vale.md              # Corry Vale  ## Eat and drink  One pub in the large...

Gate: best distance 0.262 is under the 0.45 cutoff
```

```
Question: What is worth seeing in Corry Vale?

#   distance   source                           preview
----------------------------------------------------------------------------------------------------
1   0.4128     guide_corry_vale.md              # Corry Vale  ## Where to stay  Perhaps thirty beds ...
2   0.4220     guide_walking.md                 # Walking in the region  ## Moderate, with hills  Th...
3   0.4515     guide_corry_vale.md              # Corry Vale  ## When to go  May to September. Outsi...
4   0.4645     guide_corry_vale.md              # Corry Vale  ## Getting around  Nothing within the ...
5   0.4744     guide_corry_vale.md              # Corry Vale  ## What to see  The valley itself is t...

Gate: best distance 0.413 is under the 0.45 cutoff
```

#### Q4: 

Original: *What transportation option is recommended for getting around Marchwood?*

Paraphrase: *What is the best way to get around Marchwood?*

**Function**: `python app.py retrieve "What transportation option is recommended for getting around Marchwood?"`

`python app.py retrieve "What is the best way to get around Marchwood?"`

**Output**:
```
Question: What transportation option is recommended for getting around Marchwood?

#   distance   source                           preview
----------------------------------------------------------------------------------------------------
1   0.3638     guide_marchwood.md               # Marchwood  ## Where to stay  Plentiful and, outsid...
2   0.3836     guide_accessibility.md           # Getting around the region with limited mobility  #...
3   0.4141     guide_marchwood.md               # Marchwood  ## Getting around  A tram network of fo...
4   0.4370     guide_marchwood.md               # Marchwood  ## Eat and drink  The best eating is in...
5   0.4500     guide_marchwood.md               # Marchwood  ## When to go  Any time. This is the on...

Gate: best distance 0.364 is under the 0.45 cutoff
```
```
Question: What is the best way to get around Marchwood?

#   distance   source                           preview
----------------------------------------------------------------------------------------------------
1   0.3418     guide_marchwood.md               # Marchwood  ## Where to stay  Plentiful and, outsid...
2   0.3483     guide_accessibility.md           # Getting around the region with limited mobility  #...
3   0.3827     guide_marchwood.md               # Marchwood  ## Eat and drink  The best eating is in...
4   0.4132     guide_marchwood.md               # Marchwood  ## Getting around  A tram network of fo...
5   0.4197     guide_marchwood.md               # Marchwood  ## When to go  Any time. This is the on...

Gate: best distance 0.342 is under the 0.45 cutoff
```

Q5: 

Original: *In what area is cash still useful?*

Paraphrase: *Where is it still useful to carry cash?*

**Function**: `python app.py retrieve "In what area is cash still useful?"`

`python app.py retrieve "Where is it still useful to carry cash?"`

**Output**:
```
Question: In what area is cash still useful?

#   distance   source                           preview
----------------------------------------------------------------------------------------------------
1   0.3752     guide_corry_vale.md              # Corry Vale  ## Practical notes  Cash is still usef...
2   0.3841     guide_kestrelford.md             # Kestrelford  ## Practical notes  Cash is still use...
3   0.3886     guide_marchwood.md               # Marchwood  ## Practical notes  Cash is still usefu...
4   0.3919     guide_givens_mill.md             # Givens Mill  ## Practical notes  Cash is still use...
5   0.3951     guide_halden_bay.md              # Halden Bay  ## Practical notes  Cash is still usef...

Gate: best distance 0.375 is under the 0.45 cutoff
```

```
Question: Where is it still useful to carry cash?

#   distance   source                           preview
----------------------------------------------------------------------------------------------------
1   0.4315     guide_corry_vale.md              # Corry Vale  ## Practical notes  Cash is still usef...
2   0.4403     guide_kestrelford.md             # Kestrelford  ## Practical notes  Cash is still use...
3   0.4424     guide_marchwood.md               # Marchwood  ## Practical notes  Cash is still usefu...
4   0.4480     guide_pellew_sands.md            # Pellew Sands  ## Practical notes  Cash is still us...
5   0.4493     guide_halden_bay.md              # Halden Bay  ## Practical notes  Cash is still usef...

Gate: best distance 0.432 is under the 0.45 cutoff
```


<!-- Underneath, paste the REAL output for each criterion from one of your
     runs — the actual text your system produced, not a description of it.
     Name the file and function that produced it. -->

## Verdicts

<!-- MET or MISSED for each of the five, against the target you wrote last
     unit — not a new one. Plus a sentence on how you decided. That sentence
     matters most where it was close.

     If your target said 4 of 5 and your runs came out 4, 3, 4, that's a MISS.
     The target has to hold, not show up occasionally.

     Milestone 2. -->

| # | Criterion | Verdict | How I decided |
|---|---|---|---|
| 1 | Retrieved chunks contain the answer | MET | All 5 of 5 test questions retrieved at least one chunk containing the answer, exceeding the target of 4 out of 5. |
| 2 | Every answer names a source | MET | All five generated answers named at least one source document in all three runs, meeting the 5-of-5 target each time. |
| 3 | The relevance gate stops out-of-corpus questions | MET | The relevance gate refused all 5 out-of-scope questions, exceeding the target of 4 out of 5. Because the gate is deterministic, this result is the same across all three run columns. |
| 4 | Sampled chunks contain enough context to be understood on their own | MET | All 5 sampled chunks included the document-level heading, section heading, and enough section content to understand them without reading neighboring chunks, meeting the 4-of-5 target. |
| 5 | Paraphrased question pairs retrieve the same key source material | MET | All 5 paraphrased pairs still retrieved the key material needed for the same question. Some rankings changed, especially for Corry Vale, but the relevant answer-bearing source material still appeared in both retrieval results. |

## Diagnoses

<!-- For each miss: which stage caused it, and how. The stage alone isn't
     enough — you need the mechanism.

     Not a diagnosis: "Question 3 didn't work."
     A diagnosis:     "Question 3 asks about laundry costs. The answer is in
                       one sentence that got split across two chunks, so
                       neither chunk on its own contains it."

     The five stages: loading → chunking → embedding → retrieval → generation.

     Look for a pattern. If three misses all ask about numbers, that's one
     problem, not three.

     Missed nothing? Say so, then say honestly whether your targets were set
     low, and which one you'd tighten and to what.

     Milestone 3. -->

I did not miss any of my five acceptance criteria. Looking back, though, I think some of my targets were a little safe, especially Criterion 5.

For Criterion 5, I only required 4 out of 5 paraphrased question pairs to retrieve the same key source material, but all 5 ended up doing that. If I made the criterion stricter, I would change it to 5 out of 5.

Even though all of the pairs passed, I noticed that paraphrasing could still change the ranking of the retrieved chunks. For example, for the Corry Vale question, the useful What to see chunk was still retrieved for the paraphrased version, but it appeared lower in the results. Because of that, I think requiring all 5 pairs to still retrieve the same key material would be a better test of how consistent the retrieval is when the wording changes.

## The Improvement

**What I changed:**

**Why I picked it:**

<!-- Connect it to a specific diagnosis above in one sentence. If you can't,
     you picked a fix because it sounded impressive. -->

### Run Log — After

<!-- Same format, same five criteria, three runs each.
     `python run_eval.py --label after` -->

| Criterion | Target | Run 1 | Run 2 | Run 3 | Verdict |
|---|---|---|---|---|---|
| 1. Retrieved chunk contains the answer | 4 of 5 |  |  |  |  |
| 2. Every answer names a source | 5 of 5 |  |  |  |  |
| 3. Gate stops out-of-corpus questions | 4 of 5 |  |  |  |  |
| 4. | | | | | |
| 5. | | | | | |

**Did it help?**

<!-- Say plainly whether it did, and how you know. If it made things worse,
     say that — a change that backfired, honestly reported, earns full credit
     and is more interesting than one that worked. What matters is that you can
     tell.

     Milestone 4. -->

## What's Still Broken

<!-- For each criterion still missed after your fix: what you'd do about it,
     and why you stopped where you did.

     "I ran out of time" is fine if it's true. Pretending nothing is left is
     not.

     Milestone 5. -->

## What I'd Do Differently

<!-- Knowing what you know now — which of your five criteria would you write
     differently, and why?

     Milestone 5. -->
