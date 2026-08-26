"""WidgetWare SDR Context Builder Module.

Assembles deterministically the five context layers required for WidgetWare SDR analysis.
"""

from copy import deepcopy
from pathlib import Path
from typing import Any
import yaml

from widgetware_sdr.instructions import get_system_instructions


def load_yaml_config(file_path: Path) -> dict[str, Any]:
    """Load a YAML configuration file.

    Args:
        file_path (Path): Path to the YAML file.

    Returns:
        dict: Parsed YAML dictionary.

    Raises:
        FileNotFoundError: If the configuration file does not exist.
        ValueError: If the file is invalid YAML or empty.
    """
    if not file_path.is_file():
        raise FileNotFoundError(f"Required configuration file not found: {file_path}")

    with open(file_path, "r", encoding="utf-8") as f:
        content = yaml.safe_load(f)

    if content is None:
        raise ValueError(f"Configuration file is empty: {file_path}")

    return content


def build_context(
    account: dict[str, Any],
    objective: str,
    evidence: list[dict[str, Any]],
    state: dict[str, Any] | None = None,
    config_dir: str | Path | None = None,
) -> dict[str, Any]:
    """Assemble the five-layer context package for the WidgetWare SDR task.

    Args:
        account (dict): Target account details (task context).
        objective (str): Research or qualification objective.
        evidence (list[dict]): Retrieved evidence items with provenance.
        state (dict | None): Optional workflow state. Defaults to empty dict.
        config_dir (str | Path | None): Directory containing configuration YAMLs.

    Returns:
        dict: A dictionary containing the 5 isolated context layers:
            - system_instructions (str)
            - business_context (dict)
            - task_context (dict)
            - retrieved_evidence (list)
            - state (dict)
    """
    if config_dir is None:
        base_dir = Path(__file__).resolve().parents[2]
        config_dir = base_dir / "config"
    else:
        config_dir = Path(config_dir)

    products_file = config_dir / "products.yaml"
    icp_file = config_dir / "icp.yaml"
    policies_file = config_dir / "policies.yaml"

    products_data = load_yaml_config(products_file)
    icp_data = load_yaml_config(icp_file)
    policies_data = load_yaml_config(policies_file)

    system_instructions = get_system_instructions()

    business_context = {
        "products": products_data,
        "icp": icp_data,
        "policies": policies_data,
    }

    task_context = {
        "account": deepcopy(account),
        "objective": objective,
    }

    retrieved_evidence = deepcopy(evidence)
    workflow_state = deepcopy(state) if state is not None else {}

    return {
        "system_instructions": system_instructions,
        "business_context": business_context,
        "task_context": task_context,
        "retrieved_evidence": retrieved_evidence,
        "state": workflow_state,
    }
