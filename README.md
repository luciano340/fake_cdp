# Estudo sobre CDP

## Visão Geral 🔎  
Este projeto, chamado **fake_cdp**, tem o objetivo de simular o funcionamento de um **Customer Data Platform (CDP)** e avaliar a **diferença de tempo de resposta** entre um banco de dados relacional (**MySQL**) e um **ElasticSearch** em consultas que envolvem grandes volumes de textos.  

Durante os testes, percebemos que o **ElasticSearch** é extremamente performático quando comparado ao banco de dados, pois o **tempo de resposta do banco relacional aumenta exponencialmente** com a quantidade de registros, enquanto no **ElasticSearch o impacto é quase imperceptível**.

## O que é um sistema CDP?  
Um **Customer Data Platform (CDP)** é um sistema que **coleta, unifica e organiza dados de clientes** vindos de diferentes fontes para oferecer uma visão única do cliente. Diferente de um CRM ou DMP, um CDP foca em consolidar **dados primários** (dados próprios da empresa) e fornecer informações acionáveis para **personalização de campanhas, análise de comportamento e segmentação**.

### **Principais características de um CDP:**  
✅ **Coleta de dados**: Captura eventos de diversas fontes (sites, apps, interações).  
✅ **Unificação de perfis**: Agrupa informações de diferentes fontes para formar um único perfil do cliente.  
✅ **Armazenamento estruturado**: Utiliza bancos de dados relacionais e não relacionais para manter informações organizadas.  
✅ **Consulta eficiente**: Permite buscas rápidas e análises detalhadas.  
✅ **Integração com outros sistemas**: Pode ser integrado a ferramentas de marketing, CRM e analytics.

---

## Reflexões CDP 🛣  
### **Programação e Arquitetura**  
Ao longo da construção do **fake_cdp**, experimentamos diferentes abordagens para a implementação de **producers, consumers, APIs** e **armazenamento de eventos**. Algumas reflexões importantes:

- A **ingestão de eventos** precisa ser altamente escalável, pois CDPs geralmente lidam com **grandes volumes de dados**.
- A **indexação no ElasticSearch** permite **buscas extremamente rápidas** em comparação com bancos relacionais, tornando-o ideal para consultas de eventos históricos.
- O **tempo de resposta** do banco de dados relacional **cresce exponencialmente com o volume de dados**, enquanto o ElasticSearch mantém um desempenho quase constante.

### **Infraestrutura**  
Além do código, discutimos **como configurar e monitorar o sistema** para garantir **resiliência e observabilidade**:

- O **Prometheus** é uma excelente escolha para **coletar métricas** do Kafka, ElasticSearch e aplicação.
- O uso de **Grafana** para visualizar métricas nos permitiu **comparar tempos de resposta e identificar gargalos**.
- O **Prometheus Client no Python** nos ajudou a monitorar o tempo de resposta da API **de forma eficiente**.

---

## Abordagem  

### **Fluxo do CDP**  
A arquitetura do **fake_cdp** segue um fluxo simples, mas eficaz:

1. **Producer (Python, Multi-threading)**  
   - Gera eventos aleatórios e os envia para o Kafka.  
   - Simula alta ingestão de dados, refletindo cenários reais de um CDP.  

2. **Consumer (Python, Kafka Consumer)**  
   - Consome eventos do Kafka e enriquece os dados.  
   - Armazena os eventos processados no **MySQL** e no **ElasticSearch**.  

3. **API FastAPI**  
   - Exposta com dois endpoints:  
     - `/eventos_db/` → Consulta eventos armazenados no MySQL.  
     - `/eventos_es/` → Consulta eventos armazenados no ElasticSearch.  
   - Mede o **tempo de resposta** de cada endpoint para comparação.  

---

### **Monitoramento e Métricas**  

Para garantir **observabilidade**, implementamos métricas usando o **Prometheus Client do Python**.  

- Criamos um **middleware no FastAPI** para capturar o **tempo de resposta de cada requisição**.  
- Usamos **multiproc do Prometheus Client** para expor métricas de **diferentes processos**, garantindo que **todos os containers pudessem enviar dados corretamente**.  
- Configuramos um **dashboard no Grafana**, permitindo visualizar o **tempo de resposta dos endpoints e o volume de eventos processados**.  

---

Este estudo reforçou a importância de um **CDP bem estruturado**, tanto em termos de **desempenho de consulta**, quanto de **monitoramento e escalabilidade**. 🚀