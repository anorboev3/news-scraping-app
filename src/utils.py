def add_url(url, url_list):
    if url:
        url_list.append(url)
    return url_list, ""


def clear_url_list(url_list):
    url_list.clear()
    return url_list


def format_results(results):
    output = ""
    for result in results:
        output += f"**Headline:** {result['headline']}\n"
        output += f"**Summary:** {result['summary']}\n"
        output += f"**URL:** {result['url']}\n"
        output += "\n"
    return output.strip()