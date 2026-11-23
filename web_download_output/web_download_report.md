# Autopsy Web Download Investigation

Generated (UTC): 2026-11-23T16:37:27.754836+00:00

MCP tool: `query_data_artifacts`; artefact type: `TSK_WEB_DOWNLOAD`

Verified records in response: 1; analysed: 1.

**Coverage:** One MCP query was made. Results may be paginated, capped or incomplete; this report does not establish that all case downloads were retrieved.

**Evidence handling:** Source MCP output saved separately; AI conclusions require examiner verification.

# Forensic Report: Autopsy TSK_WEB_DOWNLOAD Artefacts Analysis

## Scope
This report analyzes a single JSON row extracted from the `TSK_WEB_DOWNLOAD` artefact collection within an Autopsy investigation. The data pertains to a file download event attributed to Microsoft Edge on a system with the user profile path `C:\Users\ncidi`. No additional context regarding network connectivity, authentication status, or post-download behavior is available in this dataset.

## Observations
*   **Artifact ID**: 312250
*   **Row Number**: 1
*   **Target URL**: `https://www.nirsoft.net/toolsdownload/webbrowserpassview.zip`
*   **Domain**: nirsoft.net
*   **Destination Path**: `C:\Users\ncidi\Downloads\webbrowserpassview.zip`
*   **Associated Application**: Microsoft Edge
*   **Timestamp**: 2023-10-21T17:27:20Z (Raw)
*   **Source File**: Not recorded in this artefact row.

## Download Activity
Based on the provided record, thertrieval from `nirsoft.net`. The system indicated an association with Microsoft Edge at the time of logging. The file was intended to be saved to the local Downloads folder une is one logged download event where a file named `webbrowserpassview.zip` was targeted for reder user `ncidi`.

**Important Note**: The presence of this artefact confirms a download request or initiation event recorded by the browser's history mechanism. It does not independently verify that the transfer completed successfully, nor does it confirm the user's intent to install or execute the software contained within the archive.

## Limitations
*   **Incomplete Provenance**: The `source_file` field is null for this row; therefore, no information exists regarding the original file from which the download was initiated (e.g., a bookmarked URL vs. a search result).
*   **Transfer Status Unknown**: As per standard digital forensics principles, a log entry in `TSK_WEB_DOWNLOAD` does not prove successful completion of the HTTP/HTTPS transfer or the integrity of the downloaded file upon arrival on the disk.
*   **User Intent Unverified**: The association with "Microsoft Edge" indicates the browser used for the session but does not confirm user interaction (e.g., clicking a link) versus automated script activity
