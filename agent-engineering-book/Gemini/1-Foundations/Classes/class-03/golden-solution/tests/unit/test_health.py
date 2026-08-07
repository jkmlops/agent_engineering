from widgetware_sdr.health import health_check


def test_health_check_reports_ok_status() -> None:
    result = health_check()
    assert result["status"] == "ok"


def test_health_check_reports_package_name() -> None:
    result = health_check()
    assert result["package"] == "widgetware_sdr"


def test_health_check_reports_a_version_string() -> None:
    result = health_check()
    assert isinstance(result["version"], str)
    assert result["version"] != ""
