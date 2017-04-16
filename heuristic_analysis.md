# Heuristic Analysis
## Planning Search

## Results

[![](images/SummaryTable.png)](https://public.tableau.com/views/planningAI/SummaryTable?:embed=y&:display_count=yes)


When `depth_limited_search` found a search, it was typically the quickest to find a solution, but it was almost always insane. The best metric for measuring search performance (in my opinion) is **Optimal Plan Length** which averages the solutions to demonstrate performance across all 3 problems. 

In general, the best search strategies found 9 nodes necessary; 6 for problem 1, 9 for problem 2, and 12 for problem 13. However some searches were more expensive than others, with `astar_search_with_hg_pg_levelsum` (Duration) and `astar_search with h1` using the most time complexity, and `breadth_first_search` with space complexity (New Nodes, Expansions).

## Optimal Plan


| Problem 1                                                                                                       | Problem 2                                                                                                                                                              | Problem 3                                                                                                                                                                                                                      |
|-----------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Load(C1,P1, SFO), Load(C2, P2, JFK), Fly(P1, SFO, JFK), Fly(P2, JFK, SFO), Unload(C1, P1, JFK), Unload(C2, P2, SFO) | Load(C3,P3, ATL), Fly(P3, ATL, SFO), Unload(C3, P3, SFO), Load(C2, P2, JFK), Fly(P2, JFK, SFO), Unload(C2, P2, SFO), Load(C1, P1, SFO), Fly(P1, SFO, JFK), Unload(C1, P1, JFK) | Load(C1,P1, SFO), Fly(P1, SFO, ATL), Load(C3, P1, ATL), Fly(P1, ATL, JFK), Unload(C3, P1, JFK), Unload(C1, P1, JFK), Load(C2, P1, JFK), Fly(P1, JFK, ORD), Load(C4, P1, ORD), Fly(P1, ORD, SFO), Unload(C4,P1, SFO), Unload(C2, P1, SFO) |

These were the shortest search paths found by any kind of search, informed or otherwise. In testing, informed searches which leverage heuristics took longer to run, but `astar_search with h_ignore_preconditions` discovered an reasonable optimal path extraordinarily quickly, albeit expensively, finding reasonable solutions better than most uninformed strategies. However, the uninformed strategies like `breadth_first_search`, `uniform_cost_search` also discovered the optimal solution, also relatively expensively in both cases. 

### Uninformed Search Strategies

[![](images/UniformedStrategies.png)](https://public.tableau.com/views/planningAI/UniformedSearchStrategies?:embed=y&:display_count=yes)

These strategies are uninformed, and rely only on the immediate frontier to make decisions. 

* `breadth_first_search`: Reliable, sane, and optimal. Expensive; both in terms of time and space complexity. Durations well above the average, and far too many new nodes and goal state checks. It is comforing to know there at exists a structure that could attempt to find a solution to a crazy tree if given enough computational power. 
* `depth_first_graph_search`: This typically yields some of the most hilarious up airpline itenaries I've ever seen, with an "optimal plan" of only 875 actions. At least it finds it quickly in small networks; in large networks it just seems to chase nonsense for infinity. 
*  `uniform_cost_search`: A variant of BFS but with a path cost to approximate with. Unfortunately in this case, it performs much worse than all the other search strategies, wasting time and resources. However, it still made it to the optimal solution, so at least there's that. 
* `greedy_best_first_graph_search`: I really wish there was a way I could wrap my head around this; I'm just not getting it as well as the others. Do you guys have any suggestions? 

### Heuristic Search Strategies

[![](images/InformedStrategies.png)](https://public.tableau.com/views/planningAI/InformedSearchStrategies?:embed=y&:display_count=yes)

Compare and contrast heuristic search result metrics using A* with the and "level-sum" heuristics for Problems 1, 2, and 3.

`astar_search with h_pg_levelsum` used the fewest the resources implying reduced algorithmic complexity. I was very impressed with its performance; but as the most well defined problem, this is not atypical. That said, all of the informed searches outranked the uninformed searches, always found the best solution, often with an increased cost in space (`astar_search_with_h1`) or time (`astar_search_with_h_ignore_preconditions`). 

### Conclusion

| `h_1`        | `h_ignore_preconditions`           | `h_pg_levelsum`  |
| ------------- |-------------| -----|
| `# note that this is not a true heuristic` This heuristic is just a constant of 1 | This heuristic estimates the minimum number of actions that must be carried out from the current state in order to satisfy all of the goal conditions by ignoring the preconditions required for an action to be executed. |         This heuristic uses a planning graph representation of the problem state space to estimate the sum of all actions that must be carried out from the current state in order to satisfy each individual goal condition. |

[![](images/SummaryTable.png)](https://public.tableau.com/views/planningAI/SummaryTable?:embed=y&:display_count=yes)

#### `astar_search with h_pg_levelsum` 
Relatively more space effecient than any other search strategy, despite taking a little longer to run. With the entire structure of the planning graph, it is the most well defined problem. 

#### `astar_search_with_h1`
Wasn't really an informed search since `h1` is arbitrary, so it ended up just being a more expensive BFS, since we took one step further than we needed to every time.  

#### `astar_search_with_h_ignore_preconditions` 
Yielded some significant savings as well, and reached an optimal solution faster without the whole planning graph. Definitely the all-star in my book; a good tradeoff between implementational scale and effeciency. 

[![](images/SummaryTable_Highlight.png)](https://public.tableau.com/views/planningAI/SummaryTable?:embed=y&:display_count=yes)


