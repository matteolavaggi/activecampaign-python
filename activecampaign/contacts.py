class Contacts(object):
    def __init__(self, client):
        self.client = client

    def create_a_contact(self, data):
        """
        Create a new contact


        Args:
            data:

        Returns:

        """
        return self.client._post("/contacts", json=data)

    def create_or_update_contact(self, data):
        """
        Create a new contact or updates it


        Args:
            data:

        Returns:

        """
        return self.client._post("/contact/sync", json=data)

    def retrieve_a_contact(self, contact_id):
        """
        Retrieve an existing contact


        Args:
            contact_id:

        Returns:

        """
        return self.client._get("/contacts/{}".format(contact_id))

    def update_list_status_for_a_contact(self, data):
        """
        Subscribe a contact to a list or unsubscribe a contact from a list.


        Args:
            data:

        Returns:

        """
        return self.client._post("/contactLists", json=data)

    def update_a_contact(self, contact_id, data):
        """
        Update an existing contact


        Args:
            contact_id:
            data:

        Returns:

        """
        return self.client._put("/contacts/{}".format(contact_id), json=data)

    def delete_a_contact(self, contact_id):
        """
        Delete an existing contact


        Args:
            contact_id:

        Returns:

        """
        return self.client._delete("/contacts/{}".format(contact_id))

    def list_all_contacts(self, **params):
        """
        View many (or all) contacts by including their ID's or various filters.
        This is useful for searching for contacts that match certain criteria -
        such as being part of a certain list, or having a specific custom field value.


        Returns:

        """
        return self.client._get("/contacts", params=params)

    def list_all_automations_the_contacts_is_in(self, contact_id):
        """


        Returns:

        """
        return self.client._get("/contacts/{}/contactAutomations".format(contact_id))

    def retrieve_a_contacts_score_value(self, contact_id):
        """


        Returns:

        """
        return self.client._get("/contacts/{}/scoreValues".format(contact_id))

    def add_a_contact_to_an_automation(self, data):
        """


        Args:
            data:

        Returns:

        """
        return self.client._post("/contactAutomations", json=data)

    def retrieve_an_automation_a_contact_is_in(self, contact_automation_id):
        """


        Returns:

        """
        return self.client._get("/contactAutomations/{}".format(contact_automation_id))

    def remove_a_contact_from_an_automation(self, contact_automation_id):
        """


        Returns:

        """
        return self.client._delete(
            "/contactAutomations/{}".format(contact_automation_id)
        )

    def list_all_automations_a_contact_is_in(self):
        """


        Returns:

        """
        return self.client._get("/contactAutomations")

    def create_a_custom_field(self, data):
        """
        Create a new custom field


        Args:
            data:

        Returns:

        """
        response = self.client._post("/fields", json=data)

        # If field was created successfully, add it to default group
        if response and response.get("field", {}).get("id"):
            field_id = response["field"]["id"]
            group_response = self.add_custom_field_to_group(field_id)
            if not group_response:
                log.warning(f"Failed to add custom field {field_id} to group")

        return response

    def retrieve_a_custom_field(self, field_id):
        """
        Retrieve an existing custom field


        Args:
            field_id:

        Returns:

        """
        return self.client._get("/fields/{}".format(field_id))

    def update_a_custom_field(self, field_id, data):
        """
        Update an existing custom field


        Args:
            field_id:
            data:

        Returns:

        """
        return self.client._put("/fields/{}".format(field_id), json=data)

    def delete_a_custom_field(self, field_id):
        """
        Delete an existing custom field


        Args:
            field_id:

        Returns:

        """
        return self.client._delete("/fields/{}".format(field_id))

    def list_all_custom_fields(self, **params):
        """

        Returns:

        """
        return self.client._get("/fields", params=params)

    def create_a_custom_field_relationship_to_list(self, data):
        """

        Args:
            data:

        Returns:

        """
        return self.client._post("/fieldRels", json=data)

    def create_custom_field_options(self, data):
        """

        Args:
            data:

        Returns:

        """
        return self.client._post("/fieldOption/bulk", json=data)

    def create_a_custom_field_value(self, data):
        return self.client._post("/fieldValues", json=data)

    def retrieve_a_custom_field_value(self, field_value_id):
        return self.client._get("/fieldValues/{}".format(field_value_id))

    def update_a_custom_field_value_for_contact(self, data, field_value_id):
        return self.client._put("/fieldValues/{}".format(field_value_id), json=data)

    def delete_a_custom_field_value(self, field_value_id):
        return self.client._delete("/fieldValues/{}".format(field_value_id))

    def list_all_custom_field_values(self):
        return self.client._get("/fieldValues")

    def retrieve_a_contacts_field_values(self, contact_id):
        return self.client._get("/contacts/{}/fieldValues".format(contact_id))

    def retrieve_a_contacts_tracking_logs(self, contact_id):
        return self.client._get("/contacts/{}/trackingLogs".format(contact_id))

    def retrieve_a_contacts_data(self, contact_id):
        return self.client._get("/contacts/{}/contactData".format(contact_id))

    def retrieve_a_contacts_bounce_logs(self, contact_id):
        return self.client._get("/contacts/{}/bounceLogs".format(contact_id))

    def retrieve_a_contacts_geo_ips(self, contact_id):
        return self.client._get("/contacts/{}/geoIps".format(contact_id))

    def retrieve_a_contacts_organization(self, contact_id):
        return self.client._get("/contacts/{}/organization".format(contact_id))

    def retrieve_a_contacts_account_contacts(self, contact_id):
        return self.client._get("/contacts/{}/accountContacts".format(contact_id))

    def retrieve_a_contacts_automation_entry_counts(self, contact_id):
        return self.client._get("/contacts/{}/automationEntryCounts".format(contact_id))

    def add_a_tag_to_contact(self, data):
        """
        Add a tag to a contact

        :param data:
        :return:
        """
        return self.client._post("/contactTags", json=data)

    def remove_a_tag_from_a_contact(self, contact_tag_id):
        """
        Remove a tag from a contact

        :param contact_tag_id: The contact tag id
        :return:
        """
        return self.client._delete("/contactTags/{}".format(contact_tag_id))

    def retrieve_contact_tags(self, contact_id):
        """
        Retrieve all tags from a contact

        :param contact_id:
        :return:
        """
        return self.client._get("/contacts/{}/contactTags".format(contact_id))

    def retrieve_field_options(self, field_id):
        """


        Args:
            field_id:

        Returns:

        """
        return self.client._get("/fields/{}/options".format(field_id))

    def add_custom_field_to_group(
        self, field_id: str, group_id: int = 1, ordernum: int = None
    ) -> dict:
        """Add custom field to a field group.

        Args:
            field_id: The ID of the custom field
            group_id: The group ID (default 1 for contacts)
            ordernum: Order within group (optional)
        """
        data = {
            "groupMember": {
                "rel_id": field_id,
                "group_id": group_id,
                "ordernum": ordernum,
            }
        }
        return self.client._post("/groupMembers", json=data)

    def bulk_import_contacts(
        self,
        contacts,
        callback=None,
        exclude_automations=True,
        wait_for_completion=True,
        max_wait_time=300,
        debug_log=None,
    ):
        """Bulk import contacts into ActiveCampaign.

        This method has two phases:
        1. POST to /import/bulk_import to queue the contacts
        2. GET from /import/info?batchId=xxx to check status
        """
        import json
        import time

        def log_debug(msg, data=None):
            """Helper function for debug logging."""
            if debug_log:
                if data:
                    debug_log(f"{msg}\n{json.dumps(data, indent=2)}")
                else:
                    debug_log(msg)

        if not contacts:
            raise ValueError("Contacts list cannot be empty")

        if len(contacts) > 250:
            raise ValueError("Cannot import more than 250 contacts at once")

        if len(contacts) < 10:
            from warnings import warn

            warn(
                "It's recommended to import at least 10 contacts at once. "
                "For fewer contacts, use create_or_update_contact() instead."
            )

        # PHASE 1: Queue contacts for import
        log_debug("=== Phase 1: Queueing Contacts for Import ===")

        # Prepare request data
        data = {"contacts": contacts}
        if callback:
            data["callback"] = callback
        if exclude_automations:
            data["exclude_automations"] = True

        # Queue the import
        response = self.client._post("/import/bulk_import", json=data)
        log_debug("Bulk import queued:", response)

        if not wait_for_completion:
            return response

        # PHASE 2: Monitor import status
        log_debug("=== Phase 2: Monitoring Import Status ===")

        batch_id = response.get("batchId")
        if not batch_id:
            log_debug("Error: No batch ID in response:", response)
            raise ValueError("No batch ID returned from import request")

        log_debug(f"Starting status checks for batch: {batch_id}")
        log_debug(f"Total contacts to process: {len(contacts)}")

        # Add initial delay as recommended in the docs
        time.sleep(1)

        # Monitor progress
        start_time = time.time()
        check_count = 0
        last_progress = -1

        # Extract emails from contacts for later lookup
        contact_emails = []
        for contact in contacts:
            email = contact.get("email", "").lower()
            if email:
                contact_emails.append(email)
            else:
                contact_emails.append(None)  # Placeholder for contacts without email

        # Prepare result with contact IDs
        result = {
            "success": [],
            "failure": [],
            "batchId": batch_id,
            "contact_ids": {},  # Will store email -> id mapping
            "total_time": 0,
            "status": "",
        }

        while True:
            check_count += 1
            elapsed_time = time.time() - start_time

            if elapsed_time > max_wait_time:
                raise TimeoutError(
                    f"Import exceeded maximum wait time of {max_wait_time} seconds"
                )

            # Make status check request
            log_debug("----------------------------------------")
            log_debug(
                f"Status Check #{check_count} - Elapsed time: {elapsed_time:.1f}s"
            )

            status_url = f"/import/info?batchId={batch_id}"
            log_debug(f"Checking status at: {status_url}")

            # Get status and parse the JSON response
            raw_response = self.client._get(status_url)
            try:
                # If response is already a dict, use it as is
                if isinstance(raw_response, dict):
                    status_response = raw_response
                # If response is a string, try to parse it as JSON
                elif isinstance(raw_response, str):
                    status_response = json.loads(raw_response)
                else:
                    log_debug(f"Unexpected response type: {type(raw_response)}")
                    time.sleep(5)
                    continue

                log_debug("Status response:", status_response)
            except json.JSONDecodeError as e:
                log_debug(f"Failed to parse response as JSON: {e}")
                log_debug("Raw response:", raw_response)
                time.sleep(5)
                continue

            # Process status
            status = status_response.get("status", "").lower()
            success_list = status_response.get("success", [])
            failure_list = status_response.get("failure", [])
            success_count = len(success_list) if success_list else 0
            failure_count = len(failure_list) if failure_list else 0

            # Log progress changes
            if int((success_count + failure_count) / len(contacts) * 20) > int(
                last_progress
            ):
                last_progress = (success_count + failure_count) / len(contacts) * 20
                log_debug(
                    "Progress:",
                    {
                        "status": status,
                        "processed": f"{success_count + failure_count}/{len(contacts)}",
                        "success": success_count,
                        "failed": failure_count,
                    },
                )

            # Handle completion
            if status == "completed":
                log_debug(
                    "✓ Import completed",
                    {
                        "success": success_count,
                        "failed": failure_count,
                        "time": f"{elapsed_time:.1f}s",
                    },
                )

                # PHASE 3: Get contact IDs for successful imports
                log_debug("=== Phase 3: Getting Contact IDs ===")

                # We need to make individual API calls to get the contact IDs
                # This is more reliable than assuming the order of success_list matches contacts
                if success_count > 0:
                    log_debug(f"Looking up IDs for {success_count} successful contacts")

                    # Get the emails that were successfully imported
                    successful_emails = []
                    for i, email in enumerate(contact_emails):
                        if email and i < len(contacts) and i not in failure_list:
                            successful_emails.append(email)

                    # Look up each email individually to get its ID
                    for email in successful_emails:
                        try:
                            # Make API call to get contact by email
                            log_debug(f"Looking up contact ID for email: {email}")
                            log_debug(f"API call: GET /contacts?email={email}")

                            # Use the direct method to find contact by email
                            contact = self.find_contact_by_email(email)
                            log_debug(f"Contact found: {contact is not None}")

                            if contact:
                                contact_id = contact["id"]
                                log_debug(f"Contact details: {contact}")

                                # Verify this is the correct contact by checking the email
                                contact_email = contact.get("email", "").lower()
                                if contact_email != email.lower():
                                    log_debug(
                                        f"Email mismatch! Requested: {email}, Found: {contact_email}"
                                    )
                                else:
                                    result["contact_ids"][email] = contact_id
                                    log_debug(
                                        f"Found ID {contact_id} for email {email}"
                                    )
                            else:
                                log_debug(f"No contact found for email {email}")
                        except Exception as e:
                            log_debug(
                                f"Error looking up contact ID for {email}: {str(e)}"
                            )
                            log_debug(f"Exception details: {str(e)}")

                result["success"] = success_list
                result["failure"] = failure_list
                result["total_time"] = elapsed_time
                result["status"] = status
                return result

            elif status in ["failed", "interrupted"]:
                log_debug("✗ Import failed", status_response)
                result["success"] = success_list
                result["failure"] = failure_list
                result["total_time"] = elapsed_time
                result["status"] = status
                result["error"] = status_response.get("error")
                return result

            elif status in ["waiting", "claimed", "active"]:
                log_debug(f"Status: {status}")
                time.sleep(5)
                continue
            else:
                log_debug(f"Unknown status: {status}")
                time.sleep(5)
                continue

    def find_contact_by_email(self, email):
        """Find a contact by email address.

        This method makes a direct API call to search for a contact by email.

        Args:
            email (str): The email address to search for

        Returns:
            dict: The contact data if found, None otherwise
        """
        if not email:
            return None

        # Make a direct API call to search for the contact
        endpoint = f"/contacts?email={email}"
        response = self.client._get(endpoint)

        if response and response.get("contacts") and len(response["contacts"]) > 0:
            return response["contacts"][0]

        return None
