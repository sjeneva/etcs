import requests
import html2text
import os

# Ensure there's a directory to store the files
output_dir = "Korea_SIN_지속가능_extracted_articles"
os.makedirs(output_dir, exist_ok=True)


def extract_specific_part_from_text(text, start_marker, end_marker):
    start_index = text.find(start_marker)
    end_index = text.find(end_marker, start_index) + len(end_marker)
    if start_index != -1 and end_index != -1:
        return text[start_index:end_index]
    return "Content not found."

def extract_text_from_url(url):
    response = requests.get(url)
    response.raise_for_status()  # Raise an error for bad responses (4xx, 5xx)
    full_text = html2text.html2text(response.text)
    specific_part = extract_specific_part_from_text(full_text,  "_닫기_", "기자**")
    return specific_part



base_url = ' https://www.cargotimes.net/news/articleView.html?idxno='
article_partial_urls = [

"320043",	"320020",	"320015",	"320012",	"320009",	"319967",	"319961",	"319910",	"319908",	"319817",	"319754",	"319685",	"319681",	"319591",	"319577",	"319472",	"319385",	"319372",	"319347",	"319325",	"319244",	"319225",	"319149",	"319092",	"319090",	"319047",	"319028",	"318993",	"318971",	"318958",	"318924",	"318851",	"318842",	"318830",	"318824",	"318798",	"318772",	"318763",	"318745",	"318738",	"318735",	"318728",	"318684",	"318654",	"318644",	"318639",	"318637",	"318627",	"318606",	"318575",	"318560",	"318557",	"318517",	"318516",	"318502",	"318478",	"318471",	"318470",	"318459",	"318454",	"318428",	"318390",	"318380",	"318363",	"318353",	"318343",	"318318",	"318307",	"318300",	"318286",	"318282",	"318267",	"318254",	"318231",	"318215",	"318204",	"318202",	"318203",	"318177",	"318148",	"318126",	"318112",	"318102",	"318068",	"318067",	"318050",	"318044",	"318043",	"317951",	"317956",	"317946",	"317911",	"317910",	"317898",	"317892",	"317883",	"317856",	"317855",	"317853",	"317851",	"317835",	"317806",	"317775",	"317774",	"317752",	"317751",	"317743",	"317714",	"317713",	"317686",	"317657",	"317651",	"317634",	"317630",	"317624",	"317619",	"317609",	"317587",	"317550",	"317536",	"317509",	"317508",	"317462",	"317415",	"317406",	"317401",	"317339",	"317326",	"317319",	"317312",	"317306",	"317257",	"317250",	"317229",	"317223",	"317207",	"317153",	"317151",	"317143",	"317130",	"317072",	"317055",	"317007",	"316972",	"316970",	"316964",	"316921",	"316915",	"316902",	"316870",	"316871",	"316843",	"316827",	"316821",	"316787",	"316783",	"316722",	"316702",	"316699",	"316669",	"316633",	"316613",	"316609",	"316602",	"316590",	"316563",	"316547",	"316536",	"316517",	"316506",	"316503",	"316489",	"316486",	"316432",	"316394",	"316373",	"316354",	"316345",	"316318",	"316310",	"316298",	"316291",	"316274",	"316257",	"316249",	"316215",	"316203",	"316160",	"316138",	"316134",	"316128",	"316113",	"316098",	"316087",	"316086",	"316057",	"316016",	"316004",	"315986",	"315978",	"315940",	"315892",	"315890",	"315878",	"315863",	"315830",	"315828",	"315814",	"315798",	"315792",	"315785",	"315770",	"315751",	"315742",	"315677",	"315614",	"315569",	"315562",	"315560",	"315554",	"315491",	"315473",	"315472",	"315471",	"315414",	"315370",	"315360",	"315337",	"315316",	"315310",	"315283",	"315267",	"315264",	"315236",	"315203",	"315188",	"315169",	"315156",	"315138",	"315131",	"315110",	"315088",	"315082",	"315073",	"315039",	"315012",	"314997",	"314996",	"314989",	"314971",	"314960",	"314921",	"314919",	"314898",	"314888",	"314884",	"314795",	"314784",	"314783",	"314736",	"314718",	"314634",	"314511",	"314509",	"314464",	"314438",	"314420",	"314391",	"314380",	"314359",	"314348",	"314337",	"314294",	"314264",	"314263",	"314246",	"314186",	"314183",	"314174",	"314131",	"314069",	"314049",	"314042",	"314033",	"313985",	"313983",	"313957",	"313925",	"313924",	"313896",	"313876",	"313844",	"313804",	"313712",	"313702",	"313682",	"313637",	"313619",	"313525",	"313485",	"313466",	"313459",	"313440",	"313438",	"313436",	"313420",	"313419",	"313418",	"313415",	"313405",	"313391",	"313388",	"313384",	"313363",	"313341",	"313299",	"313246",	"313244",	"313213",	"313202",	"313168",	"313162",	"313158",	"313128",	"313108",	"313065",	"313056",	"313049",	"313047",	"313038",	"313029",	"313012",	"313001",	"312980",	"312924",	"312903",	"312853",	"312839",	"312829",	"312766",	"312747",	"312728",	"312723",	"312703",	"312669",	"312666",	"312650",	"312634",	"312633",	"312593",	"312578",	"312569",	"312551",	"312516",	"312423",	"312417",	"312406",	"312405",	"312374",	"312364",	"312335",	"312333",	"312324",	"312311",	"312278",	"312271",	"312266",	"312246",	"312232",	"312223",	"312222",	"312217",	"312198",	"312195",	"312194",	"312156",	"312052",	"312048",	"312018",	"312005",	"311967",	"311955",	"311909",	"311886",	"311880",	"311846",	"311820",	"311810",	"311796",	"311781",	"311754",	"311699",	"311670",	"311611",	"311557",	"311505",	"311504",	"311503",	"311351",	"311338",	"311286",	"311266",	"311264",	"311195",	"311157",	"311152",	"311135",	"311099",	"311070",	"311027",	"311026",	"310992",	"310990",	"310988",	"310963",	"310956",	"310954",	"310939",	"310918",	"310916",	"310912",	"310890",	"310885",	"310871",	"310858",	"310855",	"310849",	"310843",	"310838",	"310756",	"310747",	"310729",	"310728",	"310669",	"310652",	"310644",	"310616",	"310613",	"310601",	"310600",	"310598",	"310591",	"310582",	"310559",	"310509",	"310508",	"310478",	"310458",	"310441",	"310413",	"310379",	"310355",	"310354",	"310284",	"310267",	"310245",	"310241",	"310178",	"310160",	"310151",	"310074",	"310058",	"310037",	"310036",	"310012",	"310002",	"309962",	"309960",	"309950",	"309934",	"309897",	"309862",	"309856",	"309850",	"309848",	"309823",	"309758",	"309739",	"309735",	"309729",	"309708",	"309699",	"309647",	"309645",	"309640",	"309631",	"309580",	"309575",	"309497",	"309485",	"309399",	"309366",	"309363",	"309339",	"309336",	"309312",	"309302",	"309292",	"309251",	"309228",	"309186",	"309169",	"309158",	"309156",	"309125",	"309122",	"309066",	"309029",	"308994",	"308962",	"308784",	"308771",	"308718",	"308685",	"308680",	"308672",	"308642",	"308636",	"308600",	"308591",	"308554",	"308498",	"308429",	"308426",	"308419",	"308379",	"308342",	"308323",	"308268",	"308244",	"308226",	"308207",	"308199",	"308193",	"308184",	"308182",	"308172",	"308166",	"308161",	"308136",	"308110",	"308100",	"308101",	"308081",	"308078",	"308049",	"308017",	"308013",	"307998",	"307975",	"307970",	"307957",	"307951",	"307934",	"307896",	"307894",	"307884",	"307880",	"307873",	"307869",	"307842",	"307837",	"307807",	"307803",	"307798",	"307788",	"307783",	"307754",	"307737",	"307731",	"307710",	"307712",	"307698",	"307697",	"307667",	"307661",	"307649",	"307647",	"307645",	"307644",	"307627",	"307618",	"307607",	"307596",	"307579",	"307578",	"307568",	"307521",	"307512",	"307508",	"307495",	"307481",	"307465",	"307419",	"307395",	"307392",	"307356",	"307319",	"307305",	"307296",	"307264",	"307257",	"307236",	"307233",	"307220",	"307211",	"307187",	"307135",	"307119",	"307108",	"307084",	"307067",	"307050",	"307049",	"307042",	"307026",	"306964",	"306962",	"306906",	"306904",	"306875",	"306852",	"306817",	"306762",	"306715",	"306687",	"306675",	"306643",	"306583",	"306565",	"306518",	"306472",	"306462",	"306449",	"306448",	"306446",	"306402",	"306350",	"306326",	"306321",	"306314",	"306305",	"306195",	"306138",	"306081",	"306074",	"306066",	"306004",	"305985",	"305974",	"305937",	"305896",	"305862",	"305829",	"305812",	"305802",	"305768",	"305767",	"305753",	"305727",	"305686",	"305670",	"305664",	"305663",	"305661",	"305647",	"305639",	"305632",	"305614",	"305612",	"305597",	"305593",	"305577",	"305575",	"305563",	"305562",	"305546",	"305538",	"305533",	"305512",	"305500",	"305495",	"305478",	"305453",	"305424",	"305385",	"305379",	"305345",	"305322",	"305310",	"305278",	"305276",	"305256",	"305249",	"305239",	"305213",	"305202",	"305177",	"305174",	"305153",	"305125",	"305110",	"305106",	"305095",	"305062",	"305012",	"304999",	"304970",	"304945",	"304923",	"304885",	"304852",	"304818",	"304812",	"304780",	"304746",	"304740",	"304732",	"304714",	"304673",	"304604",	"304598",	"304597",	"304589",	"304583",	"304550",	"304457",	"304437",	"304424",	"304398",	"304372",	"304363",	"304351",	"304343",	"304308",	"304290",	"304245",	"304156",	"304149",	"304138",	"304024",	"303980",	"303979",	"303969",	"303962",	"303947",	"303936",	"303926",	"303919",	"303905",	"303893",	"303875",	"303869",	"303863",	"303826",	"303737",	"303724",	"303720",	"303700",	"303677",	"303589",	"303553",	"303548",	"303526",	"303525",	"303396",	"303393",	"303305",	"303297",	"303277",	"303226",	"303207",	"303149",	"303137",	"303129",	"303125",	"303123",	"303115",	"303117",	"303113",	"302975",	"302961",	"302925",	"302900",	"302867",	"302864",	"302843",	"302835",	"302789",	"302741",	"302733",	"302714",	"302712",	"302612",	"302605",	"302602",	"302591",	"302545",	"302535",	"302529",	"302502",	"302489",	"302437",	"302417",	"302414",	"302408",	"302403",	"302400",	"302398",	"302387",	"302376",	"302357",	"302297",	"302262",	"302259",	"302256",	"302255",	"302202",	"302167",	"302101",	"302068",	"302058",	"302034",	"302010",	"301994",	"301987",	"301961",	"301960",	"301910",	"301900",	"301885",	"301878",	"301854",	"301851",	"301841",	"301694",	"301627",	"301615",	"301592",	"301544",	"301530",	"301460",	"301435",	"301371",	"301289",	"301277",	"301211",	"301206",	"301174",	"301169",	"301122",	"301031",	"300970",	"300901",	"300888",	"300872",	"300745",	"300683",	"300618",	"300539",	"300521",	"300499",	"300480",	"300431",	"300371",	"300356",	"300321",	"300290",	"300218",	"300182",	"300174",	"300077",	"300023",	"300016",	"300008",	"126675",	"126626",	"126574",	"126562",	"126559",	"126532",	"126508",	"126484",	"126481",	"126465",	"126332",	"126326",	"126301",	"126291",	"126272",	"126207",	"126047",	"126023",	"125934",	"125928",	"125871",	"125835",	"125818",	"125599",	"125564",	"125456",	"125440",	"125434",	"125432",	"125431",	"125428",	"125135",	"125128",	"125125",	"125053",	"125047",	"124960",	"124914",	"124912",	"124903",	"124900",	"124894",	"124881",	"124874",	"124868",	"124801",	"124780",	"124749",	"124704",	"124626",	"124617",	"124598",	"124573",	"124571",	"124549",	"124543",	"124541",	"124432",	"124430",	"124331",	"124262",	"124261",	"124245",	"124202",	"124187",	"124171",	"124163",	"124122",	"124112",	"124111",	"124110",	"124089",	"124049",	"124017",	"124012",	"123936",	"123932",	"123901",	"123892",	"123884",	"123829",	"123775",	"123773",	"123718",	"123709",	"123675",	"123654",	"123625",	"123613",	"123606",	"123581",	"123562",	"123558",	"123517",	"123496",	"123490",	"123440",	"123347",	"123341",	"123223",	"123168",	"123151",	"123134",	"123128",	"123087",	"122941",	"122927",	"122905",	"122889",	"122882",	"122824",	"122818",	"122722",	"122710",	"122703",	"122688",	"122657",	"122531",	"122515",	"122409",	"122406",	"122379",	"122325",	"122296",	"122252",	"122213",	"122204",	"122116",	"122115",	"122093",	"122043",	"122003",	"121981",	"121977",	"121918",	"121903",	"121892",	"121803",	"121801",	"121773",	"121763",	"121731",	"121730",	"121676",	"121625",	"121548",	"121499",	"121489",	"121468",	"121430",	"121309",	"121126",	"121050",	"120985",	"120966",	"120942",	"120906",	"120758",	"120691",	"120598",	"120560",	"120517",	"120510",	"120493",	"120442",	"120400",	"120348",	"120343",	"120337",	"120290",	"120279",	"120247",	"120198",	"120146",	"120144",	"120113",	"120094",	"120084",	"120045",	"120034",	"120029",	"120012",	"120011",	"119987",	"119933",	"119858",	"119793",	"119751",	"119750",	"119738",	"119732",	"119727",	"119697",	"119692",	"119623",	"119611",	"119564",	"119556",	"119554",	"119529",	"119498",	"119455",	"119434",	"119420",	"119365",	"119292",	"119270",	"119215",	"119196",	"119185",	"119155",	"119143",	"119123",	"119064",	"118996",	"118955",	"118854",	"118760",	"118759",	"118738",	"118616",	"118537",	"118519",	"118486",	"118466",	"118445",	"118431",	"118423",	"118382",	"118337",	"118328",	"118290",	"118241",	"118211",	"117993",	"117985",	"117949",	"117945",	"117899",	"117860",	"117855",	"117713",	"117690",	"117536",	"117518",	"117112",	"117071",	"117023",	"116998",	"116988",	"116964",	"116950",	"116948",	"116923",	"116817",	"116749",	"116622",	"116567",	"116513",	"116511",	"116431",	"116107",	"116095",	"116081",	"115883",	"115766",	"115762",	"115746",	"115593",	"115517",	"115480",	"115453",	"115448",	"115433",	"115423",	"115371",	"115313",	"115284",	"115173",	"115162",	"115139",	"115022",	"114947",	"114901",	"114839",	"114817",	"114813",	"114800",	"114794",	"114738",	"114734",	"114640",	"114629",	"114579",	"114553",	"114414",	"114234",	"114060",	"113974",	"113969",	"113926",	"113901",	"113884",	"113854",	"113847",	"113745",	"113675",	"113670",	"113665",	"113612",	"113542",	"113511",	"113496",	"113438",	"113437",	"113420",	"113361",	"113337",	"113216",	"113120",	"113119",	"113026",	"113010",	"112912",	"112779",	"112713",	"112696",	"112658",	"112532",	"112357",	"112331",	"112330",	"112277",	"112272",	"112250",	"112241",	"112236",	"112205",	"111932",	"111914",	"111807",	"111643",	"111642",	"111631",	"111627",	"111545",	"111490",	"111470",	"111451",	"111406",	"111382",	"111140",	"111128",	"111042",	"111037",	"111018",	"111011",	"110893",	"110859",	"110857",	"110846",	"110823",	"110734",	"110703",	"110689",	"110592",	"110552",	"110522",	"110503",	"110477",	"110391",	"110304",	"110238",	"109839",	"109781",	"109773",	"109772",	"109753",	"109746",	"109699",	"109662",	"109646",	"109604",	"109595",	"109557",	"109462",	"109440",	"109434",	"109403",	"109386",	"109275",	"109243",	"109234",	"109217",	"109118",	"109110",	"109107",	"109084",	"109080",	"109076",	"109012",	"108995",	"108879",	"108865",	"108845",	"108788",	"108621",	"108577",	"108530",	"108480",	"108423",	"108395",	"108255",	"108232",	"108183",	"108137",	"107856",	"107721",	"107616",	"107582",	"107529",	"107514",	"107495",	"107450",	"107359",	"107220",	"106951",	"106925",	"106894",	"106866",	"106850",	"106841",	"106795",	"106779",	"106740",	"106584",	"106533",	"106511",	"106463",	"106461",	"106435",	"106411",	"106400",	"106359",	"106211",	"106205",	"106202",	"106198",	"106144",	"106045",	"106037",	"105902",	"105831",	"105802",	"105773",	"105743",	"105708",	"105674",	"105635",	"105617",	"105585",	"105575",	"105572",	"105494",	"105493",	"105181",	"105127",	"104767",	"104658",	"104636",	"104605",	"104588",	"104388",	"104221",	"104178",	"104153",	"104106",	"104063",	"103899",	"103832",	"103772",	"103764",	"103634",	"103633",	"103624",	"103455",	"103354",	"103338",	"103330",	"103328",	"103303",	"103158",	"103132",	"103092",	"103090",	"103065",	"102943",	"102822",	"102750",	"102593",	"102331",	"102328",	"102275",	"102270",	"101993",	"101829",	"101819",	"101802",	"101397",	"101360",	"101358",	"101303",	"101274",	"101174",	"100974",	"100873",	"100764",	"100687",	"100677",	"100655",	"100625",	"100588",	"100564",	"100483",	"100446",	"100354",	"100280",	"100233",	"100222",	"100221",	"100133",	"100023",	"99891",	"99772",	"99677",	"99659",	"99595",	"99577",	"99555",	"99516",	"99508",	"99480",	"99378",	"99346",	"99340",	"99127",	"99062",	"98983",	"98982",	"98898",	"98862",	"98609",	"98558",	"98369",	"98359",	"98302",	"98271",	"97903",	"97888",	"97849",	"97781",	"97777",	"97745",	"97685",	"97597",	"97121",	"97039",	"97032",	"96964",	"96825",	"96765",	"96706",	"96687",	"96678",	"96601",	"96584",	"96531",	"96512",	"96503",	"96498",	"96496",	"96494",	"96470",	"96463",	"96462",	"96434",	"96360",	"96334",	"96182",	"96175",	"95809",	"95727",	"95722",	"95670",	"95552",	"95541",	"95490",	"95446",	"95439",	"95436",	"95428",	"95392",	"95388",	"95379",	"95276",	"95197",	"95189",	"95122",	"95113",	"95002",	"94947",	"94898",	"94892",	"94890",	"94868",	"94833",	"94775",	"94617",	"94569",	"94435",	"94369",	"94234",	"94213",	"94197",	"94136",	"93994",	"93993",	"93950",	"93881",	"93711",	"93698",	"93696",	"93685",	"93660",	"93617",	"93572",	"93522",	"93446",	"93425",	"93407",	"93369",	"93333",	"93289",	"93238",	"93091",	"93032",	"92928",	"92715",	"92611",	"92484",	"92229",	"92188",	"92120",	"92059",	"92020",	"91991",	"91905",	"91863",	"91780",	"91754",	"91631",	"91553",	"91301",	"91232",	"91195",	"91114",	"91075",	"91019",	"91016",	"90974",	"90946",	"90939",	"90933",	"90932",	"90923",	"90725",	"90631",	"90556",	"90498",	"90448",	"90307",	"90239",	"90208",	"90182",	"90075",	"89919",	"89854",	"89659",	"89641",	"89637",	"89631",	"89540",	"89454",	"89418",	"89354",	"89266",	"89256",	"89211",	"89201",	"89099",	"89056",	"88945",	"88897",	"88878",	"88864",	"88736",	"88728",	"88621",	"88578",	"88370",	"88343",	"88329",	"88296",	"88291",	"88273",	"88262",	"88258",	"88236",	"88181",	"88105",	"88068",	"87904",	"87759",	"87730",	"87682",	"87583",	"87539",	"87482",	"87473",	"87253",	"87230",	"87115",	"86861",	"86817",	"86774",	"86759",	"86708",	"86695",	"86684",	"86548",	"86540",	"86444",	"86409",	"86213",	"86173",	"85944",	"85849",	"85799",	"85712",	"85614",	"85435",	"85266",	"85241",	"85234",	"84951",	"84701",	"84613",	"84536",	"84465",	"84365",	"84298",	"84262",	"84244",	"84205",	"84110",	"84075",	"84038",	"83927",	"83922",	"83909",	"83859",	"83754",	"83598",	"83577",	"83575",	"83288",	"83169",	"83156",	"83073",	"83017",	"82999",	"82995",	"82918",	"82901",	"82867",	"82739",	"82699",	"82687",	"82662",	"82347",	"82235",	"82215",	"82174",	"82167",	"82133",	"82003",	"81995",	"81989",	"81901",	"81815",	"81698",	"81625",	"81613",	"81510",	"81336",	"81177",	"80983",	"80885",	"80859",	"80766",	"80483",	"80272",	"80260",	"80198",	"80178",	"80164",	"80142",	"80100",	"80015",	"80007",	"79929",	"79908",	"79890",	"79714",	"79711",	"79621",	"79581",	"79481",	"79416",	"79376",	"79259",	"79194",	"79146",	"79093",	"79032",	"79005",	"78989",	"78982",	"78801",	"78795",	"78794",	"78741",	"78619",	"78544",	"78542",	"78459",	"78401",	"78325",	"78259",	"78087",	"77966",	"77904",	"77855",	"77837",	"77826",	"77793",	"77683",	"77628",	"77324",	"77278",	"77207",	"77062",	"77042",	"76980",	"76973",	"76870",	"76805",	"76624",	"76602",	"76289",	"76226",	"75938",	"75641",	"75584",	"75556",	"75479",	"75372",	"75039",	"74983",	"783",	"74865",	"74834",	"74779",	"74765",	"74731",	"74593",	"74582",	"74543",	"74519",	"74498",	"74385",	"74313",	"74291",	"74284",	"74270",	"74263",	"74257",	"74185",	"74048",	"74041",	"74032",	"73933",	"73923",	"73865",	"73842",	"73634",	"73592",	"73438",	"73435",	"73422",	"73214",	"73180",	"73140",	"73100",	"72911",	"72565",	"72137",	"72089",	"71915",	"71880",	"71844",	"71794",	"71558",	"71530",	"71433",	"70945",	"70867",	"70654",	"70633",	"70517",	"70324",	"70182",	"69934",	"69724",	"69604",	"69507",	"69487",	"69307",	"69154",	"69136",	"69079",	"69039",	"69032",	"69014",	"68839",	"68599",	"68198",	"68056",	"67807",	"67766",	"67024",	"66604",	"66476",	"66370",	"66093",	"66020",	"65991",	"65960",	"65836",	"65781",	"65279",	"65158",	"64835",	"64834",	"64594",	"64257",	"63953",	"63739",	"63647",	"63434",	"63417",	"63319",	"63057",	"62903",	"62834",	"62677",	"62664",	"62536",	"62530",	"62073",	"61975",	"61950",	"61680",	"61672",	"61496",	"61339",	"61336",	"60450",	"60241",	"60183",	"59984",	"59563",	"58341",	"57798",	"57635",	"57100",	"57091",	"57059",	"57027",	"56734",	"56574",	"56493",	"56416",	"55862",	"55715",	"55197",	"55112",	"54736",	"54574",	"54288",	"54154",	"54123",	"54062",	"54039",	"53963",	"53936",	"53484",	"53274",	"53047",	"52976",	"52010",	"51999",	"51828",	"51634",	"51188",	"51009",	"50901",	"50667",	"50598",	"49064",	"48973",	"48940",	"48859",	"48858",	"48857",	"48778",	"48752",	"48634",	"48633",	"48364",	"48226",	"47428",	"47259",	"46404",	"46095",	"45576",	"45518",	"45501",	"44600",	"44414",	"43866",	"43829",	"43803",	"43571",	"43568",	"42837",	"42536",	"41865",	"41517",	"41493",	"40354",	"40281",	"40168",	"39482",	"39451",	"38206",	"37480",	"37278",	"37235",	"36682",	"35411",	"35404",	"35018",	"34941",	"34421",	"33843",	"32785",	"32477",	"32466",	"32058",	"22178",	"21908",	"21778",	"538",


]

for idx, partial_url in enumerate(article_partial_urls, start=1):
    full_url = base_url + partial_url
    print(f"Extracting content from: {full_url}")
    try:
        article_text = extract_text_from_url(full_url)
        # Extract article ID from URL for filename
        article_id = partial_url.split('=')[-1]
        file_path = os.path.join(output_dir, f"article_{article_id}.txt")

        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(article_text)

        print(f"Content saved to {file_path}")
        print("\n---\n")
    except Exception as e:
        print(f"Failed to extract content from {full_url}. Error: {e}")
        print("\n---\n")
