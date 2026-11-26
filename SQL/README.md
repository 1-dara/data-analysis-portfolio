# Project 2: Superstore SQL Business Q&A

**Tools:** PostgreSQL 16, VS Code, 9,994-row Superstore dataset
**Goal:** Answer 8 business questions using SQL (GROUP BY, JOIN, CTE, CASE).

## Key Findings

1. **West leads on both sales ($725,458) and profit ($108,418).** East is second.
2. **Central has the worst profit margin (7.92%)** — roughly half of West's 14.94% — despite outselling South.
3. **Furniture is the weakest category ($18,451 profit)** vs Technology's $145,455.
4. **Three sub-categories lose money:** Tables (-$17,725), Bookcases (-$3,473), Supplies (-$1,189).
5. **Furniture carries the highest average discount (17.4%)** and the lowest profit — a likely causal link.
6. **First Class shipping has the highest average profit per order ($31.84)**, though the gap across ship modes is small.
7. **California and New York dominate state-level profit** ($76,381 and $74,039).
8. **Discounts above 40% are loss-making:** 1,139 orders average **-$107.65** profit, versus +$66.90 with no discount.

## Recommendation

Cap discounts below 40% and review pricing on Tables and Bookcases, which together erase ~$21,000 of profit. Investigate why Central converts sales into profit so poorly.