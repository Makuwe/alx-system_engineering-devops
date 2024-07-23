0x0F. Load balancer
How does Software and Hardware Load Balancer Work? (Loadbalancer Algorithms Explained with Examples)
by LUKE P. ISSAC on JANUARY 11, 2016
When you have an enterprise application or website that gets lot of hits, your server might be under heavy load. In that case, you may want to consider distributing the load across multiple servers.

Load balancer will distribute the work-load of your system to multiple individual systems, or group of systems to to reduce the amount of load on an individual system, which in turn increases the reliability, efficiency and availability of your enterprise application or website.

In this article, we’ll cover the basics of software and hardware load balancer, and explain the various algorithms used by the load balancers.


The following are the advantages of load balancing your application:

Reduced the work-load on an individual server.
Large amount of work done in same time due to concurrency.
Increased performance of your application because of faster response.
No single point of failure. In a load balanced environment, if a server crashes the application is still up and served by the other servers in the cluster.
When appropriate load balancing algorithm is used, it brings optimal and efficient utilization of the resources, as it eliminates the scenario of some server’s resources are getting used than others.
Scalability: We can increase or decrease the number of servers on the fly without bringing down the application
Load balancing increases the reliability of your enterprise application
Increased security as the physical servers and IPs are abstract in certain cases.
On a high level, there are two types of load balancers, which implements different types of scheduling algorithms and routing mechanisms.

Software load balancer
Hardware load balancer
I. Software Load Balancers
Software load balancers generally implements a combination of one or more scheduling algorithms.

The following are the three different basic algorithms used by load balancers. Most modern load balancers use combination of these algorithms to reach high performance and to set a trade off between various parameters.

1. Weighted Scheduling Algorithm
Work is assigned to the server according to the weight assigned to the server. For different types of the server in the group different weights are assigned thus the load gets distributed.


