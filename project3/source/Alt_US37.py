            # Each While loop collects a list of children that serve as the value for a dictionary.  The key for that value is the generation (child, grandchild, etc.)
            # A list of all related family ids is also appended each loop
            # Step 1:  At generation zero append children list and add family ids to family id list for every FAMS != NA
            # Step 2: At generation 1, add children from each of the families in the family id list, use cnt variable to increment through family id list with each while loop. 
            # When all generation 1 children are checked, increment generation.

            next_fam_id = fam_id
            fam_id_list = list()
            chil_id_list = defaultdict(list)
            cnt = 0
            generation = 0
            survivors = True
            while survivors:
                if families[next_fam_id]['CHIL'] != 'NA':
                    chil_id_list[generation].extend(families[next_fam_id]['CHIL'])
                    chil_list_len = len(chil_id_list[generation])
                    for i in range(chil_list_len):
                        chk_fam = chil_id_list[generation][i]
                        if individuals[chk_fam]['FAMS'] != 'NA':
                            fam_id_list.extend([individuals[chk_fam]['FAMS']])
                        if i == chil_list_len - 1:    
                            generation += 1
                    curr_tot_fam = len(fam_id_list)
                    if cnt < curr_tot_fam:
                        next_fam_id = fam_id_list[cnt]
                        cnt += 1
                    else:
                        survivors = False
                else:
                    curr_tot_fam = len(fam_id_list)
                    if cnt < curr_tot_fam:
                        next_fam_id = fam_id_list[cnt]
                        cnt += 1
                    else:
                        survivors = False

            
            for n in range(generation + 1):
                if n == 0:
                    relation = 'Child'
                elif n == 1:
                    relation = 'Grandchild'
                elif n>1:
                    relation = f"'{n}' x Great Grandchild"
                
                children = chil_id_list[n]
                num_chil = len(children)
                for y in range(num_chil):
                    recent_survivor = [children[y], individuals[children[y]]['NAME'], relation]
                    pt.add_row(recent_survivor)
            
            print(pt)

            return None