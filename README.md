# Microsoft Presidio

Presidio (Origin from Latin praesidium ‘protection, garrison’) helps to ensure sensitive data is properly managed and governed. It provides fast identification and anonymization modules for private entities in text and images such as credit card numbers, names, locations, social security numbers, bitcoin wallets, US phone numbers, financial data and more.

Goals:
- Allow organizations to preserve privacy in a simpler way by democratizing de-identification technologies and introducing transparency in decisions.
- Embrace extensibility and customizability to a specific business need.
- Facilitate both fully automated and semi-automated PII de-identification flows on multiple platforms.

## Data anonymization - 

Data anonymization is a crucial process in data management and privacy protection with several important benefits:

Privacy Protection: Anonymizing data helps protect the privacy of individuals by removing personally identifiable information (PII). This reduces the risk of data breaches and misuse of sensitive information.

Compliance with Regulations: Many jurisdictions have strict data protection laws and regulations (like GDPR in Europe, CCPA in California, or HIPAA in the United States) that require organizations to protect personal data. Anonymization helps organizations comply with these legal requirements by ensuring that data cannot be traced back to specific individuals.

Facilitating Data Sharing: Anonymized data can be shared more freely between organizations, researchers, and other stakeholders without compromising individual privacy. This is particularly useful in fields like healthcare, where sharing data can lead to advancements in research and treatment without exposing patient identities.

Mitigating Risk: By anonymizing data, organizations can reduce the risk associated with data breaches. Even if anonymized data is leaked or hacked, the lack of identifiable information reduces the potential harm to individuals.

Enabling Data Analysis and Research: Anonymized data can be used for analysis, research, and developing AI models without violating privacy agreements. Researchers and analysts can gain insights and make informed decisions while ensuring that personal information remains protected.

Building Trust: Organizations that prioritize data anonymization demonstrate a commitment to privacy and data protection, which can build trust with customers, clients, and other stakeholders.

Ethical Considerations: Beyond legal and regulatory requirements, there is an ethical obligation to protect individuals' privacy. Anonymizing data shows that an organization respects and values the privacy of the individuals whose data they handle.

## Reference

### GitHub - open-source project, MIT license
https://github.com/microsoft/presidio/

### What is Presidio?
https://microsoft.github.io/presidio/

Presidio demo: https://huggingface.co/spaces/presidio/presidio_demo

### Installation
https://microsoft.github.io/presidio/installation/

### APIs
Python: https://microsoft.github.io/presidio/api/
REST:	https://microsoft.github.io/presidio/api-docs/api-docs.html

### Modules
Presidio Analyzer: 			https://microsoft.github.io/presidio/analyzer/
Presidio Anonymizer:		https://microsoft.github.io/presidio/anonymizer/
Presidio Image Redactor:	https://microsoft.github.io/presidio/image-redactor/

## Samples

1) Analyze + Anonymize Text
2) Anonymize PII in images

3) Customizing the PII analysis process in Microsoft Presidio
	- recognize new PII entities
	- detect PII in a new language
https://microsoft.github.io/presidio/samples/python/customizing_presidio_analyzer/
customizing_presidio_analyzer.ipynb 

4) Presidio Structured Basic Usage
https://microsoft.github.io/presidio/samples/python/example_structured/
example_structured.ipynb

### Use cases:
- Analyzers customization - detect new types of PII entities (+ other languages)
- Analysis of structured data (e.g. CSV, JSON)
	- https://microsoft.github.io/presidio/structured/
- Allow lists - prevent certain words from being redacted from images
- Redact text Personal Health Information (PHI) present as pixels in DICOM images
- Annotating PII in a PDFs
- Pseudonymization of PII data - replace with PII artificial identifiers or pseudonyms
- Encrypting and Decrypting identified entities using AES cypher in CBC




