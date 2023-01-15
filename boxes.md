---
title: "Boxes with pandoc-latex-environment and awesomebox"
titlepage: true
toc: true
toc-title: "Sommaire"
toc-own-page: true
author: Gregor Walter, KidsLab.de
date: "2022-10-28"
subject: "Markdown"
keywords: [Markdown, Example]
lang: "de"
colorlinks: true
header-includes:
- |
  ```{=latex}
  \usepackage{awesomebox}
  ```
pandoc-latex-environment:
  noteblock: [note]
  tipblock: [tip]
  warningblock: [warning]
  cautionblock: [caution]
  importantblock: [important]
...

# MCreator - Erstelle eigene Mods für Minecraft

## Kurzbeschreibung

Mit [MCreator](https://mcreator.net/), einer Open-Source Entwicklungsumgebung, kann man sehr schnell und einfach eigene Erweiterungen (Mods, Data Packs, Add-Ons) für Minecraft erstellen.

 

**Lizenz:** CC BY 4.0 KidsLab gGmbH

**Zielgruppe:** ab 12 Jahren 

**Kategorie:** [Coding/Design/Gaming]

### Online-Version mit Links zu weiteren zugehörigen Dokumenten

[den Link ergänzen wir, sobald das OER hochgeladen wird]

 

# Einführung

Minecraft ist eines der beliebtesten Computerspiele überhaupt - gerade viele Jugendliche lieben das Spiel. Mit MCreator wird aus dem Spieler ein Macher: man kann das Spiel nach eigenen Ideen weiter entwickeln, eigene Inhalte erstellen und sogar ein ganz individuelles Spiel im Spiel erfinden und programmieren! Der Einstieg gehts sehr schnell, die erste Mod steht nach einer Stunde. Dann gehts aber erst los: die Phantasie der Jugendlichen ist entfacht und die Fragen schießen nur so hoch: "Wie kann ich ... machen?" - perfekt, um weiter ins Programmieren und kreative Gestalten einzusteigen.

# Was brauche ich dafür?

**Hardware:** 	Laptops oder Computer mit Linux (empfohlen), Windows oder MacOS

**Software:** 	MCreator

**Internet:** 	Für die Installation, Workshop grundsätzlich auch ohne Internet möglich

**Sonstiges:** 	… [z.B. Zusatzinfos, Cheat-Sheet mit Kurzbefehlen, etc.)

**Personenanzahl (TN + Mentor\*innen):** … Teilnehmer*innen, … Mentor*innen

# Wie lange dauert der Workshop?

Der Workshop ist in 5 Einheiten aufgeteilt:

| Teil                        | Inhalt                                                       | Dauer |
| --------------------------- | ------------------------------------------------------------ | ----- |
| #1 Einführung               | Installation, Start & erste Mod: Kuchenerz                   | 1:30h |
| #2                          |                                                              | 1:30h |
|                             |                                                              | 1:30h |
|                             |                                                              | 1:30  |
| #5 Abschluss & Präsentation | Hochladen bei GitHub oder GitLab, jeder stellt seine Mod vor |       |



# Vorbereitung

- Installation MCreator
  - Erster Start - dauert sonst zu lange
- Selbst einmal ausprobieren :-)

#  

![Bild - Cover hinten](Bild-Cover-hinten.png) 





![Scratch - Ausdenken, Entwickeln, Teilen 2022-10-26 15-18-46](boxes.assets/Scratch - Ausdenken, Entwickeln, Teilen 2022-10-26 15-18-46.png){ width=10% height=10% }::: caution
Achtung - der Erste Start kann sehr lange dauern, es werden noch Dateien nachgeladen und kompiliert, es wird empfohlen das vor dem Workshop durchzuführen 
:::

# Ablauf

…

[ Strukturiert den Haupttext so, wie es sich aus dem Inhalt ergibt. Schaut euch die existierenden OERs zur Inspiration an. Die Struktur/Abschnitte/Module sollen analog im ZIM-Papier auftauchen ]

 

 

ggf. Schlussbemerkungen/weiterführende Links/Quellen

 

 



This example demonstrates the use of the filter [`pandoc-latex-environments`] to create custom boxes with the [`awesomebox`] package. *pandoc-latex-environment* is a pandoc filter for adding LaTeX environement on specific HTML div tags.


## Box Types

For a list of all available boxes and options visit the [`awesomebox` documentation](https://ctan.org/pkg/awesomebox).

```markdown
::: note
Lorem ipsum dolor ...
:::
```

::: note
Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nam aliquet libero
quis lectus elementum fermentum.

Fusce aliquet augue sapien, non efficitur mi ornare sed. Morbi at dictum
felis. Pellentesque tortor lacus, semper et neque vitae, egestas commodo nisl.
:::

```markdown
::: tip
Lorem ipsum dolor ...
:::
```

::: tip
Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nam aliquet libero
quis lectus elementum fermentum.

Fusce aliquet augue sapien, non efficitur mi ornare sed. Morbi at dictum
felis. Pellentesque tortor lacus, semper et neque vitae, egestas commodo nisl.
:::

```markdown
::: warning
Lorem ipsum dolor ...
:::
```

::: warning
Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nam aliquet libero
quis lectus elementum fermentum.

Fusce aliquet augue sapien, non efficitur mi ornare sed. Morbi at dictum
felis. Pellentesque tortor lacus, semper et neque vitae, egestas commodo nisl.
:::

```caution
::: caution
Lorem ipsum dolor ...
:::
```

::: caution
Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nam aliquet libero
quis lectus elementum fermentum.

Fusce aliquet augue sapien, non efficitur mi ornare sed. Morbi at dictum
felis. Pellentesque tortor lacus, semper et neque vitae, egestas commodo nisl.
:::

```markdown
::: important
Lorem ipsum dolor ...
:::
```

::: important
Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nam aliquet libero
quis lectus elementum fermentum.

Fusce aliquet augue sapien, non efficitur mi ornare sed. Morbi at dictum
felis. Pellentesque tortor lacus, semper et neque vitae, egestas commodo nisl.
:::

One can also use raw HTML `div` tags to create the custom environments.

```markdown
<div class="important">
Lorem ipsum dolor ...
</div>
```

<div class="important">
Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nam aliquet libero
quis lectus elementum fermentum.
</div>

Markdown formatting inside the environments is supported.

::: important
**Lorem ipsum dolor** sit amet, `consectetur adipiscing` elit.

```
if(args.length < 2) {
	System.out.println("Lorem ipsum dolor sit amet");
}
```

*Nam aliquet libero
quis lectus elementum fermentum.*
:::

[`pandoc-latex-environments`]: https://github.com/chdemko/pandoc-latex-environment/
[`awesomebox`]: https://ctan.org/pkg/awesomebox