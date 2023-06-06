import concurrent.futures
import os
from multiprocessing import freeze_support
from typing import List, Optional, Union

import clarite
import pandas as pd

# ----  START: ExE Pairwise

def exe_pairwise(
    data: pd.DataFrame,
    outcomes: Union[str, List[str]],
    covariates: Optional[Union[str, List[str]]] = None,
    report_betas: bool = False,
    min_n: int = 200,
    process_num: Optional[int] = None,
):

    # define variables
    results: List[str] = []
    combinations = []
    # processed_combinations: set[str] = set()

    # Define the number of worker processes
    if process_num is None:
        # Set according to the number of available cores
        num_workers = os.cpu_count()
    else:
        num_workers = process_num

    # Create a set of exposomes
    exposomes_set = set(data.columns) - set(outcomes) - set(covariates or [])
    # Convert the exposomes set to a list
    exposomes = list(exposomes_set)

    if len(exposomes) < 2:
        raise ValueError(
            f"{len(exposomes)} exposomes not enought to run pairwise." # noqa E501
            )

    # Create a list of combinations
    for i in range(len(exposomes)):
        # reference_exposome = exposomes[i]
        for j in range(i+1, len(exposomes)):
            # paired_exposome = exposomes[j]
            # if (reference_exposome, paired_exposome) not in processed_combinations:  # noqa E501
            # combinations.append((reference_exposome, paired_exposome))
            combinations.append((exposomes[i], exposomes[j]))

    # Run Interaction Study
    # def _perform_regression(interactions):
    #     # Implement your regression analysis here
    #     # Return the regression results
    #     df_result = clarite.analyze.interaction_study(
    #         data,
    #         outcomes,
    #         interactions,
    #         covariates,
    #         report_betas,
    #         min_n,
    #         process_num,
    #     )
    #     return df_result

    # def _save_results(results_list, result):
    #     results_list.append(result)

    def _process_combination(interactions):
        # reference_exposome, paired_exposome = combination
        # regression_results = _perform_regression(interactions=combination)
        # regression_results = clarite.analyze.interaction_study(
        #     data,
        #     outcomes,
        #     interactions,
        #     covariates,
        #     report_betas,
        #     min_n,
        #     process_num,
        # )
        # _save_results(regression_results)
        # results.append(regression_results)
        print("dentro")
        # processed_combinations.add((reference_exposome, paired_exposome))


    # Create a ProcessPoolExecutor with the specified number of workers
    with concurrent.futures.ProcessPoolExecutor(max_workers=num_workers) as executor:  # noqa E501
        # Submit the tasks for execution
        futures = [
            executor.submit(
                _process_combination, combination
                ) for combination in combinations
            ]

        # Wait for all tasks to complete
        concurrent.futures.wait(futures)
        # Create a Pool of worker processes


    # Convert the results list to a DataFrame
    # df = pd.DataFrame(results)
    return pd.DataFrame(results)


