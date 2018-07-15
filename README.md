# Resource Allotment System
## Introduction
An algorithm to maximise the matching of resource allocations with the user preference.

## The Objective
Given a resource allocation list of a group of users, and another list of their prefrences who wish to change their allocations to some other resource, we need to find an algorithm which can allocate these resources to all the interested* users such that maximum number of users are satisfied by the new resource allocation list. 

## The Constraints
- The user who do not wish to change their resources i.e those who have not filled in their prefrences for change in their allocations should not be disturbed or asked to change to other resources.
- Each user may provide multiple prefrences to resources.
- Each prefrence/s given by the user has the same priority.

## The Algorithm.
- I have tried to solve this resource allocation problem by finding the set of largest cycle in the resources for each user in the user prefrence list.
- Find all the cyclic paths in the resouce allocation graph for each user.
- Now try to get a subset of these cyclic paths such that they are disjoint and the sum of length of all the cycles in each path present in this subset is maximum.
- Sort these paths by comparing their total sum of lengths and finally return the set of paths which sums up to the maximum length.
- Lastly, to compare the satisfaction, by measuring ratio of the number of students who got allotted to their wish rooms by the total number of students who opted for change of rooms.
