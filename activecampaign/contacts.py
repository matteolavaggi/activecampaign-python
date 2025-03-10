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
                print(f"Warning: Failed to add custom field {field_id} to group")

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
        db_tracker=None,
    ):
        """Bulk import contacts into ActiveCampaign.

        This method has two phases:
        1. POST to /import/bulk_import to queue the contacts
        2. GET from /import/info?batchId=xxx to check status

        If db_tracker is provided, it will also update contact IDs in the database
        after a successful import.
        """
        import json
        import time

        def log_debug(msg, data=None):
            """Helper function for debug logging."""
            if debug_log:
                if data:
                    if isinstance(data, dict) or isinstance(data, list):
                        # Use a separate debug logger for raw API responses
                        from src.logger import log_debug_item

                        try:
                            log_debug_item(f"{msg}\n{json.dumps(data, indent=2)}")
                        except:
                            # Fallback to regular debug log if log_debug_item is not available
                            debug_log(f"{msg}\n{json.dumps(data, indent=2)}")
                    else:
                        debug_log(f"{msg} {data}")
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

                # Return the results without looking up contact IDs
                result["success"] = success_list
                result["failure"] = failure_list
                result["total_time"] = elapsed_time
                result["status"] = status

                # PHASE 3: Update contact IDs in database if we have a database tracker
                if (
                    status == "completed"
                    and db_tracker
                    and hasattr(db_tracker, "execute")
                ):
                    log_debug("=== Phase 3: Updating Contact IDs in Database ===")

                    # Extract emails from successful contacts
                    successful_emails = []
                    email_map = {}  # Map to track email -> original case
                    for contact in contacts:
                        email = contact.get("email", "").lower()
                        if email and email not in failure_list:
                            successful_emails.append(email)
                            email_map[email.lower()] = contact.get("email", "")

                    if successful_emails:
                        log_debug(f"Updating IDs for {len(successful_emails)} contacts")

                        # Get list IDs from the contacts
                        list_ids = set()
                        for contact in contacts:
                            if contact.get("subscribe"):
                                if isinstance(contact["subscribe"], list):
                                    for list_item in contact["subscribe"]:
                                        if isinstance(
                                            list_item, dict
                                        ) and list_item.get("listid"):
                                            list_ids.add(list_item["listid"])
                                        elif isinstance(list_item, (str, int)):
                                            list_ids.add(str(list_item))
                                elif isinstance(contact["subscribe"], dict) and contact[
                                    "subscribe"
                                ].get("listid"):
                                    list_ids.add(contact["subscribe"]["listid"])
                                elif isinstance(contact["subscribe"], (str, int)):
                                    list_ids.add(str(contact["subscribe"]))

                        # If we couldn't extract list IDs from contacts, we can't update IDs
                        if not list_ids:
                            log_debug(
                                "No list IDs found in contacts, skipping ID update"
                            )
                        else:
                            log_debug(
                                f"Found {len(list_ids)} list IDs to query: {list_ids}"
                            )

                            # Create a dictionary to store contact IDs by email
                            contact_ids = {}

                            # Query each list for contacts
                            for list_id in list_ids:
                                log_debug(f"Querying contacts from list ID: {list_id}")

                                # Get all contacts from this list with pagination
                                list_contacts = self.get_contacts_by_list(
                                    list_id, limit=100, debug_log=debug_log
                                )
                                log_debug(
                                    f"Found {len(list_contacts)} contacts in list {list_id}"
                                )

                                # Process contacts from this list
                                for contact in list_contacts:
                                    if contact.get("email") and contact.get("id"):
                                        contact_email = contact["email"].lower()
                                        contact_ids[contact_email] = contact["id"]

                            log_debug(
                                f"Total unique contacts found across all lists: {len(contact_ids)}"
                            )

                            # Update database with contact IDs
                            updated_count = 0
                            not_found_count = 0
                            error_count = 0

                            for email in successful_emails:
                                email_lower = email.lower()
                                if email_lower in contact_ids:
                                    contact_id = contact_ids[email_lower]
                                    original_email = email_map.get(email_lower, email)

                                    try:
                                        db_tracker.execute(
                                            """
                                            UPDATE Contacts SET 
                                                ac_contact_id = ?
                                            WHERE Email = ?
                                            """,
                                            (contact_id, original_email),
                                        )
                                        updated_count += 1
                                        log_debug(
                                            f"Updated contact ID for {original_email}: {contact_id}"
                                        )
                                    except Exception as e:
                                        error_count += 1
                                        log_debug(
                                            f"Error updating contact ID for {original_email}: {str(e)}"
                                        )
                                else:
                                    not_found_count += 1

                            # Add stats to result
                            update_stats = {
                                "total": len(successful_emails),
                                "updated": updated_count,
                                "not_found": not_found_count,
                                "errors": error_count,
                            }
                            log_debug(f"Contact ID update stats: {update_stats}")
                            result["id_update_stats"] = update_stats

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

    def find_contact_by_email(self, email, debug_log=None):
        """Find a contact by email address.

        This method makes a direct API call to search for a contact by email.

        Args:
            email (str): The email address to search for
            debug_log (callable, optional): Function to log debug messages

        Returns:
            dict: The contact data if found, None otherwise
        """
        if not email:
            return None

        def log_debug(msg, data=None):
            if debug_log:
                if data:
                    import json

                    if isinstance(data, dict) or isinstance(data, list):
                        # Try to use debug logger for raw API responses
                        try:
                            from src.logger import log_debug_item

                            log_debug_item(f"{msg}\n{json.dumps(data, indent=2)}")
                        except:
                            # Fallback to regular debug log
                            debug_log(f"{msg}\n{json.dumps(data, indent=2)}")
                    else:
                        debug_log(f"{msg} {data}")
                else:
                    debug_log(msg)

        # Make a direct API call to search for the contact
        endpoint = f"/contacts?email={email}"
        log_debug(f"Searching for contact with email: {email}", f"GET {endpoint}")

        response = self.client._get(endpoint)

        # Log the raw response for debugging
        log_debug("Raw API response:", response)

        if response and response.get("contacts") and len(response["contacts"]) > 0:
            contact = response["contacts"][0]
            log_debug(f"Found contact with ID: {contact.get('id')}")
            return contact

        log_debug(f"No contact found with email: {email}")
        return None

    def get_contacts_by_list(
        self, list_id, limit=100, max_contacts=None, debug_log=None
    ):
        """Get all contacts from a specific list with pagination support.

        This method handles pagination automatically and returns all contacts
        from the specified list.

        Args:
            list_id (int): The ID of the list to get contacts from
            limit (int): Number of contacts to retrieve per page (max 100)
            max_contacts (int, optional): Maximum number of contacts to retrieve,
                                         None for all contacts
            debug_log (callable, optional): Function to log debug messages

        Returns:
            list: List of contact dictionaries
        """
        if not list_id:
            return []

        def log_debug(msg, data=None):
            if debug_log:
                if data:
                    import json

                    if isinstance(data, dict) or isinstance(data, list):
                        # Try to use debug logger for raw API responses
                        try:
                            from src.logger import log_debug_item

                            log_debug_item(f"{msg}\n{json.dumps(data, indent=2)}")
                        except:
                            # Fallback to regular debug log
                            debug_log(f"{msg}\n{json.dumps(data, indent=2)}")
                    else:
                        debug_log(f"{msg} {data}")
                else:
                    debug_log(msg)

        all_contacts = []
        offset = 0
        more_contacts = True
        page_count = 0

        log_debug(f"Starting to fetch contacts from list ID: {list_id}")

        while more_contacts:
            page_count += 1
            # Use id_greater parameter for better performance as recommended in the docs
            params = {"listid": list_id, "limit": limit, "orders[id]": "ASC"}

            # If we have contacts already, use id_greater for better performance
            if all_contacts and all_contacts[-1].get("id"):
                params["id_greater"] = all_contacts[-1]["id"]
                log_debug(f"Page {page_count}: Using id_greater={params['id_greater']}")
            else:
                params["offset"] = offset
                log_debug(f"Page {page_count}: Using offset={offset}")

            log_debug(f"Fetching contacts with params:", params)
            response = self.client._get("/contacts", params=params)

            if not response:
                log_debug("No response received from API")
                more_contacts = False
                continue

            log_debug(f"Raw API response for page {page_count}:", response)

            if not response.get("contacts"):
                log_debug("No contacts found in response")
                more_contacts = False
                continue

            contacts_page = response["contacts"]
            if not contacts_page:
                log_debug("Empty contacts list in response")
                more_contacts = False
                continue

            log_debug(f"Found {len(contacts_page)} contacts on page {page_count}")
            all_contacts.extend(contacts_page)

            # Check if we've reached the maximum number of contacts
            if max_contacts and len(all_contacts) >= max_contacts:
                log_debug(f"Reached maximum contacts limit: {max_contacts}")
                all_contacts = all_contacts[:max_contacts]
                more_contacts = False

            # Update offset for next page
            offset += limit

            # Check if we've reached the end of the contacts
            if len(contacts_page) < limit:
                log_debug(
                    f"Received fewer contacts ({len(contacts_page)}) than limit ({limit}), ending pagination"
                )
                more_contacts = False

        log_debug(f"Total contacts fetched from list {list_id}: {len(all_contacts)}")
        return all_contacts

    def update_contact_ids_in_database(
        self, emails_to_update, db_tracker, debug_log=None
    ):
        """Update contact IDs in the database for a list of emails.

        This method takes a list of emails, looks up their contact IDs in ActiveCampaign,
        and updates the database with the IDs.

        Args:
            emails_to_update (list): List of email addresses to update
            db_tracker: Database tracker object with execute method
            debug_log (callable, optional): Function to log debug messages

        Returns:
            dict: Statistics about the update process
        """
        if not emails_to_update or not db_tracker:
            return {"total": 0, "updated": 0, "not_found": 0, "errors": 0}

        def log_debug(msg, data=None):
            if debug_log:
                if data:
                    import json

                    if isinstance(data, dict) or isinstance(data, list):
                        # Try to use debug logger for raw API responses
                        try:
                            from src.logger import log_debug_item

                            log_debug_item(f"{msg}\n{json.dumps(data, indent=2)}")
                        except:
                            # Fallback to regular debug log
                            debug_log(f"{msg}\n{json.dumps(data, indent=2)}")
                    else:
                        debug_log(f"{msg} {data}")
                else:
                    debug_log(msg)

        stats = {
            "total": len(emails_to_update),
            "updated": 0,
            "not_found": 0,
            "errors": 0,
        }

        # Process emails in chunks to avoid too many API calls at once
        chunk_size = 100
        email_chunks = [
            emails_to_update[i : i + chunk_size]
            for i in range(0, len(emails_to_update), chunk_size)
        ]

        for chunk in email_chunks:
            # Create a mapping of lowercase emails for case-insensitive matching
            email_map = {email.lower(): email for email in chunk if email}

            if not email_map:
                continue

            log_debug(f"Processing chunk of {len(email_map)} emails")

            # Process each email individually for more reliable results
            for email in email_map.values():
                try:
                    log_debug(f"Looking up contact ID for email: {email}")

                    # Use the find_contact_by_email method which is more reliable
                    contact = self.find_contact_by_email(email, debug_log=debug_log)

                    if contact and contact.get("id"):
                        contact_id = contact["id"]
                        log_debug(f"Found contact ID: {contact_id} for email: {email}")

                        try:
                            db_tracker.execute(
                                """
                                UPDATE Contacts SET 
                                    ac_contact_id = ?
                                WHERE Email = ?
                                """,
                                (contact_id, email),
                            )
                            stats["updated"] += 1
                            log_debug(f"Updated contact ID for {email}: {contact_id}")
                        except Exception as e:
                            stats["errors"] += 1
                            log_debug(
                                f"Error updating contact ID for {email}: {str(e)}"
                            )
                    else:
                        stats["not_found"] += 1
                        log_debug(f"No contact found for email: {email}")

                except Exception as e:
                    stats["errors"] += 1
                    log_debug(f"Error processing email {email}: {str(e)}")

        return stats
