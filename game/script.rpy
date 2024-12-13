﻿# Vous pouvez placer le script de votre jeu dans ce fichier.

# Déclarez sous cette ligne les images, avec l'instruction 'image'
# ex: image eileen heureuse = "eileen_heureuse.png"

# Déclarez les personnages utilisés dans le jeu.
define i = Character('Ian', color="#0028FF")
define a = Character('Aliya', color="#ffd700")
define u = Character('???', color="#ffd700")
image ian = "Ian.png"
image aliya = "Aliya.png"
image fond = "Fond.jpg"


# Le jeu commence ici
label start:
    play music "Specialisation_Tarot.mp3"
    scene fond
    show ian
    i "Ma première cliente devrait arriver d’une minute à l’autre !"
    i "J’avoue que j’ai le trac, mon premier tirage…"
    i "Pendant toute mon enfance, mes parents m’ont répété à quel point ils me trouvaient beau avec mon jeu de tarot…"
    i "J’espère qu’ils vont être fiers de moi ! Je les appellerai après mon rendez-vous."
    u "Toc toc !"
    i "Entrez !"
    show aliya
    a "Bonjour, c’est bien ici pour la séance avec un voyant ?"
    i "Oui, c’est avec moi !"
    a "Ian? C’est bien toi ?"
    i "{i}Aliya!? C’est celle dont j’étais éperdument amoureux quand j’étais jeune ! Et j’aurais tort de dire qu’elle ne me fait pas de l’effet en ce moment…{/i}"
    i "Oui, haha, Ian du primaire ! Comment vas-tu ?"
    a "En toute honnêteté, si je suis ici, c’est justement parce que quelque chose ne va pas…"
    i "Oh, veux-tu m’en parler avant qu’on commence le tout ? Ça fait longtemps qu’on n’a pas parlé, mais ça me ferait plaisir de t’écouter."
    a "Et bien, c’est par rapport à ma mère et…"
    a "Tu sais quoi ? Je vais mettre tes talents de cartomancien au défi ! Est-ce que tu peux voir son problème ?"
    i "Ce n’est pas aussi simple, mais mon tirage me permettra de le découvrir, oui. Je t’en prie, assieds-toi et laisse-moi t’expliquer ma procédure."
    i "Je vais te faire tirer trois cartes portant soit sur ton passé, ton présent, ton futur, ta personne ou tes motivations."
    i "Tu peux te baser sur ma lecture du tirage précédent pour choisir le thème de ta prochaine carte, pas besoin de prendre une décision maintenant."
    a "Donc, puisque je veux que tu devines pourquoi je suis ici, je choisis comme premier tirage la carte sur mes motivations !"
    i "Parfait ! Je viens de mélanger les cartes. Je vais donc te les présenter. Je te les montre retournées pour ne pas influencer ta décision bien sûr, et tu peux dès maintenant choisir celle qui t’appelle le plus."
    a "Je choisis… Celle-ci !"
    i "...!!!"
    i "{i}Elle a pris l’Arcane sans nom, la carte qui symbolise la mort ! Ça ne peut signifier qu’une chose: sa mère est mourante ! Est-ce que je peux vraiment lui annoncer ça comme ça !?{/i}"
menu:
    "Être honnête sur la signification de la carte":
        jump scene2a
    "Se retenir et présenter la carte avec optimisme":
        jump scene2b

label scene2a:
    i "Aliya, permets-moi de te le demander… Comment va ta mère ?"
    a "P-Pourquoi tu me demandes ça ? Dis-moi ce que ça veut dire !"
    i "Aliya, cette carte n’augure rien de bon. Nommée l’Arcane sans nom, on la présente comme le symbole de la mort."
    a "QUOI !? Non, c’est impossible, je ne peux pas croire ce que tu dis…"
    i "Tu as raison, ces cartes ne représentent pas la vérité absolue."
    i "Il faut savoir juger par soi-même ce que l’on garde ou ce qu’on laisse comme informations."
    i "Cette carte semble toutefois t’avoir fait réagir."
    i "Je tiens donc à m’excuser. Si tu n’es pas à l’aise de continuer, nous pouvons en rester là, ne t’inquiète pas."
    a "Non, ça va, c’est juste que…"
    a "Ma mère est malade. Je n’entrerai pas dans les détails, mais son état s’aggrave de jour en jour."
    a "Les médecins nous ont expliqué que son cas est compliqué et qu’ils font de leur mieux, mais…"
    a "Disons que le manque de retours m’angoisse."
    i "Ce qui t’a motivée à venir est donc d’en savoir plus sur ce qui lui arrive ?"
    a "Pour être franche, je ne sais pas trop…"
    a "J’avoue être un peu fâchée envers les professionnels, rien n’avance…"
    a "J’ai comme voulu me rebeller contre eux en allant voir ailleurs !"
    a "Je me suis dit que, si je ne peux pas avoir confiance en eux, j’allais peut-être pouvoir me fier à un voyant quant à y être !"
    a "Parce qu’on sait à quel point vous avez l’air fiable !"
    i "… Oh."
    a "Excuse-moi, j’ai laissé ma colère parler ! Ce n’est rien contre toi évidemment."
    i "Ne t’en fais pas, tes sentiments sont valides."
    i "Que dirais-tu de passer au tirage de ta prochaine carte ?"
    i "Je te propose d’y aller avec la carte sur ta personne."
    i "Peut-être nous révèlera-t-elle des pistes concernant la bonne façon de réagir ou te comporter !"
    a "J’aime l’idée, allons-y ! Je choisis celle-ci !"
    i "{i}… La carte est celle du Chariot. Elle représente justement la présence de difficultés à vaincre, mais confirme qu’elles seront surmontées. Comment devrais-je lui présenter ça ?{/i}"
menu:
    "Parler davantage des difficultés à vaincre":
        jump scene3a
    "Mettre l’accent sur le triomphe de celles-ci":
        jump scene3b

label scene2b:
    i "… L’Arcane sans nom ! C’est le nom de cette carte, haha !"
    a "Bon, et qu’est-ce qu’elle veut dire ?"
    i "… Vois le bon côté des choses !"
    i "Cette carte peut être synonyme de régénération."
    i "Ce qui t’a poussée à venir, c’est peut-être le besoin de changements, le désir d’un renouveau !"
    a "Dans un certain sens, oui, c’est possible…"
    a "Je t’avoue que l’allure de cette carte ne m’inspire pas beaucoup."
    a "Pourquoi est-ce que l’image montre un squelette ? Je ne vois pas le lien avec ce que tu dis…"
    i "… Les squelettes sont le seul élément qu’il reste du corps après sa décomposition."
    i "Le reste disparaît, s’intègre à la terre et vient nourrir les prochaines pousses !"
    i "C’est le cycle de la vie qui se perpétue !"
    a "C’est un peu étrange, mais si tu le dis…"
    a "Ce qui m’aurait poussée à rencontrer un voyant est de vouloir changer les choses ?"
    a "Mais par rapport à quoi ?"
    i "Et bien, tu m’as dit être venue ici pour ta mère, non ?"
    i "Peut-être qu’elle a une forte emprise sur ta vie et que tu cherches à t’en émanciper ?"
    a "... Si tu le dis."
    i "Peut-être t’empêche-t-elle de suivre tes rêves, peut-être êtes-vous souvent en désaccord ?"
    a "Pour être franche, je n’aime pas la tournure que prennent les choses."
    a "J’aurais peut-être dû mieux me renseigner avant de prendre rendez-vous, j’ai été ridicule…"
    i "Mais non, il y a une première fois à tout et il est possible que les cartes t’apprennent des choses que tu ne souhaites pas connaître !"
    i "Tu peux toujours me le mentionner si je divague sur un sujet sensible, d’accord ?"
    a "D'accord. Merci Ian. Je t’avoue que j’étais un peu surprise de te retrouver ici…"
    i "Moi de même !"
    a "Ça m’intrigue: est-ce que les cartes peuvent t’en apprendre plus sur la personne que je suis devenue ?"
    i "Oui, c’est justement ce que la carte sur ta personne me permettrait d’apprendre ! Veux-tu choisir ta prochaine carte ?"
    a "Hmm... Celle-là !"
    i "{i}… La carte est celle du Chariot. Elle représente la présence de difficultés à vaincre, mais confirme qu’elles seront surmontées. Comment devrais-je lui présenter ça ?{/i}"
menu:
    "Corriger le tir en présentant la vraie nature de sa visite":
        jump scene4a
    "Mettre l’accent sur le triomphe de celles-ci":
        jump scene4b

label scene3a:
    i "Je te présente la carte des difficultés à venir !"
    i "Elle confirme justement que tu vis des temps difficiles."
    a "Tu ne cherches pas à te rendre plus crédible toi ?"
    i "Haha, non, je te promets que c’est ce qu’elle représente !"
    i "Bien qu’elle n’offre pas de solutions à ton problème, elle permet de cibler des comportements à adopter pour parvenir à surmonter le tout."
    i "On parle notamment de courage et de résilience."
    a "Ça, je sais faire ! Tu ne t’en souviens probablement pas, mais j’ai pas mal été secouée au primaire !"
    i "Je t’avoue que, même si j’avais le béguin pour toi, je n’ai jamais eu l’impression d’apprendre à te connaître quand nous étions jeunes…"
    a "Ah, tu n’as pas à t’en faire pour ça ! À 10 ans, on tombe amoureux en passant du temps ensemble à la récré, haha !"
    i "Tu as sûrement raison, mais j’aimerais beaucoup savoir en quoi tu étais résiliente au primaire, justement."
    a "... Je n’ai rien à perdre à tout te raconter, c’est du passé de toute façon."
    a "Mon père et ma mère ont plusieurs années de différence."
    a "Ma mère n’a jamais voulu m’en parler, mais je ne pense pas qu’elle est restée avec lui parce qu’elle l’aimait, disons."
    a "Elle n’avait pas beaucoup d’argent et il lui a offert son support, alors…"
    a "Bref, je suis née quelques années plus tard. Tout allait bien jusqu’à mon entrée à l’école…"
    a "C’est mon père qui m’a déposée. La réaction immédiate des autres élèves a été de me demander pourquoi mon grand-père était là."
    a "Naïve, j’ai tout de suite répliqué avec la vérité. Ah, si j’avais su !"
    a "Par la suite, je suis devenue la risée de l’école. Ça a beaucoup affecté l’enfant que j’étais…"
    a "Nous n’étions pas à la même école secondaire, mais sache que cette information s’est répandue là-bas aussi."
    a "Cerise sur le gâteau, mon père est décédé le jour de mon 13e anniversaire."
    a "Comme j’ai dû quitter l’école rapidement, la rumeur s’est propagée."
    a "« Le père d’Aliya, le vieux cochon, est sûrement mort ! Bonne chose pour elle. »"
    a "Alors voilà… "
    i "Donc il ne te reste que ta mère ? Sache que je suis de tout cœur avec toi, ce que tu vis est déjà difficile, mais surmonter ça toute seule…"
    i "Je ne peux pas le nier, tu as une battante !"
    a "Haha, merci, ça fait du bien d’en parler."
    a "Mais changeons de sujet ! Je ne peux pas repartir d’ici sans avoir vu mon futur !"
    i "Parfait, choisis une carte !"
    a "Voilà!"
    i "{i}La carte des Amoureux ! C’est ta chance, Ian, la fille de tes rêves se tient devant toi, fonce ! En même temps, qu’est-ce qu’elle va penser de moi ? À moins que ce ne soit réciproque…{/i}"
menu:
    "Présenter la carte tout en restant neutre":
        jump scene5a
    "Confesser son amour pour Aliya":
        jump scene5b

label scene3b:
    i "On appelle cette carte le Chariot."
    i "Comme tu peux le voir, elle présente un homme joyeux monté sur son char."
    i "Pourquoi est-il aussi heureux ? C’est parce qu’il est parvenu au bout de son voyage, il a triomphé de la route !"
    a "Ça me semble être une carte pas mal optimiste !"
    i "Tout à fait ! Tu peux être certaine que c’est une carte que l’on aime obtenir pour représenter sa personne !"
    a "Pourquoi ?"
    i "Et bien, euh… Je te donne un exemple."
    i "Lorsque j’étais jeune, j’ai fait un tirage pour mon père."
    i "Il a pigé la carte du Chariot lui aussi."
    i "Il travaillait depuis tout juste un an dans une grosse entreprise et il occupait un poste qui lui demandait de travailler pas mal à l’extérieur de ses heures habituelles."
    i "La semaine après son tirage, la bonne nouvelle est tombée: pour son rendement exceptionnel, il allait obtenir un super bonus !"
    a "Wow, c’est génial ! Mais qu’est-ce que la carte peut représenter dans mon cas ?"
    i "C’est difficile à dire, mais je dirais qu’elle suppose que tu seras récompensée pour tout ce que tu fais pour ta mère."
    a "Genre mon karma ?"
    i "Un peu oui ! Mon père l’avait aussi vu comme un bon présage et il en a profité pour utiliser cet argent pour s’acheter une nouvelle auto !"
    a "Ah, c’est super !"
    a "Dans mon cas, j’espère d’abord obtenir un emploi, puis on verra pour l’achat de la voiture, haha !"
    i "Une chose à la fois, oui !"
    a "Bon, j’avoue ne pas trop savoir à quoi m’attendre avec cette carte, mais si tu me dis que je dois la considérer avec optimisme, c’est ce que je ferai !"
    i "Tout à fait !"
    a "Maintenant que j’en sais plus sur ma personne et sur ce qui m’arrivera…"
    a "Penses-tu qu’on pourrait regarder la carte sur mon passé maintenant ?"
    i "Bien sûr !"
    a "Je choisis celle-ci !"
    i "{i}Le Bateleur, une carte parfaite pour représenter l’enfance ! Sauf que c’est aussi un symbole d’unité ! Je me demande sur quoi je devrais me pencher… En a-t-elle marre que je parle de mon passé ou est-ce que ce serait pertinent ?{/i}"
menu:
    "Parler de l’enfance":
        jump scene6a
    "S’attarder sur le concept de l’unité":
        jump scene6b

label scene4a:
    i "Je te présente la carte des difficultés à venir !"
    i "Est-il possible que tu vives des temps difficiles en ce moment ?"
    a "Pourquoi penses-tu que je suis ici ?"
    i "Et bien, j’ai vu précédemment le conflit avec ta mère, mais je pense qu’il y a autre chose en fait…"
    i "Aliya, permets-moi de te le demander… Comment va ta mère ?"
    a "P-Pourquoi tu me demandes ça ? Dis-moi où tu veux en venir !"
    i "Est-ce que ta mère serait malade par hasard ? Est-il possible qu’il n’y ait pas présence d’un conflit entre vous, mais plutôt d’une barrière invisible qui vous sépare ?"
    a "QUOI !? Non, c’est impossible, je ne peux pas croire ce que tu dis…"
    i "Ai-je dit quelque chose qu’il ne fallait pas ?"
    a "Non, c’est juste que… tu as visé juste, c’est exactement ça qui se passe dans ma vie en ce moment !"
    a "Je t’avoue être perplexe !"
    a "Comment peux-tu te retrouver si loin de la vérité, puis si près avec la lecture d’une seule autre carte !?"
    i "Après avoir vu ta réaction à la carte de l’Arcane sans nom, le Chariot, nom de la carte que tu as pigée pour représenter ta personne, ne pouvait prendre qu’un sens…"
    i "Que ma lecture de la carte précédente était incomplète !"
    a "... Je ne comprends pas."
    i "Les cartes ne m’offrent qu’un aperçu de l’élément tiré, soit tes motivations lors du tirage précédent."
    i "L’idée de faire trois tirages est de venir créer un portrait aussi précis que possible, chaque tirage permettant de se rapprocher de la vérité."
    a "Je ne comprends simplement pas comment l’idée de la maladie t’est venue avec cette carte…"
    i "Simple déduction avec ta réaction à la carte précédente."
    i "Tu t’es offusquée quand j’ai parlé en mal de ta mère…"
    i "Car tu es en réalité très proche d’elle, là pour l’aider même si tu souhaites plus que tout au monde ne plus être dans cette situation…"
    i "C’est alors que l’idée de la maladie m’est apparue, aussi claire que possible."
    a "Si tu le dis… Ça te va si l’on change de thème et qu’on termine avec la carte du passé ?"
    i "Certainement !"
    a "... Celle-ci."
    i "{i}Le Bateleur ! C’est une carte super symbolique pour parler de l’enfance ! Mais devrais-je y aller avec un portrait plus général ou avec mes souvenirs ? Après tout, ce n’est pas une cliente ordinaire, c’est une ancienne camarade d’école !{/i}"
menu:
    "Demeurer professionnel et présenter le symbolisme de la carte":
        jump scene7a
    "Faire des liens avec l’enfance commune et des souvenirs":
        jump scene7b

label scene4b:
    i "On appelle cette carte le Chariot."
    i "Comme tu peux le voir, elle présente un homme joyeux monté sur son char."
    i "Pourquoi est-il aussi heureux ? C’est parce qu’il est parvenu au bout de son voyage, il a triomphé de la route !"
    a "Encore une carte qui me dit de voir le bon côté des choses ?"
    i "Tout à fait ! Tu peux être certaine que c’est une carte que l’on aime obtenir pour représenter sa personne !"
    a "Pourquoi ?"
    i "Et bien, euh… Je te donne un exemple."
    i "Lorsque j’étais jeune, j’ai fait un tirage pour mon père."
    i "Il a pigé la carte du Chariot lui aussi."
    i "Il travaillait depuis tout juste un an dans une grosse entreprise et il occupait un poste qui lui demandait de travailler pas mal à l’extérieur de ses heures habituelles."
    i "La semaine après son tirage, la bonne nouvelle est tombée: pour son rendement exceptionnel, il allait obtenir un super bonus !"
    a "D’accord, mais je ne vois pas de liens à faire avec moi dans ton histoire."
    i "C’est difficile à dire, mais je dirais qu’elle suppose que tu seras sans doute mieux sans ta mère."
    a "N’en reparlons pas d’accord ?"
    i "Euh… Mon père l’avait vu comme un bon présage et il en a profité pour utiliser cet argent pour s’acheter une nouvelle auto lui !"
    a "Je m’en fiche de l’histoire de ton père, c’est de moi qu’il est question là."
    a "Je suis sans emploi, mais pas de stress, j’ai de quoi te payer après…"
    i "Je te fais confiance là-dessus, ne t’en fais pas !"
    a "Bon, j’avoue que je commence à m’ennuyer."
    i "Oh."
    a "Par contre, il y a une dernière chose qui m’intéresse."
    a "Pourrait-on regarder la carte de mon présent ?"
    i "Bien sûr."
    a "Cette carte-là."
    i "{i}… Le Diable ? La carte de la mise en garde ? Mais contre quoi ? Notre rendez-vous ? Ou bien quelque chose d’autre qui m’échappe ?{/i}"
menu:
    "La mettre en garde contre le rendez-vous":
        jump scene8a
    "Se baser sur le sens plus large de la carte":
        jump scene8b

label scene5a:
    i "Cette carte est celle des Amoureux !"
    i "Symbolisant d’abord l’amour, elle représente aussi l’hésitation, le doute."
    i "Il est donc possible que tu sois déchirée entre deux options dans l’avenir !"
    i "Si j’avais un conseil à te donner, ce serait de t’informer et de rester prudente surtout !"
    a "Je me demande quel genre de décision j’aurai à prendre… Une idée ?"
    i "Souvent, un plaisir facile est confronté à une vertu."
    i "C’est donc une opposition entre ce que tu vas vouloir et ce qu’il va te falloir !"
    a "Hmm... Si c’est dans un avenir rapproché, ça a peut-être un lien avec l’offre d’emploi que j’ai reçue."
    i "Raconte-moi ça !"
    a "En gros, je suis à la recherche d’un emploi depuis quelques mois, probablement plus à temps partiel qu’autre chose."
    a "Mais là, surprise ! J’ai reçu un courriel d’une personne voulant acheter les pièces artistiques que je publiais sur les réseaux sociaux pour les revendre !"
    i "Et tu te demandes si tu lui veux, justement ?"
    a "Oui ! Ça me ferait de l’argent pour payer l’essence que j’utilise pour aller voir ma mère à l’hôpital."
    a "Par contre, ce que la personne m’a appris, c’est qu’elle cherche à faire des NFT avec…"
    a "La cause environnementale me tenant à cœur, je pense que je vais refuser cet argent facile !"
    i "Tu restes fidèle à toi-même, je pense que c’est quelque chose que tes futurs employeurs aimeront chez toi !"
    a "Oh, merci, ça fait du bien de l’entendre…"
    a "Tu m’as apporté tant de bons conseils… Mais je réalise qu’on a seulement parlé de moi là !"
    i "Et alors ? C’est la lecture de tes cartes que je devais faire, pas la mienne !"
    a "Peut-être, mais tu es quelqu’un que je connais ! Du moins, que j’aimerais apprendre à connaître de nouveau…"
    a "Ça te dirait de faire une sortie tous les deux un de ces quatre ? Nous pourrions aller marcher et tu pourrais me parler de toi !"
    i "Et aimerais-tu que j’apporte mes cartes pour que tu essaies de m’en faire la lecture ?"
    a "J’adorerais, haha !"
    a "Tu as mon numéro, alors j’attends ton appel ! Prends soin de toi en attendant !"
    i "Toi aussi !"
    hide aliya
    i "… J’ai déjà hâte."
return

label scene5b:
    i "Cette carte est celle des Amoureux !"
    i "Comme son nom l’indique, elle symbolise l’amour."
    i "On l’associe parfois aussi au désir et à la tentation…"
    i "Aliya, n’aurais-tu pas des vues sur quelqu’un par hasard ?"
    a "Non, pas du tout ! J’imagine par contre que la carte ne précise pas si c’est dans un avenir rapproché ou non?"
    i "Non, mais quelque chose en moi me disait que tu avais sans doute un intérêt envers quelqu’un !"
    i "Si de toutes les cartes, c’est elle que tu as pigée, alors il doit sans doute y avoir un élu à ton cœur !"
    a "Haha, mais non je te dis !"
    i "Et si je te disais que c’est le destin qui t’a menée ici ?"
    a "Explique ?"
    i "Et bien, on se retrouve après toutes ces années… Puis tu piges la carte des Amoureux…"
    i "Penses-tu que… Je t’intéresserais ?"
    a "Ian, mais qu’est-ce que tu racontes, tu es rigolo toi !"
    a "On vient à peine de se retrouver et tu parles déjà de vouloir sortir avec moi ?"
    a "Décidément, tu n’as pas changé ! Je te revois me demander la même chose en 6e, hihi !"
    i "Excuse-moi, tu as raison, c’est ridicule de ma part de te demander ça…"
    i "Tu es ma cliente, pas ma future conquête…"
    i "Ça parait que tu es ma première cliente, n’est-ce pas ?"
    a "Oui haha ! Et si j’avais un conseil à te donner…"
    a "Ce serait de mettre de côté ce que tu connais d’une personne avant son rendez-vous et te concentrer sur ce que tu apprends !"
    a "Après tout, ce n’est rien contre toi, c’est juste que…"
    i "Ta mère est la priorité. Je comprends totalement, ne t’en fais pas !"
    a "Merci."
    a "Bon, je pense qu’on a terminé ?"
    i "Oui ! Je te remercie pour ton conseil, je ne l’oublierai pas."
    a "Ça fait plaisir !"
    i "Je demeure quand même inquiet pour toi… Penses-tu que ça va aller ?"
    i "Sache que je suis à un coup de fil près si tu as besoin de parler… Pas avec le cartomancien, avec l’ami !"
    a "Je ne t’oublie pas, Ian. Merci pour tout !"
    hide aliya
    i "…"
    i "Je lui souhaite que tout aille pour le mieux."
return

label scene6a:
    i "Voici la carte du Bateleur !"
    i "On l’appelle aussi le Magicien."
    i "Tu te souviens de ton kit de magie ? Tu l’as apporté à l’école tous les jours pendant un mois complet en 2e année !"
    a "... Oui ! J’avais complètement oublié ! Tu as une sacrée mémoire !"
    i "En toute honnêteté, c’est justement la carte qui me l’a rappelé !"
    a "J’en avais tellement fait sur une si courte période que j’ai fini par me tanner !"
    i "Cette carte montre aussi que tu avais un grand intérêt à apprendre, est-ce vrai ?"
    a "Oui, justement ! J’avais des phases entières pendant lesquelles je n’avais qu’un sujet en tête, la magie par exemple, et je voulais tout apprendre là-dessus !"
    i "Je m’en doutais ! Tu m’as toujours semblé intriguée par quelque chose, allumée par la possibilité de t’instruire dans tous les domaines !"
    a "Oui, tu as raison. Je n’étais peut-être pas la meilleure élève, mais j’aimais découvrir de nouveaux concepts, je voulais tout savoir !"
    i "Comme c’est mignon !"
    i "Et je tiens à ce que tu saches que ce comportement m’avait marqué chez toi."
    a "Oh, raconte-moi !"
    i "Et bien, j’ai toujours eu de la difficulté à trouver des passions."
    i "Tout le monde semblait savoir ce qui l’intéressait, que ce soit les jeux vidéo, le cinéma, le dessin ou bien la lecture…"
    i "Moi, je ne faisais que regarder ce qui était populaire auprès de mes camarades et je suivais le troupeau ...!"
    i "Quand j’ai appris à te connaître, j’ai aussi appris à connaître toutes les possibilités qui s’offraient à moi !"
    i "J’ai beau ne pas être certain de ce qui me passionne réellement encore aujourd’hui, je continue de découvrir de nouvelles choses."
    i "Je t’avoue que tu m’as inspiré à adopter ce comportement, je te remercie !"
    a "Oh, mais ça fait plaisir voyons ! C’est toi qui as choisi d’agir ainsi, je n’ai été que ta source d’inspiration, rien de plus !"
    i "Je tiens quand même à ce que tu saches que tu as un impact positif dans ma vie."
    i "S’il y a bien une chose que tu dois retenir de ce rendez-vous, c’est que tu as l’avenir devant toi. Nous n’avons peut-être pas regardé la carte du futur, mais je ne pense pas que ce soit nécessaire !"
    a "Tu as raison ! C’est maintenant à moi de te remercier pour ton tirage !"
    a "Je repars confiante et je pense que tout va aller pour le mieux. Merci !"
    i "De rien ! Prends soin de toi !"
    hide aliya
    i "… Une première cliente qui sort d’ici en souriant ?"
    i "Je pense que je peux considérer ça comme une réussite ! Il faut que je contacte mes parents et que je leur raconte !"
return

label scene6b:
    i "Voici la carte du Bateleur !"
    i "L’idée principale qu’elle transmet est celle de l’unité."
    a "Qu’est-ce que ça signifie ?"
    i "Chaque carte de tarot est associée à un chiffre."
    i "Celle-ci est la première."
    i "Elle représente donc un passé uni où tout ne semblait former qu’un."
    a "Je t’avoue que je ne suis pas sûre de comprendre comment lier cette carte à un élément de mon passé…"
    i "Peut-être que ton environnement familial était solide. T’entends-tu bien avec ta mère ?"
    a "J’imagine, mais je t’avoue que je ne me suis jamais sentie sur la même longueur d’onde qu’elle…"
    i "Hmm, ce n’est sûrement pas ça alors…"
    a "J’étais enfant unique. Est-ce possible que le fait que cette carte soit la première, donc représentée par le numéro un, soit le lien à faire ?"
    i "Oui, c’est très possible !"
    i "Cette carte offre plusieurs interprétations, et elles sont souvent contradictoires !"
    a "Pas une carte facile à en faire dégager le sens si je comprends bien ?"
    i "Exact !"
    i "Bien que tout semble converger vers l’idée de l’unité et du chiffre un…"
    i "Il n’est pas impossible que le sens réel de la carte m’échappe."
    a "J’ai surtout été élevée par ma mère, donc encore la présence du chiffre un !"
    i "Un élément de plus ! Autre chose te vient en tête ?"
    a "Ça a peut-être rapport, mais j’étais du genre à avoir une passion intense pour quelque chose pendant un moment, puis à ne plus jamais lui prêter attention."
    i "Intéressant ! C’était donc des moments uniques, des instants qui ne se sont produits qu’une seule fois dans ta vie."
    a "Oui !"
    i "Tu as utilisé le mot « passions » pour décrire le tout. Tu devais sans doute te sentir bien, comme fusionnelle avec cet intérêt ?"
    a "Oui !"
    i "Autre chose ?"
    a "Non, pas vraiment, mais je te remercie pour ton tirage. Sur ce, je vais être sur mon départ !"
    i "Parfait, au revoir !"
    hide aliya
    i "… Première séance terminée ! Ce n’était pas si pire, finalement !"
return

label scene7a:
    i "Voici la carte du Bateleur !"
    i "L’idée principale qu’elle transmet est celle de l’unité."
    a "Qu’est-ce que ça signifie ?"
    i "Chaque carte de tarot est associée à un chiffre."
    i "Celle-ci est la première."
    i "Elle représente donc un passé uni où tout ne semblait former qu’un."
    a "Je t’avoue que je ne suis pas sûre de comprendre comment lier cette carte à un élément de mon passé…"
    i "Peut-être avais-tu une tendance à réunir les gens ou à être sur la même longueur d’ondes que les autres ?"
    a "J’imagine, mais je t’avoue que je ne m’en souviens pas…"
    i "Hmm, ce n’est sûrement pas ça alors…"
    i "Il est possible qu’elle représente le fait que tu étais la première à réaliser quelque chose. Une réalisation marquante de ton enfance a peut-être besoin de te revenir en mémoire pour pouvoir aller de l’avant."
    a "D'accord..."
    i "Écoute, cette carte offre plusieurs interprétations, et elles sont souvent contradictoires."
    a "Pas une carte facile à en faire dégager le sens si je comprends bien ?"
    i "Exact !"
    i "Bien que tout semble converger vers l’idée de l’unité et du chiffre un…"
    i "Il n’est pas impossible que le sens réel de la carte m’échappe."
    a "Je comprends, c’est correct…"
    i "Je t’avoue que je n’ai pas d’autres interprétations qui me viennent en tête…"
    a "Je ne te retiendrai pas plus longtemps dans ce cas."
    i "Attends ! Je veux te remercier d’être venue."
    a "Ouais, d’accord, si tu le dis…"
    a "J’avoue que je ne sais pas trop à quoi je m’attendais, je n’ai jamais eu de séance de ce genre…"
    a "Je ne pense pas que c’est ce dont j’avais besoin. Excuse-moi de t’avoir fait perdre ton temps."
    i "Ne dis pas ça !"
    a "D’accord, au revoir."
    i "Au revoir !"
    hide aliya
    i "… Première séance terminée…"
    i "Je ne pense pas avoir compris la raison de sa visite, c’est sûrement pour ça qu’elle semblait déçue en partant…"
    i "J’espère que je ferai mieux avec mes prochains clients."
return

label scene7b:
    i "Voici la carte du Bateleur !"
    i "On l’appelle aussi le Magicien."
    i "On peut comme toi, haha ! Tu disparaissais sans cesse pendant les cours et l’on ne te revoyait pas avant le lendemain !"
    a "... J’aurais préféré que tu ne me rappelles pas ça…"
    i "Ah, excuse-moi, c’est la carte qui a ravivé ce souvenir…"
    a "Est-ce que tu sais réellement qui j’étais ? Qu’est-ce que la carte t’apprend d’autre ?"
    i "Et bien, euh… Je me souviens que tu étais souvent seule."
    a "Une fille sans ami, sans attache, ne pouvant compter sur personne d’autre qu’elle…"
    i "Exactement ! Tu faisais pitié à voir, dans ton coin, pendant la récré. Avais-tu des difficultés d’apprentissage par hasard ?"
    a "Oui, tu as raison. Je n’étais pas une bonne élève, je n’arrivais pas à me concentrer, j’avais trop de choses en tête…"
    i "C’est ce que je pensais…"
    i "J’avais remarqué ce comportement chez toi quand nous étions plus jeunes…"
    a "Oh! Tu penses vraiment ça de moi ?"
    a "Ce n’est pas la carte que tu lis, ce sont juste tes souvenirs qui refont surface !"
    a "Je sais que je n’étais pas parfaite, mais ce n’est pas le moment de renvoyer tous ces mauvais moments en plein dans ma face !"
    a "Tu profites clairement du fait que tu me connais pour me faire suer là !"
    a "À quel point dois-tu me détester pour dire des choses aussi… cruelles ?"
    i "Je ne me fie qu’aux cartes, je te jure !"
    i "C’est vrai que je suis encore débutant dans le domaine, je peux me tromper et —"
    a "Arrête ! Je ne veux plus rien entendre, compris ?"
    i "Sache que je suis désolé."
    i "Je peux peut-être te proposer un dernier tirage pour corriger le tir et —"
    a "Non ! Je veux juste m’en aller !"
    a "Laisse-moi, tu veux ?"
    i "D-D’accord…"
    hide aliya
    i "… Comment ai-je pu l’offusquer autant ?"
    i "Où est-ce que je me suis trompé ?"
return

label scene8a:
    i "Cette carte est celle du Diable…"
    a "Q-Qu’est-ce qu’elle représente ...?"
    i "C’est une mise en garde."
    a "Une mise en garde ? Pour ce qui se passe maintenant ? J-Je…"
    i "MALHEUR À CEUX QUI VONT TROP LOIN."
    a "Ian, est-ce que ça va !? Qu’est-ce qui t’arrive !?"
    a "Je n’aime pas ça !"
    a "Je veux m’en aller, c’est trop pour moi !"
    i "Rah, mais c’est toi qui as insisté pour qu’on termine, non ?"
    i "Cette carte te met en garde de ce rendez-vous."
    i "Peut-être n’aurais-tu jamais dû venir…"
    i "Après tout, tu n’as de cesse de me rabaisser et d’ignorer tout ce que j’ai eu à te dire…"
    a "Je m’excuse, d’accord ? Je vais te prendre au sérieux maintenant, je te jure !"
    i "Trop tard, tu as poussé ma patience à sa limite."
    i "Mais ça ne m’empêchera pas de continuer de t’expliquer ce que la carte représente."
    i "Malheur, malchance et mauvaises nouvelles rythmeraient ton présent si ce n’était pas déjà le cas !"
    a "ARRÊTE ! Je t’en prie, c’est une lecture que je t’ai demandée, pas un mauvais sort…"
    i "Ça t’apprendra à ne pas me prendre au sérieux !"
    i "Tu sauras que le tarot est un art, que seuls quelques élus sont capables de comprendre !"
    a "Mais qui es-tu à la fin !?"
    a "Dans mes souvenirs, tu n’étais pas aussi imbu de toi-même."
    a "Que t’est-il arrivé ?"
    i "Je viens de m’ouvrir les yeux."
    i "Tu es ma cliente. Tu es à ma merci."
    i "Rentre ça dans ta petite tête, veux-tu ?"
    i "Tu n’as aucun pouvoir ici."
    i "Maintenant, je veux que tu retiennes tout ce que tu as appris et que tu t’en serves à bon usage, d’accord ?"
    a "Oui, promis !"
    a "Tout ce que je veux, c’est partir à présent !"
    i "Soit, vas-y. Je ne te retiens plus, tu as appris ta leçon."
    hide aliya
    i "… J’espère qu’elle a compris, on ne me manque pas de respect comme elle l’a fait !"
return

label scene8b:
    i "Cette carte est celle du Diable…"
    a "Q-Qu’est-ce qu’elle représente ?"
    i "Elle te met en garde… contre les excès !"
    a "Les excès ? De quoi ?"
    i "Tu dois être du genre dépensière, peut-être devrais-tu faire attention !"
    a "Je viens juste de te dire que je suis sans emploi, tu ne m’écoutes pas ou quoi ?"
    i "Euh oui, mais… Ça ne veut pas dire que tu ne dépenses pas beaucoup justement !"
    a "Je te confirme que je suis très proche de mes sous."
    i "Alors, sache que le Diable est le Prince de la chaire…"
    i "Peut-être es-tu ce genre de fille qui vendrait son corps au plus offrant ?"
    a "Mais pour qui te prends-tu !?"
    a "Ça ne se dit pas, des choses comme ça !"
    a "Je suis une femme respectable, tu sauras !"
    a "Je pense que j’en ai assez entendu !"
    a "Me faire manquer de respect comme ça est impardonnable !"
    i "Je… Je ne faisais que te révéler ce que les cartes disaient…"
    a "Alors ça veut dire que tu n’es qu’un escroc !"
    a "Un profiteur de la pire espèce !"
    a "Tu ne fais que lire des cartes et dire tout ce qui te passe par la tête !"
    a "J’avais espoir que le tarot serait un art, mais non."
    a "Ce n’est qu’une façon simple de gagner de l’argent sur le dos d’autrui !"
    a "Je ne te pensais pas aussi… pathétique."
    a "Tu n’auras donc jamais changé Ian !"
    a "Toujours aussi seul."
    i "Je… Je…"
    a "Tu sais quoi ? N’en dis pas plus."
    a "J’en ai assez entendu."
    a "Sache que je pars avec la conviction que je ne veux plus jamais te revoir !"
    a "Adieu!"
    i "Attends !"
    a "Quoi ?"
    i "Non, tu sais quoi… Je n’en rajouterai pas. Adieu."
    a "Hmpf !"
    hide aliya
    i "… Elle avait l’air si colérique, mélancolique…"
    i "Elle a sans doute raison, je suis un être pathétique."
return
