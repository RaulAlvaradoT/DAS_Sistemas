import redis
import json

personas = [{
        "id":1, 
        "first_name":"Adelice", 
        "last_name":"Castillon", 
        "email":"acastillon0@intel.com", 
        "gender":"Male", 
        "ip_address":"110.188.66.73", 
        "school_number":"ca2bae7e-c200-4c5b-97ba-f14407cb19c5"
    }, 

    {
        "id":2, 
        "first_name":"Demott",
        "last_name":"Adderson",  
        "email":"dadderson1@weebly.com",  
        "gender":"Agender",  
        "ip_address":"116.156.113.180",  
        "school_number":"ab1552c7-5a48-448e-9563-f9236fd65d93"
    },  

    {
        "id":3,  
        "first_name":"Sheelagh",  
        "last_name":"Proven",  
        "email":"sproven2@sitemeter.com",  
        "gender":"Male",  
        "ip_address":"251.30.197.124", 
        "school_number":"2f90077f-d559-41d8-a687-83732aab5f68"
    },

    {
        "id":4, 
        "first_name":"Nerita", 
        "last_name":"Wicklen", 
        "email":"nwicklen3@auda.org.au", 
        "gender":"Bigender", 
        "ip_address":"187.71.103.59", 
        "school_number":"eece1f02-1fbc-4da1-bf4d-9a27d6243631"
    },

    {
        "id":5, 
        "first_name":"Maribeth", 
        "last_name":"Pischof", 
        "email":"mpischof4@scientificamerican.com", 
        "gender":"Polygender", 
        "ip_address":"108.175.50.222", 
        "school_number":"07b8f02a-0ae6-4c30-a812-4f56f6a21261"
    }, 

    {
        "id":6, "first_name":"Sansone", 
        "last_name":"Scading", 
        "email":"sscading5@sun.com", 
        "gender":"Polygender", 
        "ip_address":"138.116.69.35", 
        "school_number":"2b7d2a4f-39db-4d6f-aeba-cb3d38fc3aa0"
    },

    {
        "id":7, 
        "first_name":"Archer", 
        "last_name":"Wiltshear", 
        "email":"awiltshear6@engadget.com", 
        "gender":"Bigender", 
        "ip_address":"23.152.108.252", 
        "school_number":"f5cf8d2d-9b53-42fb-a8df-c2cc2302a52d"
    },
     
    {
        "id":8, 
        "first_name":"Fulvia", 
        "last_name":"Pieche", 
        "email":"fpieche7@printfriendly.com", 
        "gender":"Bigender", 
        "ip_address":"233.71.161.222", 
        "school_number":"eda09193-214d-4f87-88f8-eaf5793597a6"
    },

    {
        "id":9, 
        "first_name":"Sebastiano", 
        "last_name":"Chapelhow", 
        "email":"schapelhow8@rakuten.co.jp", 
        "gender":"Female", 
        "ip_address":"3.238.40.142", 
        "school_number":"6a3f96ae-5d6d-429e-a7fe-645517e3431c"
    },

    {
        "id":10, 
        "first_name":"Drusi", 
        "last_name":"Wethered", 
        "email":"dwethered9@bloomberg.com", 
        "gender":"Polygender", 
        "ip_address":"70.107.203.97", 
        "school_number":"b5fe5ac6-3423-40ed-840d-9e4355fbe014"
    },

    {
        "id":11, 
        "first_name":"Karisa", 
        "last_name":"Downton", 
        "email":"kdowntona@topsy.com", 
        "gender":"Non-binary", 
        "ip_address":"109.243.108.166", 
        "school_number":"72ef95db-f686-4d43-9ad6-1236c9f8a82d"
    }, 
    {
        "id":12, 
        "first_name":"Aundrea", 
        "last_name":"Havercroft", 
        "email":"ahavercroftb@stumbleupon.com", 
        "gender":"Agender", 
        "ip_address":"28.136.130.83", 
        "school_number":"fe4a4e70-c9db-4535-964e-2f9481012276"
    },

    {
        "id":13, 
        "first_name":"Antony", 
        "last_name":"Covington", 
        "email":"acovingtonc@theglobeandmail.com", 
        "gender":"Polygender", 
        "ip_address":"161.236.198.121", 
        "school_number":"8a0f2c1a-ab47-4bba-bf7b-00c165835f31"
    },

    {
        "id":14,
        "first_name":"Angela", 
        "last_name":"Deeley", 
        "email":"adeeleyd@arstechnica.com", 
        "gender":"Genderqueer", 
        "ip_address":"186.32.123.74", 
        "school_number":"929499c0-679a-4dec-9e7a-7ca3d34cc8f0"
    },

    {
        "id":15, 
        "first_name":"Lorry", 
        "last_name":"Stienham", 
        "email":"lstienhame@usnews.com", 
        "gender":"Genderqueer", 
        "ip_address":"69.82.111.38", 
        "school_number":"f0cf1b1a-d205-43f0-8874-2ef61d8500e8"
    },

    {
        "id":16, 
        "first_name":"Pacorro", 
        "last_name":"Venard", 
        "email":"pvenardf@bbc.co.uk", 
        "gender":"Genderqueer", 
        "ip_address":"196.63.55.75", 
        "school_number":"6906e51a-9d1e-48ca-97c2-dd8c0f21ec4e"
    },

    {
        "id":17, 
        "first_name":"Anthe", 
        "last_name":"Lawfull", 
        "email":"alawfullg@gizmodo.com", 
        "gender":"Genderfluid", 
        "ip_address":"22.98.130.158", 
        "school_number":"6e824271-2486-4b7a-8ffb-e59f9b6301a6"
    },

    {
        "id":18, 
        "first_name":"Rozella", 
        "last_name":"Herrieven", 
        "email":"rherrievenh@cmu.edu", 
        "gender":"Bigender", 
        "ip_address":"123.54.181.103", 
        "school_number":"21aa944c-f6c3-4a14-916e-6b3635cba6e5"
    },

    {
        "id":19, 
        "first_name":"Marni", 
        "last_name":"Dann", 
        "email":"mdanni@over-blog.com", 
        "gender":"Female", 
        "ip_address":"9.31.177.21", 
        "school_number":"25c52d71-bd1b-4216-9cc3-a7d92d20bd1c"
    },
     
    {
        "id":20, 
        "first_name":"Cybill", 
        "last_name":"Tomanek", 
        "email":"ctomanekj@abc.net.au", 
        "gender":"Genderqueer", 
        "ip_address":"111.21.250.191", 
        "school_number":"55172521-bb1f-47e4-9cfa-b8fae63da884"
    },

    {
        "id":21, 
        "first_name":"Wyatt", 
        "last_name":"Shurlock", 
        "email":"wshurlockk@cmu.edu", 
        "gender":"Agender", 
        "ip_address":"127.122.80.19", 
        "school_number":"46009186-567f-44bd-acb9-85702d4558b2"
    },

    {
        "id":22, 
        "first_name":"Orly", 
        "last_name":"Chetwind", 
        "email":"ochetwindl@mediafire.com", 
        "gender":"Bigender", 
        "ip_address":"53.117.38.105", 
        "school_number":"8b3e7bb2-610c-417e-acbf-a2bebf117438"
    },

    {
        "id":23, 
        "first_name":"Cally", 
        "last_name":"Van De Cappelle", 
        "email":"cvandecappellem@wikipedia.org", 
        "gender":"Female", 
        "ip_address":"183.115.127.214", 
        "school_number":"70dade56-a7c8-43f7-82d9-030ddac6d72d"
    },

    {
        "id":24, 
        "first_name":"Aubrey", 
        "last_name":"Cotterell", 
        "email":"acotterelln@goo.ne.jp", 
        "gender":"Male", 
        "ip_address":"227.32.222.78", 
        "school_number":"7023607c-01d7-484a-8bf3-e3b9d4211fde"
    },

    {
        "id":25, 
        "first_name":"Anders", 
        "last_name":"Braznell", 
        "email":"abraznello@drupal.org", 
        "gender":"Female", 
        "ip_address":"11.241.216.69", 
        "school_number":"358c5540-f503-4621-9e4f-5efea2a59742"
    }, 

    {
        "id":26, 
        "first_name":"Kerry", 
        "last_name":"Melmoth", 
        "email":"kmelmothp@vk.com", 
        "gender":"Genderfluid", 
        "ip_address":"145.183.61.16", 
        "school_number":"cee23939-cb95-4c6b-a9b8-3db65db5c940"
    },

    {
        "id":27, 
        "first_name":"Jasmine", 
        "last_name":"Silveston", 
        "email":"jsilvestonq@narod.ru", 
        "gender":"Male", 
        "ip_address":"125.152.98.7", 
        "school_number":"4fe7966c-1818-4377-8718-f67c94c668f0"
    },

    {
        "id":28, 
        "first_name":"Jessalin", 
        "last_name":"Gubbin", 
        "email":"jgubbinr@irs.gov", 
        "gender":"Polygender", 
        "ip_address":"106.34.142.182", 
        "school_number":"5149f4c9-1da4-4a09-9364-fb16639d618b"
    },

    {
        "id":29, 
        "first_name":"Waneta", 
        "last_name":"Manifould", 
        "email":"wmanifoulds@vkontakte.ru", 
        "gender":"Genderfluid", 
        "ip_address":"98.9.119.8", 
        "school_number":"236a9ff8-9f25-4ebf-8ca9-801e0009e815"
    },

    {
        "id":30, 
        "first_name":"Windham", 
        "last_name":"Matchett", 
        "email":"wmatchettt@creativecommons.org", 
        "gender":"Genderfluid", "ip_address":"107.83.4.98", 
        "school_number":"d9603812-edc5-48cc-aee3-ed45f572e636"
    }, 

    {
        "id":31, 
        "first_name":"Rodd", 
        "last_name":"Pierri", 
        "email":"rpierriu@berkeley.edu", 
        "gender":"Male", 
        "ip_address":"40.94.179.217", 
        "school_number":"c50cb977-cd74-4126-9dbe-0be342a0fe09"
    },

    {
        "id":32, 
        "first_name":"Jacklin", 
        "last_name":"Selbie", 
        "email":"jselbiev@ifeng.com", 
        "gender":"Female", 
        "ip_address":"245.99.74.83", 
        "school_number":"31293bda-cb38-4286-969e-53be4e12d961"
    },

    {
        "id":33, 
        "first_name":"Hailee", 
        "last_name":"Paish", 
        "email":"hpaishw@sbwire.com", 
        "gender":"Genderfluid", 
        "ip_address":"39.217.184.202", 
        "school_number":"ac1a541b-b29c-40eb-b5c6-62f15fd6dab4"
    },

    {
        "id":34, 
        "first_name":"Roselin", 
        "last_name":"Measham", 
        "email":"rmeashamx@posterous.com", 
        "gender":"Genderqueer", 
        "ip_address":"154.175.19.195", 
        "school_number":"71abb0cb-6eaf-41fd-b869-01ffd0335666"
    },

    {
        "id":35, 
        "first_name":"Roxie", 
        "last_name":"Jeannaud", 
        "email":"rjeannaudy@mysql.com", 
        "gender":"Agender", 
        "ip_address":"13.183.243.210", 
        "school_number":"d13397f6-f46b-4a51-9f10-e60260f0b267"
    },

    {
        "id":36, 
        "first_name":"Meryl", 
        "last_name":"Hawtin",
        "email":"mhawtinz@imgur.com", 
        "gender":"Male", 
        "ip_address":"43.20.115.200", 
        "school_number":"80710b8d-cc6c-4979-9912-1d93713e37e1"
    },

    {
        "id":37, 
        "first_name":"Carri", 
        "last_name":"Ianiello", 
        "email":"cianiello10@state.gov", 
        "gender":"Female", 
        "ip_address":"237.187.20.37", 
        "school_number":"73efeb1e-0751-4354-b86d-ff00cd17b8ae"
    },

    {
        "id":38, 
        "first_name":"Onofredo",
        "last_name":"Eiler", 
        "email":"oeiler11@blogspot.com", 
        "gender":"Polygender", 
        "ip_address":"22.81.137.229", 
        "school_number":"aebac350-47fd-4345-a8c9-29393f2ba7f2"
    },

    {
        "id":39, 
        "first_name":"Jess", 
        "last_name":"Krikorian", 
        "email":"jkrikorian12@economist.com", 
        "gender":"Polygender", 
        "ip_address":"124.116.237.165",
        "school_number":"343e7c1a-c912-4c9d-9332-a1a77aff4aa5"
    },

    {
        "id":40, 
        "first_name":"Dasie", 
        "last_name":"Poulson", 
        "email":"dpoulson13@google.com.au", 
        "gender":"Non-binary", 
        "ip_address":"123.101.57.229", 
        "school_number":"33cd27e1-61ec-4dc8-81ab-10eb45c0c416"
    },

    {
        "id":41, 
        "first_name":"Prissie", 
        "last_name":"Staves", 
        "email":"pstaves14@t.co", 
        "gender":"Male", 
        "ip_address":"123.47.12.65", 
        "school_number":"54a13004-2d33-435e-bf91-1c9f3da6d687"
    },

    {
        "id":42, 
        "first_name":"Gerald", 
        "last_name":"Garz", 
        "email":"ggarz15@sitemeter.com", 
        "gender":"Polygender", 
        "ip_address":"11.243.94.130", 
        "school_number":"2b160672-54b5-4108-a96b-f1a9e34e0377"
    },

    {
        "id":43,
        "first_name":"Shantee", 
        "last_name":"Raunds", 
        "email":"sraunds16@barnesandnoble.com", 
        "gender":"Agender", 
        "ip_address":"168.110.13.136", 
        "school_number":"b0809f0d-c4a4-46fc-8386-d965ed3cfce6"
    },

    {
        "id":44, 
        "first_name":"Annmarie", 
        "last_name":"Loeber", 
        "email":"aloeber17@bing.com", 
        "gender":"Genderfluid", 
        "ip_address":"233.239.115.130", 
        "school_number":"2f79c09d-1794-4b7c-a79c-d090fef7c929"
    },

    {
        "id":45, 
        "first_name":"Tim", 
        "last_name":"Vale",
        "email":"tvale18@about.com", 
        "gender":"Bigender", 
        "ip_address":"191.88.254.82", 
        "school_number":"7cb3f58e-5e0c-4232-9526-7d4d9d59f006"
    },

    {
        "id":46, 
        "first_name":"Petey", 
        "last_name":"Towns", 
        "email":"ptowns19@mysql.com", 
        "gender":"Bigender", 
        "ip_address":"203.39.117.146", 
        "school_number":"065e3cb2-bd15-45ea-95cd-60f9ce3eaacf"
    },

    {
        
        "id":47, 
        "first_name":"Sula", 
        "last_name":"Mc Carroll", 
        "email":"smccarroll1a@hexun.com", 
        "gender":"Genderfluid", 
        "ip_address":"100.255.67.166", 
        "school_number":"470e7f07-8cd8-4f53-943a-984dca3b8924"
    },

    {
        "id":48, 
        "first_name":"Sergio", 
        "last_name":"Colcutt", 
        "email":"scolcutt1b@deliciousdays.com", 
        "gender":"Female", "ip_address":"29.88.45.190", 
        "school_number":"d7709647-011b-4dc5-b340-40d4b9289612"
    },

    {
        "id":49, 
        "first_name":"Kendrick", 
        "last_name":"Cheeke", 
        "email":"kcheeke1c@senate.gov", 
        "gender":"Genderfluid", 
        "ip_address":"228.35.223.186", 
        "school_number":"a3c442a5-a7d9-4fbe-93f6-b1678d039464"
    },

    {
        "id":50, 
        "first_name":"Cherilynn", 
        "last_name":"O'Tuohy", 
        "email":"cotuohy1d@uol.com.br", 
        "gender":"Non-binary", 
        "ip_address":"196.238.220.72", 
        "school_number":"e1da1505-d76c-4adb-8569-3a12f5a03fa8"
    },

    {
        "id":51, 
        "first_name":"Clyde", 
        "last_name":"Vereker", 
        "email":"cvereker1e@census.gov", 
        "gender":"Bigender", 
        "ip_address":"63.78.207.211", 
        "school_number":"33de0620-2ffa-43fc-b0b9-f0eb5001f83e"
    },

    {
        "id":52, 
        "first_name":"Daveta",
        "last_name":"Cosgrave", 
        "email":"dcosgrave1f@360.cn", 
        "gender":"Genderqueer", 
        "ip_address":"157.187.70.147", 
        "school_number":"8dae7ecb-6cf5-4473-85b2-052ec2acae58"
    },

    {
        "id":53, 
        "first_name":"Raimund", 
        "last_name":"Warstall", 
        "email":"rwarstall1g@pagesperso-orange.fr", 
        "gender":"Polygender", "ip_address":"153.39.75.190", 
        "school_number":"0367c9ab-6968-4f8f-a3d3-f54088702203"
    },

    {
        "id":54, 
        "first_name":"Harriot", 
        "last_name":"Fullerton", 
        "email":"hfullerton1h@kickstarter.com", 
        "gender":"Female", "ip_address":"161.174.181.186", 
        "school_number":"011985ff-2fae-4390-bc1f-2eac433402db"
    },

    {
        "id":55, 
        "first_name":"Jarret", 
        "last_name":"Clemintoni", 
        "email":"jclemintoni1i@businessweek.com", 
        "gender":"Male", "ip_address":"150.201.46.142", 
        "school_number":"5bfab0e8-9bdd-4a44-9a20-f5b7c6c7595b"
    },

    {
        "id":56, 
        "first_name":"Abram", 
        "last_name":"Sigward", 
        "email":"asigward1j@bloglines.com", 
        "gender":"Agender", 
        "ip_address":"53.207.142.154", 
        "school_number":"bfbc5dbd-1676-4846-b283-1bc1bfc9d2a5"
    },

    {
        "id":57, 
        "first_name":"Ronnie", 
        "last_name":"Dawidowsky", 
        "email":"rdawidowsky1k@wordpress.org", 
        "gender":"Agender", 
        "ip_address":"237.166.4.212", 
        "school_number":"c31f2cb0-a203-41d6-9d79-86f25362b35e"
    },

    {
        "id":58, 
        "first_name":"Sebastian", 
        "last_name":"Olrenshaw", 
        "email":"solrenshaw1l@etsy.com", 
        "gender":"Polygender", 
        "ip_address":"217.18.78.119", 
        "school_number":"c9324a7a-f77d-4a5a-ac42-199ddfe6e352"
    },

    {
        "id":59, 
        "first_name":"Amos", 
        "last_name":"Meacher", 
        "email":"ameacher1m@utexas.edu", 
        "gender":"Agender", 
        "ip_address":"69.0.225.164", 
        "school_number":"fa666ad5-08fc-45a6-be7f-5cb19e861dad"
    },

    {
        "id":60, 
        "first_name":"Nellie", 
        "last_name":"Junes", 
        "email":"njunes1n@examiner.com", 
        "gender":"Polygender", 
        "ip_address":"20.18.94.239", 
        "school_number":"015beefc-f45f-4ea0-a1fe-bf289c2f84d4"
    },

    {
        "id":61, 
        "first_name":"Weston", 
        "last_name":"Putman", 
        "email":"wputman1o@uiuc.edu", 
        "gender":"Bigender", 
        "ip_address":"139.106.52.171", 
        "school_number":"c2df6ffe-29a8-48f9-b52c-183eee0db305"
    },

    {
        "id":62, 
        "first_name":"Allyson", 
        "last_name":"Blackbourn", 
        "email":"ablackbourn1p@imdb.com", 
        "gender":"Polygender", 
        "ip_address":"38.195.243.198", 
        "school_number":"5147f973-9746-477d-bc52-e8c3ab29ba2a"
    },

    {
        "id":63, 
        "first_name":"Collie", 
        "last_name":"Caunt", 
        "email":"ccaunt1q@cargocollective.com", 
        "gender":"Polygender", 
        "ip_address":"247.79.25.214", 
        "school_number":"6544d09f-e999-48ed-95ec-168cca763786"
    },

    {
        "id":64, 
        "first_name":"Durward", 
        "last_name":"Robberts", 
        "email":"drobberts1r@ibm.com", 
        "gender":"Genderqueer", 
        "ip_address":"55.62.28.142", 
        "school_number":"19f46ff2-b7e6-4101-8e57-cd58396f7f98"
    },

    {
        "id":65, 
        "first_name":"Corissa", 
        "last_name":"Rodriguez", 
        "email":"crodriguez1s@topsy.com", 
        "gender":"Bigender", 
        "ip_address":"136.17.31.181", 
        "school_number":"8f3b6885-727b-4dce-9a22-43bacf995121"
    },

    {
        "id":66, 
        "first_name":"Stafford", 
        "last_name":"Orteau", 
        "email":"sorteau1t@oracle.com", 
        "gender":"Genderqueer", 
        "ip_address":"152.2.9.30", 
        "school_number":"44fbc82a-b156-45f9-a11b-96ba1ab143a7"
    },

    {
        "id":67, 
        "first_name":"Lidia", 
        "last_name":"Senyard", 
        "email":"lsenyard1u@wsj.com", 
        "gender":"Genderfluid", 
        "ip_address":"38.166.111.146", 
        "school_number":"d1dda8a8-3afc-4da9-b51f-c5ee2c36dde8"
    },

    {
        "id":68, 
        "first_name":"Reggie", 
        "last_name":"Gatesman", 
        "email":"rgatesman1v@sciencedaily.com", 
        "gender":"Non-binary", 
        "ip_address":"235.157.188.49", 
        "school_number":"89023e2c-a395-4751-805f-a95c066e2355"
    },

    {
        "id":69, 
        "first_name":"Niel", 
        "last_name":"Hillam", 
        "email":"nhillam1w@bizjournals.com", 
        "gender":"Female", 
        "ip_address":"229.168.231.239", 
        "school_number":"900e6234-1b56-49a1-a743-67c7f4723e65"
    },

    {
        "id":70, 
        "first_name":"Bar", 
        "last_name":"Oxe", 
        "email":"boxe1x@homestead.com",
        "gender":"Male", 
        "ip_address":"217.52.199.72", 
        "school_number":"0616b582-5c21-4a84-9f4d-35b75afabd5c"
    },

    {
        "id":71, 
        "first_name":"Corbet", 
        "last_name":"Faulkner", 
        "email":"cfaulkner1y@devhub.com", 
        "gender":"Non-binary", 
        "ip_address":"203.140.124.240", 
        "school_number":"c3d8366d-6123-4acf-a00c-083f41d2760e"
    },

    {
        "id":72, 
        "first_name":"Raeann", 
        "last_name":"Spurden", 
        "email":"rspurden1z@nih.gov", 
        "gender":"Agender", 
        "ip_address":"102.67.4.123", 
        "school_number":"cc88e129-6102-4d3f-942e-574973050d87"
    },

    {
        "id":73, 
        "first_name":"Tony", 
        "last_name":"Bletsor", 
        "email":"tbletsor20@walmart.com", 
        "gender":"Agender", 
        "ip_address":"66.28.20.103", 
        "school_number":"a9fc3ca0-3396-40e2-8e99-5f2611ac71ad"
    }, 

    {
        "id":74, 
        "first_name":"Lief",
        "last_name":"Javes", 
        "email":"ljaves21@blogtalkradio.com", 
        "gender":"Male", 
        "ip_address":"227.66.184.152", 
        "school_number":"661cedb6-7d20-4bf9-9ddd-2700b60de308"
    },

    {
        "id":75, 
        "first_name":"Albrecht", 
        "last_name":"Bento", 
        "email":"abento22@youtu.be", 
        "gender":"Agender", 
        "ip_address":"25.42.76.98", 
        "school_number":"6ab922e1-1de7-4a83-904b-c744394622d2"
    },

    {
        "id":76, 
        "first_name":"Lory", 
        "last_name":"Marielle", 
        "email":"lmarielle23@blinklist.com", 
        "gender":"Female", 
        "ip_address":"205.149.159.222", 
        "school_number":"a4f7ada1-2c51-4fc2-aea4-1998c4dad221"
    }, 

    {
        "id":77, 
        "first_name":"Katerine", 
        "last_name":"Fragino", 
        "email":"kfragino24@people.com.cn", 
        "gender":"Genderfluid", 
        "ip_address":"144.37.237.180", 
        "school_number":"521269b9-a68f-42d0-af3e-ae505e4664df"
    }, 

    {
        "id":78, 
        "first_name":"Wernher", 
        "last_name":"Crowth", 
        "email":"wcrowth25@latimes.com", 
        "gender":"Agender", 
        "ip_address":"161.175.87.193", 
        "school_number":"6c2f5916-4a72-47be-858e-68eedbb346c5"
    }, 

    {
        "id":79, 
        "first_name":"Tully", 
        "last_name":"Bollum", 
        "email":"tbollum26@sakura.ne.jp", 
        "gender":"Polygender", 
        "ip_address":"139.108.45.6", 
        "school_number":"ab4cd4c2-fd8b-4b24-9517-aa2ec6e47012"
    }, 

    {
        "id":80, 
        "first_name":"Adolf", 
        "last_name":"Willishire", 
        "email":"awillishire27@hugedomains.com", 
        "gender":"Bigender", 
        "ip_address":"164.237.14.23", 
        "school_number":"bac2317e-53e6-4c96-a77c-55cfec9d44c3"}, 
    {
        "id":81, 
        "first_name":"Noll", 
        "last_name":"Leban",
        "email":"nleban28@youtu.be", 
        "gender":"Genderqueer", 
        "ip_address":"5.179.137.170", 
        "school_number":"84ce0354-0fe0-4fff-8c0d-2bcc34e33fa9"
    }, 
    
    {
        "id":82, 
        "first_name":"Teddi", 
        "last_name":"Ruddle", 
        "email":"truddle29@yellowpages.com", 
        "gender":"Male", 
        "ip_address":"255.91.92.238", 
        "school_number":"0db9668a-e573-447d-9393-706bf0b4f603"
    },

    {
        "id":83, 
        "first_name":"Bell", 
        "last_name":"Piddington", 
        "email":"bpiddington2a@google.de", 
        "gender":"Non-binary", 
        "ip_address":"61.189.66.12", 
        "school_number":"43d3b62b-1503-4e37-bed1-1dbdb313bca5"
    },

    {
        "id":84, 
        "first_name":"Anjela", 
        "last_name":"Arangy", 
        "email":"aarangy2b@simplemachines.org", 
        "gender":"Female", 
        "ip_address":"212.253.190.222", 
        "school_number":"51d8466a-3d59-4eba-9335-b37b54fd040d"
    },

    {
        "id":85,
        "first_name":"Eleonore", 
        "last_name":"Steed", 
        "email":"esteed2c@dailymotion.com", 
        "gender":"Male", 
        "ip_address":"86.243.209.2", 
        "school_number":"72535cf9-a533-45a6-9796-cce97b2708f1"
    },

    {
        "id":86, 
        "first_name":"Bordie", 
        "last_name":"Tessier", 
        "email":"btessier2d@google.nl", 
        "gender":"Non-binary", 
        "ip_address":"37.20.101.69", 
        "school_number":"b737be52-f65f-45c7-8fbe-aa5d64eccd56"
    },

    {
        "id":87, 
        "first_name":"Hersch", 
        "last_name":"Corpe", 
        "email":"hcorpe2e@nps.gov", 
        "gender":"Female", 
        "ip_address":"108.73.127.185", 
        "school_number":"624336c4-b7ec-40b8-87f7-804c30c5cc82"
    },

    {
        "id":88, 
        "first_name":"Suzie", 
        "last_name":"McCardle", 
        "email":"smccardle2f@aol.com", 
        "gender":"Agender", 
        "ip_address":"112.92.56.205", 
        "school_number":"e539c896-c38f-48e8-96ac-d792b0c2df11"
    },

    {
        "id":89, 
        "first_name":"Mord", 
        "last_name":"Sabey", 
        "email":"msabey2g@howstuffworks.com", 
        "gender":"Female", 
        "ip_address":"229.169.6.79", 
        "school_number":"54c2fef3-1a1f-4965-9012-e34a506bcc2a"
    },

    {
        "id":90, 
        "first_name":"Harriet", 
        "last_name":"Stranahan", 
        "email":"hstranahan2h@cbc.ca", 
        "gender":"Bigender", 
        "ip_address":"75.81.49.64", 
        "school_number":"698d8dc4-c830-480d-b25f-d69c0e8d9aae"
    },

    {
        "id":91, 
        "first_name":"Odessa", 
        "last_name":"Owtram", 
        "email":"oowtram2i@domainmarket.com", 
        "gender":"Bigender", 
        "ip_address":"108.27.92.150", 
        "school_number":"3c15cc73-630e-41cb-9920-006f0afd9231"
    },

    {
        "id":92, 
        "first_name":"Boyd", 
        "last_name":"Mattea", 
        "email":"bmattea2j@home.pl", 
        "gender":"Polygender", 
        "ip_address":"115.186.121.187", 
        "school_number":"c32deb89-6930-42ef-98a1-82d974f25edb"
    },

    {
        "id":93, 
        "first_name":"Zack", 
        "last_name":"Jarlmann", 
        "email":"zjarlmann2k@theglobeandmail.com", 
        "gender":"Female", 
        "ip_address":"3.48.119.98", 
        "school_number":"fce6f526-7c7a-4467-9373-ce78a8f61c0f"
    },

    {
        "id":94, 
        "first_name":"Sileas", 
        "last_name":"Callaghan", 
        "email":"scallaghan2l@1und1.de", 
        "gender":"Genderfluid", 
        "ip_address":"233.58.155.34", 
        "school_number":"808e4390-e387-4f1d-afcb-55c0eb6792b9"
    },

    {
        "id":95, 
        "first_name":"Shalna", 
        "last_name":"Vaar", 
        "email":"svaar2m@dell.com", 
        "gender":"Male", 
        "ip_address":"79.233.101.72", 
        "school_number":"616dd7ed-1759-432f-8c07-f51a6180ddcb"
    },

    {
        "id":96, "first_name":"Isabeau", 
        "last_name":"Skeates", 
        "email":"iskeates2n@walmart.com", 
        "gender":"Female", 
        "ip_address":"225.244.53.149", 
        "school_number":"40fcdcad-7e44-49c3-9a53-ed9245c94ed5"
    },

    {
        "id":97, 
        "first_name":"Thomasina", 
        "last_name":"Duckfield", 
        "email":"tduckfield2o@oracle.com", 
        "gender":"Polygender", 
        "ip_address":"51.252.204.203", 
        "school_number":"b1db96c5-604c-4ba7-b946-f613ed25bb44"
    },

    {
        "id":98, 
        "first_name":"Carita", 
        "last_name":"Whitecross", 
        "email":"cwhitecross2p@sina.com.cn", 
        "gender":"Genderfluid", 
        "ip_address":"70.154.143.27", 
        "school_number":"0dc2c4fd-307b-4aca-871d-d49a24d37f82"
    },

    {
        "id":99, 
        "first_name":"Constance", 
        "last_name":"Barrus", 
        "email":"cbarrus2q@symantec.com", 
        "gender":"Male", 
        "ip_address":"89.29.187.152", 
        "school_number":"bc65b612-d256-4fed-899e-77a707c22a98"
    },

    {
        "id":100, 
        "first_name":"Shep", 
        "last_name":"Cubbinelli", 
        "email":"scubbinelli2r@dropbox.com", 
        "gender":"Male", 
        "ip_address":"236.3.168.82", 
        "school_number":"5b1f1c40-a08a-402f-afe6-242e31dd6050"
        }
]


r = redis.StrictRedis(host='redis_volume', port=6379, db=0)
r.hset({id}-{first_name}-{last_name}, 'json_record')