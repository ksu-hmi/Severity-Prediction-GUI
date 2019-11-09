# Severity-Prediction-GUI
Severity-Prediction-GUI


Background

Our goal for this project is to build a prototype application for our client company. The application would be used by all of our companies physicians to provide better care to their patients by predicting possible adverse events for procedures being performed.  The company provides malpractice insurance to medical providers through the nation and as such has available a large dataset of all claims they have handled.  The process begins when a patient, initiates a claim of malpractice against a physician represented by our client.  The adjuster or attorney assigned the matter create a claim description, describing what occurred and listing patient diagnoses and problems, which is used to assign an overall severity level (1-9) to the claim.  The severity score is broken down in the chart below into nine levels to describe the outcomes. Additional structured data for each claim such as descriptors of the patient and medical provider is also included in the dataset.  Our company has also derived a list of medical terms associated with each claim.  

A KSU research team is working with client to develop a model for use in predicting adverse outcomes and predicting associated risk factors for such outcomes.  This model will then be used within an application by medical providers to assist them in decision making.

Proposed application

This prototype application would allow for input of claim data, including medical terms, and would return a predicted severity outcome.  Depending on the model used, it may also provide a list of associated vocabulary, in theory identifying possible risk factors for which the practitioner should be prepared.  The model to predict this severity level is an in progress project and as such, the prototype would function on a limited dataset and model.   While the project itself will continue through the upcoming year, we intend that the application be able to accept inputs such as the claim description, medical terms, and possibly demographic information, submits it to a function calling the selected model,  and returns a prediction.
