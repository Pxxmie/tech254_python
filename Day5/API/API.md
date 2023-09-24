# API

**What is an API?** 

API stands for application programming interface. They are a set of rules and protocols that allows different software applications to communicate and connect with each other.

API is the messenger that takes requests and tells a system what you want to do and then returns the response back to you. 

*For example; booking a flight ticket - you interact with the airline website to access the database to see any seats are available as well as the dates and cost on certain variables.* 

**How are API used?**

APIs are used across different industries and domains.

**Web Development** - API allows web applications to interact with external services or retrieve data from servers. For example; social media platforms allow APIs for developers to integrate features like sharing, commenting and liking.

**Mobile App Development** - Enables apps to interact with device features, access data from servers.  For example, **the weather bureau's software system contains daily weather data. The weather app on your phone “talks” to this system via APIs and shows you daily weather updates on your phone.

**Integration of Services** - Allows different software systems to work together. For example, an online shop integrating with a payment gateway service using its API to process payments securely. 

**Cloud Computing -**  Cloud service providers like Amazon Web Services (AWS), Google Cloud, and Microsoft Azure offer APIs to manage cloud resources, deploy applications, and interact with cloud services like storage, databases, and machine learning.

**Social Media Integration-** APIs provided by social media platforms like Facebook, Twitter, and Instagram allow developers to integrate social features into their applications. This includes features like user authentication, sharing content, and accessing user profiles.

Why are API so popular?

APIs are popular as they allow different applications to communicate with each other in real-time, on the internet. APIs have made it possible for different applications of different origins to interact with each other.

**Scalability-** APIs enable applications to scale by allowing them to interact with additional resources or services as needed.

**Flexibility and Customization**: APIs provide the flexibility to customise and extend software applications to meet specific business needs.

**Efficient Collaboration**: Enables teams to work on different parts of a project simultaneously. For example, one team can work on the front-end while another team works on the back-end, and they can integrate their work using APIs.

`Add a diagram to showcase the data transfer process in API commmunication`

What is REST API?

Stands for Representational state transfer

A REST API is a specific type of API that follows a set of rules and guidelines for how different programs communicate and share information. It follows the principles of RESTful architecture, which is an architectural style for designing networked applications. 

RESTful APIs often use standard formats like JSON or XML for data interchange. JSON is the most commonly used format.

In order for an API to be considered RESTful, it has to conform to these criteria:

- A client-server architecture made up of clients, servers, and resources, with requests managed through HTTP.
- [Stateless]lient-server communication, meaning no client information is stored between get requests and each request is separate and unconnected.

What is HTTP- what is used for?

HTTP stands for hypertext transfer protocol. It is a language that web browsers and servers use to communicate with each other.  

It is used to load webpages using hypertext links. 

**HTTP- Request Structure** 

![image (1).png](API%20fb802028d7e84425ba45057844b3f54b/image_(1).png)

![image.png](image.png)

Method: This is like telling the waiter how you want your food prepared. In an HTTP request, it's called the method. The most common methods are:

GET: Like asking for a menu item. It's used to retrieve information from the server.
POST: Like placing an order. It's used to send data to the server, often to submit forms or upload files.
PUT: Like asking for a replacement or making an update. It's used to update existing data on the server.
DELETE: Like asking to remove a dish from your order. It's used to delete data on the server.