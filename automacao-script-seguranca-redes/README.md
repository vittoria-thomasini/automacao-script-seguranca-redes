# project-network-security-v1
<h1>Segurança de Redes</h1>
<h2>Pre-requisitos</h2>
- GOlang
- Assetfinder
- Sublist3r
- Subfinder
- NMAP

## Instalação do projeto

Instalar os pacotes do python ```pip install -r requirements.txt```.

Instalar no seu próprio sistema os seguintes pacotes:
* subfinder
* tk ou python-tk (de acordo com o sistema operacional)

 Link Gantt no Notion: https://honorable-surf-8fc.notion.site/526f79cd26cb4154b11d275dc3f2f0b1?v=71e6cd48f88d4f5882e509fdf210f983 
<div class="page-body"><table class="collection-content"><thead><tr><th><span class="icon property-icon"><svg viewBox="0 0 14 14" style="width:14px;height:14px;display:block;fill:rgba(55, 53, 47, 0.45);flex-shrink:0;-webkit-backface-visibility:hidden" class="typesTitle"><path d="M7.73943662,8.6971831 C7.77640845,8.7834507 7.81338028,8.8943662 7.81338028,9.00528169 C7.81338028,9.49823944 7.40669014,9.89260563 6.91373239,9.89260563 C6.53169014,9.89260563 6.19894366,9.64612676 6.08802817,9.30105634 L5.75528169,8.33978873 L2.05809859,8.33978873 L1.72535211,9.30105634 C1.61443662,9.64612676 1.2693662,9.89260563 0.887323944,9.89260563 C0.394366197,9.89260563 0,9.49823944 0,9.00528169 C0,8.8943662 0.0246478873,8.7834507 0.0616197183,8.6971831 L2.46478873,2.48591549 C2.68661972,1.90669014 3.24119718,1.5 3.90669014,1.5 C4.55985915,1.5 5.12676056,1.90669014 5.34859155,2.48591549 L7.73943662,8.6971831 Z M2.60035211,6.82394366 L5.21302817,6.82394366 L3.90669014,3.10211268 L2.60035211,6.82394366 Z M11.3996479,3.70598592 C12.7552817,3.70598592 14,4.24823944 14,5.96126761 L14,9.07922535 C14,9.52288732 13.6549296,9.89260563 13.2112676,9.89260563 C12.8169014,9.89260563 12.471831,9.59683099 12.4225352,9.19014085 C12.028169,9.6584507 11.3257042,9.95422535 10.5492958,9.95422535 C9.60035211,9.95422535 8.47887324,9.31338028 8.47887324,7.98239437 C8.47887324,6.58978873 9.60035211,6.08450704 10.5492958,6.08450704 C11.3380282,6.08450704 12.040493,6.33098592 12.4348592,6.81161972 L12.4348592,5.98591549 C12.4348592,5.38204225 11.9172535,4.98767606 11.1285211,4.98767606 C10.6602113,4.98767606 10.2411972,5.11091549 9.80985915,5.38204225 C9.72359155,5.43133803 9.61267606,5.46830986 9.50176056,5.46830986 C9.18133803,5.46830986 8.91021127,5.1971831 8.91021127,4.86443662 C8.91021127,4.64260563 9.0334507,4.44542254 9.19366197,4.34683099 C9.87147887,3.90316901 10.6232394,3.70598592 11.3996479,3.70598592 Z M11.1778169,8.8943662 C11.6830986,8.8943662 12.1760563,8.72183099 12.4348592,8.37676056 L12.4348592,7.63732394 C12.1760563,7.29225352 11.6830986,7.11971831 11.1778169,7.11971831 C10.5616197,7.11971831 10.056338,7.45246479 10.056338,8.0193662 C10.056338,8.57394366 10.5616197,8.8943662 11.1778169,8.8943662 Z M0.65625,11.125 L13.34375,11.125 C13.7061869,11.125 14,11.4188131 14,11.78125 C14,12.1436869 13.7061869,12.4375 13.34375,12.4375 L0.65625,12.4375 C0.293813133,12.4375 4.43857149e-17,12.1436869 0,11.78125 C-4.43857149e-17,11.4188131 0.293813133,11.125 0.65625,11.125 Z"></path></svg></span>Name</th><th><span class="icon property-icon"><svg viewBox="0 0 14 14" style="width:14px;height:14px;display:block;fill:rgba(55, 53, 47, 0.45);flex-shrink:0;-webkit-backface-visibility:hidden" class="typesText"><path d="M7,4.56818 C7,4.29204 6.77614,4.06818 6.5,4.06818 L0.5,4.06818 C0.223858,4.06818 0,4.29204 0,4.56818 L0,5.61364 C0,5.88978 0.223858,6.11364 0.5,6.11364 L6.5,6.11364 C6.77614,6.11364 7,5.88978 7,5.61364 L7,4.56818 Z M0.5,1 C0.223858,1 0,1.223858 0,1.5 L0,2.54545 C0,2.8216 0.223858,3.04545 0.5,3.04545 L12.5,3.04545 C12.7761,3.04545 13,2.8216 13,2.54545 L13,1.5 C13,1.223858 12.7761,1 12.5,1 L0.5,1 Z M0,8.68182 C0,8.95796 0.223858,9.18182 0.5,9.18182 L11.5,9.18182 C11.7761,9.18182 12,8.95796 12,8.68182 L12,7.63636 C12,7.36022 11.7761,7.13636 11.5,7.13636 L0.5,7.13636 C0.223858,7.13636 0,7.36022 0,7.63636 L0,8.68182 Z M0,11.75 C0,12.0261 0.223858,12.25 0.5,12.25 L9.5,12.25 C9.77614,12.25 10,12.0261 10,11.75 L10,10.70455 C10,10.4284 9.77614,10.20455 9.5,10.20455 L0.5,10.20455 C0.223858,10.20455 0,10.4284 0,10.70455 L0,11.75 Z"></path></svg></span>Assign</th><th><span class="icon property-icon"><svg viewBox="0 0 14 14" style="width:14px;height:14px;display:block;fill:rgba(55, 53, 47, 0.45);flex-shrink:0;-webkit-backface-visibility:hidden" class="typesDate"><path d="M10.8889,5.5 L3.11111,5.5 L3.11111,7.05556 L10.8889,7.05556 L10.8889,5.5 Z M12.4444,1.05556 L11.6667,1.05556 L11.6667,0 L10.1111,0 L10.1111,1.05556 L3.88889,1.05556 L3.88889,0 L2.33333,0 L2.33333,1.05556 L1.55556,1.05556 C0.692222,1.05556 0.00777777,1.75556 0.00777777,2.61111 L0,12.5 C0,13.3556 0.692222,14 1.55556,14 L12.4444,14 C13.3,14 14,13.3556 14,12.5 L14,2.61111 C14,1.75556 13.3,1.05556 12.4444,1.05556 Z M12.4444,12.5 L1.55556,12.5 L1.55556,3.94444 L12.4444,3.94444 L12.4444,12.5 Z M8.55556,8.61111 L3.11111,8.61111 L3.11111,10.1667 L8.55556,10.1667 L8.55556,8.61111 Z"></path></svg></span>Date</th><th><span class="icon property-icon"><svg viewBox="0 0 14 14" style="width:14px;height:14px;display:block;fill:rgba(55, 53, 47, 0.45);flex-shrink:0;-webkit-backface-visibility:hidden" class="typesMultipleSelect"><path d="M4,3 C4,2.447715 4.447715,2 5,2 L12,2 C12.5523,2 13,2.447716 13,3 C13,3.55228 12.5523,4 12,4 L5,4 C4.447715,4 4,3.55228 4,3 Z M4,7 C4,6.447715 4.447715,6 5,6 L12,6 C12.5523,6 13,6.447716 13,7 C13,7.55228 12.5523,8 12,8 L5,8 C4.447715,8 4,7.55228 4,7 Z M4,11 C4,10.447715 4.447715,10 5,10 L12,10 C12.5523,10 13,10.447716 13,11 C13,11.55228 12.5523,12 12,12 L5,12 C4.447715,12 4,11.55228 4,11 Z M2,4 C1.44771525,4 1,3.55228475 1,3 C1,2.44771525 1.44771525,2 2,2 C2.55228475,2 3,2.44771525 3,3 C3,3.55228475 2.55228475,4 2,4 Z M2,8 C1.44771525,8 1,7.55228475 1,7 C1,6.44771525 1.44771525,6 2,6 C2.55228475,6 3,6.44771525 3,7 C3,7.55228475 2.55228475,8 2,8 Z M2,12 C1.44771525,12 1,11.5522847 1,11 C1,10.4477153 1.44771525,10 2,10 C2.55228475,10 3,10.4477153 3,11 C3,11.5522847 2.55228475,12 2,12 Z"></path></svg></span>Definition of Done</th><th><span class="icon property-icon"><svg viewBox="0 0 14 14" style="width:14px;height:14px;display:block;fill:rgba(55, 53, 47, 0.45);flex-shrink:0;-webkit-backface-visibility:hidden" class="typesSelect"><path d="M7,13 C10.31348,13 13,10.31371 13,7 C13,3.68629 10.31348,1 7,1 C3.68652,1 1,3.68629 1,7 C1,10.31371 3.68652,13 7,13 Z M3.75098,5.32278 C3.64893,5.19142 3.74268,5 3.90869,5 L10.09131,5 C10.25732,5 10.35107,5.19142 10.24902,5.32278 L7.15771,9.29703 C7.07764,9.39998 6.92236,9.39998 6.84229,9.29703 L3.75098,5.32278 Z"></path></svg></span>Status</th></tr></thead><tbody><tr id="689d82e0-7f11-48d0-96e5-0e84f6fd4170"><td class="cell-title"><a href="https://www.notion.so/Criar-projeto-github-689d82e07f1148d096e50e84f6fd4170">Criar projeto github</a></td><td class="cell-l?FF">Vittoria Thomasini</td><td class="cell-gJVg"><time>@September 13, 2022 → September 16, 2022</time></td><td class="cell-YpBD"><span class="selected-value select-value-color-default">Github criado</span></td><td class="cell-UtlQ"><span class="selected-value select-value-color-green">Completed</span></td></tr><tr id="a667a05c-259a-4d08-9615-39560cfaa4e7"><td class="cell-title"><a href="https://www.notion.so/Criar-documento-de-planejamento-a667a05c259a4d08961539560cfaa4e7">Criar documento de planejamento</a></td><td class="cell-l?FF"></td><td class="cell-gJVg"><time>@September 10, 2022 → September 20, 2022</time></td><td class="cell-YpBD"><span class="selected-value select-value-color-brown">Postar Documento Moodle</span></td><td class="cell-UtlQ"><span class="selected-value select-value-color-green">Completed</span></td></tr><tr id="137bcda0-772e-4aec-b62e-ecc199a8a8cf"><td class="cell-title"><a href="https://www.notion.so/Pesquisar-3-ferramentas-de-enumera-o-de-subdom-nio-137bcda0772e4aecb62eecc199a8a8cf">Pesquisar 3 ferramentas de enumeração de subdomínio</a></td><td class="cell-l?FF"></td><td class="cell-gJVg"><time>@September 13, 2022 → September 18, 2022</time></td><td class="cell-YpBD"></td><td class="cell-UtlQ"><span class="selected-value select-value-color-green">Completed</span></td></tr><tr id="9322b265-284c-4b1a-8334-84b06bb121fa"><td class="cell-title"><a href="https://www.notion.so/Pesquisar-API-para-integrar-buscadores-de-dominio-9322b265284c4b1a833484b06bb121fa">Pesquisar API para integrar buscadores de dominio</a></td><td class="cell-l?FF"></td><td class="cell-gJVg"><time>@September 13, 2022 → September 18, 2022</time></td><td class="cell-YpBD"></td><td class="cell-UtlQ"><span class="selected-value select-value-color-green">Completed</span></td></tr><tr id="d617fedf-75d2-4624-8885-aeda9a674e52"><td class="cell-title"><a href="https://www.notion.so/Definir-ferramentas-d617fedf75d246248885aeda9a674e52">Definir ferramentas</a></td><td class="cell-l?FF"></td><td class="cell-gJVg"><time>@September 17, 2022 → September 20, 2022</time></td><td class="cell-YpBD"></td><td class="cell-UtlQ"><span class="selected-value select-value-color-green">Completed</span></td></tr><tr id="fe5c9aaa-85d0-467b-9cc4-bf229b305e05"><td class="cell-title"><a href="https://www.notion.so/Definir-API-fe5c9aaa85d0467b9cc4bf229b305e05">Definir API</a></td><td class="cell-l?FF"></td><td class="cell-gJVg"><time>@September 17, 2022 → September 20, 2022</time></td><td class="cell-YpBD"></td><td class="cell-UtlQ"><span class="selected-value select-value-color-green">Completed</span></td></tr><tr id="7e6be190-4bb5-42a1-a474-5f3f456be4bd"><td class="cell-title"><a href="https://www.notion.so/Pedir-apenas-dom-nio-para-o-usu-rio-7e6be1904bb542a1a4745f3f456be4bd">Pedir apenas domínio para o usuário</a></td><td class="cell-l?FF"></td><td class="cell-gJVg"><time>@September 19, 2022 → September 23, 2022</time></td><td class="cell-YpBD"></td><td class="cell-UtlQ"><span class="selected-value select-value-color-green">Completed</span></td></tr><tr id="53b173c1-3845-40ce-b8e2-e85087ede294"><td class="cell-title"><a href="https://www.notion.so/Desenvolver-enumera-o-de-subdom-nio-53b173c1384540ceb8e2e85087ede294">Desenvolver enumeração de subdomínio</a></td><td class="cell-l?FF"></td><td class="cell-gJVg"><time>@September 20, 2022 → September 24, 2022</time></td><td class="cell-YpBD"></td><td class="cell-UtlQ"><span class="selected-value select-value-color-green">Completed</span></td></tr><tr id="c437e499-d83c-46e9-bb72-eb98d5f7f682"><td class="cell-title"><a href="https://www.notion.so/Desenvolver-enumera-o-de-IP-c437e499d83c46e9bb72eb98d5f7f682">Desenvolver enumeração de IP</a></td><td class="cell-l?FF"></td><td class="cell-gJVg"><time>@September 20, 2022 → September 24, 2022</time></td><td class="cell-YpBD"></td><td class="cell-UtlQ"></td></tr><tr id="10c6b4ce-0a7a-4b73-a157-bda71e8fac98"><td class="cell-title"><a href="https://www.notion.so/Desenvolver-enumera-o-de-sistemas-10c6b4ce0a7a4b73a157bda71e8fac98">Desenvolver enumeração de sistemas</a></td><td class="cell-l?FF"></td><td class="cell-gJVg"><time>@September 20, 2022 → September 24, 2022</time></td><td class="cell-YpBD"><span class="selected-value select-value-color-red">Destacar Porta</span><span class="selected-value select-value-color-purple">Destacar Protocolo</span></td><td class="cell-UtlQ"></td></tr><tr id="8449435a-368e-441b-865c-fb17747b9c2d"><td class="cell-title"><a href="https://www.notion.so/Enumerar-subdominios-8449435a368e441b865cfb17747b9c2d">Enumerar subdominios </a></td><td class="cell-l?FF"></td><td class="cell-gJVg"><time>@September 24, 2022 → September 28, 2022</time></td><td class="cell-YpBD"></td><td class="cell-UtlQ"></td></tr><tr id="0308ceea-09ec-450b-8db1-4394717c31f9"><td class="cell-title"><a href="https://www.notion.so/Destacar-protocolos-do-subdominio-0308ceea09ec450b8db14394717c31f9">Destacar protocolos do subdominio</a></td><td class="cell-l?FF"></td><td class="cell-gJVg"><time>@September 24, 2022 → September 28, 2022</time></td><td class="cell-YpBD"></td><td class="cell-UtlQ"></td></tr><tr id="ee3f5822-74ef-4de8-92b7-d8a341fa71f8"><td class="cell-title"><a href="https://www.notion.so/Destacar-portas-do-subdominio-ee3f582274ef4de892b7d8a341fa71f8">Destacar portas do subdominio</a></td><td class="cell-l?FF"></td><td class="cell-gJVg"><time>@September 24, 2022 → September 28, 2022</time></td><td class="cell-YpBD"></td><td class="cell-UtlQ"></td></tr><tr id="e15aa55f-9673-442e-a85d-9e74fc96a4aa"><td class="cell-title"><a href="https://www.notion.so/Enumerar-portas-e15aa55f9673442ea85d9e74fc96a4aa">Enumerar portas</a></td><td class="cell-l?FF"></td><td class="cell-gJVg"><time>@September 24, 2022 → September 28, 2022</time></td><td class="cell-YpBD"></td><td class="cell-UtlQ"></td></tr><tr id="e5e93536-e554-43c1-9fab-150d982860de"><td class="cell-title"><a href="https://www.notion.so/Enumeras-servi-os-e5e93536e55443c19fab150d982860de">Enumeras serviços</a></td><td class="cell-l?FF"></td><td class="cell-gJVg"><time>@September 24, 2022 → September 28, 2022</time></td><td class="cell-YpBD"></td><td class="cell-UtlQ"></td></tr><tr id="698f750b-83e9-4424-ae62-2108b48bc516"><td class="cell-title"><a href="https://www.notion.so/Enumerar-Status-698f750b83e94424ae622108b48bc516">Enumerar Status</a></td><td class="cell-l?FF"></td><td class="cell-gJVg"><time>@September 24, 2022 → September 28, 2022</time></td><td class="cell-YpBD"></td><td class="cell-UtlQ"></td></tr><tr id="2382a593-94e2-4e7c-a0b9-de55e3a6ec0a"><td class="cell-title"><a href="https://www.notion.so/Enumerar-Vers-o-2382a59394e24e7ca0b9de55e3a6ec0a">Enumerar Versão</a></td><td class="cell-l?FF"></td><td class="cell-gJVg"><time>@September 24, 2022 → September 28, 2022</time></td><td class="cell-YpBD"></td><td class="cell-UtlQ"></td></tr><tr id="2f5e78e7-64a9-4d13-b68c-3d0d589ad35e"><td class="cell-title"><a href="https://www.notion.so/Salvar-em-arquivo-TXT-2f5e78e764a94d13b68c3d0d589ad35e">Salvar em arquivo TXT</a></td><td class="cell-l?FF"></td><td class="cell-gJVg"><time>@September 28, 2022 → September 30, 2022</time></td><td class="cell-YpBD"></td><td class="cell-UtlQ"></td></tr><tr id="d5c0364f-5d14-442a-86d0-de62aa6a2319"><td class="cell-title"><a href="https://www.notion.so/Organizar-apresenta-o-d5c0364f5d14442a86d0de62aa6a2319">Organizar apresentação</a></td><td class="cell-l?FF"></td><td class="cell-gJVg"><time>@September 30, 2022 → October 4, 2022</time></td><td class="cell-YpBD"></td><td class="cell-UtlQ"></td></tr></tbody></table></div></article></body></html>