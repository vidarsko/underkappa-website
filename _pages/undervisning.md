---
layout: single # Or a different layout that Minimal Mistakes provides 
title: Undervisning
permalink: /undervisning/ 
classes: wide
author_profile: true
toc: true
toc_label: "Contents"
toc_sticky: true
toc_icon: "list"
use_math: true
toc_levels: 1-3
---

# Bruk Under Kappa i undervisningen

Ingenting gjør oss gladere enn å høre at superhelter og/eller podcasten vår blir brukt i undervisning.
Her er noen forslag:

## Fermiproblemer

Fermiproblemer er en type problem hvor målet er å estimere en størrelse som er vanskelig å måle direkte.
Et klassisk eksempel er å estimere antall pianostemmere i Chicago, eller antall fotballer som passer inn i en buss.
Superhelter er en morsom arena å øve på slike estimeringer, og vi har ofte gjort de i våre episoder. 
Under er en liste med Fermiproblemer som vi har angrepet i podcasten vår.
Som en oppgave i undervisningen, kan dere f.eks. først prøve å løse problemet selv, og deretter høre på episoden (i parantes) hvor vi presenterer vår løsning.

### Hvor sterkt er [Spider-mans](https://youtu.be/FgE0dL17Fnc?si=I_sOOOOBqyTyPb0T) nett? (Episode 1)

<iframe width="200" height="100" src="https://www.youtube.com/embed/FgE0dL17Fnc?si=JPuu7l0DRB0rVUga" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

#### Løsning

For å estimere det, la oss ta utgangspunkt i at Spider-man skal fange en fallende bil på 2 tonn.
Dersom bilen har falt $s=10 \textrm m$, har den fått en fart på

$$
v = \sqrt{2 g s} = 14 \textrm m / \textrm s
$$

Hvis den skal bremses opp ila. $s_2 =10 \textrm m$, så må kraften som nettet bremser med være på 

$$
F = m a = m \frac{v^2}{2 s_2} = 19 600\textrm N,
$$

som kommer i tillegg til bilens tyngde $G = m g = 19620 \textrm N$.
Hvis nettet har en radius på $r=1 \textrm{mm}$, så betyr dettet at nettet må tåle en belastning på

$$
P = \frac{F+G}{\pi r^2} = 12 484 \textrm {MPa}.
$$

Så styrken til Spider-mans nett må være på over 10 000 MPa, 10 ganger sterkere enn edderkoppsilke. 

### Hvor sterk er [Hulken](https://www.youtube.com/watch?v=jolXso_OO-c)? (Episode 7)

<iframe width="560" height="315" src="https://www.youtube.com/embed/jolXso_OO-c?si=3oZ_TkD48URiNujE" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

#### Løsning

For å estimere hvor sterk Hulken er, kan vi starte med en klassisk scene der han løfter en tank eller en stor bygning. 
Anta at han løfter en bygning på 10 etasjer, som veier omtrent 50 000 tonn.
Tyngdekraften på bygningen er

$$
G = m g = 50 000 000 \textrm{ kg} \cdot 9,81 \textrm{ m/s}^2 = 490 500 000 \textrm{ N}.
$$

Hulken løfter bygningen fra bakken, noe som betyr at han må overvinne denne kraften. 
Hvis vi antar at han løfter bygningen med en konstant akselerasjon $a = 1 \textrm{ m/s}^2$, utøver han en kraft på

$$
F = m (g + a) = 50 000 000 \textrm{ kg} \cdot (9,81 \textrm{ m/s}^2 + 1 \textrm{ m/s}^2) = 540 500 000 \textrm{ N}.
$$
 
En sterk vektløfter kan kanskje løfte 200 kg, som gir en kraft på:

$$
F_{\text{menneske}} = 200 \textrm{ kg} \cdot 9,81 \textrm{ m/s}^2 = 1 962 \textrm{ N}.
$$

Som betyr at forholdet mellom hva hulken kan løfte og en sterk mann er

$$
\frac{540 500 000 \textrm{ N}}{1 962 \textrm{ N}} \approx 275 500 \textrm{ ganger større enn en sterk mann}.
$$

### Hvor kraftig er et slag fra [Scorpions](https://www.youtube.com/watch?v=eo_VSTuxCDI&pp=ygUSU2NvcnBpb24gc3BpZGVybWFu) hale? (Episode 11)

<iframe width="560" height="315" src="https://www.youtube.com/embed/eo_VSTuxCDI?si=klSWOeDJpon5wJpy" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

#### Løsning

Anta at halen kan modellere som en stav som svinger om en akse i den ene enden. 
Hvis vi antar at halen har en lengde $l$ og masse $M$, kan vi beregne treghetsmomentet $I$ for halen som

$$
I = \frac{1}{3} M l^2
$$

Rotasjonsenergien $E_w$ til halen når den svinger med en vinkelhastighet $\omega$ er gitt ved

$$
E_w = \frac{1}{2} I \omega^2
$$

Ved å bruke sammenhengen mellom lineær hastighet $v$ på enden av halen og vinkelhastigheten $\omega$, altså $v = \omega l$, kan vi skrive energien som:

$$
E_w = \frac{1}{6} M v^2
$$

Videre kan vi uttrykke massen $M$ som produktet av tetthet $\rho$, tverrsnittsareal $A$, og lengde $l$:

$$
E_w = \frac{1}{6} \rho l A v^2
$$

Ved å bruke følgende verdier for Scorpions hale:
- Tetthet $\rho \approx 8000 \textrm{ kg/m}^3$ (antatt stål),
- Lengde $l = 2 \textrm{ m}$,
- Tverrsnittsareal $A \approx 0.01 \textrm{ m}^2$,
- Hastighet $v \approx 40 \textrm{ m/s}$,

kan vi beregne energien i et slag:

$$
E_w = \frac{1}{6} \cdot 8000 \textrm{ kg/m}^3 \cdot 2 \textrm{ m} \cdot 0.01 \textrm{ m}^2 \cdot (40 \textrm{ m/s})^2 \approx 42 \textrm{ kJ}
$$

Dette tilsvarer omtrent 42 ganger energien i et slag fra en profesjonell bokser. 

### Hvor raskt må [Julenissen](https://www.youtube.com/watch?v=rj7Ofm9xdqU&pp=ygUTc2FudGEgY2xhdXMgcmlkaW5naA%3D%3D) reise rundt for å levere alle julegavene på én natt? (Episode 20)

<iframe width="560" height="315" src="https://www.youtube.com/embed/rj7Ofm9xdqU?si=UtN-GMJE1cPlvwrm" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

#### Løsning

En fin løsning på dette problemet finnes i [Sunniva Roses blogg](https://sunnivarose.no/2018/12/23/rudolf-laget-karbon-fysisk-analyse-julenissen-reinsdyrene-pa-julaften/).
Den diskuteres også i episoden.

### Hvor hardt slår [One Punch Man](https://www.youtube.com/watch?v=x0CJKvevs2M&pp=ygUNb25lIHB1bmNoIG1hbg%3D%3D)? Og hvor rask er han, og hor mye tåler han? (Episode 23)

<iframe width="560" height="315" src="https://www.youtube.com/embed/x0CJKvevs2M?si=u48PVyX6xOwDnGK7" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

#### Løsning: Hvor hardt slår han?

For å estimere hvor hardt One Punch Man slår, kan vi ta utgangspunkt i fysikken bak et slag. Når du bokser, har hånden din en viss bevegelsesmengde, som er produktet av masse og fart. For eksempel, hvis armen din veier 4 kg og beveger seg med en fart på 6 m/s, så har armen din en bevegelsesmengde på:

$$
p = m v = 4 \textrm{ kg} \times 6 \textrm{ m/s} = 24 \textrm{ kg m/s}
$$

Når armen treffer noe og stopper, overføres denne bevegelsesmengden i form av kraft over en viss tid. Newtons andre lov beskriver dette som:

$$
F = \frac{\Delta p}{\Delta t}
$$

La oss nå se på et eksempel fra One Punch Man. I en episode stopper han en meteor som beskrives som en "city killer". Vi antar at meteorens masse er 200 millioner kg, og at den beveger seg med en fart på 20 000 m/s. Bevegelsesmengden til meteoren er dermed:

$$
p = 200 \times 10^6 \textrm{ kg} \times 20 \times 10^3 \textrm{ m/s} = 4 \times 10^{12} \textrm{ kg m/s}
$$

One Punch Man stopper meteoren på omtrent 0,1 sekunder, noe som gir en estimert kraft på:

$$
F = \frac{4 \times 10^{12} \textrm{ kg m/s}}{0,1 \textrm{ s}} = 4 \times 10^{13} \textrm{ N}
$$

Dette tilsvarer 40 billioner Newton, omtrent en million ganger kraften til en vanlig romferge under oppskyting (som genererer 10–30 millioner Newton). Dette gir et inntrykk av hvor ekstremt kraftig One Punch Man slår.

#### Løsning: Hvor rask er han?

I en annen episode hopper One Punch Man til månen i løpet av noen sekunder. La oss anta at han bruker 10 sekunder på å nå månen, som er omtrent 384 400 km unna. Farten hans er da:

$$
v = \frac{384 400 \times 10^3 \textrm{ m}}{10 \textrm{ s}} = 38 \times 10^6 \textrm{ m/s}
$$

Dette er omtrent 38 millioner m/s, som tilsvarer ca. 13 % av lyshastigheten (lyshastigheten er ca. 300 millioner m/s). Ved slike ekstreme hastigheter vil relativistiske effekter begynne å spille inn, hvor tiden går saktere for ham, og han besitter enorme mengder kinetisk energi.

#### Løsning: Hvor mye tåler One Punch Man?


For å forstå hvor mye One Punch Man tåler, kan vi se på en av de mest ekstreme hendelsene fra serien. I en episode blir han utsatt for en stråle som er ment å fordampe hele mennesker. For å forstå hvor mye energi dette innebærer, kan vi se på hvor mye energi som kreves for å kremere en menneskekropp.

I følge en årsberetning fra et krematorium i Vestfold, kreves det ca. 565 kWh for å kremere en kropp. Dette tilsvarer omtrent:

$$
565 \text{ kWh} \times 3.6 \times 10^6 \text{ J/kWh} = 2.03 \times 10^9 \text{ J}
$$

Dette er energien som kreves for å fordampe en enkelt menneskekropp. Men strålen som One Punch Man blir utsatt for, er langt kraftigere. Ifølge serien har denne strålen kraften til å ødelegge planeten, eller i det minste overflaten av planeten.

For å sette dette i perspektiv, kan vi sammenligne med den energien som kreves for å ødelegge en planet, noe som er anslått til å være på rundt $10^{32}$ joule. Dette er omtrent den samme energien som "Death Star" i *Star Wars* ville trenge for å sprenge en planet.

Til tross for denne ekstreme energien, overlever One Punch Man uten problemer. Dette viser at han tåler energiutladninger som tilsvarer det som trengs for å ødelegge en hel planet, noe som gjør ham praktisk talt usårlig for enhver form for angrep vi kan forestille oss. Darth Vader eller noen annen skurk har ingen sjanse mot One Punch Man!


### Gitt at [Påskeharen](https://www.youtube.com/watch?v=AtC3RikdK8U&pp=ygUQVGhlIGVhc3RlciBidW5ueQ%3D%3D) ansetter folk for å produsere og distribuere påskeegg, hvor mange ansatte trenger han? (Episode 26)

<iframe width="560" height="315" src="https://www.youtube.com/embed/AtC3RikdK8U?si=7ejhL77QQMm-KCpm" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

#### Løsning

Basert på beregningene dine:

- Det finnes ca. **2 milliarder barn** i verden.
- Du anslår at **10 %** av disse barna er med på påskejakt, altså **200 millioner barn**.
- Hvert barn finner i gjennomsnitt **10 egg**, noe som gir **2 milliarder egg** som må gjemmes.
- Hvis én person kan gjemme **500 egg** på en dag, trenger påskeharen å ansette **400 000 mennesker** for å kunne gjemme alle disse eggene.

Til sammenligning:

- **Apple** ansetter 161 000 mennesker.
- **Amazon** ansetter 1,5 millioner mennesker.

Dette betyr at påskeharens operasjon krever omtrent **en fjerdedel av Amazons arbeidsstyrke**.


## Utforskningsproblemer

Det er mye å lære i det å forsøke å besvare et spørsmål fra superheltverden.
Målet er å forsøke å ta det man ser i en superhelt, eller en superheltfilm, også forsøke å forklare det med fysikk. 
Dette fører ofte til spennende diskusjoner om begrensninger, antagelser og konsekvenser av fysikkens lover.
Her kan dere gi elevene et utforskningsproblem, og be dem om å fremlegge sin forklaring for resten av klassen, og til slutt kan dere lytte til vår løsning (episode i parantes). 
Dersom noen av elevene gjør en spesielt god jobb, er vi veldig interessert i høre om det!

Løsningene på disse utforskingsproblemene finnes i podcasten.

### Hvordan klarer [Ant-man](https://youtu.be/pWdKf3MneyI?si=NZ2QjnELmpwX5ds-) å krympe slik han gjør? (Episode 2)

<iframe width="560" height="315" src="https://www.youtube.com/embed/pWdKf3MneyI?si=GasP5NfVXRx5kjFX" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

### Hvordan klarer [Captain America](https://www.youtube.com/watch?v=hLUdF8cjzyA)s skjold å absorbere kinetisk energi for så å levere det ut igjen? (Episode 9) 

<iframe width="560" height="315" src="https://www.youtube.com/embed/hLUdF8cjzyA?si=9rvT6baRIP1G2jPj" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

### Hvordan klarer [Hell Cow](https://www.youtube.com/watch?v=JCLtXbX_BpY) å bli omgjort til støv også dukke opp igjen fra tilsynelatende intet? (Episode 13)

<iframe width="560" height="315" src="https://www.youtube.com/embed/JCLtXbX_BpY?si=xoZso3gM_iChC2ft" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

### Hva slags bergart er [The Thing](https://www.youtube.com/watch?v=RQoZ6nmMPgM) lagd av? (Episode 15)

<iframe width="560" height="315" src="https://www.youtube.com/embed/RQoZ6nmMPgM?si=8607OzPY2Fvrber-" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

### Hva er lassoen til [Wonder Woman](https://www.youtube.com/watch?v=czdGc5ADNfU) lagd av? (Episode 21)

<iframe width="560" height="315" src="https://www.youtube.com/embed/czdGc5ADNfU?si=9CWKk9iq4teV7vUA" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

### Hva er adamantiumet i [Wolverine](https://www.youtube.com/watch?v=-sqio1tiPGk)s skjelett laget av? (Episode 22)

<iframe width="560" height="315" src="https://www.youtube.com/embed/-sqio1tiPGk?si=iySQ7anijoV6_oAM" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

### Hvilket grunnstoff er det [Iron Man](https://youtu.be/Ddk9ci6geSs?si=ejvox8mLFCsSF5vR) oppdager i dette klippet? (Episode 24)

<iframe width="560" height="315" src="https://www.youtube.com/embed/Ddk9ci6geSs?si=ejvox8mLFCsSF5vR" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

### Finnes det en fysisk forklaring på hvordan [Professor X](https://www.youtube.com/watch?v=5_v15YvEo7A) kan kontrollere folks tanker? (Episode 28)

<iframe width="560" height="315" src="https://www.youtube.com/embed/5_v15YvEo7A?si=KXz9vSyOxGlJDOwS" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

## Laqe podcast-episode

Elevene kan også lage sin egen podcast, hvor de velger seg en superhelt og diskuterer ulike faglige aspekter ved den.

F.eks.:
* Gå sammen 2 og 2
* Velg to fag, f.eks., fysikk og kjemi
* Time 1: lytt til en episode "Under Kappa"
* Time 2 (fagdag?): Lag en episode hvor dere er programledere

Bruk gjerne [våre lyder og musikk](https://www.dropbox.com/scl/fo/d2pft1lm1sbkv4h1hmpq0/AAx01gEwIIeZfgHxGdnDTqA?rlkey=rliccxypxzg5d3f8us44bpiso&dl=0), og send oss gjerne episodene om de blir bra!
Hvem vet, kanskje vi kan slippe en spesialepisode laget av noen av deres elever?