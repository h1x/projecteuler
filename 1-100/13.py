# Work out the first ten digits of the sum of the following one-hundred 50-digit numbers.

numbers = ["3710728753390210279879799822083759024651013574025",
           "4637693767749000971264812489697007805041701826053",
           "7432498619952474105947423330951305812372661730962",
           "9194221336357416157252243056330181107240615490825",
           "2306758820753934617117198031042104751377806324667",
           "8926167069662363382013637841838368417873436172675",
           "2811287981284997940806548193159262169127588983273",
           "4427422891743252032192358942287679648767027218931",
           "4745144573600130643909116721685684458871160315327",
           "7038648610584302543993961982891759366568675793495",
           "6217645714185656062950215722319658675507932419333",
           "6490635246274190492910143244581382266334794475817",
           "9257586771833721766196375159057923972824559883840",
           "5820356532535939900840263356894883018945862822782",
           "8018119938482628201427819413994056758715117009439",
           "3539866437282711265382998724078447305319010429358",
           "8651550600629586486153207527337195919142051725582",
           "7169388870771546649911559348760353292171497005693",
           "5437007057682668462462149565007647178729443837760",
           "5328265410875682844319119063469403785521777929514",
           "3612327252500029607107508256381565671088525835072",
           "4587657617241097644733911060721826523687722363604",
           "1742370690585186066044820762120981328786073396941",
           "8114266041808683061932846081119106155694051268969",
           "5193432545172838864191804704929321505864256304948",
           "6246722164843507620172791803994469300473295634069",
           "1573244438690812579451408905770622942919710792820",
           "5503768752567877309186254074496984450833039368212",
           "1833638482533015468619612434876768129753437594651",
           "8038628759287849020152168555482871720121925776695",
           "7818283375799310361474035685644909552709786479758",
           "1672632010043689784255353992093183744149780686098",
           "4840309812907779179908821879532736447567559084803",
           "8708698755139271185451707854416185242432069315033",
           "5995940689575653678210707492696653767632623544721",
           "6979395067965269474259770973916669376304263398708",
           "4105268470829908521139942736573411618276031500127",
           "6537860736150108085700914993951255702819874600437",
           "3582903531743471732693212357815498262974255273730",
           "9495375976510530594696606768315657437716740187527",
           "8890280257173322961917666871381993181104877019027",
           "2526768027607800301367868099252546340106163286652",
           "3627021854049770558562994658063623799314074625596",
           "2407448690823117497779236546625724692332281091714",
           "9143028819710328859780666976089293863828502533340",
           "3441306557801612781592181500556186883646842009047",
           "2305308117281643048762379196984248725503663878458",
           "1148769693215490281042402013833512446218144177347",
           "6378329949063625966649858761822122522551248676453",
           "6772018697169854431241957240991395900895231005882",
           "9554825530026352078153229679624948164195386821877",
           "7608532713228572311042480345612486769706450799523",
           "3777424253541129168427686553892620502491032657296",
           "2370191327572567528565324825826546309220705859652",
           "2979886027225833191312637514734199488953476574550",
           "1849570145487928898485682772607771372140379887971",
           "3829820378303147352772158034814451349137322665138",
           "3482954382919991818027891652243102739225112286953",
           "4095795306640523263253804410005965493915987959363",
           "2974615218550237130764225512118369380358038858490",
           "4169811622207297718615823667842468915799353296192",
           "6246795719440126904387710727504810239089552359745",
           "2318970677254791506150550495392297953090112996751",
           "8618808822587531452958409925120382900940777077567",
           "1130673970830472448381653387350234084564705807730",
           "8295917476714036319800818712901187549131054712658",
           "9762333104481838626951545633492636657289756340050",
           "4284628018351707052783183942588214552122725125032",
           "5512160354698120058176216521282765275169129689778",
           "3223819573432933994643750190783694576588335239988",
           "7550616496518477518073816883786109152735792970133",
           "6217784275219262340194239963916804498399317331273",
           "3292418570714734956691667468763466091503591467750",
           "9951867143023521962889489010242332511691361962662",
           "7326746080059154747183079839286853520694694454072",
           "7684182252467441716151403642798227334805555621481",
           "9714261791034259864720451689398942217982608807685",
           "8778364618279934631376775430780936333301898264209",
           "1084880252167467088321512018588354322381287695278",
           "7132961247478246453863699300904931036361976387803",
           "6218407357239979422340623539380833965132740801111",
           "6662789198148808779794187687614423003098449085141",
           "6066182629368283676474477923918033511098906979071",
           "8578694408955299065364044742557608365997664579509",
           "6602439640990538960712019821997604759949019723029",
           "6491398268003297315603712004137790378556608508925",
           "1673093931987275027546890690370753941304265231501",
           "9480937724504879515095410092164586375471059843679",
           "7863916702118749243199570064191796977759902830069",
           "1536871371193661495281130587638027841075444973307",
           "4078992311553556256114232242325503368544248891735",
           "4488991150144064802036906806396067232219320414953",
           "4150312888033953605329934036800697771065056663195",
           "8123488067321014673905856855793458140362782270328",
           "8261657077394832759223284594170652509451232523060",
           "2291880205877731971983945018088807242966198081119",
           "7715854250201654509041324580978688277894872185961",
           "7210783843506918615543566288406225747369228450951",
           "2084960398013400172393067166682355524525280460972",
           "5350353422647252425087405407559178978126433033169"];
           
sum = 0;

for i in range(100):
        sum += int(numbers[i][:12]);

print(str(sum)[:10]);
