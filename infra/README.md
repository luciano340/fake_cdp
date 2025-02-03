### Localmente
Para rodar essa aplicação localmente, utilize o docker-compose.yaml presente nesse diretório.

```
docker compose up -d
```

# Arquitetura de CDP em Cloud

Este documento descreve a arquitetura cloud para um **Customer Data Platform (CDP)**, focando na ingestão, processamento e consulta de eventos em tempo real. A solução utiliza **Kafka (MSK)**, **MySQL (RDS)**, **ElasticSearch (EKS)** e **FastAPI** rodando em **EC2**.

[Diagrama da arquitetura](https://raw.githubusercontent.com/luciano340/fake_cdp/refs/heads/sexta_implementacao/infra/Diagrama-cloud.svg)

## Visão Geral

1. **Producer** gera eventos aleatórios e os envia para o **Kafka (MSK)**.
2. **Consumer** lê os eventos do **Kafka**, adiciona informações extras e armazena os dados no **MySQL (RDS)** e no **ElasticSearch (EKS)**.
3. **API FastAPI** expõe dois endpoints para consulta:
   - `GET /eventos_db/` → Consulta eventos armazenados no MySQL.
   - `GET /eventos_es/` → Consulta eventos armazenados no ElasticSearch.

## Arquitetura Detalhada

### 1. **Producer**
- Implementado em **Python** com suporte a **multi-threading** para simular alta ingestão de eventos.
- Executado em uma **instância EC2**, configurada para se conectar ao **Kafka (MSK)** via **Route 53**.

### 2. **Kafka (MSK) + Route 53**
- O **Kafka** roda no **MSK (Managed Streaming for Apache Kafka)**, garantindo **alta disponibilidade** e **gerenciamento automatizado**.
- O **Route 53** fornece um **DNS Cluster Name**, permitindo que os **producers** e **consumers** se conectem de forma estável ao Kafka sem necessidade de um **NLB (Network Load Balancer)**.
- Essa abordagem melhora a **resiliência**, pois a AWS cuida do balanceamento de conexões e failover automático entre os **brokers** do MSK.

### 3. **Consumer**
- Também implementado em **Python** e executado em uma **instância EC2**.
- Consome eventos do **Kafka (MSK)** e processa os dados antes de armazená-los em:
  - **RDS (MySQL)** → Armazena eventos estruturados para análise e persistência de longo prazo.
  - **ElasticSearch (EKS)** → Permite consultas rápidas e busca full-text otimizada.

### 4. **MySQL (RDS)**
- Gerenciado pela **AWS RDS**, oferecendo escalabilidade, backups automáticos e alta disponibilidade.
- Mantém a **integridade relacional** dos dados processados.
- MultiAZ sempre habilitado.
- Aplicar replicar de leitura conforme necessidade.

### 5. **ElasticSearch (EKS)**
- Implantado em um **cluster Kubernetes (EKS)** com **múltiplos nós distribuídos em 3 zonas de disponibilidade**.
- Indexa os eventos para permitir **consultas rápidas** via API.

### 6. **API FastAPI (EC2)**
- Exposta via **EC2** com um **ALB (Application Load Balancer)** para distribuir requisições.
- Fornece endpoints para acessar os eventos armazenados no **MySQL** e no **ElasticSearch**.

## Benefícios da Arquitetura

✅ **Escalabilidade**: Kafka (MSK) e ElasticSearch (EKS) permitem lidar com volumes altos de eventos.  
✅ **Alta Disponibilidade**: MSK e EKS distribuídos em múltiplas zonas garantem resiliência.  
✅ **Conectividade Simples**: Route 53 substitui a necessidade de um NLB para conexão com Kafka.  
✅ **Balanceamento Automático**: MSK gerencia as partições e consumidores de forma eficiente.  
✅ **Consultas Otimizadas**: MySQL oferece confiabilidade para armazenamento, enquanto ElasticSearch garante consultas rápidas.  

---
Se tiver dúvidas ou sugestões, fique à vontade para contribuir! 🚀
